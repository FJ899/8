# X1B-FRAME PR37 F028 BOUNDED REPAIR HUMAN AUTHORITY — 2026-09-06

## HumanDecision

The Human explicitly said `accept` and instructed continuation after the active chain had stopped on first-counterexample finding `X1B-FRAME-F001-IMPLEMENTATION-F028`.

This record durably binds that `accept` to **one bounded F028 repair only**.

## Exact ScriptOps pre-repair binding

- Repository: `FJ899/scriptops`
- PR: `#37`
- PR state at gate: `OPEN / DRAFT / UNMERGED`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `0f7d34476c33fdc0e530f22e3168791c600c17e1`
- OLD TREE: `615af6e036dd1f6beaa818713984a2c18b1ee475`
- OLD verifier blob `scripts/verify_repository.py`: `9292d0e637229c0d87b57519a6a10fd3cb5d8df3`
- Candidate topology: exactly one commit over frozen BASE and exactly the frozen 12 BASE-relative changed paths.

## Finding repaired by this gate

- Finding: `X1B-FRAME-F001-IMPLEMENTATION-F028`
- Durable finding: `FJ899/8 PR #293`
- Review authority consumed by finding: `FJ899/8 PR #291`

F028 concerns CommonMark ordered-list paragraph interruption inside an already-active list path. The reviewed verifier respects the non-`1` ordered-marker interruption rule only for an ordinary paragraph outside `list_frames`. Inside an active list item it treats a syntactically list-like non-`1` ordered marker as a descendant or sibling boundary even where CommonMark keeps that marker as lazy paragraph continuation. This can split one self-reference/promotion claim into separate verifier authority units and create a false negative.

Representative counterexample family:

```text
- Parent
  10. This file
  2. grants release authority.
```

The relevant security property is structural, not literal: a marker that cannot interrupt the currently open paragraph at its actual container depth must not be allowed to manufacture a new authority-unit boundary.

## Authorized repair boundary

The Human authorizes exactly one bounded repair of F028 under these constraints:

1. Relative to OLD HEAD, change only `scripts/verify_repository.py`.
2. Correct CommonMark non-`1` ordered-marker paragraph-interruption handling inside active list paths, not only at top-level ordinary paragraphs.
3. Ensure a non-`1` ordered marker that cannot interrupt the currently open paragraph is folded into the same logical authority unit rather than treated as a descendant/sibling boundary.
4. Preserve genuine list-item boundaries, including valid bullets, `1`-started ordered interruptions, established-list siblings, dedented separation, blank-line ownership, and nested list semantics.
5. Preserve F027 through F006 behavior, including F027 indented-code item ownership and F025 ASCII/non-`1` semantics.
6. Add non-vacuous F028 regressions covering the exact counterexample family plus at least one depth/marker variant.
7. Add benign controls proving the correction does not collapse genuinely distinct siblings or separately owned list items into one authority unit.
8. Run the full repository verifier and require success.
9. Construct exactly one replacement commit over frozen BASE `2f22843ac570498b506101addeba5453ab777f08`.
10. Preserve the exact frozen 12-path BASE-relative implementation surface.
11. Re-check the PR head against OLD HEAD immediately before the non-fast-forward branch update and abort on drift.
12. Require both exact-head PR workflow runs (`Verify repository state` and `Phase 6 ScriptOps smoke`) to complete successfully.
13. Freeze durable completion evidence and STOP.

## Explicitly not authorized

This gate does **not** authorize:

- independent post-F028 review;
- any later finding repair;
- merge of PR #37 or PR #35;
- ScriptOps `main` movement;
- deployment, release or tag;
- canonical effect;
- active-product status promotion;
- PR #35 integration, rebase or cherry-pick;
- X1B reopen;
- V1 action;
- any other consequential authority.

`AI PROPOSES != HUMAN DECIDES`

`F028 REPAIR AUTHORITY != POST-REPAIR REVIEW AUTHORITY`
