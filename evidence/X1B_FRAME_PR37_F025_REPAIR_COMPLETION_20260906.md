# X1B-FRAME PR37 F025 REPAIR COMPLETION EVIDENCE

## Status

F025 bounded repair COMPLETE / frozen implementation candidate / no consequential authority.

## Authority and finding chain

- Human repair authority: `FJ899/8 PR #278`
- Finding repaired: `X1B-FRAME-F001-IMPLEMENTATION-F025` in `FJ899/8 PR #277`
- Patch continuity: `FJ899/8 PR #279`

This record grants no new authority.

## Exact pre-repair ScriptOps binding

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `f75a55fd1923d115f3194827e8c0017a58587f60`
- OLD TREE: `c2e90eba0b074298820960fd33db81a155633d4a`
- OLD verifier blob: `e7c94abbf62342a360fc96d2c7ac07175c5d872e`

## Repair patch identity

- file: `X1B_FRAME_PR37_F025_REPAIR.patch`
- bytes: `5245`
- SHA-256: `02bf8afbbbb92d1a43ce5d806e6f77516499d8b5f017f559bc5a629f8ce60cc9`

The patch was applied only after an exact clean-tree preflight against OLD HEAD and OLD verifier blob.

## Local repair validation

After patch application:

- changed path surface relative to OLD HEAD was exactly `scripts/verify_repository.py`;
- `git diff --check` passed;
- new verifier blob was `16f59bd1440dcdf9fc5800ba70efc5e1e27ef9d0`;
- `python scripts/verify_repository.py` exited successfully;
- the verifier reported PASS for F025 and retained PASS for F024 through F006;
- final checkout-local coherence/currentness/runtime/offline assertions all reported PASS.

F025 regression specifically closes the non-`1` ordered-list paragraph-interruption bypass while preserving valid bullet/`1` paragraph interruption and ordinary non-`1` items inside an already active list.

## Exact replacement commit

- NEW HEAD: `e91a6b1f5754d2807920c35221fd105de57b1d87`
- NEW TREE: `f38bc8f73f12e3d6b966fff625a9c180be3e69b4`
- sole parent: `2f22843ac570498b506101addeba5453ab777f08`
- NEW verifier blob: `16f59bd1440dcdf9fc5800ba70efc5e1e27ef9d0`
- commit message: `X1B-FRAME: bounded F025 repair over frozen base`

The replacement commit is exactly one commit over frozen BASE.

## F024 -> F025 boundary

The replacement was verified locally as verifier-only relative to OLD HEAD.

Remote Git tree readback independently confirms:

- all top-level entries other than `scripts` are unchanged between OLD TREE and NEW TREE;
- OLD `scripts` tree: `744b5e69889ecb2cd22866b2e909f80707858ed8`;
- NEW `scripts` tree: `e8d140fa9e81347c120d1bf1810d5d6327f908dc`;
- `scripts/restore_v2.py` remains `fa2099d7d4530bce2256051690935625dab0e927`;
- only `scripts/verify_repository.py` changes, from `e7c94abbf62342a360fc96d2c7ac07175c5d872e` to `16f59bd1440dcdf9fc5800ba70efc5e1e27ef9d0`.

Therefore the F024 -> F025 repair boundary is verifier-only.

## Frozen BASE-relative implementation surface

The NEW HEAD remains exactly the frozen 12-path implementation surface relative to BASE:

1. `DECISION_LOG.md`
2. `HANDOFF.md`
3. `PROJECT_STATE.md`
4. `README.md`
5. `RECONSTRUCTION_REPORT.md`
6. `SOURCES.md`
7. `SOURCE_AUDIT_SUMMARY.md`
8. `SOURCE_MANIFEST.md`
9. `scripts/verify_repository.py`
10. `sources/Decision_Summary_Current_State.md`
11. `sources/RC1_SCOPE_LOCK.md`
12. `sources/ScriptOps_Main_Theme_Summary.md`

PR #37 remote state after push:

- OPEN
- DRAFT
- UNMERGED
- head `e91a6b1f5754d2807920c35221fd105de57b1d87`
- base `2f22843ac570498b506101addeba5453ab777f08`
- exactly 1 commit
- exactly 12 changed files

## Required CI on exact NEW HEAD

Both required pull-request workflows completed successfully on exact HEAD `e91a6b1f5754d2807920c35221fd105de57b1d87`:

- `Verify repository state` — run `34027141866`, run number `148`, conclusion `success`;
- `Phase 6 ScriptOps smoke` — run `34027141902`, run number `94`, conclusion `success`.

Both runs bind to tree `f38bc8f73f12e3d6b966fff625a9c180be3e69b4` and PR #37 base `2f22843ac570498b506101addeba5453ab777f08`.

## Default-branch guard

Live `FJ899/scriptops main` remains exactly:

`2f22843ac570498b506101addeba5453ab777f08`

No main movement occurred under the F025 repair authority.

## Disposition

F025 repair authority is consumed.

STOP before any independent post-F025 review. A separate explicit HumanDecision gate is required for exactly one read-only review of the frozen NEW HEAD. No merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, PR35 integration, X1B reopen or V1 authority is created by this evidence record.