# F040 validated patch pre-apply evidence

## Exact input

- ScriptOps PR #37
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `e8e745b5787f7f98c5e2df3fd03934acee332413`
- OLD TREE `6363566d5b36f4669e234f31cd4660a1687c0597`
- OLD verifier blob `73504fe6897a5b6a038da39b14478a37aa36bbc7`
- finding PR #355
- Human repair authority PR #356
- preservation/design PR #357

## Prepared patch

- path: `scripts/verify_repository.py` only
- additions: `195`
- deletions: `2`
- SHA-256: `336283e60c081ca47568262be6f39c77f8ba7af1c6264c09b64f2c57b4df7507`

The patch adds bounded indented-code leaf state, preserves paragraph non-interruption, prevents list/quote paragraph-laziness from crossing an indented-code leaf boundary, and adds non-vacuous F040 regressions while preserving the prior parser paths.

Pre-apply checks completed in the preparation environment:
- unified patch parses and reports verifier-only `195/2` numstat;
- synthetic exact-context apply-check PASS;
- synthetic apply and `git diff --check` PASS;
- bounded F040 top-level/list/quote semantic harness PASS;
- patch has no synthetic `index` binding and remains context-applicable.

These preparation checks are not completion evidence. Exact OLD HEAD real-worktree `git apply --check`, patch hash/numstat confirmation, apply, Python compile, full verifier PASS including F009-F040/R1-R24, one-commit replacement topology, guarded lease push, and both remote workflows on the exact repaired HEAD remain mandatory.

No ScriptOps mutation has been performed by this evidence record. No merge/main/deploy/release/tag/canonical/status/X1B/V1 authority.
