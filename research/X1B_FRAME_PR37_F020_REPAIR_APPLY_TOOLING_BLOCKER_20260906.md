# X1B-FRAME PR37 F020 repair apply continuity

This is a continuity record for the already Human-authorized F020 repair under `FJ899/8 PR #252`.

Exact live pre-repair target remains:

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `cdad32cdb9739b4baac30bfaf85b85b4f19056ea`
- TREE: `3c8fa40fb3885597e2348e3d9c75b8f74ef6404a`
- verifier blob: `ac18d2951f17e83ca38ca9b9a092f619e12cbcb6`

Prepared patch:

- file: `X1B_FRAME_PR37_F020_REPAIR.patch`
- bytes: `7374`
- SHA-256: `d4c9c0f891dac225864dd44cd0e5cb5dd1a1c5aeb7059bc5b87280edc37bbb22`
- changed path: only `scripts/verify_repository.py`

Repair design:

- parse Markdown list items as an active nested path;
- descendant items inherit ancestor text, so parent -> child wording cannot split one authority claim across nesting;
- a sibling at any nesting depth emits the prior active path and starts a new sibling path, preventing one sibling from donating self-reference to another sibling's promotion;
- blank-line continuation remains attached to the active leaf item when indentation owns the line;
- dedent after a blank emits the completed leaf path and resumes the nearest owning ancestor or an ordinary paragraph;
- existing F019-F006 semantics are preserved.

Non-vacuous production-validator regressions cover nested positive continuation, parent-child split promotion, ordered-parent nested promotion, nested sibling benign separation, ordered nested sibling benign separation, and nested benign negation.

The current connector has no safe patch-apply/file-upload route for the existing PR #37 branch while preserving the exact replacement-commit shape and force-with-lease stale-head guard. No ScriptOps ref/tree/commit/main mutation was attempted by this continuity record.

No new Human acceptance is required to execute this exact already-authorized repair in the retained LF local clone. Post-repair independent re-review still requires a separate Human gate.
