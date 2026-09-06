# X1B-FRAME PR37 F041 validated patch — pre-apply evidence

Date: 2026-09-06
Status: PRE-APPLY / NO SCRIPTOPS MUTATION

Target binding:
- `FJ899/scriptops PR #37`
- exact input HEAD `a504b33e0420d3ac487a1d69aeddebc6719dcd62`
- exact input TREE `590da6890ba88334aeec59a908eacb52adbade5c`
- exact verifier blob `b4df7351df142d20507aab2eff4ae2991ddc9acb`
- frozen BASE `2f22843ac570498b506101addeba5453ab777f08`
- finding `FJ899/8 PR #366`
- Human repair authority `FJ899/8 PR #367`
- preservation/design audit `FJ899/8 PR #368`

Prepared patch artifact:
- filename `X1B_FRAME_PR37_F041_REPAIR.patch`
- SHA-256 `dd65d9c38de14dd1d6f630260d748bfd8bdb623009f12fa70f6becb56d28f91c`
- parsed numstat `63  1  scripts/verify_repository.py`
- intended surface: only `scripts/verify_repository.py`

Patch mechanics:
- add F041 repair note;
- add top-level `block_quote_indented_code` state;
- reset that state when the current top-level quote leaf is flushed;
- while quoted code is active, keep explicit blank or >=4-column quoted content in the same literal leaf;
- on first explicit nonblank quoted dedent, flush the code leaf and start a new quoted leaf from the same line;
- preserve four-plus indentation as paragraph continuation when a quoted paragraph is already open;
- preserve list-owned quote/list-item semantics;
- add focused F041 benign/reject regressions and a PASS marker.

Pre-apply checks performed on an exact-context synthetic target:
- unified patch parses: PASS;
- `git apply --check`: PASS;
- `git apply --numstat`: `63  1  scripts/verify_repository.py`;
- post-apply `git diff --check`: PASS;
- focused quoted-code state harness: PASS for representative F041 split, same-code payload, blank quoted code chunk, open-paragraph non-interruption, and dedent-then-lazy behavior.

Mandatory checks still pending and must run on the real exact ScriptOps worktree before any amend/push:
1. patch SHA check;
2. real `git apply --check`;
3. verifier-only changed-file proof;
4. Python compile;
5. full `scripts/verify_repository.py` PASS including F041 and all prior regressions;
6. replacement one-commit topology proof;
7. guarded force-with-lease push;
8. both required remote workflows PASS on exact replacement HEAD;
9. completion evidence freeze.

This evidence does not authorize merge, ScriptOps main movement, deploy, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority.
