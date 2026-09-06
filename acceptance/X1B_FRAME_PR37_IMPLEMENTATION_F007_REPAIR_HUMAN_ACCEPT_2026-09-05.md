# X1B-FRAME — Human acceptance of PR #209 F007 and bounded PR #37 repair authority

Date: `2026-09-05`

## Human act

Exact Human response:

```text
accept
```

The response is bound only to the immediately preceding gate.

## Accepted finding

```text
FJ899/8 PR #209
HEAD = 49700d9f6423b5eb5ae2fe4f805c59bce1f8293e
TREE = 4479f83c14a7207a5388bd5487aaddaa7b1acda6
PATH = research/X1B_FRAME_PR37_IMPLEMENTATION_REREVIEW_F007_2026-09-05.md
BLOB = cbe311a9d7ea4940bf8d7d78bd07e5653a1d7962
FINDING = X1B-FRAME-F001-IMPLEMENTATION-F007
```

Accepted defect:

```text
R12 IS A FALSE-NEGATIVE TEST:
SOURCES.md CAN RETAIN THE REQUIRED HISTORICAL ACCESS-CHECK FENCE
AND SIMULTANEOUSLY REASSERT "ACCESS CHECK REQUIRED = CURRENT NEXT",
WHILE THE IMPLEMENTED VERIFIER ACCEPTS IT.
```

## Exact repair authority

Human authorizes exactly one bounded repair of the existing ScriptOps implementation candidate:

```text
FJ899/scriptops PR #37
BASE = 2f22843ac570498b506101addeba5453ab777f08
OLD REVIEWED-FAIL HEAD = 0cb507e1e26ad6a9e13c8098c522301d3e0cf0e6
OLD TREE = b17d5d4addcc193f4e963ea5a9c7064a6b0af870
```

Repair scope is exclusively `X1B-FRAME-F001-IMPLEMENTATION-F007`.

The repair may replace the PR #37 candidate commit so that PR #37 remains exactly one commit ahead of the same frozen base. The branch ref may be moved to that replacement commit solely for this repair.

Base-relative changed paths must remain exactly the frozen twelve paths from PR #201:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
DECISION_LOG.md
SOURCE_MANIFEST.md
SOURCES.md
SOURCE_AUDIT_SUMMARY.md
RECONSTRUCTION_REPORT.md
sources/Decision_Summary_Current_State.md
sources/RC1_SCOPE_LOCK.md
sources/ScriptOps_Main_Theme_Summary.md
scripts/verify_repository.py
```

Because F007 is a verifier false-negative / wrong-reason regression, the repair itself is narrowed further:

```text
relative to old PR #37 HEAD 0cb507e1..., only scripts/verify_repository.py may change
```

The repaired verifier must reject a `SOURCES.md` that retains every required provenance fence while also asserting stale current-next authority. At minimum the deterministic R12 regression must exercise:

```text
all required SOURCES provenance markers retained
+
ACCESS CHECK REQUIRED = CURRENT NEXT
=> FAIL because current-next authority is forbidden
```

The repair must not make the test pass merely because a required fence marker is absent. Existing F006 runtime-profile semantics must remain intact.

The repaired candidate must rerun existing repository verification and Phase-6 regression CI without modifying runtime, tests or workflows in PR #37.

## Explicit non-authority

This Human act does **not** authorize:

```text
merge of PR #37
merge/rebase/cherry-pick of PR #35
FJ899/scriptops main movement
deployment / release / tag
canonical screenplay effect
active-product status promotion
X1B reopen
V1 action
any repair outside F007
any ScriptOps path outside the frozen twelve-path candidate surface
```

Preserve:

```text
AI PROPOSES != HUMAN DECIDES
REVIEW FINDING != REPAIR AUTHORITY
GREEN NEGATIVE TEST != PROPERTY PROOF WHEN FAILURE REASON IS WRONG
IMPLEMENTATION CANDIDATE != MERGE AUTHORITY
CURRENTNESS_UNESTABLISHED != FALSE
CURRENTNESS_UNESTABLISHED != TRUE
```