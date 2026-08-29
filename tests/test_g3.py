from __future__ import annotations

import tempfile
import threading
import unittest
from pathlib import Path

from agency_kernel.g1 import ActionRequest, AuthenticationContext, AuthorityGrant, AuthorityRoot, EffectContract, EffectIntent, Principal
from agency_kernel.g2 import Capability
from agency_kernel.g3 import DishonestPrimitive, Kernel, Observer, PutIfVersionOperation


class G3ControlledEffectSoundnessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        root = Path(self.tempdir.name)
        self.control_db = root / "control-ledger.db"
        self.target_db = root / "target.db"
        self.kernel = Kernel(self.control_db, self.target_db, clock=lambda: 100)
        self.root = AuthorityRoot("root")
        self.alice = Principal("alice")
        self.context = AuthenticationContext("session-alice")
        self.intent = EffectIntent("intent.put", "versioned-put")
        self.contract = EffectContract("contract.put", self.intent.intent_id)
        self.kernel.add_authority_root(self.root)
        self.kernel.add_principal(self.alice)
        self.kernel.establish_authentication_context(self.context, self.alice)
        self.kernel.add_effect_intent(self.intent)
        self.kernel.add_effect_contract(self.contract)
        self.kernel.add_authority_grant(AuthorityGrant("grant-alice", "root", "alice", self.intent.intent_id))
        self.kernel.add_capability(Capability("cap-X", "X"))
        self.kernel.set_authorized_effect_envelope(self.contract.contract_id, self.kernel.possible_effects_for("X"))
        request = ActionRequest("request-1", self.intent.intent_id, self.contract.contract_id)
        auth = self.kernel.authorize(request, authentication_context=self.context)
        self.assertTrue(auth.allowed)
        start = self.kernel.start_attempt(auth.authorization)
        self.assertTrue(start.allowed)
        self.attempt = start.attempt
        self.kernel.seed_resource("X", "initial", 0)
        self.observer = Observer(self.target_db)

    def op(self, *, expected_version=0, value="after", effects="default") -> PutIfVersionOperation:
        if effects == "default":
            effects = self.kernel.possible_effects_for("X")
        return PutIfVersionOperation("X", expected_version, value, effects)

    def admit(self, operation=None):
        result = self.kernel.admit_put_if_version(self.attempt, "cap-X", operation or self.op())
        self.assertTrue(result.allowed, result.reason)
        return result.admission

    def test_positive_supported_primitive_effect_is_attributed_and_within_scope(self) -> None:
        operation = self.op(value="after")
        admission = self.admit(operation)
        result = self.kernel.execute_put_if_version_admission(admission.admission_id)
        self.assertTrue(result.occurred)
        self.assertTrue(self.kernel.has_control_completion(admission.admission_id))
        observation = self.observer.observe("X")
        self.assertTrue(self.kernel.did(admission, observation))
        compliance = self.kernel.assess_compliance(admission, observation, supported_possible_effects=operation.possible_effects)
        self.assertEqual(compliance.status, "PASS")
        self.assertTrue(self.kernel.within_scope(compliance))
        self.assertTrue(self.kernel.satisfied(observation, "after"))
        self.assertTrue(compliance.actual_effects.issubset(operation.possible_effects))

    def test_stale_version_denies_at_mutation_boundary(self) -> None:
        admission = self.admit(self.op(expected_version=1))
        result = self.kernel.execute_put_if_version_admission(admission.admission_id)
        self.assertFalse(result.occurred)
        self.assertEqual(result.reason, "stale_version")
        self.assertFalse(self.kernel.has_control_completion(admission.admission_id))
        obs = self.observer.observe("X")
        self.assertEqual((obs.value, obs.version), ("initial", 0))

    def test_concurrent_mutation_with_same_expected_version_yields_one_effect(self) -> None:
        a1 = self.admit(self.op(value="one"))
        a2 = self.admit(self.op(value="two"))
        barrier = threading.Barrier(3)
        results = []
        lock = threading.Lock()
        def run(admission_id):
            barrier.wait()
            r = self.kernel.execute_put_if_version_admission(admission_id)
            with lock:
                results.append((admission_id, r))
        t1 = threading.Thread(target=run, args=(a1.admission_id,))
        t2 = threading.Thread(target=run, args=(a2.admission_id,))
        t1.start(); t2.start(); barrier.wait(); t1.join(); t2.join()
        self.assertEqual(sum(1 for _, r in results if r.occurred), 1)
        self.assertEqual(sum(1 for _, r in results if r.reason == "stale_version"), 1)
        winner = next(aid for aid, r in results if r.occurred)
        loser = next(aid for aid, r in results if not r.occurred)
        self.assertTrue(self.kernel.has_control_completion(winner))
        self.assertFalse(self.kernel.has_control_completion(loser))
        self.assertEqual(self.observer.observe("X").version, 1)

    def test_unknown_possible_effects_denies_pre_effect(self) -> None:
        result = self.kernel.admit_put_if_version(self.attempt, "cap-X", self.op(effects=None))
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "unknown_possible_effects")
        self.assertEqual(self.observer.observe("X").value, "initial")

    def test_effect_envelope_overapproximation_is_safe_but_restrictive(self) -> None:
        declared = self.kernel.possible_effects_for("X") | frozenset({"MAYBE(X)"})
        result = self.kernel.admit_put_if_version(self.attempt, "cap-X", self.op(effects=declared))
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "effect_model_mismatch")

    def test_supported_primitive_underapproximation_is_rejected(self) -> None:
        result = self.kernel.admit_put_if_version(self.attempt, "cap-X", self.op(effects=frozenset({"MODIFY(X)"})))
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "effect_model_mismatch")

    def test_missing_observation_coverage_is_indeterminate(self) -> None:
        admission = self.admit()
        self.assertTrue(self.kernel.execute_put_if_version_admission(admission.admission_id).occurred)
        obs = self.observer.observe("X", covered=False)
        compliance = self.kernel.assess_compliance(admission, obs, supported_possible_effects=self.kernel.possible_effects_for("X"))
        self.assertEqual((compliance.status, compliance.reason), ("INDETERMINATE", "missing_coverage"))

    def test_ambiguous_attribution_is_indeterminate(self) -> None:
        admission = self.admit()
        self.assertTrue(self.kernel.execute_put_if_version_admission(admission.admission_id).occurred)
        obs = self.observer.observe("X", attribution_ambiguous=True)
        compliance = self.kernel.assess_compliance(admission, obs, supported_possible_effects=self.kernel.possible_effects_for("X"))
        self.assertEqual((compliance.status, compliance.reason), ("INDETERMINATE", "ambiguous_attribution"))

    def test_observed_delta_without_provenance_does_not_become_attribution(self) -> None:
        admission = self.admit()
        self.kernel.inject_unattributed_delta_for_test("X", "unattributed", 1)
        obs = self.observer.observe("X")
        self.assertEqual(obs.value, "unattributed")
        self.assertIsNone(obs.mutation_id)
        self.assertFalse(self.kernel.did(admission, obs))
        compliance = self.kernel.assess_compliance(admission, obs, supported_possible_effects=self.kernel.possible_effects_for("X"))
        self.assertEqual((compliance.status, compliance.reason), ("INDETERMINATE", "unresolved_attribution"))

    def test_crash_before_mutation_has_no_effect_and_no_blind_replay(self) -> None:
        admission = self.admit()
        result = self.kernel.execute_put_if_version_admission(admission.admission_id, crash_point="before_mutation")
        self.assertFalse(result.occurred)
        self.assertFalse(self.kernel.has_control_completion(admission.admission_id))
        self.assertEqual(self.observer.observe("X").value, "initial")
        replay = self.kernel.execute_put_if_version_admission(admission.admission_id)
        self.assertFalse(replay.occurred)
        self.assertEqual(replay.reason, "admission_consumed")

    def test_crash_after_admission_before_mutation_has_no_effect_and_no_blind_replay(self) -> None:
        admission = self.admit()
        result = self.kernel.execute_put_if_version_admission(admission.admission_id, crash_point="after_admission_before_mutation")
        self.assertFalse(result.occurred)
        self.assertFalse(self.kernel.has_control_completion(admission.admission_id))
        self.assertEqual(self.observer.observe("X").value, "initial")
        replay = self.kernel.execute_put_if_version_admission(admission.admission_id)
        self.assertEqual(replay.reason, "admission_consumed")

    def test_crash_after_mutation_before_control_completion_is_recoverable_from_target_provenance(self) -> None:
        operation = self.op(value="committed")
        admission = self.admit(operation)
        result = self.kernel.execute_put_if_version_admission(admission.admission_id, crash_point="after_mutation_before_control_completion")
        self.assertTrue(result.occurred)
        self.assertFalse(self.kernel.has_control_completion(admission.admission_id))
        obs = self.observer.observe("X")
        self.assertTrue(self.kernel.did(admission, obs))
        compliance = self.kernel.assess_compliance(admission, obs, supported_possible_effects=operation.possible_effects)
        self.assertEqual(compliance.status, "PASS")
        replay = self.kernel.execute_put_if_version_admission(admission.admission_id)
        self.assertEqual(replay.reason, "admission_consumed")

    def test_did_does_not_imply_authorized(self) -> None:
        operation = self.op(value="done")
        admission = self.admit(operation)
        self.assertTrue(self.kernel.execute_put_if_version_admission(admission.admission_id).occurred)
        obs = self.observer.observe("X")
        self.assertTrue(self.kernel.did(admission, obs))
        forged = type(self.attempt)(self.attempt.attempt_id, self.attempt.authorization_id, "mallory", self.attempt.intent_id, self.attempt.contract_id)
        denied = self.kernel.admit_put_if_version(forged, "cap-X", self.op(expected_version=1, value="other"))
        self.assertFalse(denied.allowed)

    def test_attempted_does_not_imply_effect(self) -> None:
        admission = self.admit(self.op(expected_version=7))
        result = self.kernel.execute_put_if_version_admission(admission.admission_id)
        self.assertFalse(result.occurred)
        self.assertEqual(self.observer.observe("X").value, "initial")

    def test_satisfied_does_not_imply_authorized_or_within_scope(self) -> None:
        admission = self.admit(self.op(value="goal"))
        self.assertTrue(self.kernel.execute_put_if_version_admission(admission.admission_id).occurred)
        obs = self.observer.observe("X", covered=False)
        self.assertTrue(self.kernel.satisfied(obs, "goal"))
        compliance = self.kernel.assess_compliance(admission, obs, supported_possible_effects=self.kernel.possible_effects_for("X"))
        self.assertFalse(self.kernel.within_scope(compliance))
        self.kernel.set_grant_revoked("grant-alice", True)
        denied = self.kernel.admit_put_if_version(self.attempt, "cap-X", self.op(expected_version=1, value="later"))
        self.assertFalse(denied.allowed)

    def test_acceptance_pass_can_coexist_with_compliance_fail(self) -> None:
        actual = DishonestPrimitive.execute(self.target_db)
        mutant = DishonestPrimitive.diagnostic(actual)
        acceptance = self.kernel.accept(True)
        self.assertTrue(acceptance.passed)
        self.assertEqual(mutant.status, "FAIL")
        self.assertFalse(self.kernel.within_scope(mutant))

    def test_negative_control_dishonest_primitive_causes_real_a_plus_b_and_is_detected(self) -> None:
        actual = DishonestPrimitive.execute(self.target_db)
        self.assertEqual(actual, frozenset({"A", "B"}))
        self.assertEqual(Observer(self.target_db).observe("A").value, "mutant-A")
        self.assertEqual(Observer(self.target_db).observe("B").value, "mutant-B")
        diagnostic = DishonestPrimitive.diagnostic(actual)
        self.assertEqual(diagnostic.status, "FAIL")
        self.assertEqual(diagnostic.reason, "effect_model_unsound")
        self.assertEqual(diagnostic.possible_effects, frozenset({"A"}))
        self.assertEqual(diagnostic.actual_effects, frozenset({"A", "B"}))
        self.assertFalse(diagnostic.actual_effects.issubset(diagnostic.possible_effects))

    def test_control_and_target_are_separate_durable_stores(self) -> None:
        self.assertNotEqual(self.control_db.resolve(), self.target_db.resolve())
        self.assertTrue(self.control_db.exists())
        self.assertTrue(self.target_db.exists())


if __name__ == "__main__":
    unittest.main()
