# X1B-FRAME PR #37 implementation re-review — F013

Date: 2026-09-05

Status: `FIRST CREDIBLE COUNTEREXAMPLE / STOP`

## Exact review authority

```text
FJ899/8 PR #224
HUMAN RESPONSE = accept
REVIEW TYPE = ONE INDEPENDENT READ-ONLY RE-REVIEW
```

## Exact target

```text
REPO = FJ899/scriptops
PR = #37
BASE = 2f22843ac570498b506101addeba5453ab777f08
HEAD = 115fb74607438c7237c33f413981678de4a55b01
TREE = 3d1a1e778672fc9547ec4563cf8e03055061d2a3
STATE = OPEN / DRAFT / UNMERGED
COMMITS OVER BASE = 1
CHANGED PATHS = 12
```

Frozen plan:

```text
FJ899/8 PR #201
HEAD = 5037240043ff36bbcfe50b8daa47df79ef0fcb06
```

Review order authorized by PR #224 begins with F012.

## Finding

```text
FINDING = X1B-FRAME-F001-IMPLEMENTATION-F013
CLASS = LAYER-B SELF-PROMOTION / NEGATION-SCOPE BYPASS
SHORT = COMMA/ASYNDETIC CLAUSE BOUNDARY LETS AN EARLIER NEGATION MASK A LATER POSITIVE AUTHORITY CLAIM
```

The F012 repair no longer skips an entire clause merely because it contains a recognized negative phrase. Instead it checks promotion positions and tries to scope negation locally.

However, the local scope boundary is still lexical rather than semantic:

```text
LAYER_B_CONJUNCTION_BOUNDARIES = AND / OR / BUT / HOWEVER / YET
_authority_clauses() splits on ; . ! ? and BUT/HOWEVER/YET
_normalized_authority_line() removes comma punctuation
```

A comma-separated or asyndetic second independent clause therefore remains inside the same negation segment.

Credible counterexample:

```text
This document does not grant release authority, it hereby authorizes merge.
```

After normalization, the relevant token stream is effectively:

```text
THIS DOCUMENT DOES NOT GRANT RELEASE AUTHORITY IT HEREBY AUTHORIZES MERGE
```

Promotion positions include `GRANT`, `AUTHORITY`, and `AUTHORIZES`.

For the later positive `AUTHORIZES`, `_promotion_locally_noncurrent()` scans backward only to a configured conjunction boundary. There is no configured boundary between the comma-separated independent clauses, because the comma was removed during normalization. Its prefix therefore still contains the earlier token `NOT` and the positive promotion is classified as locally non-current.

The same is true for all detected promotion positions in the line, so `_all_promotions_locally_noncurrent()` returns true and `layer_b_self_promotion_claim()` accepts the line instead of returning the positive self-promotion claim.

This violates the frozen Q4/F009 invariant and the F012 repair objective:

```text
AUTHORITY IS REGISTRY-GRANTED, NOT SELF-ASSERTED
A VALID NEGATIVE AUTHORITY PHRASE MUST NOT MASK A DISTINCT POSITIVE LAYER-B SELF-PROMOTION
```

The counterexample does not rely on changing path classes, registry membership, runtime state, remote refs, or any consequential effect. It is a direct semantic false negative in the current verifier.

## Re-review disposition

```text
F012 = NOT CLOSED
F013 = FIRST CREDIBLE COUNTEREXAMPLE
```

Per frozen review rule:

```text
FIRST CREDIBLE COUNTEREXAMPLE = DURABLE FINDING + STOP
```

Therefore the review did not continue to:

```text
F011
F010
F009
F008
F007
F006
Q5-Q15
```

## Authority boundary

No repair is authorized by this finding.

No merge, ScriptOps main movement, PR #35 integration/rebase/cherry-pick/merge, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority is granted.

```text
AI PROPOSES != HUMAN DECIDES
IMPLEMENTATION REVIEW != REPAIR AUTHORITY
IMPLEMENTATION REVIEW != MERGE AUTHORITY
PR HEAD != ACTIVE DEFAULT BRANCH
```
