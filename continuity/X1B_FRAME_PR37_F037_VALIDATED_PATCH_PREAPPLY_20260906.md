# X1B-FRAME PR #37 F037 validated patch pre-apply evidence

Human-authorized bounded F037 repair target:

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `766a392c972fb14267768af283daaf64cd3282b9`
- OLD TREE: `e7433570911943deb134947fc045bb00aaa5a1a4`
- OLD verifier blob: `c6175ca14db603442f4ce24dc9ea04b8140daecb`
- finding: `FJ899/8 PR #337`
- Human repair authority: `FJ899/8 PR #338`
- preservation/design audit: `FJ899/8 PR #339`

Prepared patch:

- file: `X1B_FRAME_PR37_F037_REPAIR.patch`
- SHA-256: `56c66ddfbea7837b13bdde69af41921a5e3ee81b32c2aa7186ebae21ee1a9d57`
- surface: `scripts/verify_repository.py` only
- patch numstat: `164 additions / 0 deletions`

Pre-apply validation completed:

- patch parses as a single-file unified diff;
- synthetic context-skeleton `git apply --check` and apply completed cleanly;
- post-synthetic-apply `git diff --check` was clean;
- bounded F037 helper/top-level semantics harness passed;
- CommonMark 0.31.2 §4.3 semantics were cross-checked, including one-or-more `=`/`-`, <=3 leading spaces, no internal whitespace, nonempty preceding heading text, no required blank after heading, and the rule that a setext underline cannot be a lazy continuation line in a list item or block quote.

Mandatory validations still outstanding on the exact real OLD HEAD worktree:

1. exact patch SHA and `git apply --check`;
2. real apply with verifier-only surface confirmation;
3. Python compile;
4. full repository verifier PASS including F037 and all preserved regressions;
5. replacement-amend topology: exactly one commit over frozen BASE and same frozen 12 BASE-relative paths;
6. guarded force-with-lease push only if remote still equals OLD HEAD;
7. both existing GitHub Actions workflows PASS on exact NEW HEAD;
8. completion evidence freeze and STOP before independent post-F037 review.

No ScriptOps mutation has been performed by this evidence record. No merge/main/deploy/release/tag/canonical/status/X1B/V1 authority.
