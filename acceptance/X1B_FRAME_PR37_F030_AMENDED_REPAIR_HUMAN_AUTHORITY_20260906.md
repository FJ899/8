# X1B-FRAME PR37 F030 AMENDED REPAIR HUMAN AUTHORITY — 2026-09-06

HumanDecision: ACCEPT.

This record supersedes only the defective repair-direction portion of PR #295 / PR #297 that was identified by `X1B-FRAME-F001-IMPLEMENTATION-F030` in PR #298.

Exactly one bounded amended repair is authorized for `FJ899/scriptops PR #37`.

Exact pre-repair binding:
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `0f7d34476c33fdc0e530f22e3168791c600c17e1`
- verifier blob `9292d0e637229c0d87b57519a6a10fd3cb5d8df3`

## Authorized repair rule

The verifier-only repair must resolve Markdown list structure by content ownership before paragraph-interruption semantics:

1. For an incoming physical line, first resolve whether its indentation remains within the current leaf item's content ownership.
2. If the line leaves the current leaf ownership, unwind the active list path to the nearest owning ancestor before classifying the marker.
3. A marker that leaves all current ownership may begin a new top-level list even when it is a non-one ordered marker; it must not be forced into lazy continuation merely because its start number is not one.
4. If the line remains within the currently owning item, then apply the CommonMark paragraph-interruption rule: a non-one ordered marker cannot interrupt the currently open paragraph and must remain lazy continuation unless it resolves to a valid established sibling at the owning depth.
5. Preserve legal ancestor-level ordered siblings reached by dedent, including the F029 family.
6. Preserve the original nested F028 lazy-continuation family.
7. Preserve F027 through F006 regressions.

## Boundaries

- Relative to OLD HEAD, only `scripts/verify_repository.py` may change.
- Final candidate remains exactly one replacement commit over frozen BASE.
- BASE-relative changed paths remain exactly the frozen twelve-path surface.
- Add non-vacuous regressions for F028, F029, and F030 distinctions.
- Run the full verifier and both exact-head required workflows.
- Freeze durable completion evidence and STOP before independent post-repair review.

No merge, ScriptOps main movement, PR #35 integration, deploy/release/tag, canonical effect, status promotion, X1B reopen, or V1 authority is granted.
