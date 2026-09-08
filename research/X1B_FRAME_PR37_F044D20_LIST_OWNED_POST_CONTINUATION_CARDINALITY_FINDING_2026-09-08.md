# X1B-FRAME PR #37 — F044-D20 list-owned post-continuation child-cardinality finding

Date: 2026-09-08
Review mode: isolated non-vacuity probe against exact GREEN D19 candidate
Disposition: **FAIL — CREDIBLE / REPRODUCED COUNTEREXAMPLE**

## Exact reviewed implementation binding

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `abbd698275b0198742d40dff83d69354d4841f59`
TREE: `131fa6ac7e3d969aba41bdf44dfe48a8b20a4a20`
Verifier entrypoint blob: `0803d1d0bca814740f5336569c49b798e7fcdd46`

## Representative

```markdown
- Parent:
  > - neutral quoted parent
  >   - This file
  >     ordinary continuation
  >   - neutral child two
  >   - neutral child three
  >   - grants release authority.
```

CommonMark keeps all nested quoted child items distinct. The self-reference child plus its continuation, both neutral siblings, and the final promotion sibling are separate list items.

## Non-vacuity evidence

Isolated `FJ899/scriptops PR #44` was based directly on exact GREEN D19 and retained verifier blob `0803d1d0bca814740f5336569c49b798e7fcdd46` byte-for-byte as the probe base. Probe HEAD: `fb15a59f9d99d25491b3c69d6a3f7c1800009962`.

- Verify run `34258896305`: **completed / success** and explicitly prints `[PASS] F044-D20 probe reproduces list-owned four-child false positive`;
- all prior regressions through D19 PASS;
- Smoke run `34258896554`: **completed / success**, including full deterministic Phase-6 regression.

Therefore exact GREEN D19 genuinely rejects this representative with forbidden self-promotion; the finding is non-vacuous.

## Classification

D17 handles one post-continuation sibling; D19 handles exactly two. D20 demonstrates the same list-owned quote sibling-boundary root cause with three post-continuation same-level child markers. The newly confirmed dimension is post-continuation sibling-run cardinality.

No repair, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is performed by this finding record.
