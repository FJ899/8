# X1B-FRAME PR #37 post-F043 list setext finding

Review mode: autonomous read-only adjacent-case F043 probe.
Disposition: **FAIL — FIRST CREDIBLE COUNTEREXAMPLE**

Exact reviewed implementation target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `4e533f4dffe08142c614eff0292744d68e57e52e`
- TREE: `8ab5a76cf6930897fc7edd3fb985c58cf5a9486a`
- verifier entrypoint blob: `dc3ffcdf59fb23dffa20cffbdafe18bdef7ce659`

## Finding

Finding ID: `X1B-FRAME-F001-IMPLEMENTATION-F043-LIST-SETEXT-INSIDE-INCOMPLETE-DEFINITION`

Representative source:

```markdown
- [This file]:
  ===
  grants release authority.
```

CommonMark permits one line ending before a reference-definition destination, and `===` is a legal bare destination. Inside the list item, an independent CommonMark oracle extracts the first two physical lines as the definition and renders only the later `grants release authority.` item paragraph.

The current list collector correctly preserves item-relative indentation after the previous repair, but still applies `_payload_interrupts_paragraph` before admitting setext-looking content. Relative `===` is therefore treated as a setext interrupter before the existing definition grammar can recognize it as a destination.

The frozen core keeps the list marker line, setext-looking line and subsequent nonblank item continuation in the same list-frame security unit. The missed definition boundary therefore falsely fuses `This file` with the later promotion paragraph and raises forbidden self-promotion.

The same collector edge also affects setext-looking content inside an incomplete multiline reference-definition title. This remains bounded F043 list-owned link-reference-definition collection; F042 and F044 remain OPEN / unrepaired.

Review STOPPED at this first credible counterexample. No ScriptOps repair or consequential action was performed by this finding record.
