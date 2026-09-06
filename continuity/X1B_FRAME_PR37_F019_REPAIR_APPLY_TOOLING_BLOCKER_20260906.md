# X1B-FRAME PR37 F019 repair apply tooling continuity

Human-authorized repair authority: `FJ899/8 PR #247`.

Exact live pre-repair target remains:

- repository `FJ899/scriptops`
- PR `#37`
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `ba8d80ac0ff5272e8e25e27145f53dd81b1ed7bd`
- TREE `07cadd354b127d39957e0e16ebed5031c94cfdc4`
- verifier blob `3b9955967635a37d4453d0a2ae449ad341392e23`

Prepared patch:

- file `X1B_FRAME_PR37_F019_REPAIR.patch`
- bytes `5558`
- SHA-256 `d80819c68dc978af6c8e85795f2f2aa092ab77f2b8872bd1716a13c2ddc4a4ed`
- changed path only `scripts/verify_repository.py`

The patch adds Markdown list-item layout tracking so blank-line continuation paragraphs indented within the same list item remain one authority unit, while sibling list items and dedented paragraphs start fresh units. It adds non-vacuous production-validator regressions for positive bullet/ordered-list continuation, benign negated continuation, sibling items, and dedented adjacent text.

The current connector has no safe patch-apply/file-upload route for the existing PR #37 branch while preserving the exact replacement-commit shape. No ScriptOps ref/tree/commit/main mutation was attempted by this continuity record. The retained LF local clone may execute the already-authorized repair. Post-repair independent review still requires a separate Human gate.
