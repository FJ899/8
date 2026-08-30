# Future Idea — Knowledge-Routed Attack / Research Method

Status: FUTURE IDEA ONLY

This note records a candidate methodology for future Agency Kernel / ScriptOps-style research work. It is not an active Gate contract, does not modify the frozen v0 validation program, and does not authorize implementation by itself.

## Motivation

The productive pattern observed during X1B–X1D was not a fixed `ATTACK <-> RESEARCH` loop. The useful behavior was that each new uncertainty was routed to the smallest method capable of reducing it.

Research was valuable when it changed the object under study, removed an unnecessary invention, narrowed the claim, changed the threat model, or changed what would be tested or built.

The method should therefore be cyclic only when knowledge actually changes.

## Candidate routing rule

```text
CLAIM
  |
  v
FRAME ATTACK
only if definition / scope / assumptions are uncertain
  |
  v
TARGETED RESEARCH
only if unknown state of the art may change claim / test / design
  |
  v
PREREGISTERED FALSIFICATION TEST
  |
  v
REALITY
  |
  v
ATTACK THE INTERPRETATION
  |
  v
DECISION GATE
```

## Decision Gate

The Decision Gate asks which state has been reached:

```text
A — CLAIM FALSIFIED
    -> record finding / STOP

B — NEW FUNDAMENTAL UNCERTAINTY
    -> route to FRAME ATTACK and/or TARGETED RESEARCH

C — UNDERSTANDING STABLE ENOUGH
    -> STOP RESEARCH
    -> DESIGN / IMPLEMENT / TEST
```

## Routing by uncertainty type

```text
NEW FINDING

Does it undermine the definition of the problem?
-> ATTACK THE FRAME

Does it introduce a concept or mechanism whose state of the art is unknown?
-> TARGETED RESEARCH

Could the experiment result be over-interpreted?
-> ATTACK THE INTERPRETATION

Is the problem already local and well defined?
-> TEST / IMPLEMENTATION
```

`ATTACK THE FRAME` and `TARGETED RESEARCH` are not mandatory as a pair.

## Research saturation rule

Every additional research cycle must materially reduce uncertainty or change a decision.

Material change means at least one of:

- claim;
- threat model;
- falsification test;
- decision;
- implementation scope;
- object that would be built.

If another research pass cannot materially change any of these:

```text
NO MATERIAL KNOWLEDGE CHANGE
-> RESEARCH SATURATION
-> STOP RESEARCH
-> REALITY TEST / IMPLEMENT
```

## GOLD

```text
NEW UNCERTAINTY -> ROUTE TO ATTACK / RESEARCH
STABLE UNDERSTANDING -> TEST / BUILD
```

And the stronger guardrail:

> Research may delay implementation only while its result can still materially change what we intend to build, the claim we intend to test, the threat model, or the decision.

## Intended effect

The method is meant to preserve the advantages observed in the X1B–X1D line:

- avoid reinventing established theory or mechanisms;
- detect when the wrong problem is being solved;
- narrow claims before implementation;
- force reality checks after conceptual stabilization;
- prevent elegant but endless research loops.

This is a future methodology candidate, not a new frozen project invariant.