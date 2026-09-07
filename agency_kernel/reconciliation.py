from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Generic, Optional, Protocol, TypeVar, runtime_checkable

from .effect_seams import (
    EffectExecutionResult,
    EffectObservation,
    EffectOperation,
    G3EffectAdapter,
    G4EffectAdapter,
)
from .g2 import OperationAdmission
from .g3 import Observation as G3Observation, PutIfVersionOperation, PutResult
from .g4 import GitExecutionResult, GitObservation, GitTreeOperation


OperationT = TypeVar("OperationT", bound=EffectOperation)
ObservationT = TypeVar("ObservationT", bound=EffectObservation)
ExecutionT = TypeVar("ExecutionT", bound=EffectExecutionResult)


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

    observation may be absent only when exact admission/operation binding fails
    before the target is read.  There is intentionally no PASS, authorized,
    within_scope, satisfied, or retry field.
    """

    status: ReconciliationStatus
    reason: str
    observation: Optional[ObservationT] = None


@runtime_checkable
class ReconciliationAdapter(Protocol[OperationT, ObservationT, ExecutionT]):
    """Read-only reconciliation projection for one effect domain.

    Implementations may observe and attribute.  They do not admit operations,
    execute effects, select capabilities, or create authority.
    """

    def observe(
        self,
        operation: OperationT,
        *,
        covered: bool = True,
        attribution_ambiguous: bool = False,
    ) -> ObservationT: ...

    def did(self, admission: OperationAdmission, observation: ObservationT) -> bool: ...

    def execution_proves_not_occurred(
        self,
        admission: OperationAdmission,
        operation: OperationT,
        execution: ExecutionT,
    ) -> bool: ...


class G3ReconciliationAdapter:
    """Conservative reconciliation projection over the existing G3 adapter."""

    __slots__ = ("_effect",)

    _NOT_OCCURRED_REASONS = frozenset(
        {
            "stale_version",
            "crash_after_admission_before_mutation",
            "crash_before_mutation",
        }
    )

    def __init__(self, effect_adapter: G3EffectAdapter) -> None:
        self._effect = effect_adapter

    def observe(
        self,
        operation: PutIfVersionOperation,
        *,
        covered: bool = True,
        attribution_ambiguous: bool = False,
    ) -> G3Observation:
        return self._effect.observe(
            operation,
            covered=covered,
            attribution_ambiguous=attribution_ambiguous,
        )

    def did(self, admission: OperationAdmission, observation: G3Observation) -> bool:
        return self._effect.did(admission, observation)

    def execution_proves_not_occurred(
        self,
        admission: OperationAdmission,
        operation: PutIfVersionOperation,
        execution: PutResult,
    ) -> bool:
        return (
            not execution.occurred
            and execution.reason in self._NOT_OCCURRED_REASONS
            and execution.operation_digest == admission.operation_digest
            and operation.operation_digest == admission.operation_digest
            and execution.resource == operation.resource
        )


class G4ReconciliationAdapter:
    """Conservative reconciliation projection over the existing G4 adapter."""

    __slots__ = ("_effect",)

    _NOT_OCCURRED_REASONS = frozenset(
        {
            "stale_ref",
            "no_target_change",
            "crash_before_ref_cas",
        }
    )

    def __init__(self, effect_adapter: G4EffectAdapter) -> None:
        self._effect = effect_adapter

    def observe(
        self,
        operation: GitTreeOperation,
        *,
        covered: bool = True,
        attribution_ambiguous: bool = False,
    ) -> GitObservation:
        return self._effect.observe(
            operation,
            covered=covered,
            attribution_ambiguous=attribution_ambiguous,
        )

    def did(self, admission: OperationAdmission, observation: GitObservation) -> bool:
        return self._effect.did(admission, observation)

    def execution_proves_not_occurred(
        self,
        admission: OperationAdmission,
        operation: GitTreeOperation,
        execution: GitExecutionResult,
    ) -> bool:
        return (
            not execution.occurred
            and execution.reason in self._NOT_OCCURRED_REASONS
            and execution.operation_digest == admission.operation_digest
            and operation.operation_digest == admission.operation_digest
            and execution.protected_ref == operation.protected_ref
        )


class Reconciler(Generic[OperationT, ObservationT, ExecutionT]):
    """Read-only, no-retry reconciliation of one exact admission.

    Target-side attribution is required for OCCURRED.  NOT_OCCURRED requires a
    trusted domain result whose reason is known to occur before the protected
    effect boundary.  An unchanged target without such a result is insufficient:
    history may be unknown, so the outcome remains INDETERMINATE.
    """

    __slots__ = ("_adapter",)

    def __init__(self, adapter: ReconciliationAdapter[OperationT, ObservationT, ExecutionT]) -> None:
        if not isinstance(adapter, ReconciliationAdapter):
            raise TypeError("adapter_does_not_satisfy_reconciliation_contract")
        self._adapter = adapter

    def reconcile(
        self,
        admission: OperationAdmission,
        operation: OperationT,
        *,
        execution: Optional[ExecutionT] = None,
        covered: bool = True,
        attribution_ambiguous: bool = False,
    ) -> ReconciliationResult[ObservationT]:
        # Never observe a caller-supplied replacement operation under an
        # admission for different canonical bytes.
        try:
            operation_digest = operation.operation_digest
        except (TypeError, ValueError, UnicodeError):
            return ReconciliationResult(
                ReconciliationStatus.INDETERMINATE,
                "invalid_operation_for_reconciliation",
            )
        if operation_digest != admission.operation_digest:
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
        except (TypeError, ValueError, RuntimeError, UnicodeError):
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

        attributed = self._adapter.did(admission, observation)

        if execution is None:
            if attributed:
                return ReconciliationResult(
                    ReconciliationStatus.OCCURRED,
                    "attributed_target_effect",
                    observation,
                )
            return ReconciliationResult(
                ReconciliationStatus.INDETERMINATE,
                "unresolved_outcome",
                observation,
            )

        execution_digest = getattr(execution, "operation_digest", None)
        if execution_digest != admission.operation_digest:
            return ReconciliationResult(
                ReconciliationStatus.INDETERMINATE,
                "execution_admission_mismatch",
                observation,
            )

        if execution.occurred:
            if attributed:
                return ReconciliationResult(
                    ReconciliationStatus.OCCURRED,
                    "attributed_target_effect",
                    observation,
                )
            return ReconciliationResult(
                ReconciliationStatus.INDETERMINATE,
                "execution_effect_not_attributed",
                observation,
            )

        if attributed:
            return ReconciliationResult(
                ReconciliationStatus.INDETERMINATE,
                "conflicting_execution_and_target_evidence",
                observation,
            )

        if self._adapter.execution_proves_not_occurred(admission, operation, execution):
            return ReconciliationResult(
                ReconciliationStatus.NOT_OCCURRED,
                "trusted_pre_effect_result",
                observation,
            )

        return ReconciliationResult(
            ReconciliationStatus.INDETERMINATE,
            "execution_result_not_sufficient",
            observation,
        )
