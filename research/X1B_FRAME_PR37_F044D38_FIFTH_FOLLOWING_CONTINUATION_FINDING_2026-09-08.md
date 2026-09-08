# X1B-FRAME PR #37 F044-D38 finding

Disposition: **FAIL — REPRODUCIBLE ADJACENT CASE / POSITION DEPENDENCE CONFIRMED**

Exact reviewed GREEN predecessor:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `8d1e6b23234013026acecdb1c63cf87a805ffc77`
- TREE: `aef612d41c3c6b4e8c23e1d44740bc93108efa7b`
- verifier entrypoint blob: `e844cfe5b0c9abef3e147af8efe8075c02cb590e`

Finding ID: `F044-D38-FIFTH-FOLLOWING-CONTINUATION`

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
  >   - neutral following five
  >     fifth continuation
  >   - grants release authority.
```

D37 repairs the run length on the fourth following sibling only. A continuation owned by the fifth following sibling interrupts D37's later-sibling scan before the promotion-bearing sibling, so the source is delegated unchanged. The predecessor therefore still fuses the target self-reference with the later promotion and produces a false-positive forbidden-self-promotion rejection.

This finding is significant beyond the literal fifth position: D30-D37 established the same two-axis pattern at following-sibling positions one through four (`one continuation line` then `continuation run`), and D38 reproduces the same family at position five. Continuing one positional overlay at a time would therefore be an unbounded ladder rather than a new structural root cause.

Isolated probe `FJ899/scriptops PR #81` retained the exact D37 verifier byte-for-byte as its probe base. Verify run `34269928136` completed/success and explicitly printed `[PASS] F044-D38 probe reproduces fifth-following-continuation false positive`; smoke run `34269928132` completed/success including full deterministic regression. Probe closed without merge.

No repair is recorded for D38. A position-generic tail-sibling repair would materially widen the current exact-position micro-repair scope and requires a separate scope authorization. No merge, main movement, deployment, release, tag, canonical effect, status promotion, X1B reopen or V1 action is recorded by this finding.
