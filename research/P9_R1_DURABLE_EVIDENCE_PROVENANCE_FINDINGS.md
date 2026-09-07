# P9-R1 — Durable Evidence Provenance Findings

Status: **OPEN FINDINGS — REPAIR NOT YET APPLIED**

Review / repair base:

- repository: `FJ899/8`
- base HEAD: `8026e47f37152cba98855f89100b5ffed6b2269c`
- base TREE: `cf1a49f94e56b5e8259467fd25d569cae006d70d`
- P8 workflow run: `34133596734` (`success`)
- P8 artifact ZIP SHA256: `c1254204829d73f431f24bd91bdc47b8ac303d47ea43debd3c678ef5db998d9d`

This record is created before corrective implementation. A green P8 workflow does not close either finding.

---

## P9-F001 — EffectEvidence trusts non-durable upstream RuntimeTrace identities

**Status:** OPEN

**Claim attacked:** `EffectEvidence` can serve as an independently auditable reference-only normalization of facts around one exact effect attempt.

**Observed mechanism:**

`EffectEvidenceCollector.collect(trace, operation)` accepts a caller-supplied `RuntimeTrace`. It checks internal consistency among the supplied `AuthorizationResult`, `BindingResult`, `StartResult`, `AdmissionResult`, and exact operation, then uses durable reconciliation for the admission/effect. However, upstream identities are not reconstructed from the durable control ledger before being emitted as evidence.

In particular:

- `RuntimeTrace` is a constructible frozen dataclass;
- `ActionAuthorization`, `ActionAttempt`, `AuthorizationResult`, `StartResult`, `BindingResult`, `CapabilityBinding`, `OperationAdmission`, and `AdmissionResult` are constructible value objects;
- `TrustedBindingRegistry` is immutable only in memory;
- durable `operation_admissions` store `admission_id`, `attempt_id`, `capability_id`, `operation_digest`, and `canonical_operation`, but do not store `binding_id`;
- the P8 collector emits `request_id`, `authorization_id`, `binding_id`, and `attempt_id` from the supplied trace.

**Credible counterexample shape:**

1. obtain one real admitted/executed operation and its real durable `OperationAdmission`;
2. construct a new `RuntimeTrace` whose `AdmissionResult` contains that real admission and whose binding uses the same exact adapter object/capability/target;
3. replace upstream request/authorization/binding identifiers with mutually consistent attacker-chosen values while preserving the real attempt/admission linkage required by current collector checks;
4. call `EffectEvidenceCollector.collect()` with the exact admitted operation;
5. durable reconciliation confirms the real effect while the collector can emit non-durable upstream identifiers from the constructed trace.

**Expected:** evidence identities that purport to describe historical request/authorization/binding/attempt provenance are derived from durable trusted records, or fields lacking durable provenance are omitted.

**Observed at review:** collector source does not perform that reconstruction; `binding_id` has no durable historical record in the current control schema.

**Invariant at risk:** `EVIDENCE = bound references to facts`, not a mixture of durable effect facts and caller-constructible historical labels.

**Classification:** EVIDENCE PROVENANCE / FALSE HISTORICAL BINDING RISK.

**Minimal reproducer:** to be added by the authorized P9-R1 adversarial test before correction. The repair may not weaken the test meaning after observing it.

**Disposition:** OPEN. Blocks P8 evidence reuse as an independent assurance basis and blocks evidence/API freeze. Does not by itself establish an untrusted-Executor effect-path bypass under the frozen v0 threat model.

---

## P9-F002 — EffectEvidence cannot be rehydrated after transient RuntimeTrace loss

**Status:** OPEN

**Claim attacked:** the normalized evidence layer remains usable for post-effect uncertainty / crash recovery when ephemeral runtime state is lost.

**Observed mechanism:**

`KernelRuntime.run()` returns a `RuntimeTrace` only after `adapter.execute()` returns. If execution commits an effect but its return path is lost by exception/process failure, P5 reconciliation can recover from durable admission + target evidence, but P8 collection requires a surviving runtime trace and currently requires `trace.execution is not None`.

**Credible counterexample shape:**

1. create a valid authorization, attempt, and exact admission;
2. execute such that the target effect occurs but the caller loses the execution result / transient runtime object;
3. retain only durable admission identity and durable target/control state;
4. attempt to reconstruct normalized effect evidence after restart;
5. P5 can reconcile, but P8 exposes no durable-admission rehydration path and cannot collect without the lost `RuntimeTrace`.

**Expected:** post-crash evidence reconstruction can begin from a durable trusted identity (at minimum exact admission identity) and re-read the durable authority/attempt/admission chain plus current target evidence, without retrying the effect.

**Observed at review:** no such collector entry point exists; current API requires the ephemeral trace.

**Invariant at risk:** post-effect uncertainty must be reconciled from durable evidence; recovery must never depend on blind replay or on ephemeral success objects surviving process failure.

**Classification:** DURABLE RECOVERY / EVIDENCE REHYDRATION GAP.

**Minimal reproducer:** to be added by the authorized P9-R1 adversarial test before correction.

**Disposition:** OPEN. Blocks crash-safe evidence subsystem / independent assurance reuse. Does not invalidate existing P5 reconciliation semantics.

---

## Repair constraints

P9-R1 repair is bounded by the Human authorization:

- finding-first history remains durable;
- no trust in caller-supplied upstream provenance;
- reconstruct durable request/authorization/attempt/admission lineage from the trusted ledger;
- `binding_id` must either gain durable historical provenance or be removed from `EffectEvidence`;
- evidence must be collectable after transient `RuntimeTrace` loss using durable identity;
- no retry/re-execution during evidence recovery;
- no generic Broker work, product/API freeze, status promotion, merge/main movement, release/deploy/tag, or canonical effect.
