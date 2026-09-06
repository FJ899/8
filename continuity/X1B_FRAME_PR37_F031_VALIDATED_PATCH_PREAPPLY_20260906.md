# X1B-FRAME PR37 F031 VALIDATED PATCH PRE-APPLY — 2026-09-06

Authority: Human F031 bounded repair authority in PR #303.

Exact ScriptOps pre-repair binding:
- PR #37
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `0f7d34476c33fdc0e530f22e3168791c600c17e1`
- verifier blob `9292d0e637229c0d87b57519a6a10fd3cb5d8df3`

Prepared patch properties:
- affected path: only `scripts/verify_repository.py` relative to OLD HEAD;
- 5 unified-diff hunks;
- 163 added lines / 15 removed lines;
- no helper deletion and no removal of F017-F027 regression families;
- patch SHA-256 `444f72b19deb5882b8f328270f492a5c007929cd1965c0c8d5c189b24f5a15c4`;
- local audit harness SHA-256 `f9fce36620893fea9244473dee89a70420b4db029d013550e5f04f6dafdb9da1`.

Differential preservation preflight:
- existing F017-F027 fixture set: 64 cases, 0 unit-shape differences versus frozen OLD HEAD;
- targeted F028-F031 structural matrix: 320 evaluated cases, 0 mismatches against CommonMark path relation;
- broader marker/indent/gap matrix: 50,466 evaluated cases, 34,476 intentionally skipped cases whose subject/predicate lived in non-inline code-like blocks, 0 mismatches;
- tab/empty-marker matrix: 924 evaluated cases, 1,980 skipped non-comparable cases, 0 mismatches;
- unified patch syntax/context check against exact fetched OLD-HEAD hunk contexts: PASS.

Repair design:
- keep ordinary nonblank text as lazy continuation when an active list paragraph remains open;
- retain existing blank-line ownership unwind for F022;
- treat any marker at an already-established marker indentation as a structural boundary regardless of list family/delimiter;
- otherwise resolve a candidate marker to the deepest active owner whose content indentation can host it with CommonMark's container-relative 0-3 extra columns;
- closing descendant frames makes the incoming marker a new structural block;
- only a candidate that remains inside the current leaf's open paragraph is subject to paragraph-interruption rules, preserving non-one/empty-marker lazy continuation;
- a deep candidate that no owner can host remains paragraph/code-like content rather than becoming a list solely because a list path is active.

Current execution blocker:
- Git Diff Patcher Bridge reports `account_link_required` before any repository/workspace can be selected.
- Therefore no patch was queued or locally applied, no final ScriptOps commit was created, and the PR #303 authority has not yet been consumed by a completed repair.

This is pre-apply continuity evidence only, not repair completion and not review PASS. No merge, ScriptOps main movement, PR #35 integration, deploy/release/tag, canonical effect, status promotion, X1B reopen or V1 authority is granted.