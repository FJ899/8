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
- 2026 Consent Integrity for black-box LLM agents.

Question for every R-property:

1. What does the cited concept actually establish?
2. What does it not establish?
3. Does it provide an explicit analogue of X1C's observational-equivalence falsification rule?

## Summary mapping

| X1C property | Closest existing line | Strongly covered | Residual gap relevant to X1C |
|---|---|---|---|
| R1 — Human-origin evidence | Trusted Path; WebAuthn UP/UV | protected channel; presence; verification of an authenticator user | whether the observed event itself justifies attribution of Human decision authorship |
| R2 — explicit decision semantics | FIDO Transaction Confirmation / WYSIWYS; consent workflows | explicit confirmation of a transaction / human-readable content | generic interaction or identity evidence still does not by itself establish decision semantics for arbitrary AI-assisted decisions |
| R3 — exact referent binding | WYSIWYS; PSD2 dynamic linking; Consent Integrity | binds approval/authentication to concrete transaction/action content or parameters | generalization to arbitrary `content + scope + decision instance` remains a modeling step, not directly supplied by payment standards |
| R4 — continuity / supersession | PSD2 invalidation on changed parameters; bind-to-execution | changed amount/payee invalidates prior code; approved action can be bound to executed action | a general provenance/supersession rule for arbitrary decisions is not supplied as a universal model |

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

R1 is **partially covered** by existing primitives, but the step from trustworthy/user-origin interaction evidence to *decision authorship of a specific decision event* is not supplied as a general rule by these sources.

Observational-equivalence analogue: `NOT FOUND IN THIS REVIEW`.

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

It does not imply that every explicit-looking interaction in an AI workflow has decision semantics. A `continue`, navigation event, acknowledgement, or generic authenticated action still requires separate interpretation.

### X1C status

R2 is **well precedented**. Project 8 should not treat explicit decision semantics as a newly discovered property.

Observational-equivalence analogue: `NOT FOUND IN THIS REVIEW` as a general falsification rule for arbitrary decision semantics.

## R3 — Exact referent binding

### Existing concepts

**PSD2 dynamic linking** requires, for remote electronic payments, strong customer authentication linked to a specific amount and payee. EBA guidance states that the authentication code is specific to the amount and payee agreed to by the payer, and that accepted authentication must correspond to those original parameters.

Sources:

- https://www.eba.europa.eu/single-rule-book-qa/qna/view/publicId/2020_5133
- https://www.eba.europa.eu/single-rule-book-qa/qna/view/publicId/2019_4556

FIDO WYSIWYS / Transaction Confirmation likewise binds displayed transaction text to the authentication result.

Source: https://fidoalliance.org/wp-content/uploads/2019/01/How_FIDO_Meets_the_RTS_Requirements_December2018.pdf

### What this establishes

The core idea behind R3 is already technically mature in transaction security:

```text
generic YES != YES to these exact parameters
```

Concrete parameters are included in or cryptographically bound to the authorization/confirmation process.

### What this does not establish

Payment standards define domain-specific referents such as amount and payee. X1C generalizes the referent to:

```text
Content C + Scope S + Decision Instance I
```

That generalization is plausible but is not itself directly specified by PSD2.

### X1C status

R3 is **strongly precedented**. The likely contribution, if any, is not the existence of binding but a domain-independent decision-evidence model for AI-assisted work.

Observational-equivalence analogue: `NOT FOUND IN THIS REVIEW`.

## R4 — Integrity / supersession visibility

### Existing concepts

PSD2 dynamic linking requires that any change to relevant transaction parameters such as amount or payee invalidates the generated authentication code.

Source: https://www.eba.europa.eu/single-rule-book-qa/qna/view/publicId/2019_4556

The 2026 Consent Integrity paper requires the action shown to the Human to be bound to the exact action that executes, rather than trusting an agent-authored narrative.

Source: https://arxiv.org/abs/2606.02668

### What this establishes

There is strong prior art for the principle:

```text
approval of A does not automatically authorize changed A-prime
```

and for binding approval to execution.

### What this does not establish

The cited work does not appear to supply a universal decision-history model covering arbitrary semantic supersession, stale consent, scope expansion, replacement and provenance beyond the concrete action/transaction binding problem.

### X1C status

R4 is **strongly precedented at the transaction/action level**. A generic supersession/provenance rule remains a modeling question.

Observational-equivalence analogue: `NOT FOUND IN THIS REVIEW`.

## Meaningful Human Control

Meaningful Human Control (MHC) introduces the `tracking` and `tracing` conditions.

Tracking asks whether a human-AI system responds to relevant Human reasons. Tracing asks whether system behavior/capabilities/effects are traceable to a relevant Human agent with appropriate moral and technical understanding.

Sources:

- https://link.springer.com/article/10.1007/s43681-022-00167-3
- https://link.springer.com/article/10.1007/s10676-019-09519-w

### Relevance to X1C

MHC is conceptually close because it resists shallow `human in the loop` claims and requires meaningful relations between Human reasons/responsibility and system behavior.

However, the cited operationalization work itself notes that translating tracking/tracing into general system-level design properties is non-trivial and remains incomplete across contexts.

MHC therefore supports the importance of provenance/control relations but is not, in this review, a drop-in technical criterion for:

```text
HumanDecision(C,S,I) = TRUE
```

## Consent Integrity for LLM agents

The closest agent-specific work found is:

**Xiaoqi Weng, "What You Approve Is What Executes: Consent Integrity for Black-Box LLM Agents" (2026).**

Source: https://arxiv.org/abs/2606.02668

The paper defines Consent Integrity by combining WYSIWYS and trusted-path ideas for LLM-agent approvals. The Human-visible action should be rendered from the real operation at the system boundary by a trusted mediator, not from agent narration, and bound to the exact action that executes.

Important limitation stated by the paper: the prototype implements analyzer/renderer/bind-to-execution, while total mediation and the trusted path are specified/assumed rather than fully implemented.

### Mapping to X1C

- R1: partially addressed through the trusted-path assumption, but not eliminated as an engineering/epistemic problem;
- R2: explicit approval is central;
- R3: strongly covered through truthful rendering and exact-action approval;
- R4: strongly covered through bind-to-execution.

This work substantially narrows any plausible novelty claim for Project 8. Any future contribution must be framed relative to Consent Integrity rather than as if LLM approval binding were unexplored.

## Observational-equivalence criterion

X1C uses the falsification question:

> Given the same system-visible observations, can a physically possible history exist in which the attributed Human decision did not occur?

If yes, the observations are insufficient to justify `HumanDecision=TRUE`.

Searches in this review combined terms around observational equivalence with consent, authorization, Human decision provenance, authentication and AI agents.

### Result

`STANDARD EQUIVALENT NOT FOUND IN THIS REVIEW`

This must **not** be promoted to:

```text
NO SUCH WORK EXISTS
```

or:

```text
PROJECT 8 IS NOVEL
```

Observational equivalence is a broad formal concept used in many technical fields. A more systematic literature search across epistemic logic, security protocol analysis, non-repudiation, provenance, accountability and formal authorization could still reveal a close equivalent.

## Gap statement after this review

The current evidence supports a narrower statement than a novelty claim:

> Existing work separately provides mature concepts for protected paths, user presence/verification, transaction confirmation, exact referent binding, execution binding and meaningful Human control. The present review did not identify a standard domain-independent rule that composes these into an epistemic predicate `HumanDecision(C,S,I)=TRUE` and falsifies that predicate whenever the same observations admit an equivalent history without the attributed Human decision.

Status:

```text
PLAUSIBLE GAP / NOT YET NOVELTY
```

## Implication for X1D

X1D should **not be built yet**.

Before authorizing X1D, decide whether the plausible gap above survives a deeper search specifically in:

- security protocol epistemics / authentication logics;
- non-repudiation and intent/authorship evidence;
- formal provenance and accountability;
- usable security / ceremony analysis;
- human-computer interaction consent semantics;
- agentic AI approval/oversight literature.

If an established formal model already provides the needed predicate, Project 8 should adopt or adapt it rather than invent a parallel vocabulary.

If not, X1D can then be framed as a test of a specific state-of-the-art gap rather than as a new mechanism-design exercise.

## Current recommendation

```text
DO NOT BUILD X1D.
DO NOT DESIGN AUTHENTICATION/BINDING MECHANISMS.
DO NOT CLAIM NOVELTY.

NEXT:
DEEPEN LITERATURE SEARCH AROUND THE OBSERVATIONAL-EQUIVALENCE / EPISTEMIC-AUTHORSHIP GAP.
```
