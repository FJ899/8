# X1B-FRAME PR #37 — Independent implementation re-review F014

Status: `NOT PASS / FIRST CREDIBLE COUNTEREXAMPLE / STOP`

Date: `2026-09-05`

## Exact review target

```text
FJ899/scriptops PR #37
BASE = 2f22843ac570498b506101addeba5453ab777f08
HEAD = d47b7525f3bcd8f36b1242d905ee60bef2a0514e
TREE = 4364cc9f787bcfcb9b9d9e3452ed407d66625a7f
STATE = OPEN / DRAFT / UNMERGED
COMMITS AHEAD = 1
CHANGED PATHS = 12
```

Human read-only review authority:

```text
FJ899/8 PR #227
HEAD = 99e309719c10b89f12e8e59d178d3252e5c233cd
```

Frozen plan/review authority:

```text
FJ899/8 PR #201 = superseding two-layer census plan
FJ899/8 PR #202 = plan-review PASS
```

Prior accepted review chain includes F006-F013. The mandated review order for this run began with F013.

## F013 re-attack

The F013 repair changes `_authority_clauses()` so comma-separated clauses reset local negation scope:

```python
parts = re.split(r"[,;.!?]+|\b(?:BUT|HOWEVER|YET)\b", raw_line.upper())
```

However, the segmentation grammar is still punctuation-specific and incomplete. It does not split other ordinary clause boundaries such as an em dash or colon.

At the same time, `_normalized_authority_line()` removes colon and slash characters before token analysis, and `_promotion_locally_noncurrent()` scans backward to the start of the current segment (or a listed conjunction boundary) and treats any earlier `NOT`, `NO`, or `CANNOT` as negating the later promotion.

Therefore a Layer-B document under an allowed prefix can contain for example:

```text
This document does not authorize merge — this file grants canonical X1B authority.
```

or equivalently:

```text
This document does not authorize merge: this file grants canonical X1B authority.
```

The first negative assertion and the later positive self-promotion remain in one verifier segment. The earlier `NOT` is therefore applied to the later `grants` / `authority` promotion positions, `_all_promotions_locally_noncurrent()` returns true, and `layer_b_self_promotion_claim()` returns no claim instead of rejecting the positive self-promotion.

This is the same authority-semantics class as F012/F013 but through a different, ordinary clause boundary not covered by the F013 repair.

## Finding

```text
FINDING = X1B-FRAME-F001-IMPLEMENTATION-F014
CLASS = NEGATION-SCOPE PUNCTUATION BYPASS / NON-COMMA CLAUSE-BOUNDARY FALSE NEGATIVE
```

Finding statement:

```text
F014 — THE F013 COMMA/ASYNDESIS REPAIR STILL BINDS NEGATION TO A FIXED LIST OF CLAUSE DELIMITERS. A LAYER-B DOCUMENT CAN PLACE A GENUINE NEGATIVE AUTHORITY STATEMENT BEFORE AN EM-DASH OR COLON AND THEN ASSERT POSITIVE SELF-AUTHORITY AFTER THAT BOUNDARY; THE VERIFIER KEEPS BOTH IN ONE NEGATION SEGMENT AND ACCEPTS THE LATER SELF-PROMOTION.
```

## Review disposition

```text
F013 = NOT CLOSED; RE-ATTACK PRODUCED F014
F012 = NOT RE-REVIEWED AFTER F014
F011 = NOT RE-REVIEWED AFTER F014
F010 = NOT RE-REVIEWED AFTER F014
F009 = NOT RE-REVIEWED AFTER F014
F008 = NOT RE-REVIEWED AFTER F014
F007 = NOT RE-REVIEWED AFTER F014
F006 = NOT RE-REVIEWED AFTER F014
Q5-Q15 = NOT EXECUTED
```

Per the frozen review rule:

```text
FIRST CREDIBLE COUNTEREXAMPLE = DURABLE FINDING + STOP
```

No repair was performed in this review.

No merge, ScriptOps main movement, PR #35 integration, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority is created by this finding.

Preserve:

```text
AI PROPOSES != HUMAN DECIDES
AUTHORITY IS REGISTRY-GRANTED, NOT SELF-ASSERTED
IMPLEMENTATION CANDIDATE != MERGE AUTHORITY
PR HEAD != ACTIVE DEFAULT BRANCH
CURRENTNESS_UNESTABLISHED != FALSE
CURRENTNESS_UNESTABLISHED != TRUE
```
