# X1B-FRAME PR #37 — F044-D2 nonconsecutive quoted sibling-list finding

Date: 2026-09-08
Review mode: **read-only adjacent probe**
Disposition: **FAIL — credible bounded counterexample**

## Exact reviewed target

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `062e32232d608ee6be7c2169eddf00d41f7ca69f`
TREE: `f7a390ebdf3e39f6279d346f4a5a24b28dbe050f`
Verifier entrypoint blob: `8149edafc03ceea9d70c133b3a6d5303dcdb304e`
Pinned F044-D overlay blob: `4052f012fef7791e23f6ced77014f2fd6802b4a5`

## Representative

```markdown
> - This file
>   ordinary continuation
> - grants release authority.
```

The first and third quoted lines are sibling bullet-list markers at the same inner list-marker indentation. The middle line is ordinary continuation content owned by the first item. CommonMark list-item structure therefore separates the final marker into a distinct sibling item.

The bounded F044-D preprocessor only remembers `previous_list_indent` from the immediately preceding physical quote line. For the middle continuation line, `_markdown_list_item_layout(...)` returns `None`, so `previous_list_indent` becomes `None`. The following same-level sibling marker therefore does not trigger the inserted authority-unit boundary.

The frozen quote accumulator then receives all three explicit quote lines without an inner sibling boundary and may synthesize one security unit containing both `This file` and `grants release authority.`, producing a false-positive forbidden-self-promotion rejection.

## Classification and scope

Finding ID: `F044-D2 — nonconsecutive quoted sibling list after ordinary same-item continuation`.

This is adjacent to the repaired F044-D consecutive-sibling family. It does not reopen F042/F043 or F044-A/B/C/E. No repair, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action was performed by this read-only probe.
