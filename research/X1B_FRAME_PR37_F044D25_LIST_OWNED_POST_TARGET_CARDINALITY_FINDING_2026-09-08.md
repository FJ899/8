# X1B-FRAME PR #37 F044-D25 finding

Disposition: **FAIL — NON-VACUOUS ADJACENT COUNTEREXAMPLE**

Exact reviewed GREEN implementation target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `ecb9ff719e3618c28cda49e35966bb1fd3bc519e`
- TREE: `248c65a6e21ba7773ffa820a50be8b2409974681`
- verifier entrypoint blob: `e3062750190721451548f241a8ae91acad6e6770`

## Finding

Finding ID: `F044-D25-LIST-OWNED-POST-TARGET-CARDINALITY`

Representative:

```markdown
- Parent:
  > - neutral quoted parent
  >   - child one
  >   - child two
  >   - This file
  >     target continuation
  >   - grants release authority.
  >   - neutral later sibling
```

D14 repairs the same post-target sibling-cardinality dimension for a source-column-zero top-level quote and explicitly leaves list-owned outer quote recursion outside its scope. D24 repairs only the list-owned target-position shape with exactly one final sibling. Therefore lifting the D14 cardinality dimension into the same source-column-zero outer-list-owned quote family falls through the current bounded normalizers, leaving the target child self-reference fused with a post-target promotion sibling when at least two later siblings are present.

Non-vacuity was proven by isolated `FJ899/scriptops PR #55`, which retained the D24 verifier byte-for-byte. Probe HEAD `a9b37886609c08383911f0568ccf248ef08fb529` / TREE `d19bf4e8b0b5efe3b8541a32d12f6a44fd81bf73`.

- Verify run `34261945070`: completed/success and explicitly printed `[PASS] F044-D25 probe reproduces list-owned post-target-cardinality false positive`.
- Phase 6 ScriptOps smoke run `34261944979`: completed/success including repository semantic/currentness verification and full deterministic Phase-6 regression.
- Probe PR #55 was closed without merge.

No repair, ScriptOps candidate mutation, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is recorded by this finding.
