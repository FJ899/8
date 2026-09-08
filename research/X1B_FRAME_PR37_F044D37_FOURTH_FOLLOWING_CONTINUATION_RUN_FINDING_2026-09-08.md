# X1B-FRAME PR #37 F044-D37 finding

Disposition: **FAIL — REPRODUCIBLE ADJACENT CASE**

Exact reviewed GREEN predecessor:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `97cd3f2734699f75526306ad7306c60a41186da7`
- TREE: `59c960976b08791d440300b212a72778940ab0da`
- verifier entrypoint blob: `b4ef7f415b245f57fb04042e860802f6825e4988`

Finding ID: `F044-D37-FOURTH-FOLLOWING-CONTINUATION-RUN`

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
  >   - neutral following four
  >     fourth continuation one
  >     fourth continuation two
  >   - grants release authority.
```

D36 repairs exactly one ordinary continuation line on the fourth following sibling. With two continuation lines D36 delegates unchanged, while D35 cannot scan through that continuation run to the promotion-bearing sibling. The predecessor therefore still fuses the target self-reference with the later promotion and produces a false-positive forbidden-self-promotion rejection.

Isolated probe `FJ899/scriptops PR #79` retained the exact D36 verifier byte-for-byte as its probe base. Verify run `34269248012` completed/success and explicitly printed `[PASS] F044-D37 probe reproduces fourth-following-continuation-run false positive`; smoke run `34269247977` completed/success including full deterministic regression. Probe closed without merge.

No repair, merge, main movement, deployment, release, tag, canonical effect, status promotion, X1B reopen or V1 action is recorded by this finding.
