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
    satisfaction, acceptance, or a security verdict. It only names a record
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
    """Reference-only normalization of durable facts around one exact effect attempt.

    P9-R1 deliberately omits `binding_id`: the current TrustedBindingRegistry is
    immutable trusted composition state, but binding resolution is not persisted
    as a historical control-ledger event. Emitting that identifier as historical
    evidence would therefore invent provenance.

    Also deliberately absent: aggregate success/PASS, authorization truth, DID,
    WITHIN_SCOPE, SATISFIED, compliance, or acceptance fields. The object binds
    durable identities and current read-only evidence so later logic can derive
    claims without treating this container itself as authority.
    """

    domain_id: str
    request_id: str
    authorization_id: str
    attempt_id: str
    admission_id: str
    operation_digest: str
    capability_id: str
    target_identity: str
    domain_evidence: Optional[DomainEvidenceReference]
    observation: Optional[ObservationReference]
    reconciliation: ReconciliationReference


@dataclass(frozen=True)
class _DurableLineage:
    request_id: str
    authorization_id: str
    principal_id: str
    grant_id: str
    intent_id: str
    contract_id: str
    attempt_id: str
    admission: OperationAdmission
    capability_resource: str


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

    @property
    def control_kernel(self):
        return self._adapter._kernel

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

    @property
    def control_kernel(self):
        return self._adapter._kernel

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

    @property
    def control_kernel(self):
        return self._adapter._kernel

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
    """Normalize exact durable effect lineage using current read-only evidence.

    `collect(trace, operation)` remains available for a live runtime caller, but
    the trace is only a candidate description: every historical identifier used
    in the returned evidence is re-read from the trusted control ledger and the
    supplied trace is checked against that durable lineage.

    `collect_from_admission_id(admission_id, operation)` is the crash/restart
    path. It requires no transient RuntimeTrace and never calls execute/admit or
    retries an effect.
    """

    __slots__ = ("_producer",)

    def __init__(self, producer) -> None:
        if not isinstance(
            producer,
            (G3EvidenceProducer, G4EvidenceProducer, HttpCasEvidenceProducer),
        ):
            raise TypeError("invalid_effect_evidence_producer")
        self._producer = producer

    def _load_durable_lineage(self, admission_id: str) -> _DurableLineage:
        if not isinstance(admission_id, str) or not admission_id:
            raise ValueError("invalid_admission_id")

        kernel = self._producer.control_kernel
        try:
            connection = kernel._connect()
        except AttributeError as exc:
            raise RuntimeError("evidence_control_ledger_unavailable") from exc

        try:
            row = connection.execute(
                """
                SELECT
                    oa.admission_id,
                    oa.attempt_id AS admission_attempt_id,
                    oa.capability_id,
                    oa.operation_digest,
                    oa.canonical_operation,
                    cap.resource AS capability_resource,
                    a.authorization_id AS attempt_authorization_id,
                    a.principal_id AS attempt_principal_id,
                    a.intent_id AS attempt_intent_id,
                    a.contract_id AS attempt_contract_id,
                    aa.authorization_id,
                    aa.request_id,
                    aa.principal_id AS authorization_principal_id,
                    aa.grant_id,
                    aa.intent_id AS authorization_intent_id,
                    aa.contract_id AS authorization_contract_id,
                    ac.authorization_id AS consumed_authorization_id,
                    ac.attempt_id AS consumed_attempt_id,
                    s.attempt_id AS started_attempt_id
                FROM operation_admissions AS oa
                JOIN capabilities AS cap
                  ON cap.capability_id = oa.capability_id
                JOIN action_attempts AS a
                  ON a.attempt_id = oa.attempt_id
                JOIN action_authorizations AS aa
                  ON aa.authorization_id = a.authorization_id
                JOIN authorization_consumed AS ac
                  ON ac.authorization_id = aa.authorization_id
                 AND ac.attempt_id = a.attempt_id
                JOIN attempt_started AS s
                  ON s.attempt_id = a.attempt_id
                JOIN effect_contracts AS ec
                  ON ec.contract_id = a.contract_id
                 AND ec.intent_id = a.intent_id
                JOIN authority_grants AS ag
                  ON ag.grant_id = aa.grant_id
                 AND ag.principal_id = aa.principal_id
                 AND ag.intent_id = aa.intent_id
                WHERE oa.admission_id = ?
                """,
                (admission_id,),
            ).fetchone()
        finally:
            connection.close()

        if row is None:
            raise ValueError("durable_admission_lineage_absent")

        attempt_id = str(row["admission_attempt_id"])
        authorization_id = str(row["authorization_id"])
        principal_id = str(row["authorization_principal_id"])
        intent_id = str(row["authorization_intent_id"])
        contract_id = str(row["authorization_contract_id"])
        if (
            str(row["attempt_authorization_id"]) != authorization_id
            or str(row["attempt_principal_id"]) != principal_id
            or str(row["attempt_intent_id"]) != intent_id
            or str(row["attempt_contract_id"]) != contract_id
            or str(row["consumed_authorization_id"]) != authorization_id
            or str(row["consumed_attempt_id"]) != attempt_id
            or str(row["started_attempt_id"]) != attempt_id
        ):
            raise RuntimeError("durable_effect_lineage_inconsistent")

        canonical = row["canonical_operation"]
        if isinstance(canonical, memoryview):
            canonical = canonical.tobytes()
        elif not isinstance(canonical, bytes):
            canonical = bytes(canonical)

        admission = OperationAdmission(
            str(row["admission_id"]),
            attempt_id,
            str(row["capability_id"]),
            str(row["operation_digest"]),
            canonical,
        )
        return _DurableLineage(
            request_id=str(row["request_id"]),
            authorization_id=authorization_id,
            principal_id=principal_id,
            grant_id=str(row["grant_id"]),
            intent_id=intent_id,
            contract_id=contract_id,
            attempt_id=attempt_id,
            admission=admission,
            capability_resource=str(row["capability_resource"]),
        )

    def _validate_operation(self, lineage: _DurableLineage, operation) -> str:
        try:
            canonical = operation.canonical_bytes()
            operation_digest = operation.operation_digest
            target_identity = self._producer.target_identity(operation)
        except (AttributeError, TypeError, ValueError, UnicodeError) as exc:
            raise ValueError("invalid_operation_for_evidence") from exc

        admission = lineage.admission
        if (
            operation_digest != admission.operation_digest
            or canonical != admission.canonical_operation
        ):
            raise ValueError("admission_operation_mismatch")
        if target_identity != lineage.capability_resource:
            raise ValueError("evidence_target_mismatch")
        return target_identity

    def _collect_durable(
        self,
        lineage: _DurableLineage,
        operation,
        target_identity: str,
    ) -> EffectEvidence:
        admission = lineage.admission
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
            request_id=lineage.request_id,
            authorization_id=lineage.authorization_id,
            attempt_id=lineage.attempt_id,
            admission_id=admission.admission_id,
            operation_digest=admission.operation_digest,
            capability_id=admission.capability_id,
            target_identity=target_identity,
            domain_evidence=domain_ref,
            observation=observation_ref,
            reconciliation=reconciliation_ref,
        )

    def collect_from_admission_id(self, admission_id: str, operation) -> EffectEvidence:
        """Rehydrate evidence from durable admission identity without re-execution."""

        lineage = self._load_durable_lineage(admission_id)
        target_identity = self._validate_operation(lineage, operation)
        return self._collect_durable(lineage, operation, target_identity)

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
        ):
            raise ValueError("evidence_requires_admitted_runtime_trace")

        authorization = authorization_result.authorization
        binding = binding_result.binding
        attempt = start_result.attempt
        admission = admission_result.admission

        if binding.adapter is not self._producer.adapter:
            raise ValueError("producer_not_bound_to_runtime_adapter")

        lineage = self._load_durable_lineage(admission.admission_id)
        durable_admission = lineage.admission

        if trace.request_id != lineage.request_id:
            raise ValueError("trace_request_durable_mismatch")
        if (
            authorization.authorization_id != lineage.authorization_id
            or authorization.request_id != lineage.request_id
            or authorization.principal_id != lineage.principal_id
            or authorization.grant_id != lineage.grant_id
            or authorization.intent_id != lineage.intent_id
            or authorization.contract_id != lineage.contract_id
        ):
            raise ValueError("trace_authorization_durable_mismatch")
        if (
            attempt.attempt_id != lineage.attempt_id
            or attempt.authorization_id != lineage.authorization_id
            or attempt.principal_id != lineage.principal_id
            or attempt.intent_id != lineage.intent_id
            or attempt.contract_id != lineage.contract_id
        ):
            raise ValueError("trace_attempt_durable_mismatch")
        if (
            start_result.consumed.authorization_id != lineage.authorization_id
            or start_result.consumed.attempt_id != lineage.attempt_id
            or start_result.started.attempt_id != lineage.attempt_id
        ):
            raise ValueError("trace_start_durable_mismatch")
        if admission != durable_admission:
            raise ValueError("trace_admission_durable_mismatch")
        if (
            binding.intent_id != lineage.intent_id
            or binding.capability_id != durable_admission.capability_id
            or binding.target_identity != lineage.capability_resource
        ):
            raise ValueError("trace_binding_durable_scope_mismatch")

        target_identity = self._validate_operation(lineage, operation)
        return self._collect_durable(lineage, operation, target_identity)
