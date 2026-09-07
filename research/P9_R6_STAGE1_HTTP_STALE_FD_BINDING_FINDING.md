# P9-R6 Stage 1 — HTTP Stale-FD Connection-Binding Finding

Status: **OPEN / BLOCKING / REPAIR NOT YET APPLIED**

## Frozen review input

- repository: `FJ899/8`
- P9-R5 final HEAD: `2aea14bdadda2995bb857c6b8389b5dcbfb94136`
- P9-R5 final TREE: `f20b277c23343eac398af4b30daf998324dcdd27`
- finding: `P9-R5-RV-F005`
- origin: **NEWLY REVEALED DURING BLIND POST-REPAIR CONTINUATION**
- classification: **REPAIR BYPASS / INCOMPLETE HTTP OBJECT-BINDING REPAIR OF P9-R3-RV-F003**

## Finding

P9-R5 fixes pathname rebinding by requiring the effecting SQLite connection to correspond to the historically bound provider-store object. The HTTP implementation opens a new sqlite3.Connection, reads `PRAGMA database_list`, then scans **all** `/proc/self/fd` entries for any FD whose link names the same main database pathname and whose `fstat` identity matches the historical target instance.

That process-global FD search does not prove that the matching FD belongs to the sqlite3.Connection that will execute the CAS.

A stale FD to historical T1 can therefore validate a new connection that actually opened replacement T2 at the same pathname:

`historical T1 -> keep stale FD(T1) open -> replace pathname with T2 -> sqlite3.Connection opens T2 -> global FD scan finds stale FD(T1) -> expected T1 identity appears satisfied -> CAS executes on T2`.

`FD WITH SAME PATHNAME AND IDENTITY != FD BACKING THIS CONNECTION`.

This is a bypass of the P9-R5 HTTP repair for the existing invariant:

`VALIDATED TARGET INSTANCE MUST BE THE INSTANCE USED BY THE EFFECT PRIMITIVE`.

It is not classified as a new untrusted-Executor CAI-001 bypass because arbitrary trusted-provider filesystem manipulation remains inside the frozen TCB. It blocks the stronger reference-runtime claim that the provider-side exact SQLite connection is historically target-bound.

## Required counterexample

1. create provider store T1 at pathname P and persist historical instance identity;
2. keep an OS FD to T1 open;
3. clone compatible T2;
4. unlink/replace pathname P with T2 while the stale T1 FD remains open;
5. invoke a historically-bound provider CAS against P;
6. frozen P9-R5 is vulnerable if the stale T1 FD satisfies `_connect_bound_target()` while the sqlite3.Connection mutates T2.

Expected secure behavior:

`a stale or unrelated process FD MUST NOT authenticate a different sqlite3.Connection`.

The Stage-1 workflow is intentionally expected-red. No repair is included in this stage.

## Subsequent repair boundary

Any repair must remain inside the dependency closure of `P9-R5-RV-F005`:

- this durable finding and exact stale-FD reproducer;
- connection-specific binding of the opened SQLite main database object;
- positive same-target execution and repeated provider compatibility;
- P9-R5/R4/R3/R2/F001/F002 targeted replay;
- broad inherited regressions as verification only.

No generic Broker work, unrelated evidence redesign, speculative architecture cleanup, API/product freeze, merge/main movement, deploy/release/tag, canonical/status promotion, or Human acceptance inference is authorized.