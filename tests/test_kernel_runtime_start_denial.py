from __future__ import annotations

import unittest

from agency_kernel.effect_seams import G3EffectAdapter, G4EffectAdapter
from agency_kernel.g1 import ActionRequest
from agency_kernel.runtime import KernelRuntime
from tests.test_effect_domain_conformance import G3Domain, G4Domain


CASES = (
    (G3Domain, G3EffectAdapter),
    (G4Domain, G4EffectAdapter),
)


class RevokeAfterAuthorizeKernel:
    """Fault injector for authority loss between authorize and start_attempt."""

    __slots__ = ("_kernel", "_grant_id")

    def __init__(self, kernel, grant_id: str) -> None:
        self._kernel = kernel
        self._grant_id = grant_id

    def authorize(self, request, *, authentication_context=None):
        result = self._kernel.authorize(
            request,
            authentication_context=authentication_context,
        )
        if result.allowed:
            self._kernel.set_grant_revoked(self._grant_id, True)
        return result

    def start_attempt(self, authorization):
        return self._kernel.start_attempt(authorization)


class KernelRuntimeStartDenialTests(unittest.TestCase):
    def test_authority_loss_before_start_stops_before_admission_and_effect(self) -> None:
        for domain_factory, adapter_factory in CASES:
            with self.subTest(domain=domain_factory.name):
                domain = domain_factory()
                self.addCleanup(domain.close)
                adapter = adapter_factory(domain.kernel, domain.observer)
                runtime = KernelRuntime(
                    RevokeAfterAuthorizeKernel(domain.kernel, domain.grant_id),
                    adapter,
                    domain.capability_id,
                )
                request = ActionRequest(
                    "runtime-start-denial",
                    domain.intent.intent_id,
                    domain.contract.contract_id,
                )
                trace = runtime.run(
                    request,
                    domain.operation("must-not-run"),
                    authentication_context=domain.context,
                )

                self.assertTrue(trace.authorization.allowed, trace.authorization.reason)
                self.assertIsNotNone(trace.start)
                self.assertFalse(trace.start.allowed)
                self.assertEqual(trace.start.reason, "authority_revoked")
                self.assertIsNone(trace.admission)
                self.assertIsNone(trace.execution)


if __name__ == "__main__":
    unittest.main()
