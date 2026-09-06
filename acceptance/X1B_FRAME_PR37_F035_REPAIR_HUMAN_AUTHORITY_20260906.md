# X1B-FRAME PR #37 — F035 bounded repair Human authority

Human authorization received: `accept`.

This record authorizes exactly one bounded repair of `X1B-FRAME-F001-IMPLEMENTATION-F035` on `FJ899/scriptops PR #37`.

## Exact binding

- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `74e11cdf52a8a0857d727030b6a6f44e40127b1b`
- OLD TREE: `260a7d09077af0fafdb679a41e124ac87f02cdfa`
- OLD verifier blob: `4e51a52af9e0f7c579f13a5faca804a9caaf912b`
- finding evidence: `FJ899/8 PR #325`

## Bounded repair authority

1. Only `scripts/verify_repository.py` may differ relative to OLD HEAD.
2. Repair the F035 CommonMark block-quote interruption/container defect without weakening F034/F033/F032/F031/F030/F029 or any earlier frozen regression.
3. Preserve block-quote lazy paragraph continuation so a quoted self-reference cannot be split from a following unmarked lazy predicate.
4. Preserve list-item ownership: a block quote structurally owned by an active list item remains in that item's security context; a top-level block quote outside every active list owner closes the old list path.
5. Invalid/non-top-level quote lookalikes, including escaped `\>` and standalone four-column-indented `>`, must not manufacture a false boundary.
6. Final candidate must remain exactly one replacement commit over frozen BASE and exactly the frozen 12-path BASE-relative surface.
7. Full local verifier must PASS, both existing GitHub Actions workflows on the exact replacement HEAD must PASS, and completion evidence must be frozen.
8. After completion evidence, STOP before independent post-repair review.

No authority is granted for repair outside F035, merge of PR #37 or PR #35, ScriptOps main movement, deployment, release, tag, canonical effect, status promotion, X1B reopen, or V1.
