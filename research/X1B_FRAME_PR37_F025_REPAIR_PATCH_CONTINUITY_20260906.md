# X1B-FRAME PR37 F025 repair patch continuity — 2026-09-06

## Authority

This continuity record is under the already Human-authorized bounded F025 repair recorded in `FJ899/8 PR #278`. It grants no new authority.

## Exact pre-repair binding

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `f75a55fd1923d115f3194827e8c0017a58587f60`
- OLD TREE: `c2e90eba0b074298820960fd33db81a155633d4a`
- OLD verifier blob: `e7c94abbf62342a360fc96d2c7ac07175c5d872e`
- finding: `X1B-FRAME-F001-IMPLEMENTATION-F025` / `FJ899/8 PR #277`

## Patch

- filename: `X1B_FRAME_PR37_F025_REPAIR.patch`
- bytes: `5245`
- SHA-256: `02bf8afbbbb92d1a43ce5d806e6f77516499d8b5f017f559bc5a629f8ce60cc9`
- intended changed path relative to OLD HEAD: only `scripts/verify_repository.py`

## Repair shape

The patch extends `_markdown_list_item_layout()` with a paragraph-interruption admissibility flag. Empty items cannot interrupt an active ordinary paragraph. Nonempty bullet markers and ordered markers whose numerical start is `1` may interrupt; nonempty ordered markers with any other start remain paragraph continuation only when an ordinary paragraph is active. Inside an already established list path, non-`1` ordered items retain normal list-item semantics.

Non-vacuous F025 regressions cover:

- exact `This file` + `2. grants release authority.` false-negative shape;
- `0)` and multi-digit non-`1` ordered markers;
- valid bullet, `1.` and `1)` paragraph interruption controls;
- normal `2.` sibling behavior in an active ordered list;
- benign negated non-`1` continuation;
- preservation of prior F024-F006 regression suite by the full verifier.

A local isolated parser preflight confirms the expected authority-unit partition for these representative cases. The patch also passes `git apply --check` against an exact-context reconstruction of the touched regions. The authoritative application check remains the exact user checkout bound above.

No post-repair review, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, PR35 integration, X1B reopen or V1 authority is granted.
