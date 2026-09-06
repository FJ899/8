# X1B-FRAME PR37 F027 BOUNDED REPAIR HUMAN AUTHORITY — 2026-09-06

## HumanDecision

The Human explicitly said `accept` immediately after presentation of the first-counterexample finding `X1B-FRAME-F001-IMPLEMENTATION-F027` and the proposed next gate of exactly one bounded F027 repair.

This record durably binds that `accept` to **one bounded F027 repair only**.

## Exact ScriptOps pre-repair binding

- Repository: `FJ899/scriptops`
- PR: `#37`
- PR state at gate: `OPEN / DRAFT / UNMERGED`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `72f1e00c45a58c107a4e4f2a90cccd92fa76cbe9`
- OLD TREE: `9b9f858d2b505809332e85c6cbf506d8f031a441`
- OLD verifier blob `scripts/verify_repository.py`: `914ff100f03b23268a0a96db57103727e912a569`
- Candidate topology: exactly one commit over frozen BASE and exactly the frozen 12 BASE-relative changed paths.

## Finding repaired by this gate

- Finding: `X1B-FRAME-F001-IMPLEMENTATION-F027`
- Durable finding: `FJ899/8 PR #287`
- Review authority consumed by finding: `FJ899/8 PR #286`

F027 concerns CommonMark list-item ownership when a nonempty list item begins with an indented code block. For such a start, structural ownership indentation is marker width `W + 1`, not the entire physical post-marker whitespace width. The reviewed verifier inflated `content_indent` from the physical gap and could split later same-item paragraphs after a blank line, producing a subject/predicate authority false negative.

Representative first counterexample:

```text
1.     This file

   grants release authority.
```

## Authorized repair boundary

The Human authorizes exactly one bounded repair of F027 under these constraints:

1. Relative to OLD HEAD, change only `scripts/verify_repository.py`.
2. Correct CommonMark ownership for nonempty list items that begin with indented code, so the special `W+1` item indentation rule is applied where required rather than counting all physical post-marker whitespace.
3. Preserve ordinary nonempty-item indentation semantics where the post-marker gap remains within the normal CommonMark item-start range.
4. Preserve F026 ASCII-only ordered-marker semantics and all prior F025 through F006 behavior.
5. Add non-vacuous positive F027 regressions covering at least ordered and bullet forms, including the exact first counterexample family and a nested/owned variant where appropriate.
6. Add benign controls sufficient to show the correction does not collapse genuinely distinct list items or dedented paragraphs into one authority unit.
7. Run the full repository verifier and require success.
8. Construct exactly one replacement commit over frozen BASE `2f22843ac570498b506101addeba5453ab777f08`.
9. Preserve the exact frozen 12-path BASE-relative implementation surface.
10. Push only with a stale-head guard/force-with-lease bound to OLD HEAD.
11. Require both exact-head PR workflow runs (`Verify repository state` and `Phase 6 ScriptOps smoke`) to complete successfully.
12. Freeze durable completion evidence and STOP.

## Explicitly not authorized

This gate does **not** authorize:

- independent post-F027 review;
- any later finding repair;
- merge or ScriptOps `main` movement;
- deployment, release or tag;
- canonical effect;
- active-product status promotion;
- PR #35 integration;
- X1B reopen;
- V1 action;
- any other consequential authority.

`AI PROPOSES != HUMAN DECIDES`

`F027 REPAIR AUTHORITY != POST-REPAIR REVIEW AUTHORITY`
