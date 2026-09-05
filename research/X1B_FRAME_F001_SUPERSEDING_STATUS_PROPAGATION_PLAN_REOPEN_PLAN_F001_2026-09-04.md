# X1B-FRAME F001 — Superseding Bounded Status-Propagation Plan

Status: `SUPERSEDING PLAN ONLY / HUMAN-AUTHORIZED TO PREPARE / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-04`

## 1. Authority and supersession

Original frame finding:

```text
FJ899/8 PR #182
HEAD = 7f2c182700eea2951199467e539e3d04d037452f
TREE = 11096215dcef4722576fcb97e77c31967db7a0a0
PATH = research/X1B_FRAME_F001_DEFAULT_BRANCH_STATUS_AMBIGUITY_2026-09-04.md
BLOB = 1ce333cf2acb1e29657d80e0ddc0749cf50f8c27
FINDING = X1B-FRAME-F001
CLASS = STATUS/DOCUMENTATION AMBIGUITY
```

Human acceptance of that finding is recorded in PR #183.

The first bounded correction plan was:

```text
FJ899/8 PR #184
HEAD = 4924e395c96158bfd148ef9b6841e0f0bebb09e6
TREE = d41e8797e9aa49f9c6dbfe6909fb197c75e54572
PATH = research/X1B_FRAME_F001_BOUNDED_STATUS_PROPAGATION_CORRECTION_PLAN_2026-09-04.md
BLOB = 38d2008a0c9fc5f6edfcdb95bd53790bb239ef94
```

Independent plan review found:

```text
FJ899/8 PR #185
HEAD = 4104ed9f763574692522a8e95d97086c1de21477
TREE = bc87c691cff88b78ab5e0653a96b8779c67c0168
PATH = research/X1B_FRAME_F001_BOUNDED_STATUS_PLAN_REVIEW_F001_2026-09-04.md
BLOB = dbe7d5110cf6754757dc95b819f707c76d62ac05
```

Finding:

```text
X1B-FRAME-F001-PLAN-F001 — OFFLINE CHECKED-OUT RUNTIME CLASSIFICATION
CAN BE USED TO ACCEPT ACTIVE_PRODUCT_REMEDIATED=YES ON A V2 PR CANDIDATE
BEFORE THE ACTIVE DEFAULT BRANCH IS ACTUALLY CHANGED
```

Human response `accept` to that exact plan-review finding is durably recorded in:

```text
FJ899/8 PR #186
HEAD = 79b7b703b83afd9a09168feb7006b7b369062b94
```

This document is the one authorized superseding bounded plan.

It supersedes PR #184 for future implementation authority purposes.
PR #184 remains historical provenance and is not silently rewritten.

## 2. Core correction to the failed plan

The failed plan blurred two different facts:

```text
WHAT CODE IS IN THIS CHECKOUT?
```

and:

```text
WHAT CODE IS THE ACTIVE PRODUCT CURRENTLY RUNNING / EXPOSING AS DEFAULT-BRANCH STATE?
```

The superseding invariant is therefore:

```text
CHECKED_OUT_RUNTIME_CLASS
!=
ACTIVE_PRODUCT_STATE
```

More specifically:

```text
A LOCAL OR CI CHECKOUT MAY CLASSIFY ITS OWN FILES.
A LOCAL OR CI CHECKOUT MUST NOT ESTABLISH ACTIVE_PRODUCT_REMEDIATED=YES.
```

And:

```text
PR HEAD != ACTIVE DEFAULT BRANCH
GREEN VERIFICATION != DEPLOYED ENFORCEMENT
CANDIDATE V2 MARKERS != ACTIVE PRODUCT V2
```

This separation is mandatory and is the direct repair of `X1B-FRAME-F001-PLAN-F001`.

## 3. Frozen current repository state

At superseding-plan preparation time:

```text
FJ899/scriptops refs/heads/main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Reviewed X1B V2 remediation remains:

```text
FJ899/scriptops PR #35
BASE = 2f22843ac570498b506101addeba5453ab777f08
HEAD = 7c40a92165714023743e91c63b5b11b102fadd92
TREE = 31e1f15a2e667811b9617bbb10bf6af2242961b0
STATE = OPEN / DRAFT / UNMERGED
```

Current active runtime on `main`:

```text
phase6/scriptops-v2-hardening.py
BLOB = 4f379960ed5677634dd234af6aa39626782b6133
RUNTIME CLASS = LEGACY_PRE_X1B
```

Reviewed V2 runtime in PR #35:

```text
phase6/scriptops-v2-hardening.py
BLOB = 9da50a3e33c982396049c7618f7154b360194350
CANDIDATE RUNTIME CLASS = X1B_V2
```

These identities must remain distinct throughout this correction.

If `FJ899/scriptops refs/heads/main` changes before implementation begins, this exact plan is no longer executable without a new Human disposition rebinding the baseline.

## 4. Scope of this correction

The correction remains status/frame propagation only.

Exactly four ScriptOps paths may change in a future implementation candidate:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
scripts/verify_repository.py
```

No other ScriptOps path may change.

Forbidden in this correction:

```text
phase6/scriptops-v2-hardening.py
phase6/x1b_human_decision.py
legacy/scriptops-v2-single.py
tests/*
.github/workflows/*
SOURCE_MANIFEST.md
scripts/restore_v2.py
```

The implementation candidate, if later authorized, must be exactly one commit on top of:

```text
2f22843ac570498b506101addeba5453ab777f08
```

No runtime remediation is performed by this plan.

## 5. Required state model

The three current-state documents must expose the following dimensions separately:

```text
X1B_RESEARCH_CLOSURE
X1B_ACTIVE_PRODUCT_REMEDIATED
X1B_ACTIVE_MAIN_LAST_OBSERVED_SHA
X1B_ACTIVE_RUNTIME_LAST_OBSERVED_CLASS
X1B_REVIEWED_REMEDIATION
X1B_ACTIVE_PRODUCT_STATE_AUTHORITY
```

For this exact correction baseline, the values are frozen as:

```text
X1B_RESEARCH_CLOSURE: CLOSED
X1B_ACTIVE_PRODUCT_REMEDIATED: NO
X1B_ACTIVE_MAIN_LAST_OBSERVED_SHA: 2f22843ac570498b506101addeba5453ab777f08
X1B_ACTIVE_RUNTIME_LAST_OBSERVED_CLASS: LEGACY_PRE_X1B
X1B_REVIEWED_REMEDIATION: FJ899/scriptops PR #35 / UNMERGED / HEAD 7c40a92165714023743e91c63b5b11b102fadd92
X1B_ACTIVE_PRODUCT_STATE_AUTHORITY: REMOTE_DEFAULT_BRANCH_READBACK_AFTER_ACTIVATION; NOT OFFLINE CHECKOUT
```

Required invariant:

```text
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
```

The current status may conservatively remain `NO` even after a future runtime integration until a separately authorized post-activation/currentness procedure promotes it.

A conservative false negative is allowed.
A premature false positive is not.

## 6. Critical prohibition — no offline YES

For the implementation governed by this plan:

```text
scripts/verify_repository.py
MUST NOT HAVE ANY SUCCESS PATH THAT ACCEPTS
X1B_ACTIVE_PRODUCT_REMEDIATED = YES
```

This is intentional.

The verifier may classify only the checked-out runtime as a local fact, for example:

```text
CHECKOUT_RUNTIME_CLASS = LEGACY_PRE_X1B
CHECKOUT_RUNTIME_CLASS = X1B_V2_CHECKOUT
CHECKOUT_RUNTIME_CLASS = UNKNOWN
```

But that classification must never be converted into:

```text
ACTIVE_PRODUCT_REMEDIATED = YES
```

The verifier must explicitly report that active-product remediation is not an offline-checkout fact.

Allowed output shape:

```text
[PASS] checkout runtime class: LEGACY_PRE_X1B
[PASS] X1B frame status: research closure is separate from active-product remediation
[INFO] active-product YES cannot be established by the offline repository verifier
```

Forbidden output implication:

```text
V2 CHECKOUT + GREEN VERIFIER -> ACTIVE_PRODUCT_REMEDIATED=YES
```

## 7. Current correction verifier contract

The verifier change must be intentionally baseline-specific rather than pretending to implement future deployment semantics.

For this exact correction candidate it must require:

```text
CHECKOUT_RUNTIME_CLASS = LEGACY_PRE_X1B
X1B_ACTIVE_PRODUCT_REMEDIATED = NO
X1B_ACTIVE_MAIN_LAST_OBSERVED_SHA = 2f22843ac570498b506101addeba5453ab777f08
```

Legacy classification must require a conjunction strong enough to avoid a loose marker match, including at least:

```text
approve parser requires --why
legacy decision path contains "approver": "human"
x1b.approve_scene( is absent
--decision-pr is absent from the approve parser
```

If the checked-out runtime does not classify as the exact expected `LEGACY_PRE_X1B` baseline, this verifier contract must fail closed.

That means a future PR containing the V2 runtime will fail this exact status verifier until a separately authorized integration/update replaces this baseline-specific contract.

That failure is desired and prevents PR #35 or a derivative from silently inheriting a stale active-state claim.

## 8. Required explicit rejection cases

The current verifier must fail if any of the following are observed:

```text
R1 docs claim X1B_ACTIVE_PRODUCT_REMEDIATED: YES
R2 docs omit X1B_ACTIVE_PRODUCT_REMEDIATED
R3 docs omit the observed active-main SHA
R4 docs claim a different active-main SHA than 2f22843...
R5 docs claim active runtime class X1B_V2 while the checked-out baseline runtime is legacy
R6 checked-out runtime classification is UNKNOWN
R7 checked-out runtime class is X1B_V2_CHECKOUT under this legacy-bound correction contract
R8 any current-state document presents legacy approve --why as sufficient X1B Human-decision authority
R9 any current-state document treats PR #35 as active/default-branch code
R10 any current-state document says successful corrective verification is deployment evidence
```

There is no `YES` acceptance branch in this plan.

## 9. README.md required correction

Add a compact, machine-readable current X1B frame block near the top-level status containing all frozen fields from section 5.

The Human-readable text must state:

```text
X1B research/corrective closure is Human-accepted.
The active ScriptOps product is not X1B-remediated.
The active default branch remains 2f22843...
The reviewed V2 remediation is PR #35 and is unmerged.
The legacy approve --why path remains present on active main but is not an X1B Human-decision-authorship mechanism.
```

Historical Phase-6 proof language may remain, but any `approve --why` wording must be explicitly labelled historical/legacy where it could otherwise be read as current Human-authorship security semantics.

The `Co dalej` section must not direct a consequential X1B-authorship effect through legacy `approve --why`.

Instead it must state that such an effect remains blocked until separately authorized V2 integration and active-state binding.

## 10. PROJECT_STATE.md required correction

Because `PROJECT_STATE.md` declares itself the state owner, it must carry the same frozen X1B frame fields.

The existing line:

```text
human approve --why = semantic decision
```

may remain only as historical Phase-6 semantics and must be paired with an explicit statement:

```text
HISTORICAL PHASE-6 SEMANTIC ACCEPTANCE
!=
X1B HumanDecision authorship evidence
```

The current state model must represent separately:

```text
CONTENT SEMANTIC ACCEPTANCE
SYSTEM HumanDecision ATTRIBUTION
ACTIVE PRODUCT REMEDIATION STATE
```

The current state must say:

```text
ACTIVE PRODUCT X1B REMEDIATION = NO
```

and must not imply that PR #35 or its successful verification has changed that active state.

DEC-SO-011 remains valid historical/current project semantics and is not revoked.

## 11. HANDOFF.md required correction

Add stable YAML fields equivalent to:

```text
x1b_research_closure: "CLOSED"
x1b_active_product_remediated: "NO"
x1b_active_main_last_observed_sha: "2f22843ac570498b506101addeba5453ab777f08"
x1b_active_runtime_last_observed_class: "LEGACY_PRE_X1B"
x1b_reviewed_remediation: "FJ899/scriptops PR #35 / UNMERGED / 7c40a92165714023743e91c63b5b11b102fadd92"
x1b_active_product_state_authority: "REMOTE DEFAULT-BRANCH POST-ACTIVATION READBACK; NOT OFFLINE CHECKOUT"
```

The Human-readable handoff must repeat the same distinction.

The handoff must not name legacy `approve --why` as the next secure Human-authorship execution route.

It must preserve:

```text
DEC-SO-011 semantic acceptance = YES
canonical screenplay effect for that historical route = NOT APPLIED
X1B active remediation = NO
```

## 12. scripts/verify_repository.py required correction

Add a deterministic offline check, for example:

```text
check_x1b_frame_status_current_baseline()
```

It must:

1. require the stable frame markers in README, PROJECT_STATE and HANDOFF;
2. require `X1B_ACTIVE_PRODUCT_REMEDIATED = NO` in all authoritative current-state surfaces;
3. require exact observed active-main SHA `2f22843...` in those surfaces;
4. classify the checked-out runtime as `LEGACY_PRE_X1B` using the conjunction in section 7;
5. fail if V2/unknown runtime markers are present under this exact correction contract;
6. fail if any authoritative current-state surface says or implies active remediation `YES`;
7. preserve historical Phase-6 proof checks while preventing those PASS messages from being interpreted as X1B active-remediation PASS;
8. print a distinct bounded success line that does not claim deployment.

The verifier must not:

```text
call GitHub
read a remote ref
use network access
infer deployment
infer active-product YES from checkout state
implement a forward-compatible YES branch
```

The absence of remote access is not a weakness here because the verifier is deliberately not the authority for active-product promotion.

## 13. Future activation state transition — explicitly out of scope

This superseding plan intentionally does not solve the future transition to:

```text
X1B_ACTIVE_PRODUCT_REMEDIATED = YES
```

That transition requires a separate later procedure after actual runtime integration.

Minimum future ordering is frozen conceptually as:

```text
1. integrate a separately reviewed V2 runtime candidate into refs/heads/main
   WITHOUT pre-claiming active remediation YES;
2. perform an external read-only post-activation readback of the actual
   FJ899/scriptops refs/heads/main identity;
3. bind that observed active-main commit/tree to the expected V2 runtime identity;
4. freeze durable activation/currentness evidence;
5. obtain separate Human acceptance of that evidence;
6. only then prepare a separate status-promotion candidate that may propose
   X1B_ACTIVE_PRODUCT_REMEDIATED = YES.
```

Nothing in this plan authorizes any of those six future steps.

The key property is:

```text
NO PRE-MERGE / PR-LOCAL YES
```

## 14. PR #35 overlap hazard

PR #35 currently changes all four paths in this correction surface:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
scripts/verify_repository.py
```

Therefore, if this frame/status correction is later merged first:

```text
PR #35 MUST NOT BE MERGED AS-IS
```

because doing so could overwrite or bypass the newly established frame boundary.

A future V2 integration must start from the then-current corrected main and preserve the reviewed V2 runtime/security properties while carrying the frame separation forward.

That future integration is a new candidate and requires separate review and Human authority.

This plan does not authorize rebasing, editing, cherry-picking, merging, or replacing PR #35.

## 15. Deterministic acceptance checks for a future correction candidate

Before any candidate under this plan can be submitted for independent implementation review, all must hold:

```text
C1 base exactly 2f22843ac570498b506101addeba5453ab777f08
C2 exactly one commit ahead
C3 changed paths exactly README.md, PROJECT_STATE.md, HANDOFF.md, scripts/verify_repository.py
C4 phase6/scriptops-v2-hardening.py unchanged at blob 4f379960ed5677634dd234af6aa39626782b6133
C5 no runtime/test/workflow/source-manifest/restore file changed
C6 all three status surfaces expose the exact research-closure vs active-remediation split
C7 all three status surfaces expose active main last observed = 2f22843...
C8 all three status surfaces say active remediation = NO
C9 legacy approve --why is explicitly non-X1B-remediated in current interpretation
C10 verifier classifies exact checkout as LEGACY_PRE_X1B
C11 verifier rejects docs with ACTIVE_PRODUCT_REMEDIATED=YES
C12 verifier rejects a synthetic V2 checkout under this legacy-bound correction contract
C13 verifier rejects unknown/ambiguous runtime classification
C14 verifier has no success branch for ACTIVE_PRODUCT_REMEDIATED=YES
C15 existing repository checks still pass
C16 existing Phase-6 test suite remains green without modification
C17 remote FJ899/scriptops refs/heads/main remains unchanged throughout candidate preparation/review
```

C11-C14 may be demonstrated with ephemeral copies or direct pure-helper invocation; no canonical repository mutation is permitted for those negative checks.

If those checks cannot be demonstrated within the four-path implementation surface, STOP and record a plan defect rather than expanding scope.

## 16. Independent review target

A future independent read-only review of this exact superseding plan must attack at least:

```text
P1 can any PR-local/candidate-local state still establish active-product YES?
P2 does the offline verifier have any hidden YES or V2->YES success path?
P3 can a V2 checkout plus edited docs pass before default-branch activation?
P4 is the current plan safely conservative if runtime changes but status remains NO?
P5 can PR #35 later overwrite the boundary without a new review?
P6 does the plan preserve X1B closure without falsely claiming deployment?
P7 can active-main currentness be confused with last-observed provenance?
P8 does any required wording accidentally turn this plan into merge/deployment authority?
```

Review semantics:

```text
FIRST CREDIBLE COUNTEREXAMPLE = DURABLE FINDING + STOP
```

No plan repair may be performed during that review.

## 17. Exit and authority boundary

This document is plan-only.

It authorizes no ScriptOps mutation.

Current legal state after this document is frozen:

```text
X1B = CLOSED AT ACCEPTED RESEARCH/CORRECTIVE SCOPE
X1B-FRAME-F001 = HUMAN ACCEPTED / OPEN FOR CORRECTION
X1B-FRAME-F001-PLAN-F001 = HUMAN ACCEPTED
PR #184 = SUPERSEDED PLAN / HISTORICAL NOT PASS
THIS SUPERSEDING PLAN = PREPARED / NOT YET REVIEWED
SCRIPTOPS IMPLEMENTATION AUTHORITY = NO
PR #35 MERGE AUTHORITY = NO
DEPLOYMENT / RELEASE / TAG = NO
V1 AUTHORITY = NO
```

Next legal stage:

```text
ONE INDEPENDENT READ-ONLY REVIEW OF THIS EXACT SUPERSEDING PLAN
```

That review requires separate Human authorization.

Preserve:

```text
AI PROPOSES != HUMAN DECIDES
PLAN REVIEW PASS != IMPLEMENTATION AUTHORITY
CHECKED_OUT_RUNTIME_CLASS != ACTIVE_PRODUCT_STATE
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
```
