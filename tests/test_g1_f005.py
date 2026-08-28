from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from agency_kernel import (
    ActionRequest,
    AuthorityGrant,
    AuthorityRoot,
    EffectContract,
    EffectIntent,
    Kernel,
    Principal,
)


class G1F005PrincipalProvenanceRegression(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.kernel = Kernel(Path(self.tempdir.name) / "ledger.sqlite", clock=lambda: 100)
        self.root = AuthorityRoot("root")
        self.alice = Principal("alice")
        self.mallory = Principal("mallory")
        self.intent = EffectIntent("intent.read", "bounded-reference-intent")
        self.contract = EffectContract("contract.read", self.intent.intent_id)
        self.kernel.add_authority_root(self.root)
        self.kernel.add_principal(self.alice)
        self.kernel.add_principal(self.mallory)
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

    def test_constructed_alice_principal_does_not_establish_authenticated_alice(self) -> None:
        forged_identity = Principal("alice")
        result = self.kernel.authorize(
            self.request,
            trusted_principal=forged_identity,
        )
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "missing_authentication_context")
        self.assertIsNone(result.authorization)
        self.assertEqual(self.kernel.snapshot()["action_authorizations"], [])

    def test_missing_authentication_context_denies_before_authorization(self) -> None:
        result = self.kernel.authorize(self.request)
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "missing_authentication_context")
        self.assertIsNone(result.authorization)
        self.assertEqual(self.kernel.snapshot()["action_authorizations"], [])

    def test_registered_fixture_identity_resolves_independently_of_request(self) -> None:
        hostile_request = ActionRequest(
            "request-2",
            self.intent.intent_id,
            self.contract.contract_id,
            declared_principal="mallory",
            untrusted_authority=Principal("mallory"),
        )
        result = self.kernel.authorize(
            hostile_request,
            trusted_principal=self.alice,
        )
        self.assertTrue(result.allowed)
        self.assertEqual(result.authorization.principal_id, "alice")


if __name__ == "__main__":
    unittest.main()
