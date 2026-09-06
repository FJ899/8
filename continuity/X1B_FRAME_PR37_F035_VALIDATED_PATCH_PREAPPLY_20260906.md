# X1B-FRAME PR #37 — F035 validated patch pre-apply evidence

Bound to:
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `74e11cdf52a8a0857d727030b6a6f44e40127b1b`
- OLD TREE `260a7d09077af0fafdb679a41e124ac87f02cdfa`
- OLD verifier blob `4e51a52af9e0f7c579f13a5faca804a9caaf912b`
- finding `FJ899/8 PR #325`
- Human repair authority `FJ899/8 PR #326`
- preservation/design audit `FJ899/8 PR #327`

Prepared patch artifact: `X1B_FRAME_PR37_F035_REPAIR.patch`.

Patch SHA-256: `be7e30837ea2b3b9af73cd59153275e59f6c693755d3e330e40a4482d843362e`.

Prepared mutation surface:
- `scripts/verify_repository.py` only
- additions `221`
- deletions `0`

The patch adds bounded block-quote recognition, a top-level quote security-unit accumulator with lazy paragraph continuation, list-owner resolution for quotes, negative controls for escaped/four-column quote-like text, F035 regressions, and one F035 PASS line. It does not add general fenced-code, HTML-block, or unrelated Markdown parsing.

Synthetic patch generation/application checks passed against exact old-code hunk contexts, and an isolated parser harness exercised the F035 boundary, lazy continuation, list ownership, structural interruption, and lookalike matrix successfully.

Authoritative application has not yet occurred on the user's exact OLD HEAD worktree. Exact real-worktree `git apply --check`, compile, full verifier, replacement-commit invariants, remote workflow runs, and completion evidence remain mandatory before F035 can be considered complete.

No ScriptOps branch has been mutated by this evidence record. No merge/main/deploy/release/tag/canonical/status/X1B/V1 authority is granted.
