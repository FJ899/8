# X1B Human Decision Authorship — Independent AK-CANON R4R2 Implementation-Brief Review

Status: `INDEPENDENT REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: `2026-09-01`

## 1. Verdict

`AK-CANON X1B R4R2 IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

R4R2 materially improves R4R1 and directly addresses both findings frozen in PR #117:

1. the request/effect identity no longer requires a fixed point through its own `decision_request_id`;
2. the known legacy `scene-promote --to accepted` canonical-acceptance path is now explicitly required to fail closed at both CLI and internal-command layers.

However, independent adversarial review found new material effect-binding and implementation-contract blockers. Any one of the first three findings independently prevents implementation authority. The fourth finding is an additional unresolved normative design obligation.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R2 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R2 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#118`

```text
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
BASE TREE = df807db7003dfd201e9be4d5927472e515a2e737
HEAD = b2c5de19ef678b18899751915060df5397edeb1b
TREE = 90848115ac15d0611e87f9bcb6bb9b16f69c6d5a
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R2.md
BLOB = 80a2b6326d0d021a7b7a2ebf9306f7e1853c2fcb
```

Immediately before review write, PR #118 remained:

```text
state = OPEN
merged = false
draft = true
commits = 1
changed_files = 1
```

The reviewed file BLOB was freshly re-read at the exact HEAD and remained `80a2b6326d0d021a7b7a2ebf9306f7e1853c2fcb`.

## 3. Normative lineage

### 3.1 Accepted corrective design

```text
FJ899/scriptops PR #34
HEAD = d7a5065c87e9a4b49fb608235c908bceac42b4b1
TREE = 3140d0ac95c120a7b1532942bae2e0dad38b4839
PATH = governance/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_CANDIDATE.md
BLOB = dac16f109d1414a2208c2ed9a166ae9e9a329216
```

The design requires, among other things:

```text
exact content/scope/candidate/effect binding
current active Human decision evidence
explicit freshness/activity/supersession/conflict/replay semantics
executor no-substitution
fail closed on ambiguity
```

### 3.2 Independent design review

```text
FJ899/8 PR #109
HEAD = 132d65be48331a822039262b707c47a81d02a64d
TREE = a8bdc363d293beb7b15ae8b787cc3ebdd694fd99
BLOB = 439109e104244552a5ac1f3f08988dba283733d0
VERDICT = AK-CANON X1B CORRECTIVE DESIGN REVIEW R2 = PASS
```

### 3.3 R4R1 and its binding review

```text
FJ899/8 PR #116
HEAD = 0319b13cbe85675db0b40d36f5940cbfba36c130
TREE = 55dc82a52117d7234915a0b84193a4b2a26c226a
BLOB = 0fc30617ae7c378bdd90e7f9c5e1ab37a59661a4
```

```text
FJ899/8 PR #117
HEAD = a40187f1fd05193ad562551b3e332af574725e32
TREE = 799ad0f23c6b45cf985d35d0062ec0d916a32e09
BLOB = ceafb1b8a01d5044ed5e1e0feea5d62cfe6ac7e0
VERDICT = AK-CANON X1B R4R1 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #117 froze exactly two R4R1 blockers: request-ID circularity and the un-dispositioned legacy `scene-promote --to accepted` path.

## 4. Frozen ScriptOps baseline rechecked

```text
FJ899/scriptops main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Relevant current BLOBs remain:

```text
phase6/scriptops-v2-hardening.py
4f379960ed5677634dd234af6aa39626782b6133

legacy/scriptops-v2-single.py
9baa7b3a1eb746e34b79207a382eea1f5dd4ec55

phase6/bounded-proposal-view.py
27f50f0df85fe6b66cfd3c33be00c6d975762b45

scripts/restore_v2.py
fa2099d7d4530bce2256051690935625dab0e927

scripts/verify_repository.py
a61278086b92824d7e442b390c951e918c88517b
```

Current executable inspection confirmed:

- current Phase-6 hardening has the defect-era `approve --scene ... --why ...` effect path;
- current legacy has direct `approve --scene`;
- current legacy has direct `scene-promote --to accepted`, which can write the canonical scene and commit;
- current bounded-proposal-view explicitly operates on task-local proposal context and does not itself create canonical acceptance.

No third concrete accepted-state command was established by this review from the bounded executable surfaces inspected. This does not waive the later mandatory complete candidate-tree effect-entry inventory.

## 5. Review method

The review did not infer PASS from R4R2 being self-contained or from predecessor findings being fixed.

The adversarial questions included:

```text
Can the exact Human-bound effect land on a different local Git ref?
Can ambient local Git configuration execute or transform extra effects?
Can filesystem aliasing make two named paths mutate more than two objects?
Is Human evidence freshness/supersession fully defined rather than inferred?
Can request identity be reconstructed without self-reference?
Can any known current accepted-state command bypass the decision-PR path?
Can complete review evidence be reconstructed from the real GitHub API shape?
Can FinalEffectGateV2 actually prevent substitution through the first mutation?
```

The review also read a real public GitHub review record from the completed X1D-A5 control. The observed `submitted_at` value was `2026-09-01T05:14:04Z`, which is compatible with R4R2's exact second-resolution UTC `Z` timestamp profile.

## 6. R4R1 finding F001 — R4R2 disposition

`ADDRESSED AT BRIEF LEVEL`.

R4R2 now defines:

```text
PresentedMaterialEffectV2.local_git_effect.commit_message
=
"scriptops x1b: accept <exact scene_id>"
```

The concrete scene ID exists before request hashing.

R4R2 explicitly prohibits request-digest inputs from containing the later-derived request digest/ID, PR number/head, review identity, admission identity, final-gate digest, or future effect commit SHA.

The construction order is now acyclic:

```text
pre-state
-> accepted preview
-> PresentedMaterialEffectV2
-> HumanDecisionRequestBindingV2
-> request_digest
-> decision_request_id
-> committed HumanDecisionRequestV2
```

No fixed-point search or placeholder authority rule is required.

## 7. R4R1 finding F002 — R4R2 disposition

`ADDRESSED AT BRIEF LEVEL`.

R4R2 explicitly requires:

```text
legacy approve --scene
=> DENY / no effect
```

and:

```text
legacy scene-promote --to accepted
=> DENY / no effect
```

For `scene-promote`, R4R2 requires both:

1. removal of `accepted` from the direct CLI choices;
2. an independent `cmd_scene_promote` guard against `target_status == "accepted"` even if called programmatically or parser checks are bypassed.

The current legacy code confirms this is a real required correction: its state machine permits `candidate -> accepted`, and `cmd_scene_promote` selects `scenes/<scene_id>.fountain` when the target status is `accepted`.

## 8. Finding X1B-R4R2-IBR-F001 — local effect Git ref is not Human-bound or admission-bound

Severity: `BLOCKER`.

R4R2 binds:

```text
repository = FJ899/scriptops
repository_head_at_request = <exact SHA>
local HEAD = request.repository_head_at_request
```

and its material effect binds one local Git commit with exact message and exact two changed paths.

However, R4R2 does not bind the local Git ref on which that effect commit must land.

There is no requirement equivalent to:

```text
current local ref = refs/heads/main
```

nor a deliberate alternative such as a specifically named disposable effect ref.

Therefore these pre-states are indistinguishable under the literal R4R2 checks when they point at the same exact HEAD:

```text
refs/heads/main -> H
refs/heads/shadow -> H
DETACHED HEAD at H
```

Concrete counterexample:

```text
local main points to exact request base H
create/switch to branch shadow at exact H
run approve --decision-pr <N>
all SHA/content/review/final-gate checks pass
local effect commit advances shadow, not main
main remains at H
```

The Human-bound material-effect object says a local Git effect commit will occur, but it does not identify which ref is the target of that commit.

In a Git source-of-truth system, advancing `main`, advancing an arbitrary side branch, and creating a detached commit are materially different durable effects.

A future implementer would have to choose whether to:

```text
require local refs/heads/main
allow any branch at the exact SHA
allow detached HEAD
introduce a separately named canonical execution ref
```

That is a core effect/scope decision, not a mechanical implementation detail.

This violates:

```text
HUMAN-BOUND EFFECT = OPERATIVE EFFECT
NO CORE AUTHORITY / SECURITY SEMANTIC CHOICE LEFT TO IMPLEMENTER
```

Disposition: `NOT PASS`.

## 9. Finding X1B-R4R2-IBR-F002 — ambient Git hooks/filters/signing configuration can expand or transform the effect after FinalEffectGateV2

Severity: `BLOCKER`.

R4R2 makes an important credential improvement: local Git subprocesses must use a sanitized environment, disable interactive credential acquisition, and use an empty credential helper. It also forbids explicit network Git commands.

But the exact local effect still uses ordinary Git staging/commit behavior after FinalEffectGateV2:

```text
stage exactly two paths
commit exactly once
```

R4R2 does not freeze or neutralize ambient Git execution configuration such as:

```text
core.hooksPath
.git/hooks/*
pre-commit
prepare-commit-msg
commit-msg
post-commit
filter.<name>.clean
filter.<name>.process
core.attributesFile / local info attributes
commit.gpgSign / signing helper execution
```

A Git hook is not a `git fetch/pull/push` command. It can nevertheless execute arbitrary local commands, perform network I/O, mutate files, stage additional paths, or create external effects while `git commit` is running.

A clean tracked worktree before FinalEffectGateV2 does not prove that `.git/hooks`, local Git config, global Git config, or external filter/signing programs are inert.

Concrete counterexample:

```text
exact request/review/admission/final gate pass
pre-commit hook exists outside tracked repository content
hook stages a third path or performs an external side effect
git commit executes hook after the Human-currentness commitment point
```

If a third path reaches the commit, R4R2's post-effect changed-set check can detect the mismatch only after an unauthorized commit has already been created. R4R2 explicitly preserves such a failed post-commit artifact for forensic recovery rather than silently rewriting history.

A `post-commit` hook can perform an external side effect even when the resulting Git commit itself has the expected two-path tree.

Likewise a configured clean/process filter can transform bytes during `git add`, so the committed blob can differ from the Human-bound working-tree bytes unless the implementation either prevents such transformation or independently verifies the committed tree/blob identities.

The implementer therefore must invent the local Git isolation policy, for example whether/how to disable hooks, filters, attributes and signing helpers and whether to verify exact committed blobs. R4R2 does not make that authority/security choice.

Disposition: `NOT PASS`.

## 10. Finding X1B-R4R2-IBR-F003 — write-target hardlink aliasing is not excluded from the exact two-path effect

Severity: `BLOCKER`.

R4R2 explicitly treats symlink/nonregular ambiguity as fail-closed in several places. Candidate and impact inputs are required to be regular non-symlink files, and canonical pre-state rejects symlink/nonregular ambiguity.

However, R4R2 does not require single-link identity (`st_nlink == 1`) for authority-critical write targets such as:

```text
scenes/<scene_id>.fountain
.scriptops/decision-log.ndjson
```

A hardlink is a regular non-symlink file and therefore is not excluded by the stated checks.

Concrete counterexample:

```text
an external file and scenes/<scene_id>.fountain are hardlinks to the same inode
content equals the expected bound pre-state
Git tracked content can still appear unchanged before invocation
R4R2 pre-state/hash checks pass
executor writes accepted bytes to scenes/<scene_id>.fountain
external hardlink target changes simultaneously
```

The same aliasing class applies to a pre-existing decision-log file.

The Human-bound `PresentedMaterialEffectV2` says the operative effect changes exactly:

```text
scenes/<scene_id>.fountain
.scriptops/decision-log.ndjson
```

but hardlink aliasing permits additional filesystem objects outside that named scope to change without appearing as extra Git paths.

This is an exact-effect/scope mismatch and is not repaired by a later Git changed-path check.

The brief must freeze whether hardlink aliasing is forbidden and what fail-closed file-identity/open-time checks establish that fact; leaving it to implementation is security relevant.

Disposition: `NOT PASS`.

## 11. Finding X1B-R4R2-IBR-F004 — stale/supersession policy is not explicitly frozen

Severity: `VALIDATION-CONTRACT BLOCKER`.

The accepted corrective design explicitly requires the implementation contract to define:

```text
when a Human event becomes active
when it ceases to be active
what constitutes stale evidence
how supersession is represented
how multiple active events are evaluated
how conflicting active events are detected
what complete event set is considered
```

R4R2 defines substantial currentness semantics inside one selected decision PR:

```text
PR open / unmerged
exact base and head
exact current-head review
APPROVED active
CHANGES_REQUESTED conflicting
COMMENTED nondecision
DISMISSED inactive
second same-head approval ambiguous
old-commit approval historical
final fresh reread before mutation
```

It also records exact request and Human-review timestamps.

But it does not state an exact stale-age rule or explicitly state that there is deliberately no age-based expiry while the other currentness predicates remain true.

It also does not define whether a later separately approved decision PR for the same scene/base/canonical target supersedes, conflicts with, or coexists with an earlier still-open approved decision PR. The bounded read set enumerates reviews for the selected PR, not other decision PRs.

This review does not assert that R4R2 must choose time expiry or global PR enumeration. It asserts that the normative choice must be explicit because the accepted design requires a defined freshness/supersession policy.

Examples of materially different policies the implementer must not choose silently include:

```text
approval remains active indefinitely while exact PR/head/state remain current
approval expires after a fixed interval
new approved request for the same target supersedes old request
multiple exact approvals coexist until one effect changes the repository HEAD
explicit Human dismissal/PR closure is the only supersession mechanism
```

R4R2 currently leaves this policy partly inferential rather than frozen.

Disposition: `NOT PASS`.

## 12. Mandatory adversarial question matrix

### Q1 — R4R1 request-ID self-reference

`PASS AT BRIEF LEVEL`.

R4R2's request digest preimage contains no later request identity.

### Q2 — Material-effect commit message

`PASS AS TO REQUEST CIRCULARITY`.

The message binds the exact scene ID and no self-derived request identity. F001 of this review concerns the unbound local Git ref, not the message string.

### Q3 — V2 schema consistency

`PASS AT BRIEF LEVEL` with one editorial typo noted below.

R4R2 consistently uses V2 for the material effect, request, Human review marker, CompleteReviewSet, admission, final gate and decision record. `CanonicalPreStateV1` and `LOCAL_WORKTREE_DECISION_LOG_V1` are explicitly retained named subcontracts rather than accidental inheritance.

Section 16 refers once to `FinalEffectGateV1.observed_at` while the actual gate is `FinalEffectGateV2`. The timestamp format itself is otherwise unambiguous. This typo is not an independent blocker because the closed V2 gate field is explicit, but it should be corrected in any successor.

### Q4 — Real GitHub timestamp/body compatibility

`PASS AT BRIEF LEVEL`.

A real prior public Human review from `litrgratis-pixel` was read through GitHub and returned:

```text
submitted_at = 2026-09-01T05:14:04Z
state = APPROVED
commit_id = 2f2dc1aaa9a775f37e778e8a735cf8ef5b8a9660
```

This is compatible with the strict R4R2 timestamp form.

### Q5 — Direct legacy scene-promote accepted

`PASS AT BRIEF LEVEL`.

The exact known route is now required to be denied at both parser and command implementation layers with a real staged-candidate regression.

### Q6 — Other current accepted-state routes

`NO THIRD ROUTE ESTABLISHED BY THIS REVIEW`.

Current Phase-6 hardening, current legacy, and bounded proposal view were inspected. The known effect routes are the defect-era Phase-6 approve, legacy approve, and legacy scene-promote accepted. Bounded proposal view is explicitly noncanonical.

Later implementation review must still inspect the complete candidate tree; this review does not convert a bounded current-tree inspection into a global impossibility claim.

### Q7 — Implementation surface completeness

`ADEQUATE FOR THE KNOWN APPLICATION-LEVEL FILES, SUBJECT TO F001–F003`.

F001–F003 concern execution/environment contracts, not necessarily additional tracked source paths. Their exact correction must be frozen before implementation authority.

### Q8 — Decision PR / transport / pagination / conflict handling

`ADEQUATELY SPECIFIED AT BRIEF LEVEL, SUBJECT TO F004`.

One-file request PR shape, exact base/head/ref binding, public exact-origin transport, credential denial, no redirects/auth fallback, complete page collection and selected-PR review-state conflict semantics are substantially frozen.

### Q9 — FinalEffectGateV2 substitution window

`NOT PASS DUE TO F001–F003`.

Remote/currentness substitution is well constrained, but local ref identity, ambient Git execution behavior and hardlink aliasing remain capable of changing the material effect after the evidence/admission checks.

### Q10 — Durable decision record / exact two-path effect

`NOT PASS DUE TO F001–F003`.

The record itself avoids effect-commit self-hash circularity, but exact two-path durable effect is not yet guaranteed by the local Git/filesystem boundary.

### Q11 — Original X1B attacks and real regressions

`SUBSTANTIALLY TESTABLE, BUT INCOMPLETE UNTIL FINDINGS ARE FROZEN`.

R4R2 retains all ten preregistered attacks and direct real-boundary regressions. Successor brief/tests must add negative controls corresponding to any accepted correction of F001–F004.

### Q12 — Core security/authority choice left to implementer

`FAIL`.

At minimum:

```text
local effect ref policy
ambient Git execution/config isolation policy
hardlink/write-target alias policy
freshness/supersession policy
```

remain insufficiently frozen.

## 13. What R4R2 successfully preserves

This NOT PASS does not erase the substantial progress already made.

At brief level R4R2 preserves or improves:

```text
separate trusted Human event
exact request/content/candidate/effect hashes
non-circular request identity
exact one-file decision PR
exact Human actor + strict review body
credential-free public GitHub read boundary
no redirect/authenticated fallback
complete selected-PR review reconstruction
bounded replay claim
same-worktree X1B invocation lock
fresh FinalEffectGateV2
real .scriptops/decision-log.ndjson target
exact two named Git paths
no effect-commit self-hash in the decision record
legacy approve denial
legacy scene-promote accepted denial
historical prototype vs active-runtime split
restore/verifier source-of-truth correction
current README/PROJECT_STATE/HANDOFF correction
real separately authorized Human positive control requirement
closure/V1 separation
```

These are not reopened merely because new findings were discovered.

## 14. Required successor-brief acceptance obligations

This review does not authorize a repair. A separately Human-authorized successor brief would need to resolve, without weakening existing R4R2 properties:

```text
F001 exact local effect ref identity and ref-drift checks
F002 deterministic fail-closed local Git execution environment
     including hooks/filter/attributes/signing behavior and committed-blob truth
F003 single-object/non-aliased write-target identity for exact effect scope
F004 explicit freshness/activity/supersession/multiple-decision policy
```

The exact mechanism is a future Human-authorized brief decision, not this review's authority.

## 15. Final disposition

```text
R4R1 F001 REQUEST CIRCULARITY = ADDRESSED IN R4R2
R4R1 F002 LEGACY SCENE-PROMOTE BYPASS = ADDRESSED IN R4R2

R4R2 IBR F001 LOCAL EFFECT REF = BLOCKER
R4R2 IBR F002 AMBIENT GIT EXECUTION CONFIG = BLOCKER
R4R2 IBR F003 HARDLINK / WRITE-TARGET ALIAS = BLOCKER
R4R2 IBR F004 FRESHNESS / SUPERSESSION = BLOCKER

AK-CANON X1B R4R2 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
IMPLEMENTATION AUTHORITY = NOT ESTABLISHED
X1B = OPEN
V1 AUTHORITY = NOT ESTABLISHED
```

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R2 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R2 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 16. STOP

No ScriptOps implementation, repair, Human decision PR/review, live positive control, canonical effect, merge, closure, V1, release, deployment or tag is authorized by this review artifact.

`STOP`
