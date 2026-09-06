# X1B-FRAME PR #37 F039 validated patch pre-apply evidence

Date: 2026-09-06

Bound repair chain:

- finding: `FJ899/8 PR #349`
- Human repair authority: `FJ899/8 PR #350`
- preservation/design audit: `FJ899/8 PR #351`

Exact ScriptOps input:

- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `8ae5e9ac5f1c3ea48eccec25367ff0081d65df21`
- OLD TREE `09555ed85e4f70fd99d6df61ee9b2db459281448`
- OLD verifier blob `216231f460da2a775fa76c49081d50a74e943743`

Prepared patch:

- path: `X1B_FRAME_PR37_F039_REPAIR.patch`
- SHA-256: `b4a5a7cc7f9b107dd5c37a01bee77acccf81f35c1fc873553b57c87b5ba276c6`
- surface: `scripts/verify_repository.py` only
- numstat: `158` additions / `14` deletions

Prepared semantics:

1. Adds a dedicated complete-tag recognizer for CommonMark HTML block type 7.
2. Preserves existing types 1-6 precedence.
3. Starts type-7 raw state only when no top-level paragraph is open, or in a list path only after paragraph/block closure is already established by `blank_seen`.
4. Extends raw HTML blank-line termination from type 6 to `{6, 7}` while leaving type 1-5 explicit terminators unchanged.
5. Preserves type-7 non-interruption of an already-open paragraph and does not add type 7 to block-quote lazy-paragraph interrupt logic.
6. Adds F039 regressions for the `<Warning>` representative, raw ATX/list/thematic markers, nested HTML, EOF/blank termination, exact complete-tag grammar, invalid lookalikes, and paragraph non-interruption.

Validation already completed before exact worktree apply:

- patch syntax/parse: PASS
- synthetic exact-context `git apply --check`: PASS
- synthetic apply: PASS
- post-apply `git diff --check`: PASS
- patch numstat/surface check: PASS (`158/14`, verifier only)
- bounded helper/top-level F039 harness: PASS
- CommonMark 0.31.2 §4.6 cross-check: type-7 complete-tag start, blank/container/EOF end, raw payload, and non-interruption rule confirmed

Still mandatory on the exact OLD HEAD worktree before any push:

1. clean-tree/head/parent/one-commit/hash preflight;
2. exact `git apply --check` and numstat;
3. apply verifier-only patch;
4. compile and full verifier PASS including F039 and all prior regressions;
5. replacement amend preserving one commit over BASE and the frozen 12-path BASE surface;
6. fresh remote lease-check before guarded force-with-lease push;
7. both required workflows PASS on exact NEW HEAD;
8. completion evidence, then STOP before independent review.

No ScriptOps mutation has been performed by this evidence record. No merge/main/deploy/release/tag/canonical/status/X1B/V1 authority.
