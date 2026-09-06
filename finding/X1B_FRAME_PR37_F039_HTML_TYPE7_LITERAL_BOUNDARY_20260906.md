# X1B-FRAME-F001-IMPLEMENTATION-F039 — CommonMark type-7 HTML block literal-state omission

Disposition: `FAIL — FIRST CREDIBLE COUNTEREXAMPLE`

Independent review authority: `FJ899/8 PR #348`.
Reviewed ScriptOps candidate:
- PR `FJ899/scriptops #37`
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `8ae5e9ac5f1c3ea48eccec25367ff0081d65df21`
- TREE `09555ed85e4f70fd99d6df61ee9b2db459281448`
- verifier blob `216231f460da2a775fa76c49081d50a74e943743`
- F038 completion evidence `FJ899/8 PR #347`

## Review order

F038 was re-attacked first. Its original type-6 paragraph-interruption finding remains closed: the repaired verifier recognizes HTML block types 1-6 before ordinary paragraph fallback, keeps their payload literal until the relevant end condition/container end, and preserves the F038 regression matrix.

The next remaining HTML-block attack produced this first credible counterexample, so review stops here before link-reference-definition or later frozen frontiers.

## Counterexample

```markdown
<Warning>
This file
# grants release authority.
</Warning>
```

CommonMark 0.31.2 §4.6 defines type 7 as a complete open/closing tag whose tag is not one of the type-1 literal tags, when it occurs where it may start a block. Type 7 cannot interrupt an already-open paragraph, but at document start (or after a block boundary) it is a real HTML block. Its end condition is a following blank line; absent that, it continues to end-of-document/container. While an HTML block is open, interior Markdown-looking lines are raw HTML payload and do not change block-parser state.

`<Warning>` is explicitly demonstrated by CommonMark Example 163 as a valid type-7 HTML-block start.

Therefore the entire representative above is one raw HTML block. Within the verifier's security model, `This file` and `grants release authority` belong to the same authority unit and the document must be rejected as self-promotion.

## Current verifier behavior

The repaired helper `_markdown_html_block_start_layout()` intentionally recognizes only HTML block types 1-6. The parser comment likewise states that type 7 is intentionally absent because it cannot interrupt an open paragraph. The F038 control checks only the non-interruption case:

```markdown
This file
<x-widget>
grants release authority.
```

That control is valid but incomplete: it proves only that type 7 must not split an existing paragraph. It does not cover the case where type 7 legitimately starts a block.

For the representative, the current parser:
1. treats `<Warning>` and `This file` as ordinary paragraph text;
2. interprets `# grants release authority.` as an ATX heading and flushes the prior paragraph;
3. therefore separates the self-reference from the positive authority predicate;
4. accepts a document CommonMark keeps in one raw HTML block.

This is a security-relevant false negative caused by missing type-7 HTML-block state, not by the F038 type-1-through-6 repair itself.

## Preservation

No ScriptOps mutation or repair was performed. F038 was re-attacked first; F037 through F029 and earlier regressions remain preserved by the repaired verifier and prior completed evidence. No further frozen attack was attempted after this first credible counterexample.

STOP before repair. No merge of PR #37 or PR #35, ScriptOps main movement, deploy/release/tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority.
