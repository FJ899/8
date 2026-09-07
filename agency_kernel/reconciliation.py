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
    """Stage-local reconciliation fact with no aggregate security verdict."""

    status: ReconciliationStatus
    reason: str
    observation: Optional[ObservationT] = None


@runtime_checkable
class ReconciliationAdapter(Protocol[OperationT, ObservationT]):
    """Read-only reconciliation projection for one effect domain.

    A terminal_not_occurred proof must mean that this exact admission can no
    longer produce the protected effect.  A mere observation that execution has
    not started yet is not such a proof.
    """

    def admission_matches_ledger(self, admission: OperationAdmission) -> bool: ...

    def execution_started(self, admission_id: str) -> bool: ...

    def terminal_not_occurred(
        self,
        admission: OperationAdmission,
        operation: OperationT,
        observation: ObservationT,
    ) -> bool: ...

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

    def terminal_not_occurred(
        self,
        admission: OperationAdmission,
        operation: PutIfVersionOperation,
        observation: G3Observation,
    ) -> bool:
        # G3 has no durable terminal no-effect record.  An unstarted admission
        # remains executable, while a started-but-unattributed admission may
        # have crashed before or after the target boundary.
        return False

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

    def terminal_not_occurred(
        self,
        admission: OperationAdmission,
        operation: GitTreeOperation,
        observation: GitObservation,
    ) -> bool:
        # G4 likewise has no durable terminal no-effect record.  An unchanged
        # ref is not historical proof: the admission may still be executable or
        # an already-started execution may have an uncertain outcome.
        return False

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

    OCCURRED requires a durable execution-start fact plus target-side
    attribution.  NOT_OCCURRED requires a domain-specific *terminal* durable
    proof that the exact admission cannot produce the effect now or later.

    Current G3/G4 do not possess such a terminal no-effect marker, so their
    non-attributed cases are deliberately INDETERMINATE.  The API also accepts
    no execution-result object because those result dataclasses are
    constructible and are not provenance-authenticated evidence.
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

        try:
            canonical = operation.canonical_bytes()
            operation_digest = operation.operation_digest
        except (TypeError, ValueError, UnicodeError):
            return ReconciliationResult(
                ReconciliationStatus.INDETERMINATE,
                "invalid_operation_for_reconciliation",
            )
        if operation_digest != admission.operation_digest or canonical != admission.canonical_operation:
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

        try:
            terminal_no_effect = self._adapter.terminal_not_occurred(
                admission,
                operation,
                observation,
            )
        except Exception:
            return ReconciliationResult(
                ReconciliationStatus.INDETERMINATE,
                "terminal_proof_unavailable",
                observation,
            )
        if terminal_no_effect:
            return ReconciliationResult(
                ReconciliationStatus.NOT_OCCURRED,
                "terminal_nonoccurrence_proof",
                observation,
            )
        if not started:
            return ReconciliationResult(
                ReconciliationStatus.INDETERMINATE,
                "execution_not_started_but_still_executable",
                observation,
            )
        return ReconciliationResult(
            ReconciliationStatus.INDETERMINATE,
            "execution_started_without_attributed_effect",
            observation,
        )
