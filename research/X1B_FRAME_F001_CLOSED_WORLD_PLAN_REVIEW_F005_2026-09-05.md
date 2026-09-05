# X1B-FRAME F001 — Closed-World Plan Review — First Finding F005

Status: `PLAN REVIEW FAIL / FIRST CREDIBLE COUNTEREXAMPLE / STOP / NO PLAN-REPAIR AUTHORITY`

Date: `2026-09-05`

## 1. Exact review target and Human authority

Human-authorized review target:

```text
FJ899/8 PR #198
HEAD = c42c6a4137df5afbefc8e99fb3d5f5f6f349b612
TREE = 7631199c91c30737593d9b0721dcb0c95d01d49c
PATH = research/X1B_FRAME_F001_SUPERSEDING_CLOSED_WORLD_RECOVERY_AUTHORITY_PLAN_REOPEN_PLAN_F004_2026-09-05.md
BLOB = 8a4788af73ce72007345749bbede1ffb1dce5b34
```

The immediately preceding Human response was exactly:

```text
accept
```

and is bound only to one independent read-only review of the exact PR #198 plan.

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
X1B-FRAME-F001-PLAN-F005 — THE CLOSED-WORLD CENSUS CONTRACT IS INTERNALLY
INCONSISTENT: THE PLAN REQUIRES THE VERIFIER TO ENUMERATE ONLY ROOT `*.md` AND
DIRECT `sources/*.md`, BUT ITS FROZEN "FOURTEEN-DOCUMENT" CENSUS ALSO INCLUDES
`sources/prototype/RESTORE.md`, WHICH IS NEITHER ROOT-LEVEL NOR A DIRECT
`sources/*.md` FILE.

A CONFORMING VERIFIER CANNOT SIMULTANEOUSLY SATISFY THE SPECIFIED ENUMERATION
ALGORITHM AND THE SPECIFIED FOURTEEN-DOCUMENT EXACT-CENSUS ACCEPTANCE CHECK
WITHOUT AN UNFROZEN SPECIAL CASE OR A DIFFERENT ENUMERATION RULE.
```

Primary classification:

```text
CLOSED-WORLD CENSUS SPECIFICATION CONTRADICTION
ACCEPTANCE CONTRACT NOT EXECUTABLE AS WRITTEN
```

Preregistered review class reached:

```text
Q1 — is the root/direct-sources census actually complete at the frozen baseline?
```

The review stops here. No later Q1-Q15 discovery is claimed.

## 3. Frozen plan statements that conflict

PR #198 section 5 lists ten root-level Markdown files:

```text
CODEX_START.md
DECISION_LOG.md
HANDOFF.md
IDEA_ARCHIVE.md
PROJECT_STATE.md
README.md
RECONSTRUCTION_REPORT.md
SOURCES.md
SOURCE_AUDIT_SUMMARY.md
SOURCE_MANIFEST.md
```

It then lists three direct `sources/*.md` files:

```text
sources/Decision_Summary_Current_State.md
sources/RC1_SCOPE_LOCK.md
sources/ScriptOps_Main_Theme_Summary.md
```

That is exactly:

```text
10 root-level Markdown
+ 3 direct sources/*.md
= 13 root/direct-sources Markdown documents
```

The plan then separately adds:

```text
sources/prototype/RESTORE.md
```

under a `plus:` clause and classifies it as pre-fenced/non-authority provenance.

That path is nested under `sources/prototype/` and therefore is not matched by either:

```text
root/*.md
```

or:

```text
sources/*.md  (direct only)
```

## 4. Exact verifier rule creates the contradiction

PR #198 section 23.1 requires the verifier to:

```text
enumerate actual root `*.md` and direct `sources/*.md` files at runtime
and compare them to the frozen census
```

But PR #198 later requires:

```text
P3  all fourteen root/direct-sources Markdown documents have exactly one registry class -> PASS
```

and:

```text
C15 actual root/direct-sources Markdown census equals the frozen fourteen-document census
```

The specified enumeration set has cardinality 13 at the frozen baseline.

The specified acceptance set has cardinality 14 because it includes the nested:

```text
sources/prototype/RESTORE.md
```

Therefore:

```text
ENUMERATE(root *.md + direct sources/*.md)
= 13 paths

FROZEN FOURTEEN-DOCUMENT CENSUS
= those 13 paths + sources/prototype/RESTORE.md
= 14 paths
```

The two sets cannot be equal under the exact algorithm as written.

## 5. Baseline path fact

At the frozen ScriptOps baseline:

```text
FJ899/scriptops
HEAD = 2f22843ac570498b506101addeba5453ab777f08
PATH = sources/prototype/RESTORE.md
BLOB = 8a79aca4c93b23c4842792bea9ecaae146e1fc48
```

The file is a real nested path, not a direct child of `sources/`.

Its content explicitly describes historical prototype reconstruction, which supports the plan's intended non-authority classification; this finding does not dispute that semantic classification.

The defect is the census algorithm/cardinality contract.

## 6. Minimal implementation counterexample

Consider a future candidate that implements section 23.1 literally:

```text
root_md = enumerate root/*.md
sources_md = enumerate direct sources/*.md
actual_census = root_md U sources_md
```

At the frozen baseline this yields exactly 13 documents.

Now enforce C15 literally:

```text
actual root/direct-sources Markdown census
== frozen fourteen-document census
```

Result:

```text
13 != 14
=> FAIL
```

A correct candidate can never satisfy C15.

Alternatively, an implementer could silently special-case:

```text
sources/prototype/RESTORE.md
```

into `actual_census`.

But then the verifier is no longer implementing the frozen enumeration rule `root *.md + direct sources/*.md`; it is implementing an unstated expanded rule.

A third option would be to recurse under `sources/`, but that likewise changes the specified census rule and potentially changes what future files are in scope.

Thus a future implementer is forced to choose between:

```text
A. obey section 23.1 and fail C15/P3 forever;
B. violate section 23.1 by adding an unstated special case;
C. silently broaden enumeration semantics beyond the frozen plan.
```

None is a valid executable-plan result.

## 7. Why this matters to the closed-world property

The central repair claim of PR #198 is:

```text
AUTHORITY IS REGISTRY-GRANTED, NOT SELF-ASSERTED
```

and the verifier is supposed to prove the world is closed by comparing the actual document census against a frozen complete registry.

A closed-world proof requires the universe of documents being compared to be unambiguous.

Here the plan has two different universes:

```text
U1 = root *.md + direct sources/*.md
U2 = U1 + sources/prototype/RESTORE.md
```

If the verifier universe is not frozen unambiguously, then neither `UNCLASSIFIED_AUTHORITY_CAPABLE_DOCUMENT` nor exact registry cardinality has a single deterministic meaning.

This is a plan-level blocker rather than a cosmetic counting typo because C15, P3, section 23.1 and registry exactness all depend on the census definition.

## 8. Expected vs observed plan semantics

Expected executable closed-world plan:

```text
ONE EXACTLY DEFINED DOCUMENT UNIVERSE
-> ONE ENUMERATION ALGORITHM
-> ONE FROZEN CENSUS
-> EXACTLY ONE REGISTRY CLASS PER MEMBER
-> UNKNOWN MEMBER = FAIL CLOSED
```

Observed PR #198 contract:

```text
ENUMERATION ALGORITHM = root *.md + direct sources/*.md
FROZEN ACCEPTANCE COUNT = 14
EXTRA NESTED MEMBER = sources/prototype/RESTORE.md
=> universe definition is inconsistent
```

## 9. Invariants violated

```text
CLOSED WORLD != TWO DIFFERENT CENSUS UNIVERSES
EXACT CENSUS != APPROXIMATE / SPECIAL-CASED CENSUS
VERIFIER CONTRACT != IMPLEMENTER-GUESSED ENUMERATION
FAIL-CLOSED REGISTRY != AMBIGUOUS MEMBERSHIP RULE
```

Preserved prior invariants remain:

```text
CURRENTNESS_UNESTABLISHED != FALSE
CURRENTNESS_UNESTABLISHED != TRUE
CHECKED_OUT_RUNTIME_CLASS != ACTIVE_PRODUCT_STATE
PR HEAD != ACTIVE DEFAULT BRANCH
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
```

## 10. Scope classification

This finding is only a plan specification defect.

```text
X1B PROPERTY FALSIFIED = NO
X1B CLOSURE REOPENED = NO
RUNTIME REMEDIATION FINDING = NO
SCRIPTOPS IMPLEMENTATION AUTHORITY = NO
```

The review did not continue to search for later authority-surface or runtime counterexamples after this first credible finding.

## 11. Minimal reproducer

Read only PR #198 and the frozen baseline tree:

```text
1. Count section 5 root-level Markdown entries: 10.
2. Count direct sources/*.md entries: 3.
3. Apply section 23.1 enumeration rule: 10 + 3 = 13.
4. Observe separately listed nested sources/prototype/RESTORE.md.
5. Read P3/C15: frozen root/direct-sources census is required to contain 14 documents.
6. Compare: 13 != 14.
```

No runtime execution or repository mutation is necessary to reproduce the contradiction.

## 12. Review disposition

```text
X1B-FRAME F001 CLOSED-WORLD PLAN REVIEW = FAIL
X1B-FRAME-F001-PLAN-F005 = OPEN
FIRST CREDIBLE COUNTEREXAMPLE = STOP
PR #198 = NOT PASS
SCRIPTOPS IMPLEMENTATION AUTHORITY = NO
PR #35 MERGE AUTHORITY = NO
DEPLOYMENT / RELEASE / TAG = NO
V1 AUTHORITY = NO
X1B = REMAINS CLOSED AT ACCEPTED RESEARCH/CORRECTIVE SCOPE
```

No plan repair is performed in this review.

The next legal stage is a separate Human disposition of this exact finding. Only after Human acceptance may one bounded superseding plan repair be prepared.

Preserve:

```text
FIRST CREDIBLE COUNTEREXAMPLE = STOP
PLAN REVIEW FINDING != PLAN-REPAIR AUTHORITY
PLAN REVIEW PASS != IMPLEMENTATION AUTHORITY
AI PROPOSES != HUMAN DECIDES
```