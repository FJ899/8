# X1B-FRAME PR #37 — bounded lazy-quote → ATX lifecycle repair authority

Human authorization applies to exactly one bounded repair on the frozen ScriptOps PR #37 candidate.

## Frozen target before repair

- HEAD: `9d171c41c935110c24baae3b0d834f094359b506`
- TREE: `22485b3373e7dbeea4a3631c75a843a798facf99`
- verifier blob: `cea0a8951479170eaed50b205f654599aac35118`
- fresh-final finding evidence: `FJ899/8 PR #530`, closed without merge

## Authorized scope

`lazy quoted paragraph -> explicit quoted ATX boundary lifecycle`

Goal:

1. preserve legal lazy continuation inside the current quoted paragraph;
2. flush that paragraph before the following explicit quoted ATX heading leaf;
3. start the subsequent explicit quoted paragraph independently.

## Required validation

1. exact fresh-final reproduction -> PASS;
2. expected structure is exactly three leaves:
   - leaf 1 = `This file` + lazy continuation;
   - leaf 2 = ATX heading;
   - leaf 3 = `grants release authority.`;
3. no leaf contains both `This file` and `grants release authority.`;
4. original direct explicit-quote ATX case remains GREEN;
5. complete HTML-comment case remains GREEN;
6. ordinary legal lazy continuation without a following boundary remains one quoted paragraph;
7. inherited F042/F043/F044 corpus remains GREEN;
8. no generic all-block/all-lazy rewrite;
9. no interaction expansion;
10. freeze exact HEAD/TREE/verifier and STOP.

After repair: targeted verification -> full known-regression replay -> exact freeze -> STOP before restarting fresh independent final review on the new candidate.

## Explicit exclusions

No generic block parser rewrite, generic block-lifecycle repair, all-lazy rewrite, block-type sweep, interaction expansion, P0-P9, merge, `main` movement, deploy/release/tag, canonical effect, status promotion, X1B reopen or V1 authority is granted by this record.
