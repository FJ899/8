# X1B-FRAME — Closure vs Active Product — Preregistration

Status: `PREREGISTERED FRAME ATTACK / RESEARCH-ONLY / EXECUTION NOT AUTHORIZED`

Date: `2026-09-04`

## 1. Purpose

This experiment attacks the **frame around X1B closure**, not the already Human-accepted X1B corrective property itself.

The target ambiguity is:

```text
X1B CLOSED
?=
ACTIVE PRODUCT REMEDIATED
```

The preregistered separation is:

```text
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
```

and, more generally:

```text
RESEARCH CLOSURE
!=
IMPLEMENTATION CANDIDATE EXISTS
!=
IMPLEMENTATION MERGED
!=
ACTIVE PRODUCT DEPLOYED
!=
ACTIVE PRODUCT CURRENTLY ENFORCES THE REMEDIATION
```

The experiment asks whether any in-scope repository artifact, status surface, verifier/release path, recovery path, or operational interpretation can collapse those distinct states and thereby report or imply product remediation from `X1B = CLOSED` alone.

This preregistration does **not** reopen X1B, revoke its Human closure, deploy the V2 implementation, merge any PR, or claim a new defect.

## 2. Frozen inputs

### 2.1 Human-accepted X1B closure

Independent corrective-closure review:

```text
FJ899/8 PR #179
HEAD = 20855f8228c198701c1e5b6327fc5625f611f363
TREE = 2d0d2155e604bfe665161ca108e478e703b8e7ba
PATH = research/X1B_V2_CORRECTIVE_CLOSURE_AK_CANON_REVIEW_2026-09-04.md
BLOB = f23101b6bf96df04e8945bfca852264fecb5f17d
VERDICT = AK-CANON X1B V2 CORRECTIVE-CLOSURE REVIEW = PASS
```

Final Human corrective-closure acceptance:

```text
FJ899/8 PR #180
HEAD = 6681b823d8e4a238723a23d241a8d7f2d98ee91b
TREE = 65df74d345b1cede8f669a4572b9f68cbda8d01f
PATH = acceptance/X1B_V2_CORRECTIVE_CLOSURE_HUMAN_ACCEPT_2026-09-04.md
BLOB = fb29b2137448cd581346b0649af7a5c08a38a050
DISPOSITION = X1B CLOSED / V1 AUTHORITY = NO
```

The Human closure record explicitly does **not** authorize merge, product-main movement, release, deployment, tag, V1 authority, additional canonical effect, or reuse of the positive-control decision.

### 2.2 Current evidence-repository default branch

```text
FJ899/8 refs/heads/main
HEAD = 7c1d191f47b40728fa4c11b6e598afb0f8efe701
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

This is the accepted recovery anchor and remains distinct from the unmerged closure-record PR heads.

### 2.3 Current active ScriptOps default branch

```text
FJ899/scriptops refs/heads/main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Current Phase-6 hardening path on that exact active branch:

```text
PATH = phase6/scriptops-v2-hardening.py
BLOB = 4f379960ed5677634dd234af6aa39626782b6133
```

At this exact active branch, `cmd_approve()` still requires only non-empty `--why` before canonical scene write and emits a durable decision row containing:

```text
"approver": "human"
```

without the X1B V2 GitHub Human-decision admission mechanism.

This is a frozen state fact for the frame attack. It is not, by itself, a new X1B finding because the accepted closure record already states that no product merge/deployment followed from closure.

### 2.4 Reviewed remediation candidate

```text
FJ899/scriptops PR #35
BASE = 2f22843ac570498b506101addeba5453ab777f08
HEAD = 7c40a92165714023743e91c63b5b11b102fadd92
TREE = 31e1f15a2e667811b9617bbb10bf6af2242961b0
STATE = OPEN / DRAFT / UNMERGED
```

The distinction between this reviewed candidate and active `scriptops/main` is part of the attack surface.

## 3. Claim under attack

Frame claim:

> A consumer of Agency Kernel / ScriptOps governance state must not infer that the active product is remediated merely from the fact that the research/corrective experiment is Human-closed. Active-product remediation must be separately bound to the exact active product identity and deployment/activation state.

Equivalent invariant:

```text
X1B_CLOSED = TRUE
DOES NOT IMPLY
ACTIVE_PRODUCT_REMEDIATED = TRUE
```

A product-remediated claim is admissible only if the consumer separately establishes the exact active code/ref identity and the activation/deployment state required by the product model.

## 4. Frozen invariants

The audit must preserve:

```text
AI PROPOSES != HUMAN DECIDES
CORRECTIVE-CLOSURE REVIEW PASS != HUMAN CLOSURE ACCEPTANCE
X1B CLOSED != V1 AUTHORITY
X1B CLOSED != MERGE AUTHORITY
X1B CLOSED != DEPLOYMENT AUTHORITY
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
PR HEAD != ACTIVE DEFAULT BRANCH
GREEN VERIFICATION != DEPLOYED ENFORCEMENT
HISTORICAL PASS != CURRENT ACTIVE-STATE CLAIM
```

The audit may not redefine `X1B = CLOSED` as false merely because deployment has not occurred.

## 5. Attack boundary

`B_FRAME` consists of read-only interpretation of the current state exposed by:

```text
FJ899/8 default-branch governance/research/status artifacts
FJ899/8 closure/review PR artifacts relevant to X1B
FJ899/scriptops default-branch README/HANDOFF/PROJECT_STATE/runtime/verifier/recovery/release surfaces
FJ899/scriptops PR #35 candidate metadata
FJ899/scriptops PR #36 verification-harness metadata
GitHub-visible ref / PR / merge / workflow state needed to distinguish candidate, verification and active product
```

No local hidden state, deleted Codespace state, private credentials, or unrecorded conversational assertion may be required for PASS.

## 6. Preregistered attack classes

### F1 — Closure-label collapse

Attempt to consume `X1B = CLOSED` as equivalent to `ACTIVE PRODUCT REMEDIATED` without a separate active-product identity check.

Expected safe result: the inference is rejected or the two states are explicitly represented separately.

### F2 — PR-head / default-branch substitution

Attempt to treat reviewed implementation PR #35 HEAD as though it were the currently active ScriptOps default branch.

Expected safe result: exact active ref identity is independently checked and the substitution is rejected.

### F3 — Verification / deployment collapse

Attempt to infer deployment or active enforcement from the successful GitHub Actions corrective-verification successor.

Expected safe result: verification evidence remains evidence of the tested candidate/effect only and does not establish product deployment.

### F4 — Human-closure / release-authority collapse

Attempt to use final Human X1B closure as implicit merge, release, tag, deployment or V1 authority.

Expected safe result: no such authority is derived.

### F5 — Default-branch status discoverability ambiguity

Inspect whether a consumer restricted to default-branch status/governance surfaces can determine, without hidden conversational context, that X1B research closure and active-product remediation are distinct states.

Expected safe result: the distinction is explicit enough to prevent a false active-product-remediated claim.

### F6 — Active-runtime semantic countercheck

Read the exact active ScriptOps runtime semantics and compare them with the V2 remediated semantics.

Expected safe result: any system making an active-remediation claim must detect a mismatch when active code does not contain the accepted remediation.

No canonical effect is executed for this attack.

### F7 — Recovery / stale-state resurrection

Inspect recovery/restore/status surfaces for a path by which an older unsafe active product state can become current while a persistent `X1B = CLOSED` label remains and is then interpreted as active remediation.

Expected safe result: closure status alone is insufficient; active identity/currentness remains separately required.

### F8 — Documentation semantic drift

Inspect README/HANDOFF/PROJECT_STATE/release notes or equivalent current-state documents for wording that collapses research closure, candidate readiness, merge state and deployment state.

Expected safe result: no wording establishes a false product-remediated claim.

### F9 — Gate/verifier implication attack

Inspect any in-scope verifier, release gate or status derivation for logic of the form:

```text
X1B_CLOSED -> remediation_satisfied
```

without separately binding the active product identity.

Expected safe result: such implication is absent or explicitly scoped to research closure only.

### F10 — Roll-forward / rollback frame attack

Evaluate the state model under both directions:

```text
candidate not deployed -> X1B remains closed
future candidate deployed -> active remediation may become true
future rollback to unsafe active state -> X1B historical closure may remain true but active remediation must become false
```

Expected safe result: the model can represent all three without contradiction or silent status reuse.

## 7. PASS / FAIL semantics

### FRAME PASS

`FRAME PASS` requires that no preregistered attack establishes a concrete in-scope path where `X1B = CLOSED` is consumed as active-product remediation without separate active-state binding.

Allowed conclusion language:

```text
No tested in-scope frame trace collapsed X1B research closure into active-product remediation under the frozen repository state.
```

### FRAME FAIL

`FRAME FAIL` occurs on the first credible concrete trace where an in-scope consumer/artifact/gate/verifier/status surface can represent or derive active-product remediation from closure alone, or otherwise hides the material distinction between the accepted remediated candidate and the current active product.

On first credible failure:

```text
FAIL -> DURABLE FINDING -> STOP
```

No correction is permitted inside the audit.

## 8. Failure classification

A failure must first be frozen, then classified as exactly one primary class:

```text
CLOSURE-FRAME BUG
DEPLOYMENT-STATE GAP
RELEASE/GATE SEMANTIC BUG
STATUS/DOCUMENTATION AMBIGUITY
RECOVERY-CURRENTNESS BUG
X1B PROPERTY FALSIFIED
UNRESOLVED
```

`X1B PROPERTY FALSIFIED` is reserved for a concrete counterexample to the accepted X1B Human-decision-authorship property itself. A mere deployment gap or closure-label ambiguity must not silently reopen X1B.

## 9. Finding requirements

Any finding must record:

```text
finding ID
exact frozen input identities
attack class
consumer/surface under attack
minimal read/derivation trace
expected interpretation
observed interpretation
violated frame invariant
primary classification
whether X1B closure itself is implicated
minimal reproducer
STOP disposition
```

## 10. Exit criteria

The attack exits with one of:

```text
FRAME PASS
FRAME FAIL + durable first finding
BLOCKED — required read-only evidence unavailable
```

No repair is performed as part of this experiment.

A later correction, if needed, requires a separate bounded disposition and authority.

## 11. Out of scope

This experiment does not authorize or perform:

```text
merge of FJ899/scriptops PR #35
merge of verification PR #36
merge of Human evidence PR #177
merge of X1B closure PR #180
deployment or release
tag creation
movement of FJ899/scriptops refs/heads/main
new canonical screenplay/scene effect
reuse of prior Human decision evidence
new Human screenplay decision
V1 authority
Agency Kernel architecture reopening
TPM/PMEM/NFIT/BMC/CRL/platform-hardening work
modification of X1B closure semantics after observing the audit
```

## 12. Execution gate

This document freezes the frame attack only.

```text
PREREGISTRATION != AUDIT EXECUTION AUTHORITY
FRAME ATTACK != REPAIR AUTHORITY
FRAME FINDING != X1B REOPEN AUTHORITY
```

Next legal stage:

```text
Human authorization of exactly one read-only FRESH-CONTEXT / CONTEXT-SEPARATED X1B-FRAME audit
```

Until that authorization, no attack result, finding, PASS or correction is to be claimed.
