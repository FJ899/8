# F036 preservation audit and bounded repair design

Date: 2026-09-06

Exact target:

- `FJ899/scriptops PR #37`
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `827d97a28bae8e4a6981739c616e1e6578a99665`
- OLD TREE `592a68f826d1b480d58319571b4df0e342f2513e`
- OLD verifier blob `cd079df9446d8a1781943670ec614615311a2564`
- F036 finding `FJ899/8 PR #331`
- Human repair authority `FJ899/8 PR #332`

## Preservation audit

Current verifier structure already has explicit bounded handling for:

- F032 thematic breaks;
- F033 top-level thematic/setext boundaries;
- F034 ATX headings;
- F035 block quotes and quoted lazy paragraph continuation;
- list ownership, ancestor unwind, same-level boundaries, and F031 lazy paragraph continuation.

F036 must not weaken or reorder those semantics except where fenced-code precedence necessarily comes before ordinary paragraph/list lazy fallback.

CommonMark 0.31.2 §4.5 properties used by the repair:

1. opening fence is at least three consecutive backticks or tildes;
2. opening indentation is at most three columns at top level;
3. backtick-fence info strings may not contain backticks;
4. closing fence uses the same character and at least the opening length;
5. closing fence may have up to three columns indentation and trailing spaces/tabs only;
6. fenced code may interrupt a paragraph and may be followed immediately by another block;
7. an unclosed fence runs to the end of its containing block/document;
8. fenced-code contents are literal and internal Markdown-looking lines must not be parsed as headings, lists, thematic breaks, or block quotes.

## Bounded repair design

1. Add narrow fenced-code opening/closing helpers only; do not introduce a general Markdown parser.
2. Add explicit fenced-code state before generic blank handling and before F035/F034/F032/list parsing, so all lines inside an open fence are literal until a valid close or containing-list exit.
3. Top-level opening fence flushes the preceding ordinary paragraph and starts a distinct authority unit containing only fenced literal payload, not the delimiter lines. This closes the F036 false subject-donation path while preserving self-promotion detection when the fenced payload itself contains a complete claim.
4. A top-level fence encountered while a list path is active closes that list path before the fenced block, preventing stale list self-reference donation.
5. A fence whose indentation is owned by an active list item remains in that item security context. Deeper descendants are closed first; fenced literal payload is appended to the surviving owner frame. A valid close forces the next line to re-resolve ownership because lazy continuation is paragraph-only.
6. If a list-owned fence reaches a nonblank line dedented outside its owner before a valid close, the fenced block ends with its containing item and that same line is reprocessed under ordinary outer structure.
7. F035 quote-laziness helper must treat an explicit fenced-code opener in quote content as non-paragraph content, so an unquoted following line cannot be borrowed as lazy quote paragraph continuation.
8. Invalid lookalikes remain ordinary text: fewer than three markers, four-column top-level opener, mixed/internal-space marker sequences, and invalid backtick info strings.
9. Wrong-character or too-short would-be closing fences remain literal fenced payload and cannot terminate the block.
10. Add regressions for backtick/tilde/three-column/unclosed top-level boundaries, immediate paragraph after close, top-level fence closing a list, list-owned and ancestor-owned fenced payload, post-close ownership re-resolution, quote-lazy interaction, fenced self-promotion, helper valid/invalid shapes, and invalid closing behavior.
11. Preserve F035/F034/F033/F032/F031/F030/F029 and all earlier regressions unchanged.
12. Only `scripts/verify_repository.py` may differ OLD→NEW; final topology remains one replacement commit over BASE with the same frozen 12 BASE-relative paths.

No ScriptOps mutation is performed by this audit record. No merge/main/deploy/release/tag/canonical/status/X1B/V1 authority is granted.
