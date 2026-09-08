# Human authority — bounded F044 depth-generic nested outer-list recursion repair

Authorized target: `FJ899/scriptops PR #37` frozen HEAD `8589fdbf49ecc62e9df8097fedb06b6bb0b7c222`, TREE `e3c94616e3971dbdf6aea9c68f5b971e420d4caf`, verifier blob `98ef815bd246d600a64de3f379ebd0d7483aa21d`.

Finding basis: `FJ899/8 PR #514` established depth=1 -> depth=2 failure before bounded repair; `FJ899/8 PR #516` records repaired/GREEN depth=1 -> depth=2; `FJ899/8 PR #517` established depth=2 -> depth=3 FAIL with the same active-list ownership/flattening mechanism.

## Authorized scope

Exactly one bounded depth-generic F044 nested-outer-list recursion repair:

- existing F044 outer-list ownership / list-frame / active-path emission boundary only;
- implementation + verification only;
- one common structural recursion rule; no depth-specific enumeration, limit table, or equivalent `depth == N` handling;
- do not expand into multiple quoted parents, block transitions, blank/fence/HTML boundaries, outer-list siblings, continuation-run generalization, or another independent F044 dimension;
- no merge, ScriptOps `main` movement, deploy, release, tag, canonical effect, status promotion, X1B reopen, or V1.

## Mandatory success conditions

1. depth=1, depth=2, and depth=3 PASS under the common rule.
2. One parameterized depth-invariance property covers at least depth=1..12 (preferably 1..16) while preserving semantic shape; only outer-list container depth varies.
3. The same self-reference/promotion oracle is used for every depth.
4. An intermediate ownership invariant confirms that semantically separate child/sibling fragments never coexist in one authority unit after normalization.
5. No depth-specific implementation branch or enumerated depth table.
6. Existing position-invariance N=1..24 remains GREEN.
7. All inherited F042/F043/F044 regressions remain GREEN.
8. Freeze exact final HEAD/TREE/verifier binding and validation evidence, then STOP before another F044 review dimension.

FAIL of any mandatory condition => freeze evidence and STOP.
