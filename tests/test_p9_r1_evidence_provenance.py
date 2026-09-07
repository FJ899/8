from __future__ import annotations

import unittest

from agency_kernel.bindings import BindingResult, CapabilityBinding, TrustedBindingRegistry
from agency_kernel.effect_seams import G3EffectAdapter
from agency_kernel.evidence import EffectEvidenceCollector, G3EvidenceProducer
from agency_kernel.g1 import (
    ActionAttempt,
    ActionAuthorization,
    ActionRequest,
    AttemptStarted,
    AuthorizationConsumed,
    AuthorizationResult,
    StartResult,
)
from agency_kernel.runtime import KernelRuntime, RuntimeTrace
from tests.test_effect_domain_conformance import G3Domain


class DurableEvidenceProvenanceRepairTests(unittest.TestCase):
    def domain(self) -> G3Domain:
        domain = G3Domain()
        self.addCleanup(domain.close)
        return domain

    def admitted_runtime(self):
        domain = self.domain()
        adapter = G3EffectAdapter(domain.kernel, domain.observer)
        operation = domain.operation("durable-evidence")
        binding = CapabilityBinding(
            "binding-real",
            domain.intent.intent_id,
            domain.capability_id,
            "X",
            adapter,
        )
        runtime = KernelRuntime(
            domain.kernel,
            TrustedBindingRegistry((binding,)),
        )
        trace = runtime.run(
            ActionRequest(
                "request-real",
                domain.intent.intent_id,
                domain.contract.contract_id,
            ),
            operation,
            authentication_context=domain.context,
        )
        self.assertTrue(trace.authorization.allowed, trace.authorization.reason)
        self.assertIsNotNone(trace.authorization.authorization)
        self.assertIsNotNone(trace.binding)
        self.assertTrue(trace.binding.allowed, trace.binding.reason)
        self.assertIsNotNone(trace.binding.binding)
        self.assertIsNotNone(trace.start)
        self.assertTrue(trace.start.allowed, trace.start.reason)
        self.assertIsNotNone(trace.start.attempt)
        self.assertIsNotNone(trace.start.consumed)
        self.assertIsNotNone(trace.start.started)
        self.assertIsNotNone(trace.admission)
        self.assertTrue(trace.admission.allowed, trace.admission.reason)
        self.assertIsNotNone(trace.admission.admission)
        self.assertIsNotNone(trace.execution)
        self.assertTrue(trace.execution.occurred, trace.execution.reason)
        return domain, adapter, operation, trace

    def test_forged_runtime_trace_cannot_supply_historical_evidence_identities(self) -> None:
        domain, adapter, operation, real = self.admitted_runtime()
        real_authorization = real.authorization.authorization
        real_attempt = real.start.attempt
        real_consumed = real.start.consumed
        real_started = real.start.started

        forged_authorization = ActionAuthorization(
            "authorization-forged",
            "request-forged",
            real_authorization.principal_id,
            real_authorization.grant_id,
            real_authorization.intent_id,
            real_authorization.contract_id,
            real_authorization.issued_at,
        )
        forged_attempt = ActionAttempt(
            real_attempt.attempt_id,
            forged_authorization.authorization_id,
            real_attempt.principal_id,
            real_attempt.intent_id,
            real_attempt.contract_id,
        )
        forged_start = StartResult(
            True,
            "attempt_started",
            forged_attempt,
            AuthorizationConsumed(
                forged_authorization.authorization_id,
                real_attempt.attempt_id,
                real_consumed.consumed_at,
            ),
            AttemptStarted(real_attempt.attempt_id, real_started.started_at),
        )
        forged_binding = CapabilityBinding(
            "binding-forged",
            real_authorization.intent_id,
            real.admission.admission.capability_id,
            "X",
            adapter,
        )
        forged = RuntimeTrace(
            request_id="request-forged",
            authorization=AuthorizationResult(True, "authorized", forged_authorization),
            binding=BindingResult(True, "binding_resolved", forged_binding),
            start=forged_start,
            admission=real.admission,
            execution=real.execution,
        )

        collector = EffectEvidenceCollector(G3EvidenceProducer(adapter))
        with self.assertRaises(ValueError):
            collector.collect(forged, operation)

        # The real durable trace must remain collectable; the attack must not be
        # repaired by rejecting all evidence collection.
        real_evidence = collector.collect(real, operation)
        self.assertEqual(real_evidence.request_id, "request-real")
        self.assertEqual(
            real_evidence.authorization_id,
            real_authorization.authorization_id,
        )
        self.assertEqual(real_evidence.attempt_id, real_attempt.attempt_id)
        self.assertEqual(
            real_evidence.admission_id,
            real.admission.admission.admission_id,
        )

    def test_evidence_can_be_rehydrated_from_durable_admission_after_trace_loss_without_retry(self) -> None:
        domain, adapter, operation, trace = self.admitted_runtime()
        admission_id = trace.admission.admission.admission_id
        expected_request_id = trace.authorization.authorization.request_id
        expected_authorization_id = trace.authorization.authorization.authorization_id
        expected_attempt_id = trace.start.attempt.attempt_id
        before = domain.observer.observe("X")

        # From this point the transient RuntimeTrace is deliberately not used as
        # input to recovery.  Only durable admission identity + exact operation
        # are supplied to the evidence layer.
        collector = EffectEvidenceCollector(G3EvidenceProducer(adapter))
        evidence = collector.collect_from_admission_id(admission_id, operation)

        after = domain.observer.observe("X")
        self.assertEqual((after.value, after.version), (before.value, before.version))
        self.assertEqual(evidence.request_id, expected_request_id)
        self.assertEqual(evidence.authorization_id, expected_authorization_id)
        self.assertEqual(evidence.attempt_id, expected_attempt_id)
        self.assertEqual(evidence.admission_id, admission_id)
        self.assertEqual(evidence.operation_digest, operation.operation_digest)

        # Evidence recovery must not retry/re-execute the already-consumed
        # admission.  A direct second execution remains denied as replay.
        replay = adapter.execute(admission_id)
        self.assertFalse(replay.occurred)
        self.assertEqual(replay.reason, "admission_consumed")


if __name__ == "__main__":
    unittest.main()
