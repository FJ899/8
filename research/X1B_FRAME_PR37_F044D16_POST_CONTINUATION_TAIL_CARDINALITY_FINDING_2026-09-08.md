# X1B-FRAME PR #37 — F044-D16 post-continuation tail-cardinality finding

Date: 2026-09-08
Review mode: bounded read-only adjacent probe
Disposition: **FAIL — FIRST CREDIBLE COUNTEREXAMPLE**

## Exact reviewed implementation binding

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `4eb14c672eed4a58b4f19859dbacc66e6f113be6`
TREE: `b3046dd71ae1c21fc1008da84dd1ce1999c53942`
Verifier entrypoint blob: `d12fcc3fbbadf52173d161b26d690e2bbb653bd2`
Frozen repaired F044-D14 entrypoint: `a1b4f8666ec8915532b3e12addb3abdda549dd3f`

## Finding

Finding ID: `X1B-FRAME-F044-D16-POST-CONTINUATION-TAIL-CARDINALITY`

Representative source:

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

CommonMark parses the quoted outer item as a nested list whose relevant children are all distinct: target child `This file` plus `target continuation`; `neutral post-target one` plus its continuation; marker-only `neutral post-target two`; and `grants release authority.`. Therefore target-local self-reference and the final promotion are not one authority unit.

The F044-D15 repair handles exactly one continuation-bearing post-target child followed by exactly one final sibling. In the representative, D15 treats `neutral post-target two` as that final sibling, but its `bounded_after` condition fails because the promotion sibling follows immediately. D15 therefore leaves the representative untouched.

D14 cannot recover the boundary because its post-target cardinality collector requires consecutive marker-only siblings immediately after the target continuation; the continuation owned by `neutral post-target one` breaks that run. D13 and earlier overlays likewise stop before this combined post-target-continuation plus later-cardinality shape.

Expected security decomposition:

1. outer neutral parent + `child one`;
2. outer neutral parent + `child two`;
3. outer neutral parent + `This file` + `target continuation`;
4. outer neutral parent + `neutral post-target one` + `post-target continuation`;
5. outer neutral parent + `neutral post-target two`;
6. outer neutral parent + `grants release authority.`.

Current bounded overlays do not provide that decomposition for this representative, allowing target-child self-reference to remain fused across later child items and into the promotion sibling, synthesizing a false forbidden-self-promotion rejection.

## Classification

D15 established continuation inside the first post-target child with exactly one final sibling. D16 establishes the adjacent cardinality dimension after that continuation-bearing child. This remains F044 nested quoted-list sibling-boundary recursion; it is not F042 or F043.

Review stops at this first credible counterexample.

No ScriptOps repair, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is performed by this finding record.
