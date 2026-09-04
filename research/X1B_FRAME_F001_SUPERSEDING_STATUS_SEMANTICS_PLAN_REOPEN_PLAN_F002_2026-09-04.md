# X1B-FRAME F001 — Superseding Status-Semantics Plan After PLAN-F002

Status: `SUPERSEDING PLAN ONLY / HUMAN-AUTHORIZED TO PREPARE / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-04`

## 1. Authority and supersession

Original frame finding:

```text
FJ899/8 PR #182
FINDING = X1B-FRAME-F001
CLASS = STATUS/DOCUMENTATION AMBIGUITY
```

The first bounded plan was PR #184 and failed independent review in PR #185 on `PLAN-F001`.

The next superseding plan was:

```text
FJ899/8 PR #187
HEAD = 1ceb7a7d56437d794a0f2eb280f98eeb92e40026
TREE = 7b34f50a01bb4b27b2c8eb89915fd27b5f586a3f
PATH = research/X1B_FRAME_F001_SUPERSEDING_STATUS_PROPAGATION_PLAN_REOPEN_PLAN_F001_2026-09-04.md
BLOB = d7744c1cc2a51e9bcb17e5b9a95ded3bebcaef1c
```

Its resumed independent review found:

```text
FJ899/8 PR #190
HEAD = c5500d39cab837133a7068e1e9f8ee4bc9aab42d
TREE = 88284845b0efe22b42f804c9641f76079a40a0af
PATH = research/X1B_FRAME_F001_SUPERSEDING_PLAN_REVIEW_F002_2026-09-04.md
BLOB = 981ea78e3683d7269c59c4fdca1edea4ce026f1a
FINDING = X1B-FRAME-F001-PLAN-F002
```

Finding invariant:

```text
NOT ESTABLISHED != FALSE
```

Human acceptance of that exact finding and authority to prepare exactly one next superseding bounded plan are recorded in:

```text
FJ899/8 PR #191
HEAD = 3494ab48b92c1cd303e5dfc912013238f5ae9024
HUMAN RESPONSE = accept
```

This document is that one authorized superseding plan.

It supersedes PR #187 for future implementation-authority purposes. PR #184 and PR #187 remain historical provenance and are not silently rewritten.

## 2. Core semantic repair

The prior plan used a boolean active-product field:

```text
X1B_ACTIVE_PRODUCT_REMEDIATED = NO | YES
```

That model is retired for this correction.

The problem is that these three states are not equivalent:

```text
A. accepted evidence establishes active runtime is legacy / not remediated
B. active-product currentness/remediation has not yet been established
C. accepted evidence establishes active runtime is X1B-remediated
```

Therefore the status model must preserve three distinct epistemic/authority states:

```text
CONFIRMED_NOT_REMEDIATED
CURRENTNESS_UNESTABLISHED
CONFIRMED_REMEDIATED
```

with the mandatory invariant:

```text
CURRENTNESS_UNESTABLISHED != CONFIRMED_NOT_REMEDIATED
CURRENTNESS_UNESTABLISHED != CONFIRMED_REMEDIATED
```

No boolean alias may collapse these states back into `NO` / `YES`.

## 3. Frozen current repository state

At plan preparation time:

```text
FJ899/8 refs/heads/main
HEAD = 0b516edb210fd4029972e932fec0206d8a6df1cb
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

Current active ScriptOps default branch:

```text
FJ899/scriptops refs/heads/main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Current active Human-approval runtime:

```text
phase6/scriptops-v2-hardening.py
BLOB = 4f379960ed5677634dd234af6aa39626782b6133
RUNTIME CLASS = LEGACY_PRE_X1B
```

Reviewed X1B V2 remediation provenance remains:

```text
FJ899/scriptops PR #35
REVIEWED HEAD = 7c40a92165714023743e91c63b5b11b102fadd92
TREE = 31e1f15a2e667811b9617bbb10bf6af2242961b0
V2 runtime blob = 9da50a3e33c982396049c7618f7154b360194350
```

PR #35 is remediation provenance, not active-product-state authority.

If `FJ899/scriptops refs/heads/main` changes before implementation of this plan begins, implementation authority must be rebound by a fresh Human disposition. Do not silently rebase this plan.

## 4. Correction scope

The correction remains frame/status propagation only.

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

The implementation candidate, if separately authorized later, must be exactly one commit on top of:

```text
2f22843ac570498b506101addeba5453ab777f08
```

No runtime remediation, merge, deployment, status promotion to confirmed-remediated, release, tag, V1 action, or canonical screenplay effect is part of this plan.

## 5. Required status schema

The three authoritative current-state surfaces must carry stable fields equivalent to:

```text
X1B_RESEARCH_CLOSURE
X1B_ACTIVE_PRODUCT_REMEDIATION_ASSERTION
X1B_ACTIVE_PRODUCT_ASSERTION_AUTHORITY
X1B_ACTIVE_PRODUCT_ASSERTION_EVIDENCE
X1B_REVIEWED_REMEDIATION_PROVENANCE
```

The legal values for `X1B_ACTIVE_PRODUCT_REMEDIATION_ASSERTION` are exactly:

```text
CONFIRMED_NOT_REMEDIATED
CURRENTNESS_UNESTABLISHED
CONFIRMED_REMEDIATED
```

No `YES`, `NO`, `TRUE`, `FALSE`, `DEPLOYED`, or equivalent two-state shortcut may be used as the authoritative active-product remediation status.

Required closure invariant:

```text
X1B_RESEARCH_CLOSURE = CLOSED
```

must remain separate from all three active-product assertion states.

## 6. State semantics

### 6.1 CONFIRMED_NOT_REMEDIATED

This means:

```text
accepted external currentness evidence establishes that the active default-branch
runtime is a legacy/pre-X1B runtime and the evidence is authoritative for the
status assertion being published.
```

It is an evidence-backed negative claim.

It must never be inferred merely because:

```text
there is no accepted V2 activation evidence
or
an offline checkout does not prove V2 is active
```

### 6.2 CURRENTNESS_UNESTABLISHED

This means only:

```text
this status surface does not currently possess accepted authority to assert
CONFIRMED_NOT_REMEDIATED or CONFIRMED_REMEDIATED for the active product.
```

It is not a negative product claim and not a positive product claim.

It is the mandatory transition-safe state whenever active default-branch currentness may have changed without a completed accepted rebind.

### 6.3 CONFIRMED_REMEDIATED

This means:

```text
accepted external post-activation evidence establishes that the active
default-branch runtime is the reviewed X1B-remediated runtime state, and a
separate Human acceptance authorizes publishing that confirmed status.
```

An offline checkout, PR head, green CI result, or reviewed candidate can never by itself establish this state.

## 7. Status chosen for the bounded correction candidate

The implementation governed by this plan must publish:

```text
X1B_ACTIVE_PRODUCT_REMEDIATION_ASSERTION: CURRENTNESS_UNESTABLISHED
```

not `CONFIRMED_NOT_REMEDIATED`.

Reason: the correction candidate itself is a default-branch-changing candidate if later merged. A current-main SHA or currentness observation made before that merge cannot be embedded as if it were post-activation authority for the resulting default-branch state.

Therefore this correction deliberately makes no ontic claim that the post-correction active product is either remediated or not remediated.

The Human-readable meaning must be equivalent to:

```text
X1B research/corrective closure is Human-accepted.
Active-product X1B remediation currentness is not established by this checkout.
Do not infer remediated or not-remediated from this status alone.
The legacy approve --why path is not sufficient X1B Human-decision authority.
PR/candidate review success is not active-product evidence.
```

This state is truthful both:

```text
before merge, when the document is only candidate-local
and
after merge, before a separate external currentness rebind is accepted.
```

## 8. No fixed active-main SHA as a durable current-state claim

The prior plan embedded:

```text
X1B_ACTIVE_MAIN_LAST_OBSERVED_SHA = 2f22843...
```

as part of current authoritative status.

That is not safe for a candidate that may itself change `refs/heads/main`.

This superseding plan therefore forbids treating a pre-merge default-branch SHA as a timeless active-state fact.

The exact ScriptOps base SHA remains valid as implementation provenance:

```text
IMPLEMENTATION_BASE = 2f22843ac570498b506101addeba5453ab777f08
```

but must be labelled provenance, not `CURRENT ACTIVE MAIN` after integration.

If a Human-readable document mentions `2f22843...`, it must say that it is the frozen pre-correction baseline / last observed pre-correction active main, not an eternal current pointer.

## 9. Reviewed remediation provenance semantics

The three current-state surfaces may name:

```text
FJ899/scriptops PR #35
HEAD = 7c40a92165714023743e91c63b5b11b102fadd92
```

only as reviewed remediation provenance.

They must not freeze a dynamic PR-state statement such as `OPEN / UNMERGED` as a permanent current-state truth.

Allowed wording is equivalent to:

```text
X1B_REVIEWED_REMEDIATION_PROVENANCE:
PR #35 / reviewed candidate HEAD 7c40a921...
This provenance does not establish what is active on refs/heads/main.
```

If current PR state is mentioned, it must be explicitly qualified as `last observed at plan/correction time`, not status authority.

## 10. README.md required correction

Near the top-level status, add a compact machine-readable X1B frame block equivalent to:

```text
X1B_RESEARCH_CLOSURE: CLOSED
X1B_ACTIVE_PRODUCT_REMEDIATION_ASSERTION: CURRENTNESS_UNESTABLISHED
X1B_ACTIVE_PRODUCT_ASSERTION_AUTHORITY: EXTERNAL_CURRENTNESS_REBIND_REQUIRED
X1B_ACTIVE_PRODUCT_ASSERTION_EVIDENCE: NONE_ACCEPTED_FOR_THIS_STATUS_PUBLICATION
X1B_REVIEWED_REMEDIATION_PROVENANCE: PR #35 / REVIEWED HEAD 7c40a92165714023743e91c63b5b11b102fadd92
```

The README must explain:

1. `CURRENTNESS_UNESTABLISHED` is neither `NO` nor `YES`.
2. X1B research closure does not establish active-product remediation.
3. the legacy `approve --why` mechanism is not sufficient X1B Human-decision-authorship authority;
4. PR #35 and its successful review/verification are candidate provenance, not active-state proof;
5. no consequential X1B-authorship effect may be routed through the legacy path merely because the historical Phase-6 semantic-decision text exists.

Historical Phase-6 wording may remain only if clearly labelled historical/legacy where it could otherwise be interpreted as current X1B authority.

## 11. PROJECT_STATE.md required correction

Because `PROJECT_STATE.md` declares itself the state owner, it must carry the same status schema and selected state:

```text
X1B_ACTIVE_PRODUCT_REMEDIATION_ASSERTION = CURRENTNESS_UNESTABLISHED
```

The historical line:

```text
human approve --why = semantic decision
```

may remain only as historical Phase-6 semantics and must be paired with:

```text
HISTORICAL PHASE-6 CONTENT SEMANTIC ACCEPTANCE
!=
X1B HumanDecision authorship evidence
```

The current-state model must separate:

```text
CONTENT SEMANTIC ACCEPTANCE
SYSTEM HumanDecision ATTRIBUTION
ACTIVE-PRODUCT REMEDIATION ASSERTION
ACTIVE-PRODUCT ASSERTION AUTHORITY
```

It must explicitly say that the active-product remediation assertion is currently unestablished, not false.

DEC-SO-011 remains valid project-history/semantic provenance and is not revoked.

## 12. HANDOFF.md required correction

Add stable YAML fields equivalent to:

```text
x1b_research_closure: "CLOSED"
x1b_active_product_remediation_assertion: "CURRENTNESS_UNESTABLISHED"
x1b_active_product_assertion_authority: "EXTERNAL_CURRENTNESS_REBIND_REQUIRED"
x1b_active_product_assertion_evidence: "NONE_ACCEPTED_FOR_THIS_STATUS_PUBLICATION"
x1b_reviewed_remediation_provenance: "PR #35 / REVIEWED HEAD 7c40a92165714023743e91c63b5b11b102fadd92"
```

The Human-readable handoff must repeat:

```text
CURRENTNESS_UNESTABLISHED != NOT REMEDIATED
CURRENTNESS_UNESTABLISHED != REMEDIATED
```

The next-action section must not direct a consequential Human-authorship effect through legacy `approve --why`.

It must state that active-product status requires a separate external currentness rebind and separate Human authority before either confirmed state may be published.

## 13. scripts/verify_repository.py required correction

Add a deterministic offline frame/status check, e.g.:

```text
check_x1b_frame_status_semantics()
```

The verifier may inspect only repository-local files and must not use network access.

### 13.1 Required document semantics

The verifier must require all three authoritative current-state surfaces to contain unambiguous markers for:

```text
X1B_RESEARCH_CLOSURE = CLOSED
X1B_ACTIVE_PRODUCT_REMEDIATION_ASSERTION = CURRENTNESS_UNESTABLISHED
CURRENTNESS_UNESTABLISHED != CONFIRMED_NOT_REMEDIATED
CURRENTNESS_UNESTABLISHED != CONFIRMED_REMEDIATED
PR #35 = remediation provenance, not active-state authority
legacy approve --why != X1B Human-decision authority
```

### 13.2 Retire boolean collapse

The verifier must reject authoritative status surfaces containing the retired field or equivalent active-state shortcut:

```text
X1B_ACTIVE_PRODUCT_REMEDIATED: YES
X1B_ACTIVE_PRODUCT_REMEDIATED: NO
ACTIVE PRODUCT X1B REMEDIATION = YES
ACTIVE PRODUCT X1B REMEDIATION = NO
```

Equivalent exact forbidden markers may be chosen by implementation, but the semantic rule must be deterministic.

Historical quotations are permitted only in clearly delimited historical/provenance sections that the verifier does not parse as current authoritative status.

### 13.3 Local runtime classification is separate

The verifier may classify the checked-out runtime as:

```text
LEGACY_PRE_X1B
X1B_V2_CHECKOUT
UNKNOWN
```

using conjunctions strong enough to avoid loose marker matches.

Legacy classification must include at least:

```text
approve parser requires --why
legacy decision record contains "approver": "human"
x1b.approve_scene( absent
--decision-pr absent from approve parser
```

V2 classification must include at least:

```text
import x1b_human_decision as x1b
x1b.approve_scene(
approve parser requires --decision-pr
```

Unknown/ambiguous classification must fail.

### 13.4 Allowed relation between checkout class and status assertion

Under this exact correction contract:

```text
LEGACY_PRE_X1B + CURRENTNESS_UNESTABLISHED = PASS
X1B_V2_CHECKOUT + CURRENTNESS_UNESTABLISHED = PASS
UNKNOWN + CURRENTNESS_UNESTABLISHED = FAIL
```

The V2-checkout PASS is intentional and must not be described as active-product remediation PASS. It says only that a candidate/local checkout can contain V2 while active-product currentness remains unestablished.

The verifier must have no path that converts either recognized checkout class into a confirmed active-product state.

### 13.5 Confirmed states are out of the current verifier contract

For this bounded correction, the offline verifier must reject current-state assertions:

```text
CONFIRMED_NOT_REMEDIATED
CONFIRMED_REMEDIATED
```

because publishing either confirmed state requires a separate external-evidence/currentness procedure that is not part of this implementation.

A later separately authorized status-promotion plan may replace this restriction.

### 13.6 Required output meaning

Allowed success output is equivalent to:

```text
[PASS] checkout runtime class: LEGACY_PRE_X1B
[PASS] X1B frame status: active-product remediation currentness is unestablished
[INFO] offline checkout classification does not establish active-product state
```

No PASS line may imply deployment, active-product remediation, or HumanDecision authority from the legacy path.

## 14. Future runtime-integration safety rule

The frame correction must survive a future V2 integration candidate without becoming false.

Therefore any future candidate that changes the runtime may carry forward:

```text
X1B_ACTIVE_PRODUCT_REMEDIATION_ASSERTION = CURRENTNESS_UNESTABLISHED
```

and the offline verifier may pass a recognized V2 checkout in that state.

This does not grant merge authority.

It means only:

```text
candidate contains V2
!=
active product confirmed remediated
```

If such a candidate is later merged under separate authority, the same `CURRENTNESS_UNESTABLISHED` status remains truthful until external rebind evidence is completed.

This directly repairs PLAN-F002.

## 15. Future confirmed-state publication — separately gated

Neither confirmed state is authorized by this plan.

A future publication of:

```text
CONFIRMED_NOT_REMEDIATED
```

or:

```text
CONFIRMED_REMEDIATED
```

must require a separately preregistered status-promotion procedure with at least:

```text
1. external read-only resolution of actual FJ899/scriptops refs/heads/main;
2. binding of that active commit to the relevant runtime blob/semantic class;
3. durable currentness evidence;
4. separate Human acceptance of that evidence;
5. a status-promotion candidate that changes no runtime path;
6. verification that the promotion candidate preserves the runtime identity proven by the accepted evidence.
```

The exact future promotion design is out of scope here.

Important semantic rule:

```text
NO ACCEPTED CURRENTNESS EVIDENCE
=> CURRENTNESS_UNESTABLISHED
NOT
=> CONFIRMED_NOT_REMEDIATED
```

## 16. PR #35 overlap hazard

PR #35 changes all four status-correction paths:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
scripts/verify_repository.py
```

Therefore, if this status-semantics correction is later merged first:

```text
PR #35 MUST NOT BE MERGED AS-IS IF IT WOULD DROP THIS FRAME BOUNDARY
```

A future V2 integration must preserve the reviewed V2 runtime/security properties while carrying forward `CURRENTNESS_UNESTABLISHED` until a separately accepted external rebind/promotion occurs.

This plan does not authorize editing, rebasing, cherry-picking, replacing, or merging PR #35.

## 17. Deterministic acceptance checks for a future correction candidate

Before any candidate under this plan can be submitted for independent implementation review, all must hold:

```text
C1  base exactly 2f22843ac570498b506101addeba5453ab777f08
C2  exactly one commit ahead of base
C3  changed paths exactly README.md, PROJECT_STATE.md, HANDOFF.md, scripts/verify_repository.py
C4  phase6/scriptops-v2-hardening.py unchanged at blob 4f379960ed5677634dd234af6aa39626782b6133
C5  no runtime/test/workflow/source-manifest/restore file changed
C6  all three current-state surfaces say X1B_RESEARCH_CLOSURE = CLOSED
C7  all three surfaces use CURRENTNESS_UNESTABLISHED as the active-product remediation assertion
C8  none of the three surfaces uses YES/NO as authoritative active-product remediation state
C9  all three surfaces distinguish CURRENTNESS_UNESTABLISHED from both confirmed states
C10 PR #35 appears only as remediation provenance, not active-product authority
C11 legacy approve --why is explicitly non-X1B-authoritative in current interpretation
C12 verifier classifies exact correction checkout as LEGACY_PRE_X1B
C13 verifier accepts a synthetic recognized X1B_V2_CHECKOUT only when assertion remains CURRENTNESS_UNESTABLISHED
C14 verifier rejects UNKNOWN/ambiguous runtime class
C15 verifier rejects any current authoritative YES/NO shortcut
C16 verifier rejects CONFIRMED_NOT_REMEDIATED under this correction contract
C17 verifier rejects CONFIRMED_REMEDIATED under this correction contract
C18 verifier has no network access and no remote-ref inference
C19 existing repository verification still passes after the bounded changes
C20 existing Phase-6 test suite remains green without modification
C21 remote FJ899/scriptops refs/heads/main remains 2f22843... throughout candidate preparation/review
```

C13-C17 may be demonstrated with ephemeral copies or pure helper invocation. No canonical repository mutation is permitted for negative/synthetic checks.

If these checks cannot be demonstrated within the frozen four-path surface, STOP and record a plan defect rather than expanding scope silently.

## 18. Independent review requirements

A future independent read-only review of this exact plan must attack at least:

```text
P1 can CURRENTNESS_UNESTABLISHED still be read as an ontic NO or YES?
P2 can any PR-local checkout still establish a confirmed active-product state?
P3 can a V2 checkout pass only as unestablished, without implied deployment?
P4 does the status remain truthful across the instant of a future runtime merge?
P5 does removing fixed current-main SHA avoid self-invalidating status after a docs-only merge?
P6 can reviewed PR #35 provenance be mistaken for active state?
P7 can historical approve --why semantics leak back into current X1B authority?
P8 can any current verifier path publish a confirmed state without external accepted evidence?
P9 can a future stale PR #35 overwrite the frame semantics?
P10 does any wording accidentally create merge/deployment/V1 authority?
```

Review rule:

```text
FIRST CREDIBLE COUNTEREXAMPLE = DURABLE FINDING + STOP
```

No plan repair may occur inside that review.

## 19. Exit and authority boundary

Current legal state after this plan is frozen:

```text
X1B = CLOSED AT ACCEPTED RESEARCH/CORRECTIVE SCOPE
X1B-FRAME-F001 = HUMAN ACCEPTED / OPEN FOR CORRECTION
X1B-FRAME-F001-PLAN-F001 = HUMAN ACCEPTED
X1B-FRAME-F001-PLAN-F002 = HUMAN ACCEPTED
PR #184 = SUPERSEDED / HISTORICAL NOT PASS
PR #187 = SUPERSEDED / HISTORICAL NOT PASS
THIS PLAN = PREPARED / NOT YET REVIEWED
SCRIPTOPS IMPLEMENTATION AUTHORITY = NO
PR #35 MERGE AUTHORITY = NO
DEPLOYMENT / RELEASE / TAG = NO
V1 AUTHORITY = NO
```

Next legal stage:

```text
ONE INDEPENDENT READ-ONLY REVIEW OF THIS EXACT SUPERSEDING PLAN
```

That review requires a separate Human authorization.

Preserve:

```text
NOT ESTABLISHED != FALSE
NOT ESTABLISHED != TRUE
CHECKED_OUT_RUNTIME_CLASS != ACTIVE_PRODUCT_STATE
PR HEAD != ACTIVE DEFAULT BRANCH
PLAN REVIEW PASS != IMPLEMENTATION AUTHORITY
AI PROPOSES != HUMAN DECIDES
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
```
