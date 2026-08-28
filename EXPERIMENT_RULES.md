# Agency Kernel v0 — Experiment Rules

Status: **FROZEN**

## 1. One Gate, one implementation PR

Each Gate has a dedicated bounded implementation PR.

A later Gate may extend the accepted trace of an earlier Gate, but may not silently implement future-Gate behavior before that behavior is in scope.

## 2. Gate preregistration

Before implementation starts, the Gate Contract must already define:

- base/candidate binding rule;
- claim under attack;
- frozen invariants;
- attack classes;
- expected fail semantics;
- exit criteria;
- out-of-scope items;
- architecture changes forbidden during the Gate.

If the contract is discovered to be wrong, that is a finding or explicit preregistration defect. The test meaning may not be silently changed after observing a failure.

## 3. Candidate fixation

Before adversarial audit, freeze:

- exact repository HEAD;
- exact repository tree;
- exact workflow/container definitions relevant to the Gate;
- exact controlled dependency/action/image identities required by the Gate.

A change to any candidate-defining element creates a new Experiment Candidate.

## 4. Audit terminology

The standard audit is:

`FRESH-CONTEXT ADVERSARIAL AUDIT`

or:

`CONTEXT-SEPARATED ADVERSARIAL AUDIT`

A separate session is not automatically an independent trust root.

## 5. Finding-first rule

On first failure:

`FAIL → DURABLE FINDING → only then correction`

A failure may not disappear from history because an implementer immediately fixes it.

## 6. Minimal finding requirements

Every finding records:

- Finding ID;
- Gate;
- exact candidate HEAD/tree;
- claim attacked;
- minimal execution trace;
- expected result;
- observed result;
- invariant violated;
- classification;
- minimal reproducer;
- disposition.

## 7. Implementation authority

The implementation session may:

- implement the preregistered contract;
- run tests;
- report observations;
- prepare a candidate.

The implementation session may not:

- ACCEPT its own Gate;
- modify frozen architecture;
- redefine PASS/FAIL semantics;
- weaken/remove a failing attack to obtain green;
- classify its own failure as accepted;
- merge its own Gate by procedural implication.

## 8. Human acceptance

Only Human authority closes a Gate.

Neither Copilot, ChatGPT, GitHub Actions, a verifier script, nor a green workflow may substitute for Human Gate acceptance.

## 9. Reopening architecture

New architecture is not an argument by itself.

Reopening the architecture freeze requires:

- a concrete falsification;
- a failing test that exposes an architectural defect; or
- a measured blocker that cannot be resolved within the frozen model.

## 10. No false proof language

Do not state:

`tests passed → system proven secure`

Allowed phrasing is bounded and falsification-oriented, e.g.:

`No accepted tested adversarial trace falsified Claim B under the preregistered topology and recorded execution substrate.`
