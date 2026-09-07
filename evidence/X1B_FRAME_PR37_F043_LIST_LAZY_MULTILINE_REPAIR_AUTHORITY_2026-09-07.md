# X1B-FRAME — F043 list-lazy multiline bounded repair authority

Human authorization: `accept`

Target: `FJ899/scriptops PR #37`

- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `3a9bac7b36be067999717b0819137c6a9524b063`
- TREE `3402de92c468cd90b0b82c8bb48e63b2c15e408f`
- verifier entrypoint blob `c2b5a356e744be802d204ab8eaea901e76aa1219`
- pinned prior F043 overlay `61bf107ad59da33a6576032d341b41c538d0453a`
- pinned F041 core `be645c1a3ee49a04d700a3ef7fde86a92e413a14`

Finding source: `FJ899/8 PR #379`.

Authorized scope is exactly one verifier-only repair of F043 list-owned multiline link-reference-definition folding when valid paragraph continuation lines omit list content indentation under CommonMark laziness. F042 and F044 remain OPEN and unrepaired.

Required gates: preserve the frozen prior verifier layers byte-for-byte; run the complete frozen synthetic/regression matrix plus F043 list-lazy controls; if green, create exactly one replacement commit over frozen BASE, guarded update of the PR branch, run both required workflows, collect completion evidence, then STOP.

No merge, main movement, deploy, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority is granted.
