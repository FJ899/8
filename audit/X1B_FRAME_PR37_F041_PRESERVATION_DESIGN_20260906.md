# X1B-FRAME PR37 F041 preservation audit and bounded repair design

Date: 2026-09-06
Status: PRE-REPAIR DESIGN / NO SCRIPTOPS MUTATION

Target:
- `FJ899/scriptops PR #37`
- HEAD `a504b33e0420d3ac487a1d69aeddebc6719dcd62`
- TREE `590da6890ba88334aeec59a908eacb52adbade5c`
- verifier blob `b4df7351df142d20507aab2eff4ae2991ddc9acb`
- finding `FJ899/8 PR #366`
- repair authority `FJ899/8 PR #367`

## Root cause

Top-level block quotes are currently represented by one coarse `block_quote_parts` accumulator plus `block_quote_lazy`. That is sufficient for a single quoted paragraph and its lazy continuation, but it does not represent an indented-code leaf inside the quote. Consequently an explicit quoted dedent after quoted indented code is appended to the same authority unit instead of ending the code leaf and starting a new quoted paragraph leaf.

Representative false positive:

```markdown
>     This file
> grants release authority.
```

The first line is quoted indented code. The second line is a distinct quoted paragraph beginning immediately after code dedent. They must not be folded into one top-level authority unit.

## Preservation constraints

The repair must preserve all existing F040/F035 semantics:

1. A quoted ordinary paragraph may continue explicitly or lazily as one authority unit.
2. Four-plus content columns cannot interrupt an already-open quoted paragraph.
3. Multiple quoted indented-code lines remain one literal code leaf and remain security-relevant as one unit.
4. Blank quoted lines may remain within an active quoted indented-code block; they do not manufacture a paragraph boundary.
5. Leaving the quote container ends the quoted code leaf before outside text is processed.
6. List-owned quotes remain inside their owning list-item security context; F019/F020/F035 list-item inheritance is not changed.
7. F036-F039 leaf handling, F031 lazy list continuation, and all prior F009-F040 regressions remain unchanged.

## Bounded design

Add one top-level quote-local state bit, conceptually `block_quote_indented_code`.

- It becomes true only when a top-level quote leaf starts with nonblank quoted content whose post-marker indentation is at least four columns while no quoted paragraph is already open.
- While active:
  - explicit quoted blank content stays inside the code leaf;
  - explicit quoted nonblank content with at least four content columns stays inside the same code leaf;
  - the first explicit quoted nonblank line with fewer than four content columns flushes the code leaf as its own authority unit, then starts a fresh quoted leaf from that same line;
  - a line leaving the quote container flushes the code leaf before normal processing.
- If `block_quote_lazy` already indicates an open quoted paragraph, a four-plus-column explicit quoted line remains paragraph continuation and must not activate code state.
- `flush_block_quote()` resets both paragraph-lazy and quote-code state.

This is deliberately not a generic nested CommonMark parser and does not expand the repair to link reference definitions or other future frontier items.

## Regression additions

Minimum new F041 controls:

- benign: quoted indented code followed immediately by dedented quoted paragraph must remain split;
- benign: quoted code followed by a dedented quoted paragraph and later outside text must not donate the code self-reference;
- reject: multiple quoted indented-code lines remain one security-relevant code unit;
- reject: quoted blank line between indented chunks does not split one code block;
- reject: four-plus indentation cannot interrupt an already-open quoted paragraph.

Expected implementation surface: only `scripts/verify_repository.py`.

No merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority is implied.
