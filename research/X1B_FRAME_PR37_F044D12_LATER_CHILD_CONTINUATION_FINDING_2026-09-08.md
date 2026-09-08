# X1B-FRAME PR #37 — F044-D12 later-child-continuation sibling finding

Date: 2026-09-08
Review mode: bounded read-only adjacent probe
Disposition: **FAIL — FIRST CREDIBLE COUNTEREXAMPLE**

## Exact reviewed implementation binding

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `65c3168d0f45bae1cf4ea80e74c129fa9f9f07bc`
TREE: `a3ebac3570f1166cc9862d5cb137ac68bd301fd2`
Verifier entrypoint blob: `9562a7bf8af9db20b45ea7f61907c41c4c7ad0d4`
Frozen repaired F044-D10 entrypoint: `db7391da5ec577e622b912ddee5800371b959427`

## Finding

Finding ID: `X1B-FRAME-F044-D12-LATER-CHILD-CONTINUATION`

Representative source:

```markdown
> - neutral parent
>   - child one
>   - This file
>     child two continuation
>   - grants release authority.
```

CommonMark parses the quoted outer item as a nested list whose three child items are distinct: `child one`; `This file` plus its ordinary continuation; and `grants release authority.`. Therefore the child-local self-reference and the later sibling promotion are not one authority unit.

The current D11 generalizer explicitly leaves continuation in later children outside its repair. D10, D9 and D8 likewise only repair continuation owned by the first child in their bounded fragment. D7 repairs only consecutive child markers without child continuation. The lower F044-D sibling splitter inserts a boundary between consecutive same-indent child markers, but an ordinary continuation clears its previous-list-indent state; therefore the later sibling after `child two continuation` receives no boundary.

This reproduces the D8 continuation-to-sibling root cause at a later child position. The new parameter is child position, not continuation-run length or child cardinality.

Expected security decomposition:

1. outer neutral parent + `child one`;
2. outer neutral parent + `This file` + `child two continuation`;
3. outer neutral parent + `grants release authority.`.

Current bounded overlays do not produce that decomposition for the representative, so self-reference from child two can be fused with the promotion in child three and synthesize a false forbidden-self-promotion rejection.

## Scope classification

This is F044 nested quoted-list recursion/sibling-boundary handling. It is not F042 or F043. The adjacent probe stops at this first credible counterexample.

No ScriptOps repair, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is performed by this finding record.
