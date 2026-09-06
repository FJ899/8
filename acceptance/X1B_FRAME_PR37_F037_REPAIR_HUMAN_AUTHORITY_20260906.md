# X1B-FRAME PR #37 F037 bounded repair — Human authority

Human `accept` on 2026-09-06 authorizes exactly one bounded repair of `X1B-FRAME-F001-IMPLEMENTATION-F037`.

Exact ScriptOps target:

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `766a392c972fb14267768af283daaf64cd3282b9`
- OLD TREE: `e7433570911943deb134947fc045bb00aaa5a1a4`
- OLD verifier blob: `c6175ca14db603442f4ce24dc9ea04b8140daecb`
- finding evidence: `FJ899/8 PR #337`

Authorized repair boundary:

- close F037 only: CommonMark setext `=` underline must terminate the preceding top-level paragraph/heading security unit so later paragraph text cannot inherit its self-reference;
- preserve F036, F035, F034, F033, F032, F031, F030, F029 and every earlier regression;
- relative to OLD HEAD, only `scripts/verify_repository.py` may differ;
- final PR #37 candidate must remain exactly one replacement commit over frozen BASE with the same frozen 12 BASE-relative changed paths;
- full local verifier must PASS;
- both existing PR #37 GitHub Actions workflows must PASS on the exact repaired NEW HEAD;
- completion evidence must be frozen before any independent post-repair review.

This authority does not authorize merge of PR #37 or PR #35, ScriptOps main movement, deploy/release/tag, canonical effect, active-product status promotion, X1B reopen, V1 action, or unrelated cleanup.
