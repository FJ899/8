# X1B-FRAME F001 — ScriptOps PR #37 Independent Implementation Re-review Finding F007

Status: `INDEPENDENT READ-ONLY IMPLEMENTATION RE-REVIEW = FAIL / FIRST CREDIBLE COUNTEREXAMPLE = STOP`

Date: `2026-09-05`

## 1. Exact Human-authorized review target

```text
FJ899/scriptops PR #37
BASE = 2f22843ac570498b506101addeba5453ab777f08
HEAD = 0cb507e1e26ad6a9e13c8098c522301d3e0cf0e6
TREE = b17d5d4addcc193f4e963ea5a9c7064a6b0af870
STATE = OPEN / DRAFT / UNMERGED
```

Human re-review authority is durably recorded in:

```text
FJ899/8 PR #208
HEAD = bcacbd7834a2e6d13e01d5528b57cd45cf2a9d52
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

Prior implementation finding / repair authority:

```text
PR #206 = X1B-FRAME-F001-IMPLEMENTATION-F006
PR #207 = Human-bounded F006 repair authority
```

No repair or ScriptOps mutation is authorized by this re-review.

## 2. F006-first result

The literal F006 mechanism is corrected for the exact reviewed PR #35 V2 profile:

- the unconditional `runtime_class != LEGACY_PRE_X1B` rejection is gone;
- the real repository path now calls `validate_runtime_profile(...)`;
- both `LEGACY_PRE_X1B` and the exact frozen PR #35 `X1B_V2_CHECKOUT` profile are admitted only with `CURRENTNESS_UNESTABLISHED`;
- `UNKNOWN` and mixed profiles fail closed.

Therefore the re-review continued to the remaining frozen implementation attacks.

This statement is not a PASS for PR #37 as a whole.

## 3. First credible counterexample

```text
X1B-FRAME-F001-IMPLEMENTATION-F007

R12 IS A FALSE-NEGATIVE TEST:
SOURCES.md CAN RETAIN THE REQUIRED HISTORICAL ACCESS-CHECK FENCE
AND SIMULTANEOUSLY REASSERT "ACCESS CHECK REQUIRED = CURRENT NEXT",
WHILE THE IMPLEMENTED VERIFIER ACCEPTS IT.
```

Primary class:

```text
VERIFIER FALSE NEGATIVE
NEGATIVE-TEST VACUITY / WRONG-REASON FAILURE
```

## 4. Frozen plan requirement

PR #201 section 19 requires:

```text
R12 SOURCES restores ACCESS CHECK as current next action -> FAIL
```

PR #201 section 21 additionally requires:

```text
C25 SOURCES is reconstruction-provenance-only and no longer reasserts stale current/canonical/ACCESS-CHECK authority
C40 R1-R24 demonstrated fail closed
```

This requirement is directly descended from the accepted PLAN-F004 recovery-authority finding: a supporting reconstruction source must not recover stale current-next authority merely by preserving a historical fence elsewhere in the same document.

## 5. Implemented verifier behavior

For `SOURCES.md`, `PROVENANCE_MARKERS` requires these substrings:

```text
HISTORICAL_RECONSTRUCTION_PROVENANCE_ONLY
SOURCE_MANIFEST canonical label != current X1B authority
Decision_Summary_Current_State filename != current X1B authority
historical ACCESS CHECK gap != current next action
```

`validate_provenance_text()` then performs only two checks:

```text
1. every required provenance marker is present;
2. none of POSITIVE_AUTHORITY_MARKERS is present.
```

But `POSITIVE_AUTHORITY_MARKERS` does not include any marker for:

```text
ACCESS CHECK REQUIRED = CURRENT NEXT
```

or an equivalent stale current-next assertion.

## 6. Passing counterexample

Start from the exact PR #37 `SOURCES.md`, which already contains every required provenance marker, and append:

```text
ACCESS CHECK REQUIRED = CURRENT NEXT
```

No other file changes are needed for the counterexample.

The resulting document simultaneously contains:

```text
historical ACCESS CHECK gap != current next action
ACCESS CHECK REQUIRED = CURRENT NEXT
```

Under the implemented verifier:

```text
required marker presence = PASS
POSITIVE_AUTHORITY_MARKERS scan = PASS
Layer-A membership/count = unchanged
bootstrap trio = unchanged
runtime checks = unchanged
```

Therefore `validate_provenance_text("SOURCES.md", ...)` accepts the conflicting current-next assertion.

That violates R12 and C25.

## 7. Why the embedded R12 test does not prove R12

The synthetic R12 case constructs this reduced text:

```text
HISTORICAL_RECONSTRUCTION_PROVENANCE_ONLY
SOURCE_MANIFEST canonical label != current X1B authority
Decision_Summary_Current_State filename != current X1B authority
ACCESS CHECK REQUIRED = CURRENT NEXT
```

Critically, it omits the required marker:

```text
historical ACCESS CHECK gap != current next action
```

So the test fails because a required fence marker is missing, not because stale current-next authority is detected.

A correct adversarial R12 case must preserve all required fences and add the forbidden current-next assertion. The current implementation does not test or reject that case.

Thus:

```text
R12 GREEN != R12 PROPERTY PROVED
```

## 8. Why current candidate text being correct does not close the finding

Exact PR #37 currently writes a correctly fenced `SOURCES.md` and does not itself publish `ACCESS CHECK REQUIRED = CURRENT NEXT`.

However the frozen implementation contract explicitly requires a deterministic fail-closed R12 regression and verifier protection against reintroduction of that stale authority. The implemented verifier allows the forbidden state, and the negative test passes for the wrong reason.

This is therefore an implementation/verifier defect, not a hypothetical documentation style concern.

## 9. Disposition

```text
F006 LITERAL UNCONDITIONAL-LEGACY REJECTION = CORRECTED FOR THE EXACT REVIEWED V2 PROFILE
X1B-FRAME PR #37 IMPLEMENTATION RE-REVIEW = FAIL
X1B-FRAME-F001-IMPLEMENTATION-F007 = OPEN
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

The independent re-review stops here. Remaining acceptance/review attacks are not claimed as completed.

## 10. Narrow repair pressure

A future Human-authorized repair, if any, must ensure that the verifier rejects a `SOURCES.md` which preserves every required historical fence while also asserting stale current-next authority.

At minimum the regression must exercise the exact adversarial shape:

```text
all required SOURCES provenance markers retained
+
ACCESS CHECK REQUIRED = CURRENT NEXT
=> FAIL for current-next authority conflict
```

This paragraph describes the defect boundary only. It does not authorize or select a repair.

Preserve:

```text
AI PROPOSES != HUMAN DECIDES
REVIEW FINDING != REPAIR AUTHORITY
GREEN NEGATIVE TEST != PROPERTY PROOF WHEN FAILURE REASON IS WRONG
CURRENT-LOOKING RECOVERY SOURCE != CURRENT AUTHORITY BY SELF-ASSERTION
IMPLEMENTATION CANDIDATE != MERGE AUTHORITY
```