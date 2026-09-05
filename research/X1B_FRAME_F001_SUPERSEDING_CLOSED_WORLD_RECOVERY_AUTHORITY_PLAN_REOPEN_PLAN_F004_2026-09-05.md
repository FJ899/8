# X1B-FRAME F001 — Superseding Closed-World Recovery-Authority Plan After PLAN-F004

Status: `SUPERSEDING PLAN ONLY / HUMAN-AUTHORIZED TO PREPARE / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-05`

## 1. Authority and supersession

Original frame finding:

```text
FJ899/8 PR #182
FINDING = X1B-FRAME-F001
CLASS = STATUS / DOCUMENTATION AMBIGUITY
```

Prior plan/review chain:

```text
PR #184 = first bounded plan / NOT PASS
PR #185 = PLAN-F001
PR #187 = superseding plan after PLAN-F001 / NOT PASS
PR #190 = PLAN-F002
PR #192 = superseding status-semantics plan after PLAN-F002 / NOT PASS
PR #193 = PLAN-F003
PR #195 = superseding recovery-authority plan after PLAN-F003 / NOT PASS
PR #196 = PLAN-F004
```

Exact accepted PLAN-F004 finding:

```text
FJ899/8 PR #196
BASE = 0b516edb210fd4029972e932fec0206d8a6df1cb
HEAD = b3fe7e4afaed3fac2720e18322d238a43eb92166
TREE = 4977544a3b44194b67ec19f662216acd9aeaff10
PATH = research/X1B_FRAME_F001_RECOVERY_AUTHORITY_PLAN_REVIEW_F004_2026-09-05.md
BLOB = f93b65efe6f62939c6f5a7f85df88ca6828562d8
FINDING = X1B-FRAME-F001-PLAN-F004
```

Human acceptance and authority to prepare exactly one next superseding bounded plan are recorded in:

```text
FJ899/8 PR #197
HEAD = 32a3dc85ab8e8b21358d091f28a686ea3cad4f31
HUMAN RESPONSE = accept
```

This document is that one authorized superseding plan.

It supersedes PR #195 for future implementation-authority purposes. Older plans remain provenance and are not silently rewritten.

No ScriptOps mutation is authorized by this document.

## 2. PLAN-F004 repair strategy

PLAN-F004 showed that a hand-curated list of stale current-looking files can remain incomplete. `SOURCES.md` was outside the seven-path surface while still reasserting `SOURCE_MANIFEST.md` as canonical, `Decision_Summary_Current_State.md` as current, and `ACCESS CHECK REQUIRED` as an active gap.

This plan therefore replaces ad-hoc discovery with a **closed-world recovery-authority model**.

The core rule is:

```text
CURRENT X1B AUTHORITY IS GRANTED BY AN EXPLICIT CLOSED-WORLD REGISTRY.
NO DOCUMENT MAY ACQUIRE CURRENT AUTHORITY FROM ITS FILE NAME, TITLE, STATUS WORD,
"CURRENT", "CANONICAL", "ACTIVE", "LAW", "LOCK", "NEXT STEP", OR SIMILAR PROSE.
```

The current bootstrap authority remains exactly:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
```

All other documentation belongs to a non-current authority class unless a later separately Human-authorized status promotion changes the registry.

The future correction candidate governed by this plan must also explicitly fence every root-level or `sources/*.md` document that currently carries authority-capable wording not already self-fenced as historical/non-authoritative.

## 3. Preserved PLAN-F002 active-product semantics

The three-state model remains mandatory:

```text
CONFIRMED_NOT_REMEDIATED
CURRENTNESS_UNESTABLISHED
CONFIRMED_REMEDIATED
```

with:

```text
CURRENTNESS_UNESTABLISHED != CONFIRMED_NOT_REMEDIATED
CURRENTNESS_UNESTABLISHED != CONFIRMED_REMEDIATED
CURRENTNESS_UNESTABLISHED != FALSE
CURRENTNESS_UNESTABLISHED != TRUE
```

For the bounded documentation/status correction governed by this plan, the only allowed publication is:

```text
X1B_ACTIVE_PRODUCT_REMEDIATION_ASSERTION = CURRENTNESS_UNESTABLISHED
```

No offline checkout, PR head, reviewed candidate, green verifier, historical approval record or source label can promote that value.

## 4. Frozen repository anchors

Evidence repository planning anchor:

```text
FJ899/8 refs/heads/main
HEAD = 0b516edb210fd4029972e932fec0206d8a6df1cb
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

ScriptOps active default branch independently re-read during preparation:

```text
FJ899/scriptops refs/heads/main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Reviewed X1B V2 remediation provenance remains:

```text
FJ899/scriptops PR #35
HEAD = 7c40a92165714023743e91c63b5b11b102fadd92
TREE = 31e1f15a2e667811b9617bbb10bf6af2242961b0
STATE = OPEN / DRAFT / UNMERGED AT PLAN PREPARATION TIME
```

If `FJ899/scriptops refs/heads/main` changes before implementation begins, this exact plan is no longer executable without a fresh Human disposition rebinding the baseline.

## 5. Read-only authority-surface census performed during plan preparation

The accepted PR #197 explicitly allowed read-only inventory during plan preparation.

The frozen ScriptOps baseline contains the following root-level Markdown files relevant to recovery/status interpretation:

```text
CODEX_START.md
DECISION_LOG.md
HANDOFF.md
IDEA_ARCHIVE.md
PROJECT_STATE.md
README.md
RECONSTRUCTION_REPORT.md
SOURCES.md
SOURCE_AUDIT_SUMMARY.md
SOURCE_MANIFEST.md
```

and the following direct `sources/*.md` files:

```text
sources/Decision_Summary_Current_State.md
sources/RC1_SCOPE_LOCK.md
sources/ScriptOps_Main_Theme_Summary.md
```

plus:

```text
sources/prototype/RESTORE.md
```

which is already explicitly about reconstruction of a historical prototype rather than current X1B state.

The census divides these documents into three classes.

### 5.1 CURRENT_BOOTSTRAP_AUTHORITY — exactly three

```text
README.md
PROJECT_STATE.md
HANDOFF.md
```

### 5.2 AUTHORITY-CAPABLE SUPPORTING DOCUMENTS — explicit fence required

The following eight baseline documents contain current/canonical/active/law/lock/decision/next-step wording capable of competing with the current trio unless explicitly fenced:

```text
DECISION_LOG.md
RECONSTRUCTION_REPORT.md
SOURCES.md
SOURCE_AUDIT_SUMMARY.md
SOURCE_MANIFEST.md
sources/Decision_Summary_Current_State.md
sources/RC1_SCOPE_LOCK.md
sources/ScriptOps_Main_Theme_Summary.md
```

These eight documents must be changed only to add/reconcile bounded authority classification and stale-current wording. Their substantive historical decisions, product vision, scope provenance and evidence must not be rewritten into new policy.

### 5.3 PRE-FENCED / NON-AUTHORITY SUPPORTING DOCUMENTS — unchanged

The following baseline documents already carry sufficiently strong context for this bounded frame correction and are not included in the implementation surface:

```text
CODEX_START.md
IDEA_ARCHIVE.md
sources/prototype/RESTORE.md
```

The verifier must retain baseline checks proving their relevant non-authority/history markers remain present.

Subdirectories are path-classed as provenance rather than current bootstrap authority:

```text
analysis/*
continuity/*
evidence/*
acceptance/*
legacy/*
phase6/*
tests/*
```

No document in those path classes may override the closed-world current-authority registry.

## 6. Frozen future implementation surface

A future implementation candidate under this plan may change exactly these twelve ScriptOps paths:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
DECISION_LOG.md
SOURCE_MANIFEST.md
SOURCES.md
SOURCE_AUDIT_SUMMARY.md
RECONSTRUCTION_REPORT.md
sources/Decision_Summary_Current_State.md
sources/RC1_SCOPE_LOCK.md
sources/ScriptOps_Main_Theme_Summary.md
scripts/verify_repository.py
```

No other ScriptOps path may change.

The future candidate, if separately authorized, must be exactly one commit on top of:

```text
2f22843ac570498b506101addeba5453ab777f08
```

No runtime file, test file, workflow, restore mechanism, evidence file, acceptance file or implementation module may change.

## 7. Closed-world authority registry

The future candidate must define one frozen registry in `scripts/verify_repository.py` and publish equivalent human-readable semantics in the current trio.

The registry must classify the complete baseline root/direct-sources Markdown census from section 5.

Minimum classes:

```text
CURRENT_BOOTSTRAP_AUTHORITY
DECISION_PROVENANCE_ONLY
HISTORICAL_RECONSTRUCTION_PROVENANCE_ONLY
HISTORICAL_PRODUCT_GOVERNANCE_PROVENANCE_ONLY
PRE_FENCED_NONAUTHORITY_PROVENANCE
PATH_CLASS_PROVENANCE_ONLY
```

Exactly these three files may belong to `CURRENT_BOOTSTRAP_AUTHORITY`:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
```

No other file may become current X1B state, HumanDecision, current-next-action, active-product, merge/deployment/release or V1 authority by self-description.

Mandatory invariant:

```text
AUTHORITY IS REGISTRY-GRANTED, NOT SELF-ASSERTED.
```

## 8. Current bootstrap algorithm

The zero-history current recovery algorithm remains:

```text
1. READ README.md
2. READ PROJECT_STATE.md
3. READ HANDOFF.md
4. VERIFY INTERNAL AGREEMENT
5. CURRENT-STATE RECOVERY COMPLETE
6. STOP BEFORE CONSEQUENTIAL WORK
7. LOAD ONLY TASK-RELEVANT SUPPORTING PROVENANCE
```

Supporting provenance may be read after step 5, but its authority class is fixed by the registry.

Therefore:

```text
READ LATER != AUTHORITATIVE LATER
SELF-LABEL != AUTHORITY
ACTIVE DECISION != ACTIVE PRODUCT STATE
CORE PRODUCT LAW != X1B HumanDecision ADMISSION AUTHORITY
SCOPE LOCK != CURRENT X1B REMEDIATION STATUS
```

If the current trio disagrees, fail closed and require Human rebind.

## 9. Current X1B status schema

All three current-authority files must expose equivalent stable fields:

```text
X1B_RESEARCH_CLOSURE
X1B_ACTIVE_PRODUCT_REMEDIATION_ASSERTION
X1B_ACTIVE_PRODUCT_ASSERTION_AUTHORITY
X1B_ACTIVE_PRODUCT_ASSERTION_EVIDENCE
X1B_REVIEWED_REMEDIATION_PROVENANCE
X1B_CURRENT_AUTHORITY_BOOTSTRAP
X1B_AUTHORITY_MODEL
```

For this correction candidate:

```text
X1B_RESEARCH_CLOSURE: CLOSED
X1B_ACTIVE_PRODUCT_REMEDIATION_ASSERTION: CURRENTNESS_UNESTABLISHED
X1B_ACTIVE_PRODUCT_ASSERTION_AUTHORITY: EXTERNAL_CURRENTNESS_REBIND_REQUIRED
X1B_ACTIVE_PRODUCT_ASSERTION_EVIDENCE: NONE_ACCEPTED_FOR_THIS STATUS PUBLICATION
X1B_REVIEWED_REMEDIATION_PROVENANCE: PR #35 / REVIEWED HEAD 7c40a92165714023743e91c63b5b11b102fadd92
X1B_CURRENT_AUTHORITY_BOOTSTRAP: README.md -> PROJECT_STATE.md -> HANDOFF.md
X1B_AUTHORITY_MODEL: CLOSED_WORLD_REGISTRY
```

No fixed old `main` SHA may be presented as a timeless current-state assertion.

## 10. README.md correction

README remains the recovery router.

It must:

```text
publish the schema in section 9
identify exactly README -> PROJECT_STATE -> HANDOFF as current bootstrap
state that current-state recovery ends after the trio agrees
separate supporting provenance from current authority
state that authority is closed-world registry-granted
state CURRENTNESS_UNESTABLISHED != YES/NO
state legacy approve --why != sufficient X1B HumanDecision authority
state PR #35 reviewed candidate != active-product proof
state green verification != deployment
state X1B CLOSED != ACTIVE PRODUCT REMEDIATED
```

It must not restore a long static mandatory startup list.

## 11. PROJECT_STATE.md correction

PROJECT_STATE remains current status owner but not sole authority outside the trio contract.

It must distinguish:

```text
CONTENT SEMANTIC ACCEPTANCE
DECISION PROVENANCE
X1B HumanDecision AUTHORSHIP EVIDENCE
ACTIVE-PRODUCT REMEDIATION ASSERTION
CURRENT NEXT-ACTION AUTHORITY
```

Historical `human decision with why` / `approve --why` semantics may remain only with a current fence:

```text
HISTORICAL CONTENT-SEMANTIC / PHASE-6 GOVERNANCE
!=
X1B HumanDecision AUTHORSHIP EVIDENCE
```

## 12. HANDOFF.md correction

HANDOFF remains the bounded resume pointer.

It must include the current schema and exact bootstrap trio.

It must not direct a consequential Human-authorship effect through the legacy approval path.

It may refer to supporting provenance only after explicitly stating the registry class and non-override rule.

## 13. DECISION_LOG.md classification

`DECISION_LOG.md` contains active decisions and currently states that `PROJECT_STATE.md` is canonical operational state. It also preserves historical Human approval / `approve --why` decisions.

The file must gain a stable top-level fence equivalent to:

```text
document_class: DECISION_PROVENANCE_ONLY
current_x1b_state_authority: NO
x1b_humandecision_admission_authority: NO
current_active_product_state_authority: NO
current_next_action_authority: NO
```

Existing decision statuses such as `ACTIVE` remain decision-lifecycle facts only.

Mandatory semantic fence:

```text
ACTIVE DECISION RECORD != CURRENT ACTIVE-PRODUCT STATE
GENERIC / HISTORICAL HUMAN APPROVAL != X1B HumanDecision AUTHORSHIP EVIDENCE
```

No historical decision content is deleted or converted into a new decision.

## 14. SOURCE_MANIFEST.md classification

It must become an explicit historical/reconstruction provenance index:

```text
document_class: HISTORICAL_RECONSTRUCTION_PROVENANCE_ONLY
current_x1b_state_authority: NO
x1b_humandecision_admission_authority: NO
current_next_action_authority: NO
```

Its old `canonical operational sources` wording must be removed or rewritten as reconstruction provenance.

Any reference to files whose names contain `Current_State` must explicitly say the file name is historical provenance and does not confer current authority.

## 15. SOURCES.md classification — direct PLAN-F004 repair

`SOURCES.md` must be added to the correction surface and explicitly fenced:

```text
document_class: HISTORICAL_RECONSTRUCTION_PROVENANCE_ONLY
current_x1b_state_authority: NO
x1b_humandecision_admission_authority: NO
current_next_action_authority: NO
```

The following current-looking claims must be rewritten or historically qualified:

```text
SOURCE_MANIFEST.md = canonical source index
Decision_Summary_Current_State = current product-decision summary
ACCESS CHECK REQUIRED = current gap / current project-state requirement
```

It must route current state to:

```text
README.md -> PROJECT_STATE.md -> HANDOFF.md
```

## 16. SOURCE_AUDIT_SUMMARY.md classification

This document may retain audit conclusions and historical identification findings, but it must gain a top-level fence:

```text
document_class: HISTORICAL_RECONSTRUCTION_PROVENANCE_ONLY
current_x1b_state_authority: NO
x1b_humandecision_admission_authority: NO
current_next_action_authority: NO
```

Phrases equivalent to `canonical conclusions` or `strongest user decisions` must be explicitly audit/provenance descriptions, not current authority grants.

## 17. RECONSTRUCTION_REPORT.md classification

It must remain historical reconstruction provenance with explicit non-current authority fields.

Its historical `AI candidate -> human decision -> reason -> commit` model must carry a current X1B fence.

Its historical `ACCESS CHECK` next step must be labelled as historical-at-reconstruction-time, not current.

## 18. sources/Decision_Summary_Current_State.md classification

The path name remains for provenance compatibility, but content must explicitly state:

```text
document_class: HISTORICAL_PRODUCT_GOVERNANCE_PROVENANCE_ONLY
current_x1b_state_authority: NO
x1b_humandecision_admission_authority: NO
current_next_action_authority: NO
```

The title must no longer self-present as current authority.

Generic Human approval governance may remain only with:

```text
GENERIC HUMAN APPROVAL GOVERNANCE != X1B HumanDecision AUTHORSHIP EVIDENCE
```

## 19. sources/RC1_SCOPE_LOCK.md classification

The RC1 scope document may continue to preserve the historical product scope lock, but it must explicitly state:

```text
document_class: HISTORICAL_PRODUCT_GOVERNANCE_PROVENANCE_ONLY
current_x1b_state_authority: NO
x1b_humandecision_admission_authority: NO
current_active_product_state_authority: NO
```

`Scope Lock` means historical/product-scope provenance. It does not establish current X1B remediation, deployment, HumanDecision admission or V1 authority.

The historical loop containing `human decision` must not be interpretable as sufficient X1B authorship evidence.

## 20. sources/ScriptOps_Main_Theme_Summary.md classification

The historical product vision may remain, including its generic `human approves` product-law language, but it must gain:

```text
document_class: HISTORICAL_PRODUCT_GOVERNANCE_PROVENANCE_ONLY
current_x1b_state_authority: NO
x1b_humandecision_admission_authority: NO
current_next_action_authority: NO
```

The phrase `Core product law` must be explicitly scoped as historical/product-vision provenance and not current X1B HumanDecision admission semantics.

Mandatory fence:

```text
PRODUCT VISION LAW != X1B HumanDecision AUTHORSHIP EVIDENCE
```

## 21. Pre-fenced unchanged documents

The verifier must require baseline non-authority/history markers in:

```text
CODEX_START.md
IDEA_ARCHIVE.md
sources/prototype/RESTORE.md
```

Minimum expectations:

```text
CODEX_START = HISTORICAL / SUPERSEDED / NOT CURRENT ROUTE
IDEA_ARCHIVE = preserved ideas are not implementation authority
prototype/RESTORE = historical prototype reconstruction context
```

These files remain unchanged.

If a required marker is missing on the baseline/candidate, fail closed; do not silently expand the implementation surface.

## 22. Path-classed provenance directories

The verifier must classify the following directories as non-current authority by path:

```text
analysis/
continuity/
evidence/
acceptance/
```

Files under these paths may contain historical claims, accepted evidence or dated next-step language within their own evidence meaning.

They cannot establish current X1B status, active-product remediation, current HumanDecision admission, current next action, merge/deployment/release or V1 authority unless a later current-authority trio explicitly and Human-validly incorporates an accepted state promotion.

Runtime/code directories remain implementation material, not status authority:

```text
legacy/
phase6/
tests/
.github/
scripts/  (except verifier logic as verification mechanism)
```

## 23. scripts/verify_repository.py — closed-world authority proof

Add a deterministic offline check, for example:

```text
check_x1b_closed_world_recovery_authority()
```

The verifier must not use network access and must not infer remote/default-branch state from the checkout.

### 23.1 Exact census

The verifier must enumerate actual root `*.md` and direct `sources/*.md` files at runtime and compare them to the frozen census in section 5.

Any unexpected new root/direct-sources Markdown path must fail closed as:

```text
UNCLASSIFIED_AUTHORITY_CAPABLE_DOCUMENT
```

This is the central PLAN-F004 repair: the verifier must not rely on a manually remembered subset while ignoring another root/source recovery document.

### 23.2 Registry exactness

Every censused document must have exactly one registry class.

Exactly three may be current authority.

No duplicate, missing or unknown classification is allowed.

### 23.3 Explicit fences

The verifier must require the eight authority-capable supporting documents from section 5.2 to carry explicit non-current X1B authority markers.

### 23.4 Pre-fenced documents

The verifier must require the historical/non-authority baseline markers from section 21 without changing those files.

### 23.5 Generic Human approval separation

The verifier must require explicit distinction between:

```text
generic Human approval
historical approve --why semantic acceptance
active decision provenance
X1B HumanDecision authorship evidence
```

in every changed authority-capable document that contains the first three concepts.

### 23.6 Three-state active-product semantics

Only the current trio may publish the active-product assertion field, and for this correction it must be:

```text
CURRENTNESS_UNESTABLISHED
```

No supporting document may publish a competing current active-product state.

### 23.7 Runtime-class separation

Local checked-out runtime classification may remain:

```text
LEGACY_PRE_X1B
X1B_V2_CHECKOUT
UNKNOWN
```

Allowed:

```text
LEGACY_PRE_X1B + CURRENTNESS_UNESTABLISHED = PASS
X1B_V2_CHECKOUT + CURRENTNESS_UNESTABLISHED = PASS
UNKNOWN + CURRENTNESS_UNESTABLISHED = FAIL
```

No recognized local class establishes remote currentness.

## 24. Deterministic synthetic rejection cases

A future candidate must demonstrate fail-closed behavior for at least:

```text
R1  README adds a fourth mandatory bootstrap file -> FAIL
R2  HANDOFF adds a fourth mandatory bootstrap file -> FAIL
R3  SOURCES drops non-current fence -> FAIL
R4  SOURCES restores SOURCE_MANIFEST as current canonical authority -> FAIL
R5  SOURCES restores Decision_Summary as current summary -> FAIL
R6  SOURCES restores ACCESS CHECK REQUIRED as current gap -> FAIL
R7  SOURCE_MANIFEST drops fence -> FAIL
R8  Decision_Summary restores current-authority title -> FAIL
R9  RECONSTRUCTION_REPORT restores ACCESS CHECK as unqualified current next step -> FAIL
R10 SOURCE_AUDIT_SUMMARY drops provenance-only fence -> FAIL
R11 DECISION_LOG drops decision-provenance-only fence -> FAIL
R12 DECISION_LOG `ACTIVE` is mapped to active-product state -> FAIL
R13 RC1_SCOPE_LOCK drops non-X1B authority fence -> FAIL
R14 Main_Theme generic Human approval is treated as X1B HumanDecision authority -> FAIL
R15 a new root `CURRENT_STATUS.md` appears without registry class -> FAIL
R16 a new direct `sources/CurrentFoo.md` appears without registry class -> FAIL
R17 one censused file has two registry classes -> FAIL
R18 one censused file has no registry class -> FAIL
R19 CODEX_START historical/not-current marker disappears -> FAIL
R20 IDEA_ARCHIVE no-implementation-authority marker disappears -> FAIL
R21 current trio disagrees on X1B state -> FAIL
R22 one current-authority file uses CONFIRMED_NOT_REMEDIATED -> FAIL
R23 one current-authority file uses CONFIRMED_REMEDIATED -> FAIL
R24 one current-authority file uses YES/NO or TRUE/FALSE -> FAIL
R25 recognized V2 checkout is promoted to confirmed remediation -> FAIL
R26 recognized legacy checkout is promoted to confirmed-not-remediated -> FAIL
R27 UNKNOWN runtime classification -> FAIL
R28 a supporting document publishes current merge/deploy/release/V1 authority -> FAIL
```

Negative tests must operate on ephemeral copies or pure helper data only and must not mutate canonical repository state.

## 25. Required positive cases

```text
P1 exact twelve-path candidate on baseline + CURRENTNESS_UNESTABLISHED -> PASS
P2 synthetic recognized V2 checkout + same authority documents -> PASS only as CURRENTNESS_UNESTABLISHED
P3 all fourteen root/direct-sources Markdown documents have exactly one registry class -> PASS
P4 all eight authority-capable supporting docs remain readable as provenance while denied current authority -> PASS
P5 CODEX_START / IDEA_ARCHIVE / prototype RESTORE retain their baseline non-authority/history meaning -> PASS
P6 evidence/analysis/continuity/acceptance files remain readable as provenance but cannot override current trio -> PASS
P7 existing repository verification passes after bounded changes -> PASS
P8 existing Phase-6 test suite remains green without modification -> PASS
```

## 26. Exact future candidate acceptance checks

All must hold:

```text
C1  base exactly 2f22843ac570498b506101addeba5453ab777f08
C2  exactly one commit ahead
C3  changed paths exactly the twelve paths in section 6
C4  phase6/scriptops-v2-hardening.py unchanged at baseline blob
C5  phase6/x1b_human_decision.py unchanged / absent exactly as baseline requires
C6  legacy/scriptops-v2-single.py unchanged
C7  scripts/restore_v2.py unchanged
C8  tests/* unchanged
C9  .github/workflows/* unchanged
C10 evidence/* unchanged
C11 current bootstrap exactly README -> PROJECT_STATE -> HANDOFF
C12 current trio agrees on the complete X1B schema
C13 active-product assertion exactly CURRENTNESS_UNESTABLISHED
C14 authority model exactly CLOSED_WORLD_REGISTRY
C15 actual root/direct-sources Markdown census equals the frozen fourteen-document census
C16 every censused document has exactly one registry class
C17 exactly three documents are CURRENT_BOOTSTRAP_AUTHORITY
C18 all eight authority-capable supporting docs carry explicit non-current X1B authority fences
C19 SOURCES no longer reasserts canonical/current/ACCESS-CHECK current authority
C20 SOURCE_MANIFEST is provenance-only
C21 Decision_Summary is provenance-only
C22 RECONSTRUCTION_REPORT is provenance-only
C23 SOURCE_AUDIT_SUMMARY is provenance-only
C24 DECISION_LOG is decision-provenance-only and `ACTIVE` does not mean active product
C25 RC1_SCOPE_LOCK is product-governance provenance only
C26 Main_Theme is product-vision/governance provenance only
C27 generic Human approval / approve --why / active decision provenance are explicitly distinct from X1B HumanDecision authorship evidence
C28 CODEX_START baseline historical/not-current markers remain
C29 IDEA_ARCHIVE baseline non-authority marker remains
C30 prototype RESTORE historical-prototype context remains
C31 verifier is offline and performs no remote-ref inference
C32 verifier accepts recognized legacy checkout only as CURRENTNESS_UNESTABLISHED
C33 verifier accepts recognized V2 checkout only as CURRENTNESS_UNESTABLISHED
C34 verifier rejects UNKNOWN runtime class
C35 verifier demonstrates R1-R28 fail closed
C36 existing repository verification passes
C37 existing Phase-6 tests pass without modification
C38 remote FJ899/scriptops refs/heads/main remains 2f22843ac570498b506101addeba5453ab777f08 throughout candidate preparation/review
```

If any check cannot be satisfied within the exact twelve-path surface, STOP and record a plan defect rather than expanding implementation scope.

## 27. PR #35 overlap hazard

PR #35 overlaps multiple future correction paths, including at least:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
SOURCE_MANIFEST.md
scripts/verify_repository.py
```

Therefore if the frame/status correction is later separately authorized, reviewed, accepted and merged first:

```text
PR #35 MUST NOT THEN BE MERGED AS-IS
```

Any later runtime integration must create a new reviewed candidate based on the then-current default branch or an equivalently reviewed integration preserving both the X1B V2 runtime/security properties and this closed-world frame boundary.

This plan does not authorize rebase, merge, replacement or modification of PR #35.

## 28. Future active-product confirmation remains separate

Neither confirmed state may be published under this plan.

A future promotion requires separately:

```text
1. external read-only resolution of actual FJ899/scriptops refs/heads/main
2. binding that commit to runtime identity/class
3. durable currentness evidence
4. separate Human acceptance
5. status-only promotion candidate
6. independent verification that publication still matches active runtime identity
```

No part of that procedure is authorized here.

## 29. Independent review requirements

A future independent read-only review of this exact plan must attack at least:

```text
Q1  is the root/direct-sources census actually complete at the frozen baseline?
Q2  can any file outside the census still enter current bootstrap authority?
Q3  can a new root/direct-sources Markdown file evade the verifier classification?
Q4  can DECISION_LOG `ACTIVE` or canonical wording become current X1B authority?
Q5  can Main_Theme `Core product law` generic Human approval become X1B HumanDecision authority?
Q6  can RC1_SCOPE_LOCK become current remediation/deployment authority?
Q7  can SOURCE_AUDIT_SUMMARY canonical language become current authority?
Q8  does SOURCES fully close PLAN-F004 rather than merely defer to SOURCE_MANIFEST?
Q9  can path-classed evidence/analysis/continuity/acceptance material override the current trio?
Q10 can CURRENTNESS_UNESTABLISHED collapse into ontic NO/YES?
Q11 can a PR-local V2 checkout establish active-product remediation?
Q12 can PR #35 later overwrite the frame boundary without a new reviewed candidate?
Q13 does any wording create merge/deployment/release/tag/V1 authority?
Q14 can disagreement inside the trio pass instead of failing closed?
Q15 is the twelve-path implementation surface larger than necessary in a way that creates a new capability/runtime change?
```

Review rule:

```text
FIRST CREDIBLE COUNTEREXAMPLE = DURABLE FINDING + STOP
```

No repair may occur inside that review.

## 30. Authority boundary and exit state

```text
X1B = CLOSED AT ACCEPTED RESEARCH/CORRECTIVE SCOPE
X1B-FRAME-F001 = HUMAN ACCEPTED / OPEN FOR CORRECTION
X1B-FRAME-F001-PLAN-F001 = HUMAN ACCEPTED
X1B-FRAME-F001-PLAN-F002 = HUMAN ACCEPTED
X1B-FRAME-F001-PLAN-F003 = HUMAN ACCEPTED
X1B-FRAME-F001-PLAN-F004 = HUMAN ACCEPTED
PR #184 = SUPERSEDED / HISTORICAL NOT PASS
PR #187 = SUPERSEDED / HISTORICAL NOT PASS
PR #192 = SUPERSEDED / HISTORICAL NOT PASS
PR #195 = SUPERSEDED / HISTORICAL NOT PASS
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
AI PROPOSES != HUMAN DECIDES
PLAN PREPARATION AUTHORITY != PLAN REVIEW AUTHORITY
PLAN REVIEW PASS != IMPLEMENTATION AUTHORITY
AUTHORITY IS REGISTRY-GRANTED, NOT SELF-ASSERTED
CURRENTNESS_UNESTABLISHED != FALSE
CURRENTNESS_UNESTABLISHED != TRUE
CURRENT-LOOKING RECOVERY SOURCE != CURRENT AUTHORITY BY SELF-LABEL
READ LATER != AUTHORITATIVE LATER
CHECKED_OUT_RUNTIME_CLASS != ACTIVE_PRODUCT_STATE
PR HEAD != ACTIVE DEFAULT BRANCH
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
```