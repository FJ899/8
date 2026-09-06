# X1B-FRAME PR37 F027 REPAIR PATCH CONTINUITY — 2026-09-06

This is a continuity record under the already Human-authorized bounded F027 repair (`FJ899/8 PR #288`). It grants no new authority.

## Exact pre-repair ScriptOps binding

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `72f1e00c45a58c107a4e4f2a90cccd92fa76cbe9`
- OLD TREE: `9b9f858d2b505809332e85c6cbf506d8f031a441`
- OLD verifier blob: `914ff100f03b23268a0a96db57103727e912a569`

## Patch identity

- filename: `X1B_FRAME_PR37_F027_REPAIR.patch`
- bytes: `4865`
- SHA-256: `5145d171934c781d5337041ce67daa276f84abbb040ad9ebe63053e6c50d87f9`
- relative repair surface: `scripts/verify_repository.py` only
- patch numstat: `74 additions / 2 deletions`

## Repair shape

The patch changes CommonMark list ownership only for a nonempty list item whose physical post-marker whitespace spans more than four columns. In that special indented-code-start case, item ownership uses `marker_indent + marker_width + 1`; the remaining whitespace belongs to the initial code block. For ordinary 1–4-column post-marker gaps, the existing physical content indentation remains unchanged.

The patch also:

- preserves F026 ASCII-only ordered marker recognition;
- preserves F025 paragraph-interruption behavior;
- adds exact ordered and bullet F027 positive regressions;
- adds a nested same-item F027 positive regression;
- checks the 4-column normal / 5-column special boundary non-vacuously;
- adds benign dedent and sibling controls;
- adds `[PASS] F027 indented-code list-item ownership regression`.

A standalone parser matrix confirmed:

- `1.     This file` ownership indent = `3`;
- `-     This document` ownership indent = `2`;
- `1.    This file` (four-column gap) ownership indent remains `6`;
- ordered, bullet and nested F027 subject/predicate cases fold into one authority unit;
- dedented text and a following sibling remain separate authority units.

`F027_PARSER_MATRIX_PASS`

## Authority boundary

This continuity artifact does not authorize application, push, review, merge, main movement, deployment, release, tag, canonical effect, status promotion, PR #35 integration, X1B reopen or V1 action beyond what is already explicitly authorized by PR #288. The repair must still satisfy all stale-head, exact-surface, full-verifier, workflow and completion-evidence requirements of that Human gate.
