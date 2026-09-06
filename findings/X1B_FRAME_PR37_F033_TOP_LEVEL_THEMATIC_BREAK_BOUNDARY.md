# X1B-FRAME-F001-IMPLEMENTATION-F033 — top-level thematic-break boundary is not recognized

## Review authority

Independent post-repair adversarial review authorized by Human `accept` after F032 repair completion.

Exact review target:

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `5c32af7127000e86f33e9f0e79ac09de8441b49d`
- TREE: `456ef9210d74a24f8702c15b6c28c244328e02ad`
- verifier blob: `f3d196b6712037b4fda08fc6f40888c6c663c3ca`
- F032 completion evidence: `FJ899/8 PR #312`

Review order was preserved: re-attack F032 first, preserve F031/F030/F029 and earlier regressions, then continue frozen structural attacks until the first credible counterexample.

## Re-attack / preservation disposition before F033

F032 survives its representative list-context thematic-break attack. F031 lazy continuation remains represented separately from structural list boundaries; F030 same-level cross-family/delimiter separation and F029 ancestor-level separation remain present. No repair was attempted during review.

## First credible counterexample

```markdown
This file
***
grants release authority.
```

CommonMark parses this as three blocks:

1. paragraph `This file`
2. thematic break `***`
3. paragraph `grants release authority.`

Thematic breaks can interrupt an ordinary paragraph without blank lines before or after. See CommonMark Spec section 4.1, e.g. current Example 58: `Foo / *** / bar` -> paragraph, thematic break, paragraph.

## Why the repaired verifier is wrong

The F032 repair added `_markdown_thematic_break_layout()`, but `_authority_soft_wrapped_units()` applies thematic-break boundary handling only under:

```python
if list_frames and thematic is not None:
```

When no list is active, the recognized thematic break is ignored. `_markdown_list_item_layout("***")` also returns no list item, so the fallback ordinary-paragraph path appends all three physical lines to one authority unit.

The verifier therefore evaluates an authority unit equivalent to:

```text
This file *** grants release authority.
```

and falsely donates the self-reference from the first paragraph across a real thematic-break block boundary to the later unrelated paragraph.

## Security / correctness impact

This is a structural false-positive / false-promotion: distinct CommonMark blocks are collapsed into one security authority unit. It is the same class of boundary-integrity failure that motivated F029/F030/F032, now exposed outside list context.

The defect is generic. Equivalent examples include top-level `___` and unambiguous spaced dash thematic breaks such as `- - -`; dash-only `---` retains Setext-heading precedence and is not needed for this finding.

## Disposition

`FAIL — FIRST CREDIBLE COUNTEREXAMPLE`

Mandatory STOP before repair.

No mutation to `FJ899/scriptops`, no merge of PR #37 or PR #35, no ScriptOps main movement, deploy/release/tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority is granted by this finding.
