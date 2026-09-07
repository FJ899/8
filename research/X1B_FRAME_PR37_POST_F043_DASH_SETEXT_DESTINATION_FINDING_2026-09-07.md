# X1B-FRAME PR #37 post-F043 dash-setext destination finding

Review mode: autonomous read-only adjacent-case F043 probe.
Disposition: **FAIL — FIRST CREDIBLE COUNTEREXAMPLE**

Exact reviewed implementation target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `af4ac1af91a4d0e6790b60021a72b58575f58dbc`
- TREE: `e75da49daba0ada67a5783eff5607cdc61e5291a`
- verifier entrypoint blob: `1601a04573f3151a60ef861f4cb0757907173805`

## Finding

Finding ID: `X1B-FRAME-F001-IMPLEMENTATION-F043-QUOTED-DASH-SETEXT-DESTINATION`

Representative source:

```markdown
> [This file]:
--
> grants release authority.
```

CommonMark allows one line ending before a link-reference-definition destination, and `--` is a legal bare destination. It is setext-underline-shaped, but unlike a single `-` it is not an empty bullet-list marker, and unlike `---` or longer runs it is not a thematic break. An independent CommonMark oracle consumes the first two physical lines as the definition and renders only the later quoted promotion paragraph.

The current quoted collector treats setext underline syntax as an interruption and its bounded exception recognizes only the equals (`=`) family. Therefore `--` is rejected before the existing link-reference-definition grammar can accept it, leaving the block-quote lazy unitizer able to fuse self-reference with the later promotion paragraph and produce a false-positive forbidden-self-promotion rejection.

This is F043 reference-definition/block-precedence handling. F042 and F044 remain OPEN / unrepaired.

Review STOPPED at this first credible counterexample. No ScriptOps repair, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action was performed by this finding record.
