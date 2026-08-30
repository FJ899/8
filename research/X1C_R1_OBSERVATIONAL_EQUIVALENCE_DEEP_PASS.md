# X1C Deep Literature Pass — R1 + Observational Equivalence

Date: 2026-08-30
Status: RESEARCH ARTIFACT / NO NOVELTY CLAIM / NO X1D AUTHORIZATION / NO IMPLEMENTATION

## Research question

Search narrowly for formal prior art equivalent to either:

```text
HumanDecision(C,S,I) = TRUE
```

under an evidence rule for Human-origin decision authorship, or the X1C falsification criterion:

> if the same system-visible observations are compatible with a history in which the attributed Human decision did not occur, those observations are insufficient to justify `HumanDecision(C,S,I)=TRUE`.

This pass does not search for implementation mechanisms and does not authorize X1D.

## Lines reviewed

- BAN logic and epistemic foundations of authentication logics;
- Lowe-style agreement properties, especially injective agreement;
- strand spaces and authentication tests;
- non-repudiation / evidence-of-origin models;
- evidential transaction / authorization logics;
- observational equivalence in protocol security;
- security ceremonies and formal human-protocol interaction;
- formal FIDO2 analyses that explicitly model the Human.

## Strongest structural prior art found

The closest existing family is not BAN logic alone, but **agreement properties**, especially **injective agreement / correspondence**, embedded where useful in **security ceremonies** that explicitly model Human interaction.

Structurally this can represent much of:

```text
origin/peer
+ exact agreed data
+ unique matching instance/run
+ freshness / anti-replay
```

This is substantially closer to X1C than generic authentication.

## Why injective agreement matters

A correspondence/agreement property can require that when one role reaches a completion/record event on data `M`, there exists a matching prior event/run by the peer on the same `M`.

Injective agreement strengthens this by requiring a unique matching run, excluding replay-like reuse of one peer event for multiple completions.

For X1C, let:

```text
M = (Content C, Scope S, Decision Instance I)
```

Then injective agreement is a strong structural prior-art analogue for:

- exact referent binding;
- unique decision instance;
- correspondence between Human-side and System-side protocol events.

This significantly narrows any claim that Project 8 invented the need for `C,S,I` binding or instance uniqueness.

## Critical limitation

Agreement machinery reasons over the semantics assigned to protocol events.

If the model defines:

```text
H_ACCEPT(C,S,I)
```

then agreement can prove a unique matching relation involving that event.

But agreement does not, by itself, prove that the real-world observable action represented by `H_ACCEPT` actually carries the Human decision semantics later attributed to it.

Thus:

```text
INJECTIVE AGREEMENT != HUMAN DECISION SEMANTICS
```

## Security ceremonies

Security-ceremony work is important because it explicitly extends analysis beyond machine-only protocol roles to Human interaction, channels, devices and user actions.

This helps address the earlier R1 problem by making Human-side events first-class parts of the model rather than treating a device/account as equivalent to a Human.

However, the composition test now shows the residual issue more sharply:

```text
Human-side observable event
!= automatically grounded Human decision meaning
```

A ceremony can model `press`, `confirm`, `read`, `select`, `touch`, or `accept` events. The semantic meaning of the event still has to be justified rather than imported by its label.

## Formal FIDO2 / Human interaction

Formal analyses that explicitly include Human interaction and consent semantics are particularly relevant because they combine:

- Human-side ceremony events;
- authenticator/server protocol roles;
- origin/authentication properties;
- consent/confirmation semantics;
- agreement-style reasoning.

This prior art means Project 8 should not claim novelty merely for combining a Human actor with authentication/agreement properties.

The open question is narrower: how the formal model grounds the semantics of the Human-side consent/decision event relative to observable behavior.

## BAN / authentication logics

BAN-style logics and successors reason about beliefs, message origin/freshness and authentication conclusions.

They are useful background for epistemic protocol reasoning, but they do not appear in this review to be a direct drop-in answer to:

```text
this observed Human action semantically constitutes this decision
```

They can reason over assumptions/events/messages already represented in the model; the difficult step remains grounding the Human decision semantics of the event itself.

Status: `PARTIAL STRUCTURAL PRIOR ART`.

## Non-repudiation / evidence logics

Non-repudiation and evidential transaction models contribute durable evidence that a principal participated in, sent, received, signed or accepted some protocol-relevant object.

This is strong prior art for provenance/evidential persistence, but does not automatically establish the semantic equivalence between an observable Human action and the proposition:

```text
Human decided C,S,I
```

Status: `STRONG PROVENANCE PRIOR ART / NOT FULL SEMANTIC GROUNDING`.

## Observational equivalence

Observational equivalence / trace equivalence / indistinguishability are standard formal tools across protocol privacy, anonymity and related security properties.

Therefore Project 8 does **not** claim novelty in observational equivalence itself.

The potentially distinctive use under X1C is narrower:

```text
H1: HumanDecision(C,S,I) occurred
H0: HumanDecision(C,S,I) did not occur

if Trace(H1) = Trace(H0)
then the trace is insufficient evidence for HumanDecision(C,S,I)=TRUE
```

A standard named **decision-authorship** equivalent of this exact criterion was `NOT FOUND IN THIS PASS`.

That is not a non-existence claim.

## Composition test result

The no-new-primitives composition test is recorded in:

```text
research/X1C_COMPOSITION_TEST.md
```

It combines:

- security ceremony;
- injective agreement/correspondence;
- referent binding;
- provenance/non-repudiation;
- observational-equivalence attack.

Result:

```text
BLOCKED — SEMANTICS CANNOT BE GROUNDED FROM THE TESTED TRACE MODEL
```

The structural composition successfully handles much of origin/channel control, exact `(C,S,I)` agreement, uniqueness, anti-replay, binding and provenance.

The attack survives at the transition:

```text
observable Human-origin event
=> Human decision semantics
```

H1 and H0 can retain the same system-visible Human-side action and the same structural agreement/binding/provenance properties while differing in the semantic proposition being attributed to the Human.

Therefore the broad `PLAUSIBLE FORMALIZATION GAP` can now be narrowed.

## Current gap statement

```text
PLAUSIBLE SEMANTIC-GROUNDING / FORMALIZATION GAP
NOT YET NOVELTY
```

More precisely:

> Existing formal security machinery appears capable of representing Human-side roles/channels, exact referent agreement, unique matching instances, replay resistance, binding and provenance. The tested composition remains unable to justify `HumanDecision(C,S,I)` from the trace unless the decision semantics of the Human-side event are independently grounded rather than assumed by event naming or ceremony specification.

## Strongest attack on the gap hypothesis

The live alternative is:

> existing security-ceremony, formal HCI consent, epistemic/action or agency logics may already provide a principled way to ground the Human-side event semantics.

If so, Project 8 should adopt that model and rerun the composition test.

The current artifacts do not justify a new logic.

## Next bounded literature pass

Search only for formal treatments of:

```text
observable Human action
-> consent / decision / intention semantics
```

especially in:

- security ceremony semantics beyond event labels;
- formal HCI consent;
- epistemic logic of agency;
- action/intention logics;
- authorization-with-intent;
- formal human-protocol interaction;
- usable-security models that distinguish gesture from informed/meaningful consent.

Do not build X1D, V1 or new mechanisms before this pass.
