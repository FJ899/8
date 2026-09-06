# X1B-FRAME PR37 F028 REPAIR CONTINUITY — 2026-09-06

Human repair authority: PR #294.
Finding: X1B-FRAME-F001-IMPLEMENTATION-F028, durable finding PR #293.
Exact pre-repair ScriptOps binding:
- BASE 2f22843ac570498b506101addeba5453ab777f08
- OLD HEAD 0f7d34476c33fdc0e530f22e3168791c600c17e1
- OLD TREE 615af6e036dd1f6beaa818713984a2c18b1ee475
- OLD verifier blob 9292d0e637229c0d87b57519a6a10fd3cb5d8df3

## Minimal repair design

The repair is verifier-only and targets `_authority_soft_wrapped_units()` plus a small marker-signature helper and F028 regressions.

The reviewed implementation already computes `can_interrupt_paragraph` correctly for non-one ordered markers, but consumes that result only for an ordinary paragraph outside an active `list_frames` path. In an active list path it therefore promotes a syntactically list-like non-one ordered marker into a descendant or sibling boundary even when CommonMark keeps it as lazy continuation of the currently open list-item paragraph.

The correction must track the list marker family/delimiter for each active frame. For a recognized non-one ordered marker while a list path is active and no blank-line ownership transition has occurred:

1. Treat it as an established ordered-list sibling only when its marker indentation equals the current leaf indentation and its ordered delimiter matches the current leaf's ordered delimiter.
2. Otherwise, because it cannot interrupt the currently open paragraph, append that physical line to the current leaf paragraph instead of creating a new list frame.
3. Preserve existing blank-line ownership resolution before this decision.
4. Preserve bullets and one-start ordered markers as valid paragraph interruptions.
5. Preserve same-delimiter non-one ordered siblings inside an already-established ordered list.

## Required implementation edits

- Add an F028 repair note to the verifier module docstring.
- Add a helper returning a marker signature such as `("bullet", marker_char)` or `("ordered", delimiter)` for recognized ASCII CommonMark markers.
- Extend `list_frames` from `(marker_indent, content_indent, parts)` to `(marker_indent, content_indent, marker_signature, parts)`.
- Update list-frame unpacking and continuation append indexes accordingly.
- Before `flush_paragraph()` in the `layout is not None` branch, add the active-list/non-interrupting-marker rule described above.
- Keep the existing F027 W+1 ownership rule unchanged.

## Required F028 regressions

Positive rejection regressions must cover:
- a bullet item whose open paragraph is followed at the same column by a non-one ordered marker carrying the second half of a self-promotion claim;
- the nested family from F028 where a bullet parent is followed by non-one ordered-looking continuation lines at child indentation;
- at least one parenthesis-delimited ordered-marker variant.

Benign controls must cover:
- an established `1.` then `2.` ordered list remaining separate sibling authority units;
- an established nested `1)` then `2)` ordered list remaining separate sibling authority units;
- preservation of F027 through F006 regressions.

## Finalization requirements

After applying the edit to ScriptOps PR #37:
- full verifier must pass;
- final candidate must be exactly one replacement commit over frozen BASE;
- BASE-relative changed paths must remain exactly the frozen twelve-path surface;
- relative to OLD HEAD only `scripts/verify_repository.py` may change;
- both exact-head PR workflows must succeed;
- durable completion evidence must be frozen;
- STOP before any independent post-F028 review.

No merge, ScriptOps main movement, PR35 integration, deploy/release/tag, canonical effect, status promotion, X1B reopen or V1 authority is granted.
