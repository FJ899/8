from __future__ import annotations

from dataclasses import replace
import unittest

from agency_kernel.effect_seams import G3EffectAdapter, G4EffectAdapter
from agency_kernel.reconciliation import (
    G3ReconciliationAdapter,
    G4ReconciliationAdapter,
    Reconciler,
    ReconciliationStatus,
)
from tests.test_effect_domain_conformance import G3Domain, G4Domain


DOMAIN_FACTORIES = (G3Domain, G4Domain)


class CommonReconciliationTests(unittest.TestCase):
    def domain(self, factory):
        domain = factory()
        self.addCleanup(domain.close)
        if factory is G3Domain:
            effect = G3EffectAdapter(domain.kernel, domain.observer)
            adapter = G3ReconciliationAdapter(effect)
        else:
            effect = G4EffectAdapter(domain.kernel, domain.observer)
            adapter = G4ReconciliationAdapter(effect)
        return domain, Reconciler(adapter)

    def admitted(self, domain, value="after"):
        operation = domain.operation(value)
        result = domain.admit(operation)
        self.assertTrue(result.allowed, result.reason)
        self.assertIsNotNone(result.admission)
        return operation, result.admission

    def test_successful_effect_reconciles_occurred_from_target_attribution(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "done")
                execution = d.execute(admission.admission_id)
                self.assertTrue(execution.occurred, execution.reason)
                result = reconciler.reconcile(admission, operation, execution=execution)
                self.assertEqual(result.status, ReconciliationStatus.OCCURRED)
                self.assertEqual(result.reason, "attributed_target_effect")

    def test_lost_success_result_still_reconciles_occurred_from_target_evidence(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "lost-result")
                execution = d.execute(admission.admission_id)
                self.assertTrue(execution.occurred, execution.reason)
                result = reconciler.reconcile(admission, operation, execution=None)
                self.assertEqual(result.status, ReconciliationStatus.OCCURRED)
                self.assertEqual(result.reason, "attributed_target_effect")

    def test_crash_after_effect_before_control_completion_reconciles_occurred(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "committed")
                execution = d.execute(admission.admission_id, crash_point=d.crash_after_effect)
                self.assertTrue(execution.occurred, execution.reason)
                self.assertFalse(d.has_control_completion(admission.admission_id))
                result = reconciler.reconcile(admission, operation, execution=None)
                self.assertEqual(result.status, ReconciliationStatus.OCCURRED)

    def test_trusted_pre_effect_result_can_establish_not_occurred(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "never")
                execution = d.execute(admission.admission_id, crash_point=d.crash_before_effect)
                self.assertFalse(execution.occurred)
                result = reconciler.reconcile(admission, operation, execution=execution)
                self.assertEqual(result.status, ReconciliationStatus.NOT_OCCURRED)
                self.assertEqual(result.reason, "trusted_pre_effect_result")

    def test_lost_pre_effect_result_does_not_infer_not_occurred_from_unchanged_target(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "never")
                execution = d.execute(admission.admission_id, crash_point=d.crash_before_effect)
                self.assertFalse(execution.occurred)
                result = reconciler.reconcile(admission, operation, execution=None)
                self.assertEqual(result.status, ReconciliationStatus.INDETERMINATE)
                self.assertEqual(result.reason, "unresolved_outcome")

    def test_missing_coverage_remains_indeterminate_even_with_attributed_effect(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "covered")
                execution = d.execute(admission.admission_id)
                self.assertTrue(execution.occurred)
                result = reconciler.reconcile(
                    admission,
                    operation,
                    execution=execution,
                    covered=False,
                )
                self.assertEqual((result.status, result.reason), (ReconciliationStatus.INDETERMINATE, "missing_coverage"))

    def test_ambiguous_attribution_remains_indeterminate(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "ambiguous")
                execution = d.execute(admission.admission_id)
                self.assertTrue(execution.occurred)
                result = reconciler.reconcile(
                    admission,
                    operation,
                    execution=execution,
                    attribution_ambiguous=True,
                )
                self.assertEqual((result.status, result.reason), (ReconciliationStatus.INDETERMINATE, "ambiguous_attribution"))

    def test_unattributed_external_target_change_without_execution_result_is_indeterminate(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "authorized")
                d.inject_unattributed("external")
                result = reconciler.reconcile(admission, operation, execution=None)
                self.assertEqual((result.status, result.reason), (ReconciliationStatus.INDETERMINATE, "unresolved_outcome"))

    def test_later_unattributed_change_invalidates_current_attribution(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "authorized")
                execution = d.execute(admission.admission_id)
                self.assertTrue(execution.occurred)
                self.assertEqual(reconciler.reconcile(admission, operation).status, ReconciliationStatus.OCCURRED)
                d.inject_unattributed("later")
                result = reconciler.reconcile(admission, operation, execution=None)
                self.assertEqual(result.status, ReconciliationStatus.INDETERMINATE)
                self.assertEqual(result.reason, "unresolved_outcome")

    def test_execution_claim_without_target_attribution_is_indeterminate(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "authorized")
                execution = d.execute(admission.admission_id)
                self.assertTrue(execution.occurred)
                d.inject_unattributed("later")
                result = reconciler.reconcile(admission, operation, execution=execution)
                self.assertEqual((result.status, result.reason), (ReconciliationStatus.INDETERMINATE, "execution_effect_not_attributed"))

    def test_false_execution_result_conflicting_with_attributed_target_is_indeterminate(self) -> None:
        safe_reason = {
            G3Domain: "crash_before_mutation",
            G4Domain: "crash_before_ref_cas",
        }
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "committed")
                execution = d.execute(admission.admission_id)
                self.assertTrue(execution.occurred)
                contradictory = replace(execution, occurred=False, reason=safe_reason[factory])
                result = reconciler.reconcile(admission, operation, execution=contradictory)
                self.assertEqual(
                    (result.status, result.reason),
                    (ReconciliationStatus.INDETERMINATE, "conflicting_execution_and_target_evidence"),
                )

    def test_execution_result_for_other_admission_cannot_establish_not_occurred(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "never")
                execution = d.execute(admission.admission_id, crash_point=d.crash_before_effect)
                bad = replace(execution, operation_digest="0" * 64)
                result = reconciler.reconcile(admission, operation, execution=bad)
                self.assertEqual((result.status, result.reason), (ReconciliationStatus.INDETERMINATE, "execution_admission_mismatch"))

    def test_admission_consumed_result_never_means_not_occurred(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "once")
                first = d.execute(admission.admission_id)
                self.assertTrue(first.occurred)
                replay = d.execute(admission.admission_id)
                self.assertFalse(replay.occurred)
                self.assertEqual(replay.reason, "admission_consumed")
                result = reconciler.reconcile(admission, operation, execution=replay)
                self.assertEqual(result.status, ReconciliationStatus.INDETERMINATE)
                self.assertNotEqual(result.status, ReconciliationStatus.NOT_OCCURRED)

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
        self.assertTrue(forbidden.isdisjoint(set(dir(G3ReconciliationAdapter))))
        self.assertTrue(forbidden.isdisjoint(set(dir(G4ReconciliationAdapter))))

    def test_reconciliation_does_not_create_authorization(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d, reconciler = self.domain(factory)
                operation, admission = self.admitted(d, "goal")
                before = len(d.kernel.snapshot()["action_authorizations"])
                result = reconciler.reconcile(admission, operation, execution=None)
                self.assertEqual(result.status, ReconciliationStatus.INDETERMINATE)
                after = len(d.kernel.snapshot()["action_authorizations"])
                self.assertEqual(after, before)

    def test_reconciliation_result_does_not_collapse_security_verdicts(self) -> None:
        fields = set(ReconciliationStatus.__members__)
        self.assertEqual(fields, {"OCCURRED", "NOT_OCCURRED", "INDETERMINATE"})
        from agency_kernel.reconciliation import ReconciliationResult

        result_fields = set(ReconciliationResult.__dataclass_fields__)
        self.assertEqual(result_fields, {"status", "reason", "observation"})
        self.assertTrue({"authorized", "pass", "within_scope", "satisfied", "accepted"}.isdisjoint(result_fields))


if __name__ == "__main__":
    unittest.main()
