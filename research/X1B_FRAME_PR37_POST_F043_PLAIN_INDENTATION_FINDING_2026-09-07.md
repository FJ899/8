# X1B-FRAME PR #37 post-F043 plain multiline indentation finding

Review mode: autonomous read-only adjacent-case F043 probe.
Disposition: **FAIL — FIRST CREDIBLE COUNTEREXAMPLE**

Exact reviewed implementation target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `adbd167ce47d21d1d6f4439c4f7fe2fc361f8006`
- TREE: `71c94de595c880bcba8f2e76de2a41e40e492a9b`
- verifier entrypoint blob: `8f8f5e87912c6af0e63b38be1d574265c1962257`

## Finding

Finding ID: `X1B-FRAME-F001-IMPLEMENTATION-F043-PLAIN-MULTILINE-INDENTATION-ERASURE`

Representative source:

```markdown
[This file]:
    #
grants release authority.
```

CommonMark permits the destination on the next physical line. Four-space-indented `#` cannot start an ATX heading and indented code cannot interrupt the already-open paragraph/reference-definition candidate. An independent CommonMark oracle consumes the first two lines as the definition and renders only the later promotion paragraph.

The frozen plain multiline collector strips leading whitespace before `_payload_interrupts_paragraph`, so physical `    #` becomes synthetic `#` and is misclassified as an ATX heading. Definition extraction is missed, and the core paragraph unitizer can retain self-reference with the following promotion text, creating a false-positive forbidden-self-promotion rejection.

This is F043 multiline reference-definition collection, not F042 or F044.

Review STOPPED at this first credible counterexample. No repair or consequential action was performed by this finding record.
