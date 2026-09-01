# X1D — ScriptOps Constitutive-Rule Reality Check

Date: 2026-08-30
Status: PREREGISTERED / READ-ONLY REALITY CHECK / NO IMPLEMENTATION

## Research target

Test the existing ScriptOps approval workflow against the composed state-of-the-art model established after X1C.

Primary claim under test:

```text
ScriptOps may assert
HumanDecisionAttributionJustified_K(C,S,I) = TRUE
only if:

1. an authoritative Q_K governs the approval;
2. the applicable version of Q_K is knowable for that decision instance;
3. Q_K is applicable to the exact domain/content/scope/instance;
4. changes to Q_K are controlled by an authorized rule authority rather than by the evaluated AI/process merely possessing modification capability;
5. the approval justified under Q_K is bound end-to-end to the exact later canonical effect.
```

## Frozen external system under test

Repository:
`FJ899/scriptops`

Baseline:
`main@68a1bb996e1345e2a8f86813042ff7b40109ae74`

Tree:
`2001e2c501fc92197e8b59f18693b3bbf6d7e7cd`

The ScriptOps repository is read-only for this test. No implementation, workflow, canon, rule, decision-log, or approval behavior may be changed.

## Scope

Inspect only the existing workflow and artifacts needed to answer five questions:

### A1 — Authority
Who actually establishes the constitutive approval rule `Q_K` in ScriptOps?

Evidence must distinguish:

```text
CAPABILITY TO MODIFY RULE REPRESENTATION
!=
AUTHORITY TO MODIFY NORMATIVE RULE
```

### A2 — Provenance / version
For a concrete approval decision instance `I`, can the system establish which exact rule/version `Q_K@v` was authoritative at the time of the decision?

### A3 — Applicability
What observable binding establishes that this exact `Q_K@v` applies to the exact `C,S,I` and domain/context K?

### A4 — Change control
Who may create, replace, broaden, narrow, or supersede `Q_K`? Can the evaluated AI/process influence the authoritative rule merely by editing/generating the rule artifact or approval path?

### A5 — End-to-end binding
If an approval is valid under `Q_K@v`, is that approval bound to the exact later canonical effect, such that changed content/scope/effect cannot inherit the original attribution without a new valid decision or explicit authorized supersession?

## Method

Read-only inspection of existing ScriptOps artifacts and implementation.

For each dimension, record only what the repository currently establishes. Do not infer authority from filenames, authorship fields, or comments unless an operative rule binds those facts.

## Falsification discipline

At the first credible counterexample to the primary claim:

```text
STOP
RECORD DURABLE FINDING
DO NOT CONTINUE SEARCHING FOR A PASS
DO NOT DESIGN A FIX
DO NOT CHANGE SCRIPTOPS
DO NOT BUILD X1D IMPLEMENTATION
DO NOT BUILD V1
```

A counterexample is credible if ScriptOps can reach or record a Human-decision attribution while one of A1–A5 is materially unestablished or bypassable under the existing model.

## Outcome vocabulary

```text
PASS
```

Only if all A1–A5 are positively established for the existing real workflow.

```text
FAIL — <FIRST EXACT BROKEN PROPERTY>
```

At the first credible counterexample.

```text
BLOCKED — <EXACT MISSING OBSERVABILITY>
```

Only if the repository does not expose enough evidence to decide a property either way, without inventing assumptions.

## No-solution boundary

This test does not authorize:

- authentication redesign;
- new approval UI;
- new tokens/signatures/brokers;
- new normative-rule registry;
- new provenance ledger;
- ScriptOps implementation changes;
- Agency Kernel v1;
- merge/release/deploy/tag actions.

The result must remain an observation about the current system AS-IS.
