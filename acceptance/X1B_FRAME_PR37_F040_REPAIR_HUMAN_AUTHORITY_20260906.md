# HUMAN AUTHORITY — X1B-FRAME PR #37 F040 bounded repair

Human said `accept` after the independent post-F039 review stopped on `X1B-FRAME-F001-IMPLEMENTATION-F040`.

This records authority for exactly one bounded F040 repair.

## Bound target

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `e8e745b5787f7f98c5e2df3fd03934acee332413`
- OLD TREE: `6363566d5b36f4669e234f31cd4660a1687c0597`
- OLD verifier blob: `73504fe6897a5b6a038da39b14478a37aa36bbc7`
- finding: `FJ899/8 PR #355`

## Authorized scope

Exactly one verifier-only repair of F040, the CommonMark indented-code block boundary omission.

The repair must preserve F039 through F029 and every earlier frozen regression/invariant. Relative to OLD HEAD, only `scripts/verify_repository.py` may differ.

The final candidate must remain exactly one replacement commit over frozen BASE, with the same frozen 12 BASE-relative changed paths. It must pass the full local verifier and both existing required workflows on the exact repaired HEAD. Completion evidence must then be frozen and work must STOP before any independent post-F040 adversarial review.

## Not authorized

No merge of PR #37 or PR #35, no ScriptOps main movement, deploy, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority.
