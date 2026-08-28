# G1 Contract — Semantic Integrity

Status: **PREREGISTERED / FROZEN BEFORE IMPLEMENTATION**

## Candidate binding

- `BASE` = Human-accepted PR #0 exact HEAD/tree.
- `CANDIDATE` = exact HEAD/tree of PR #1 presented for G1 audit.
- Allowed delta = only the implementation, tests, and evidence machinery explicitly required by G1 scope.


Any modification of the accepted base outside the preregistered Gate scope must be explicitly identified in candidate evidence. An undisclosed or unjustified out-of-scope delta blocks Gate acceptance.


## Claim under attack

**Claim A — Semantic Enforcement, authority-semantic subset**

G1 does not claim to validate semantic relations that do not yet exist in the candidate.

## Scope

G1 implements only enough state and logic for:

`request → MAY → ActionAuthorization → AuthorizationConsumed → durable AttemptStarted`

Expected minimal implementation areas:

- `Principal`
- `AuthorityRoot`
- `AuthorityGrant`
- `EffectIntent`
- `EffectContract`
- `ActionRequest`
- `ActionAuthorization`
- `AuthorizationConsumed`
- `ActionAttempt`
- minimal durable ledger/projection semantics
- `authorize()`
- atomic single-use consume + attempt start

A minimal inert `Capability` representation / `CAN` evaluator may exist solely to test that technical capability does not create normative authority. It must not execute effects or introduce the G2 capability boundary.

G1 must not grow into the full effect-execution system.

## Attack classes

At minimum:

- request content attempts to self-authorize;
- invalid/expired/revoked grant attempts to authorize;
- untrusted input attempts to create proof-bearing authority state;
- forged `ActionAuthorization`;
- replay of `ActionAuthorization`;
- double-consume authorization;
- attempt to start after authority becomes invalid where start semantics require active authority;
- if inert `Capability/CAN` exists: `CAN → MAY` substitution attempt.

The following global Claim A attacks are **not claimed by G1** because their semantics do not yet exist non-vacuously:

- `DID → AUTHORIZED`;
- `ATTEMPTED → EFFECT`;
- `SATISFIED → AUTHORIZED`;
- `SATISFIED → WITHIN_SCOPE`.

They are preregistered for G3 and repeated in G4.

## Expected fail semantics

Invalid semantic substitutions and invalid authority transitions must not create trusted proof-bearing state.

Unknown pre-effect authority facts → `DENY`.

Double consumption/replay → `DENY` or invariant-enforced conflict, never a second valid attempt.

## Exit criteria

G1 may be proposed for Human acceptance only after:

- fixed exact candidate HEAD/tree;
- preregistered G1 subset tests executed;
- fresh-context adversarial audit completed;
- every failure recorded first as a durable finding;
- no OPEN finding currently falsifies the G1 authority-semantic subset of Claim A for the candidate.

A green test suite alone is insufficient.

## Out of scope

- physical hostile process;
- authenticated IPC;
- OS/container capability isolation;
- real Broker target capability;
- effectful `OperationAdmission`;
- `put_if_version()` effect execution;
- `DID`, `WITHIN_SCOPE`, `SATISFIED`;
- observer/coverage/attribution;
- Git.

## Forbidden architecture changes during G1

No change to frozen architecture, threat model, Claim A meaning, uncertainty policy, or G1 PASS/FAIL semantics without explicit reopen finding.
