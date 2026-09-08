# X1B-FRAME PR #37 F044-D23 finding

Disposition: **FAIL — NON-VACUOUS ADJACENT COUNTEREXAMPLE**

Exact reviewed GREEN implementation target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `370fe1d07e893f3b944acc7483e9a74233614871`
- TREE: `48f8ceb0b7fd73c743e0db9170ec2af5031e85db`
- verifier entrypoint blob: `ccf89daf24a4241331f62b363cc1a4358db5e07a`

## Finding

Finding ID: `F044-D23-LIST-OWNED-LATER-CHILD-CONTINUATION`

Representative:

```markdown
- Parent:
  > - neutral quoted parent
  >   - child one
  >   - This file
  >     child two continuation
  >   - grants release authority.
```

D12 repairs the same second-child-continuation shape for a source-column-zero top-level quote and explicitly leaves list-owned outer quote recursion outside its scope. D17-D22 establish the bounded source-column-zero outer-list-owned quote family, but their normalizers target child-one continuation and sibling cardinality. Lifting the D12 shape into that list-owned family therefore falls through current bounded normalizers, leaving the self-reference second child and later promotion sibling fused.

Non-vacuity was proven by isolated `FJ899/scriptops PR #51`, which retained the D22 verifier byte-for-byte. Probe HEAD `c20d4418308f296f79f88c9da1883070e5ac0509` / TREE `327a1751d270b1fc9cb7c5eb382186c54ef93679`.

- Verify run `34260899438`: completed/success and explicitly printed `[PASS] F044-D23 probe reproduces list-owned later-child-continuation false positive`.
- Phase 6 ScriptOps smoke run `34260899445`: completed/success including repository semantic/currentness verification and full deterministic Phase-6 regression.
- Probe PR #51 was closed without merge.

No repair, ScriptOps candidate mutation, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is recorded by this finding.
