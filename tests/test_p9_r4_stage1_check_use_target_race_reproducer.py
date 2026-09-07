from __future__ import annotations

import sqlite3
import unittest
from pathlib import Path

from agency_kernel.effect_seams import G3EffectAdapter
from agency_kernel.g3 import Observer as G3Observer
from tests.test_effect_domain_conformance import G3Domain


class SwapAfterValidationG3Adapter(G3EffectAdapter):
    __slots__ = ("_swap_target",)

    def __init__(self, kernel, observer, swap_target: Path) -> None:
        super().__init__(kernel, observer)
        self._swap_target = swap_target

    def _execution_target_binding(self, logical_target: str):
        # First derive the current binding while T1 is still configured. Then
        # switch the kernel route before the base execute() delegates to the
        # domain primitive. This isolates the check/use window itself.
        binding = super()._execution_target_binding(logical_target)
        self._kernel.target_db = str(self._swap_target)
        self._observer = G3Observer(self._swap_target)
        return binding


class P9R4Stage1CheckUseTargetRace(unittest.TestCase):
    @staticmethod
    def _sqlite_clone(source: Path, destination: Path) -> None:
        with sqlite3.connect(str(source)) as src, sqlite3.connect(str(destination)) as dst:
            src.backup(dst)

    def test_validated_t1_must_be_same_instance_used_by_effect_primitive(self) -> None:
        domain = G3Domain()
        self.addCleanup(domain.close)

        operation = domain.operation("check-use-target-race")
        t2 = Path(domain.tempdir.name) / "check-use-t2.db"
        self._sqlite_clone(Path(domain.target_db), t2)

        adapter = SwapAfterValidationG3Adapter(domain.kernel, domain.observer, t2)
        admitted = adapter.admit(domain.attempt, domain.capability_id, operation)
        self.assertTrue(admitted.allowed, admitted.reason)
        self.assertIsNotNone(admitted.admission)
        admission_id = admitted.admission.admission_id

        result = adapter.execute(admission_id)

        # Security requirement. On the frozen P9-R3 candidate the adapter's
        # validation sees T1, the route switches immediately afterwards, and
        # the domain kernel subsequently opens/mutates T2.
        self.assertFalse(
            result.occurred,
            "target changed after successful instance check and T2 received the historical T1 effect",
        )

        t2_observation = G3Observer(t2).observe(operation.resource)
        self.assertNotEqual(
            t2_observation.admission_id,
            admission_id,
            "substituted T2 contains provenance for the historical T1 admission",
        )


if __name__ == "__main__":
    unittest.main()
