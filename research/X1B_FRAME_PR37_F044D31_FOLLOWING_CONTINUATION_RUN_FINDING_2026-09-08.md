# X1B-FRAME PR #37 F044-D31 finding

Disposition: **FAIL — REPRODUCIBLE ADJACENT CASE**

Exact reviewed GREEN predecessor:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `072084ce4a6e6cc01492e129e6ebcbc111a62636`
- TREE: `008e59d51de6d583ece3a3238af8917eef8bb0ee`
- verifier entrypoint blob: `2f2eaf443f30955d73beb7fd652cfa60f3605d7b`

Finding ID: `F044-D31-FOLLOWING-CONTINUATION-RUN`

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
  >   - grants release authority.
```

D30 intentionally repairs exactly one ordinary continuation line on the first following sibling. With two continuation lines the D30 bounded splitter delegates unchanged; D29 also cannot isolate the later sibling because the continuation run interrupts its consecutive-marker scan. The predecessor therefore fuses the target self-reference with the later promotion and produces a false-positive forbidden-self-promotion rejection.

Isolated probe `FJ899/scriptops PR #67` retained the exact D30 verifier byte-for-byte as its probe base. Verify run `34266174187` completed/success and explicitly printed `[PASS] F044-D31 probe reproduces following-continuation-run false positive`; smoke run `34266174309` completed/success including full deterministic regression. Probe closed without merge.

No repair, merge, main movement, deployment, release, tag, canonical effect, status promotion, X1B reopen or V1 action is recorded by this finding.
