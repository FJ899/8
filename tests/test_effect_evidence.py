from __future__ import annotations

import inspect
import unittest
from dataclasses import FrozenInstanceError, fields

from agency_kernel.bindings import CapabilityBinding, TrustedBindingRegistry
from agency_kernel.effect_seams import G3EffectAdapter, G4EffectAdapter
from agency_kernel.evidence import (
    EffectEvidence,
    EffectEvidenceCollector,
    G3EvidenceProducer,
    G4EvidenceProducer,
    HttpCasEvidenceProducer,
)
from agency_kernel.g1 import ActionRequest
from agency_kernel.g3 import PutIfVersionOperation
from agency_kernel.http_cas import HttpCasEffectAdapter
from agency_kernel.reconciliation import ReconciliationStatus
from agency_kernel.runtime import KernelRuntime
from tests.test_effect_domain_conformance import G3Domain, G4Domain
from tests.test_http_cas import HttpCasDomain


FORBIDDEN_EVIDENCE_FIELDS = {
    "allowed",
    "authorized",
    "compliant",
    "did",
    "passed",
    "satisfied",
    "secure",
    "within_scope",
}


class EffectEvidenceNormalizationTests(unittest.TestCase):
    def add_domain_cleanup(self, domain):
        self.addCleanup(domain.close)
        return domain

    def run_case(self, domain, adapter, producer, operation, *, request_id: str):
        binding = CapabilityBinding(
            f"binding-{request_id}",
            domain.intent.intent_id,
            domain.capability_id,
            adapter.target_identity(operation),
            adapter,
        )
        runtime = KernelRuntime(
            domain.kernel,
            TrustedBindingRegistry((binding,)),
        )
        trace = runtime.run(
            ActionRequest(
                request_id,
                domain.intent.intent_id,
                domain.contract.contract_id,
            ),
            operation,
            authentication_context=domain.context,
        )
        self.assertTrue(trace.authorization.allowed, trace.authorization.reason)
        self.assertIsNotNone(trace.binding)
        self.assertTrue(trace.binding.allowed, trace.binding.reason)
        self.assertIsNotNone(trace.start)
        self.assertTrue(trace.start.allowed, trace.start.reason)
        self.assertIsNotNone(trace.admission)
        self.assertTrue(trace.admission.allowed, trace.admission.reason)
        self.assertIsNotNone(trace.execution)
        return trace, binding, EffectEvidenceCollector(producer)

    def test_three_domains_share_one_reference_only_evidence_shape(self) -> None:
        g3 = self.add_domain_cleanup(G3Domain())
        g3_adapter = G3EffectAdapter(g3.kernel, g3.observer)
        g3_op = g3.operation("evidence-g3")
        g3_trace, g3_binding, g3_collector = self.run_case(
            g3,
            g3_adapter,
            G3EvidenceProducer(g3_adapter),
            g3_op,
            request_id="p8-g3",
        )

        g4 = self.add_domain_cleanup(G4Domain())
        g4_adapter = G4EffectAdapter(g4.kernel, g4.observer)
        g4_op = g4.operation("evidence-g4")
        g4_trace, g4_binding, g4_collector = self.run_case(
            g4,
            g4_adapter,
            G4EvidenceProducer(g4_adapter),
            g4_op,
            request_id="p8-g4",
        )

        http = self.add_domain_cleanup(HttpCasDomain())
        http_adapter = HttpCasEffectAdapter(http.kernel, http.observer)
        http_op = http.operation("evidence-http")
        http_trace, http_binding, http_collector = self.run_case(
            http,
            http_adapter,
            HttpCasEvidenceProducer(http_adapter),
            http_op,
            request_id="p8-http",
        )

        cases = (
            (
                "g3-versioned-store",
                g3_trace,
                g3_binding,
                g3_op,
                g3_collector,
                "g3_mutation_provenance",
                g3_trace.execution.mutation_id,
            ),
            (
                "g4-sanitized-git",
                g4_trace,
                g4_binding,
                g4_op,
                g4_collector,
                "g4_git_commit",
                g4_trace.execution.after_oid,
            ),
            (
                "http-cas",
                http_trace,
                http_binding,
                http_op,
                http_collector,
                "http_provider_receipt",
                http_trace.admission.admission.admission_id,
            ),
        )

        for domain_id, trace, binding, operation, collector, ref_kind, ref_id in cases:
            with self.subTest(domain=domain_id):
                evidence = collector.collect(trace, operation)
                self.assertIsInstance(evidence, EffectEvidence)
                self.assertEqual(evidence.domain_id, domain_id)
                self.assertEqual(evidence.request_id, trace.request_id)
                self.assertEqual(
                    evidence.authorization_id,
                    trace.authorization.authorization.authorization_id,
                )
                self.assertEqual(evidence.binding_id, binding.binding_id)
                self.assertEqual(evidence.attempt_id, trace.start.attempt.attempt_id)
                self.assertEqual(
                    evidence.admission_id,
                    trace.admission.admission.admission_id,
                )
                self.assertEqual(
                    evidence.operation_digest,
                    trace.admission.admission.operation_digest,
                )
                self.assertEqual(
                    evidence.capability_id,
                    trace.admission.admission.capability_id,
                )
                self.assertEqual(
                    evidence.target_identity,
                    binding.target_identity,
                )
                self.assertIsNotNone(evidence.domain_evidence)
                self.assertEqual(evidence.domain_evidence.kind, ref_kind)
                self.assertEqual(evidence.domain_evidence.record_id, ref_id)
                self.assertIsNotNone(evidence.observation)
                self.assertEqual(
                    evidence.reconciliation.status,
                    ReconciliationStatus.OCCURRED,
                )
                self.assertEqual(
                    evidence.reconciliation.observation_digest,
                    evidence.observation.digest,
                )

    def test_evidence_object_has_no_authority_compliance_or_pass_fields(self) -> None:
        names = {field.name for field in fields(EffectEvidence)}
        self.assertTrue(FORBIDDEN_EVIDENCE_FIELDS.isdisjoint(names))
        for forbidden in FORBIDDEN_EVIDENCE_FIELDS:
            self.assertFalse(hasattr(EffectEvidence, forbidden), forbidden)

    def test_collector_accepts_no_caller_supplied_observation_or_verdict(self) -> None:
        parameters = set(inspect.signature(EffectEvidenceCollector.collect).parameters)
        self.assertEqual(parameters, {"self", "trace", "operation"})
        self.assertTrue(
            {"observation", "reconciliation", "compliance", "did", "pass"}.isdisjoint(parameters)
        )

    def test_exact_runtime_adapter_object_is_required(self) -> None:
        domain = self.add_domain_cleanup(G3Domain())
        runtime_adapter = G3EffectAdapter(domain.kernel, domain.observer)
        operation = domain.operation("bound-adapter")
        trace, _binding, _collector = self.run_case(
            domain,
            runtime_adapter,
            G3EvidenceProducer(runtime_adapter),
            operation,
            request_id="p8-exact-adapter",
        )
        different_adapter_object = G3EffectAdapter(domain.kernel, domain.observer)
        collector = EffectEvidenceCollector(G3EvidenceProducer(different_adapter_object))
        with self.assertRaisesRegex(ValueError, "producer_not_bound_to_runtime_adapter"):
            collector.collect(trace, operation)

    def test_o1_evidence_cannot_be_rebound_to_o2(self) -> None:
        domain = self.add_domain_cleanup(G3Domain())
        adapter = G3EffectAdapter(domain.kernel, domain.observer)
        op1 = domain.operation("O1")
        trace, _binding, collector = self.run_case(
            domain,
            adapter,
            G3EvidenceProducer(adapter),
            op1,
            request_id="p8-o1",
        )
        op2 = PutIfVersionOperation(
            "X",
            0,
            "O2",
            domain.kernel.possible_effects_for("X"),
        )
        self.assertNotEqual(op1.operation_digest, op2.operation_digest)
        with self.assertRaisesRegex(ValueError, "admission_operation_mismatch"):
            collector.collect(trace, op2)

    def test_denied_or_incomplete_runtime_trace_cannot_be_normalized(self) -> None:
        domain = self.add_domain_cleanup(G3Domain())
        adapter = G3EffectAdapter(domain.kernel, domain.observer)
        operation = domain.operation("never")
        binding = CapabilityBinding(
            "binding-denied",
            domain.intent.intent_id,
            domain.capability_id,
            "X",
            adapter,
        )
        runtime = KernelRuntime(domain.kernel, TrustedBindingRegistry((binding,)))
        trace = runtime.run(
            ActionRequest(
                "p8-denied",
                domain.intent.intent_id,
                domain.contract.contract_id,
            ),
            operation,
            authentication_context=None,
        )
        self.assertFalse(trace.authorization.allowed)
        collector = EffectEvidenceCollector(G3EvidenceProducer(adapter))
        with self.assertRaisesRegex(ValueError, "evidence_requires_admitted_runtime_trace"):
            collector.collect(trace, operation)

    def test_later_target_drift_produces_new_observation_reference_and_no_stored_pass(self) -> None:
        domain = self.add_domain_cleanup(G3Domain())
        adapter = G3EffectAdapter(domain.kernel, domain.observer)
        operation = domain.operation("authorized")
        trace, _binding, collector = self.run_case(
            domain,
            adapter,
            G3EvidenceProducer(adapter),
            operation,
            request_id="p8-drift",
        )
        first = collector.collect(trace, operation)
        self.assertEqual(first.reconciliation.status, ReconciliationStatus.OCCURRED)
        self.assertIsNotNone(first.domain_evidence)

        domain.kernel.inject_unattributed_delta_for_test("X", "external", 2)
        later = collector.collect(trace, operation)
        self.assertEqual(later.reconciliation.status, ReconciliationStatus.INDETERMINATE)
        self.assertIsNone(later.domain_evidence)
        self.assertNotEqual(first.observation.digest, later.observation.digest)
        self.assertEqual(first.reconciliation.status, ReconciliationStatus.OCCURRED)

    def test_http_terminal_nonoccurrence_is_referenced_without_becoming_security_pass(self) -> None:
        domain = self.add_domain_cleanup(HttpCasDomain())
        adapter = HttpCasEffectAdapter(domain.kernel, domain.observer)
        operation = domain.operation("never", expected_version=7)
        trace, _binding, collector = self.run_case(
            domain,
            adapter,
            HttpCasEvidenceProducer(adapter),
            operation,
            request_id="p8-http-stale",
        )
        self.assertFalse(trace.execution.occurred)
        self.assertEqual(trace.execution.reason, "provider_rejected_stale")
        evidence = collector.collect(trace, operation)
        self.assertEqual(
            evidence.reconciliation.status,
            ReconciliationStatus.NOT_OCCURRED,
        )
        self.assertEqual(
            evidence.domain_evidence.kind,
            "http_provider_receipt",
        )
        self.assertEqual(
            evidence.domain_evidence.record_id,
            trace.admission.admission.admission_id,
        )
        for forbidden in FORBIDDEN_EVIDENCE_FIELDS:
            self.assertFalse(hasattr(evidence, forbidden), forbidden)

    def test_effect_evidence_is_immutable(self) -> None:
        domain = self.add_domain_cleanup(G3Domain())
        adapter = G3EffectAdapter(domain.kernel, domain.observer)
        operation = domain.operation("immutable")
        trace, _binding, collector = self.run_case(
            domain,
            adapter,
            G3EvidenceProducer(adapter),
            operation,
            request_id="p8-immutable",
        )
        evidence = collector.collect(trace, operation)
        with self.assertRaises(FrozenInstanceError):
            evidence.request_id = "rewritten"


if __name__ == "__main__":
    unittest.main()
