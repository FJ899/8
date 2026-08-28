from .g1 import (
    ActionAttempt,
    ActionAuthorization,
    ActionRequest,
    AttemptStarted,
    AuthenticationContext,
    AuthorityGrant,
    AuthorityRoot,
    AuthorizationConsumed,
    AuthorizationResult,
    EffectContract,
    EffectIntent,
    Kernel as _Kernel,
    MayResult,
    Principal,
    StartResult,
)


class Kernel(_Kernel):
    """G1 kernel with kernel-controlled trusted fixture identity provenance."""

    def __init__(self, *args, **kwargs):
        self._trusted_fixture_contexts = {}
        self._fixture_principal_contexts = {}
        super().__init__(*args, **kwargs)

    def establish_authentication_context(
        self,
        context: AuthenticationContext,
        principal: Principal,
        *,
        valid=True,
    ) -> None:
        super().establish_authentication_context(context, principal, valid=valid)
        self._trusted_fixture_contexts[id(context)] = context

    def add_principal(self, principal: Principal) -> None:
        super().add_principal(principal)
        context = AuthenticationContext(f"fixture:{id(principal)}:{id(self)}")
        self.establish_authentication_context(context, principal)
        self._fixture_principal_contexts[id(principal)] = context

    def _trusted_context(self, value):
        if isinstance(value, AuthenticationContext):
            registered = self._trusted_fixture_contexts.get(id(value))
            return value if registered is value else None
        if isinstance(value, Principal):
            return self._fixture_principal_contexts.get(id(value))
        return None

    def may(self, trusted_identity, request):
        return super().may(self._trusted_context(trusted_identity), request)

    def authorize(
        self,
        request: ActionRequest,
        *,
        authentication_context: AuthenticationContext | None = None,
        trusted_principal=None,
    ) -> AuthorizationResult:
        supplied = authentication_context if authentication_context is not None else trusted_principal
        return super().authorize(
            request,
            authentication_context=self._trusted_context(supplied),
        )


__all__ = [
    "ActionAttempt",
    "ActionAuthorization",
    "ActionRequest",
    "AttemptStarted",
    "AuthenticationContext",
    "AuthorityGrant",
    "AuthorityRoot",
    "AuthorizationConsumed",
    "AuthorizationResult",
    "EffectContract",
    "EffectIntent",
    "Kernel",
    "MayResult",
    "Principal",
    "StartResult",
]
