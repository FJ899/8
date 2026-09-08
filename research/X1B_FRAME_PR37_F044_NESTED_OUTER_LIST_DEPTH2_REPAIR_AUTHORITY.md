# X1B-FRAME PR #37 — Human authority for bounded F044 nested outer-list depth2 repair

Human authorization is granted for exactly one bounded F044 nested-outer-list-recursion repair on frozen `FJ899/scriptops PR #37`:

- HEAD `f286a6351a20037de7d9948f4f021dac7ed22547`
- TREE `2ab1f67e42c0b995fc52c64c06536dd933eb42f5`
- finding evidence: `FJ899/8 PR #514`

## Scope

- only the depth=1 -> depth=2 transition;
- only existing F044 list-frame / ownership / active-path emission boundary;
- implementation + verification only;
- preserve semantic separation across exactly one additional nested outer-list owner;
- no depth>=3 expansion;
- no merge/main/deploy/release/tag/canonical/status/X1B/V1 action.

## Mandatory success conditions

1. Existing depth=1 F044-D17 control remains GREEN.
2. Exact depth=2 finding from PR #514 becomes PASS.
3. Position-dependence/invariance axis remains GREEN.
4. All inherited F042/F043/F044 regressions remain GREEN.
5. No `if depth == 2` or equivalent numeric depth special case.
6. Exact final HEAD/TREE and validation evidence are frozen, then STOP.

Any failed condition requires evidence freeze and STOP.

This authority does not establish a generic recursion rule and does not authorize depth=3+ review or repair.