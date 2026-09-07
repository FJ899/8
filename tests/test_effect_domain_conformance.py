from __future__ import annotations

import tempfile
import threading
import unittest
from pathlib import Path

from agency_kernel.g1 import (
    ActionRequest,
    AuthenticationContext,
    AuthorityGrant,
    AuthorityRoot,
    EffectContract,
    EffectIntent,
    Principal,
)
from agency_kernel.g2 import Capability
from agency_kernel.g3 import Kernel as G3Kernel, Observer, PutIfVersionOperation
from agency_kernel.g4 import (
    GitFile,
    GitObserver,
    GitTreeOperation,
    Kernel as G4Kernel,
    PROTECTED_REF_DEFAULT,
)


class G3Domain:
    name = "g3-versioned-store"
    expected_underapprox_reason = "effect_model_mismatch"

    def __init__(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        root = Path(self.tempdir.name)
        self.control_db = root / "control.db"
        self.target_db = root / "target.db"
        self.kernel = G3Kernel(self.control_db, self.target_db, clock=lambda: 100)
        self.root = AuthorityRoot("root")
        self.principal = Principal("alice")
        self.context = AuthenticationContext("session-alice")
        self.intent = EffectIntent("intent.put", "versioned-put")
        self.contract = EffectContract("contract.put", self.intent.intent_id)
        self.grant_id = "grant-alice"
        self.capability_id = "cap-X"

        self.kernel.add_authority_root(self.root)
        self.kernel.add_principal(self.principal)
        self.kernel.establish_authentication_context(self.context, self.principal)
        self.kernel.add_effect_intent(self.intent)
        self.kernel.add_effect_contract(self.contract)
        self.kernel.add_authority_grant(
            AuthorityGrant(
                self.grant_id,
                self.root.root_id,
                self.principal.principal_id,
                self.intent.intent_id,
            )
        )
        self.kernel.add_capability(Capability(self.capability_id, "X"))
        self.kernel.set_authorized_effect_envelope(
            self.contract.contract_id,
            self.kernel.possible_effects_for("X"),
        )
        auth = self.kernel.authorize(
            ActionRequest("request-1", self.intent.intent_id, self.contract.contract_id),
            authentication_context=self.context,
        )
        if not auth.allowed:
            raise AssertionError(auth.reason)
        start = self.kernel.start_attempt(auth.authorization)
        if not start.allowed:
            raise AssertionError(start.reason)
        self.attempt = start.attempt
        self.kernel.seed_resource("X", "initial", 0)
        self.observer = Observer(self.target_db)

    def close(self) -> None:
        self.tempdir.cleanup()

    def operation(self, value: str = "after", *, effects="auto", stale: bool = False):
        if effects == "auto":
            effects = self.kernel.possible_effects_for("X")
        return PutIfVersionOperation("X", 1 if stale else 0, value, effects)

    def underapproximated_operation(self):
        return self.operation(effects=frozenset({"MODIFY(X)"}))

    def admit(self, operation, *, capability_id: str | None = None, attempt=None):
        return self.kernel.admit_put_if_version(
            attempt or self.attempt,
            capability_id or self.capability_id,
            operation,
        )

    def execute(self, admission_id: str, *, crash_point: str | None = None):
        return self.kernel.execute_put_if_version_admission(admission_id, crash_point=crash_point)

    def observe(self, *, covered: bool = True, ambiguous: bool = False):
        return self.observer.observe("X", covered=covered, attribution_ambiguous=ambiguous)

    def did(self, admission, observation) -> bool:
        return self.kernel.did(admission, observation)

    def assess(self, admission, observation, *, supported=None):
        if supported is None:
            supported = self.kernel.possible_effects_for("X")
        return self.kernel.assess_compliance(
            admission,
            observation,
            supported_possible_effects=supported,
        )

    def within_scope(self, compliance) -> bool:
        return self.kernel.within_scope(compliance)

    def satisfied(self, observation, value: str) -> bool:
        return self.kernel.satisfied(observation, value)

    def invalidate_capability(self) -> None:
        self.kernel.set_capability_valid(self.capability_id, False)

    def mismatched_capability_id(self) -> str:
        self.kernel.add_capability(Capability("cap-Y", "Y"))
        return "cap-Y"

    def revoke_authority(self) -> None:
        self.kernel.set_grant_revoked(self.grant_id, True)

    def forged_attempt(self):
        return type(self.attempt)(
            self.attempt.attempt_id,
            self.attempt.authorization_id,
            "mallory",
            self.attempt.intent_id,
            self.attempt.contract_id,
        )

    def inject_unattributed(self, value: str) -> None:
        self.kernel.inject_unattributed_delta_for_test("X", value, 1)

    def stale_projection(self):
        admission = self.admit(self.operation(stale=True))
        if not admission.allowed:
            return False, admission.reason
        result = self.execute(admission.admission.admission_id)
        return result.occurred, result.reason

    def race_same_precondition(self):
        a1 = self.admit(self.operation("one"))
        a2 = self.admit(self.operation("two"))
        if not a1.allowed or not a2.allowed:
            raise AssertionError((a1.reason, a2.reason))
        barrier = threading.Barrier(3)
        results = []
        lock = threading.Lock()

        def run(admission_id: str) -> None:
            barrier.wait()
            result = self.execute(admission_id)
            with lock:
                results.append(result)

        t1 = threading.Thread(target=run, args=(a1.admission.admission_id,))
        t2 = threading.Thread(target=run, args=(a2.admission.admission_id,))
        t1.start()
        t2.start()
        barrier.wait()
        t1.join()
        t2.join()
        return results

    @property
    def crash_before_effect(self) -> str:
        return "before_mutation"

    @property
    def crash_after_effect(self) -> str:
        return "after_mutation_before_control_completion"

    def has_control_completion(self, admission_id: str) -> bool:
        return self.kernel.has_control_completion(admission_id)

    def bad_supported_effects(self):
        return frozenset({"MODIFY(X)"})

    def accept(self):
        return self.kernel.accept(True)

    def authorization_count(self) -> int:
        return len(self.kernel.snapshot()["action_authorizations"])

    def authorize_without_authentication(self):
        return self.kernel.authorize(
            ActionRequest("request-no-session", self.intent.intent_id, self.contract.contract_id)
        )


class G4Domain:
    name = "g4-sanitized-git"
    expected_underapprox_reason = "effect_model_underapproximation"

    def __init__(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        root = Path(self.tempdir.name)
        self.control_db = root / "control.db"
        self.repo_path = root / "target.git"
        self.kernel = G4Kernel(self.control_db, self.repo_path, clock=lambda: 100)
        self.root = AuthorityRoot("root")
        self.principal = Principal("alice")
        self.context = AuthenticationContext("session-alice")
        self.intent = EffectIntent("intent.git", "sanitized-git-transfer")
        self.contract = EffectContract("contract.git", self.intent.intent_id)
        self.grant_id = "grant-alice"
        self.capability_id = "cap-git"

        self.kernel.add_authority_root(self.root)
        self.kernel.add_principal(self.principal)
        self.kernel.establish_authentication_context(self.context, self.principal)
        self.kernel.add_effect_intent(self.intent)
        self.kernel.add_effect_contract(self.contract)
        self.kernel.add_authority_grant(
            AuthorityGrant(
                self.grant_id,
                self.root.root_id,
                self.principal.principal_id,
                self.intent.intent_id,
            )
        )
        self.kernel.add_capability(Capability(self.capability_id, PROTECTED_REF_DEFAULT))
        self.kernel.set_authorized_effect_envelope(
            self.contract.contract_id,
            frozenset(
                {
                    self.kernel.ref_effect(PROTECTED_REF_DEFAULT),
                    self.kernel.path_effect("A.txt"),
                }
            ),
        )
        auth = self.kernel.authorize(
            ActionRequest("request-1", self.intent.intent_id, self.contract.contract_id),
            authentication_context=self.context,
        )
        if not auth.allowed:
            raise AssertionError(auth.reason)
        start = self.kernel.start_attempt(auth.authorization)
        if not start.allowed:
            raise AssertionError(start.reason)
        self.attempt = start.attempt
        self.observer = GitObserver(self.kernel.git_repo)

    def close(self) -> None:
        self.tempdir.cleanup()

    def operation(self, value: str = "after", *, effects="auto", stale: bool = False):
        if stale:
            effects = frozenset(
                {
                    self.kernel.ref_effect(PROTECTED_REF_DEFAULT),
                    self.kernel.path_effect("A.txt"),
                }
            )
            return GitTreeOperation(
                PROTECTED_REF_DEFAULT,
                "0" * 40,
                (GitFile("A.txt", value),),
                effects,
            )
        expected = self.kernel.git_repo.rev_parse_ref()
        shell = GitTreeOperation(
            PROTECTED_REF_DEFAULT,
            expected,
            (GitFile("A.txt", value),),
            frozenset(),
        )
        if effects == "auto":
            effects = self.kernel.required_possible_effects(shell)
        return GitTreeOperation(
            PROTECTED_REF_DEFAULT,
            expected,
            shell.files,
            effects,
        )

    def underapproximated_operation(self):
        op = self.operation("after")
        return GitTreeOperation(
            op.protected_ref,
            op.expected_old_oid,
            op.files,
            frozenset({self.kernel.ref_effect(PROTECTED_REF_DEFAULT)}),
        )

    def admit(self, operation, *, capability_id: str | None = None, attempt=None):
        return self.kernel.admit_git_operation(
            attempt or self.attempt,
            capability_id or self.capability_id,
            operation,
        )

    def execute(self, admission_id: str, *, crash_point: str | None = None):
        return self.kernel.execute_git_admission(admission_id, crash_point=crash_point)

    def observe(self, *, covered: bool = True, ambiguous: bool = False):
        return self.observer.observe(covered=covered, attribution_ambiguous=ambiguous)

    def did(self, admission, observation) -> bool:
        return self.kernel.did(admission, observation)

    def assess(self, admission, observation, *, supported=None):
        if supported is None:
            supported = self.operation("unused").possible_effects
        return self.kernel.assess_compliance(
            admission,
            observation,
            supported_possible_effects=supported,
        )

    def within_scope(self, compliance) -> bool:
        return self.kernel.within_scope(compliance)

    def satisfied(self, observation, value: str) -> bool:
        return self.kernel.satisfied(observation, {"A.txt": value})

    def invalidate_capability(self) -> None:
        self.kernel.set_capability_valid(self.capability_id, False)

    def mismatched_capability_id(self) -> str:
        self.kernel.add_capability(Capability("cap-other", "refs/heads/other"))
        return "cap-other"

    def revoke_authority(self) -> None:
        self.kernel.set_grant_revoked(self.grant_id, True)

    def forged_attempt(self):
        return type(self.attempt)(
            self.attempt.attempt_id,
            self.attempt.authorization_id,
            "mallory",
            self.attempt.intent_id,
            self.attempt.contract_id,
        )

    def inject_unattributed(self, value: str) -> None:
        self.kernel.inject_unattributed_ref_for_test((GitFile("A.txt", value),))

    def stale_projection(self):
        admission = self.admit(self.operation(stale=True))
        if not admission.allowed:
            return False, admission.reason
        result = self.execute(admission.admission.admission_id)
        return result.occurred, result.reason

    def race_same_precondition(self):
        old = self.kernel.git_repo.rev_parse_ref()

        def build(value: str):
            shell = GitTreeOperation(
                PROTECTED_REF_DEFAULT,
                old,
                (GitFile("A.txt", value),),
                frozenset(),
            )
            effects = self.kernel.required_possible_effects(shell)
            return GitTreeOperation(PROTECTED_REF_DEFAULT, old, shell.files, effects)

        a1 = self.admit(build("one"))
        a2 = self.admit(build("two"))
        if not a1.allowed or not a2.allowed:
            raise AssertionError((a1.reason, a2.reason))
        barrier = threading.Barrier(3)
        results = []
        lock = threading.Lock()

        def run(admission_id: str) -> None:
            barrier.wait()
            result = self.execute(admission_id)
            with lock:
                results.append(result)

        t1 = threading.Thread(target=run, args=(a1.admission.admission_id,))
        t2 = threading.Thread(target=run, args=(a2.admission.admission_id,))
        t1.start()
        t2.start()
        barrier.wait()
        t1.join()
        t2.join()
        return results

    @property
    def crash_before_effect(self) -> str:
        return "before_ref_cas"

    @property
    def crash_after_effect(self) -> str:
        return "after_ref_cas_before_control_completion"

    def has_control_completion(self, admission_id: str) -> bool:
        return self.kernel.has_control_completion(admission_id)

    def bad_supported_effects(self):
        return frozenset({self.kernel.ref_effect(PROTECTED_REF_DEFAULT)})

    def accept(self):
        return self.kernel.accept(True)

    def authorization_count(self) -> int:
        return len(self.kernel.snapshot()["action_authorizations"])

    def authorize_without_authentication(self):
        return self.kernel.authorize(
            ActionRequest("request-no-session", self.intent.intent_id, self.contract.contract_id)
        )


DOMAIN_FACTORIES = (G3Domain, G4Domain)


class EffectDomainConformanceTests(unittest.TestCase):
    def domain(self, factory):
        domain = factory()
        self.addCleanup(domain.close)
        return domain

    def test_positive_effect_is_attributed_within_scope_and_satisfied(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d = self.domain(factory)
                op = d.operation("after")
                admission = d.admit(op)
                self.assertTrue(admission.allowed, admission.reason)
                result = d.execute(admission.admission.admission_id)
                self.assertTrue(result.occurred, result.reason)
                observation = d.observe()
                self.assertTrue(d.did(admission.admission, observation))
                compliance = d.assess(admission.admission, observation, supported=op.possible_effects)
                self.assertEqual(compliance.status, "PASS")
                self.assertTrue(d.within_scope(compliance))
                self.assertTrue(d.satisfied(observation, "after"))

    def test_unknown_effect_model_denies_before_effect(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d = self.domain(factory)
                result = d.admit(d.operation(effects=None))
                self.assertFalse(result.allowed)
                self.assertEqual(result.reason, "unknown_possible_effects")

    def test_effect_model_underapproximation_denies(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d = self.domain(factory)
                result = d.admit(d.underapproximated_operation())
                self.assertFalse(result.allowed)
                self.assertEqual(result.reason, d.expected_underapprox_reason)

    def test_invalid_capability_denies(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d = self.domain(factory)
                d.invalidate_capability()
                result = d.admit(d.operation())
                self.assertFalse(result.allowed)
                self.assertEqual(result.reason, "capability_invalid")

    def test_capability_resource_mismatch_denies(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d = self.domain(factory)
                result = d.admit(d.operation(), capability_id=d.mismatched_capability_id())
                self.assertFalse(result.allowed)
                self.assertEqual(result.reason, "capability_resource_mismatch")

    def test_authority_revocation_before_admission_denies(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d = self.domain(factory)
                d.revoke_authority()
                result = d.admit(d.operation())
                self.assertFalse(result.allowed)
                self.assertEqual(result.reason, "authority_revoked")

    def test_forged_attempt_denies(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d = self.domain(factory)
                result = d.admit(d.operation(), attempt=d.forged_attempt())
                self.assertFalse(result.allowed)
                self.assertEqual(result.reason, "forged_attempt")

    def test_exact_operation_binding_prevents_o1_to_o2_substitution(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d = self.domain(factory)
                op1 = d.operation("O1")
                admission = d.admit(op1)
                self.assertTrue(admission.allowed, admission.reason)
                op2 = d.operation("O2")
                self.assertNotEqual(op1.operation_digest, op2.operation_digest)
                result = d.execute(admission.admission.admission_id)
                self.assertTrue(result.occurred, result.reason)
                observation = d.observe()
                self.assertTrue(d.satisfied(observation, "O1"))
                self.assertFalse(d.satisfied(observation, "O2"))

    def test_admission_replay_denies_second_effect(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d = self.domain(factory)
                admission = d.admit(d.operation("once"))
                self.assertTrue(admission.allowed, admission.reason)
                first = d.execute(admission.admission.admission_id)
                self.assertTrue(first.occurred, first.reason)
                second = d.execute(admission.admission.admission_id)
                self.assertFalse(second.occurred)
                self.assertEqual(second.reason, "admission_consumed")

    def test_stale_mutable_precondition_prevents_effect(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d = self.domain(factory)
                occurred, reason = d.stale_projection()
                self.assertFalse(occurred)
                self.assertIn(reason, {"stale_version", "stale_ref"})

    def test_concurrent_same_precondition_allows_one_effect(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d = self.domain(factory)
                results = d.race_same_precondition()
                self.assertEqual(sum(1 for result in results if result.occurred), 1)
                self.assertEqual(
                    sum(1 for result in results if result.reason in {"stale_version", "stale_ref"}),
                    1,
                )

    def test_missing_observation_coverage_is_indeterminate(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d = self.domain(factory)
                op = d.operation("covered")
                admission = d.admit(op)
                self.assertTrue(admission.allowed, admission.reason)
                self.assertTrue(d.execute(admission.admission.admission_id).occurred)
                compliance = d.assess(
                    admission.admission,
                    d.observe(covered=False),
                    supported=op.possible_effects,
                )
                self.assertEqual((compliance.status, compliance.reason), ("INDETERMINATE", "missing_coverage"))

    def test_ambiguous_attribution_is_indeterminate(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d = self.domain(factory)
                op = d.operation("ambiguous")
                admission = d.admit(op)
                self.assertTrue(admission.allowed, admission.reason)
                self.assertTrue(d.execute(admission.admission.admission_id).occurred)
                compliance = d.assess(
                    admission.admission,
                    d.observe(ambiguous=True),
                    supported=op.possible_effects,
                )
                self.assertEqual((compliance.status, compliance.reason), ("INDETERMINATE", "ambiguous_attribution"))

    def test_unattributed_target_delta_does_not_become_did(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d = self.domain(factory)
                op = d.operation("authorized")
                admission = d.admit(op)
                self.assertTrue(admission.allowed, admission.reason)
                d.inject_unattributed("external")
                observation = d.observe()
                self.assertFalse(d.did(admission.admission, observation))
                compliance = d.assess(admission.admission, observation, supported=op.possible_effects)
                self.assertEqual((compliance.status, compliance.reason), ("INDETERMINATE", "unresolved_attribution"))

    def test_crash_before_effect_has_no_effect_and_no_blind_replay(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d = self.domain(factory)
                admission = d.admit(d.operation("crash-before"))
                self.assertTrue(admission.allowed, admission.reason)
                result = d.execute(
                    admission.admission.admission_id,
                    crash_point=d.crash_before_effect,
                )
                self.assertFalse(result.occurred)
                replay = d.execute(admission.admission.admission_id)
                self.assertFalse(replay.occurred)
                self.assertEqual(replay.reason, "admission_consumed")

    def test_crash_after_effect_before_control_completion_is_recoverable(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d = self.domain(factory)
                op = d.operation("committed")
                admission = d.admit(op)
                self.assertTrue(admission.allowed, admission.reason)
                result = d.execute(
                    admission.admission.admission_id,
                    crash_point=d.crash_after_effect,
                )
                self.assertTrue(result.occurred, result.reason)
                self.assertFalse(d.has_control_completion(admission.admission.admission_id))
                observation = d.observe()
                self.assertTrue(d.did(admission.admission, observation))
                compliance = d.assess(admission.admission, observation, supported=op.possible_effects)
                self.assertEqual(compliance.status, "PASS")
                replay = d.execute(admission.admission.admission_id)
                self.assertEqual(replay.reason, "admission_consumed")

    def test_satisfied_unattributed_outcome_does_not_create_authorization(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d = self.domain(factory)
                before = d.authorization_count()
                d.inject_unattributed("goal")
                observation = d.observe()
                self.assertTrue(d.satisfied(observation, "goal"))
                denied = d.authorize_without_authentication()
                self.assertFalse(denied.allowed)
                self.assertEqual(d.authorization_count(), before)

    def test_acceptance_cannot_repair_compliance_failure(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                d = self.domain(factory)
                op = d.operation("after")
                admission = d.admit(op)
                self.assertTrue(admission.allowed, admission.reason)
                self.assertTrue(d.execute(admission.admission.admission_id).occurred)
                observation = d.observe()
                compliance = d.assess(
                    admission.admission,
                    observation,
                    supported=d.bad_supported_effects(),
                )
                self.assertEqual(compliance.status, "FAIL")
                self.assertTrue(d.accept().passed)
                self.assertFalse(d.within_scope(compliance))


if __name__ == "__main__":
    unittest.main()
