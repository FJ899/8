# X1B-FRAME-F001-IMPLEMENTATION-F020

Independent post-F019 re-review under Human authority `FJ899/8 PR #250` found the first credible counterexample at F019 and STOPPED.

Exact reviewed ScriptOps candidate:

- PR: `FJ899/scriptops PR #37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `cdad32cdb9739b4baac30bfaf85b85b4f19056ea`
- TREE: `3c8fa40fb3885597e2348e3d9c75b8f74ef6404a`
- verifier blob: `ac18d2951f17e83ca38ca9b9a092f619e12cbcb6`

## Finding

`X1B-FRAME-F001-IMPLEMENTATION-F020` — nested sibling Markdown list items are incorrectly merged into one authority unit by the F019 list-state repair.

Counterexample raw Markdown:

```text
- Parent context:
  - This file contains background notes.

  - Release authority belongs to a separate Human gate.
```

The two nested bullets are siblings and are semantically independent. This is the same benign sibling pattern exercised by the F019 top-level regression, merely nested one level deeper.

In `_authority_soft_wrapped_units()` the initial top-level list item establishes `list_marker_indent = 0` and `list_content_indent = 2`. Each nested bullet has `layout[0] = 2`, so the sibling check `layout[0] <= list_marker_indent` is false. The parser therefore never adopts the nested list-item context. After the blank line, the second nested sibling has leading indentation `2`, which is not less than the still-active parent `list_content_indent = 2`, so it is appended to the same pending unit.

The clause-level pass sees self-reference only in the first nested sibling and `AUTHORITY` only in the second. The F016 whole-unit fallback then sees both in the incorrectly merged unit and rejects the benign text as forbidden self-promotion.

Therefore the F019 claim that sibling list items remain separate is incomplete for nested sibling items, and the required benign/list-adjacent safety coverage is not closed.

Per the Human gate, no F018-F006 or Q5-Q15 review was performed after this first counterexample.

No repair, merge, ScriptOps main movement, PR #35 integration, deployment/release/tag, canonical effect, active-product status promotion, X1B reopen or V1 authority is granted by this finding.
