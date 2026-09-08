# X1B-FRAME PR #37 — F044-D6 three-child parent-context finding

Date: 2026-09-08
Review mode: **read-only adjacent probe**
Disposition: **FAIL — credible bounded counterexample**

## Exact reviewed target

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `8940ff9265b2443fed51dba72293d7beaa7d00ec`
TREE: `234736bd893b7876f1753afb3955f8ab3fd59e84`
Verifier entrypoint blob: `17cfdd6aec80aace8ed755040f025796c3e18488`
Pinned F044-D5 overlay blob: `fd8290e38723f9b69ba06a60adec37e1797f25f4`
Pinned F044-D overlay blob: `4052f012fef7791e23f6ced77014f2fd6802b4a5`

## Representative

```markdown
> - This file
>   - child one
>   - child two
>   - grants release authority.
```

All three indented markers are sibling child items of the same nested list owned by the outer `This file` item. Under the established F020 security model, the outer parent context must be inherited by every descendant child item, including the third child containing `grants release authority.`.

The repaired F044-D5 normalizer is deliberately limited to exactly two child siblings in a three-line fragment and explicitly lists the representative above as untouched. The current F044-D4 retry also does not match this shape because it handles exactly one child followed by an outer sibling.

The earlier F044-D preprocessor subsequently inserts blank boundaries between consecutive equal-indent child markers. With the D5 normalizer inactive for this larger run, those boundaries separate later child siblings from the outer parent security context. The third child can therefore lose `This file` and evade the forbidden-self-promotion rejection.

## Classification and next bounded scope

Finding ID: `F044-D6 — third quoted child sibling loses inherited outer parent context`.

The next repair is limited to one nonempty outer quoted list item with exactly three consecutive nonempty child sibling markers at the outer content indentation, bounded by BOF/blank before and EOF/blank after. It must keep all child siblings separate while repeating the outer parent context into the second and third child units. Four-or-more child siblings, child continuation, deeper nesting, outer sibling transitions and list-owned outer quotes remain outside this finding.

No repair, merge, main movement, deployment, release, tag, canonical effect, status promotion, X1B reopen or V1 action was performed by this read-only probe.
