# Human authority — F043 destination-newline bounded repair

Human authorization received: `accept` on 2026-09-07.

This authorizes exactly one bounded verifier-only repair of the F043 destination-newline grammar-loss defect recorded in FJ899/8 PR #383.

Exact ScriptOps target:
- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `9422be98cf86bc889c2663aed4437e11a0f62cf2`
- TREE: `9df5a0a95c3e0ff3d105d391ce58a13f5fc1906f`
- verifier entrypoint blob: `040365f5825c386b1e74405ca51c63edd2ca55ac`
- pinned F043 multiline blob: `c2b5a356e744be802d204ab8eaea901e76aa1219`
- pinned F043 single-line blob: `61bf107ad59da33a6576032d341b41c538d0453a`
- pinned F041 core blob: `be645c1a3ee49a04d700a3ef7fde86a92e413a14`

Repair scope is limited to preserving physical line-ending grammar when evaluating multiline CommonMark §4.7 link-reference definitions, specifically preventing a line ending inside a link destination from being normalized into a legal space. Existing legal multiline positions (label continuation, one line ending before destination, one line ending before title, multiline title as already frozen by this verifier) and the existing list-lazy behavior must remain intact.

F042 and F044 remain OPEN and unrepaired.

After repair: rerun the full frozen verifier matrix including R1–R24, F009–F041, all prior F043 regressions and new destination-newline controls; then run both required workflows. Only after full PASS may one replacement commit, guarded ref update and completion evidence be retained.

No merge, ScriptOps main movement, deploy, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 authority is granted.
