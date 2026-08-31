# X1D-A5 Effect-Method-Binding — Bounded Implementation Brief

## Status

`HUMAN-AUTHORIZED IMPLEMENTATION BRIEF PREPARATION`

`IMPLEMENTATION = NOT AUTHORIZED BY THIS ARTIFACT`

`CANON IMPLEMENTATION BRIEF != IMPLEMENTER AUTHORITY`

`IMPLEMENTATION SUCCESS != CORRECTIVE CLOSURE`

`DESIGN PASS != IMPLEMENTATION AUTHORITY`

`DESIGN PASS != FINDING CLOSED`

`AI PROPOSES != HUMAN DECIDES`

This artifact freezes exactly one bounded future IMPLEMENTER task for the Human-accepted X1D-A5 effect-method-binding finding. It does not implement, execute, activate, merge, verify, accept, close, release, deploy, or tag anything.

## 1. Exact bound authority and design

Accepted finding, preserved exactly:

`EFFECT METHOD NOT BOUND TO THE EXACT HUMAN DECISION`

Corrective design authority is bound exactly to:

```text
FJ899/scriptops PR #31
BASE = 30095c3170d16263e2db553a2b199bd6e33feace
HEAD = eda29d9b2916425cfa4048c8eff989b5f767ee58
TREE = 4cd9ab6d457d3496d76a47c3a6d031ea5e6cde83
PATH = governance/X1D_A5_EFFECT_METHOD_BINDING_CORRECTIVE_CANDIDATE.md
BLOB = 1247088730cbf5dddb2aea667c9842f8cc8bf980
STATE = OPEN / DRAFT / NOT MERGED
```

Independent CANON review is bound exactly to:

```text
FJ899/8 PR #93
HEAD = f9628cd29e2001e76223053ec67aec41bd303a67
TREE = 63d9522df23c7d6b4216f2912f5e4b0558cffa90
PATH = research/X1D_A5_EFFECT_METHOD_BINDING_CORRECTIVE_DESIGN_AK_CANON_REVIEW.md
BLOB = 84938da42ef4354583917d01e31f8001f21f4e84
AK-CANON CORRECTIVE DESIGN REVIEW = PASS
```

The future implementation target begins from exact ScriptOps BASE:

`FJ899/scriptops main@30095c3170d16263e2db553a2b199bd6e33feace`

Any changed BASE requires a new bounded authorization/brief. This brief must not be silently rebound to a later ScriptOps HEAD.

## 2. Pre-implementation state that was verified before this brief was written

```text
FJ899/scriptops main = 30095c3170d16263e2db553a2b199bd6e33feace
PR #31 = OPEN / DRAFT / UNMERGED
PR #31 HEAD = eda29d9b2916425cfa4048c8eff989b5f767ee58
ruleset_id = 21147233
ruleset enforcement = active
allowed_merge_methods = { merge, squash, rebase }
FJ899/8 main = b2c92ec5cd8fbb7272d701d229adc8a8019f951e
```

These observations authorize only durable freezing of this implementation brief in `FJ899/8`. They do not authorize correction execution or governance mutation.

## 3. Intended future governance state — not an implementation mutation

The corrective design requires the future governance envelope:

```text
Q_K@v_next.ruleset_id = 21147233
Q_K@v_next.allowed_merge_methods = { merge }
```

Preserve exactly:

`DESIRED GOVERNANCE STATE != AUTHORITY TO APPLY GOVERNANCE STATE`

The IMPLEMENTER candidate MUST NOT mutate the live GitHub ruleset. The live ruleset transition from `{ merge, squash, rebase }` to `{ merge }` remains a separate Human-governance action under the already established Human rule-authority boundary.

The IMPLEMENTER MUST NOT dynamically rewrite `allowed_merge_methods` per Human D0. Human decision evidence does not confer authority to mutate Q_K.

## 4. Bounded IMPLEMENTER objective

Under separate future Human IMPLEMENTER authorization, implement only the application-side portion of the exact PR #31 corrective design against ScriptOps BASE `30095c3170d16263e2db553a2b199bd6e33feace`.

The implementation must establish all of the following without weakening the frozen design:

1. a proof-bearing `OperationAdmission` representation;
2. deterministic exact admission serialization and digesting;
3. an admission broker that derives admission only from trusted observed state;
4. exact binding of Human decision/review, repository, PR, base state, candidate state, canonical ref, merge method, governance identity, and expected effect;
5. executor derivation of the GitHub merge method exclusively from a valid admission;
6. rejection of caller-selected or substituted `squash` / `rebase` before transport invocation;
7. fail-closed behavior for stale, unknown, ambiguous, or mismatched state;
8. bounded automated tests proving these application-layer properties.

No application implementation may claim platform capability closure. Platform closure is independently supplied only by the separately Human-authorized merge-only Q_K state and later verification.

`APPLICATION GUARD != PLATFORM CAPABILITY CLOSURE`

## 5. `OperationAdmission` minimum schema

The implementation must expose an immutable or equivalently tamper-resistant validated admission carrying at least:

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

A changed repository, PR, base HEAD/tree, candidate HEAD/tree, path set, canonical ref, merge method, expected post tree, Human decision/review referent, or Q_K identity invalidates the admission.

## 6. Frozen deterministic serialization and digest contract

For the future implementation candidate, exact admission serialization is frozen as follows and MUST NOT be replaced by semantically equivalent but byte-different encoding without a new bounded correction authority.

### 6.1 Encoding

Use UTF-8 encoded canonical JSON with:

```text
sort_keys = true
ensure_ascii = false
separators = (",", ":")
allow_nan = false
final newline = absent
```

All field names and string values are serialized exactly as UTF-8 JSON strings. Integers are base-10 JSON integers. Null is not permitted for any required field. Unknown extra fields are not admitted into either digest input.

### 6.2 `canonical_operation_digest`

Digest algorithm:

`sha256`

Digest input is canonical JSON containing exactly these keys and no others:

```text
repository
pr
candidate_head
canonical_ref
merge_method
expected_post_tree
```

Conceptually:

```text
canonical_operation_digest = hex(
  SHA256(
    canonical_json_utf8({
      "canonical_ref": canonical_ref,
      "candidate_head": candidate_head,
      "expected_post_tree": expected_post_tree,
      "merge_method": merge_method,
      "pr": pr,
      "repository": repository
    })
  )
)
```

The resulting digest is lowercase 64-character hexadecimal.

### 6.3 `qk_allowed_merge_methods_digest`

The normalized allowed-method value for this profile is the exact ordered JSON array:

`["merge"]`

Digest algorithm:

`sha256`

Digest input is the UTF-8 canonical JSON serialization of exactly that array. The resulting digest is lowercase 64-character hexadecimal.

No set iteration order, locale, whitespace, platform newline, or caller-provided ordering may affect the digest.

### 6.4 `admission_digest`

Digest algorithm:

`sha256`

Digest input is canonical JSON containing every required `OperationAdmission` field except `admission_digest`, including the already-computed `canonical_operation_digest` and `qk_allowed_merge_methods_digest`.

The broker computes the digest only after all validation succeeds. The executor recomputes it from the supplied admission and rejects any mismatch before transport.

## 7. Trusted-state admission broker requirements

The broker must be logically separate from the executor and may create an admission only after independently validating trusted observed state.

At minimum it must validate:

```text
valid Human D0 event
Human actor exact
Human review identity exact
review state = APPROVED
review commit_id = exact candidate_head
review body / decision tuple = exact
D0.merge_method = merge
repository = exact governed repository
PR = exact governed PR
current PR candidate HEAD/tree = exact admission candidate HEAD/tree
current main HEAD/tree = exact admission base HEAD/tree
canonical_ref = exact governed canonical ref
expected_post_tree = exact expected candidate effect for this profile
Q_K ruleset_id = 21147233
Q_K allowed_merge_methods = { merge }
Q_K identity/freshness fields match the admission
no bypass condition required by the frozen design is violated
canonical_operation_digest recomputes exactly
admission_digest recomputes exactly
```

The broker must derive these facts from trusted state inputs. Caller assertions are data to compare, not authority.

Any unknown, missing, stale, ambiguous, changed, mismatched, unsupported, or unverifiable value results in:

`DENY / BLOCKED BEFORE EFFECT`

The broker must not normalize a mismatched method into `merge`, repair stale state, broaden Human authority, or generate an admission from partial evidence.

The executor must not create, self-sign, self-approve, or repair its own admission.

## 8. Exact D0/repository/PR/candidate/ref/method/effect binding

The application implementation must ensure that one valid admission is usable only for the exact operation it names.

The binding includes at least:

```text
Human D0 identity and exact decision tuple
Human review identity / actor / reviewed commit
repository
PR number
base HEAD
base TREE
candidate HEAD
candidate TREE
path_set_digest
canonical ref
merge method
expected post TREE
Q_K ruleset identity and allowed-method digest
canonical operation digest
```

Reuse or replay against changed content, changed PR, changed repository, changed candidate, changed base, changed canonical ref, changed method, changed expected effect, or changed governance state MUST fail closed.

A changed method requires a new valid Human decision and, for any method other than `merge`, separate governance authorization/design because this corrective profile is merge-only.

## 9. Executor requirements

The executor consumes only a valid `OperationAdmission`.

It MUST derive:

```text
transport.merge_method = OperationAdmission.merge_method
transport.expected_head_sha = OperationAdmission.candidate_head
```

For this profile:

`transport.merge_method = merge`

The executor must not expose an independently authoritative merge-method parameter. If a compatibility/API surface accepts a method-shaped caller value, that value may only be used as a consistency assertion and MUST equal the admission method exactly; otherwise reject before transport.

Caller request, override, injection, substitution, or attempted selection of:

```text
squash
rebase
any value != admission.merge_method
```

must result in rejection before any GitHub merge transport call.

No fallback, normalization, aliasing, best-effort substitution, or retry with a different merge method is permitted.

`METHOD SELECTION != AUTHORITY TO CHANGE METHOD`

## 10. Fail-closed stale/mismatch behavior

Before transport, the implementation must deny on at least:

```text
missing admission
malformed admission
serialization mismatch
digest mismatch
unknown admission version
unknown / unsupported merge method
stale Human D0
stale or changed Human review
review no longer APPROVED
review commit mismatch
candidate HEAD drift
candidate TREE drift
base HEAD drift
base TREE drift
repository mismatch
PR mismatch
canonical-ref mismatch
path-set mismatch
expected-post-tree mismatch
ruleset-id mismatch
ruleset freshness/identity mismatch
allowed-method digest mismatch
live Q_K not exactly { merge }
caller method mismatch
ambiguous trusted-state read
```

No such condition may be converted into PASS, silently repaired, or deferred until after a transport call.

## 11. Bounded implementation surface

Allowed implementation scope is limited to the smallest ScriptOps application-side changes needed to realize Sections 5–10 plus tests.

The IMPLEMENTER may add narrowly scoped modules/types/functions/tests and minimally adapt an existing effect/transport path where necessary. The IMPLEMENTER must prefer integration with the existing ScriptOps structure over unrelated rewrite.

If the exact BASE does not contain a suitable canonical-effect transport path and satisfying this brief would require inventing a materially new execution architecture, classify that as an `IMPLEMENTATION BLOCKER` and STOP for CANON review rather than silently broadening scope.

## 12. Required automated tests

The implementation candidate must include bounded deterministic tests that establish at least:

```text
valid exact merge-only state -> broker emits one exact admission
serialization is byte-deterministic
canonical_operation_digest is deterministic and field-sensitive
qk_allowed_merge_methods_digest is deterministic
admission_digest is deterministic and covers all required fields
executor derives merge method only from admission
caller-selected squash rejected before transport
caller-selected rebase rejected before transport
candidate HEAD mismatch -> no admission / no transport
candidate TREE mismatch -> no admission / no transport
base HEAD/TREE mismatch -> no admission / no transport
repository or PR mismatch -> no admission / no transport
canonical-ref mismatch -> no admission / no transport
expected-post-tree mismatch -> no admission / no transport
Human review / D0 mismatch or staleness -> no admission / no transport
Q_K ruleset-id or allowed-method mismatch -> no admission / no transport
digest tamper -> no transport
unknown/ambiguous state -> fail closed
```

Transport-negative tests must use a fake/mock/recording transport and assert zero transport invocations when admission or method validation fails. They must not perform a live unauthorized merge.

Tests proving only parsing or object construction are insufficient.

`GREEN UNIT TESTS != CORRECTIVE CLOSURE`

## 13. AT0–AT10 — preserved without weakening or reinterpretation

The following future acceptance tests are preserved from exact PR #31 and remain normative. This implementation brief does not execute them and does not alter their PASS/FAIL/BLOCKED/INDETERMINATE meaning.

### AT0 — Exact candidate and governance preregistration

Freeze exact implementation candidate HEAD/TREE, exact next Q_K identity, exact test target, exact Human decision body, and exact OperationAdmission serialization before execution.

Candidate or contract drift:

`BLOCKED`

### AT1 — Q_K method envelope

Read live protected-branch ruleset.

Require:

```text
allowed_merge_methods = { merge }
bypass_actors = []
current evaluated process cannot bypass
```

Any `squash` or `rebase` in the live allowed set:

`FAIL`

### AT2 — Admission exact-method positive construction

Using a fresh valid merge-only Human D0 and exact candidate state, broker creates one admission.

Require:

```text
D0.merge_method = merge
admission.merge_method = merge
operation digest = exact frozen digest
```

### AT3 — Executor substitution negative: squash

Present a request that attempts `squash` while the admission says `merge`.

Require rejection before any GitHub merge transport call.

Any transport invocation with `squash`:

`FAIL`

### AT4 — Executor substitution negative: rebase

Same as AT3 for `rebase`.

Any transport invocation with `rebase`:

`FAIL`

### AT5 — Live GitHub UI negative: squash

Under exact fresh candidate, valid merge D0, exact current Q_K, and no unrelated blocker, inspect the method-specific GitHub merge control non-destructively.

Require `Squash and merge` to be absent, disabled, or non-executable.

Enabled executable squash:

`FAIL — EFFECT METHOD NOT BOUND`

### AT6 — Live GitHub UI negative: rebase

Same as AT5 for `Rebase and merge`.

Enabled executable rebase:

`FAIL — EFFECT METHOD NOT BOUND`

### AT7 — Direct API-path closure evidence

Read exact live Q_K and GitHub method capability state sufficient to establish that protected-branch alternate methods are rejected by platform policy.

Do not perform an unauthorized canonical merge as a negative probe.

If direct API-path closure cannot be established non-destructively with trusted evidence:

`BLOCKED`

Do not downgrade uncertainty to PASS.

### AT8 — Changed-decision method negative

Attempt admission construction with the same exact candidate but a D0 tuple naming `squash` or `rebase` while Q_K remains merge-only.

Require:

`NO ADMISSION`

This establishes that a new decision cannot silently override the governance envelope.

### AT9 — Authorized merge positive control

Only after AT0-AT8 pass, use a fresh valid merge-only D0 and admission to execute exactly one authorized GitHub `merge` positive control under separate execution authorization.

Before effect require exact candidate/main/Q_K/D0/admission.

After effect require exact C9 post-effect truth.

### AT10 — Post-effect method truth

Require generated canonical commit to have:

```text
parent1 = exact pre-main
parent2 = exact candidate
TREE = exact expected_post_tree
```

If the effect shape is squash/rebase-like, has wrong parents/tree, or cannot be established:

`FAIL` if wrong effect is established;

`INDETERMINATE` if effect occurred but exact truth cannot be established.

## 14. Explicitly forbidden / out of scope

This brief does NOT authorize the IMPLEMENTER, CANON, or any AI/process to perform any of the following as part of this brief-freeze action:

```text
implementation now
ScriptOps code mutation now
merge of PR #31
live ruleset mutation
CODEOWNERS mutation
mutation of PR #30
Human D0 issuance
corrective execution
corrective verification
canonical effect
finding closure
V1
release
deployment
tag
```

For the later IMPLEMENTER candidate specifically, live ruleset mutation remains forbidden. If live Q_K is not in the separately Human-activated merge-only state when later acceptance testing requires it, the correct disposition is `BLOCKED` / governance action required, not application-side ruleset mutation.

## 15. Future candidate evidence requirements

A future IMPLEMENTER handoff must freeze and report at minimum:

```text
ScriptOps BASE = 30095c3170d16263e2db553a2b199bd6e33feace
candidate branch
candidate HEAD
candidate TREE
exact changed paths
per-path blob identities
BASE -> candidate diff
all bounded automated test commands and results
proof that negative method cases invoked transport zero times
proof that no live ruleset / CODEOWNERS mutation is in the candidate
```

No implementation candidate is ACCEPTED merely because tests are green.

## 16. STOP conditions for the future IMPLEMENTER

STOP and return for CANON/Human disposition if any of the following occurs:

```text
BASE drift from 30095c3170d16263e2db553a2b199bd6e33feace
PR #31 design ambiguity material to implementation
conflict between this brief and exact PR #31 semantics
need to weaken or reinterpret AT0-AT10
need to treat squash/rebase as equivalent to merge
need to mutate live Q_K from implementation code
need to broaden Human D0
trusted-state provenance cannot be established without a new semantic assumption
existing ScriptOps architecture lacks a bounded application-side effect path and requires material redesign
required stale/mismatch condition cannot fail closed
application tests can pass only by bypassing the exact binding contract
```

Classify the problem explicitly as one of:

```text
finding
implementation blocker
validation-contract problem
possible freeze reopen
```

Do not silently repair a frozen contradiction.

## 17. Corrective closure remains separate

This brief freezes an implementation task only.

The accepted finding is not closed by:

```text
this brief
design PASS
implementation completion
green automated tests
merge-only ruleset text alone
application guard alone
```

Closure still requires the separately authorized complete corrective verification composition defined by PR #31, including Human decision, exact admission binding, executor no-substitution, platform alternate-method closure, authorized positive control, and exact post-effect truth, followed by Human acceptance authority.

`SPECIFICATION != IMPLEMENTATION != EXECUTION != ACCEPTANCE`

`CANON IMPLEMENTATION BRIEF != IMPLEMENTER AUTHORITY`

`IMPLEMENTATION SUCCESS != CORRECTIVE CLOSURE`

`AI PROPOSES != HUMAN DECIDES`
