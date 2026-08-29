from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from agency_kernel.g1 import ActionRequest, AuthenticationContext, AuthorityGrant, AuthorityRoot, EffectContract, EffectIntent, Principal
from agency_kernel.g2 import Capability
from agency_kernel.g4 import GitObserver, GitTreeOperation, Kernel, PROTECTED_REF_DEFAULT


class G4F005NoOpEffectRegression(unittest.TestCase):
    def test_identical_reachable_tree_is_not_admitted_as_modeled_effect(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            kernel = Kernel(root / "control.db", root / "target.git", clock=lambda: 100)
            alice = Principal("alice")
            context = AuthenticationContext("session-alice")
            intent = EffectIntent("intent.git", "sanitized-git-transfer")
            contract = EffectContract("contract.git", intent.intent_id)
            kernel.add_authority_root(AuthorityRoot("root"))
            kernel.add_principal(alice)
            kernel.establish_authentication_context(context, alice)
            kernel.add_effect_intent(intent)
            kernel.add_effect_contract(contract)
            kernel.add_authority_grant(AuthorityGrant("grant", "root", "alice", intent.intent_id))
            kernel.add_capability(Capability("cap", PROTECTED_REF_DEFAULT))
            kernel.set_authorized_effect_envelope(contract.contract_id, frozenset({kernel.ref_effect(PROTECTED_REF_DEFAULT)}))
            auth = kernel.authorize(ActionRequest("request", intent.intent_id, contract.contract_id), authentication_context=context)
            attempt = kernel.start_attempt(auth.authorization).attempt

            before = GitObserver(kernel.git_repo).observe()
            operation = GitTreeOperation(PROTECTED_REF_DEFAULT, before.commit_oid, tuple(), frozenset())
            self.assertEqual(kernel.required_possible_effects(operation), frozenset())
            admission = kernel.admit_git_operation(attempt, "cap", operation)
            self.assertFalse(admission.allowed)
            self.assertEqual(admission.reason, "no_target_change")

            after = GitObserver(kernel.git_repo).observe()
            self.assertEqual(after.commit_oid, before.commit_oid)
            self.assertEqual(after.tree_oid, before.tree_oid)
            self.assertEqual(after.entries, before.entries)
            self.assertEqual(kernel.snapshot()["operation_admissions"], [])


if __name__ == "__main__":
    unittest.main()
