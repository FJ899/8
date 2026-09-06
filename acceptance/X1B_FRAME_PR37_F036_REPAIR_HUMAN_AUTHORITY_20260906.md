# Human acceptance — bounded F036 repair

Date: 2026-09-06

The Human explicitly accepted exactly one bounded repair of finding `X1B-FRAME-F001-IMPLEMENTATION-F036` against `FJ899/scriptops PR #37`.

Exact binding:

- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `827d97a28bae8e4a6981739c616e1e6578a99665`
- OLD TREE `592a68f826d1b480d58319571b4df0e342f2513e`
- OLD verifier blob `cd079df9446d8a1781943670ec614615311a2564`
- finding evidence `FJ899/8 PR #331`

Authorized scope:

1. repair only the fenced-code block-boundary/container defect described by F036;
2. only `scripts/verify_repository.py` may differ relative to OLD HEAD;
3. preserve F035/F034/F033/F032/F031/F030/F029 and every earlier regression;
4. preserve the frozen 12-path BASE-relative surface;
5. finish as exactly one replacement commit directly over BASE;
6. full local verifier must PASS;
7. both existing ScriptOps GitHub Actions workflows must PASS on the exact repaired HEAD;
8. freeze repair-completion evidence and STOP before independent post-repair review.

Not authorized:

- any unrelated Markdown-parser expansion;
- merge of PR #37 or PR #35;
- ScriptOps main movement;
- deploy/release/tag;
- canonical effect;
- active-product status promotion;
- X1B reopen;
- V1 action.

This record is durable Human repair authority only; it is not merge or product-effect authority.
