# X1B-FRAME PR #37 F044-D30 finding

Disposition: **FAIL — NON-VACUOUS ADJACENT COUNTEREXAMPLE**

Exact reviewed GREEN implementation target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `8a69591e3af72bc80b28df5d19b40233d2f902fd`
- TREE: `e003b50d1e4e6c491f52e4cf7eef7b7a01e3ef0e`
- verifier entrypoint blob: `0299bf89a7fe743dee683df09f850a68567bb3e5`

## Finding

Finding ID: `F044-D30-FOLLOWING-CHILD-CONTINUATION`

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
  >   - neutral following one
  >     following continuation
  >   - grants release authority.
```

D29 repairs marker-only following-sibling cardinality in the existing list-owned D28 family and explicitly leaves continuation in following siblings outside its boundary. Giving the first following sibling one ordinary continuation line therefore disables D29's marker-only following-run normalization; the target-local self-reference can remain fused through the following child continuation into the subsequent promotion-bearing sibling.

Non-vacuity was proven by isolated `FJ899/scriptops PR #65`, which retained the D29 verifier byte-for-byte. Probe HEAD `95751e4cc6c183a57d2373f863f057762456ff41` / TREE `be851bac000451dc0479aee482aecf27e2ecb5e1`.

- Verify run `34264849302`: completed/success and explicitly printed `[PASS] F044-D30 probe reproduces following-child-continuation false positive`.
- Phase 6 ScriptOps smoke run `34264849230`: completed/success including repository semantic/currentness verification and full deterministic Phase-6 regression.
- Probe PR #65 was closed without merge.

No repair, ScriptOps candidate mutation, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is recorded by this finding.
