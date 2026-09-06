# X1B-FRAME-F001-IMPLEMENTATION-F019

## Target

Independent post-F018 re-review under Human authority recorded in `FJ899/8 PR #245`.

Exact reviewed candidate:

- `FJ899/scriptops PR #37`
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `ba8d80ac0ff5272e8e25e27145f53dd81b1ed7bd`
- TREE `07cadd354b127d39957e0e16ebed5031c94cfdc4`
- verifier blob `3b9955967635a37d4453d0a2ae449ad341392e23`

## Finding

F018 still permits a Markdown-structural subject/predicate fragmentation bypass when a blank physical line occurs inside one list item.

Counterexample raw Markdown:

```text
- This file...

  therefore grants release authority.
```

The two nonblank fragments remain paragraphs of the same Markdown list item, so the second paragraph is a continuation of the same bullet-level declaration. However `_authority_soft_wrapped_units()` flushes `pending` on every physically blank line.

It therefore produces two authority units:

1. `- This file...` — self-reference without promotion;
2. `therefore grants release authority.` — promotion without self-reference.

`layer_b_self_promotion_claim()` evaluates the units independently, so neither unit satisfies both predicates and the production Layer-B validator accepts the combined same-list-item self-promotion.

This is the first credible counterexample in the authorized order, at F018.

## Disposition

`FAIL / DURABLE FINDING / STOP`

No F017-F006 or Q5-Q15 review was performed after this first counterexample.

No repair, merge, ScriptOps main movement, PR35 integration, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen, V1 authority, or further review authority is granted by this record.
