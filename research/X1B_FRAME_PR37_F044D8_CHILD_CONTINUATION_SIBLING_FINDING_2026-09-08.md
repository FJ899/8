# X1B-FRAME PR #37 — F044-D8 child-continuation sibling-separation finding

Date: 2026-09-08
Review mode: **read-only adjacent probe**
Disposition: **FAIL — credible bounded counterexample**

## Exact reviewed target

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `646cffbfe1daaeeaf61e38d8867c88d3bf3d99f3`
TREE: `6e48072fcbd2660245a8adb77bb33e5c12c6ca7a`
Verifier entrypoint blob: `fcf1920eae399bb0bc09b103e105d23116c2a5d0`
Pinned F044-D3 continuation-run overlay blob: `943e5f741f51f2e89aa2ac0264f511f31ea842b3`

## Representative

```markdown
> - neutral parent
>   - This file
>     ordinary continuation
>   - grants release authority.
```

The two indented list markers are sibling child items of one nested list under a neutral outer item. The middle text line is ordinary continuation content owned by the first child item. Because the outer parent is neutral, the self-reference in child one must not donate context to the promotion in child two.

The F044-D7 child-run normalizer deliberately covers only consecutive child marker lines and stops when an ordinary continuation line occurs. The older F044-D3 tracker also does not cover this nested shape: when it sees the first child marker at a different level from the outer marker it clears the active tracker; the following continuation line cannot restore child ownership tracking before the second child sibling marker. The original consecutive-sibling splitter likewise cannot see through the continuation line.

The frozen quote accumulator can therefore retain both child items in one security unit, synthesizing a false-positive `This file` + `grants release authority.` claim across sibling items.

## Next bounded scope

The next repair is limited to one nonempty source-column-zero quoted outer list item, one nonempty child item beginning exactly at the outer content indentation, exactly one ordinary continuation line owned by that child, and one nonempty sibling child marker returning to the same child marker indentation. The fragment must be bounded by BOF/blank before and EOF/blank after.

The repair must preserve outer-parent inheritance into both child units while preventing one child from donating self-reference to its sibling. Two-or-more child continuation lines, deeper nesting, blank/fence transitions, outer-sibling transitions and list-owned outer quotes remain outside this finding.

No repair or consequential action was performed by this read-only probe.
