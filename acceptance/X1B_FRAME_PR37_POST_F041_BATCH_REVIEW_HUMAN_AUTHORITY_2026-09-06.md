# HUMAN AUTHORIZATION — POST-F041 BATCHED ADVERSARIAL REVIEW

Date: 2026-09-06

The Human explicitly wrote `accept` after F041 bounded repair completion and after being presented with the proposed faster procedure.

This authorization is interpreted narrowly as authority for exactly one batched, read-only adversarial review of:

- repository: `FJ899/scriptops`
- PR: `#37`
- exact repaired HEAD: `6579dbccb2dbccc54875d51f377ce1c574e4bce6`
- exact repaired TREE: `425683ac0db4e1811f57ef10c5b9f75050846b55`
- frozen BASE: `2f22843ac570498b506101addeba5453ab777f08`
- exact verifier blob: `be645c1a3ee49a04d700a3ef7fde86a92e413a14`

## Authorized review procedure

The review may execute the entire predeclared frozen attack batch instead of stopping at the first credible counterexample. The purpose is to discover and record all credible failures in that bounded batch before any repair.

The batch is limited to:

1. re-attack F041 and preserve F040 and earlier regressions;
2. quoted indented-code combinations and quote/list/container ownership;
3. link reference definition recognition, paragraph removal, multiline/continuation boundaries, and container interactions;
4. blank-line, dedent, and EOF leaf/container boundaries around those cases;
5. targeted positive/negative controls for false split, false join, stale ownership, and literal-payload leakage.

## Prohibited during this review

- no repair;
- no modification of `FJ899/scriptops`;
- no merge of PR #37 or any evidence PR;
- no ScriptOps main movement;
- no deploy/release/tag;
- no canonical effect;
- no active-product status promotion;
- no X1B reopen;
- no V1 authority.

The review may record all credible counterexamples found in the frozen batch in one or more evidence files/PRs. After the batch, repair authority must be separately granted. Multiple failures may later be grouped by root cause, but this authorization does not itself grant any repair.

`BATCH DISCOVERY AUTHORITY != REPAIR AUTHORITY`
