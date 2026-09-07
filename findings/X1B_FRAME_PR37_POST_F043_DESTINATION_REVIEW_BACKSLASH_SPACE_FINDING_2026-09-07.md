# X1B-FRAME PR #37 post-F043 destination-newline adversarial review finding — 2026-09-07

Authority: `FJ899/8 PR #386`.

Reviewed exact candidate:
- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `9ef034b8cb87500d2c160c88ab04c36f39ac417b`
- TREE: `25fcee396a9ee81a25837863e2dfc3f124506e5f`
- verifier entrypoint blob: `277eb91bbcf46dfb766e39ed23962b5179450c87`
- pinned F043 list-lazy: `040365f5825c386b1e74405ca51c63edd2ca55ac`
- pinned F043 multiline: `c2b5a356e744be802d204ab8eaea901e76aa1219`
- pinned F043 single-line: `61bf107ad59da33a6576032d341b41c538d0453a`
- pinned F041 core: `be645c1a3ee49a04d700a3ef7fde86a92e413a14`

Disposition: `FAIL — FIRST CREDIBLE COUNTEREXAMPLE`.

Representative:

```markdown
[This file]: foo\ bar
grants release authority.
```

CommonMark 0.31.2 rules:
- backslash escapes apply to ASCII punctuation; a backslash before a space remains a literal backslash plus a space;
- a bare link destination may not contain a space character.

Therefore the first line is not a valid link reference definition. With no other block boundary, the two physical lines form one paragraph and the self-reference must remain in the same authority unit as `grants release authority.`.

Current frozen F043 single-line parser instead treats backslash as escaping any following character. In the bare-destination loop, once `\` is seen it sets `escaped=True`; the next character is then consumed without applying the space/control-character rejection. Thus `foo\ bar` is accepted as a destination. The top-level F043 extraction path then emits the first line as a definition unit and parses `grants release authority.` separately, creating an F043 false negative.

This is the same F043 grammar-recognition/extraction root family, not F042 or F044.

Review stopped immediately at this first credible counterexample. No repair was performed. F042 and F044 remain OPEN / unrepaired. No merge, ScriptOps `main` movement, deploy, release, tag, canonical effect, status promotion, X1B reopen or V1 action was performed or authorized.
