# X1B-FRAME PR #37 — F033 validated patch pre-apply evidence

Human-authorized bounded F033 repair input:

- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `5c32af7127000e86f33e9f0e79ac09de8441b49d`
- OLD TREE: `456ef9210d74a24f8702c15b6c28c244328e02ad`
- OLD verifier blob: `f3d196b6712037b4fda08fc6f40888c6c663c3ca`
- finding: `FJ899/8 PR #313`
- Human authority: `FJ899/8 PR #314`
- preservation/design audit: `FJ899/8 PR #315`

Prepared artifact:

`X1B_FRAME_PR37_F033_REPAIR.patch`

SHA-256:

`fb8bcc20ec640001d4b7f06ca527a97547638d8439701614f9b61967868e5000`

Prepared patch surface:

- `scripts/verify_repository.py` only;
- `64` additions;
- `0` deletions;
- no runtime/workflow/documentation changes;
- adds top-level thematic/setext block-boundary handling before existing list-specific F032 handling;
- adds F033 regression controls while retaining the frozen F032 and earlier tests.

Patch-format/application syntax was checked against exact old-code hunk contexts in an isolated synthetic repository. The authoritative exact-OLD-HEAD `git apply --check`, Python compile, full verifier, replacement-commit invariants and GitHub Actions workflows remain mandatory before completion; this record does not claim those later gates have passed.

No patch has been pushed to ScriptOps by this evidence record. No merge/main/deploy/release/tag/canonical/status/X1B/V1 authority is granted.
