# X1B-FRAME PR #37 F044-D22 finding

Disposition: **FAIL — NON-VACUOUS ADJACENT COUNTEREXAMPLE**

Exact reviewed GREEN implementation target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `2e8e31de0cffb1857a7bb811246348189f332e84`
- TREE: `c8309743b1f37ee2fe899817e089c51ecda78ed5`
- verifier entrypoint blob: `d726566e683365d1071df2cd0930af88da96abd6`

## Finding

Finding ID: `F044-D22-TWO-SIBLING-MULTI-CONTINUATION`

Representative:

```markdown
- Parent:
  > - neutral quoted parent
  >   - This file
  >     continuation one
  >     continuation two
  >   - neutral child two
  >   - grants release authority.
```

This is the final missing cell in the bounded continuation-run x later-sibling-cardinality matrix for the existing source-column-zero outer-list-owned quote family. D18 handles continuation-run length >=2 with exactly one later sibling. D19 handles exactly one continuation with exactly two later siblings. D20 handles exactly one continuation with >=3 later siblings. D21 handles continuation-run length >=2 with >=3 later siblings. The combination continuation-run length >=2 with exactly two later siblings falls through those bounded normalizers and leaves the self-reference child fused with the final promotion sibling.

Non-vacuity was proven by isolated `FJ899/scriptops PR #49`, which retained the D21 verifier byte-for-byte. Probe HEAD `32457fb9393b32ee7a95649c1a8575b6ee8e7b41` / TREE `b68e9ccf55a6e5d3375073a0df9f7538d8e89a66`.

- Verify run `34260349136`: completed/success and explicitly printed `[PASS] F044-D22 probe reproduces two-sibling multi-continuation false positive`.
- Phase 6 ScriptOps smoke run `34260349086`: completed/success including repository semantic/currentness verification and full deterministic Phase-6 regression.
- Probe PR #49 was closed without merge.

No repair, ScriptOps candidate mutation, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is recorded by this finding.
