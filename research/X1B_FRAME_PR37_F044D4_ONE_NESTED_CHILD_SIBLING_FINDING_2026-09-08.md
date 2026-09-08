# X1B-FRAME PR #37 — F044-D4 one nested-child outer-sibling finding

Date: 2026-09-08
Review mode: **read-only adjacent probe**
Disposition: **FAIL — credible bounded counterexample**

## Exact reviewed target

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `07648433bd08a2aa2cbb48dc090d84e23993a914`
TREE: `dabcd6a8af5650a8282b22ae55bb07ea47e2f228`
Verifier entrypoint blob: `943e5f741f51f2e89aa2ac0264f511f31ea842b3`

## Representative

```markdown
> - This file
>   - child detail
> - grants release authority.
```

The middle marker is a nested child list owned by the first outer item. The final marker returns to the first marker's inner list indentation and therefore starts a new outer sibling item.

The F044-D3 tracker deliberately terminates on a different-level list marker. The earlier consecutive-sibling preprocessor likewise sees marker indents `0 -> 2 -> 0`, never two consecutive equal levels. No inner sibling authority boundary is therefore inserted before the final outer sibling, and the frozen quote accumulator may fuse the first outer item's self-reference with the final sibling's promotion.

## Classification

Finding ID: `F044-D4 — outer quoted sibling after exactly one nested child marker`.

The next bounded repair is limited to exactly one nested nonempty child marker between one outer item and a nonempty sibling returning to the same outer marker indentation. Multiple child items, child continuation, deeper nesting, blank/fence transitions and list-owned outer quote recursion remain outside this finding.

No repair or consequential action was performed by this read-only probe.
