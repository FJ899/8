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

## 1. BAN-style and epistemic authentication logics

Authentication logics reason about what principals can conclude or believe from protocol evidence. Later epistemic foundations provide semantics in terms of possible states/worlds rather than treating protocol messages as self-interpreting assertions.

Relevant source:

- Halpern & van der Meyden, `An Epistemic Foundation for Authentication Logics` — https://arxiv.org/abs/1707.08750

### Relevance

This family is close to the *form* of the X1C question because it asks when observed protocol evidence warrants a conclusion about another principal.

### Residual mismatch

The reviewed material does not provide a domain-independent primitive equivalent to:

```text
Human decided Content C within Scope S for Decision Instance I
```

The logics require a protocol semantics / interpretation of events. They can reason from an event once that event has been modeled with meaning, but do not by themselves solve the Human-origin + decision-semantics grounding problem.

Status relative to X1C:

```text
CLOSE FORMAL FAMILY / NOT DROP-IN EQUIVALENT
```

## 2. Lowe agreement hierarchy — strongest close formal analogue found

Lowe-style authentication distinguishes increasingly strong properties including aliveness, weak agreement, non-injective agreement and injective agreement.

A standard formulation of non-injective agreement says, informally: when one principal completes a run apparently with a peer and on data `M`, the peer must previously have been running the corresponding role and the principals agree on `M`.

Injective agreement strengthens this so that each completed run corresponds to a **unique** matching peer run. Formalizations may additionally require recentness.

Reference overview / formal trace formulation:

- Crypto Engineering security-protocol notes summarizing Lowe hierarchy and Tamarin-style agreement claims: https://www-verimag.imag.fr/~ene/m2p/main.pdf

### Mapping to X1C

Injective agreement is unexpectedly close to three X1C requirements:

```text
peer/role origin          ~ R1 origin
agreement on data M       ~ R3 exact referent
unique corresponding run  ~ decision instance / anti-replay
```

It also naturally supports causal ordering and recentness.

### Why it is not yet `HumanDecision(C,S,I)=TRUE`

The crucial difference is semantic grounding.

Injective agreement proves a relation between **modeled protocol roles/runs and agreed data**. It does not independently establish that a Human protocol event means:

```text
I decide / accept this proposition
```

If the model labels some Human-side event as a `running`, `commit`, or consent event, the formalism can verify correspondence. But the semantic legitimacy of treating the observed Human interaction as a decision event is outside the agreement property itself.

Therefore:

```text
INJECTIVE AGREEMENT != HUMAN DECISION SEMANTICS
```

but it is the strongest formal prior-art candidate found for the structural core of:

```text
origin + referent + unique instance
```

Status:

```text
VERY CLOSE STRUCTURAL PRIOR ART / PARTIAL ADOPTION CANDIDATE
```

## 3. Strand spaces and authentication tests

Authentication tests infer that certain regular protocol nodes/events must exist when a trace contains cryptographically constrained challenge/response transformations.

Sources:

- Guttman, `Authentication Tests`: https://web.cs.wpi.edu/~guttman/pubs/auth_tests.pdf
- Thayer, Herzog, Guttman, Strand Spaces literature.

### Relevance

This is epistemically close to R1 because the proof shape is:

```text
observed trace
=> some corresponding regular event must have existed
```

That is substantially stronger than a self-asserted `approver="human"` field.

### Residual mismatch

The inference establishes the existence of a protocol participant/event under cryptographic assumptions. It does not establish that the event is a **Human decision** unless that semantics has already been validly grounded in the ceremony/protocol model.

Status:

```text
STRONG EVENT-EXISTENCE ANALOGUE / NOT DECISION-AUTHORSHIP EQUIVALENT
```

## 4. Non-repudiation and evidence logics

Non-repudiation work formalizes evidence that a principal originated, submitted, received, approved, or otherwise participated in a transaction. Standards and protocol proofs distinguish evidence of origin and receipt and often bind evidence to concrete message content and transaction labels.

Relevant lines:

- ISO/ITU non-repudiation service concepts, including evidence of approval/origin;
- formal proofs of non-repudiation protocols such as Zhou-Gollmann;
- accountability / evidence logics.

Example standard reference:

- ITU-T X.842 / ISO non-repudiation framework.

### Relevance

This is close to R1 + R3 because it explicitly asks what evidence is valid for attributing an action/content to a principal.

### Residual mismatch

Cryptographic evidence of origin generally establishes that a key/principal generated or authorized a protocol artifact under the security model. It does not automatically establish private Human intent or semantic decision authorship.

This supports an important X1C distinction:

```text
EVIDENCE OF ORIGIN != EVIDENCE OF HUMAN DECISION SEMANTICS
```

Status:

```text
STRONG PRIOR ART FOR ATTRIBUTION EVIDENCE / NOT FULL X1C RULE
```

## 5. Cyberlogic / evidential transactions

`Evidential Transactions with Cyberlogic` provides an attestation/knowledge logic for distributed transactions, authorization, delegation, revocation and verifiable evidence assembled by distributed proof search.

Source:

- Ruess & Shankar, `Evidential Transactions with Cyberlogic`: https://arxiv.org/abs/2304.00060

### Relevance

Cyberlogic is a strong candidate substrate for expressing a future X1C-style evidence predicate. It already treats authorization and evidence as logical objects rather than informal audit fields.

### Residual mismatch

The reviewed formulation still treats attestations/signatures and authorization facts as externally grounded evidence primitives. It does not supply a standard Human-decision-authorship predicate or solve when a Human-computer event is semantically a decision.

Status:

```text
POSSIBLE FORMAL SUBSTRATE / NO DIRECT EQUIVALENT FOUND
```

## 6. Observational equivalence in security protocols

Observational equivalence is mature prior art in cryptographic and protocol security. Two systems/runs can be considered equivalent when an observer/adversary cannot distinguish them from available observations. This is widely used for privacy, anonymity, secrecy and process equivalence.

Examples include applied pi-calculus style equivalence and epistemic formulations of protocol indistinguishability.

### Critical finding

Therefore **X1C did not invent observational equivalence**.

The potentially distinctive step is its use as a **sufficiency falsifier for decision attribution**:

```text
if observations O are compatible with
H1: HumanDecision(C,S,I) occurred
and
H0: HumanDecision(C,S,I) did not occur,
then O does not justify HumanDecision(C,S,I)=TRUE.
```

This is essentially an epistemic indistinguishability argument applied to Human decision provenance.

### Search result

Within this pass, no standard named criterion was found that combines:

1. Human-origin event attribution;
2. explicit decision semantics;
3. exact referent/instance binding;
4. an indistinguishable-history falsifier for the decision predicate itself.

Status:

```text
OBSERVATIONAL EQUIVALENCE = ESTABLISHED PRIOR ART
APPLICATION AS HUMAN-DECISION EVIDENCE SUFFICIENCY TEST = NOT FOUND IN THIS PASS
```

This is **not a novelty claim**.

## 7. Security ceremonies — key bridge between protocol logic and Human action

Security-ceremony research extends protocol models to include Human actors and communication surfaces that ordinary protocol models treat as out-of-band. Formal ceremony work also models Human deviations/mutations and analyzes whether expected authentication/security claims still hold.

Relevant lines:

- Bella et al., layered/security-ceremony analysis;
- formal analysis of Human-protocol interaction;
- recent mutation-based human-centric ceremony verification.

### Relevance

This line attacks exactly the hidden assumption that a technically valid protocol event automatically corresponds to the intended Human interaction.

It is therefore highly relevant to X1C R1/R2.

### Residual gap

Ceremony analysis provides machinery to model Humans explicitly, but the reviewed work does not establish a universal criterion for when an observed Human interaction has **decision semantics** for arbitrary AI-assisted content/scope/instance.

Status:

```text
CRITICAL ADJACENT FIELD / NO UNIVERSAL DECISION-AUTHORSHIP RULE FOUND
```

## 8. Formal FIDO2 with Human interaction — closest domain-specific consent formalization

A particularly important prior-art result is formal analysis of FIDO2 that explicitly models the Human and discusses user consent using agreement-style properties.

Source:

- Schrempp, `Formal Verification of FIDO2 with Human Interaction` (2023): https://www.research-collection.ethz.ch/bitstreams/952083ec-7dea-4f73-85cf-83224610b096/download

The work is reported to model user consent via an injective-agreement relation among relevant protocol actors while explicitly including Human interaction.

### Why this matters

This substantially narrows the X1C gap claim.

It shows that the literature has already combined:

```text
Human interaction
+ consent semantics
+ formal agreement / unique run correspondence
```

in at least a domain-specific authentication setting.

Therefore Project 8 must **not** claim that formal Human consent + unique protocol instance binding is unexplored.

### Remaining question

What remains potentially distinct is whether there is a **domain-independent epistemic rule** for arbitrary AI-assisted decisions that refuses `HumanDecision(C,S,I)=TRUE` whenever the evidence admits an observationally indistinguishable no-decision history.

Status:

```text
MAJOR PRIOR ART / X1C GAP NARROWED
```

## Deep-pass synthesis

The deep pass changes the state-of-the-art map.

### What is clearly prior art

```text
belief/knowledge reasoning about protocol evidence
agreement on exact data
injective uniqueness / anti-replay correspondence
proof that corresponding protocol events must exist
non-repudiation / evidence of origin
formal authorization/evidential transactions
observational equivalence / indistinguishable runs
formal inclusion of Humans in security ceremonies
formal consent properties in at least FIDO2-style Human interaction
```

### What was NOT found as a standard drop-in rule in this pass

A domain-independent rule equivalent to:

```text
HumanDecision(C,S,I)=TRUE
```

where truth is justified only when the available observations rule out an observationally equivalent history in which that Human decision did not occur, while keeping distinct:

```text
origin
semantics
referent/instance
continuity/supersession
```

## Revised gap status

The original label remains correct, but the candidate gap is now much narrower:

```text
PLAUSIBLE FORMALIZATION GAP / NOT YET NOVELTY
```

More precisely:

> The potential gap is not authentication, agreement, non-repudiation, observational equivalence, consent confirmation, or Human-in-protocol modeling individually. The potential gap is a domain-independent epistemic composition rule for Human decision attribution in AI-assisted systems, with explicit negative sufficiency testing by indistinguishable no-decision histories.

## ATTACK THE FRAME

A serious alternative explanation must remain live:

> X1C may ultimately be expressible as an ordinary composition of existing ceremony modeling + injective agreement + transaction/content binding + non-repudiation evidence, with no genuinely new formal primitive required.

If that composition is sufficient, Project 8 should **adopt that composition** rather than coin a new logic.

This is currently the strongest threat to a novelty claim and should be treated as a positive research outcome, not a failure.

## Decision consequence

```text
DO NOT BUILD X1D.
DO NOT BUILD V1.
DO NOT DESIGN NEW AUTHENTICATION / SIGNATURE / BROKER MECHANISMS.
DO NOT CLAIM NOVELTY.
```

Next research question:

> Can `HumanDecision(C,S,I)` be represented faithfully using existing security-ceremony + injective-agreement / correspondence properties, with observational equivalence used only as the counterexample method?

If YES:

```text
ADOPT EXISTING FORMALISM
```

If NO, and the failure is precisely identified:

```text
FORMALIZATION GAP STRENGTHENED
```

Only after that comparison should X1D be reconsidered.
