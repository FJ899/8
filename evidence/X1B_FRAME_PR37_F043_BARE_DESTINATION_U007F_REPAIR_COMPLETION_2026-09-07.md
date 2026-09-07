# X1B-FRAME PR #37 — F043 bare-destination U+007F repair completion

Human authority: `FJ899/8 PR #392`.
Finding repaired: `FJ899/8 PR #391`.

Final ScriptOps binding:
- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `96cec000860a18f01a9d3bae733a552eaff22559`
- TREE: `7ec2f777dac3bf9629019801a58ba7bc69ef8d9c`
- topology: exactly 1 commit ahead / 0 behind frozen BASE
- changed paths: 18

Verifier layering:
- `scripts/verify_repository.py`: `8dc5d3e207f3b1e82fc6384609ccc67c9c41495a`
- pinned prior `scripts/verify_repository_f043_bare_destination_escape.py`: `e20d7b4036c13d9cb74152e57c6242aad90415f0`
- pinned destination-newline: `277eb91bbcf46dfb766e39ed23962b5179450c87`
- pinned list-lazy: `040365f5825c386b1e74405ca51c63edd2ca55ac`
- pinned multiline: `c2b5a356e744be802d204ab8eaea901e76aa1219`
- pinned single-line: `61bf107ad59da33a6576032d341b41c538d0453a`
- frozen F041 core: `be645c1a3ee49a04d700a3ef7fde86a92e413a14`

Repair semantics:
- the previous recognizer remains authoritative and is run first;
- only an otherwise accepted bare destination is narrowed by rejecting ASCII control `U+007F DELETE`;
- no label/title/angle-destination/list/multiline/destination-newline/backslash-escape semantics are reinterpreted;
- F042 and F044 remain OPEN/unrepaired.

Verification on exact HEAD `96cec000860a18f01a9d3bae733a552eaff22559`:
- `Verify repository state` run `34096018942`: PASS;
- log explicitly PASSes R1-R24, F009-F041, all prior F043 regressions, and `F043 bare-destination ASCII-control U+007F regression`;
- `Phase 6 ScriptOps smoke` run `34096019061`: PASS;
- step `Run full deterministic Phase 6 regression`: PASS.

No merge, ScriptOps `main` movement, deployment, release, tag, canonical effect, status promotion, X1B reopen, or V1 authority was performed or granted.

STOP before any next review/repair transition.
