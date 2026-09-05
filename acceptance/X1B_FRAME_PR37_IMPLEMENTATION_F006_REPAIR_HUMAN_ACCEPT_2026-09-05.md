# X1B-FRAME — Human acceptance of PR #206 F006 and bounded PR #37 repair authority

Date: `2026-09-05`

## Human act

Exact Human response:

```text
accept
```

The response is bound only to the immediately preceding gate.

## Accepted finding

```text
FJ899/8 PR #206
HEAD = 1293fa9b963b6a9a08bd72f73afdf71ffba92aff
TREE = 55ba0c62664a66fde8f9d27b6629c3117b7dd232
PATH = research/X1B_FRAME_PR37_IMPLEMENTATION_REVIEW_F006_2026-09-05.md
BLOB = 5417aa5918262a38a828501267fe46ab5f77f424
FINDING = X1B-FRAME-F001-IMPLEMENTATION-F006
```

Accepted defect:

```text
REAL V2 CHECKOUT IS REJECTED BY THE IMPLEMENTED VERIFIER
DESPITE THE FROZEN PLAN REQUIRING
X1B_V2_CHECKOUT + CURRENTNESS_UNESTABLISHED = PASS
```

## Exact repair authority

Human authorizes exactly one bounded repair of the existing ScriptOps implementation candidate:

```text
FJ899/scriptops PR #37
BASE = 2f22843ac570498b506101addeba5453ab777f08
OLD REVIEWED-FAIL HEAD = ac061227fada7995490675f5413bce3d44ef516a
OLD TREE = 732a8cc084f4c5a527d9ae00800bf644b85c932f
```

Repair scope is exclusively `X1B-FRAME-F001-IMPLEMENTATION-F006`.

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

Because F006 is a verifier/transition-state contradiction, the repair itself is narrowed further:

```text
relative to old PR #37 HEAD ac061227..., only scripts/verify_repository.py may change
```

The repaired verifier must preserve all existing frame/status semantics and must make both recognized runtime transition rows executable through the real verifier path:

```text
LEGACY_PRE_X1B + CURRENTNESS_UNESTABLISHED = PASS
X1B_V2_CHECKOUT + CURRENTNESS_UNESTABLISHED = PASS
UNKNOWN + CURRENTNESS_UNESTABLISHED = FAIL
```

Neither recognized local runtime class may establish `CONFIRMED_REMEDIATED`, `CONFIRMED_NOT_REMEDIATED`, YES/NO, TRUE/FALSE, deployment, merge, release, tag, canonical-effect or V1 authority.

The repair must add/retain deterministic regression coverage proving the V2 positive transition row through the same runtime-profile validation path used by repository verification, not merely through a weaker classifier helper.

The repaired candidate must rerun the existing ScriptOps repository verification and Phase-6 regression CI without modifying runtime, tests or workflows in PR #37.

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
any repair outside F006
any ScriptOps path outside the frozen twelve-path candidate surface
```

Preserve:

```text
AI PROPOSES != HUMAN DECIDES
REVIEW FINDING != REPAIR AUTHORITY
IMPLEMENTATION CANDIDATE != MERGE AUTHORITY
CHECKED_OUT_RUNTIME_CLASS != ACTIVE_PRODUCT_STATE
CURRENTNESS_UNESTABLISHED != FALSE
CURRENTNESS_UNESTABLISHED != TRUE
```
