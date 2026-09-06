# X1B-FRAME — F022 repair patch continuity

Continuity record under the already Human-authorized F022 repair (`FJ899/8 PR #263`).

Exact ScriptOps pre-repair target:
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `33b6691cdebb4a5ba07d38a492976cc84230fecb`
- OLD TREE `af96d8bbdcdc5b579a438c945ded90061890a07d`
- OLD verifier blob `0a468ba609df2a3484e2fbdea57b2f7d07e7c591`

Prepared artifact:
- `X1B_FRAME_PR37_F022_REPAIR.patch`
- bytes `5017`
- SHA-256 `99f1023f6363954af53b6075c57e4393f87d4deae9b903ef4401f4c43699973e`

Bounded design:
- changes only `scripts/verify_repository.py` relative to OLD HEAD;
- after a blank line, resolve indentation ownership against active list frames before deep-marker recognition;
- if the line leaves the current leaf, emit that path and pop to the nearest owning ancestor (or ordinary paragraph) before deciding whether a 4+ column marker is a nested list item;
- preserves valid deep descendants, deep siblings, and same-item continuations;
- adds F022 benign wide-ordered-item/four-space-block regression plus positive valid-descendant and same-item-continuation controls;
- preserves F021-F006 behavior by scope.

Validation performed before handoff:
- parser matrix covering F019-F022 passed;
- generated patch passed `git apply --check` and `git diff --check` on an exact-context mock carrying the frozen verifier hunk contexts.

This is continuity/evidence only. It grants no new authority and no post-repair independent review authority.
