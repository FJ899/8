# X1B-FRAME F001 — Recovery-Authority Plan Review — First Finding F004

Status: `PLAN REVIEW FAIL / FIRST CREDIBLE COUNTEREXAMPLE / STOP / NO PLAN-REPAIR AUTHORITY`

Date: `2026-09-05`

## 1. Exact review target and authority

Human-authorized review target:

```text
FJ899/8 PR #195
HEAD = 208208764ca557da04dcd9cd0b6c48f2eb6d41a6
TREE = fbf0499995af4c2f68ab39d432f736024d19cde2
PATH = research/X1B_FRAME_F001_SUPERSEDING_RECOVERY_AUTHORITY_PLAN_REOPEN_PLAN_F003_2026-09-04.md
BLOB = 93caa5cacd5945524a571881a544184a48204d40
```

The immediately preceding Human response was exactly:

```text
accept
```

and was bound only to one independent read-only review of that exact PR #195 plan.

Review anchors independently re-read before freezing this finding:

```text
FJ899/8 refs/heads/main
HEAD = 0b516edb210fd4029972e932fec0206d8a6df1cb

FJ899/scriptops refs/heads/main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
```

Review rule:

```text
FIRST CREDIBLE COUNTEREXAMPLE = DURABLE FINDING + STOP
```

## 2. First credible counterexample

```text
X1B-FRAME-F001-PLAN-F004 — THE PLAN'S SEVEN-PATH AUTHORITY SURFACE IS STILL
INCOMPLETE: ROOT-LEVEL SOURCES.md REMAINS OUTSIDE THE FROZEN CORRECTION SET
WHILE SELF-LABELLING SOURCE_MANIFEST.md AS THE CANONICAL SOURCE INDEX,
sources/Decision_Summary_Current_State.md AS CURRENT PRODUCT-DECISION CONTENT,
AND ACCESS CHECK REQUIRED AS AN "AKTUALNA LUKA" / CURRENT PROJECT-STATE GAP.
A CANDIDATE CAN SATISFY C1-C30 WHILE THIS UNFENCED SUPPORTING-PROVENANCE FILE
REINTRODUCES THE SAME CURRENT/CANONICAL/NEXT-STEP AUTHORITY AMBIGUITY.
```

Primary classification:

```text
AUTHORITATIVE-SURFACE SET STILL UNDER-SPECIFIED
SUPPORTING-PROVENANCE SELF-PROMOTION
```

Preregistered review classes reached:

```text
Q1 — can any file outside README/PROJECT_STATE/HANDOFF still self-promote into current X1B authority?
Q9 — does the exact seven-path set cover every concrete current/canonical surface without unnecessary runtime expansion?
```

The review stops at this first credible counterexample. No later Q1-Q12 discovery is claimed.

## 3. Frozen plan boundary that creates the gap

PR #195 freezes the future ScriptOps correction surface to exactly seven paths:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
SOURCE_MANIFEST.md
sources/Decision_Summary_Current_State.md
RECONSTRUCTION_REPORT.md
scripts/verify_repository.py
```

and forbids every other ScriptOps path from changing.

The same plan states that after current-state recovery is established, supporting provenance may still be loaded as required by the bounded handoff/task, while preserving:

```text
READ LATER != AUTHORITATIVE LATER
STALE SELF-LABEL != CURRENT AUTHORITY
```

It also requires explicit in-file historical/non-current fences for the three PLAN-F003 files because relying on ordering alone is insufficient.

## 4. Concrete omitted current/canonical-looking surface: SOURCES.md

At the frozen ScriptOps baseline:

```text
FJ899/scriptops
REF = refs/heads/main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
PATH = SOURCES.md
BLOB = 28c3f6d8fa9142b41721c8835f211f52cc3fa8bf
```

`SOURCES.md` is a root-level source/recovery document and is outside the seven-path correction set.

It states, in substance and with those current/canonical labels:

```text
Kanoniczny wykaz źródeł ... znajduje się w SOURCE_MANIFEST.md.
```

It also says that the repository contains:

```text
aktualne podsumowanie decyzji produktu
```

which refers to the still-named:

```text
sources/Decision_Summary_Current_State.md
```

And under:

```text
## Aktualna luka
```

it says that the missing later RC1 implementation / Codex answer is:

```text
ACCESS CHECK REQUIRED
```

and characterizes that as a project-state gap rather than merely historical reconstruction provenance.

Thus the plan reclassifies `SOURCE_MANIFEST.md`, `sources/Decision_Summary_Current_State.md` and `RECONSTRUCTION_REPORT.md` in place, while leaving an adjacent root-level source guide unchanged that reasserts the old canonical/current interpretation of two of those files and an old current gap/next-action frame.

## 5. Minimal passing-candidate counterexample

Consider a future implementation candidate that satisfies PR #195 exactly:

```text
1. base = 2f22843ac570498b506101addeba5453ab777f08;
2. exactly one commit ahead;
3. changes exactly the seven frozen paths;
4. narrows mandatory current bootstrap to README -> PROJECT_STATE -> HANDOFF;
5. publishes CURRENTNESS_UNESTABLISHED in the current trio;
6. reclassifies SOURCE_MANIFEST, Decision_Summary and RECONSTRUCTION_REPORT;
7. implements the required verifier checks and R1-R16 synthetic failures;
8. leaves SOURCES.md unchanged, as the exact seven-path freeze requires.
```

That candidate can satisfy every explicit C1-C30 acceptance check because none requires `SOURCES.md` to be reclassified, removed, rewritten or checked by the verifier.

After current bootstrap, a bounded task may legally load supporting provenance. If it loads root `SOURCES.md`, it encounters an unfenced source guide that still says:

```text
SOURCE_MANIFEST = canonical source index
Decision_Summary_Current_State = current product-decision summary
ACCESS CHECK REQUIRED = current gap
```

while the corrected files themselves say they are historical/non-current provenance.

The repository therefore contains two incompatible authority frames for the same supporting material, and the offline verifier required by PR #195 has no frozen rejection path for that conflict.

## 6. Why the general precedence sentence is not sufficient here

PR #195 correctly adds a general rule that supporting/historical material cannot override the current authority trio.

But PLAN-F003 was specifically about current/canonical self-labelling surviving into recovery. PR #195 therefore also chose explicit in-file reclassification of concrete stale surfaces to avoid relying on ordering or reader discipline alone.

`SOURCES.md` is another concrete stale source/recovery surface of the same class:

```text
root-level recovery/source guide
+ explicit "canonical" label
+ explicit "current product-decision summary" label
+ explicit "current gap" / ACCESS CHECK label
```

Leaving it unfenced means the plan does not actually establish its own stronger property:

```text
NO OTHER FILE MAY SELF-PROMOTE INTO CURRENT AUTHORITY THROUGH STALE PROSE
```

The conflict is not cured merely by reading the corrected trio first; it remains present in repository semantics and is invisible to the proposed deterministic verifier.

## 7. Relationship to prior findings

This finding does not reject the PLAN-F002 three-state repair:

```text
CURRENTNESS_UNESTABLISHED != CONFIRMED_NOT_REMEDIATED
CURRENTNESS_UNESTABLISHED != CONFIRMED_REMEDIATED
```

It also does not reject the PLAN-F003 strategy of narrowing the mandatory bootstrap and explicitly fencing stale supporting sources.

The blocker is narrower:

```text
PR #195 DOES NOT YET COVER THE COMPLETE CONCRETE SUPPORTING-PROVENANCE
SELF-PROMOTION SURFACE NECESSARY FOR ITS OWN Q1/Q9 CLAIM.
```

## 8. Scope classification

This is a plan-level frame/status/recovery-authority finding only.

```text
X1B PROPERTY FALSIFIED = NO
X1B CLOSURE REOPENED = NO
RUNTIME REMEDIATION FINDING = NO
```

No ScriptOps runtime change, PR #35 merge/rebase, deployment, release, tag, canonical effect or V1 action follows from this review.

## 9. Review disposition

```text
X1B-FRAME F001 RECOVERY-AUTHORITY PLAN REVIEW = FAIL
X1B-FRAME-F001-PLAN-F004 = OPEN
FIRST CREDIBLE COUNTEREXAMPLE = STOP
PR #195 = NOT PASS
SCRIPTOPS IMPLEMENTATION AUTHORITY = NO
PR #35 MERGE AUTHORITY = NO
DEPLOYMENT / RELEASE / TAG = NO
V1 AUTHORITY = NO
X1B = REMAINS CLOSED AT ACCEPTED RESEARCH/CORRECTIVE SCOPE
```

No plan repair is performed in this review.

The next legal stage is a separate Human disposition of this exact finding. Only after acceptance may one bounded superseding plan repair be prepared.

Preserve:

```text
CURRENTNESS_UNESTABLISHED != FALSE
CURRENTNESS_UNESTABLISHED != TRUE
CURRENT-LOOKING RECOVERY SOURCE != CURRENT AUTHORITY BY SELF-LABEL
READ LATER != AUTHORITATIVE LATER
PLAN REVIEW FINDING != PLAN-REPAIR AUTHORITY
PLAN REVIEW PASS != IMPLEMENTATION AUTHORITY
AI PROPOSES != HUMAN DECIDES
```
