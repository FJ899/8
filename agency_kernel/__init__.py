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
    """G1 kernel with trusted fixture identity provenance compatibility.

    A Principal becomes usable as the G1 trusted fixture premise only when that
    exact object was registered with this Kernel via add_principal(). Merely
    constructing another Principal with the same principal_id establishes no
    authenticated provenance. authorize() resolves MAY through the resulting
    kernel-controlled AuthenticationContext rather than through caller identity
    data or ActionRequest.
    """

    def __init__(self, *args, **kwargs):
        self._fixture_authentication_contexts = {}
        super().__init__(*args, **kwargs)

    def add_principal(self, principal: Principal) -> None:
        super().add_principal(principal)
        context = AuthenticationContext(f"fixture:{id(principal)}")
        self.establish_authentication_context(context, principal)
        self._fixture_authentication_contexts[id(principal)] = context

    def _fixture_context(self, principal):
        if not isinstance(principal, Principal):
            return None
        return self._fixture_authentication_contexts.get(id(principal))

    def may(self, trusted_identity, request):
        if isinstance(trusted_identity, AuthenticationContext):
            context = trusted_identity
        else:
            context = self._fixture_context(trusted_identity)
        return super().may(context, request)

    def authorize(
        self,
        request: ActionRequest,
        *,
        authentication_context: AuthenticationContext | None = None,
        trusted_principal=None,
    ) -> AuthorizationResult:
        context = authentication_context
        if context is None and trusted_principal is not None:
            context = self._fixture_context(trusted_principal)
        return super().authorize(request, authentication_context=context)


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
