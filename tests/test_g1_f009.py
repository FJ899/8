from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from agency_kernel.g1 import (
    ActionRequest, AuthenticationContext, AuthorityGrant, AuthorityRoot,
    EffectContract, EffectIntent, Kernel, Principal,
)


class G1F009DirectImportContextProvenanceRegression(unittest.TestCase):
    def test_equal_copied_context_does_not_authenticate(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            kernel = Kernel(Path(tempdir) / "ledger.sqlite", clock=lambda: 100)
            root = AuthorityRoot("root")
            alice = Principal("alice")
            context = AuthenticationContext("fixture-session-alice")
            intent = EffectIntent("intent.read", "bounded-reference-intent")
            contract = EffectContract("contract.read", intent.intent_id)
            kernel.add_authority_root(root)
            kernel.add_principal(alice)
            kernel.establish_authentication_context(context, alice)
            kernel.add_effect_intent(intent)
            kernel.add_effect_contract(contract)
            kernel.add_authority_grant(AuthorityGrant("grant-alice", root.root_id, alice.principal_id, intent.intent_id))
            request = ActionRequest("request-1", intent.intent_id, contract.contract_id)

            forged = AuthenticationContext(context.context_id)
            denied = kernel.authorize(request, authentication_context=forged)
            self.assertFalse(denied.allowed)
            self.assertIsNone(denied.authorization)
            self.assertEqual(kernel.snapshot()["action_authorizations"], [])

            may = kernel.may(context, request)
            self.assertTrue(may.allowed)
            self.assertEqual(may.reason, "may")
            allowed = kernel.authorize(request, authentication_context=context)
            self.assertTrue(allowed.allowed)
            self.assertIsNotNone(allowed.authorization)
            self.assertEqual(allowed.authorization.principal_id, "alice")


if __name__ == "__main__":
    unittest.main()
