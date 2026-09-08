# X1B-FRAME PR #37 — F044 multiple quoted parents repair authority

Human authorization from the current session permits exactly one bounded parser repair for the already reproduced F044 `multiple quoted parents / parent-scope separation` finding.

Exact ScriptOps starting candidate:
- PR: `FJ899/scriptops PR #37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `e666bdbd1ccf74f39433bf41d5a2985577d8ebcd`
- TREE: `5e956544953f206b47061a0268332a76d628dec2`
- verifier blob: `8535941463926c4b9101fc462e56eaa28aebf099`

Authorized scope:
- quoted-parent sibling separation only;
- opening a new sibling quoted parent must end the previous quoted-parent ownership scope;
- no expansion into outer-list sibling transitions;
- no block-transition work;
- no new recursion-depth variants;
- no other independent F044 dimension.

Mandatory validation:
1. existing one-quoted-parent control remains GREEN;
2. reproduced two-quoted-parent finding becomes PASS;
3. position-invariance remains GREEN;
4. depth-invariance remains GREEN;
5. inherited F042/F043/F044 regressions remain GREEN;
6. no `parent_count == 2` or equivalent numeric parent-count enumeration;
7. if any condition fails, record evidence and STOP;
8. if all conditions pass, freeze exact candidate state and STOP.

This authority does not authorize a parent-count sweep `1..N`, a new dimension-selection pass, merge, movement of `main`, deployment, release, tag, canonical effect, status promotion, X1B reopen or V1 action.