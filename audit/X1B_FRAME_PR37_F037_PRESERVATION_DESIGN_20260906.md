# X1B-FRAME PR #37 F037 preservation audit and bounded repair design

Exact target: `FJ899/scriptops PR #37` at OLD HEAD `766a392c972fb14267768af283daaf64cd3282b9`, TREE `e7433570911943deb134947fc045bb00aaa5a1a4`, verifier blob `c6175ca14db603442f4ce24dc9ea04b8140daecb`, BASE `2f22843ac570498b506101addeba5453ab777f08`.

Bound to finding `FJ899/8 PR #337` and Human repair authority `FJ899/8 PR #338`.

## Normative CommonMark semantics checked

CommonMark 0.31.2 §4.3 defines a setext heading as one or more paragraph-text lines followed by a setext heading underline. The underline is one or more `=` or one or more `-`, with at most three leading spaces and optional trailing spaces/tabs; internal spaces/tabs are invalid. `=` creates level 1. Four leading spaces are too many. A blank line is generally not required after the heading. An underline without preceding heading text is not an empty setext heading. A setext underline cannot be a lazy continuation line in a list item or block quote.

## Preservation audit

The OLD verifier already has dedicated precedence/state for F036 fenced code, F035 block quotes, F034 ATX headings, F033/F032 thematic/dash-setext behavior, and F031-F029 list ownership/boundaries. F037 must not rewrite that machinery or broaden into HTML-block/indented-code parsing.

Required preserved behavior:

- F036 fenced literal payload remains opaque to all inner Markdown recognition.
- F035 unmarked lazy block-quote continuation remains valid; specifically an unmarked `===` after an open quoted paragraph must not be promoted into an outside setext boundary merely because it resembles an underline.
- Explicit quoted `> ===` after quoted paragraph text ends the quoted paragraph/setext heading, so a later unquoted line cannot lazily inherit that heading subject.
- F033/F032 dash/setext/thematic precedence is unchanged; F037 adds the missing `=` family rather than refactoring `---` semantics.
- A top-level `===` is structural only when there is preceding open ordinary paragraph text. Without preceding heading text it remains ordinary paragraph text.
- Invalid `=` lookalikes (`= =`, payload after underline, escaped marker, four-column top-level indentation) remain ordinary/code-like text and may not manufacture a boundary.
- A top-level `=` underline that appears after an active list path cannot be a lazy list continuation; if it is outside every current list owner, the list path closes before that line.
- An `=` underline owned by the current list leaf after open item paragraph text ends that paragraph block. Following dedented text must re-resolve ownership; following still-owned text remains in the same list-item security context.
- No attempt is made in F037 to reinterpret ancestor-owned ambiguous `=` lines across nested child blocks; fail-closed existing behavior is preserved there.

## Bounded repair design

1. Add a small `_markdown_setext_heading_underline_layout()` helper recognizing only the CommonMark underline shape and returning indentation/marker family.
2. In explicit block-quote paragraph state, treat a quoted setext underline as ending paragraph laziness; do not add unmarked top-level setext recognition to the block-quote lazy-continuation test.
3. Before ordinary paragraph/list lazy fallback, handle `=` setext underlines:
   - top level + open ordinary paragraph: flush the preceding paragraph/heading security unit and consume the underline;
   - active list + underline outside all owners: emit/close the list path and reclassify the underline as ordinary top-level text because an empty setext heading is invalid;
   - active current leaf + owned underline + no prior block boundary: keep it in that list-item security context but force the following line to re-resolve ownership.
4. Leave `-` handling on the existing F032/F033 path.
5. Add F037 regression controls for top-level, multiline, three-column, quote, list-close/current-leaf ownership, self-promotion inside heading text, and invalid underline lookalikes.

Only `scripts/verify_repository.py` may change relative to OLD HEAD. Final topology and workflow requirements remain those in Human authority PR #338.
