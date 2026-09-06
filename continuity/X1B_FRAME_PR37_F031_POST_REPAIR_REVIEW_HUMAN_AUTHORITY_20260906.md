# X1B-FRAME PR #37 — Human authority for one independent post-F031-repair review

Date: 2026-09-06

Human gate received in the controlling conversation: `accept`.

This authorizes exactly one independent, read-only adversarial post-repair review of the repaired `FJ899/scriptops PR #37` candidate.

## Exact review binding

- repository: `FJ899/scriptops`
- PR: `#37`
- state at authorization: OPEN / DRAFT / UNMERGED
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- reviewed HEAD: `841ecbf18f346becb4baf4bb11a31eaf391975eb`
- reviewed TREE: `c127542b6aaac202ac4fa7a96a4026b76455efca`
- reviewed verifier blob: `5fb041541b4c80c00f94b8c32ec2a3aa96389864`
- completion evidence: `FJ899/8 PR #305`
- candidate shape: exactly 1 commit over BASE; exactly the frozen 12-path BASE-relative surface
- pre-review CI: `Verify repository state` PASS and `Phase 6 ScriptOps smoke` PASS on the reviewed HEAD

## Review order and stop rule

The review must:

1. first re-attack the repaired F031 condition;
2. preserve the established regressions, including F030 and F029 and the earlier F017-F028 chain;
3. continue the remaining frozen/adversarial attacks against the same exact reviewed HEAD;
4. stop at the first credible counterexample, after freezing a durable finding; otherwise freeze PASS evidence.

## Read-only boundary

This authority does not authorize repair or mutation of the ScriptOps candidate during review.

Allowed writes are durable review/finding evidence in a separate `FJ899/8` evidence branch/draft PR only.

It does not authorize:

- merge of `FJ899/scriptops PR #37`;
- merge/rebase/cherry-pick of PR #35;
- ScriptOps main movement;
- deploy, release, or tag;
- canonical effect;
- active-product status promotion;
- X1B reopen;
- V1 authority;
- any repair after a finding without a fresh Human gate.

`INDEPENDENT REVIEW AUTHORITY != REPAIR AUTHORITY`

`GREEN CI != ADVERSARIAL REVIEW PASS`
