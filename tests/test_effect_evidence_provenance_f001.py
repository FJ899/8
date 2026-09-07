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


class P9F001EvidenceProvenanceRegression(unittest.TestCase):
    def test_forged_runtime_trace_cannot_relabel_real_durable_effect_chain(self) -> None:
        domain = G3Domain()
        self.addCleanup(domain.close)
        adapter = G3EffectAdapter(domain.kernel, domain.observer)
        operation = domain.operation("real-effect")
        binding = CapabilityBinding(
            "real-binding",
            domain.intent.intent_id,
            domain.capability_id,
            "X",
            adapter,
        )
        runtime = KernelRuntime(domain.kernel, TrustedBindingRegistry((binding,)))
        real = runtime.run(
            ActionRequest("real-request", domain.intent.intent_id, domain.contract.contract_id),
            operation,
            authentication_context=domain.context,
        )
        self.assertTrue(real.authorization.allowed)
        self.assertTrue(real.binding.allowed)
        self.assertTrue(real.start.allowed)
        self.assertTrue(real.admission.allowed)
        self.assertTrue(real.execution.occurred)

        real_auth = real.authorization.authorization
        real_start = real.start
        real_attempt = real_start.attempt
        fake_authorization_id = "forged-authorization"
        fake_request_id = "forged-request"

        forged_authorization = ActionAuthorization(
            fake_authorization_id,
            fake_request_id,
            real_auth.principal_id,
            real_auth.grant_id,
            real_auth.intent_id,
            real_auth.contract_id,
            real_auth.issued_at,
        )
        forged_binding = CapabilityBinding(
            "forged-binding",
            binding.intent_id,
            binding.capability_id,
            binding.target_identity,
            adapter,
        )
        forged_attempt = ActionAttempt(
            real_attempt.attempt_id,
            fake_authorization_id,
            real_attempt.principal_id,
            real_attempt.intent_id,
            real_attempt.contract_id,
        )
        forged_start = StartResult(
            True,
            "started",
            forged_attempt,
            AuthorizationConsumed(
                fake_authorization_id,
                real_attempt.attempt_id,
                real_start.consumed.consumed_at,
            ),
            AttemptStarted(
                real_attempt.attempt_id,
                real_start.started.started_at,
            ),
        )
        forged_trace = RuntimeTrace(
            request_id=fake_request_id,
            authorization=AuthorizationResult(True, "authorized", forged_authorization),
            binding=BindingResult(True, "binding_resolved", forged_binding),
            start=forged_start,
            admission=real.admission,
            execution=real.execution,
        )

        collector = EffectEvidenceCollector(G3EvidenceProducer(adapter))
        with self.assertRaisesRegex(ValueError, "durable_.*mismatch|evidence_requires_durable_chain"):
            collector.collect(forged_trace, operation)


if __name__ == "__main__":
    unittest.main()
