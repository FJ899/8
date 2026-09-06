# X1B-FRAME-F001-IMPLEMENTATION-F038 — CommonMark HTML-block boundary collapse

Date: 2026-09-06

Disposition: `FAIL — FIRST CREDIBLE COUNTEREXAMPLE`

Review authority: `FJ899/8 PR #342`

Exact reviewed candidate:

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `5d07e181c1a9d43f4bfca000962790b087b6fe15`
- TREE: `bdbc73b06bb29c5b334cb2cd4bca0d49b68df63b`
- verifier blob: `b29df53ab96596ac075118943b364d9b47eda6cd`

## Review order

The independent review first re-attacked F037 and confirmed that the repaired verifier now recognizes equals-family setext underlines, preserves quoted/list-owned setext semantics, and retains F036 through F029 plus earlier frozen regressions.

The next frozen CommonMark leaf-block frontier was HTML blocks.

## Counterexample

Representative source:

```markdown
This file
<div>
grants release authority.
</div>
```

CommonMark 0.31.2 §4.6 defines `<div>` as a type-6 HTML-block start. HTML blocks of types 1–6 can interrupt a paragraph without a preceding blank line. Type-6 content continues until the following blank line or end of document.

Therefore the CommonMark block structure is:

1. paragraph: `This file`
2. HTML block containing `<div>`, `grants release authority.`, and `</div>`

The HTML block must not inherit the self-reference from the preceding paragraph.

## Current verifier failure mechanism

The exact reviewed verifier has explicit block handling for:

- fenced code;
- block quotes;
- ATX headings;
- equals-family setext underlines;
- thematic breaks;
- list items.

It has no HTML-block opening/state/end recognition on this parsing path.

For the representative source:

1. `This file` enters the ordinary paragraph buffer.
2. `<div>` matches no implemented block-boundary branch and falls through to the same paragraph buffer.
3. `grants release authority.` is appended to that same buffer.
4. `</div>` is also appended.
5. The verifier therefore evaluates one folded authority unit equivalent to `This file <div> grants release authority. </div>`.
6. Normalization still exposes `THIS FILE` and `GRANTS ... AUTHORITY`, so the Layer-B self-promotion detector rejects it.

That rejection is a false positive caused by collapsing a real CommonMark HTML-block boundary.

## Security significance

The verifier uses Markdown block structure as a security boundary for self-reference/predicate donation. Missing a paragraph-interrupting HTML block lets text outside the HTML block donate a self-reference into literal/raw HTML-block content.

This is structurally the same class of boundary-integrity failure previously found for ATX headings, block quotes, fenced code, and setext headings, but it is a distinct CommonMark block type and is not covered by the current parser.

## Scope note

This finding does not require or authorize a full HTML parser. It only establishes that the current verifier is not yet sound for CommonMark HTML-block boundaries relevant to authority-unit folding.

No repair was performed.

No ScriptOps mutation, merge of PR #37 or PR #35, default-branch movement, deploy, release, tag, canonical effect, active-product status promotion, X1B reopen, V1 action, or unrelated cleanup is authorized.

Mandatory next state: `STOP BEFORE F038 REPAIR`.
