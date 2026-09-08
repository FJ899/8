# X1B-FRAME PR #37 — F044-D18 list-owned quote continuation-run finding

Date: 2026-09-08
Review mode: isolated non-vacuity probe against exact GREEN D17 candidate
Disposition: **FAIL — CREDIBLE / REPRODUCED COUNTEREXAMPLE**

## Exact reviewed implementation binding

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `87b08053393dd1864aef04bd1c0470c1b0e7ad1c`
TREE: `f63be61ad152a59c577db54e6f5c133edeb714ca`
Verifier entrypoint blob: `bb159df7a1920b952d7a65ea741cca2460128b00`

## Representative

```markdown
- Parent:
  > - neutral quoted parent
  >   - This file
  >     continuation one
  >     continuation two
  >   - grants release authority.
```

CommonMark keeps `This file` plus both continuation lines in one nested child item and `grants release authority.` in the following sibling item. The self-reference and promotion therefore belong to distinct child authority units.

## Non-vacuity evidence

This adjacent shape was tested through isolated `FJ899/scriptops PR #40`, based directly on exact GREEN D17. The exact D17 entrypoint blob `bb159df7a1920b952d7a65ea741cca2460128b00` was retained byte-for-byte as `scripts/verify_repository_probe_base.py`; the wrapper added only this probe.

Probe identities:

- probe PR: `FJ899/scriptops #40`
- probe HEAD: `9ea6c6055e30da3b9e58122552b58bf6aed37b7b`
- probe base: exact GREEN D17 HEAD `87b08053393dd1864aef04bd1c0470c1b0e7ad1c`
- probe wrapper blob: `c40a3b2824e08db215612dc9c26fb8808ab1e69a`
- Verify run `34257893710`: **completed / success**
- verifier log explicitly prints:

```text
[PASS] F044-D18 probe reproduces list-owned two-continuation false positive
```

- all prior F009-F044-D17 regressions also PASS;
- Smoke run `34257893750`: **completed / success**, including full deterministic Phase-6 regression.

A successful probe means the exact D17 validator actually rejects the representative with `publishes forbidden self-promotion`; this is therefore a reproduced false positive, not a scope-only inference.

## Classification

D17 repaired the same list-owned outer-quote child/sibling shape for exactly one ordinary continuation line. D18 demonstrates the same root cause for continuation-run length two. The newly proven parameter is continuation-run length within that exact list-owned quote family.

This remains F044 nested quote/list authority-unit decomposition and is not F042 or F043. Review stops at this reproduced counterexample.

No ScriptOps repair, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is performed by this finding record.
