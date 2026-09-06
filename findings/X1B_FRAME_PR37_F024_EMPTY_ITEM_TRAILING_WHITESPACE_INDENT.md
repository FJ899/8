# X1B-FRAME-F001-IMPLEMENTATION-F024

## Status

OPEN FINDING / review STOP

## Review authority

Durable HumanDecision authority: `FJ899/8 PR #271`.

Exact reviewed ScriptOps target:

- PR `FJ899/scriptops #37`
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `beba918e23b3b98c8324c8b735265ca8931db562`
- TREE `f2026d57aad61dd08b175cdedba20087b7598720`
- PATH `scripts/verify_repository.py`
- BLOB `020c4ebe4ce2073c6172d316ad8a582a26832f46`

Review order required F023 first. This finding was discovered during F023 review; later review items were not reached.

## Counterexample

Exact text bytes, expressed as a Python-style escaped string so trailing spaces are unambiguous:

```text
"-    \n  This file contains background notes.\n\n  therefore grants release authority.\n"
```

The first line is a bullet marker followed by four spaces and then end-of-line. Under CommonMark 0.31.2, this is a list item starting with a blank line. For such an item, the number of spaces following the list marker does not change the required indentation; subsequent lines need `W + 1` indentation. For bullet marker width `W = 1`, two leading spaces are sufficient. List items may contain multiple paragraphs separated by blank lines.

Therefore both indented paragraphs above belong to the same list item, and the self-reference in the first paragraph plus the positive authority promotion in the second paragraph must remain within one security unit.

## Implementation cause

Current `_markdown_list_item_layout()` returns `(marker_indent, content_indent, empty_item)`.

For marker-only items with no gap it special-cases `content_indent = marker_indent + marker_width + 1`. But when trailing whitespace exists, it instead computes:

```python
content_indent = len(raw_line[:match.end()].expandtabs(4))
```

For `"-    "`, that yields `content_indent = 5`, even though CommonMark rule 3 requires subsequent content indentation of only `W + 1 = 2` for an item starting with a blank line.

`_authority_soft_wrapped_units()` then behaves as follows:

1. the empty marker opens a frame with `content_indent = 5`;
2. the first two-space-indented paragraph is absorbed because there has not yet been a physical blank line and the implementation allows lazy continuation;
3. after the physical blank line, the second two-space-indented paragraph has `leading = 2 < 5`;
4. the active list path is emitted and popped before the second paragraph;
5. the authority unit is therefore split into:

```text
- This file contains background notes.
```

and

```text
therefore grants release authority.
```

No single unit contains both the self-reference and promotion, so `layer_b_self_promotion_claim()` fails to reject the text.

## Security significance

This is a non-vacuous false negative in the F023 boundary model. Trailing spaces or tabs after a valid empty list marker can inflate the stored content indentation and turn a later paragraph inside the same CommonMark list item into a separate authority unit, allowing subject/predicate separation across a blank line.

## Required disposition

Per PR #271 review authority: durable finding + immediate STOP.

No F022-F006 review and no Q5-Q15 review is authorized after this first credible counterexample in the same pass. No repair, merge, main movement, deployment, release, tag, canonical effect, status promotion, PR35 integration, X1B reopen, or V1 action is authorized by this finding.
