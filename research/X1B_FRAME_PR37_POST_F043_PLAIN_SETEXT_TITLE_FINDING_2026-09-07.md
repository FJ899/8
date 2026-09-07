# X1B-FRAME PR #37 post-F043 plain multiline setext-title finding

Review mode: autonomous read-only adjacent-case F043 probe.
Disposition: **FAIL — FIRST CREDIBLE COUNTEREXAMPLE**

Exact reviewed implementation target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `33da6f66b25a1be3d469d153cc732c5244706589`
- TREE: `18fdff7b309ffbcfc9dd19daf94793be09f7f690`
- verifier entrypoint blob: `d40169c63c95519e5e14805ffbd6957397eb47bf`

## Finding

Finding ID: `X1B-FRAME-F001-IMPLEMENTATION-F043-PLAIN-SETEXT-INSIDE-MULTILINE-TITLE`

Representative source:

```markdown
[This file]: /url "
===
grants release authority
"
```

CommonMark 0.31.2 permits link titles to extend over multiple nonblank lines. An independent CommonMark oracle consumes all four physical lines above as a single link reference definition and renders no visible content. The authority-bearing words inside that definition metadata therefore remain security-relevant as one definition unit.

The current plain multiline collector preserves physical indentation after the previous repair, but still calls `_payload_interrupts_paragraph(raw_line)` before adding a setext-looking continuation to the candidate. Unindented `===` is therefore treated as a setext interruption and collection stops before the later closing quote.

The frozen core then treats `===` as a setext underline for the preceding open paragraph, flushing the first line `[This file]: /url "` as its own authority unit. The later `grants release authority` text is processed separately. This can split self-reference from promotion text even though CommonMark places both inside one link-reference-definition metadata unit, creating a false negative in the Layer-B self-promotion check.

This remains bounded F043 link-reference-definition extraction/precedence. F042 and F044 remain OPEN / unrepaired.

Review STOPPED at this first credible counterexample. No ScriptOps repair, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action was performed by this finding record.
