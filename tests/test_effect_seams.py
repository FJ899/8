from __future__ import annotations

import unittest

from agency_kernel.effect_seams import (
    EffectAdapter,
    EffectExecutionResult,
    EffectObservation,
    EffectOperation,
    G3EffectAdapter,
    G4EffectAdapter,
)
from tests.test_effect_domain_conformance import G3Domain, G4Domain


CASES = (
    (G3Domain, G3EffectAdapter),
    (G4Domain, G4EffectAdapter),
)


class EffectSeamConformanceTests(unittest.TestCase):
    def make(self, domain_factory, adapter_factory):
        domain = domain_factory()
        self.addCleanup(domain.close)
        return domain, adapter_factory(domain.kernel, domain.observer)

    def test_existing_operations_results_observations_and_adapters_satisfy_common_projection(self) -> None:
        for domain_factory, adapter_factory in CASES:
            with self.subTest(domain=domain_factory.name):
                domain, adapter = self.make(domain_factory, adapter_factory)
                operation = domain.operation("projection")
                self.assertIsInstance(adapter, EffectAdapter)
                self.assertIsInstance(operation, EffectOperation)
                admission = adapter.admit(domain.attempt, domain.capability_id, operation)
                self.assertTrue(admission.allowed, admission.reason)
                result = adapter.execute(admission.admission.admission_id)
                self.assertIsInstance(result, EffectExecutionResult)
                observation = adapter.observe(operation)
                self.assertIsInstance(observation, EffectObservation)

    def test_target_identity_and_supported_effects_are_domain_exact(self) -> None:
        for domain_factory, adapter_factory in CASES:
            with self.subTest(domain=domain_factory.name):
                domain, adapter = self.make(domain_factory, adapter_factory)
                operation = domain.operation("identity")
                expected_target = "X" if domain_factory is G3Domain else domain.kernel.protected_ref
                self.assertEqual(adapter.target_identity(operation), expected_target)
                self.assertEqual(adapter.supported_possible_effects(operation), operation.possible_effects)

    def test_positive_effect_through_seam_preserves_did_scope_and_satisfaction(self) -> None:
        for domain_factory, adapter_factory in CASES:
            with self.subTest(domain=domain_factory.name):
                domain, adapter = self.make(domain_factory, adapter_factory)
                operation = domain.operation("after")
                admission = adapter.admit(domain.attempt, domain.capability_id, operation)
                self.assertTrue(admission.allowed, admission.reason)
                result = adapter.execute(admission.admission.admission_id)
                self.assertTrue(result.occurred, result.reason)
                observation = adapter.observe(operation)
                self.assertTrue(adapter.did(admission.admission, observation))
                compliance = adapter.assess_compliance(
                    admission.admission,
                    observation,
                    supported_possible_effects=operation.possible_effects,
                )
                self.assertEqual(compliance.status, "PASS")
                self.assertTrue(adapter.within_scope(compliance))
                expected = "after" if domain_factory is G3Domain else {"A.txt": "after"}
                self.assertTrue(adapter.satisfied(observation, expected))

    def test_capability_invalid_and_forged_attempt_still_deny_through_seam(self) -> None:
        for domain_factory, adapter_factory in CASES:
            with self.subTest(domain=domain_factory.name, case="capability_invalid"):
                domain, adapter = self.make(domain_factory, adapter_factory)
                domain.invalidate_capability()
                result = adapter.admit(domain.attempt, domain.capability_id, domain.operation())
                self.assertFalse(result.allowed)
                self.assertEqual(result.reason, "capability_invalid")
            with self.subTest(domain=domain_factory.name, case="forged_attempt"):
                domain, adapter = self.make(domain_factory, adapter_factory)
                result = adapter.admit(domain.forged_attempt(), domain.capability_id, domain.operation())
                self.assertFalse(result.allowed)
                self.assertEqual(result.reason, "forged_attempt")

    def test_effect_envelope_exceeded_still_denies_through_seam(self) -> None:
        for domain_factory, adapter_factory in CASES:
            with self.subTest(domain=domain_factory.name):
                domain, adapter = self.make(domain_factory, adapter_factory)
                domain.kernel.set_authorized_effect_envelope(domain.contract.contract_id, frozenset())
                result = adapter.admit(domain.attempt, domain.capability_id, domain.operation())
                self.assertFalse(result.allowed)
                self.assertEqual(result.reason, "effect_envelope_exceeded")

    def test_exact_operation_binding_prevents_o1_to_o2_substitution_through_seam(self) -> None:
        for domain_factory, adapter_factory in CASES:
            with self.subTest(domain=domain_factory.name):
                domain, adapter = self.make(domain_factory, adapter_factory)
                op1 = domain.operation("O1")
                admission = adapter.admit(domain.attempt, domain.capability_id, op1)
                self.assertTrue(admission.allowed, admission.reason)
                op2 = domain.operation("O2")
                self.assertNotEqual(op1.operation_digest, op2.operation_digest)
                result = adapter.execute(admission.admission.admission_id)
                self.assertTrue(result.occurred, result.reason)
                observation = adapter.observe(op1)
                expected_o1 = "O1" if domain_factory is G3Domain else {"A.txt": "O1"}
                expected_o2 = "O2" if domain_factory is G3Domain else {"A.txt": "O2"}
                self.assertTrue(adapter.satisfied(observation, expected_o1))
                self.assertFalse(adapter.satisfied(observation, expected_o2))

    def test_admission_replay_still_denies_second_effect_through_seam(self) -> None:
        for domain_factory, adapter_factory in CASES:
            with self.subTest(domain=domain_factory.name):
                domain, adapter = self.make(domain_factory, adapter_factory)
                operation = domain.operation("once")
                admission = adapter.admit(domain.attempt, domain.capability_id, operation)
                self.assertTrue(admission.allowed, admission.reason)
                first = adapter.execute(admission.admission.admission_id)
                self.assertTrue(first.occurred, first.reason)
                second = adapter.execute(admission.admission.admission_id)
                self.assertFalse(second.occurred)
                self.assertEqual(second.reason, "admission_consumed")

    def test_coverage_and_attribution_uncertainty_remain_indeterminate_through_seam(self) -> None:
        for domain_factory, adapter_factory in CASES:
            with self.subTest(domain=domain_factory.name, case="coverage"):
                domain, adapter = self.make(domain_factory, adapter_factory)
                operation = domain.operation("coverage")
                admission = adapter.admit(domain.attempt, domain.capability_id, operation)
                self.assertTrue(admission.allowed, admission.reason)
                self.assertTrue(adapter.execute(admission.admission.admission_id).occurred)
                compliance = adapter.assess_compliance(
                    admission.admission,
                    adapter.observe(operation, covered=False),
                    supported_possible_effects=operation.possible_effects,
                )
                self.assertEqual((compliance.status, compliance.reason), ("INDETERMINATE", "missing_coverage"))
            with self.subTest(domain=domain_factory.name, case="attribution"):
                domain, adapter = self.make(domain_factory, adapter_factory)
                operation = domain.operation("attribution")
                admission = adapter.admit(domain.attempt, domain.capability_id, operation)
                self.assertTrue(admission.allowed, admission.reason)
                self.assertTrue(adapter.execute(admission.admission.admission_id).occurred)
                compliance = adapter.assess_compliance(
                    admission.admission,
                    adapter.observe(operation, attribution_ambiguous=True),
                    supported_possible_effects=operation.possible_effects,
                )
                self.assertEqual((compliance.status, compliance.reason), ("INDETERMINATE", "ambiguous_attribution"))

    def test_crash_before_effect_preserves_no_blind_replay_through_seam(self) -> None:
        for domain_factory, adapter_factory in CASES:
            with self.subTest(domain=domain_factory.name):
                domain, adapter = self.make(domain_factory, adapter_factory)
                operation = domain.operation("before-crash")
                admission = adapter.admit(domain.attempt, domain.capability_id, operation)
                self.assertTrue(admission.allowed, admission.reason)
                result = adapter.execute(
                    admission.admission.admission_id,
                    crash_point=domain.crash_before_effect,
                )
                self.assertFalse(result.occurred)
                replay = adapter.execute(admission.admission.admission_id)
                self.assertFalse(replay.occurred)
                self.assertEqual(replay.reason, "admission_consumed")

    def test_crash_after_effect_remains_recoverable_from_observation_through_seam(self) -> None:
        for domain_factory, adapter_factory in CASES:
            with self.subTest(domain=domain_factory.name):
                domain, adapter = self.make(domain_factory, adapter_factory)
                operation = domain.operation("committed")
                admission = adapter.admit(domain.attempt, domain.capability_id, operation)
                self.assertTrue(admission.allowed, admission.reason)
                result = adapter.execute(
                    admission.admission.admission_id,
                    crash_point=domain.crash_after_effect,
                )
                self.assertTrue(result.occurred, result.reason)
                self.assertFalse(adapter.has_control_completion(admission.admission.admission_id))
                observation = adapter.observe(operation)
                self.assertTrue(adapter.did(admission.admission, observation))
                compliance = adapter.assess_compliance(
                    admission.admission,
                    observation,
                    supported_possible_effects=operation.possible_effects,
                )
                self.assertEqual(compliance.status, "PASS")
                self.assertEqual(adapter.execute(admission.admission.admission_id).reason, "admission_consumed")

    def test_common_seam_does_not_expose_authority_routing_or_backing_objects_publicly(self) -> None:
        forbidden = {
            "authorize",
            "start_attempt",
            "add_capability",
            "set_authorized_effect_envelope",
            "select_capability",
            "route",
            "kernel",
            "observer",
        }
        for domain_factory, adapter_factory in CASES:
            with self.subTest(adapter=adapter_factory.__name__):
                _domain, adapter = self.make(domain_factory, adapter_factory)
                public_surface = {name for name in dir(adapter) if not name.startswith("_")}
                self.assertTrue(forbidden.isdisjoint(public_surface))


if __name__ == "__main__":
    unittest.main()
