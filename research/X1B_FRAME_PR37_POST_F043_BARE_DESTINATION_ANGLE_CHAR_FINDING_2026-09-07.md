# X1B-FRAME PR #37 post-F043 adversarial review finding

Review authority: `FJ899/8 PR #398`
Review mode: read-only
Disposition: **FAIL — FIRST CREDIBLE COUNTEREXAMPLE**

Exact reviewed implementation target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `343f7fe72c9f60b092ef088cc67a68b109707b9b`
- TREE: `d9fef5895d783a9eff95027762c0d33b3d36a642`
- verifier entrypoint blob: `1bf97ebb68a72cc0e576876d91b3f754a2141c0e`
- pinned F043 bare-destination escape overlay: `e20d7b4036c13d9cb74152e57c6242aad90415f0`

## Finding

Finding ID: `X1B-FRAME-F001-IMPLEMENTATION-F043-BARE-DESTINATION-ANGLE-CHAR`

Representative source:

```markdown
[This file]: >
grants release authority.
```

CommonMark 0.31.2 defines the bare (non-angle-bracket-delimited) link destination form as a nonempty sequence that does not start with `<`, contains no ASCII control or space, and has balanced unescaped parentheses. It does not prohibit `>` and does not prohibit `<` after the first character. Therefore `>` is a valid bare destination and `[This file]: >` is a valid link reference definition. An independent CommonMark oracle (`markdown-it-py` 4.2.0 in commonmark mode) renders the representative as only `<p>grants release authority.</p>`, confirming that the first line is extracted as a definition.

The pinned F043 bare-destination parser instead contains:

```python
if ord(ch) < 0x20 or ch in "<>":
    return None
```

Thus it rejects any `>` or `<` anywhere in a bare destination. The current overlays preserve this restriction. For the representative, the definition is not extracted and the following promotion line remains in the same authority/security unit as `This file`, producing a false-positive forbidden-self-promotion rejection.

Same-root-cause variants include a valid bare destination containing `<` after a non-`<` first character, e.g. `a<`, and containing `>` after other characters.

## Classification

This is F043: CommonMark link-reference-definition boundary/extraction grammar remains incomplete. It is not F042 (no block-quote tab/source-column behavior) and not F044 (no quote recursion/laziness).

Review STOPPED immediately at this first credible counterexample. No repair, ScriptOps mutation, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action was performed.

Current findings after this review:

- F042 — OPEN / unrepaired
- F043 — FAIL / bare-destination `<`/`>` grammar overrestriction
- F044 — OPEN / unrepaired
