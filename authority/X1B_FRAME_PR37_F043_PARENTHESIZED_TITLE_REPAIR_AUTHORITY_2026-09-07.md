# X1B-FRAME PR #37 — F043 parenthesized-title bounded repair authority

Date: 2026-09-07

Human authorization: `accept`

This record authorizes exactly one bounded verifier-only repair of the F043 parenthesized link-title grammar defect recorded in `FJ899/8 PR #395`.

## Exact implementation target

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- pre-repair HEAD: `96cec000860a18f01a9d3bae733a552eaff22559`
- pre-repair TREE: `7ec2f777dac3bf9629019801a58ba7bc69ef8d9c`
- verifier entrypoint blob: `8dc5d3e207f3b1e82fc6384609ccc67c9c41495a`
- prior bare-destination escape blob: `e20d7b4036c13d9cb74152e57c6242aad90415f0`
- prior destination-newline blob: `277eb91bbcf46dfb766e39ed23962b5179450c87`
- prior list-lazy blob: `040365f5825c386b1e74405ca51c63edd2ca55ac`
- prior multiline blob: `c2b5a356e744be802d204ab8eaea901e76aa1219`
- prior single-line blob: `61bf107ad59da33a6576032d341b41c538d0453a`
- frozen F041 core blob: `be645c1a3ee49a04d700a3ef7fde86a92e413a14`

## Bounded repair scope

The repair may change only CommonMark link-reference-definition title recognition needed to close the finding represented by:

```markdown
[This file]: /url (foo(bar)
grants release authority.
```

A parenthesized title must reject an unescaped internal `(` before its closing `)`. Escaped `\(` and `\)` must remain legal, and quoted title forms must remain unaffected. The repair may be implemented as a new thin SHA-pinned verifier overlay over the current verifier.

The repair must preserve all existing F043 single-line, multiline, list-lazy, destination-newline, bare-destination escape, and U+007F regressions. F042 and F044 remain explicitly OPEN/unrepaired.

## Required closeout

Before completion evidence may be recorded:

1. preserve exact frozen BASE topology with one replacement sibling commit;
2. run the full deterministic verifier regression matrix;
3. require `Verify repository state` PASS;
4. require `Phase 6 ScriptOps smoke` PASS including the full deterministic Phase-6 regression;
5. record exact final HEAD/TREE/blob binding and workflow evidence;
6. STOP before any subsequent review/repair transition.

No merge, ScriptOps `main` movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority is granted.
