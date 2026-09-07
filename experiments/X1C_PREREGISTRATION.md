# X1C — Human Decision Evidence Boundary

Status: `PREREGISTERED / HUMAN AUTHORIZED / NOT YET EXECUTED`

Date: 2026-08-30

## Motivation

X1B established that the current ScriptOps approval path can record a durable Human-attributed approval state without itself establishing that the observed approval operation was a Human decision act about the exact operative content. X1C does not ask how to secure that path. It asks what must be observable before `HumanDecision = TRUE` is epistemically justified.

X1C preserves the distinction:

```text
IDENTIFIED HUMAN != HUMAN ACT
HUMAN ACT != HUMAN DECISION ABOUT THIS CONTENT
HUMAN DECISION ABOUT A != HUMAN DECISION ABOUT A-prime
```

## Research question

> What minimum observable evidence is sufficient to justify `HumanDecision(content, scope) = TRUE`?

Equivalent falsification question:

> For a proposed evidence set E, can there exist another physically possible history with the same observable E in which the Human did not make the attributed decision about that exact content and scope?

If yes, E is insufficient.

## Scope

X1C is an epistemic-boundary experiment. It does not infer a private mental state. It asks only what observable facts are sufficient for a system to justify an attribution.

X1C does not reopen Agency Kernel v0 and does not redesign ScriptOps approval.

## Forbidden premature solutions

The experiment must not presuppose or select any implementation such as:

- login or account identity;
- MFA;
- biometrics;
- cryptographic signatures;
- hashes as the answer by themselves;
- trusted hardware;
- append-only ledgers;
- approval UI;
- separate devices;
- human-in-the-loop workflow products.

Those may later be candidate mechanisms, but X1C first determines the required observable properties.

## Method — observational-equivalence test

For each candidate evidence class or combination:

1. define exactly what the system can observe;
2. construct History H1 in which the Human really makes decision D about exact content C and scope S;
3. attempt to construct History H0 with the same system-visible observations but without that Human decision D(C,S);
4. if H0 is possible, the evidence is insufficient;
5. if H0 cannot be constructed without changing at least one required observation, record the surviving observable property;
6. minimize the surviving property set by removing one property at a time and repeating the attack.

The goal is not to prove metaphysical authorship. The goal is to identify a minimal observable lower bound for justified attribution.

## Candidate observable-property classes to test

These are hypotheses to attack, not preregistered conclusions.

### O1 — operation occurrence

The approval operation occurred.

### O2 — actor/source distinguishability

The system can distinguish the source that produced the approval act from other processes with equivalent capability.

### O3 — explicit decision act

There is a distinct observable act whose semantics are acceptance/decision, not merely continuation, viewing, silence, or generic interaction.

### O4 — content visibility

The exact decision content presented for the act is observable.

### O5 — scope visibility

The exact scope presented for the act is observable.

### O6 — decision-to-content binding

The observed act is bound to the exact content and scope later attributed as the decision.

### O7 — post-act integrity / mutation detectability

A later A-prime cannot be treated as the accepted A without an observable change that invalidates or supersedes the prior attribution.

### O8 — freshness / non-reuse

An old Human decision act cannot be silently reused as evidence for a new decision instance.

### O9 — attribution provenance

The system can distinguish evidence produced by the Human decision path from a mere assertion such as `approver="human"` written by the same process that performs the effect.

## Preregistered attack families

At minimum, X1C must try to falsify sufficiency using these histories:

1. same command/effect, different invoker;
2. authenticated/identified Human account, but approval executed by automation using that account/session;
3. Human performs an act, but the act is only `continue` / acknowledge / view;
4. Human explicitly accepts, but content was not the content later attributed;
5. Human accepts A, system later treats A-prime as accepted;
6. Human accepts one scope, system expands scope;
7. old acceptance is replayed for a new decision instance;
8. system writes `approver=human` without independent evidence of a Human decision act;
9. Human act exists, but exact accepted content cannot be reconstructed afterward;
10. exact content exists, but no evidence links that content to the Human act.

## Positive-control requirement

A candidate evidence set cannot be considered sufficient unless there is also a positive history where:

```text
exact content + exact scope are presented
→ a distinct decision act occurs
→ the act is observably attributable to the Human decision path
→ the act is bound to that exact content + scope + decision instance
→ later attributed content remains the same or any change invalidates/supersedes the prior decision
→ HumanDecision(content, scope) = TRUE
```

## PASS

`X1C PASS` means the experiment identifies a bounded minimal observable property set for which no preregistered observationally-equivalent no-Human-decision history can be constructed, and removing any member reintroduces at least one credible counterhistory.

PASS is bounded to the tested model. It does not prove private mental intent, informed consent, legal validity, identity assurance, product safety, or universal authorship.

## FAIL

`X1C FAIL — EVIDENCE SET NOT SUFFICIENT`

Use when a proposed candidate evidence set is shown insufficient. This is an expected intermediate outcome and does not terminate X1C unless all candidate property sets fail to produce a bounded lower bound.

## BLOCKED

`X1C BLOCKED — OBSERVABLE DECISION EVIDENCE NOT TESTABLE`

Use if the available real workflow cannot expose enough state to run the observational-equivalence test without inventing the result.

## Stop / discipline

During X1C:

- do not design the final authentication mechanism;
- do not implement a ScriptOps fix;
- do not build Agency Kernel v1;
- do not claim that a particular technology is required merely because it could implement a surviving property;
- separate `required observable property` from `candidate implementation mechanism`;
- record counterexamples before any corrective proposal.

## Exit

After X1C result is recorded, a separate Human decision is required before selecting a mechanism or changing any runtime component.
