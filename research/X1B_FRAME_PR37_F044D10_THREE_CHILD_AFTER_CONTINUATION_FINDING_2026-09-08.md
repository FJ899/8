# X1B-FRAME PR #37 — F044-D10 three-child sibling set after child continuation finding

Date: 2026-09-08
Review mode: **read-only adjacent probe**
Disposition: **FAIL — credible bounded counterexample**

## Exact reviewed target

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `c0b4bde81a86064644d3a601e8a9599e4bfe10b7`
TREE: `7388e5a9745164d5db59246568ae7aee342cddf3`
Verifier entrypoint blob: `e28213dbe6a1b9808ea57ffa437ce34caa29e614`

## Representative

```markdown
> - neutral parent
>   - This file
>     ordinary continuation
>   - grants release authority.
>   - neutral child three
```

The three indented markers are sibling child items of one nested list. The continuation line belongs only to child one. Because the outer parent is neutral, child one's `This file` self-reference must not donate context to child two's promotion.

F044-D9 recognizes child one plus an ordinary continuation run followed by child two only when child two is the end of the bounded fragment (EOF/blank after it). Here child three follows immediately, so D9's `bounded_after` condition is false and the D9 normalizer leaves the fragment unchanged.

The earlier consecutive-child splitter can still separate child two from child three, but it does not create the missing boundary between child one (plus its continuation) and child two. The frozen quote accumulator can therefore fuse child one's self-reference with child two's promotion and synthesize a false-positive forbidden-self-promotion claim.

## Next bounded scope

The next repair is limited to one nonempty source-column-zero quoted outer item containing exactly three nonempty child items at the outer content indentation, where child one has a run of one or more ordinary owned continuation lines and child two/child three are marker-only child starts with ordinary item text. The fragment remains bounded by BOF/blank before and EOF/blank after.

Child one and its continuation run must remain one authority unit. Child two and child three must each be separate authority units. The outer parent context must be repeated into all three units. Four-or-more child items, continuation in later children, deeper nesting, block transitions and outer-sibling/list-owned quote families remain outside this finding.

No repair or consequential action was performed by this read-only probe.
