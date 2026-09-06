# X1B-FRAME PR37 F021 repair — Human authority

Date: 2026-09-06

The Human explicitly entered `accept` after finding `X1B-FRAME-F001-IMPLEMENTATION-F021` in `FJ899/8 PR #256`.

This record authorizes exactly one bounded replacement repair of existing `FJ899/scriptops PR #37` and nothing beyond that repair.

## Exact pre-repair binding

```text
repository = FJ899/scriptops
PR = #37
BASE = 2f22843ac570498b506101addeba5453ab777f08
HEAD = 78eb25f7b07270919658fe0eeb839bcaabcfed52
TREE = d21afc0caef5664e86065301b17e4d18be4f57bf
PATH = scripts/verify_repository.py
BLOB = 2bec91059ce98595f14226d9e9898ff94336864c
finding = X1B-FRAME-F001-IMPLEMENTATION-F021
```

## Bounded repair requirements

1. Final PR #37 remains exactly one replacement commit over frozen BASE `2f22843ac570498b506101addeba5453ab777f08`.
2. BASE-relative changed paths remain exactly the frozen twelve-path implementation surface.
3. Relative to pre-repair HEAD `78eb25f7b07270919658fe0eeb839bcaabcfed52`, only `scripts/verify_repository.py` may change.
4. Repair the F021 defect: valid deeper nested Markdown list markers with absolute indentation of four or more columns must participate in the list-item path model, so siblings at any supported nesting depth remain distinct authority units while parent->descendant wording and same-item continuation paragraphs remain correctly folded.
5. Preserve F020 through F006 semantics and existing non-vacuous regressions.
6. Add non-vacuous production-validator regressions covering at least: deep nested benign sibling separation, deep nested positive continuation/self-promotion rejection, and deep nested benign negation; include mixed ordered/unordered nesting where useful.
7. Run the full repository verifier and both required PR workflows.
8. Any branch update must be stale-head protected and may update only the existing PR #37 branch.
9. Freeze exact repaired HEAD/TREE/verifier blob and STOP.

## Explicit non-authority

This acceptance does not authorize merge, ScriptOps `main` movement, PR #35 integration, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen, V1 authority, or post-repair independent re-review.

`AI PROPOSES != HUMAN DECIDES`
