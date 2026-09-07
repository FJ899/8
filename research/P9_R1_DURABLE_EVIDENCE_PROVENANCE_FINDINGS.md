# P9-R1 — Durable Evidence Provenance Findings

Status: **REPAIRED / GREEN CANDIDATE — NOT HUMAN-CLOSED**

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

Verified repair candidate before this documentation-only disposition commit:

- repair HEAD: `8d4a1f31b70dfcd9b2c3611b85e0346e1c5df338`
- repair TREE: `e4d6c1667bfd6321d500de6e98c6e4c20d37d9ee`
- workflow run: `34135883125`
- result: `success`
- repair artifact ID: `10023953226`
- repair artifact ZIP SHA256: `4f3ff3fd258365d8c840289d725567949c592739567804a5d0821ffb7f3fc49d`
- P9-R1 provenance/rehydration attacks: `4/4` GREEN
- locked G1–G4 + P1–P6 + P8: GREEN
- G2/G4/P7 physical topology regressions: GREEN

This finding record was created before corrective implementation. Neither the green repair workflow nor this document constitutes Human acceptance or Gate closure.

---

## P9-F001 — EffectEvidence trusts non-durable upstream RuntimeTrace identities

**Status:** REPAIRED / GREEN CANDIDATE — NOT HUMAN-CLOSED

**Claim attacked:** `EffectEvidence` can serve as an independently auditable reference-only normalization of facts around one exact effect attempt.

**Observed mechanism:**

`EffectEvidenceCollector.collect(trace, operation)` accepted a caller-supplied `RuntimeTrace`, checked only internal consistency among supplied value objects, then used durable reconciliation for the admission/effect. Upstream identities were not reconstructed from the durable control ledger before being emitted as evidence.

In particular:

- `RuntimeTrace` and its authorization/start/admission value objects are constructible;
- `TrustedBindingRegistry` is immutable only in memory;
- durable `operation_admissions` store `admission_id`, `attempt_id`, `capability_id`, `operation_digest`, and `canonical_operation`, but do not store `binding_id`;
- the P8 collector emitted `request_id`, `authorization_id`, `binding_id`, and `attempt_id` from the supplied trace.

**Executed pre-repair counterexample:**

`tests.test_p9_r1_evidence_provenance.DurableEvidenceProvenanceRepairTests.test_forged_runtime_trace_cannot_supply_historical_evidence_identities`

The test created a real admitted/executed G3 operation, preserved its real admission/effect, then constructed a mutually consistent forged upstream trace with attacker-chosen request/authorization/binding identifiers while retaining the same exact trusted adapter, capability, target, real admission, and admitted operation.

Expected: collector rejects the synthetic historical chain.

Observed on run `34135531254`: `AssertionError: ValueError not raised`.

**Repair implemented:**

- `EffectEvidenceCollector` now re-reads durable lineage from the trusted control ledger by exact `admission_id`;
- the durable join binds `operation_admissions → action_attempts → action_authorizations → authorization_consumed → attempt_started → capabilities`, with contract/grant consistency joins;
- `collect(trace, operation)` treats the supplied trace only as a candidate description and rejects request/authorization/attempt/start/admission values that do not match durable lineage;
- exact operation canonical bytes/digest and target identity are revalidated against the durable admission/capability resource;
- `binding_id` was removed from `EffectEvidence` because no durable historical binding event exists; no synthetic provenance was introduced.

**Repair verification:**

- forged upstream RuntimeTrace attack: GREEN (rejected);
- real durable trace remains collectable;
- `EffectEvidence` explicitly has no `binding_id` field;
- inherited P8 reference-only semantics remain GREEN.

**Invariant after repair candidate:** historical request/authorization/attempt/admission/capability identities emitted by `EffectEvidence` come from durable ledger state; non-durable binding identity is omitted.

**Classification:** EVIDENCE PROVENANCE / FALSE HISTORICAL BINDING RISK.

**Disposition:** REPAIRED CANDIDATE. Human closure/acceptance not inferred.

---

## P9-F002 — EffectEvidence cannot be rehydrated after transient RuntimeTrace loss

**Status:** REPAIRED / GREEN CANDIDATE — NOT HUMAN-CLOSED

**Claim attacked:** the normalized evidence layer remains usable for post-effect uncertainty / crash recovery when ephemeral runtime state is lost.

**Observed mechanism:**

P5 reconciliation could recover from durable admission + target evidence, but P8 exposed only `collect(trace, operation)` and required a surviving runtime trace. There was no durable-admission evidence rehydration path.

**Executed pre-repair counterexample:**

`tests.test_p9_r1_evidence_provenance.DurableEvidenceProvenanceRepairTests.test_evidence_can_be_rehydrated_from_durable_admission_after_trace_loss_without_retry`

Expected: read-only evidence rehydration from exact durable admission identity; no effect retry.

Observed on run `34135531254`: `AttributeError: 'EffectEvidenceCollector' object has no attribute 'collect_from_admission_id'`.

**Repair implemented:**

`EffectEvidenceCollector.collect_from_admission_id(admission_id, operation)` now:

1. loads the exact durable authority/attempt/admission/capability lineage;
2. verifies the supplied operation is byte/digest-identical to the persisted admitted operation;
3. verifies target identity against durable capability resource;
4. performs read-only reconciliation using current target/domain evidence;
5. returns normalized evidence without calling `authorize`, `start_attempt`, `admit`, or `execute`.

**Repair verification:**

- evidence rehydration after transient trace loss: GREEN;
- effect state unchanged by evidence collection;
- direct admission replay remains `admission_consumed`;
- stronger crash case `effect committed + no control completion + no RuntimeTrace` rehydrates as `OCCURRED` from durable admission + target provenance;
- O1 admission + O2 supplied to rehydration is rejected as `admission_operation_mismatch`.

**Invariant after repair candidate:** crash/restart evidence reconstruction can begin from durable admission identity and never retries the effect.

**Classification:** DURABLE RECOVERY / EVIDENCE REHYDRATION GAP.

**Disposition:** REPAIRED CANDIDATE. Human closure/acceptance not inferred.

---

## Repair constraints and retained limits

P9-R1 remained within the authorized bounds:

- finding-first history remains durable;
- no trust in caller-supplied upstream provenance;
- no synthetic durable binding event;
- no retry/re-execution during evidence recovery;
- no generic Broker work;
- no product/API freeze;
- no merge/main movement;
- no release/deploy/tag;
- no canonical effect or status promotion.

Retained architectural limitation: evidence producers still use trusted adapter/kernel internals as a reference-runtime implementation mechanism. P9-R1 does not declare that internal coupling a stable public API.
