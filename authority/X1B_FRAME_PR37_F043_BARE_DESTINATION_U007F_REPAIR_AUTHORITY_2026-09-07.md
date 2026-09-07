# X1B-FRAME PR #37 — F043 bare-destination U+007F repair authority

Human authorization: `accept`.

Authorizes exactly one bounded verifier-only repair of the F043 bare-destination ASCII-control defect recorded in `FJ899/8 PR #391`.

Exact ScriptOps target:
- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- pre-repair HEAD: `4a399016525fbfc7de956e1aa03387e6dd8c1051`
- pre-repair TREE: `65c2cb3009181f5a04a586901ece0426c2091bf3`
- verifier entrypoint blob: `e20d7b4036c13d9cb74152e57c6242aad90415f0`
- prior destination-newline blob: `277eb91bbcf46dfb766e39ed23962b5179450c87`
- prior list-lazy blob: `040365f5825c386b1e74405ca51c63edd2ca55ac`
- prior multiline blob: `c2b5a356e744be802d204ab8eaea901e76aa1219`
- prior single-line blob: `61bf107ad59da33a6576032d341b41c538d0453a`
- frozen F041 core blob: `be645c1a3ee49a04d700a3ef7fde86a92e413a14`

Bounded repair scope:
- reject ASCII control `U+007F DELETE` when it occurs inside a bare CommonMark link destination;
- preserve all previous F043 semantics and SHA-pinned layers;
- preserve F042 and F044 as OPEN/unrepaired;
- one replacement commit over the frozen ScriptOps BASE;
- run the full existing verifier/regression matrix and both required workflows;
- record completion evidence only after PASS.

Not authorized: repair of F042/F044, merge, ScriptOps `main` movement, deployment, release, tag, canonical effect, status promotion, X1B reopen, or V1 authority.
