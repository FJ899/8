# X1B-FRAME — Evidence-main Recovery Incident During Superseding Plan Review

Status: `RECOVERY RECORD / REVIEW PAUSED / HUMAN RE-ANCHOR REQUIRED`

Date: `2026-09-04`

## 1. Context

The Human had authorized exactly one independent read-only review of:

```text
FJ899/8 PR #187
HEAD = 1ceb7a7d56437d794a0f2eb280f98eeb92e40026
TREE = 7b34f50a01bb4b27b2c8eb89915fd27b5f586a3f
PATH = research/X1B_FRAME_F001_SUPERSEDING_STATUS_PROPAGATION_PLAN_REOPEN_PLAN_F001_2026-09-04.md
BLOB = d7744c1cc2a51e9bcb17e5b9a95ded3bebcaef1c
```

At the start of that review, the evidence-repository default branch was:

```text
FJ899/8 refs/heads/main
HEAD = 7c1d191f47b40728fa4c11b6e598afb0f8efe701
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

## 2. First accidental direct-main write

An incorrect write target created a placeholder directly on evidence `main`.

```text
ACCIDENTAL COMMIT = 630c6756a01871983e48f615d1e82b8289c0f8e8
PATH = research/X1B_FRAME_F001_SUPERSEDING_PLAN_REVIEW_F002_2026-09-04.md
CONTENT = # placeholder
BLOB = f4572339b970c63ed56fd068602d35e2be8933c5
```

This write was outside the Human-authorized read-only review and is VOID process residue, not review evidence.

It was immediately removed by:

```text
RECOVERY COMMIT = 5c7891cf56ab31656d80b3ff5c7afc1f16de1a43
MESSAGE = RECOVERY: remove accidental review placeholder from evidence main
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

## 3. Second accidental direct-main write during incident recording

While attempting to freeze the incident itself, the intended incident artifact was again mistakenly targeted at `main` instead of a dedicated branch.

```text
ACCIDENTAL INCIDENT-RECORD COMMIT = e4d9eba22437a54f5aa74c959ff553df5bba5bad
PATH = research/X1B_FRAME_PLAN_REVIEW_EVIDENCE_MAIN_RECOVERY_INCIDENT_2026-09-04.md
```

That file was immediately removed, and no other path was touched, by:

```text
RECOVERY COMMIT = 0b516edb210fd4029972e932fec0206d8a6df1cb
MESSAGE = RECOVERY: remove accidental incident record from evidence main
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

## 4. Exact recovered state

The current evidence default branch is now:

```text
FJ899/8 refs/heads/main
HEAD = 0b516edb210fd4029972e932fec0206d8a6df1cb
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

The tree is exactly the same Git tree as the pre-incident accepted recovery anchor:

```text
PRE-INCIDENT TREE = df807db7003dfd201e9be4d5927472e515a2e737
POST-RECOVERY TREE = df807db7003dfd201e9be4d5927472e515a2e737
TREE EQUALITY = TRUE
```

History cannot be silently rewritten. Therefore the evidence-main commit identity has changed even though repository content is restored exactly.

The following commits are VOID process residue for experiment semantics:

```text
630c6756a01871983e48f615d1e82b8289c0f8e8
e4d9eba22437a54f5aa74c959ff553df5bba5bad
```

The corresponding bounded recovery commits are:

```text
5c7891cf56ab31656d80b3ff5c7afc1f16de1a43
0b516edb210fd4029972e932fec0206d8a6df1cb
```

## 5. Unchanged plan target and product state

The exact review target remains unchanged:

```text
PR #187 HEAD = 1ceb7a7d56437d794a0f2eb280f98eeb92e40026
PLAN TREE = 7b34f50a01bb4b27b2c8eb89915fd27b5f586a3f
PLAN BLOB = d7744c1cc2a51e9bcb17e5b9a95ded3bebcaef1c
```

The ScriptOps active default branch was independently re-read and remains:

```text
FJ899/scriptops refs/heads/main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
```

No ScriptOps path or ref was changed by either incident.
No merge, deployment, release, tag, V1 authority, X1B reopen, runtime mutation, or status correction occurred.

## 6. Review disposition

The independent superseding-plan review is paused at this incident boundary.

No plan-review verdict is frozen by this recovery record.
No plan repair is authorized or performed.

To preserve explicit evidence-state binding, the next legal step is a separate Human disposition that:

```text
1. accepts the recovered evidence-main re-anchor:
   HEAD = 0b516edb210fd4029972e932fec0206d8a6df1cb
   TREE = df807db7003dfd201e9be4d5927472e515a2e737;
2. treats accidental commits 630c6756... and e4d9eba... as VOID process residue;
3. recognizes recovery commits 5c7891cf... and 0b516edb... as bounded tree-restoration history;
4. authorizes one resumed independent read-only review of the still-exact PR #187 target.
```

Until that Human disposition:

```text
PLAN REVIEW = PAUSED
PLAN REVIEW VERDICT = NOT FROZEN
SCRIPTOPS IMPLEMENTATION AUTHORITY = NO
PR #35 MERGE AUTHORITY = NO
DEPLOYMENT / RELEASE / TAG = NO
V1 AUTHORITY = NO
```

Preserve:

```text
ACCIDENTAL WRITE != REVIEW EVIDENCE
TREE RESTORED != HISTORY UNCHANGED
REVIEW FINDING != REPAIR AUTHORITY
AI PROPOSES != HUMAN DECIDES
```
