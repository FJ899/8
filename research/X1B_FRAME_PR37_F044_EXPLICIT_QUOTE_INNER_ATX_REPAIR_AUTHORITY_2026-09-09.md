# X1B-FRAME PR #37 — F044 explicit quote / inner ATX repair authority

Human authorization recorded from the project conversation on 2026-09-09.

## Frozen implementation target

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `fd0bbed3399a4eb72a4d9658e502e17b394f01a5`
- TREE: `cddb1b8aaa3afbdb2cf690b1d20a44c1c12c8429`
- verifier blob: `88bce47c461836cb6db5452e2de02fa5f50630e3`

## Finding being repaired

`EXPLICIT QUOTE / INNER ATX HEADING BOUNDARY = FAIL / REPRODUCIBLE`

Recognition is already correct. The defect is block-leaf lifecycle ordering: an explicit quoted ATX line is appended to `block_quote_parts` before its ATX boundary is applied, so the prior quoted paragraph, the heading, and the following quoted paragraph remain fused in one interpretive unit.

## Authorized scope

Exactly one bounded parser repair for:

- explicit top-level block quote;
- inner ATX heading boundary;
- block-leaf flush/separation lifecycle.

Do not expand to fenced code, HTML, thematic breaks, list ownership changes, recursion/cardinality variants, generic all-block-transition handling, cross-axis interaction testing, or parent-count sweeps.

## Required validation

1. ordinary explicit-quote continuation control remains exactly one unit;
2. exact ATX reproduction yields three sequential block leaves: quoted paragraph / quoted ATX heading / quoted paragraph;
3. `This file` and `grants release authority.` do not coexist in one unit;
4. the split is caused by structural ATX recognition and flush/boundary lifecycle, not heading text special-casing;
5. inherited F042/F043/F044 regressions remain GREEN;
6. no text-specific special case;
7. freeze exact final candidate and STOP.

Any failure -> record evidence and STOP.

No merge, `main` movement, deploy/release/tag, canonical effect, status promotion, X1B reopen or V1 authority is granted.
