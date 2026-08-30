# Literature → X1C Gap Analysis

Date: 2026-08-30
Status: RESEARCH ARTIFACT / NO ARCHITECTURE DECISION / NO X1D AUTHORIZATION

## Purpose

Map the X1C lower-bound properties R1–R4 against existing literature and standards before designing any further experiment or mechanism.

X1C rule under review:

```text
HumanDecision(C, S, I) = TRUE
only if there is independent observable Human-origin evidence
of an explicit decision act
bound to exact Content C + Scope S + Decision Instance I,
and the later operative attribution preserves that binding
or records observable supersession.
```

This document does **not** claim scientific novelty. Where no equivalent was located in the present review, the status is `NOT FOUND IN THIS REVIEW`, not `DOES NOT EXIST`.

## Scope and method

Reviewed lines:

- NIST trusted path;
- WebAuthn user presence and user verification;
- FIDO transaction confirmation / WYSIWYS;
- PSD2 / RTS dynamic linking;
- Meaningful Human Control (tracking / tracing and operationalization);
- 2026 Consent Integrity for black-box LLM agents;
- security protocol epistemics / authentication logics;
- Lowe-style agreement and injective agreement;
- strand spaces / authentication tests;
- non-repudiation and evidential transaction logics;
- security ceremonies and formal Human-protocol interaction;
- formal FIDO2 with Human interaction.

Question for every R-property:

1. What does the cited concept actually establish?
2. What does it not establish?
3. Does it provide an explicit analogue of X1C's observational-equivalence falsification rule?

## Summary mapping

| X1C property | Closest existing line | Strongly covered | Residual gap relevant to X1C |
|---|---|---|---|
| R1 — Human-origin evidence | Trusted Path; WebAuthn UP/UV; security ceremonies | protected channel; presence; verification; Human-side protocol role | whether the observed Human-side event itself justifies semantic attribution of decision authorship |
| R2 — explicit decision semantics | FIDO Transaction Confirmation / WYSIWYS; consent workflows | explicit confirmation of a transaction / human-readable content | whether protocol event semantics truthfully ground `Human decided`, rather than merely naming an observable event `accept` |
| R3 — exact referent binding | WYSIWYS; PSD2 dynamic linking; injective agreement/correspondence; Consent Integrity | exact data/referent agreement, unique matching run, concrete transaction/action binding | generalization to arbitrary `content + scope + decision instance` is a modeling step but structurally well precedented |
| R4 — continuity / supersession | bind-to-execution; dynamic linking; injective uniqueness/freshness; provenance | changed action cannot silently inherit old authorization; replay/duplicate runs can be excluded | general semantic supersession remains domain-dependent, but structural continuity is well precedented |

## Key update after deep pass + composition test

The strongest structural prior-art analogue found is **injective agreement / correspondence**, especially when embedded in a **security ceremony** that explicitly models Human interaction.

That combination already supports much of:

```text
origin/peer + exact data + unique instance + matching run
```

Therefore the plausible gap is narrower than originally stated.

A no-new-primitives composition test was performed in:

```text
research/X1C_COMPOSITION_TEST.md
```

using only:

- security ceremony;
- injective agreement/correspondence;
- referent binding;
- non-repudiation/provenance;
- observational-equivalence attack.

The composition successfully covers most structural aspects of R1/R3/R4, but remains blocked at the semantic inference:

```text
observable Human-origin event with protocol-defined acceptance semantics
=> Human decision semantics
```

The test found H1/H0 histories with the same system-visible Human-side action and the same agreement/binding/provenance structure, while differing in whether the Human actually performed the decision semantics later attributed by the System.

This yields the current bounded verdict:

```text
BLOCKED — SEMANTICS CANNOT BE GROUNDED FROM THE TESTED TRACE MODEL
```

This does **not** establish that a new logic is required. It establishes only that event naming + existing structural agreement/binding/provenance properties are insufficient unless the Human-side decision semantics are independently grounded.

## R1 — Human-origin evidence

### Existing concepts

**NIST Trusted Path** defines a mechanism by which a user can communicate directly with security functions with confidence sufficient for the security policy; the path can be activated only by the user or security functions and cannot be imitated by untrusted software.

Source: https://csrc.nist.gov/glossary/term/trusted_path

**WebAuthn** distinguishes:

- `User Presence (UP)` — a simple authorization gesture such as touching an authenticator;
- `User Verification (UV)` — a local authenticator process intended to distinguish users, e.g. PIN/password/biometric.

The specification explicitly notes that UP does not constitute user verification and that even UV does not necessarily identify a unique natural person when multiple natural persons share an authenticator.

Source: https://www.w3.org/TR/webauthn-3/

### What this establishes

These mechanisms can establish stronger evidence about:

- a protected communication path;
- interaction with an authenticator;
- user presence;
- user verification within the authenticator security model.

### What this does not establish

Neither trusted path nor UP/UV alone establishes that a particular event should be interpreted as:

```text
this Human decided this exact proposition
```

A trusted path is a trustworthy channel property, not a universal semantic rule for every event carried over that path.

Likewise:

```text
USER PRESENT != USER VERIFIED != HUMAN DECISION ABOUT THIS CONTENT
```

### X1C status

R1 is **partially covered** by existing primitives. Security ceremonies and trusted paths can strengthen Human-side origin assumptions, but origin alone still does not supply decision semantics.

Observational-equivalence analogue for decision authorship: `NOT FOUND IN THIS REVIEW`.

## R2 — Explicit decision semantics

### Existing concepts

FIDO UAF explicitly separates ordinary authentication from **Transaction Confirmation**. The specification explains that ordinary authentication may authorize an application/session broadly, while transaction confirmation is used where the relying party needs evidence that the user saw and accepted particular human-readable content. This is described as What You See Is What You Sign (WYSIWYS).

Sources:

- https://fidoalliance.org/specs/fido-uaf-v1.1-id-20170202/fido-uaf-protocol-v1.1-id-20170202.html
- https://fidoalliance.org/specs/fido-uaf-v1.2-id-20180220/fido-uaf-overview-v1.2-id-20180220.html

### What this establishes

The literature already recognizes the crucial distinction:

```text
authenticated session != confirmation of this particular action/content
```

This strongly supports X1C R2 as a known requirement class.

### What this does not establish

The composition test shows a subtler residual issue:

```text
EVENT LABEL = "accept"
```

is not itself proof that the observable event truthfully grounds the semantic proposition:

```text
Human decided C,S,I
```

A Human may perform the same observable action while interpreting it as continue/acknowledge/dismiss/routine confirmation, or while understanding the proposition differently from the System-attributed decision meaning.

Existing transaction-confirmation work may solve this adequately inside bounded transaction semantics. The current review has not yet shown a domain-independent formal rule for arbitrary AI-assisted decisions.

### X1C status

R2 is **well precedented as an interaction requirement**, but the formal semantic-grounding step remains the main unresolved part of the tested composition.

## R3 — Exact referent binding

### Existing concepts

**PSD2 dynamic linking** requires, for remote electronic payments, strong customer authentication linked to a specific amount and payee. EBA guidance states that the authentication code is specific to the amount and payee agreed to by the payer, and that accepted authentication must correspond to those original parameters.

FIDO WYSIWYS / Transaction Confirmation likewise binds displayed transaction text to the authentication result.

Injective agreement/correspondence adds a formal structural analogue: one unique matching run agrees on exact data values.

### X1C status

R3 is **strongly precedented**. Project 8 should not claim novelty in exact referent binding or unique matching instances.

## R4 — Integrity / supersession visibility

Dynamic linking, bind-to-execution, injective uniqueness/freshness and provenance already provide strong structural prior art for:

```text
approval of A does not automatically authorize changed A-prime
```

and for replay/duplicate-instance resistance.

### X1C status

R4 is **strongly precedented structurally**. General semantic supersession remains domain-dependent, but this is no longer the strongest candidate gap.

## Meaningful Human Control

Meaningful Human Control (MHC) introduces the `tracking` and `tracing` conditions.

Tracking asks whether a human-AI system responds to relevant Human reasons. Tracing asks whether system behavior/capabilities/effects are traceable to a relevant Human agent with appropriate moral and technical understanding.

MHC remains conceptually important, but it is not a drop-in technical proof rule for:

```text
HumanDecision(C,S,I) = TRUE
```

## Consent Integrity for LLM agents

The closest agent-specific work found is:

**Xiaoqi Weng, "What You Approve Is What Executes: Consent Integrity for Black-Box LLM Agents" (2026).**

Source: https://arxiv.org/abs/2606.02668

The paper defines Consent Integrity by combining WYSIWYS and trusted-path ideas for LLM-agent approvals. The Human-visible action should be rendered from the real operation at the system boundary by a trusted mediator, not from agent narration, and bound to the exact action that executes.

This substantially narrows any plausible novelty claim for Project 8.

## Observational-equivalence criterion

X1C uses the falsification question:

> Given the same system-visible observations, can a physically possible history exist in which the attributed Human decision did not occur?

If yes, the observations are insufficient to justify `HumanDecision=TRUE`.

Observational equivalence itself is standard formal machinery. The potentially distinctive use here is its application as a falsifier of **semantic decision authorship**.

### Current result

`STANDARD DECISION-AUTHORSHIP EQUIVALENT NOT FOUND IN THIS REVIEW`

This must **not** be promoted to:

```text
NO SUCH WORK EXISTS
```

or:

```text
PROJECT 8 IS NOVEL
```

## Gap statement after composition test

The earlier broad statement:

```text
PLAUSIBLE FORMALIZATION GAP / NOT YET NOVELTY
```

can now be narrowed to:

> Existing formal machinery appears sufficient for protected Human-side roles/channels, agreement on exact data, unique matching instances, referent binding, replay resistance and provenance. The tested composition remains unable to derive semantic Human decision authorship from the trace unless the Human-side event's decision semantics are independently grounded rather than assumed by naming/specification.

Current status:

```text
PLAUSIBLE SEMANTIC-GROUNDING / FORMALIZATION GAP
NOT YET NOVELTY
```

## Implication for X1D

X1D should **not be built yet**.

Before authorizing X1D, perform a bounded deep pass specifically around:

- formal HCI consent semantics;
- security-ceremony semantics beyond event labels;
- epistemic/action logics of agency and intention;
- authorization-with-intent;
- formal models connecting observable action to consent/decision semantics;
- human-protocol interaction models that explicitly avoid importing intent by event naming.

If an established model grounds the Human-side event sufficiently, Project 8 should adopt it and rerun the composition test.

If not, the gap claim can be strengthened carefully to a specific **Human decision-event semantic grounding gap**.

## Current recommendation

```text
DO NOT BUILD X1D.
DO NOT DESIGN AUTHENTICATION/BINDING MECHANISMS.
DO NOT CLAIM NOVELTY.

NEXT:
BOUND THE RESEARCH AROUND HUMAN DECISION-EVENT SEMANTIC GROUNDING.
```
