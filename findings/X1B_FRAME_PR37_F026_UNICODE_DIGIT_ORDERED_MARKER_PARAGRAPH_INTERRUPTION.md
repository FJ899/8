# X1B-FRAME-F001-IMPLEMENTATION-F026

## Status

OPEN FINDING / review STOP

## Review authority

Durable HumanDecision authority: `FJ899/8 PR #281`.

Exact reviewed ScriptOps target:

- PR `FJ899/scriptops #37`
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `e91a6b1f5754d2807920c35221fd105de57b1d87`
- TREE `f38bc8f73f12e3d6b966fff625a9c180be3e69b4`
- PATH `scripts/verify_repository.py`
- BLOB `16f59bd1440dcdf9fc5800ba70efc5e1e27ef9d0`

Review order required F025 first. This finding was discovered during F025 review; F024-F006 and Q5-Q15 were not reached.

## Counterexample

```md
This file
١. grants release authority.
```

The first character of the second line is ARABIC-INDIC DIGIT ONE (`U+0661`), not ASCII `1` (`U+0031`).

CommonMark 0.31.2 defines an ordered list marker as 1-9 ASCII arabic digits `0-9` followed by `.` or `)`. Therefore `١.` is not a CommonMark ordered list marker. In this position the second physical line remains ordinary paragraph continuation text, so the self-reference and promotion belong to one paragraph/security unit.

The intended normalized authority relationship is equivalent to:

```text
THIS FILE ١ GRANTS RELEASE AUTHORITY
```

and must be rejected.

## Implementation cause

`_markdown_list_item_layout()` currently uses Python regex `\d{1,9}`:

```python
r"^(?P<indent>[ \t]*)(?P<marker>[-+*]|\d{1,9}[.)])(?:(?P<gap>[ \t]+)|$)"
```

Python `\d` is Unicode-aware and matches Unicode decimal digits, not only ASCII `0-9`. The implementation then computes:

```python
ordered_start = int(marker[:-1]) if marker[0].isdigit() else None
can_interrupt_paragraph = (
    not empty_item
    and (ordered_start is None or ordered_start == 1)
)
```

For `١.` Python accepts the digit as numeric one, so the verifier classifies the line as an ordered start-1 marker that may interrupt an active paragraph.

Exact reproduction of the reviewed parser produces:

```text
['This file', '١. grants release authority.']
```

instead of one paragraph authority unit.

The first unit contains self-reference but no promotion; the second contains promotion but no self-reference. `layer_b_self_promotion_claim()` therefore misses the positive self-promotion even though CommonMark keeps the wording in one paragraph.

The same mechanism is reproducible with other Unicode decimal digit forms whose numeric value is one, including FULLWIDTH DIGIT ONE (`１`) and DEVANAGARI DIGIT ONE (`१`).

## Security significance

This is a non-vacuous false-negative subject/predicate bypass introduced/preserved at the F025 ordered-list paragraph-interruption boundary. A Unicode decimal digit visually or semantically resembling an ordered marker can cause the verifier to invent a list boundary that CommonMark does not have.

## Required disposition

Per PR #281 review authority: durable finding + immediate STOP.

F024-F006 and Q5-Q15 were not reviewed after this first credible counterexample. No repair, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, PR35 integration, X1B reopen, or V1 action is authorized by this finding.
