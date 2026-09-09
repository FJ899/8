# X1B-FRAME PR #37 — bounded fresh-final lazy-quote to HTML lifecycle repair authority

Human authorization in the project conversation authorizes exactly one bounded verifier-only repair for the fresh-final finding recorded in `FJ899/8 PR #534`.

## Frozen predecessor

- `FJ899/scriptops PR #37`
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `4c7684189602f12ca95f9363ebdba09d1876827b`
- TREE `c28d6b399cdf39cc2d84370a99a4fd5179ed84ed`
- verifier blob `9699fbe49d570f5b2e6ff0a9ec1ee569d93a2704`

## Finding

Direct complete explicit quoted HTML-comment boundary remains GREEN, but the same semantic boundary after a legal lazy continuation is reproducibly fused on the frozen predecessor:

```markdown
> This file
lazy continuation
> <!-- neutral comment -->
> grants release authority.
```

Fresh review evidence: `FJ899/8 PR #534`, run `34389407714`.

## Authorized scope

Exactly:

`lazy quoted paragraph -> complete explicit quoted HTML comment -> leaf-boundary lifecycle`

Goal:
1. preserve legal lazy continuation inside the current quoted paragraph;
2. flush that paragraph before the complete explicit quoted HTML-comment leaf;
3. begin the following explicit quoted paragraph independently.

## Required success conditions

1. exact fresh-final HTML reproduction => PASS;
2. exactly three semantic leaves: first paragraph with lazy continuation, complete HTML comment, following quoted paragraph;
3. no unit contains both `This file` and `grants release authority.`;
4. direct HTML-comment control remains GREEN;
5. repaired lazy->ATX case remains GREEN;
6. direct ATX control remains GREEN;
7. ordinary legal lazy continuation without a boundary remains one quoted paragraph;
8. inherited F042/F043/F044 corpus remains GREEN;
9. no generic all-HTML/all-block/all-lazy rewrite;
10. no new interaction testing;
11. freeze exact HEAD/TREE/verifier and STOP after targeted verification + final Verify/Smoke + full known-regression replay.

## Explicit non-authority

This authorization does not authorize:
- generic block lifecycle rewrite;
- generic HTML parser expansion;
- generic lazy-paragraph rewrite;
- interaction expansion or fresh discovery in the repair session;
- P0-P9;
- merge, movement of `main`, deploy/release/tag;
- canonical effect, active-product status promotion, X1B reopen, or V1.

After a successful repair and replay, fresh independent final review must be restarted from zero on the new exact freeze under a separate gate.