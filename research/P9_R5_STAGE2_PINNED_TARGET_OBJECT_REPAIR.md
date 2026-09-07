# P9-R5 Stage 2 — Pinned Target-Object Repair

Status: **REPAIR IMPLEMENTED / TARGETED REPLAY GREEN / BLIND REVIEW CONTINUATION PENDING / NOT HUMAN-CLOSED**

## Frozen input

- repository: `FJ899/8`
- P9-R4 final HEAD: `e77be4dd57125fa7ee0c577ece6c9293726f2970`
- P9-R4 final TREE: `62f0af4bf7955584b64c969196842785f745a497`
- P9-R5 Stage-1 red HEAD: `c9ad927ab99a9dcb6a3db44b3d09ee64f949e865`
- P9-R5 Stage-1 red TREE: `93fc672a2ba6f88b349dea9c7cc06623115928e1`
- P9-R5 Stage-1 run: `34154644716`
- finding: `P9-R4-RV-F004`
- classification: **REGRESSION / INCOMPLETE REPAIR OF P9-R3-RV-F003**

## Repair mechanism

P9-R5 closes pathname rebinding by requiring the object validated for a historically bound execution to be the same concrete object used by the effect primitive.

- G3 pins the target SQLite file with an open FD, verifies its `fstat`-derived historical identity, and executes while that object remains pinned.
- G4 pins the bare repository with a directory FD, verifies the opened directory identity, and executes Git through a trusted FD-rooted repository view.
- HTTP keeps normal SQLite/WAL pathname semantics but binds target identity to the main database file opened by the exact sqlite3.Connection: `PRAGMA database_list` identifies that connection's `main` file, `/proc/self/fd` identifies an open descriptor to the same file, and `fstat` is checked against the historical provider-store instance before the same connection enters `BEGIN IMMEDIATE`.

The final HTTP mechanism deliberately replaces an earlier `/proc/self/fd/N`-as-SQLite-path attempt, which preserved identity but produced repeatable `disk I/O error` failures in the P7 physical topology. That failure is classified as a compatibility defect of the repair implementation, not as a new CAI finding.

## Security and compatibility gates

The final candidate before this documentation-only commit is:

- HEAD: `bbfb89f876f209e117fba4fc4091f8d181699dd1`
- TREE: `63457706c4212a0f7b6468a0da488d6e90ba8250`
- workflow run: `34156040679`
- result: `success`
- artifact ID: `10031000756`
- artifact ZIP SHA256: `d2101e123b2ef11257f2cb3e812feb397ef2a67b0a427cfe57ffaa231d87dcca`

That exact run established simultaneously:

- exact P9-R5 Stage-1 pathname-rebind replay: GREEN;
- P9-R5 pinned-object gates: 5/5 GREEN, including repeated bound provider commits with intervening direct SQLite reads;
- P9-R4 bound-route replay: GREEN;
- P9-R3 execution target-binding replay: GREEN;
- P9-R2 target-instance provenance replay: GREEN;
- P9-F001/P9-F002 replay: GREEN;
- locked G1-G4 regression oracle: GREEN;
- inherited P1-P8 regressions: GREEN;
- P6 HTTP CAS: 26/26 GREEN;
- G2 physical topology: GREEN;
- G4 physical topology: GREEN;
- P7 HTTP physical/adversarial topology: GREEN.

Broad regression scope is verification evidence only; it does not widen mutation authority.

## Genealogy / disposition

`P9-R4-RV-F004`

- classification: `REGRESSION / INCOMPLETE REPAIR OF P9-R3-RV-F003`
- repair: `P9-R5`
- targeted replay: `PASS`
- blind review survival: `PENDING`

`P9-R3-RV-F003`

- P9-R4 targeted replay: `PASS`
- P9-R4 blind survival: `FAILED via F004 regression`
- P9-R5 targeted replay of the strengthened invariant: `PASS`
- further blind survival: `PENDING`

Current status:

- `P9-R5 REPAIR = COMPLETE / GREEN CANDIDATE`
- `KNOWN-FINDING REPLAY = GREEN`
- `BLIND POST-REPAIR CONTINUATION = NOT YET RESUMED ON FINAL DOCUMENTED HEAD`
- `POST-REPAIR REVIEW PASS = NO`
- `HUMAN ACCEPTANCE = NOT INFERRED`

No merge/main movement, deploy/release/tag, canonical/status promotion, generic Broker work, API/product freeze, or Human acceptance inference is authorized or implied by this record.
