# X1B-FRAME PR37 post-F016 independent review Human acceptance

Date: 2026-09-06

Human message accepted in the governing conversation:

> w porzadku accept na wczesniejsze ustalenia

This acceptance is interpreted narrowly as authority for exactly one independent read-only implementation re-review of the exact repaired `FJ899/scriptops PR #37` candidate below.

## Exact review target

- repository: `FJ899/scriptops`
- PR: `#37`
- base: `2f22843ac570498b506101addeba5453ab777f08`
- head: `a94a4018b469ae864e4715157f00b9d765df11c0`
- tree: `420faf0b06f4b53228770735f1504b3f58d5c580`
- verifier path: `scripts/verify_repository.py`
- verifier blob: `d7153ccdf4469c7355e9b6aa0926228a91e74c00`
- expected PR state at authorization: OPEN / DRAFT / UNMERGED
- expected base-relative shape: exactly one commit over frozen base and exactly the frozen 12-path implementation surface

## Review order and stop rule

The review is authorized exactly once and must proceed in this order:

1. F016 regression and parser-fragmentation repair;
2. F015;
3. F014;
4. F013;
5. F012;
6. F011;
7. F010;
8. F009;
9. F008;
10. F007;
11. F006;
12. plan attacks Q5 through Q15.

The first credible counterexample or material review failure must be recorded durably as a new finding and the review must STOP. No repair may be performed inside this review.

If no credible counterexample is found through the complete authorized sequence, a durable PASS review artifact may be created and the review must then STOP.

## Explicit non-authority

This acceptance does **not** authorize:

- any repair or implementation mutation;
- merge of PR #37 or PR #35;
- movement of `scriptops/main`;
- deployment, release or tag;
- canonical effect;
- active-product status promotion;
- X1B reopen;
- V1 authority;
- any further review after this single bounded review.

`AI PROPOSES != HUMAN DECIDES`

`REVIEW AUTHORITY != REPAIR AUTHORITY`

`REVIEW PASS != MERGE AUTHORITY`
