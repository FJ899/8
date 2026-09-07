from __future__ import annotations

import multiprocessing
import shutil
import sqlite3
import unittest
from pathlib import Path

from agency_kernel.effect_seams import G3EffectAdapter, G4EffectAdapter
from agency_kernel.g3 import Observer as G3Observer
from agency_kernel.g4 import GitObserver, Kernel as G4Kernel
from agency_kernel.http_cas import Kernel as HttpCasKernel
from agency_kernel.http_cas_provider import HttpCasObserver, serve_http_cas_provider
from tests.test_effect_domain_conformance import G3Domain, G4Domain
from tests.test_http_cas import HttpCasDomain


class SwapAfterValidationG3Adapter(G3EffectAdapter):
    __slots__ = ("_swap_target",)

    def __init__(self, kernel, observer, swap_target: Path) -> None:
        super().__init__(kernel, observer)
        self._swap_target = swap_target

    def _execution_target_binding(self, logical_target: str):
        binding = super()._execution_target_binding(logical_target)
        self._kernel.target_db = str(self._swap_target)
        self._observer = G3Observer(self._swap_target)
        return binding


class SwapAfterValidationG4Adapter(G4EffectAdapter):
    __slots__ = ("_swap_repo",)

    def __init__(self, kernel, observer, swap_repo) -> None:
        super().__init__(kernel, observer)
        self._swap_repo = swap_repo

    def _execution_target_binding(self, logical_target: str):
        binding = super()._execution_target_binding(logical_target)
        self._kernel.git_repo = self._swap_repo
        self._observer = GitObserver(self._swap_repo)
        return binding


class BoundEffectRouteRepairTests(unittest.TestCase):
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

    def test_g3_checked_t1_route_remains_effect_route_after_composition_switch(self) -> None:
        domain = G3Domain()
        self.addCleanup(domain.close)
        operation = domain.operation("p9-r4-g3")
        t1 = Path(domain.target_db)
        t2 = Path(domain.tempdir.name) / "p9-r4-g3-t2.db"
        self._sqlite_clone(t1, t2)

        adapter = SwapAfterValidationG3Adapter(domain.kernel, domain.observer, t2)
        admitted = adapter.admit(domain.attempt, domain.capability_id, operation)
        self.assertTrue(admitted.allowed, admitted.reason)
        admission_id = admitted.admission.admission_id

        result = adapter.execute(admission_id)
        self.assertTrue(result.occurred, result.reason)
        self.assertEqual(G3Observer(t1).observe(operation.resource).admission_id, admission_id)
        self.assertNotEqual(G3Observer(t2).observe(operation.resource).admission_id, admission_id)

    def test_g4_checked_t1_route_remains_effect_route_after_composition_switch(self) -> None:
        domain = G4Domain()
        self.addCleanup(domain.close)
        operation = domain.operation("p9-r4-g4")
        t2_path = Path(domain.tempdir.name) / "p9-r4-g4-t2.git"
        shutil.copytree(domain.repo_path, t2_path)
        wrong_kernel = G4Kernel(domain.control_db, t2_path, clock=lambda: 100)
        t2_before = wrong_kernel.git_repo.rev_parse_ref()

        adapter = SwapAfterValidationG4Adapter(domain.kernel, domain.observer, wrong_kernel.git_repo)
        admitted = adapter.admit(domain.attempt, domain.capability_id, operation)
        self.assertTrue(admitted.allowed, admitted.reason)
        admission_id = admitted.admission.admission_id

        result = adapter.execute(admission_id)
        self.assertTrue(result.occurred, result.reason)
        self.assertEqual(domain.observer.observe().admission_id, admission_id)
        self.assertEqual(wrong_kernel.git_repo.rev_parse_ref(), t2_before)

    def test_http_provider_rejects_correct_credentials_on_wrong_concrete_store_instance(self) -> None:
        domain = HttpCasDomain()
        self.addCleanup(domain.close)
        operation = domain.operation("p9-r4-http")
        historical = domain.adapter.historical_target_binding(operation)
        admitted = domain.adapter.admit(domain.attempt, domain.capability_id, operation)
        self.assertTrue(admitted.allowed, admitted.reason)
        admission_id = admitted.admission.admission_id

        t2 = Path(domain.tempdir.name) / "p9-r4-http-t2.db"
        self._sqlite_clone(domain.provider_db, t2)
        _process, endpoint = self._start_provider(t2, domain.provider_token, "provider-local")
        wrong_observer = HttpCasObserver(endpoint, domain.provider_token, "provider-local", timeout=0.15)
        self.assertNotEqual(
            wrong_observer.historical_target_binding(operation.resource).instance_id,
            historical.instance_id,
        )

        wrong_kernel = HttpCasKernel(
            domain.control_db,
            endpoint,
            domain.provider_token,
            "provider-local",
            clock=lambda: 100,
            timeout=0.10,
        )
        result = wrong_kernel.execute_http_cas_admission(
            admission_id,
            expected_target_instance_id=historical.instance_id,
        )
        self.assertEqual((result.occurred, result.reason), (False, "target_instance_mismatch"))
        self.assertIsNone(wrong_observer.observe(operation.resource).admission_id)

    def test_http_legacy_raw_execution_without_expected_instance_remains_compatible(self) -> None:
        domain = HttpCasDomain()
        self.addCleanup(domain.close)
        operation = domain.operation("p9-r4-http-legacy")
        admitted = domain.kernel.admit_http_cas(domain.attempt, domain.capability_id, operation)
        self.assertTrue(admitted.allowed, admitted.reason)
        result = domain.kernel.execute_http_cas_admission(admitted.admission.admission_id)
        self.assertTrue(result.occurred, result.reason)


if __name__ == "__main__":
    unittest.main()
