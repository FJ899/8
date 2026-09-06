# X1B-FRAME PR #37 F039 bounded repair — Human authority

Date: 2026-09-06

Human authorization token: `accept`

This record binds exactly one bounded repair of finding `X1B-FRAME-F001-IMPLEMENTATION-F039` on `FJ899/scriptops PR #37`.

Exact target before repair:

- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `8ae5e9ac5f1c3ea48eccec25367ff0081d65df21`
- OLD TREE: `09555ed85e4f70fd99d6df61ee9b2db459281448`
- OLD verifier blob: `216231f460da2a775fa76c49081d50a74e943743`
- finding evidence: `FJ899/8 PR #349`
- prior F038 completion evidence: `FJ899/8 PR #347`

Authorized scope:

1. Close F039 only: correctly preserve CommonMark HTML block type-7 literal state when a complete type-7 tag legally starts a block, while preserving the normative rule that type 7 cannot interrupt an already-open paragraph.
2. Preserve F038, F037, F036, F035, F034, F033, F032, F031, F030, F029 and every earlier regression.
3. OLD→NEW may change only `scripts/verify_repository.py`.
4. Final PR #37 topology remains exactly one replacement commit over BASE and exactly the same frozen 12 BASE-relative paths.
5. Full local verifier must PASS, then both required remote workflows must PASS on the exact replacement HEAD.
6. Freeze completion evidence, then STOP before any independent post-F039 review.

Not authorized: merge PR #37 or PR #35, ScriptOps `main` movement, deploy/release/tag, canonical effect, active-product status promotion, X1B reopen, V1, or any broader Markdown/parser expansion beyond the bounded F039 correction.
