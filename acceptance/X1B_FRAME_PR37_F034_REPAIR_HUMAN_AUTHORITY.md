# X1B-FRAME PR #37 — F034 bounded repair Human authority

Human explicitly accepted exactly one bounded repair for finding `X1B-FRAME-F001-IMPLEMENTATION-F034`.

Exact ScriptOps binding:
- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `d127ca34ee9b6f03a4e7286913e7cd89fa55fa33`
- OLD TREE: `9f4b273a7e8f05360a972e2606353fb2e7f4b5ae`
- OLD verifier blob: `e793f9558e9f55ba33bedf90068e185d229d70e9`
- F034 evidence: `FJ899/8 PR #319`

Authorized repair scope:
- only `scripts/verify_repository.py` may differ relative to OLD HEAD;
- close the F034 CommonMark ATX-heading structural-boundary false promotion;
- preserve F033/F032/F031/F030/F029 and every earlier frozen regression;
- final ScriptOps candidate remains exactly one replacement commit over BASE;
- BASE-relative PR surface remains exactly the frozen 12 paths;
- full repository verifier must pass;
- both existing GitHub Actions workflows must pass on the exact repaired HEAD;
- freeze completion evidence, then STOP before any independent post-repair review.

Not authorized:
- repair outside the bounded verifier surface;
- merge of PR #37 or PR #35;
- ScriptOps main movement;
- deploy, release, tag, canonical effect;
- active-product status promotion;
- X1B reopen or V1 authority.

`F034 REPAIR AUTHORITY != MERGE AUTHORITY`
