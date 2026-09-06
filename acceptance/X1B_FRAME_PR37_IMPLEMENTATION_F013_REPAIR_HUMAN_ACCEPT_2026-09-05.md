# X1B-FRAME PR37 F013 — Human Acceptance and Bounded Repair Authority

Date: 2026-09-05

Status: `HUMAN ACCEPTED / EXACTLY ONE BOUNDED REPAIR AUTHORIZED`

## Human response

```text
accept
```

## Accepted finding

```text
FJ899/8 PR #225
FINDING = X1B-FRAME-F001-IMPLEMENTATION-F013
CLASS = COMMA/ASYNDETIC CLAUSE-BOUNDARY NEGATION MASKING / LAYER-B SELF-PROMOTION FALSE NEGATIVE
```

The accepted finding is that a comma-separated/asydetic later positive authority clause can remain inside an earlier negation segment, allowing a Layer-B document to self-promote despite path-class denial.

Representative counterexample:

```text
This document does not grant release authority, it hereby authorizes merge.
```

## Exact pre-repair ScriptOps target

```text
FJ899/scriptops PR #37
BASE = 2f22843ac570498b506101addeba5453ab777f08
HEAD = 115fb74607438c7237c33f413981678de4a55b01
TREE = 3d1a1e778672fc9547ec4563cf8e03055061d2a3
STATE = OPEN / DRAFT / UNMERGED
COMMITS AHEAD = 1
CHANGED PATHS = 12
```

## Repair authority

Human authorizes exactly one bounded replacement repair of existing `FJ899/scriptops PR #37`, exclusively for F013.

Mandatory boundaries:

```text
replacement candidate remains exactly one commit over frozen BASE
base-relative changed paths remain exactly the frozen twelve-path surface
relative to pre-repair HEAD, only scripts/verify_repository.py may change
no runtime/test/workflow/restore/evidence/acceptance path changes
```

The repair must prevent an earlier local negation from masking a later positive Layer-B self-promotion across comma/asydetic clause boundaries, while preserving valid local negation and all accepted/regression behavior for F012, F011, F010, F009, F008, F007 and F006.

The repair must not merely special-case the representative sentence.

After repair, ordinary candidate verification/CI may run. A new independent read-only re-review requires a separate Human gate.

## No-effect boundary

This authority does not authorize:

```text
merge
ScriptOps main movement
PR #35 integration/rebase/cherry-pick
deployment
release
tag
canonical effect
active-product status promotion
X1B reopen
V1 authority
```

Preserve:

```text
AI PROPOSES != HUMAN DECIDES
IMPLEMENTATION CANDIDATE != MERGE AUTHORITY
PR HEAD != ACTIVE DEFAULT BRANCH
CHECKED_OUT_RUNTIME_CLASS != ACTIVE_PRODUCT_STATE
CURRENTNESS_UNESTABLISHED != FALSE
CURRENTNESS_UNESTABLISHED != TRUE
```
