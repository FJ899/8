# X1B-FRAME PR #37 — F044-D9 child-continuation-run sibling finding

Date: 2026-09-08
Review mode: **read-only adjacent probe**
Disposition: **FAIL — credible bounded counterexample / parameterized run-length root cause**

## Exact reviewed target

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `8f15127099029ddd1b704353aa64e24db87ff588`
TREE: `55d380b4c1474e9c9b405f6ee55cf8b6b76f4b5a`
Verifier entrypoint blob: `43b72994b538a872ebaa36991a5dd127ad47592b`

## Representative

```markdown
> - neutral parent
>   - This file
>     continuation one
>     continuation two
>   - grants release authority.
```

The two indented text lines are ordinary continuation content owned by child item one. The final marker returns to the same child list-marker indentation and is a sibling child item. Because the outer parent is neutral, child one's self-reference must not donate context to child two's promotion.

F044-D8 handles exactly one child-continuation line and explicitly lists this two-continuation representative as untouched. The preceding D7 child-run normalizer covers only consecutive child markers and therefore also does not apply. The frozen quote accumulator can consequently retain both child siblings in one security unit and synthesize a false-positive `This file` + `grants release authority.` claim.

D8 (continuation count N=1) and this D9 probe (N=2) establish continuation-run length as the same parameterized root cause rather than a new Markdown block family.

## Next bounded scope

The next repair may generalize only this proven family: one nonempty source-column-zero quoted outer list item, one nonempty child item beginning exactly at the outer content indentation, a run of one or more ordinary continuation lines all owned by that child, and one nonempty sibling child returning to the same child marker indentation, with BOF/blank before and EOF/blank after.

Continuation lines must be interpreted relative to the child content indentation and must not be deep list markers or other block families. The repair must keep child one plus its continuation run together, keep child two separate, and preserve outer-parent inheritance into both child units.

Deeper nesting, blank/fence/block transitions inside the continuation run, more than two child items, outer-sibling transitions and list-owned outer quotes remain outside this finding.

No repair or consequential action was performed by this read-only probe.
