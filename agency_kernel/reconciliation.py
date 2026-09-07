from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Generic, Optional, Protocol, TypeVar, runtime_checkable

from .effect_seams import EffectObservation, EffectOperation
from .g2 import OperationAdmission
from .g3 import Kernel as G3Kernel, Observation as G3Observation, Observer as G3Observer, PutIfVersionOperation
from .g4 import GitObservation, GitObserver, GitTreeOperation, Kernel as G4Kernel


OperationT = TypeVar("OperationT", bound=EffectOperation)
ObservationT = TypeVar("ObservationT", bound=EffectObservation)


class ReconciliationStatus(str, Enum):
    """Outcome of reconciling one exact admitted operation.

    The status is deliberately not a compliance, authorization, satisfaction,
    or acceptance verdict.
    """

    OCCURRED = "OCCURRED"
    NOT_OCCURRED = "NOT_OCCURRED"
    INDETERMINATE = "INDETERMINATE"


@dataclass(frozen=True)
class ReconciliationResult(Generic[ObservationT]):
    """Stage-local reconciliation fact.

    observation may be absent when control/operation binding fails before the
    target is read.  There is intentionally no PASS, authorized, within_scope,
    satisfied, accepted, or retry field.
    """

    status: ReconciliationStatus
    reason: str
    observation: Optional[ObservationT] = None


@runtime_checkable
class ReconciliationAdapter(Protocol[OperationT, ObservationT]):
    """Read-only reconciliation projection for one effect domain.

    Implementations may read the trusted control ledger, observe the target, and
    establish attribution.  They do not admit operations, execute effects,
    select capabilities, retry effects, or create authority.
    """

    def admission_matches_ledger(self, admission: OperationAdmission) -> bool: ...

    def execution_started(self, admission_id: str) -> bool: ...

    def observe(
        self,
        operation: OperationT,
        *,
        covered: bool = True,
        attribution_ambiguous: bool = False,
    ) -> ObservationT: ...

    def did(self, admission: OperationAdmission, observation: ObservationT) -> bool: ...


class G3ReconciliationAdapter:
    """Read-only reconciliation projection over G3 control and target state."""

    __slots__ = ("_kernel", "_observer")

    def __init__(self, kernel: G3Kernel, observer: G3Observer) -> None:
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

    def observe(
        self,
        operation: PutIfVersionOperation,
        *,
        covered: bool = True,
        attribution_ambiguous: bool = False,
    ) -> G3Observation:
        return self._observer.observe(
            operation.resource,
            covered=covered,
            attribution_ambiguous=attribution_ambiguous,
        )

    def did(self, admission: OperationAdmission, observation: G3Observation) -> bool:
        return self._kernel.did(admission, observation)


class G4ReconciliationAdapter:
    """Read-only reconciliation projection over G4 control and target state."""

    __slots__ = ("_kernel", "_observer")

    def __init__(self, kernel: G4Kernel, observer: GitObserver) -> None:
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

    def observe(
        self,
        operation: GitTreeOperation,
        *,
        covered: bool = True,
        attribution_ambiguous: bool = False,
    ) -> GitObservation:
        if operation.protected_ref != self._kernel.protected_ref:
            raise ValueError("operation_target_mismatch")
        return self._observer.observe(
            covered=covered,
            attribution_ambiguous=attribution_ambiguous,
        )

    def did(self, admission: OperationAdmission, observation: GitObservation) -> bool:
        return self._kernel.did(admission, observation)


class Reconciler(Generic[OperationT, ObservationT]):
    """Read-only, no-retry reconciliation of one exact admission.

    OCCURRED requires both a durable execution-start fact and target-side
    attribution.  NOT_OCCURRED is deliberately narrower: it requires a durable
    exact admission for which execution never started.  Once execution has
    started, an unattributed or unchanged target is insufficient to prove
    historical non-occurrence and therefore remains INDETERMINATE.

    The API intentionally accepts no execution-result object.  Existing G3/G4
    execution results are constructible dataclasses and are not provenance-
    authenticated evidence; accepting them would permit forged NOT_OCCURRED.
    """

    __slots__ = ("_adapter",)

    def __init__(self, adapter: ReconciliationAdapter[OperationT, ObservationT]) -> None:
        if not isinstance(adapter, ReconciliationAdapter):
            raise TypeError("adapter_does_not_satisfy_reconciliation_contract")
        self._adapter = adapter

    def reconcile(
        self,
        admission: OperationAdmission,
        operation: OperationT,
        *,
        covered: bool = True,
        attribution_ambiguous: bool = False,
    ) -> ReconciliationResult[ObservationT]:
        try:
            if not self._adapter.admission_matches_ledger(admission):
                return ReconciliationResult(
                    ReconciliationStatus.INDETERMINATE,
                    "unbound_admission",
                )
        except Exception:
            return ReconciliationResult(
                ReconciliationStatus.INDETERMINATE,
                "control_evidence_unavailable",
            )

        # Never observe a caller-supplied replacement operation under an
        # admission for different canonical bytes.
        try:
            canonical = operation.canonical_bytes()
            operation_digest = operation.operation_digest
        except (TypeError, ValueError, UnicodeError):
            return ReconciliationResult(
                ReconciliationStatus.INDETERMINATE,
                "invalid_operation_for_reconciliation",
            )
        if (
            operation_digest != admission.operation_digest
            or canonical != admission.canonical_operation
        ):
            return ReconciliationResult(
                ReconciliationStatus.INDETERMINATE,
                "admission_operation_mismatch",
            )

        try:
            observation = self._adapter.observe(
                operation,
                covered=covered,
                attribution_ambiguous=attribution_ambiguous,
            )
        except Exception:
            return ReconciliationResult(
                ReconciliationStatus.INDETERMINATE,
                "observation_failed",
            )

        if not observation.covered:
            return ReconciliationResult(
                ReconciliationStatus.INDETERMINATE,
                "missing_coverage",
                observation,
            )
        if observation.attribution_ambiguous:
            return ReconciliationResult(
                ReconciliationStatus.INDETERMINATE,
                "ambiguous_attribution",
                observation,
            )

        try:
            started = self._adapter.execution_started(admission.admission_id)
        except Exception:
            return ReconciliationResult(
                ReconciliationStatus.INDETERMINATE,
                "control_evidence_unavailable",
                observation,
            )

        attributed = self._adapter.did(admission, observation)

        if attributed and not started:
            return ReconciliationResult(
                ReconciliationStatus.INDETERMINATE,
                "target_attribution_without_execution_start",
                observation,
            )
        if attributed:
            return ReconciliationResult(
                ReconciliationStatus.OCCURRED,
                "attributed_target_effect",
                observation,
            )
        if not started:
            return ReconciliationResult(
                ReconciliationStatus.NOT_OCCURRED,
                "execution_never_started",
                observation,
            )
        return ReconciliationResult(
            ReconciliationStatus.INDETERMINATE,
            "execution_started_without_attributed_effect",
            observation,
        )
