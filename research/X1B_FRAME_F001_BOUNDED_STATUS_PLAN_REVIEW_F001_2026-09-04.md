# X1B-FRAME F001 — Independent Bounded Status-Plan Review — First Finding

Status: `PLAN REVIEW FAIL / FIRST CREDIBLE COUNTEREXAMPLE / STOP`

Date: `2026-09-04`

## 1. Review target

Exact plan under review:

```text
FJ899/8 PR #184
HEAD = 4924e395c96158bfd148ef9b6841e0f0bebb09e6
TREE = d41e8797e9aa49f9c6dbfe6909fb197c75e54572
PATH = research/X1B_FRAME_F001_BOUNDED_STATUS_PROPAGATION_CORRECTION_PLAN_2026-09-04.md
BLOB = 38d2008a0c9fc5f6edfcdb95bd53790bb239ef94
```

Review authority comes from the Human-accepted disposition recorded in PR #183, which authorizes one independent read-only review of this exact bounded plan and no implementation.

## 2. Verdict

```text
X1B-FRAME F001 STATUS-PROPAGATION PLAN REVIEW = FAIL
FIRST CREDIBLE PLAN COUNTEREXAMPLE = STOP
```

Finding:

```text
X1B-FRAME-F001-PLAN-F001 — OFFLINE CHECKED-OUT RUNTIME CLASSIFICATION
CAN BE USED TO ACCEPT ACTIVE_PRODUCT_REMEDIATED=YES ON A V2 PR CANDIDATE
BEFORE THE ACTIVE DEFAULT BRANCH IS ACTUALLY CHANGED
```

Primary class:

```text
CANDIDATE / ACTIVE-STATE COLLAPSE IN PLAN SEMANTICS
```

This is a plan defect. It is not an X1B runtime-property falsification and does not reopen X1B.

## 3. Plan requirement attacked

The plan correctly requires the current correction candidate to represent:

```text
runtime classification = LEGACY_PRE_X1B
X1B_ACTIVE_PRODUCT_REMEDIATED = NO
```

However, section 8.2 also asks the offline repository verifier to recognize a future V2 route from checked-out source markers such as:

```text
import x1b_human_decision as x1b
x1b.approve_scene(
approve parser requires --decision-pr
```

and section 8.3 states:

```text
Any future V2 integration must update the status surfaces in the same reviewed integration candidate so that verifier/runtime/status truth stays coherent.
```

The plan also says the verifier design must avoid making `ACTIVE_PRODUCT_REMEDIATED=NO` a timeless hard-coded truth.

Those requirements do not separately bind an `ACTIVE_PRODUCT_REMEDIATED=YES` state to the real active default branch or a post-activation readback.

## 4. Minimal counterexample trace

Read-only / candidate-state trace permitted by the plan:

```text
1. Active remote ScriptOps main remains the legacy pre-X1B ref.
2. A future V2 integration PR is checked out in CI or a review workspace.
3. The checked-out candidate contains the V2 source markers required by section 8.2.
4. The same candidate updates README/PROJECT_STATE/HANDOFF to say
   X1B_ACTIVE_PRODUCT_REMEDIATED = YES,
   following the plan instruction that future V2 integration update status
   surfaces in the same integration candidate.
5. The offline verifier sees only the checked-out candidate files.
6. It classifies runtime = V2 and accepts docs/runtime coherence.
7. The verifier can therefore report a passing active-remediation status
   while remote refs/heads/main is still the old legacy implementation.
```

The plan does not require a trusted remote `refs/heads/main` read, post-merge activation event, deployment readback, or another external currentness proof before allowing the future `YES` state to become verifier-consistent.

## 5. Expected vs observed plan semantics

Expected safe plan property:

```text
CHECKED_OUT CANDIDATE CONTAINS V2
!=
ACTIVE PRODUCT REMEDIATED
```

and:

```text
ACTIVE_PRODUCT_REMEDIATED = YES
requires independent active-state / activation binding
not merely local source classification
```

Observed plan semantics admit:

```text
V2 markers in checked-out candidate
+
status text updated in same candidate
+
offline verifier coherence
->
possible PASS before active main changes
```

That recreates the exact class of frame collapse the correction is supposed to prevent:

```text
PR HEAD != ACTIVE DEFAULT BRANCH
GREEN VERIFICATION != DEPLOYED ENFORCEMENT
```

## 6. Why the existing caveats do not close the counterexample

The plan says the verifier must not independently flip status text, perform deployment, or claim PR #35 merged. That is necessary but insufficient.

The counterexample does not require the verifier to mutate anything. The candidate itself supplies the `YES` status text and the verifier merely validates candidate-local coherence.

The plan also records the PR #35 overlap hazard and forbids silently dropping the frame boundary. That prevents one form of stale-file regression, but it does not establish active-state currentness for a future `YES` claim.

## 7. Required conceptual repair direction

No repair is authorized by this review. The minimum conceptual correction that a successor plan would need to establish is:

```text
CHECKED_OUT_RUNTIME_CLASS
!=
ACTIVE_PRODUCT_REMEDIATION_STATE
```

and:

```text
OFFLINE REPOSITORY VERIFIER
may verify candidate-local status syntax / runtime classification
but
must not establish ACTIVE_PRODUCT_REMEDIATED=YES
from a PR checkout alone
```

A future `ACTIVE_PRODUCT_REMEDIATED=YES` claim must be separately bound to an actual activation/currentness fact, for example an exact post-merge/post-deployment active-ref readback or another explicitly accepted active-product identity mechanism.

Conservative intermediate truth is allowed:

```text
V2 candidate present / even merged candidate under evaluation
while active-remediation currentness not yet established
-> ACTIVE_PRODUCT_REMEDIATED remains NO / NOT ESTABLISHED
```

until the separate active-state proof occurs.

This review does not choose or authorize the final repair mechanism.

## 8. Disposition

```text
PLAN PR #184 = NOT PASS
X1B-FRAME-F001-PLAN-F001 = OPEN
IMPLEMENTATION AUTHORITY = NO
SCRIPTOPS EDIT = NO
PR #35 MERGE = NO
DEPLOYMENT = NO
X1B REOPEN = NO
V1 AUTHORITY = NO
```

Per the frozen plan-review rule:

```text
PLAN REVIEW FAIL -> DURABLE FINDING -> STOP
```

Next legal stage is a separate Human disposition of this exact plan finding and, only if authorized, preparation of a superseding bounded plan correction.

Preserve:

```text
PR HEAD != ACTIVE DEFAULT BRANCH
GREEN VERIFICATION != DEPLOYED ENFORCEMENT
PLAN REVIEW FINDING != PLAN-REPAIR AUTHORITY
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
AI PROPOSES != HUMAN DECIDES
```
