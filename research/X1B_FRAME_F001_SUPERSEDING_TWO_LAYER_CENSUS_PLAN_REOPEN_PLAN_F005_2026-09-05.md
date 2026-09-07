# X1B-FRAME F001 — Superseding Two-Layer Census Plan After PLAN-F005

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
PR #187 = superseding plan after PLAN-F001 / NOT PASS
PR #192 = superseding plan after PLAN-F002 / NOT PASS
PR #195 = superseding plan after PLAN-F003 / NOT PASS
PR #198 = superseding closed-world plan after PLAN-F004 / NOT PASS
PR #199 = PLAN-F005
```

Exact accepted PLAN-F005 finding:

```text
FJ899/8 PR #199
BASE = 0b516edb210fd4029972e932fec0206d8a6df1cb
HEAD = 3efb622f929a96c02d568979bdf6637f2677da15
TREE = 2c7a851b0a905192a67fccd9c23a2c8488de2c28
PATH = research/X1B_FRAME_F001_CLOSED_WORLD_PLAN_REVIEW_F005_2026-09-05.md
BLOB = f93ca81db79c06e40ee19a0301d2ada3fff8ec3f
FINDING = X1B-FRAME-F001-PLAN-F005
```

Human acceptance and authority to prepare exactly one successor plan are recorded in:

```text
FJ899/8 PR #200
HEAD = 7581dbb52c2bf0c9f2c4ec0a2d0230831e674e12
HUMAN RESPONSE = accept
```

This document is that one authorized superseding plan.

It supersedes PR #198 for future implementation-authority purposes. Earlier plans remain historical provenance and are not silently rewritten.

No ScriptOps mutation is authorized by this document.

## 2. PLAN-F005 repair strategy

PLAN-F005 found that PR #198 mixed two incompatible universes:

```text
U1 = root *.md + direct sources/*.md = 13 documents
U2 = U1 + sources/prototype/RESTORE.md = 14 documents
```

The repair is not to guess which count was intended.

The repair is to define **two separate layers with different semantics** and never mix their cardinalities.

```text
LAYER A = ENUMERATED AUTHORITY-REGISTRY SURFACE
LAYER B = PATH-CLASS DENY-BY-DEFAULT PROVENANCE SURFACE
```

Mandatory invariant:

```text
REGISTRY CENSUS != PATH-CLASS SENTINEL SET
```

and:

```text
CLOSED WORLD = ONE EXACT REGISTRY UNIVERSE + EXPLICIT DENY-BY-PATH OUTSIDE IT
```

There is no 14-document registry census in this plan.

## 3. Preserved active-product semantics

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

For the bounded frame/status correction governed by this plan, the only allowed current publication is:

```text
X1B_ACTIVE_PRODUCT_REMEDIATION_ASSERTION = CURRENTNESS_UNESTABLISHED
```

No local checkout, PR head, reviewed candidate, green verifier, source label, historical approval or path class may promote that value.

## 4. Frozen repository anchors

Evidence planning anchor:

```text
FJ899/8 refs/heads/main
HEAD = 0b516edb210fd4029972e932fec0206d8a6df1cb
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

ScriptOps implementation baseline:

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

If `FJ899/scriptops refs/heads/main` changes before implementation begins, this plan is no longer executable without fresh Human rebinding.

## 5. Exact Layer-A enumeration algorithm

Define the registry universe `U_REGISTRY` exactly as:

```text
U_REGISTRY =
  every Markdown file whose parent directory is the repository root
  UNION
  every Markdown file whose parent directory is exactly repository-root/sources
```

Equivalent pseudocode:

```text
root_md = sorted(p for p in ROOT.iterdir()
                 if p.is_file() and p.suffix == ".md")

direct_sources_md = sorted(p for p in (ROOT / "sources").iterdir()
                           if p.is_file() and p.suffix == ".md")

U_REGISTRY = root_md + direct_sources_md
```

Explicit exclusions:

```text
NO RECURSION
NO GLOB **/*.md
NO nested sources/*/*.md
NO special-case insertion
NO separately appended sentinel path
```

At the frozen baseline, `U_REGISTRY` must contain exactly these 13 paths:

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
sources/Decision_Summary_Current_State.md
sources/RC1_SCOPE_LOCK.md
sources/ScriptOps_Main_Theme_Summary.md
```

Therefore:

```text
CARDINALITY(U_REGISTRY) = 13
```

This count is normative for this exact baseline.

## 6. Exact Layer-B path-class model

Markdown documents outside `U_REGISTRY` are not silently added to the registry census.

Instead, nested/supporting locations are governed by explicit path classes.

At minimum, the verifier must recognize these deny-by-default provenance prefixes:

```text
analysis/
continuity/
evidence/
acceptance/
sources/prototype/
```

and these implementation/non-status prefixes:

```text
legacy/
phase6/
tests/
.github/
scripts/
```

For every Markdown path outside `U_REGISTRY`:

```text
if path is under an allowed provenance prefix:
    current_x1b_authority = DENIED_BY_PATH_CLASS
elif path is under an implementation/non-status prefix:
    current_x1b_authority = DENIED_BY_PATH_CLASS
else:
    FAIL as UNCLASSIFIED_MARKDOWN_LOCATION
```

This rule is recursive for path-class membership only.

It does **not** make nested members part of the 13-document registry census.

Mandatory invariant:

```text
PATH-CLASS DENIAL != REGISTRY MEMBERSHIP
```

## 7. Exact treatment of sources/prototype/RESTORE.md

At the frozen baseline:

```text
PATH = sources/prototype/RESTORE.md
BLOB = 8a79aca4c93b23c4842792bea9ecaae146e1fc48
```

Its classification is:

```text
LAYER = B
PATH CLASS = sources/prototype/
AUTHORITY = DENIED_BY_PATH_CLASS
REGISTRY MEMBER = NO
REGISTRY CARDINALITY CONTRIBUTION = 0
```

The verifier may retain a baseline semantic sentinel that confirms this existing file still contains historical prototype reconstruction context.

That sentinel is separate from registry exactness.

Therefore:

```text
RESTORE semantic sentinel PASS/FAIL
!=
U_REGISTRY membership
```

No special-case insertion of `RESTORE.md` into `U_REGISTRY` is permitted.

## 8. Closed-world authority registry

Every path in `U_REGISTRY` must have exactly one registry class.

Minimum classes:

```text
CURRENT_BOOTSTRAP_AUTHORITY
DECISION_PROVENANCE_ONLY
HISTORICAL_RECONSTRUCTION_PROVENANCE_ONLY
HISTORICAL_PRODUCT_GOVERNANCE_PROVENANCE_ONLY
PRE_FENCED_NONAUTHORITY_PROVENANCE
```

Exactly these three may be current bootstrap authority:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
```

The other ten registry members must be explicitly non-current-authority classes.

No registry member may be missing, duplicated, or multi-classified.

Any new root-level Markdown file or new direct `sources/*.md` file changes `U_REGISTRY` and must fail closed until a separately reviewed/Human-authorized registry update exists.

Mandatory invariant:

```text
AUTHORITY IS REGISTRY-GRANTED, NOT SELF-ASSERTED
```

## 9. Current bootstrap contract

The mandatory current recovery route remains exactly:

```text
1. README.md
2. PROJECT_STATE.md
3. HANDOFF.md
4. verify internal agreement
5. current-state recovery complete
6. STOP before consequential work
7. load only task-relevant supporting provenance
```

The trio must publish equivalent current X1B fields:

```text
X1B_RESEARCH_CLOSURE: CLOSED
X1B_ACTIVE_PRODUCT_REMEDIATION_ASSERTION: CURRENTNESS_UNESTABLISHED
X1B_ACTIVE_PRODUCT_ASSERTION_AUTHORITY: EXTERNAL_CURRENTNESS_REBIND_REQUIRED
X1B_ACTIVE_PRODUCT_ASSERTION_EVIDENCE: NONE_ACCEPTED_FOR_THIS_STATUS_PUBLICATION
X1B_REVIEWED_REMEDIATION_PROVENANCE: PR #35 / REVIEWED HEAD 7c40a92165714023743e91c63b5b11b102fadd92
X1B_CURRENT_AUTHORITY_BOOTSTRAP: README.md -> PROJECT_STATE.md -> HANDOFF.md
X1B_AUTHORITY_MODEL: TWO_LAYER_CLOSED_WORLD_V1
```

If the trio disagrees, fail closed.

## 10. Frozen future implementation surface

A future implementation candidate may change exactly these twelve ScriptOps paths:

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

The candidate, if later separately authorized, must be exactly one commit on top of:

```text
2f22843ac570498b506101addeba5453ab777f08
```

No other ScriptOps path may change.

In particular, this plan does not authorize editing:

```text
CODEX_START.md
IDEA_ARCHIVE.md
sources/prototype/RESTORE.md
phase6/*
legacy/*
tests/*
.github/workflows/*
scripts/restore_v2.py
evidence/*
acceptance/*
analysis/*
continuity/*
```

## 11. Bound baseline blobs for the twelve-path surface

```text
README.md = c52f515dd3d736c749eca75cf319b514f8427c5a
PROJECT_STATE.md = dea1d11c847765026f8766fa70aa111c3f77c7bd
HANDOFF.md = 2e0c3be2a9bdebfeac161773ca9631f8312f42f6
DECISION_LOG.md = b2fd2ae4224d4d33a47d0c8ba198bff3777750f5
SOURCE_MANIFEST.md = 2acf2ece298bfcf89254087c9e747fcb808ab241
SOURCES.md = 28c3f6d8fa9142b41721c8835f211f52cc3fa8bf
SOURCE_AUDIT_SUMMARY.md = 55180fd64b2e64f0a5efc9608be6371fe17d2b86
RECONSTRUCTION_REPORT.md = 383354c61c707ed4a1210f60f03125fca4daae8a
sources/Decision_Summary_Current_State.md = 9aea3d7e8de5dde8025278adca0546324d21dd00
sources/RC1_SCOPE_LOCK.md = 0851bc0a26d90338a18d219bf76b022f1cc4668d
sources/ScriptOps_Main_Theme_Summary.md = 08e88855810d7f8ff913b375ba82c1f2c402d56f
scripts/verify_repository.py = a61278086b92824d7e442b390c951e918c88517b
```

Any baseline mismatch before implementation starts requires STOP and Human rebind.

## 12. Required registry classification of the 13 members

The verifier must freeze one exact mapping equivalent to:

```text
README.md -> CURRENT_BOOTSTRAP_AUTHORITY
PROJECT_STATE.md -> CURRENT_BOOTSTRAP_AUTHORITY
HANDOFF.md -> CURRENT_BOOTSTRAP_AUTHORITY

DECISION_LOG.md -> DECISION_PROVENANCE_ONLY
RECONSTRUCTION_REPORT.md -> HISTORICAL_RECONSTRUCTION_PROVENANCE_ONLY
SOURCES.md -> HISTORICAL_RECONSTRUCTION_PROVENANCE_ONLY
SOURCE_AUDIT_SUMMARY.md -> HISTORICAL_RECONSTRUCTION_PROVENANCE_ONLY
SOURCE_MANIFEST.md -> HISTORICAL_RECONSTRUCTION_PROVENANCE_ONLY
sources/Decision_Summary_Current_State.md -> HISTORICAL_PRODUCT_GOVERNANCE_PROVENANCE_ONLY
sources/RC1_SCOPE_LOCK.md -> HISTORICAL_PRODUCT_GOVERNANCE_PROVENANCE_ONLY
sources/ScriptOps_Main_Theme_Summary.md -> HISTORICAL_PRODUCT_GOVERNANCE_PROVENANCE_ONLY
CODEX_START.md -> PRE_FENCED_NONAUTHORITY_PROVENANCE
IDEA_ARCHIVE.md -> PRE_FENCED_NONAUTHORITY_PROVENANCE
```

Exactly 13 keys. Exactly one class per key.

## 13. Required document corrections

### README.md

Must become the explicit recovery router and state:

```text
current bootstrap = README -> PROJECT_STATE -> HANDOFF
supporting provenance cannot override the trio
Layer-A registry and Layer-B path denial are distinct
CURRENTNESS_UNESTABLISHED != YES/NO
legacy approve --why != sufficient X1B HumanDecision evidence
PR #35 reviewed candidate != active-product proof
green verification != deployment
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
```

### PROJECT_STATE.md

Must remain current status owner while distinguishing:

```text
content semantic acceptance
decision provenance
X1B HumanDecision authorship evidence
active-product remediation assertion
current next-action authority
```

Historical `human decision with why` / `approve --why` semantics must be fenced as non-X1B authorship evidence.

### HANDOFF.md

Must expose the same status schema, same three-file bootstrap and same two-layer authority model.

It must not direct a consequential X1B-authorship effect through legacy approval semantics.

### DECISION_LOG.md

Must gain an explicit top-level `DECISION_PROVENANCE_ONLY` fence.

`ACTIVE` decision status remains decision-lifecycle provenance and must not mean active-product state.

### SOURCE_MANIFEST.md

Must be fenced as historical/reconstruction provenance only. Old `canonical operational sources` wording must not grant current authority.

### SOURCES.md

Must be fenced as historical/reconstruction provenance only and close the accepted PLAN-F004 path:

```text
SOURCE_MANIFEST canonical label != current X1B authority
Decision_Summary_Current_State filename != current X1B authority
historical ACCESS CHECK gap != current next action
```

### SOURCE_AUDIT_SUMMARY.md

Must remain audit provenance. `canonical conclusions`, `strongest decisions`, or similar wording must be scoped as historical audit description, not current X1B authority.

### RECONSTRUCTION_REPORT.md

Must be historical reconstruction provenance only. Historical next-step and generic Human-decision language must be fenced.

### sources/Decision_Summary_Current_State.md

Path name remains provenance-compatible but content must not self-present as current authority.

Generic Human approval governance must be explicitly distinct from X1B HumanDecision authorship evidence.

### sources/RC1_SCOPE_LOCK.md

`Scope Lock` remains historical product-scope provenance and cannot establish current remediation, deployment, HumanDecision admission or V1 authority.

### sources/ScriptOps_Main_Theme_Summary.md

`Core product law` and generic Human approval remain historical product-vision provenance only.

### scripts/verify_repository.py

Must implement the exact Layer-A/Layer-B model in this plan and no alternative census semantics.

## 14. Required verifier functions

A future candidate must add deterministic offline logic equivalent to:

```text
enumerate_registry_surface()
classify_registry_member(path)
classify_nonregistry_markdown_path(path)
check_x1b_two_layer_authority_model()
```

The verifier must remain network-free.

It must not infer remote `main`, deployment, release or active-product currentness from its checkout.

## 15. Layer-A exactness requirements

The verifier must prove:

```text
actual U_REGISTRY == frozen 13-path set
len(actual U_REGISTRY) == 13
len(registry mapping) == 13
set(registry keys) == actual U_REGISTRY
exactly 3 registry members == CURRENT_BOOTSTRAP_AUTHORITY
```

Any new root `.md` or direct `sources/*.md` file fails closed.

No nested path may affect this count.

## 16. Layer-B exactness requirements

The verifier must recursively enumerate Markdown outside `U_REGISTRY` only for path-class validation.

For each such file:

```text
known deny-by-path prefix -> allowed as non-current authority
unknown prefix/location -> FAIL UNCLASSIFIED_MARKDOWN_LOCATION
```

This recursive walk is not the Layer-A registry census.

The verifier output must use distinct names/counts, for example:

```text
registry_surface_count = 13
path_classed_markdown_count = N
```

It must never print or imply that their sum is the registry cardinality.

## 17. Pre-fenced sentinel checks

The following remain unchanged but must retain their relevant fences:

```text
CODEX_START.md
BLOB baseline = 5f28888f98a245503fcfc28548133e9ef4b44961
required meaning = HISTORICAL / SUPERSEDED / NOT CURRENT ROUTE

IDEA_ARCHIVE.md
BLOB baseline = c7cde73b821e197b9fcf2f51105d466ab308e2f6
required meaning = preserved ideas are not implementation authority

sources/prototype/RESTORE.md
BLOB baseline = 8a79aca4c93b23c4842792bea9ecaae146e1fc48
required meaning = historical prototype reconstruction context
```

These sentinel checks do not change Layer-A cardinality.

## 18. Runtime-class separation

Local runtime classification may remain:

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

Neither recognized local class establishes remote active-product state.

## 19. Deterministic synthetic rejection cases

A future candidate must demonstrate at least:

```text
R1  add new root CURRENT_STATUS.md -> FAIL Layer A unknown registry member
R2  add new direct sources/CurrentFoo.md -> FAIL Layer A unknown registry member
R3  duplicate registry class for one Layer-A path -> FAIL
R4  omit registry class for one Layer-A path -> FAIL
R5  classify four Layer-A files as current bootstrap -> FAIL
R6  recursively add sources/prototype/RESTORE.md to Layer-A census -> FAIL
R7  special-case append RESTORE.md to Layer-A census -> FAIL
R8  report Layer-A cardinality as 14 -> FAIL
R9  add nested sources/prototype/extra.md -> Layer-A remains 13; path class denies current authority
R10 add nested docs/Current.md outside known prefixes -> FAIL UNCLASSIFIED_MARKDOWN_LOCATION
R11 SOURCES drops non-current fence -> FAIL
R12 SOURCES restores ACCESS CHECK as current next action -> FAIL
R13 DECISION_LOG ACTIVE is mapped to active-product state -> FAIL
R14 Main_Theme generic Human approval becomes X1B authorship authority -> FAIL
R15 RC1_SCOPE_LOCK becomes current remediation/deployment authority -> FAIL
R16 SOURCE_AUDIT_SUMMARY loses provenance fence -> FAIL
R17 current trio disagrees -> FAIL
R18 current assertion becomes CONFIRMED_NOT_REMEDIATED -> FAIL
R19 current assertion becomes CONFIRMED_REMEDIATED -> FAIL
R20 current assertion becomes YES/NO or TRUE/FALSE -> FAIL
R21 recognized V2 checkout promotes current state -> FAIL
R22 recognized legacy checkout promotes confirmed-not-remediated -> FAIL
R23 UNKNOWN runtime class -> FAIL
R24 supporting document publishes merge/deploy/release/V1 authority -> FAIL
```

Negative tests must use pure helpers or ephemeral copies only.

## 20. Required positive cases

```text
P1 exact twelve-path candidate on frozen baseline -> PASS
P2 Layer-A enumeration returns exactly the frozen 13 paths -> PASS
P3 all 13 Layer-A members have exactly one registry class -> PASS
P4 exactly README/PROJECT_STATE/HANDOFF are current bootstrap authority -> PASS
P5 RESTORE.md is excluded from Layer A and accepted only through sources/prototype/ path class -> PASS
P6 CODEX_START and IDEA_ARCHIVE retain baseline non-authority meaning -> PASS
P7 recognized legacy checkout + CURRENTNESS_UNESTABLISHED -> PASS
P8 synthetic recognized V2 checkout + CURRENTNESS_UNESTABLISHED -> PASS
P9 path-classed provenance remains readable but denied current authority -> PASS
P10 existing repository verification passes after bounded changes -> PASS
P11 existing Phase-6 tests pass without modification -> PASS
```

## 21. Exact future candidate acceptance checks

All must hold:

```text
C1  base exactly 2f22843ac570498b506101addeba5453ab777f08
C2  exactly one commit ahead
C3  changed paths exactly the twelve paths in section 10
C4  all non-listed ScriptOps paths unchanged
C5  phase6/scriptops-v2-hardening.py unchanged at baseline blob
C6  legacy/scriptops-v2-single.py unchanged
C7  scripts/restore_v2.py unchanged
C8  tests/* unchanged
C9  .github/workflows/* unchanged
C10 evidence/* unchanged
C11 Layer-A enumeration algorithm exactly root *.md + direct sources/*.md, non-recursive
C12 Layer-A frozen set exactly the 13 paths in section 5
C13 Layer-A cardinality exactly 13
C14 registry mapping keys exactly equal Layer-A set
C15 every Layer-A member has exactly one registry class
C16 exactly three Layer-A members are CURRENT_BOOTSTRAP_AUTHORITY
C17 RESTORE.md is not a Layer-A member
C18 RESTORE.md is classified only via Layer-B sources/prototype/ path class
C19 recursive Layer-B validation does not alter Layer-A count
C20 unknown nested Markdown location outside allowed prefixes fails closed
C21 current trio agrees on complete X1B schema
C22 active-product assertion exactly CURRENTNESS_UNESTABLISHED
C23 authority model exactly TWO_LAYER_CLOSED_WORLD_V1
C24 DECISION_LOG is decision-provenance-only
C25 SOURCES is reconstruction-provenance-only and no longer reasserts stale current/canonical/ACCESS-CHECK authority
C26 SOURCE_MANIFEST is provenance-only
C27 SOURCE_AUDIT_SUMMARY is provenance-only
C28 RECONSTRUCTION_REPORT is provenance-only
C29 Decision_Summary is product-governance provenance only
C30 RC1_SCOPE_LOCK is product-governance provenance only
C31 Main_Theme is product-vision/governance provenance only
C32 generic Human approval / approve --why / active decision provenance remain distinct from X1B HumanDecision authorship evidence
C33 CODEX_START baseline not-current marker remains
C34 IDEA_ARCHIVE baseline no-implementation-authority marker remains
C35 RESTORE baseline historical-prototype marker remains
C36 verifier is offline and performs no remote-ref inference
C37 recognized legacy checkout accepted only as CURRENTNESS_UNESTABLISHED
C38 recognized V2 checkout accepted only as CURRENTNESS_UNESTABLISHED
C39 UNKNOWN runtime class rejected
C40 R1-R24 demonstrated fail closed
C41 existing repository verification passes
C42 existing Phase-6 tests pass without modification
C43 remote FJ899/scriptops refs/heads/main remains 2f22843ac570498b506101addeba5453ab777f08 throughout candidate preparation/review
```

If any check cannot be satisfied inside the exact twelve-path implementation surface, STOP and record a plan defect.

## 22. PR #35 overlap hazard

PR #35 overlaps multiple future frame/status correction paths.

If a future frame/status correction is separately authorized, reviewed, accepted and merged first:

```text
PR #35 MUST NOT THEN BE MERGED AS-IS
```

Any later X1B V2 integration must produce a fresh reviewed candidate based on then-current default branch or an equivalently reviewed integration preserving both runtime/security properties and this authority model.

This plan grants no PR #35 rebase/merge/replacement authority.

## 23. Future active-product confirmation remains separate

Neither confirmed active-product state may be published under this plan.

Any future promotion requires separately:

```text
1. external read-only resolution of actual FJ899/scriptops refs/heads/main
2. binding that commit to runtime identity/class
3. durable currentness evidence
4. separate Human acceptance
5. status-only promotion candidate
6. independent verification that publication still matches the active runtime identity
```

No such procedure is authorized here.

## 24. Independent review requirements

A future independent read-only review of this exact plan must attack at least:

```text
Q1  is Layer-A enumeration exactly executable and exactly 13 on the frozen baseline?
Q2  can any nested file change Layer-A cardinality through recursion or special casing?
Q3  can a nested Markdown file outside allowed path prefixes evade fail-closed classification?
Q4  can a path-classed file self-promote despite registry/path denial?
Q5  can a new root/direct-sources Markdown file avoid registry failure?
Q6  can DECISION_LOG ACTIVE or canonical wording become current X1B authority?
Q7  can Main_Theme generic Human approval become X1B HumanDecision authority?
Q8  can RC1_SCOPE_LOCK become current remediation/deployment authority?
Q9  does SOURCES fully close PLAN-F004?
Q10 can CURRENTNESS_UNESTABLISHED collapse into ontic NO/YES?
Q11 can a PR-local V2 checkout establish active-product remediation?
Q12 can PR #35 later overwrite the frame boundary without a new reviewed candidate?
Q13 does any wording create merge/deployment/release/tag/V1 authority?
Q14 can disagreement inside the trio pass?
Q15 does the exact twelve-path implementation surface remain bounded to docs/verifier only?
```

Review rule:

```text
FIRST CREDIBLE COUNTEREXAMPLE = DURABLE FINDING + STOP
```

No repair may occur inside that review.

## 25. Authority boundary and exit state

```text
X1B = CLOSED AT ACCEPTED RESEARCH/CORRECTIVE SCOPE
X1B-FRAME-F001 = HUMAN ACCEPTED / OPEN FOR CORRECTION
X1B-FRAME-F001-PLAN-F001 = HUMAN ACCEPTED
X1B-FRAME-F001-PLAN-F002 = HUMAN ACCEPTED
X1B-FRAME-F001-PLAN-F003 = HUMAN ACCEPTED
X1B-FRAME-F001-PLAN-F004 = HUMAN ACCEPTED
X1B-FRAME-F001-PLAN-F005 = HUMAN ACCEPTED
PR #198 = SUPERSEDED / HISTORICAL NOT PASS
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

That review requires separate Human authorization.

Preserve:

```text
AI PROPOSES != HUMAN DECIDES
PLAN PREPARATION AUTHORITY != PLAN REVIEW AUTHORITY
PLAN REVIEW PASS != IMPLEMENTATION AUTHORITY
REGISTRY CENSUS != PATH-CLASS SENTINEL SET
CLOSED WORLD != TWO DIFFERENT CENSUS UNIVERSES
AUTHORITY IS REGISTRY-GRANTED, NOT SELF-ASSERTED
CURRENTNESS_UNESTABLISHED != FALSE
CURRENTNESS_UNESTABLISHED != TRUE
CHECKED_OUT_RUNTIME_CLASS != ACTIVE_PRODUCT_STATE
PR HEAD != ACTIVE DEFAULT BRANCH
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
```
