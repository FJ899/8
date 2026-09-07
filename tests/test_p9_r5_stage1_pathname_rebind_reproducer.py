from __future__ import annotations

import sqlite3
import unittest
from pathlib import Path

from agency_kernel.effect_seams import G3EffectAdapter
from agency_kernel.g3 import Observer as G3Observer
from tests.test_effect_domain_conformance import G3Domain


class RebindPathAfterValidationG3Adapter(G3EffectAdapter):
    __slots__ = ("_route", "_replacement")

    def __init__(self, kernel, observer, route: Path, replacement: Path) -> None:
        super().__init__(kernel, observer)
        self._route = route
        self._replacement = replacement

    def _execution_target_binding(self, logical_target: str):
        # P9-R4 snapshots the pathname before this call. Resolve/stat while R
        # still names T1, then atomically alter the namespace mapping so the
        # same pathname R names T2 before the domain primitive opens it.
        binding = super()._execution_target_binding(logical_target)
        self._route.unlink()
        self._route.symlink_to(self._replacement)
        self._observer = G3Observer(self._route)
        return binding


class P9R5Stage1PathnameRebindCounterexample(unittest.TestCase):
    @staticmethod
    def _sqlite_clone(source: Path, destination: Path) -> None:
        with sqlite3.connect(str(source)) as src, sqlite3.connect(str(destination)) as dst:
            src.backup(dst)

    def test_validated_pathname_must_not_rebind_to_different_effect_object(self) -> None:
        domain = G3Domain()
        self.addCleanup(domain.close)

        operation = domain.operation("pathname-rebind")
        t1 = Path(domain.target_db).resolve()
        t2 = Path(domain.tempdir.name) / "pathname-t2.db"
        self._sqlite_clone(t1, t2)

        route = Path(domain.tempdir.name) / "bound-route.db"
        route.symlink_to(t1)
        domain.kernel.target_db = str(route)
        adapter = RebindPathAfterValidationG3Adapter(
            domain.kernel,
            G3Observer(route),
            route,
            t2,
        )

        admitted = adapter.admit(domain.attempt, domain.capability_id, operation)
        self.assertTrue(admitted.allowed, admitted.reason)
        self.assertIsNotNone(admitted.admission)
        admission_id = admitted.admission.admission_id

        result = adapter.execute(admission_id)

        # Security requirement. On the frozen P9-R4 candidate the pathname was
        # snapshotted, but not the underlying file object, so re-resolving the
        # same pathname after the symlink switch reaches T2.
        self.assertFalse(
            result.occurred,
            "pathname R was validated as T1 but rebound to T2 before sqlite open",
        )
        t2_observation = G3Observer(t2).observe(operation.resource)
        self.assertNotEqual(
            t2_observation.admission_id,
            admission_id,
            "rebound T2 contains provenance for the historical T1 admission",
        )


if __name__ == "__main__":
    unittest.main()
