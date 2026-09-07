# X1B-FRAME — Human authority for post-F043-list-lazy adversarial review

## Human authorization

Human supplied `accept` for exactly one read-only post-repair adversarial review.

## Exact review target

- Repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `9422be98cf86bc889c2663aed4437e11a0f62cf2`
- TREE: `9df5a0a95c3e0ff3d105d391ce58a13f5fc1906f`
- Verifier entrypoint blob: `040365f5825c386b1e74405ca51c63edd2ca55ac`
- Pinned F043 multiline overlay: `c2b5a356e744be802d204ab8eaea901e76aa1219`
- Pinned F043 single-line overlay: `61bf107ad59da33a6576032d341b41c538d0453a`
- Pinned F041 core: `be645c1a3ee49a04d700a3ef7fde86a92e413a14`

## Review order and stopping rule

1. Re-attack F043 first, including the newly repaired list-lazy multiline frontier.
2. Preserve F042 and F044 as OPEN / unrepaired.
3. Stop at the first credible counterexample, or record PASS for the declared F043 frontier if none is found.

## Explicit prohibitions

This authorization grants no repair authority and no merge, default-branch movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen, V1 authority, or capability expansion.
