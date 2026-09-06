# X1B-FRAME PR37 F040 attempt-2 correction pre-apply evidence

Status: evidence only; no ScriptOps push.

Authority/finding chain:
- F040 finding: FJ899/8 PR #355
- Human bounded repair authority: FJ899/8 PR #356
- preservation/design: FJ899/8 PR #357
- attempt-1 pre-apply: FJ899/8 PR #358
- attempt-1 local verifier failure: FJ899/8 PR #359

Exact original ScriptOps repair input remains:
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `e8e745b5787f7f98c5e2df3fd03934acee332413`
- OLD TREE `6363566d5b36f4669e234f31cd4660a1687c0597`
- OLD verifier blob `73504fe6897a5b6a038da39b14478a37aa36bbc7`

Current Human worktree expectation before this correction: attempt-1 patch is applied but uncommitted, with only `scripts/verify_repository.py` modified; attempt-1 full verifier failed at preserved F021 and no commit/push occurred.

Correction delta artifact:
- file: `X1B_FRAME_PR37_F040_ATTEMPT1_CORRECTION.patch`
- SHA-256: `75348d812c5d432c481271cac08e22459a0938f8b8c375f8c0dd31c78d50b16c`
- delta surface: `scripts/verify_repository.py` only
- delta numstat relative to attempt-1 working tree: `+12/-18`

Correction semantics: after a blank line inside an active list path, first resolve the deepest surviving list owner for the current indentation. Only that owner may start indented code, and only at `owner_content_indent + 4` or deeper. The algorithm must not search past a still-owning deeper leaf merely because an ancestor also satisfies a four-column code threshold.

This directly preserves the failing F021 cases:
- deep bullet continuation at the current leaf content indent remains ordinary same-item continuation;
- mixed ordered/unordered deep continuation remains owned by its deepest leaf.

It also preserves F040 intent:
- a parent-owned line four columns beyond that parent's content indent starts indented code;
- a current deep leaf can start code at its own content indent + 4;
- a dedent resolves to the nearest surviving owner before later block parsing.

Validation performed before Human apply:
- unified correction patch parse: PASS
- synthetic exact-context `git apply --check`: PASS
- synthetic apply: PASS
- synthetic `git diff --check`: PASS
- correction decision harness for F021 bullet/mixed continuation and F040 parent/deep code cases: PASS

Real current dirty-worktree `git apply --check`, correction apply, full compile, full verifier F009-F040, and final verifier-only diff remain mandatory before any amend/push.

Disposition: `F040 ATTEMPT2 CORRECTION = PREAPPLY VALIDATED / HUMAN WORKTREE CHECK REQUIRED`.

No merge/main/deploy/release/tag/canonical/status/X1B/V1 authority.
