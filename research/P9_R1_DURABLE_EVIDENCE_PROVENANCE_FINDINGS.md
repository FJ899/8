# P9-R1 — Durable Evidence Provenance Findings

Status: **OPEN FINDINGS — EXECUTION REPRODUCER CONFIRMED; REPAIR NOT YET APPLIED**

Review / repair base:

- repository: `FJ899/8`
- base HEAD: `8026e47f37152cba98855f89100b5ffed6b2269c`
- base TREE: `cf1a49f94e56b5e8259467fd25d569cae006d70d`
- P8 workflow run: `34133596734` (`success`)
- P8 artifact ZIP SHA256: `c1254204829d73f431f24bd91bdc47b8ac303d47ea43debd3c678ef5db998d9d`

Pre-repair adversarial execution:

- candidate HEAD: `62f22eb0964fec35871f8b2b256f29c506983c8b`
- candidate TREE: `3e2a2090a000164dda87a428ccd49c676f1d23ca`
- workflow run: `34135531254`
- result: `failure` at `Run P9-R1 provenance and rehydration attacks`
- failure artifact ID: `10023803094`
- failure artifact ZIP SHA256: `d6d7c831fd880673ed05b021b2d39be8542f282387e26760f6be19bcdfd10690`

This record was created before corrective implementation. A green P8 workflow does not close either finding.

---

## P9-F001 — EffectEvidence trusts non-durable upstream RuntimeTrace identities

**Status:** OPEN — EXECUTION REPRODUCER CONFIRMED

**Claim attacked:** `EffectEvidence` can serve as an independently auditable reference-only normalization of facts around one exact effect attempt.

**Observed mechanism:**

`EffectEvidenceCollector.collect(trace, operation)` accepts a caller-supplied `RuntimeTrace`. It checks internal consistency among the supplied `AuthorizationResult`, `BindingResult`, `StartResult`, `AdmissionResult`, and exact operation, then uses durable reconciliation for the admission/effect. However, upstream identities are not reconstructed from the durable control ledger before being emitted as evidence.

In particular:

- `RuntimeTrace` is a constructible frozen dataclass;
- `ActionAuthorization`, `ActionAttempt`, `AuthorizationResult`, `StartResult`, `BindingResult`, `CapabilityBinding`, `OperationAdmission`, and `AdmissionResult` are constructible value objects;
- `TrustedBindingRegistry` is immutable only in memory;
- durable `operation_admissions` store `admission_id`, `attempt_id`, `capability_id`, `operation_digest`, and `canonical_operation`, but do not store `binding_id`;
- the P8 collector emits `request_id`, `authorization_id`, `binding_id`, and `attempt_id` from the supplied trace.

**Executed counterexample:**

`tests.test_p9_r1_evidence_provenance.DurableEvidenceProvenanceRepairTests.test_forged_runtime_trace_cannot_supply_historical_evidence_identities`

The test creates a real admitted/executed G3 operation, preserves its real `AdmissionResult` and execution, then constructs a mutually consistent forged upstream trace with:

- `request_id = request-forged`;
- `authorization_id = authorization-forged`;
- `binding_id = binding-forged`;
- the real `attempt_id` rewritten to point at the forged authorization in the constructed `ActionAttempt`;
- the same exact trusted adapter object, capability, target, real admission, and exact admitted operation.

Expected: collector rejects the synthetic historical chain.

Observed on run `34135531254`: `AssertionError: ValueError not raised`.

Therefore the current collector accepted the constructed trace far enough to violate the adversarial expectation; durable effect reconciliation did not authenticate the upstream labels supplied by the trace.

**Expected invariant:** evidence identities that purport to describe historical request/authorization/attempt provenance are derived from durable trusted records, and fields lacking durable historical provenance are omitted.

**Additional binding finding:** `binding_id` has no durable historical record in the current control schema. P9-R1 therefore selects repair option **B: remove `binding_id` from `EffectEvidence`** rather than synthesize provenance.

**Invariant at risk:** `EVIDENCE = bound references to facts`, not a mixture of durable effect facts and caller-constructible historical labels.

**Classification:** EVIDENCE PROVENANCE / FALSE HISTORICAL BINDING RISK.

**Minimal reproducer:** `tests/test_p9_r1_evidence_provenance.py`, bound above to exact pre-repair HEAD/TREE/run.

**Disposition:** OPEN. Blocks P8 evidence reuse as an independent assurance basis and blocks evidence/API freeze. Does not by itself establish an untrusted-Executor effect-path bypass under the frozen v0 threat model.

---

## P9-F002 — EffectEvidence cannot be rehydrated after transient RuntimeTrace loss

**Status:** OPEN — EXECUTION REPRODUCER CONFIRMED

**Claim attacked:** the normalized evidence layer remains usable for post-effect uncertainty / crash recovery when ephemeral runtime state is lost.

**Observed mechanism:**

`KernelRuntime.run()` returns a `RuntimeTrace` only after `adapter.execute()` returns. If execution commits an effect but its return path is lost by exception/process failure, P5 reconciliation can recover from durable admission + target evidence, but P8 collection requires a surviving runtime trace and currently requires `trace.execution is not None`.

**Executed counterexample:**

`tests.test_p9_r1_evidence_provenance.DurableEvidenceProvenanceRepairTests.test_evidence_can_be_rehydrated_from_durable_admission_after_trace_loss_without_retry`

The test first creates a real admitted/executed operation, retains only exact durable `admission_id` plus the exact operation for recovery input, and then requests normalized evidence without supplying the transient `RuntimeTrace`.

Expected: read-only evidence rehydration from durable admission identity; target state remains unchanged; a later direct replay of the admission remains denied.

Observed on run `34135531254`: `AttributeError: 'EffectEvidenceCollector' object has no attribute 'collect_from_admission_id'`.

This confirms that P5 durable reconciliation semantics exist but P8 has no crash/restart evidence rehydration entry point.

**Expected invariant:** post-crash evidence reconstruction can begin from a durable trusted identity (at minimum exact admission identity) and re-read the durable authority/attempt/admission chain plus current target evidence, without retrying the effect.

**Invariant at risk:** post-effect uncertainty must be reconciled from durable evidence; recovery must never depend on blind replay or on ephemeral success objects surviving process failure.

**Classification:** DURABLE RECOVERY / EVIDENCE REHYDRATION GAP.

**Minimal reproducer:** `tests/test_p9_r1_evidence_provenance.py`, bound above to exact pre-repair HEAD/TREE/run.

**Disposition:** OPEN. Blocks crash-safe evidence subsystem / independent assurance reuse. Does not invalidate existing P5 reconciliation semantics.

---

## Repair constraints

P9-R1 repair is bounded by the Human authorization:

- finding-first history remains durable;
- no trust in caller-supplied upstream provenance;
- reconstruct durable request/authorization/attempt/admission lineage from the trusted ledger;
- `binding_id` must either gain durable historical provenance or be removed from `EffectEvidence`;
- selected disposition for this repair: remove `binding_id`; do not invent a durable binding event;
- evidence must be collectable after transient `RuntimeTrace` loss using durable admission identity;
- no retry/re-execution during evidence recovery;
- no generic Broker work, product/API freeze, status promotion, merge/main movement, release/deploy/tag, or canonical effect.
