from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, is_dataclass
from typing import Optional

from .effect_seams import G3EffectAdapter, G4EffectAdapter
from .g2 import OperationAdmission
from .g3 import Observation as G3Observation
from .g4 import GitObservation
from .http_cas import HttpCasEffectAdapter, HttpCasReconciliationAdapter
from .http_cas_types import HttpCasObservation
from .reconciliation import (
    G3ReconciliationAdapter,
    G4ReconciliationAdapter,
    Reconciler,
    ReconciliationResult,
    ReconciliationStatus,
)
from .runtime import RuntimeTrace


@dataclass(frozen=True)
class DomainEvidenceReference:
    """Reference to one domain-native durable evidence record.

    This reference does not assert attribution, authorization, compliance,
    satisfaction, acceptance, or a security verdict.  It only names a record
    that later assurance logic may inspect independently.
    """

    kind: str
    record_id: str
    producer_identity: str


@dataclass(frozen=True)
class ObservationReference:
    """Content-addressed reference to the exact observation used in reconciliation."""

    kind: str
    digest: str


@dataclass(frozen=True)
class ReconciliationReference:
    """Reference to a stage-local reconciliation result, not a security verdict."""

    status: ReconciliationStatus
    reason: str
    observation_digest: Optional[str]


@dataclass(frozen=True)
class EffectEvidence:
    """Reference-only normalization of facts around one exact effect attempt.

    Deliberately absent: aggregate success/PASS, authorization truth, DID,
    WITHIN_SCOPE, SATISFIED, compliance, or acceptance fields.  The object binds
    identifiers and current read-only evidence so later logic can derive claims
    without treating this container itself as authority.
    """

    domain_id: str
    request_id: str
    authorization_id: str
    binding_id: str
    attempt_id: str
    admission_id: str
    operation_digest: str
    capability_id: str
    target_identity: str
    domain_evidence: Optional[DomainEvidenceReference]
    observation: Optional[ObservationReference]
    reconciliation: ReconciliationReference


def _observation_digest(kind: str, observation) -> str:
    if not is_dataclass(observation):
        raise TypeError("observation_is_not_dataclass")
    payload = {
        "kind": kind,
        "observation": asdict(observation),
    }
    canonical = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


class G3EvidenceProducer:
    """Evidence producer bound to one exact G3 adapter object."""

    __slots__ = ("_adapter", "_reconciler")
    domain_id = "g3-versioned-store"
    observation_kind = "g3_observation"

    def __init__(self, adapter: G3EffectAdapter) -> None:
        if not isinstance(adapter, G3EffectAdapter):
            raise TypeError("invalid_g3_evidence_adapter")
        self._adapter = adapter
        self._reconciler = Reconciler(
            G3ReconciliationAdapter(adapter._kernel, adapter._observer)
        )

    @property
    def adapter(self) -> G3EffectAdapter:
        return self._adapter

    def target_identity(self, operation) -> str:
        return self._adapter.target_identity(operation)

    def reconcile(self, admission: OperationAdmission, operation) -> ReconciliationResult:
        return self._reconciler.reconcile(admission, operation)

    def observation_reference(self, observation: G3Observation) -> ObservationReference:
        if not isinstance(observation, G3Observation):
            raise TypeError("g3_observation_type_mismatch")
        return ObservationReference(
            self.observation_kind,
            _observation_digest(self.observation_kind, observation),
        )

    def domain_evidence_reference(
        self,
        admission: OperationAdmission,
        observation: G3Observation,
    ) -> Optional[DomainEvidenceReference]:
        if not isinstance(observation, G3Observation):
            raise TypeError("g3_observation_type_mismatch")
        if observation.mutation_id is None:
            return None
        return DomainEvidenceReference(
            "g3_mutation_provenance",
            observation.mutation_id,
            "g3-target-store",
        )


class G4EvidenceProducer:
    """Evidence producer bound to one exact G4 adapter object."""

    __slots__ = ("_adapter", "_reconciler")
    domain_id = "g4-sanitized-git"
    observation_kind = "g4_git_observation"

    def __init__(self, adapter: G4EffectAdapter) -> None:
        if not isinstance(adapter, G4EffectAdapter):
            raise TypeError("invalid_g4_evidence_adapter")
        self._adapter = adapter
        self._reconciler = Reconciler(
            G4ReconciliationAdapter(adapter._kernel, adapter._observer)
        )

    @property
    def adapter(self) -> G4EffectAdapter:
        return self._adapter

    def target_identity(self, operation) -> str:
        return self._adapter.target_identity(operation)

    def reconcile(self, admission: OperationAdmission, operation) -> ReconciliationResult:
        return self._reconciler.reconcile(admission, operation)

    def observation_reference(self, observation: GitObservation) -> ObservationReference:
        if not isinstance(observation, GitObservation):
            raise TypeError("g4_observation_type_mismatch")
        return ObservationReference(
            self.observation_kind,
            _observation_digest(self.observation_kind, observation),
        )

    def domain_evidence_reference(
        self,
        admission: OperationAdmission,
        observation: GitObservation,
    ) -> Optional[DomainEvidenceReference]:
        if not isinstance(observation, GitObservation):
            raise TypeError("g4_observation_type_mismatch")
        if observation.commit_oid is None:
            return None
        return DomainEvidenceReference(
            "g4_git_commit",
            observation.commit_oid,
            observation.protected_ref,
        )


class HttpCasEvidenceProducer:
    """Evidence producer bound to one exact HTTP CAS adapter object."""

    __slots__ = ("_adapter", "_reconciler")
    domain_id = "http-cas"
    observation_kind = "http_cas_observation"

    def __init__(self, adapter: HttpCasEffectAdapter) -> None:
        if not isinstance(adapter, HttpCasEffectAdapter):
            raise TypeError("invalid_http_cas_evidence_adapter")
        self._adapter = adapter
        self._reconciler = Reconciler(
            HttpCasReconciliationAdapter(adapter._kernel, adapter._observer)
        )

    @property
    def adapter(self) -> HttpCasEffectAdapter:
        return self._adapter

    def target_identity(self, operation) -> str:
        return self._adapter.target_identity(operation)

    def reconcile(self, admission: OperationAdmission, operation) -> ReconciliationResult:
        return self._reconciler.reconcile(admission, operation)

    def observation_reference(self, observation: HttpCasObservation) -> ObservationReference:
        if not isinstance(observation, HttpCasObservation):
            raise TypeError("http_observation_type_mismatch")
        return ObservationReference(
            self.observation_kind,
            _observation_digest(self.observation_kind, observation),
        )

    def domain_evidence_reference(
        self,
        admission: OperationAdmission,
        observation: HttpCasObservation,
    ) -> Optional[DomainEvidenceReference]:
        if not isinstance(observation, HttpCasObservation):
            raise TypeError("http_observation_type_mismatch")

        try:
            receipt = self._adapter._observer.receipt(admission.admission_id)
        except Exception:
            receipt = None
        if receipt is not None and (
            receipt.provider_id == observation.provider_id
            and receipt.admission_id == admission.admission_id
            and receipt.operation_digest == admission.operation_digest
            and receipt.resource == observation.resource
        ):
            return DomainEvidenceReference(
                "http_provider_receipt",
                receipt.admission_id,
                receipt.provider_id,
            )
        if observation.mutation_id is not None:
            return DomainEvidenceReference(
                "http_provider_mutation",
                observation.mutation_id,
                observation.provider_id,
            )
        return None


class EffectEvidenceCollector:
    """Normalize one admitted runtime trace using current durable evidence.

    The collector accepts no caller-supplied observation, reconciliation,
    compliance, DID, or verdict.  It is bound to the exact adapter object used by
    trusted runtime composition and performs one read-only reconciliation when
    collect() is called.
    """

    __slots__ = ("_producer",)

    def __init__(self, producer) -> None:
        if not isinstance(
            producer,
            (G3EvidenceProducer, G4EvidenceProducer, HttpCasEvidenceProducer),
        ):
            raise TypeError("invalid_effect_evidence_producer")
        self._producer = producer

    def collect(self, trace: RuntimeTrace, operation) -> EffectEvidence:
        if not isinstance(trace, RuntimeTrace):
            raise TypeError("invalid_runtime_trace")

        authorization_result = trace.authorization
        binding_result = trace.binding
        start_result = trace.start
        admission_result = trace.admission
        if (
            not authorization_result.allowed
            or authorization_result.authorization is None
            or binding_result is None
            or not binding_result.allowed
            or binding_result.binding is None
            or start_result is None
            or not start_result.allowed
            or start_result.attempt is None
            or start_result.consumed is None
            or start_result.started is None
            or admission_result is None
            or not admission_result.allowed
            or admission_result.admission is None
            or trace.execution is None
        ):
            raise ValueError("evidence_requires_admitted_runtime_trace")

        authorization = authorization_result.authorization
        binding = binding_result.binding
        attempt = start_result.attempt
        admission = admission_result.admission

        if binding.adapter is not self._producer.adapter:
            raise ValueError("producer_not_bound_to_runtime_adapter")
        if authorization.request_id != trace.request_id:
            raise ValueError("trace_request_authorization_mismatch")
        if authorization.intent_id != binding.intent_id:
            raise ValueError("trace_authorization_binding_mismatch")
        if attempt.authorization_id != authorization.authorization_id:
            raise ValueError("trace_authorization_attempt_mismatch")
        if attempt.intent_id != authorization.intent_id or attempt.contract_id != authorization.contract_id:
            raise ValueError("trace_attempt_scope_mismatch")
        if admission.attempt_id != attempt.attempt_id:
            raise ValueError("trace_attempt_admission_mismatch")
        if admission.capability_id != binding.capability_id:
            raise ValueError("trace_binding_capability_mismatch")

        try:
            canonical = operation.canonical_bytes()
            operation_digest = operation.operation_digest
            target_identity = self._producer.target_identity(operation)
        except (AttributeError, TypeError, ValueError, UnicodeError) as exc:
            raise ValueError("invalid_operation_for_evidence") from exc
        if (
            operation_digest != admission.operation_digest
            or canonical != admission.canonical_operation
        ):
            raise ValueError("admission_operation_mismatch")
        if target_identity != binding.target_identity:
            raise ValueError("evidence_target_mismatch")

        reconciled = self._producer.reconcile(admission, operation)
        observation_ref: Optional[ObservationReference] = None
        domain_ref: Optional[DomainEvidenceReference] = None
        if reconciled.observation is not None:
            observation_ref = self._producer.observation_reference(reconciled.observation)
            domain_ref = self._producer.domain_evidence_reference(
                admission,
                reconciled.observation,
            )

        reconciliation_ref = ReconciliationReference(
            reconciled.status,
            reconciled.reason,
            None if observation_ref is None else observation_ref.digest,
        )

        return EffectEvidence(
            domain_id=self._producer.domain_id,
            request_id=trace.request_id,
            authorization_id=authorization.authorization_id,
            binding_id=binding.binding_id,
            attempt_id=attempt.attempt_id,
            admission_id=admission.admission_id,
            operation_digest=admission.operation_digest,
            capability_id=admission.capability_id,
            target_identity=target_identity,
            domain_evidence=domain_ref,
            observation=observation_ref,
            reconciliation=reconciliation_ref,
        )
