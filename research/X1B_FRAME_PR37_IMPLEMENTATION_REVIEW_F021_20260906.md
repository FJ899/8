# X1B-FRAME PR #37 IMPLEMENTATION REVIEW — F021

Review authority: `FJ899/8 PR #255`.

Exact reviewed candidate:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `78eb25f7b07270919658fe0eeb839bcaabcfed52`
- TREE: `d21afc0caef5664e86065301b17e4d18be4f57bf`
- verifier blob: `2bec91059ce98595f14226d9e9898ff94336864c`

## Finding

`X1B-FRAME-F001-IMPLEMENTATION-F021`

F020 does not correctly recognize nested sibling Markdown list items once their raw marker indentation exceeds three spaces. `_markdown_list_item_layout()` accepts only ` {0,3}` before a list marker. This works for the first nested level used by the F020 regressions, but a valid deeper nested list normally places the next marker at four or more raw leading spaces.

Credible benign counterexample:

```text
- Parent:
  - Child context:
    - This file contains background notes.

    - Release authority belongs to a separate Human gate.
```

The two four-space-indented third-level markers are valid sibling list items. The production parser does not recognize either as `layout`; both are treated as ordinary continuation lines of the active second-level frame. After the blank line, the second sibling is therefore appended to the same active authority path rather than starting a fresh sibling unit.

The resulting synthetic unit contains `This file` from one third-level sibling and `authority` from the other. The F016 whole-unit fallback then sees self-reference plus a promotion term and rejects this benign sibling-list structure as forbidden self-promotion.

This is the same class of incorrect sibling conflation that F020 was meant to close, now exposed at deeper valid Markdown nesting depth. Current F020 tests cover only one nested level with marker indentation of two or three spaces and therefore do not exercise this boundary.

## Disposition

First credible counterexample occurred at F020. Review STOPPED immediately under PR #255.

F019 through F006 and Q5-Q15 were **not** re-reviewed after this finding.

No repair, merge, ScriptOps `main` movement, PR #35 integration, deployment/release/tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority is granted by this finding.
