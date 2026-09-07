# P9-R2 — Target-Instance Provenance Repair Finding

Status: **REPAIRED / GREEN CANDIDATE — TARGETED REPLAY PASS — BLIND REVIEW PENDING — NOT HUMAN-CLOSED**

## Frozen repair base

- repository: `FJ899/8`
- base HEAD: `a482fd2bda8413c47a239eb6339582bf3bbc200d`
- base TREE: `ae2e534b8ad2a5b313e301d64c474dbae00a6160`
- target finding: `P9-R1-RV-F001`
- origin: **NEWLY REVEALED DURING POST-REPAIR REVIEW**

The original OPEN record was committed before corrective implementation at commit `03114acdc8efd8482f360ff6b8ed561383624a88`.

## Finding

P9-R1 repaired durable upstream control lineage and crash/restart evidence rehydration, but `EffectEvidenceCollector.collect_from_admission_id()` did not durably bind a historical admission to the concrete historical target instance observed during recovery.

The pre-repair durable lineage bound the exact admission, attempt, authorization, capability ID, logical capability resource, operation digest, and canonical operation. It did not bind the admission to a concrete target-store/repository/provider-store instance.

The missing semantics were domain-specific:

- **G3:** logical resource identity (for example `X`) is not the identity of the physical target SQLite store instance.
- **G4:** protected ref identity is not the identity of the bare repository instance.
- **HTTP CAS:** provider/resource identity is not automatically proof of the concrete historical provider-store instance.

This is an evidence/recovery provenance finding. It is **not** classified here as an untrusted-Executor CAI-001 enforcement bypass, because the frozen threat model trusts Broker/adapter/observer configuration. It blocks independent durable evidence closure for crash/restart assurance until the historical target instance is established.

## Executed pre-repair counterexample

Pre-repair reproducer candidate:

- HEAD: `65e62aed56da3fa86899a3dbcd063b3f339b8915`
- TREE: `265943d918cb1612a8ef3f3295877db6770fe2ab`
- workflow run: `34141054462`
- result: `failure` at `Run P9-R2 Gate A/B target-instance tests`
- artifact ID: `10025901566`
- artifact ZIP SHA256: `425b3e63b43d335c6384e4e75cd53d9a8ad1147ebddd6be26163f8b69523c637`

Observed before repair:

- G3 historical T1 -> cloned T2 with copied target provenance: `ValueError not raised` — Gate A FAIL.
- G4 historical T1 -> cloned T2 repository with matching commit/provenance: `ValueError not raised` — Gate A FAIL.
- HTTP historical T1 -> cloned provider DB with the same provider ID/token and matching receipts/state: `ValueError not raised` — Gate A FAIL.
- G3 restart over the same T1 store: Gate B already PASS.
- G4 restart over the same T1 repository: Gate B already PASS.
- HTTP new provider process/endpoint over the same T1 provider DB: Gate B already PASS.

Thus the executed counterexample isolated the missing target-instance binding rather than a generic inability to recover after restart.

## Repair implemented

### Minimal common shape

P9-R2 adds an opaque `HistoricalTargetBinding`:

- `kind`
- `logical_target`
- `instance_id`

The common shape does **not** assert common identity semantics.

Guard retained:

`COMMON TYPE != COMMON SEMANTICS`.

### Domain semantics

**G3**

- kind: `g3-sqlite-store`
- logical target: operation resource
- reference-runtime instance identity: opaque hash over the concrete local target DB filesystem object identity (`st_dev`, `st_ino`) under a G3 namespace.

**G4**

- kind: `g4-bare-repository`
- logical target: protected ref
- reference-runtime instance identity: opaque hash over the concrete bare-repository directory filesystem object identity (`st_dev`, `st_ino`) under a G4 namespace.

**HTTP CAS**

- kind: `http-cas-provider-store`
- logical target: HTTP resource
- reference-runtime instance identity: authenticated provider-side identity of the concrete provider DB filesystem object, namespaced by provider ID.
- endpoint/port changes do not define target identity; restarting a provider process over the same provider DB preserves the binding.

These identities are intentionally reference-runtime/local-storage semantics. P9-R2 does **not** claim device/inode identity is a universal target identity mechanism for arbitrary storage or distributed services.

### Historical persistence and recovery

A trusted `EffectAdapter.admit()` that succeeds now persists one `operation_target_bindings` row keyed by exact `admission_id` before returning the admitted path to `KernelRuntime`.

The record contains:

- target kind;
- logical target;
- opaque target instance ID.

`EffectEvidenceCollector` now:

1. reconstructs the durable authority/attempt/admission/capability lineage;
2. requires an exact durable target-binding row for the admission;
3. verifies the historical logical target equals the durable capability resource;
4. verifies canonical operation bytes/digest and current logical target;
5. obtains the current adapter/observer target-instance binding using domain-specific semantics;
6. rejects a different instance with `target_instance_mismatch` **before reconciliation**;
7. only then performs read-only reconciliation.

`EffectEvidence` records `target_instance_kind` and `target_instance_id` as historical references. It still contains no aggregate authorization/DID/compliance/SATISFIED/PASS field, and `binding_id` remains omitted because P4 binding resolution itself is not persisted as a historical event.

## Transactional / compatibility limits retained deliberately

Historical target binding is persisted in a second trusted control-ledger transaction after the legacy domain admission transaction and before `EffectAdapter.admit()` returns success. P9-R2 does **not** claim atomic `OperationAdmission + HistoricalTargetBinding` persistence.

If a process fails between those writes, the durable admission may exist without historical target proof. Evidence recovery must then fail closed with missing target binding; it must not synthesize restart-time identity.

Legacy/raw direct kernel admission APIs remain unchanged for regression compatibility. An admission created outside the trusted EffectAdapter/runtime path may therefore lack this P9-R2 historical target record; normalized P9-R2 evidence recovery for such an admission is intentionally unavailable/fail-closed rather than inferred.

## Required repair gates and targeted replay

### Gate A — substitution rejection: PASS on repair candidate

Historical admission targets T1; restart reconstruction points to different T2; logical resource/ref remains the same and matching copied provenance exists.

Repair candidate rejects T2 before reconciliation for G3, G4, and HTTP.

### Gate B — legitimate rehydration: PASS on repair candidate

Historical admission targets T1; process state is lost; trusted reconstruction points to the same historical T1.

Repair candidate preserves `OCCURRED` rehydration for G3, G4, and HTTP and direct replay remains `admission_consumed`. No recovery path invokes a new effect.

### Gate C — domain semantics: PASS on repair candidate

Explicit Gate C verifies:

- G3 clone retains logical resource but receives different `g3-sqlite-store` instance ID;
- G4 clone retains protected ref but receives different `g4-bare-repository` instance ID;
- HTTP clone retains provider ID/resource but receives different `http-cas-provider-store` instance ID;
- the three `kind` values remain distinct even though the common data shape is shared.

## Verified repair candidate before this documentation-only disposition commit

- HEAD: `d37312b89e76975a186d2f1679391667d2d89a6a`
- TREE: `b9536180a85d29ecd8ce8a08642a05a54068aa5e`
- workflow run: `34141648587`
- result: `success`
- artifact ID: `10026123596`
- artifact ZIP SHA256: `44ba9ff0ad4a62d19907f722ee135e53f02a63894b8751283ceae95187353958`

Verification on that exact candidate:

- P9-R2 Gate A/B/C: `7/7` GREEN;
- P9-F001/P9-F002 replay: `4/4` GREEN;
- locked G1-G4 oracle: GREEN;
- P1 common conformance: `19/19` GREEN;
- P2 effect seams: `11/11` GREEN;
- P3 trusted runtime: `10/10` GREEN;
- P4 trusted binding: `10/10` GREEN;
- P5 reconciliation: `18/18` GREEN;
- P6 HTTP CAS: `26/26` GREEN;
- P8 effect evidence: `9/9` GREEN;
- G2 physical topology: GREEN;
- G4 physical topology: GREEN;
- P7 HTTP physical topology: GREEN.

This broad regression scope is verification evidence only; it does not expand P9-R2 mutation authority.

## Authorized mutation boundary retained

P9-R2 mutations remain limited to the dependency closure of `P9-R1-RV-F001`:

- this durable finding record;
- T1 -> wrong-T2 reproducer and same-T1 rehydration tests;
- domain-specific historical target binding for G3, G4, and HTTP CAS;
- the minimum common seam required to express those bindings;
- tests/workflow/evidence directly required to prove the repair.

No blind post-repair review, speculative abstraction cleanup, unrelated evidence redesign, generic Broker work, API/product freeze, merge/main movement, deploy/release/tag, canonical/status promotion, or Human acceptance inference is part of P9-R2.

## Genealogy / disposition

`P9-R1-RV-F001`

- origin: `NEWLY REVEALED DURING POST-REPAIR REVIEW`
- repair: `P9-R2`
- targeted replay: `PASS`
- blind review survival: `PENDING`

Current repair-session status:

- `P9-R2 REPAIR = COMPLETE / GREEN CANDIDATE`
- `KNOWN-FINDING REPLAY = GREEN`
- `BLIND POST-REPAIR REVIEW = NOT RESUMED`
- `POST-REPAIR REVIEW PASS = NO`
- `HUMAN ACCEPTANCE = NOT INFERRED`

A successful targeted repair is not independent closure. A separate verifier-only `P9-R2-RV` continuation is required before this repair can be said to survive post-repair review.