# X1B-FRAME PR37 F019 bounded repair Human authority

Human `accept` authorizes exactly one bounded replacement repair of `FJ899/scriptops PR #37` for finding `X1B-FRAME-F001-IMPLEMENTATION-F019` recorded in `FJ899/8 PR #246`.

Exact pre-repair target:

- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `ba8d80ac0ff5272e8e25e27145f53dd81b1ed7bd`
- TREE `07cadd354b127d39957e0e16ebed5031c94cfdc4`
- verifier blob `3b9955967635a37d4453d0a2ae449ad341392e23`

Bounded repair authority:

1. final PR #37 remains exactly one commit over frozen BASE;
2. base-relative changed paths remain exactly the frozen twelve-path surface;
3. relative to pre-repair HEAD, only `scripts/verify_repository.py` may change;
4. close F019 blank-line continuation inside one Markdown list item without globally joining unrelated paragraphs;
5. preserve F018-F006 behavior;
6. add non-vacuous production-validator regressions for positive list-item continuation and benign negative/list-adjacent cases;
7. run repository verifier plus `Verify repository state` and `Phase 6 ScriptOps smoke`;
8. force-update only the existing PR #37 branch with stale-head protection;
9. freeze repaired HEAD/TREE/verifier blob/CI and STOP.

No independent post-repair review is authorized by this acceptance. No merge, ScriptOps main movement, PR35 integration, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority is granted.
