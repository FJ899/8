# X1B-FRAME F028 REPAIR-PLAN REVIEW — F029 — 2026-09-06

## Disposition

**NOT PASS — first credible counterexample. STOP.**

Reviewed solution: F028 repair continuity in PR #295 under Human F028 repair authority PR #294.

Exact pre-repair ScriptOps binding remains:
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `0f7d34476c33fdc0e530f22e3168791c600c17e1`
- OLD TREE `615af6e036dd1f6beaa818713984a2c18b1ee475`
- OLD verifier blob `9292d0e637229c0d87b57519a6a10fd3cb5d8df3`

## Finding

`X1B-FRAME-F001-IMPLEMENTATION-F029` — the proposed F028 current-leaf-only ordered-sibling test mishandles an ordered ancestor sibling after a nested child when there is no intervening blank line.

The PR #295 design says that, for a recognized non-one ordered marker while a list path is active and no blank transition occurred, it is an established ordered-list sibling only when its marker indentation equals the **current leaf** indentation and its ordered delimiter matches the **current leaf** ordered delimiter. Otherwise the line is appended to the current leaf paragraph.

That criterion is too narrow. A non-one ordered marker can validly close one or more nested descendants and become a sibling of an already-established **ancestor** ordered item without a blank line.

Representative structure:

```text
1. Parent context
   - This file contains background notes.
2. grants release authority.
```

Under CommonMark structure, `2.` is a top-level sibling of `1.`; it is not lazy continuation of the nested bullet paragraph. Correct authority-unit treatment must therefore keep the nested child from donating `This file` to the top-level `2.` sibling.

Under the proposed PR #295 rule, the active current leaf is the nested bullet. The incoming non-one ordered marker has a different indentation and an ordered signature that cannot match the bullet current leaf, so the rule's `otherwise` branch appends the physical `2.` line to that leaf. The verifier would then synthesize an authority unit equivalent to `This file ... grants release authority`, producing a false self-promotion rejection from text that Markdown keeps in separate list items.

This is security-relevant because the verifier's authority boundary is intended to follow Markdown container structure in both directions: it must not split one claim into multiple units, and it must not combine structurally distinct siblings so one unit donates a self-reference to another.

## Required repair direction, not authority

A future repair should resolve a non-one ordered marker against the active list path, not only the current leaf. Before treating the marker as lazy continuation, it must determine whether dedenting the marker reaches an already-established ordered ancestor at the same marker indentation with a compatible delimiter; if so, the marker is an ancestor-level sibling boundary. Only when no valid established-list sibling exists at the resolved container depth should the non-interrupting marker be folded into the currently open paragraph.

Regression coverage should include at least:
- ordered ancestor -> nested bullet -> dedented non-one ordered ancestor sibling without a blank line;
- deeper nested variants;
- same-level established ordered siblings;
- the original F028 lazy-continuation cases.

## Boundary

This finding authorizes no repair. No ScriptOps PR #37 mutation, merge, main movement, PR #35 integration, deployment, release, tag, canonical effect, status promotion, X1B reopen or V1 authority is granted.
