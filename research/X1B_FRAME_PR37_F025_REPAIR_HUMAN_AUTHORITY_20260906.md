# X1B-FRAME PR37 F025 bounded repair Human authority — 2026-09-06

## HumanDecision

The Human explicitly accepted exactly one bounded repair of finding `X1B-FRAME-F001-IMPLEMENTATION-F025`.

## Exact pre-repair ScriptOps binding

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `f75a55fd1923d115f3194827e8c0017a58587f60`
- OLD TREE: `c2e90eba0b074298820960fd33db81a155633d4a`
- verifier path: `scripts/verify_repository.py`
- OLD verifier blob: `e7c94abbf62342a360fc96d2c7ac07175c5d872e`
- finding: `FJ899/8 PR #277`

## Authorized repair boundary

Exactly one bounded F025 repair is authorized. Relative to OLD HEAD, the repair is verifier-only and must close the CommonMark ordered-list paragraph-interruption false negative recorded in F025: while an ordinary paragraph is active, a nonempty ordered marker may interrupt that paragraph only when its start number is `1`; non-`1` ordered markers must remain paragraph continuation text. This restriction applies only to paragraph interruption and must not prevent normal non-`1` ordered list items inside an already established list context.

The repair must:

1. preserve exactly one replacement commit over frozen BASE;
2. preserve the exact frozen 12-path BASE-relative implementation surface;
3. change only `scripts/verify_repository.py` relative to OLD HEAD;
4. add non-vacuous F025 regressions covering the exact `2.` counterexample and representative non-`1` ordered forms, while preserving valid bullet interruption, valid `1.`/`1)` interruption, existing-list non-`1` siblings, and F024-F006 behavior;
5. run the full repository verifier and both required PR workflows;
6. freeze the repaired exact binding and record completion evidence;
7. STOP before any post-repair independent review.

## Explicit exclusions

This acceptance grants no authority for merge, movement of `main`, deployment, release, tag, canonical effect, active-product status promotion, PR #35 integration, X1B reopen, V1 action, or any independent post-repair review.
