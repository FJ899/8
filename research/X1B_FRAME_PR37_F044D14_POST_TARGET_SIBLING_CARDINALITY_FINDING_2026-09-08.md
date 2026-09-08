# X1B-FRAME PR #37 — F044-D14 post-target sibling-cardinality finding

Date: 2026-09-08
Review mode: bounded read-only adjacent probe
Disposition: **FAIL — FIRST CREDIBLE COUNTEREXAMPLE**

## Exact reviewed implementation binding

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `7badb857fbface0dfb8aa9c65077271a3069abbc`
TREE: `a347c94f9f280cfacee4426af72d564599f6dd14`
Verifier entrypoint blob: `35f8fa0fa4004f00c57f1dc8e9d9432819022a84`
Frozen repaired F044-D12 entrypoint: `6a71863f5488e287780ba536079ba6c19fa4e302`

## Finding

Finding ID: `X1B-FRAME-F044-D14-POST-TARGET-SIBLING-CARDINALITY`

Representative source:

```markdown
> - neutral parent
>   - child one
>   - child two
>   - This file
>     target continuation
>   - grants release authority.
>   - neutral later sibling
```

CommonMark parses the quoted outer item as a nested list whose child items are distinct: `child one`; `child two`; `This file` plus `target continuation`; `grants release authority.`; and `neutral later sibling`. Therefore the target-child self-reference and the following promotion are not one authority unit.

The F044-D13 repair intentionally covers target-child positions three and later only when exactly one final same-level sibling follows the target continuation run. Its normalizer records the first same-level post-target list marker as `final_sibling_index`, then requires `final_sibling_index + 1` to be EOF or blank. The extra `neutral later sibling` makes that bounded-after condition false, so D13 leaves this representative untouched.

D11 generalized child cardinality only after a child-one continuation run. D12 handles child-two continuation with exactly one later sibling. Thus neither predecessor covers this later-position target with multiple post-target siblings. The lower consecutive quoted sibling splitter also cannot supply the missing boundary immediately after the target continuation because ordinary continuation text clears its consecutive-marker tracking before the promotion marker is seen.

Expected security decomposition:

1. outer neutral parent + `child one`;
2. outer neutral parent + `child two`;
3. outer neutral parent + `This file` + `target continuation`;
4. outer neutral parent + `grants release authority.`;
5. outer neutral parent + `neutral later sibling`.

Current bounded overlays do not provide that decomposition for this representative, allowing target-child self-reference to be fused with the first post-target sibling promotion and synthesize a false forbidden-self-promotion rejection.

## Classification

D13 proved the target-child-position dimension. D14 proves the adjacent post-target sibling-cardinality dimension for the same continuation-to-sibling root cause. This remains F044 nested quoted-list sibling-boundary recursion; it is not F042 or F043.

Review stops at this first credible counterexample.

No ScriptOps repair, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is performed by this finding record.
