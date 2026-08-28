from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from agency_kernel import (
    ActionRequest,
    AuthenticationContext,
    AuthorityGrant,
    AuthorityRoot,
    EffectContract,
    EffectIntent,
    Kernel,
    Principal,
)


class G1F006AuthenticationSeparationRegression(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.kernel = Kernel(Path(self.tempdir.name) / "ledger.sqlite", clock=lambda: 100)
        self.root = AuthorityRoot("root")
        self.alice = Principal("alice")
        self.intent = EffectIntent("intent.read", "bounded-reference-intent")
        self.contract = EffectContract("contract.read", self.intent.intent_id)
        self.kernel.add_authority_root(self.root)
        self.kernel.add_principal(self.alice)
        self.kernel.add_effect_intent(self.intent)
        self.kernel.add_effect_contract(self.contract)
        self.kernel.add_authority_grant(
            AuthorityGrant(
                "grant-alice",
                self.root.root_id,
                self.alice.principal_id,
                self.intent.intent_id,
            )
        )
        self.request = ActionRequest(
            "request-1",
            self.intent.intent_id,
            self.contract.contract_id,
            declared_principal="alice",
        )

    def test_registration_and_grant_without_session_denies(self) -> None:
        may = self.kernel.may(self.alice, self.request)
        self.assertFalse(may.allowed)
        self.assertEqual(may.reason, "missing_authentication_context")

        result = self.kernel.authorize(self.request, trusted_principal=self.alice)
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "missing_authentication_context")
        self.assertIsNone(result.authorization)
        self.assertEqual(self.kernel.snapshot()["action_authorizations"], [])

    def test_independent_established_context_allows_ordinary_may(self) -> None:
        context = AuthenticationContext("fixture-session-alice")
        self.kernel.establish_authentication_context(context, self.alice)

        may = self.kernel.may(context, self.request)
        self.assertTrue(may.allowed)
        self.assertEqual(may.reason, "may")

        result = self.kernel.authorize(self.request, authentication_context=context)
        self.assertTrue(result.allowed)
        self.assertEqual(result.authorization.principal_id, "alice")

    def test_caller_created_context_with_matching_id_is_not_trusted(self) -> None:
        context = AuthenticationContext("fixture-session-alice")
        self.kernel.establish_authentication_context(context, self.alice)
        forged = AuthenticationContext("fixture-session-alice")

        result = self.kernel.authorize(self.request, authentication_context=forged)
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "missing_authentication_context")
        self.assertIsNone(result.authorization)


if __name__ == "__main__":
    unittest.main()
