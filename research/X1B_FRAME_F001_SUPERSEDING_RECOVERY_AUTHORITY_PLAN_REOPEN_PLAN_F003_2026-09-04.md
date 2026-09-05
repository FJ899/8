# X1B-FRAME F001 — Superseding Recovery-Authority Plan After PLAN-F003

Status: `SUPERSEDING PLAN ONLY / HUMAN-AUTHORIZED TO PREPARE / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-04`

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
```

Exact PLAN-F003 finding:

```text
FJ899/8 PR #193
HEAD = b50a219007a197700940d4d698c430f29ae62824
TREE = 8de69ec60365e7965fc138183c765b996ffa4af3
PATH = research/X1B_FRAME_F001_STATUS_SEMANTICS_PLAN_REVIEW_F003_2026-09-04.md
BLOB = 81babf1c52c407142ebad150deca291b3b9ab329
FINDING = X1B-FRAME-F001-PLAN-F003
```

PLAN-F003 states that the four-path plan can pass while the repository's own zero-history startup route still consumes unchanged files with current/canonical-looking authority and pre-X1B Human-approval semantics.

Human acceptance of that exact finding and authority to prepare exactly one next superseding bounded plan are recorded in:

```text
FJ899/8 PR #194
HEAD = e6e7b397a1ac9ff1bf90e41a1caeb44fa5a9ef7f
HUMAN RESPONSE = accept
```

This document is that one authorized superseding plan.

It supersedes PR #192 for future implementation-authority purposes. PR #184, PR #187 and PR #192 remain historical provenance and are not silently rewritten.

No ScriptOps mutation is authorized by this document.

## 2. Repair strategy chosen for PLAN-F003

The accepted finding allowed four bounded repair classes:

```text
A. narrow current startup/recovery route;
B. explicitly reclassify stale current/canonical-looking sources;
C. correct identified stale authority semantics within a bounded path set;
D. make the offline verifier prove the resulting recovery-authority boundary.
```

This superseding plan deliberately uses a bounded combination of all four.

The core repair is:

```text
CURRENT-STATE AUTHORITY MUST BE EXPLICITLY TIERED.
A FILE DOES NOT BECOME CURRENT AUTHORITY MERELY BECAUSE ITS OLD TITLE OR BODY
CONTAINS "CURRENT", "CANONICAL", "DECISION", "SOURCE OF TRUTH", OR "NEXT STEP".
```

For zero-history recovery, the mandatory current-authority bootstrap is reduced to exactly:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
```

Everything else is either decision provenance, evidence, implementation material or historical reconstruction provenance and must not override that current-authority trio.

The three concrete stale/current-looking surfaces identified by PLAN-F003 are additionally reclassified in place:

```text
SOURCE_MANIFEST.md
sources/Decision_Summary_Current_State.md
RECONSTRUCTION_REPORT.md
```

This avoids relying on ordering alone.

The verifier then proves the route, the authority classes and the reclassification fences.

## 3. Preserved semantic repair from PLAN-F002

PLAN-F003 did not reject the three-state active-product status model from PR #192.

That model remains mandatory:

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

The bounded correction governed by this plan must publish only:

```text
X1B_ACTIVE_PRODUCT_REMEDIATION_ASSERTION = CURRENTNESS_UNESTABLISHED
```

No offline checkout, PR head, green verifier result, reviewed candidate, stale source label or generic Human-approval wording may convert that state into either confirmed state.

## 4. Frozen repository state

Evidence repository planning anchor:

```text
FJ899/8 refs/heads/main
HEAD = 0b516edb210fd4029972e932fec0206d8a6df1cb
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

Current active ScriptOps default branch independently re-read before plan preparation:

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

The current ScriptOps baseline files relevant to this plan are:

```text
README.md
BLOB = c52f515dd3d736c749eca75cf319b514f8427c5a

PROJECT_STATE.md
BLOB = dea1d11c847765026f8766fa70aa111c3f77c7bd

HANDOFF.md
BLOB = 2e0c3be2a9bdebfeac161773ca9631f8312f42f6

SOURCE_MANIFEST.md
BLOB = 2acf2ece298bfcf89254087c9e747fcb808ab241

sources/Decision_Summary_Current_State.md
BLOB = 9aea3d7e8de5dde8025278adca0546324d21dd00

RECONSTRUCTION_REPORT.md
BLOB = 383354c61c707ed4a1210f60f03125fca4daae8a

scripts/verify_repository.py
BLOB = a61278086b92824d7e442b390c951e918c88517b
```

If `FJ899/scriptops refs/heads/main` changes before implementation begins, this exact plan is no longer executable without a fresh Human disposition rebinding the baseline.

## 5. Exact future implementation surface

A future implementation candidate under this plan may change exactly seven ScriptOps paths:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
SOURCE_MANIFEST.md
sources/Decision_Summary_Current_State.md
RECONSTRUCTION_REPORT.md
scripts/verify_repository.py
```

No other ScriptOps path may change.

The implementation candidate, if separately authorized later, must be exactly one commit on top of:

```text
2f22843ac570498b506101addeba5453ab777f08
```

Forbidden paths include, without limitation:

```text
phase6/scriptops-v2-hardening.py
phase6/x1b_human_decision.py
legacy/scriptops-v2-single.py
scripts/restore_v2.py
tests/*
.github/workflows/*
SOURCE_AUDIT_SUMMARY.md
CODEX_START.md
DECISION_LOG.md
IDEA_ARCHIVE.md
evidence/*
sources/prototype/*
sources/RC1_SCOPE_LOCK.md
sources/ScriptOps_Main_Theme_Summary.md
```

No runtime remediation is performed by this plan.

## 6. Current-authority model

The repository must distinguish at least four authority classes.

### 6.1 CURRENT_BOOTSTRAP_AUTHORITY

Exactly:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
```

Their roles are separate:

```text
README.md       = current recovery entry and authority-routing contract
PROJECT_STATE.md = current project/status owner
HANDOFF.md      = current bounded resume/next-action pointer
```

No other file may self-promote into this class through its title or stale prose.

### 6.2 DECISION_PROVENANCE

Examples:

```text
DECISION_LOG.md
```

Decision provenance may establish that a Human decision historically occurred and what it said.

It does not by itself establish:

```text
current active-product remediation state
current default-branch identity
current deployment state
current V1 authority
current next action
current X1B HumanDecision admission semantics
```

unless the current-authority trio explicitly incorporates a later accepted decision into current state.

### 6.3 EVIDENCE / IMPLEMENTATION PROVENANCE

Examples include:

```text
evidence/*
analysis/*
phase6/*
legacy/*
tests/*
```

These files may establish historical or candidate facts within their bounded evidence meaning.

They may not override current status/next-action authority.

### 6.4 HISTORICAL_RECONSTRUCTION_PROVENANCE

For the concrete PLAN-F003 surfaces:

```text
SOURCE_MANIFEST.md
sources/Decision_Summary_Current_State.md
RECONSTRUCTION_REPORT.md
```

These must be explicitly fenced as historical/reconstruction provenance and not current X1B state authority.

## 7. Zero-history recovery contract

The current zero-history recovery algorithm must be frozen as:

```text
1. READ README.md
2. READ PROJECT_STATE.md
3. READ HANDOFF.md
4. CURRENT-STATE RECOVERY COMPLETE
5. STOP BEFORE CONSEQUENTIAL WORK
6. LOAD ONLY THE SUPPORTING PROVENANCE NEEDED BY THE CURRENT HANDOFF/TASK
```

The current mandatory startup list must contain exactly those three current-authority files.

A static extended list of old evidence, old reconstruction documents or implementation files must not be presented as part of the current-authority bootstrap.

Supporting provenance can still be consulted after the current state is established, but it must be introduced as supporting material, not as co-equal current authority.

Mandatory invariant:

```text
READ LATER != AUTHORITATIVE LATER
```

and:

```text
STALE SELF-LABEL != CURRENT AUTHORITY
```

## 8. Cross-file precedence rule

README, PROJECT_STATE and HANDOFF must state an equivalent precedence rule:

```text
FOR CURRENT X1B STATUS, HUMANDECISION AUTHORITY, CURRENT NEXT ACTION,
ACTIVE-PRODUCT REMEDIATION STATE, MERGE/DEPLOYMENT/RELEASE/V1 STATUS:

README + PROJECT_STATE + HANDOFF CURRENT-AUTHORITY CONTRACT WINS.

OLDER / SUPPORTING / HISTORICAL FILES MAY NOT OVERRIDE IT.
```

This is not a generic claim that history is unimportant.

It is an explicit authority boundary for current-state interpretation.

If the trio conflicts internally, fail closed and require Human rebind rather than choosing a convenient value.

## 9. Required X1B current-state schema in the authority trio

All three current-authority files must expose equivalent stable fields:

```text
X1B_RESEARCH_CLOSURE
X1B_ACTIVE_PRODUCT_REMEDIATION_ASSERTION
X1B_ACTIVE_PRODUCT_ASSERTION_AUTHORITY
X1B_ACTIVE_PRODUCT_ASSERTION_EVIDENCE
X1B_REVIEWED_REMEDIATION_PROVENANCE
X1B_CURRENT_AUTHORITY_BOOTSTRAP
```

For this exact correction candidate:

```text
X1B_RESEARCH_CLOSURE: CLOSED
X1B_ACTIVE_PRODUCT_REMEDIATION_ASSERTION: CURRENTNESS_UNESTABLISHED
X1B_ACTIVE_PRODUCT_ASSERTION_AUTHORITY: EXTERNAL_CURRENTNESS_REBIND_REQUIRED
X1B_ACTIVE_PRODUCT_ASSERTION_EVIDENCE: NONE_ACCEPTED_FOR_THIS STATUS PUBLICATION
X1B_REVIEWED_REMEDIATION_PROVENANCE: PR #35 / REVIEWED HEAD 7c40a92165714023743e91c63b5b11b102fadd92
X1B_CURRENT_AUTHORITY_BOOTSTRAP: README.md -> PROJECT_STATE.md -> HANDOFF.md
```

Equivalent exact implementation spelling may be chosen, but the verifier must enforce one frozen spelling consistently.

No fixed pre-merge `CURRENT ACTIVE MAIN` SHA may be published as timeless current state.

The baseline SHA `2f22843...` may appear only as implementation/provenance identity.

## 10. README.md required correction

README must become the explicit current recovery router.

Near the top, it must carry the X1B status block from section 9.

Its zero-history startup section must identify exactly:

```text
1. README.md
2. PROJECT_STATE.md
3. HANDOFF.md
```

as the mandatory current-authority bootstrap.

It must then state an explicit stop boundary equivalent to:

```text
After these three files, current-state recovery is complete.
Do not infer current authority from older files merely because they are later consulted.
```

The existing static list that currently includes `DECISION_LOG.md`, evidence files, `IDEA_ARCHIVE.md`, `SOURCE_MANIFEST.md` and `RECONSTRUCTION_REPORT.md` must no longer be presented as the mandatory current startup route.

README may include a separate supporting-provenance section, but it must state:

```text
supporting provenance != current state authority
```

README must preserve the PLAN-F002 semantics:

```text
CURRENTNESS_UNESTABLISHED != CONFIRMED_NOT_REMEDIATED
CURRENTNESS_UNESTABLISHED != CONFIRMED_REMEDIATED
```

README must also state:

```text
legacy approve --why != sufficient X1B HumanDecision authorship authority
PR #35 reviewed candidate != active-product proof
green verification != deployment
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
```

Any historical Phase-6 `approve --why` prose that remains must be clearly labelled historical/legacy in its current interpretation.

The current next-action section must not direct a consequential X1B-authorship effect through legacy `approve --why`.

## 11. PROJECT_STATE.md required correction

`PROJECT_STATE.md` remains the current status owner.

It must carry the same X1B status and authority-routing fields.

The current top-level state must explicitly distinguish:

```text
CONTENT SEMANTIC ACCEPTANCE
SYSTEM HumanDecision ATTRIBUTION
ACTIVE-PRODUCT REMEDIATION ASSERTION
CURRENT NEXT-ACTION AUTHORITY
```

The existing historical Phase-6 model:

```text
human decision with why
human approve --why = semantic decision
```

may remain only with an explicit current fence equivalent to:

```text
HISTORICAL PHASE-6 CONTENT SEMANTIC ACCEPTANCE
!=
X1B HumanDecision authorship evidence
```

`PROJECT_STATE.md` must say that current X1B active-product remediation is `CURRENTNESS_UNESTABLISHED`, not `NO` and not `YES`.

It must state that supporting provenance cannot override the current authority trio.

DEC-SO-011 remains preserved as historical/current semantic-decision provenance but does not become X1B V2 HumanDecision admission evidence.

## 12. HANDOFF.md required correction

`HANDOFF.md` remains the current bounded resume/next-action pointer.

Its YAML header must include fields equivalent to:

```text
x1b_research_closure: "CLOSED"
x1b_active_product_remediation_assertion: "CURRENTNESS_UNESTABLISHED"
x1b_active_product_assertion_authority: "EXTERNAL_CURRENTNESS_REBIND_REQUIRED"
x1b_current_authority_bootstrap: "README.md -> PROJECT_STATE.md -> HANDOFF.md"
x1b_supporting_provenance_authority: "NO CURRENT-STATE OVERRIDE"
```

The current blocker/next step must be reconciled with the X1B frame correction and must not direct a consequential Human-authorship effect through the legacy path.

The section currently titled equivalent to `files to open by a new session` must no longer present a fourteen-file static list as the mandatory startup authority chain.

It must instead contain:

```text
Mandatory current bootstrap:
1. README.md
2. PROJECT_STATE.md
3. HANDOFF.md

Supporting provenance:
load only after current state is established and only as required by the bounded task.
```

The handoff must explicitly say:

```text
A supporting file's old current/canonical label does not override the current trio.
```

## 13. SOURCE_MANIFEST.md required reclassification

The current file is a concrete PLAN-F003 counterexample because it calls itself an operational/canonical source index and labels `sources/Decision_Summary_Current_State.md` as current.

It must be reclassified in place with a machine-readable or equally stable fence equivalent to:

```text
document_class: "HISTORICAL_RECONSTRUCTION_PROVENANCE_INDEX"
current_state_authority: "NO"
x1b_humandecision_authority: "NO"
current_next_action_authority: "NO"
```

Its old heading equivalent to:

```text
Kanoniczne źródła operacyjne
```

must be removed or explicitly rewritten so it cannot be read as current operational authority.

Its description of:

```text
sources/Decision_Summary_Current_State.md
```

must state that the file name is historical provenance and does not confer current X1B state authority.

The manifest may continue indexing reconstruction assets and historical sources.

It must point a zero-history reader back to:

```text
README.md -> PROJECT_STATE.md -> HANDOFF.md
```

for current state.

It must not introduce a competing current next action.

## 14. sources/Decision_Summary_Current_State.md required reclassification

The path name is preserved for provenance compatibility, but its content must no longer self-present as current authority.

It must gain a top-level fence equivalent to:

```text
STATUS: HISTORICAL PRODUCT-DECISION SUMMARY / RECONSTRUCTION PROVENANCE
CURRENT X1B STATE AUTHORITY: NO
CURRENT HumanDecision AUTHORITY: NO
```

The old title:

```text
# Current Decision Summary
```

must be replaced by an explicitly historical/reconstruction title.

The generic governance statement that the Agent may create candidates but may not approve/commit/edit canon without Human approval may remain only as historical product-governance provenance and must be paired with an X1B fence equivalent to:

```text
GENERIC HUMAN APPROVAL GOVERNANCE
!=
X1B HumanDecision authorship evidence
```

The document must direct current-state recovery to the authority trio.

It must not claim current deployment, remediation, next-action or V1 status.

## 15. RECONSTRUCTION_REPORT.md required reclassification

The report must gain an explicit historical fence equivalent to:

```text
STATUS: HISTORICAL RECONSTRUCTION PROVENANCE / NOT CURRENT RECOVERY AUTHORITY
CURRENT X1B STATE AUTHORITY: NO
CURRENT NEXT-ACTION AUTHORITY: NO
```

Its historical model:

```text
AI candidate -> validation -> Human decision -> reason -> commit
```

may remain as reconstruction history only if paired with an explicit current X1B fence.

Its historical product rule about Human approval must not be readable as sufficient current HumanDecision authorship authority.

The existing historical section equivalent to:

```text
Jeden następny krok -> ACCESS CHECK
```

must be relabelled as the historical next step at reconstruction time, not a current instruction.

The report must direct current recovery to:

```text
README.md -> PROJECT_STATE.md -> HANDOFF.md
```

and must not self-claim current implementation activation status.

## 16. scripts/verify_repository.py required correction

Add a deterministic offline authority/recovery check, for example:

```text
check_x1b_recovery_authority_boundary()
```

The verifier remains offline and must not call GitHub or infer active-product confirmed state from its checkout.

### 16.1 Current authority trio

The verifier must require the exact current-authority set:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
```

and fail if the mandatory current bootstrap includes any additional file.

It must require the same X1B status schema and `CURRENTNESS_UNESTABLISHED` value in all three.

### 16.2 Route exactness

The verifier must deterministically reject a candidate if README or HANDOFF again presents any of these as mandatory current startup authority:

```text
DECISION_LOG.md
SOURCE_MANIFEST.md
RECONSTRUCTION_REPORT.md
sources/Decision_Summary_Current_State.md
evidence/*
analysis/*
legacy/*
phase6/*
tests/*
```

Those files may appear only in clearly delimited supporting-provenance/history sections.

### 16.3 PLAN-F003 concrete fences

The verifier must require explicit provenance-only fences in:

```text
SOURCE_MANIFEST.md
sources/Decision_Summary_Current_State.md
RECONSTRUCTION_REPORT.md
```

It must reject the stale current-authority markers identified by PLAN-F003, including equivalent exact implementation markers for:

```text
SOURCE_MANIFEST: old "canonical operational sources" current-authority heading
Decision Summary: old top-level "Current Decision Summary" authority title
Reconstruction Report: old unqualified "one next step" current instruction
```

Historical quotation is allowed only inside a file that also carries the required explicit non-current authority fence.

### 16.4 X1B HumanDecision semantic fence

The verifier must require current-authority files and the three reclassified PLAN-F003 files to distinguish:

```text
generic Human approval
historical approve --why semantic acceptance
X1B HumanDecision authorship evidence
```

and must fail if generic/historical approval is presented as sufficient current X1B authority.

### 16.5 Three-state active-product semantics retained

The verifier must continue to enforce:

```text
CURRENTNESS_UNESTABLISHED != CONFIRMED_NOT_REMEDIATED
CURRENTNESS_UNESTABLISHED != CONFIRMED_REMEDIATED
```

and reject `YES/NO`, `TRUE/FALSE`, `DEPLOYED/NOT DEPLOYED` or equivalent two-state active-product shortcuts in current authority fields.

### 16.6 Local runtime classification remains separate

The verifier may classify the checked-out runtime as:

```text
LEGACY_PRE_X1B
X1B_V2_CHECKOUT
UNKNOWN
```

but neither recognized class may establish a confirmed active-product status.

Allowed under this correction contract:

```text
LEGACY_PRE_X1B + CURRENTNESS_UNESTABLISHED = PASS
X1B_V2_CHECKOUT + CURRENTNESS_UNESTABLISHED = PASS
UNKNOWN + CURRENTNESS_UNESTABLISHED = FAIL
```

A V2 checkout PASS means only that the local candidate is recognized while active-product currentness remains unestablished.

### 16.7 Historical Phase-6 checks

Existing checks for Phase-6 proof may remain, including historical `approve --why` markers, but their output must be explicitly historical/bounded and must not imply current X1B HumanDecision authority or active remediation.

## 17. Deterministic synthetic rejection cases

Before a future correction candidate can enter independent implementation review, the verifier must demonstrate at least the following fail-closed cases using ephemeral copies or pure-helper invocation only:

```text
R1  README re-adds SOURCE_MANIFEST to mandatory current startup -> FAIL
R2  README re-adds RECONSTRUCTION_REPORT to mandatory current startup -> FAIL
R3  HANDOFF re-adds static extended current startup list -> FAIL
R4  SOURCE_MANIFEST drops provenance-only fence -> FAIL
R5  SOURCE_MANIFEST restores old canonical-operational authority heading -> FAIL
R6  Decision_Summary restores top-level Current Decision Summary authority title -> FAIL
R7  Decision_Summary drops generic-Human-approval != X1B fence -> FAIL
R8  RECONSTRUCTION_REPORT drops historical/non-current fence -> FAIL
R9  RECONSTRUCTION_REPORT restores unqualified ACCESS CHECK as current next step -> FAIL
R10 one current-authority file says CONFIRMED_NOT_REMEDIATED -> FAIL
R11 one current-authority file says CONFIRMED_REMEDIATED -> FAIL
R12 one current-authority file uses boolean YES/NO active-product status -> FAIL
R13 current-authority trio disagrees on X1B state -> FAIL
R14 recognized V2 checkout is converted into confirmed remediation -> FAIL
R15 recognized legacy checkout is converted into confirmed-not-remediated -> FAIL
R16 UNKNOWN/ambiguous runtime classification -> FAIL
```

No canonical repository mutation is permitted for these negative checks.

## 18. Required positive cases

The future candidate must also show:

```text
P1 exact seven-path candidate on legacy baseline + CURRENTNESS_UNESTABLISHED -> PASS
P2 synthetic recognized V2 checkout + same authority/status documents -> PASS only as CURRENTNESS_UNESTABLISHED
P3 current trio routes to supporting historical evidence without allowing override -> PASS
P4 the three reclassified PLAN-F003 files remain readable as provenance -> PASS
P5 existing repository verification still passes after bounded changes -> PASS
P6 existing Phase-6 test suite remains green without modification -> PASS
```

No positive case may claim deployment, active-product remediation or HumanDecision authority from generic Human approval.

## 19. Exact acceptance checks for a future implementation candidate

All must hold:

```text
C1  base exactly 2f22843ac570498b506101addeba5453ab777f08
C2  exactly one commit ahead of base
C3  changed paths exactly the seven paths in section 5
C4  phase6/scriptops-v2-hardening.py unchanged at blob 4f379960ed5677634dd234af6aa39626782b6133
C5  phase6/x1b_human_decision.py unchanged / absent exactly as baseline requires
C6  legacy/scriptops-v2-single.py unchanged
C7  tests/* unchanged
C8  .github/workflows/* unchanged
C9  scripts/restore_v2.py unchanged
C10 README mandatory current startup is exactly README -> PROJECT_STATE -> HANDOFF
C11 HANDOFF mandatory current startup is exactly README -> PROJECT_STATE -> HANDOFF
C12 all three current-authority files carry the same X1B status schema
C13 active-product assertion is CURRENTNESS_UNESTABLISHED in all three
C14 no current-authority file uses boolean active-remediation state
C15 SOURCE_MANIFEST is explicitly historical/reconstruction provenance, not current authority
C16 Decision_Summary is explicitly historical/reconstruction provenance, not current authority
C17 RECONSTRUCTION_REPORT is explicitly historical/reconstruction provenance, not current authority
C18 old SOURCE_MANIFEST canonical/current authority wording is removed or fenced so it cannot self-promote
C19 old Decision Summary generic Human-approval semantics are explicitly non-X1B-authoritative
C20 old Reconstruction next-step semantics are explicitly historical, not current
C21 legacy approve --why is explicitly non-X1B-authoritative in current interpretation
C22 PR #35 appears only as reviewed remediation provenance, not active-product proof
C23 verifier has no network access and no remote-ref inference
C24 verifier accepts recognized legacy checkout only as CURRENTNESS_UNESTABLISHED
C25 verifier accepts recognized V2 checkout only as CURRENTNESS_UNESTABLISHED
C26 verifier rejects UNKNOWN runtime classification
C27 verifier demonstrates R1-R16 fail closed
C28 existing repository verification passes
C29 existing Phase-6 tests pass without modification
C30 remote FJ899/scriptops refs/heads/main remains 2f22843... throughout candidate preparation and review
```

If any acceptance check cannot be demonstrated within the exact seven-path surface, STOP and record a plan defect rather than silently expanding scope.

## 20. PR #35 overlap hazard

PR #35 currently overlaps this correction in at least these paths:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
SOURCE_MANIFEST.md
scripts/verify_repository.py
```

Therefore, if a future PLAN-F003 correction candidate is separately authorized, reviewed, accepted and merged first:

```text
PR #35 MUST NOT THEN BE MERGED AS-IS
```

A later V2 integration must start from the then-current default branch or otherwise produce a new reviewed candidate that preserves both:

```text
reviewed X1B V2 runtime/security properties
and
this recovery-authority / three-state frame boundary
```

This plan does not authorize any edit, rebase, cherry-pick, replacement or merge of PR #35.

## 21. Future active-product confirmation remains separately gated

This plan still does not authorize publication of:

```text
CONFIRMED_NOT_REMEDIATED
```

or:

```text
CONFIRMED_REMEDIATED
```

Either future confirmed state requires a separate later procedure with, at minimum:

```text
1. external read-only resolution of actual FJ899/scriptops refs/heads/main;
2. binding of that active commit to the relevant runtime identity/class;
3. durable currentness evidence;
4. separate Human acceptance of that evidence;
5. a status-promotion candidate that changes no runtime path;
6. verification that the publication still corresponds to the proven active runtime identity.
```

Nothing in this plan authorizes those steps.

## 22. Independent review requirements

A future independent read-only review of this exact plan must attack at least:

```text
Q1  can any file outside README/PROJECT_STATE/HANDOFF still self-promote into current X1B authority?
Q2  can README or HANDOFF still cause a zero-history session to treat supporting provenance as mandatory current authority?
Q3  do SOURCE_MANIFEST, Decision_Summary and RECONSTRUCTION_REPORT have strong enough non-current fences?
Q4  can the filename Decision_Summary_Current_State itself still defeat the content fence?
Q5  can generic Human approval or historical approve --why leak back into current HumanDecision semantics?
Q6  can CURRENTNESS_UNESTABLISHED still collapse into an ontic NO or YES?
Q7  can a PR-local V2 checkout establish active-product remediation?
Q8  can historical Phase-6 verifier PASS output be mistaken for current X1B remediation PASS?
Q9  does the exact seven-path set cover every concrete PLAN-F003 current/canonical surface without unnecessary runtime expansion?
Q10 can PR #35 later overwrite the boundary without creating a new reviewed candidate?
Q11 does any wording accidentally create merge/deployment/release/tag/V1 authority?
Q12 can disagreement inside the current-authority trio pass instead of failing closed?
```

Review rule:

```text
FIRST CREDIBLE COUNTEREXAMPLE = DURABLE FINDING + STOP
```

No plan repair may occur inside that review.

## 23. Authority boundary and exit state

Current legal state after this plan is frozen:

```text
X1B = CLOSED AT ACCEPTED RESEARCH/CORRECTIVE SCOPE
X1B-FRAME-F001 = HUMAN ACCEPTED / OPEN FOR CORRECTION
X1B-FRAME-F001-PLAN-F001 = HUMAN ACCEPTED
X1B-FRAME-F001-PLAN-F002 = HUMAN ACCEPTED
X1B-FRAME-F001-PLAN-F003 = HUMAN ACCEPTED
PR #184 = SUPERSEDED / HISTORICAL NOT PASS
PR #187 = SUPERSEDED / HISTORICAL NOT PASS
PR #192 = SUPERSEDED / HISTORICAL NOT PASS
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
CURRENTNESS_UNESTABLISHED != FALSE
CURRENTNESS_UNESTABLISHED != TRUE
CURRENT-LOOKING RECOVERY SOURCE != CURRENT AUTHORITY BY SELF-LABEL
READ LATER != AUTHORITATIVE LATER
CHECKED_OUT_RUNTIME_CLASS != ACTIVE_PRODUCT_STATE
PR HEAD != ACTIVE DEFAULT BRANCH
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
```