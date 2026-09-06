# X1B-FRAME PR #37 — F024 repair patch continuity

This is a durable continuity record under the already Human-authorized F024 repair in `FJ899/8 PR #273`.

## Exact ScriptOps pre-repair binding

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `beba918e23b3b98c8324c8b735265ca8931db562`
- OLD TREE: `f2026d57aad61dd08b175cdedba20087b7598720`
- OLD verifier path: `scripts/verify_repository.py`
- OLD verifier blob: `020c4ebe4ce2073c6172d316ad8a582a26832f46`
- finding: `X1B-FRAME-F001-IMPLEMENTATION-F024` / `FJ899/8 PR #272`

## Patch artifact

- file: `X1B_FRAME_PR37_F024_REPAIR.patch`
- bytes: `3533`
- SHA-256: `be6187e1b79ee90a370a1bb6c3675ca9f590f99aa240cb25ca068dc28fe49472`
- intended relative change surface: only `scripts/verify_repository.py`

The patch changes empty-list-item ownership indentation only when the parsed item is empty. For an empty bullet/ordered item, `content_indent` is set to `marker_indent + marker_width + 1` regardless of trailing spaces/tabs on the marker line. Non-empty list-item indentation remains unchanged.

The patch adds a F024 repair note and non-vacuous regressions for:

1. the exact bullet-plus-four-spaces F024 bypass;
2. an ordered empty marker with trailing spaces;
3. a bullet empty marker with a trailing tab;
4. a nested empty marker with trailing spaces;
5. benign same-item text without self-reference;
6. a benign historical/negated same-item authority statement.

Existing F023 paragraph-interruption semantics and representative F022/F021 parser behavior were exercised in a local parser matrix and remained unchanged. The matrix confirms that the OLD algorithm splits the exact F024/ordered/tab/nested cases while the repaired algorithm keeps each within the proper active item path. Patch syntax/apply behavior was checked against exact frozen hunk contexts arranged at the real target line positions.

This continuity record does not claim the user's actual checkout has applied or executed the patch. Actual checkout `git apply --check`, full verifier, replacement commit topology, guarded remote update, and both PR workflows remain required under PR #273.

No new review, repair, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, PR #35 integration, X1B reopen, or V1 authority is granted by this record.