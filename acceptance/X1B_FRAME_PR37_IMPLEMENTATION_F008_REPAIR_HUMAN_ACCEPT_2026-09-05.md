# X1B-FRAME — Human acceptance of PR #212 F008 and bounded PR #37 repair authority

Date: `2026-09-05`

## Human act

Exact Human response:

```text
accept
```

This acceptance binds only to the immediately preceding gate: acceptance of the exact F008 finding frozen in `FJ899/8 PR #212` and authorization for exactly one bounded repair of the existing `FJ899/scriptops PR #37` candidate, exclusively for F008.

## Accepted finding

```text
FJ899/8 PR #212
HEAD = f086c7de76a7d194d2c2344edef5135cdf1d2653
TREE = aa18fce3aa5201e1254c5234371571850c7eba0b
PATH = research/X1B_FRAME_PR37_IMPLEMENTATION_REREVIEW_F008_2026-09-05.md
BLOB = 1ac82dc990d934bd1a6610f5593ab60e1ab9521a
FINDING = X1B-FRAME-F001-IMPLEMENTATION-F008
```

Accepted defect boundary:

```text
R14 is currently a wrong-reason / vacuous negative test.
A correctly fenced Main_Theme document can also assert
GENERIC HUMAN APPROVAL = X1B HumanDecision AUTHORSHIP EVIDENCE
without the implemented verifier rejecting that authorship collapse.
```

## Exact ScriptOps repair target

```text
FJ899/scriptops PR #37
BASE = 2f22843ac570498b506101addeba5453ab777f08
CURRENT FAIL HEAD = a5bc1eb55ef0d3b41814d5ceddaa382f67fa64db
CURRENT FAIL TREE = 544ef3af58393d956569cec1ad6c350ddfb1d3c2
STATE = OPEN / DRAFT / UNMERGED
```

## Authorized repair boundary

Exactly one replacement candidate commit may be prepared on the same frozen base.

Base-relative requirements remain:

```text
commits ahead of base = exactly 1
changed paths = exactly the frozen 12-path PR #201 implementation surface
behind base = 0
```

Relative to the current FAIL HEAD, only this file may change:

```text
scripts/verify_repository.py
```

The repair may do only what is necessary to close F008, including:

1. deterministically rejecting an explicit Main_Theme Human-authorship-promotion assertion equivalent to:

```text
GENERIC HUMAN APPROVAL = X1B HumanDecision AUTHORSHIP EVIDENCE
```

2. making R14 non-vacuous by starting from the real correctly fenced `sources/ScriptOps_Main_Theme_Summary.md`, adding the forbidden authorship-promotion assertion, and requiring failure for the intended Human-authorship-promotion reason rather than for a missing provenance marker;
3. preserving the accepted F007 non-vacuous R12 behavior;
4. preserving the F006 exact legacy/V2 runtime-profile behavior;
5. rerunning the existing repository verifier and Phase-6 regression without editing tests or workflows.

No broader verifier redesign or new implementation surface is authorized.

## No additional authority

This Human act does not authorize:

```text
PR #37 merge
PR #35 merge / rebase / cherry-pick
ScriptOps main movement
deployment / release / tag
canonical effect
active-product status promotion
X1B reopen
V1
```

After repair and CI, the next legal stage is a separately Human-authorized independent read-only re-review of the new exact PR #37 HEAD.

Preserve:

```text
AI PROPOSES != HUMAN DECIDES
REVIEW FINDING != REPAIR AUTHORITY
REPAIR AUTHORITY != MERGE AUTHORITY
GENERIC HUMAN APPROVAL != X1B HumanDecision AUTHORSHIP EVIDENCE
IMPLEMENTATION CANDIDATE != MERGE AUTHORITY
```
