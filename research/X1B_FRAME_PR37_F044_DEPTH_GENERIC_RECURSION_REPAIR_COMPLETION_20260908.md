# Completion evidence — bounded F044 depth-generic nested outer-list recursion repair

Authority: `FJ899/8 PR #518`.

Finding chain: `FJ899/8 PR #514` (depth=1 -> 2 finding), `FJ899/8 PR #516` (bounded depth=2 repair completion), `FJ899/8 PR #517` (depth=2 -> 3 finding with the same active-list ownership/flattening mechanism).

## Final ScriptOps binding

`FJ899/scriptops PR #37`

- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `e666bdbd1ccf74f39433bf41d5a2985577d8ebcd`
- TREE `5e956544953f206b47061a0268332a76d628dec2`
- verifier entrypoint blob `8535941463926c4b9101fc462e56eaa28aebf099`
- previous bounded depth=2 entrypoint retained byte-for-byte at `scripts/verify_repository_f044_nested_outer_depth2.py`, blob `98ef815bd246d600a64de3f379ebd0d7483aa21d`
- exactly 1 replacement commit ahead / 0 behind
- exactly 75 changed paths

The replacement commit has parent exactly BASE and carries the same repair TREE that passed the isolated repair probe.

## Repair boundary

The repair uses one structural owner-chain rule and never consults numeric recursion depth. Starting at a source-column-zero outer list item, it follows repeated child list owners only while the child marker indentation equals the current owner's content indentation, then applies the already-isolated quoted child/sibling ownership separation.

The semantic shape is intentionally bounded to one quoted parent, one child with exactly one ordinary continuation, and one same-level sibling. Multiple quoted parents, block transitions, blank/fence/HTML boundaries, outer-list siblings, continuation-run generalization, and other independent recursion/topology dimensions remain outside scope.

## Validation

Isolated repair-probe: `FJ899/scriptops PR #88`, closed without merge.

- probe Verify `34276439999`: PASS
- probe Smoke `34276439879`: PASS
- final Verify `34276528831`: PASS
- final Smoke `34276528781`: PASS

The verifier explicitly PASSes:

- depth=1,2,3 under the same common structural rule;
- one generated depth-invariance property for depth=1..16 with constant semantic payload and only outer-list container depth varying;
- intermediate ownership separation: `This file` and `grants release authority.` do not coexist in one normalized authority unit after the common transformation;
- outer-owner, deepest-owner, and same-child self-promotion security negatives;
- existing position-invariance N=1..24 for run lengths 1 and 2;
- all inherited F042/F043/F044 regressions.

## Disposition

`POSITION-DEPENDENCE AXIS = CLOSED`

`F044 NESTED OUTER-LIST RECURSION DEPTH-DEPENDENCE AXIS = CLOSED FOR THE ISOLATED SEMANTIC SHAPE`

`DEPTH-GENERIC ROOT CAUSE = VALIDATED CLOSED FOR THIS SHAPE`

`F044 FAMILY = NOT CLOSED`

STOP before a new independent F044 review dimension.

No merge, ScriptOps main movement, deploy, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1 action was performed or authorized.
