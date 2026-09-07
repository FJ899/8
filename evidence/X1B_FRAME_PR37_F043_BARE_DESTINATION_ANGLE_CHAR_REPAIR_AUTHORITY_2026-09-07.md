# X1B-FRAME PR #37 — Human authority for bounded F043 bare-destination angle-character repair

Date: 2026-09-07
Authority source: Human `accept` in the controlling conversation.

## Exact repair target

Repository: `FJ899/scriptops`
PR: `#37`
State required during repair: OPEN / DRAFT / UNMERGED
Base branch: `main`
Frozen BASE: `2f22843ac570498b506101addeba5453ab777f08`
Pre-repair HEAD: `343f7fe72c9f60b092ef088cc67a68b109707b9b`
Pre-repair TREE: `d9fef5895d783a9eff95027762c0d33b3d36a642`
Pre-repair verifier entrypoint blob: `1bf97ebb68a72cc0e576876d91b3f754a2141c0e`
Finding source: `FJ899/8 PR #399`

Pinned predecessor layers include:
- F043 U+007F overlay: `8dc5d3e207f3b1e82fc6384609ccc67c9c41495a`
- F043 bare-destination escape overlay: `e20d7b4036c13d9cb74152e57c6242aad90415f0`
- F043 destination-newline overlay: `277eb91bbcf46dfb766e39ed23962b5179450c87`
- F043 list-lazy overlay: `040365f5825c386b1e74405ca51c63edd2ca55ac`
- F043 multiline overlay: `c2b5a356e744be802d204ab8eaea901e76aa1219`
- F043 single-line overlay: `61bf107ad59da33a6576032d341b41c538d0453a`
- frozen F041 core: `be645c1a3ee49a04d700a3ef7fde86a92e413a14`

## Authorized repair boundary

Exactly one bounded verifier-only repair of the F043 CommonMark bare-link-destination angle-character overrestriction is authorized.

The repair may correct only this grammar family:
- a bare destination is invalid if its first character is `<`;
- an otherwise valid bare destination may contain `>`;
- an otherwise valid bare destination may contain `<` after its first character;
- existing requirements for nonempty destination, whitespace/ASCII-control rejection, balanced unescaped parentheses, CommonMark backslash escapes, title parsing, multiline folding, container ownership, and all earlier F043 repairs must remain preserved.

Representative closure from PR #399:

```markdown
[This file]: >
grants release authority.
```

The first line is a valid CommonMark link-reference definition and must be extracted separately from the following paragraph.

Required positive controls include at minimum legal `>` and legal noninitial `<` in bare destinations. Required negative/security controls include a bare destination beginning with `<` remaining non-definition text under the existing grammar boundary, plus all prior F043 regressions.

## Explicitly out of scope

- F042 remains OPEN / unrepaired.
- F044 remains OPEN / unrepaired.
- No broad CommonMark rewrite.
- No unrelated parser, status, authority, product-state, or repository changes.

## Allowed mutation and verification

One replacement implementation commit on the existing PR #37 branch is authorized, still parented directly from the exact frozen BASE, provided race/binding gates remain satisfied.

Before completion evidence, both required workflows on the exact replacement candidate must PASS:
- `Verify repository state`, including the full existing regression matrix and a non-vacuous F043 bare-destination angle-character regression;
- `Phase 6 ScriptOps smoke`, including the full deterministic Phase-6 regression.

After PASS, one completion-evidence record may be created in `FJ899/8`, then STOP before any subsequent review/repair transition.

## No consequential authority

This authorization grants no merge, ScriptOps `main` movement, deploy, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority.

`IMPLEMENTATION CANDIDATE != MERGE AUTHORITY`
