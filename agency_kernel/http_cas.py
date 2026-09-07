from __future__ import annotations

import hashlib
import json
import socket
import urllib.error
import urllib.request
import uuid
from pathlib import Path
from typing import Any, FrozenSet, Optional

from .g1 import ActionAttempt
from .g2 import AdmissionResult, Kernel as G2Kernel, OperationAdmission
from .g3 import ComplianceResult
from .http_cas_provider import HttpCasObserver
from .http_cas_types import (
    HttpCasExecutionResult,
    HttpCasObservation,
    HttpCasOperation,
    decode_http_operation_payload,
    validate_loopback_endpoint,
)
from .target_instance import HistoricalTargetBinding, persist_operation_target_binding

_MAX_BODY = 65536


class Kernel(G2Kernel):
    """HTTP CAS effect domain using the existing authority/admission ledger."""

    def __init__(
        self,
        control_db: str | Path,
        endpoint: str,
        provider_token: str,
        provider_id: str,
        *,
        clock=None,
        timeout: float = 0.2,
    ) -> None:
        self._provider_endpoint = validate_loopback_endpoint(endpoint)
        if not isinstance(provider_token, str) or not provider_token:
            raise ValueError("invalid_provider_token")
        if not isinstance(provider_id, str) or not provider_id:
            raise ValueError("invalid_provider_id")
        self._provider_token = provider_token
        self.provider_id = provider_id
        self._provider_timeout = timeout
        super().__init__(control_db, Path(str(control_db) + ".unused-http-boundary"), clock=clock)
        with self._connect() as c:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS http_cas_execution_completions (
                    admission_id TEXT PRIMARY KEY REFERENCES operation_admissions(admission_id),
                    mutation_id TEXT NOT NULL,
                    completed_at INTEGER NOT NULL
                )
                """
            )

    @staticmethod
    def possible_effects_for(resource: str) -> FrozenSet[str]:
        return frozenset({f"MODIFY({resource})", f"PROVENANCE({resource})"})

    def has_control_completion(self, admission_id: str) -> bool:
        with self._connect() as c:
            return c.execute(
                "SELECT 1 FROM http_cas_execution_completions WHERE admission_id = ?",
                (admission_id,),
            ).fetchone() is not None

    def admit_http_cas(
        self,
        attempt: ActionAttempt,
        capability_id: str,
        operation: HttpCasOperation,
    ) -> AdmissionResult:
        try:
            canonical = operation.canonical_bytes()
        except (TypeError, ValueError, UnicodeError):
            return AdmissionResult(False, "invalid_operation")
        if operation.possible_effects is None:
            return AdmissionResult(False, "unknown_possible_effects")
        if operation.possible_effects != self.possible_effects_for(operation.resource):
            return AdmissionResult(False, "effect_model_mismatch")
        c = self._connect()
        try:
            c.execute("BEGIN IMMEDIATE")
            row = self._attempt_row(c, attempt.attempt_id)
            if row is None:
                c.execute("ROLLBACK")
                return AdmissionResult(False, "invalid_attempt")
            if (
                row["authorization_id"],
                row["principal_id"],
                row["intent_id"],
                row["contract_id"],
            ) != (
                attempt.authorization_id,
                attempt.principal_id,
                attempt.intent_id,
                attempt.contract_id,
            ):
                c.execute("ROLLBACK")
                return AdmissionResult(False, "forged_attempt")
            authority = self._specific_grant_status(
                c,
                row["grant_id"],
                row["principal_id"],
                row["intent_id"],
                int(self._clock()),
            )
            if not authority.allowed:
                c.execute("ROLLBACK")
                return AdmissionResult(False, authority.reason)
            cap = c.execute(
                "SELECT resource, valid FROM capabilities WHERE capability_id = ?",
                (capability_id,),
            ).fetchone()
            if cap is None:
                c.execute("ROLLBACK")
                return AdmissionResult(False, "capability_absent")
            if cap["valid"] is None:
                c.execute("ROLLBACK")
                return AdmissionResult(False, "unknown_capability_fact")
            if cap["valid"] != 1:
                c.execute("ROLLBACK")
                return AdmissionResult(False, "capability_invalid")
            if cap["resource"] != operation.resource:
                c.execute("ROLLBACK")
                return AdmissionResult(False, "capability_resource_mismatch")
            envelope = frozenset(
                r["effect"]
                for r in c.execute(
                    "SELECT effect FROM effect_envelopes WHERE contract_id = ?",
                    (row["contract_id"],),
                ).fetchall()
            )
            if not operation.possible_effects.issubset(envelope):
                c.execute("ROLLBACK")
                return AdmissionResult(False, "effect_envelope_exceeded")
            admission = OperationAdmission(
                str(uuid.uuid4()),
                attempt.attempt_id,
                capability_id,
                hashlib.sha256(canonical).hexdigest(),
                canonical,
            )
            c.execute(
                """
                INSERT INTO operation_admissions(
                    admission_id, attempt_id, capability_id, operation_digest, canonical_operation
                ) VALUES (?, ?, ?, ?, ?)
                """,
                (
                    admission.admission_id,
                    admission.attempt_id,
                    admission.capability_id,
                    admission.operation_digest,
                    admission.canonical_operation,
                ),
            )
            c.execute("COMMIT")
            return AdmissionResult(True, "admitted", admission)
        except BaseException:
            if c.in_transaction:
                c.execute("ROLLBACK")
            raise
        finally:
            c.close()

    @staticmethod
    def _decode_admitted(canonical: bytes, expected_digest: str):
        digest = hashlib.sha256(canonical).hexdigest()
        if digest != expected_digest:
            return None, "admission_digest_mismatch", digest
        try:
            payload = json.loads(canonical.decode("utf-8"))
            op = decode_http_operation_payload(payload)
            if op.canonical_bytes() != canonical:
                return None, "noncanonical_admitted_operation", digest
            return op, None, digest
        except (TypeError, ValueError, UnicodeDecodeError, json.JSONDecodeError, UnicodeError):
            return None, "invalid_admitted_operation", digest

    def _post_provider(self, admission_id: str, digest: str, op: HttpCasOperation, *, fault: str = "") -> dict[str, Any]:
        payload = {
            "admission_id": admission_id,
            "operation_digest": digest,
            "operation": json.loads(op.canonical_bytes().decode("utf-8")),
        }
        headers = {
            "Authorization": "Bearer " + self._provider_token,
            "Content-Type": "application/json",
        }
        if fault:
            headers["X-Agency-Kernel-Test-Fault"] = fault
        req = urllib.request.Request(
            self._provider_endpoint + "/cas",
            data=json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8"),
            headers=headers,
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=self._provider_timeout) as response:
                return json.loads(response.read(_MAX_BODY).decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code == 412:
                return json.loads(exc.read(_MAX_BODY).decode("utf-8"))
            raise

    def _provider_commit_is_observed(
        self,
        admission_id: str,
        digest: str,
        op: HttpCasOperation,
        mutation_id: str,
        after_version: int,
    ) -> bool:
        try:
            observer = HttpCasObserver(
                self._provider_endpoint,
                self._provider_token,
                self.provider_id,
                timeout=max(self._provider_timeout, 0.25),
            )
            observation = observer.observe(op.resource)
        except Exception:
            return False
        return (
            observation.admission_id == admission_id
            and observation.operation_digest == digest
            and observation.mutation_id == mutation_id
            and observation.value == op.new_value
            and observation.version == after_version
            and observation.receipt_status == "committed"
            and observation.receipt_mutation_id == mutation_id
            and observation.receipt_after_version == after_version
            and observation.receipt_value == op.new_value
        )

    def execute_http_cas_admission(
        self,
        admission_id: str,
        *,
        crash_point: Optional[str] = None,
    ) -> HttpCasExecutionResult:
        c = self._connect()
        try:
            c.execute("BEGIN IMMEDIATE")
            row = c.execute(
                "SELECT operation_digest, canonical_operation FROM operation_admissions WHERE admission_id = ?",
                (admission_id,),
            ).fetchone()
            if row is None:
                c.execute("ROLLBACK")
                return HttpCasExecutionResult(False, "admission_absent", "")
            if c.execute(
                "SELECT 1 FROM operation_admission_executions WHERE admission_id = ?",
                (admission_id,),
            ).fetchone() is not None:
                c.execute("ROLLBACK")
                return HttpCasExecutionResult(False, "admission_consumed", "")
            op, error, digest = self._decode_admitted(bytes(row["canonical_operation"]), str(row["operation_digest"]))
            if error is not None or op is None:
                c.execute("ROLLBACK")
                return HttpCasExecutionResult(False, error or "invalid_admitted_operation", "", operation_digest=digest)
            c.execute(
                "INSERT INTO operation_admission_executions(admission_id, executed_at) VALUES (?, ?)",
                (admission_id, int(self._clock())),
            )
            c.execute("COMMIT")
        except BaseException:
            if c.in_transaction:
                c.execute("ROLLBACK")
            raise
        finally:
            c.close()

        if crash_point == "before_transport":
            return HttpCasExecutionResult(False, "transport_not_sent", op.resource, operation_digest=digest)

        fault = {
            "response_lost_after_commit": "response_lost_after_commit",
            "timeout_before_commit": "delay_before_commit",
            "timeout_after_commit": "delay_after_commit",
            "drop_before_decision": "drop_before_decision",
            "forged_success_response": "forge_success_without_commit",
        }.get(crash_point or "", "")
        try:
            receipt = self._post_provider(admission_id, digest, op, fault=fault)
            if crash_point == "duplicate_delivery":
                second = self._post_provider(admission_id, digest, op)
                if second != receipt:
                    return HttpCasExecutionResult(False, "duplicate_delivery_conflict", op.resource, operation_digest=digest)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, socket.timeout, ConnectionError, OSError, json.JSONDecodeError, UnicodeDecodeError):
            return HttpCasExecutionResult(False, "transport_uncertain", op.resource, operation_digest=digest)

        if (
            receipt.get("provider_id") != self.provider_id
            or receipt.get("admission_id") != admission_id
            or receipt.get("operation_digest") != digest
            or receipt.get("resource") != op.resource
            or receipt.get("expected_version") != op.expected_version
            or receipt.get("new_value") != op.new_value
        ):
            return HttpCasExecutionResult(False, "provider_response_mismatch", op.resource, operation_digest=digest)

        status = receipt.get("status")
        if status == "rejected_stale":
            return HttpCasExecutionResult(
                False,
                "provider_rejected_stale",
                op.resource,
                digest,
                status,
                None,
                receipt.get("before_version"),
                receipt.get("after_version"),
            )
        if status != "committed" or not isinstance(receipt.get("mutation_id"), str):
            return HttpCasExecutionResult(False, "provider_response_invalid", op.resource, operation_digest=digest)

        mutation_id = str(receipt["mutation_id"])
        after_version = int(receipt["after_version"])
        if not self._provider_commit_is_observed(admission_id, digest, op, mutation_id, after_version):
            return HttpCasExecutionResult(
                False,
                "provider_commit_unverified",
                op.resource,
                digest,
                status,
                mutation_id,
                int(receipt["before_version"]),
                after_version,
            )
        with self._connect() as c:
            c.execute(
                "INSERT INTO http_cas_execution_completions(admission_id, mutation_id, completed_at) VALUES (?, ?, ?)",
                (admission_id, mutation_id, int(self._clock())),
            )
        return HttpCasExecutionResult(
            True,
            "executed",
            op.resource,
            digest,
            status,
            mutation_id,
            int(receipt["before_version"]),
            after_version,
        )

    def did(self, admission: OperationAdmission, observation: HttpCasObservation) -> bool:
        if observation.provider_id != self.provider_id or observation.mutation_id is None:
            return False
        if observation.admission_id != admission.admission_id or observation.operation_digest != admission.operation_digest:
            return False
        if (
            observation.receipt_status != "committed"
            or observation.receipt_mutation_id != observation.mutation_id
            or observation.receipt_after_version != observation.version
            or observation.receipt_value != observation.value
        ):
            return False
        with self._connect() as c:
            row = c.execute(
                "SELECT operation_digest FROM operation_admissions WHERE admission_id = ?",
                (admission.admission_id,),
            ).fetchone()
        return row is not None and str(row["operation_digest"]) == admission.operation_digest

    def assess_compliance(
        self,
        admission: OperationAdmission,
        observation: HttpCasObservation,
        *,
        supported_possible_effects: FrozenSet[str],
    ) -> ComplianceResult:
        if not observation.covered:
            return ComplianceResult("INDETERMINATE", "missing_coverage", frozenset(), supported_possible_effects)
        if observation.attribution_ambiguous:
            return ComplianceResult("INDETERMINATE", "ambiguous_attribution", frozenset(), supported_possible_effects)
        if not self.did(admission, observation):
            return ComplianceResult("INDETERMINATE", "unresolved_attribution", frozenset(), supported_possible_effects)
        actual = self.possible_effects_for(observation.resource)
        if not actual.issubset(supported_possible_effects):
            return ComplianceResult("FAIL", "effect_model_unsound", actual, supported_possible_effects)
        return ComplianceResult("PASS", "within_scope", actual, supported_possible_effects)

    @staticmethod
    def within_scope(compliance: ComplianceResult) -> bool:
        return compliance.status == "PASS"

    @staticmethod
    def satisfied(observation: HttpCasObservation, expected: Any) -> bool:
        if isinstance(expected, tuple) and len(expected) == 2:
            return (observation.value, observation.version) == expected
        return observation.value == expected


class HttpCasEffectAdapter:
    __slots__ = ("_kernel", "_observer")

    def __init__(self, kernel: Kernel, observer: HttpCasObserver) -> None:
        self._kernel = kernel
        self._observer = observer

    def target_identity(self, operation: HttpCasOperation) -> str:
        return operation.resource

    def historical_target_binding(self, operation: HttpCasOperation) -> HistoricalTargetBinding:
        return self._observer.historical_target_binding(operation.resource)

    def supported_possible_effects(self, operation: HttpCasOperation) -> FrozenSet[str]:
        return self._kernel.possible_effects_for(operation.resource)

    def admit(self, attempt: ActionAttempt, capability_id: str, operation: HttpCasOperation) -> AdmissionResult:
        result = self._kernel.admit_http_cas(attempt, capability_id, operation)
        if result.allowed:
            if result.admission is None:
                raise RuntimeError("allowed_admission_missing_object")
            persist_operation_target_binding(
                self._kernel,
                result.admission.admission_id,
                self.historical_target_binding(operation),
            )
        return result

    def execute(self, admission_id: str, *, crash_point: Optional[str] = None) -> HttpCasExecutionResult:
        return self._kernel.execute_http_cas_admission(admission_id, crash_point=crash_point)

    def observe(self, operation: HttpCasOperation, *, covered: bool = True, attribution_ambiguous: bool = False) -> HttpCasObservation:
        return self._observer.observe(operation.resource, covered=covered, attribution_ambiguous=attribution_ambiguous)

    def did(self, admission: OperationAdmission, observation: HttpCasObservation) -> bool:
        return self._kernel.did(admission, observation)

    def assess_compliance(
        self,
        admission: OperationAdmission,
        observation: HttpCasObservation,
        *,
        supported_possible_effects: FrozenSet[str],
    ) -> ComplianceResult:
        return self._kernel.assess_compliance(admission, observation, supported_possible_effects=supported_possible_effects)

    def within_scope(self, compliance: ComplianceResult) -> bool:
        return self._kernel.within_scope(compliance)

    def satisfied(self, observation: HttpCasObservation, expected: Any) -> bool:
        return self._kernel.satisfied(observation, expected)

    def has_control_completion(self, admission_id: str) -> bool:
        return self._kernel.has_control_completion(admission_id)


class HttpCasReconciliationAdapter:
    """P5 reconciliation projection for the HTTP provider's durable evidence."""

    __slots__ = ("_kernel", "_observer")

    def __init__(self, kernel: Kernel, observer: HttpCasObserver) -> None:
        self._kernel = kernel
        self._observer = observer

    def admission_matches_ledger(self, admission: OperationAdmission) -> bool:
        with self._kernel._connect() as c:
            row = c.execute(
                """
                SELECT attempt_id, capability_id, operation_digest, canonical_operation
                FROM operation_admissions WHERE admission_id = ?
                """,
                (admission.admission_id,),
            ).fetchone()
        return row is not None and (
            str(row["attempt_id"]) == admission.attempt_id
            and str(row["capability_id"]) == admission.capability_id
            and str(row["operation_digest"]) == admission.operation_digest
            and bytes(row["canonical_operation"]) == admission.canonical_operation
        )

    def execution_started(self, admission_id: str) -> bool:
        with self._kernel._connect() as c:
            return c.execute(
                "SELECT 1 FROM operation_admission_executions WHERE admission_id = ?",
                (admission_id,),
            ).fetchone() is not None

    def terminal_not_occurred(self, admission: OperationAdmission, operation: HttpCasOperation, observation: HttpCasObservation) -> bool:
        if not self.execution_started(admission.admission_id):
            return False
        receipt = self._observer.receipt(admission.admission_id)
        return receipt is not None and (
            receipt.provider_id == self._kernel.provider_id
            and receipt.admission_id == admission.admission_id
            and receipt.operation_digest == admission.operation_digest
            and receipt.resource == operation.resource
            and receipt.expected_version == operation.expected_version
            and receipt.new_value == operation.new_value
            and receipt.status == "rejected_stale"
            and receipt.mutation_id is None
        )

    def observe(self, operation: HttpCasOperation, *, covered: bool = True, attribution_ambiguous: bool = False) -> HttpCasObservation:
        return self._observer.observe(operation.resource, covered=covered, attribution_ambiguous=attribution_ambiguous)

    def did(self, admission: OperationAdmission, observation: HttpCasObservation) -> bool:
        return self._kernel.did(admission, observation)
