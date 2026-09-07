# X1B-FRAME PR #37 post-F043 quoted setext-destination finding

Review mode: autonomous read-only adjacent-case F043 probe.
Disposition: **FAIL — FIRST CREDIBLE COUNTEREXAMPLE**

Exact reviewed implementation target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `2a06399264dbeefadd32be5196e98c8d37937933`
- TREE: `a56b44a5f398595d57539fd573d0bba153f07ae0`
- verifier entrypoint blob: `3534b2551e1c9d82d1665464529d42e615dfc94d`

## Finding

Finding ID: `X1B-FRAME-F001-IMPLEMENTATION-F043-QUOTED-SETEXT-LIKE-DESTINATION`

Representative source:

```markdown
> [This file]:
===
> grants release authority.
```

CommonMark 0.31.2 permits one line ending between the reference-definition colon and destination, and `===` is a legal bare destination. In a block quote, the destination line may be a lazy paragraph continuation with the repeated `>` omitted. An independent CommonMark oracle (`markdown-it-py` commonmark mode) consumes the first two physical lines as the link-reference definition and renders only the later quoted promotion paragraph.

The current quoted multiline collector classifies each continuation with `multiline._payload_interrupts_paragraph(...)` before adding it to the definition candidate. That helper treats setext underline syntax as a paragraph interrupter. For the incomplete definition line `[This file]:`, however, the following `===` is not a setext underline in the resulting CommonMark parse: it is the valid destination completing the definition. The collector therefore stops too early, misses definition extraction, and the frozen block-quote lazy logic can fuse `[This file]:`, `===`, and the later quoted `grants release authority.` into one security unit, producing a false-positive forbidden-self-promotion rejection.

This is a bounded F043 reference-definition boundary/precedence defect. F042 and F044 remain OPEN / unrepaired.

Review STOPPED at this first credible counterexample. No ScriptOps repair, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action was performed by this finding record.
