from __future__ import annotations

import multiprocessing
import shutil
import sqlite3
import tempfile
import unittest
from pathlib import Path

from agency_kernel.bindings import CapabilityBinding, TrustedBindingRegistry
from agency_kernel.effect_seams import G3EffectAdapter, G4EffectAdapter
from agency_kernel.evidence import (
    EffectEvidenceCollector,
    G3EvidenceProducer,
    G4EvidenceProducer,
    HttpCasEvidenceProducer,
)
from agency_kernel.g1 import ActionRequest
from agency_kernel.g3 import Kernel as G3Kernel, Observer as G3Observer
from agency_kernel.g4 import GitObserver, Kernel as G4Kernel
from agency_kernel.http_cas import HttpCasEffectAdapter, Kernel as HttpCasKernel
from agency_kernel.http_cas_provider import HttpCasObserver, serve_http_cas_provider
from agency_kernel.reconciliation import ReconciliationStatus
from agency_kernel.runtime import KernelRuntime
from tests.test_effect_domain_conformance import G3Domain, G4Domain
from tests.test_http_cas import HttpCasDomain


class TargetInstanceProvenanceRepairTests(unittest.TestCase):
    def _run(self, domain, adapter, operation, request_id: str):
        binding = CapabilityBinding(
            f"binding-{request_id}",
            domain.intent.intent_id,
            domain.capability_id,
            adapter.target_identity(operation),
            adapter,
        )
        runtime = KernelRuntime(domain.kernel, TrustedBindingRegistry((binding,)))
        trace = runtime.run(
            ActionRequest(request_id, domain.intent.intent_id, domain.contract.contract_id),
            operation,
            authentication_context=domain.context,
        )
        self.assertTrue(trace.authorization.allowed, trace.authorization.reason)
        self.assertIsNotNone(trace.start)
        self.assertTrue(trace.start.allowed, trace.start.reason)
        self.assertIsNotNone(trace.admission)
        self.assertTrue(trace.admission.allowed, trace.admission.reason)
        self.assertIsNotNone(trace.execution)
        self.assertTrue(trace.execution.occurred, trace.execution.reason)
        return trace

    @staticmethod
    def _sqlite_clone(source: Path, destination: Path) -> None:
        with sqlite3.connect(str(source)) as src, sqlite3.connect(str(destination)) as dst:
            src.backup(dst)

    def _start_provider(self, db_path: Path, token: str, provider_id: str):
        parent, child = multiprocessing.Pipe(duplex=False)
        process = multiprocessing.Process(
            target=serve_http_cas_provider,
            args=(db_path, token, provider_id, child),
            kwargs={"allow_test_faults": True},
            daemon=True,
        )
        process.start()
        child.close()
        if not parent.poll(5.0):
            process.terminate()
            process.join(2.0)
            self.fail("provider_start_timeout")
        port = parent.recv()
        parent.close()
        self.addCleanup(lambda: process.is_alive() and process.terminate())
        self.addCleanup(lambda: process.join(2.0))
        return process, f"http://127.0.0.1:{port}"

    def test_gate_a_g3_wrong_store_copy_cannot_rehydrate_historical_occurred(self) -> None:
        domain = G3Domain()
        self.addCleanup(domain.close)
        adapter = G3EffectAdapter(domain.kernel, domain.observer)
        operation = domain.operation("historical-g3")
        trace = self._run(domain, adapter, operation, "p9-r2-g3")
        admission_id = trace.admission.admission.admission_id

        clone = Path(domain.tempdir.name) / "wrong-target.db"
        self._sqlite_clone(domain.target_db, clone)
        wrong_kernel = G3Kernel(domain.control_db, clone, clock=lambda: 100)
        wrong_observer = G3Observer(clone)
        wrong_adapter = G3EffectAdapter(wrong_kernel, wrong_observer)
        collector = EffectEvidenceCollector(G3EvidenceProducer(wrong_adapter))

        with self.assertRaisesRegex(ValueError, "target_instance_mismatch"):
            collector.collect_from_admission_id(admission_id, operation)

    def test_gate_b_g3_same_store_restart_still_rehydrates_occurred(self) -> None:
        domain = G3Domain()
        self.addCleanup(domain.close)
        adapter = G3EffectAdapter(domain.kernel, domain.observer)
        operation = domain.operation("same-g3")
        trace = self._run(domain, adapter, operation, "p9-r2-g3-same")
        admission_id = trace.admission.admission.admission_id

        restarted_kernel = G3Kernel(domain.control_db, domain.target_db, clock=lambda: 100)
        restarted_adapter = G3EffectAdapter(restarted_kernel, G3Observer(domain.target_db))
        collector = EffectEvidenceCollector(G3EvidenceProducer(restarted_adapter))
        evidence = collector.collect_from_admission_id(admission_id, operation)
        self.assertEqual(evidence.reconciliation.status, ReconciliationStatus.OCCURRED)
        replay = restarted_adapter.execute(admission_id)
        self.assertEqual((replay.occurred, replay.reason), (False, "admission_consumed"))

    def test_gate_a_g4_wrong_repository_copy_cannot_rehydrate_historical_occurred(self) -> None:
        domain = G4Domain()
        self.addCleanup(domain.close)
        adapter = G4EffectAdapter(domain.kernel, domain.observer)
        operation = domain.operation("historical-g4")
        trace = self._run(domain, adapter, operation, "p9-r2-g4")
        admission_id = trace.admission.admission.admission_id

        clone = Path(domain.tempdir.name) / "wrong-target.git"
        shutil.copytree(domain.repo_path, clone)
        wrong_kernel = G4Kernel(domain.control_db, clone, clock=lambda: 100)
        wrong_adapter = G4EffectAdapter(wrong_kernel, GitObserver(wrong_kernel.git_repo))
        collector = EffectEvidenceCollector(G4EvidenceProducer(wrong_adapter))

        with self.assertRaisesRegex(ValueError, "target_instance_mismatch"):
            collector.collect_from_admission_id(admission_id, operation)

    def test_gate_b_g4_same_repository_restart_still_rehydrates_occurred(self) -> None:
        domain = G4Domain()
        self.addCleanup(domain.close)
        adapter = G4EffectAdapter(domain.kernel, domain.observer)
        operation = domain.operation("same-g4")
        trace = self._run(domain, adapter, operation, "p9-r2-g4-same")
        admission_id = trace.admission.admission.admission_id

        restarted_kernel = G4Kernel(domain.control_db, domain.repo_path, clock=lambda: 100)
        restarted_adapter = G4EffectAdapter(restarted_kernel, GitObserver(restarted_kernel.git_repo))
        collector = EffectEvidenceCollector(G4EvidenceProducer(restarted_adapter))
        evidence = collector.collect_from_admission_id(admission_id, operation)
        self.assertEqual(evidence.reconciliation.status, ReconciliationStatus.OCCURRED)
        replay = restarted_adapter.execute(admission_id)
        self.assertEqual((replay.occurred, replay.reason), (False, "admission_consumed"))

    def test_gate_a_http_wrong_provider_store_copy_cannot_rehydrate_historical_occurred(self) -> None:
        domain = HttpCasDomain()
        self.addCleanup(domain.close)
        operation = domain.operation("historical-http")
        trace = self._run(domain, domain.adapter, operation, "p9-r2-http")
        admission_id = trace.admission.admission.admission_id

        clone = Path(domain.tempdir.name) / "wrong-provider.db"
        self._sqlite_clone(domain.provider_db, clone)
        _process, endpoint = self._start_provider(clone, domain.provider_token, "provider-local")
        wrong_kernel = HttpCasKernel(
            domain.control_db,
            endpoint,
            domain.provider_token,
            "provider-local",
            clock=lambda: 100,
            timeout=0.10,
        )
        wrong_observer = HttpCasObserver(endpoint, domain.provider_token, "provider-local", timeout=0.15)
        wrong_adapter = HttpCasEffectAdapter(wrong_kernel, wrong_observer)
        collector = EffectEvidenceCollector(HttpCasEvidenceProducer(wrong_adapter))

        with self.assertRaisesRegex(ValueError, "target_instance_mismatch"):
            collector.collect_from_admission_id(admission_id, operation)

    def test_gate_b_http_same_provider_store_process_restart_still_rehydrates_occurred(self) -> None:
        domain = HttpCasDomain()
        self.addCleanup(domain.close)
        operation = domain.operation("same-http")
        trace = self._run(domain, domain.adapter, operation, "p9-r2-http-same")
        admission_id = trace.admission.admission.admission_id

        domain.process.terminate()
        domain.process.join(2.0)
        process, endpoint = self._start_provider(domain.provider_db, domain.provider_token, "provider-local")
        domain.process = process
        restarted_kernel = HttpCasKernel(
            domain.control_db,
            endpoint,
            domain.provider_token,
            "provider-local",
            clock=lambda: 100,
            timeout=0.10,
        )
        restarted_observer = HttpCasObserver(endpoint, domain.provider_token, "provider-local", timeout=0.15)
        restarted_adapter = HttpCasEffectAdapter(restarted_kernel, restarted_observer)
        collector = EffectEvidenceCollector(HttpCasEvidenceProducer(restarted_adapter))
        evidence = collector.collect_from_admission_id(admission_id, operation)
        self.assertEqual(evidence.reconciliation.status, ReconciliationStatus.OCCURRED)
        replay = restarted_adapter.execute(admission_id)
        self.assertEqual((replay.occurred, replay.reason), (False, "admission_consumed"))


if __name__ == "__main__":
    unittest.main()
