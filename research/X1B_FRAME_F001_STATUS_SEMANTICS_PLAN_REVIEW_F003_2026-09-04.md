# X1B-FRAME F001 — Status-Semantics Plan Review — First Finding F003

Status: `PLAN REVIEW FAIL / FIRST CREDIBLE COUNTEREXAMPLE / STOP / NO PLAN-REPAIR AUTHORITY`

Date: `2026-09-04`

## 1. Exact review target and authority

Human-authorized review target:

```text
FJ899/8 PR #192
HEAD = bff112dd61b67d2c3e18c3194cba12072d2cfd6a
TREE = 42ca9e5532abe935977ce58c5a15ec828ea17a97
PATH = research/X1B_FRAME_F001_SUPERSEDING_STATUS_SEMANTICS_PLAN_REOPEN_PLAN_F002_2026-09-04.md
BLOB = ab975e1b9656315e506dc95615472113c649c55d
```

The immediately preceding Human response was:

```text
accept
```

bound only to one independent read-only review of the exact PR #192 plan.

Accepted evidence-repository review anchor:

```text
FJ899/8 refs/heads/main
HEAD = 0b516edb210fd4029972e932fec0206d8a6df1cb
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

Independently re-read ScriptOps active default branch:

```text
FJ899/scriptops refs/heads/main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
```

Review rule:

```text
FIRST CREDIBLE COUNTEREXAMPLE = DURABLE FINDING + STOP
```

## 2. First credible counterexample

```text
X1B-FRAME-F001-PLAN-F003 — THE PLAN'S AUTHORITATIVE-SURFACE SET IS INCOMPLETE:
A CANDIDATE CAN SATISFY C1-C21 WHILE THE README-ORDERED ZERO-HISTORY STARTUP
STILL CONSUMES UNCHANGED FILES THAT DECLARE CURRENT/CANONICAL AUTHORITY AND
RETAIN PRE-X1B HUMAN-APPROVAL SEMANTICS.
```

Primary classification:

```text
AUTHORITATIVE-SURFACE SET UNDER-SPECIFIED
STARTUP / RECOVERY STATUS DRIFT
```

Preregistered review class reached by the finding:

```text
P7 — can historical approve / Human-approval semantics leak back into current X1B authority?
```

The review stops here. No later P1-P10 discovery is claimed.

## 3. Why the four-path plan is insufficient as written

PR #192 freezes the future ScriptOps correction surface to exactly:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
scripts/verify_repository.py
```

and explicitly forbids all other ScriptOps path changes.

The plan then treats the first three documents as the authoritative current-state surfaces and makes C6-C18 reason only over those surfaces plus the local verifier.

However, the actual active `README.md` recovery contract instructs a zero-history AI to continue reading beyond those three files.

Current `README.md` at active main `2f22843...` contains:

```text
## Uruchomienie nowej sesji

1. README.md
2. PROJECT_STATE.md
3. HANDOFF.md
4. DECISION_LOG.md
...
9. SOURCE_MANIFEST.md
10. RECONSTRUCTION_REPORT.md
```

Therefore `SOURCE_MANIFEST.md` and `RECONSTRUCTION_REPORT.md` are not merely dormant history. They are explicitly in the current startup path unless the correction contract requires their removal or reclassification from that path.

PR #192 does not require that.

## 4. Unchanged SOURCE_MANIFEST retains current/canonical authority labels

At active ScriptOps main:

```text
SOURCE_MANIFEST.md
BLOB = 2acf2ece298bfcf89254087c9e747fcb808ab241
```

It states:

```text
Repo contains the minimal package needed to resume and continue work without earlier chat.
```

and has a section equivalent to:

```text
Canonical operational sources
```

It also labels:

```text
sources/Decision_Summary_Current_State.md
```

as the current product-decision summary.

Thus, after a future four-path correction candidate, a zero-history reader may receive:

```text
README / PROJECT_STATE / HANDOFF
=> new X1B frame semantics

then

SOURCE_MANIFEST
=> another file is still presented as current product-decision summary
```

without any plan-level rule that reconciles or de-authorizes that second current-looking surface.

## 5. The referenced current-decision summary retains the old Human-approval frame

At active main:

```text
sources/Decision_Summary_Current_State.md
BLOB = 9aea3d7e8de5dde8025278adca0546324d21dd00
```

It is headed:

```text
Current Decision Summary
```

and includes the policy:

```text
Agent may create candidates.
Agent may not approve, commit, edit canon, or change rules without human approval.
```

That statement is historical/generic Human-approval governance. It does not carry the X1B V2 authorship boundary that the corrected current surfaces are supposed to establish:

```text
generic Human approval
!=
separate trusted HumanDecision evidence bound to exact content/scope/candidate/effect
```

Because `SOURCE_MANIFEST.md` still calls this a current product-decision summary, the stale wording cannot safely be assumed to be self-demoted history.

## 6. RECONSTRUCTION_REPORT is also in the active startup list

At active main:

```text
RECONSTRUCTION_REPORT.md
BLOB = 383354c61c707ed4a1210f60f03125fca4daae8a
```

It describes the governing flow as:

```text
AI candidate
-> validation
-> impact report
-> human decision
-> reason
-> commit
```

and states the product rule equivalently as:

```text
an AI answer becomes truth after validation, Human approval, recorded reason and repository commit
```

It later identifies an old ACCESS CHECK as the next step.

The document does say `PROJECT_STATE.md` is the current owner, but README still orders the zero-history session to consume this report as part of startup, and PR #192 has no deterministic rule requiring the report to be removed from current startup or explicitly fenced as non-authoritative for X1B HumanDecision semantics.

## 7. Minimal passing-candidate counterexample

Consider a future implementation candidate that does exactly what PR #192 requires:

```text
1. changes only README.md, PROJECT_STATE.md, HANDOFF.md and scripts/verify_repository.py;
2. publishes CURRENTNESS_UNESTABLISHED in all three selected surfaces;
3. rejects YES/NO collapse;
4. marks legacy approve --why non-X1B-authoritative in those three surfaces;
5. passes local runtime classification and all C1-C21 checks;
6. leaves the rest of the repository unchanged, as required by the four-path freeze.
```

Now leave the existing README startup list structurally intact except for adding the required new X1B frame block.

This implementation still satisfies the explicit acceptance checks in section 17 of PR #192: none of C1-C21 requires removal of `SOURCE_MANIFEST.md` / `RECONSTRUCTION_REPORT.md` from startup, reclassification of `sources/Decision_Summary_Current_State.md`, or a verifier assertion that all README-ordered recovery surfaces defer to the new X1B authority model.

A zero-history session then legally follows README and reads:

```text
corrected X1B current-state block
then
unchanged SOURCE_MANIFEST declaring additional current/canonical sources
then
unchanged Current Decision Summary with generic Human-approval semantics
then
unchanged reconstruction guidance
```

The candidate can therefore be `PASS` under C1-C21 while the original frame ambiguity remains recoverable from the repository's own startup contract.

That is a plan-level counterexample, not an implementation-quality nit.

## 8. Why corrected-first ordering does not cure it

It is not enough that README, PROJECT_STATE and HANDOFF are read first.

The defect being corrected is a frame/authority ambiguity. A later startup document explicitly labelled `current`, `canonical`, or `current decision summary` can re-open that ambiguity unless one of the following is frozen by the plan:

```text
A. it is removed from the current startup/recovery path;
B. it is explicitly reclassified as historical/non-authoritative for X1B;
C. its relevant stale semantics are corrected;
D. the verifier proves that every README-ordered current/recovery surface defers to the new X1B frame.
```

PR #192 requires none of A-D for these unchanged paths.

The review does not choose among A-D; choosing a repair is outside review authority.

## 9. Relationship to PLAN-F002

PR #192 materially improves the prior boolean model:

```text
CURRENTNESS_UNESTABLISHED != CONFIRMED_NOT_REMEDIATED
CURRENTNESS_UNESTABLISHED != CONFIRMED_REMEDIATED
```

No counterexample was found to that three-state distinction before this finding.

The blocker is orthogonal: the new semantics are not yet guaranteed to dominate the complete current startup/recovery authority surface.

Therefore:

```text
PLAN-F002 SEMANTIC REPAIR = NOT REJECTED BY THIS FINDING
PR #192 AS A COMPLETE EXECUTABLE PLAN = NOT PASS
```

## 10. Scope classification

This is not a claim that X1B runtime/security closure is false.

```text
X1B PROPERTY FALSIFIED = NO
X1B CLOSURE REOPENED = NO
```

It is a status/frame correction-plan defect: the frozen path set and acceptance checks do not cover all files that the repository itself currently puts into the zero-history recovery chain with current/canonical authority language.

No runtime remediation, merge, deployment, V1 action or canonical effect follows from this finding.

## 11. Review disposition

```text
X1B-FRAME F001 STATUS-SEMANTICS PLAN REVIEW = FAIL
X1B-FRAME-F001-PLAN-F003 = OPEN
FIRST CREDIBLE COUNTEREXAMPLE = STOP
PR #192 = NOT PASS
SCRIPTOPS IMPLEMENTATION AUTHORITY = NO
PR #35 MERGE AUTHORITY = NO
DEPLOYMENT / RELEASE / TAG = NO
V1 AUTHORITY = NO
X1B = REMAINS CLOSED AT ACCEPTED RESEARCH/CORRECTIVE SCOPE
```

No plan repair is performed in this review.

Next legal stage is a separate Human disposition of this exact finding. Only after acceptance may a bounded plan repair be prepared, including any Human-approved decision about whether the authoritative surface set itself must expand or whether the current recovery route must instead be narrowed.

Preserve:

```text
CURRENTNESS_UNESTABLISHED != FALSE
CURRENTNESS_UNESTABLISHED != TRUE
CURRENT-LOOKING RECOVERY SOURCE != HISTORICAL BY ASSUMPTION
PLAN REVIEW FINDING != PLAN-REPAIR AUTHORITY
PLAN REVIEW PASS != IMPLEMENTATION AUTHORITY
AI PROPOSES != HUMAN DECIDES
```