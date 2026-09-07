# P9-R2 Stage 2 — Target-Instance Provenance Repair

Status: **REPAIR IMPLEMENTED / TARGETED GATES GREEN / BLIND REVIEW NOT RESUMED / NOT HUMAN-CLOSED**

## Frozen identity

- repository: `FJ899/8`
- BASE HEAD: `a482fd2bda8413c47a239eb6339582bf3bbc200d`
- BASE TREE: `ae2e534b8ad2a5b313e301d64c474dbae00a6160`
- Stage-1 red HEAD: `8ca5810e746542f7b4f816987c9544baa855b964`
- Stage-1 red TREE: `b67a46d57a5c6407a2e6f60b5c3b8271ef3ab621`
- target finding: `P9-R1-RV-F001`
- origin: `NEWLY REVEALED DURING POST-REPAIR REVIEW`

## Stage-1 executed counterexample

Workflow run `34142923548` on the frozen Stage-1 candidate failed as expected because recovery using the real durable control ledger and exact historical admission/operation, but a distinct cloned G3 target store `T2`, returned `ReconciliationStatus.OCCURRED` for the historical `T1` claim.

Stage-1 artifact ID: `10026571206`.
Stage-1 artifact ZIP SHA256: `5785d920dd22868d7c2218ec298cfcd26b19de991ae7893b4e2fdcab7be2f603`.

The frozen Stage-1 branch remains unchanged and preserves the red reproducer.

## Repair mechanism

P9-R2 introduces a deliberately small common shape:

`HistoricalTargetBinding(kind, logical_target, instance_id)`

Semantic guard:

`COMMON TYPE != COMMON SEMANTICS`.

The historical binding is persisted by exact `admission_id` before trusted `EffectAdapter.admit()` returns success. Evidence recovery reconstructs the durable admission lineage, loads the historical target binding, derives the current target-instance binding through domain-specific semantics, and rejects a mismatch before reconciliation.

Domain semantics are intentionally distinct:

- G3: logical resource != concrete SQLite target-store instance; reference-runtime instance identity is bound to the concrete local target DB filesystem object.
- G4: protected ref != bare repository instance; reference-runtime instance identity is bound to the concrete repository directory filesystem object.
- HTTP CAS: provider/resource identity != concrete historical provider-store instance; authenticated provider identity exposes the concrete provider-store instance independently of endpoint/port.

These identities are reference-runtime/local-storage semantics only. No universal distributed-storage identity claim is made.

## Gate A — substitution rejection

Historical `T1` admission + reconstructed adapter/observer for distinct copied `T2` with the same logical target and matching copied provenance MUST NOT establish historical `T1` `OCCURRED`.

Targeted Stage-2 tests reject T2 with `target_instance_mismatch` for G3, G4, and HTTP. The exact Stage-1 G3 counterexample is replayed on the repair branch in regression form and is GREEN.

## Gate B — legitimate rehydration

A new trusted process/adapter over the SAME historical target instance must preserve read-only evidence rehydration and permit `OCCURRED` when target-side evidence independently establishes it.

Targeted Stage-2 tests preserve same-target rehydration for G3, G4, and HTTP. Recovery uses `collect_from_admission_id()` and does not authorize, admit, execute, or retry an effect. A separate replay probe remains `admission_consumed`.

## Gate C — domain semantics

Targeted Stage-2 tests establish that copied targets retain the same logical identity while receiving different instance identities for all three domains, and that the common shape retains distinct domain `kind` values:

- `g3-sqlite-store`
- `g4-bare-repository`
- `http-cas-provider-store`

## Targeted repair verification before this documentation-only commit

Stage-2 candidate HEAD: `183a53b1ae23021ae5de0935130a7150e29ec37c`
Stage-2 candidate TREE: `aa38deb348c1a1b56c7b2459563117cdc31a5262`
Workflow run: `34143593861`
Result: `success`
Artifact ID: `10026821048`
Artifact ZIP SHA256: `7cb46334515a4548bd11a70ca5e731d985019b07dbcb16ed8bf7ce5a1cf91f09`

That run established:

- exact Stage-1 original counterexample replay: GREEN;
- P9-R2 Gate A/B/C tests: GREEN;
- P9-F001/P9-F002 known-finding replay: GREEN;
- locked G1-G4 oracle: GREEN;
- inherited P1-P8 regressions: GREEN;
- G2/G4/P7 physical/adversarial topology regressions: GREEN.

The broad regression scope is verification evidence only and does not expand mutation authority.

## Genealogy / current disposition

`P9-R1-RV-F001`

- origin: `NEWLY REVEALED DURING POST-REPAIR REVIEW`
- repair: `P9-R2`
- targeted replay: `PASS`
- blind review survival: `PENDING`

Current status:

- `P9-R2 REPAIR = COMPLETE / GREEN CANDIDATE`
- `KNOWN-FINDING REPLAY = GREEN`
- `BLIND POST-REPAIR REVIEW = NOT RESUMED`
- `POST-REPAIR REVIEW PASS = NO`
- `HUMAN ACCEPTANCE = NOT INFERRED`

No merge/main movement, deploy/release/tag, canonical/status promotion, generic Broker work, API/product freeze, or blind review is authorized or inferred by this record.
