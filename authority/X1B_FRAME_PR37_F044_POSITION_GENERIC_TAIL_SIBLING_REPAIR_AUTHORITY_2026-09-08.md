# X1B-FRAME PR #37 F044 position-generic tail-sibling repair authority

Human authorization recorded from the current project session.

## Exact starting implementation candidate

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `f750b6ee5dcb7e55d0815b232220f6559c9df033`
- TREE: `46db54cbc6c0ebeb139f77c818a66e78c0990e5a`
- verifier entrypoint blob: `14a99f1bce97a08c84eb1cee2c1245af93b7fab3`
- current open finding: `FJ899/8 PR #511` / `F044-D40`

## Authorized scope

Bounded position-generic F044 tail-sibling repair, limited to the existing F044 parser boundary / tail-sibling ownership logic.

- implementation + verification only;
- one common position-independent rule;
- D30-D40 are the mandatory regression matrix;
- no merge, main movement, deploy, release, tag, canonical effect, status promotion, X1B reopen or V1.

## Mandatory success conditions

1. No parser/repair logic enumerating sibling positions (`if sibling_position == N` or equivalent positional ladder).
2. D30-D40 all PASS under the common rule.
3. Position-invariance property validation covers out-of-history positions including N=7, N=10 and N=20, preferably a wider generated range.
4. Property generator preserves semantic topology: `SEMANTIC SHAPE = CONSTANT`; only the continuation-bearing sibling position varies.
5. Existing inherited F042/F043/F044 regressions remain GREEN.
6. Root-cause validation PASS is required before declaring the position-dependence axis closed.
7. Freeze exact final HEAD/TREE after validation.
8. STOP before any new independent review dimension.

## Status semantics

A PASS may establish only:

`POSITION-DEPENDENCE AXIS = CLOSED`

It must not automatically claim:

`F044 FAMILY = CLOSED`

Other independent dimensions remain subject to later review.
