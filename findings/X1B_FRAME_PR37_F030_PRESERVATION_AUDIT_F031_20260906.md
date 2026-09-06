# X1B-FRAME PR37 F030 PRESERVATION AUDIT — F031 — 2026-09-06

Disposition: **NOT PASS — first credible preservation counterexample. STOP.**

Audit target:
- `FJ899/scriptops PR #37`
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `0f7d34476c33fdc0e530f22e3168791c600c17e1`
- verifier blob `9292d0e637229c0d87b57519a6a10fd3cb5d8df3`
- amended repair authority `FJ899/8 PR #299`
- amended repair specification `FJ899/8 PR #300`

Finding: `X1B-FRAME-F001-IMPLEMENTATION-F031`.

## Counterexample

Representative Markdown:

```text
- This file
grants release authority.
```

CommonMark treats the second physical line as a lazy continuation of the paragraph inside the same bullet item even though the continuation indentation has been completely removed. A CommonMark-mode reference parse therefore produces one list-item paragraph containing both `This file` and `grants release authority.`

The current frozen verifier also keeps these two physical lines in one active list-frame authority unit.

PR #300 step 3, however, requires content-ownership unwind for **every nonblank incoming line** before marker classification: while `leading < current_leaf.content_indent`, emit/pop frames. For the second line above, `leading = 0` and the bullet item content indentation is `2`, so the proposed rule closes the bullet frame before the continuation text is processed. The self-reference and authority predicate are then evaluated as separate security units.

Result: the amended F030 repair direction reopens a subject/predicate false negative through ordinary CommonMark lazy continuation. This violates the explicit preservation requirement for F027-F006 and cuts away behavior that current F017/F019-style folding relies on.

The same defect persists in nested form, e.g. a nested bullet paragraph whose continuation lazily dedents below the child content indentation.

## Preservation implication

`content_indent` cannot be used as an unconditional ownership-pop boundary for all nonblank lines. Before unwinding an active list item, the repair must distinguish paragraph lazy-continuation text from structural block starts/markers that actually terminate or rebind ownership. In other words, indentation ownership and laziness must be resolved together; unconditional dedent-pop is not semantics-preserving.

This finding does **not** authorize a replacement repair design. A new Human gate is required before changing the already-authorized F030 repair direction.

## Boundary

No mutation to `FJ899/scriptops PR #37` occurred during this audit. No patch was queued or applied. No merge, ScriptOps main movement, PR #35 integration, deploy/release/tag, canonical effect, status promotion, X1B reopen or V1 authority is granted.
