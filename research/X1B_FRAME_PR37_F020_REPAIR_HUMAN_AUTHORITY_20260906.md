# X1B-FRAME PR37 F020 repair Human authority

Human acceptance source: user `accept` in the governing Sedzia session on 2026-09-06.

Accepted finding: `X1B-FRAME-F001-IMPLEMENTATION-F020` as durably recorded in `FJ899/8 PR #251`.

## Exact pre-repair target

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `cdad32cdb9739b4baac30bfaf85b85b4f19056ea`
- TREE: `3c8fa40fb3885597e2348e3d9c75b8f74ef6404a`
- verifier path: `scripts/verify_repository.py`
- verifier blob: `ac18d2951f17e83ca38ca9b9a092f619e12cbcb6`

## Authorized repair

Exactly one bounded replacement repair of existing PR #37 is authorized.

The repair must:

1. remain exactly one commit over frozen BASE `2f22843ac570498b506101addeba5453ab777f08`;
2. preserve the exact frozen 12 base-relative changed paths;
3. relative to pre-repair HEAD `cdad32cdb9739b4baac30bfaf85b85b4f19056ea`, change only `scripts/verify_repository.py`;
4. close F020 by treating nested sibling Markdown list items as separate authority units while still joining continuation paragraphs that belong to the same list item;
5. preserve F019 through F006 behavior and existing runtime/status separations;
6. add non-vacuous production-validator regressions covering nested sibling benign separation, nested continuation positive rejection, ordered/unordered nesting where relevant, and benign negation;
7. run the repository verifier and both existing PR workflows successfully;
8. update only the existing PR #37 branch with stale-head protection and freeze the repaired identifiers;
9. STOP after repair completion evidence.

## Explicit non-authority

This acceptance does not authorize merge, ScriptOps `main` movement, PR #35 integration, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen, V1 authority, or post-repair independent re-review.

`REPAIR AUTHORITY != REVIEW AUTHORITY`
`REPAIR AUTHORITY != MERGE AUTHORITY`
