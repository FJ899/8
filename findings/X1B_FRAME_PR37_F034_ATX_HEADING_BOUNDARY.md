# X1B-FRAME-F001-IMPLEMENTATION-F034 — ATX heading boundary false promotion

## Exact reviewed candidate

`FJ899/scriptops PR #37`

- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `d127ca34ee9b6f03a4e7286913e7cd89fa55fa33`
- TREE `9f4b273a7e8f05360a972e2606353fb2e7f4b5ae`
- verifier blob `e793f9558e9f55ba33bedf90068e185d229d70e9`
- review authority `FJ899/8 PR #318`
- F033 completion evidence `FJ899/8 PR #317`

## Review order

F033 was re-attacked first and its exact top-level thematic-break/setext controls remain present. F032/F031/F030/F029 and earlier frozen regressions remain preserved in the reviewed verifier. Review then continued to the next CommonMark block-interruption attack and stopped at the first credible counterexample below.

## Representative counterexample

```markdown
This file
# grants release authority.
```

## Expected CommonMark structure

CommonMark ATX headings need no surrounding blank lines and may interrupt paragraphs. The example therefore parses as two distinct top-level blocks:

1. paragraph: `This file`
2. ATX heading: `grants release authority.`

The heading has no self-reference. The preceding paragraph has no authority promotion. The Layer-B self-promotion check must not donate `This file` across the ATX-heading boundary.

CommonMark 0.31.2 section 4.2, Example 78, explicitly demonstrates `Foo bar` followed immediately by `# baz` as a paragraph followed by an ATX heading, then a later paragraph.

## Actual repaired verifier behavior

The current `_authority_soft_wrapped_units()` has explicit structural handling for thematic breaks, then list markers. It has no ATX-heading block-interruption recognition.

For the representative input:

- `This file` is appended to the ordinary `paragraph` buffer.
- `# grants release authority.` is nonblank, is not a thematic break, and is not a list item.
- with no active `list_frames`, it is appended to the same `paragraph` buffer.
- the resulting manufactured authority unit is effectively `This file # grants release authority.`
- `_normalized_authority_line()` strips `#`, yielding a normalized unit containing `THIS FILE` plus `GRANTS` / `AUTHORITY`.
- `layer_b_self_promotion_claim()` therefore reports forbidden self-promotion even though CommonMark places the two phrases in distinct blocks.

## Security/correctness impact

This is a false-positive / false-promotion structural correctness failure in the same class as F029/F030/F032/F033: a self-reference from one Markdown block is borrowed into a separate authority-bearing block across a real CommonMark boundary.

It also shows that the F033 repair is still construct-specific: top-level thematic breaks are fixed, but other paragraph-interrupting leaf blocks are not yet modeled.

## Disposition

`FAIL — FIRST CREDIBLE COUNTEREXAMPLE`

Review stops here before repair.

No ScriptOps mutation, PR #37/PR #35 merge, main movement, deploy/release/tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority is granted by this finding.
