# X1B-FRAME PR37 F029 REPAIR HUMAN AUTHORITY — 2026-09-06

HumanDecision: ACCEPT.

This record authorizes exactly one bounded F029 repair of `FJ899/scriptops PR #37`.

Finding: `X1B-FRAME-F001-IMPLEMENTATION-F029`, durable finding PR #296.

Exact pre-repair ScriptOps binding:
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `0f7d34476c33fdc0e530f22e3168791c600c17e1`
- verifier scope: `scripts/verify_repository.py`
- PR remains draft/open/unmerged with exactly one commit over BASE and the frozen twelve-path BASE-relative surface.

Authorized repair boundary:
1. Repair only the F028/F029 CommonMark active-list handling in the verifier.
2. Resolve non-`1` ordered markers against the active list path, not only the current leaf.
3. Preserve a legal sibling boundary when dedenting reaches an already-established ordered ancestor at the same marker indentation with a compatible ordered delimiter.
4. Preserve the original F028 lazy-continuation behavior when no such established sibling boundary exists.
5. Preserve F027 through F006 behavior and genuine sibling/dedent boundaries.
6. Add non-vacuous F029 regressions and retain the existing regressions.
7. Relative to OLD HEAD, only `scripts/verify_repository.py` may change.
8. Final ScriptOps candidate must remain exactly one replacement commit over frozen BASE and retain exactly the frozen twelve BASE-relative changed paths.
9. Full verifier must pass and both required exact-head workflows must succeed.
10. Freeze durable repair-completion evidence, then STOP before any independent post-F029 review.

No merge, ScriptOps main movement, PR #35 integration, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 authority is granted.
