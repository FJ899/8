from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path

from agency_kernel.g1 import ActionRequest, AuthenticationContext, AuthorityGrant, AuthorityRoot, EffectContract, EffectIntent, Principal
from agency_kernel.g2 import Capability
from agency_kernel.g4 import GitFile, GitObserver, GitTreeOperation, Kernel, PROTECTED_REF_DEFAULT


class G4F003TreeCoverageRegression(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        root = Path(self.tempdir.name)
        self.kernel = Kernel(root / "control.db", root / "target.git", clock=lambda: 100)
        alice = Principal("alice")
        context = AuthenticationContext("session-alice")
        intent = EffectIntent("intent.git", "sanitized-git-transfer")
        contract = EffectContract("contract.git", intent.intent_id)
        self.kernel.add_authority_root(AuthorityRoot("root"))
        self.kernel.add_principal(alice)
        self.kernel.establish_authentication_context(context, alice)
        self.kernel.add_effect_intent(intent)
        self.kernel.add_effect_contract(contract)
        self.kernel.add_authority_grant(AuthorityGrant("grant", "root", "alice", intent.intent_id))
        self.kernel.add_capability(Capability("cap", PROTECTED_REF_DEFAULT))
        self.kernel.set_authorized_effect_envelope(contract.contract_id, frozenset({self.kernel.ref_effect(PROTECTED_REF_DEFAULT), self.kernel.path_effect("A.txt")}))
        auth = self.kernel.authorize(ActionRequest("request", intent.intent_id, contract.contract_id), authentication_context=context)
        self.attempt = self.kernel.start_attempt(auth.authorization).attempt
        self.observer = GitObserver(self.kernel.git_repo)

    def _legal_a(self, content: str = "same"):
        old = self.kernel.git_repo.rev_parse_ref()
        files = (GitFile("A.txt", content),)
        shell = GitTreeOperation(PROTECTED_REF_DEFAULT, old, files, frozenset())
        op = GitTreeOperation(PROTECTED_REF_DEFAULT, old, files, self.kernel.required_possible_effects(shell))
        adm = self.kernel.admit_git_operation(self.attempt, "cap", op)
        self.assertTrue(adm.allowed)
        self.assertTrue(self.kernel.execute_git_admission(adm.admission.admission_id).occurred)
        return adm.admission

    def test_mode_only_tree_change_is_observed_and_not_satisfied(self) -> None:
        admission = self._legal_a("same")
        old = self.kernel.git_repo.rev_parse_ref()
        entry = self.kernel.git_repo.tree_entries(old)[0]
        _mode, obj_type, oid, path = entry
        self.assertEqual((obj_type, path), ("blob", "A.txt"))
        tree = self.kernel.git_repo.git("mktree", input_text=f"100755 blob {oid}\tA.txt\n")
        commit = self.kernel.git_repo.git("commit-tree", tree, "-p", old, input_text="unattributed executable-bit change\n")
        self.assertTrue(self.kernel.git_repo.cas_update(commit, old))
        obs = self.observer.observe()
        self.assertEqual(obs.entries[0][0], "100755")
        self.assertEqual(dict(obs.files), {"A.txt": "same"})
        self.assertFalse(self.kernel.satisfied(obs, {"A.txt": "same"}))
        self.assertFalse(self.kernel.did(admission, obs))

    def test_binary_blob_target_state_is_observed_without_decode_failure(self) -> None:
        old = self.kernel.git_repo.rev_parse_ref()
        cp = subprocess.run(
            ["git", "--git-dir", str(self.kernel.git_repo.repo), "hash-object", "-w", "--stdin"],
            input=b"\xff\x00binary\n",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=self.kernel.git_repo._env(),
            check=True,
        )
        oid = cp.stdout.decode("ascii").strip()
        tree = self.kernel.git_repo.git("mktree", input_text=f"100644 blob {oid}\tA.txt\n")
        commit = self.kernel.git_repo.git("commit-tree", tree, "-p", old, input_text="unattributed binary target\n")
        self.assertTrue(self.kernel.git_repo.cas_update(commit, old))
        obs = self.observer.observe()
        self.assertEqual(obs.entries, (("100644", "blob", oid, "A.txt"),))
        observed = dict(obs.files)["A.txt"]
        self.assertEqual(observed.encode("utf-8", "surrogateescape"), b"\xff\x00binary\n")


if __name__ == "__main__":
    unittest.main()
