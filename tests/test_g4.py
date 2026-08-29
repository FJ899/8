from __future__ import annotations

import tempfile
import threading
import unittest
from pathlib import Path

from agency_kernel.g1 import ActionRequest, AuthenticationContext, AuthorityGrant, AuthorityRoot, EffectContract, EffectIntent, Principal
from agency_kernel.g2 import Capability
from agency_kernel.g4 import GitFile, GitObserver, GitTreeOperation, Kernel, PROTECTED_REF_DEFAULT


class G4SanitizedGitTransferTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        root = Path(self.tempdir.name)
        self.control_db = root / "control.db"
        self.repo_path = root / "target.git"
        self.kernel = Kernel(self.control_db, self.repo_path, clock=lambda: 100)
        self.root = AuthorityRoot("root")
        self.alice = Principal("alice")
        self.context = AuthenticationContext("session-alice")
        self.intent = EffectIntent("intent.git", "sanitized-git-transfer")
        self.contract = EffectContract("contract.git", self.intent.intent_id)
        self.kernel.add_authority_root(self.root)
        self.kernel.add_principal(self.alice)
        self.kernel.establish_authentication_context(self.context, self.alice)
        self.kernel.add_effect_intent(self.intent)
        self.kernel.add_effect_contract(self.contract)
        self.kernel.add_authority_grant(AuthorityGrant("grant-alice", "root", "alice", self.intent.intent_id))
        self.kernel.add_capability(Capability("cap-git", PROTECTED_REF_DEFAULT))
        self.kernel.set_authorized_effect_envelope(
            self.contract.contract_id,
            frozenset({
                self.kernel.ref_effect(PROTECTED_REF_DEFAULT),
                self.kernel.path_effect("A.txt"),
                self.kernel.path_effect("B.txt"),
                self.kernel.path_effect("goal.txt"),
            }),
        )
        auth = self.kernel.authorize(ActionRequest("request-1", self.intent.intent_id, self.contract.contract_id), authentication_context=self.context)
        self.assertTrue(auth.allowed)
        start = self.kernel.start_attempt(auth.authorization)
        self.assertTrue(start.allowed)
        self.attempt = start.attempt
        self.observer = GitObserver(self.kernel.git_repo)

    def operation(self, files: dict[str, str], *, expected: str | None = None, effects="auto") -> GitTreeOperation:
        expected = expected or self.kernel.git_repo.rev_parse_ref()
        items = tuple(GitFile(path, value) for path, value in sorted(files.items()))
        shell = GitTreeOperation(PROTECTED_REF_DEFAULT, expected, items, frozenset())
        actual_effects = self.kernel.required_possible_effects(shell)
        if effects == "auto":
            effects = actual_effects
        return GitTreeOperation(PROTECTED_REF_DEFAULT, expected, items, effects)

    def admit(self, op: GitTreeOperation):
        result = self.kernel.admit_git_operation(self.attempt, "cap-git", op)
        self.assertTrue(result.allowed, result.reason)
        return result.admission

    def test_positive_transfer_is_attributed_within_scope_and_satisfied(self) -> None:
        op = self.operation({"A.txt": "one"})
        admission = self.admit(op)
        result = self.kernel.execute_git_admission(admission.admission_id)
        self.assertTrue(result.occurred)
        obs = self.observer.observe()
        self.assertTrue(self.kernel.did(admission, obs))
        comp = self.kernel.assess_compliance(admission, obs, supported_possible_effects=op.possible_effects)
        self.assertEqual(comp.status, "PASS")
        self.assertTrue(self.kernel.within_scope(comp))
        self.assertTrue(self.kernel.satisfied(obs, {"A.txt": "one"}))
        self.assertTrue(comp.actual_effects.issubset(op.possible_effects))

    def test_stale_expected_ref_denies_before_effect(self) -> None:
        stale = "0" * 40
        op = GitTreeOperation(PROTECTED_REF_DEFAULT, stale, (GitFile("A.txt", "x"),), frozenset({self.kernel.ref_effect(PROTECTED_REF_DEFAULT), self.kernel.path_effect("A.txt")}))
        result = self.kernel.admit_git_operation(self.attempt, "cap-git", op)
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "stale_ref")

    def test_concurrent_same_expected_ref_allows_one_cas(self) -> None:
        old = self.kernel.git_repo.rev_parse_ref()
        a1 = self.admit(self.operation({"A.txt": "one"}, expected=old))
        a2 = self.admit(self.operation({"A.txt": "two"}, expected=old))
        barrier = threading.Barrier(3)
        results = []
        lock = threading.Lock()
        def run(admission_id):
            barrier.wait()
            r = self.kernel.execute_git_admission(admission_id)
            with lock:
                results.append(r)
        t1 = threading.Thread(target=run, args=(a1.admission_id,))
        t2 = threading.Thread(target=run, args=(a2.admission_id,))
        t1.start(); t2.start(); barrier.wait(); t1.join(); t2.join()
        self.assertEqual(sum(1 for r in results if r.occurred), 1)
        self.assertEqual(sum(1 for r in results if r.reason == "stale_ref"), 1)

    def test_unknown_possible_effects_denies(self) -> None:
        old = self.kernel.git_repo.rev_parse_ref()
        op = GitTreeOperation(PROTECTED_REF_DEFAULT, old, (GitFile("A.txt", "x"),), None)
        result = self.kernel.admit_git_operation(self.attempt, "cap-git", op)
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "unknown_possible_effects")

    def test_declared_effects_exceed_authorized_envelope_denies(self) -> None:
        op = self.operation({"A.txt": "x"})
        over = GitTreeOperation(op.protected_ref, op.expected_old_oid, op.files, op.possible_effects | frozenset({self.kernel.path_effect("secret.txt")}))
        result = self.kernel.admit_git_operation(self.attempt, "cap-git", over)
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "effect_envelope_exceeded")

    def test_supported_operation_underapproximation_denies(self) -> None:
        op = self.operation({"A.txt": "x"})
        under = GitTreeOperation(op.protected_ref, op.expected_old_oid, op.files, frozenset({self.kernel.ref_effect(PROTECTED_REF_DEFAULT)}))
        result = self.kernel.admit_git_operation(self.attempt, "cap-git", under)
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "effect_model_underapproximation")

    def test_missing_coverage_is_indeterminate(self) -> None:
        op = self.operation({"A.txt": "x"})
        admission = self.admit(op)
        self.assertTrue(self.kernel.execute_git_admission(admission.admission_id).occurred)
        comp = self.kernel.assess_compliance(admission, self.observer.observe(covered=False), supported_possible_effects=op.possible_effects)
        self.assertEqual((comp.status, comp.reason), ("INDETERMINATE", "missing_coverage"))

    def test_ambiguous_attribution_is_indeterminate(self) -> None:
        op = self.operation({"A.txt": "x"})
        admission = self.admit(op)
        self.assertTrue(self.kernel.execute_git_admission(admission.admission_id).occurred)
        comp = self.kernel.assess_compliance(admission, self.observer.observe(attribution_ambiguous=True), supported_possible_effects=op.possible_effects)
        self.assertEqual((comp.status, comp.reason), ("INDETERMINATE", "ambiguous_attribution"))

    def test_crash_before_ref_cas_has_no_effect_and_no_blind_replay(self) -> None:
        before = self.kernel.git_repo.rev_parse_ref()
        admission = self.admit(self.operation({"A.txt": "x"}, expected=before))
        result = self.kernel.execute_git_admission(admission.admission_id, crash_point="before_ref_cas")
        self.assertFalse(result.occurred)
        self.assertEqual(self.kernel.git_repo.rev_parse_ref(), before)
        replay = self.kernel.execute_git_admission(admission.admission_id)
        self.assertEqual(replay.reason, "admission_consumed")

    def test_crash_after_ref_cas_recovers_from_admission_plus_git_correlation(self) -> None:
        op = self.operation({"A.txt": "x"})
        admission = self.admit(op)
        result = self.kernel.execute_git_admission(admission.admission_id, crash_point="after_ref_cas_before_control_completion")
        self.assertTrue(result.occurred)
        self.assertFalse(self.kernel.has_control_completion(admission.admission_id))
        obs = self.observer.observe()
        self.assertTrue(self.kernel.did(admission, obs))
        self.assertEqual(self.kernel.assess_compliance(admission, obs, supported_possible_effects=op.possible_effects).status, "PASS")
        self.assertEqual(self.kernel.execute_git_admission(admission.admission_id).reason, "admission_consumed")

    def test_exact_operation_binding_o1_cannot_execute_o2(self) -> None:
        op1 = self.operation({"A.txt": "O1"})
        admission = self.admit(op1)
        _op2 = self.operation({"B.txt": "O2"}, expected=op1.expected_old_oid)
        self.assertTrue(self.kernel.execute_git_admission(admission.admission_id).occurred)
        self.assertEqual(dict(self.observer.observe().files), {"A.txt": "O1"})

    def test_reuse_of_valid_admission_denies_second_transition(self) -> None:
        admission = self.admit(self.operation({"A.txt": "one"}))
        self.assertTrue(self.kernel.execute_git_admission(admission.admission_id).occurred)
        replay = self.kernel.execute_git_admission(admission.admission_id)
        self.assertFalse(replay.occurred)
        self.assertEqual(replay.reason, "admission_consumed")

    def test_observed_git_delta_without_provenance_is_not_did(self) -> None:
        op = self.operation({"A.txt": "authorized"})
        admission = self.admit(op)
        self.assertTrue(self.kernel.execute_git_admission(admission.admission_id).occurred)
        self.kernel.inject_unattributed_ref_for_test((GitFile("A.txt", "unauthorized"),))
        obs = self.observer.observe()
        self.assertFalse(self.kernel.did(admission, obs))
        comp = self.kernel.assess_compliance(admission, obs, supported_possible_effects=op.possible_effects)
        self.assertEqual((comp.status, comp.reason), ("INDETERMINATE", "unresolved_attribution"))

    def test_successful_unauthorized_outcome_does_not_retroactively_authorize(self) -> None:
        before_count = len(self.kernel.snapshot()["action_authorizations"])
        self.kernel.inject_unattributed_ref_for_test((GitFile("goal.txt", "goal"),))
        obs = self.observer.observe()
        self.assertTrue(self.kernel.satisfied(obs, {"goal.txt": "goal"}))
        self.assertEqual(len(self.kernel.snapshot()["action_authorizations"]), before_count)
        denied = self.kernel.authorize(ActionRequest("request-no-session", self.intent.intent_id, self.contract.contract_id))
        self.assertFalse(denied.allowed)

    def test_git_capability_does_not_create_may(self) -> None:
        denied = self.kernel.authorize(ActionRequest("request-can-not-may", self.intent.intent_id, self.contract.contract_id))
        self.assertFalse(denied.allowed)
        self.assertEqual(denied.reason, "missing_authentication_context")

    def test_acceptance_pass_does_not_repair_compliance_fail(self) -> None:
        op = self.operation({"A.txt": "x"})
        admission = self.admit(op)
        self.assertTrue(self.kernel.execute_git_admission(admission.admission_id).occurred)
        obs = self.observer.observe()
        comp = self.kernel.assess_compliance(admission, obs, supported_possible_effects=frozenset({self.kernel.ref_effect(PROTECTED_REF_DEFAULT)}))
        self.assertEqual(comp.status, "FAIL")
        acceptance = self.kernel.accept(True)
        self.assertTrue(acceptance.passed)
        self.assertFalse(self.kernel.within_scope(comp))

    def test_controlled_git_config_and_no_alternates(self) -> None:
        hooks = self.kernel.git_repo.git("config", "--get", "core.hooksPath")
        self.assertEqual(Path(hooks), self.kernel.git_repo.hooks_dir)
        self.assertFalse((self.repo_path / "objects" / "info" / "alternates").exists())


if __name__ == "__main__":
    unittest.main()
