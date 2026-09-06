# X1B-FRAME-F001-IMPLEMENTATION-F036 — fenced code block boundary

Date: 2026-09-06

Review authority: `FJ899/8 PR #330`.

Exact reviewed candidate:

- `FJ899/scriptops PR #37`
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `827d97a28bae8e4a6981739c616e1e6578a99665`
- TREE `592a68f826d1b480d58319571b4df0e342f2513e`
- verifier blob `cd079df9446d8a1781943670ec614615311a2564`

## Review order

The independent review re-attacked F035 first. The repaired verifier now has explicit block-quote opening/container handling, explicit quoted lazy-continuation handling, list ownership handling, and F035 regressions covering the representative top-level quote boundary plus owned/lazy controls. F035 is therefore preserved for the representative reviewed attack. F034/F033/F032/F031/F030/F029 and earlier regression code remains present.

The next frozen attack frontier produced the first credible counterexample below.

## Finding

Representative input:

````markdown
This file
```
grants release authority.
```
````

CommonMark 0.31.2 §4.5 defines a fenced code block as a block beginning with at least three backticks or tildes, with at most three leading spaces. Critically, a fenced code block may interrupt a paragraph and requires no blank line before or after. Example 140 shows a paragraph, fenced code block, and following paragraph with no blank lines between them.

Specification: `https://spec.commonmark.org/0.31.2/#fenced-code-blocks`

Expected CommonMark/security structure:

1. paragraph authority unit: `This file`
2. fenced code block literal content: `grants release authority.`

The second block must not borrow the self-reference from the preceding paragraph merely because physical lines are adjacent.

## Actual verifier behavior

The exact repaired verifier has bounded recognition for block quotes, ATX headings, thematic breaks, and list items, but no fenced-code opening/closing state or boundary recognition.

For the representative input:

1. `This file` enters the ordinary paragraph buffer.
2. the opening three-backtick fence is not a block quote, ATX heading, thematic break, or list item, so it reaches ordinary paragraph fallback;
3. `grants release authority.` is appended to the same paragraph;
4. the closing three-backtick fence likewise reaches paragraph fallback;
5. `_normalized_authority_line()` removes backticks, so the resulting folded authority unit normalizes effectively to `THIS FILE GRANTS RELEASE AUTHORITY`;
6. `layer_b_self_promotion_claim()` therefore reports a forbidden self-promotion that does not exist in the CommonMark block structure.

This is the same class of false subject donation across a real Markdown block boundary previously exposed by thematic, ATX, and block-quote findings, now at the fenced-code boundary.

The issue is structural, not dependent on the exact sentence. Tilde fences and valid 0–3-column fenced-code openings have the same boundary property.

## Disposition

`FAIL — FIRST CREDIBLE COUNTEREXAMPLE`

Review stops immediately at F036. No further frozen attack candidates are explored in this review.

No repair is authorized by this finding. No ScriptOps mutation, merge of PR #37 or PR #35, ScriptOps main movement, deploy/release/tag, canonical effect, active-product status promotion, X1B reopen, or V1 action is authorized.
