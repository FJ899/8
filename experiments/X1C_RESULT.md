# X1C — Human Decision Evidence Boundary — Result

Status: `BLOCKED AFTER NECESSARY-LOWER-BOUND IDENTIFICATION`

Date: 2026-08-30

Preregistration: `a589c52b738a693ac6d689eccbc595f89c9cf0be`

## Result headline

```text
X1C BLOCKED — OBSERVABLE DECISION EVIDENCE NOT YET SUFFICIENTLY TESTABLE
```

X1C successfully falsified several weaker evidence models and identified a compact necessary lower bound. It did **not** establish a sufficient minimal evidence set because the available ScriptOps workflow does not expose an independent observable Human-origin boundary needed for the positive control.

This is therefore not `X1C PASS`.

## Grounded real workflow

The real ScriptOps workflow contains useful pieces of the decision boundary:

- proposal artifacts are separated from canonical effect;
- a Human semantic decision can contain exact bounded content and scope;
- the recorded SCN-012/SCN-027 acceptance preserves exact proposal bodies and explicitly limits scope;
- canonical effect still requires a separate Human gate;
- the Phase-6 `approve` operation requires a non-empty `why` before canonical write.

However, the approval command path itself does not independently establish that the observed invocation originated from a Human decision act. A recorded attribution such as `approver="human"` is produced by the same execution path and is therefore an assertion, not independent provenance of Human origin.

## Observational-equivalence attacks

### O1 — operation occurrence

Observation:

```text
approve operation occurred
```

Counterhistory:

A non-Human process with the same approval capability invokes the operation.

System-visible operation result can be the same.

Result: `INSUFFICIENT`.

### O2 — identified Human / account source

Observation:

```text
operation is associated with a Human identity/account/session
```

Counterhistory:

Automation or another process acts through the same account/session/capability.

Result:

```text
IDENTIFIED HUMAN != HUMAN ACT
```

`INSUFFICIENT`.

### O3 — explicit approval-shaped act

Observation:

```text
an explicit approve/accept action occurred
```

Counterhistory:

The act has approval semantics but the system cannot establish which exact content and scope the act referred to.

Result:

```text
HUMAN ACT != HUMAN DECISION ABOUT THIS CONTENT
```

`INSUFFICIENT`.

### O4/O5 — exact content or scope visibility

Observation:

Exact content and/or exact scope exist in the record.

Counterhistory:

The exact content exists, but the Human act is not bound to it; or the act refers to another scope.

Result: `INSUFFICIENT`.

### O6 — binding without Human-origin evidence

Observation:

An approval event is strongly bound to exact content and scope.

Counterhistory:

A non-Human process creates the bound approval event.

Result: `INSUFFICIENT`.

### O7 — mutation detection / A vs A-prime

Observation:

The system can detect later content mutation.

Counterhistory:

The initial approval event itself was never established as a Human decision act.

Result: `INSUFFICIENT` by itself.

### O8 — freshness / non-reuse

Observation:

The approval event is fresh and cannot be replayed for another decision instance.

Counterhistory:

A fresh event is still produced by a non-Human process or is not bound to the Human's intended referent.

Result: `INSUFFICIENT` by itself.

### O9 — attribution field/provenance assertion

Observation:

The durable record says the approver is Human.

Counterhistory:

The same process that performs the effect writes the Human attribution.

Result:

```text
ATTRIBUTION ASSERTION != ATTRIBUTION EVIDENCE
```

`INSUFFICIENT`.

## Necessary lower bound that survived

The attacks reduce the problem to four observable property families.

### R1 — independent Human-origin evidence

There must be observable evidence distinguishing a Human-origin decision act from mere possession/use of the approval capability.

This is **not** equivalent to account identity.

```text
IDENTITY != ORIGIN OF DECISION ACT
```

The observation must not be merely self-asserted by the same process that executes or records the effect.

### R2 — explicit decision semantics

The observable Human-origin act must itself have decision/acceptance semantics.

Viewing, silence, continuation, navigation, acknowledgement, or generic interaction are insufficient.

### R3 — exact referent binding

The act must be bound to the exact:

- content;
- scope;
- decision instance.

This collapses the critical distinction:

```text
HUMAN DECISION ABOUT A != HUMAN DECISION ABOUT A-prime
```

into an observable requirement rather than a UI assumption.

### R4 — integrity / supersession visibility

The content later treated as the operative Human decision must remain the exact bound referent, or any mutation/scope expansion/new decision instance must observably invalidate or supersede the prior attribution.

This prevents stale consent, replay, A→A-prime substitution and silent scope expansion.

## Candidate epistemic rule

The strongest bounded rule supported by X1C is currently:

```text
HumanDecision(C, S, I) = TRUE
only if there is independent observable Human-origin evidence
of an explicit decision act
bound to exact Content C + Scope S + Decision Instance I,
and the later operative attribution preserves that binding
or records an observable supersession.
```

This is a **necessary lower bound**, not yet a proven sufficient condition.

## Why X1C cannot PASS yet

The current real ScriptOps workflow exposes:

- exact proposal content;
- bounded scope;
- semantic decision records;
- separate future effect gate;
- approval command semantics;
- durable decision/effect artifacts.

But it does not expose an independent observable boundary capable of distinguishing:

```text
Human-origin decision act
```

from:

```text
another process using the same approval capability / account / session
```

Without that boundary, the X1C positive control cannot establish R1 on a real substrate. Declaring the full set sufficient would therefore bake the desired answer into the evidence model.

## Important negative conclusion

X1C does **not** conclude that the solution is authentication, MFA, signatures, hashes, trusted hardware, a ledger, or any specific UI.

Those are possible implementation mechanisms for one or more surviving properties. They are not themselves the property.

```text
PROPERTY != MECHANISM
```

## Decision boundary now exposed

The missing property is no longer vaguely `secure approve`.

It is:

> establish an observable Human-origin decision event, separately from generic approval capability, then bind that event to exact content, scope and decision instance with preserved integrity.

## Stop discipline

No ScriptOps code was changed.

No authentication/binding mechanism was designed.

No Agency Kernel v1 was built.

No accepted v0 semantics were modified.

No `X1C PASS` was claimed.

## Next decision

A separate Human decision is required before the next experiment.

The evidence-driven next question is narrower than X1C:

> Can an existing real Human-facing interaction surface provide an independently observable Human-origin decision event without first inventing a new decision system?

That experiment should test R1 first, while preserving R2–R4 as already identified required properties.
