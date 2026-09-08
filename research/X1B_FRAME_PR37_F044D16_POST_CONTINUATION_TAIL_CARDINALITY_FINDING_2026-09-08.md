# X1B-FRAME PR #37 — F044-D16 post-continuation tail-cardinality probe correction

Date: 2026-09-08
Review mode: bounded adjacent probe with non-vacuity verification
Disposition: **PASS — PROPOSED FINDING WITHDRAWN**

## Exact reviewed implementation binding

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `4eb14c672eed4a58b4f19859dbacc66e6f113be6`
TREE: `b3046dd71ae1c21fc1008da84dd1ce1999c53942`
Verifier entrypoint blob: `d12fcc3fbbadf52173d161b26d690e2bbb653bd2`

## Probed representative

```markdown
> - neutral parent
>   - child one
>   - child two
>   - This file
>     target continuation
>   - neutral post-target one
>     post-target continuation
>   - neutral post-target two
>   - grants release authority.
```

An independent CommonMark oracle parses these as distinct nested child items, so the probe was initially suspected to expose a continuation-to-tail boundary gap.

## Non-vacuity result

Before accepting that suspicion as a repairable finding, a bounded D16 candidate added an explicit non-vacuity oracle requiring the pinned D15 predecessor to reproduce a forbidden self-promotion unit for the representative.

Candidate-only identities:

- attempted candidate HEAD: `046122d3fa63c579fc159a72dcd1a4b329a78424`
- attempted candidate TREE: `c385b7fabf80be737bfc8f627a5347e914ee4225`
- attempted verifier blob: `2b9a0da08fd0037161c032b991ba3c6b00bf9ed2`

The existing smoke run `34256808188` failed immediately in the repository semantic/currentness verifier with:

```text
[FAIL] F044-D16 predecessor no longer reproduces tail-cardinality finding
```

All prior F009-F044-D15 regressions printed PASS before this intentional non-vacuity failure. The full deterministic Phase-6 regression was therefore skipped.

This means the pinned D15 predecessor already avoids a forbidden self-promotion unit for this representative through the composed earlier overlay chain. The initially inferred D16 defect is therefore **not reproducible on the exact reviewed candidate** and is not a credible new F044 finding.

## State correction

The attempted D16 replacement candidate was not accepted. `FJ899/scriptops PR #37` was restored to the last verified GREEN D15 implementation:

- HEAD `4eb14c672eed4a58b4f19859dbacc66e6f113be6`
- TREE `b3046dd71ae1c21fc1008da84dd1ce1999c53942`
- verifier blob `d12fcc3fbbadf52173d161b26d690e2bbb653bd2`
- Verify run `34256511425`: PASS
- Smoke run `34256511328`: PASS

No D16 repair is retained. No merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action was performed.
