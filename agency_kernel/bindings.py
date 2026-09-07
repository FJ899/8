from __future__ import annotations

from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Mapping, Optional

from .effect_seams import EffectAdapter
from .g1 import ActionAuthorization


@dataclass(frozen=True)
class CapabilityBinding:
    """Trusted composition binding from one authorized intent to one effect path."""

    binding_id: str
    intent_id: str
    capability_id: str
    target_identity: str
    adapter: EffectAdapter

    def __post_init__(self) -> None:
        for name, value in (
            ("binding_id", self.binding_id),
            ("intent_id", self.intent_id),
            ("capability_id", self.capability_id),
            ("target_identity", self.target_identity),
        ):
            if not isinstance(value, str) or not value:
                raise ValueError(f"invalid_{name}")
        if not isinstance(self.adapter, EffectAdapter):
            raise TypeError("adapter_does_not_satisfy_effect_contract")


@dataclass(frozen=True)
class BindingResult:
    allowed: bool
    reason: str
    binding: Optional[CapabilityBinding] = None


@dataclass(frozen=True)
class TrustedBindingRegistry:
    """Immutable trusted mapping from persisted authorization intent to capability binding.

    The registry has no mutation API.  A duplicate binding ID or duplicate intent is
    rejected at construction time so runtime resolution is total-or-absent rather
    than order-dependent.
    """

    bindings: tuple[CapabilityBinding, ...]
    _by_intent: Mapping[str, CapabilityBinding] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        by_intent: dict[str, CapabilityBinding] = {}
        binding_ids: set[str] = set()
        for binding in self.bindings:
            if not isinstance(binding, CapabilityBinding):
                raise TypeError("invalid_capability_binding")
            if binding.binding_id in binding_ids:
                raise ValueError("duplicate_binding_id")
            if binding.intent_id in by_intent:
                raise ValueError("duplicate_binding_intent")
            binding_ids.add(binding.binding_id)
            by_intent[binding.intent_id] = binding
        object.__setattr__(self, "_by_intent", MappingProxyType(by_intent))

    def resolve(self, authorization: ActionAuthorization) -> BindingResult:
        if not isinstance(authorization, ActionAuthorization):
            return BindingResult(False, "invalid_binding_authorization")
        binding = self._by_intent.get(authorization.intent_id)
        if binding is None:
            return BindingResult(False, "binding_absent")
        return BindingResult(True, "binding_resolved", binding)
