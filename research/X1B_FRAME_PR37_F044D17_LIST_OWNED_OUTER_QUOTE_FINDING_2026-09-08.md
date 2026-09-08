# X1B-FRAME PR #37 — F044-D17 list-owned outer-quote recursion finding

Date: 2026-09-08
Review mode: isolated non-vacuity probe against exact GREEN D15 candidate
Disposition: **FAIL — CREDIBLE / REPRODUCED COUNTEREXAMPLE**

## Exact reviewed implementation binding

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `4eb14c672eed4a58b4f19859dbacc66e6f113be6`
TREE: `b3046dd71ae1c21fc1008da84dd1ce1999c53942`
Verifier entrypoint blob: `d12fcc3fbbadf52173d161b26d690e2bbb653bd2`

## Representative

```markdown
- Parent:
  > - neutral quoted parent
  >   - This file
  >     ordinary continuation
  >   - grants release authority.
```

CommonMark parses this as one outer list item containing a block quote; inside that quote is one list item (`neutral quoted parent`) whose nested child list has two distinct items: `This file` plus `ordinary continuation`, and `grants release authority.`. Therefore the child-local self-reference and sibling promotion are not one authority unit.

## Non-vacuity evidence

To avoid another scope-only false inference, this finding was tested through an isolated probe harness on `FJ899/scriptops PR #38`, based directly on the exact GREEN D15 branch. The D15 entrypoint blob `d12fcc3fbbadf52173d161b26d690e2bbb653bd2` was retained byte-for-byte as `scripts/verify_repository_probe_base.py`; the wrapper added exactly one probe and no repair.

Probe identities:

- probe PR: `FJ899/scriptops #38`
- probe HEAD: `707d36c82be36cb0e8f06d349d81ab6b3b3ccfd2`
- probe base: exact GREEN D15 HEAD `4eb14c672eed4a58b4f19859dbacc66e6f113be6`
- probe wrapper blob: `874f3920f921a4cdc5eb4cb9e8535ec42afedcbd`
- Verify run `34257200555`: **completed / success**
- verifier log explicitly prints:

```text
[PASS] F044 probe reproduces list-owned outer-quote false positive
```

- all prior F009-F044-D15 regressions also PASS in that run;
- Smoke run `34257200547`: **completed / success**;
- full deterministic Phase-6 regression passes on the isolated probe harness.

A successful probe means the exact D15 validator actually rejects the representative with `publishes forbidden self-promotion`; therefore this is a non-vacuously reproduced false positive rather than a static scope guess.

## Classification

The prior F044-D adapters operate on source-column-zero quoted structures and explicitly leave list-owned outer quote recursion outside their repair boundaries. D17 is the first confirmed list-owned-quote recursion case. It remains F044 nested quote/list authority-unit decomposition and is not F042 or F043.

Review stops at this reproduced counterexample.

No ScriptOps repair, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is performed by this finding record.
