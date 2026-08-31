# X1D-A5 — CONTRACT CORRECTION AMENDMENT

Status: `CORRECTIVE PREREGISTRATION AMENDMENT / NOT EXECUTED`
Date: `2026-08-31`
Repository context: `FJ899/8`

## 1. Human authority for this amendment

Human authorized preparation of a separate corrective preregistration amendment resolving the blocker recorded in FJ899/8 PR #75 by introducing:

`PROBE PREPARATION AUTHORITY != A5 EXECUTION AUTHORITY`

This amendment is the authorized correction artifact only. The current Human instruction ends after preparation of this amendment and therefore does not itself execute probe preparation.

## 2. Historical records preserved

The following remain valid and are not rewritten:

- FJ899/8 PR #74 — frozen corrected A5 preregistration;
- FJ899/8 PR #75 — valid validation-contract blocker;
- `X1D-F001 = VERIFIED CLOSED`;
- `FJ899/scriptops PR #27 = DO NOT MERGE`;
- `V1 = STOP`.

PR #75 remains the correct historical observation that the #74 sequence required an exact candidate identity before the candidate was permitted to exist.

This amendment supersedes only that preparation-order contradiction. It does not erase the blocker record and does not alter the A5 claim, attack classes, first-counterexample discipline, or acceptance semantics.

## 3. Corrected phase separation

The corrected sequence is:

```text
CORRECTED PREREGISTRATION FREEZE (#74)
→ CONTRACT BLOCKER RECORD (#75)
→ CORRECTIVE PREREGISTRATION AMENDMENT (this artifact)
→ HUMAN PROBE-PREPARATION AUTHORITY
→ INERT PROBE CANDIDATE PREPARATION ONLY
→ PRE-EXECUTION PACKET WITH EXACT CANDIDATE HEAD/TREE
→ AK-CANON EXECUTABILITY REVIEW
→ SEPARATE HUMAN A5 EXECUTION AUTHORIZATION
→ A5 EXECUTION
→ RESULT / AUDIT / HUMAN ACCEPT AS SEPARATE LATER PHASES
```

Invariant:

`PROBE PREPARATION AUTHORITY != A5 EXECUTION AUTHORITY`

Probe preparation creates an identity-bearing experimental candidate. It does not run the experiment and does not authorize a canonical effect.

## 4. Bounded future probe-preparation authority

This amendment permits a later Human-directed exercise of probe preparation solely to materialize an exact inert A5 candidate whose identities can be frozen in the PRE-EXECUTION PACKET.

Before any such preparation action, ScriptOps must still match the frozen execution-start environment from PR #74, including at minimum:

- repository: `FJ899/scriptops`;
- `main HEAD = 30095c3170d16263e2db553a2b199bd6e33feace`;
- `main TREE = 7ba16fab7879d7640801c410f171a08f79c8168b`;
- CODEOWNERS blob: `5dd686893d265217d921c352df033ff72fdf910e`;
- ruleset: `21147233 / CANONICAL_MAIN_PROTECTION_V1 / active` with the frozen relevant semantics;
- PR #27 remains unmerged and excluded.

Any mismatch before candidate preparation yields:

`PREPARATION TARGET MISMATCH -> STOP -> NO PROBE CREATED`

No silent refresh or rebase is allowed.

## 5. Exact permitted preparation surface

When separately instructed to exercise the bounded preparation authority, the preparation step may perform only the minimum actions needed to obtain a real immutable candidate identity:

1. create one dedicated A5 branch from the exact frozen ScriptOps base;
2. create one inert A5 probe commit;
3. add only one dedicated inert probe artifact;
4. open one Draft PR targeting `main`;
5. read back and freeze the exact candidate HEAD, TREE, changed path set, blob/content identity, base identity, and PR identity for the PRE-EXECUTION PACKET.

The intended inert probe path is:

`governance/X1D_A5_INERT_BINDING_PROBE.md`

Its sole purpose is to provide a harmless identity-bearing object for content/scope/effect binding tests. It must not modify runtime code, product behavior, existing governance rules, CODEOWNERS, branch protection, rulesets, decision logs, release state, deployment state, or unrelated repository semantics.

If this exact path already exists or cannot be created as a single inert artifact without broader changes:

`PREPARATION COLLISION / SCOPE EXPANSION REQUIRED -> STOP`

No substitute path may be chosen ad hoc.

## 6. Forbidden during probe preparation

Probe preparation authority does NOT authorize:

- A5 execution;
- Human approval of the probe;
- requesting or manufacturing a Human approval as A5 evidence;
- marking the probe PR Ready for review;
- merging the probe PR;
- any canonical effect on `main`;
- any ScriptOps repair or implementation change;
- any change to CODEOWNERS, rulesets, branch protection, or Human-authority semantics;
- any `approve --why` or equivalent Human-decision operation;
- reuse, mutation, or merge of PR #27;
- V1;
- release;
- deployment;
- tag.

The probe PR must remain Draft and unmerged throughout preparation.

`CANDIDATE EXISTENCE != HUMAN APPROVAL`

`CANDIDATE EXISTENCE != A5 EXECUTION`

`DRAFT PR != CANONICAL EFFECT`

## 7. PRE-EXECUTION PACKET after probe preparation

Only after the inert candidate exists may the PRE-EXECUTION PACKET freeze its actual identities.

The packet must include, at minimum:

- exact ScriptOps base HEAD/TREE;
- exact probe PR identity;
- exact probe candidate HEAD/TREE;
- exact changed path set;
- exact probe blob/content identity;
- exact content manifest;
- exact scope manifest;
- exact intended effect manifest;
- exact canonical pre-state;
- authoritative/applicable `Q_K@v`;
- the exact decision tuple specification `D` to be presented for Human decision during the later A5 execution;
- allowed transitions and forbidden transitions;
- complete evidence requirements;
- exact expected post-effect identity representation, including the resolved GitHub-generated merge-SHA treatment;
- PASS / FAIL / BLOCKED / STOP predicates.

Clarification required by this correction:

The packet freezes the exact candidate-bound decision tuple to be presented during execution. It does not claim that the Human has already approved that tuple during probe preparation.

The actual Human decision/approval event and its durable evidence may occur only inside the separately authorized A5 execution sequence under the applicable `Q_K@v`.

`DECISION TUPLE SPECIFICATION != HUMAN DECISION EVENT`

## 8. Review and execution gate

After the PRE-EXECUTION PACKET is frozen:

1. AK-CANON performs the separate executability review required by PR #74;
2. any contract ambiguity or identity gap yields STOP and correction before execution;
3. only after a satisfactory executability review may Human separately authorize A5 execution;
4. A5 execution then follows the frozen order from PR #74:

```text
PREFLIGHT
→ CONTENT ATTACK
→ SCOPE ATTACK
→ EFFECT ATTACK
→ EXACT-EFFECT POSITIVE CONTROL
```

The first credible counterexample still requires:

`FAIL -> DURABLE FINDING -> STOP`

No repair or compensating PASS is permitted in the same run.

## 9. Non-authorizations preserved

This amendment does not authorize A5 execution, Human approval, merge, canonical effect, ScriptOps repair, PR #27 merge, V1, release, deployment, or tag.

It authorizes no ScriptOps mutation in the current amendment-preparation step.

Any later exercise of the bounded probe-preparation authority must occur only after a new Human instruction following this STOP.

## 10. State after amendment preparation

```text
#74: HISTORICAL FROZEN PREREGISTRATION — PRESERVED
#75: VALID CONTRACT BLOCKER — PRESERVED

X1D-A5 CONTRACT CORRECTION:
PREPARED AS SEPARATE AMENDMENT

PROBE PREPARATION AUTHORITY:
DEFINED / BOUNDED
NOT EXERCISED IN THIS STEP

A5 PROBE:
NOT CREATED

A5 PRE-EXECUTION PACKET:
NOT PREPARED

AK-CANON EXECUTABILITY REVIEW:
NOT STARTED

A5 EXECUTION:
NOT AUTHORIZED / NOT STARTED

FJ899/scriptops PR #27:
DO NOT MERGE

V1:
STOP

RELEASE / DEPLOYMENT / TAG:
NOT AUTHORIZED
```

# STOP
