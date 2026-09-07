# P9-R2 — Target-Instance Provenance Repair Finding

Status: **OPEN / REPAIR AUTHORIZED — NOT HUMAN-CLOSED**

## Frozen repair base

- repository: `FJ899/8`
- base HEAD: `a482fd2bda8413c47a239eb6339582bf3bbc200d`
- base TREE: `ae2e534b8ad2a5b313e301d64c474dbae00a6160`
- target finding: `P9-R1-RV-F001`
- origin: **NEWLY REVEALED DURING POST-REPAIR REVIEW**

This record is intentionally committed before corrective implementation.

## Finding

P9-R1 repaired durable upstream control lineage and crash/restart evidence rehydration, but `EffectEvidenceCollector.collect_from_admission_id()` does not durably bind the historical admission to the concrete historical target instance observed during recovery.

The current durable lineage binds the exact admission, attempt, authorization, capability ID, logical capability resource, operation digest, and canonical operation. It does not bind the admission to a concrete target-store/repository/provider-service instance.

Consequences differ by domain:

- **G3:** logical resource identity (for example `X`) is not the identity of the physical target SQLite store instance.
- **G4:** protected ref identity is not the identity of the bare repository instance.
- **HTTP CAS:** provider/resource identity is not automatically proof of the concrete historical service instance used by the admission.

A restart-time adapter/observer configured for the wrong target instance can therefore be semantically compatible at the logical-resource level. If matching target-side provenance is copied or reproduced on that wrong instance, current reconciliation may establish `OCCURRED` without proving that the evidence came from the historical target instance bound to the admission.

This is an evidence/recovery provenance finding. It is **not** presently classified as an untrusted-Executor CAI-001 enforcement bypass, because the frozen threat model trusts Broker/adapter/observer configuration. It blocks independent durable evidence closure for crash/restart assurance.

## Required repair gates

### Gate A — substitution rejection

Historical admission targets `T1`; restart reconstruction points to different `T2`; logical resource/ref remains the same and matching copied/parallel provenance exists.

**Required:** recovery MUST NOT establish `OCCURRED` for the historical `T1` claim.

### Gate B — legitimate rehydration

Historical admission targets `T1`; process state is lost; a new trusted process reconstructs the adapter/observer for the same historical `T1`.

**Required:** durable evidence recovery still works; `OCCURRED` remains derivable when independently established; evidence recovery performs zero effect retries and zero new effect execution.

### Gate C — domain semantics

Historical target binding must be semantically correct for all three domains:

- G3: logical resource != physical target-store instance.
- G4: protected ref != repository instance.
- HTTP CAS: provider/resource identity != automatically concrete historical service instance.

A common representation may be introduced only if its semantic adequacy is established for all applicable domains.

**Guard:** `COMMON TYPE != COMMON SEMANTICS`.

## Authorized mutation boundary

Mutation is limited to the dependency closure of `P9-R1-RV-F001`:

- this durable finding record;
- the T1 -> wrong-T2 reproducer;
- legitimate same-T1 crash/restart rehydration tests;
- domain-specific historical target binding for G3, G4, and HTTP CAS;
- the minimum common seam strictly required to express those bindings;
- tests/workflow/evidence directly required to prove the repair.

Not authorized during repair:

- blind post-repair review;
- changes outside the finding dependency closure;
- speculative abstraction cleanup;
- unrelated `EffectEvidence` redesign;
- generic Broker work;
- API/product freeze;
- merge/main movement;
- deploy/release/tag;
- canonical/status promotion;
- inference of Human acceptance.

## Required verification after implementation — not mutation authority

1. replay P9-F001 forged upstream lineage;
2. replay P9-F002 durable rehydration with zero retry/execute;
3. replay P9-R1-RV-F001 across G3/G4/HTTP, including T1/T2 rejection and same-T1 restart success;
4. inherited P1-P8 regression suite;
5. physical/adversarial topology regressions;
6. exact-operation/admission/replay regressions;
7. final candidate fixation: HEAD, TREE, changed files, commit chain, evidence identities.

After green targeted replay, the repair session must stop. Blind post-repair continuation requires a separate verifier-only authorization boundary.

## Genealogy

`P9-R1-RV-F001`

- origin: `NEWLY REVEALED DURING POST-REPAIR REVIEW`
- repair: `P9-R2`
- targeted replay: `PENDING`
- blind review survival: `PENDING`

A successful targeted repair is not independent closure.