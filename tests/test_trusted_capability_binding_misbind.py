from __future__ import annotations

import unittest

from agency_kernel.bindings import CapabilityBinding, TrustedBindingRegistry
from agency_kernel.runtime import KernelRuntime
from tests.test_trusted_capability_binding import MultiDomainFixture


class TrustedCapabilityMisbindingTests(unittest.TestCase):
    def test_resolved_binding_with_wrong_capability_still_denies_at_admission(self) -> None:
        fixture = MultiDomainFixture()
        self.addCleanup(fixture.close)
        wrong_capability_binding = CapabilityBinding(
            "binding-put-wrong-capability",
            fixture.put_intent.intent_id,
            "cap-git",
            "X",
            fixture.g3_adapter,
        )
        runtime = KernelRuntime(
            fixture.authority,
            TrustedBindingRegistry((wrong_capability_binding, fixture.git_binding)),
        )

        trace = runtime.run(
            fixture.request(
                fixture.put_intent,
                fixture.put_contract,
                "wrong-trusted-capability",
            ),
            fixture.put_operation("must-not-run"),
            authentication_context=fixture.context,
        )

        self.assertTrue(trace.authorization.allowed, trace.authorization.reason)
        self.assertTrue(trace.binding.allowed, trace.binding.reason)
        self.assertEqual(
            trace.binding.binding.capability_id,
            "cap-git",
        )
        self.assertTrue(trace.start.allowed, trace.start.reason)
        self.assertFalse(trace.admission.allowed)
        self.assertEqual(trace.admission.reason, "capability_resource_mismatch")
        self.assertIsNone(trace.execution)


if __name__ == "__main__":
    unittest.main()
