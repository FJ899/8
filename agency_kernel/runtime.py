from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Optional, Protocol, TypeVar

from .effect_seams import EffectAdapter, EffectExecutionResult, EffectObservation, EffectOperation
from .g1 import (
    ActionRequest,
    AuthenticationContext,
    AuthorizationResult,
    StartResult,
)
from .g2 import AdmissionResult


OperationT = TypeVar("OperationT", bound=EffectOperation)
ObservationT = TypeVar("ObservationT", bound=EffectObservation)
ExecutionT = TypeVar("ExecutionT", bound=EffectExecutionResult)


class RuntimeAuthorityKernel(Protocol):
    """Authority operations consumed by KernelRuntime.

    The runtime deliberately depends on the existing G1 authority semantics
    rather than re-implementing MAY or authorization state.
    """

    def authorize(
        self,
        request: ActionRequest,
        *,
        authentication_context: AuthenticationContext | None = None,
    ) -> AuthorizationResult: ...

    def start_attempt(self, authorization) -> StartResult: ...


class RuntimeInvariantError(RuntimeError):
    """Trusted-component contract violation detected before a later stage runs."""


@dataclass(frozen=True)
class RuntimeTrace(Generic[ExecutionT]):
    """Stage-separated trace of one runtime invocation.

    This object intentionally has no aggregate PASS/success/authorized field.
    MAY/authorization, attempt creation, admission, and effect execution remain
    separate facts and must be interpreted separately by later assurance logic.
    """

    request_id: str
    authorization: AuthorizationResult
    start: Optional[StartResult] = None
    admission: Optional[AdmissionResult] = None
    execution: Optional[ExecutionT] = None


class KernelRuntime(Generic[OperationT, ObservationT, ExecutionT]):
    """One trusted orchestration path from authenticated request to one effect attempt.

    Adapter and capability are bound when the trusted runtime is composed.  They
    are never selected from ActionRequest or operation payload fields.  The
    runtime performs no retry and exposes no execute-admission continuation API.
    """

    __slots__ = ("_kernel", "_adapter", "_capability_id")

    def __init__(
        self,
        kernel: RuntimeAuthorityKernel,
        adapter: EffectAdapter[OperationT, ObservationT, ExecutionT],
        capability_id: str,
    ) -> None:
        if not isinstance(adapter, EffectAdapter):
            raise TypeError("adapter_does_not_satisfy_effect_contract")
        if not isinstance(capability_id, str) or not capability_id:
            raise ValueError("invalid_capability_binding")
        self._kernel = kernel
        self._adapter = adapter
        self._capability_id = capability_id

    def run(
        self,
        request: ActionRequest,
        operation: OperationT,
        *,
        authentication_context: AuthenticationContext | None,
    ) -> RuntimeTrace[ExecutionT]:
        """Execute exactly one linear authorization/admission/effect path.

        A denied pre-effect stage terminates the invocation.  If trusted code
        reports an allowed stage without the corresponding durable object, the
        runtime raises RuntimeInvariantError rather than advancing.
        """

        authorization = self._kernel.authorize(
            request,
            authentication_context=authentication_context,
        )
        if not authorization.allowed:
            return RuntimeTrace(request.request_id, authorization)
        if authorization.authorization is None:
            raise RuntimeInvariantError("authorization_missing_durable_object")

        start = self._kernel.start_attempt(authorization.authorization)
        if not start.allowed:
            return RuntimeTrace(request.request_id, authorization, start)
        if start.attempt is None or start.consumed is None or start.started is None:
            raise RuntimeInvariantError("attempt_start_missing_durable_objects")

        admission = self._adapter.admit(
            start.attempt,
            self._capability_id,
            operation,
        )
        if not admission.allowed:
            return RuntimeTrace(request.request_id, authorization, start, admission)
        if admission.admission is None:
            raise RuntimeInvariantError("admission_missing_durable_object")

        execution = self._adapter.execute(admission.admission.admission_id)
        return RuntimeTrace(
            request.request_id,
            authorization,
            start,
            admission,
            execution,
        )
