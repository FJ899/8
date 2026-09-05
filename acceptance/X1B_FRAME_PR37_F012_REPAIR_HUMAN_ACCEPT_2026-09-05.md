# X1B-FRAME PR #37 — F012 Human acceptance and bounded repair authority

Date: 2026-09-05

## Human decision

Human accepted the exact durable finding recorded in `FJ899/8 PR #222`:

`X1B-FRAME-F001-IMPLEMENTATION-F012 — MIXED-CLAUSE NEGATION MASKS POSITIVE LAYER-B SELF-PROMOTION`

This record authorizes exactly one bounded replacement repair of existing `FJ899/scriptops PR #37` for F012.

## Exact target binding

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- current pre-repair HEAD: `d9dd915cb7e8e66388b191f4a68ade58c301b096`
- current pre-repair TREE: `fa523574e9e87fbc5358d9cba706ce66f8455d43`
- finding authority: `FJ899/8 PR #222`
- review authority that produced F012: `FJ899/8 PR #221`
- superseding frozen plan: `FJ899/8 PR #201`
- plan-review PASS: `FJ899/8 PR #202`

## Authorized repair surface

Exactly one bounded replacement repair is authorized.

Requirements:

1. PR #37 must remain exactly one commit over frozen BASE `2f22843ac570498b506101addeba5453ab777f08`.
2. Base-relative changed paths must remain the same frozen twelve-path implementation surface.
3. Relative to pre-repair HEAD `d9dd915c...`, only `scripts/verify_repository.py` may change.
4. The repair must close F012 by preventing a valid negative authority phrase from masking a distinct positive self-promotion in the same clause.
5. The repair must preserve F011 valid-negation handling, F010 inert technical `binding` handling, F009 free-form self-promotion rejection, and F008/F007/F006 regressions.
6. The correction must not merely special-case the exact review sentence; it must enforce promotion-level/local-negation semantics so mixed positive and negative authority assertions cannot collapse into a whole-clause allow.
7. Existing green repository verification and Phase-6 deterministic regression behavior must be preserved.

## Explicit non-authority

This Human acceptance does **not** authorize:

- merge of PR #37;
- any ScriptOps `main` movement;
- PR #35 merge/rebase/cherry-pick or integration;
- deployment, release, or tag;
- canonical effect execution;
- active-product status promotion;
- X1B reopen;
- V1 authority;
- any second repair after this bounded repair.

After the repair and CI, a fresh independent read-only re-review requires a separate Human gate.

`AI PROPOSES != HUMAN DECIDES`
