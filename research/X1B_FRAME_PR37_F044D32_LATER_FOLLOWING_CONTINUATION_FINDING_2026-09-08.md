# X1B-FRAME PR #37 F044-D32 finding

Disposition: **FAIL — REPRODUCIBLE ADJACENT CASE**

Exact reviewed GREEN predecessor:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `20840d15184daf30ef1544790d7a37ae5494518d`
- TREE: `8fbb1548b1fe8a5e4991e22aaeb359409dafdf5f`
- verifier entrypoint blob: `2b3d0af9e04f79cdc6f70e08404791e0159b4ef9`

Finding ID: `F044-D32-LATER-FOLLOWING-CONTINUATION`

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
  >     following continuation one
  >     following continuation two
  >   - neutral following two
  >     later continuation
  >   - grants release authority.
```

D31 repairs the continuation-run length on the first following sibling only. When the next same-level following sibling owns an ordinary continuation line, D31 stops its later-sibling marker scan before reaching the promotion-bearing sibling and delegates the source unchanged. The predecessor therefore still fuses the target self-reference with the later promotion and produces a false-positive forbidden-self-promotion rejection.

Isolated probe `FJ899/scriptops PR #69` retained the exact D31 verifier byte-for-byte as its probe base. Verify run `34266705422` completed/success and explicitly printed `[PASS] F044-D32 probe reproduces later-following-continuation false positive`; smoke run `34266705540` completed/success including full deterministic regression. Probe closed without merge.

No repair, merge, main movement, deployment, release, tag, canonical effect, status promotion, X1B reopen or V1 action is recorded by this finding.
