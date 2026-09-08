# X1B-FRAME PR #37 F044-D33 finding

Disposition: **FAIL — REPRODUCIBLE ADJACENT CASE**

Exact reviewed GREEN predecessor:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `f5c8fc78f034cf0ef1b8d68a98bd62b93b8b35a7`
- TREE: `73b9cdbd7d7fda3434dd579e085f932b6013f835`
- verifier entrypoint blob: `30e90f016803ee127e24eec79b3bc7194c297d0d`

Finding ID: `F044-D33-LATER-FOLLOWING-CONTINUATION-RUN`

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
  >   - grants release authority.
```

D32 repairs exactly one ordinary continuation line on the second following sibling. With two continuation lines D32 delegates unchanged, while D31 cannot scan through that later continuation run to the promotion-bearing sibling. The predecessor therefore still fuses the target self-reference with the later promotion and produces a false-positive forbidden-self-promotion rejection.

Isolated probe `FJ899/scriptops PR #71` retained the exact D32 verifier byte-for-byte as its probe base. Verify run `34267142489` completed/success and explicitly printed `[PASS] F044-D33 probe reproduces later-following-continuation-run false positive`; smoke run `34267142510` completed/success including full deterministic regression. Probe closed without merge.

No repair, merge, main movement, deployment, release, tag, canonical effect, status promotion, X1B reopen or V1 action is recorded by this finding.
