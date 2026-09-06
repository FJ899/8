# X1B-FRAME PR37 F031 REPAIR HUMAN AUTHORITY — 2026-09-06

Human input: `accept`.

This record authorizes exactly one bounded F031 repair after preservation audit PR #302.

Exact ScriptOps target rechecked at authorization time:
- PR #37
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `0f7d34476c33fdc0e530f22e3168791c600c17e1`
- verifier blob `9292d0e637229c0d87b57519a6a10fd3cb5d8df3`

Repair boundary:
- supersede the unsafe unconditional content-ownership unwind from the earlier F030 plan;
- implement a laziness-aware structural decision order;
- preserve F017-F031 behavior and earlier F006-F016 behavior;
- relative to OLD HEAD, change only `scripts/verify_repository.py`;
- final ScriptOps candidate remains exactly one replacement commit over frozen BASE;
- BASE-relative changed paths remain exactly the frozen twelve-path surface;
- full verifier and required workflows must pass before completion evidence is frozen;
- STOP before independent post-repair review.

No merge of PR #37 or PR #35, no ScriptOps main movement, deploy/release/tag, canonical effect, status promotion, X1B reopen or V1 authority is granted.