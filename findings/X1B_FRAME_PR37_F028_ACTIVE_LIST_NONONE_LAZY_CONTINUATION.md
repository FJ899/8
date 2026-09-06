# X1B-FRAME-F001-IMPLEMENTATION-F028

## Finding

The post-F027 independent read-only review authorized by FJ899/8 PR #291 found its first credible counterexample after F027 and F026 had no credible counterexample.

Exact reviewed ScriptOps binding:
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `0f7d34476c33fdc0e530f22e3168791c600c17e1`
- TREE `615af6e036dd1f6beaa818713984a2c18b1ee475`
- verifier blob `9292d0e637229c0d87b57519a6a10fd3cb5d8df3`

## Counterexample

```md
- This file
2. grants release authority.
```

Under CommonMark 0.31.2, an ordered list item interrupting an active paragraph must start with number `1`. Therefore `2. grants release authority.` is paragraph continuation text in this position, not a new ordered-list item. CommonMark laziness permits paragraph-continuation indentation inside a list item to be partially or completely removed, so the two physical lines above remain one bullet-list-item paragraph/security path.

The intended combined authority unit normalizes to wording containing both `THIS FILE` and `GRANTS` / `AUTHORITY` and must be rejected.

## Current verifier behavior

`_markdown_list_item_layout()` correctly marks a non-one ordered item as unable to interrupt an ordinary paragraph. However `_authority_soft_wrapped_units()` applies that guard only when `paragraph` is active and `list_frames` is empty:

```python
if paragraph and not list_frames and not can_interrupt_paragraph:
    paragraph.append(stripped)
    blank_seen = False
    continue
```

When the first line has already opened a bullet `list_frame`, the second physical line `2. grants release authority.` is recognized as a list marker with the same marker indentation as the active frame. The active-list branch therefore emits the parent path, pops it as a sibling/ancestor boundary, and starts a new frame instead of treating the line as lazy paragraph continuation of the current item.

Exact parser behavior for the counterexample is:

```text
['- This file', '2. grants release authority.']
```

The first authority unit contains the self-reference without the promotion; the second contains the promotion without the self-reference. `layer_b_self_promotion_claim()` therefore returns no claim: a subject/predicate false negative.

## Security impact

A Layer-B Markdown document can split a self-referential authority promotion across a bullet-list paragraph and a same-column non-one ordered-looking lazy continuation line. CommonMark keeps the wording in one list-item paragraph, while the verifier creates a false security boundary.

Representative affected starts include `0.`, `2.`, `42.`, and other non-one ordered markers that cannot interrupt the active paragraph.

## Review disposition

- F027: reviewed; no credible counterexample before this point.
- F026: reviewed; no credible counterexample before this point.
- F025: first credible counterexample found in its active-list/laziness interaction; finding recorded as F028.
- F024-F006 and Q5-Q15: NOT reviewed in this review run.

Immediate STOP under PR #291 authority.

No repair, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, PR35 integration, X1B reopen or V1 authority is granted by this finding.
