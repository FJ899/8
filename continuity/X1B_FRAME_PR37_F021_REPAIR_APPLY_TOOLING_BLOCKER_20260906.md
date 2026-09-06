# X1B-FRAME PR37 F021 repair — apply tooling continuity

Date: 2026-09-06

This record preserves continuity for the already Human-authorized F021 repair under `FJ899/8 PR #257`.

## Exact live pre-repair target

```text
repository = FJ899/scriptops
PR = #37
BASE = 2f22843ac570498b506101addeba5453ab777f08
HEAD = 78eb25f7b07270919658fe0eeb839bcaabcfed52
TREE = d21afc0caef5664e86065301b17e4d18be4f57bf
PATH = scripts/verify_repository.py
BLOB = 2bec91059ce98595f14226d9e9898ff94336864c
```

Live re-check before this continuity record: PR #37 remains OPEN/DRAFT/UNMERGED at the exact HEAD above, and ScriptOps `main` remains frozen at BASE.

## Prepared repair artifact

```text
artifact = X1B_FRAME_PR37_F021_REPAIR.patch
bytes = 4833
sha256 = 2b8011902dd71bbf9e77d7a3d7783af5d28616d15c2e8db58d8ae70727d1b43e
changed path = scripts/verify_repository.py only
```

The repair makes deep list-marker recognition context-aware: top-level list markers retain the Markdown 0–3-column rule, while an already active list path may recognize nested markers at four or more absolute columns (including tab-expanded columns). This separates deep siblings without globally reclassifying standalone indented code as a top-level list.

Prepared production regressions cover deep positive continuation/self-promotion, deep benign siblings, mixed ordered/unordered deep siblings, deep benign negation, and a standalone four-space bullet-like code-block guard. Existing F020-F006 tests remain present.

Local logic tests passed for deep sibling separation, deep same-item continuation folding, mixed nesting, tab-expanded nesting, benign negation and top-level indented-code separation. The patch changes one path, passes `git diff --check`, and `git apply --check` succeeds on an exact-context displaced-line mock.

The current connector cannot safely apply this patch to the existing PR #37 branch while preserving the required replacement-commit topology and stale-head force-with-lease guard, so no ScriptOps ref/tree/commit/main mutation was attempted here.

Post-repair independent re-review remains a separate Human gate.
