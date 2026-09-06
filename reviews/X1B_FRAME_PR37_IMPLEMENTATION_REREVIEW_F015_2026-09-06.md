# X1B-FRAME PR #37 — Independent implementation re-review F015

Date: 2026-09-06

Status: `FINDING / STOP`

## 1. Human review authority

This review is the exactly one independent read-only re-review authorized by Human `accept` and durably recorded in:

```text
FJ899/8 PR #230
HEAD = ce65c5b5ce7dba32a538db4c1557b14ee682cf70
```

Authorized review order:

```text
F014 -> F013 -> F012 -> F011 -> F010 -> F009 -> F008 -> F007 -> F006 -> Q5..Q15
FIRST CREDIBLE COUNTEREXAMPLE = DURABLE FINDING + STOP
```

## 2. Exact review target

Repository: `FJ899/scriptops`

Pull request: `#37`

```text
BASE = 2f22843ac570498b506101addeba5453ab777f08
HEAD = 2fab77397cceda52725c86f3c7f4ea071174d5b0
TREE = b18df96e569c1b61065c4389dc143e7bd5db5e16
STATE = OPEN / DRAFT / UNMERGED
COMMITS = 1
BASE-RELATIVE CHANGED PATHS = 12
```

Current verifier target:

```text
PATH = scripts/verify_repository.py
BLOB = dca3d338b2d6ee32d5fb4ee87f186ac850d0b7c1
```

The candidate remains bound to superseding plan `FJ899/8 PR #201` and plan-review PASS `FJ899/8 PR #202`.

## 3. Re-attack started at F014

F014 had found that the prior parser allowed a positive Layer-B self-promotion after a non-comma clause boundary to inherit earlier negation. The bounded F014 repair added explicit splitting for colon and whitespace-surrounded em dash, en dash, and double hyphen, while retaining comma/semicolon/sentence punctuation handling.

Current `_authority_clauses()` uses:

```python
re.split(
    r"[,;:.!?]+|\s+(?:—|–|--)\s+|\b(?:BUT|HOWEVER|YET)\b",
    raw_line.upper(),
)
```

Current `_normalized_authority_line()` separately replaces, among other characters:

```text
( ) [ ] { } / \
```

with spaces.

Therefore those delimiters are normalized away without becoming clause boundaries.

## 4. Credible counterexample

Use a Layer-B document containing:

```text
This document does not authorize merge (this file grants canonical X1B authority).
```

Semantics:

```text
CLAUSE 1 = This document does not authorize merge
CLAUSE 2 = this file grants canonical X1B authority
```

The second clause is an explicit positive self-promotion and must be rejected under the Layer-B non-authority requirement.

Observed verifier logic on the exact current implementation:

1. `_authority_clauses()` does not split at `(` or `)`.
2. `_normalized_authority_line()` removes the parentheses.
3. The resulting single normalized token sequence is equivalent to:

```text
THIS DOCUMENT DOES NOT AUTHORIZE MERGE THIS FILE GRANTS CANONICAL X1B AUTHORITY
```

4. For the later `GRANTS`, `CANONICAL X1B`, and `AUTHORITY` promotion positions, `_promotion_locally_noncurrent()` searches backward to the start of the same unsplit segment.
5. The prefix still contains `NOT` from the first assertion.
6. `_all_promotions_locally_noncurrent()` therefore treats the later positive self-promotion as locally non-current.
7. `layer_b_self_promotion_claim()` returns no claim for the line, so the Layer-B validator accepts the text.

Equivalent non-enumerated separator classes such as square brackets or slash separation have the same structural risk because they are normalized away rather than used as clause boundaries. One counterexample is sufficient for STOP.

## 5. Finding

```text
X1B-FRAME-F001-IMPLEMENTATION-F015 — F014 REMAINS DELIMITER-ENUMERATION INCOMPLETE: A PARENTHETICAL POSITIVE LAYER-B SELF-PROMOTION CAN INHERIT AN EARLIER NEGATION BECAUSE PARENTHESES ARE NORMALIZED AWAY INSTEAD OF FORMING A CLAUSE BOUNDARY.
```

Classification:

```text
F014 REPAIR INCOMPLETE / NEGATION-SCOPE DELIMITER BYPASS / FALSE NEGATIVE
```

This is not a failure of the newly added colon/em-dash examples themselves. It is a structural continuation of the same negation-scope problem: semantic clause separation still depends on an enumerated delimiter list, while other punctuation separators are erased before authority-locality evaluation.

## 6. Disposition

```text
F014 = NOT VERIFIED CLOSED
F015 = OPEN FINDING
REVIEW = STOP
```

Per the frozen review rule, no further ordered work was executed after this first credible counterexample:

```text
F013 = NOT RE-REVIEWED IN THIS RUN
F012 = NOT RE-REVIEWED IN THIS RUN
F011 = NOT RE-REVIEWED IN THIS RUN
F010 = NOT RE-REVIEWED IN THIS RUN
F009 = NOT RE-REVIEWED IN THIS RUN
F008 = NOT RE-REVIEWED IN THIS RUN
F007 = NOT RE-REVIEWED IN THIS RUN
F006 = NOT RE-REVIEWED IN THIS RUN
Q5-Q15 = NOT EXECUTED IN THIS RUN
```

No repair is authorized by this finding or by PR #230.

No ScriptOps mutation, merge, default-branch movement, PR #35 integration, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority occurs.

`FIRST CREDIBLE COUNTEREXAMPLE = DURABLE FINDING + STOP`

`REVIEW FINDING != REPAIR AUTHORITY`

`AI PROPOSES != HUMAN DECIDES`
