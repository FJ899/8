from __future__ import annotations

import gc
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


class G1F011PrincipalIdentityReuseRegression(unittest.TestCase):
    def test_reused_principal_object_id_cannot_recover_authentication_provenance(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            kernel = Kernel(Path(tempdir) / "ledger.sqlite", clock=lambda: 100)
            root = AuthorityRoot("root")
            original = Principal("alice")
            context = AuthenticationContext("fixture-session-alice")
            intent = EffectIntent("intent.read", "bounded-reference-intent")
            contract = EffectContract("contract.read", intent.intent_id)
            kernel.add_authority_root(root)
            kernel.add_principal(original)
            kernel.establish_authentication_context(context, original)
            kernel.add_effect_intent(intent)
            kernel.add_effect_contract(contract)
            kernel.add_authority_grant(
                AuthorityGrant(
                    "grant-alice",
                    root.root_id,
                    original.principal_id,
                    intent.intent_id,
                )
            )
            request = ActionRequest(
                "request-1",
                intent.intent_id,
                contract.contract_id,
                declared_principal="alice",
            )

            former_id = id(original)
            del original
            gc.collect()

            colliding = None
            for _ in range(1_000_000):
                candidate = Principal("alice")
                if id(candidate) == former_id:
                    colliding = candidate
                    break
                del candidate
            self.assertIsNotNone(
                colliding,
                "CPython did not reuse the released Principal object ID within the bounded regression loop",
            )
            self.assertEqual(id(colliding), former_id)

            may = kernel.may(colliding, request)
            self.assertFalse(may.allowed)
            self.assertEqual(may.reason, "missing_authentication_context")

            denied = kernel.authorize(request)
            self.assertFalse(denied.allowed)
            self.assertEqual(denied.reason, "missing_authentication_context")
            self.assertIsNone(denied.authorization)
            snapshot = kernel.snapshot()
            self.assertEqual(snapshot["action_authorizations"], [])
            self.assertEqual(snapshot["authorization_consumed"], [])
            self.assertEqual(snapshot["action_attempts"], [])
            self.assertEqual(snapshot["attempt_started"], [])

            genuine_may = kernel.may(context, request)
            self.assertTrue(genuine_may.allowed)
            self.assertEqual(genuine_may.reason, "may")
            genuine = kernel.authorize(request, authentication_context=context)
            self.assertTrue(genuine.allowed)
            self.assertIsNotNone(genuine.authorization)
            self.assertEqual(genuine.authorization.principal_id, "alice")


if __name__ == "__main__":
    unittest.main()
