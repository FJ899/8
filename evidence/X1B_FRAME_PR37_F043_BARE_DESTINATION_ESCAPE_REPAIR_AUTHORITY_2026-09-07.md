# X1B-FRAME — Human authority for F043 bare-destination escape bounded repair

Date: 2026-09-07

Human authorization: `accept`

This record authorizes exactly one bounded verifier-only repair of the F043 single-line bare-destination backslash-escape defect recorded in `FJ899/8 PR #387`.

Exact ScriptOps target:

- repository: `FJ899/scriptops`
- PR: `#37`
- state at authorization: open / draft / unmerged
- base branch: `main`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `9ef034b8cb87500d2c160c88ab04c36f39ac417b`
- TREE: `25fcee396a9ee81a25837863e2dfc3f124506e5f`
- verifier entrypoint blob: `277eb91bbcf46dfb766e39ed23962b5179450c87`
- pinned F043 list-lazy overlay: `040365f5825c386b1e74405ca51c63edd2ca55ac`
- pinned F043 multiline overlay: `c2b5a356e744be802d204ab8eaea901e76aa1219`
- pinned F043 single-line overlay: `61bf107ad59da33a6576032d341b41c538d0453a`
- pinned F041 core: `be645c1a3ee49a04d700a3ef7fde86a92e413a14`

Authorized repair boundary:

1. Repair only CommonMark backslash handling inside a bare link destination used by F043 link-reference-definition recognition.
2. Backslash may suppress syntax only when escaping ASCII punctuation; it must not mask whitespace or other non-punctuation characters.
3. Preserve valid escaped punctuation, valid literal backslashes before non-punctuation characters, all prior F043 single-line/multiline/list-lazy/destination-newline behavior, and the rule that a definition cannot interrupt an already-open paragraph.
4. Preserve F042 and F044 as `OPEN / UNREPAIRED`.
5. Use one replacement commit over the exact frozen BASE and run the complete prior verifier matrix plus a new focused F043 regression matrix.
6. Require both `Verify repository state` and `Phase 6 ScriptOps smoke` to pass before completion evidence may be recorded.
7. Stop on any credible failure.

Not authorized:

- repair of F042 or F044;
- merge or ScriptOps `main` movement;
- deploy, release, tag;
- canonical effect or active-product status promotion;
- X1B reopen or V1 authority.

`IMPLEMENTATION CANDIDATE != MERGE AUTHORITY`
