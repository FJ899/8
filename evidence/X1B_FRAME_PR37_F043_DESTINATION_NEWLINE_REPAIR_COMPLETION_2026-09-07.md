# X1B-FRAME PR #37 — F043 destination-newline bounded repair completion

Human repair authority: `FJ899/8 PR #384`.

Finding repaired: `FJ899/8 PR #383` — multiline folding previously collapsed a prohibited physical newline inside an angle-bracket CommonMark link destination into an ordinary space, allowing an invalid paragraph candidate to become a synthetic valid link reference definition.

## Exact ScriptOps replacement binding

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `9422be98cf86bc889c2663aed4437e11a0f62cf2`
- OLD TREE: `9df5a0a95c3e0ff3d105d391ce58a13f5fc1906f`
- NEW HEAD: `9ef034b8cb87500d2c160c88ab04c36f39ac417b`
- NEW TREE: `25fcee396a9ee81a25837863e2dfc3f124506e5f`
- topology: exactly 1 commit ahead / 0 behind frozen BASE
- changed paths: exactly 16

Verifier layers:
- entrypoint `scripts/verify_repository.py`: `277eb91bbcf46dfb766e39ed23962b5179450c87`
- pinned prior list-lazy layer `scripts/verify_repository_f043_list_lazy.py`: `040365f5825c386b1e74405ca51c63edd2ca55ac`
- pinned prior multiline layer `scripts/verify_repository_f043_multiline.py`: `c2b5a356e744be802d204ab8eaea901e76aa1219`
- pinned prior single-line layer `scripts/verify_repository_f043_singleline.py`: `61bf107ad59da33a6576032d341b41c538d0453a`
- pinned F041 core `scripts/verify_repository_f041_core.py`: `be645c1a3ee49a04d700a3ef7fde86a92e413a14`

## Repair boundary

The new entrypoint changes only the longest-valid-definition decision used by the frozen multiline collectors. It preserves physical line boundaries while checking `<...>` link destinations and rejects any fold candidate whose destination contains a physical line ending, including when the preceding character is a backslash. Legal newline-before-destination and newline-before-title behavior remains available through the frozen grammar. The already-repaired list-lazy behavior is retained unchanged behind the pinned prior layer.

F042 and F044 remain OPEN and intentionally unrepaired.

## Verification evidence

`Verify repository state`:
- run: `34093970818`
- conclusion: `success`
- log explicitly PASSes R1–R24, F009–F041, F043 single-line, F043 multiline, F043 list-lazy multiline, and `F043 destination-newline grammar-preservation regression`.

`Phase 6 ScriptOps smoke`:
- run: `34093970789`
- conclusion: `success`
- repository semantic/currentness verifier: PASS
- `Run full deterministic Phase 6 regression`: PASS

## Governance result

This record freezes completion of only the F043 destination-newline bounded repair. It grants no merge, ScriptOps main movement, deploy, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 authority.

STOP before any next review/repair transition pending separate Human authorization.
