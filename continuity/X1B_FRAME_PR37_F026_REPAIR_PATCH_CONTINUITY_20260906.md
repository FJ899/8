# X1B-FRAME PR37 F026 repair patch continuity — 2026-09-06

## Binding

Authorized by HumanDecision repair gate `FJ899/8 PR #283` for finding `X1B-FRAME-F001-IMPLEMENTATION-F026` (`PR #282`).

Exact ScriptOps pre-repair binding:
- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `e91a6b1f5754d2807920c35221fd105de57b1d87`
- OLD TREE: `f38bc8f73f12e3d6b966fff625a9c180be3e69b4`
- OLD verifier blob: `16f59bd1440dcdf9fc5800ba70efc5e1e27ef9d0`

## Patch artifact

- filename: `X1B_FRAME_PR37_F026_REPAIR.patch`
- bytes: `3287`
- SHA-256: `30aa0d0e941ff157278391479c08c92ce8cbae396a68eefafa09a3d5182ae3d7`
- unified diff summary: `39 additions / 1 deletion`
- changed path: `scripts/verify_repository.py` only

## Repair content

The patch:

1. changes ordered-list marker recognition from Python Unicode-aware `\d{1,9}` to ASCII-only `[0-9]{1,9}`;
2. leaves F025 `ordered_start` / paragraph-interruption logic unchanged for valid ASCII ordered markers;
3. adds F026 regressions asserting Arabic-Indic `١.`, fullwidth `１.`, and Devanagari `१.` are not recognized as Markdown list markers;
4. adds non-vacuous self-reference/promotion rejection controls for those lookalikes and a locally-negated benign control;
5. preserves all earlier F025-F006 regression code unchanged outside the added F026 block.

The patch is verifier-only. It does not grant or perform merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, PR35 integration, X1B reopen, V1 action, or post-F026 review.

This continuity record grants no new authority.
