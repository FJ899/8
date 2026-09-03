# X1C — Composition Test

Date: 2026-08-30
Status: RESEARCH ARTIFACT / NO NEW PRIMITIVES / NO IMPLEMENTATION / NO X1D / NO NOVELTY CLAIM

## Updated question

Can a public Human-decision attribution be justified using only existing formal machinery, without introducing a new decision-semantic primitive?

Target predicate:

```text
HumanDecisionAttributionJustified_K(C,S,I)=TRUE
```

where `K` is the relevant domain/context.

This predicate does **not** claim direct access to private Human mental state. It claims only that the system has sufficient public, observable and normatively justified grounds to attribute a bounded act to the Human as a decision concerning exact content C, scope S and decision instance I.

## Refined composition

```text
Security Ceremony
+ independently justified Counts-As / Constitutive Rule Q_K
+ Injective Agreement / Correspondence
+ Exact Referent / Execution Binding
+ Provenance / Non-Repudiation
+ Observational-Equivalence Counterhistory Attack
```

## Core correction

The previous composition failed because it modeled decision semantics by labeling an observable event `H_ACCEPT`.

```text
EVENT LABEL != DECISION SEMANTICS
```

A subsequent literature pass identified strong prior art in contextual constitutive rules:

```text
X counts as Y in context K
```

This provides an existing formal bridge from low-level observable action X to public/institutional action Y, provided the constitutive rule is independently justified in the relevant context.

Therefore the refined model is:

```text
Observable Human Act A
+ Domain/Context K
+ independently justified validity conditions Q_K
=> A counts-as ValidHumanDecisionAct_K(C,S,I)
```

Then:

```text
ValidHumanDecisionAct_K(C,S,I)
+ injective agreement on (C,S,I)
+ preserved referent/execution binding
+ provenance/non-repudiation
=> HumanDecisionAttributionJustified_K(C,S,I)=TRUE
```

## What the existing machinery covers

```text
PUBLIC DECISION SEMANTICS -> contextual counts-as / constitutive rule
WHO/ORIGIN CHANNEL        -> ceremony/provenance
EXACT C,S                 -> agreement + binding
UNIQUE I                  -> injective agreement/freshness
NO A -> A-prime LEAK      -> binding/supersession
DURABLE EVIDENCE          -> provenance/non-repudiation
```

No new foundational primitive has been shown necessary for these properties.

## Attack the constitutive rule, not the event label

### H0-1 — arbitrary rule declaration

Designer declares:

```text
pressing Continue counts-as Decision(A)
```

but supplies no independent normative/domain justification.

Later agreement, provenance and binding may all be perfect.

Result:

```text
CONSTITUTIVE DECLARATION != JUSTIFIED CONSTITUTIVE RULE
```

Formal correctness after the declaration would be circular.

### H0-2 — incomplete/misrepresented presentation

Human performs a genuine affirmative act, but operative content/scope differs materially from what the Human-facing ceremony presents.

Result:

```text
Q_K must constrain presentation/referent validity;
security agreement alone is insufficient.
```

### H0-3 — exact referent but generic interaction

Exact C,S,I are available, but the observable Human act publicly functions only as navigation/acknowledgement/continue.

Result:

```text
Q_K must contain an independently justified affirmative-decision condition.
```

### H0-4 — domain-invalid context

A clear affirmative act exists for exact C,S,I, but a domain-specific validity condition is absent: e.g. lack of required voluntariness, mandatory disclosure, authority or other constitutive condition.

Origin, agreement, binding and provenance may all still hold.

Result:

```text
ATTRIBUTION VALIDITY IS DOMAIN-NORMATIVE.
```

### H0-5 — universal-Q transfer failure

A Q-set derived from one domain is applied unchanged across payments, medical consent, privacy consent, Git approval, creative canon acceptance or employment decisions.

Counterexample: conditions constitutive of valid consent/decision differ by domain.

Result:

```text
ONE UNIVERSAL COMPLETE Q-SET NOT ESTABLISHED.
```

## Revised H1/H0 observational-equivalence test

### H1

The authoritative domain rule Q_K is independently justified; all required observable conditions hold; Human performs the constitutively valid act; unique agreement, binding and provenance all hold.

### H0-A — private mental difference only

The same publicly valid act occurs under the same valid context and exact C,S,I, but the Human internally feels uncertainty, regret or some different private attitude.

The trace is identical.

This no longer falsifies:

```text
HumanDecisionAttributionJustified_K
```

because that predicate deliberately claims a justified public/normative attribution, not private psychological truth.

### H0-B — required validity condition outside observation coverage

A condition that Q_K treats as necessary is absent or violated, but the attribution system cannot observe it.

Then H1 and H0 can produce the same visible trace while attribution validity differs.

Result:

```text
INSUFFICIENT OBSERVATION COVERAGE
```

### H0-C — Q_K itself arbitrary or silently changed

If the system/AI can invent, reinterpret or silently supersede Q_K, then formal proof under that rule does not establish legitimate attribution.

Result:

```text
RULE PROVENANCE / AUTHORITY / VERSIONING BECOMES PART OF THE PROBLEM.
```

## Verdict

The earlier verdict:

```text
BLOCKED — SEMANTICS CANNOT BE GROUNDED FROM THE TESTED TRACE MODEL
```

is superseded as the strongest current conclusion.

Semantic grounding has strong prior art through contextual constitutive rules.

The strongest supported verdict is now:

```text
COMPOSITION CONDITIONALLY SUFFICIENT
— RELATIVE TO AN INDEPENDENTLY JUSTIFIED DOMAIN RULE Q_K
— AND COMPLETE OBSERVATION OF THE CONDITIONS Q_K REQUIRES
```

Also:

```text
NO NEW DECISION-SEMANTICS PRIMITIVE DEMONSTRATED AS NECESSARY.
NO UNIVERSAL COMPLETE Q-SET ESTABLISHED.
```

## Current gap candidate

The candidate gap is no longer Human decision semantics itself.

It is now closer to:

> How should an AI-assisted system identify, source, govern, version and evidence the authoritative domain-specific constitutive rule Q_K under which an observable Human act counts as a valid public decision act, without allowing the AI/system to invent or silently change that rule?

This is **not** a novelty claim.

Existing normative systems, policy logics, institutional-rule frameworks, legal-computational models or governance systems may already solve substantial parts of it.

## Revised status

```text
SEMANTIC-GROUNDING: STRONG PRIOR ART / COMPOSITION AVAILABLE
UNIVERSAL Q-SET: NOT ESTABLISHED
DOMAIN-INDEPENDENT SCHEMA: STRONGLY SUPPORTED
POTENTIAL GAP: AUTHORITATIVE DOMAIN-RULE GOVERNANCE + EVIDENCE COMPOSITION
NOVELTY: NOT ESTABLISHED
```

## Stop discipline

- No X1D created.
- No code changed.
- No Agency Kernel v1 designed.
- No new security primitive introduced.
- No authentication/MFA/token/signature/broker mechanism selected.
- No scientific novelty claim made.

Full constitutive-rule attack is recorded in:

`research/X1C_CONSTITUTIVE_RULE_COMPOSITION_TEST.md`.
