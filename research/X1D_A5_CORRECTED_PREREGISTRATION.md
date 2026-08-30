# X1D-A5 — CORRECTED PREREGISTRATION

Status: PREREGISTRATION ONLY / EXECUTION NOT AUTHORIZED

Repository context: `FJ899/8`

Human decision state at freeze:

- `X1D-F001 = VERIFIED CLOSED`
- Human ACCEPT recorded separately; this document does not extend that acceptance.
- `FJ899/scriptops PR #27 = DO NOT MERGE`
- `A5 EXECUTION = NOT AUTHORIZED`
- `V1 = STOP`
- release / deployment / tag = NOT AUTHORIZED

## 1. Purpose

A5 tests the remaining end-to-end binding question after X1D-F001 closure:

> Does the Human-authorized, exact decision content/scope remain bound to the exact canonical effect actually produced, without silent substitution, scope expansion, or effect mismatch?

This preregistration defines the experiment shape only. It does not authorize creation of A5 probe artifacts in ScriptOps, execution of any A5 transition, merge, canonical mutation, A5 closure, V1, release, deployment, or tag.

## 2. Separation of phases

The following phases are distinct and must not be collapsed:

1. `CORRECTED PREREGISTRATION FREEZE` — this artifact.
2. `A5 PRE-EXECUTION PACKET` — separately prepared, readied, reviewed, and frozen before execution.
3. `AK-CANON EXECUTABILITY REVIEW` — independent review of whether the packet is sufficiently executable without interpretation during the run.
4. `HUMAN EXECUTION AUTHORIZATION` — separate explicit Human decision.
5. `A5 EXECUTION` — only after the preceding phases pass and are explicitly authorized.
6. `AUDIT / RESULT / HUMAN ACCEPT` — separate from execution and never implied by technical PASS.

`PREREGISTRATION != EXECUTION AUTHORIZATION`

## 3. Required frozen inputs before execution

The A5 PRE-EXECUTION PACKET must freeze, at minimum:

- authoritative and applicable `Q_K@v`;
- exact Human decision tuple `D`;
- exact probe candidate `HEAD` and `TREE`;
- exact content manifest;
- exact scope manifest;
- exact intended effect manifest;
- exact canonical pre-state;
- allowed PR / review / readiness / merge transitions;
- required evidence for every transition and every tested predicate;
- STOP behavior for mismatch, ambiguity, counterexample, or target mutation.

No material value above may be supplied ad hoc during execution.

## 4. Probe design constraint

The execution probe must use one dedicated, inert A5 artifact that does not change product behavior.

The probe exists only to make content / scope / effect binding observable under real repository mechanics. Its canonical effect, if the positive control is eventually reached and separately authorized, must remain a controlled test artifact rather than a product-functional change.

Dedicated A5 branches, commits, and PRs are permitted as probe artifacts only after separate Human authorization of A5 execution.

This preregistration creates none of them.

## 5. A5 predicates

The experiment must separately attack at least these properties:

### A5-CONTENT
The canonical effect must correspond to the exact Human-authorized content, not a substituted or materially altered payload.

### A5-SCOPE
The canonical effect must remain inside the exact Human-authorized scope; no additional path, object, semantic responsibility, or repository effect may be silently added.

### A5-EFFECT
The observed canonical effect must be the effect that was authorized and predicted by the frozen packet; success cannot be inferred from intent, command success, PR state, or merge-event existence alone.

The positive control may establish end-to-end binding only after all preregistered negative attacks survive.

## 6. Execution order — frozen

The run order is fixed:

1. `PREFLIGHT`
2. `CONTENT ATTACK`
3. `SCOPE ATTACK`
4. `EFFECT ATTACK`
5. `EXACT-EFFECT POSITIVE CONTROL`

The order may not be rearranged during the run.

## 7. First-counterexample rule

At the first credible negative counterexample:

`FAIL -> DURABLE FINDING -> STOP`

After first credible FAIL:

- do not repair;
- do not continue to later attacks;
- do not run the positive control;
- do not redesign the mechanism in the same run;
- do not reinterpret the failed target as a new target;
- do not declare A5 PASS;
- do not start V1.

Unknown or materially incomplete evidence yields `BLOCKED`, not PASS.

## 8. Preflight invariants

Before any A5 execution action, the executor/auditor must verify the exact frozen packet still matches reality.

Any mutation of a packet-bound candidate HEAD/TREE, canonical pre-state, applicable `Q_K@v`, rule-bearing governance state, or other frozen execution identity invalidates the execution target.

On mismatch:

`TARGET IDENTITY MISMATCH -> STOP -> NEW FREEZE REQUIRED`

No silent refresh is allowed.

## 9. Exact effect and GitHub-generated merge identity

The PRE-EXECUTION PACKET must resolve, before execution, how expected post-effect identity is represented when GitHub generates the final merge commit and its future SHA cannot be known in advance.

This preregistration does not choose that mechanism.

The packet and subsequent AK-CANON executability review must explicitly determine whether the preregistered expected post-effect identity is represented by a composition such as:

- exact expected post-effect `TREE`;
- exact candidate `HEAD`;
- exact base identity;
- exact permitted merge method;
- exact permitted diff/effect manifest;
- with final generated canonical `HEAD` captured and frozen only after the operation;

or by another equally explicit mechanism.

This question may not be left to interpretation during execution.

`UNKNOWN FUTURE MERGE SHA != PERMISSION FOR RUNTIME IMPROVISATION`

## 10. Evidence discipline

Each step in the future execution packet must state:

- predicate under test;
- allowed action;
- forbidden action;
- pre-state evidence;
- transition evidence;
- post-state evidence;
- exact identity binding requirements;
- PASS condition;
- FAIL condition;
- BLOCKED condition;
- STOP condition.

`CLAIM != EVIDENCE`

`COMMAND SUCCESS != EFFECT TRUTH`

`MERGE EVENT != AUTHORIZED EFFECT PROOF`

## 11. Historical evidence preserved

This preregistration preserves, without rewriting:

- FJ899/8 PR #67 as the valid historical FAIL of the previous bootstrap model;
- FJ899/8 PR #71 as the valid historical BLOCKED T1–T10 result;
- FJ899/8 PR #72 as the supplemental exact-target T1–T10 PASS;
- the separate Human ACCEPT / X1D-F001 verified-closure record;
- ScriptOps PR #27 as `DO NOT MERGE` unless separately authorized.

No prior result is retroactively rewritten by A5.

## 12. Explicit STOP state after this freeze

After this corrected preregistration is frozen:

```text
A5 CORRECTED PREREGISTRATION: FROZEN
A5 PRE-EXECUTION PACKET: NOT YET PREPARED
AK-CANON EXECUTABILITY REVIEW: NOT STARTED
A5 EXECUTION: NOT AUTHORIZED
SCRIPTOPS PROBE ARTIFACTS: NOT CREATED
SCRIPTOPS PR #27: DO NOT MERGE
V1: STOP
RELEASE / DEPLOYMENT / TAG: NOT AUTHORIZED
```

The only next permissible project step is preparation of a separate A5 PRE-EXECUTION PACKET after a new Human instruction.
