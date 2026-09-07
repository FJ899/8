# X1B-FRAME PR #37 — F043 bare-destination angle-character bounded repair completion evidence

Date: 2026-09-07
Authority: `FJ899/8 PR #400`
Finding source: `FJ899/8 PR #399`

## Exact final ScriptOps binding

Repository: `FJ899/scriptops`
PR: `#37`
State: OPEN / DRAFT / UNMERGED
Base branch: `main`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `1c158cc78bd7f9012e98864c5baa265c4a7ddcdc`
TREE: `786ce4af139984f5a0a6ece5f0f29542c2965254`
Topology: exactly 1 commit ahead / 0 behind BASE
Changed paths: 20

Verifier entrypoint:
- `scripts/verify_repository.py`
- blob `a81ba336e7b324961988cee89e107680a5c6b76f`

Pinned predecessor layers:
- `scripts/verify_repository_f043_parenthesized_title.py` = `1bf97ebb68a72cc0e576876d91b3f754a2141c0e`
- `scripts/verify_repository_f043_bare_destination_u007f.py` = `8dc5d3e207f3b1e82fc6384609ccc67c9c41495a`
- `scripts/verify_repository_f043_bare_destination_escape.py` = `e20d7b4036c13d9cb74152e57c6242aad90415f0`
- `scripts/verify_repository_f043_destination_newline.py` = `277eb91bbcf46dfb766e39ed23962b5179450c87`
- `scripts/verify_repository_f043_list_lazy.py` = `040365f5825c386b1e74405ca51c63edd2ca55ac`
- `scripts/verify_repository_f043_multiline.py` = `c2b5a356e744be802d204ab8eaea901e76aa1219`
- `scripts/verify_repository_f043_singleline.py` = `61bf107ad59da33a6576032d341b41c538d0453a`
- `scripts/verify_repository_f041_core.py` = `be645c1a3ee49a04d700a3ef7fde86a92e413a14`

## Repair boundary delivered

The F043 recognizer now follows the bounded CommonMark bare-destination angle-character rule:
- a leading `<` still selects the angle-bracket destination form and therefore cannot begin a bare destination;
- `>` is legal in an otherwise valid bare destination;
- `<` is legal after the first character in an otherwise valid bare destination;
- existing whitespace and ASCII-control rejection, including U+007F, remains preserved;
- corrected bare-destination backslash-escape semantics remain preserved;
- unescaped parentheses still must balance;
- title parsing, including the parenthesized-title internal-unescaped-`(` repair, remains preserved;
- multiline folding, physical destination-newline protection, list-lazy handling, container ownership, and all prior F043/F041 regressions remain preserved.

The exact PR #399 representative `[This file]: >` is now treated as a valid link-reference definition and does not falsely fuse its self-reference metadata with a following promotion paragraph.

F042 and F044 remain OPEN / unrepaired.

## Required verification

Exact HEAD `1c158cc78bd7f9012e98864c5baa265c4a7ddcdc`:

- `Verify repository state` run `34098109998`: PASS.
  - R1-R24: PASS.
  - F009-F041: PASS.
  - all prior F043 regression layers: PASS.
  - `F043 bare-destination angle-character grammar regression`: PASS.
  - X1B coherence/currentness assertions: PASS.
- `Phase 6 ScriptOps smoke` run `34098110036`: PASS.
  - repository semantic/currentness verifier: PASS.
  - full deterministic Phase-6 regression: PASS.

## Completion disposition

`F043 = REPAIRED / GREEN under the current implemented regression suite.`

This evidence does not independently adversarially close F043. A separate Human `accept` is required before any next read-only post-repair adversarial review.

`F042 = OPEN / UNREPAIRED.`
`F044 = OPEN / UNREPAIRED.`

No merge, ScriptOps `main` movement, deploy, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1 action occurred or is authorized by this record.

STOP before any next review/repair transition.
