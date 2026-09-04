# X1B-FRAME — First Credible Finding F001

Status: `FRAME FAIL / FIRST CREDIBLE COUNTEREXAMPLE / STOP / NO REPAIR AUTHORITY`

Date: `2026-09-04`

## 1. Finding

```text
X1B-FRAME-F001 — DEFAULT-BRANCH CURRENT-STATE / HANDOFF SURFACES
PRESERVE THE KNOWN-UNSAFE approve --why HUMAN-DECISION MODEL
AND OMIT THE UNMERGED X1B V2 REMEDIATION STATE
```

Primary classification:

```text
STATUS/DOCUMENTATION AMBIGUITY
```

Preregistered attack class:

```text
F5 — Default-branch status discoverability ambiguity
```

Supporting cross-check only, not a second finding:

```text
F8 — Documentation semantic drift
```

Per preregistration:

```text
FIRST CREDIBLE COUNTEREXAMPLE = STOP
```

No further F1–F10 attack discovery is performed in this audit after this finding.

## 2. Frozen audit authority and preregistration

Preregistered frame attack:

```text
FJ899/8 PR #181
HEAD = a7ca5abc422da0f0d8e347baf7f27bbf7f3a53aa
TREE = 55f8f8672cce152831784f36b5fe78e86231c79b
PATH = experiments/X1B_FRAME_CLOSURE_VS_ACTIVE_PRODUCT_PREREGISTRATION_2026-09-04.md
BLOB = 089bd0cce0ee2e6ac5af06375ea4ce636d1c2c6e
```

Human audit authorization:

```text
accept
```

The authorization was consumed only for exactly one read-only fresh-context/context-separated X1B-FRAME audit under PR #181.

## 3. Frozen current repository identities

Evidence repository current default branch during the audit:

```text
FJ899/8 refs/heads/main
HEAD = 7c1d191f47b40728fa4c11b6e598afb0f8efe701
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

Active ScriptOps default branch during the audit:

```text
FJ899/scriptops refs/heads/main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Exact active Human-approval runtime path:

```text
PATH = phase6/scriptops-v2-hardening.py
BLOB = 4f379960ed5677634dd234af6aa39626782b6133
```

Reviewed remediation candidate remains separate and unmerged:

```text
FJ899/scriptops PR #35
BASE = 2f22843ac570498b506101addeba5453ab777f08
HEAD = 7c40a92165714023743e91c63b5b11b102fadd92
TREE = 31e1f15a2e667811b9617bbb10bf6af2242961b0
STATE = OPEN / DRAFT / UNMERGED
```

Final Human X1B corrective-closure record remains separate and unmerged:

```text
FJ899/8 PR #180
HEAD = 6681b823d8e4a238723a23d241a8d7f2d98ee91b
STATE = OPEN / DRAFT / UNMERGED
DISPOSITION = X1B CLOSED / V1 AUTHORITY = NO
```

The PR #180 body explicitly states that the closure creates no merge, product-main movement, release or deployment authority.

## 4. Claim attacked

Preregistered frame invariant:

```text
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
```

F5 expected safe result:

> A consumer restricted to default-branch status/governance surfaces can determine, without hidden conversational context, that X1B research closure and active-product remediation are distinct states.

The current-state surface must therefore not present the known-old Human-decision mechanism as the current valid Human-decision model while omitting the existence/state of the separately reviewed remediation candidate.

## 5. Minimal read / derivation trace

### Step 1 — consumer resolves the active ScriptOps default branch

The live default branch is:

```text
2f22843ac570498b506101addeba5453ab777f08
```

It is not the reviewed V2 remediation candidate HEAD `7c40a921...`.

### Step 2 — consumer follows the repository's own startup route

Current `README.md` tells a new AI/session to read, first:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
DECISION_LOG.md
...
```

The same README labels the current repository state:

```text
PHASE 6 CONTROLLED WORKFLOW MECHANISM PASS
```

and states:

```text
kanoniczny zapis Phase 6 następuje dopiero po approve --why
```

It also directs the next Human effect gate to provide an exact `why` and then authorize `approve --why` / canonical write.

### Step 3 — current state names the old attribution rule as the Human decision model

Current `PROJECT_STATE.md` defines the slice responsibility model as:

```text
human approve --why = semantic decision
canonical scene write = consequence after human decision
decision log + Git = durable evidence
```

It also states that `PROJECT_STATE.md` is the current state owner and that the current live main should be resolved before consequential work.

### Step 4 — current HANDOFF reinforces the same model

Current `HANDOFF.md` states:

```text
Lokalne źródło prawdy: PROJECT_STATE.md
```

and describes the proof as including:

```text
approve --why jest obowiązkowe
impact report istnieje przed human decision
canonical scene jest zapisywana dopiero po explicit approval
decision log + Git zachowują evidence
```

It identifies `DEC-SO-011` from `2026-08-21` as the latest explicit Human decision in the active handoff and directs the next effect through the same `approve --why` route.

### Step 5 — active runtime matches the old model

At exact active `main@2f22843...`, `cmd_approve()` requires only a non-empty `--why` before the canonical scene write and then writes a durable decision row with:

```json
"approver": "human"
```

without the X1B V2 GitHub Human-decision admission mechanism.

### Step 6 — repository verifier positively preserves this current-state framing

Current `scripts/verify_repository.py` requires the active hardening source to contain:

```text
approve --why
"why": why
```

and positively reconciles current `README.md`, `PROJECT_STATE.md` and `HANDOFF.md`, printing PASS messages for the B1–B5/current-state contract.

It does not bind those current-state PASS claims to the unmerged X1B V2 remediation candidate or expose a distinct `ACTIVE_PRODUCT_REMEDIATED` state.

### Step 7 — X1B closure/remediation information is outside that startup/default-branch current-state model

The Human-accepted X1B closure is recorded in separate unmerged PR #180, and the V2 implementation is in separate unmerged ScriptOps PR #35.

Neither is represented in the current default-branch ScriptOps startup/status/handoff state as the distinction:

```text
X1B research closure = CLOSED
active product remediation = NOT DEPLOYED / FALSE
```

## 6. Expected vs observed

Expected:

```text
CURRENT STATUS SURFACE
must distinguish
research closure
from
active product remediation
```

and, while active code is still the pre-remediation implementation, the old `approve --why` path must not be presented as the current sufficient Human-decision model without an explicit warning that it is not X1B-remediated.

Observed:

```text
active default-branch startup route
-> current PROJECT_STATE/HANDOFF
-> old approve --why model is named as Human semantic decision / explicit approval
-> active verifier positively preserves that model
-> reviewed V2 remediation remains unmerged and absent from current-state framing
```

A fresh consumer using the repository's declared current-state route cannot reconstruct the required frame distinction from those current surfaces alone. The material difference between "X1B research closed" and "active ScriptOps still pre-remediation" is therefore not represented where the repository says current operational interpretation lives.

## 7. Violated invariant

```text
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
```

More precisely:

```text
CURRENT-STATE/HANDOFF TRUTH
must not hide
ACTIVE PRODUCT IDENTITY != REVIEWED REMEDIATION CANDIDATE IDENTITY
```

The finding does not require or claim that PR #180 itself falsely says deployment occurred. PR #180 explicitly preserves the separation. The defect is that the active product's own current-state/startup surfaces do not carry that separation forward and continue to affirm the old Human-decision model.

## 8. X1B closure implication

```text
X1B PROPERTY FALSIFIED = NO
X1B CLOSURE REOPENED = NO
```

This is not a counterexample to the accepted X1B Human-decision-authorship property or to the corrective verification of PR #35.

It is a frame/status propagation defect between:

```text
accepted research closure
reviewed remediation candidate
active product identity
operational startup/current-state interpretation
```

Therefore the primary classification is exactly:

```text
STATUS/DOCUMENTATION AMBIGUITY
```

and not `X1B PROPERTY FALSIFIED`.

## 9. Minimal reproducer

Read-only:

```text
1. Resolve FJ899/scriptops refs/heads/main -> 2f22843...
2. Read active README.md startup order and approve --why current route.
3. Read active PROJECT_STATE.md responsibility model:
   human approve --why = semantic decision.
4. Read active HANDOFF.md current source-of-truth and next effect route.
5. Read active phase6/scriptops-v2-hardening.py and observe
   non-empty --why -> canonical write -> "approver":"human".
6. Read active scripts/verify_repository.py and observe that it positively
   preserves the old approve --why/current-state contract.
7. Compare with unmerged PR #35 and unmerged final X1B closure PR #180.
```

No canonical effect, write to ScriptOps, merge, deployment or local execution is needed.

## 10. Disposition

```text
X1B-FRAME AUDIT = FRAME FAIL
X1B-FRAME-F001 = OPEN
PRIMARY CLASS = STATUS/DOCUMENTATION AMBIGUITY
FIRST CREDIBLE COUNTEREXAMPLE = STOP
X1B = REMAINS CLOSED AT ITS ACCEPTED RESEARCH/CORRECTIVE SCOPE
ACTIVE PRODUCT REMEDIATED = NOT ESTABLISHED
```

This finding authorizes no repair, no merge of PR #35, no deployment, no update of README/PROJECT_STATE/HANDOFF/verifier, no X1B reopen, no V1 authority and no release/tag.

Next legal stage is a separate Human disposition of this exact finding and, only if authorized, a bounded correction plan for frame/status propagation.

Preserve:

```text
FRAME FINDING != REPAIR AUTHORITY
FRAME FINDING != X1B REOPEN AUTHORITY
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
AI PROPOSES != HUMAN DECIDES
```
