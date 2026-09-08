# X1B-FRAME PR #37 — F044-D11 child-cardinality after continuation finding

Date: 2026-09-08
Review mode: **read-only adjacent probe**
Disposition: **FAIL — credible bounded counterexample / parameterized child-cardinality root cause**

## Exact reviewed target

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `082e4fdef8beb727e6a7da17e5d9f74326b0f9fd`
TREE: `7a814cba1df571a3a3a795e03411d317905141f3`
Verifier entrypoint blob: `db7391da5ec577e622b912ddee5800371b959427`

## Representative

```markdown
> - neutral parent
>   - This file
>     ordinary continuation
>   - grants release authority.
>   - neutral child three
>   - neutral child four
```

All four indented markers are sibling child items of one nested list. The continuation line belongs only to child one. With a neutral outer parent, child one's self-reference must not donate context to child two's promotion.

F044-D10 handles exactly three child items: after locating child two it requires one immediate child three and then requires EOF/blank after child three. In this representative child four follows, so D10's bounded-after condition is false and the D10 normalizer leaves the fragment unchanged.

The earlier equal-indent sibling splitter may separate later consecutive child markers, but it still does not create the missing boundary between child one plus its continuation run and child two. The frozen quote accumulator can therefore fuse child one's `This file` with child two's `grants release authority.` and synthesize a false-positive forbidden-self-promotion claim.

D10 (total child count N=3) and this D11 probe (N=4) establish child cardinality after a child-one continuation run as one parameterized root cause.

## Next bounded scope

The next repair may generalize only this proven family: one nonempty source-column-zero quoted outer item, one nonempty child one at the outer content indentation, a run of one or more ordinary continuation lines owned by child one, then a bounded run of at least two additional consecutive nonempty child sibling markers at the same child marker indentation, with BOF/blank before and EOF/blank after.

Child one plus its continuation run remains one authority unit. Every later child is a separate authority unit. The outer parent context is repeated into every child unit.

Continuation in later children, deeper nesting, blank/fence/block transitions, outer-sibling transitions and list-owned outer quotes remain outside this finding.

No repair or consequential action was performed by this read-only probe.
