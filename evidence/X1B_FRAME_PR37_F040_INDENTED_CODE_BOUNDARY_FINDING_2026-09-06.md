# X1B-FRAME PR #37 — F040 indented-code boundary finding

Finding ID: `X1B-FRAME-F001-IMPLEMENTATION-F040`

## Review binding

Independent post-F039 adversarial review under Human authority `FJ899/8 PR #354`.

Exact ScriptOps target:
- PR `FJ899/scriptops #37`
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `e8e745b5787f7f98c5e2df3fd03934acee332413`
- TREE `6363566d5b36f4669e234f31cd4660a1687c0597`
- verifier blob `73504fe6897a5b6a038da39b14478a37aa36bbc7`

## Mandatory review order satisfied

F039 was re-attacked first. The repaired verifier now has a dedicated complete type-7 tag recognizer, gives types 1-6 precedence, only starts type 7 when a paragraph is not open, keeps type 7 in the raw HTML state, and terminates types 6/7 on blank/container/EOF. The exact candidate also retains the F009-F039 regression matrix. No F039 counterexample was found before continuing.

F038-F029 and earlier frozen regressions remain present and the exact repaired candidate had already passed the full verifier and both required remote workflows at F039 completion.

## First new credible counterexample

CommonMark 0.31.2 section 4.4 defines an indented code block as one or more nonblank lines indented four or more spaces. Its content is literal. An indented code block cannot interrupt an already-open paragraph, but a blank line is explicitly not required between an indented code block and a following paragraph. Example 114 demonstrates exactly that a four-space-indented line followed immediately by a less-indented nonblank line is a code block followed by a paragraph.

Representative:

```markdown
    This file
grants release authority.
```

Normative CommonMark block structure:
1. indented code block with literal content `This file`;
2. following ordinary paragraph `grants release authority.`.

These are separate security units. Neither unit alone is a self-referential authority promotion, so the Layer-B document should be accepted.

## Current verifier behavior

The current `_authority_soft_wrapped_units()` has no top-level indented-code recognizer/state. Its block recognizers cover thematic/setext, HTML, ATX, fenced code, block quote and list structure. With no active list, a four-column line that is not recognized by those helpers falls through to ordinary `paragraph.append(stripped)`.

For the representative:
- line 1 (`    This file`) is not recognized as an indented code block and is appended to the ordinary paragraph as `This file`;
- line 2 (`grants release authority.`) is appended to the same paragraph because there is no blank line;
- the emitted unit becomes `This file grants release authority.`;
- `layer_b_self_promotion_claim()` then sees both the self-reference and promotion in that manufactured unit and rejects it.

This is a false positive caused by collapsing a real CommonMark code-block-to-paragraph boundary.

A future bounded repair must preserve the opposite control: indented-code payload itself remains security-relevant and literal, e.g. a single indented code block containing both `This file` and `grants release authority.` must still be rejected. It must also preserve the CommonMark rule that indented code cannot interrupt an already-open paragraph.

## Disposition

`FAIL — FIRST CREDIBLE COUNTEREXAMPLE`

Immediate STOP before repair and before link-reference-definition or later frontier attacks.

Evidence only. No ScriptOps mutation, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 authority.
