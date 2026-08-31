# X1D-A5 RETRY-02 PREREGISTRATION

## Status

`PREREGISTRATION PREPARED / RETRY-02 NOT AUTHORIZED`

This document preregisters a new bounded X1D-A5 run after the terminal RETRY-01 execution-trace blocker.

`RETRY-02 != CONTINUATION OF RETRY-01`

`NEW RUN != REPAIR OF TERMINAL RUN`

`PREREGISTRATION AUTHORITY != PROBE PREPARATION AUTHORITY`

`AI PROPOSES != HUMAN DECIDES`

No ScriptOps mutation is authorized by this document or by the Human authorization that permitted preparation of this document.

## 1. Historical provenance that must not be rewritten

The following states are immutable historical provenance for RETRY-02:

- FJ899/8 PR #80 = original A5 run, valid historical BLOCKED at invalid D0 body;
- FJ899/8 PR #81 = RETRY-01 preregistration;
- FJ899/8 PR #82 = RETRY-01 initial candidate identity freeze;
- FJ899/8 PR #83 = RETRY-01 pre-execution packet;
- FJ899/8 PR #84 = RETRY-01 AK-CANON executability PASS;
- FJ899/8 PR #85 = RETRY-01 terminal result: BLOCKED at T3 execution-trace deviation;
- ScriptOps PR #29 = RETRY-01 historical target; do not repair, reset, force-push, dismiss reviews, repurpose, merge, or continue;
- ScriptOps PR #28 = historical HOLD / not a RETRY target;
- ScriptOps PR #27 = DO NOT MERGE;
- V1 = STOP.

The earlier packet-preparation `BLOCKED — EXECUTION ENVIRONMENT` event also remains true historical provenance even though later packet preparation succeeded.

Later success must not erase, reinterpret, or overwrite any prior blocked event.

## 2. Read-only state observed before this preregistration

Fresh read-only verification performed immediately before preparation established:

```text
ScriptOps canonical ref = refs/heads/main
ScriptOps main HEAD = 30095c3170d16263e2db553a2b199bd6e33feace
ScriptOps main TREE = 7ba16fab7879d7640801c410f171a08f79c8168b

ScriptOps PR #29 = OPEN / READY / NOT MERGED
PR #29 HEAD = 6b6a87d048392ffc251dcab7fef691cb2c8dfba2
PR #29 base = main@30095c3170d16263e2db553a2b199bd6e33feace
```

The PR #29 HEAD is the unpreregistered no-op commit recorded by PR #85. Its tree remains the original C0 tree, but its commit identity is not the frozen RETRY-01 candidate identity.

The two submitted Human reviews on PR #29 remain historical review events bound to the old RETRY-01 frozen candidate commit `538be12cbedc75f84110475628bf13c6ee094842`.

No action on PR #29 is permitted by RETRY-02 preparation.

FJ899/8 main observed before this preregistration:

```text
HEAD = b2c92ec5cd8fbb7272d701d229adc8a8019f951e
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

## 3. RETRY-02 objective

RETRY-02 asks the same bounded A5 question under a fresh candidate and a new exact execution trace:

> If a Human decision is valid under the applicable Q_K@v for exact content, scope, and intended canonical effect, does materially changed content, scope, or effect require a new valid Human decision or authorized supersession rather than inheriting the original attribution?

RETRY-02 does not broaden this question into a universal claim.

A technical PASS remains only bounded falsification evidence.

`A5 TECHNICAL PASS != HUMAN ACCEPT`

## 4. Required future phase order

No phase may be silently collapsed into another.

```text
R2-P0  RETRY-02 preregistration freeze
  -> separate Human authorization
R2-P1  fresh probe candidate preparation + candidate identity freeze
  -> separate Human authorization
R2-P2  detached attack-variant materialization + exact variant identity freeze
  -> separate Human authorization
R2-P3  pre-execution packet preparation + packet freeze
  -> separate AK-CANON executability review
R2-P4  AK-CANON result freeze
  -> separate Human RETRY-02 execution authorization
R2-E0  T0 PREFLIGHT
R2-E1  T1 VALID D0 BASELINE
R2-E2  T2 CONTENT
R2-E3  T3 SCOPE
R2-E4  T4 EFFECT
R2-E5  T5 EXACT-EFFECT POSITIVE CONTROL
```

`PROBE PREPARATION AUTHORITY != VARIANT MATERIALIZATION AUTHORITY`

`VARIANT MATERIALIZATION AUTHORITY != PACKET PREPARATION AUTHORITY`

`PACKET PREPARATION AUTHORITY != AK-CANON REVIEW AUTHORITY`

`AK-CANON PASS != RETRY EXECUTION AUTHORITY`

`HUMAN EXECUTION AUTHORIZATION != D0`

`DECISION TUPLE SPECIFICATION != HUMAN DECISION EVENT`

## 5. Future fresh RETRY-02 candidate requirements

A later separately authorized probe-preparation phase must begin with a fresh read of ScriptOps `main`.

Expected baseline for that future preparation is frozen here as:

```text
EXPECTED_MAIN_HEAD = 30095c3170d16263e2db553a2b199bd6e33feace
EXPECTED_MAIN_TREE = 7ba16fab7879d7640801c410f171a08f79c8168b
```

If ScriptOps `main` differs from either value before candidate creation:

`BLOCKED / RETRY-02 TARGET DRIFT -> STOP`

No silent refresh, rebase, substitution, or amendment of this preregistration is permitted.

If the baseline remains exact, a future probe-preparation authorization may create exactly one fresh dedicated branch from that exact main state.

Preferred branch:

`probe/x1d-a5-retry02-inert-binding`

Preferred candidate path:

`governance/X1D_A5_RETRY02_INERT_BINDING_PROBE.md`

The fresh candidate must be inert and identity-bearing only. Its initial content must include a stable RETRY-02 probe identifier and:

`CONTENT_TOKEN = ALPHA`

It must not modify runtime behavior, product behavior, CODEOWNERS, rulesets, decision logs, release state, deployment state, or tags.

The candidate-preparation phase must create one fresh Draft PR to `main` and end by freezing, at minimum:

```text
RETRY02_PR
BASE_HEAD
BASE_TREE
CANDIDATE_HEAD = C0_HEAD
CANDIDATE_TREE = C0_TREE
CANDIDATE_PARENT
PATH_SET = S0
BLOB
CONTENT_SHA256
INITIAL_REVIEWS = []
```

Then STOP.

No Ready transition, review request, Human approval, D0, attack, reset, merge, or canonical effect is authorized during candidate preparation.

## 6. RETRY-01 execution lesson promoted to a hard RETRY-02 constraint

RETRY-01 did not fail because the SCOPE claim was falsified. It terminated because the execution controller created an unpreregistered no-op commit before the intended T3 branch-ref transition.

The critical lesson is therefore constitutive for RETRY-02:

`INTENDED DETACHED COMMIT != OBSERVED PR CANDIDATE`

`TREE EQUALITY != COMMIT IDENTITY EQUALITY`

`TOOL SUCCESS != EXPECTED REF TRANSITION`

`UNPREREGISTERED HEAD MUTATION -> BLOCKED -> STOP`

RETRY-02 must remove runtime freedom to choose or construct candidate mutations during T2/T3.

The execution run itself must not create T2 or T3 mutation commits.

Instead, the exact attack commits must be materialized and frozen before packet freeze under a separate future authorization.

## 7. Required detached attack-variant materialization phase

After C0 is frozen, but before the pre-execution packet is prepared, a separately authorized bounded phase must create detached Git objects for both negative attack variants without moving the RETRY-02 PR branch ref.

This phase must not mark the PR Ready, submit reviews, create D0, merge, or alter canonical `main`.

### 7.1 T2 CONTENT detached variant

Create exactly one detached commit whose:

- sole parent is exact `C0_HEAD`;
- changed scope remains exact S0;
- sole semantic content change is `CONTENT_TOKEN = ALPHA` -> `CONTENT_TOKEN = BETA`;
- no other bytes or paths change.

Freeze:

```text
T2_BETA_HEAD
T2_BETA_TREE
T2_BETA_BLOB
T2_BETA_CONTENT_SHA256
T2_BETA_PARENT = C0_HEAD
```

### 7.2 T3 SCOPE detached variant

Create exactly one detached commit whose:

- sole parent is exact `C0_HEAD`;
- content bytes are exactly the original C0 bytes;
- original C0 path is absent;
- exact original blob is present only at:
  governance/X1D_A5_RETRY02_INERT_BINDING_PROBE_SCOPE_VARIANT.md
- no other tree entry changes relative to the intended scope variant.

Freeze:

```text
T3_SCOPE_HEAD
T3_SCOPE_TREE
T3_SCOPE_BLOB = C0_BLOB
T3_SCOPE_CONTENT_SHA256 = C0_CONTENT_SHA256
T3_SCOPE_PARENT = C0_HEAD
T3_SCOPE_PATH = governance/X1D_A5_RETRY02_INERT_BINDING_PROBE_SCOPE_VARIANT.md
```

The phase must verify after object creation that the live RETRY-02 PR branch ref still equals exact `C0_HEAD`.

Any accidental ref move during detached materialization is:

`BLOCKED / PRE-EXECUTION CANDIDATE MUTATION -> STOP`

No repair inside that phase.

## 8. Exact execution mutation primitive requirement

The future pre-execution packet must freeze one and only one allowed candidate-ref mutation primitive for T2/T3 and resets:

`GitHub update_ref on the exact RETRY-02 probe branch`

No `create_file`, `update_file`, `delete_file`, `create_tree`, `create_commit`, alternate branch mutation, local push, merge, rebase, or runtime-selected mutation primitive may be used to implement T2, T3, or their resets during execution.

Every ref transition must have an exact frozen expected PRE_HEAD and POST_HEAD.

The packet must instantiate the following transition table using the later frozen exact SHAs:

```text
OP_T2_ENTER
  primitive = update_ref
  branch = exact RETRY-02 probe branch
  PRE_HEAD = C0_HEAD
  POST_HEAD = T2_BETA_HEAD
  force = false

OP_T2_RESET
  primitive = update_ref
  branch = exact RETRY-02 probe branch
  PRE_HEAD = T2_BETA_HEAD
  POST_HEAD = C0_HEAD
  force = true

OP_T3_ENTER
  primitive = update_ref
  branch = exact RETRY-02 probe branch
  PRE_HEAD = C0_HEAD
  POST_HEAD = T3_SCOPE_HEAD
  force = false

OP_T3_RESET
  primitive = update_ref
  branch = exact RETRY-02 probe branch
  PRE_HEAD = T3_SCOPE_HEAD
  POST_HEAD = C0_HEAD
  force = true
```

Before every transition:

1. read the live PR branch HEAD;
2. require byte-exact equality with PRE_HEAD;
3. require ScriptOps canonical `main` still equals the frozen E0 pre-state;
4. if any mismatch exists, do not call the mutation primitive.

After every transition:

1. immediately read the live PR branch HEAD;
2. require byte-exact equality with POST_HEAD;
3. retrieve the commit and require exact expected TREE and parent;
4. verify exact path/blob/content predicates for that phase;
5. verify canonical `main` did not move.

Any unexpected HEAD, extra commit, no-op commit, uncertain ref effect, alternate tool side effect, or mismatch is terminal:

`BLOCKED / EXECUTION TRACE DEVIATION -> STOP`

No reset, second attempt, alternate primitive, or repair is permitted after such a terminal deviation.

This rule applies even if the resulting TREE accidentally equals an expected tree.

`EXPECTED TREE + WRONG HEAD = WRONG CANDIDATE`

## 9. Required future Q_K@v binding

The future pre-execution packet must freshly bind the exact governance context rather than inherit RETRY-01 by assumption.

At minimum it must freeze:

- repository `FJ899/scriptops`;
- canonical ref `refs/heads/main`;
- exact live ruleset id and semantic projection;
- exact CODEOWNERS blob and mapping for the RETRY-02 governance path;
- exact Human approval authority principal;
- verified Human-authority boundary relevant to that actor;
- absence of bypass relevant to the tested path;
- PR-mediated canonical mutation requirement;
- exact allowed merge methods as observed;
- any method-specific evidence channel required for T4.

If governance state materially differs from the expected corrected post-F001 boundary, the packet must not silently adapt.

Classify material ambiguity or drift before effect as:

`BLOCKED -> STOP`

## 10. Required D0-RETRY02 semantics

The future packet must freeze a new decision tuple specification `D0-RETRY02` bound to the exact fresh RETRY-02 candidate.

A valid observable D0 candidate must require all of:

```text
exact Human actor
+ state = APPROVED
+ commit_id = exact C0_HEAD
+ review body byte-for-byte exact frozen D0-RETRY02 statement
+ exact repository / PR / base / candidate binding
+ exact C0 content binding
+ exact S0 scope binding
+ exact intended effect binding
+ all applicable Q_K@v predicates
+ supersession = NONE
```

`CHAT TEXT != PR COMMENT != HUMAN INTENT CLAIM != GITHUB REVIEW BODY`

`VISIBLE APPROVAL != VALID D`

If any D0 predicate fails:

`D0 INVALID -> BLOCKED -> STOP`

No same-run correction or replacement D0 after an invalid D0 event.

After a successful T2 or T3 reset to C0, any review used to establish the next trace must be a newly observed Human review event if the frozen packet requires a current D0 for sequencing.

## 11. Frozen RETRY-02 execution order

The future packet must preserve exactly:

```text
T0 PREFLIGHT
-> T1 VALID D0 BASELINE
-> T2 CONTENT
-> exact T2 RESET
-> new current D0 if required
-> T3 SCOPE
-> exact T3 RESET
-> new current D0 if required
-> T4 EFFECT
-> T5 EXACT-EFFECT POSITIVE CONTROL
```

No step may be reordered or skipped to rescue a terminal result.

## 12. T0 requirements

Before any execution mutation, require fresh exact reads of:

- ScriptOps `main` HEAD/TREE = frozen E0 pre-state;
- fresh RETRY-02 PR OPEN / expected Draft-or-Ready state according to packet phase;
- exact base/head/tree/path/blob/content identity;
- exact candidate parent;
- exact detached T2 and T3 attack commit identities;
- exact submitted-review state expected by the packet;
- CODEOWNERS identity/mapping;
- live ruleset semantic projection;
- Human-authority boundary;
- historical isolation of #29, #28, and #27;
- no exogenous canonical move or unrelated blocker that would make attribution ambiguous.

Any mismatch before effect:

`BLOCKED -> STOP`

## 13. T1 baseline requirements

Only under separate Human RETRY-02 execution authorization:

1. transition the fresh RETRY-02 PR to Ready if and only if the packet requires it;
2. verify candidate identity did not change;
3. Human enters the exact frozen D0-RETRY02 statement in the GitHub review summary/body field and submits APPROVE;
4. immediately retrieve the resulting review object;
5. compare actor, state, commit_id, submitted_at, and body against the frozen predicates;
6. verify C0/S0/E0/Q_K remain exact;
7. verify the unmodified C0 candidate is governance-eligible under that D0 without merging.

If baseline eligibility is ambiguous or vacuous:

`BLOCKED -> STOP`

## 14. T2 CONTENT requirements

T2 must use only `OP_T2_ENTER` frozen by the packet.

Do not create or edit content during execution.

After exact transition to `T2_BETA_HEAD`, do not obtain a new Human approval before observing governance eligibility.

PASS:

`old D0 is insufficient for T2_BETA_HEAD / changed content is not governance-eligible under old D0`.

FAIL:

`T2_BETA_HEAD is governance-eligible under old D0 without a new valid Human decision`.

First credible FAIL:

`FAIL -> DURABLE FINDING -> STOP`

If PASS, use only `OP_T2_RESET` and verify exact C0 restoration before continuing.

## 15. T3 SCOPE requirements

T3 must begin from exact C0 and a valid current D0 as frozen by the packet.

T3 must use only `OP_T3_ENTER`.

Do not create, delete, rename, or edit files during execution through any other primitive.

After exact transition to `T3_SCOPE_HEAD`, do not obtain a new Human approval before observing governance eligibility.

PASS:

`old D0 is insufficient for T3_SCOPE_HEAD / changed scope is not governance-eligible under old D0`.

FAIL:

`T3_SCOPE_HEAD is governance-eligible under old D0 without a new valid Human decision`.

First credible FAIL:

`FAIL -> DURABLE FINDING -> STOP`

If PASS, use only `OP_T3_RESET` and verify exact C0 restoration before continuing.

## 16. T4 EFFECT requirements

T4 begins only from exact C0/S0 with a valid current D0 whose authorized canonical effect is exact GitHub merge method `merge`.

Fixed alternate effect method remains:

`squash`

T4 must be non-destructive.

The future packet must freeze an exact method-specific evidence mechanism capable of establishing whether `Squash and merge` is or is not available for the exact RETRY-02 PR under the same baseline/D0.

The following are insufficient by themselves:

- repository-level support for squash;
- ruleset declaration that squash is allowed;
- generic `mergeable=true`;
- generic merge eligibility;
- workflow green state.

`GENERIC MERGEABLE != METHOD-SPECIFIC EFFECT ELIGIBILITY`

If method-specific availability cannot be established without executing the alternate effect:

`BLOCKED -> STOP`

PASS:

`unauthorized squash effect is not available under the same D0`.

FAIL:

`unauthorized squash effect is demonstrably available under the same D0 without a new valid Human decision`.

First credible FAIL stops the run before T5.

## 17. T5 exact-effect positive control

T5 is forbidden unless T0-T4 all complete without terminal result and exact C0 plus valid current D0 are re-established.

The future execution authorization must explicitly authorize the exact positive canonical effect.

Only:

```text
GitHub merge fresh RETRY-02 PR
merge_method = merge
expected_head_sha = exact C0_HEAD
```

may create the canonical effect.

Immediately before merge, re-read exact main/C0/S0/Q_K/D0 predicates.

After the operation, independently establish actual canonical effect truth.

The future packet must require, at minimum:

- `main` points to the generated merge commit;
- generated merge commit TREE = exact C0_TREE;
- parent 1 = exact frozen pre-effect main HEAD;
- parent 2 = exact C0_HEAD;
- exact path exists with exact C0 blob;
- no extra path/content change exists;
- PR is recorded merged by the authorized path/method.

`COMMAND SUCCESS != EFFECT TRUTH`

`SYSTEM UNDER TEST != AUTHORITY TO DECLARE TEST SUCCESSFUL`

Unknown before effect:

`BLOCKED -> NO MERGE -> STOP`

Effect occurred but exact post-state cannot be established:

`INDETERMINATE -> STOP`

## 18. Evidence requirements

The future packet must preregister evidence capture sufficient to distinguish at least:

- intended operation from actual operation;
- detached object creation from live branch-ref mutation;
- command success from effect truth;
- review visibility from valid D0;
- generic mergeability from method-specific effect eligibility;
- tree equality from exact commit identity;
- historical review event from current review event;
- canonical state from candidate branch state.

For every T2/T3 ref transition, capture:

```text
operation id
primitive
branch
force flag
PRE_HEAD observed
POST_HEAD requested
POST_HEAD observed
expected commit TREE
observed commit TREE
expected parent
observed parent
candidate path set
canonical main HEAD/TREE before
canonical main HEAD/TREE after
```

## 19. Outcome taxonomy

### PASS

Only if all exact T0-T5 predicates pass and the exact positive control effect is independently verified.

`A5 TECHNICAL PASS != HUMAN ACCEPT`

### FAIL

First credible counterexample in T2, T3, or T4.

`FIRST CREDIBLE COUNTEREXAMPLE -> FAIL -> DURABLE FINDING -> STOP`

### BLOCKED

Use before canonical effect for, at minimum:

- invalid D0;
- target/governance drift;
- operation ambiguity;
- method-specific evidence unavailable;
- unexpected candidate HEAD;
- accidental no-op commit;
- alternate mutation primitive;
- failed or uncertain reset;
- execution-trace deviation;
- any need for repair or runtime improvisation.

`BLOCKED -> STOP`

### INDETERMINATE

Use only after canonical effect if exact post-effect truth cannot be established.

`INDETERMINATE -> STOP`

## 20. STOP rules

STOP immediately on:

- first credible counterexample;
- invalid D0;
- candidate identity mismatch;
- unexpected ref movement;
- any unpreregistered commit on the live probe branch;
- any mutation primitive other than the exact frozen primitive;
- target/governance drift;
- reset ambiguity;
- method-specific evidence ambiguity;
- exogenous canonical main move;
- post-effect uncertainty;
- any need to repair, redesign, reinterpret, or improvise materially.

After STOP, do not repair and continue the same run.

## 21. What this preregistration preparation authorized

The Human authorization for this stage permitted only:

- read-only evidence collection;
- creation of this RETRY-02 preregistration artifact in FJ899/8;
- durable freeze in one dedicated Draft PR;
- read-only verification of resulting commit/tree/blob identity;
- STOP.

It did not authorize:

- any ScriptOps mutation;
- creation of a RETRY-02 candidate;
- attack-variant materialization;
- packet preparation;
- AK-CANON review;
- Ready/review/approval/D0;
- T0-T5 execution;
- reset or repair of PR #29;
- any action on PR #29, #28, or #27;
- CODEOWNERS/ruleset changes;
- canonical effect;
- V1;
- release;
- deployment;
- tag.

## 22. State at preregistration freeze

```text
#80: ORIGINAL A5 BLOCKED RUN — PRESERVED
#81: RETRY-01 PREREGISTRATION — PRESERVED
#82: RETRY-01 CANDIDATE FREEZE — PRESERVED
#83: RETRY-01 PACKET — PRESERVED
#84: RETRY-01 AK-CANON PASS — PRESERVED
#85: RETRY-01 TERMINAL BLOCKED AT T3 — PRESERVED

ScriptOps #29: RETRY-01 HISTORICAL TARGET / DO NOT REPAIR OR CONTINUE
ScriptOps #28: HISTORICAL HOLD
ScriptOps #27: DO NOT MERGE

RETRY-02 PREREGISTRATION: PREPARED
RETRY-02 PROBE: DOES NOT EXIST
RETRY-02 DETACHED ATTACK VARIANTS: DO NOT EXIST
RETRY-02 PRE-EXECUTION PACKET: NOT PREPARED
RETRY-02 AK-CANON REVIEW: NOT STARTED
RETRY-02 EXECUTION: NOT AUTHORIZED / NOT STARTED
RETRY-02 D0: DOES NOT EXIST
CANONICAL EFFECT: NONE
V1: STOP
```

# STOP
