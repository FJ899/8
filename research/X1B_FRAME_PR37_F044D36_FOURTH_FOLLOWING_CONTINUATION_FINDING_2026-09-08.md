# X1B-FRAME PR #37 F044-D36 finding

Disposition: **FAIL — REPRODUCIBLE ADJACENT CASE**

Exact reviewed GREEN predecessor:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `29bff8404fe0275d5f194e34b4bc2bf8b8fdcd7d`
- TREE: `c4e10a2727c44846b776168b05b1c5acc5281370`
- verifier entrypoint blob: `f4c9824b20d95275dfd832b289155d60052b8645`

Finding ID: `F044-D36-FOURTH-FOLLOWING-CONTINUATION`

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
  >     fourth continuation
  >   - grants release authority.
```

D35 repairs the run length on the third following sibling only. A continuation owned by the fourth following sibling interrupts D35's consecutive later-sibling scan before the promotion-bearing sibling, so the source is delegated unchanged. The predecessor therefore still fuses the target self-reference with the later promotion and produces a false-positive forbidden-self-promotion rejection.

Isolated probe `FJ899/scriptops PR #77` retained the exact D35 verifier byte-for-byte as its probe base. Verify run `34268653099` completed/success and explicitly printed `[PASS] F044-D36 probe reproduces fourth-following-continuation false positive`; smoke run `34268653184` completed/success including full deterministic regression. Probe closed without merge.

No repair, merge, main movement, deployment, release, tag, canonical effect, status promotion, X1B reopen or V1 action is recorded by this finding.
