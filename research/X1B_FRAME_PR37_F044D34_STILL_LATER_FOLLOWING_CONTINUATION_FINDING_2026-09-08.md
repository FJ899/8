# X1B-FRAME PR #37 F044-D34 finding

Disposition: **FAIL — REPRODUCIBLE ADJACENT CASE**

Exact reviewed GREEN predecessor:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `1490182ed01f8201576d6e01a1cc9cea6221c8fb`
- TREE: `79428450a7fcf719bc90dd2355f546e64a0a958c`
- verifier entrypoint blob: `dc0f6904ea0236f00d27367b006f08357a5eaab6`

Finding ID: `F044-D34-STILL-LATER-FOLLOWING-CONTINUATION`

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
  >     still later continuation
  >   - grants release authority.
```

D33 repairs the run length on the second following sibling only. A continuation owned by the third following sibling interrupts D33's consecutive later-sibling scan before the promotion-bearing sibling, so the source is delegated unchanged. The predecessor therefore still fuses the target self-reference with the later promotion and produces a false-positive forbidden-self-promotion rejection.

Isolated probe `FJ899/scriptops PR #73` retained the exact D33 verifier byte-for-byte as its probe base. Verify run `34267610640` completed/success and explicitly printed `[PASS] F044-D34 probe reproduces still-later-following-continuation false positive`; smoke run `34267610658` completed/success including full deterministic regression. Probe closed without merge.

No repair, merge, main movement, deployment, release, tag, canonical effect, status promotion, X1B reopen or V1 action is recorded by this finding.
