# X1B-FRAME PR #37 F044-D29 finding

Disposition: **FAIL — NON-VACUOUS ADJACENT COUNTEREXAMPLE**

Exact reviewed GREEN implementation target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `b855b2241434501d2dc957eaeaf330886cb50626`
- TREE: `4329dd643bc9b65fa683564f7e18ecf915b25986`
- verifier entrypoint blob: `897400e515a1bcf599cfa43901447a7ca695f7d8`

## Finding

Finding ID: `F044-D29-CONTINUED-FINAL-FOLLOWING-CARDINALITY`

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
  >   - neutral following two
```

D28 repairs exactly one following same-level sibling after the continued final child and explicitly leaves multiple following final siblings outside its boundary. Adding a second following sibling therefore disables D28's bounded-after condition and allows the target-local self-reference to remain fused through the continued-final region into the promotion-bearing following child.

Non-vacuity was proven by isolated `FJ899/scriptops PR #63`, which retained the D28 verifier byte-for-byte. Probe HEAD `22184ecaea61d0ace1094ca3975124766160fc61` / TREE `2a54ed81e24167a625d6aa44e1e4ec426b8e17ed`.

- Verify run `34264342325`: completed/success and explicitly printed `[PASS] F044-D29 probe reproduces continued-final following-cardinality false positive`.
- Phase 6 ScriptOps smoke run `34264342320`: completed/success including repository semantic/currentness verification and full deterministic Phase-6 regression.
- Probe PR #63 was closed without merge.

No repair, ScriptOps candidate mutation, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is recorded by this finding.
