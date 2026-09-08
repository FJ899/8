# X1B-FRAME PR #37 — F044-D3 ordinary-continuation-run repair completion

Date: 2026-09-08
Disposition: **REPAIRED / GREEN**

## Exact implementation binding

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `07648433bd08a2aa2cbb48dc090d84e23993a914`
TREE: `dabcd6a8af5650a8282b22ae55bb07ea47e2f228`
Verifier entrypoint blob: `943e5f741f51f2e89aa2ac0264f511f31ea842b3`
Frozen prior repaired F044-D2 entrypoint: `05856621e882f5559004c7e33f4804e3ba238be8`
Changed paths: 37
Commit distance from BASE: exactly 1 ahead / 0 behind

## Repair boundary

F044-D3 generalizes the D2 root cause from exactly one to one-or-more ordinary continuation lines owned by the current inner list item's content indentation before a same-inner-level sibling marker.

Different-level list markers, blank lines, fenced/heading/thematic/HTML inner blocks, ownership loss and list-owned outer quotes terminate tracking and remain outside this repair. Same-item promotion remains one security unit and is rejected.

## Verification

- `Verify repository state` run `34189782604`: **completed / success**;
- verifier log explicitly PASSes all prior regressions plus `F044-D3 ordinary-continuation-run quoted sibling-list regression`;
- `Phase 6 ScriptOps smoke` run `34189782629`: **completed / success**;
- full deterministic Phase-6 regression passed.

This closes only the ordinary-continuation-run sibling family. It is not a global parser-completeness claim.

No merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is authorized or performed by this record.
