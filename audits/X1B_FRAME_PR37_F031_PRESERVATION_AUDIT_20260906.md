# X1B-FRAME PR37 F031 PRESERVATION AUDIT — 2026-09-06

Disposition: READ-ONLY DESIGN AUDIT COMPLETE / NO REPAIR APPLIED.

Exact ScriptOps target remains:
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `0f7d34476c33fdc0e530f22e3168791c600c17e1`
- verifier blob `9292d0e637229c0d87b57519a6a10fd3cb5d8df3`
- PR #37 remains OPEN / DRAFT / UNMERGED / one commit / frozen twelve-path surface.

Active blocker: `X1B-FRAME-F001-IMPLEMENTATION-F031` in PR #301.

## Priority order executed

P0. Freeze exact PR #37 binding and prohibit patch/apply during audit.
P1. Extract preservation invariants from F017-F030 and the existing production regression matrix.
P2. Derive a laziness-aware list-boundary decision order that does not require a parser rewrite.
P3. Attack that decision order across soft/lazy continuation, blank/no-blank, nested/dedent, sibling/new-list, delimiter change, empty item, ASCII ordered marker, and F027 W+1 ownership.
P4. Patch is intentionally NOT executed: F031 still requires a separate Human repair gate.

## Preservation invariants

The next repair must preserve all of the following simultaneously:

1. F017/F018: physical soft wraps remain one logical authority paragraph.
2. F019: after a blank line, an indented continuation paragraph that remains owned by the same list item stays in the same security unit.
3. F020/F021: nested descendants inherit ancestor text; siblings at any supported depth remain separate units; deep-marker validity is container-relative rather than a global absolute-indent exemption.
4. F022: after a blank line, ownership is resolved before interpreting a deep marker.
5. F023/F024: marker-only empty items are real boundaries inside lists but cannot interrupt an ordinary paragraph; blank-start item ownership uses marker width plus one.
6. F025: a non-one ordered marker cannot interrupt an open paragraph.
7. F026: ordered markers remain ASCII `0-9` only.
8. F027: post-marker whitespace beyond four columns uses the W+1 ownership rule for an item beginning with indented code.
9. F028: a non-one ordered-looking line inside an open list-item paragraph is lazy continuation when it cannot interrupt that paragraph.
10. F029: a dedented marker that resolves to an already-active ancestor list level is a structural sibling boundary.
11. F030: a marker at the same structural list level is a boundary even when it changes list family or delimiter; changing bullet/delimiter starts a new list rather than joining distinct units.
12. F031: ordinary paragraph continuation text may lazily lose some or all list-item indentation; indentation alone must not force ownership unwind when no blank line or structural block boundary exists.

## Safe decision order for the existing list_frames design

Do not perform unconditional nonblank ownership unwind.

For each nonblank line:

A. Parse a possible ASCII CommonMark list marker as a candidate, without yet declaring it structural.

B. If there is no marker candidate:
- with active list frames and no preceding blank: append to the current leaf as lazy continuation regardless of reduced indentation;
- with a preceding blank: retain the existing F022 ownership check and pop only while the line is below the current leaf `content_indent`;
- after the ownership check, append to the nearest remaining owner or ordinary paragraph.

C. If there is a marker candidate and its `marker_indent` equals the marker indentation of any active frame:
- it is a sibling/new-list boundary at that structural depth;
- emit the old active path and replace that frame plus descendants;
- do NOT require matching bullet character, ordered family, or ordered delimiter; a delimiter/family change is still a boundary.

D. Otherwise resolve the candidate against container-relative indentation:
- an owner can host a nested list marker only when `owner.content_indent <= marker_indent <= owner.content_indent + 3`;
- if reaching that owner requires closing one or more active descendant frames, the marker begins a new block after the closed child list and is structural even when an ordered start is not `1`;
- if no active owner can host it but the marker is valid at top level (0-3 leading columns), close the active list path and treat it as a new top-level list boundary.

E. Only when the candidate remains inside the CURRENT leaf container, with no blank boundary and no structural sibling/ancestor/new-list resolution, apply paragraph-interruption semantics:
- bullet or ordered start `1` may interrupt and start a descendant list;
- empty items and non-one ordered markers may not interrupt and are appended as lazy paragraph continuation.

F. A candidate more than three columns beyond the owning item's `content_indent` is not a nested list marker for that owner. It remains paragraph/code-like content according to the existing ownership state; do not create a list boundary merely because an active list exists.

This preserves F028 and F031 without sacrificing F029/F030 and removes the need for PR #300's marker-signature-only sibling rule.

## Adversarial preservation matrix required before any patch is accepted

Positive rejection cases that must remain joined:
- ordinary unindented lazy continuation inside bullet item (F031);
- partially dedented lazy continuation;
- nested lazy continuation;
- F028 nested non-one ordered-looking continuation;
- blank-line owned continuation (F019);
- F027 W+1 continuation;
- parent -> descendant subject/predicate split (F020/F021).

Benign separation cases that must remain separate:
- same-level bullet siblings;
- same-level ordered `1.` -> `2.` siblings;
- same-level change of bullet character;
- same-level change of ordered delimiter `.` -> `)`;
- bullet list followed at the same structural level by an ordered list starting at `2` (F030);
- ordered ancestor -> nested child -> dedented ancestor sibling (F029);
- parent item -> child list -> a new non-one ordered list at the parent content level;
- blank-line dedent to ordinary paragraph;
- F022 wide-item followed by separate code-like block.

Marker validity controls:
- empty marker cannot interrupt paragraph;
- non-one ordered marker cannot interrupt paragraph;
- Unicode decimal lookalikes are not ordered markers;
- nested marker may use only 0-3 extra columns relative to the owning container;
- F027 W+1 behavior remains unchanged.

## Patch budget after future Human F031 repair authority

The preferred repair should remain confined to `scripts/verify_repository.py` and to the list-layout / `_authority_soft_wrapped_units()` logic plus new non-vacuous regressions. No removal of F017-F027 regression families, no broad helper deletion, and no change to the other eleven PR #37 paths.

A candidate must be rejected before apply if it:
- unconditionally unwinds every nonblank line by `content_indent`;
- treats all deep marker-shaped lines as structural merely because `list_frames` is nonempty;
- requires same marker family/delimiter for a real same-level boundary;
- deletes or weakens existing F017-F027 positive or benign controls;
- changes any path other than `scripts/verify_repository.py` relative to the frozen old HEAD.

## Boundary

This audit record grants no repair authority. It does not modify `FJ899/scriptops PR #37`, does not queue/apply a GDP patch, and grants no merge, ScriptOps main movement, PR #35 integration, deploy/release/tag, canonical effect, status promotion, X1B reopen, or V1 authority.

Next legal step: separate explicit Human acceptance of F031 and authorization for exactly one bounded laziness-aware F031 repair, followed by full differential preservation validation and STOP before independent post-repair review.
