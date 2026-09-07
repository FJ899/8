# X1B-FRAME — Human authority for one post-F043 adversarial review

Date: 2026-09-07

Human authorization received in-session: `accept`.

Authorized target:

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `3521a6c9f9c0db1103c49274d979766de1abfefa`
- TREE: `6d2a5dbcceb5fd41f9988ef63d64c77bba45b8c1`
- verifier overlay blob: `61bf107ad59da33a6576032d341b41c538d0453a`
- pinned frozen F041 core blob: `be645c1a3ee49a04d700a3ef7fde86a92e413a14`

Authorized operation:

Exactly one read-only post-F043 adversarial review.

Review order / stopping rule:

1. Re-attack F043 first.
2. Preserve known F042 and F044 findings as OPEN / UNREPAIRED; do not silently reclassify them as closed.
3. Continue only within the declared read-only review frontier.
4. Stop at the first credible counterexample, or record PASS if the declared frontier survives.

Explicitly not authorized:

- repair or code mutation in `FJ899/scriptops`;
- merge of PR #37 or PR #35;
- movement of ScriptOps `main`;
- deploy / release / tag;
- canonical effect;
- active-product status promotion;
- X1B reopen;
- V1 authority.

`REVIEW AUTHORITY != REPAIR AUTHORITY`
`IMPLEMENTATION CANDIDATE != MERGE AUTHORITY`
