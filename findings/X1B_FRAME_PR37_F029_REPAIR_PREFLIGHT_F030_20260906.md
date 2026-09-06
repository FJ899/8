# X1B-FRAME PR37 F029 REPAIR PREFLIGHT — F030 — 2026-09-06

## Disposition

**REPAIR BLOCKED — first credible pre-implementation counterexample. STOP before ScriptOps mutation.**

Human F029 repair authority: PR #297.
F029 finding: PR #296.
F028 continuity being superseded by this finding: PR #295.

Exact untouched ScriptOps binding at discovery:
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `0f7d34476c33fdc0e530f22e3168791c600c17e1`
- verifier blob `9292d0e637229c0d87b57519a6a10fd3cb5d8df3`

## Finding

`X1B-FRAME-F001-IMPLEMENTATION-F030` — PR #295 contains an invalid same-column CommonMark regression and the accepted F029 repair wording is therefore unsafe to implement literally.

PR #295 requires a same-column bullet-item / non-one ordered-marker case to be folded as lazy continuation. CommonMark does not do that. A marker which is outside the current item's ownership indentation closes the item/list before the new list marker is interpreted; an ordered list beginning with a non-one number may then start because it is no longer interrupting that item's paragraph.

Reference-parser preflight using `markdown-it-py` in CommonMark mode:

```text
- A
2. B
```

parses as two top-level lists: one bullet list followed by an ordered list starting at 2.

By contrast:

```text
- A
  2. B
```

parses as one bullet-list item paragraph containing the second physical line as lazy continuation. This is the actual F028 family that needs repair.

The distinction is ownership indentation, not merely current-leaf marker family/delimiter. CommonMark also explicitly states that ordered list markers use `.` or `)` delimiters, that only an ordered list which interrupts an active paragraph must start at 1, and that changing an ordered-list delimiter starts a new list.

## Correct repair direction, not authority

A future amended repair should resolve a recognized non-one ordered marker against active item ownership before paragraph-interruption logic:

1. Preserve whether a blank line preceded the incoming physical line.
2. If no blank preceded it and the marker remains inside the current leaf's content indentation, it cannot interrupt that open paragraph and must remain lazy continuation.
3. If the marker indentation leaves the current leaf (`marker_indent < leaf.content_indent`), close/pop list-item frames according to content ownership until the correct container is reached; then interpret the marker as a sibling/new list boundary rather than forcing lazy continuation.
4. This same ownership unwind handles the F029 ordered-ancestor case without requiring a current-leaf-only signature test.
5. Preserve the durable nested F028 family, F029 ancestor-dedent separation, delimiter-change boundaries, blank-line behavior, and F027-F006 regressions.

Representative structural controls should include:
- `- A\n2. B` => separate authority units;
- `- A\n  2. B` => one folded authority unit;
- `1. A\n2) B` => separate lists/units;
- ordered ancestor -> nested child -> dedented non-one ordered marker => ancestor-level boundary;
- same established ordered-list siblings remain separate.

## Boundary

No change was made to `FJ899/scriptops PR #37`. The F029 repair authority in PR #297 is not consumed by a repair commit, but its current wording requires amendment before use because literal execution would encode an incorrect CommonMark boundary.

No repair, merge, ScriptOps main movement, PR #35 integration, deployment, release, tag, canonical effect, status promotion, X1B reopen or V1 authority is granted by this record.
