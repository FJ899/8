# X1B-FRAME PR37 F040 attempt-3 expectation correction pre-apply — 2026-09-06

## Binding

- ScriptOps target: `FJ899/scriptops PR #37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `e8e745b5787f7f98c5e2df3fd03934acee332413`
- OLD TREE: `6363566d5b36f4669e234f31cd4660a1687c0597`
- OLD verifier blob: `73504fe6897a5b6a038da39b14478a37aa36bbc7`
- F040 finding: PR #355
- Human repair authority: PR #356
- preservation/design: PR #357
- attempt-1 pre-apply: PR #358
- attempt-1 local failure: PR #359
- attempt-2 correction pre-apply: PR #360
- attempt-2 local failure: PR #362

## Exact correction

Prepared delta path: `scripts/verify_repository.py` only.

SHA-256:

`87242696e1955f8b817a3c992e0ef39e4e0bbd28a6ef2c1d04447d24ef63cdbb`

Patch numstat: `+11/-5`.

The delta changes no parser behavior. It changes one stale F021 regression expectation only.

Former control:

```markdown
    - This file contains background notes.

    - Release authority belongs to a separate Human gate.
```

Formerly this was expected to be benign to demonstrate that a standalone four-space bullet-looking line is not a top-level list marker.

CommonMark 0.31.2 §4.4 makes the stronger structural fact explicit: an indented code block may contain multiple indented chunks separated by blank lines. Therefore the two chunks above are one literal indented-code block, not two top-level list siblings. Under the F040 security-unit model, their literal contents remain in one unit and the representative must be rejected.

The new expectation uses `expect_failure_message(..., "publishes forbidden self-promotion", ...)`. This preserves and strengthens the F021 classification invariant: if the parser incorrectly reclassified the two four-space bullet-looking chunks as top-level list siblings, the self-reference and authority phrase would be split and this regression would stop rejecting.

Synthetic patch parsing and exact-context apply-check on the unchanged F021 source block passed. No ScriptOps commit or push exists. Real dirty-worktree apply-check, compile, full verifier, and final diff checks remain mandatory.

No link-reference work, generic parser expansion, merge/main/deploy/release/tag/canonical/status/X1B/V1 authority.
