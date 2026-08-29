# Agency Kernel v0 — Release Notes

Status: **post-v0 release preparation**

The frozen G1-G4 validation program has completed with Human ACCEPT for all four exact Gate candidates. The resulting statement is bounded and falsification-oriented:

> In the defined v0 threat model, across the controlled reference domain and the mandatory Sanitized Git transfer domain, no accepted tested adversarial trace falsified Claims A, B, or C without weakening the frozen invariants between domains.

## Accepted Gate identities

- G1: `7805da179b3a8a9575effdec7e8cdd83384ffdff`
- G2: `4b031327df4a4a783e7cea9a9ee0b830f4522eab`
- G3: `55117c30b5ecc27c9e16cbc1ecced572113eb087`
- G4: `930b8cae575edba1becc47fbebd9d944a5ebd68d`

The final accepted implementation snapshot is G4 HEAD `930b8cae...`, preserved by branch `v0-accepted-snapshot`.

## What v0 contains

- authority-semantic separation and single-use authorization;
- exact-operation admission and physical capability-boundary validation;
- controlled effect-domain soundness with state binding, provenance, observation, coverage and attribution;
- transfer of the same frozen semantics into a sanitized Git protected-ref/tree domain;
- durable finding-first audit history and exact execution/evidence identities.

## Post-v0 integration check

A separate post-v0 integration workflow was added without modifying the accepted snapshot. Full G1-G4 regressions, G2/G4 hostile topology, and deterministic G4 evidence capture completed successfully in run `33251314511` for integration HEAD `92f3243b36664265a20f6736a220b19d4e9e8843`.

Artifact:

- ID `9714446348`
- SHA-256 `ca20391411867fcdffc27806f129ac5d9ca892348d4dbf632d146197624e0ced`

## Important limitation

A later merge, squash, rebase, release commit or tag target is a new repository state. It does not inherit Gate acceptance merely because it contains the accepted code.

`AGENCY KERNEL v0 COMPLETE` is not a proof of universal security, Git security, host security, or protection outside the frozen threat model.
