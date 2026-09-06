# X1B-FRAME-F001-IMPLEMENTATION-F018

## Review authority

Independent post-F017 read-only re-review under Human authority `FJ899/8 PR #241`.

Exact candidate reviewed:

- repo `FJ899/scriptops`
- PR `#37`
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `467a4d1be44f11cbfa8ada85885397b4c7283d40`
- TREE `d7ab8679065844e93d979b0712f5eadb4b73758a`
- verifier blob `178881c7fe485b054a265462b908d69ff44bb9a6`

## Finding

F017 is incomplete: `_authority_soft_wrapped_units()` treats any nonblank physical line whose stripped tail ends in `.`, `!`, or `?` as a hard sentence boundary. That allows a normal Markdown soft line break after an ellipsis to split a self-referential subject from its positive authority predicate.

Counterexample:

```text
This file...
therefore grants release authority.
```

This is one Markdown paragraph with a soft line break and reads as the positive self-promotion `This file... therefore grants release authority.`

The production path behaves as follows:

1. `_authority_soft_wrapped_units()` receives `This file...`, sees a tail ending in `.`, emits it as a complete unit, and clears `pending`.
2. `therefore grants release authority.` becomes a second unit.
3. In the first unit, `THIS FILE` is self-referential but there is no promotion term.
4. In the second unit, `GRANTS` / `AUTHORITY` are promotion terms but there is no self-reference.
5. The F016 whole-unit fallback is still scoped to each emitted unit, so it also cannot reconnect the subject and predicate.
6. `layer_b_self_promotion_claim()` therefore returns no claim for this positive self-promotion.

Finding class: Markdown soft-wrap boundary classification / F017 repair incomplete.

## Disposition

`FAIL / FIRST CREDIBLE COUNTEREXAMPLE`

Review STOPPED immediately at F017. F016-F006 and Q5-Q15 were not reviewed under this authorization.

No repair, merge, ScriptOps main movement, PR35 integration, deployment/release/tag, canonical effect, active-product status promotion, X1B reopen, V1 authority, or further independent re-review is authorized by this finding.