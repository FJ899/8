# HUMAN AUTHORITY — F043 multiline bounded repair

Human authorization: `accept`.

This authorizes exactly one bounded verifier-only repair of the F043 multiline CommonMark link-reference-definition defect recorded in FJ899/8 PR #375.

Exact ScriptOps target:

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- current HEAD: `3521a6c9f9c0db1103c49274d979766de1abfefa`
- current TREE: `6d2a5dbcceb5fd41f9988ef63d64c77bba45b8c1`
- verifier overlay blob: `61bf107ad59da33a6576032d341b41c538d0453a`
- pinned frozen F041 core blob: `be645c1a3ee49a04d700a3ef7fde86a92e413a14`
- finding authority: FJ899/8 PR #375

Authorized repair scope:

1. repair F043 multiline CommonMark §4.7 link-reference-definition recognition/extraction;
2. cover multiline labels and permitted destination/title line breaks, including equivalent fresh definition candidates in supported list/quote container contexts;
3. preserve the rule that a definition cannot interrupt an already-open paragraph;
4. keep definition metadata security-relevant as its own authority unit;
5. preserve all frozen R1-R24 / F009-F041 regressions and the existing F043 one-line/container controls;
6. keep F042 and F044 explicitly OPEN and unrepaired;
7. produce one replacement commit over the same frozen BASE, guarded ref update, both required workflows, and completion evidence only after PASS.

Any credible counterexample or regression failure stops the repair and returns to a single-stage diagnosis.

Not authorized: merge, default-branch movement, deploy, release, tag, canonical effect, active-product status promotion, X1B reopen, V1 authority, or repair of F042/F044.
