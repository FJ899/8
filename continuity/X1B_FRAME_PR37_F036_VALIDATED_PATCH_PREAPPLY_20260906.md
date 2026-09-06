# F036 validated patch — pre-apply evidence

Date: 2026-09-06

Exact input candidate:

- `FJ899/scriptops PR #37`
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `827d97a28bae8e4a6981739c616e1e6578a99665`
- OLD TREE `592a68f826d1b480d58319571b4df0e342f2513e`
- OLD verifier blob `cd079df9446d8a1781943670ec614615311a2564`
- finding `FJ899/8 PR #331`
- Human repair authority `FJ899/8 PR #332`
- preservation/design `FJ899/8 PR #333`

Prepared patch:

- file: `X1B_FRAME_PR37_F036_REPAIR.patch`
- SHA-256 `6877115c2a7b7e9c282fdc746b56ce816f495e8f481a45b409e29abf07d79dae`
- changed path: `scripts/verify_repository.py` only
- patch numstat: `268` additions / `1` deletion

Validation performed before real-worktree apply:

1. patch parses and passes a synthetic `git apply --check` against exact old-side hunk contexts;
2. synthetic `git apply --numstat` reports only `scripts/verify_repository.py`, `268/1`;
3. isolated parser/security harness passes representative F036 cases for top-level backtick/tilde/three-column/unclosed fences, immediate following paragraph, list closure, quote-lazy interaction, list-owned and ancestor-owned fences, invalid opening shapes, wrong-character and too-short closes, and fenced-payload self-promotion;
4. CommonMark parser cross-check confirms the representative block structures, including paragraph interruption, EOF closure, list ownership, quote-container termination, too-short/wrong-character closing behavior, and invalid backtick info-string behavior;
5. the patch preserves the existing F035/F034/F033/F032/F031/F030/F029 code and test surfaces and adds a new F036 PASS regression marker.

Mandatory before any commit/push:

- exact OLD HEAD real-worktree `git apply --check`;
- exact patch SHA verification;
- verifier-only surface check;
- Python compile;
- full local verifier PASS, including F035 and all earlier regressions plus F036.

Mandatory after replacement push:

- exact NEW HEAD remains one commit over frozen BASE;
- same frozen 12 BASE-relative changed paths;
- OLD→NEW only `scripts/verify_repository.py`;
- both existing ScriptOps GitHub Actions workflows complete successfully on exact NEW HEAD;
- freeze completion evidence and STOP before independent post-F036 review.

No ScriptOps mutation is performed by this evidence record. No merge/main/deploy/release/tag/canonical/status/X1B/V1 authority is granted.
