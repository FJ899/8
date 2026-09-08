# X1B-FRAME PR #37 F044-D21 finding

Disposition: **FAIL — NON-VACUOUS ADJACENT COUNTEREXAMPLE**

Exact reviewed GREEN implementation target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `bd91d757b5a126aceb806bf5a92dc9f901eaf48b`
- TREE: `1af426ec7f35582d7bef328d6716f48729144df2`
- verifier entrypoint blob: `0d3156b954b0988672b5b183b3e1149d211f9324`

## Finding

Finding ID: `F044-D21-CONTINUATION-RUN-X-CHILD-CARDINALITY`

Representative:

```markdown
- Parent:
  > - neutral quoted parent
  >   - This file
  >     continuation one
  >     continuation two
  >   - neutral child two
  >   - neutral child three
  >   - grants release authority.
```

D18 generalizes continuation-run length only for the two-child list-owned quote shape. D20 generalizes post-continuation child-run cardinality only when child one owns exactly one ordinary continuation line. Combining the already-proven dimensions — continuation run length `>=2` and three later same-level siblings — falls through both bounded normalizers, leaving the self-reference child and later promotion sibling fused into one authority unit.

Non-vacuity was proven by isolated `FJ899/scriptops PR #47`, whose exact D20 verifier base was retained byte-for-byte. Probe HEAD `99a267913eeb47864962c2a6c85a3f4b434af483` / TREE `9cec54a88fc4c862bee323e441c5e11cad591a31`.

- Verify run `34259859158`: completed/success and explicitly printed `[PASS] F044-D21 probe reproduces continuation-run x child-cardinality false positive`.
- Phase 6 ScriptOps smoke run `34259859151`: completed/success including repository semantic/currentness verification and full deterministic Phase-6 regression.
- Probe PR #47 was closed without merge.

## Scope

This finding concerns only the cross-product of two already-proven F044 dimensions inside the existing source-column-zero outer-list-owned quote family: child-one continuation-run length and later child-run cardinality.

No repair, ScriptOps candidate mutation, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is recorded by this finding.
