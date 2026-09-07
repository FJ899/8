from __future__ import annotations

import multiprocessing
import os
import shutil
import sqlite3
import threading
import time
import unittest
from pathlib import Path

from agency_kernel.effect_seams import G3EffectAdapter, G4EffectAdapter
from agency_kernel.g3 import Observer as G3Observer
from agency_kernel.g4 import GitObserver
from agency_kernel.http_cas import HttpCasEffectAdapter, Kernel as HttpCasKernel
from agency_kernel.http_cas_provider import HttpCasObserver, serve_http_cas_provider
from tests.test_effect_domain_conformance import G3Domain, G4Domain
from tests.test_http_cas import HttpCasDomain


class RebindPathAfterValidationG3Adapter(G3EffectAdapter):
    __slots__ = ("_route", "_replacement")

    def __init__(self, kernel, observer, route: Path, replacement: Path) -> None:
        super().__init__(kernel, observer)
        self._route = route
        self._replacement = replacement

    def _execution_target_binding(self, logical_target: str):
        binding = super()._execution_target_binding(logical_target)
        self._route.unlink()
        self._route.symlink_to(self._replacement)
        self._observer = G3Observer(self._route)
        return binding


class RebindPathAfterValidationG4Adapter(G4EffectAdapter):
    __slots__ = ("_route", "_replacement")

    def __init__(self, kernel, observer, route: Path, replacement: Path) -> None:
        super().__init__(kernel, observer)
        self._route = route
        self._replacement = replacement

    def _execution_target_binding(self, logical_target: str):
        binding = super()._execution_target_binding(logical_target)
        self._route.unlink()
        self._route.symlink_to(self._replacement, target_is_directory=True)
        return binding


class PinnedTargetObjectRepairTests(unittest.TestCase):
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

    def test_g3_rebound_path_object_is_rejected_without_consuming_admission(self) -> None:
        domain = G3Domain()
        self.addCleanup(domain.close)
        operation = domain.operation("p9-r5-g3")
        t1 = Path(domain.target_db).resolve()
        t2 = Path(domain.tempdir.name) / "p9-r5-g3-t2.db"
        self._sqlite_clone(t1, t2)
        route = Path(domain.tempdir.name) / "p9-r5-g3-route.db"
        route.symlink_to(t1)
        domain.kernel.target_db = str(route)

        attacker = RebindPathAfterValidationG3Adapter(
            domain.kernel,
            G3Observer(route),
            route,
            t2,
        )
        admitted = attacker.admit(domain.attempt, domain.capability_id, operation)
        self.assertTrue(admitted.allowed, admitted.reason)
        admission_id = admitted.admission.admission_id

        rejected = attacker.execute(admission_id)
        self.assertEqual((rejected.occurred, rejected.reason), (False, "target_instance_mismatch"))
        self.assertNotEqual(G3Observer(t2).observe(operation.resource).admission_id, admission_id)

        route.unlink()
        route.symlink_to(t1)
        correct = G3EffectAdapter(domain.kernel, G3Observer(route)).execute(admission_id)
        self.assertTrue(correct.occurred, correct.reason)
        self.assertEqual(G3Observer(t1).observe(operation.resource).admission_id, admission_id)
        replay = G3EffectAdapter(domain.kernel, G3Observer(route)).execute(admission_id)
        self.assertEqual((replay.occurred, replay.reason), (False, "admission_consumed"))

    def test_g4_rebound_path_object_is_rejected_without_consuming_admission(self) -> None:
        domain = G4Domain()
        self.addCleanup(domain.close)
        operation = domain.operation("p9-r5-g4")
        t1 = Path(domain.repo_path).resolve()
        t2 = Path(domain.tempdir.name) / "p9-r5-g4-t2.git"
        shutil.copytree(t1, t2)
        route = Path(domain.tempdir.name) / "p9-r5-g4-route.git"
        route.symlink_to(t1, target_is_directory=True)
        domain.kernel.git_repo.repo = route
        domain.observer = GitObserver(domain.kernel.git_repo)

        attacker = RebindPathAfterValidationG4Adapter(
            domain.kernel,
            domain.observer,
            route,
            t2,
        )
        admitted = attacker.admit(domain.attempt, domain.capability_id, operation)
        self.assertTrue(admitted.allowed, admitted.reason)
        admission_id = admitted.admission.admission_id

        rejected = attacker.execute(admission_id)
        self.assertEqual((rejected.occurred, rejected.reason), (False, "target_instance_mismatch"))

        route.unlink()
        route.symlink_to(t1, target_is_directory=True)
        correct = G4EffectAdapter(domain.kernel, GitObserver(domain.kernel.git_repo)).execute(admission_id)
        self.assertTrue(correct.occurred, correct.reason)
        self.assertEqual(GitObserver(domain.kernel.git_repo).observe().admission_id, admission_id)
        replay = G4EffectAdapter(domain.kernel, GitObserver(domain.kernel.git_repo)).execute(admission_id)
        self.assertEqual((replay.occurred, replay.reason), (False, "admission_consumed"))

    def test_http_provider_rebind_during_delay_is_caught_by_pinned_cas_object(self) -> None:
        domain = HttpCasDomain()
        self.addCleanup(domain.close)
        domain.process.terminate()
        domain.process.join(2.0)

        t1 = Path(domain.provider_db).resolve()
        t2 = Path(domain.tempdir.name) / "p9-r5-http-t2.db"
        self._sqlite_clone(t1, t2)
        route = Path(domain.tempdir.name) / "p9-r5-http-route.db"
        route.symlink_to(t1)

        process, endpoint = self._start_provider(route, domain.provider_token, "provider-local")
        domain.process = process
        kernel = HttpCasKernel(
            domain.control_db,
            endpoint,
            domain.provider_token,
            "provider-local",
            clock=lambda: 100,
            timeout=1.0,
        )
        observer = HttpCasObserver(endpoint, domain.provider_token, "provider-local", timeout=1.0)
        adapter = HttpCasEffectAdapter(kernel, observer)
        operation = domain.operation("p9-r5-http")
        admitted = adapter.admit(domain.attempt, domain.capability_id, operation)
        self.assertTrue(admitted.allowed, admitted.reason)
        admission_id = admitted.admission.admission_id

        def rebind() -> None:
            time.sleep(0.10)
            route.unlink()
            route.symlink_to(t2)

        thread = threading.Thread(target=rebind)
        thread.start()
        try:
            result = adapter.execute(admission_id, crash_point="timeout_before_commit")
        finally:
            thread.join(2.0)

        self.assertEqual((result.occurred, result.reason), (False, "target_instance_mismatch"))
        self.assertNotEqual(HttpCasObserver(endpoint, domain.provider_token, "provider-local", timeout=1.0).observe(operation.resource).admission_id, admission_id)

    def test_g3_same_object_path_executes_through_pinned_fd(self) -> None:
        domain = G3Domain()
        self.addCleanup(domain.close)
        operation = domain.operation("p9-r5-g3-positive")
        adapter = G3EffectAdapter(domain.kernel, domain.observer)
        admitted = adapter.admit(domain.attempt, domain.capability_id, operation)
        self.assertTrue(admitted.allowed, admitted.reason)
        result = adapter.execute(admitted.admission.admission_id)
        self.assertTrue(result.occurred, result.reason)


if __name__ == "__main__":
    unittest.main()
