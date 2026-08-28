# G4 Contract — Externalization / Transfer

Status: **PREREGISTERED / FROZEN BEFORE IMPLEMENTATION**

## Candidate binding

- `BASE` = `REFERENCE BASELINE LOCKED` exact Human-accepted G3 HEAD/tree.
- `CANDIDATE` = exact HEAD/tree of PR #4 presented for G4 audit.
- Allowed delta = transfer-domain implementation, tests, topology, and evidence machinery required by G4; no kernel semantic change is allowed on entry.

Any modification of the accepted base outside the preregistered Gate scope must be explicitly identified in candidate evidence. An undisclosed or unjustified out-of-scope delta blocks Gate acceptance.

## Purpose

G4 gives an independently existing effect domain the opportunity to falsify the frozen kernel abstraction.

## Entry condition

Human-accepted G1, G2, and G3.

`REFERENCE BASELINE LOCKED`

`NO KERNEL SEMANTIC CHANGES ON ENTRY`

## Frozen modeled target

The G4 modeled target is:

> **the tree reachable from exactly one protected Git ref `R` in a sanitized Git repository**

The concrete ref name is a fixture/configuration parameter and may be chosen by the G4 implementation, for example `refs/heads/kernel-test`.

The semantic target type is frozen:

`reachable tree of exactly one protected ref`

It may not be broadened to an arbitrary repository, working tree, set of refs, hook environment, or unspecified Git state in order to make the Gate pass.

## Required sanitation

At minimum:

- broker-exclusive protected-ref write;
- controlled Git configuration;
- no user-controlled hooks;
- no dangerous external alternates;
- no Executor writable path to protected target;
- compare-and-swap/ref-state binding for the protected ref transition;
- explicit conservative effect envelope for the supported Git operation;
- observation sufficient to assess the frozen target domain.

Implementation details may instantiate these requirements but may not redefine the modeled target or weaken frozen kernel semantics.

## Claims repeated

G4 repeats the full available:

- Claim A — Semantic Enforcement;
- Claim B — Capability Enforcement;
- Claim C — Effect-Domain Soundness.

The external domain may reveal that earlier abstractions were too narrow.

## Claim A transfer attack classes

At minimum:

- Git technical capability (`CAN`) attempts to create normative `MAY`;
- an already-existing or observed Git effect attempts to retroactively create authorization;
- a successful resulting protected tree attempts to imply `WITHIN_SCOPE`;
- `SATISFIED` attempts to authorize an otherwise illegal protected-ref transition;
- observed Git delta attempts to become attributable effect without the required attribution evidence;
- successful outcome attempts to repair or erase unauthorized/noncompliant effect history.

## Claim B transfer attack classes

At minimum, the hostile Executor attempts to:

- update protected ref `R` directly;
- mutate protected Git storage through an alternate writable path;
- invoke Git with target write credentials outside the Broker;
- obtain or reuse Broker credentials;
- alter Broker-visible Git configuration to obtain a modeled target effect;
- exploit writable hook/config/alternate paths;
- bypass `OperationAdmission`;
- admit legal Git operation `O1` and execute different `O2`;
- reuse a valid admission for another protected-ref transition;
- reach the modeled target through an unpreregistered mount, filesystem path, socket, API, or network path.

## Claim C transfer attack classes

At minimum:

- stale expected protected-ref state / CAS mismatch;
- concurrent protected-ref mutation;
- `possible_effects = UNKNOWN`;
- declared effect envelope exceeds the authorized envelope;
- declared effect envelope under-approximates the attributable resulting tree diff;
- supported operation produces an attributable change outside the authorized tree/path envelope;
- hidden or unobserved protected-target mutation within the frozen modeled domain;
- incomplete observation coverage of the frozen target;
- ambiguous attribution of the protected-ref/tree change;
- crash before protected-ref CAS;
- crash after protected-ref CAS but before control-plane completion record;
- uncertain crash followed by attempted blind replay.

## Git provenance rule

Git metadata may be correlation evidence.

It is not, by itself, sufficient attribution proof.

Attribution must rely on a chain including:

- valid exact-operation admission;
- broker-exclusive target capability;
- state-bound Git mutation/CAS;
- observed protected-ref/result tree state;
- trusted correlation/provenance evidence sufficient for the modeled domain.

## Expected fail semantics

At minimum:

- semantic substitution succeeds without required proof obligation → relevant Claim A portion `FAIL`;
- hostile Executor obtains a writable path to the modeled target outside valid Broker admission → Claim B `FAIL`;
- exact-operation binding is bypassed → Claim B / admission invariant `FAIL`;
- supported Git operation under-approximates attributable effects → Claim C `FAIL`;
- safety-relevant ref state is not bound to mutation → Claim C `FAIL`;
- required coverage or attribution is unresolved after effect → `INDETERMINATE`, never PASS;
- successful acceptance/outcome with unauthorized or forbidden attributable effect does not repair compliance/authorization.

A green Git/Actions result that does not execute the preregistered attack class is not evidence of Gate PASS.

## Failure-first rule

Any G4 failure is recorded before correction.

Initial classification:

- `ADAPTER BUG`
- `EFFECT-DOMAIN LIMITATION`
- `KERNEL ABSTRACTION FALSIFIED`
- `UNRESOLVED`

Do not automatically classify a real-domain failure as "unsupported adapter."

## Architecture reopen

Only a justified `KERNEL ABSTRACTION FALSIFIED` finding may reopen the semantic/architecture freeze.

If kernel semantics change:

- G1–G3 acceptance is invalidated;
- reference baseline must be rerun;
- G4 must be rerun;
- no earlier PASS is grandfathered.

Forbidden:

`Git problem → quietly weaken invariant → PASS`

## Exit criteria

G4 may be proposed for Human acceptance only after:

- all preregistered Claim A/B/C transfer attack classes were actually executed or explicitly blocked by a preregistered precondition;
- exact candidate and execution instance were recorded;
- frozen modeled target remained unchanged;
- no kernel-semantic special case was introduced on entry;
- fresh-context audit completed;
- all findings durably recorded and dispositioned;
- no OPEN finding currently falsifies A/B/C for the transfer candidate.

Human acceptance of G4, together with accepted G1–G3, yields:

`AGENCY KERNEL v0 COMPLETE`

This remains a bounded falsification result, not a proof of universal security.

## Out of scope

- arbitrary Git repositories;
- arbitrary working-tree semantics;
- multiple protected refs;
- user-controlled hooks;
- unsafe/unbounded alternates;
- general filesystem effects outside the frozen modeled target;
- proof of Git security in general;
- proof of Docker/GitHub/host security;
- broker/OS compromise.

## Forbidden architecture changes during G4

No change to frozen kernel semantics, threat model, modeled-target type, Claim A/B/C meaning, uncertainty policy, admission semantics, state-binding requirements, coverage requirements, attribution requirements, or compliance/acceptance orthogonality.

Any required semantic change must first be recorded and classified through the architecture-reopen procedure.
