# Human authority — F038 bounded repair

The Human explicitly accepted exactly one bounded repair of `X1B-FRAME-F001-IMPLEMENTATION-F038`.

## Exact ScriptOps binding

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `5d07e181c1a9d43f4bfca000962790b087b6fe15`
- OLD TREE: `bdbc73b06bb29c5b334cb2cd4bca0d49b68df63b`
- OLD verifier blob: `b29df53ab96596ac075118943b364d9b47eda6cd`
- finding evidence: `FJ899/8 PR #343`

## Authorized repair scope

Exactly one bounded F038 repair is authorized.

Only `scripts/verify_repository.py` may differ relative to OLD HEAD.

The repair must address the CommonMark HTML-block boundary/state defect identified by F038 while preserving F037, F036, F035, F034, F033, F032, F031, F030, F029 and every earlier frozen regression and security invariant.

The final ScriptOps candidate must remain:

- exactly one replacement commit over frozen BASE;
- exactly the same frozen 12 BASE-relative changed paths;
- verifier-only relative to OLD HEAD;
- locally coherent under the full verifier;
- green in both existing remote workflows on the exact repaired HEAD.

After successful local and remote validation, completion evidence must be frozen durably and work must STOP before any independent post-repair adversarial review.

## Not authorized

This acceptance does not authorize repair outside the bounded verifier surface, merge of PR #37 or PR #35, ScriptOps `main` movement, deploy/release/tag, canonical effect, active-product status promotion, X1B reopen, V1 action, or unrelated cleanup.
