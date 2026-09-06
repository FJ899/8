# X1B-FRAME PR37 F040 attempt-1 local verifier failure

Status: durable evidence only.

Bound repair authority: FJ899/8 PR #356.
Finding: FJ899/8 PR #355.
Preservation/design: FJ899/8 PR #357.
Pre-apply evidence: FJ899/8 PR #358.

Exact ScriptOps input before apply:
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `e8e745b5787f7f98c5e2df3fd03934acee332413`
- OLD TREE: `6363566d5b36f4669e234f31cd4660a1687c0597`
- OLD verifier blob: `73504fe6897a5b6a038da39b14478a37aa36bbc7`

Prepared attempt-1 patch:
- SHA-256: `336283e60c081ca47568262be6f39c77f8ba7af1c6264c09b64f2c57b4df7507`
- surface: `scripts/verify_repository.py` only
- numstat: `+195/-2`

Human-side exact-worktree preflight passed: exact HEAD/parent/one-commit, clean worktree, exact patch hash, `git apply --check` PASS, exact numstat.

Human-side apply and compile passed. Post-apply surface remained verifier-only `+195/-2`, and `git diff --check` was clean.

Full local verifier then failed before F040 completion at preserved regression:

`[FAIL] synthetic rejection did not fail: F021 third-level bullet continuation promotion`

Therefore attempt 1 is NOT a valid F040 repair candidate and MUST NOT be committed or pushed. No ScriptOps remote mutation occurred from this attempt.

Diagnosis: the attempt-1 list-owned indented-code start logic searched ancestors for any owner whose content indent was four or more columns shallower than the current line. After a blank line in the existing F021 deep-list regression, the current deepest leaf still owns the continuation at its own content indentation, but the new logic skipped that ownership and reclassified the line as indented code under an ancestor. That split the existing authority unit and caused the F021 expected rejection to disappear.

Correction constraint: after a blank, first resolve the deepest surviving list owner for the current indentation. Only that owner may be considered for an indented-code start, and only at owner-content-indent + 4 or deeper. Do not search past a still-owning deeper leaf merely because an ancestor would satisfy +4. This preserves F021 while retaining the bounded F040 mechanism.

Disposition: `F040 ATTEMPT 1 = LOCAL VERIFIER FAIL / NO PUSH`.

The existing Human F040 repair authority remains bounded to verifier-only F040 correction; no new finding, no merge/main/deploy/release/tag/canonical/status/X1B/V1 authority is created by this evidence record.
