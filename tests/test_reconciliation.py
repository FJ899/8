from __future__ import annotations

from dataclasses import replace
from types import SimpleNamespace
import unittest

from agency_kernel.reconciliation import (
    G3ReconciliationAdapter,
    G4ReconciliationAdapter,
    Reconciler,
    ReconciliationResult,
    ReconciliationStatus,
)
from tests.test_effect_domain_conformance import G3Domain, G4Domain


DOMAIN_FACTORIES = (G3Domain, G4Domain)


class CommonReconciliationTests(unittest.TestCase):
    def domain(self, factory):
        domain = factory()
        self.addCleanup(domain.close)
        if factory is G3Domain:
            adapter = G3ReconciliationAdapter(domain.kernel, domain.observer)
        else:
            adapter = G4ReconciliationAdapter(domain.kernel, domain.observer)
        return domain, Reconciler(adapter)

    def admitted(self, domain, value="after"):
        operation = domain.operation(value)
        result = domain.admit(operation)
        self.assertTrue(result.allowed, result.reason)
        self.assertIsNotNone(result.admission)
        return operation, result.admission

    def test_successful_effect_reconciles_occurred_from_durable_start_and_target_attribution(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "done")
                execution = d.execute(admission.admission_id)
                self.assertTrue(execution.occurred, execution.reason)
                result = reconciler.reconcile(admission, operation)
                self.assertEqual((result.status, result.reason), (ReconciliationStatus.OCCURRED, "attributed_target_effect"))

    def test_lost_success_result_still_reconciles_occurred_from_durable_evidence(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "lost-result")
                self.assertTrue(d.execute(admission.admission_id).occurred)
                result = reconciler.reconcile(admission, operation)
                self.assertEqual(result.status, ReconciliationStatus.OCCURRED)

    def test_crash_after_effect_before_control_completion_reconciles_occurred(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "committed")
                execution = d.execute(admission.admission_id, crash_point=d.crash_after_effect)
                self.assertTrue(execution.occurred, execution.reason)
                self.assertFalse(d.has_control_completion(admission.admission_id))
                result = reconciler.reconcile(admission, operation)
                self.assertEqual((result.status, result.reason), (ReconciliationStatus.OCCURRED, "attributed_target_effect"))

    def test_admitted_but_never_executed_is_durably_not_occurred(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "never-started")
                result = reconciler.reconcile(admission, operation)
                self.assertEqual((result.status, result.reason), (ReconciliationStatus.NOT_OCCURRED, "execution_never_started"))

    def test_crash_before_effect_after_execution_start_is_indeterminate_not_not_occurred(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "never")
                execution = d.execute(admission.admission_id, crash_point=d.crash_before_effect)
                self.assertFalse(execution.occurred)
                result = reconciler.reconcile(admission, operation)
                self.assertEqual(
                    (result.status, result.reason),
                    (ReconciliationStatus.INDETERMINATE, "execution_started_without_attributed_effect"),
                )
                self.assertNotEqual(result.status, ReconciliationStatus.NOT_OCCURRED)

    def test_missing_coverage_remains_indeterminate_even_when_effect_is_attributable(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "covered")
                self.assertTrue(d.execute(admission.admission_id).occurred)
                result = reconciler.reconcile(admission, operation, covered=False)
                self.assertEqual((result.status, result.reason), (ReconciliationStatus.INDETERMINATE, "missing_coverage"))

    def test_ambiguous_attribution_remains_indeterminate(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "ambiguous")
                self.assertTrue(d.execute(admission.admission_id).occurred)
                result = reconciler.reconcile(admission, operation, attribution_ambiguous=True)
                self.assertEqual((result.status, result.reason), (ReconciliationStatus.INDETERMINATE, "ambiguous_attribution"))

    def test_unattributed_external_change_after_execution_started_is_indeterminate(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "authorized")
                execution = d.execute(admission.admission_id, crash_point=d.crash_before_effect)
                self.assertFalse(execution.occurred)
                d.inject_unattributed("external")
                result = reconciler.reconcile(admission, operation)
                self.assertEqual(
                    (result.status, result.reason),
                    (ReconciliationStatus.INDETERMINATE, "execution_started_without_attributed_effect"),
                )

    def test_later_unattributed_change_invalidates_current_attribution(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "authorized")
                self.assertTrue(d.execute(admission.admission_id).occurred)
                self.assertEqual(reconciler.reconcile(admission, operation).status, ReconciliationStatus.OCCURRED)
                d.inject_unattributed("later")
                result = reconciler.reconcile(admission, operation)
                self.assertEqual(
                    (result.status, result.reason),
                    (ReconciliationStatus.INDETERMINATE, "execution_started_without_attributed_effect"),
                )

    def test_forged_execution_shaped_input_has_no_reconciliation_surface(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "never")
                forged = SimpleNamespace(
                    occurred=False,
                    reason=d.crash_before_effect,
                    operation_digest=admission.operation_digest,
                )
                with self.assertRaises(TypeError):
                    reconciler.reconcile(admission, operation, execution=forged)
                result = reconciler.reconcile(admission, operation)
                self.assertEqual(result.status, ReconciliationStatus.NOT_OCCURRED)

    def test_forged_or_altered_admission_is_not_treated_as_durable_fact(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "bound")
                forged = replace(admission, admission_id="forged-admission")
                result = reconciler.reconcile(forged, operation)
                self.assertEqual((result.status, result.reason, result.observation), (ReconciliationStatus.INDETERMINATE, "unbound_admission", None))

    def test_replacement_operation_is_rejected_before_observation(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "O1")
                replacement = d.operation("O2")
                self.assertNotEqual(operation.operation_digest, replacement.operation_digest)
                result = reconciler.reconcile(admission, replacement)
                self.assertEqual(
                    (result.status, result.reason, result.observation),
                    (ReconciliationStatus.INDETERMINATE, "admission_operation_mismatch", None),
                )

    def test_control_target_contradiction_does_not_create_occurred(self) -> None:
        class ContradictoryAdapter:
            def admission_matches_ledger(self, admission):
                return True

            def execution_started(self, admission_id):
                return False

            def observe(self, operation, *, covered=True, attribution_ambiguous=False):
                return SimpleNamespace(
                    admission_id="anything",
                    operation_digest=operation.operation_digest,
                    covered=covered,
                    attribution_ambiguous=attribution_ambiguous,
                )

            def did(self, admission, observation):
                return True

        d = G3Domain()
        self.addCleanup(d.close)
        operation, admission = self.admitted(d, "contradiction")
        result = Reconciler(ContradictoryAdapter()).reconcile(admission, operation)
        self.assertEqual(
            (result.status, result.reason),
            (ReconciliationStatus.INDETERMINATE, "target_attribution_without_execution_start"),
        )

    def test_reconciliation_has_no_execution_admission_authority_or_retry_surface(self) -> None:
        forbidden = {
            "execute",
            "admit",
            "authorize",
            "start_attempt",
            "retry",
            "accept",
            "within_scope",
            "satisfied",
        }
        self.assertTrue(forbidden.isdisjoint(set(dir(Reconciler))))
        self.assertTrue(forbidden.isdisjoint({name for name in dir(G3ReconciliationAdapter) if not name.startswith("_")}))
        self.assertTrue(forbidden.isdisjoint({name for name in dir(G4ReconciliationAdapter) if not name.startswith("_")}))

    def test_reconciliation_does_not_create_authorization(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "goal")
                before = len(d.kernel.snapshot()["action_authorizations"])
                result = reconciler.reconcile(admission, operation)
                self.assertEqual(result.status, ReconciliationStatus.NOT_OCCURRED)
                after = len(d.kernel.snapshot()["action_authorizations"])
                self.assertEqual(after, before)

    def test_reconciliation_result_does_not_collapse_security_verdicts(self) -> None:
        self.assertEqual(set(ReconciliationStatus.__members__), {"OCCURRED", "NOT_OCCURRED", "INDETERMINATE"})
        result_fields = set(ReconciliationResult.__dataclass_fields__)
        self.assertEqual(result_fields, {"status", "reason", "observation"})
        self.assertTrue(
            {"authorized", "pass", "within_scope", "satisfied", "accepted", "retry"}.isdisjoint(result_fields)
        )


if __name__ == "__main__":
    unittest.main()
