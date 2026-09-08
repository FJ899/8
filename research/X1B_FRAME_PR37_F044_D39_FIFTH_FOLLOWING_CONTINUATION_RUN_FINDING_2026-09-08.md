# X1B-FRAME PR #37 F044-D39 finding

Disposition: **FAIL — REPRODUCIBLE ADJACENT RUN-LENGTH CASE**

Exact reviewed GREEN predecessor:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `efb09d67314f41ff249c2e61054d2d13d6251f70`
- TREE: `d4b29d5dc63925b7eee1cf566618cb63ee203cb3`
- verifier entrypoint blob: `94f506fd07113733438a25a11ab625ede6274806`

Finding ID: `F044-D39-FIFTH-FOLLOWING-CONTINUATION-RUN`

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
  >     fifth continuation one
  >     fifth continuation two
  >   - grants release authority.
```

D38 repairs exactly one ordinary continuation line on the fifth following sibling and deliberately delegates two-or-more lines. The representative therefore remains unchanged by the D38 pre-normalizer; the predecessor still fuses the target self-reference with the later promotion-bearing sibling and produces a false-positive forbidden-self-promotion rejection.

This is the run-length pair to D38 at the same fifth position. It does not authorize a position-generic tail-sibling refactor or a sixth-position repair.

Isolated probe `FJ899/scriptops PR #83` retained the exact GREEN D38 verifier byte-for-byte as `scripts/verify_repository_probe_base.py`. Verify run `34271206384` completed/success and explicitly printed `[PASS] F044-D39 probe reproduces fifth-following-continuation-run false positive`; smoke run `34271206567` completed/success including the full deterministic regression. Probe closed without merge.

No repair is recorded by this finding. No merge, main movement, deployment, release, tag, canonical effect, status promotion, X1B reopen or V1 action is recorded.
