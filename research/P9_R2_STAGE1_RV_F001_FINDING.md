# P9-R2 Stage 1 — P9-R1-RV-F001 Target-Instance Provenance Finding

Status: **OPEN / REPRODUCTION STAGE — NO REPAIR IN THIS STAGE**

Frozen repair base:

- repository: `FJ899/8`
- BASE HEAD: `a482fd2bda8413c47a239eb6339582bf3bbc200d`
- BASE TREE: `ae2e534b8ad2a5b313e301d64c474dbae00a6160`
- target finding: `P9-R1-RV-F001`
- origin: `NEWLY REVEALED DURING POST-REPAIR REVIEW`

## Claim attacked

Crash/restart evidence rehydration for a historical admission must remain bound to the same historical physical target instance. Logical resource/ref identity alone must not permit evidence from a different physical target instance to establish `OCCURRED` for the historical target claim.

## Exact Stage-1 counterexample

G3 minimal reproducer:

1. establish and execute a real admitted operation against physical target store `T1` and logical resource `X`;
2. preserve the real control ledger and admission identity;
3. clone the resulting target database to a distinct physical target store `T2` so that `T2` contains matching resource state and copied mutation provenance;
4. reconstruct a new trusted G3 kernel/observer/adapter using the original control ledger but `T2` as the target store;
5. call `EffectEvidenceCollector.collect_from_admission_id(real_admission_id, exact_operation)`;
6. require that the historical `T1` claim is **not** established as `OCCURRED` from `T2` evidence.

Expected secure behavior:

`historical admission → T1; restart/recovery → wrong T2; same logical resource X; copied matching provenance → MUST NOT yield OCCURRED for historical T1 claim`.

The Stage-1 GitHub workflow is intentionally **expected-red**: a failing assertion is the executable evidence that the frozen pre-repair base still permits `T2` evidence to establish historical `T1` `OCCURRED`. A green run would mean the counterexample was not reproduced and Stage 1 would remain incomplete.

## Why this is distinct from P9-F001/P9-F002

P9-F001 repaired upstream control-lineage provenance by reconstructing request/authorization/attempt/admission identities from the durable control ledger.

P9-F002 added read-only rehydration from durable admission identity after transient `RuntimeTrace` loss without retrying the effect.

This newly revealed finding is deeper in the assurance chain: the current durable lineage binds a capability to logical resource identity, but does not independently establish which physical target-store instance is the historical target for the admission.

## Stage boundary

This Stage 1 authorizes only durable recording and executable reproduction of the counterexample. It deliberately does **not** implement target-instance binding, common seams, domain repairs, or any change to `EffectEvidence`, G3/G4/HTTP execution, runtime, binding, or reconciliation semantics.

Finding genealogy:

- `P9-F001` — original P9 finding — repaired candidate; survival review incomplete.
- `P9-F002` — original P9 finding — repaired candidate; survival review incomplete.
- `P9-R1-RV-F001` — **NEWLY REVEALED DURING POST-REPAIR REVIEW** — OPEN / BLOCKING.

No Human closure, merge, main movement, deploy/release/tag, canonical effect, or status promotion is inferred by this record.
