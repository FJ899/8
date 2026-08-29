from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from agency_kernel.g1 import ActionRequest, AuthenticationContext, AuthorityGrant, AuthorityRoot, EffectContract, EffectIntent, Principal
from agency_kernel.g2 import Capability
from agency_kernel.g4 import GitFile, GitObserver, GitTreeOperation, Kernel, PROTECTED_REF_DEFAULT


class G4F001F002RegressionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        root = Path(self.tempdir.name)
        self.kernel = Kernel(root / "control.db", root / "target.git", clock=lambda: 100)
        self.principal = Principal("alice")
        self.context = AuthenticationContext("session-alice")
        self.intent = EffectIntent("intent.git", "sanitized-git-transfer")
        self.contract = EffectContract("contract.git", self.intent.intent_id)
        self.kernel.add_authority_root(AuthorityRoot("root"))
        self.kernel.add_principal(self.principal)
        self.kernel.establish_authentication_context(self.context, self.principal)
        self.kernel.add_effect_intent(self.intent)
        self.kernel.add_effect_contract(self.contract)
        self.kernel.add_authority_grant(AuthorityGrant("grant", "root", "alice", self.intent.intent_id))
        self.kernel.add_capability(Capability("cap", PROTECTED_REF_DEFAULT))
        self.kernel.set_authorized_effect_envelope(
            self.contract.contract_id,
            frozenset({
                self.kernel.ref_effect(PROTECTED_REF_DEFAULT),
                self.kernel.path_effect("A.txt"),
                self.kernel.path_effect("goal.txt"),
                self.kernel.path_effect("hidden.txt"),
            }),
        )
        auth = self.kernel.authorize(ActionRequest("request", self.intent.intent_id, self.contract.contract_id), authentication_context=self.context)
        start = self.kernel.start_attempt(auth.authorization)
        self.attempt = start.attempt
        self.observer = GitObserver(self.kernel.git_repo)

    def operation(self, files: dict[str, str]) -> GitTreeOperation:
        expected = self.kernel.git_repo.rev_parse_ref()
        items = tuple(GitFile(p, v) for p, v in sorted(files.items()))
        shell = GitTreeOperation(PROTECTED_REF_DEFAULT, expected, items, frozenset())
        effects = self.kernel.required_possible_effects(shell)
        return GitTreeOperation(PROTECTED_REF_DEFAULT, expected, items, effects)

    def test_exact_blob_observation_preserves_whitespace_and_final_newline(self) -> None:
        expected = "  leading and trailing  \n"
        op = self.operation({"A.txt": expected})
        admission = self.kernel.admit_git_operation(self.attempt, "cap", op)
        self.assertTrue(admission.allowed, admission.reason)
        self.assertTrue(self.kernel.execute_git_admission(admission.admission.admission_id).occurred)
        obs = self.observer.observe()
        self.assertEqual(dict(obs.files)["A.txt"], expected)
        self.assertTrue(self.kernel.satisfied(obs, {"A.txt": expected}))

    def test_complete_observer_sees_additional_hidden_protected_tree_path(self) -> None:
        op = self.operation({"A.txt": "authorized"})
        admission = self.kernel.admit_git_operation(self.attempt, "cap", op)
        self.assertTrue(admission.allowed)
        self.assertTrue(self.kernel.execute_git_admission(admission.admission.admission_id).occurred)
        self.kernel.inject_unattributed_ref_for_test((GitFile("A.txt", "authorized"), GitFile("hidden.txt", "hidden")))
        obs = self.observer.observe()
        self.assertEqual(dict(obs.files), {"A.txt": "authorized", "hidden.txt": "hidden"})
        self.assertFalse(self.kernel.did(admission.admission, obs))
        comp = self.kernel.assess_compliance(admission.admission, obs, supported_possible_effects=op.possible_effects)
        self.assertEqual((comp.status, comp.reason), ("INDETERMINATE", "unresolved_attribution"))

    def test_actual_unauthorized_path_proposal_is_denied_by_effect_envelope(self) -> None:
        expected = self.kernel.git_repo.rev_parse_ref()
        items = (GitFile("secret.txt", "forbidden"),)
        shell = GitTreeOperation(PROTECTED_REF_DEFAULT, expected, items, frozenset())
        required = self.kernel.required_possible_effects(shell)
        self.assertIn(self.kernel.path_effect("secret.txt"), required)
        op = GitTreeOperation(PROTECTED_REF_DEFAULT, expected, items, required)
        before = self.kernel.git_repo.rev_parse_ref()
        result = self.kernel.admit_git_operation(self.attempt, "cap", op)
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "effect_envelope_exceeded")
        self.assertEqual(self.kernel.git_repo.rev_parse_ref(), before)

    def test_successful_unauthorized_outcome_and_acceptance_do_not_repair_history(self) -> None:
        legal = self.operation({"A.txt": "legal"})
        admission = self.kernel.admit_git_operation(self.attempt, "cap", legal)
        self.assertTrue(admission.allowed)
        self.assertTrue(self.kernel.execute_git_admission(admission.admission.admission_id).occurred)
        before_auth = len(self.kernel.snapshot()["action_authorizations"])

        self.kernel.inject_unattributed_ref_for_test((GitFile("goal.txt", "goal"),))
        obs = self.observer.observe()
        self.assertTrue(self.kernel.satisfied(obs, {"goal.txt": "goal"}))
        comp = self.kernel.assess_compliance(admission.admission, obs, supported_possible_effects=legal.possible_effects)
        self.assertEqual((comp.status, comp.reason), ("INDETERMINATE", "unresolved_attribution"))
        acceptance = self.kernel.accept(True)
        self.assertTrue(acceptance.passed)
        self.assertFalse(self.kernel.within_scope(comp))
        self.assertEqual(len(self.kernel.snapshot()["action_authorizations"]), before_auth)

    def test_broker_git_environment_scrubs_config_injection_variables(self) -> None:
        old_count = os.environ.get("GIT_CONFIG_COUNT")
        old_key = os.environ.get("GIT_CONFIG_KEY_0")
        old_value = os.environ.get("GIT_CONFIG_VALUE_0")
        try:
            os.environ["GIT_CONFIG_COUNT"] = "1"
            os.environ["GIT_CONFIG_KEY_0"] = "core.hooksPath"
            os.environ["GIT_CONFIG_VALUE_0"] = "/tmp/attacker-hooks"
            hooks = self.kernel.git_repo.git("config", "--get", "core.hooksPath")
            self.assertEqual(Path(hooks), self.kernel.git_repo.hooks_dir)
        finally:
            for key, value in (("GIT_CONFIG_COUNT", old_count), ("GIT_CONFIG_KEY_0", old_key), ("GIT_CONFIG_VALUE_0", old_value)):
                if value is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = value


if __name__ == "__main__":
    unittest.main()
