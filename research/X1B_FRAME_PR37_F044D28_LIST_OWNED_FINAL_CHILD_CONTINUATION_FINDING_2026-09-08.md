# X1B-FRAME PR #37 F044-D28 finding

Disposition: **FAIL — NON-VACUOUS ADJACENT COUNTEREXAMPLE**

Exact reviewed GREEN implementation target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `0d8c44cd6aa189361889925d93a6f19a66300746`
- TREE: `9eec23049b2b69db55c4a757b010ee9cc6c94b0e`
- verifier entrypoint blob: `0880d22461495d2ea349fe2fb49dcd50470a8f47`

## Finding

Finding ID: `F044-D28-LIST-OWNED-FINAL-CHILD-CONTINUATION`

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
  >   - neutral final one
  >     final continuation
  >   - grants release authority.
```

D27 repairs marker-only final-sibling cardinality in the existing list-owned D26 family and explicitly leaves continuation inside a final sibling outside its boundary. Giving the first final sibling one ordinary continuation line therefore disables D27's marker-only final-sibling run normalization; the target-local self-reference can remain fused across the final child continuation into the following promotion-bearing sibling.

Non-vacuity was proven by isolated `FJ899/scriptops PR #61`, which retained the D27 verifier byte-for-byte. Probe HEAD `e2bca5507171f9479c48e6905145f174602dea32` / TREE `9f7b38b5e5d435bad66ae1e982d604c527f5db7b`.

- Verify run `34263766506`: completed/success and explicitly printed `[PASS] F044-D28 probe reproduces list-owned final-child-continuation false positive`.
- Phase 6 ScriptOps smoke run `34263766503`: completed/success including repository semantic/currentness verification and full deterministic Phase-6 regression.
- Probe PR #61 was closed without merge.

No repair, ScriptOps candidate mutation, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is recorded by this finding.
