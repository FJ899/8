# X1B Human Decision Authorship V2 — Independent AK-CANON Implementation Re-review R4

Status: `INDEPENDENT IMPLEMENTATION RE-REVIEW / PASS / NO EXECUTION AUTHORITY`

Date: `2026-09-03`

## 1. Verdict

```text
AK-CANON X1B HUMAN DECISION AUTHORSHIP V2 IMPLEMENTATION RE-REVIEW R4 = PASS
```

No in-scope implementation blocker remains established against the exact frozen candidate reviewed here.

This PASS is an implementation-review disposition only. It is not authority to create a live executable screenplay decision request, submit a Human screenplay approval, invoke ScriptOps `approve`, move the canonical ScriptOps ref, merge, close X1B, claim V1 authority, release, deploy or tag.

## 2. Exact review target

Repository:

```text
FJ899/scriptops
```

Pull request:

```text
PR #35
```

Exact candidate:

```text
BASE = 2f22843ac570498b506101addeba5453ab777f08
BASE TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
HEAD = 7c40a92165714023743e91c63b5b11b102fadd92
TREE = 31e1f15a2e667811b9617bbb10bf6af2242961b0
COMMITS = 1
CHANGED FILES = 13
BEHIND BASE = 0
```

The exact candidate commit has exactly one parent:

```text
2f22843ac570498b506101addeba5453ab777f08
```

The 13 changed paths remain exactly within the Human-frozen implementation surface:

```text
.github/workflows/x1b-human-decision.yml
HANDOFF.md
PROJECT_STATE.md
README.md
SOURCE_MANIFEST.md
legacy/scriptops-v2-single.py
phase6/scriptops-v2-hardening.py
phase6/x1b_human_decision.py
scripts/restore_v2.py
scripts/verify_repository.py
sources/prototype/RESTORE.md
tests/test_phase6_scriptops_smoke.py
tests/test_x1b_human_decision.py
```

During this R4 review, `FJ899/scriptops main` was re-read and remained exact baseline:

```text
2f22843ac570498b506101addeba5453ab777f08
```

`FJ899/8 main` was re-read and remained:

```text
1e4114e3f7ab6383af2549383b25329bed21eef9
```

No main-branch mutation is performed by this review.

## 3. Governing specification and accepted scope

Normative implementation specification:

```text
FJ899/8 PR #155
HEAD = 3509c6e0922b28eb2d141fb3599ee21a1c7ee102
BLOB = e796e00c778c4b149dbc79abf05795a61450360d

+

FJ899/8 PR #158
HEAD = e188a452b0960d846479a975fc2d9f2c76aac50d
BLOB = ff06a772275bc861de9211375e8bda08d67ead3e
```

Specification-level independent PASS:

```text
FJ899/8 PR #159
```

Scope firewall remains the Human-accepted convergence disposition of PR #150 / PR #151. This review does not reopen TPM, PMEM/NFIT, EK/AK, CRL, bare-metal locality, BMC/console provenance or universal crash durability.

## 4. Prior implementation findings — final dispositions

### 4.1 Initial implementation F001 — symbolic-main CAS substitution

Initial finding in PR #160:

```text
X1B-V2-IMPL-F001 — MAIN-REF CAS DEREFERENCES A CONCURRENT SYMBOLIC refs/heads/main AND CAN MUTATE AN UNBOUND TARGET REF
```

Human repair authority: PR #161.

Final candidate requires direct `refs/heads/main` at authority/effect checkpoints and canonicalizes only with:

```text
git update-ref --no-deref refs/heads/main NEW OLD
```

Deterministic regressions cover both pre-effect symbolic-main rejection and the narrow race after the direct-ref check; the symref target is not mutated.

Disposition:

```text
X1B-V2-IMPL-F001 = CLOSED
```

### 4.2 R2 F005 supported-host proof

R2 finding in PR #162:

```text
X1B-V2-IMPL-R2-F001 — F005 SUPPORTED-HOST LIVE GITHUB AUTHORITY POSITIVE-PATH EVIDENCE IS ABSENT
```

Human proof authority: PR #163.

Inert Human evidence: PR #164.

Trusted Human review:

```text
review id = 5106168696
user.id = 226907434
state = APPROVED
H = a9326fc3524f9c1073785901df24520aa9d0a364
request digest = d7820bee447aea43861f097d21da8133c41157deac360d8ec2e250729222a8d8
```

Supported-host proof: PR #165, workflow run `33799081048`, job `100793781612`, conclusion `success`.

The proof established the isolated child positive path with direct public GitHub reads, no Authorization, durable Human user ID `226907434`, hostname verification, `CERT_REQUIRED`, TLS >= 1.2 and nonempty default CA roots.

R4 specifically compared the authority/currentness/network-child source region in reviewed predecessor `b281383...` with final candidate `7c40a921...`; the child/request/currentness/TLS logic is unchanged. The only later production-runtime change is the separately authorized parent-side credential/proxy fail-closed guard in `approve_scene`, before child invocation. Therefore the PR #165 live proof remains evidence for the unchanged F005 child boundary rather than being silently generalized across changed child code.

Disposition:

```text
X1B-V2-IMPL-R2-F001 = CLOSED BY PR #165 EVIDENCE
```

### 4.3 R3 F001 — incomplete frozen deterministic matrix

R3 finding in PR #166:

```text
X1B-V2-IMPL-R3-F001 — MANDATORY DETERMINISTIC X1B ATTACK / CURRENTNESS / CAS / GIT / FAIL-CLOSED TEST MATRIX IS NOT IMPLEMENTED
```

Human test/evidence-completion authority: PR #167.

Final candidate now executes/maps the full frozen matrix:

```text
A1..A10
RB1..RB5
ID1..ID5
CUR1..CUR13
CAS1..CAS9
GIT1..GIT6
PU1..PU6
TLS1..TLS15
retained malformed/drift/replay/token-proxy/network/replace-ref/mode/metadata fail-closed cases
```

The repository verifier now has an explicit matrix map and fails if a required evidence marker disappears. The map contains 82 frozen case labels. The workflow executes the grouped hostile-environment, prospective-commit, failure-truth and isolated-child fuses in addition to the permanent unittest suites.

Disposition:

```text
X1B-V2-IMPL-R3-F001 = CLOSED
```

### 4.4 R3T F001 — forbidden parent credential/proxy environment

The first mandatory regression added under PR #167 exposed a real runtime defect and correctly stopped test-only work. Finding frozen in PR #168:

```text
X1B-V2-R3T-F001 — FORBIDDEN PARENT GITHUB CREDENTIAL / PROXY ENVIRONMENT REACHES THE AUTHORITY-CHILD INVOCATION INSTEAD OF FAILING CLOSED
```

Human bounded runtime repair authority: PR #169.

The final `approve_scene()` now rejects a nonempty value for every frozen parent authority variable before Git discovery, lock/preflight or network-child invocation:

```text
GITHUB_TOKEN
GH_TOKEN
GITHUB_ENTERPRISE_TOKEN
GH_ENTERPRISE_TOKEN
HTTP_PROXY
HTTPS_PROXY
ALL_PROXY
http_proxy
https_proxy
all_proxy
```

The exact regression that originally failed now passes for the complete list.

Disposition:

```text
X1B-V2-R3T-F001 = CLOSED
```

## 5. Final-head CI evidence

All required final-head checks execute on exact candidate HEAD:

```text
x1b-human-decision
run = 33802491835
conclusion = success

Verify repository state
run = 33802491822
conclusion = success

Phase 6 ScriptOps smoke
run = 33802491776
conclusion = success
```

The X1B workflow on the exact final HEAD reports success for:

```text
parent credential/proxy fail-closed regression
CAS1 + GIT1..GIT6 fuse
CAS3..CAS5 + wrong mode + machine metadata fuse
CAS7..CAS8 pre/post-CAS failure-truth fuse
CUR2/CUR12 + TLS1..TLS15 deterministic child fuse
full unittest suites
repository self-verification
historical reconstruction integrity
```

The Phase-6 workflow independently runs the full deterministic Phase-6 regression and repository semantic/currentness verifier successfully.

Accordingly:

```text
GREEN CI = EXECUTION OF THE NOW-COMPLETE FROZEN MATRIX
```

rather than the R3 condition where omitted tests could not be inferred from green CI.

## 6. Human-origin and exact-binding review

The final implementation retains the accepted V2 chain:

```text
HumanDecisionRequestV2
-> exact GitHub APPROVED review
-> durable GitHub user.id = 226907434
-> immutable review.commit_id H
-> exact request/content/effect reconstruction at H
-> X1BOperationAdmissionV2
-> prospective exact two-path commit
-> direct named-ref CAS
-> post-effect truth
-> HumanDecision = TRUE
```

Review selection uses numeric Human identity rather than mutable display login. Wrong-ID/Human-looking reviews and reserved-marker ambiguity fail closed. Latest Human authority-relevant state determines currentness; immutable H prevents proposer head motion from substituting new content under an old review.

The original distinctions remain true:

```text
APPROVAL COMMAND POSSESSION != HUMAN DECISION AUTHORSHIP
NON-EMPTY WHY != HUMAN ACT
HUMAN DECISION EVIDENCE != MACHINE ADMISSION != EXECUTOR CAPABILITY
```

## 7. Git/effect no-substitution review

`AnchoredGitV2` derives the intended ScriptOps root from source location, strips inherited `GIT_*`, freezes git-dir/common-dir, and invokes authority-critical Git with explicit repository/work-tree arguments and executor-controlled environment.

The final matrix exercises hostile values for:

```text
GIT_DIR
GIT_WORK_TREE
GIT_COMMON_DIR
GIT_INDEX_FILE
GIT_OBJECT_DIRECTORY
GIT_ALTERNATE_OBJECT_DIRECTORIES
GIT_NAMESPACE
GIT_CONFIG_COUNT / KEY / VALUE
GIT_CONFIG_GLOBAL
GIT_CONFIG_SYSTEM
GIT_NO_REPLACE_OBJECTS
```

The common-dir lock serializes cooperating X1B operations. Prospective commit verification rejects wrong parent, extra path, scene/log mismatch, wrong modes and non-machine metadata before canonicalization.

The canonical linearization remains atomic named-ref CAS using `--no-deref`. Pre-CAS failure leaves real ref/index/worktree unchanged. Post-CAS synchronization failure yields `RECOVERY_REQUIRED`, not false `HumanDecision=TRUE`.

Direct legacy `cmd_approve`, `scene-promote --to accepted`, CLI parser paths and direct function-call bypasses are all exercised fail-closed.

No contrary in-scope no-substitution counterexample was established in R4.

## 8. TLS / authority-reader review

The child still receives exactly:

```text
X1B_NETWORK_CHILD=1
```

and constructs stdlib TLS after process start. No parent CA/proxy/token/Python-path environment is inherited. Parent independently reparses child evidence. The deterministic suite covers malformed/extra/missing child results, link-pagination ambiguity, network failure during immutable-H retrieval, fixed child request schema, TLS invariants and fresh-child/no-cache behavior.

The real public positive path remains PR #165. No new runtime code was introduced inside that proven child boundary after the proof.

No F005 counterexample is established on the final candidate.

## 9. Scope-firewall result

R4 found no reason to reopen any C-class platform/hardware property. All reviewed issues and repairs remained inside the frozen X1B properties:

```text
Human origin
exact content/scope/candidate/effect binding
currentness/supersession/replay
fail-closed evidence handling
Human evidence separation from effect capability
anchored Git identity
local exclusivity + exact CAS
legacy bypass closure
negative/positive verification
post-effect logical truth
```

Convergence strategy remains valid.

## 10. PASS disposition

The exact frozen candidate satisfies the implementation-level conditions necessary to proceed to preregistered corrective verification.

```text
IMPLEMENTATION REVIEW R4 = PASS
X1B = STILL OPEN
REAL HUMAN POSITIVE SCREENPLAY CONTROL = NOT YET EXECUTED
CANONICAL SCREENPLAY EFFECT = NOT YET EXECUTED
CORRECTIVE CLOSURE = NOT YET ESTABLISHED
V1 AUTHORITY = NO
```

This PASS does not itself authorize the next live effect-bearing stage.

## 11. Next legal stage

Per the already Human-accepted sequence:

```text
prepare and freeze a fresh preregistered corrective-verification packet
-> STOP
-> separate Human execution authorization
-> full negative matrix + real Human positive control
-> independent corrective-closure review
-> Human corrective-closure acceptance
```

The verification packet may specify future evidence and exact execution boundaries, but until separate Human execution authorization it must not create a live executable screenplay decision PR, solicit/consume Human approval for a canonical screenplay effect, invoke ScriptOps `approve`, perform the canonical CAS or claim X1B closure.

Preserve:

```text
IMPLEMENTATION REVIEW PASS != EXECUTION AUTHORITY
PREREGISTRATION != EXECUTION
AI PROPOSES != HUMAN DECIDES
```
