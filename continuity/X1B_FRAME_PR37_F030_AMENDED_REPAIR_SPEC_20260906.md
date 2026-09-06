# X1B-FRAME PR37 F030 AMENDED REPAIR SPEC — 2026-09-06

Human authority: PR #299.
Findings preserved: F028 / F029 / F030.

Exact ScriptOps pre-repair binding:
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `0f7d34476c33fdc0e530f22e3168791c600c17e1`
- verifier blob `9292d0e637229c0d87b57519a6a10fd3cb5d8df3`

## Minimal structural repair

The repair must remain confined to `scripts/verify_repository.py` relative to OLD HEAD.

1. Add a small marker-signature helper for recognized CommonMark list markers, returning ordered delimiter identity or bullet identity.
2. Extend each active list frame so it stores marker indentation, content ownership indentation, marker signature, and accumulated parts.
3. Before marker classification, resolve content ownership for every nonblank incoming line, not only after a blank line: while the incoming leading indentation is below the current leaf content indentation, emit the active path and pop frames until an owning frame remains or the path becomes empty.
4. Only after this ownership unwind, parse a list marker with deep-indent recognition allowed only when an active owner remains.
5. For a non-interrupting non-one ordered marker while an owner remains, preserve an established sibling boundary only when the marker resolves to an active ordered frame at the same marker indentation with the same delimiter. Otherwise append the physical line to the current owning item's paragraph as lazy continuation.
6. A marker that leaves all active ownership is evaluated as top-level Markdown structure. Therefore a non-one ordered marker may begin a new list after a preceding list has closed; it must not be forced into the previous item's paragraph merely because its number is not one.
7. Preserve the existing F027 W+1 item-ownership rule and all earlier F006-F027 behavior.

## Structural preflight results

A neutral local harness implementing the rule above produced these unit shapes:

- F028 nested lazy family: one inherited parent/child unit containing both non-one ordered-looking continuation lines.
- F029 ordered ancestor -> nested child -> dedented ordered ancestor sibling: first path emitted, then the dedented marker starts a separate ancestor-level sibling unit.
- F030 same-column bullet item followed by non-one ordered marker: bullet unit closes and the ordered marker starts a separate list unit.
- Established top-level ordered 1 -> 2: separate sibling units.
- Established nested ordered 1) -> 2): separate sibling paths inheriting the parent.

## Required regressions

Non-vacuous regressions in the verifier should prove all five structural distinctions above plus preserve F027 through F006.

## Finalization requirements

- Final candidate exactly one replacement commit over frozen BASE.
- BASE-relative changed paths exactly the frozen twelve-path surface.
- Relative to OLD HEAD only `scripts/verify_repository.py` changes.
- Full verifier passes.
- Exact-head `Verify repository state` and `Phase 6 ScriptOps smoke` workflows both succeed.
- Durable completion evidence is frozen.
- STOP before independent post-F030 review.

This continuity record grants no additional authority and no merge, main movement, PR #35 integration, deploy/release/tag, canonical effect, status promotion, X1B reopen or V1 authority.
