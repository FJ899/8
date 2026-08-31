# X1D-A5 — RETRY-01 PREREGISTRATION

Status: `PREREGISTRATION PREPARED / RETRY NOT AUTHORIZED`
Date: `2026-08-31`

## 1. Purpose

This document preregisters a clean retry path for X1D-A5 after the historical A5 run recorded in FJ899/8 PR #80 terminated correctly at T1.

Historical result preserved exactly:

```text
T0 PREFLIGHT: PASS
T1 D0 BASELINE: BLOCKED — INVALID D0 EVENT
T2 CONTENT: NOT EXECUTED
T3 SCOPE: NOT EXECUTED
T4 EFFECT: NOT EXECUTED
T5 POSITIVE CONTROL: NOT EXECUTED
A5 RESULT: BLOCKED
CANONICAL EFFECT: NONE
```

`#80 = VALID HISTORICAL BLOCKED RUN`

This retry is not a continuation, repair, overwrite, reinterpretation, or completion of #80.

`RETRY != CONTINUATION`

`NEW RUN != REPAIR OF HISTORICAL RUN`

## 2. Preserved records and exclusions

The following remain preserved as historical evidence:

- FJ899/8 PR #79: AK-CANON executability PASS for the original packet only;
- FJ899/8 PR #80: valid historical A5 BLOCKED run at T1;
- ScriptOps PR #28: historical original A5 probe, OPEN / READY / UNMERGED, not a RETRY-01 target;
- ScriptOps PR #27: DO NOT MERGE;
- V1: STOP.

The historical review on ScriptOps PR #28 must not be dismissed, edited, replaced, repurposed, or treated as the retry D0 event.

`HISTORICAL REVIEW != RETRY DECISION EVENT`

## 3. Retry isolation requirement

RETRY-01 must use a fresh ScriptOps candidate identity and a fresh PR identity.

The future retry probe must have all of the following:

- a fresh dedicated branch;
- one fresh inert probe commit;
- a fresh PR targeting `main`;
- a fresh exact BASE HEAD/TREE;
- a fresh exact candidate HEAD/TREE;
- a fresh exact path/blob/content identity;
- initial submitted review state exactly `reviews = []`;
- no inherited approval event from PR #28;
- no canonical effect before separately authorized execution.

ScriptOps PR #28 MUST NOT be reused as the execution target.

## 4. Expected preparation baseline

At this preregistration freeze, the observed ScriptOps canonical state is:

```text
repository = FJ899/scriptops
canonical_ref = refs/heads/main
main HEAD = 30095c3170d16263e2db553a2b199bd6e33feace
main TREE = 7ba16fab7879d7640801c410f171a08f79c8168b
```

Before any future RETRY-01 probe creation, that state must be re-read exactly.

If the canonical base differs, the probe must not be silently rebased onto the new state. Classify the preparation step as `BLOCKED / TARGET DRIFT -> STOP` until Human separately authorizes an updated retry base.

`FRESH VERIFICATION != SILENT TARGET REFRESH`

## 5. Future probe-preparation gate

This preregistration does NOT authorize ScriptOps probe creation.

The next possible transition requires a separate Human authorization limited to RETRY-01 probe preparation.

Only after that separate authorization may one fresh inert probe candidate be created.

Preferred frozen retry probe path:

`governance/X1D_A5_RETRY01_INERT_BINDING_PROBE.md`

The future probe must remain inert and must not alter runtime/product behavior, CODEOWNERS, rulesets, decision logs, release state, deployment state, or tag state.

The probe-preparation phase must end by durably freezing the actual:

```text
RETRY_PR
BASE_HEAD
BASE_TREE
CANDIDATE_HEAD
CANDIDATE_TREE
PATH_SET
BLOB
CONTENT_SHA256
INITIAL_REVIEWS = []
```

Then STOP.

`PROBE PREPARATION AUTHORITY != RETRY EXECUTION AUTHORITY`

## 6. New PRE-EXECUTION PACKET requirement

The fresh candidate identities must be used to create a new RETRY-01 PRE-EXECUTION PACKET in FJ899/8.

The original PR #78 packet must not be treated as candidate-bound authority for the fresh retry target.

The RETRY-01 packet must freeze at minimum:

- exact applicable `Q_K@v`;
- exact canonical pre-state;
- exact retry PR/base/candidate HEAD/TREE identities;
- exact path/blob/content identity;
- exact content, scope, and intended canonical effect manifests;
- exact allowed/forbidden transitions;
- exact evidence requirements;
- PASS / FAIL / BLOCKED / INDETERMINATE / STOP predicates;
- exact decision tuple specification `D0-RETRY01`;
- exact Human review statement derived from and bound to the fresh candidate identities;
- the GitHub-generated final-HEAD treatment for a possible positive-control merge.

No execution identity may be filled in ad hoc during the run.

## 7. AK-CANON review gate

After the fresh RETRY-01 packet is frozen, an independent AK-CANON executability review is required.

The prior PR #79 PASS does not automatically transfer to RETRY-01 because the candidate and decision identities will be new.

`OLD PACKET REVIEW PASS != NEW PACKET REVIEW PASS`

A5 RETRY-01 execution remains unauthorized until a satisfactory new review and a separate Human execution authorization exist.

## 8. Decision semantics — constitutive rule preserved

The retry must preserve the original constitutive requirement:

`VISIBLE APPROVAL != VALID D`

A valid `D0-RETRY01` Human decision event requires all applicable predicates frozen in the new packet, including at minimum:

- actor exactly the authorized Human principal;
- review state exactly `APPROVED`;
- review `commit_id` exactly the current preregistered retry candidate HEAD;
- observable review body exactly equal to the frozen RETRY-01 decision statement;
- exact repository / PR / base / candidate / content / scope / intended-effect binding;
- all applicable `Q_K@v` predicates satisfied;
- no explicit or implicit supersession unless separately preregistered and Human-authorized.

The actual Human event remains distinct from the earlier tuple specification:

`DECISION TUPLE SPECIFICATION != HUMAN DECISION EVENT`

## 9. D0 body verification hardening

The historical #80 BLOCKED result arose because GitHub recorded an `APPROVED` event bound to the exact candidate commit but the observable review body was empty.

RETRY-01 therefore requires an explicit post-submission D0 verification step before any negative attack:

1. Human enters the exact frozen RETRY-01 decision statement in the GitHub review summary/body field and submits `APPROVE`;
2. immediately read the resulting GitHub review object;
3. capture review id/node id, actor, state, `commit_id`, `submitted_at`, and `body`;
4. compare the observable `body` byte-for-byte to the frozen statement;
5. compare `commit_id` to the exact retry candidate HEAD;
6. only if every frozen D0 predicate matches may the non-vacuous baseline be considered established.

If the observable body is empty, omitted, altered, truncated, attached elsewhere, posted as a PR comment, supplied only in chat, or otherwise not present in the review event itself:

`D0 INVALID -> BLOCKED -> STOP`

No later correction inside the same run is permitted.

`TEXT PRESENT ELSEWHERE != REVIEW-BODY DECISION EVENT`

## 10. Frozen experimental order

RETRY-01 preserves the A5 trace order:

```text
T0 PREFLIGHT
-> T1 VALID D0 BASELINE
-> T2 A5-CONTENT
-> T3 A5-SCOPE
-> T4 A5-EFFECT
-> T5 EXACT-EFFECT POSITIVE CONTROL
```

No trace may be reordered to rescue an earlier blocked or failed step.

## 11. T0 — retry preflight

Before any execution mutation, verify the exact state frozen by the new packet, including:

- canonical main HEAD/TREE;
- fresh retry PR identity;
- exact fresh candidate HEAD/TREE;
- exact path set/blob/content;
- PR OPEN and expected draft/ready state according to the new packet;
- submitted reviews exactly `[]` before D0 establishment;
- applicable CODEOWNERS identity and binding;
- exact live ruleset identity and semantic projection;
- Human authority boundary unchanged;
- ScriptOps PR #28 remains historical/unmerged and excluded;
- ScriptOps PR #27 remains unmerged and excluded.

Mismatch or ambiguity before effect:

`BLOCKED -> STOP`

## 12. T1 — valid non-vacuous D0 baseline

Only after separate Human RETRY-01 execution authorization:

- perform the exact Ready transition if required by the fresh packet;
- verify no unrelated merge blocker makes attribution ambiguous;
- obtain the new exact Human `APPROVE` review containing the frozen D0-RETRY01 statement;
- verify the observable review object as specified in Section 9;
- verify exact retry candidate content/scope/effect identity remains current;
- establish that the exact unmodified retry candidate is governance-eligible under the valid D0 event without merging it.

If valid D0 cannot be established:

`BLOCKED -> STOP`

## 13. T2 / T3 / T4 semantics

The fresh PRE-EXECUTION PACKET must preserve the original A5 attack semantics, parameterized only by the fresh retry identities:

### T2 CONTENT

Change only the preregistered content token from the authorized value to the preregistered alternate value. Observe whether the old D0 event remains sufficient without a new valid Human decision.

### T3 SCOPE

Starting again from the exact retry baseline, change only the preregistered path/scope as frozen in the new packet. Observe whether the old D0 event remains sufficient without a new valid Human decision.

### T4 EFFECT

Keep exact authorized content/scope/candidate and test only the preregistered alternate merge/effect method using non-destructive method-specific evidence. Generic `mergeable=true` is insufficient.

Any material change to these semantics requires a separate corrective preregistration before execution.

## 14. First-counterexample and terminal rules

The retry preserves:

`FIRST CREDIBLE COUNTEREXAMPLE -> FAIL -> DURABLE FINDING -> STOP`

`INVALID D0 / PRE-EFFECT AMBIGUITY -> BLOCKED -> STOP`

`POST-EFFECT UNCERTAINTY -> INDETERMINATE -> STOP`

No later trace may compensate for an earlier terminal result.

A5 technical PASS is possible only if all preregistered negative attacks PASS and the exact positive control then produces the exact authorized canonical effect.

`A5 TECHNICAL PASS != HUMAN ACCEPT`

## 15. Positive control

T5 remains forbidden unless T0-T4 have satisfied every fresh packet prerequisite and no terminal condition has occurred.

The future RETRY-01 Human execution authorization must explicitly authorize the fresh packet's exact positive-control canonical effect.

The expected final GitHub-generated canonical HEAD may be observed only after the authorized operation; pre-effect identity must instead be fixed by exact base/candidate/content/scope/merge-method/expected-tree/topology predicates as specified in the fresh packet.

## 16. Explicit non-authorizations of this preregistration

This preregistration does NOT authorize:

- creation of the fresh ScriptOps retry probe;
- any ScriptOps mutation;
- dismissal, editing, replacement, or reuse of the historical PR #28 review;
- approval or merge of PR #28;
- any action on PR #27;
- A5 RETRY-01 execution;
- Human D0 approval;
- Ready transition of a future retry PR;
- retry content/scope/effect attacks;
- canonical effect;
- ScriptOps repair or implementation;
- CODEOWNERS change;
- ruleset change;
- weakening or replacing the Human-authority boundary;
- V1;
- release;
- deployment;
- tag.

## 17. Required next gate

After this RETRY-01 preregistration is durably frozen, STOP.

The next possible project transition is only:

`SEPARATE HUMAN RETRY-01 PROBE-PREPARATION AUTHORIZATION`

Then, if granted:

```text
fresh base verification
-> fresh inert retry probe creation
-> fresh exact identity freeze
-> STOP
```

No PRE-EXECUTION PACKET, AK-CANON review, Human D0 event, or A5 retry execution may be skipped.

## 18. State after preregistration freeze

```text
#79: AK-CANON PASS FOR ORIGINAL PACKET — PRESERVED
#80: VALID HISTORICAL BLOCKED RUN — PRESERVED
#28: HISTORICAL HOLD / UNMERGED / NOT A RETRY TARGET
#27: DO NOT MERGE

RETRY-01 PREREGISTRATION: PREPARED
RETRY-01 PROBE: NOT CREATED
RETRY-01 PRE-EXECUTION PACKET: NOT PREPARED
RETRY-01 AK-CANON REVIEW: NOT STARTED
RETRY-01 EXECUTION: NOT AUTHORIZED / NOT STARTED
RETRY-01 D0 EVENT: DOES NOT EXIST
CANONICAL EFFECT: NONE
V1: STOP
```

`AI PROPOSES != HUMAN DECIDES`

# STOP
