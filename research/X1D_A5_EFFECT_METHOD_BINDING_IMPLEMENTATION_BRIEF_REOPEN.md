# X1D-A5 Effect-Method-Binding — Superseding Bounded Implementation Brief Reopen

## Status

`HUMAN-AUTHORIZED IMPLEMENTATION BRIEF BOUNDED ARCHITECTURE REOPEN PREPARATION`

`BRIEF REOPEN != IMPLEMENTATION AUTHORITY`

`ARCHITECTURE PERMISSION != IMPLEMENTED ARCHITECTURE`

`IMPLEMENTATION SUCCESS != CORRECTIVE CLOSURE`

`AI PROPOSES != HUMAN DECIDES`

This artifact is a superseding bounded implementation brief only. It resolves the implementation-surface blocker identified by the exact CANON review below. It does not implement, execute, activate, merge, provision credentials, mutate governance, verify corrective closure, close the finding, start V1, release, deploy, or tag anything.

## 1. Exact binding

Original implementation brief, preserved as immutable historical state:

```text
FJ899/8 PR #94
HEAD = 18dad44cc6330ad29d523a8a9d73e34fb6aae7b7
TREE = e39cd290045272494cb969b1f11c5b0201e02450
PATH = research/X1D_A5_EFFECT_METHOD_BINDING_IMPLEMENTATION_BRIEF.md
BLOB = fd97c645a4e9ae93f1024ed278f4d002adb47335
STATE = OPEN / DRAFT / UNMERGED
```

Implementation-blocker CANON review:

```text
FJ899/8 PR #95
HEAD = c2cc128c33bd26ff2dff3b04500c69ca488904ba
TREE = 4bc96fc4bafea90fe350338adc6252817497846b
PATH = research/X1D_A5_EFFECT_METHOD_BINDING_IMPLEMENTATION_BLOCKER_CANON_REVIEW.md
BLOB = 7c31f4c932aec59589dfaa39a47e25c6d0cd56ef
STATE = OPEN / DRAFT / UNMERGED
```

Exact CANON disposition:

```text
IMPLEMENTATION BLOCKER CONFIRMED
IMPLEMENTATION BRIEF REOPEN REQUIRED
VALIDATION-CONTRACT PROBLEM = NO
DESIGN REOPEN REQUIRED = NO
POSSIBLE FREEZE REOPEN = NO ON CURRENT EVIDENCE
```

Corrective design remains frozen and unchanged:

```text
FJ899/scriptops PR #31
BASE = 30095c3170d16263e2db553a2b199bd6e33feace
HEAD = eda29d9b2916425cfa4048c8eff989b5f767ee58
TREE = 4cd9ab6d457d3496d76a47c3a6d031ea5e6cde83
PATH = governance/X1D_A5_EFFECT_METHOD_BINDING_CORRECTIVE_CANDIDATE.md
BLOB = 1247088730cbf5dddb2aea667c9842f8cc8bf980
STATE = OPEN / DRAFT / UNMERGED
```

Exact future implementation BASE remains:

`FJ899/scriptops main@30095c3170d16263e2db553a2b199bd6e33feace`

Preserve exactly:

`EFFECT METHOD NOT BOUND TO THE EXACT HUMAN DECISION`

`IMPLEMENTATION BLOCKER CONFIRMED`

`DESIGN REOPEN REQUIRED = NO`

`SPECIFICATION != IMPLEMENTATION != EXECUTION != ACCEPTANCE`

## 2. Supersession rule

This brief supersedes PR #94 **only for the implementation-surface blocker identified by PR #95**.

PR #94 remains immutable historical state. No file, commit, branch, or PR belonging to #94 is modified by this reopen.

The only superseded restriction is the prior requirement that the implementation must minimally adapt an already-existing GitHub canonical-effect/transport seam. PR #95 established that no such seam exists at the exact BASE.

The reopened boundary therefore explicitly permits introduction of the missing, narrowly bounded remote GitHub trust/effect boundary described in this artifact.

Every other normative requirement of exact PR #94 and exact PR #31 remains in force, including:

```text
OperationAdmission exact binding
deterministic serialization and digests
trusted-state derivation
broker/executor separation
executor no-substitution
fail-closed stale/mismatch behavior
exact repository / PR / base / candidate / ref / method / expected-effect binding
Q_K identity binding
AT0-AT10
post-effect truth requirements
Human-only acceptance/closure
```

If a future implementer discovers a conflict between this narrowly reopened surface and any other frozen requirement, the implementer must classify `IMPLEMENTATION BLOCKER` and STOP for CANON review. No silent reinterpretation is permitted.

## 3. New bounded remote trust/effect boundary

The reopened implementation surface explicitly recognizes:

`NEW GITHUB ADMISSION/EXECUTOR BOUNDARY != MINIMAL ADAPTATION OF EXISTING LOCAL GIT COMMIT SEAM`

The exact ScriptOps BASE has a local scene-write/local-Git canonical effect path. That local path is not the remote GitHub PR-merge boundary required by X1D-A5.

A future implementation candidate may therefore introduce exactly the following new application-side components and no broader GitHub automation architecture:

```text
1. authenticated read-only GitHub trusted-state adapter;
2. trusted-state admission broker producing exact OperationAdmission;
3. GitHub PR-merge executor/transport consuming only valid admission;
4. strict credential/effect interface sufficient only for that executor;
5. deterministic fake/mock trusted-state and transport test doubles;
6. minimal wiring required to connect these components.
```

These components form one bounded remote trust/effect boundary for the exact X1D-A5 correction.

## 4. Authority/capability invariants

Preserve exactly:

`EXECUTOR CAPABILITY != HUMAN AUTHORITY`

`EXECUTOR CAPABILITY != AUTHORITY TO MUTATE Q_K`

`D0 METHOD SELECTION != AUTHORITY TO MUTATE Q_K`

`APPLICATION GUARD != PLATFORM CAPABILITY CLOSURE`

`AUTHORIZATION TEXT != ENFORCEMENT`

`OPERATION REQUEST != OPERATION ADMISSION`

`METHOD SELECTION != AUTHORITY TO CHANGE METHOD`

The ability to authenticate to GitHub, read GitHub state, or invoke a merge endpoint does not establish Human decision authority and does not authorize governance mutation.

## 5. Authenticated read-only GitHub trusted-state adapter

The future implementation may introduce a narrowly typed read-only adapter whose sole purpose is to obtain the trusted remote facts required by the frozen broker contract.

The adapter may expose only the minimum read capabilities needed to establish, at least:

```text
repository identity
PR identity and state
PR base ref / base HEAD
PR candidate HEAD
candidate commit/tree identity
Human review events including actor, state, reviewed commit, review id, and body
canonical ref HEAD/tree
ruleset id / name / enforcement / updated_at
allowed_merge_methods
bypass_actors
whether the evaluated process may bypass
```

The adapter must not accept caller assertions as authoritative replacements for these facts.

Unknown, unavailable, stale, contradictory, partial, or ambiguous remote reads are not normalized into usable state.

They result in:

`DENY / BLOCKED BEFORE EFFECT`

The adapter must be read-only. It must not expose generic write methods and must not perform reviews, comments, branch movement, ruleset changes, CODEOWNERS changes, issue mutations, release operations, tag operations, or merges.

## 6. Credential interfaces — definition only, no provisioning authority

A future implementation may define narrow credential/authentication interfaces required by the read adapter and merge executor.

This brief does not authorize provisioning, creating, rotating, storing, activating, exporting, or embedding any live credential.

No secret value may be committed to the repository.

The implementation must permit deterministic tests with fake credentials/auth contexts and fake transports without live network effects.

Any production/live credential binding is a separate execution-environment concern requiring separate Human authorization where applicable.

`CREDENTIAL INTERFACE != CREDENTIAL PROVISIONING AUTHORITY`

## 7. OperationAdmission — unchanged normative contract

The `OperationAdmission` requirements of PR #94 remain normative and are incorporated here by exact blob identity.

At minimum, a validated admission must bind:

```text
admission_version
admission_id
human_decision_id
human_review_id
human_actor
repository
pr
base_head
base_tree
candidate_head
candidate_tree
path_set_digest
canonical_ref
merge_method
expected_post_tree
qk_ruleset_id
qk_ruleset_updated_at
qk_allowed_merge_methods_digest
canonical_operation_digest
admission_digest
```

For this corrective profile:

```text
merge_method = merge
qk_ruleset_id = 21147233
qk_allowed_merge_methods = { merge }
```

A changed repository, PR, base state, candidate state, path set, canonical ref, merge method, expected effect, Human decision/review identity, or Q_K identity invalidates the admission.

## 8. Deterministic serialization/digest contract — unchanged

The exact PR #94 serialization and digest contract remains normative without weakening or reinterpretation.

Required encoding:

```text
UTF-8 canonical JSON
sort_keys = true
ensure_ascii = false
separators = (",", ":")
allow_nan = false
final newline = absent
```

Digest algorithm remains `sha256`.

`canonical_operation_digest` continues to bind exactly:

```text
repository
pr
candidate_head
canonical_ref
merge_method
expected_post_tree
```

The normalized allowed-method value remains exactly:

`["merge"]`

`admission_digest` continues to cover every required admission field except itself, including the already-computed canonical-operation and Q_K allowed-method digests.

The broker computes admission only after validation succeeds. The executor recomputes and rejects any mismatch before transport.

## 9. Trusted-state admission broker

The broker must be logically separate from the executor.

It may create `OperationAdmission` only from trusted state obtained through the bounded read adapter plus the exact Human decision evidence required by the frozen design.

At minimum it must independently establish and compare:

```text
valid Human D0 event
Human actor exact
Human review id exact
review state = APPROVED
review commit_id = exact candidate_head
review body / exact decision tuple = exact
D0.merge_method = merge
repository = exact governed repository
PR = exact governed PR
current PR candidate HEAD/tree = exact
current main HEAD/tree = exact
canonical_ref = exact
expected_post_tree = exact
Q_K ruleset_id = 21147233
Q_K identity/freshness exact
Q_K allowed_merge_methods = { merge }
bypass state exact and acceptable
canonical_operation_digest exact
admission_digest exact
```

Caller-supplied values are assertions to compare, not authority.

The broker must not repair stale state, infer missing authority, reinterpret another merge method as `merge`, mutate Q_K, broaden D0, or create an admission from partial evidence.

The executor may not create or repair its own admission.

## 10. GitHub PR-merge executor/transport

The future implementation may introduce one narrow effect transport for the GitHub PR merge operation required by this correction.

The executor consumes only a valid admission and derives transport values from that admission.

Required derivation:

```text
transport.repository = OperationAdmission.repository
transport.pr = OperationAdmission.pr
transport.merge_method = OperationAdmission.merge_method
transport.expected_head_sha = OperationAdmission.candidate_head
```

For this profile:

`transport.merge_method = merge`

The executor must not expose an independently authoritative merge-method selector.

If an outer compatibility surface carries a method-shaped assertion, it must equal the admission method exactly. Any caller request, override, injection, or substitution of `squash`, `rebase`, or any other value must be rejected before the effect transport is invoked.

No fallback, aliasing, normalization, best-effort method substitution, or retry under a different merge method is permitted.

## 11. Strict effect API allowlist

The new remote effect boundary is not a general-purpose GitHub client.

The future effect transport may implement only the minimum PR-merge call required by the frozen design.

It must not provide a generic arbitrary-method/arbitrary-endpoint facility to the application layer.

Outside the exact merge call, the implementation must not add effect capabilities for:

```text
ruleset mutation
CODEOWNERS mutation
branch/ref mutation
review submission
issue/comment mutation
release creation
release publication
tag creation/deletion
repository settings mutation
workflow dispatch
deployment
unrelated PR mutation
```

A future need for any such capability requires separate bounded design/authorization.

## 12. Fail-closed pre-effect behavior

All fail-closed requirements of PR #94 remain normative.

Before any effect transport invocation, deny on at least:

```text
missing or malformed admission
unknown admission version
serialization mismatch
digest mismatch
unknown / unsupported merge method
stale or changed D0
stale or changed Human review
review not APPROVED
review commit mismatch
repository mismatch
PR mismatch
candidate HEAD/TREE drift
base HEAD/TREE drift
canonical-ref mismatch
path-set mismatch
expected-post-tree mismatch
ruleset-id mismatch
ruleset freshness mismatch
allowed-method digest mismatch
live Q_K not exactly { merge }
bypass ambiguity or mismatch
caller method mismatch
remote read ambiguity
credential/auth context unavailable or ambiguous
```

No such condition may be silently repaired, downgraded, or deferred until after transport.

## 13. Separate live governance requirement

The application architecture does not itself close the platform capability path.

The separate future governance state remains:

```text
Q_K@v_next.ruleset_id = 21147233
Q_K@v_next.allowed_merge_methods = { merge }
```

Preserve:

`DESIRED GOVERNANCE STATE != AUTHORITY TO APPLY GOVERNANCE STATE`

The implementation candidate must not mutate the live ruleset and must not dynamically rewrite merge-method policy per D0.

Live transition from `{ merge, squash, rebase }` to `{ merge }` remains a separate Human-governance action under the established Human rule-authority boundary.

## 14. Deterministic test boundary

The future implementation candidate must include deterministic fake/mock components sufficient to prove the application-side properties without live unauthorized effects.

Required bounded tests from PR #94 remain normative, including at least:

```text
valid exact merge-only state -> broker emits exact admission
serialization byte determinism
field-sensitive canonical_operation_digest
qk_allowed_merge_methods_digest determinism
admission_digest determinism and coverage
executor derives method only from admission
caller-selected squash -> reject before transport
caller-selected rebase -> reject before transport
repository / PR mismatch -> no admission / no transport
candidate HEAD/TREE drift -> no admission / no transport
base HEAD/TREE drift -> no admission / no transport
canonical-ref mismatch -> no admission / no transport
expected-post-tree mismatch -> no admission / no transport
Human review / D0 mismatch or staleness -> no admission / no transport
Q_K identity / allowed-method mismatch -> no admission / no transport
bypass ambiguity -> no admission / no transport
digest tamper -> no transport
unknown remote state -> fail closed
read adapter performs no writes
negative cases produce zero effect-transport invocations
```

Tests must not perform live unauthorized merges.

Fake/mock transport must record invocations so zero-effect assertions are machine-checkable.

## 15. Minimal wiring rule

The future implementation may add narrowly scoped modules/types/functions/tests and the minimal wiring necessary to connect the new boundary.

The implementation may minimally adapt an existing ScriptOps entry point or add one narrowly scoped X1D-A5 entry point if needed to exercise the broker/executor composition.

It must not rewrite the existing local scene acceptance workflow merely to host the GitHub boundary.

The local `cmd_approve` / local Git commit path remains semantically distinct from the new remote PR-merge boundary unless a separately authorized design explicitly changes that relationship.

Any broader restructuring, general-purpose SDK layer, autonomous agent loop, or unrelated remote orchestration is outside scope.

## 16. No general-purpose GitHub automation

Expressly prohibited under the future implementation boundary:

```text
general-purpose GitHub automation infrastructure
unrelated GitHub API operations
autonomous governance mutation
dynamic ruleset mutation per D0
credential creation/provisioning as part of implementation
live merge execution during implementation testing
live canonical effect during implementation testing
expansion beyond exact X1D-A5 correction
```

The implementation may define narrow interfaces; it may not convert those interfaces into broader operational authority.

## 17. AT0-AT10 preserved

AT0-AT10 from exact PR #31 and exact PR #94 remain normative **without weakening or reinterpretation**.

In particular:

```text
AT0 exact candidate/governance preregistration
AT1 live Q_K method envelope requires { merge }
AT2 exact-method admission positive construction
AT3 squash substitution negative before transport
AT4 rebase substitution negative before transport
AT5 live GitHub UI squash negative
AT6 live GitHub UI rebase negative
AT7 non-destructive direct API-path closure evidence
AT8 changed-decision method -> NO ADMISSION under merge-only Q_K
AT9 authorized merge positive control only after AT0-AT8 pass and under separate execution authority
AT10 exact post-effect method truth
```

This brief does not execute any acceptance test.

## 18. Future implementation candidate deliverables

Under a separate Human IMPLEMENTER authorization, a candidate produced against exact ScriptOps BASE must durably freeze at least:

```text
exact candidate HEAD/TREE
complete changed-file set
new bounded read-adapter code
new admission-broker code
new narrow merge executor/transport code
credential/auth interface definitions only
fake/mock read and effect transports
bounded deterministic tests
any minimal wiring
exact test command(s) and results
```

The candidate must contain no live credential and must perform no live governance or canonical effect as part of implementation preparation/testing.

If implementation requires anything beyond this reopened boundary, classify `IMPLEMENTATION BLOCKER` and STOP for CANON review.

## 19. Implementation is not corrective closure

Even a fully green implementation candidate establishes only an application candidate.

It does not establish:

```text
live Q_K = { merge }
live UI/API alternate-method closure
valid future Human D0
authorized positive canonical effect
exact post-effect truth
Human closure
```

Preserve:

`IMPLEMENTATION SUCCESS != CORRECTIVE CLOSURE`

`GREEN TESTS != GATE ACCEPTANCE`

`SYSTEM UNDER TEST != AUTHORITY TO DECLARE TEST SUCCESSFUL`

## 20. Reopen boundary summary

```text
ORIGINAL BRIEF #94 = IMMUTABLE HISTORICAL STATE
BLOCKER REVIEW #95 = IMPLEMENTATION BRIEF REOPEN REQUIRED
DESIGN #31 = UNCHANGED
REOPEN SCOPE = APPLICATION-SIDE GITHUB TRUST/EFFECT BOUNDARY ONLY
LIVE Q_K CHANGE = SEPARATE HUMAN-GOVERNANCE ACTION
IMPLEMENTATION = NOT AUTHORIZED BY THIS ARTIFACT
CORRECTIVE CLOSURE = NO
V1 = STOP
```

`BRIEF REOPEN != IMPLEMENTATION AUTHORITY`

`ARCHITECTURE PERMISSION != IMPLEMENTED ARCHITECTURE`

`IMPLEMENTATION SUCCESS != CORRECTIVE CLOSURE`

`AI PROPOSES != HUMAN DECIDES`
