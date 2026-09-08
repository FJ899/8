# X1B-FRAME PR #37 F044-D35 finding

Disposition: **FAIL — REPRODUCIBLE ADJACENT CASE**

Exact reviewed GREEN predecessor:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `8ad88847f7b954972661826d563b1d1bfe21fecd`
- TREE: `5c9dcfa3648ed8b5b10247cae65df7a6c26167ac`
- verifier entrypoint blob: `e338a69b385de05c17901bd004e27bab4c203172`

Finding ID: `F044-D35-STILL-LATER-FOLLOWING-CONTINUATION-RUN`

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
  >     later continuation one
  >     later continuation two
  >   - neutral following three
  >     still later continuation one
  >     still later continuation two
  >   - grants release authority.
```

D34 repairs exactly one ordinary continuation line on the third following sibling. With two continuation lines D34 delegates unchanged, while D33 cannot scan through that still-later continuation run to the promotion-bearing sibling. The predecessor therefore still fuses the target self-reference with the later promotion and produces a false-positive forbidden-self-promotion rejection.

Isolated probe `FJ899/scriptops PR #75` retained the exact D34 verifier byte-for-byte as its probe base. Verify run `34268166899` completed/success and explicitly printed `[PASS] F044-D35 probe reproduces still-later-following-continuation-run false positive`; smoke run `34268167007` completed/success including full deterministic regression. Probe closed without merge.

No repair, merge, main movement, deployment, release, tag, canonical effect, status promotion, X1B reopen or V1 action is recorded by this finding.
