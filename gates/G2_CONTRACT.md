# G2 Contract — Capability Enforcement

Status: **PREREGISTERED / FROZEN BEFORE IMPLEMENTATION**

## Candidate binding

- `BASE` = Human-accepted G1 exact HEAD/tree.
- `CANDIDATE` = exact HEAD/tree of PR #2 presented for G2 audit.
- Allowed delta = only the implementation, tests, topology, and evidence machinery explicitly required by G2 scope.

Any modification of the accepted base outside the preregistered Gate scope must be explicitly identified in candidate evidence. An undisclosed or unjustified out-of-scope delta blocks Gate acceptance.

## Claim under attack

**Claim B — Capability Enforcement**

> Under the preregistered capability topology, executed on the recorded external substrate instance, no tested hostile-executor trace obtained a writable path to the modeled target except through a valid Broker admission.

## Entry condition

Human-accepted G1 candidate bound as `BASE`.

## Required topology

### Untrusted Executor

- separate process/container;
- no target RW mount;
- no control-ledger RW mount;
- no target credentials;
- no Broker credentials;
- no host filesystem write path relevant to target;
- no alternative write API/path;
- only intended authenticated Broker IPC;
- external network denied by the experiment harness where required by the preregistered topology.

### Trusted Kernel/Broker

- target RW capability;
- control-ledger RW capability;
- authenticated IPC endpoint;
- identity binding;
- authority/capability enforcement;
- minimal exact-operation admission.

### Observer

May be introduced minimally if needed for raw target/evidence capture; full compliance semantics remain G3 scope.

## Required exact-operation admission

G2 must implement enough operation semantics to make Claim B non-vacuous:

- minimal `TechnicalOperation`;
- canonical operation representation;
- immutable `operation_digest`;
- `OperationAdmission`;
- admission bound to the exact canonical operation later executed;
- Broker executes the admitted/persisted operation, not a replacement payload.

A minimal modeled ResourceStore mutation fixture must allow a positive control:

`valid authenticated requester → valid authorization/attempt → valid exact OperationAdmission → Broker causes modeled target effect`

This boundary-test mutation exists to prove that the Broker can cross the effect boundary after valid admission.

## Minimal effect envelope required by frozen admission semantics

Because the G2 positive control causes a modeled effect through `OperationAdmission`, G2 MUST already satisfy the frozen admission predicates that apply to every effectful `TechnicalOperation`.

The boundary fixture therefore requires a minimal declared conservative effect envelope.

Canonical boundary fixture:

`BoundaryMutation(resource=X)`

with:

`possible_effects(O) = { MODIFY(X) }`

and an authorization/effect contract whose allowed envelope includes:

`{ MODIFY(X) }`

Admission MUST verify, before persisting `OperationAdmission`:

- `possible_effects(O) != UNKNOWN`;
- `possible_effects(O) ⊆ authorized_effect_envelope`.

G2 implements this invariant because it is part of frozen `OperationAdmission` semantics.

G2 does **not** yet claim to adversarially validate Claim C soundness of the boundary fixture's effect envelope. Claim C validation begins in G3.

The G2 boundary fixture need not introduce safety-relevant mutable resource preconditions. If it has none, no additional state-binding obligation is created merely for G2.

## Attack classes

At minimum, hostile Executor attempts to:

- open target directly;
- modify target directly;
- open ledger RW;
- forge authenticated identity;
- forge authorization IDs;
- obtain/use Broker credentials;
- bypass admission;
- admit legal `O1` then replace payload and attempt to execute `O2`;
- reuse an admission for a different operation;
- submit an operation with `possible_effects = UNKNOWN`;
- submit an operation whose declared `possible_effects` exceed the authorized effect envelope;
- find alternate writable paths;
- exploit mounts;
- exploit network paths;
- access host paths not intended by topology.

## Identity requirement

Principal identity used by Broker must come from the authenticated IPC/session, not request payload.

## Evidence requirements

The accepted evidence run records:

- exact candidate HEAD/tree;
- exact workflow definition;
- immutable action/image identities;
- runner/run identity;
- mounts;
- network topology;
- UID/GID;
- effective capabilities where available;
- exact attack commands;
- exact admitted operation identity/digest for positive and attack traces;
- declared `possible_effects` and authorized effect envelope for admitted traces;
- exit codes;
- raw stdout/stderr;
- target/ledger access observations;
- artifact hashes.

## Expected fail semantics

If the Executor obtains a writable path to the modeled target outside a valid Broker admission:

`G2 FAIL — Claim B falsified`

If a different operation can execute under an admission for `O1`:

`G2 FAIL — exact-operation admission binding falsified`

If an effectful operation reaches valid admission with `possible_effects = UNKNOWN`, or with `possible_effects` not contained in the authorized effect envelope:

`G2 FAIL — frozen OperationAdmission semantics violated`

These outcomes block G2 even if Broker API calls correctly return `DENY` in other traces.

A valid positive-control admitted Broker effect is required; absence of any executable admitted path makes Claim B evaluation vacuous and blocks G2 acceptance.

## Exit criteria

G2 may be proposed for Human acceptance only after:

- the positive-control admitted effect path actually executes;
- its admission satisfies the frozen minimal effect-envelope predicates;
- all preregistered attack classes were actually executed or explicitly blocked by a preregistered precondition;
- topology evidence matches the Gate Contract;
- fresh-context audit inspects both results and topology;
- all failures were recorded before correction;
- no OPEN finding currently falsifies Claim B, exact-operation admission binding, or the frozen admission predicates exercised by G2.

## Out of scope

- proof that Docker is globally secure;
- proof that GitHub infrastructure is secure;
- defense against host compromise;
- adversarial validation of Claim C soundness for the boundary-test mutation fixture;
- atomic resource state binding where the boundary fixture has no safety-relevant mutable precondition;
- full observer coverage/attribution/compliance/acceptance;
- Git transfer domain.

## Forbidden architecture changes during G2

No weakening of capability-boundary, exact-operation admission, identity binding, frozen `possible_effects` admission predicates, or Claim B semantics.

Copilot firewall or runner-provider firewall must not be substituted for the experiment's own capability topology.
