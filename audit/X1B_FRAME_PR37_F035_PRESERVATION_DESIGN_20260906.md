# X1B-FRAME PR #37 — F035 preservation audit and bounded repair design

Bound to:
- `FJ899/scriptops PR #37`
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `74e11cdf52a8a0857d727030b6a6f44e40127b1b`
- OLD TREE `260a7d09077af0fafdb679a41e124ac87f02cdfa`
- OLD verifier blob `4e51a52af9e0f7c579f13a5faca804a9caaf912b`
- F035 finding `FJ899/8 PR #325`
- Human repair authority `FJ899/8 PR #326`

## Preservation audit

The existing verifier already has independently repaired and frozen handling for ordinary soft wraps, list-item ownership/laziness, thematic breaks, top-level setext/thematic separation, and ATX heading boundaries. F035 must not reinterpret any of those paths.

The missing structural rule is the block-quote container marker: a valid CommonMark block quote may interrupt an ordinary paragraph with no blank line, while paragraph continuation inside an open block quote may lazily omit the `>` marker. A list-owned block quote remains inside the owning list item; a quote at 0–3 columns outside every list owner is top level and closes the old list path.

## Bounded design

1. Add `_markdown_block_quote_layout()` recognizing a block-quote marker after 0–3 leading columns at top level, or at deeper absolute indentation only when list context asks for ownership resolution. Escaped `\>` and standalone 4-column-indented `>` remain non-markers at top level.
2. Add a small top-level block-quote accumulator. Starting a top-level quote flushes the preceding ordinary paragraph. Consecutive quoted lines remain one quote security unit.
3. Preserve CommonMark lazy paragraph continuation for an open top-level quoted paragraph: an unmarked ordinary continuation remains in the quote unit. Existing recognized paragraph interrupters — ATX headings, thematic breaks, and list markers that may interrupt paragraphs — close the lazy quote before normal parser handling.
4. Track whether the last explicitly quoted line can carry lazy paragraph continuation. Empty quote lines, nested quote openers, ATX headings, and thematic breaks do not grant lazy continuation into an unmarked following line. This avoids over-joining a quoted non-paragraph block to later top-level text.
5. With active list frames, resolve quote indentation against the same owner ranges used by F034/F032. An owned quote is appended to the owning item security path; a quote outside every owner at indentation <=3 closes the list path and starts a top-level quote. Deeper non-owned quote-like text falls through unchanged.
6. Do not add fenced-code, HTML-block, reference-definition, or general-purpose Markdown parsing under F035 authority.

## Required regression matrix

Benign/separated structural boundaries:
- `This file\n> grants release authority.`
- `This document\n   > authorizes merge.`
- `This record\n>controls current X1B authority.`
- `- This file\n> grants release authority.`
- quoted paragraph followed by top-level ATX/thematic/bullet interruption.

Must still reject one security context:
- `> This file\n> grants release authority.`
- `> This file\ngrants release authority.` (lazy quoted paragraph continuation)
- `> This file\n2. grants release authority.` (non-one ordered text cannot interrupt the quoted paragraph)
- `- This file\n  > grants release authority.`
- ancestor-owned quote inheriting the owning ancestor self-reference.

Invalid/non-boundary controls:
- `This file\n\\> grants release authority.`
- `This file\n    > grants release authority.`

Preserve all F034/F033/F032/F031/F030/F029 and earlier regression results unchanged.

No ScriptOps mutation is performed by this evidence record. No merge/main/deploy/release/tag/canonical/status/X1B/V1 authority is granted.
