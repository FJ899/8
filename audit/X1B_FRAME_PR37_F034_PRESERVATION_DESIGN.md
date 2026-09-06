# X1B-FRAME PR #37 — F034 preservation audit and bounded repair design

## Binding

- ScriptOps PR: `FJ899/scriptops PR #37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `d127ca34ee9b6f03a4e7286913e7cd89fa55fa33`
- OLD TREE: `9f4b273a7e8f05360a972e2606353fb2e7f4b5ae`
- OLD verifier blob: `e793f9558e9f55ba33bedf90068e185d229d70e9`
- F034 finding: `FJ899/8 PR #319`
- Human repair authority: `FJ899/8 PR #320`

## Preservation audit

F034 is the first post-F033 credible counterexample. The existing F033 repair correctly handles top-level thematic/setext boundaries, but `_authority_soft_wrapped_units()` has no equivalent CommonMark ATX-heading interruption path. A valid ATX line therefore falls through to ordinary paragraph/list lazy-continuation handling.

The repair must preserve all earlier security semantics, especially:

- F019: blocks inside one list item remain one security unit; an owned heading must inherit its owning item context rather than becoming an unrelated top-level unit.
- F029/F030: descendant/same-level boundaries cannot donate context across structural siblings.
- F031: invalid marker-looking ordinary text may remain lazy continuation; indentation loss alone is not a boundary.
- F032/F033: thematic/setext precedence and boundary handling remain unchanged.

CommonMark 0.31.2 section 4.2 constraints used for the bounded ATX parser:

- opening sequence is 1–6 unescaped `#` characters;
- it must be followed by space/tab or end-of-line;
- up to 3 leading columns are valid at top level;
- 4 leading columns are not top-level ATX;
- ATX headings can interrupt paragraphs without blank lines;
- more than 6 opening `#` characters and `#hashtag`/`#5` shapes are ordinary paragraph text.

## Bounded repair design

1. Add `_markdown_atx_heading_layout(raw_line, allow_deep_indent=False)` returning the heading indentation only when the CommonMark opening shape is valid.
2. Evaluate ATX structure before list-marker parsing and before ordinary lazy-continuation fallback.
3. Top level, no active list:
   - flush the open ordinary paragraph;
   - emit the heading line as its own authority unit, so a heading that itself says `This file grants release authority` still fails;
   - do not discard heading text.
4. Active list:
   - resolve the deepest owning list frame with the same container-relative window already used for F032: `content_indent <= heading_indent <= content_indent + 3`;
   - if no owner exists and the heading is valid top-level (0–3 columns), emit/close the active list path, clear it, then emit the heading as a separate top-level authority unit;
   - if an owner exists, close any deeper descendants, append the heading text to that owning item security context, and set block-boundary state so the following dedented line must re-resolve ownership instead of borrowing F031 lazy continuation.
5. Invalid ATX lookalikes remain ordinary text:
   - `####### heading`;
   - `#hashtag` / `#5 bolt`;
   - escaped `\# heading`;
   - 4-column top-level `    # heading`.
6. Regression coverage must include:
   - F034 representative top-level boundary;
   - levels 1 and 6, 3-column indentation, empty ATX heading;
   - heading self-promotion rejection;
   - list-closing top-level heading separation;
   - owned list-item heading inheritance rejection;
   - ancestor-owned heading after nested child closure;
   - invalid lookalikes preserving prior paragraph/lazy behavior;
   - explicit helper positive/negative shape checks.
7. No parser expansion to block quotes, fenced code blocks, HTML blocks, indented-code semantics beyond the ATX-specific cases above; those remain outside this repair unless later independently found.

## Candidate invariants

- only `scripts/verify_repository.py` may differ relative to OLD HEAD;
- final ScriptOps candidate is one replacement commit directly over BASE;
- BASE-relative surface remains exactly the frozen 12 paths;
- full verifier PASS;
- `Verify repository state` PASS on exact new HEAD;
- `Phase 6 ScriptOps smoke` PASS on exact new HEAD;
- completion evidence then mandatory STOP before independent post-repair review.

No ScriptOps mutation is performed by this audit record.
