# X1B-FRAME-F001-IMPLEMENTATION-F037 — setext `=` heading boundary

Date: 2026-09-06

Review authority: `FJ899/8 PR #336`.

Exact reviewed candidate:

- `FJ899/scriptops PR #37`
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `766a392c972fb14267768af283daaf64cd3282b9`
- TREE `e7433570911943deb134947fc045bb00aaa5a1a4`
- verifier blob `c6175ca14db603442f4ce24dc9ea04b8140daecb`

## Review order

The independent review re-attacked F036 first. The repaired verifier has explicit fenced-code opening/closing state, top-level paragraph interruption, literal fenced payload handling, list ownership handling, and F036 regressions for the representative top-level fence plus owned/closing/opening controls. The representative F036 attack is therefore preserved. F035/F034/F033/F032/F031/F030/F029 and earlier regression code remains present.

The next remaining frozen structural-boundary attack produced the first credible counterexample below.

## Finding

Representative input:

```markdown
This file
===
grants release authority.
```

CommonMark 0.31.2 §4.3 defines a setext heading underline as a sequence of `=` characters or a sequence of `-` characters with no more than three leading spaces. `=` creates a level-1 setext heading. A setext heading need not be followed by a blank line. Thus the representative parses as:

1. level-1 setext heading whose content is `This file`;
2. following ordinary paragraph `grants release authority.`

Specification: `https://spec.commonmark.org/0.31.2/#setext-headings`

Expected security units:

1. heading unit: `This file`
2. paragraph unit: `grants release authority.`

The second block must not borrow the heading's self-reference.

## Actual verifier behavior

The exact verifier recognizes dash-only setext ambiguity only inside `_markdown_thematic_break_layout()`. That helper accepts only `-`, `_`, or `*`; it has no recognition for `=` setext underlines. There is no separate setext-heading state/boundary helper.

For the representative input:

1. `This file` enters the ordinary paragraph buffer.
2. `===` is not a fenced-code opener, block quote, ATX heading, thematic break, or list item, so it reaches ordinary paragraph fallback.
3. `grants release authority.` is appended to that same paragraph.
4. the emitted authority unit is effectively `This file === grants release authority.`.
5. `_normalized_authority_line()` preserves `=` but tokenization still leaves `THIS FILE` and the positive promotion terms `GRANTS` / `RELEASE AUTHORITY` in one logical unit.
6. `layer_b_self_promotion_claim()` therefore reports a forbidden self-promotion even though CommonMark places the subject and predicate in distinct blocks.

This is a false subject donation across a real CommonMark block boundary. It is distinct from F033's dash-only setext/thematic handling because level-1 `=` underlines never enter `_markdown_thematic_break_layout()`.

## Disposition

`FAIL — FIRST CREDIBLE COUNTEREXAMPLE`

Review stops immediately at F037. No HTML-block or other later frozen attack candidates are explored in this review.

No repair is authorized by this finding. No ScriptOps mutation, merge of PR #37 or PR #35, ScriptOps main movement, deploy/release/tag, canonical effect, active-product status promotion, X1B reopen, or V1 action is authorized.
