# P9-R5 Stage 1 — Pathname-Rebind Regression of Bound-Route Repair

Status: **OPEN / BLOCKING / P9-R4 REPAIR DOES NOT YET SURVIVE BLIND REVIEW**

## Frozen review input

- repository: `FJ899/8`
- P9-R4 final HEAD: `e77be4dd57125fa7ee0c577ece6c9293726f2970`
- P9-R4 final TREE: `62f0af4bf7955584b64c969196842785f745a497`
- P9-R4 final workflow run: `34154507644`
- finding: `P9-R4-RV-F004`
- classification: **REGRESSION / INCOMPLETE REPAIR OF P9-R3-RV-F003**
- discovery context: **BLIND POST-REPAIR CONTINUATION**

## Finding

P9-R4 correctly snapshots the route-bearing composition value before target-instance validation and delegates execution through a trusted shallow kernel/repository view containing that snapshot. For local filesystem domains, however, the snapshot is still a pathname rather than an already-open/pinned filesystem object.

Therefore the validated route can be rebound in the filesystem namespace after validation while retaining the same pathname string:

`bound pathname R -> resolve/stat T1 -> validation succeeds -> namespace rebind R -> T2 -> primitive opens R -> effect T2`.

This is not a new assurance layer beyond P9-R3-RV-F003. It is a bypass of the P9-R4 repair for the same invariant:

`VALIDATED TARGET INSTANCE MUST BE THE INSTANCE USED BY THE EFFECT PRIMITIVE`.

The deterministic G3 reproducer uses a symlink pathname `R`. Historical admission and P9-R4 validation resolve `R` to T1. Immediately after `_execution_target_binding()` returns the correct T1 binding, the trusted test hook repoints `R` to a distinct compatible T2. The P9-R4 bound kernel still carries pathname `R`, so `sqlite3.connect(R)` resolves it again and can open T2.

This remains inside trusted/local target-composition assumptions rather than an established untrusted-Executor CAI-001 bypass. It blocks the stronger claim that P9-R4 has closed the execution check/use target-instance race.

## Required counterexample

1. create T1 and distinct T2 with compatible logical state;
2. expose T1 through a route pathname/symlink R;
3. admit through the trusted adapter while R -> T1;
4. execution validation resolves R -> T1 and matches the durable historical binding;
5. after validation, rebind R -> T2 before the domain primitive opens R;
6. execute exact historical admission.

The frozen P9-R4 candidate is vulnerable if T2 receives the mutation/provenance.

Expected secure behavior:

`PATH SNAPSHOT != OBJECT SNAPSHOT` must be handled so namespace rebinding cannot redirect a historically bound execution.

The Stage-1 workflow is intentionally expected-red. No repair is included in this stage.

## Subsequent repair boundary

Any repair must stay inside the dependency closure of this F003 regression:

- durable finding and exact pathname-rebind reproducer;
- object-level or transaction-level target-instance binding through the effect boundary for G3/G4/HTTP as applicable;
- domain-correct positive same-target execution;
- minimum common seam only if semantically justified;
- tests/evidence directly required;
- broad inherited regressions as verification only.

No generic Broker work, unrelated evidence redesign, speculative abstraction cleanup, API/product freeze, merge/main movement, deploy/release/tag, canonical/status promotion, or Human acceptance inference is authorized.
