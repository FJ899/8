# X1B-FRAME PR #37 — F044-D19 list-owned quote child-cardinality finding

Date: 2026-09-08
Review mode: isolated non-vacuity probe against exact GREEN D18 candidate
Disposition: **FAIL — CREDIBLE / REPRODUCED COUNTEREXAMPLE**

## Exact reviewed implementation binding

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `2f26fdc522a32638795332a3a28a14f79366fb08`
TREE: `0c0e6d87f0b005d6156e25b94f01edb72c22b5b4`
Verifier entrypoint blob: `b575f659b3b22ca8d2f5fef8d8c68f295e5faa5a`

## Representative

```markdown
- Parent:
  > - neutral quoted parent
  >   - This file
  >     ordinary continuation
  >   - neutral child two
  >   - grants release authority.
```

CommonMark keeps the nested quoted child items distinct: child one contains `This file` plus its ordinary continuation; child two is neutral; child three contains `grants release authority.`. Therefore the child-one self-reference and child-three promotion are not one authority unit.

## Non-vacuity evidence

This adjacent shape was tested through isolated `FJ899/scriptops PR #42`, based directly on exact GREEN D18. The exact D18 entrypoint blob `b575f659b3b22ca8d2f5fef8d8c68f295e5faa5a` was retained byte-for-byte as `scripts/verify_repository_probe_base.py`; the wrapper added only this probe.

Probe identities:

- probe PR: `FJ899/scriptops #42`
- probe HEAD: `1f99f6892cf2cd76a3daffbe638812e78e716477`
- probe base: exact GREEN D18 HEAD `2f26fdc522a32638795332a3a28a14f79366fb08`
- probe wrapper blob: `74cd47a1572a085874f91f6acf0b45018fd6454a`
- Verify run `34258369743`: **completed / success**
- verifier log explicitly prints:

```text
[PASS] F044-D19 probe reproduces list-owned child-cardinality false positive
```

- all prior F009-F044-D18 regressions also PASS;
- Smoke run `34258369745`: **completed / success**, including full deterministic Phase-6 regression.

A successful probe means the exact D18 validator actually rejects the representative with `publishes forbidden self-promotion`; this is therefore a reproduced false positive, not a static scope inference.

## Classification

D17 established the list-owned outer-quote sibling boundary for two child items with one continuation line, and D18 parameterized continuation-run length. D19 demonstrates the adjacent child-cardinality dimension: one additional same-level marker-only child between the continuation-bearing self-reference child and the promotion child reopens the false-positive fusion.

This remains F044 nested quote/list authority-unit decomposition and is not F042 or F043. Review stops at this reproduced counterexample.

No ScriptOps repair, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is performed by this finding record.
