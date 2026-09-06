# X1B-FRAME-F001-IMPLEMENTATION-F027

## Status

OPEN FINDING — first credible counterexample from the Human-authorized post-F026 independent read-only review.

Review authority: `FJ899/8 PR #286`.

Exact reviewed ScriptOps binding:

- PR `FJ899/scriptops #37`
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `72f1e00c45a58c107a4e4f2a90cccd92fa76cbe9`
- TREE `9b9f858d2b505809332e85c6cbf506d8f031a441`
- verifier blob `914ff100f03b23268a0a96db57103727e912a569`

## Finding

The Markdown authority-unit parser mishandles a CommonMark list item whose first block is an indented code block. It counts the entire physical post-marker whitespace as the item's ownership indentation, although CommonMark's indented-code-start rule uses one post-marker space and therefore requires only `W + 1` indentation for subsequent blocks in the same item.

Exact counterexample:

```text
1.     This file

   grants release authority.
```

For marker `1.` the marker width is `W = 2`. The five literal spaces after the marker represent one list-item indentation space plus the four spaces that start the indented code block. The later three-space-indented paragraph therefore remains inside the same CommonMark list item.

The reviewed verifier instead matches all post-marker whitespace and computes:

```python
content_indent = len(raw_line[:match.end()].expandtabs(4))
```

For the first line this yields `content_indent = 7`. After the blank line, the next line has leading indentation `3`, so the parser executes the blank-line ownership pop path because `3 < 7`.

Observed security units under the reviewed parser:

```text
['1.     This file', 'grants release authority.']
```

The first unit contains the self-reference but not the promotion. The second contains the promotion but not the self-reference. `layer_b_self_promotion_claim()` therefore returns no claim, creating a subject/predicate false negative.

A CommonMark parser resolves the same source as one ordered list item containing an indented code block `This file` followed by a paragraph `grants release authority.`. Under the verifier's own list-item-path security model these blocks must not be separated into unrelated authority units merely because the first block is code-indented.

## Root cause

`_markdown_list_item_layout()` has only two ownership-indentation cases:

1. empty item -> `marker_indent + marker_width + 1`;
2. every nonempty item -> physical width through the entire matched gap.

That omits CommonMark's distinct "item starting with indented code" rule. A gap large enough to encode the initial four-space code indentation is incorrectly treated as part of the list item's structural ownership indentation.

## Required future repair boundary

Any future bounded repair should distinguish the indented-code-start case from the ordinary 1-4-space first-block case, preserve F026 ASCII-only ordered markers and F025 paragraph-interruption semantics, add non-vacuous positive and benign regressions for bullet and ordered indented-code-start items, preserve F026-F006, and retain the exact one-replacement-commit/frozen-12-path topology.

This finding does not itself authorize repair.

## Review stop

This was the first credible counterexample at checkpoint F026.

Immediate STOP under PR #286 authority. F025 through F006 and Q5-Q15 were not reviewed. No repair, merge, ScriptOps main movement, deployment, release, tag, canonical effect, active-product status promotion, PR35 integration, X1B reopen or V1 action is authorized.
