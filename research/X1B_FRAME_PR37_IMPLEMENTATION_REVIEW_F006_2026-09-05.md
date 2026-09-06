# X1B-FRAME F001 — ScriptOps PR #37 Independent Implementation Review Finding F006

Status: `INDEPENDENT READ-ONLY IMPLEMENTATION REVIEW = FAIL / FIRST CREDIBLE COUNTEREXAMPLE = STOP`

Date: `2026-09-05`

## 1. Exact Human-authorized review target

```text
FJ899/scriptops PR #37
BASE = 2f22843ac570498b506101addeba5453ab777f08
HEAD = ac061227fada7995490675f5413bce3d44ef516a
TREE = 732a8cc084f4c5a527d9ae00800bf644b85c932f
STATE = OPEN / DRAFT / UNMERGED
```

Human review authority is durably recorded in:

```text
FJ899/8 PR #205
HEAD = 2b5573e9277cfe148e3e9b5ec073fcf7dd7c35f4
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

No repair or ScriptOps mutation is authorized by this review.

## 2. Finding

```text
X1B-FRAME-F001-IMPLEMENTATION-F006

REAL V2 CHECKOUT IS REJECTED BY THE IMPLEMENTED VERIFIER
DESPITE THE FROZEN PLAN REQUIRING
X1B_V2_CHECKOUT + CURRENTNESS_UNESTABLISHED = PASS
```

Primary class:

```text
VERIFIER / TRANSITION-STATE CONTRADICTION
```

## 3. Frozen plan requirement

PR #201 section 18 requires:

```text
LEGACY_PRE_X1B + CURRENTNESS_UNESTABLISHED = PASS
X1B_V2_CHECKOUT + CURRENTNESS_UNESTABLISHED = PASS
UNKNOWN + CURRENTNESS_UNESTABLISHED = FAIL
```

PR #201 section 20 also requires:

```text
P8 synthetic recognized V2 checkout + CURRENTNESS_UNESTABLISHED -> PASS
```

and section 21 requires:

```text
C38 recognized V2 checkout accepted only as CURRENTNESS_UNESTABLISHED
```

The point of this requirement is that the frame/status correction remains valid across a future reviewed V2 runtime integration while active-product currentness still remains epistemically unestablished.

## 4. Implemented verifier behavior

In exact PR #37 `scripts/verify_repository.py`, helper logic initially appears to allow both recognized classes:

```python
def validate_runtime_currentness(runtime_class: str, assertion: str) -> None:
    if assertion != "CURRENTNESS_UNESTABLISHED":
        raise VerificationError("local runtime class may not promote active-product state")
    if runtime_class not in {"LEGACY_PRE_X1B", "X1B_V2_CHECKOUT"}:
        raise VerificationError(f"unknown local runtime class: {runtime_class}")
```

But the actual repository verification path then adds this unconditional requirement:

```python
def check_runtime_separation() -> None:
    hardening = read_text("phase6/scriptops-v2-hardening.py")
    runtime_class = classify_runtime_text(hardening)
    validate_runtime_currentness(
        runtime_class,
        EXPECTED_FIELDS["X1B_ACTIVE_PRODUCT_REMEDIATION_ASSERTION"],
    )
    if runtime_class != "LEGACY_PRE_X1B":
        raise VerificationError(
            f"frozen implementation baseline expected LEGACY_PRE_X1B, got {runtime_class}"
        )
```

Therefore a real checkout whose runtime is recognized as `X1B_V2_CHECKOUT` is rejected even when the published assertion remains exactly `CURRENTNESS_UNESTABLISHED`.

## 5. Passing counterexample against the frozen implementation contract

Take the exact frame/status correction and later perform the separately reviewed V2 integration contemplated by the plan, without promoting active-product currentness:

```text
runtime class = X1B_V2_CHECKOUT
X1B_ACTIVE_PRODUCT_REMEDIATION_ASSERTION = CURRENTNESS_UNESTABLISHED
```

Under PR #201 this combination must PASS.

Under PR #37:

```text
validate_runtime_currentness(...) = accepts
check_runtime_separation()        = rejects because runtime != LEGACY_PRE_X1B
```

So the implemented verifier makes the future valid transition state impossible without another verifier edit.

That contradicts the frozen cross-transition semantics and C38.

## 6. Why green CI does not close the finding

Current PR #37 CI is green because the actual checked-out runtime is still the frozen legacy baseline:

```text
phase6/scriptops-v2-hardening.py = baseline legacy runtime blob
runtime class = LEGACY_PRE_X1B
```

The green run therefore exercises only the first allowed row of the plan's runtime matrix.

The synthetic matrix in PR #37 confirms that synthetic V2 text is classified as `X1B_V2_CHECKOUT`, and confirms that V2 may not promote to `CONFIRMED_REMEDIATED`; however it does not execute the full `check_runtime_separation()` path with a recognized V2 runtime and `CURRENTNESS_UNESTABLISHED`.

Thus green CI does not prove C38.

## 7. Disposition

```text
X1B-FRAME PR #37 IMPLEMENTATION REVIEW = FAIL
X1B-FRAME-F001-IMPLEMENTATION-F006 = OPEN
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

The independent review stops here. No implementation repair is performed in the same review.

## 8. Narrow repair pressure

A future Human-authorized repair, if any, must preserve both truths simultaneously:

```text
exact PR #37 candidate baseline verification must still recognize the current legacy checkout
AND
recognized X1B_V2_CHECKOUT + CURRENTNESS_UNESTABLISHED must be accepted by the real verifier path
```

The repair must not let either recognized local runtime class promote active-product state, and must continue to reject `UNKNOWN`.

This paragraph describes the defect boundary only. It does not authorize or select a repair.

Preserve:

```text
AI PROPOSES != HUMAN DECIDES
REVIEW FINDING != REPAIR AUTHORITY
GREEN CI != COMPLETE CONTRACT PROOF
CHECKED_OUT_RUNTIME_CLASS != ACTIVE_PRODUCT_STATE
CURRENTNESS_UNESTABLISHED != FALSE
CURRENTNESS_UNESTABLISHED != TRUE
IMPLEMENTATION CANDIDATE != MERGE AUTHORITY
```
