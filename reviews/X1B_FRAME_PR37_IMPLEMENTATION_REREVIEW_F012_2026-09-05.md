# X1B-FRAME PR #37 implementation re-review — F012

Date: 2026-09-05

## Authority

Human re-review authority: `FJ899/8 PR #221`.

## Exact target

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `d9dd915cb7e8e66388b191f4a68ade58c301b096`
- TREE: `fa523574e9e87fbc5358d9cba706ce66f8455d43`
- candidate shape: exactly one commit over BASE, exactly twelve base-relative changed paths
- pre-review CI: repository verifier PASS; Phase-6 smoke PASS

## Required review order

F011 -> F010 -> F009 -> F008 -> F007 -> F006 -> remaining frozen PR #201 attacks.

## First credible counterexample

### Finding

`X1B-FRAME-F001-IMPLEMENTATION-F012 — MIXED-CLAUSE NEGATION MASKS POSITIVE LAYER-B SELF-PROMOTION`

Classification: `AUTHORITY-SEMANTICS BYPASS / NEGATION-SCOPE FALSE NEGATIVE`.

The F011 repair adds clause splitting plus local negation handling, but `layer_b_self_promotion_claim()` still performs an earlier whole-clause skip whenever *any* string from `LAYER_B_NEGATING_TERMS` appears in the normalized clause.

`_authority_clauses()` splits on punctuation and `BUT` / `HOWEVER` / `YET`, but does not split an ordinary conjunction such as `AND`.

Therefore a single clause can contain both a legitimate negative statement and a separate positive self-promotion statement. The negative phrase causes the entire clause to be skipped before the positive promotion is evaluated.

Representative counterexample:

```text
THIS DOCUMENT DOES NOT AUTHORIZE DEPLOYMENT AND THIS DOCUMENT GRANTS CURRENT X1B AUTHORITY
```

Why it passes the current production validator:

1. `_authority_clauses()` leaves the sentence as one clause because `AND` is not a split boundary.
2. the normalized clause contains the recognized negating term `DOES NOT AUTHORIZE`;
3. `layer_b_self_promotion_claim()` immediately `continue`s for the whole clause;
4. the later structural/local-negation check is never reached;
5. the sentence does not match the small exact `POSITIVE_AUTHORITY_MARKERS` tuple;
6. `validate_layer_b_non_authority_text()` therefore accepts this positive Layer-B self-promotion.

This defeats the intended F009/F011 semantic boundary: a path-denied Layer-B document can still self-promote by combining one negated authority phrase with one positive authority phrase in the same conjunction clause.

## Disposition

- F011 re-attack: **FAIL — F012 found**.
- F010 and earlier regressions: not re-reviewed after F012 because the frozen first-counterexample rule requires STOP.
- Remaining frozen attacks Q5-Q15: not executed.

## STOP

Per Human authority and frozen review rule, review stops at the first credible counterexample. No repair is authorized or performed here.

No ScriptOps merge, default-branch movement, PR #35 integration, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1 action is authorized or performed.

`AI PROPOSES != HUMAN DECIDES`
`FINDING != REPAIR AUTHORITY`
