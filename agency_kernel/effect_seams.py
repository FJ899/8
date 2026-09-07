from __future__ import annotations

from dataclasses import dataclass
from typing import Any, FrozenSet, Optional, Protocol, TypeVar, runtime_checkable

from .g1 import ActionAttempt
from .g2 import AdmissionResult, OperationAdmission
from .g3 import (
    ComplianceResult,
    Kernel as G3Kernel,
    Observation as G3Observation,
    Observer as G3Observer,
    PutIfVersionOperation,
    PutResult,
)
from .g4 import (
    GitExecutionResult,
    GitObservation,
    GitObserver,
    GitTreeOperation,
    Kernel as G4Kernel,
)


@runtime_checkable
class EffectOperation(Protocol):
    """Minimal structural contract already shared by G3 and G4 operations."""

    possible_effects: Optional[FrozenSet[str]]

    def canonical_bytes(self) -> bytes: ...

    @property
    def operation_digest(self) -> str: ...


@runtime_checkable
class EffectExecutionResult(Protocol):
    """Common projection of an effect execution result."""

    occurred: bool
    reason: str


@runtime_checkable
class EffectObservation(Protocol):
    """Common attribution/coverage projection of a target observation."""

    admission_id: Optional[str]
    operation_digest: Optional[str]
    covered: bool
    attribution_ambiguous: bool


OperationT = TypeVar("OperationT", bound=EffectOperation)
ObservationT = TypeVar("ObservationT", bound=EffectObservation)
ExecutionT = TypeVar("ExecutionT", bound=EffectExecutionResult)


class EffectAdapter(Protocol[OperationT, ObservationT, ExecutionT]):
    """Smallest shared effect-domain seam justified by both G3 and G4.

    The seam does not own authority, capability selection, routing, or recovery
    policy. It only normalizes the already-existing per-domain operations needed
    by a later trusted runtime.
    """

    def target_identity(self, operation: OperationT) -> str: ...

    def supported_possible_effects(self, operation: OperationT) -> FrozenSet[str]: ...

    def admit(
        self,
        attempt: ActionAttempt,
        capability_id: str,
        operation: OperationT,
    ) -> AdmissionResult: ...

    def execute(
        self,
        admission_id: str,
        *,
        crash_point: Optional[str] = None,
    ) -> ExecutionT: ...

    def observe(
        self,
        operation: OperationT,
        *,
        covered: bool = True,
        attribution_ambiguous: bool = False,
    ) -> ObservationT: ...

    def did(self, admission: OperationAdmission, observation: ObservationT) -> bool: ...

    def assess_compliance(
        self,
        admission: OperationAdmission,
        observation: ObservationT,
        *,
        supported_possible_effects: FrozenSet[str],
    ) -> ComplianceResult: ...

    def within_scope(self, compliance: ComplianceResult) -> bool: ...

    def satisfied(self, observation: ObservationT, expected: Any) -> bool: ...

    def has_control_completion(self, admission_id: str) -> bool: ...


@dataclass(frozen=True)
class G3EffectAdapter:
    """Thin delegating seam over the existing G3 versioned-store domain."""

    kernel: G3Kernel
    observer: G3Observer

    def target_identity(self, operation: PutIfVersionOperation) -> str:
        return operation.resource

    def supported_possible_effects(self, operation: PutIfVersionOperation) -> FrozenSet[str]:
        return self.kernel.possible_effects_for(operation.resource)

    def admit(
        self,
        attempt: ActionAttempt,
        capability_id: str,
        operation: PutIfVersionOperation,
    ) -> AdmissionResult:
        return self.kernel.admit_put_if_version(attempt, capability_id, operation)

    def execute(
        self,
        admission_id: str,
        *,
        crash_point: Optional[str] = None,
    ) -> PutResult:
        return self.kernel.execute_put_if_version_admission(admission_id, crash_point=crash_point)

    def observe(
        self,
        operation: PutIfVersionOperation,
        *,
        covered: bool = True,
        attribution_ambiguous: bool = False,
    ) -> G3Observation:
        return self.observer.observe(
            operation.resource,
            covered=covered,
            attribution_ambiguous=attribution_ambiguous,
        )

    def did(self, admission: OperationAdmission, observation: G3Observation) -> bool:
        return self.kernel.did(admission, observation)

    def assess_compliance(
        self,
        admission: OperationAdmission,
        observation: G3Observation,
        *,
        supported_possible_effects: FrozenSet[str],
    ) -> ComplianceResult:
        return self.kernel.assess_compliance(
            admission,
            observation,
            supported_possible_effects=supported_possible_effects,
        )

    def within_scope(self, compliance: ComplianceResult) -> bool:
        return self.kernel.within_scope(compliance)

    def satisfied(self, observation: G3Observation, expected: Any) -> bool:
        return self.kernel.satisfied(observation, expected)

    def has_control_completion(self, admission_id: str) -> bool:
        return self.kernel.has_control_completion(admission_id)


@dataclass(frozen=True)
class G4EffectAdapter:
    """Thin delegating seam over the existing G4 sanitized-Git domain."""

    kernel: G4Kernel
    observer: GitObserver

    def target_identity(self, operation: GitTreeOperation) -> str:
        return operation.protected_ref

    def supported_possible_effects(self, operation: GitTreeOperation) -> FrozenSet[str]:
        return self.kernel.required_possible_effects(operation)

    def admit(
        self,
        attempt: ActionAttempt,
        capability_id: str,
        operation: GitTreeOperation,
    ) -> AdmissionResult:
        return self.kernel.admit_git_operation(attempt, capability_id, operation)

    def execute(
        self,
        admission_id: str,
        *,
        crash_point: Optional[str] = None,
    ) -> GitExecutionResult:
        return self.kernel.execute_git_admission(admission_id, crash_point=crash_point)

    def observe(
        self,
        operation: GitTreeOperation,
        *,
        covered: bool = True,
        attribution_ambiguous: bool = False,
    ) -> GitObservation:
        if operation.protected_ref != self.kernel.protected_ref:
            raise ValueError("operation_target_mismatch")
        return self.observer.observe(
            covered=covered,
            attribution_ambiguous=attribution_ambiguous,
        )

    def did(self, admission: OperationAdmission, observation: GitObservation) -> bool:
        return self.kernel.did(admission, observation)

    def assess_compliance(
        self,
        admission: OperationAdmission,
        observation: GitObservation,
        *,
        supported_possible_effects: FrozenSet[str],
    ) -> ComplianceResult:
        return self.kernel.assess_compliance(
            admission,
            observation,
            supported_possible_effects=supported_possible_effects,
        )

    def within_scope(self, compliance: ComplianceResult) -> bool:
        return self.kernel.within_scope(compliance)

    def satisfied(self, observation: GitObservation, expected: Any) -> bool:
        return self.kernel.satisfied(observation, expected)

    def has_control_completion(self, admission_id: str) -> bool:
        return self.kernel.has_control_completion(admission_id)
