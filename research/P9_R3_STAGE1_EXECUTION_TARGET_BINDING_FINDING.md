# P9-R3 Stage 1 — Execution-Time Target-Binding Finding

Status: **OPEN / BLOCKING / REPAIR NOT YET APPLIED**

## Frozen review input

- repository: `FJ899/8`
- P9-R2 final HEAD: `d1e1442fcd932690c99e0429794b17416d297eb3`
- P9-R2 final TREE: `668a61b8f5687537e201658289875edd2261aba8`
- finding: `P9-R2-RV-F002`
- origin: **NEWLY REVEALED DURING BLIND POST-REPAIR CONTINUATION**

## Finding

P9-R2 correctly persists a historical target-instance binding after successful admission and correctly checks that binding during evidence recovery. The effect path does not, however, revalidate that historical target binding at execution time.

The current runtime sequence is:

`authorize -> binding -> start_attempt -> adapter.admit() -> adapter.execute(admission_id)`

P9-R2's `adapter.admit()` persists `HistoricalTargetBinding`, but the G3, G4, and HTTP adapter `execute()` methods delegate directly to their domain kernels. The domain execution paths consume the admission and then operate on the target currently configured at execution time. They do not load or compare the persisted `operation_target_bindings` row before the protected effect boundary.

Therefore the following temporal substitution is not yet excluded:

`admit on T1 -> persist historical T1 binding -> target composition changes to T2 -> execute(admission_id) -> effect can occur on T2`.

A later recovery check may fail closed because current T2 does not match historical T1, but that does not undo an effect already applied to T2.

This is distinct from `P9-R1-RV-F001`:

- `P9-R1-RV-F001`: wrong T2 evidence could establish historical T1 `OCCURRED` during recovery.
- `P9-R2-RV-F002`: effect execution itself can target T2 after admission-time T1 binding.

The issue is a temporal target-binding/reference-monitor obligation. It is not classified here as an untrusted-Executor CAI-001 bypass because the frozen threat model treats trusted adapter/target composition as TCB. It nevertheless blocks the stronger reference-runtime claim that the historical target binding remains enforced through the effect boundary.

## Required counterexample

At minimum:

`admission on T1`

then, before execution:

`same trusted adapter/control ledger -> target switched to distinct T2 with same logical resource and compatible state`

then:

`execute(admission_id)`

must **not** mutate T2 under the historical T1 admission.

The Stage-1 workflow for this record is intentionally expected-red on the frozen P9-R2 implementation. A failing security assertion is the executable evidence for this finding.

## Repair boundary for continuation

Any subsequent repair must remain limited to the dependency closure of `P9-R2-RV-F002`:

- durable finding and reproducer;
- execution-time enforcement of the persisted historical target binding;
- domain-correct checks for G3, G4, and HTTP;
- minimum common seam if and only if justified by all domains;
- tests/evidence directly required for the repair;
- broad regressions as verification only.

No generic Broker work, unrelated evidence redesign, API/product freeze, merge/main movement, deploy/release/tag, canonical/status promotion, or Human acceptance inference is authorized by this finding record.
