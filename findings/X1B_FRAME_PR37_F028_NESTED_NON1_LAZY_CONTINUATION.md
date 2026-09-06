# X1B-FRAME-F001-IMPLEMENTATION-F028

## Status

OPEN finding from the Human-authorized post-F027 independent read-only review.

Review authority: `FJ899/8 PR #291`.

Exact reviewed ScriptOps binding:

- PR: `FJ899/scriptops PR #37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `0f7d34476c33fdc0e530f22e3168791c600c17e1`
- TREE: `615af6e036dd1f6beaa818713984a2c18b1ee475`
- verifier blob: `9292d0e637229c0d87b57519a6a10fd3cb5d8df3`

## Review position

F027 and F026 produced no earlier credible counterexample. The first credible counterexample was found while reviewing F025 interaction with an already-active list frame. Review STOPPED immediately. F024-F006 and Q5-Q15 were not reviewed.

## Counterexample

```markdown
- Parent
  10. This file
  2. grants release authority.
```

## Normative CommonMark basis

CommonMark 0.31.2 states that when a first ordered list item would interrupt an active paragraph, its start number must be `1`. It also defines lazy continuation lines: indentation may be omitted from lines whose next non-whitespace content is paragraph continuation text while preserving the same list-item contents.

Therefore, inside the already-open bullet item, `10. This file` does not start a nested ordered list because ordered start `10` cannot interrupt the active paragraph `Parent`. It is paragraph continuation text. The following `2. grants release authority.` likewise cannot interrupt that same paragraph. The three physical lines are one bullet-list-item paragraph/security unit.

A conforming CommonMark parse is structurally equivalent to:

```html
<ul>
<li>Parent
10. This file
2. grants release authority.</li>
</ul>
```

## Exact verifier mechanism

The reviewed verifier correctly computes `can_interrupt_paragraph = False` for non-one ordered markers, but only applies that guard when an ordinary top-level `paragraph` is active:

```python
if paragraph and not list_frames and not can_interrupt_paragraph:
    paragraph.append(stripped)
    blank_seen = False
    continue
```

When `list_frames` is already active, the guard is skipped entirely. A recognized deeper marker is therefore treated as a descendant list frame even when CommonMark says it is paragraph continuation text. A later marker at the same nested marker indentation is then treated as a sibling and forces emission of the prior active path.

For the counterexample, the reviewed `_authority_soft_wrapped_units()` logic produces:

```text
['- Parent 10. This file', '- Parent 2. grants release authority.']
```

instead of one logical unit containing both `This file` and `grants release authority.`.

## Security impact

This is a non-vacuous subject/predicate false negative. The first verifier unit contains the self-reference `THIS FILE` without the positive authority predicate. The second contains `GRANTS` / `RELEASE AUTHORITY` without the self-reference. `layer_b_self_promotion_claim()` therefore accepts text that CommonMark keeps inside one list-item paragraph and that, normalized as one security unit, should be rejected as self-promotion.

The bypass is not limited to the exact numbers `10` and `2`; it applies to nested non-one ordered markers encountered while a parent list frame is active and an existing paragraph would make them lazy continuation text rather than real nested list items.

## Required repair property

Any repair must preserve F027-F006 while ensuring paragraph-interruption semantics are enforced inside active list-item paragraphs, not only for the separate top-level `paragraph` buffer. A non-one ordered marker that CommonMark treats as lazy continuation text must remain in the current list-item paragraph/security path and must not create a descendant/sibling frame boundary.

## Gate consequence

Per PR #291 authority: first credible counterexample => durable finding + immediate STOP.

No repair, merge, ScriptOps main movement, deployment, release, tag, canonical effect, active-product status promotion, PR35 integration, X1B reopen or V1 action is authorized by this finding.
