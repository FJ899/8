# X1B-FRAME PR #37 — Human authority for post-F038 independent review

Human input: `accept`

This records authority for exactly one independent read-only adversarial review of repaired `FJ899/scriptops PR #37`.

Exact target:
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `8ae5e9ac5f1c3ea48eccec25367ff0081d65df21`
- TREE `09555ed85e4f70fd99d6df61ee9b2db459281448`
- verifier blob `216231f460da2a775fa76c49081d50a74e943743`
- F038 repair completion evidence `FJ899/8 PR #347`

Review order and stop rule:
1. Re-attack F038 first.
2. Preserve F037 through F029 and all earlier regressions.
3. Continue the remaining frozen adversarial frontier.
4. At the first credible counterexample, record a durable finding and STOP before any repair.
5. If no credible counterexample remains, record PASS.

This authority is review-only. It grants no repair, ScriptOps mutation, merge of PR #37 or PR #35, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority.
