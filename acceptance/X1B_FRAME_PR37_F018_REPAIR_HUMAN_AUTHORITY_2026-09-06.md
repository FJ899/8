# X1B-FRAME PR37 F018 bounded repair Human authority

Human `accept` authorizes exactly one bounded replacement repair of existing `FJ899/scriptops PR #37` for finding `X1B-FRAME-F001-IMPLEMENTATION-F018` recorded in `FJ899/8 PR #242`.

Exact pre-repair target:

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `467a4d1be44f11cbfa8ada85885397b4c7283d40`
- TREE: `d7ab8679065844e93d979b0712f5eadb4b73758a`
- verifier path: `scripts/verify_repository.py`
- verifier blob: `178881c7fe485b054a265462b908d69ff44bb9a6`

Authorized repair boundary:

- keep PR #37 exactly one commit over frozen BASE;
- keep the frozen twelve-path base-relative implementation surface unchanged;
- relative to current HEAD, only `scripts/verify_repository.py` may change;
- close F018 ellipsis / false sentence-tail soft-wrap fragmentation without reopening F017-F006;
- add non-vacuous regressions through the production validator for positive ellipsis/multiline bypasses and benign multiline negatives;
- run repository verification and Phase 6 smoke before freezing the repaired candidate.

This authority does **not** grant merge, ScriptOps main movement, PR35 integration, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen, V1 authority, or post-repair independent re-review.

`AI PROPOSES != HUMAN DECIDES`
