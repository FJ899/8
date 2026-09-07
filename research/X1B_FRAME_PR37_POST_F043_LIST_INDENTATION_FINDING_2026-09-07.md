# X1B-FRAME PR #37 post-F043 list multiline indentation finding

Review mode: autonomous read-only adjacent-case F043 probe.
Disposition: **FAIL — FIRST CREDIBLE COUNTEREXAMPLE**

Exact reviewed implementation target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `1ed1465cf75bae63c731715cd9162262535afc7b`
- TREE: `0b996d0a0e8bebcfbbf9a5af04d0fe96e9b04ad8`
- verifier entrypoint blob: `7ccdfe7500ffb342396b0883918a9b4cf403d554`

## Finding

Finding ID: `X1B-FRAME-F001-IMPLEMENTATION-F043-LIST-MULTILINE-INDENTATION-ERASURE`

Representative source:

```markdown
- [This file]:
      #
  grants release authority.
```

For a `- ` list item the content indent is two columns. The second physical line therefore has four columns of indentation relative to item content. CommonMark permits a reference-definition destination on the next physical line, and indented code cannot interrupt an already-open paragraph/reference-definition candidate. An independent CommonMark oracle consumes the first two physical lines as the definition and renders only `grants release authority.` inside the list item.

The current F043 list-lazy collector first removes the item content indent and then unconditionally strips all remaining leading spaces before structural-interrupter classification. Thus relative `    #` becomes synthetic `#`, which `_payload_interrupts_paragraph` misclassifies as an ATX heading. The definition is not folded.

The frozen core then keeps non-structural list continuation text in the active list frame. The first line, stripped `#`, and later promotion text can therefore remain in one list security unit. Self-reference from the definition candidate is falsely fused with the separate promotion paragraph, creating a forbidden-self-promotion false positive.

This is bounded F043 multiline link-reference-definition collection inside a list. F042 and F044 remain OPEN / unrepaired.

Review STOPPED at this first credible counterexample. No ScriptOps repair or consequential action was performed by this finding record.
