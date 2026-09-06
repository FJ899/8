# X1B-FRAME PR #37 — F032 thematic-break boundary false-promotion

## Exact review binding

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- reviewed HEAD: `841ecbf18f346becb4baf4bb11a31eaf391975eb`
- reviewed TREE: `c127542b6aaac202ac4fa7a96a4026b76455efca`
- reviewed verifier blob: `5fb041541b4c80c00f94b8c32ec2a3aa96389864`
- Human post-repair review authority: `FJ899/8 PR #306`
- repair-completion evidence: `FJ899/8 PR #305`

Review is read-only with respect to ScriptOps. This file records the first credible counterexample found after the authorized F031 post-repair review began.

## Required review order

The repaired verifier was first re-attacked on F031 lazy paragraph continuation semantics, then the F030/F029 structural-boundary controls and earlier frozen regressions were preserved. The exact repaired F031 positive shapes remain rejected as intended, while the F029/F030 benign boundary shapes remain accepted as intended.

The review then continued to the next Markdown block-boundary attack.

## Finding ID

`X1B-FRAME-F001-IMPLEMENTATION-F032`

## Counterexample

```markdown
- This file
---
grants release authority.
```

## Expected CommonMark structure

This is not one lazy list-item paragraph.

The first line is a bullet-list item containing the paragraph `This file`. The `---` line is a thematic break at top level, which closes the list. The following `grants release authority.` line is a separate top-level paragraph.

The official CommonMark specification explicitly demonstrates the same structural transition in its thematic-break examples: `- Foo` followed immediately by `---` renders as a list followed by a thematic break. CommonMark laziness applies only when the de-indented continuation line is paragraph-continuation text; a thematic break is a block boundary, not lazy paragraph continuation.

Therefore the self-reference in the list item must not be donated across the thematic break to the later top-level paragraph.

## Actual repaired-verifier behavior

In `_authority_soft_wrapped_units()` the F031 repair now keeps every nonblank non-list-marker line inside the active list frame when no blank line was seen:

```python
if list_frames:
    # Without a blank line, Markdown permits lazy continuation text.
    # After a blank, ownership was already resolved above.
    list_frames[-1][2].append(stripped)
    blank_seen = False
    continue
```

The verifier does not recognize thematic-break lines as a block boundary. For the counterexample above, the repaired folding path produces one authority unit equivalent to:

```text
- This file --- grants release authority.
```

`layer_b_self_promotion_claim()` then sees `THIS FILE` plus `GRANTS`/`AUTHORITY` in that manufactured unit and returns a forbidden self-promotion claim.

So a CommonMark document whose self-reference and authority predicate are in distinct top-level blocks is falsely rejected.

## Why this is credible

This is the same correctness class as F029/F030: structural Markdown boundaries must prevent unrelated later text from borrowing an earlier self-reference. F031 correctly restored true lazy paragraph continuation, but its unconditional nonblank fallback is broader than CommonMark laziness and collapses non-list block interrupters as if they were lazy paragraph text.

The counterexample requires no unusual Unicode, malformed Markdown, or parser-specific extension. It uses only a bullet item, a standard CommonMark thematic break, and a following paragraph.

## Scope consequence

Post-repair review disposition: **FAIL at first credible counterexample**.

No repair is authorized by this finding. Do not modify `FJ899/scriptops PR #37` under review authority.

Any future repair must preserve F031 true unindented/partially-dedented lazy continuation, F030 same-level cross-family/delimiter boundaries, F029 ancestor-level boundaries, and all earlier frozen regressions, while distinguishing paragraph-continuation text from CommonMark block interrupters.

## STOP boundary

STOP before repair. Separate Human authorization is required for any F032 repair work.

No merge of PR #37 or PR #35, no ScriptOps main movement, no deploy/release/tag, no canonical effect, no active-product status promotion, no X1B reopen, and no V1 authority is granted by this finding.
