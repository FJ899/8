# X1B-FRAME PR #37 — F044-D15 post-target-continuation finding

Date: 2026-09-08
Review mode: bounded read-only adjacent probe
Disposition: **FAIL — FIRST CREDIBLE COUNTEREXAMPLE**

## Exact reviewed implementation binding

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `8a3dfe342d0539507cbaca16af46eab26095021a`
TREE: `6082d77b1cabe7c96c32e581a234d44405bec58c`
Verifier entrypoint blob: `a1b4f8666ec8915532b3e12addb3abdda549dd3f`
Frozen repaired F044-D13 entrypoint: `35f8fa0fa4004f00c57f1dc8e9d9432819022a84`

## Finding

Finding ID: `X1B-FRAME-F044-D15-POST-TARGET-CONTINUATION`

Representative source:

```markdown
> - neutral parent
>   - child one
>   - child two
>   - This file
>     target continuation
>   - neutral post-target
>     post-target continuation
>   - grants release authority.
```

CommonMark parses the quoted outer item as a nested list whose relevant child items are distinct: `This file` plus `target continuation`; `neutral post-target` plus `post-target continuation`; and `grants release authority.`. Therefore target-local self-reference and the final sibling promotion are not one authority unit.

The F044-D14 repair intentionally excludes continuation inside post-target children. Its post-target collector accepts only consecutive same-level nonempty list markers. After collecting the first post-target marker (`neutral post-target`), the following ordinary continuation is not a list marker, so collection stops with only one post-target marker. Because D14 requires at least two collected post-target siblings and EOF/blank immediately after the bounded run, the D14 normalizer leaves the representative untouched.

D13 likewise treats the first post-target marker as its one final sibling and then fails its bounded-after check because the sibling owns a nonblank continuation. D12 and the child-one continuation overlays do not cover this later target/post-target structure. The lower consecutive quoted sibling splitter loses same-level marker tracking across ordinary continuation text, leaving the continuation-to-next-sibling boundary unavailable.

Expected security decomposition:

1. outer neutral parent + `child one`;
2. outer neutral parent + `child two`;
3. outer neutral parent + `This file` + `target continuation`;
4. outer neutral parent + `neutral post-target` + `post-target continuation`;
5. outer neutral parent + `grants release authority.`.

Current bounded overlays do not produce that decomposition for this representative, so target-child self-reference may remain fused across the post-target child and into the final promotion sibling, synthesizing a false forbidden-self-promotion rejection.

## Classification

D14 parameterized the number of marker-only post-target siblings. D15 establishes an adjacent structural dimension: a post-target sibling may itself own ordinary continuation text before the next sibling boundary. This remains F044 nested quoted-list sibling-boundary recursion; it is not F042 or F043.

Review stops at this first credible counterexample.

No ScriptOps repair, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is performed by this finding record.
