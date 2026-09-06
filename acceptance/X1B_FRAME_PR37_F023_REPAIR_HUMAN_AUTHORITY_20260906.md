# X1B-FRAME PR #37 — Human authorization for one bounded F023 repair

Human authorization received in conversation: `accept`.

This record binds that HumanDecision to exactly one bounded repair of finding `X1B-FRAME-F001-IMPLEMENTATION-F023` from `FJ899/8 PR #267`.

## Exact ScriptOps pre-repair target

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `0e86039856a97af04a7c0c06e5ffdf061abd1ada`
- OLD TREE: `dcc8b80cfe0d863fe29f981c0527fe8a70d23dbd`
- OLD verifier blob: `7043d154d8fde33e0f2452a74422a2d5ba4cb50a`
- state: `OPEN / DRAFT / UNMERGED`
- shape: exactly one commit over frozen BASE and exactly the frozen 12-path BASE-relative surface.

## Authorized repair boundary

The bounded F023 repair may change only `scripts/verify_repository.py` relative to OLD HEAD and must:

1. recognize valid CommonMark marker-only empty bullet/ordered list items as real list-item boundaries, including nested forms;
2. ensure an empty sibling cannot leave a stale prior list frame that absorbs a later structurally separate paragraph;
3. preserve F022 blank-line ownership behavior, F021 deep indentation behavior, F020 nested sibling separation, and all earlier F019-F006 behavior;
4. add non-vacuous regressions for benign empty-sibling separation and positive same-item/nested security controls;
5. preserve exactly one commit over frozen BASE and the exact frozen 12-path BASE-relative implementation surface.

No independent post-repair review authority is granted here.

No merge, ScriptOps `main` movement, deployment, release, tag, canonical effect, active-product status promotion, PR #35 integration, X1B reopen, V1, or any other consequential authority is granted.
