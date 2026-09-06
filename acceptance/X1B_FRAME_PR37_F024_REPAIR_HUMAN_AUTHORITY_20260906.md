# X1B-FRAME PR #37 — Human authorization for one bounded F024 repair

Human authorization received in conversation: `accept`.

This record binds that HumanDecision to exactly one bounded repair of finding `X1B-FRAME-F001-IMPLEMENTATION-F024` from `FJ899/8 PR #272`.

## Exact ScriptOps pre-repair target

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `beba918e23b3b98c8324c8b735265ca8931db562`
- OLD TREE: `f2026d57aad61dd08b175cdedba20087b7598720`
- OLD verifier path: `scripts/verify_repository.py`
- OLD verifier blob: `020c4ebe4ce2073c6172d316ad8a582a26832f46`
- state: `OPEN / DRAFT / UNMERGED`
- shape: exactly one commit over frozen BASE and exactly the frozen 12-path BASE-relative surface.

## Authorized repair boundary

The bounded F024 repair may change only `scripts/verify_repository.py` relative to OLD HEAD and must:

1. correct empty list-item indentation so an item whose marker is followed only by end-of-line or trailing spaces/tabs uses CommonMark blank-start ownership indentation `marker_indent + marker_width + 1`, rather than treating trailing whitespace width as content indentation;
2. close the exact F024 subject/predicate false-negative where two paragraphs that belong to one empty-marker-started item are split after a blank line;
3. cover bullet and ordered marker forms, including trailing spaces/tabs and nested/deep forms where useful;
4. preserve the F023 rule that valid marker-only empty items are boundaries but cannot interrupt an active ordinary paragraph;
5. preserve F022 blank-line ownership, F021 deep indentation, F020 nested sibling separation, and all earlier F019-F006 behavior;
6. add non-vacuous positive and benign regressions, including the exact F024 counterexample;
7. preserve exactly one replacement commit over frozen BASE and the exact frozen 12-path BASE-relative implementation surface;
8. run the full local verifier and both existing PR workflows, then freeze the repaired HEAD/TREE/verifier blob and STOP.

The branch update must be stale-head protected against OLD HEAD and must not move ScriptOps `main`.

No independent post-repair review authority is granted here.

No merge, ScriptOps `main` movement, deployment, release, tag, canonical effect, active-product status promotion, PR #35 integration, X1B reopen, V1, or any other consequential authority is granted.