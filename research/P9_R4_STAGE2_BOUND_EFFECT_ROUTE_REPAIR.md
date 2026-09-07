# P9-R4 Stage 2 — Bound Effect-Route Repair

Status: **REPAIR IMPLEMENTED / TARGETED REPLAY GREEN / BLIND REVIEW CONTINUATION PENDING / NOT HUMAN-CLOSED**

## Frozen input

- repository: `FJ899/8`
- P9-R3 green HEAD: `673461f6aaadf1ff2ada5c3cb1902c151f8433bf`
- P9-R3 green TREE: `2d2d38bb6c5c10ca359977ee852d28da4e725b43`
- P9-R3 green workflow run: `34153650811`
- P9-R4 Stage-1 red HEAD: `097cdd375dd1ee914aee0fb968b8a19cc8c51c9d`
- P9-R4 Stage-1 red TREE: `6ef2a1a4208f3e9a1cf279a14eb0ec2c699a3fa6`
- P9-R4 Stage-1 red workflow run: `34154012807`
- finding: `P9-R3-RV-F003`
- origin: **NEWLY REVEALED DURING BLIND POST-REPAIR CONTINUATION**

## Executed counterexample

The Stage-1 reproducer derived a matching historical T1 target binding, then changed the G3 kernel route to a distinct compatible T2 before the domain primitive opened its target connection. On the frozen P9-R3 candidate the exact historical admission executed successfully on T2.

- Stage-1 artifact ID: `10030319349`
- Stage-1 ZIP SHA256: `a9fd3b333b443d15c47f1af86589bf2628fb3f6599a53e9503953ad5e62df92d`
- observed result: `occurred=True` with T2 carrying provenance for the historical T1 admission.

This established a check/use target-instance race distinct from P9-R2-RV-F002. P9-R3 detected a route already changed before execution validation; P9-R4 addresses route substitution after validation but before the effect primitive resolves/uses its target.

## Repair mechanism

The repair does not add another later comparison. It binds the route that is validated to the route delegated into the domain effect operation.

### G3

The adapter snapshots `kernel.target_db` before target-instance validation. If the historical binding matches, execution is delegated through a trusted shallow kernel view whose `target_db` is the captured route. Mutation of the original kernel composition object after validation does not redirect the primitive.

### G4

The adapter snapshots the current `SanitizedGitRepo` route and protected ref before validation. After a matching historical target check, execution is delegated through a trusted shallow kernel view bound to that captured repository/ref rather than re-reading mutable composition state.

### HTTP CAS

The adapter snapshots the route-bearing kernel/observer before validation and delegates through that kernel snapshot. In addition, bound historical executions include `expected_target_instance_id` in the trusted `/cas` request. The provider compares this expected identity with the concrete provider-store instance before applying CAS and returns `target_instance_mismatch` on disagreement.

Legacy/raw HTTP requests omit that optional field and preserve the prior P6 wire/execution semantics; they do not thereby gain P9-R4 historical target assurance.

The common invariant is:

`VALIDATED TARGET ROUTE == EFFECTING TARGET ROUTE`

while the concrete binding semantics remain domain-specific.

## Targeted gates

The repair tests establish:

- G3: target composition changes immediately after validation, yet the effect remains on historical T1 and T2 receives no admission provenance;
- G4: analogous composition switch leaves cloned T2 ref unchanged while historical T1 receives the admitted commit;
- HTTP: same credentials/provider ID/resource on a cloned T2 provider store are rejected by provider-side expected-instance enforcement before mutation;
- legacy/raw HTTP execution remains compatible.

The frozen Stage-1 G3 race reproducer is replayed on this branch in regression form: a secure implementation may reject or complete on T1, but T2 must never receive the historical effect.

## Verified candidate before this documentation-only commit

- HEAD: `c5097264d73781d10bd5d7b73f8098a5bbf3f8d5`
- TREE: `5d013ae454fbce0739190034867bff1c329abc05`
- workflow run: `34154417165`
- result: `success`
- artifact ID: `10030461218`
- artifact ZIP SHA256: `9726e84b7b5ae618bdc40836a42da2e5e94906a4f7f1b27731a1b7630cbc614c`

That run established:

- exact P9-R4 Stage-1 race replay: GREEN;
- P9-R4 bound-route gates: GREEN;
- P9-R3 execution target-binding replay: GREEN;
- P9-R2 target-instance provenance replay: GREEN;
- P9-F001/P9-F002 replay: GREEN;
- locked G1-G4 regression oracle: GREEN;
- inherited P1-P8 regressions: GREEN;
- G2/G4/P7 physical/adversarial topology regressions: GREEN.

Broad regression scope is verification evidence only; it does not widen mutation authority.

## Genealogy / disposition

`P9-R3-RV-F003`

- origin: `NEWLY REVEALED DURING BLIND POST-REPAIR CONTINUATION`
- repair: `P9-R4`
- targeted replay: `PASS`
- blind review survival: `PENDING`

Current status:

- `P9-R4 REPAIR = COMPLETE / GREEN CANDIDATE`
- `KNOWN-FINDING REPLAY = GREEN`
- `BLIND POST-REPAIR CONTINUATION = NOT YET RESUMED ON FINAL DOCUMENTED HEAD`
- `POST-REPAIR REVIEW PASS = NO`
- `HUMAN ACCEPTANCE = NOT INFERRED`

No merge/main movement, deploy/release/tag, canonical/status promotion, generic Broker work, API/product freeze, or Human acceptance inference is authorized or implied by this record.
