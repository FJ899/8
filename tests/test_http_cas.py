from __future__ import annotations

import multiprocessing
import tempfile
import threading
import time
import unittest
from pathlib import Path

from agency_kernel.bindings import CapabilityBinding, TrustedBindingRegistry
from agency_kernel.g1 import (
    ActionRequest,
    AuthenticationContext,
    AuthorityGrant,
    AuthorityRoot,
    EffectContract,
    EffectIntent,
    Principal,
)
from agency_kernel.g2 import Capability
from agency_kernel.http_cas import (
    HttpCasEffectAdapter,
    HttpCasReconciliationAdapter,
    Kernel as HttpCasKernel,
)
from agency_kernel.http_cas_provider import (
    HttpCasObserver,
    initialize_http_cas_provider,
    inject_committed_receipt_without_state_for_test,
    inject_unattributed_http_cas_change_for_test,
    read_http_cas_resource_for_test,
    seed_http_cas_resource,
    serve_http_cas_provider,
)
from agency_kernel.http_cas_types import HttpCasOperation
from agency_kernel.reconciliation import Reconciler, ReconciliationStatus
from agency_kernel.runtime import KernelRuntime


class HttpCasDomain:
    def __init__(
        self,
        *,
        kernel_token: str = "provider-secret",
        observer_token: str | None = None,
        provider_id: str = "provider-local",
        allow_test_faults: bool = True,
    ) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        root = Path(self.tempdir.name)
        self.control_db = root / "control.db"
        self.provider_db = root / "provider.db"
        self.provider_token = "provider-secret"
        self.provider_id = provider_id
        initialize_http_cas_provider(self.provider_db, "provider-local")
        seed_http_cas_resource(self.provider_db, "X", "initial", 0)

        parent, child = multiprocessing.Pipe(duplex=False)
        self.process = multiprocessing.Process(
            target=serve_http_cas_provider,
            args=(self.provider_db, self.provider_token, "provider-local", child),
            kwargs={"allow_test_faults": allow_test_faults},
            daemon=True,
        )
        self.process.start()
        child.close()
        if not parent.poll(5.0):
            self.close()
            raise RuntimeError("provider_start_timeout")
        port = parent.recv()
        parent.close()
        self.endpoint = f"http://127.0.0.1:{port}"

        self.kernel = HttpCasKernel(
            self.control_db,
            self.endpoint,
            kernel_token,
            provider_id,
            clock=lambda: 100,
            timeout=0.10,
        )
        self.observer = HttpCasObserver(
            self.endpoint,
            observer_token if observer_token is not None else kernel_token,
            provider_id,
            timeout=0.15,
        )
        self.adapter = HttpCasEffectAdapter(self.kernel, self.observer)
        self.reconciler = Reconciler(HttpCasReconciliationAdapter(self.kernel, self.observer))

        self.root = AuthorityRoot("root")
        self.principal = Principal("alice")
        self.context = AuthenticationContext("session-alice")
        self.intent = EffectIntent("intent.http", "http-cas")
        self.contract = EffectContract("contract.http", self.intent.intent_id)
        self.grant_id = "grant-alice"
        self.capability_id = "cap-X"
        self.kernel.add_authority_root(self.root)
        self.kernel.add_principal(self.principal)
        self.kernel.establish_authentication_context(self.context, self.principal)
        self.kernel.add_effect_intent(self.intent)
        self.kernel.add_effect_contract(self.contract)
        self.kernel.add_authority_grant(
            AuthorityGrant(
                self.grant_id,
                self.root.root_id,
                self.principal.principal_id,
                self.intent.intent_id,
            )
        )
        self.kernel.add_capability(Capability(self.capability_id, "X"))
        self.kernel.set_authorized_effect_envelope(
            self.contract.contract_id,
            self.kernel.possible_effects_for("X"),
        )
        auth = self.kernel.authorize(
            ActionRequest("request-direct", self.intent.intent_id, self.contract.contract_id),
            authentication_context=self.context,
        )
        if not auth.allowed:
            raise AssertionError(auth.reason)
        start = self.kernel.start_attempt(auth.authorization)
        if not start.allowed:
            raise AssertionError(start.reason)
        self.attempt = start.attempt

    def close(self) -> None:
        process = getattr(self, "process", None)
        if process is not None and process.is_alive():
            process.terminate()
            process.join(2.0)
        self.tempdir.cleanup()

    def operation(self, value: str = "after", *, expected_version: int = 0, effects="auto") -> HttpCasOperation:
        if effects == "auto":
            effects = self.kernel.possible_effects_for("X")
        return HttpCasOperation("X", expected_version, value, effects)

    def admit(self, operation: HttpCasOperation, *, capability_id: str | None = None, attempt=None):
        return self.kernel.admit_http_cas(attempt or self.attempt, capability_id or self.capability_id, operation)


class HttpCasThirdDomainTests(unittest.TestCase):
    def domain(self, **kwargs) -> HttpCasDomain:
        d = HttpCasDomain(**kwargs)
        self.addCleanup(d.close)
        return d

    def admitted(self, d: HttpCasDomain, operation: HttpCasOperation):
        result = d.admit(operation)
        self.assertTrue(result.allowed, result.reason)
        self.assertIsNotNone(result.admission)
        return result.admission

    def test_positive_http_cas_is_attributed_within_scope_and_satisfied(self) -> None:
        d = self.domain()
        op = d.operation("after")
        admission = self.admitted(d, op)
        result = d.adapter.execute(admission.admission_id)
        self.assertTrue(result.occurred, result.reason)
        observation = d.adapter.observe(op)
        self.assertTrue(d.adapter.did(admission, observation))
        compliance = d.adapter.assess_compliance(admission, observation, supported_possible_effects=op.possible_effects)
        self.assertEqual(compliance.status, "PASS")
        self.assertTrue(d.adapter.within_scope(compliance))
        self.assertTrue(d.adapter.satisfied(observation, ("after", 1)))
        self.assertTrue(d.adapter.has_control_completion(admission.admission_id))

    def test_unknown_and_underapproximated_effect_models_deny_before_transport(self) -> None:
        d = self.domain()
        unknown = d.admit(d.operation(effects=None))
        self.assertEqual((unknown.allowed, unknown.reason), (False, "unknown_possible_effects"))
        under = d.admit(d.operation(effects=frozenset({"MODIFY(X)"})))
        self.assertEqual((under.allowed, under.reason), (False, "effect_model_mismatch"))
        self.assertEqual(read_http_cas_resource_for_test(d.provider_db, "X"), ("initial", 0))

    def test_invalid_capability_mismatch_and_revocation_deny_before_transport(self) -> None:
        d = self.domain()
        d.kernel.set_capability_valid(d.capability_id, False)
        self.assertEqual(d.admit(d.operation()).reason, "capability_invalid")

        d2 = self.domain()
        d2.kernel.add_capability(Capability("cap-Y", "Y"))
        self.assertEqual(d2.admit(d2.operation(), capability_id="cap-Y").reason, "capability_resource_mismatch")

        d3 = self.domain()
        d3.kernel.set_grant_revoked(d3.grant_id, True)
        self.assertEqual(d3.admit(d3.operation()).reason, "authority_revoked")

    def test_effect_envelope_exceeded_denies(self) -> None:
        d = self.domain()
        d.kernel.set_authorized_effect_envelope(d.contract.contract_id, frozenset({"MODIFY(X)"}))
        result = d.admit(d.operation())
        self.assertEqual((result.allowed, result.reason), (False, "effect_envelope_exceeded"))

    def test_o1_admitted_cannot_be_replaced_by_o2(self) -> None:
        d = self.domain()
        op1 = d.operation("O1")
        admission = self.admitted(d, op1)
        op2 = d.operation("O2")
        self.assertNotEqual(op1.operation_digest, op2.operation_digest)
        result = d.adapter.execute(admission.admission_id)
        self.assertTrue(result.occurred, result.reason)
        observation = d.adapter.observe(op1)
        self.assertTrue(d.adapter.satisfied(observation, "O1"))
        self.assertFalse(d.adapter.satisfied(observation, "O2"))

    def test_admission_replay_denies_second_delivery(self) -> None:
        d = self.domain()
        op = d.operation("once")
        admission = self.admitted(d, op)
        self.assertTrue(d.adapter.execute(admission.admission_id).occurred)
        replay = d.adapter.execute(admission.admission_id)
        self.assertEqual((replay.occurred, replay.reason), (False, "admission_consumed"))
        self.assertEqual(read_http_cas_resource_for_test(d.provider_db, "X"), ("once", 1))

    def test_duplicate_transport_delivery_is_idempotent_at_provider(self) -> None:
        d = self.domain()
        op = d.operation("once")
        admission = self.admitted(d, op)
        result = d.adapter.execute(admission.admission_id, crash_point="duplicate_delivery")
        self.assertTrue(result.occurred, result.reason)
        self.assertEqual(read_http_cas_resource_for_test(d.provider_db, "X"), ("once", 1))
        self.assertEqual(d.reconciler.reconcile(admission, op).status, ReconciliationStatus.OCCURRED)

    def test_stale_expected_version_creates_terminal_provider_rejection_and_not_occurred(self) -> None:
        d = self.domain()
        op = d.operation("never", expected_version=7)
        admission = self.admitted(d, op)
        result = d.adapter.execute(admission.admission_id)
        self.assertEqual((result.occurred, result.reason), (False, "provider_rejected_stale"))
        reconciled = d.reconciler.reconcile(admission, op)
        self.assertEqual(
            (reconciled.status, reconciled.reason),
            (ReconciliationStatus.NOT_OCCURRED, "terminal_nonoccurrence_proof"),
        )
        self.assertEqual(read_http_cas_resource_for_test(d.provider_db, "X"), ("initial", 0))
        self.assertEqual(d.adapter.execute(admission.admission_id).reason, "admission_consumed")

    def test_response_lost_after_commit_reconciles_occurred_from_provider_state(self) -> None:
        d = self.domain()
        op = d.operation("committed")
        admission = self.admitted(d, op)
        result = d.adapter.execute(admission.admission_id, crash_point="response_lost_after_commit")
        self.assertEqual((result.occurred, result.reason), (False, "transport_uncertain"))
        self.assertFalse(d.adapter.has_control_completion(admission.admission_id))
        reconciled = d.reconciler.reconcile(admission, op)
        self.assertEqual(reconciled.status, ReconciliationStatus.OCCURRED)
        self.assertEqual(d.adapter.execute(admission.admission_id).reason, "admission_consumed")

    def test_timeout_before_provider_commit_is_indeterminate_then_becomes_occurred(self) -> None:
        d = self.domain()
        op = d.operation("late")
        admission = self.admitted(d, op)
        result = d.adapter.execute(admission.admission_id, crash_point="timeout_before_commit")
        self.assertEqual((result.occurred, result.reason), (False, "transport_uncertain"))
        first = d.reconciler.reconcile(admission, op)
        self.assertEqual(first.status, ReconciliationStatus.INDETERMINATE)
        time.sleep(0.45)
        second = d.reconciler.reconcile(admission, op)
        self.assertEqual(second.status, ReconciliationStatus.OCCURRED)

    def test_drop_before_provider_decision_is_indeterminate_not_false_not_occurred(self) -> None:
        d = self.domain()
        op = d.operation("unknown")
        admission = self.admitted(d, op)
        result = d.adapter.execute(admission.admission_id, crash_point="drop_before_decision")
        self.assertEqual((result.occurred, result.reason), (False, "transport_uncertain"))
        reconciled = d.reconciler.reconcile(admission, op)
        self.assertEqual(reconciled.status, ReconciliationStatus.INDETERMINATE)
        self.assertNotEqual(reconciled.status, ReconciliationStatus.NOT_OCCURRED)

    def test_execution_started_but_transport_never_sent_is_indeterminate_and_not_replayed(self) -> None:
        d = self.domain()
        op = d.operation("never-sent")
        admission = self.admitted(d, op)
        result = d.adapter.execute(admission.admission_id, crash_point="before_transport")
        self.assertEqual((result.occurred, result.reason), (False, "transport_not_sent"))
        self.assertEqual(read_http_cas_resource_for_test(d.provider_db, "X"), ("initial", 0))
        self.assertIsNone(d.observer.receipt(admission.admission_id))
        reconciled = d.reconciler.reconcile(admission, op)
        self.assertEqual(reconciled.status, ReconciliationStatus.INDETERMINATE)
        self.assertEqual(d.adapter.execute(admission.admission_id).reason, "admission_consumed")

    def test_forged_success_response_without_provider_state_does_not_create_did(self) -> None:
        d = self.domain()
        op = d.operation("forged")
        admission = self.admitted(d, op)
        result = d.adapter.execute(admission.admission_id, crash_point="forged_success_response")
        self.assertEqual((result.occurred, result.reason), (False, "provider_commit_unverified"))
        self.assertFalse(d.adapter.has_control_completion(admission.admission_id))
        observation = d.adapter.observe(op)
        self.assertFalse(d.adapter.did(admission, observation))
        reconciled = d.reconciler.reconcile(admission, op)
        self.assertEqual(reconciled.status, ReconciliationStatus.INDETERMINATE)
        self.assertEqual(read_http_cas_resource_for_test(d.provider_db, "X"), ("initial", 0))

    def test_fault_header_is_ignored_by_default_provider_mode(self) -> None:
        d = self.domain(allow_test_faults=False)
        op = d.operation("real-commit")
        admission = self.admitted(d, op)
        result = d.adapter.execute(admission.admission_id, crash_point="forged_success_response")
        self.assertTrue(result.occurred, result.reason)
        self.assertEqual(read_http_cas_resource_for_test(d.provider_db, "X"), ("real-commit", 1))
        self.assertEqual(d.reconciler.reconcile(admission, op).status, ReconciliationStatus.OCCURRED)

    def test_committed_receipt_without_matching_state_is_not_did(self) -> None:
        d = self.domain()
        op = d.operation("claimed")
        admission = self.admitted(d, op)
        inject_committed_receipt_without_state_for_test(
            d.provider_db,
            admission_id=admission.admission_id,
            operation_digest=admission.operation_digest,
            resource="X",
            expected_version=0,
            new_value="claimed",
        )
        observation = d.adapter.observe(op)
        self.assertFalse(d.adapter.did(admission, observation))
        result = d.reconciler.reconcile(admission, op)
        self.assertEqual(result.status, ReconciliationStatus.INDETERMINATE)

    def test_matching_state_without_admission_attribution_is_not_did(self) -> None:
        d = self.domain()
        op = d.operation("goal")
        admission = self.admitted(d, op)
        inject_unattributed_http_cas_change_for_test(d.provider_db, "X", "goal", 1)
        observation = d.adapter.observe(op)
        self.assertTrue(d.adapter.satisfied(observation, "goal"))
        self.assertFalse(d.adapter.did(admission, observation))
        self.assertEqual(d.reconciler.reconcile(admission, op).status, ReconciliationStatus.INDETERMINATE)

    def test_external_change_after_commit_invalidates_current_attribution(self) -> None:
        d = self.domain()
        op = d.operation("authorized")
        admission = self.admitted(d, op)
        self.assertTrue(d.adapter.execute(admission.admission_id).occurred)
        self.assertEqual(d.reconciler.reconcile(admission, op).status, ReconciliationStatus.OCCURRED)
        inject_unattributed_http_cas_change_for_test(d.provider_db, "X", "external", 2)
        later = d.reconciler.reconcile(admission, op)
        self.assertEqual(later.status, ReconciliationStatus.INDETERMINATE)

    def test_wrong_provider_credential_has_no_effect_and_no_terminal_claim(self) -> None:
        d = self.domain(kernel_token="wrong-token")
        op = d.operation("denied")
        admission = self.admitted(d, op)
        result = d.adapter.execute(admission.admission_id)
        self.assertEqual((result.occurred, result.reason), (False, "transport_uncertain"))
        self.assertEqual(read_http_cas_resource_for_test(d.provider_db, "X"), ("initial", 0))
        reconciled = d.reconciler.reconcile(admission, op)
        self.assertEqual(reconciled.status, ReconciliationStatus.INDETERMINATE)

    def test_wrong_provider_identity_rejects_response_and_observation(self) -> None:
        d = self.domain(provider_id="wrong-provider-id")
        op = d.operation("denied")
        admission = self.admitted(d, op)
        result = d.adapter.execute(admission.admission_id)
        self.assertEqual((result.occurred, result.reason), (False, "provider_response_mismatch"))
        reconciled = d.reconciler.reconcile(admission, op)
        self.assertEqual((reconciled.status, reconciled.reason), (ReconciliationStatus.INDETERMINATE, "observation_failed"))

    def test_runtime_and_p4_registry_drive_http_domain_through_same_common_path(self) -> None:
        d = self.domain()
        registry = TrustedBindingRegistry(
            (
                CapabilityBinding(
                    "binding-http",
                    d.intent.intent_id,
                    d.capability_id,
                    "X",
                    d.adapter,
                ),
            )
        )
        runtime = KernelRuntime(d.kernel, registry)
        op = d.operation("runtime")
        trace = runtime.run(
            ActionRequest("request-runtime", d.intent.intent_id, d.contract.contract_id),
            op,
            authentication_context=d.context,
        )
        self.assertTrue(trace.authorization.allowed)
        self.assertIsNotNone(trace.binding)
        self.assertTrue(trace.binding.allowed)
        self.assertIsNotNone(trace.admission)
        self.assertTrue(trace.admission.allowed)
        self.assertIsNotNone(trace.execution)
        self.assertTrue(trace.execution.occurred, trace.execution.reason)
        observation = d.adapter.observe(op)
        self.assertTrue(d.adapter.did(trace.admission.admission, observation))

    def test_operation_exposes_no_provider_url_or_credential_routing_fields(self) -> None:
        d = self.domain()
        op = d.operation("safe")
        self.assertEqual(set(op.__dataclass_fields__), {"resource", "expected_version", "new_value", "possible_effects"})
        self.assertFalse(hasattr(op, "provider"))
        self.assertFalse(hasattr(op, "url"))
        self.assertFalse(hasattr(op, "credential"))
        public_adapter = {name for name in dir(d.adapter) if not name.startswith("_")}
        self.assertTrue({"provider_token", "endpoint", "url", "credential"}.isdisjoint(public_adapter))

    def test_forged_attempt_and_missing_authentication_do_not_gain_http_effect_path(self) -> None:
        d = self.domain()
        forged = type(d.attempt)(
            d.attempt.attempt_id,
            d.attempt.authorization_id,
            "mallory",
            d.attempt.intent_id,
            d.attempt.contract_id,
        )
        denied = d.admit(d.operation("forged"), attempt=forged)
        self.assertEqual((denied.allowed, denied.reason), (False, "forged_attempt"))
        unauth = d.kernel.authorize(ActionRequest("request-no-auth", d.intent.intent_id, d.contract.contract_id))
        self.assertFalse(unauth.allowed)
        self.assertEqual(read_http_cas_resource_for_test(d.provider_db, "X"), ("initial", 0))

    def test_concurrent_same_expected_version_allows_one_commit_and_one_terminal_rejection(self) -> None:
        d = self.domain()
        a1 = self.admitted(d, d.operation("one"))
        a2 = self.admitted(d, d.operation("two"))
        barrier = threading.Barrier(3)
        results = []
        lock = threading.Lock()

        def run(admission_id: str) -> None:
            barrier.wait()
            result = d.adapter.execute(admission_id)
            with lock:
                results.append(result)

        t1 = threading.Thread(target=run, args=(a1.admission_id,))
        t2 = threading.Thread(target=run, args=(a2.admission_id,))
        t1.start(); t2.start(); barrier.wait(); t1.join(); t2.join()
        self.assertEqual(sum(r.occurred for r in results), 1)
        self.assertEqual(sum(r.reason == "provider_rejected_stale" for r in results), 1)
        self.assertEqual(read_http_cas_resource_for_test(d.provider_db, "X")[1], 1)

    def test_canonicalization_rejects_invalid_resource_without_normalizing_it_into_target(self) -> None:
        d = self.domain()
        bad = HttpCasOperation("X/../Y", 0, "bad", d.kernel.possible_effects_for("X/../Y"))
        denied = d.admit(bad)
        self.assertEqual((denied.allowed, denied.reason), (False, "invalid_operation"))
        self.assertEqual(read_http_cas_resource_for_test(d.provider_db, "X"), ("initial", 0))

    def test_canonicalization_preserves_value_bytes_and_distinguishes_semantics(self) -> None:
        d = self.domain()
        op1 = d.operation("line one\nline two  ")
        op2 = d.operation("line one\nline two")
        self.assertNotEqual(op1.canonical_bytes(), op2.canonical_bytes())
        self.assertNotEqual(op1.operation_digest, op2.operation_digest)
        admission = self.admitted(d, op1)
        self.assertTrue(d.adapter.execute(admission.admission_id).occurred)
        self.assertEqual(d.adapter.observe(op1).value, "line one\nline two  ")

    def test_missing_coverage_and_ambiguous_attribution_remain_indeterminate(self) -> None:
        d = self.domain()
        op = d.operation("done")
        admission = self.admitted(d, op)
        self.assertTrue(d.adapter.execute(admission.admission_id).occurred)
        missing = d.reconciler.reconcile(admission, op, covered=False)
        self.assertEqual((missing.status, missing.reason), (ReconciliationStatus.INDETERMINATE, "missing_coverage"))
        ambiguous = d.reconciler.reconcile(admission, op, attribution_ambiguous=True)
        self.assertEqual((ambiguous.status, ambiguous.reason), (ReconciliationStatus.INDETERMINATE, "ambiguous_attribution"))


if __name__ == "__main__":
    unittest.main()
