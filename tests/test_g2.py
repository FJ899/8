from __future__ import annotations

import tempfile
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
from agency_kernel.g2 import Capability, Kernel, TechnicalOperation


class G2AdmissionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        root = Path(self.tempdir.name)
        self.kernel = Kernel(root / "ledger.sqlite", root / "target", clock=lambda: 100)
        self.root = AuthorityRoot("root")
        self.alice = Principal("alice")
        self.context = AuthenticationContext("session-alice")
        self.intent = EffectIntent("intent.write", "boundary-write")
        self.contract = EffectContract("contract.write", self.intent.intent_id)
        self.kernel.add_authority_root(self.root)
        self.kernel.add_principal(self.alice)
        self.kernel.establish_authentication_context(self.context, self.alice)
        self.kernel.add_effect_intent(self.intent)
        self.kernel.add_effect_contract(self.contract)
        self.kernel.add_authority_grant(
            AuthorityGrant("grant-alice", self.root.root_id, self.alice.principal_id, self.intent.intent_id)
        )
        self.kernel.add_capability(Capability("cap-X", "X"))
        self.kernel.set_authorized_effect_envelope(self.contract.contract_id, frozenset({"MODIFY(X)"}))
        request = ActionRequest("request-1", self.intent.intent_id, self.contract.contract_id)
        auth = self.kernel.authorize(request, authentication_context=self.context)
        self.assertTrue(auth.allowed)
        start = self.kernel.start_attempt(auth.authorization)
        self.assertTrue(start.allowed)
        self.attempt = start.attempt

    def op(self, resource: str = "X", value: str = "value", effects=None) -> TechnicalOperation:
        if effects is None:
            effects = frozenset({f"MODIFY({resource})"})
        return TechnicalOperation("boundary_mutation", resource, value, effects)

    def test_positive_exact_operation_admission_and_effect(self) -> None:
        operation = self.op(value="after")
        admission = self.kernel.admit_operation(self.attempt, "cap-X", operation)
        self.assertTrue(admission.allowed)
        self.assertEqual(admission.admission.operation_digest, operation.operation_digest)

        result = self.kernel.execute_admission(admission.admission.admission_id)
        self.assertTrue(result.allowed)
        self.assertEqual(result.operation_digest, operation.operation_digest)
        self.assertEqual((self.kernel.target_root / "X").read_text(encoding="utf-8"), "after")

    def test_unknown_possible_effects_denies(self) -> None:
        operation = TechnicalOperation("boundary_mutation", "X", "after", None)
        result = self.kernel.admit_operation(self.attempt, "cap-X", operation)
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "unknown_possible_effects")

    def test_effect_envelope_exceeded_denies(self) -> None:
        self.kernel.set_authorized_effect_envelope(self.contract.contract_id, frozenset())
        result = self.kernel.admit_operation(self.attempt, "cap-X", self.op(value="after"))
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "effect_envelope_exceeded")

    def test_malformed_effect_declaration_denies(self) -> None:
        operation = TechnicalOperation(
            "boundary_mutation",
            "X",
            "after",
            frozenset({"MODIFY(X)", "MODIFY(Y)"}),
        )
        result = self.kernel.admit_operation(self.attempt, "cap-X", operation)
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "nonconservative_boundary_effect_declaration")

    def test_capability_resource_mismatch_denies(self) -> None:
        self.kernel.add_capability(Capability("cap-Y", "Y"))
        result = self.kernel.admit_operation(self.attempt, "cap-Y", self.op())
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "capability_resource_mismatch")

    def test_invalid_capability_denies(self) -> None:
        self.kernel.set_capability_valid("cap-X", False)
        result = self.kernel.admit_operation(self.attempt, "cap-X", self.op())
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "capability_invalid")

    def test_revocation_before_admission_denies(self) -> None:
        self.kernel.set_grant_revoked("grant-alice", True)
        result = self.kernel.admit_operation(self.attempt, "cap-X", self.op())
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "authority_revoked")

    def test_forged_attempt_denies(self) -> None:
        forged = type(self.attempt)(
            self.attempt.attempt_id,
            self.attempt.authorization_id,
            "mallory",
            self.attempt.intent_id,
            self.attempt.contract_id,
        )
        result = self.kernel.admit_operation(forged, "cap-X", self.op())
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "forged_attempt")

    def test_execution_accepts_only_admission_id_not_replacement_payload(self) -> None:
        operation = self.op(value="O1")
        admission = self.kernel.admit_operation(self.attempt, "cap-X", operation)
        self.assertTrue(admission.allowed)
        replacement = self.op(value="O2")
        self.assertNotEqual(replacement.operation_digest, admission.admission.operation_digest)

        result = self.kernel.execute_admission(admission.admission.admission_id)
        self.assertTrue(result.allowed)
        self.assertEqual((self.kernel.target_root / "X").read_text(encoding="utf-8"), "O1")

    def test_reusing_admission_cannot_select_different_operation(self) -> None:
        operation = self.op(value="O1")
        admission = self.kernel.admit_operation(self.attempt, "cap-X", operation)
        self.assertTrue(admission.allowed)
        first = self.kernel.execute_admission(admission.admission.admission_id)
        second = self.kernel.execute_admission(admission.admission.admission_id)
        self.assertTrue(first.allowed)
        self.assertTrue(second.allowed)
        self.assertEqual(first.operation_digest, second.operation_digest)
        self.assertEqual((self.kernel.target_root / "X").read_text(encoding="utf-8"), "O1")


if __name__ == "__main__":
    unittest.main()
