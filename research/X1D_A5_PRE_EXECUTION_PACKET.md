# X1D-A5 — PRE-EXECUTION PACKET

Status: `PREPARED / FROZEN FOR AK-CANON REVIEW / NOT EXECUTED`
Date: `2026-08-31`
Repository context: `FJ899/8`
System under test: `FJ899/scriptops`

## 1. Authority and purpose

Human authorized preparation of this packet only.

This packet is downstream of:

- FJ899/8 PR #74 — frozen corrected A5 preregistration;
- FJ899/8 PR #75 — valid preparation-contract blocker;
- FJ899/8 PR #76 — corrective amendment introducing `PROBE PREPARATION AUTHORITY != A5 EXECUTION AUTHORITY`;
- FJ899/8 PR #77 — exact inert-probe candidate identity freeze.

The packet fixes all material execution inputs that can be fixed before A5 execution, resolves the GitHub-generated merge-SHA treatment, and defines the exact decision tuple, traces, evidence, predicates, and STOP behavior to be reviewed by AK-CANON before any A5 run.

This packet does not authorize A5 execution.

`PACKET PREPARATION AUTHORITY != A5 EXECUTION AUTHORITY`

`DECISION TUPLE SPECIFICATION != HUMAN DECISION EVENT`

## 2. Read-only preparation preflight observed

At packet preparation time, the frozen ScriptOps target remained unchanged.

Canonical pre-state:

- repository: `FJ899/scriptops`;
- canonical ref: `refs/heads/main`;
- main HEAD: `30095c3170d16263e2db553a2b199bd6e33feace`;
- main TREE: `7ba16fab7879d7640801c410f171a08f79c8168b`.

Probe PR:

- PR: `#28 — X1D-A5: inert binding probe candidate`;
- state: `OPEN`;
- draft: `true`;
- merged: `false`;
- base: `main@30095c3170d16263e2db553a2b199bd6e33feace`;
- branch: `probe/x1d-a5-inert-binding`;
- candidate HEAD: `4b420f50ba863d8d856e870ade6aa3834c4bf96c`;
- candidate TREE: `57711cc4058547b2355d1f12c0fca14f8bb0d036`;
- changed files: exactly `1`;
- submitted reviews observed: `[]`.

Exact probe artifact:

- path: `governance/X1D_A5_INERT_BINDING_PROBE.md`;
- Git blob SHA: `b83e8facdb7f5c57617f1b6e3253f26f01709ff8`;
- SHA-256 of exact UTF-8 content including final newline: `a4f715545ae13474415ee35482064ab42a185a3b53304847da58667b11e19c6f`;
- status inside artifact: `PROBE CANDIDATE ONLY / NOT APPROVED / NOT EXECUTED`;
- `CONTENT_TOKEN = ALPHA`.

Human-rule environment:

- CODEOWNERS blob: `5dd686893d265217d921c352df033ff72fdf910e`;
- applicable CODEOWNERS entry: `/governance/ @litrgratis-pixel`;
- live ruleset id: `21147233`;
- name: `CANONICAL_MAIN_PROTECTION_V1`;
- enforcement: `active`;
- target: default branch;
- required approving review count: `1`;
- code-owner review required: `true`;
- last-push approval required: `true`;
- review-thread resolution required: `true`;
- dismiss stale reviews on push: `false`;
- required reviewers: `[]`;
- bypass actors: `[]`;
- current user can bypass: `never`;
- ruleset observed `updated_at`: `2026-08-30T18:30:51.689+02:00`;
- allowed merge methods: `merge`, `squash`, `rebase`.

Repository merge settings observed during packet preparation:

- merge commits enabled: `true`;
- squash merge enabled: `true`;
- rebase merge enabled: `true`;
- auto-merge enabled: `false`.

Historical controlled PR #27 remained `OPEN / NOT MERGED / DO NOT MERGE` and is excluded from A5.

Any mismatch in these material identities before execution yields:

`EXECUTION PREFLIGHT MISMATCH -> A5 NOT STARTED -> STOP`

No silent refresh, rebase, substitution, or target update is allowed.

## 3. Authoritative/applicable Q_K@v freeze

For this A5 packet only, the exact observable rule environment is labeled:

`Q_K@v = X1D-A5-QK-01`

This label does not create or modify a governance rule. It names the exact composition already governing the frozen target.

`X1D-A5-QK-01` consists of:

1. repository `FJ899/scriptops`;
2. canonical target `refs/heads/main`;
3. live ruleset `21147233 / CANONICAL_MAIN_PROTECTION_V1` at the exact semantic projection frozen in Section 2;
4. CODEOWNERS blob `5dd686893d265217d921c352df033ff72fdf910e`;
5. `/governance/ @litrgratis-pixel` as the applicable ownership rule for the probe artifact;
6. Human approval authority principal `@litrgratis-pixel` under the Human-authority boundary preserved by `X1D-F001 = VERIFIED CLOSED`;
7. no bypass actor and `current_user_can_bypass = never` for the evaluated repository principal;
8. pull-request-mediated canonical mutation only.

For an approval to count as a valid Human decision under this packet, all of the following must be true:

- the review actor is exactly `@litrgratis-pixel`;
- review state is `APPROVED`;
- the review is bound to the exact candidate commit required by the decision tuple;
- the exact decision statement required by Section 5 is present as the Human review body;
- the decision occurs only after A5 execution has been separately authorized;
- no material target identity has drifted;
- no bypass or alternate authority substitutes for the required Human event.

`VISIBLE APPROVAL != VALID D` unless the complete tuple and Q_K@v predicates hold.

## 4. Exact content, scope, and effect manifests

### 4.1 Content manifest C0

Exact approved candidate content identity:

- candidate HEAD: `4b420f50ba863d8d856e870ade6aa3834c4bf96c`;
- candidate TREE: `57711cc4058547b2355d1f12c0fca14f8bb0d036`;
- path: `governance/X1D_A5_INERT_BINDING_PROBE.md`;
- blob: `b83e8facdb7f5c57617f1b6e3253f26f01709ff8`;
- SHA-256: `a4f715545ae13474415ee35482064ab42a185a3b53304847da58667b11e19c6f`;
- content token: `ALPHA`.

No semantic equivalence or near-match is accepted as C0. Identity is exact.

### 4.2 Scope manifest S0

Exact authorized scope:

```text
repository = FJ899/scriptops
canonical_ref = refs/heads/main
PR = 28
changed_path_set = { governance/X1D_A5_INERT_BINDING_PROBE.md }
object_count = 1 inert probe artifact
runtime/product/governance-rule changes = none
```

A path rename, second path, path deletion without exact authorized replacement, repository change, target-ref change, or broader semantic responsibility is outside S0.

### 4.3 Intended canonical effect E0

The only effect that the future Human decision D0 may authorize is:

```text
PRE:
main HEAD = 30095c3170d16263e2db553a2b199bd6e33feace
main TREE = 7ba16fab7879d7640801c410f171a08f79c8168b

ACTION:
merge ScriptOps PR #28 by GitHub merge method = merge
("Create a merge commit" / REST merge_method=merge)

CANDIDATE:
HEAD = 4b420f50ba863d8d856e870ade6aa3834c4bf96c
TREE = 57711cc4058547b2355d1f12c0fca14f8bb0d036

EXPECTED POST-EFFECT TREE:
57711cc4058547b2355d1f12c0fca14f8bb0d036

EXPECTED CANONICAL PATH/BLOB:
governance/X1D_A5_INERT_BINDING_PROBE.md
= b83e8facdb7f5c57617f1b6e3253f26f01709ff8

EXPECTED MERGE TOPOLOGY:
new canonical HEAD is a GitHub-generated merge commit
parent 1 = 30095c3170d16263e2db553a2b199bd6e33feace
parent 2 = 4b420f50ba863d8d856e870ade6aa3834c4bf96c
```

No squash, rebase, alternate candidate, alternate path, extra path, extra commit content, or different canonical tree is included in E0.

## 5. Exact Human decision tuple specification D0

The decision tuple to be presented later to Human is frozen as:

```text
D0.decision_id = X1D-A5-D0
D0.actor = @litrgratis-pixel
D0.repository = FJ899/scriptops
D0.pr = 28
D0.base_head = 30095c3170d16263e2db553a2b199bd6e33feace
D0.base_tree = 7ba16fab7879d7640801c410f171a08f79c8168b
D0.candidate_head = 4b420f50ba863d8d856e870ade6aa3834c4bf96c
D0.candidate_tree = 57711cc4058547b2355d1f12c0fca14f8bb0d036
D0.path_set = { governance/X1D_A5_INERT_BINDING_PROBE.md }
D0.blob = b83e8facdb7f5c57617f1b6e3253f26f01709ff8
D0.content_sha256 = a4f715545ae13474415ee35482064ab42a185a3b53304847da58667b11e19c6f
D0.canonical_ref = refs/heads/main
D0.merge_method = merge
D0.expected_post_tree = 57711cc4058547b2355d1f12c0fca14f8bb0d036
D0.supersession = NONE
```

Exact Human review statement to be presented during the separately authorized A5 run:

> X1D-A5-D0 — I approve only FJ899/scriptops PR #28 at candidate HEAD 4b420f50ba863d8d856e870ade6aa3834c4bf96c, TREE 57711cc4058547b2355d1f12c0fca14f8bb0d036, path governance/X1D_A5_INERT_BINDING_PROBE.md, blob b83e8facdb7f5c57617f1b6e3253f26f01709ff8, targeting refs/heads/main from base HEAD 30095c3170d16263e2db553a2b199bd6e33feace, with canonical effect only by GitHub merge method `merge` and expected post-effect TREE 57711cc4058547b2355d1f12c0fca14f8bb0d036. Any different content, candidate HEAD/TREE, path/scope, merge method, or canonical effect requires a new Human decision. No supersession is granted.

A valid D0 event requires Human to submit an `APPROVE` review as `@litrgratis-pixel` with that exact statement and with the review bound to the exact current candidate commit.

A typo, omitted binding field, different actor, different current candidate, or materially different statement yields `D0 INVALID / BLOCKED -> STOP`.

A later re-approval of the exact same C0/S0/E0 after a preregistered probe-branch reset is a new Human event instantiating the same frozen D0 tuple. It is not a new or broadened tuple.

## 6. GitHub-generated merge SHA resolution

The future final canonical merge-commit SHA cannot be fixed in advance without manufacturing a GitHub event that has not occurred.

Therefore the expected post-effect identity is represented before execution by the exact composition:

```text
pre main HEAD/TREE
+ exact PR #28
+ exact candidate HEAD/TREE
+ exact path/blob/content
+ exact merge method = merge
+ exact expected post-effect TREE
+ exact expected merge parents
```

The final generated canonical HEAD is a post-operation observation, not a pre-operation free variable.

After an authorized positive-control merge, the final HEAD must be captured immediately and accepted only if:

1. `refs/heads/main` points to that exact generated commit;
2. its TREE is exactly `57711cc4058547b2355d1f12c0fca14f8bb0d036`;
3. its parents are exactly the frozen base and candidate in the expected merge topology;
4. the canonical probe path resolves to blob `b83e8facdb7f5c57617f1b6e3253f26f01709ff8`;
5. no additional canonical path/effect is present;
6. PR #28 reports merged by the authorized `merge` path.

The open-PR API may expose a provisional/test `merge_commit_sha`. Any such pre-merge value is evidence of GitHub's mergeability machinery only and is NOT treated as the future authorized canonical HEAD.

`PRE-MERGE TEST MERGE SHA != AUTHORIZED FINAL CANONICAL HEAD`

If a canonical effect may have occurred but the exact resulting HEAD/TREE cannot be established, the frozen post-effect uncertainty rule applies: `INDETERMINATE -> STOP`, never PASS.

## 7. Allowed execution transitions — NOT AUTHORIZED BY THIS PACKET

The following transitions are preregistered for a later, separately authorized A5 execution. Listing them here does not execute them.

### T0 — PREFLIGHT

Required observations before any execution mutation:

- main HEAD/TREE exact as Section 2;
- PR #28 exact base/head/tree/path/blob and still OPEN/DRAFT/UNMERGED;
- reviews still `[]`;
- Q_K@v exact;
- CODEOWNERS exact;
- ruleset exact;
- #27 still unmerged and excluded.

Mismatch: `BLOCKED -> STOP` before A5 starts.

### T1 — Establish valid D0 baseline

Only after separate Human A5 execution authorization:

1. mark PR #28 Ready for review;
2. verify no unrelated merge blocker makes later attribution ambiguous;
3. Human `@litrgratis-pixel` submits the exact D0 APPROVE review;
4. capture review id, actor, state, commit_id, body, and timestamp;
5. verify exact C0/S0/E0 remains current;
6. verify D0 is sufficient under Q_K@v to make the exact unmodified candidate governance-eligible, without merging it.

If the exact baseline cannot become governance-eligible for reasons unrelated to A5 binding, result is `BLOCKED -> STOP`.

This baseline is necessary so later negative results are not vacuous.

### T2 — A5-CONTENT attack

Starting from an established valid D0 baseline:

- modify exactly one field in the same probe artifact:

`CONTENT_TOKEN = ALPHA`

becomes:

`CONTENT_TOKEN = BETA`

- no other byte or path may change;
- create exactly one new probe-branch commit;
- do not obtain a new Human approval before observing the result;
- capture the attack HEAD/TREE/blob and exact diff;
- read review state and governance eligibility.

Secure result / CONTENT PASS:

- old D0 may remain visible historically, but it is not sufficient to cross the canonical boundary for the BETA candidate;
- a new valid Human decision is required before merge eligibility can be restored.

CONTENT FAIL:

- changed BETA content is governance-eligible for canonical merge under D0 alone, or GitHub represents D0 as sufficient for the changed candidate without a new valid Human decision or explicit authorized supersession.

On CONTENT FAIL:

`FAIL -> DURABLE FINDING -> STOP`

No reset, later attack, repair, or positive control is permitted after FAIL.

If CONTENT PASS, the probe branch may be reset exactly to frozen C0 HEAD `4b420f50ba863d8d856e870ade6aa3834c4bf96c` solely to prepare the next preregistered trace. After reset, exact C0 identity must be re-read. If Q_K@v requires a post-reset Human approval, Human may instantiate the same exact D0 tuple again before T3. No broadened tuple is allowed.

### T3 — A5-SCOPE attack

Starting again from exact C0 bytes and a currently valid D0 baseline:

- preserve exact original probe blob bytes;
- move the sole probe artifact from:

`governance/X1D_A5_INERT_BINDING_PROBE.md`

exactly to:

`governance/X1D_A5_INERT_BINDING_PROBE_SCOPE_VARIANT.md`

- final attack tree contains exactly one inert probe artifact;
- original path is absent in the attack tree;
- alternate path contains the exact original blob bytes;
- no runtime/product/rule content changes;
- perform the rename as one preregistered scope-change commit if the available Git data operation can do so atomically;
- if the environment cannot create that exact final tree without an ambiguous/intermediate broader scope, classify `BLOCKED -> STOP` rather than improvising;
- do not obtain a new Human approval before observing the result.

Secure result / SCOPE PASS:

- old D0 is not sufficient for the renamed path scope;
- a new valid Human decision would be required.

SCOPE FAIL:

- the alternate-path candidate is governance-eligible for canonical merge under D0 alone, or GitHub represents D0 as sufficient for the changed scope without a new valid Human decision or explicit authorized supersession.

On SCOPE FAIL:

`FAIL -> DURABLE FINDING -> STOP`

If SCOPE PASS, the probe branch may be reset exactly to frozen C0 HEAD `4b420f50ba863d8d856e870ade6aa3834c4bf96c`. Exact C0 identity must be re-read. If required by Q_K@v after reset, Human may instantiate the same exact D0 tuple again before T4.

### T4 — A5-EFFECT attack

Starting from exact C0/S0 with a currently valid D0 event:

- do not change candidate content, path, HEAD, TREE, or base;
- authorized effect remains `merge_method=merge`;
- adversarial effect is fixed as `merge_method=squash`;
- do not execute any merge;
- obtain method-specific read-only evidence of whether GitHub would permit `Squash and merge` under the same D0 without a new Human decision.

Method-specific evidence must be affirmative and non-destructive, for example an enabled GitHub merge-method control for `Squash and merge`, or an API/UI state that expressly establishes the alternate method is currently available under the same satisfied review state.

Do not infer alternate-method eligibility solely from generic `mergeable=true`.

Secure result / EFFECT PASS:

- the unauthorized squash effect is unavailable or separately blocked unless a new valid Human decision authorizes it, while the authorized merge effect can remain eligible.

EFFECT FAIL:

- the unauthorized squash effect is available to cross the canonical boundary under D0 alone, with no new valid Human decision or explicit authorized supersession.

Because squash and merge produces a different canonical commit identity/topology from the authorized merge-commit effect, its availability under the same exact-effect decision is a changed-effect counterexample even if the resulting working-tree content would be identical.

If the environment cannot establish method-specific availability without performing the unauthorized merge, result is `BLOCKED -> STOP`. The attack must not merge merely to discover whether the boundary fails.

On EFFECT FAIL:

`FAIL -> DURABLE FINDING -> STOP`

### T5 — EXACT-EFFECT POSITIVE CONTROL

Run only if T2, T3, and T4 all PASS and no counterexample has occurred.

Preconditions immediately before the operation:

- main still exact pre-state `30095c3170d16263e2db553a2b199bd6e33feace / 7ba16fab7879d7640801c410f171a08f79c8168b`;
- PR #28 current candidate is exact C0 HEAD/TREE/path/blob;
- D0 is currently valid under Q_K@v;
- no candidate, policy, CODEOWNERS, ruleset, or authority drift;
- Human A5 execution authorization explicitly includes the preregistered positive-control canonical effect.

Authorized operation:

`merge PR #28 with merge_method=merge`

Expected canonical effect is exactly E0 from Section 4.3.

Positive-control PASS requires all expected post-effect identity predicates from Section 6.

Any different content, scope, tree, merge topology, parent binding, or extra canonical effect is A5 FAIL.

If pre-effect identity is unknown: `BLOCKED -> NO MERGE -> STOP`.

If the operation may have occurred but post-effect identity cannot be established: `INDETERMINATE -> STOP`.

## 8. Evidence requirements

For every trace, preserve at minimum:

- exact timestamped pre-state reads;
- repository/ref identity;
- main HEAD/TREE;
- PR number/base/head/tree/draft/merged state;
- exact changed path set;
- exact relevant blobs/content identities;
- Q_K@v components;
- CODEOWNERS blob and applicable line;
- live ruleset id, semantic projection, and `updated_at`;
- review objects including actor/state/commit_id/body/timestamp;
- mergeability/governance-eligibility evidence with the reason for blocking or eligibility;
- exact mutation diff for negative attacks;
- probe-branch reset evidence where used;
- method-specific effect-attack evidence;
- positive-control merge response if reached;
- resulting main HEAD/TREE/parents/path/blob if a canonical effect occurs.

For negative attacks, generic workflow success or generic `mergeable=true` is not sufficient evidence of Human-decision binding.

`COMMAND SUCCESS != EFFECT TRUTH`

`VISIBLE APPROVAL != VALID D`

`GENERIC MERGEABLE != METHOD-SPECIFIC EFFECT ELIGIBILITY`

## 9. PASS / FAIL / BLOCKED / INDETERMINATE / STOP predicates

### PASS

A5 technical PASS is permitted only if:

1. exact preflight passes;
2. a non-vacuous valid D0 baseline is established;
3. CONTENT attack PASS;
4. SCOPE attack PASS;
5. EFFECT attack PASS;
6. exact-effect positive control executes;
7. canonical post-state matches E0 exactly;
8. no policy, CODEOWNERS, ruleset, Human-authority boundary, or product implementation was weakened or repaired during the run.

Permitted conclusion only:

> No preregistered A5 trace falsified end-to-end decision-to-canonical-effect binding under the exact recorded target and observable Human-authority/ruleset environment.

A5 PASS is not Human ACCEPT and is not V1 authorization.

### FAIL

One credible counterexample is sufficient when old Human decision attribution is sufficient for changed content, changed scope, or a changed canonical effect without a new valid Human decision or explicit authorized supersession, or when the positive control produces an effect different from E0.

`FIRST CREDIBLE COUNTEREXAMPLE -> FAIL -> DURABLE FINDING -> STOP`

### BLOCKED

Use BLOCKED before a canonical effect when required evidence, target identity, attribution, operation exactness, or non-destructive observation is unavailable or materially ambiguous.

BLOCKED is not PASS and not FAIL.

### INDETERMINATE

Use INDETERMINATE only if an effect may already have occurred but its exact resulting canonical identity cannot be established.

INDETERMINATE is terminal for the run and never counts as PASS.

### STOP

STOP immediately on:

- preflight mismatch;
- invalid D0;
- material evidence ambiguity;
- first credible counterexample;
- unauthorized/exogenous main movement;
- inability to perform an exact preregistered attack without scope expansion;
- post-effect indeterminacy;
- any need to repair, reinterpret, or redesign during the run.

No later trace may compensate for an earlier FAIL.

## 10. Explicit forbidden actions

Until a separate Human A5 execution authorization is given, do not:

- mark PR #28 Ready;
- request or submit Human approval;
- mutate PR #28 head/content/path;
- reset or force-update its probe branch;
- perform CONTENT/SCOPE/EFFECT attacks;
- merge PR #28 by any method;
- create any canonical effect;
- modify ScriptOps runtime/product implementation;
- alter CODEOWNERS;
- alter ruleset `21147233`;
- touch, reuse, or merge PR #27;
- start V1;
- release;
- deploy;
- tag.

This packet itself creates no ScriptOps mutation.

## 11. Required next gate

The next permissible project step is:

`AK-CANON EXECUTABILITY REVIEW OF THIS EXACT PACKET`

That review must determine whether every trace above can be executed without material interpretation or improvisation and whether the packet remains faithful to PR #74 plus the #76 corrective amendment.

AK-CANON review does not authorize execution.

Only after a satisfactory review may Human separately decide whether to authorize A5 execution.

## 12. State after packet freeze

```text
#74: HISTORICAL FROZEN PREREGISTRATION — PRESERVED
#75: VALID CONTRACT BLOCKER — PRESERVED
#76: CORRECTIVE AMENDMENT — PRESERVED
#77: PROBE IDENTITY FREEZE — PRESERVED

A5 PROBE:
CREATED / IDENTITY FROZEN

SCRIPTOPS PR #28:
OPEN / DRAFT / UNMERGED
NO HUMAN APPROVAL
DO NOT MARK READY
DO NOT MERGE

Q_K@v:
X1D-A5-QK-01 — FROZEN FOR THIS PACKET

DECISION TUPLE D0:
SPECIFIED / NO HUMAN DECISION EVENT YET

A5 PRE-EXECUTION PACKET:
PREPARED / FROZEN FOR REVIEW

AK-CANON EXECUTABILITY REVIEW:
NOT STARTED

A5 EXECUTION:
NOT AUTHORIZED / NOT STARTED

SCRIPTOPS PR #27:
DO NOT MERGE

V1:
STOP

RELEASE / DEPLOYMENT / TAG:
NOT AUTHORIZED
```

# STOP
