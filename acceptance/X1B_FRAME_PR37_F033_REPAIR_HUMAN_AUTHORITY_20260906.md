# X1B-FRAME PR #37 — Human acceptance of bounded F033 repair

Human authorization received: `accept`.

This authority permits exactly one bounded repair for finding `X1B-FRAME-F001-IMPLEMENTATION-F033`, recorded in `FJ899/8 PR #313`.

Exact binding:

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `5c32af7127000e86f33e9f0e79ac09de8441b49d`
- OLD TREE: `456ef9210d74a24f8702c15b6c28c244328e02ad`
- OLD verifier blob: `f3d196b6712037b4fda08fc6f40888c6c663c3ca`
- finding evidence: `FJ899/8 PR #313`

Repair boundary:

1. Relative to OLD HEAD, only `scripts/verify_repository.py` may differ.
2. Preserve F032, F031, F030, F029 and every earlier frozen regression/control.
3. Repair the top-level CommonMark thematic-break boundary without weakening list-context thematic-break handling or Markdown soft-wrap semantics.
4. Final candidate must remain exactly one replacement commit over BASE.
5. BASE-relative changed surface must remain exactly the frozen 12 paths already present in PR #37.
6. Full verifier must pass and both existing GitHub Actions workflows must be green on the exact repaired HEAD.
7. Freeze completion evidence and STOP before an independent post-repair adversarial review.

Not authorized:

- merge of PR #37 or PR #35;
- ScriptOps main movement;
- deploy, release, tag;
- canonical effect;
- active-product status promotion;
- X1B reopen;
- V1 authority;
- unrelated cleanup or refactor.
