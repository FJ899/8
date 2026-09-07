from __future__ import annotations

import sqlite3
import unittest
from pathlib import Path

from agency_kernel.effect_seams import G3EffectAdapter
from agency_kernel.g3 import Observer as G3Observer
from tests.test_effect_domain_conformance import G3Domain


class P9R3Stage1ExecutionTargetBindingCounterexample(unittest.TestCase):
    @staticmethod
    def _sqlite_clone(source: Path, destination: Path) -> None:
        with sqlite3.connect(str(source)) as src, sqlite3.connect(str(destination)) as dst:
            src.backup(dst)

    def test_admitted_t1_must_not_execute_on_wrong_t2_after_target_switch(self) -> None:
        domain = G3Domain()
        self.addCleanup(domain.close)

        operation = domain.operation("execution-target-binding")
        adapter = G3EffectAdapter(domain.kernel, domain.observer)
        admitted = adapter.admit(domain.attempt, domain.capability_id, operation)
        self.assertTrue(admitted.allowed, admitted.reason)
        self.assertIsNotNone(admitted.admission)
        admission_id = admitted.admission.admission_id

        historical_t1 = Path(domain.target_db)
        wrong_t2 = Path(domain.tempdir.name) / "execution-wrong-t2.db"
        self._sqlite_clone(historical_t1, wrong_t2)

        # Simulate trusted target-composition drift after admission but before the
        # protected effect boundary. The same adapter/control ledger continues,
        # but its domain kernel now points at a distinct physical target store T2.
        domain.kernel.target_db = str(wrong_t2)
        adapter._observer = G3Observer(wrong_t2)

        result = adapter.execute(admission_id)

        # Security requirement: an admission historically bound to T1 must not
        # execute against T2. On the frozen P9-R2 candidate this assertion is
        # expected to fail because execute() does not revalidate target binding.
        self.assertFalse(
            result.occurred,
            "historical T1 admission executed on substituted target T2",
        )

        t1 = G3Observer(historical_t1).observe(operation.resource)
        t2 = G3Observer(wrong_t2).observe(operation.resource)
        self.assertNotEqual(t1.admission_id, admission_id)
        self.assertNotEqual(t2.admission_id, admission_id)


if __name__ == "__main__":
    unittest.main()
