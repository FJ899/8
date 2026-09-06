# X1B-FRAME PR #37 — Human authority for one independent post-F014 re-review

Date: 2026-09-06

Human authorization received in chat as exact `accept` after the bounded F014 repair completed and both candidate CI workflows passed.

## Exact review target

Repository: `FJ899/scriptops`

Pull request: `#37`

BASE: `2f22843ac570498b506101addeba5453ab777f08`

HEAD: `2fab77397cceda52725c86f3c7f4ea071174d5b0`

TREE: `b18df96e569c1b61065c4389dc143e7bd5db5e16`

Candidate shape at authorization: exactly 1 commit over BASE, exactly 12 base-relative changed paths, OPEN / DRAFT / UNMERGED.

The review is bound to superseding plan `FJ899/8 PR #201` at HEAD `5037240043ff36bbcfe50b8daa47df79ef0fcb06` and independent plan-review PASS `FJ899/8 PR #202` at HEAD `91f9a3f3966dca320fb48d3681223d3558f6259f`.

F014 provenance:
- finding: `FJ899/8 PR #228`, HEAD `acd3e4bc600ebe11acca3e933a5ab697150388e8`;
- Human acceptance + one bounded repair authority: `FJ899/8 PR #229`, HEAD `8ef85fea1bdc50db3b7c9dcac981837d3dd42236`;
- repaired ScriptOps candidate: HEAD/TREE above.

## Authorized operation

Exactly one independent read-only implementation re-review of this exact PR #37 target.

Order:
1. re-attack F014;
2. regress F013, F012, F011, F010, F009, F008, F007, F006;
3. if none yields a credible counterexample, continue frozen independent attacks Q5 through Q15 under PR #201;
4. first credible in-scope counterexample => record one durable finding in `FJ899/8` and STOP;
5. if no credible counterexample remains, record one bounded implementation re-review PASS in `FJ899/8`.

Q1-Q3 were already exercised without a credible counterexample before F009; Q4 was the F009 finding. This authority resumes only the remaining ordered work stated above.

## Non-authority / prohibitions

This authorization is read-only with respect to `FJ899/scriptops`.

It does **not** authorize:
- any repair or further ScriptOps edit;
- merge or movement of ScriptOps `main`;
- PR #35 integration/rebase/superseding implementation;
- deployment, release, tag, canonical effect, or active-product status promotion;
- X1B reopen or V1 authority;
- treating a review PASS as execution authority.

`AI PROPOSES != HUMAN DECIDES`

`REVIEW AUTHORITY != REPAIR AUTHORITY`

`REVIEW PASS != MERGE AUTHORITY`
