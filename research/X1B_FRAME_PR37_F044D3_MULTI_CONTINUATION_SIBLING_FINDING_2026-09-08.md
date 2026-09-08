# X1B-FRAME PR #37 — F044-D3 multi-continuation quoted sibling-list finding

Date: 2026-09-08
Review mode: **read-only adjacent probe**
Disposition: **FAIL — credible bounded counterexample**

## Exact reviewed target

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `609ff08b0411e1221b7fdcde4b37227e1c4978d9`
TREE: `c83dcc69f94222707b2c6411e9da15af66c138d7`
Verifier entrypoint blob: `05856621e882f5559004c7e33f4804e3ba238be8`

## Representative

```markdown
> - This file
>   continuation one
>   continuation two
> - grants release authority.
```

The first three inner lines belong to one list item: the latter two are ordinary continuation lines indented to that item's content column. The final marker is a same-inner-level sibling list item.

The F044-D2 repair handles exactly one continuation line by examining a fixed three-line window. With two continuation lines, no examined window has the required `item -> continuation -> sibling` shape, so no authority boundary is inserted before the final sibling marker. The frozen quote accumulator can therefore still fuse the first item's self-reference with the sibling item's promotion.

## Classification

Finding ID: `F044-D3 — same-level quoted sibling after an ordinary continuation run of length > 1`.

This demonstrates that the D2 root cause is continuation-run length, not a new Markdown block family. The next bounded repair may generalize only this ordinary owned continuation run to length >= 1. Nested list children, blank-line transitions, fenced blocks and list-owned outer quotes remain outside this finding.

No repair or consequential action was performed by this read-only probe.
