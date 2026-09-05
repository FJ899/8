# X1B-FRAME F001 — ScriptOps PR #37 Independent Implementation Re-review Finding F008

Status: `INDEPENDENT READ-ONLY IMPLEMENTATION RE-REVIEW = FAIL / FIRST CREDIBLE COUNTEREXAMPLE = STOP`

Date: `2026-09-05`

## 1. Exact Human-authorized review target

```text
FJ899/scriptops PR #37
BASE = 2f22843ac570498b506101addeba5453ab777f08
HEAD = a5bc1eb55ef0d3b41814d5ceddaa382f67fa64db
TREE = 544ef3af58393d956569cec1ad6c350ddfb1d3c2
STATE = OPEN / DRAFT / UNMERGED
COMMITS AHEAD = 1
CHANGED PATHS = 12
```

Human re-review authority is durably recorded in:

```text
FJ899/8 PR #211
HEAD = a31ddb14ffea085812b296f04ed5961c801fc334
HUMAN RESPONSE = accept
```

Reviewed plan:

```text
FJ899/8 PR #201
HEAD = 5037240043ff36bbcfe50b8daa47df79ef0fcb06
PATH = research/X1B_FRAME_F001_SUPERSEDING_TWO_LAYER_CENSUS_PLAN_REOPEN_PLAN_F005_2026-09-05.md
BLOB = 73ae15473c37d9b62c3b7479e14556603260e110
PLAN REVIEW PASS = FJ899/8 PR #202
```

Prior implementation findings / repair authorities:

```text
PR #206 = X1B-FRAME-F001-IMPLEMENTATION-F006
PR #207 = Human-bounded F006 repair authority
PR #209 = X1B-FRAME-F001-IMPLEMENTATION-F007
PR #210 = Human-bounded F007 repair authority
```

No repair or ScriptOps mutation is authorized by this re-review.

## 2. F007-first result

The literal F007 mechanism is corrected:

- `SOURCES.md` has a path-specific forbidden stale-current-next marker check for `ACCESS CHECK REQUIRED = CURRENT NEXT`;
- synthetic R12 starts from the real correctly fenced `SOURCES.md` rather than a reduced document;
- the R12 assertion also checks the rejection reason, so a missing-fence failure cannot masquerade as the intended stale-current-next rejection.

Therefore the re-review continued.

## 3. F006 regression result

The prior F006 correction remains present:

- both exact recognized runtime profiles are accepted only with `CURRENTNESS_UNESTABLISHED`;
- the real repository path uses `validate_runtime_profile(...)`;
- mixed / unknown runtime profiles remain fail-closed;
- local runtime class still cannot promote active-product state.

This is not a PASS for PR #37 as a whole.

## 4. First credible counterexample

```text
X1B-FRAME-F001-IMPLEMENTATION-F008

R14 IS A FALSE-NEGATIVE TEST:
MAIN_THEME CAN PRESERVE EVERY REQUIRED NON-AUTHORITY FENCE
AND SIMULTANEOUSLY ASSERT THAT GENERIC HUMAN APPROVAL
IS X1B HumanDecision AUTHORSHIP EVIDENCE,
WHILE THE IMPLEMENTED VERIFIER ACCEPTS IT.
```

Primary class:

```text
VERIFIER FALSE NEGATIVE
NEGATIVE-TEST VACUITY / WRONG-REASON FAILURE
HUMAN-AUTHORSHIP SEMANTIC COLLAPSE
```

## 5. Frozen plan requirement

PR #201 section 13 requires for `sources/ScriptOps_Main_Theme_Summary.md`:

```text
Core product law and generic Human approval remain historical product-vision provenance only.
```

PR #201 section 19 requires:

```text
R14 Main_Theme generic Human approval becomes X1B authorship authority -> FAIL
```

PR #201 section 21 additionally requires:

```text
C31 Main_Theme is product-vision/governance provenance only
C32 generic Human approval / approve --why / active decision provenance remain distinct from X1B HumanDecision authorship evidence
C40 R1-R24 demonstrated fail closed
```

The intended property is therefore not merely that a particular marker exists. The verifier must reject a Main_Theme document that keeps its historical fence while also collapsing generic Human approval into X1B authorship authority.

## 6. Current Main_Theme state

Exact PR #37 currently writes a correctly fenced document containing, among other text:

```text
HISTORICAL_PRODUCT_GOVERNANCE_PROVENANCE_ONLY
PRODUCT VISION / GENERIC HUMAN APPROVAL
!=
X1B HumanDecision AUTHORSHIP EVIDENCE
```

The exact candidate text is currently semantically correct.

That current correctness does not prove the required R14 rejection property.

## 7. Implemented verifier behavior

For `sources/ScriptOps_Main_Theme_Summary.md`, `PROVENANCE_MARKERS` requires only the presence of:

```text
HISTORICAL_PRODUCT_GOVERNANCE_PROVENANCE_ONLY
PRODUCT VISION / GENERIC HUMAN APPROVAL
X1B HumanDecision AUTHORSHIP EVIDENCE
```

`validate_provenance_text()` then:

1. checks required marker presence;
2. checks path-specific forbidden markers, but the only current path-specific entry is for `SOURCES.md` / ACCESS CHECK;
3. scans the generic `POSITIVE_AUTHORITY_MARKERS` list.

That generic list contains active-product booleans and exact merge/deploy/release/V1/current-authority markers, but it does not contain a Human-authorship-collapse marker such as:

```text
GENERIC HUMAN APPROVAL = X1B HumanDecision AUTHORSHIP EVIDENCE
```

or an equivalent assertion.

## 8. Passing counterexample

Start from the exact correctly fenced PR #37 file:

```text
sources/ScriptOps_Main_Theme_Summary.md
```

and append only:

```text
GENERIC HUMAN APPROVAL = X1B HumanDecision AUTHORSHIP EVIDENCE
```

All required Main_Theme provenance markers remain present.

The resulting document now contains both:

```text
PRODUCT VISION / GENERIC HUMAN APPROVAL
!=
X1B HumanDecision AUTHORSHIP EVIDENCE
```

and:

```text
GENERIC HUMAN APPROVAL = X1B HumanDecision AUTHORSHIP EVIDENCE
```

Under the implemented `validate_provenance_text()`:

```text
required provenance-marker presence = PASS
path-specific forbidden-marker scan = PASS
POSITIVE_AUTHORITY_MARKERS scan = PASS
registry class = unchanged
Layer-A cardinality = unchanged
bootstrap trio = unchanged
runtime profile = unchanged
```

Therefore the contradictory authorship-promotion assertion is accepted.

That violates R14, C31 and C32.

## 9. Why the embedded R14 test does not prove R14

The current synthetic R14 case does not start from the real correctly fenced Main_Theme document.

It instead validates only:

```text
HISTORICAL_PRODUCT_GOVERNANCE_PROVENANCE_ONLY
Core product law
```

That reduced text omits required markers including:

```text
PRODUCT VISION / GENERIC HUMAN APPROVAL
X1B HumanDecision AUTHORSHIP EVIDENCE
```

So the test fails because required provenance markers are missing, not because generic Human approval was detected as being promoted into X1B HumanDecision authorship authority.

Unlike repaired R12, R14 does not use the real fenced document and does not assert the intended failure reason.

Thus:

```text
R14 GREEN != R14 PROPERTY PROVED
```

## 10. Why this is within the frozen review scope

This is the same class of wrong-reason negative-test failure already accepted for F007, but on the frozen R14 Human-authorship boundary.

It directly attacks the plan's required separation:

```text
GENERIC HUMAN APPROVAL != X1B HumanDecision AUTHORSHIP EVIDENCE
```

and the plan's deterministic R14 requirement.

No broader new property is being introduced.

## 11. Disposition

```text
F007 LITERAL WRONG-REASON R12 DEFECT = CORRECTED
F006 RUNTIME-PROFILE REGRESSION = PRESERVED
X1B-FRAME PR #37 IMPLEMENTATION RE-REVIEW = FAIL
X1B-FRAME-F001-IMPLEMENTATION-F008 = OPEN
FIRST CREDIBLE COUNTEREXAMPLE = STOP
PR #37 = NOT PASS
PR #37 REPAIR AUTHORITY = NO
PR #37 MERGE AUTHORITY = NO
PR #35 MERGE / REBASE / CHERRY-PICK AUTHORITY = NO
SCRIPTOPS MAIN MOVEMENT = NO
DEPLOYMENT / RELEASE / TAG = NO
CANONICAL EFFECT AUTHORITY = NO
ACTIVE-PRODUCT STATUS PROMOTION = NO
X1B = REMAINS CLOSED AT ACCEPTED RESEARCH/CORRECTIVE SCOPE
V1 AUTHORITY = NO
```

The independent re-review stops here. Remaining frozen attacks after this first credible counterexample are not claimed as completed.

## 12. Narrow repair pressure

A future Human-authorized repair, if any, must make R14 non-vacuous.

At minimum it must exercise the adversarial shape:

```text
real correctly fenced Main_Theme text
+
GENERIC HUMAN APPROVAL = X1B HumanDecision AUTHORSHIP EVIDENCE
=> FAIL specifically because Human-authorship promotion is forbidden
```

A wrong-reason failure caused by deleting required fence markers is not sufficient.

This section describes the defect boundary only. It does not authorize or select a repair.

Preserve:

```text
AI PROPOSES != HUMAN DECIDES
REVIEW FINDING != REPAIR AUTHORITY
GREEN NEGATIVE TEST != PROPERTY PROOF WHEN FAILURE REASON IS WRONG
GENERIC HUMAN APPROVAL != X1B HumanDecision AUTHORSHIP EVIDENCE
IMPLEMENTATION CANDIDATE != MERGE AUTHORITY
```
