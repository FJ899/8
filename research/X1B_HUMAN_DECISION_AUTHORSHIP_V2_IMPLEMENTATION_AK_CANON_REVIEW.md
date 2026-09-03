# X1B Human Decision Authorship V2 — Independent AK-CANON Implementation Review

Status: `INDEPENDENT IMPLEMENTATION REVIEW / NOT REPAIR AUTHORITY`

Date: `2026-09-03`

## 1. Verdict

```text
AK-CANON X1B HUMAN DECISION AUTHORSHIP V2 IMPLEMENTATION REVIEW = NOT PASS
```

The Human-authorized implementation candidate materially implements the passed composite brief and finishes with all frozen CI suites green. The implementation stays within the exact 13-path implementation surface, preserves the Human/GitHub V2 authority boundary, closes the old `--why` and direct legacy acceptance paths, isolates the TLS reader, constructs a prospective two-path commit, and uses an old-value ref CAS.

However, independent review found one first credible counterexample inside the frozen F003/no-substitution threat model:

```text
X1B-V2-IMPL-F001 — MAIN-REF CAS DEREFERENCES A CONCURRENT SYMBOLIC refs/heads/main AND CAN MUTATE AN UNBOUND TARGET REF = BLOCKER
```

The implementation calls:

```text
git update-ref refs/heads/main C B0
```

without `--no-deref`, and its pre/post ref-value checks use `rev-parse`, which also observe the resolved object identity rather than the direct-vs-symbolic structure of `refs/heads/main`.

Git explicitly defines `update-ref` as possibly dereferencing symbolic refs; `--no-deref` is the option that writes the named ref itself instead of the ref reached through a symbolic pointer.

A non-X1B/external Git actor — exactly the class for which the brief says the X1B advisory lock is insufficient and the atomic CAS remains necessary — can therefore replace `refs/heads/main` with a symbolic ref to another branch that still resolves to `B0` after the initial local preflight and before the CAS.

The implementation then:

```text
rev-parse refs/heads/main -> B0        # passes
working tree/index clean               # can remain true
update-ref refs/heads/main C B0        # follows the symref and updates its target
rev-parse refs/heads/main -> C         # passes post-check
```

while the actual mutated direct ref is the attacker-selected symbolic target and `refs/heads/main` remains a symbolic ref.

This is a logical-effect/ref-target substitution, not a platform/hardware finding.

Per first-credible-counterexample discipline, review STOPped blocker discovery after F001 was established.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
GREEN CI != SECURITY-PROPERTY PROOF
FIRST CREDIBLE COUNTEREXAMPLE = STOP
NOT PASS != X1B DESIGN FAILURE
NOT PASS != PHYSICAL-PLATFORM REOPEN
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed implementation candidate

Repository:

```text
FJ899/scriptops
PR #35
TITLE = X1B: bounded Human decision authorship V2 implementation candidate
STATE = OPEN / DRAFT / UNMERGED
```

Frozen candidate:

```text
BASE HEAD = 2f22843ac570498b506101addeba5453ab777f08
BASE TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
HEAD = 4f6cb09f7d6b103afb06d511b261ac68fd9c4494
TREE = 02bffae1d24278590bbb8e82c4584d9ff5bb5906
COMMITS = 1
CHANGED FILES = 13
```

The implementation commit has exactly one parent:

```text
2f22843ac570498b506101addeba5453ab777f08
```

The exact changed-path set is:

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

This equals the frozen implementation surface in the composite brief. No CODEOWNERS/ruleset, TPM, PKI/CRL, PMEM/NFIT, BMC or other path was introduced.

Key final blobs inspected from candidate tree include:

```text
.github/workflows/x1b-human-decision.yml  a39321840f1c94a90776a9f149bcaddf44ac11f8
HANDOFF.md                                edeefc238c792e45a86d7336661757cf78011180
PROJECT_STATE.md                          1be376f538a06e841aa1dc6ac5085cad322f6d2d
README.md                                 c04a0cb5b98fcf50596177ef2cea83e7a1f8ccd8
SOURCE_MANIFEST.md                        c2e100f113e9ee803822b33fae24994e96bb0084
legacy/scriptops-v2-single.py             883669a4a141519483b56d9cde54897fb4c7b17c
phase6/scriptops-v2-hardening.py          9da50a3e33c982396049c7618f7154b360194350
phase6/x1b_human_decision.py              e78df1407e56fa4bf1726b0ffd84a2bc1cebf7c2
scripts/restore_v2.py                     20b0b506e537640d0859b687ba0d6ddc78e8ccd0
scripts/verify_repository.py              9b84646069b94359a3410691d8e39e2052b7f846
```

## 3. Governing implementation authority

The implementation was separately Human-authorized after the exact composite planning chain reached AK-CANON PASS:

```text
FJ899/8 PR #155 = final bounded V2 brief for F001-F004
FJ899/8 PR #156 = independent review; F001-F004 materially closed; F005 found
FJ899/8 PR #157 = Human acceptance of F005
FJ899/8 PR #158 = F005-only TLS trust repair brief
FJ899/8 PR #159 = independent AK-CANON PASS of F005 repair
Human response after PR #159 = accept
```

That Human `accept` authorized bounded implementation of the PR #155 + PR #158 composite only.

It did not authorize:

```text
live decision-evidence PR
trusted Human V2 approval
real corrective positive control
canonical screenplay effect
merge
X1B closure
Agency Kernel V1
release/deployment/tag
```

This independent implementation review is the next planned legal stage and does not add repair authority.

## 4. Scope firewall

Review blocks only for a counterexample to an actual X1B V2 claim under the selected threat model, including:

```text
trusted Human origin
exact request/content/scope/candidate/effect binding
Human-currentness/replay
fail-closed admission
legacy/current bypass closure
anchored intended Git repository/ref truth
prospective exact effect
atomic canonical main CAS
executor no-substitution
post-effect truth
```

Do not block merely for:

```text
TPM/EK/AK
CRLs
PMEM/NFIT
bare-metal locality
BMC console origin
hostile kernel/filesystem/Git binary
compromised Human GitHub account
universal power-loss durability
```

The finding below is directly in the selected `refs/heads/main` logical-effect/CAS boundary.

## 5. Final CI evidence

The exact frozen candidate HEAD `4f6cb09f7d6b103afb06d511b261ac68fd9c4494` completed all required final CI successfully.

### 5.1 X1B V2 workflow

```text
workflow = x1b-human-decision
run_id = 33794688053
event = pull_request
head_sha = 4f6cb09f7d6b103afb06d511b261ac68fd9c4494
conclusion = success
```

The workflow exercises:

```text
X1B deterministic authority/CAS tests
Phase-6 X1B smoke tests
repository self-verification
historical reconstruction integrity check
```

### 5.2 Existing full Phase-6 regression

```text
workflow = Phase 6 ScriptOps smoke
run_id = 33794688012
head_sha = 4f6cb09f7d6b103afb06d511b261ac68fd9c4494
conclusion = success
```

The full deterministic Phase-6 regression completed successfully, including bounded-proposal/P3 compatibility restored during the implementation loop.

### 5.3 Existing repository verifier

```text
workflow = Verify repository state
run_id = 33794688006
head_sha = 4f6cb09f7d6b103afb06d511b261ac68fd9c4494
conclusion = success
```

### 5.4 CI interpretation

The green suites are strong evidence for implemented nominal and frozen negative cases. They do not cover a concurrent structural ref substitution where the resolved object ID remains `B0`, which is why F001 is not contradicted by the green CI result.

## 6. Implementation properties materially present before STOP

No regression was found before the first blocker in the following implementation directions.

### 6.1 Durable Human identity

The implementation freezes:

```text
TRUSTED_HUMAN_GITHUB_USER_ID = 226907434
```

Review qualification uses numeric `user.id`; login is observed metadata. Tests cover wrong-user/same-login and changed-login/same-ID cases.

### 6.2 Human currentness and immutable reviewed content

The GitHub reader uses one bounded reviews response to choose current Human state and then binds exact request/accepted-scene bytes to immutable `review.commit_id`.

Reserved-marker ambiguity, review-cap, CHANGES_REQUESTED/DISMISSED, request/effect drift and replay cases are fail closed in the deterministic test surface.

### 6.3 F005 TLS isolation

Authority network operations run in a fresh child environment with fixed direct `api.github.com:443`, verified stdlib TLS, no caller-selected URL/proxy/token/CA inputs, and parent-side evidence revalidation.

### 6.4 Git environment anchoring

Authority-critical Git subprocesses construct a clean environment and use frozen `git_dir`/`work_tree`. Attacker `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE` and namespace-style inherited environment values are not used.

### 6.5 Legacy bypass closure

The active legacy compatibility shim rejects:

```text
direct cmd_approve
scene-promote --to accepted
```

before accepted-state mutation. The active Phase-6 CLI requires:

```text
approve --scene <SCN-ID> --decision-pr <PR-NUMBER>
```

and does not accept `--why` as authority.

Historical prototype transport remains reconstructable but restore tooling refuses to overwrite the active legacy shim with unsafe historical bytes.

### 6.6 Prospective effect construction

The implementation constructs scene/log blobs, a private-index tree and a single-parent prospective commit before moving main. It verifies exact two-path diff, modes, scene/log bytes and machine Git identity before CAS.

These directions remain useful; F001 is a narrow structural-ref defect in the canonicalization step.

# FIRST CREDIBLE BLOCKER

## 7. X1B-V2-IMPL-F001 — main-ref CAS dereferences a concurrent symbolic `refs/heads/main`

Severity:

```text
BLOCKER
```

Classification:

```text
CORE X1B / F003 / EXECUTOR NO-SUBSTITUTION / CANONICAL REF CAS
```

### 7.1 Frozen claim

The Human-bound material effect names:

```text
canonical_ref = refs/heads/main
old_ref = B0
canonicalization = git-update-ref-compare-and-swap
```

The brief's F003 repair requires that an external/non-X1B Git change not cause a stale or substituted effect to become canonical.

The implementation likewise claims the canonical linearization point is an atomic old-value CAS on exact `refs/heads/main`.

### 7.2 Relevant implementation behavior

The final implementation uses an object-value read equivalent to:

```text
git rev-parse refs/heads/main
```

and canonicalizes with:

```text
git update-ref refs/heads/main C B0
```

without `--no-deref`.

The initial local preflight does verify that symbolic `HEAD` resolves to the main branch. But after the potentially slow Human-authority network read, later base checks verify only the resolved main object ID and cleanliness. They do not reassert that `refs/heads/main` itself remains a direct ref before the CAS.

### 7.3 Git semantics

Git's `update-ref` documentation states that the three-argument form stores the new value after checking the expected old value while **possibly dereferencing symbolic refs**.

Git separately specifies:

```text
--no-deref
```

to overwrite the named ref itself instead of following a symbolic pointer.

`git symbolic-ref` permits creation/update of symbolic refs whose target is another `refs/...` name.

Therefore object-ID CAS alone does not prove ref-identity CAS when the named ref's structural type can change concurrently.

### 7.4 Concrete counterexample

Let the accepted request bind:

```text
B0 = exact ScriptOps main base
C  = exact verified prospective Human-bound commit
```

Preflight begins in the ordinary state:

```text
HEAD -> refs/heads/main
refs/heads/main = B0
```

and passes.

During the later Human-authority read, an external/non-X1B Git actor creates:

```text
refs/heads/shadow = B0
refs/heads/main -> refs/heads/shadow     # symbolic ref
```

No tracked worktree/index change is required.

The implementation's later resolved-value check obtains:

```text
rev-parse refs/heads/main = B0
```

so the base test still passes.

Then:

```text
git update-ref refs/heads/main C B0
```

follows the symbolic pointer and updates:

```text
refs/heads/shadow: B0 -> C
```

while leaving:

```text
refs/heads/main -> refs/heads/shadow
```

The post-check again observes:

```text
rev-parse refs/heads/main = C
```

and can proceed to exact tree/worktree verification and report `HumanDecision=TRUE`.

Yet the direct ref actually mutated by the canonicalization command was an unbound attacker-selected ref, and the Human-bound canonical ref was not a direct B0->C ref update.

### 7.5 Independent minimal probe

A minimal local Git probe reproduced the relevant Git behavior:

```text
sym=refs/heads/other
resolved=<B0>

update-ref refs/heads/main <C> <B0>

after_main_sym=refs/heads/other
main=<C>
other=<C>
```

That is: the three-argument CAS succeeded because the symbolic ref resolved to the expected old object; Git updated the symbolic target.

This uses normal documented Git behavior, not a malicious Git binary or filesystem.

### 7.6 Why the X1B lock does not remove the counterexample

The common-dir `flock` serializes cooperating X1B invocations.

The accepted F003 mechanism explicitly retains CAS because:

```text
non-X1B/external Git activity need not honor the X1B lock
```

The symbolic-ref substitution is exactly such external Git activity. Therefore treating the lock as excluding the race would contradict the frozen F003 threat rationale.

### 7.7 Why this is in scope

F001 can alter:

```text
which direct Git ref receives the canonical CAS
whether the Human-bound canonical ref retains the expected structural identity
whether an undeclared ref is mutated
whether postverify proves the same ref effect that the Human approved
```

This is executor/ref no-substitution, not a hardware or durability theorem.

### 7.8 Required disposition

```text
X1B-V2-IMPL-F001 = BLOCKER
```

A repair can remain narrow at the existing Git-ref boundary. For example, a successor may make the CAS operate on the named ref without symbolic dereference and/or require direct-ref structure at the authority-critical checks. This review does not choose or authorize the repair.

## 8. Tests missing the blocker

The current stale-base test changes the resolved main object from `B0` to another commit. It correctly proves that an OID-changing race fails closed.

It does not exercise:

```text
same resolved OID B0
+
structural refs/heads/main direct-ref -> symbolic-ref substitution
```

A future repair should add a deterministic regression that changes `refs/heads/main` to a symbolic ref targeting another ref at `B0` after initial preflight and proves that:

```text
no unbound target ref is mutated
no false HumanDecision=TRUE occurs
```

Exact repair/test details require separate repair authority.

## 9. Candidate freeze provenance

Implementation work initially used multiple working commits while compatibility and CI were exercised. Three accidental temporary-file add/delete operations occurred on working/helper branches during connector use; none touched `main` and none survives in the final candidate tree or final candidate ancestry.

Before final review the branch was deliberately rebuilt as one commit whose parent is exact baseline `2f22843...` and whose tree contains only the 13 allowed implementation paths.

A first clean one-commit freeze exposed a nondeterministic `TemporaryDirectory.cleanup()` `ENOTEMPTY` teardown race after all semantic tests had passed. The test harness was hardened with a narrow retry for that cleanup race, and the candidate was rebuilt again as the exact final one-commit HEAD reviewed here.

Final candidate identity is only:

```text
HEAD = 4f6cb09f7d6b103afb06d511b261ac68fd9c4494
TREE = 02bffae1d24278590bbb8e82c4584d9ff5bb5906
PARENT = 2f22843ac570498b506101addeba5453ab777f08
```

Earlier working commits are not review authority.

## 10. Convergence assessment

The correct disposition is:

```text
COMPOSITE IMPLEMENTATION BRIEF DIRECTION = STILL VALID
IMPLEMENTATION CANDIDATE = NOT PASS DUE ONE NARROW F003 REF-IDENTITY DEFECT
F001/F002/F004/F005 DIRECTIONS = NO REGRESSION FOUND BEFORE STOP
HARDWARE/PHYSICAL PLATFORM LINEAGE = NOT REOPENED
```

This does not justify returning to TPM, PMEM, BMC or other R4 scope. The problem is one missing structural constraint on the already-selected Git CAS primitive.

## 11. Explicit non-authority / STOP

This implementation review authorizes no:

```text
ScriptOps repair
candidate mutation
successor implementation commit
live X1B decision-evidence PR
Human V2 approval
real positive control
canonical screenplay effect
merge
X1B closure
Agency Kernel V1
release
deployment
tag
```

After durable freeze of this review:

```text
STOP
NEXT LEGAL STAGE = HUMAN DISPOSITION ON X1B-V2-IMPL-F001
```

Preserve:

```text
GREEN CI != SECURITY PROOF
REVIEW FINDING != REPAIR AUTHORITY
ONE CORE BLOCKER != SCOPE FAILURE
AI PROPOSES != HUMAN DECIDES
```
