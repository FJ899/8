# X1B-FRAME — F043 bare-destination escape bounded repair completion

Date: 2026-09-07

Human authority: `FJ899/8 PR #388`
Finding repaired: `FJ899/8 PR #387`

Exact ScriptOps completion binding:

- repository: `FJ899/scriptops`
- PR: `#37`
- state: open / draft / unmerged
- base branch: `main`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `4a399016525fbfc7de956e1aa03387e6dd8c1051`
- TREE: `65c2cb3009181f5a04a586901ece0426c2091bf3`
- exactly 1 commit ahead / 0 behind
- exactly 17 changed paths
- verifier entrypoint blob: `e20d7b4036c13d9cb74152e57c6242aad90415f0`
- pinned F043 destination-newline overlay: `277eb91bbcf46dfb766e39ed23962b5179450c87`
- pinned F043 list-lazy overlay: `040365f5825c386b1e74405ca51c63edd2ca55ac`
- pinned F043 multiline overlay: `c2b5a356e744be802d204ab8eaea901e76aa1219`
- pinned F043 single-line overlay: `61bf107ad59da33a6576032d341b41c538d0453a`
- pinned F041 core: `be645c1a3ee49a04d700a3ef7fde86a92e413a14`

Bounded repair result:

- single-line bare link destination backslash handling now treats backslash as an escape only before ASCII punctuation;
- backslash before non-punctuation remains literal and the next character is still parsed normally;
- `foo\ bar` and `foo\<TAB>bar` therefore cannot hide forbidden whitespace inside a bare destination;
- escaped punctuation remains valid;
- literal backslash before non-punctuation remains valid;
- a following space can still terminate the destination and introduce a legal title;
- F042 and F044 were not repaired or reinterpreted.

Verification on exact HEAD `4a399016525fbfc7de956e1aa03387e6dd8c1051`:

- `Verify repository state` run `34095140071`: `completed / success`;
- log explicitly PASSes R1-R24;
- log explicitly PASSes F009-F041;
- log explicitly PASSes F043 single-line extraction;
- log explicitly PASSes F043 multiline extraction;
- log explicitly PASSes F043 list-lazy multiline extraction;
- log explicitly PASSes F043 destination-newline grammar preservation;
- log explicitly PASSes `F043 bare-destination backslash-escape grammar regression`;
- `Phase 6 ScriptOps smoke` run `34095140064`: `completed / success`;
- smoke step `Run full deterministic Phase 6 regression`: `success`.

Outstanding findings remain:

- F042 — `OPEN / UNREPAIRED`;
- F044 — `OPEN / UNREPAIRED`.

Disposition for F043 at this repair checkpoint: `REPAIRED / GREEN` for the complete current regression matrix.

STOP before any next review/repair transition. A new post-repair adversarial review requires separate Human `accept`.

No merge, ScriptOps `main` movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 authority was performed or granted.
