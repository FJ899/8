# X1B-FRAME PR #37 F044-D26 repair completion

Disposition: **REPAIRED / GREEN**

Exact final implementation binding:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `ee0317c5b73e84c25823dad2bc4232fff22c5abd`
- TREE: `83db57184224392cc359b537f291ac1a2d1723c7`
- verifier entrypoint blob: `ea830bc54b9c6bc4f07905fd964539885de841c6`
- previous GREEN D25 entrypoint blob: `df2f7dcc4e2a8406c7c6b8dbae81c30676979849`
- exactly one replacement commit over fixed BASE
- 59 changed paths

Finding provenance: `FJ899/8 PR #483`.

Non-vacuity probe: `FJ899/scriptops PR #57`, closed without merge after Verify run `34262495200` explicitly printed `[PASS] F044-D26 probe reproduces list-owned post-target-continuation false positive`; smoke run `34262494937` completed/success.

Repair validation probe: `FJ899/scriptops PR #58`, HEAD `250556ec0ce89fcf301ebe40286625fcf3404c54`, identical repair TREE `83db57184224392cc359b537f291ac1a2d1723c7`, verifier blob `ea830bc54b9c6bc4f07905fd964539885de841c6`; closed without merge after Verify run `34262705775` and smoke run `34262705763` both completed/success.

Final candidate verification:

- Verify repository state run `34262783745`: completed/success and explicitly PASSes all prior regressions plus `F044-D26 list-owned post-target-child continuation regression`.
- Phase 6 ScriptOps smoke run `34262783747`: completed/success; repository semantic/currentness verifier and full deterministic Phase-6 regression both passed.

D26 repairs only the list-owned lift of D15 inside one source-column-zero outer list item: one quoted parent list item, at least two one-line preceding children, one target child at position three or later with one-or-more ordinary continuation lines, exactly one post-target child at the same child-marker indentation with its own one-or-more ordinary continuation lines, and exactly one final sibling. Outer-list and quoted-parent context are preserved in every child authority unit; each preceding child is separate, target keeps its continuation run, the post-target child keeps its own continuation run, and the final sibling is separate.

Marker-only post-target sibling cardinality remains delegated to D25. Continuation in preceding/final children, more post-target children, multiple final siblings, deeper nesting, block transitions, multiple quoted parents, outer-list siblings, nested outer lists and further list-owned quote recursion remain outside D26.

No merge, ScriptOps main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is authorized or recorded by this completion evidence.
