# Agency Kernel v0 — Canonical Architecture

Status: **FROZEN**

This document defines the semantic and enforcement properties of Agency Kernel v0. It does not freeze implementation language, database technology, IPC mechanism, container runtime, or runner provider.

## 1. Purpose

Agency Kernel mediates transitions from a request to a modeled real-world effect without conflating:

- authority,
- technical capability,
- occurrence of effect,
- effect compliance,
- outcome satisfaction.

The system does not control how the Executor thinks. It controls transitions into modeled effectful action.

## 2. Canonical relations

### MAY

`MAY(requesting_principal, effect_intent, authority_state)`

Question: does the requesting principal have normative authority to request the effect?

### CAN

`CAN(effecting_principal, technical_operation, resource, capability_state)`

Question: does the effecting principal possess the technical capability required for the operation on the resource?

### DID

`DID(attempt, attributable_effect)`

Question: can the observed effect be attributed to the attempt?

### WITHIN_SCOPE

`WITHIN_SCOPE(attempt, observed_effects, effect_contract)`

Question: did attributable effects remain within the authorized effect envelope?

### SATISFIED

`SATISFIED(evidence, evidence_contract)`

Question: does the evidence establish the required outcome?

No relation automatically implies another.

## 3. Fundamental separations

- `AUTHORITY HOLDER ≠ CREDENTIAL HOLDER`
- `CAPABILITY ≠ AUTHORITY`
- `ATTEMPT ≠ EFFECT`
- `OBSERVED DELTA ≠ ATTRIBUTED EFFECT`
- `COMPLIANCE ≠ ACCEPTANCE`
- `SATISFIED ≠ AUTHORIZED`
- `SATISFIED ≠ WITHIN_SCOPE`

A requester may have `MAY(...) = TRUE` while direct `CAN(...) = FALSE`.

The trusted Broker may have `CAN(...) = TRUE` but may exercise target capabilities only pursuant to a valid `OperationAdmission`.

Therefore:

`requester MAY + broker CAN ≠ permission to execute`

## 4. Legal effect chain

The canonical path is:

`authenticated request`
→ `MAY`
→ `ActionAuthorization`
→ atomic `AuthorizationConsumed + AttemptStarted`
→ operation proposal
→ `CAN`
→ `OperationAdmission`
→ capability exercise
→ effect
→ observation
→ attribution
→ `WITHIN_SCOPE`
→ `SATISFIED`

No shortcut is valid.

## 5. Single-use authorization

`ActionAuthorization` is single-use.

The system must atomically:

1. verify authorization exists and is unused;
2. verify authority is active;
3. verify start preconditions;
4. append `AuthorizationConsumed`;
5. append durable `AttemptStarted`;
6. commit.

No first modeled effect may occur before durable attempt start.

Crash after consumption may waste the authorization. Replay of the authorization is forbidden.

## 6. Operation admission

Every effectful `TechnicalOperation` must pass a linearized admission boundary.

Admission evaluates, in one logical control-plane snapshot:

- valid attempt;
- live authority;
- valid capability;
- valid contract;
- known conservative `possible_effects(operation)`;
- `possible_effects(operation) ⊆ authorized_effect_envelope`;
- runtime invariants.

`OperationAdmission` is bound to the exact canonical operation that is later executed.

A legal implementation may use a canonical byte representation plus an immutable operation digest. The Broker must execute the admitted operation, not a replacement payload.

## 7. Revocation semantics

Revocation is evaluated per operation at the admission linearization point.

- revocation before admission → `DENY`
- admission before revocation → admitted operation may complete
- revocation applies to all later operations

The same temporal rule applies to capability invalidation.

## 8. Effect model

Every supported effectful primitive must provide a conservative effect envelope:

`actual_effects(O) ⊆ possible_effects(O)`

Semantics:

- over-approximation → safe but restrictive;
- under-approximation → `EFFECT MODEL UNSOUND`;
- unknown envelope before effect → `DENY`.

A deliberately malicious trusted primitive is outside the v0 adversary model. If adversarial testing shows that a trusted primitive under-approximates its effects, the result is a falsified TCB/effect-domain assumption, not proof that the kernel prevented the effect.

## 9. State binding

A safety-relevant mutable precondition may not be satisfied by an earlier observation alone.

Where required:

`CONDITION + MUTATION`

must be bound atomically at the mutation boundary, unless the contract explicitly authorizes the relevant concurrency.

## 10. Observation, coverage, attribution

Observation is not self-report by the Executor.

Effect-compliance assessment requires:

`OBSERVATION + COVERAGE + ATTRIBUTION`

Coverage is complete relative to the contract-defined compliance domain, not the entire world.

If required coverage is incomplete, or an important observed delta cannot be attributed to or excluded from the attempt:

`EffectCompliance = INDETERMINATE`

## 11. Compliance and acceptance

Compliance and acceptance are orthogonal.

Legal states include:

- `Compliance PASS / Acceptance FAIL`
- `Compliance FAIL / Acceptance PASS`

Acceptance cannot retroactively authorize or legalize an effect.

## 12. Uncertainty policy

Before effect:

`PRE-EFFECT UNKNOWN → DENY`

After effect:

`POST-EFFECT UNKNOWN → INDETERMINATE`

## 13. Claims

### Claim A — Semantic Enforcement

No tested public kernel path may obtain a valid proof-bearing transition through substitutions such as:

- `CAN → MAY`
- `DID → AUTHORIZED`
- `ATTEMPTED → EFFECT`
- `SATISFIED → WITHIN_SCOPE`
- `SATISFIED → AUTHORIZED`

without the required proof obligations.

### Claim B — Capability Enforcement

Under the frozen v0 threat model, no tested hostile requester trace may obtain a writable path to the modeled target except through a valid Broker admission.

### Claim C — Effect-Domain Soundness

For supported primitives, tested execution traces must not falsify:

`actual_effects(O) ⊆ possible_effects(O)`

and required mutable preconditions must remain bound to the mutation boundary.

## 14. Not frozen by this document

This architecture does not require forever:

- Python;
- SQLite;
- a specific IPC mechanism;
- a specific container/runtime mechanism;
- GitHub Actions;
- a particular process topology beyond the required trust/capability separation.

Those are reference implementation or experimental substrate choices.
