# X1B-FRAME PR #37 F044-D27 finding

Disposition: **FAIL — NON-VACUOUS ADJACENT COUNTEREXAMPLE**

Exact reviewed GREEN implementation target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `ee0317c5b73e84c25823dad2bc4232fff22c5abd`
- TREE: `83db57184224392cc359b537f291ac1a2d1723c7`
- verifier entrypoint blob: `ea830bc54b9c6bc4f07905fd964539885de841c6`

## Finding

Finding ID: `F044-D27-LIST-OWNED-TAIL-CARDINALITY`

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
  >   - neutral extra final sibling
```

This is not the withdrawn top-level D16 finding. D16 proved that the pinned top-level D15 chain already handles its tail-cardinality representative. D27 instead crosses the repaired list-owned D15 shape from D26 with final-sibling cardinality: D26 is deliberately bounded to exactly one final sibling after the post-target continuation run, so an additional same-level final sibling disables that normalizer and the list-owned target self-reference can again remain fused with the promotion-bearing final child.

Non-vacuity was proven by isolated `FJ899/scriptops PR #59`, which retained the D26 verifier byte-for-byte. Probe HEAD `2bd04fdb134ec1f28d0e9bd7eac04bea52680abc` / TREE `5c1bc7cc9292747a7836c9b6648638df96c88302`.

- Verify run `34263084504`: completed/success and explicitly printed `[PASS] F044-D27 probe reproduces list-owned tail-cardinality false positive`.
- Phase 6 ScriptOps smoke run `34263084471`: completed/success including repository semantic/currentness verification and full deterministic Phase-6 regression.
- Probe PR #59 was closed without merge.

No repair, ScriptOps candidate mutation, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is recorded by this finding.
