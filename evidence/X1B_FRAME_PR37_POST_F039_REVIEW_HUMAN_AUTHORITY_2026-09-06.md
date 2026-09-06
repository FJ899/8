# X1B-FRAME PR #37 — Human authority for post-F039 independent review

Human authorization was given for exactly one independent read-only adversarial review after completion of the bounded F039 repair.

## Exact bound target

- Repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `e8e745b5787f7f98c5e2df3fd03934acee332413`
- TREE: `6363566d5b36f4669e234f31cd4660a1687c0597`
- verifier blob: `73504fe6897a5b6a038da39b14478a37aa36bbc7`
- completion evidence: `FJ899/8 PR #353`

## Review order and stop rule

1. Re-attack F039 first.
2. Preserve F038-F029 and all earlier frozen regressions/invariants.
3. Continue the frozen block-structure attack frontier only until the first credible counterexample or PASS.
4. On the first credible counterexample: freeze durable finding evidence and STOP immediately before any repair.

## Excluded authority

This authorization grants no repair authority and no authority for ScriptOps mutation, merge of PR #37 or PR #35, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1.
