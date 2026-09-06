# X1B-FRAME-F001-IMPLEMENTATION-F025

## Status

OPEN FINDING / review STOP

## Review authority

Durable HumanDecision authority: `FJ899/8 PR #276`.

Exact reviewed ScriptOps target:

- PR `FJ899/scriptops #37`
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `f75a55fd1923d115f3194827e8c0017a58587f60`
- TREE `c2e90eba0b074298820960fd33db81a155633d4a`
- PATH `scripts/verify_repository.py`
- BLOB `e7c94abbf62342a360fc96d2c7ac07175c5d872e`

Review order required F024 first, then F023. F024 produced no credible counterexample. This finding was discovered during F023 review; later review items were not reached.

## Counterexample

```md
This file
2. grants release authority.
```

Under CommonMark 0.31.2, an ordered list may interrupt an active paragraph only when the first item starts with `1`. A line beginning with `2.` in this position is paragraph continuation text. Therefore the two physical lines above form one paragraph and must remain one security unit for self-promotion detection.

The intended normalized authority relationship is:

```text
THIS FILE 2 GRANTS RELEASE AUTHORITY
```

which contains both the self-reference and a positive promotion predicate and must be rejected.

## Implementation cause

`_markdown_list_item_layout()` recognizes every 1-9 digit ordered marker matching `\d{1,9}[.)]` without carrying the ordered start number or paragraph-interruption admissibility into `_authority_soft_wrapped_units()`.

The only paragraph-interruption guard introduced for F023 is:

```python
if empty_item and paragraph and not list_frames:
    paragraph.append(stripped)
    blank_seen = False
    continue
```

That guard covers marker-only empty items, but not nonempty ordered markers whose start number is not `1`.

For the counterexample, the current implementation therefore produces two authority units:

```text
This file
```

and

```text
2. grants release authority.
```

The first unit has self-reference but no promotion; the second has promotion but no self-reference. `layer_b_self_promotion_claim()` therefore does not reject the text, even though CommonMark keeps the text in one paragraph.

## Security significance

This is a non-vacuous false-negative subject/predicate bypass in the F023 paragraph-interruption boundary model. Any nonempty ordered marker beginning with `2` through `999999999` can be used at a physical soft wrap to split a self-reference from a later authority promotion even though CommonMark does not start a list there.

## Required disposition

Per PR #276 review authority: durable finding + immediate STOP.

F022-F006 and Q5-Q15 were not reviewed after this first credible counterexample. No repair, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, PR35 integration, X1B reopen, or V1 action is authorized by this finding.
