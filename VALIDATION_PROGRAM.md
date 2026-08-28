# Agency Kernel v0 — Validation Program

Status: **FROZEN — G1–G4**

The program is falsification-oriented. A green test suite or green GitHub Actions workflow does not itself establish Gate acceptance.

`PASS` means only that the accepted evidence run and fresh-context adversarial audit found no tested trace that falsified the preregistered claim under the stated threat model and domain.

## Claim A validation rule

Claim A is globally frozen but validated **cumulatively** as the relevant semantics come into existence.

A Gate must not claim a non-vacuous test of a semantic relation that is not implemented in that candidate.

- G1 validates the authority-semantic subset and may use an inert `Capability` representation to test `CAN ≠ MAY`.
- G2 preserves G1 Claim A results while introducing exact-operation admission and physical capability enforcement.
- G3 performs the cross-layer Claim A attacks that require `DID`, `WITHIN_SCOPE`, `SATISFIED`, observation, attribution, compliance, or acceptance.
- G4 repeats the full available Claim A together with B and C in the transfer domain.

## Gate sequence

### G1 — Semantic Integrity

Domain: controlled reference model.

Primary claim: **A — Semantic Enforcement, authority-semantic subset**

Minimal trace grows only through:

`request → MAY → authorization → consume → durable AttemptStarted`

G1 must not prematurely implement the physical capability boundary or full effect path.

### G2 — Capability Enforcement

Domain: minimal `VersionedResourceStore` boundary fixture.

Primary claim: **B — Capability Enforcement**

G2 extends the trace with:

`authenticated IPC → trusted Broker → CAN → canonical TechnicalOperation → operation_digest → OperationAdmission → physical capability boundary → minimal admitted target effect`

The G2 target effect exists to make Claim B non-vacuous: the Broker must be able to cross the modeled effect boundary after valid exact-operation admission, while the hostile Executor must be unable to cross it directly.

G2 does **not** yet claim effect-domain soundness for a supported production primitive.

### G3 — Controlled Effect Soundness

Domain: `VersionedResourceStore`

Primary claim: **C — Effect-Domain Soundness**

G3 replaces/extends the boundary fixture with supported effect semantics:

`put_if_version → possible_effects → state binding → target-side provenance → observation → coverage → attribution → WITHIN_SCOPE → SATISFIED`

G3 also executes the cross-layer Claim A attacks that could not exist non-vacuously in G1.

After Human acceptance of G1–G3:

`REFERENCE BASELINE LOCKED`

This is not a new architecture freeze. Architecture and validation semantics were frozen before implementation.

### G4 — Externalization / Transfer

Domain: `Sanitized Git`

Claims repeated: **A + B + C**

Entry condition:

`NO KERNEL SEMANTIC CHANGES ON ENTRY`

G4 tests whether one independently existing effect domain can satisfy the frozen kernel contract without weakening frozen invariants.

## Gate 4 failure classification

A G4 failure must first be recorded as a durable finding, then classified as one of:

- `ADAPTER BUG`
- `EFFECT-DOMAIN LIMITATION`
- `KERNEL ABSTRACTION FALSIFIED`
- `UNRESOLVED`

Only `KERNEL ABSTRACTION FALSIFIED` may justify reopening the architecture freeze.

If architecture is reopened and kernel semantics change:

1. previous G1–G3 acceptance is invalidated;
2. the reference baseline is rerun;
3. G4 is rerun;
4. no previous PASS is grandfathered.

No `special_case_for_git` may silently weaken a frozen invariant.

## v0 completion

`AGENCY KERNEL v0 COMPLETE`

requires Human acceptance of:

- G1;
- G2;
- G3;
- G4.

Canonical final claim:

> In the defined threat model, across the controlled reference domain and the mandatory externalization domain, no accepted tested adversarial trace falsified Claims A, B, or C without weakening the frozen invariants between domains.
