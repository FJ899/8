# X1B-FRAME PR #37 F044-D24 finding

Disposition: **FAIL — NON-VACUOUS ADJACENT COUNTEREXAMPLE**

Exact reviewed GREEN implementation target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `9c91ba991b8477b71c4056e6ee0b19236d9eea8c`
- TREE: `49ff0ace737fa13d34fde7ca8f4fa607c0ecf2aa`
- verifier entrypoint blob: `595b0e461261fb56710a9e48c6865da61ef3177f`

## Finding

Finding ID: `F044-D24-LIST-OWNED-LATER-CHILD-POSITION`

Representative:

```markdown
- Parent:
  > - neutral quoted parent
  >   - child one
  >   - child two
  >   - This file
  >     target continuation
  >   - grants release authority.
```

D13 repairs the same target-child-position-three-and-later continuation shape for a source-column-zero top-level quote and explicitly leaves list-owned outer quote recursion outside its scope. D23 repairs only the list-owned child-two target shape. Therefore lifting the D13 target-position dimension into the same source-column-zero outer-list-owned quote family falls through the current bounded normalizers, leaving the target child self-reference fused with the final promotion sibling.

Non-vacuity was proven by isolated `FJ899/scriptops PR #53`, which retained the D23 verifier byte-for-byte. Probe HEAD `930e25d725d8d479b61c75c5434df003c5509fae` / TREE `0cdeca8c3117a126456cfb5f8d7f2fcb580e18ae`.

- Verify run `34261490932`: completed/success and explicitly printed `[PASS] F044-D24 probe reproduces list-owned later-child-position false positive`.
- Phase 6 ScriptOps smoke run `34261490652`: completed/success including repository semantic/currentness verification and full deterministic Phase-6 regression.
- Probe PR #53 was closed without merge.

No repair, ScriptOps candidate mutation, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is recorded by this finding.
