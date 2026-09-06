# X1B-FRAME — Human acceptance of F017 and bounded PR37 repair authority

Date: 2026-09-06

## Human decision

The Human `accept` in the controlling conversation accepts exactly the immediately preceding finding `X1B-FRAME-F001-IMPLEMENTATION-F017` recorded in `FJ899/8 PR #238` and authorizes exactly one bounded replacement repair of `FJ899/scriptops PR #37` for that finding.

`AI PROPOSES != HUMAN DECIDES`

## Exact pre-repair target

- repository: `FJ899/scriptops`
- PR: `#37`
- state: `OPEN / DRAFT / UNMERGED`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `a94a4018b469ae864e4715157f00b9d765df11c0`
- TREE: `420faf0b06f4b53228770735f1504b3f58d5c580`
- verifier path: `scripts/verify_repository.py`
- verifier blob: `d7153ccdf4469c7355e9b6aa0926228a91e74c00`
- commits above BASE: exactly `1`
- base-relative changed paths: exactly the frozen `12`-path frame/status/verifier surface.

## Accepted finding

`F017`: the F016 whole-line fallback is still scoped to each physical line because `layer_b_self_promotion_claim()` iterates over `text.splitlines()`. A normal Markdown soft line break can therefore separate a self-reference from its positive authority predicate, for example:

```text
This file,
therefore grants release authority.
```

and evade Layer-B self-promotion rejection.

## Authorized repair only

Exactly one replacement repair may:

1. keep the final PR #37 candidate exactly one commit over frozen BASE `2f22843ac570498b506101addeba5453ab777f08`;
2. preserve exactly the frozen twelve base-relative changed paths;
3. relative to pre-repair HEAD `a94a4018b469ae864e4715157f00b9d765df11c0`, change only `scripts/verify_repository.py`;
4. close F017 multiline / Markdown soft-wrap subject-predicate fragmentation so line wrapping cannot separate a Layer-B self-reference from its positive authority predicate;
5. preserve the F016 through F006 security and false-positive boundaries already established;
6. add non-vacuous F017 regression coverage through the production Layer-B validator, including positive multiline self-promotion rejection and benign multiline negation acceptance;
7. run the repository verifier and the existing GitHub `Verify repository state` and `Phase 6 ScriptOps smoke` checks;
8. force-update the existing PR #37 head branch only after exact pre-push binding checks and only with stale-head protection;
9. stop after freezing the exact repaired HEAD/TREE/verifier blob and CI outcome.

## Not authorized

This acceptance does **not** authorize:

- any repair beyond F017;
- any independent post-repair review;
- merge of PR #37 or PR #35;
- movement of `scriptops/main`;
- deployment, release, tag, or canonical effect;
- active-product status promotion;
- X1B reopen;
- V1 authority;
- new capability or broader parser redesign beyond what is necessary to close F017 while preserving prior regressions.

A separate Human gate is required before any post-F017 independent re-review.