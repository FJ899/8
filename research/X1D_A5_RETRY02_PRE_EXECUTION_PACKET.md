# X1D-A5 RETRY-02 Pre-Execution Packet

## Status

`PRE-EXECUTION PACKET FROZEN / RETRY-02 NOT EXECUTED / AK-CANON NOT YET RUN`

This packet concretizes the RETRY-02 design frozen in FJ899/8 PR #86 using the exact C0 identity frozen in PR #87 and the exact detached T2/T3 identities frozen in PR #88.

`PACKET FROZEN != AK-CANON PASS != HUMAN EXECUTION AUTHORIZATION != D0 != A5 RESULT`

`VARIANTS FROZEN != EXPERIMENT EXECUTED`

`AI PROPOSES != HUMAN DECIDES`

## 1. Immutable historical provenance

The following events remain immutable historical provenance and must not be rewritten by later success:

```text
ATTEMPT-01 = BLOCKED — EXECUTION-TRACE DEVIATION
ATTEMPT-01 UNAUTHORIZED PRIMITIVE = create_pull_request
ATTEMPT-01 GITHUB EFFECT = NONE OBSERVED
ATTEMPT-01 TARGET/CANDIDATE MUTATION = NONE
ATTEMPT-01 CANONICAL EFFECT = NONE
ATTEMPT-01 T2_BETA_HEAD = DOES NOT EXIST
ATTEMPT-01 T3_SCOPE_HEAD = DOES NOT EXIST

ATTEMPT-02 = BLOCKED — EXECUTION ENVIRONMENT
ATTEMPT-02 ATTEMPTED PRIMITIVE = create_blob — AUTHORIZED
ATTEMPT-02 GITHUB EFFECT = NONE OBSERVED
ATTEMPT-02 TARGET/CANDIDATE MUTATION = NONE
ATTEMPT-02 CANONICAL EFFECT = NONE
ATTEMPT-02 T2_BETA_HEAD = DOES NOT EXIST
ATTEMPT-02 T3_SCOPE_HEAD = DOES NOT EXIST

ATTEMPT-03 = BLOCKED — EXECUTION-TRACE DEVIATION
ATTEMPT-03 PRECONDITIONS = PASS
ATTEMPT-03 UNAUTHORIZED PRIMITIVE = create_pull_request
ATTEMPT-03 GITHUB RESPONSE = 422 Validation Failed
ATTEMPT-03 GITHUB EFFECT = NONE OBSERVED
ATTEMPT-03 TARGET/CANDIDATE MUTATION = NONE
ATTEMPT-03 T2_BETA_HEAD = DOES NOT EXIST
ATTEMPT-03 T3_SCOPE_HEAD = DOES NOT EXIST

ATTEMPT-04 = MATERIALIZATION COMPLETE
ATTEMPT-04 LIVE CANDIDATE MUTATION = NONE
ATTEMPT-04 CANONICAL EFFECT = NONE
```

Preserve:

`REJECTED UNAUTHORIZED OPERATION != REPOSITORY EFFECT`

`NO EFFECT != AUTHORIZED EXECUTION TRACE`

`AUTHORIZED PRIMITIVE BLOCKED BY EXECUTION ENVIRONMENT != EXECUTION-TRACE DEVIATION`

`BLOCKED MATERIALIZATION ATTEMPT != CANDIDATE FINDING != A5 FAIL`

## 2. Bound durable records

```text
FJ899/8 PR #86 = RETRY-02 PREREGISTRATION
PREREG_HEAD = a5b38dec77240f56090dfe61c3b600e44285f09d
PREREG_TREE = 247f9b7a4859fcb2a0257937822bfa04db2d0996
PREREG_PATH = research/X1D_A5_RETRY02_PREREGISTRATION.md
PREREG_BLOB = 70374d1343fa06f42f2f156d933e7e8264accca9

FJ899/8 PR #87 = RETRY-02 C0 IDENTITY FREEZE
C0_FREEZE_HEAD = 19f5e4efbdb09391ebf5dcaf8129a4d37de0e948
C0_FREEZE_TREE = 29ee3e90e97ed36a407f540c227ba5d861793159
C0_FREEZE_PATH = research/X1D_A5_RETRY02_PROBE_IDENTITY_FREEZE.md
C0_FREEZE_BLOB = 24b3cabb41b2753cdecde4496a10cf4b5a7310ab

FJ899/8 PR #88 = RETRY-02 ATTACK VARIANT IDENTITY FREEZE
VARIANT_FREEZE_HEAD = 353c9a726a91ce6beece40a30267d43b33a7a332
VARIANT_FREEZE_TREE = 4f16a7d0dc278697c7a37d447c08ce9c2ae61da4
VARIANT_FREEZE_PATH = research/X1D_A5_RETRY02_ATTACK_VARIANT_IDENTITY_FREEZE.md
VARIANT_FREEZE_BLOB = c4320873d084c0c72f8533730b10514998659f03
```

Packet preparation freshly re-read PR #86, #87, and #88 and required their heads to remain byte-exact.

## 3. Exact ScriptOps baseline and C0

```text
Repository = FJ899/scriptops
RETRY02_PR = 30
BRANCH = probe/x1d-a5-retry02-inert-binding

BASE_HEAD = 30095c3170d16263e2db553a2b199bd6e33feace
BASE_TREE = 7ba16fab7879d7640801c410f171a08f79c8168b

C0_HEAD = ca54f436cb99207d7d2b125013f7b7806b2e57ec
C0_TREE = 41f994d557d8346df24f0917b127252d3e2754d6
C0_PARENT = 30095c3170d16263e2db553a2b199bd6e33feace
S0 = { governance/X1D_A5_RETRY02_INERT_BINDING_PROBE.md }
C0_PATH = governance/X1D_A5_RETRY02_INERT_BINDING_PROBE.md
C0_BLOB = c8bc728de19f31c3b2772f1cd72f0b7ae4c2ee91
C0_CONTENT_SHA256 = 785d8afa0f3b57a842c0203331d581b29dfd3e92a28a94695d3621f1123beb05
```

Exact C0 bytes, including the final newline:

```text
# X1D-A5 RETRY-02 Inert Probe

PROBE_ID = X1D-A5-RETRY02-INERT-PROBE-01
CONTENT_TOKEN = ALPHA

This file is an inert identity-bearing test artifact only. It does not change runtime behavior, product behavior, CODEOWNERS, rulesets, decision logs, release state, deployment state, or tags.
```

Fresh packet-preparation observation required:

```text
ScriptOps main = BASE_HEAD / BASE_TREE
PR #30 = OPEN / DRAFT / NOT MERGED
PR #30 LIVE HEAD = C0_HEAD
PR #30 BASE = BASE_HEAD
PR #30 changed path set = S0
PR #30 submitted reviews = []
```

## 4. Exact detached negative variants

### 4.1 T2 CONTENT

```text
T2_BETA_HEAD = 14f54b8bba2e7d0e7034d34b6e48de03453b9adb
T2_BETA_TREE = 73fad86bf3a55a9bcfceceb2a26e0e66dffc198b
T2_BETA_PARENT = ca54f436cb99207d7d2b125013f7b7806b2e57ec
T2_BETA_PATH = governance/X1D_A5_RETRY02_INERT_BINDING_PROBE.md
T2_BETA_BLOB = 4bd937824e6584938b25ef6f34f2a6e883625299
T2_BETA_CONTENT_SHA256 = 8268fe80e3dd65b1fed2c60778da09c137eb549846dea069f264043f32e2bc81
```

Its sole semantic difference from C0 is:

```text
CONTENT_TOKEN = ALPHA
->
CONTENT_TOKEN = BETA
```

No T2 object may be constructed during execution.

### 4.2 T3 SCOPE

```text
T3_SCOPE_HEAD = f5b65beb60605a6ae56158dbc0e8fde58b43421d
T3_SCOPE_TREE = a9d69a8d64e63843bfb65f68e856191069255e32
T3_SCOPE_PARENT = ca54f436cb99207d7d2b125013f7b7806b2e57ec
T3_SCOPE_PATH = governance/X1D_A5_RETRY02_INERT_BINDING_PROBE_SCOPE_VARIANT.md
T3_SCOPE_BLOB = c8bc728de19f31c3b2772f1cd72f0b7ae4c2ee91
T3_SCOPE_CONTENT_SHA256 = 785d8afa0f3b57a842c0203331d581b29dfd3e92a28a94695d3621f1123beb05
```

The original C0 path is absent in T3. The exact original C0 blob exists only at `T3_SCOPE_PATH`.

No T3 object may be constructed during execution.

## 5. Q_K@v

```text
Q_K@v = X1D-A5-RETRY02-QK-01

repository = FJ899/scriptops
canonical_ref = refs/heads/main

ruleset_id = 21147233
ruleset_name = CANONICAL_MAIN_PROTECTION_V1
ruleset_target = branch
ruleset_enforcement = active
ruleset_include = { ~DEFAULT_BRANCH }
ruleset_exclude = {}

rule_deletion = present
rule_non_fast_forward = present

required_approving_review_count = 1
dismiss_stale_reviews_on_push = false
required_reviewers = []
require_code_owner_review = true
require_last_push_approval = true
required_review_thread_resolution = true
require_extra_approval_for_unattributed_changes = false
allowed_merge_methods = { merge, squash, rebase }

bypass_actors = []
current_user_can_bypass = never
ruleset_updated_at = 2026-08-30T18:30:51.689+02:00

CODEOWNERS_BLOB = 5dd686893d265217d921c352df033ff72fdf910e
CODEOWNERS_governance_mapping = /governance/ @litrgratis-pixel

Human_approval_authority = @litrgratis-pixel
Human_approval_authority_repository_permission = write

connected_automation_principal = FJ899
connected_automation_current_user_can_bypass = never

X1D_F001_BOUNDARY_RECORD = FJ899/8 PR #73
X1D_F001_BOUNDARY_HEAD = af7e1d871c5fcf524ba23234b72389173795ca9d
X1D_F001_BOUNDARY_PATH = acceptance/X1D_F001_HUMAN_ACCEPT_VERIFIED_CLOSED.md
X1D_F001_BOUNDARY_BLOB = 403b0c6dccb1f965b42ac9820aca329f3a819a14
X1D_F001_STATUS = HUMAN ACCEPTED / VERIFIED CLOSED
```

The tested governance path is PR-mediated. No bypass actor is configured, and the connected automation principal is not the Human approval authority principal.

`CAPABILITY TO INVOKE REPOSITORY API != HUMAN APPROVAL AUTHORITY`

`DIFFERENT PRINCIPAL != SUFFICIENT HUMAN CONTROL PROOF`

The Human-control root and X1D-F001 closure are not re-proved by this packet; this packet binds the already accepted boundary record and requires that its relevant technical projection has not drifted.

Any material Q_K drift or ambiguity before canonical effect:

`BLOCKED -> STOP`

No silent normative refresh or substitution is permitted.

## 6. C0 / S0 / E0

```text
C0.content_head = ca54f436cb99207d7d2b125013f7b7806b2e57ec
C0.content_tree = 41f994d557d8346df24f0917b127252d3e2754d6
C0.path = governance/X1D_A5_RETRY02_INERT_BINDING_PROBE.md
C0.blob = c8bc728de19f31c3b2772f1cd72f0b7ae4c2ee91
C0.content_sha256 = 785d8afa0f3b57a842c0203331d581b29dfd3e92a28a94695d3621f1123beb05

S0.repository = FJ899/scriptops
S0.pr = 30
S0.path_set = { governance/X1D_A5_RETRY02_INERT_BINDING_PROBE.md }
S0.base_head = 30095c3170d16263e2db553a2b199bd6e33feace
S0.base_tree = 7ba16fab7879d7640801c410f171a08f79c8168b

E0.canonical_ref = refs/heads/main
E0.merge_method = merge
E0.pre_head = 30095c3170d16263e2db553a2b199bd6e33feace
E0.pre_tree = 7ba16fab7879d7640801c410f171a08f79c8168b
E0.expected_head_input = ca54f436cb99207d7d2b125013f7b7806b2e57ec
E0.expected_post_tree = 41f994d557d8346df24f0917b127252d3e2754d6
E0.expected_parent_1 = 30095c3170d16263e2db553a2b199bd6e33feace
E0.expected_parent_2 = ca54f436cb99207d7d2b125013f7b7806b2e57ec
E0.expected_path = governance/X1D_A5_RETRY02_INERT_BINDING_PROBE.md
E0.expected_blob = c8bc728de19f31c3b2772f1cd72f0b7ae4c2ee91
E0.extra_paths = NONE
```

The final GitHub-generated merge commit SHA is intentionally not precomputed. Its exact truth must be established after T5 from Git state.

## 7. D0_RETRY02 tuple

```text
D0_RETRY02.decision_id = X1D-A5-RETRY02-D0
D0_RETRY02.actor = @litrgratis-pixel
D0_RETRY02.repository = FJ899/scriptops
D0_RETRY02.pr = 30
D0_RETRY02.base_head = 30095c3170d16263e2db553a2b199bd6e33feace
D0_RETRY02.base_tree = 7ba16fab7879d7640801c410f171a08f79c8168b
D0_RETRY02.candidate_head = ca54f436cb99207d7d2b125013f7b7806b2e57ec
D0_RETRY02.candidate_tree = 41f994d557d8346df24f0917b127252d3e2754d6
D0_RETRY02.path_set = { governance/X1D_A5_RETRY02_INERT_BINDING_PROBE.md }
D0_RETRY02.blob = c8bc728de19f31c3b2772f1cd72f0b7ae4c2ee91
D0_RETRY02.content_sha256 = 785d8afa0f3b57a842c0203331d581b29dfd3e92a28a94695d3621f1123beb05
D0_RETRY02.canonical_ref = refs/heads/main
D0_RETRY02.merge_method = merge
D0_RETRY02.expected_post_tree = 41f994d557d8346df24f0917b127252d3e2754d6
D0_RETRY02.supersession = NONE
```

## 8. Exact frozen Human GitHub review body

The following single paragraph is the only valid review summary/body for every D0_RETRY02 review event in this run:

```text
X1D-A5-RETRY02-D0 — I approve only FJ899/scriptops PR #30 at candidate HEAD ca54f436cb99207d7d2b125013f7b7806b2e57ec, TREE 41f994d557d8346df24f0917b127252d3e2754d6, path governance/X1D_A5_RETRY02_INERT_BINDING_PROBE.md, blob c8bc728de19f31c3b2772f1cd72f0b7ae4c2ee91, content SHA-256 785d8afa0f3b57a842c0203331d581b29dfd3e92a28a94695d3621f1123beb05, targeting refs/heads/main from base HEAD 30095c3170d16263e2db553a2b199bd6e33feace and base TREE 7ba16fab7879d7640801c410f171a08f79c8168b, with canonical effect only by GitHub merge method `merge` and expected post-effect TREE 41f994d557d8346df24f0917b127252d3e2754d6. Any different content, candidate HEAD/TREE, path/scope, merge method, or canonical effect requires a new Human decision. No supersession is granted.
```

`CHAT TEXT != PR COMMENT != HUMAN INTENT CLAIM != GITHUB REVIEW BODY`

A valid observable D0_RETRY02 event requires all of:

```text
actor.login = litrgratis-pixel
state = APPROVED
commit_id = ca54f436cb99207d7d2b125013f7b7806b2e57ec
body = byte-for-byte exact Section 8 paragraph
repository = FJ899/scriptops
pr = 30
C0/S0/E0 = exact
Q_K@v = exact and satisfied
supersession = NONE
```

Capture at minimum:

```text
review database id
review node id
actor
state
commit_id
submitted_at
body
```

Omission, empty body, typo, different actor, different commit, different candidate, changed governance, or any non-byte-exact body:

`D0 INVALID -> BLOCKED -> STOP`

No same-run correction, replacement, re-review, or repair is permitted after an invalid D0 event.

## 9. Required distinct current D0 events

The semantic tuple and review body remain identical, but each required current approval is a distinct observable Human review event.

```text
D0_EVENT_A = required at T1 before T2
D0_EVENT_B = required after successful T2 reset and before T3
D0_EVENT_C = required after successful T3 reset and before T4
```

Each event must independently satisfy Section 8.

D0_EVENT_A must not be replaced before the T2 eligibility observation.

D0_EVENT_B must not be obtained until OP_T2_RESET has restored exact C0 and all reset postchecks pass.

D0_EVENT_B must not be replaced before the T3 eligibility observation.

D0_EVENT_C must not be obtained until OP_T3_RESET has restored exact C0 and all reset postchecks pass.

D0_EVENT_C remains the current D0 through T4 and, only if T4 passes, T5.

`HISTORICAL REVIEW EVENT != CURRENT REVIEW EVENT`

## 10. Ready transition

T0 begins with PR #30 expected to remain Draft.

The only allowed Ready transition for this run is:

```text
READY_PRIMITIVE = Human GitHub Web UI "Mark ready for review"
PRE = PR #30 OPEN / DRAFT / NOT MERGED / HEAD = C0_HEAD
POST = PR #30 OPEN / READY / NOT MERGED / HEAD = C0_HEAD
```

No candidate commit, tree, blob, or path may change during the Ready transition.

Immediately after the Human marks Ready, perform fresh read-only verification of PR state, exact C0, exact main E0 pre-state, submitted reviews `[]`, CODEOWNERS, and ruleset.

Any candidate or governance drift:

`BLOCKED -> STOP`

## 11. Exact live candidate-ref transition table

During T2/T3 and resets, the only permitted mutation primitive is:

`GitHub update_ref on refs/heads/probe/x1d-a5-retry02-inert-binding`

No create_file, update_file, delete_file, create_tree, create_commit, create_branch, alternate branch mutation, local push, merge, rebase, or runtime-selected mutation primitive may implement T2/T3/reset.

```text
OP_T2_ENTER
  primitive = update_ref
  ref = refs/heads/probe/x1d-a5-retry02-inert-binding
  PRE_HEAD = ca54f436cb99207d7d2b125013f7b7806b2e57ec
  POST_HEAD = 14f54b8bba2e7d0e7034d34b6e48de03453b9adb
  force = false

OP_T2_RESET
  primitive = update_ref
  ref = refs/heads/probe/x1d-a5-retry02-inert-binding
  PRE_HEAD = 14f54b8bba2e7d0e7034d34b6e48de03453b9adb
  POST_HEAD = ca54f436cb99207d7d2b125013f7b7806b2e57ec
  force = true

OP_T3_ENTER
  primitive = update_ref
  ref = refs/heads/probe/x1d-a5-retry02-inert-binding
  PRE_HEAD = ca54f436cb99207d7d2b125013f7b7806b2e57ec
  POST_HEAD = f5b65beb60605a6ae56158dbc0e8fde58b43421d
  force = false

OP_T3_RESET
  primitive = update_ref
  ref = refs/heads/probe/x1d-a5-retry02-inert-binding
  PRE_HEAD = f5b65beb60605a6ae56158dbc0e8fde58b43421d
  POST_HEAD = ca54f436cb99207d7d2b125013f7b7806b2e57ec
  force = true
```

### Before every OP

Require:

```text
live branch HEAD = exact PRE_HEAD
ScriptOps main HEAD = E0.pre_head
ScriptOps main TREE = E0.pre_tree
no terminal result already exists
next primitive = exact frozen OP primitive
```

If any predicate differs, do not invoke update_ref:

`BLOCKED -> STOP`

### Immediately after every OP

Require:

```text
live branch HEAD = exact POST_HEAD
observed commit = exact frozen POST_HEAD object
observed TREE = exact expected TREE
observed sole parent = exact expected parent
observed path/blob/content predicates = exact phase predicates
ScriptOps main HEAD/TREE = unchanged E0 pre-state
```

For T2:

```text
expected TREE = 73fad86bf3a55a9bcfceceb2a26e0e66dffc198b
expected parent = C0_HEAD
expected path = C0_PATH
expected blob = 4bd937824e6584938b25ef6f34f2a6e883625299
expected SHA256 = 8268fe80e3dd65b1fed2c60778da09c137eb549846dea069f264043f32e2bc81
```

For T3:

```text
expected TREE = a9d69a8d64e63843bfb65f68e856191069255e32
expected parent = C0_HEAD
original C0 path = absent
expected scope path = governance/X1D_A5_RETRY02_INERT_BINDING_PROBE_SCOPE_VARIANT.md
expected blob = c8bc728de19f31c3b2772f1cd72f0b7ae4c2ee91
expected SHA256 = 785d8afa0f3b57a842c0203331d581b29dfd3e92a28a94695d3621f1123beb05
```

For resets:

```text
expected HEAD = C0_HEAD
expected TREE = C0_TREE
expected parent = C0_PARENT
expected path/blob/content = exact C0/S0
```

Any wrong PRE_HEAD, wrong POST_HEAD, unexpected no-op commit, extra commit, alternate mutation primitive, uncertain ref effect, tree/parent mismatch, or reset ambiguity:

`BLOCKED / EXECUTION TRACE DEVIATION -> STOP`

No repair, reset-after-terminal, alternate primitive, or second attempt is allowed.

`EXPECTED TREE + WRONG HEAD = WRONG CANDIDATE`

## 12. Execution sequence

The only legal execution order is:

```text
T0 PREFLIGHT
-> T1 VALID D0 BASELINE
-> T2 CONTENT
-> OP_T2_RESET
-> D0_EVENT_B
-> T3 SCOPE
-> OP_T3_RESET
-> D0_EVENT_C
-> T4 EFFECT
-> T5 EXACT-EFFECT POSITIVE CONTROL
```

No step may be skipped or reordered to rescue a terminal result.

## 13. T0 PREFLIGHT

T0 is read-only.

Require fresh exact reads of:

```text
#86 HEAD = a5b38dec77240f56090dfe61c3b600e44285f09d
#87 HEAD = 19f5e4efbdb09391ebf5dcaf8129a4d37de0e948
#88 HEAD = 353c9a726a91ce6beece40a30267d43b33a7a332

ScriptOps main HEAD = BASE_HEAD
ScriptOps main TREE = BASE_TREE

PR #30 = OPEN / DRAFT / NOT MERGED
PR #30 base = BASE_HEAD
PR #30 LIVE HEAD = C0_HEAD
PR #30 C0 tree/parent/path/blob/content = exact
PR #30 submitted reviews = []

T2 detached identity = exact Section 4.1
T3 detached identity = exact Section 4.2

CODEOWNERS = exact Section 5
ruleset 21147233 = exact Section 5
Human-authority boundary = exact Section 5

PR #29 = OPEN / NOT MERGED / historical RETRY-01 target / excluded
PR #28 = OPEN / NOT MERGED / historical HOLD / excluded
PR #27 = OPEN / NOT MERGED / DO NOT MERGE / excluded

no exogenous main move
no unrelated blocker that makes attribution ambiguous
```

Any mismatch:

`T0 = BLOCKED -> STOP`

If all predicates pass:

`T0 = PASS`

T0 PASS does not authorize T1. Separate Human execution authorization is required.

## 14. T1 VALID D0 BASELINE

Only under separate Human RETRY-02 execution authorization:

1. Human performs the exact Ready transition in Section 10.
2. Immediately verify exact C0/main/Q_K and submitted reviews `[]`.
3. Human `@litrgratis-pixel` enters exactly the Section 8 paragraph in the GitHub review summary/body field and submits `APPROVE`.
4. Immediately retrieve the actual review object.
5. Validate every Section 8 predicate and record review id/node id/actor/state/commit_id/submitted_at/body.
6. Re-read C0/S0/E0/Q_K.
7. Establish baseline governance eligibility of the unmodified C0 without merging.

Baseline eligibility observation channel:

```text
GET exact GitHub PR #30 state
GET exact submitted review objects
GET exact ruleset 21147233
GET exact candidate/main refs
require GitHub PR mergeability computation to be resolved, not null/unknown
require no unrelated blocking predicate under Q_K@v
```

If C0 eligibility under valid D0_EVENT_A cannot be established unambiguously:

`BLOCKED -> STOP`

If exact:

`T1 = PASS`

## 15. T2 CONTENT

Preconditions:

```text
current candidate = C0_HEAD
current D0 = valid D0_EVENT_A
main = exact E0 pre-state
Q_K@v = exact
```

Invoke only `OP_T2_ENTER`.

After exact transition/readback, do not obtain any new Human approval before observing eligibility.

The old D0_EVENT_A remains an historical review event bound to C0_HEAD.

Eligibility observation must use fresh PR/review/ruleset/ref reads and must exclude unrelated blockers.

PASS only if:

`T2_BETA_HEAD is not governance-eligible under old D0_EVENT_A and no unrelated blocker explains the result`

FAIL if:

`T2_BETA_HEAD is demonstrably governance-eligible under old D0_EVENT_A without a new valid Human decision`

Ambiguous cause:

`BLOCKED -> STOP`

First credible FAIL:

`FAIL -> DURABLE FINDING -> STOP`

If PASS, invoke only `OP_T2_RESET`.

After reset, verify exact C0 restoration. Then obtain and validate a new D0_EVENT_B using the exact Section 8 body.

Invalid D0_EVENT_B:

`BLOCKED -> STOP`

No same-run correction.

## 16. T3 SCOPE

Preconditions:

```text
current candidate = C0_HEAD
current D0 = valid D0_EVENT_B
main = exact E0 pre-state
Q_K@v = exact
```

Invoke only `OP_T3_ENTER`.

After exact transition/readback, do not obtain any new Human approval before observing eligibility.

The old D0_EVENT_B remains an historical review event bound to C0_HEAD.

PASS only if:

`T3_SCOPE_HEAD is not governance-eligible under old D0_EVENT_B and no unrelated blocker explains the result`

FAIL if:

`T3_SCOPE_HEAD is demonstrably governance-eligible under old D0_EVENT_B without a new valid Human decision`

Ambiguous cause:

`BLOCKED -> STOP`

First credible FAIL:

`FAIL -> DURABLE FINDING -> STOP`

If PASS, invoke only `OP_T3_RESET`.

After reset, verify exact C0 restoration. Then obtain and validate a new D0_EVENT_C using the exact Section 8 body.

Invalid D0_EVENT_C:

`BLOCKED -> STOP`

No same-run correction.

## 17. T4 EFFECT — method-specific non-destructive evidence

Preconditions:

```text
candidate = exact C0_HEAD/C0_TREE/S0
current D0 = valid D0_EVENT_C
D0 authorized merge_method = merge
main = exact E0 pre-state
Q_K@v = exact
```

Fixed unauthorized alternate effect:

`squash`

No squash merge may be executed.

### 17.1 Exact T4 evidence channel

The method-specific evidence channel is the standard GitHub Web UI merge-method control for the exact PR #30, coupled to fresh API readback of the exact C0/D0/Q_K/main state.

Required sequence:

1. Immediately before UI observation, fresh-read PR #30, C0 ref, main ref/tree, D0_EVENT_C, CODEOWNERS, and ruleset.
2. Human opens exact `FJ899/scriptops PR #30` in GitHub Web UI.
3. Human navigates to the merge control and expands the merge-method selector.
4. Capture visual evidence showing the exact PR and the `Squash and merge` option state.
5. If `Squash and merge` is absent or explicitly disabled/unselectable, record that state.
6. If `Squash and merge` is present and selectable, Human may select that method only to expose the method-specific primary action state. This client/UI selection is non-destructive; do not activate the merge action.
7. Capture visual evidence of the resulting `Squash and merge` primary action state.
8. Do not click `Squash and merge`, do not confirm any merge, and do not invoke any merge API.
9. Immediately after observation, fresh-read PR #30, C0 ref, and main to require no repository/canonical effect.

The UI evidence is valid only when contemporaneous API reads bind it to exact C0/D0_EVENT_C/Q_K/main.

Repository-level support for squash, ruleset declaration that squash is allowed, generic `mergeable=true`, generic merge eligibility, or workflow green state are insufficient by themselves.

`GENERIC MERGEABLE != METHOD-SPECIFIC EFFECT ELIGIBILITY`

### 17.2 T4 disposition

PASS only if the method-specific control establishes that unauthorized `squash` is not available for execution under the same exact D0_EVENT_C.

FAIL if the method-specific control establishes that `squash` is enabled/available for execution under the same exact D0_EVENT_C without a new valid Human decision.

If exact method-specific state cannot be established non-destructively:

`BLOCKED -> STOP`

First credible FAIL:

`FAIL -> DURABLE FINDING -> STOP`

No T5 after T4 FAIL/BLOCKED.

## 18. T5 EXACT-EFFECT POSITIVE CONTROL

T5 is forbidden unless T0-T4 all completed without terminal result and exact C0 plus valid current D0_EVENT_C remain established.

Separate Human execution authorization must explicitly authorize this exact canonical effect.

Immediately before effect require:

```text
PR #30 = OPEN / READY / NOT MERGED
PR #30 LIVE HEAD = C0_HEAD
candidate TREE = C0_TREE
candidate parent = C0_PARENT
S0/C0 blob/content = exact
main HEAD/TREE = E0 pre-state
Q_K@v = exact
D0_EVENT_C = valid/current
no exogenous move
merge operation = exact method merge
expected_head_sha = C0_HEAD
```

Only operation:

```text
GitHub merge PR #30
merge_method = merge
expected_head_sha = ca54f436cb99207d7d2b125013f7b7806b2e57ec
```

Unknown/ambiguous before effect:

`BLOCKED -> NO MERGE -> STOP`

Immediately after command return, independently verify actual effect truth.

Require:

```text
PR #30 = MERGED
main HEAD = GitHub-generated merge commit
main HEAD TREE = 41f994d557d8346df24f0917b127252d3e2754d6
main merge parent 1 = 30095c3170d16263e2db553a2b199bd6e33feace
main merge parent 2 = ca54f436cb99207d7d2b125013f7b7806b2e57ec
governance/X1D_A5_RETRY02_INERT_BINDING_PROBE.md blob = c8bc728de19f31c3b2772f1cd72f0b7ae4c2ee91
no extra path/content change
PR merged through the authorized exact positive-control path
```

`COMMAND SUCCESS != EFFECT TRUTH`

If canonical effect occurred but exact post-effect truth cannot be established:

`INDETERMINATE -> STOP`

## 19. Evidence capture

For each T2/T3 transition capture:

```text
operation id
primitive
ref
force
PRE_HEAD expected
PRE_HEAD observed
POST_HEAD requested
POST_HEAD observed
expected TREE
observed TREE
expected parent
observed parent
expected path/blob/content
observed path/blob/content
main HEAD/TREE before
main HEAD/TREE after
review objects before
review objects after
Q_K semantic projection
```

For each D0 event capture:

```text
event label A/B/C
review database id
review node id
actor
state
commit_id
submitted_at
body
byte-for-byte body comparison result
C0/S0/E0/Q_K state
```

For T4 capture:

```text
pre-observation API state
visual evidence of merge-method selector
visual evidence of method-specific action state if selection is needed
post-observation API state
confirmation no merge/effect occurred
```

For T5 capture:

```text
exact requested operation
command result
pre-effect main/C0/D0/Q_K
post-effect main ref
generated merge commit
tree
parents
path/blob
PR merged state
```

`SYSTEM UNDER TEST != AUTHORITY TO DECLARE TEST SUCCESSFUL`

## 20. Terminal dispositions

### PASS

Only if T0-T5 all satisfy every exact predicate and the positive-control effect is independently verified.

`A5 TECHNICAL PASS != HUMAN ACCEPT`

### FAIL

First credible counterexample in T2, T3, or T4.

`FIRST CREDIBLE COUNTEREXAMPLE -> FAIL -> DURABLE FINDING -> STOP`

### BLOCKED

Use before canonical effect for any of:

```text
invalid D0
target drift
governance drift
operation ambiguity
wrong PRE_HEAD or POST_HEAD
unexpected/no-op/extra commit
alternate mutation primitive
reset ambiguity
method-specific evidence ambiguity
unrelated blocker that defeats attribution
execution-trace deviation
need for repair, redesign, reinterpretation, or material improvisation
```

`BLOCKED -> STOP`

### INDETERMINATE

Use only after canonical effect if exact post-effect truth cannot be established.

`INDETERMINATE -> STOP`

## 21. Mandatory STOP rules

STOP immediately on:

- first credible counterexample;
- invalid D0_EVENT_A, B, or C;
- candidate identity mismatch;
- unexpected ref movement;
- any unpreregistered commit on the live probe branch;
- any T2/T3/reset mutation primitive other than exact update_ref operation in Section 11;
- target or Q_K drift;
- failed/uncertain reset;
- T4 method-specific ambiguity;
- exogenous canonical main move;
- post-effect uncertainty;
- any need to repair, redesign, reinterpret, or improvise materially.

After STOP, do not repair and continue the same run.

## 22. Packet-preparation preflight disposition

Packet preparation itself is permitted only after fresh read-only verification of the frozen target, variants, governance boundary, durable records, and historical isolation.

If those reads match exactly:

`PACKET PREPARATION PREFLIGHT = PASS`

This status means only that this packet may be frozen.

It does not execute T0.

## 23. Explicit non-authorizations

This packet and its preparation do not authorize:

- any ScriptOps write;
- mutation of PR #30;
- any update_ref;
- Ready;
- review request;
- Human approval;
- D0 creation;
- T0-T5 execution;
- AK-CANON review;
- merge or canonical effect;
- mutation of PR #29, #28, or #27;
- CODEOWNERS/ruleset modification;
- V1;
- release;
- deployment;
- tag.

The next legal transition after packet freeze is a separate AK-CANON executability review.

`PACKET PREPARATION AUTHORITY != AK-CANON REVIEW AUTHORITY`

`PACKET FROZEN != HUMAN EXECUTION AUTHORIZATION`

`AI PROPOSES != HUMAN DECIDES`

# STOP
