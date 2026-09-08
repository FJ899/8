# X1B-FRAME PR #37 — F044-D7 child-sibling run-length finding

Date: 2026-09-08
Review mode: **read-only adjacent probe**
Disposition: **FAIL — credible bounded counterexample / parameterized root cause**

## Exact reviewed target

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `3807870d8005879fda43c06775c3721b8a4158c5`
TREE: `7210c48047cd2680e5818dbfdc21d3414e2fc5d6`
Verifier entrypoint blob: `9353ae5d9d52536a7bce0c9ac8e1b5dc657cadc4`

## Representative

```markdown
> - This file
>   - child one
>   - child two
>   - child three
>   - grants release authority.
```

All four indented markers are sibling child items of the same nested list owned by the outer `This file` item. The established F020 security model therefore requires every child item to inherit the outer parent context.

The F044-D6 repair deliberately handles exactly three child siblings and explicitly lists the four-child representative above as untouched. F044-D5 likewise handles exactly two children. The earlier F044-D equal-indent splitter can therefore continue separating later child items without repeating their outer parent security context.

D5 (N=2), D6 (N=3) and this D7 probe (N=4) establish that the defect is parameterized by child-sibling run length rather than a distinct Markdown structure at each N.

## Next bounded scope

The next repair may generalize only this proven family: one nonempty source-column-zero quoted outer list item, followed by a bounded run of two or more consecutive nonempty child list markers all beginning at the outer item's content indentation, with BOF/blank before and EOF/blank after. Each child remains a separate authority unit and receives the same outer parent context.

Child continuation lines, different-level/deeper nesting, outer-sibling transitions, blank/fence/block transitions and list-owned outer quotes remain outside this finding.

No repair, merge, main movement, deployment, release, tag, canonical effect, status promotion, X1B reopen or V1 action was performed by this read-only probe.
