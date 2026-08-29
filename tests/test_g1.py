from __future__ import annotations

import tempfile
import threading
import unittest
from dataclasses import replace
from pathlib import Path

from agency_kernel import (
    ActionAuthorization,
    ActionRequest,
    AuthenticationContext,
    AuthorityGrant,
    AuthorityRoot,
    EffectContract,
    EffectIntent,
    Kernel,
    Principal,
)


class ManualClock:
    def __init__(self, value: int = 100):
        self.value = value

    def __call__(self) -> int:
        return self.value


class G1SemanticIntegrityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.db_path = Path(self.tempdir.name) / "ledger.sqlite"
        self.clock = ManualClock(100)
        self.kernel = Kernel(self.db_path, clock=self.clock)
        self.root = AuthorityRoot("root")
        self.alice = Principal("alice")
        self.mallory = Principal("mallory")
        self.alice_context = AuthenticationContext("fixture-session-alice")
        self.mallory_context = AuthenticationContext("fixture-session-mallory")
        self.intent = EffectIntent("intent.read", "bounded-reference-intent")
        self.contract = EffectContract("contract.read", self.intent.intent_id)
        self.kernel.add_authority_root(self.root)
        self.kernel.add_principal(self.alice)
        self.kernel.add_principal(self.mallory)
        self.kernel.establish_authentication_context(self.alice_context, self.alice)
        self.kernel.establish_authentication_context(self.mallory_context, self.mallory)
        self.kernel.add_effect_intent(self.intent)
        self.kernel.add_effect_contract(self.contract)

    def grant_for(
        self,
        principal: Principal,
        *,
        grant_id: str = "grant",
        validity=True,
        revoked=False,
        expires_at=None,
    ) -> AuthorityGrant:
        grant = AuthorityGrant(
            grant_id=grant_id,
            root_id=self.root.root_id,
            principal_id=principal.principal_id,
            intent_id=self.intent.intent_id,
            validity=validity,
            revoked=revoked,
            expires_at=expires_at,
        )
        self.kernel.add_authority_grant(grant)
        return grant

    def request(self, **overrides) -> ActionRequest:
        values = dict(
            request_id="request-1",
            intent_id=self.intent.intent_id,
            contract_id=self.contract.contract_id,
            declared_principal=None,
            untrusted_authority=None,
        )
        values.update(overrides)
        return ActionRequest(**values)

    def test_positive_legal_trace_is_durable_and_single_use(self) -> None:
        self.grant_for(self.alice)
        request = self.request()
        may = self.kernel.may(self.alice_context, request)
        self.assertTrue(may.allowed)
        self.assertEqual(may.reason, "may")
        authorization_result = self.kernel.authorize(
            request, authentication_context=self.alice_context
        )
        self.assertTrue(authorization_result.allowed)
        authorization = authorization_result.authorization
        self.assertIsNotNone(authorization)

        start = self.kernel.start_attempt(authorization)
        self.assertTrue(start.allowed)
        self.assertIsNotNone(start.consumed)
        self.assertIsNotNone(start.attempt)
        self.assertIsNotNone(start.started)
        self.assertEqual(start.consumed.attempt_id, start.attempt.attempt_id)
        self.assertEqual(start.started.attempt_id, start.attempt.attempt_id)

        reopened = Kernel(self.db_path, clock=self.clock)
        snapshot = reopened.snapshot()
        self.assertEqual(len(snapshot["action_authorizations"]), 1)
        self.assertEqual(len(snapshot["authorization_consumed"]), 1)
        self.assertEqual(len(snapshot["action_attempts"]), 1)
        self.assertEqual(len(snapshot["attempt_started"]), 1)

        replay = reopened.start_attempt(authorization)
        self.assertFalse(replay.allowed)
        self.assertEqual(replay.reason, "authorization_consumed")
        self.assertEqual(len(reopened.snapshot()["action_attempts"]), 1)

    def test_request_self_authorization_does_not_override_trusted_identity(self) -> None:
        trusted_grant = self.grant_for(self.alice)
        hostile = self.request(
            declared_principal=self.alice.principal_id,
            untrusted_authority=trusted_grant,
        )
        result = self.kernel.authorize(
            hostile, authentication_context=self.mallory_context
        )
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "authority_absent")
        self.assertEqual(self.kernel.snapshot()["action_authorizations"], [])

    def test_invalid_grant_denies(self) -> None:
        self.grant_for(self.alice, validity=False)
        result = self.kernel.authorize(
            self.request(), authentication_context=self.alice_context
        )
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "authority_invalid")
        self.assertEqual(self.kernel.snapshot()["action_authorizations"], [])

    def test_expired_grant_denies(self) -> None:
        self.grant_for(self.alice, expires_at=100)
        result = self.kernel.authorize(
            self.request(), authentication_context=self.alice_context
        )
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "authority_expired")
        self.assertEqual(self.kernel.snapshot()["action_authorizations"], [])

    def test_revoked_grant_denies(self) -> None:
        self.grant_for(self.alice, revoked=True)
        result = self.kernel.authorize(
            self.request(), authentication_context=self.alice_context
        )
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "authority_revoked")
        self.assertEqual(self.kernel.snapshot()["action_authorizations"], [])

    def test_untrusted_authority_shaped_input_never_becomes_trusted_state(self) -> None:
        hostile_grant = AuthorityGrant(
            grant_id="hostile-grant",
            root_id="hostile-root",
            principal_id=self.mallory.principal_id,
            intent_id=self.intent.intent_id,
            validity=True,
            revoked=False,
        )
        before = self.kernel.snapshot()
        result = self.kernel.authorize(
            self.request(untrusted_authority=hostile_grant),
            authentication_context=self.mallory_context,
        )
        after = self.kernel.snapshot()
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "authority_absent")
        self.assertEqual(after["authority_roots"], before["authority_roots"])
        self.assertEqual(after["authority_grants"], before["authority_grants"])
        self.assertEqual(after["action_authorizations"], [])
        self.assertEqual(after["authorization_consumed"], [])
        self.assertEqual(after["action_attempts"], [])
        self.assertEqual(after["attempt_started"], [])

    def test_forged_or_altered_authorization_denies_without_consumption(self) -> None:
        grant = self.grant_for(self.alice)
        forged = ActionAuthorization(
            authorization_id="forged-id",
            request_id="request-1",
            principal_id=self.alice.principal_id,
            grant_id=grant.grant_id,
            intent_id=self.intent.intent_id,
            contract_id=self.contract.contract_id,
            issued_at=100,
        )
        rejected = self.kernel.start_attempt(forged)
        self.assertFalse(rejected.allowed)
        self.assertEqual(rejected.reason, "forged_authorization")

        issued = self.kernel.authorize(
            self.request(), authentication_context=self.alice_context
        )
        self.assertTrue(issued.allowed)
        authorization = issued.authorization
        altered = replace(authorization, principal_id=self.mallory.principal_id)
        rejected_alteration = self.kernel.start_attempt(altered)
        self.assertFalse(rejected_alteration.allowed)
        self.assertEqual(rejected_alteration.reason, "forged_authorization")
        snapshot = self.kernel.snapshot()
        self.assertEqual(snapshot["authorization_consumed"], [])
        self.assertEqual(snapshot["action_attempts"], [])
        self.assertEqual(snapshot["attempt_started"], [])

    def test_replay_after_successful_consume_never_creates_second_attempt(self) -> None:
        self.grant_for(self.alice)
        issued = self.kernel.authorize(
            self.request(), authentication_context=self.alice_context
        )
        first = self.kernel.start_attempt(issued.authorization)
        second = self.kernel.start_attempt(issued.authorization)
        self.assertTrue(first.allowed)
        self.assertFalse(second.allowed)
        self.assertEqual(second.reason, "authorization_consumed")
        snapshot = self.kernel.snapshot()
        self.assertEqual(len(snapshot["authorization_consumed"]), 1)
        self.assertEqual(len(snapshot["action_attempts"]), 1)
        self.assertEqual(len(snapshot["attempt_started"]), 1)

    def test_double_consume_competition_yields_at_most_one_valid_attempt(self) -> None:
        self.grant_for(self.alice)
        issued = self.kernel.authorize(
            self.request(), authentication_context=self.alice_context
        )
        authorization = issued.authorization
        barrier = threading.Barrier(3)
        results = []
        lock = threading.Lock()

        def consume() -> None:
            barrier.wait()
            result = self.kernel.start_attempt(authorization)
            with lock:
                results.append(result)

        threads = [threading.Thread(target=consume) for _ in range(2)]
        for thread in threads:
            thread.start()
        barrier.wait()
        for thread in threads:
            thread.join()

        self.assertEqual(sum(1 for result in results if result.allowed), 1)
        self.assertEqual(sum(1 for result in results if not result.allowed), 1)
        snapshot = Kernel(self.db_path, clock=self.clock).snapshot()
        self.assertEqual(len(snapshot["authorization_consumed"]), 1)
        self.assertEqual(len(snapshot["action_attempts"]), 1)
        self.assertEqual(len(snapshot["attempt_started"]), 1)

    def test_authority_invalidation_before_start_denies_without_consuming(self) -> None:
        grant = self.grant_for(self.alice)
        issued = self.kernel.authorize(
            self.request(), authentication_context=self.alice_context
        )
        self.assertTrue(issued.allowed)
        self.kernel.set_grant_revoked(grant.grant_id, True)
        start = self.kernel.start_attempt(issued.authorization)
        self.assertFalse(start.allowed)
        self.assertEqual(start.reason, "authority_revoked")
        snapshot = self.kernel.snapshot()
        self.assertEqual(snapshot["authorization_consumed"], [])
        self.assertEqual(snapshot["action_attempts"], [])
        self.assertEqual(snapshot["attempt_started"], [])

    def test_unknown_required_pre_effect_authority_fact_denies(self) -> None:
        self.grant_for(self.alice, validity=None)
        result = self.kernel.authorize(
            self.request(), authentication_context=self.alice_context
        )
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "unknown_authority_fact")
        self.assertEqual(self.kernel.snapshot()["action_authorizations"], [])

    def test_unknown_authority_fact_at_start_denies_without_consuming(self) -> None:
        grant = self.grant_for(self.alice)
        issued = self.kernel.authorize(
            self.request(), authentication_context=self.alice_context
        )
        self.assertTrue(issued.allowed)
        self.kernel.set_grant_validity(grant.grant_id, None)
        start = self.kernel.start_attempt(issued.authorization)
        self.assertFalse(start.allowed)
        self.assertEqual(start.reason, "unknown_authority_fact")
        snapshot = self.kernel.snapshot()
        self.assertEqual(snapshot["authorization_consumed"], [])
        self.assertEqual(snapshot["action_attempts"], [])
        self.assertEqual(snapshot["attempt_started"], [])


if __name__ == "__main__":
    unittest.main()
