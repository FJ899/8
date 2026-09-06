# X1B-FRAME PR #37 — F034 validated patch pre-apply evidence

## Exact input

- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `d127ca34ee9b6f03a4e7286913e7cd89fa55fa33`
- OLD TREE: `9f4b273a7e8f05360a972e2606353fb2e7f4b5ae`
- OLD verifier blob: `e793f9558e9f55ba33bedf90068e185d229d70e9`
- F034 finding: `FJ899/8 PR #319`
- Human repair authority: `FJ899/8 PR #320`
- preservation/design audit: `FJ899/8 PR #321`

## Prepared patch

- file: `X1B_FRAME_PR37_F034_REPAIR.patch`
- SHA-256: `3839862c2cc93fec90a0813abbecd1ee3312f2b9c68781e32e39af9aa221ad46`
- parsed surface: `scripts/verify_repository.py` only
- numstat: `160` additions / `0` deletions

## Repair shape

The patch:

1. adds a CommonMark ATX-heading opening parser for 1–6 unescaped `#` characters followed by space/tab or EOL;
2. recognizes 0–3-column ATX headings at top level before list/lazy handling;
3. flushes the preceding ordinary paragraph and emits heading text as its own security-relevant unit;
4. resolves list ownership for ATX headings, preserving owned heading text inside the owning list-item security context;
5. closes deeper descendants when an ATX heading belongs to an ancestor item;
6. forces following dedented text to re-resolve ownership instead of borrowing F031 paragraph laziness;
7. keeps invalid lookalikes (`#######`, `#hashtag`, `#5`, escaped opener, 4-column top-level form) as ordinary text;
8. adds F034 positive/negative/helper/list-ownership regression coverage and a dedicated PASS marker.

## Pre-apply validation

An isolated model of the exact folding/authority logic with the proposed ATX branch confirmed:

- benign/separated: top-level H1/H6, 3-column ATX, empty ATX, ATX closing an active list, ancestor-owned ATX closing a nested child;
- preserved rejecting: heading self-promotion, owned-list heading promotion, ancestor-owned heading inheriting the parent self-reference, seven-hash lookalike, hashtag form, escaped opener, and 4-column top-level lookalike;
- F033/F032/F031/F030/F029 semantics are not replaced or weakened by the ATX branch.

CommonMark 0.31.2 cross-check confirmed the representative shapes: ATX headings interrupt paragraphs without blank lines; levels 1–6 and up to 3 leading spaces are headings; more than 6 hashes, hashtag-like forms, escaped openers, and 4-column top-level forms are not ATX headings.

The patch parses as a single verifier-only unified diff with `160/0` numstat. Exact OLD-HEAD `git apply --check`, compile, and full verifier execution remain mandatory before commit; both GitHub Actions workflows remain mandatory after push.

No ScriptOps mutation has been performed by this evidence record. No merge/main/deploy/release/tag/canonical/status/X1B/V1 authority is granted.
