# X1B Human Decision Authorship V2 — Independent AK-CANON Implementation Re-review R3

Status: `INDEPENDENT IMPLEMENTATION RE-REVIEW / NOT REPAIR OR EXECUTION AUTHORITY`

Date: `2026-09-03`

## 1. Verdict

```text
AK-CANON X1B HUMAN DECISION AUTHORSHIP V2 IMPLEMENTATION RE-REVIEW R3 = NOT PASS
```

First credible blocker in this R3 review:

```text
X1B-V2-IMPL-R3-F001 — MANDATORY DETERMINISTIC X1B ATTACK / CURRENTNESS / CAS / GIT / FAIL-CLOSED TEST MATRIX IS NOT IMPLEMENTED = BLOCKER
```

This is a frozen specification/evidence failure, not a newly invented hardware/platform requirement and not a claim that a new runtime exploit has been established.

The separately missing F005 supported-host public-GitHub/TLS positive path from R2 is materially satisfied by the Human-authorized proof frozen in PR #165. The prior symbolic-main implementation blocker is also materially closed. The candidate nevertheless cannot receive implementation-review PASS because the governing implementation brief explicitly makes the full deterministic negative/positive matrix executable evidence a PASS condition, while the frozen candidate implements only a subset of that matrix.

Per the review rule:

```text
FIRST CREDIBLE COUNTEREXAMPLE / MANDATORY-PROOF FAILURE = STOP
```

No further blocker discovery is claimed after R3-F001.

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
HEAD = b281383be083be24d7e4b9f6c9411d3cc1c317f2
TREE = aa2b974efa01f55e0f909a0de60fcbde2b7e6a3f
COMMITS = 1
CHANGED FILES = 13
BEHIND BASE = 0
```

The exact ScriptOps `main` was re-read during this review and remained:

```text
2f22843ac570498b506101addeba5453ab777f08
```

The evidence/governance repository `FJ899/8 main` was re-read and remained:

```text
1e4114e3f7ab6383af2549383b25329bed21eef9
```

No main-branch mutation is performed by this review.

## 3. Governing implementation specification

Normative composite:

```text
FJ899/8 PR #155
HEAD = 3509c6e0922b28eb2d141fb3599ee21a1c7ee102
BLOB = e796e00c778c4b149dbc79abf05795a61450360d

+

FJ899/8 PR #158
HEAD = e188a452b0960d846479a975fc2d9f2c76aac50d
BLOB = ff06a772275bc861de9211375e8bda08d67ead3e
```

Brief review:

```text
FJ899/8 PR #159 = PASS
```

The PR #155 brief explicitly freezes:

```text
section 29 — original X1B attacks A1..A10
section 30 — F001 identity tests ID1..ID5
section 31 — F002 currentness tests CUR1..CUR13
section 32 — F003 CAS/concurrency tests CAS1..CAS9
section 33 — F004 Git-environment tests GIT1..GIT6
section 34 — retained malformed/drift/replay/network/replace/mode/metadata fail-closed tests
section 34 — positive deterministic PU1..PU6
section 39 criterion 9 — required negative/positive tests are executable
```

PR #158 additionally freezes TLS tests TLS1..TLS15 and states that the existing PR #155 negative/positive F001-F004, original-X1B and bypass tests remain mandatory without modification.

Therefore test-matrix completeness is not optional hardening and is not being added by this review.

## 4. Prior implementation findings — disposition

### 4.1 Initial implementation F001

Prior finding:

```text
X1B-V2-IMPL-F001 — main-ref CAS dereferences a concurrent symbolic refs/heads/main
```

Human repair authority:

```text
FJ899/8 PR #161
```

The reviewed candidate now:

```text
requires refs/heads/main to be direct at authority/effect checkpoints
uses git update-ref --no-deref refs/heads/main NEW OLD
contains deterministic pre-effect symbolic-main rejection
contains deterministic narrow-race no-deref regression
```

Disposition:

```text
X1B-V2-IMPL-F001 = MATERIALLY CLOSED
```

### 4.2 R2 F005 positive-path evidence

R2 finding:

```text
X1B-V2-IMPL-R2-F001 — F005 supported-host live GitHub authority positive-path evidence is absent
```

Human proof authority:

```text
FJ899/8 PR #163
```

Inert Human review evidence:

```text
FJ899/8 PR #164
H = a9326fc3524f9c1073785901df24520aa9d0a364
review numeric ID = 5106168696
review user.id = 226907434
state = APPROVED
request digest = d7820bee447aea43861f097d21da8133c41157deac360d8ec2e250729222a8d8
```

Supported-host proof:

```text
FJ899/8 PR #165
HEAD = 117ed075b7b056587f17c5643cb7eefff76b002f
TREE = d9053c23683dd0ee6c3f8d6e573de79ef7aafb5d
BLOB = 7ba4f9b6c3f412ec980da010ba311b04f44d1c60
workflow run = 33799081048
job = 100793781612
conclusion = success
```

The exact child from candidate HEAD `b281383...` successfully performed the real public GitHub reviews/content reads and observed:

```text
human user.id = 226907434
review id = 5106168696
check_hostname = true
verify_mode = CERT_REQUIRED
minimum TLS >= 1.2
default CA x509_ca = 121
forbidden caller CA/token/proxy/PYTHON variables absent from child environment
```

Disposition:

```text
X1B-V2-IMPL-R2-F001 = MATERIALLY SATISFIED BY PR #165 PROOF
```

This R3 NOT PASS is therefore not a repetition of F005.

## 5. R3-F001 — exact mandatory-proof failure

### 5.1 Candidate deterministic X1B suite actually present

The frozen `tests/test_x1b_human_decision.py` contains a compact suite covering, among other things:

```text
test_wrong_login_same_name_does_not_override_numeric_id
test_nonhuman_reserved_marker_denied
test_latest_changes_requested_or_dismissed_denies
test_duplicate_json_key_denied
test_request_candidate_or_effect_drift_denied
test_network_child_env_is_fresh
test_anchored_git_ignores_attacker_git_environment
test_positive_two_path_cas_effect
test_stale_base_cannot_canonicalize
test_symbolic_main_substitution_is_rejected_before_effect
test_no_deref_cas_cannot_mutate_symref_target_if_race_follows_check
test_legacy_approve_and_promote_accepted_block
test_review_limit_and_replay_are_fail_closed
```

The Phase-6 smoke suite additionally proves:

```text
approve without --decision-pr rejects
old --why is not accepted as approval authority
controlled pre-approval path stops at REVIEW_REQUIRED
unrelated dirty state blocks candidate import
```

These are useful and several are strong direct regressions.

They are not the complete frozen matrix.

### 5.2 Concrete frozen cases without deterministic implementation evidence

Examples required by PR #155 but not represented by an executable deterministic test on this exact candidate include:

#### Original X1B matrix

```text
X1B-A2  Continue treated as Human decision -> DENY
X1B-A3  silence / no Human review -> DENY
X1B-A6  parameter change after approval -> DENY
X1B-A7  scope expansion after approval -> DENY
X1B-A8  general Human direction attributed as exact Human-specific parameters -> DENY
X1B-A10 AI-filled value attributed as Human-chosen -> DENY
```

Some other A-cases have partial analogues in the present suite, but the brief froze the original matrix as an explicit retained matrix, not merely equivalent prose coverage.

#### F002 currentness / immutable-review semantics

Required named cases not deterministically exercised include, among others:

```text
X1B-CUR2  Link rel=next -> DENY
X1B-CUR3  duplicate review numeric ID -> DENY
X1B-CUR6  Human APPROVED H1 + proposer moves PR head H2 -> only H1 can admit
X1B-CUR7  H2 cannot inherit H1 approval
X1B-CUR8  later Human APPROVED H2 supersedes H1
X1B-CUR9  immutable H request.json missing/mutated/digest mismatch -> DENY
X1B-CUR10 immutable H accepted-scene mismatch -> DENY
X1B-CUR12 network failure after review selection before immutable file completion -> DENY / no effect
```

The live F005 proof establishes one positive real path. It does not replace these deterministic negative/currentness regressions.

#### F003 concurrency / prospective-effect / failure semantics

Required named cases without dedicated deterministic evidence include, among others:

```text
X1B-CAS1 second concurrent X1B invocation cannot acquire common-dir lock
X1B-CAS3 prospective C parent != B0 -> DENY before CAS
X1B-CAS4 prospective C has extra changed path -> DENY before CAS
X1B-CAS5 prospective scene/log bytes mismatch -> DENY before CAS
X1B-CAS7 failure before CAS leaves real index/worktree/ref unchanged
X1B-CAS8 failure after CAS before synchronization -> RECOVERY_REQUIRED / never HumanDecision TRUE
```

The stale-base test and the repaired symref tests do not establish all of those separate frozen failure classes.

#### F004 Git environment matrix

The present test injects only:

```text
GIT_DIR
GIT_WORK_TREE
GIT_INDEX_FILE
GIT_NAMESPACE
```

The brief explicitly requires individual/combined attacker-environment coverage including:

```text
GIT_COMMON_DIR
GIT_OBJECT_DIRECTORY
GIT_ALTERNATE_OBJECT_DIRECTORIES
GIT_CONFIG_COUNT / GIT_CONFIG_KEY_* / GIT_CONFIG_VALUE_*
GIT_CONFIG_GLOBAL
GIT_CONFIG_SYSTEM
GIT_NO_REPLACE_OBJECTS
```

and GIT1..GIT6 outcomes.

#### Other retained fail-closed evidence

Examples not given dedicated deterministic tests include:

```text
refs/replace present -> DENY
wrong resulting file modes -> DENY before CAS
machine commit metadata mismatch -> DENY before CAS
child result malformed/extra/missing/tampered -> parent DENY
```

PR #158 additionally freezes TLS1..TLS15. The supported-host proof satisfies the required live positive path, but the candidate deterministic suite does not implement all frozen negative child/TLS cases such as child request override attempts, malformed child output, authority-HTTP failure, and fresh-child/no-cache repetition as named executable regressions.

### 5.3 Repository verifier does not close the gap

`scripts/verify_repository.py` checks only a short marker subset, currently requiring names such as:

```text
test_wrong_login_same_name_does_not_override_numeric_id
test_nonhuman_reserved_marker_denied
test_network_child_env_is_fresh
test_anchored_git_ignores_attacker_git_environment
test_positive_two_path_cas_effect
test_stale_base_cannot_canonicalize
test_symbolic_main_substitution_is_rejected_before_effect
test_no_deref_cas_cannot_mutate_symref_target_if_race_follows_check
test_legacy_approve_and_promote_accepted_block
```

It does not verify that the full frozen A/CUR/CAS/GIT/TLS/fail-closed matrix exists.

Accordingly:

```text
GREEN REPOSITORY VERIFIER != FULL FROZEN TEST MATRIX
GREEN CI != EXECUTION OF TESTS THAT DO NOT EXIST
```

## 6. Why this blocks implementation-review PASS

The governing brief did not say only that the runtime mechanism should appear secure. It explicitly made executable negative/positive regression evidence part of the implementation contract and of AK-CANON PASS criterion 9.

An independent implementation review cannot infer execution evidence for omitted tests from:

```text
code inspection
one positive end-to-end test
one live TLS/GitHub positive proof
green CI whose suite omits the frozen cases
```

Therefore the exact candidate does not yet satisfy the accepted implementation contract even though no new runtime counterexample was established in R3 before STOP.

Disposition:

```text
X1B-V2-IMPL-R3-F001 = BLOCKER
IMPLEMENTATION REVIEW = NOT PASS
```

## 7. Scope-firewall check

This finding is inside the Human-accepted X1B scope because it concerns evidence explicitly frozen for:

```text
Human origin
current review semantics
request/content/scope/effect binding
replay
fail-closed behavior
Git no-substitution
CAS/failure truth
legacy bypass closure
positive/negative verification
```

It does not add or reopen:

```text
TPM / EK / AK
CRL
PMEM / NFIT
bare-metal locality
BMC/console origin
universal crash durability
malicious trusted Python/Git/kernel/filesystem
```

Convergence strategy remains valid.

## 8. Bounded repair recommendation — not authority

The narrow next repair should begin as **test/evidence completion only**.

Recommended initial repair surface:

```text
tests/test_x1b_human_decision.py
tests/test_phase6_scriptops_smoke.py
scripts/verify_repository.py
.github/workflows/x1b-human-decision.yml
```

The repair should:

1. map every frozen A1..A10, ID, CUR, CAS, GIT, retained fail-closed, PU and TLS deterministic case to an executable test ID/name;
2. make the verifier fail if any mandatory case disappears;
3. execute that matrix in CI on the exact candidate;
4. preserve the already-passing supported-host proof as separate live evidence rather than replacing deterministic tests with it.

Critically:

```text
TEST COMPLETION AUTHORITY != RUNTIME REPAIR AUTHORITY
```

If a newly added mandatory regression exposes an actual production-code defect, STOP and record that concrete defect. Do not silently modify runtime code under test-only repair authority.

This review itself authorizes no repair.

## 9. Explicit non-authority

This review does not authorize:

```text
modification of FJ899/scriptops PR #35
new tests or verifier changes
runtime repair
live executable decision-evidence PR
Human V2 screenplay approval
ScriptOps approve
prospective executable screenplay commit
refs/heads/main CAS
canonical screenplay effect
merge
X1B closure
V1
release / deployment / tag
```

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
GREEN CI != COMPLETE REQUIRED EVIDENCE
PROOF PASS != IMPLEMENTATION REVIEW PASS
AI PROPOSES != HUMAN DECIDES
```

## 10. Next legal stage

```text
STOP
NEXT LEGAL STAGE = SEPARATE HUMAN ACCEPTANCE OF R3-F001
                   + BOUNDED TEST-MATRIX COMPLETION AUTHORITY ONLY
```

If that Human authority is granted, add the missing frozen deterministic tests and verifier/CI enforcement only. If all mandatory tests pass without production-code changes, freeze the repaired candidate and perform a new independent implementation re-review. If any mandatory test exposes a runtime defect, stop at that new defect for separate Human repair authority.
