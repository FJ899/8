from __future__ import annotations

import sqlite3
import unittest
from pathlib import Path

from agency_kernel.effect_seams import G3EffectAdapter
from agency_kernel.evidence import EffectEvidenceCollector, G3EvidenceProducer
from agency_kernel.g3 import Kernel as G3Kernel, Observer as G3Observer
from agency_kernel.reconciliation import ReconciliationStatus
from tests.test_effect_domain_conformance import G3Domain


class P9R2Stage1TargetInstanceCounterexample(unittest.TestCase):
    @staticmethod
    def _sqlite_clone(source: Path, destination: Path) -> None:
        with sqlite3.connect(str(source)) as src, sqlite3.connect(str(destination)) as dst:
            src.backup(dst)

    def test_historical_t1_admission_must_not_rehydrate_occurred_from_wrong_t2_clone(self) -> None:
        domain = G3Domain()
        self.addCleanup(domain.close)

        operation = domain.operation("historical-target-instance")
        adapter_t1 = G3EffectAdapter(domain.kernel, domain.observer)
        admitted = adapter_t1.admit(domain.attempt, domain.capability_id, operation)
        self.assertTrue(admitted.allowed, admitted.reason)
        self.assertIsNotNone(admitted.admission)
        admission_id = admitted.admission.admission_id

        executed = adapter_t1.execute(admission_id)
        self.assertTrue(executed.occurred, executed.reason)

        # T2 is a distinct physical SQLite target-store instance containing a
        # logically equivalent copy of T1 state and mutation provenance.
        target_t2 = Path(domain.tempdir.name) / "wrong-target-t2.db"
        self._sqlite_clone(Path(domain.target_db), target_t2)
        self.assertNotEqual(Path(domain.target_db).resolve(), target_t2.resolve())

        # Recovery deliberately reuses the real durable control ledger and exact
        # admission/operation, but reconstructs the effect domain against T2.
        wrong_kernel = G3Kernel(domain.control_db, target_t2, clock=lambda: 100)
        wrong_adapter = G3EffectAdapter(wrong_kernel, G3Observer(target_t2))
        collector = EffectEvidenceCollector(G3EvidenceProducer(wrong_adapter))

        # Stage-1 frozen branch records the pre-repair red form of this attack.
        # On the Stage-2 repair branch, fail-closed rejection before
        # reconciliation is a valid repair outcome. If evidence is returned,
        # it still must never establish historical T1 OCCURRED from T2.
        try:
            evidence = collector.collect_from_admission_id(admission_id, operation)
        except ValueError as exc:
            self.assertEqual(str(exc), "target_instance_mismatch")
            return

        self.assertNotEqual(
            evidence.reconciliation.status,
            ReconciliationStatus.OCCURRED,
            "wrong physical target T2 was accepted as historical T1 evidence",
        )


if __name__ == "__main__":
    unittest.main()
