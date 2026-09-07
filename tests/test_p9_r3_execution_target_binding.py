from __future__ import annotations

import multiprocessing
import shutil
import sqlite3
import unittest
from pathlib import Path

from agency_kernel.effect_seams import G3EffectAdapter, G4EffectAdapter
from agency_kernel.g3 import Kernel as G3Kernel, Observer as G3Observer
from agency_kernel.g4 import GitObserver, Kernel as G4Kernel
from agency_kernel.http_cas import HttpCasEffectAdapter, Kernel as HttpCasKernel
from agency_kernel.http_cas_provider import HttpCasObserver, serve_http_cas_provider
from tests.test_effect_domain_conformance import G3Domain, G4Domain
from tests.test_http_cas import HttpCasDomain


class ExecutionTargetBindingRepairTests(unittest.TestCase):
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

    def test_gate_a_g3_t1_admission_rejects_t2_execution_and_does_not_consume(self) -> None:
        domain = G3Domain()
        self.addCleanup(domain.close)
        operation = domain.operation("p9-r3-g3-a")
        adapter_t1 = G3EffectAdapter(domain.kernel, domain.observer)
        admitted = adapter_t1.admit(domain.attempt, domain.capability_id, operation)
        self.assertTrue(admitted.allowed, admitted.reason)
        admission_id = admitted.admission.admission_id

        t2 = Path(domain.tempdir.name) / "g3-execution-t2.db"
        self._sqlite_clone(Path(domain.target_db), t2)
        wrong_kernel = G3Kernel(domain.control_db, t2, clock=lambda: 100)
        wrong_adapter = G3EffectAdapter(wrong_kernel, G3Observer(t2))

        rejected = wrong_adapter.execute(admission_id)
        self.assertEqual((rejected.occurred, rejected.reason), (False, "target_instance_mismatch"))
        self.assertIsNone(G3Observer(t2).observe(operation.resource).admission_id)

        correct = adapter_t1.execute(admission_id)
        self.assertTrue(correct.occurred, correct.reason)
        replay = adapter_t1.execute(admission_id)
        self.assertEqual((replay.occurred, replay.reason), (False, "admission_consumed"))

    def test_gate_b_g3_same_t1_reconstructed_adapter_executes(self) -> None:
        domain = G3Domain()
        self.addCleanup(domain.close)
        operation = domain.operation("p9-r3-g3-b")
        admitted = G3EffectAdapter(domain.kernel, domain.observer).admit(domain.attempt, domain.capability_id, operation)
        self.assertTrue(admitted.allowed, admitted.reason)
        admission_id = admitted.admission.admission_id

        restarted_kernel = G3Kernel(domain.control_db, domain.target_db, clock=lambda: 100)
        restarted = G3EffectAdapter(restarted_kernel, G3Observer(domain.target_db))
        result = restarted.execute(admission_id)
        self.assertTrue(result.occurred, result.reason)

    def test_gate_a_g4_t1_admission_rejects_t2_execution_and_does_not_consume(self) -> None:
        domain = G4Domain()
        self.addCleanup(domain.close)
        operation = domain.operation("p9-r3-g4-a")
        adapter_t1 = G4EffectAdapter(domain.kernel, domain.observer)
        admitted = adapter_t1.admit(domain.attempt, domain.capability_id, operation)
        self.assertTrue(admitted.allowed, admitted.reason)
        admission_id = admitted.admission.admission_id

        t2 = Path(domain.tempdir.name) / "g4-execution-t2.git"
        shutil.copytree(domain.repo_path, t2)
        wrong_kernel = G4Kernel(domain.control_db, t2, clock=lambda: 100)
        wrong_adapter = G4EffectAdapter(wrong_kernel, GitObserver(wrong_kernel.git_repo))

        rejected = wrong_adapter.execute(admission_id)
        self.assertEqual((rejected.occurred, rejected.reason), (False, "target_instance_mismatch"))

        correct = adapter_t1.execute(admission_id)
        self.assertTrue(correct.occurred, correct.reason)
        replay = adapter_t1.execute(admission_id)
        self.assertEqual((replay.occurred, replay.reason), (False, "admission_consumed"))

    def test_gate_b_g4_same_t1_reconstructed_adapter_executes(self) -> None:
        domain = G4Domain()
        self.addCleanup(domain.close)
        operation = domain.operation("p9-r3-g4-b")
        admitted = G4EffectAdapter(domain.kernel, domain.observer).admit(domain.attempt, domain.capability_id, operation)
        self.assertTrue(admitted.allowed, admitted.reason)
        admission_id = admitted.admission.admission_id

        restarted_kernel = G4Kernel(domain.control_db, domain.repo_path, clock=lambda: 100)
        restarted = G4EffectAdapter(restarted_kernel, GitObserver(restarted_kernel.git_repo))
        result = restarted.execute(admission_id)
        self.assertTrue(result.occurred, result.reason)

    def test_gate_a_http_t1_admission_rejects_t2_execution_and_does_not_consume(self) -> None:
        domain = HttpCasDomain()
        self.addCleanup(domain.close)
        operation = domain.operation("p9-r3-http-a")
        admitted = domain.adapter.admit(domain.attempt, domain.capability_id, operation)
        self.assertTrue(admitted.allowed, admitted.reason)
        admission_id = admitted.admission.admission_id

        t2 = Path(domain.tempdir.name) / "http-execution-t2.db"
        self._sqlite_clone(domain.provider_db, t2)
        _process, endpoint = self._start_provider(t2, domain.provider_token, "provider-local")
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

        rejected = wrong_adapter.execute(admission_id)
        self.assertEqual((rejected.occurred, rejected.reason), (False, "target_instance_mismatch"))
        self.assertIsNone(wrong_observer.observe(operation.resource).admission_id)

        correct = domain.adapter.execute(admission_id)
        self.assertTrue(correct.occurred, correct.reason)
        replay = domain.adapter.execute(admission_id)
        self.assertEqual((replay.occurred, replay.reason), (False, "admission_consumed"))

    def test_gate_b_http_same_t1_provider_restart_executes(self) -> None:
        domain = HttpCasDomain()
        self.addCleanup(domain.close)
        operation = domain.operation("p9-r3-http-b")
        admitted = domain.adapter.admit(domain.attempt, domain.capability_id, operation)
        self.assertTrue(admitted.allowed, admitted.reason)
        admission_id = admitted.admission.admission_id

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
        restarted = HttpCasEffectAdapter(restarted_kernel, restarted_observer)
        result = restarted.execute(admission_id)
        self.assertTrue(result.occurred, result.reason)


if __name__ == "__main__":
    unittest.main()
