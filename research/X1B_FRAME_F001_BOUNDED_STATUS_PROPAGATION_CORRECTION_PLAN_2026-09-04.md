# X1B-FRAME F001 — Bounded Status-Propagation Correction Plan

Status: `PLAN ONLY / HUMAN-AUTHORIZED TO PREPARE / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-04`

## 1. Authority and target

Accepted finding:

```text
FJ899/8 PR #182
HEAD = 7f2c182700eea2951199467e539e3d04d037452f
TREE = 11096215dcef4722576fcb97e77c31967db7a0a0
BLOB = 1ce333cf2acb1e29657d80e0ddc0749cf50f8c27
FINDING = X1B-FRAME-F001
CLASS = STATUS/DOCUMENTATION AMBIGUITY
```

Human disposition:

```text
FJ899/8 PR #183
Human response = accept
X1B-FRAME-F001 = HUMAN ACCEPTED
ONE BOUNDED FRAME/STATUS CORRECTION PLAN = AUTHORIZED TO PREPARE
IMPLEMENTATION = NOT AUTHORIZED
```

The correction target is exactly the frame/status propagation defect. It is not the X1B runtime remediation itself.

Preserve:

```text
X1B PROPERTY FALSIFIED = NO
X1B = REMAINS CLOSED AT ACCEPTED RESEARCH/CORRECTIVE SCOPE
ACTIVE PRODUCT REMEDIATED = NOT ESTABLISHED
```

## 2. Exact ScriptOps baseline bound to this plan

```text
FJ899/scriptops refs/heads/main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Relevant baseline files:

```text
README.md
BLOB = c52f515dd3d736c749eca75cf319b514f8427c5a

PROJECT_STATE.md
BLOB = dea1d11c847765026f8766fa70aa111c3f77c7bd

HANDOFF.md
BLOB = 2e0c3be2a9bdebfeac161773ca9631f8312f42f6

scripts/verify_repository.py
BLOB = a61278086b92824d7e442b390c951e918c88517b
```

Active Human-approval runtime on this exact baseline:

```text
phase6/scriptops-v2-hardening.py
BLOB = 4f379960ed5677634dd234af6aa39626782b6133
```

Its current `cmd_approve()` accepts non-empty `--why`, performs the canonical scene write and records:

```json
"approver": "human"
```

without X1B V2 Human-decision admission.

Reviewed X1B V2 remediation remains separate:

```text
FJ899/scriptops PR #35
BASE = 2f22843ac570498b506101addeba5453ab777f08
HEAD = 7c40a92165714023743e91c63b5b11b102fadd92
TREE = 31e1f15a2e667811b9617bbb10bf6af2242961b0
STATE = OPEN / DRAFT / UNMERGED
```

The reviewed V2 runtime has the materially different route:

```text
import x1b_human_decision as x1b
x1b.approve_scene(args.scene, args.decision_pr, root=ROOT)
approve --decision-pr <number>
```

and explicitly states that `--why` is proposal text, never authority.

## 3. Correction objective

After the bounded correction is implemented on the exact baseline, a fresh consumer following the ScriptOps default-branch startup/current-state route must be able to determine, without hidden conversation context:

```text
X1B RESEARCH CLOSURE = CLOSED
ACTIVE PRODUCT REMEDIATED = NO
ACTIVE HUMAN-DECISION RUNTIME = LEGACY / PRE-X1B
REVIEWED X1B V2 REMEDIATION = PR #35 / UNMERGED
LEGACY approve --why ATTRIBUTION = NOT X1B-REMEDIATED
```

and must preserve:

```text
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
PR HEAD != ACTIVE DEFAULT BRANCH
GREEN VERIFICATION != DEPLOYED ENFORCEMENT
HISTORICAL PASS != CURRENT ACTIVE-STATE CLAIM
```

No runtime remediation is part of this correction.

## 4. Frozen implementation surface

Exactly four ScriptOps paths may change:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
scripts/verify_repository.py
```

No other path may change.

In particular, implementation must not change:

```text
phase6/scriptops-v2-hardening.py
phase6/x1b_human_decision.py
legacy/scriptops-v2-single.py
tests/*
.github/workflows/*
SOURCE_MANIFEST.md
scripts/restore_v2.py
```

The correction candidate must be exactly one commit on top of:

```text
2f22843ac570498b506101addeba5453ab777f08
```

If `FJ899/scriptops refs/heads/main` changes before implementation begins, this exact plan is no longer executable without a fresh baseline-binding disposition. Do not silently rebase the plan.

## 5. README.md required changes

Near the top-level current status, add an explicit machine- and Human-readable X1B frame block containing all of:

```text
X1B_RESEARCH_CLOSURE: CLOSED
X1B_ACTIVE_PRODUCT_REMEDIATED: NO
X1B_ACTIVE_RUNTIME: LEGACY_PRE_X1B
X1B_REVIEWED_REMEDIATION: FJ899/scriptops PR #35 / UNMERGED
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
```

The block must explain that:

1. PR #35 is a reviewed remediation candidate, not the active default branch.
2. successful corrective verification is not deployment evidence.
3. the current `approve --why` route remains physically present on active main but is pre-X1B and must not be treated as sufficient evidence for X1B Human-decision authorship.
4. no merge/deployment/V1 authority follows from X1B closure.

Current wording that says canonical Phase-6 write occurs after `approve --why` may remain only if explicitly qualified as historical/legacy behavior. It must not read as the current secure Human-authorship route.

The current `Co dalej` / next-step language must not direct a consequential Human-authorship effect through legacy `approve --why` as though that route were X1B-remediated.

Allowed bounded wording is equivalent to:

```text
The legacy Phase-6 approve --why command remains present on the active pre-X1B runtime.
It is not an X1B-remediated Human-decision-authority mechanism.
Do not derive HumanDecision authorship from that path.
```

This change does not revoke historical Phase-6 evidence; it corrects current interpretation.

## 6. PROJECT_STATE.md required changes

Add a current-state X1B section near the top of the file and ensure it is treated as part of the state-owner surface.

Required current-state facts:

```text
X1B research/corrective closure: CLOSED
active product X1B remediation: NOT DEPLOYED / NO
active default-branch runtime class: LEGACY_PRE_X1B
reviewed remediation candidate: PR #35 / UNMERGED
```

The existing responsibility-model line:

```text
human approve --why = semantic decision
```

must no longer appear as an unqualified current X1B Human-authorship rule.

It may be retained only as explicitly historical Phase-6 semantics, for example:

```text
historical Phase-6 model: human approve --why = semantic decision
X1B status: this legacy attribution rule is not sufficient for X1B Human-decision authorship
```

The current-state model must separately represent:

```text
HUMAN SEMANTIC ACCEPTANCE OF CONTENT
!=
SYSTEM ATTRIBUTION HumanDecision=TRUE
```

This correction does not alter DEC-SO-011 or prior Human semantic acceptance. It only prevents that semantic acceptance from being confused with the security property established by X1B V2.

Any current next-action language must preserve that a consequential effect requiring X1B Human-decision authorship cannot rely on the legacy route while active remediation remains `NO`.

## 7. HANDOFF.md required changes

Extend the YAML/current handoff with explicit fields equivalent to:

```text
x1b_research_closure: "CLOSED"
x1b_active_product_remediated: "NO"
x1b_active_runtime: "LEGACY_PRE_X1B"
x1b_reviewed_remediation: "PR #35 / UNMERGED"
```

The Human-readable handoff must repeat the same distinction.

The current handoff must not identify legacy `approve --why` as the next secure Human-authorship execution route.

The handoff must state that:

```text
legacy approve --why exists
but
legacy approve --why != X1B Human-decision authority
```

It must preserve:

```text
DEC-SO-011 semantic acceptance = historical/current project fact
canonical effect = still not applied
X1B active remediation = not deployed
```

No new effect authority is created.

## 8. scripts/verify_repository.py required changes

Add one deterministic, offline check dedicated to the X1B frame boundary, e.g.:

```text
check_x1b_frame_status()
```

The verifier must not call GitHub or rely on network access.

### 8.1 Required document markers

The verifier must require the three current-state surfaces to contain explicit markers sufficient to reconstruct:

```text
X1B_RESEARCH_CLOSURE = CLOSED
X1B_ACTIVE_PRODUCT_REMEDIATED = NO
X1B_ACTIVE_RUNTIME = LEGACY_PRE_X1B
PR #35 = reviewed remediation / unmerged
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
```

Exact spelling may follow the implementation, but the verifier must bind to unambiguous stable strings rather than loose prose.

### 8.2 Required runtime/status consistency check

The verifier must read the active repository copy of:

```text
phase6/scriptops-v2-hardening.py
```

and classify the checked-out runtime using explicit semantic markers.

For the legacy/pre-X1B route, classification must require a conjunction strong enough to avoid one-token false positives, including at least:

```text
approve parser requires --why
legacy decision record contains "approver": "human"
X1B V2 x1b.approve_scene route is absent
```

For the reviewed V2 route, the future-recognizable classification should be based on a conjunction including at least:

```text
import x1b_human_decision as x1b
x1b.approve_scene(
approve parser requires --decision-pr
```

This plan does not authorize changing runtime to V2, but the verifier design must avoid making `ACTIVE_PRODUCT_REMEDIATED=NO` a timeless hard-coded truth.

### 8.3 Fail-closed consistency table

For this correction candidate the only accepted runtime/status combination is:

```text
runtime classification = LEGACY_PRE_X1B
X1B_ACTIVE_PRODUCT_REMEDIATED = NO
```

The verifier must fail if the current docs claim active remediation while the checked-out runtime classifies as legacy/pre-X1B.

The verifier must also fail if runtime classification is unknown/ambiguous.

The implementation may include the V2 classification branch for forward compatibility, but it must not independently flip status text, perform deployment, or claim that PR #35 is merged.

Any future V2 integration must update the status surfaces in the same reviewed integration candidate so that verifier/runtime/status truth stays coherent.

### 8.4 Preserve historical proof checks without semantic promotion

Existing historical checks for Phase-6 B1-B5, including source markers such as `approve --why` and `"why": why`, may remain as historical proof-contract checks.

They must not be the only current Human-authorship status check and their PASS output must not imply `ACTIVE_PRODUCT_REMEDIATED=YES`.

Add a distinct success line equivalent to:

```text
[PASS] X1B frame status: research closure and active-product remediation are represented separately
```

## 9. PR #35 overlap hazard — mandatory handling

Current PR #35 changes all four correction-plan paths:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
scripts/verify_repository.py
```

Therefore:

```text
STATUS CORRECTION MERGED FIRST
-> PR #35 BECOMES STALE AGAINST MAIN ON OVERLAPPING CURRENT-STATE FILES
```

This is not a reason to broaden this correction into runtime work.

Required rule:

```text
DO NOT LATER MERGE STALE PR #35 AS-IS IF IT WOULD DROP THE FRAME/STATUS BOUNDARY.
```

A future V2 integration must preserve the exact reviewed runtime/security implementation properties while carrying forward the frame/status separation. That future integration is a separate consequential step and requires separate authority/review.

No change to PR #35 is authorized by this plan.

## 10. Deterministic acceptance checks for the correction candidate

Before any implementation candidate can be submitted for independent review, all of the following must hold:

```text
C1 exact base = 2f22843ac570498b506101addeba5453ab777f08
C2 exactly one commit ahead of base
C3 changed paths = exactly the four frozen paths
C4 phase6/scriptops-v2-hardening.py blob unchanged = 4f379960ed5677634dd234af6aa39626782b6133
C5 no runtime/test/workflow file changed
C6 README has explicit research-closure vs active-remediation split
C7 PROJECT_STATE no longer presents approve --why as unqualified current X1B Human-authorship rule
C8 HANDOFF exposes active remediation = NO and legacy runtime class
C9 verifier deterministically classifies current runtime as LEGACY_PRE_X1B
C10 verifier fails on synthetic mismatch: legacy runtime + docs claiming active remediation YES
C11 verifier fails on unknown/ambiguous runtime classification
C12 verifier passes on the exact correction candidate
C13 existing repository verifier checks still pass
C14 existing Phase-6 test suite remains green without modification
```

C10-C11 may be exercised by unit-level temporary-file fixtures or by a small pure helper inside `verify_repository.py`; they must not mutate canonical repository state.

Because the frozen implementation surface excludes tests, if deterministic C10/C11 cannot be demonstrated without adding/modifying test files, STOP and record a plan defect rather than expanding scope silently.

## 11. Independent review requirements

The exact plan must receive one independent read-only review before any implementation authority is requested.

The review must attack at least:

```text
P1 does the plan actually close F001 rather than merely add another stale label?
P2 can docs claim remediated while legacy runtime remains active?
P3 can verifier misclassify runtime from weak markers?
P4 does the plan accidentally redefine X1B=CLOSED as deployment?
P5 does it alter/revoke DEC-SO-011 instead of separating semantics from authorship?
P6 does it create implicit PR #35 merge/deployment authority?
P7 can future stale PR #35 integration erase the correction silently?
P8 does historical Phase-6 PASS get misrepresented as X1B active-remediation PASS?
P9 are all implementation paths truly limited to four?
P10 can the correction be validated without a canonical effect or network dependency?
```

First credible plan counterexample:

```text
PLAN REVIEW FAIL -> DURABLE FINDING -> STOP
```

## 12. Out of scope

This plan does not authorize:

```text
editing ScriptOps now
runtime X1B implementation
modification of PR #35
merge of PR #35
merge of PR #36 or PR #177
movement of ScriptOps main
deployment/release/tag
V1 authority
X1B reopen
new Human screenplay decision
canonical screenplay effect
new GitHub review evidence
new architecture
TPM/PMEM/NFIT/BMC/platform work
```

## 13. Next gate

After independent review:

- if review FAIL: freeze first finding and STOP;
- if review PASS: STOP for separate Human implementation authority.

Preserve:

```text
PLAN REVIEW PASS != IMPLEMENTATION AUTHORITY
STATUS CORRECTION != X1B RUNTIME REMEDIATION
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
AI PROPOSES != HUMAN DECIDES
```
