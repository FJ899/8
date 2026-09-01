# X1D — ScriptOps Constitutive-Rule Reality Check — RESULT

Date: 2026-08-30
Status: FAIL / STOPPED AT FIRST CREDIBLE COUNTEREXAMPLE / NO REPAIR

## Frozen test

Preregistration:
`experiments/X1D_PREREGISTRATION.md`

System under test:
`FJ899/scriptops`

Frozen baseline:

```text
main@68a1bb996e1345e2a8f86813042ff7b40109ae74
TREE 2001e2c501fc92197e8b59f18693b3bbf6d7e7cd
```

Primary claim:

```text
ScriptOps may assert
HumanDecisionAttributionJustified_K(C,S,I) = TRUE
only if an authoritative, applicable and then-current Q_K governs the approval,
changes to Q_K are authority-controlled,
and the approval is bound to the exact later canonical effect.
```

Per preregistration, execution stops at the first credible counterexample.

# A1 — Authority

## Evidence observed

`DECISION_LOG.md` contains:

- `DEC-SO-001 — człowiek pozostaje właścicielem kanonu`, status ACTIVE;
- AI creates candidates/analyses and does not independently approve/change canon;
- `DEC-SO-010`, status ACTIVE, `Owner: USER`;
- DEC-SO-010 freezes Phase-6 B1–B5 and requires mandatory Human `why` before canonical write;
- it explicitly states ScriptOps does not receive its own authority.

The Phase-6 `cmd_approve` implementation enforces a non-empty `--why`, requires an exact staged candidate plus matching `REVIEW_REQUIRED` impact report, writes the canonical target, and records `approver: "human"`.

## X1D assessment

For the narrow question `who normatively establishes the approval rule`, the repository contains enough explicit evidence to identify the Human/User as the declared rule authority rather than ScriptOps itself.

```text
A1: SUPPORTED AS A DECLARED NORMATIVE RULE
```

This does not itself prove enforcement of rule-change authority. That is A4.

# A2 — Provenance / version

The repository uses Git as source of truth and both the constitutive decision rules and implementation are versioned in Git.

For an approval committed by the Phase-6 path, the commit containing the canonical scene + decision-log change can be located, and its parent fixes the repository state under which the approval operation was executed. The operative `DEC-SO-*` entries and approval implementation are therefore historically reconstructable at commit granularity.

The individual runtime decision record does **not** embed an explicit `Q_K` rule id/hash/version. This is weaker than explicit rule-instance binding, but the preregistered question was whether the applicable version is knowable, not whether a dedicated field exists.

No counterexample was established at A2 before reaching A4.

```text
A2: NOT FALSIFIED IN THIS RUN
```

# A3 — Applicability

`DEC-SO-010` is explicitly scoped to Phase 6 and defines the approval/canonical-write boundary for that slice. The tested implementation is the Phase-6 hardening shim and its `approve` command implements that same bounded path.

This gives a repository-visible basis for applying the declared approval rule to this workflow class.

No counterexample was established at A3 before reaching A4.

```text
A3: NOT FALSIFIED IN THIS RUN
```

# A4 — Change control — FIRST CREDIBLE COUNTEREXAMPLE

## Repository rule observed

GitHub ruleset:

```text
CANONICAL_MAIN_PROTECTION_V1
ENFORCEMENT: active
TARGET: default branch
```

It requires changes to reach the default branch through a pull request and blocks deletion/non-fast-forward.

However its pull-request rule has:

```text
required_approving_review_count: 0
required_reviewers: []
require_code_owner_review: false
require_last_push_approval: false
bypass_actors: []
```

Therefore the repository-level change-control boundary does **not** require an independent Human approval/reviewer before a change to the normative-rule artifacts or approval implementation can become eligible for merge.

## Why this falsifies the X1D claim

The normative authority declared by `DEC-SO-001` / `DEC-SO-010` is Human/User authority.

But the repository mechanism that controls changes to the artifacts implementing/expressing `Q_K` does not bind rule modification to a separate Human approval event.

A process with sufficient repository mutation/merge capability can, at the repository-policy level, submit and merge a change to:

- `DECISION_LOG.md` approval semantics;
- `phase6/scriptops-v2-hardening.py` approval logic;
- other rule-bearing artifacts;

without the ruleset itself requiring a Human approval.

The system therefore does not enforce:

```text
CAPABILITY TO MODIFY RULE REPRESENTATION
!=
AUTHORITY TO MODIFY NORMATIVE RULE
```

It declares that distinction normatively, but current repository change control does not make it an enforced precondition of an authoritative rule change.

This is sufficient to defeat the primary X1D claim AS-IS.

## Exact counterexample class

```text
H0-QK-CHANGE

1. Current Q_K is Human-authored/declared.
2. A repository-capable non-Human process prepares a PR that changes the rule-bearing artifact or approval logic.
3. Repository rules require a PR but require zero approving reviews and no Human/code-owner/last-push approval.
4. The change can therefore satisfy repository merge-policy requirements without an independently required Human rule-authorization event.
5. The resulting repository state can contain a different effective approval rule Q_K-prime.
6. Later ScriptOps decisions may be evaluated under Q_K-prime even though the repository itself did not establish the Human/User authorization required by the declared normative model.
```

This counterexample does **not** claim that such an unauthorized merge has actually occurred. It establishes that the current technical change-control boundary does not enforce the declared authority invariant.

# Verdict

```text
X1D FAIL — Q_K CHANGE AUTHORITY NOT ENFORCED
```

More explicitly:

```text
DECLARED HUMAN RULE AUTHORITY
!=
ENFORCED HUMAN AUTHORIZATION OF RULE CHANGE
```

# Stop discipline

Per preregistration, STOP occurred at A4.

Therefore:

- A5 end-to-end binding was NOT executed in this X1D run;
- no attempt was made to search for a later PASS;
- no ScriptOps code or repository rule was changed;
- no repair was designed;
- no X1D implementation was built;
- no Agency Kernel v1 was designed;
- no merge/release/deploy/tag was performed.

# Research consequence

The failure is not a missing formalism. X1C literature work already showed that authority/delegation/change-control formal machinery exists.

The failure is an AS-IS implementation/governance mismatch:

```text
ScriptOps declares Human authority over the constitutive rule,
but its current repository change-control boundary does not require
an independent Human authorization for changes to the rule-bearing artifacts.
```

No solution is authorized by this result.
