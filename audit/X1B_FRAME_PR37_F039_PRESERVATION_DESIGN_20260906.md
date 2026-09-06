# X1B-FRAME PR #37 F039 preservation audit and bounded repair design

Date: 2026-09-06

Bound target:

- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `8ae5e9ac5f1c3ea48eccec25367ff0081d65df21`
- OLD TREE `09555ed85e4f70fd99d6df61ee9b2db459281448`
- OLD verifier blob `216231f460da2a775fa76c49081d50a74e943743`
- finding `FJ899/8 PR #349`
- Human repair authority `FJ899/8 PR #350`

## Preservation audit

The F038 implementation correctly introduced literal raw-block state for CommonMark HTML block types 1-6, with type-specific termination, list/container ownership and suppression of nested Markdown parsing. F037-F029 and earlier regression matrices remain present. The F039 change must not alter those paths except where type 7 shares the same blank-line/EOF literal-state machinery.

Normative CommonMark 0.31.2 constraints used by this design:

1. HTML block type 7 starts only on a line whose post-indent content is a complete open tag (open tag name other than `pre`, `script`, `style`, `textarea`) or complete closing tag, followed only by spaces/tabs to EOL.
2. Up to three leading indentation columns are allowed at top level.
3. Type 7 ends at the following blank line, the end of its container, or EOF.
4. Interior Markdown-looking lines remain literal raw HTML-block payload and do not change parser state.
5. Type 7 cannot interrupt an already-open paragraph; this is the critical difference from types 1-6.
6. Types 1-6 retain precedence on their existing helper/path.

## Bounded repair design

1. Add a dedicated `_markdown_html_block_type7_start_layout()` helper implementing the single-line CommonMark open/closing-tag grammar needed for the type-7 start condition. It is separate from the existing types-1-6 helper so non-interruption can be enforced by parser context rather than by tag syntax alone.
2. Extend `_markdown_html_block_end_matches()` so block type 7 uses the same blank-line end condition as type 6.
3. Extend the existing raw HTML state machine so `{6, 7}` use blank-line termination and types 1-5 keep their current explicit terminators.
4. At top level, start a type-7 raw block only when `paragraph` is empty. If an ordinary paragraph is already open, do not consume the type-7 candidate; let existing paragraph/ATX/thematic/list rules continue unchanged. This preserves CommonMark's non-interruption rule.
5. In an active list path, a type-7 candidate may start raw state only after the current paragraph/block has already ended (`blank_seen`), and only under the nearest indentation owner; an outside 0-3-column candidate closes the old list path and starts a top-level type-7 block. A candidate in an open list-item paragraph remains ordinary/lazy text.
6. Do not add type-7 recognition to the existing block-quote lazy-paragraph interrupt test. A type-7-looking line in an already-open quoted paragraph must remain eligible for paragraph laziness because type 7 cannot interrupt that paragraph. Explicit quoted lines already remain in the same quote security unit.
7. Add F039 regressions covering: the `<Warning>` representative with ATX-looking raw payload; raw list/thematic markers inside type 7; EOF and blank-line termination; complete custom open/closing tags with attributes; invalid/incomplete/trailing-payload lookalikes; four-column indentation; and non-interruption of an already-open paragraph.
8. Preserve OLD→NEW surface as `scripts/verify_repository.py` only; no generic HTML parser, no link-reference-definition work, no unrelated Markdown expansion.

Required completion invariants remain: one replacement commit over frozen BASE, the same 12 BASE-relative paths, full local verifier PASS, both required workflows PASS on exact NEW HEAD, completion evidence, then STOP before independent review.
