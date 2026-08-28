# G3 Contract — Controlled Effect Soundness

Status: **PREREGISTERED / FROZEN BEFORE IMPLEMENTATION**

## Candidate binding

- `BASE` = Human-accepted G2 exact HEAD/tree.
- `CANDIDATE` = exact HEAD/tree of PR #3 presented for G3 audit.
- Allowed delta = only the implementation, tests, and evidence machinery explicitly required by G3 scope.


Any modification of the accepted base outside the preregistered Gate scope must be explicitly identified in candidate evidence. An undisclosed or unjustified out-of-scope delta blocks Gate acceptance.


## Claims under attack

Primary:

**Claim C — Effect-Domain Soundness**

For the supported `VersionedResourceStore` primitive, no accepted tested trace may falsify:

`actual_effects(O) ⊆ possible_effects(O)`

and required mutable preconditions must remain bound to the mutation boundary.

Cumulative semantic regression:

**Claim A — complete cross-layer checks now made non-vacuous by G3**

including the preregistered attacks requiring `DID`, `WITHIN_SCOPE`, `SATISFIED`, observation, attribution, compliance, or acceptance.

## Entry condition

Human-accepted G1 and G2 candidates, with G2 exact-operation admission already present and bound to the admitted operation.

## Required controlled domain

Separate durable stores:

- `control-ledger.db` = control/authority history;
- `target.db` = modeled reality.

These must not be collapsed into one database merely to obtain cross-boundary atomicity.

## Supported candidate primitive

The supported G3 primitive is:

`put_if_version(resource, expected_version, value)`

It must provide:

1. **Effect legibility** — conservative `possible_effects(operation)`.
2. **State binding** — relevant mutable precondition bound to mutation.
3. **Target-side mutation provenance** — mutation and provenance committed atomically at the target boundary.

Claim C applies to this supported primitive and any other primitive explicitly added to the supported candidate set.

## Exact-operation admission

G3 reuses the G2 exact-operation admission invariant.

The supported primitive must execute only the exact canonical operation bound by `OperationAdmission`.

## Required observer semantics

Observer is executor-independent and read-only.

It may read:

- target state;
- target mutation provenance;
- control ledger/evidence.

Attribution must not rely only on Executor or Broker self-report.

Expected chain:

`OperationAdmission + target-side mutation provenance + observed state → attributable effect`

## Required compliance semantics

Compliance requires:

`OBSERVATION + COVERAGE + ATTRIBUTION`

Missing required coverage or unresolved attribution → `INDETERMINATE`.

Acceptance remains orthogonal to compliance.

## Claim A cross-layer attack classes

At minimum, now that the relevant semantics exist:

- `DID → AUTHORIZED`;
- `ATTEMPTED → EFFECT`;
- `SATISFIED → AUTHORIZED`;
- `SATISFIED → WITHIN_SCOPE`;
- successful outcome attempts to retroactively authorize an effect;
- observed delta attempts to become attribution without required evidence.

## Claim C attack classes

At minimum:

- stale resource version;
- concurrent mutation;
- unknown `possible_effects`;
- effect-envelope over-approximation;
- supported primitive effect-envelope under-approximation;
- missing observation coverage;
- ambiguous attribution;
- crash before mutation;
- crash after admission before mutation;
- crash after mutation before control-plane completion record;
- replay after uncertain crash;
- acceptance PASS with compliance FAIL.

## Negative control — intentionally unsound mutant

`DishonestPrimitive` is a **negative-control mutant**, not a supported candidate primitive.

It deliberately declares:

`possible_effects = {A}`

while causing:

`A + B`

Expected negative-control result:

- `EFFECT OCCURRED = YES`
- `COMPLIANCE = FAIL`
- `EFFECT MODEL = UNSOUND`
- `TCB ASSUMPTION = FALSIFIED / DETECTED`
- compliance must not be misclassified as PASS.

If the system produces that expected diagnostic result, the **negative-control test passes**. This does not mean the kernel prevented the unauthorized effect.

Because the mutant is explicitly outside the supported candidate primitive set, its deliberate unsoundness does not by itself falsify candidate Claim C.

By contrast, if the actual supported `put_if_version()` ever under-approximates its possible effects, that is:

`G3 FAIL — Claim C falsified`

and requires a durable finding.

## Crash policy

After an uncertain crash:

- do not blindly replay;
- observe target;
- inspect trusted target-side provenance;
- if occurrence/attribution remains unresolved → `INDETERMINATE`.

The experiment does not claim distributed exactly-once execution.

## Exit criteria

G3 may be proposed for Human acceptance only after:

- supported-primitive Claim C attack classes executed;
- G3 cross-layer Claim A attacks executed non-vacuously;
- negative-control mutant behaves according to its preregistered diagnostic semantics;
- crash/concurrency traces are deterministic or barrier-controlled rather than sleep-based;
- target/control boundaries are preserved;
- fresh-context audit completed;
- no OPEN finding currently falsifies Claim C for the supported candidate primitive or the now-testable cross-layer portion of Claim A.

After Human acceptance:

`REFERENCE BASELINE LOCKED`

## Out of scope

- Git;
- arbitrary shell primitive;
- general filesystem effects;
- broker/OS compromise;
- mathematical proof of effect-domain soundness.

## Forbidden architecture changes during G3

No weakening of effect-envelope, state-binding, coverage, attribution, uncertainty, compliance/acceptance, exact-operation admission, or Claim A semantics.
