# X1C — Composition Test

Date: 2026-08-30
Status: RESEARCH ARTIFACT / NO NEW PRIMITIVES / NO IMPLEMENTATION / NO X1D

## Question

Can the X1C predicate

```text
HumanDecision(C,S,I) = TRUE
```

be represented sufficiently using only existing formal machinery, without introducing a new logic or a new decision primitive?

## Allowed composition

This test intentionally permits only existing classes of machinery:

1. **Security ceremony** — roles, Human/AI/System interaction, observable events and channels.
2. **Injective agreement / correspondence** — agreement on exact data and a unique matching run/instance.
3. **Referent binding** — exact binding of the accepted content/scope to the later attributed decision/effect.
4. **Non-repudiation / provenance** — durable evidence about the attributed actor/event.
5. **Observational-equivalence attack** — search for two histories with the same system-visible trace but different truth of `HumanDecision(C,S,I)`.

No new primitive such as `verified_intent`, `true_consent`, `human_mind_state`, or a bespoke Agency-Kernel decision token may be added.

## R1–R4 mapping

| X1C lower bound | Existing formal machinery used | What it can establish |
|---|---|---|
| R1 — Human-origin | security ceremony + trusted/Human-controlled interaction assumption + provenance | an event is attributable to the Human-side role/channel rather than merely to the effect executor |
| R2 — explicit decision semantics | ceremony event label / consent or transaction-confirmation event | the protocol treats an observed event as an acceptance/decision event |
| R3 — exact referent | injective agreement/correspondence on `(C,S,I)` + referent binding | the Human-side event and System-side attribution refer to the same exact content, scope and unique instance |
| R4 — continuity/supersession | binding + uniqueness/freshness + provenance | later A-prime cannot silently inherit the evidence for A; replacement requires a new matching event or explicit supersession |

## Proposed composition without new primitives

Define an existing-ceremony Human-side event:

```text
H_ACCEPT(C,S,I)
```

and a System-side attribution event:

```text
S_RECORD_HUMAN_DECISION(C,S,I)
```

Require:

```text
P1 Human-origin ceremony condition:
   H_ACCEPT(C,S,I) occurs on the Human-side interaction path / role.

P2 Injective agreement / correspondence:
   every S_RECORD_HUMAN_DECISION(C,S,I)
   has one unique prior matching H_ACCEPT(C,S,I).

P3 Referent integrity:
   the exact C,S,I used by H_ACCEPT are the exact C,S,I later recorded and acted upon.

P4 No silent inheritance:
   mutation of C or S, or a new decision instance I-prime,
   requires a new matching Human-side event or explicit supersession.

P5 Evidential persistence:
   provenance/non-repudiation evidence preserves the matching relation.
```

If these properties were sufficient, the System could infer:

```text
P1 && P2 && P3 && P4 && P5
=> HumanDecision(C,S,I) = TRUE
```

The test below attacks that implication.

# Attack the composition

## H1 — genuine Human decision

1. System presents exact `C,S,I`.
2. Human understands the decision proposition and decides to accept it.
3. Human performs the observable ceremony action that emits `H_ACCEPT(C,S,I)`.
4. System records `S_RECORD_HUMAN_DECISION(C,S,I)`.
5. Injective agreement/correspondence holds on exact `(C,S,I)`.
6. Provenance records the Human-side event.
7. No mutation or replay occurs.

Ground truth for the hypothesis being tested:

```text
HumanDecision(C,S,I) = TRUE
```

All P1–P5 hold.

## H0-A — same Human-origin act, no decision semantics

1. System presents exact `C,S,I`.
2. Human does **not** form/perform the decision represented by `HumanDecision(C,S,I)`.
3. Human nevertheless performs the same observable action — for example because the control is understood as `continue`, acknowledgement, navigation, dismissal, routine confirmation, or because the Human acts without the decision semantics the model attributes to the event.
4. The same ceremony event `H_ACCEPT(C,S,I)` is emitted.
5. System records the same `S_RECORD_HUMAN_DECISION(C,S,I)`.
6. Injective agreement/correspondence holds on exact `(C,S,I)`.
7. Provenance records the same Human-side origin.
8. No mutation or replay occurs.

Ground truth for the hypothesis being tested:

```text
HumanDecision(C,S,I) = FALSE
```

Yet P1–P5 still hold.

The System-visible security trace can be the same as H1.

### Result

This defeats the implication **unless the semantics of `H_ACCEPT` are grounded independently of the event label**.

Merely naming the event `HumanAccept` or treating a button/gesture as an acceptance event imports the desired conclusion into the model.

```text
EVENT LABEL != DECISION SEMANTICS
```

## H0-B — Human-origin confirmation under misframed referent meaning

This is a stronger semantic variant.

1. Exact machine-level `C,S,I` is bound and displayed through the ceremony.
2. Human performs the genuine Human-origin confirmation gesture.
3. The protocol correctly proves injective agreement on exact bits/fields `(C,S,I)`.
4. The Human, however, reasonably interprets the presented proposition differently from the semantic decision later attributed by the System.
5. The same provenance, correspondence, uniqueness and referent-binding properties hold.

If X1C's claim is about semantic authorship of the System-attributed decision rather than merely cryptographic agreement on displayed fields, the protocol trace again does not by itself establish equivalence between:

```text
Human-facing meaning
```

and

```text
System-attributed decision meaning
```

This is not a failure of injective agreement. It is outside what agreement is designed to prove.

## H0-C — automated origin attempt

If the Human-side ceremony event can also be generated by software/process possession of the same interaction capability, then H0-C breaks P1 directly:

```text
non-Human process emits the event
```

This is the original R1 problem.

A trusted/Human-controlled path or ceremony assumption can rule out H0-C. Therefore H0-C is **not** the decisive composition falsifier once P1 is genuinely satisfied.

The decisive residual issue is H0-A/H0-B: even a genuine Human-origin event can remain semantically underdetermined.

# What existing formalisms successfully solve

The composition is already strong enough to solve most of the structural problem:

```text
WHO/ORIGIN CHANNEL   -> ceremony/provenance
EXACT C,S            -> agreement + binding
UNIQUE I             -> injective agreement/freshness
NO A -> A-prime LEAK -> binding/supersession
DURABLE EVIDENCE     -> provenance/non-repudiation
```

Therefore Project 8 should not claim novelty in those properties.

# Exact residual gap

The composition breaks at the inference:

```text
observable Human-origin event with protocol-defined acceptance semantics
=> Human decision semantics
```

Existing agreement/correspondence machinery can prove that the correct Human-side event occurred and that the System-side run uniquely corresponds to it on exact `(C,S,I)`.

It does **not**, by itself, establish that the ceremony event's protocol label truthfully captures the Human decision semantics whose authorship is later asserted.

The gap can be stated narrowly as:

> How can a formal model ground the semantics of an observable Human-origin event strongly enough that `HumanDecision(C,S,I)` is not merely true by event naming/ceremony specification, while remaining based on observable evidence rather than inaccessible private mental state?

This is narrower than `secure approval`, narrower than R1 alone, and narrower than a general Human-intent problem.

# Observational-equivalence result

For H1 and H0-A, under an event model where both produce the same externally observable Human-side action:

```text
Trace(H1) = Trace(H0-A)
```

while:

```text
HumanDecision_H1(C,S,I) = TRUE
HumanDecision_H0-A(C,S,I) = FALSE
```

Therefore the current composition cannot justify the semantic predicate from the trace alone.

This does **not** prove that no existing formalism can solve the problem. It proves only that the tested composition, when decision semantics are represented by a ceremony event label plus existing agreement/binding/provenance properties, is insufficient unless semantic grounding is supplied by an additional justified assumption/model.

# Verdict

```text
BLOCKED — SEMANTICS CANNOT BE GROUNDED FROM THE TESTED TRACE MODEL
```

Not:

```text
COMPOSITION INSUFFICIENT — NEW LOGIC REQUIRED
```

because the review has not established that existing security-ceremony, HCI consent, epistemic or action-theoretic formalisms cannot supply the missing grounding.

Not:

```text
COMPOSITION SUFFICIENT
```

because H1 and H0-A remain observationally equivalent under P1–P5.

# Consequence for the Project 8 hypothesis

The plausible gap is now narrower:

```text
NOT: missing authentication
NOT: missing trusted path
NOT: missing exact binding
NOT: missing unique agreement
NOT: missing provenance

POSSIBLE GAP:
formal grounding of Human decision semantics at the Human-side ceremony event,
such that semantic authorship is not obtained merely by naming an observable event `accept`.
```

Status:

```text
PLAUSIBLE SEMANTIC-GROUNDING / FORMALIZATION GAP
NOT YET NOVELTY
```

# Stop discipline

- No X1D was created.
- No code was changed.
- No Agency Kernel v1 was designed.
- No new security primitive was introduced.
- No authentication, MFA, token, signature, broker or trusted-hardware mechanism was selected.
- No scientific novelty claim is made.

# Next research question

Before any new experiment or architecture work, search specifically for existing formal treatments of:

```text
observable action -> intentional/consent semantics
```

in security ceremonies, usable-security ceremony analysis, formal HCI consent, action/intent logics, epistemic logic of agency, authorization-with-intent, and human-protocol interaction.

If an existing model grounds the Human-side event sufficiently, adopt it and rerun this composition test.

If no such model is found after a bounded systematic pass, the gap claim can be strengthened from a broad X1C formalization gap to a specific **Human decision-event semantic grounding gap**.
