from __future__ import annotations

import unittest

from agency_kernel.effect_seams import G3EffectAdapter, G4EffectAdapter
from agency_kernel.g1 import ActionRequest
from agency_kernel.runtime import KernelRuntime, RuntimeTrace
from tests.test_effect_domain_conformance import G3Domain, G4Domain


CASES = (
    (G3Domain, G3EffectAdapter),
    (G4Domain, G4EffectAdapter),
)


class LostResultG3Adapter(G3EffectAdapter):
    """Fault injector: effect path runs once, then its result is lost."""

    __slots__ = ("execute_calls", "last_admission_id")

    def __init__(self, kernel, observer) -> None:
        super().__init__(kernel, observer)
        self.execute_calls = 0
        self.last_admission_id = None

    def execute(self, admission_id: str, *, crash_point=None):
        self.execute_calls += 1
        self.last_admission_id = admission_id
        super().execute(admission_id, crash_point=crash_point)
        raise RuntimeError("simulated_lost_execution_result")


class KernelRuntimeTests(unittest.TestCase):
    def make(self, domain_factory, adapter_factory, *, capability_id=None):
        domain = domain_factory()
        self.addCleanup(domain.close)
        adapter = adapter_factory(domain.kernel, domain.observer)
        runtime = KernelRuntime(
            domain.kernel,
            adapter,
            capability_id or domain.capability_id,
        )
        return domain, adapter, runtime

    @staticmethod
    def request(domain, request_id: str = "runtime-request", **kwargs) -> ActionRequest:
        return ActionRequest(
            request_id,
            domain.intent.intent_id,
            domain.contract.contract_id,
            **kwargs,
        )

    def test_positive_g3_and_g4_use_one_runtime_path(self) -> None:
        for domain_factory, adapter_factory in CASES:
            with self.subTest(domain=domain_factory.name):
                domain, adapter, runtime = self.make(domain_factory, adapter_factory)
                operation = domain.operation("runtime-effect")
                trace = runtime.run(
                    self.request(domain),
                    operation,
                    authentication_context=domain.context,
                )
                self.assertIsInstance(trace, RuntimeTrace)
                self.assertTrue(trace.authorization.allowed, trace.authorization.reason)
                self.assertIsNotNone(trace.start)
                self.assertTrue(trace.start.allowed, trace.start.reason)
                self.assertIsNotNone(trace.admission)
                self.assertTrue(trace.admission.allowed, trace.admission.reason)
                self.assertIsNotNone(trace.execution)
                self.assertTrue(trace.execution.occurred, trace.execution.reason)
                self.assertEqual(
                    trace.admission.admission.operation_digest,
                    operation.operation_digest,
                )
                observation = adapter.observe(operation)
                self.assertTrue(adapter.did(trace.admission.admission, observation))
                compliance = adapter.assess_compliance(
                    trace.admission.admission,
                    observation,
                    supported_possible_effects=operation.possible_effects,
                )
                self.assertEqual(compliance.status, "PASS")

    def test_authentication_denial_stops_before_attempt_admission_and_effect(self) -> None:
        for domain_factory, adapter_factory in CASES:
            with self.subTest(domain=domain_factory.name):
                domain, _adapter, runtime = self.make(domain_factory, adapter_factory)
                before = domain.kernel.snapshot()
                trace = runtime.run(
                    self.request(domain, "no-auth"),
                    domain.operation("must-not-run"),
                    authentication_context=None,
                )
                after = domain.kernel.snapshot()
                self.assertFalse(trace.authorization.allowed)
                self.assertEqual(trace.authorization.reason, "missing_authentication_context")
                self.assertIsNone(trace.start)
                self.assertIsNone(trace.admission)
                self.assertIsNone(trace.execution)
                self.assertEqual(
                    len(after["action_authorizations"]),
                    len(before["action_authorizations"]),
                )
                self.assertEqual(
                    len(after["action_attempts"]),
                    len(before["action_attempts"]),
                )

    def test_admission_denial_stops_before_effect(self) -> None:
        for domain_factory, adapter_factory in CASES:
            with self.subTest(domain=domain_factory.name):
                domain, _adapter, runtime = self.make(domain_factory, adapter_factory)
                domain.invalidate_capability()
                trace = runtime.run(
                    self.request(domain, "invalid-capability"),
                    domain.operation("must-not-run"),
                    authentication_context=domain.context,
                )
                self.assertTrue(trace.authorization.allowed)
                self.assertTrue(trace.start.allowed)
                self.assertIsNotNone(trace.admission)
                self.assertFalse(trace.admission.allowed)
                self.assertEqual(trace.admission.reason, "capability_invalid")
                self.assertIsNone(trace.execution)

    def test_capability_binding_is_fixed_at_composition_time(self) -> None:
        for domain_factory, adapter_factory in CASES:
            with self.subTest(domain=domain_factory.name):
                domain = domain_factory()
                self.addCleanup(domain.close)
                wrong_capability = domain.mismatched_capability_id()
                adapter = adapter_factory(domain.kernel, domain.observer)
                runtime = KernelRuntime(domain.kernel, adapter, wrong_capability)
                trace = runtime.run(
                    self.request(domain, "wrong-bound-capability"),
                    domain.operation("must-not-run"),
                    authentication_context=domain.context,
                )
                self.assertTrue(trace.authorization.allowed)
                self.assertTrue(trace.start.allowed)
                self.assertFalse(trace.admission.allowed)
                self.assertEqual(trace.admission.reason, "capability_resource_mismatch")
                self.assertIsNone(trace.execution)

    def test_untrusted_request_fields_cannot_select_adapter_or_capability(self) -> None:
        for domain_factory, adapter_factory in CASES:
            with self.subTest(domain=domain_factory.name):
                domain, adapter, runtime = self.make(domain_factory, adapter_factory)
                operation = domain.operation("trusted-binding-wins")
                request = self.request(
                    domain,
                    "hostile-routing-fields",
                    declared_principal="mallory",
                    untrusted_authority={
                        "adapter_id": "attacker-adapter",
                        "capability_id": "attacker-capability",
                        "principal_id": "mallory",
                    },
                )
                trace = runtime.run(
                    request,
                    operation,
                    authentication_context=domain.context,
                )
                self.assertTrue(trace.authorization.allowed, trace.authorization.reason)
                self.assertTrue(trace.admission.allowed, trace.admission.reason)
                self.assertEqual(
                    trace.admission.admission.capability_id,
                    domain.capability_id,
                )
                self.assertTrue(trace.execution.occurred, trace.execution.reason)
                self.assertTrue(adapter.satisfied(
                    adapter.observe(operation),
                    "trusted-binding-wins"
                    if domain_factory is G3Domain
                    else {"A.txt": "trusted-binding-wins"},
                ))

    def test_exact_operation_binding_survives_runtime_orchestration(self) -> None:
        for domain_factory, adapter_factory in CASES:
            with self.subTest(domain=domain_factory.name):
                domain, adapter, runtime = self.make(domain_factory, adapter_factory)
                op1 = domain.operation("O1")
                op2 = domain.operation("O2")
                self.assertNotEqual(op1.operation_digest, op2.operation_digest)
                trace = runtime.run(
                    self.request(domain, "exact-operation"),
                    op1,
                    authentication_context=domain.context,
                )
                self.assertTrue(trace.execution.occurred, trace.execution.reason)
                self.assertEqual(
                    trace.admission.admission.operation_digest,
                    op1.operation_digest,
                )
                observation = adapter.observe(op1)
                expected_o1 = "O1" if domain_factory is G3Domain else {"A.txt": "O1"}
                expected_o2 = "O2" if domain_factory is G3Domain else {"A.txt": "O2"}
                self.assertTrue(adapter.satisfied(observation, expected_o1))
                self.assertFalse(adapter.satisfied(observation, expected_o2))

    def test_runtime_exposes_no_admission_continuation_or_routing_surface(self) -> None:
        forbidden = {
            "adapter",
            "capability_id",
            "execute_admission",
            "execute_operation",
            "route",
            "select_adapter",
            "select_capability",
        }
        public = {name for name in dir(KernelRuntime) if not name.startswith("_")}
        self.assertEqual(public, {"run"})
        self.assertTrue(forbidden.isdisjoint(public))

    def test_runtime_trace_does_not_collapse_security_relations(self) -> None:
        domain, _adapter, runtime = self.make(G3Domain, G3EffectAdapter)
        trace = runtime.run(
            self.request(domain, "trace-separation"),
            domain.operation("trace"),
            authentication_context=domain.context,
        )
        for forbidden in (
            "allowed",
            "authorized",
            "did",
            "passed",
            "satisfied",
            "status",
            "within_scope",
        ):
            self.assertFalse(hasattr(trace, forbidden), forbidden)
        self.assertIsNotNone(trace.authorization)
        self.assertIsNotNone(trace.start)
        self.assertIsNotNone(trace.admission)
        self.assertIsNotNone(trace.execution)

    def test_runtime_never_retries_when_execution_result_is_lost(self) -> None:
        domain = G3Domain()
        self.addCleanup(domain.close)
        adapter = LostResultG3Adapter(domain.kernel, domain.observer)
        runtime = KernelRuntime(domain.kernel, adapter, domain.capability_id)
        operation = domain.operation("committed-once")

        with self.assertRaisesRegex(RuntimeError, "simulated_lost_execution_result"):
            runtime.run(
                self.request(domain, "lost-result"),
                operation,
                authentication_context=domain.context,
            )

        self.assertEqual(adapter.execute_calls, 1)
        self.assertIsNotNone(adapter.last_admission_id)
        replay = G3EffectAdapter(domain.kernel, domain.observer).execute(
            adapter.last_admission_id
        )
        self.assertFalse(replay.occurred)
        self.assertEqual(replay.reason, "admission_consumed")
        observation = domain.observer.observe("X")
        self.assertEqual(observation.value, "committed-once")


if __name__ == "__main__":
    unittest.main()
