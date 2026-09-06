# X1B-FRAME — Human authority for post-F037 independent review

Date: 2026-09-06

Human decision: `accept`

This record binds exactly one independent read-only adversarial review of the repaired `FJ899/scriptops PR #37` candidate.

Exact review target:

- `BASE = 2f22843ac570498b506101addeba5453ab777f08`
- `HEAD = 5d07e181c1a9d43f4bfca000962790b087b6fe15`
- `TREE = bdbc73b06bb29c5b334cb2cd4bca0d49b68df63b`
- `scripts/verify_repository.py BLOB = b29df53ab96596ac075118943b364d9b47eda6cd`
- PR state at completion: `OPEN / DRAFT / UNMERGED`

Evidence chain:

- post-F036 review authority: `FJ899/8 PR #336`
- F037 finding: `FJ899/8 PR #337`
- F037 bounded repair Human authority: `FJ899/8 PR #338`
- F037 preservation/design: `FJ899/8 PR #339`
- F037 validated patch pre-apply: `FJ899/8 PR #340`
- F037 repair completion: `FJ899/8 PR #341`

Review order is fixed:

1. re-attack F037 first;
2. preserve F036, F035, F034, F033, F032, F031, F030, F029 and every earlier frozen regression;
3. continue the remaining frozen adversarial frontier;
4. stop at the first credible counterexample or PASS.

First credible counterexample requires durable finding evidence and immediate STOP before repair.

This authority does not authorize repair, mutation of ScriptOps, merge of PR #37 or PR #35, default-branch movement, deploy, release, tag, canonical effect, active-product status promotion, X1B reopen, V1 action, or unrelated cleanup.
