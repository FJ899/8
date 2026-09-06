# X1B-FRAME PR #37 — F023 repair patch continuity

Evidence-only continuity under the Human-authorized F023 bounded repair recorded in `FJ899/8 PR #268`.

## Exact ScriptOps pre-repair binding

- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `0e86039856a97af04a7c0c06e5ffdf061abd1ada`
- OLD TREE `dcc8b80cfe0d863fe29f981c0527fe8a70d23dbd`
- OLD verifier blob `7043d154d8fde33e0f2452a74422a2d5ba4cb50a`

## Patch artifact

- name `X1B_FRAME_PR37_F023_REPAIR.patch`
- bytes `4910`
- SHA-256 `f090034bcf631cc8ca1a0615d504d72319ce2eef8043dd4ab917d128de742ccd`
- relative changed path: only `scripts/verify_repository.py`

## Repair design

1. `_markdown_list_item_layout()` accepts bullet/ordered marker-only empty items (`-`, `+`, `*`, `2.`, `2)`) as valid list markers, including nested use when a list path is active.
2. The layout result carries an `empty_item` flag and a minimal synthetic content indent for marker-only items.
3. `_authority_soft_wrapped_units()` refuses to let an empty item interrupt an already-active ordinary paragraph, matching CommonMark's empty-item interruption rule and preventing a new subject/predicate bypass.
4. A marker-only sibling therefore terminates the stale prior list path instead of being appended as lazy continuation.
5. Regressions cover the exact F023 benign counterexample, ordered and nested benign variants, bare/whitespace-only/ordered paragraph-interruption positive controls, and an empty-parent nested positive control.
6. Existing F022-F006 behavior is intended to remain unchanged.

Local parser matrix passed for F023 benign boundaries, paragraph-interruption positive controls, F022 benign/positive ownership, and F021 nested sibling behavior. `git apply --check` passed on a mock built with exact frozen hunk contexts.

This record grants no new authority and does not itself apply or push the repair.
