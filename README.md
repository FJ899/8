# Agency Kernel v0 — Falsification Laboratory

Status at bootstrap:

- `ARCHITECTURE v0: FROZEN`
- `VALIDATION PROGRAM: FROZEN — G1–G4`
- `EXPERIMENT OPERATING MODEL: FROZEN`
- `KERNEL IMPLEMENTATION: NOT STARTED`

This repository is a temporary falsification laboratory. It is not a new product and not a parallel Executor.

Its purpose is to test whether a minimal Agency Kernel can preserve the separation:

`MAY ≠ CAN ≠ DID ≠ WITHIN_SCOPE ≠ SATISFIED`

under a frozen threat model and a preregistered validation program.

## Validation sequence

1. **G1 — Semantic Integrity**  
   Controlled reference model. Claim A authority-semantic subset, with only minimal inert capability representation if needed to test `CAN ≠ MAY`.

2. **G2 — Capability Enforcement**  
   Hostile Executor + physical capability boundary + Broker + minimal exact-operation admission + `VersionedResourceStore` boundary fixture. Claim B.

3. **G3 — Controlled Effect Soundness**  
   Supported `put_if_version()`, effect model, state binding, target-side provenance, observation, coverage, attribution. Claim C plus completion of cross-layer Claim A checks that require `DID`, `WITHIN_SCOPE`, and `SATISFIED`.

4. **G4 — Externalization / Transfer**  
   `SanitizedGitAdapter`. Claims A+B+C repeated without weakening frozen invariants.

`v0 COMPLETE` requires Human acceptance of all four Gates.

Claim A validation is cumulative. G1 must not claim to test semantic relations that do not yet exist in the candidate.

## Experimental rule

A Gate is not closed by implementation, CI, a green workflow, or an AI statement.

The flow is:

`PREREGISTERED GATE CONTRACT → IMPLEMENTATION CANDIDATE → FIXED HEAD/TREE → FRESH-CONTEXT ADVERSARIAL AUDIT → DURABLE FINDINGS → HUMAN ACCEPT / REJECT`

A failure is recorded before any corrective change.

## Bootstrap invariant

PR #0 contains specification, threat model, validation contracts, experiment rules, substrate rules, and finding format only.

**ZERO KERNEL IMPLEMENTATION.**
