# X1B-FRAME — post-F043-multiline adversarial review finding

Date: 2026-09-07

Review authority: `FJ899/8 PR #378`.

Reviewed candidate:

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `3a9bac7b36be067999717b0819137c6a9524b063`
- TREE: `3402de92c468cd90b0b82c8bb48e63b2c15e408f`
- verifier entrypoint blob: `c2b5a356e744be802d204ab8eaea901e76aa1219`
- pinned prior F043 overlay blob: `61bf107ad59da33a6576032d341b41c538d0453a`
- pinned F041 core blob: `be645c1a3ee49a04d700a3ef7fde86a92e413a14`

## Disposition

`FAIL — FIRST CREDIBLE COUNTEREXAMPLE`

The review re-attacked F043 first and stopped at the first credible counterexample. No repair was performed.

## Finding

Same F043 root cause family: incomplete CommonMark §4.7 multiline definition extraction in a list container when continuation lines use valid list-item laziness.

Representative:

```markdown
- [
This file
]: /url
grants release authority.
```

Normative block semantics:

1. The first line opens a list item whose paragraph candidate begins with `[`.
2. CommonMark list-item laziness permits deletion of item indentation from paragraph continuation lines.
3. `This file` and `]: /url` therefore continue that list-item paragraph candidate despite lacking the nominal content indent.
4. CommonMark §4.7 recognizes the resulting multiline link-reference definition at the beginning of that paragraph candidate and extracts it; link-reference definitions are allowed inside block containers.
5. After extraction the list item has no remaining paragraph content, so the following unindented `grants release authority.` is a separate top-level paragraph.
6. The definition contains the self-reference only; the later paragraph contains the promotion only. The document must not be rejected for combined self-promotion.

Current verifier mechanism:

- `_try_fold_list_marker_definition()` requires every continuation line to survive `_markdown_remove_leading_columns(..., content_indent)`.
- Valid lazy continuation with less indentation therefore aborts multiline folding before a valid definition can be recognized.
- `_try_fold_plain_definition()` cannot recover because the first physical line begins with the list marker, not `[`.
- The pinned single-line F043 parser then preserves its earlier F031 behavior: while a list-item paragraph remains open, ordinary unindented nonblock lines are appended as lazy continuation.
- Because the definition was never extracted, `- [`, `This file`, `]: /url`, and `grants release authority.` are accumulated into one list-item authority unit.
- The Layer-B self-promotion validator therefore sees `THIS FILE` together with `grants release authority` and produces a false positive.

This is not F042 and not F044. It is a direct F043 container-relative multiline extraction failure exposed by already-established list lazy-continuation semantics.

## Preserved outstanding findings

- F042 — OPEN / unrepaired.
- F044 — OPEN / unrepaired.

## Stop rule

Review stopped at this finding. No repair, merge, ScriptOps `main` movement, deploy/release/tag, canonical effect, active-product status promotion, X1B reopen, or V1 action was performed or authorized.
