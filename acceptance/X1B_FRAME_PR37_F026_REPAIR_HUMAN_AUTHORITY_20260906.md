# X1B-FRAME PR37 F026 bounded repair Human authority — 2026-09-06

## HumanDecision

The Human explicitly authorized exactly one bounded repair of finding `X1B-FRAME-F001-IMPLEMENTATION-F026` by saying `accept` immediately after the F026 finding/STOP.

## Exact pre-repair ScriptOps binding

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `e91a6b1f5754d2807920c35221fd105de57b1d87`
- OLD TREE: `f38bc8f73f12e3d6b966fff625a9c180be3e69b4`
- OLD verifier blob: `16f59bd1440dcdf9fc5800ba70efc5e1e27ef9d0`
- state: OPEN / DRAFT / UNMERGED
- exactly one commit over frozen BASE
- exact frozen 12-path BASE-relative implementation surface

## Finding being repaired

`X1B-FRAME-F001-IMPLEMENTATION-F026` is recorded by `FJ899/8 PR #282`.

The verifier currently uses Python `\d{1,9}` for ordered-list markers. Python `\d` accepts Unicode decimal digits, while CommonMark ordered-list markers are limited to ASCII digits `0-9`. A Unicode digit such as Arabic-Indic `١.` can therefore be misclassified as an ordered-list marker and can split a CommonMark paragraph into separate security units, creating a self-reference/promotion false negative.

## Authorized repair boundary

This HumanDecision authorizes exactly one bounded F026 repair, limited to `scripts/verify_repository.py` relative to OLD HEAD.

The repair must:

1. restrict ordered Markdown list-marker recognition to ASCII digits `0-9` only;
2. preserve the F025 rule that a nonempty ordered marker interrupts an active ordinary paragraph only when the ASCII start number is `1`;
3. preserve normal ASCII non-`1` ordered list items inside an already established list;
4. add non-vacuous regressions for representative non-ASCII decimal-digit lookalikes, including Arabic-Indic, fullwidth, and Devanagari forms, demonstrating they remain paragraph text rather than Markdown list markers;
5. preserve F025 through F006 behavior and the existing R/P/currentness/runtime assertions;
6. preserve exactly one replacement commit over frozen BASE and the exact frozen 12-path BASE-relative surface;
7. require full local verifier PASS and both required ScriptOps workflows SUCCESS before completion evidence is frozen.

## Explicit exclusions

This authority does **not** authorize:

- any repair beyond F026;
- any independent post-F026 review;
- merge or movement of ScriptOps `main`;
- deployment, release, tag, or canonical effect;
- active-product status promotion;
- PR #35 integration;
- X1B reopen;
- V1 action;
- any new capability.

`AI PROPOSES != HUMAN DECIDES`

`IMPLEMENTATION CANDIDATE != MERGE AUTHORITY`
