# X1B-FRAME PR #37 — Human authority for independent post-F035 review

Date: 2026-09-06

Human acceptance authorizes exactly one independent read-only adversarial review of the repaired `FJ899/scriptops PR #37` candidate.

## Exact review binding

- repository: `FJ899/scriptops`
- PR: `#37`
- base: `main`
- BASE SHA: `2f22843ac570498b506101addeba5453ab777f08`
- repaired HEAD: `827d97a28bae8e4a6981739c616e1e6578a99665`
- repaired TREE: `592a68f826d1b480d58319571b4df0e342f2513e`
- repaired verifier blob: `cd079df9446d8a1781943670ec614615311a2564`
- F035 finding evidence: `FJ899/8 PR #325`
- F035 repair authority: `FJ899/8 PR #326`
- F035 preservation/design: `FJ899/8 PR #327`
- F035 pre-apply evidence: `FJ899/8 PR #328`
- F035 completion evidence: `FJ899/8 PR #329`

PR #37 is to remain OPEN / DRAFT / UNMERGED for this review.

## Review order and stop rule

1. Re-attack F035 first on the exact repaired verifier.
2. Preserve F034, F033, F032, F031, F030, F029 and all earlier frozen regressions.
3. Continue the remaining frozen adversarial attack frontier only until the first credible counterexample or PASS.
4. On the first credible counterexample, freeze durable finding evidence and STOP immediately before any repair.

## Negative authority

This authority does not permit repair, ScriptOps mutation, merge of PR #37 or PR #35, ScriptOps `main` movement, deploy, release, tag, canonical effect, active-product status promotion, X1B reopen, V1 action, or unrelated cleanup.

`REVIEW AUTHORITY != REPAIR AUTHORITY`
