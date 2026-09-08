# X1B-FRAME PR #37 — F044-D13 third-child-continuation sibling finding

Date: 2026-09-08
Review mode: bounded read-only adjacent probe
Disposition: **FAIL — FIRST CREDIBLE COUNTEREXAMPLE**

## Exact reviewed implementation binding

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `f92c5ecc3b562050e91b6be662403b14fb0e1325`
TREE: `8c90cbb3ce46af058c49fbe3bdfe59d06a856c29`
Verifier entrypoint blob: `6a71863f5488e287780ba536079ba6c19fa4e302`
Frozen repaired F044-D12 predecessor: `9562a7bf8af9db20b45ea7f61907c41c4c7ad0d4` retained under the D12 overlay chain

## Finding

Finding ID: `X1B-FRAME-F044-D13-THIRD-CHILD-CONTINUATION`

Representative source:

```markdown
> - neutral parent
>   - child one
>   - child two
>   - This file
>     child three continuation
>   - grants release authority.
```

An independent CommonMark parse yields one quoted outer list item containing four distinct nested child items: `child one`; `child two`; `This file` plus its ordinary continuation; and `grants release authority.`. Therefore the self-reference in child three and the promotion in child four are distinct sibling authority units.

The D12 repair covers only the same continuation-to-sibling boundary when the continuation-bearing item is child two. D11 and earlier continuation/cardinality overlays likewise do not cover a later continuation-bearing child at this position. The lower consecutive quoted sibling splitter inserts boundaries between consecutive same-indent markers, but its state is cleared by an ordinary continuation line. Consequently the marker after `child three continuation` receives no sibling boundary and the D8-style cross-child false-positive mechanism remains reachable at child position three.

D8 established continuation-to-sibling separation at child position one; D12 established it at child position two; this D13 probe establishes the same root cause at child position three. The newly demonstrated parameter is the position of the continuation-bearing child.

Expected security decomposition:

1. outer neutral parent + `child one`;
2. outer neutral parent + `child two`;
3. outer neutral parent + `This file` + `child three continuation`;
4. outer neutral parent + `grants release authority.`.

Current bounded overlays do not provide that decomposition for the representative, so child-three self-reference can be fused with child-four promotion and synthesize a false forbidden-self-promotion rejection.

## Scope classification

This remains F044 nested quoted-list sibling-boundary recursion. It is not F042 or F043. Review stops at this first credible counterexample.

No ScriptOps repair, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is performed by this finding record.
