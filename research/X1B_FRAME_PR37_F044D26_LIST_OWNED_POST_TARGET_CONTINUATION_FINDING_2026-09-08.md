# X1B-FRAME PR #37 F044-D26 finding

Disposition: **FAIL — NON-VACUOUS ADJACENT COUNTEREXAMPLE**

Exact reviewed GREEN implementation target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `6e44b95c8d13c08fda8d42eff0a0519c121b64c5`
- TREE: `39afa48007343a328cd48ba87f1195e9c2b95b38`
- verifier entrypoint blob: `df2f7dcc4e2a8406c7c6b8dbae81c30676979849`

## Finding

Finding ID: `F044-D26-LIST-OWNED-POST-TARGET-CONTINUATION`

Representative:

```markdown
- Parent:
  > - neutral quoted parent
  >   - child one
  >   - child two
  >   - This file
  >     target continuation
  >   - neutral post-target
  >     post-target continuation
  >   - grants release authority.
```

D15 repairs the same target+continuation -> post-target child+continuation -> final sibling shape for a source-column-zero top-level quote and explicitly leaves list-owned outer quote recursion outside its scope. D25 repairs only marker-only post-target sibling cardinality in the list-owned family. Therefore lifting the D15 post-target-child-continuation dimension into the same source-column-zero outer-list-owned quote family falls through current bounded normalizers, leaving target-local self-reference capable of being fused across the post-target child into the final promotion sibling.

Non-vacuity was proven by isolated `FJ899/scriptops PR #57`, which retained the D25 verifier byte-for-byte. Probe HEAD `a737b5acae9f4f9d0213e15ba204054b91ceff92` / TREE `676211030aa8fa9d84ec17969b83feba63a77da3`.

- Verify run `34262495200`: completed/success and explicitly printed `[PASS] F044-D26 probe reproduces list-owned post-target-continuation false positive`.
- Phase 6 ScriptOps smoke run `34262494937`: completed/success including repository semantic/currentness verification and full deterministic Phase-6 regression.
- Probe PR #57 was closed without merge.

No repair, ScriptOps candidate mutation, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is recorded by this finding.
