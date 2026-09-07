from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Optional, Protocol, TypeVar

from .bindings import BindingResult, CapabilityBinding, TrustedBindingRegistry
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
    Authorization, trusted binding, attempt creation, admission, and effect
    execution remain separate facts for later assurance logic.
    """

    request_id: str
    authorization: AuthorizationResult
    binding: Optional[BindingResult] = None
    start: Optional[StartResult] = None
    admission: Optional[AdmissionResult] = None
    execution: Optional[ExecutionT] = None


class KernelRuntime(Generic[OperationT, ObservationT, ExecutionT]):
    """One trusted orchestration path from authenticated request to one effect attempt.

    P4 supports two trusted composition modes without exposing a routing surface:

    * the P3 fixed mode keeps one adapter/capability pair fixed at construction;
    * the P4 registry mode resolves one immutable CapabilityBinding only from the
      persisted successful ActionAuthorization.intent_id.

    Neither mode reads adapter IDs, capability IDs, providers, or resource routing
    hints from ActionRequest.  The runtime performs no retry and exposes no
    execute-admission continuation API.
    """

    __slots__ = (
        "_kernel",
        "_registry",
        "_fixed_adapter",
        "_fixed_capability_id",
    )

    def __init__(
        self,
        kernel: RuntimeAuthorityKernel,
        binding_source,
        capability_id: Optional[str] = None,
    ) -> None:
        self._kernel = kernel
        if isinstance(binding_source, TrustedBindingRegistry):
            if capability_id is not None:
                raise ValueError("registry_mode_rejects_fixed_capability")
            self._registry = binding_source
            self._fixed_adapter = None
            self._fixed_capability_id = None
            return

        if not isinstance(binding_source, EffectAdapter):
            raise TypeError("invalid_runtime_binding_source")
        if not isinstance(capability_id, str) or not capability_id:
            raise ValueError("invalid_capability_binding")
        self._registry = None
        self._fixed_adapter = binding_source
        self._fixed_capability_id = capability_id

    def _resolve_binding(
        self,
        authorization,
        operation: OperationT,
    ) -> tuple[BindingResult, Optional[EffectAdapter], Optional[str]]:
        if self._registry is None:
            if self._fixed_adapter is None or self._fixed_capability_id is None:
                raise RuntimeInvariantError("fixed_binding_missing")
            return (
                BindingResult(True, "composition_fixed"),
                self._fixed_adapter,
                self._fixed_capability_id,
            )

        result = self._registry.resolve(authorization)
        if not result.allowed:
            return result, None, None
        binding = result.binding
        if binding is None:
            raise RuntimeInvariantError("binding_resolution_missing_object")
        adapter = binding.adapter
        try:
            actual_target = adapter.target_identity(operation)
        except (AttributeError, TypeError, ValueError):
            return (
                BindingResult(False, "binding_operation_mismatch", binding),
                None,
                None,
            )
        if actual_target != binding.target_identity:
            return (
                BindingResult(False, "binding_target_mismatch", binding),
                None,
                None,
            )
        return result, adapter, binding.capability_id

    def run(
        self,
        request: ActionRequest,
        operation: OperationT,
        *,
        authentication_context: AuthenticationContext | None,
    ) -> RuntimeTrace[ExecutionT]:
        """Execute exactly one linear authorization/binding/admission/effect path.

        A denied pre-effect stage terminates the invocation.  Registry resolution
        occurs only after successful authorization and is keyed by the durable
        authorization object, never by untrusted routing fields.  If trusted code
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

        binding_result, adapter, capability_id = self._resolve_binding(
            authorization.authorization,
            operation,
        )
        if not binding_result.allowed:
            return RuntimeTrace(
                request_id=request.request_id,
                authorization=authorization,
                binding=binding_result,
            )
        if adapter is None or capability_id is None:
            raise RuntimeInvariantError("binding_missing_effect_path")

        start = self._kernel.start_attempt(authorization.authorization)
        if not start.allowed:
            return RuntimeTrace(
                request_id=request.request_id,
                authorization=authorization,
                binding=binding_result,
                start=start,
            )
        if start.attempt is None or start.consumed is None or start.started is None:
            raise RuntimeInvariantError("attempt_start_missing_durable_objects")

        admission = adapter.admit(
            start.attempt,
            capability_id,
            operation,
        )
        if not admission.allowed:
            return RuntimeTrace(
                request_id=request.request_id,
                authorization=authorization,
                binding=binding_result,
                start=start,
                admission=admission,
            )
        if admission.admission is None:
            raise RuntimeInvariantError("admission_missing_durable_object")

        execution = adapter.execute(admission.admission.admission_id)
        return RuntimeTrace(
            request_id=request.request_id,
            authorization=authorization,
            binding=binding_result,
            start=start,
            admission=admission,
            execution=execution,
        )
