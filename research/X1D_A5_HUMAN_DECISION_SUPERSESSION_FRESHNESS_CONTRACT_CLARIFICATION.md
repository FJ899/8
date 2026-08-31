# X1D-A5 Human D0 / Review Supersession-Freshness Contract Clarification

## Status

`HUMAN-AUTHORIZED BOUNDED CANON CONTRACT CLARIFICATION`

`VALIDATION-CONTRACT CLARIFICATION = PASS`

`DESIGN REOPEN REQUIRED = NO`

`VALIDATION-EVIDENCE PROBLEM = EXACT FROZEN-HEAD TEST REPLAY REQUIRED`

`STOP = YES`

Preserve exactly:

`EFFECT METHOD NOT BOUND TO THE EXACT HUMAN DECISION`

`APPLICATION GUARD != PLATFORM CAPABILITY CLOSURE`

`HUMAN DECISION != EXECUTOR CREDENTIAL`

`EXECUTOR CAPABILITY != HUMAN AUTHORITY`

`EXECUTOR CAPABILITY != AUTHORITY TO MUTATE Q_K`

`CONTRACT CLARIFICATION != IMPLEMENTATION AUTHORITY`

`CONTRACT CLARIFICATION PASS != IMPLEMENTATION REVIEW PASS`

`IMPLEMENTATION REVIEW PASS != CORRECTIVE CLOSURE`

`AI PROPOSES != HUMAN DECIDES`

This artifact performs exactly one bounded clarification of the Human D0/review supersession and freshness validation contract. It does not modify ScriptOps, any implementation candidate, Human D0, Q_K/rulesets, CODEOWNERS, credentials, canonical state, releases, deployments, or tags.

## 1. Exact trigger binding

The clarification is triggered by the exact implementation-candidate AK-CANON review:

```text
FJ899/8 PR #99
HEAD = ac46186f5bb9a2a1b34373a1421b154413bcc5fe
TREE = 69dc69d9d4d1b8c0d79d607ea125caef2f44b3cc
PATH = research/X1D_A5_EFFECT_METHOD_BINDING_IMPLEMENTATION_CANDIDATE_AK_CANON_REVIEW.md
BLOB = 09f498c42f1d1816b6e9f2f8e6942335222bbffb
STATE = OPEN / DRAFT / UNMERGED
```

Preserve its disposition exactly:

```text
AK-CANON BOUNDED IMPLEMENTATION CANDIDATE REVIEW = NOT PASS
VALIDATION-CONTRACT PROBLEM = HUMAN D0/REVIEW SUPERSESSION/FRESHNESS RULE INSUFFICIENTLY DETERMINATE
VALIDATION-EVIDENCE PROBLEM = EXACT FROZEN-HEAD TEST REPLAY REQUIRED
STOP
```

The stop-level contract problem is narrow: a bound APPROVED Human review/D0 may remain present and individually valid while another Human review event for the same candidate may create a conflicting decision state. The frozen contract previously required stale/superseded Human evidence to fail closed but did not define a machine rule for that case.

## 2. Normative inputs remain unchanged

Corrective design:

```text
FJ899/scriptops PR #31
HEAD = eda29d9b2916425cfa4048c8eff989b5f767ee58
TREE = 4cd9ab6d457d3496d76a47c3a6d031ea5e6cde83
PATH = governance/X1D_A5_EFFECT_METHOD_BINDING_CORRECTIVE_CANDIDATE.md
BLOB = 1247088730cbf5dddb2aea667c9842f8cc8bf980
STATE = OPEN / DRAFT / UNMERGED
```

Superseding bounded implementation brief:

```text
FJ899/8 PR #96
HEAD = 5f5475dbff9269be667b9675d36a9c8cbd727e73
TREE = f9f015d457e0721ea9a8de62a5567b19a251cfff
PATH = research/X1D_A5_EFFECT_METHOD_BINDING_IMPLEMENTATION_BRIEF_REOPEN.md
BLOB = 4a0783f3b6092747cbd315861e71231e622e3808
STATE = OPEN / DRAFT / UNMERGED
```

Operative review of that brief:

```text
FJ899/8 PR #98
HEAD = cc2ebce5df12c9b4ec1550642848ddc30b540f87
TREE = be69f6dfde4005110a03cd374e18cda9f5aa53da
PATH = research/X1D_A5_EFFECT_METHOD_BINDING_IMPLEMENTATION_BRIEF_REOPEN_AK_CANON_REVIEW.md
BLOB = 3e2672f62c3aa9b2f1b5823ad20f900bd5fdd3f1
AK-CANON SUPERSEDING IMPLEMENTATION BRIEF REVIEW = PASS
STATE = OPEN / DRAFT / UNMERGED
```

No normative meaning in PR #31, PR #96, or PR #98 is replaced by this clarification. This artifact only makes the already-required stale/ambiguous Human-decision denial machine-decidable.

## 3. Frozen authority facts that constrain the clarification

The accepted design and superseding brief already require all of the following:

```text
valid Human D0 event
Human actor exact
Human review id exact
review state = APPROVED
review commit_id = exact candidate_head
review body / exact decision tuple = exact
caller assertions != authority
stale or changed D0 -> DENY
stale or changed Human review -> DENY
unknown / ambiguous trusted state -> DENY / BLOCKED BEFORE EFFECT
executor revalidation immediately before effect
```

The design also preserves:

```text
Human D0 = decision evidence
OperationAdmission = machine-checkable admission derived from trusted state
Executor credential = effect capability
Q_K = platform enforcement envelope
```

The clarification must therefore resolve ambiguity conservatively. It may not promote a different event merely because that event is later, has a larger id, or appears last in an API response.

## 4. Trusted GitHub-observable evidence inspected

### 4.1 Review event surface

GitHub review submissions expose stable review identity together with at least:

```text
review id / node id
actor
review state
review body
reviewed commit_id
submitted_at
```

A dismissed review is observable with state `DISMISSED`.

The clarification does not require chronology to select a winner.

### 4.2 Existing Human D0 history on the governed PR

Read-only inspection of `FJ899/scriptops PR #30` shows three distinct APPROVED review submissions from the same Human actor, all on the exact same candidate commit and with byte-identical D0 body, but with different review identities and timestamps:

```text
review node_id = PRR_kwDOTlowk88AAAABLd0T9g
numeric id = 5064430582
actor = litrgratis-pixel
state = APPROVED
commit_id = ca54f436cb99207d7d2b125013f7b7806b2e57ec
submitted_at = 2026-08-31T08:20:09Z

review node_id = PRR_kwDOTlowk88AAAABLd6udA
numeric id = 5064535668
actor = litrgratis-pixel
state = APPROVED
commit_id = ca54f436cb99207d7d2b125013f7b7806b2e57ec
submitted_at = 2026-08-31T08:34:26Z

review node_id = PRR_kwDOTlowk88AAAABLeEEEA
numeric id = 5064688656
actor = litrgratis-pixel
state = APPROVED
commit_id = ca54f436cb99207d7d2b125013f7b7806b2e57ec
submitted_at = 2026-08-31T08:54:20Z
```

All three carry the same D0 body beginning:

```text
X1D-A5-RETRY02-D0 — I approve only FJ899/scriptops PR #30 ...
```

and ending:

```text
Any different content, candidate HEAD/TREE, path/scope, merge method, or canonical effect requires a new Human decision. No supersession is granted.
```

This existing accepted evidence rules out a clarification that requires exactly one review submission or that automatically treats a later identical approval as superseding an earlier one.

It also demonstrates why `latest review wins`, `highest review id wins`, or `last timestamp wins` would be a new policy rather than a faithful reading of the frozen decision model.

## 5. Clarified concept: decision currency is consistency, not chronology

The bounded rule is:

`CURRENT HUMAN D0 = EXACT BOUND APPROVAL + COMPLETE NON-CONFLICTING ACTIVE DECISION SET`

The rule is intentionally order-independent.

It does not select a winning Human review event.

It determines only whether the exact D0 named by an admission is still safely usable.

A different Human decision is never auto-promoted into the existing admission. A new decision, if otherwise valid, requires its own exact admission and exact Human decision/review binding.

This preserves:

`CHANGED HUMAN DECISION != AUTOMATIC REBINDING OF EXISTING ADMISSION`

## 6. Exact currently-effective predicate

For an admission bound to:

```text
human_review_id = R0
human_actor = H
candidate_head = C
human_review_body = B
exact D0 tuple = D
```

let `REVIEWS` be the complete trusted GitHub review-submission set for the exact governed PR.

The exact bound Human D0/review is `CURRENT / EFFECTIVE` only if every condition below is true.

### 6.1 Complete trusted review set

The adapter must establish a complete review-submission set for the exact PR. Pagination, truncation, partial reads, unknown read completeness, contradictory duplicate records, or unavailable review state are not usable evidence.

Any inability to establish completeness is:

`DENY / BLOCKED BEFORE EFFECT`

### 6.2 Exact bound review still exists once

Exactly one review event in the complete set must have `review_id = R0`.

Missing or duplicate exact review identity is:

`STALE / AMBIGUOUS -> DENY`

### 6.3 Exact bound review remains the same approval

The exact `R0` event must satisfy:

```text
actor = H
state = APPROVED
commit_id = C
body = B
parsed exact D0 tuple = D
```

Any mismatch is:

`STALE / CHANGED / REVOKED -> DENY`

If `R0.state = DISMISSED`, the exact bound Human approval is revoked for this admission:

`STALE / REVOKED -> DENY`

### 6.4 Active same-Human same-candidate decision-set consistency

Consider every non-dismissed review event `r` satisfying:

```text
r.actor = H
r.commit_id = C
```

Review submissions whose state is `COMMENTED` are non-decision feedback for this bounded D0 currency predicate because the frozen Human D0 contract requires `review state = APPROVED`. They do not create or replace a D0.

Every other decision-bearing active event for `H` and `C` must be concordant with the bound D0.

A concordant event is exactly:

```text
state = APPROVED
body = B
parsed exact D0 tuple = D
```

Different review ids and different `submitted_at` values are permitted for concordant duplicates.

If all active decision-bearing events for the exact Human actor and exact candidate are concordant, the bound D0 remains:

`CURRENT / EFFECTIVE`

### 6.5 Conflict condition

Any active same-Human same-candidate decision-bearing event that is not concordant invalidates the bound D0 for effect execution.

This includes at least:

```text
state = CHANGES_REQUESTED
state = APPROVED with body != B
state = APPROVED with parsed D0 tuple != D
unknown or unsupported decision-bearing review state
unparseable putative D0 evidence where classification is required
```

The result is:

`STALE / SUPERSEDED / CONFLICTING / AMBIGUOUS -> DENY BEFORE EFFECT`

The broker and executor do not need to decide which competing event is the winner.

They need only establish that the old admission is no longer backed by one unambiguous current Human decision.

### 6.6 Dismissed competing events

A review whose trusted current state is `DISMISSED` is historical/inactive for the competing active-decision set.

It cannot be used as current D0 evidence.

A dismissed old approval therefore does not permanently poison a later independently bound D0.

This permits explicit replacement without chronology guessing:

```text
old conflicting approval = DISMISSED
new exact approval = separately bound
no other active conflict
=> new admission may be evaluated under its own exact binding
```

The clarification does not authorize dismissing any review. It only defines how an already-observed dismissal is interpreted.

## 7. Treatment of multiple otherwise valid Human events

### 7.1 Multiple identical approvals

Multiple distinct reviews are allowed when all of the following are exact:

```text
actor = H
commit_id = C
state = APPROVED
body = B
D0 tuple = D
```

They are multiple pieces of evidence for the same Human decision, not multiple competing decisions.

No review-id ordering is used.

No timestamp ordering is used.

This rule matches the already-observed PR #30 D0 history.

### 7.2 Different approved D0 on the same candidate

If the same exact Human actor has another active APPROVED review on `C` whose body or D0 tuple differs, the existing admission is not current enough to execute.

Result:

`CONFLICTING HUMAN DECISIONS -> DENY`

The newer/different review is not auto-selected.

To make a replacement D0 usable, conflicting old active decision evidence must become unambiguously inactive and the replacement must be separately bound into a new admission.

### 7.3 CHANGES_REQUESTED on the same candidate

An active same-Human `CHANGES_REQUESTED` review on `C` conflicts with an APPROVED D0 for the same candidate.

Result:

`CURRENT HUMAN AUTHORITY AMBIGUOUS / NEGATIVE -> DENY`

A later approval does not silently override that event under this contract. If the negative review is no longer authoritative, that must be observable through an unambiguous inactive/dismissed state rather than inferred from event ordering.

### 7.4 COMMENTED review

A `COMMENTED` review is not a valid D0 because the frozen valid-D0 predicate requires `state = APPROVED`.

It therefore does not supersede or create Human D0 authority under this bounded clarification.

If a future Human-authority design wants a comment body to revoke or replace a D0, that would be a new authority semantic and requires separate design.

### 7.5 Different actor

The frozen contract binds `Human actor exact`.

A review event from an actor other than `H` is not silently elevated into authority to supersede this D0.

It does not replace the exact bound Human decision under this contract.

If future governance authorizes multiple Human actors to supersede one another's D0 events, that is a separate Human-authority design question and is not created here.

Other reviewers may still affect independent GitHub/Q_K merge predicates; this clarification addresses only D0 currency.

### 7.6 Different candidate commit

A review event whose `commit_id != C` does not supersede the D0 for exact candidate `C` under this predicate.

If the actual PR candidate changes, the independently frozen candidate-HEAD/TREE drift checks already invalidate the admission before effect.

Thus candidate drift remains the primary fail-closed mechanism for changed content.

## 8. Chronology and ordering are deliberately non-authoritative

`submitted_at` is useful audit evidence but is not a winner-selection field.

The clarification explicitly rejects:

```text
latest review wins
latest approval wins
highest review id wins
last timestamp wins
same actor latest event wins
API list order wins
```

Therefore equal timestamps, reordered API results, or absence of a usable total chronology do not require inventing a winner.

The contract is set-based and order-independent.

However, review identity/state/actor/commit/body completeness remains mandatory. Missing or ambiguous required event data is fail-closed.

## 9. Exact supersession/revocation effect on an existing admission

For the existing admission, supersession is defined operationally, not by winner promotion:

```text
BOUND D0 CURRENT
IFF
bound review exact and active
AND
all active same-Human same-candidate decision events are concordant
```

The moment trusted state contains an active conflict, the bound admission is no longer usable:

`CURRENT / EFFECTIVE -> STALE / SUPERSEDED / AMBIGUOUS -> DENY`

The executor must never repair the admission by substituting the conflicting event.

A separate new admission is required for any different Human decision.

This is the narrowest deterministic rule that satisfies both:

```text
stale/superseded Human evidence must fail closed
```

and:

```text
multiple identical existing approvals must not be falsely treated as supersession
```

## 10. Required trusted-state adapter evidence

The bounded read-only adapter must make available, for the exact governed PR, a complete set sufficient to evaluate the predicate above.

For each relevant review event, the trusted evidence must include at least:

```text
stable review identity
actor identity
state
reviewed commit_id
body
```

`submitted_at` may be retained for audit but is not normative for currency selection.

The adapter must establish collection completeness across pagination and must not return only the review id requested by the caller.

Caller-supplied review lists, caller-supplied latest ids, or caller-supplied ordering are not authority.

Unknown/partial/contradictory reads result in:

`DENY / BLOCKED BEFORE EFFECT`

The adapter remains read-only.

## 11. Required broker validation

Before creating an `OperationAdmission`, the broker must:

1. obtain the complete trusted review set;
2. locate the exact bound review id exactly once;
3. validate exact actor/state/commit/body/D0 tuple;
4. evaluate the full active same-Human same-candidate decision set;
5. require every decision-bearing active event in that set to be concordant;
6. deny on any conflict, unknown state, incomplete evidence, or ambiguity;
7. only then create the admission.

The broker must not:

```text
select the newest event
select the largest id
normalize conflicting bodies
treat CHANGES_REQUESTED as equivalent to APPROVED
infer dismissal from a later approval
mutate or dismiss a review
repair/rewrite a Human decision
```

## 12. Required executor revalidation

Immediately before any effect transport invocation, the executor must repeat the same currency predicate against a fresh complete trusted review set.

If a conflicting Human event appeared after admission creation, transport invocation count must remain zero.

The executor must not reuse the broker's earlier review-set snapshot as proof of current Human decision state unless that snapshot is freshly re-established under the already-frozen executor revalidation requirement.

Preserve:

`ADMISSION VALID WHEN CREATED != HUMAN DECISION STILL CURRENT AT EFFECT TIME`

## 13. Deterministic implementation tests required

Any future candidate claiming conformance to this clarification must deterministically establish at least:

```text
1. one exact APPROVED bound review -> admission allowed
2. three distinct identical APPROVED reviews, same actor/candidate/body/D0 -> admission allowed
3. later-or-earlier identical APPROVED duplicate -> same result; order irrelevant
4. same actor + same candidate + APPROVED different body -> no admission / zero transport
5. same actor + same candidate + APPROVED different D0 tuple -> no admission / zero transport
6. same actor + same candidate + CHANGES_REQUESTED -> no admission / zero transport
7. exact bound review DISMISSED -> no admission / zero transport
8. old conflicting approval DISMISSED + separately bound concordant approval -> new admission can be evaluated
9. COMMENTED same-actor review does not create or replace D0 authority
10. unknown review state -> fail closed / zero transport
11. incomplete or truncated review collection -> fail closed / zero transport
12. duplicate exact review identity records -> fail closed / zero transport
13. different actor event does not silently supersede exact Human actor D0
14. different commit review does not silently supersede exact candidate D0
15. candidate drift still invalidates independently
16. bound review body/state/actor/commit mutation -> fail closed
17. conflicting event introduced after admission but before executor effect -> executor revalidation denies with zero transport
18. review-list ordering and timestamp ordering do not affect the result
```

Tests must use deterministic fakes/mocks and must not perform live merge, review mutation, dismissal, governance mutation, or canonical effect.

## 14. Why this is clarification rather than design reopen

This rule does not create a new Human actor, new Human decision type, new effect method, new executor capability, new Q_K authority, new admission field, or new chronology-based winner policy.

It operationalizes already-frozen requirements:

```text
Human actor exact
Human review exact
stale/changed Human evidence -> DENY
unknown/ambiguous trusted state -> DENY
caller assertion != authority
executor revalidation before effect
```

It also respects the existing real D0 evidence containing multiple identical approvals.

The only added validation precision is:

`COMPLETE ACTIVE DECISION-SET CONSISTENCY MUST BE PROVEN`

Therefore:

`DESIGN REOPEN REQUIRED = NO`

## 15. Relationship to exact PR #32

This clarification does not modify or repair `FJ899/scriptops PR #32`.

It does not declare PR #32 defective merely because the earlier frozen contract omitted this rule.

A separate authority must determine whether exact PR #32 already conforms to the clarified complete-decision-set predicate or requires a bounded implementation correction.

No implementation conformance disposition is made here.

Preserve:

`CONTRACT CLARIFICATION PASS != IMPLEMENTATION REVIEW PASS`

## 16. Validation evidence remains independently open

The exact PR #99 finding remains:

`VALIDATION-EVIDENCE PROBLEM = EXACT FROZEN-HEAD TEST REPLAY REQUIRED`

No replay is performed by this clarification.

Because a later implementation correction may produce a new candidate HEAD, the direct exact-HEAD replay must target the final frozen candidate presented for the next implementation review.

`SAME TREE != DIRECT FROZEN-HEAD EXECUTION PROVENANCE`

## 17. Final determination

```text
EXACT TRIGGER #99 BINDING = PRESERVED
CORRECTIVE DESIGN #31 = UNCHANGED
SUPERSEDING BRIEF #96 = UNCHANGED
OPERATIVE BRIEF REVIEW #98 = UNCHANGED
HUMAN AUTHORITY MODEL = NOT BROADENED
CHRONOLOGY-BASED WINNER POLICY = NOT INTRODUCED
MULTIPLE IDENTICAL APPROVALS = PERMITTED / CONCORDANT
BOUND REVIEW DISMISSED = REVOKED / DENY
SAME-HUMAN SAME-CANDIDATE CHANGES_REQUESTED = CONFLICT / DENY
SAME-HUMAN SAME-CANDIDATE DIFFERENT APPROVED D0 = CONFLICT / DENY
DIFFERENT HUMAN ACTOR = NOT SILENTLY PROMOTED TO SUPERSESSION AUTHORITY
DIFFERENT CANDIDATE = HANDLED BY EXACT CANDIDATE BINDING / DRIFT
INCOMPLETE REVIEW SET = DENY
EXECUTOR FRESH REVALIDATION = REQUIRED
CALLER ASSERTIONS != AUTHORITY = PRESERVED
EXACT FROZEN-HEAD REPLAY = STILL REQUIRED LATER
PR #32 CONFORMANCE = NOT DETERMINED UNDER THIS AUTHORITY
```

Therefore:

`VALIDATION-CONTRACT CLARIFICATION = PASS`

`VALIDATION-CONTRACT PROBLEM = RESOLVED BY ORDER-INDEPENDENT ACTIVE-DECISION CONSISTENCY RULE`

`DESIGN REOPEN REQUIRED = NO`

`VALIDATION-EVIDENCE PROBLEM = EXACT FROZEN-HEAD TEST REPLAY REQUIRED`

`STOP`

No implementation authorization, live Human D0 mutation, Q_K/ruleset mutation, CODEOWNERS mutation, credential provisioning, merge execution, canonical effect, AT0-AT10 execution, corrective verification, finding closure, V1, release, deployment, or tag is established by this artifact.
