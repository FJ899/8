# X1B HUMAN DECISION AUTHORSHIP — CLEAN IMPLEMENTATION BRIEF R4R7

Status: `CLEAN R4R7 CORRECTIVE BRIEF / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-01`

## 1. Authority, purpose, and STOP boundary

This document is the self-contained successor to R4R6 after independent AK-CANON review PR #127 returned `NOT PASS`.

It preserves the accepted X1B corrective design and every R4R6 property not rejected by PR #127, while correcting exactly the two blockers frozen by that review:

1. logical `refs/heads/main` identity is insufficient when the `files` reference backend can resolve through real ref symlinks or filesystem aliases;
2. `git update-ref` can create or append a durable reflog whose identity/time/content were not included in the Human-presented effect.

R4R7 therefore replaces `git update-ref` as the commitment primitive with a closed physical loose-ref profile and an alias-safe fd-relative lockfile CAS. It also makes the main-branch reflog an explicit deterministic post-CAS projection bound into the Human-presented material effect.

New exact profiles:

```text
SINGLE_WORKTREE_REAL_GITDIR_V1
PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1
ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V1
DETERMINISTIC_MAIN_REFLOG_PROJECTION_V1
CRASH_DURABLE_OBJECT_AND_ALIAS_SAFE_REF_V2
ALIAS_SAFE_MAIN_REF_COMMITMENT_V3
REF_CAS_FIRST_ALIAS_SAFE_GIT_PLUMBING_V5
```

The material effect changes again. All authority-critical schemas, review markers, admission identities, final-gate identities and records are therefore V7.

This document is an implementation brief only. It authorizes no ScriptOps source mutation, no Human decision PR/review, no live positive control, no canonical screenplay effect, no recovery, no merge, no X1B closure, no Agency Kernel v1, no release, deployment, or tag.

```text
R4R7 BRIEF != IMPLEMENTATION AUTHORITY
R4R7 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R7 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

After durable freeze of this brief, STOP. The next stage is a separately Human-authorized independent AK-CANON R4R7 implementation-brief review.

## 2. Exact governance lineage

### 2.1 Accepted corrective design

```text
FJ899/scriptops PR #34
HEAD = d7a5065c87e9a4b49fb608235c908bceac42b4b1
TREE = 3140d0ac95c120a7b1532942bae2e0dad38b4839
PATH = governance/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_CANDIDATE.md
BLOB = dac16f109d1414a2208c2ed9a166ae9e9a329216
```

Higher-level normative properties remain:

```text
separate trusted Human decision act
exact content/scope/candidate/effect binding
explicit freshness/activity/supersession/conflict/replay semantics
executor no-substitution
fail closed on ambiguity
real-boundary negative regressions
real separately authorized positive Human control
post-effect truth matching the Human-bound effect
no failed operation durably misreported as successful Human-attributed effect
no core authority/security choice left implicit
```

### 2.2 Independent corrective-design review

```text
FJ899/8 PR #109
HEAD = 132d65be48331a822039262b707c47a81d02a64d
TREE = a8bdc363d293beb7b15ae8b787cc3ebdd694fd99
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_DESIGN_AK_CANON_REVIEW_R2.md
BLOB = 439109e104244552a5ac1f3f08988dba283733d0
VERDICT = AK-CANON X1B CORRECTIVE DESIGN REVIEW R2 = PASS
```

### 2.3 R4R6 predecessor

```text
FJ899/8 PR #126
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 8cbe07b7e48379a49fdb6d154ffa56d489a45b5e
TREE = af54604cb1deb19e016a44e96efc5ee290be6d8e
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R6.md
BLOB = 8d9be9d8d2e481f990c90e63ed7de85320317cbb
```

### 2.4 Binding R4R6 NOT-PASS review

```text
FJ899/8 PR #127
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = d91ff8eb13fe3cf5eb4269320a014c730084aecd
TREE = 14ea92ce702dc0719f19d61355a753d387b06b7a
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R6_AK_CANON_REVIEW.md
BLOB = 2a096efe585c0f06fcc8da3bc7b049f357cf7240
VERDICT = AK-CANON X1B R4R6 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #127 froze:

```text
X1B-R4R6-IBR-F001 — physical files-ref topology is not bound
X1B-R4R6-IBR-F002 — update-ref reflog is an unbound durable effect
```

PR #127 also recorded that R4R6 addressed at brief level:

```text
X1B-R4R5-IBR-F001 configured Git hooks
X1B-R4R5-IBR-F002 unfrozen Git fsync / crash durability
```

and preserved prior lazy-fetch, replacement-ref, commit-encoding, local-ref, hardlink/write-target-alias and freshness/supersession corrections.

`REVIEW FINDING != REPAIR AUTHORITY`; R4R7 exists only under the fresh Human authorization for successor brief preparation.

## 3. Exact evidence-repository base

```text
FJ899/8 main
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

No history rewrite is part of R4R7.

## 4. Frozen ScriptOps baseline

```text
FJ899/scriptops main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Security-relevant baseline BLOBs remain:

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

sources/prototype/RESTORE.md
8a79aca4c93b23c4842792bea9ecaae146e1fc48

SOURCE_MANIFEST.md
2acf2ece298bfcf89254087c9e747fcb808ab241

README.md
c52f515dd3d736c749eca75cf319b514f8427c5a

PROJECT_STATE.md
dea1d11c847765026f8766fa70aa111c3f77c7bd

HANDOFF.md
2e0c3be2a9bdebfeac161773ca9631f8312f42f6

tests/test_phase6_scriptops_smoke.py
d6065047268cee5591883a3065ce49886ec85bcf

.github/workflows/phase6-scriptops-smoke.yml
a811dc75b4d3c7a1ebd8375c24fc71c74586ddf5

.github/workflows/verify-repository.yml
7d896d425012479c97bf1e6539f9a861a4a17aa5
```

Historical prototype reconstruction remains immutable evidence with SHA-256 `881dade6c6c506b9a9d41ebfbf68afb18b66db7583d35f746fb29ed7b36ac596`, size `51980` bytes.

## 5. Normative precedence and V7 migration

```text
R4R7 TEXT = CURRENT IMPLEMENTATION-BRIEF AUTHORITY
R4R6 / R4R5 / R4R4 / R4R3 / R4R2 / R4R1 / R4 / R3 / R2 / R1 = HISTORICAL INPUT ONLY
CORRECTIVE DESIGN PR #34 = HIGHER-LEVEL PROPERTY CONTRACT
```

R4R7 materially changes the local Git effect and commitment mechanism:

```text
Git update-ref is no longer the commitment primitive
physical loose-main-ref topology is Human-bound by profile
ref commitment is fd-relative no-follow lockfile CAS
main reflog is an explicit deterministic post-CAS projection
```

Therefore:

```text
V6 REQUEST/REVIEW/ADMISSION/GATE != R4R7 AUTHORITY
V6 HUMAN REVIEW MARKER != V7 HUMAN DECISION
V7 EFFECT PROFILE REQUIRES FRESH V7 HUMAN-BOUND REQUEST
```

No V6 or earlier Human evidence may authorize a V7 effect.

## 6. Future bounded implementation surface

Expected implementation surface remains:

```text
phase6/scriptops-v2-hardening.py
legacy/scriptops-v2-single.py
phase6/x1b_human_decision.py
scripts/restore_v2.py
scripts/verify_repository.py
sources/prototype/RESTORE.md
SOURCE_MANIFEST.md
README.md
PROJECT_STATE.md
HANDOFF.md
tests/test_phase6_scriptops_smoke.py
tests/test_x1b_human_decision.py
.github/workflows/x1b-human-decision.yml
```

Expected unchanged:

```text
phase6/bounded-proposal-view.py
.github/workflows/phase6-scriptops-smoke.yml
.github/workflows/verify-repository.yml
sources/prototype/scriptops-v2-single.py.part01..part07
```

Any additional tracked path requires STOP and fresh Human authorization before mutation.

## 7. Core Human-decision rule

```text
HumanDecision = TRUE
ONLY IF
separate trusted Human decision evidence
for exact current content + scope + candidate + material effect
is independently validated and admitted.
```

Never sufficient by itself:

```text
approval command possession
non-empty --why
caller rationale
continuation
silence
AI-created proposal/PR/comment/record
identity label
hard-coded approver="human"
CI success
green tests
mergeability
effect credential
```

Preserve:

```text
AI PROPOSED != HUMAN DECIDED
APPROVAL COMMAND POSSESSION != HUMAN DECISION AUTHORSHIP
NON-EMPTY WHY != HUMAN ACT
IDENTITY != CREDENTIAL != CHANNEL != CAPABILITY != AUTHORITY
HUMAN DECISION EVIDENCE != EXECUTION CREDENTIAL
EFFECT CAPABILITY != AUTHORITY TO CREATE HUMAN DECISION EVIDENCE
SHAPE MATCH != TRUSTED ORIGIN
```

## 8. Exactly one current acceptance interface

After implementation, the only current effect-capable Human-decision acceptance interface is:

```text
python phase6/scriptops-v2-hardening.py approve --decision-pr <positive-integer>
```

PR number is a locator only, never authority.

No caller-controlled field may supply Human actor/result/rationale, request path/digest, task/scene/candidate/impact identities, canonical target/ref, physical Git-dir/ref topology, reflog semantics, effect type, material effect, raw-object profile, hook profile, durability profile, commitment profile, or effect commit metadata.

Defect-era Phase-6 `approve --scene ... --why ...`, direct legacy `approve --scene ...`, and direct legacy `scene-promote --to accepted` remain disabled and non-effect-capable.

## 9. Historical restore/verifier/docs obligations

Historical prototype reconstruction remains evidence only. Active corrected runtime identity is distinct from historical prototype byte identity.

Authority documentation must state at minimum:

```text
current Human-decision route = approve --decision-pr <N> only
direct legacy approve = disabled
direct accepted promotion = disabled
canonical local effect ref = refs/heads/main only
Git ref-mutating commands = forbidden in V7 effect path
physical Git-dir profile = SINGLE_WORKTREE_REAL_GITDIR_V1
physical main-ref profile = PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1
main ref CAS profile = ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V1
main reflog projection = DETERMINISTIC_MAIN_REFLOG_PROJECTION_V1
raw object profile = NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2
object-store profile = COMPLETE_LOCAL_OBJECT_STORE_V1
hook profile = NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1
commit object profile = CLOSED_RAW_COMMIT_OBJECT_V1
combined durability profile = CRASH_DURABLE_OBJECT_AND_ALIAS_SAFE_REF_V2
success commitment profile = ALIAS_SAFE_MAIN_REF_COMMITMENT_V3
effect transport profile = REF_CAS_FIRST_ALIAS_SAFE_GIT_PLUMBING_V5
file identity profile = SINGLE_LINK_ALIAS_SAFE_REPOSITORY_TARGETS_V1
```

## 10. Canonical JSON, hashes and time

Authority-critical canonical JSON remains exact UTF-8 with:

```text
sort_keys=True
separators=(",", ":")
ensure_ascii=False
allow_nan=False
no trailing newline
closed-schema/type validation before serialization
```

```text
sha256_hex_bytes(B) = lowercase 64-hex SHA-256 of exact bytes
sha256_canonical(X) = sha256_hex_bytes(canonical_json_bytes(X))
```

Authority-critical UTC timestamps remain exactly:

```text
YYYY-MM-DDTHH:MM:SSZ
```

The deterministic Unix epoch used by the raw effect commit and by the V7 reflog entry is derived from exact `request_created_at` with offset `+0000`.

## 11. CanonicalPreStateV1 and MainReflogPreStateV1

Canonical scene prestate remains:

```text
CanonicalPreStateV1 = {
  "exists": <true|false>,
  "file_sha256": <64 lowercase hex or null>
}
```

R4R7 adds:

```text
MainReflogPreStateV1 = {
  "exists": <true|false>,
  "file_sha256": <64 lowercase hex or null>,
  "byte_length": <nonnegative integer>
}
```

If the reflog exists, the digest and length bind its exact bytes. No newline repair, canonicalization or truncation is permitted.

## 12. Git/runtime/OS platform profile V7

Git semantics remain bounded to:

```text
2.55.0 <= parsed Git version < 2.56.0
object format = sha1
ref storage format = files
```

R4R7 additionally requires a POSIX-style filesystem/runtime with working semantics for:

```text
dir_fd relative open
O_NOFOLLOW
O_DIRECTORY
O_EXCL
O_CLOEXEC
fstat/lstat
renameat or Python os.rename with src_dir_fd/dst_dir_fd
fsync regular file
fsync directory
atomic same-directory rename
```

A platform that cannot provide these primitives is `BLOCKED`.

Successful fsync is trusted only within the same bounded OS/filesystem contract used by R4R6: hardware/firmware/filesystems that falsely report durable completion are outside the claim.

Mount namespace or filesystem topology must remain stable during the final descriptor-relative commitment interval. A detected topology change produces an uncertainty/recovery class, never complete success.

## 13. R4R7 correction F001 — SINGLE_WORKTREE_REAL_GITDIR_V1

The effect is authorized only for a normal single-worktree repository layout.

Before request creation, admission, FinalEffectGateV7, pre-CAS and post-effect, prove:

```text
repository root = exact canonical physical directory R
R/.git exists as a real directory
R/.git is not a symlink, gitfile, reparse-style redirect or non-directory
absolute Git dir = R/.git
Git common dir = R/.git
Git worktree top level = R
repository is non-bare
.git/worktrees is absent
no linked-worktree layout
core.worktree is absent
extensions.worktreeConfig is absent or false
```

The process opens and retains a descriptor for R and then opens `.git` relative to that descriptor with no-follow directory semantics. Stable `st_dev/st_ino` identity is held through the commitment interval.

Any linked-worktree, gitfile, external common-dir or redirected Git-dir layout is `BLOCKED` for R4R7.

## 14. R4R7 correction F001 — PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1

The only authorized physical main-ref representation is a direct loose regular file.

Required topology under held `.git` descriptor:

```text
refs                 = real directory, no symlink
refs/heads           = real directory, no symlink
refs/heads/main      = regular file, no symlink, no symbolic-ref contents
HEAD                 = regular file, no symlink
```

Exact `HEAD` bytes:

```text
ref: refs/heads/main\n
```

Exact loose main bytes before effect:

```text
<40 lowercase request-base SHA>\n
```

Additional requirements:

```text
refs/heads/main st_nlink = 1
refs/heads/main owner = current execution user
refs/heads/main mode = frozen implementation-supported regular-ref mode
main.lock absent before lock acquisition
core.preferSymlinkRefs absent/false
```

`packed-refs`, if present, must be a regular non-symlink single-link file under `.git` and a strict direct parse must prove that it contains no `refs/heads/main` entry.

A real symlink ref such as:

```text
refs/heads/main -> refs/heads/other
```

is unconditionally `BLOCKED`.

A symlink or redirect in `.git`, `refs`, or `refs/heads` is unconditionally `BLOCKED`.

A packed copy of `refs/heads/main` is unconditionally `BLOCKED`.

## 15. Descriptor identity and race discipline

The process retains descriptors for:

```text
repository root
.git
.git/refs
.git/refs/heads
```

All physical main-ref lock/read/write/rename operations use the held `refs/heads` descriptor and leaf names only.

The hierarchy is re-opened from the retained repository-root descriptor and its `st_dev/st_ino` identities are compared at these checkpoints:

```text
request creation
admission
FinalEffectGateV7
immediately before main.lock acquisition
immediately after main.lock acquisition
immediately before final rename
immediately after rename/fsync
post-effect
```

A path-level symlink substitution after descriptor acquisition therefore cannot redirect the descriptor-relative CAS to another directory.

If the canonical root -> .git -> refs -> heads chain ceases to resolve to the held directory identities after ref replacement, the state is `REF_COMMITTED_TOPOLOGY_UNCERTAIN`; the process must not claim complete success and must not silently rewrite the ref.

## 16. PresentedMaterialEffectV7

Closed schema:

```text
PresentedMaterialEffectV7 = {
  "schema_version": "scriptops-x1b-presented-material-effect/v7",
  "repository": "FJ899/scriptops",
  "scene_id": <exact scene ID>,
  "candidate_path": <exact repo-relative candidate path>,
  "candidate_file_sha256": <64 lowercase hex>,
  "canonical_scene_effect": {
    "target_path": "scenes/<scene_id>.fountain",
    "before": <CanonicalPreStateV1>,
    "after_file_sha256": <accepted canonical SHA256>,
    "source_status": "candidate",
    "canonical_status_after": "accepted",
    "candidate_source_preserved": true,
    "git_mode_after": "100644"
  },
  "decision_log_effect": {
    "target_path": ".scriptops/decision-log.ndjson",
    "append_count": 1,
    "record_schema_version": "scriptops-x1b-decision-record/v7",
    "record_result": "REF_COMMITTED",
    "append_semantics": "EXACT_PRIOR_BYTES_PLUS_ONE_CANONICAL_RECORD_PLUS_LF",
    "git_mode_after": "100644"
  },
  "local_git_effect": {
    "target_ref": "refs/heads/main",
    "ref_before": <repository_head_at_request>,
    "commit_count": 1,
    "commit_message": "scriptops x1b: accept <exact scene_id>",
    "commit_author_name": "ScriptOps X1B",
    "commit_author_email": "scriptops-x1b@local.invalid",
    "commit_committer_name": "ScriptOps X1B",
    "commit_committer_email": "scriptops-x1b@local.invalid",
    "commit_time_source": "request_created_at",
    "git_semantics_profile": "GIT_2_55_X1B_V1",
    "ref_storage_format": "files",
    "gitdir_profile": "SINGLE_WORKTREE_REAL_GITDIR_V1",
    "physical_main_ref_profile": "PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1",
    "raw_object_profile": "NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2",
    "object_store_profile": "COMPLETE_LOCAL_OBJECT_STORE_V1",
    "hook_profile": "NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1",
    "commit_object_profile": "CLOSED_RAW_COMMIT_OBJECT_V1",
    "ref_cas_profile": "ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V1",
    "durability_profile": "CRASH_DURABLE_OBJECT_AND_ALIAS_SAFE_REF_V2",
    "success_commitment_profile": "ALIAS_SAFE_MAIN_REF_COMMITMENT_V3",
    "effect_transport_profile": "REF_CAS_FIRST_ALIAS_SAFE_GIT_PLUMBING_V5",
    "git_ref_mutating_command": "NONE",
    "reflog_effect": {
      "target_git_metadata_path": "logs/refs/heads/main",
      "before": <MainReflogPreStateV1>,
      "projection_profile": "DETERMINISTIC_MAIN_REFLOG_PROJECTION_V1",
      "entry_old_oid_source": "REQUEST_BASE_SHA",
      "entry_new_oid_source": "EXACT_DERIVED_EFFECT_COMMIT_SHA",
      "entry_committer": "ScriptOps X1B <scriptops-x1b@local.invalid>",
      "entry_time_source": "request_created_at",
      "entry_timezone": "+0000",
      "entry_message": "scriptops x1b: accept <exact scene_id>",
      "append_count": 1
    },
    "post_ref_projection": "REFLOG_THEN_WORKTREE_THEN_REAL_INDEX_FROM_DURABLY_COMMITTED_TREE",
    "exact_changed_paths": [
      "scenes/<scene_id>.fountain",
      ".scriptops/decision-log.ndjson"
    ]
  },
  "file_identity_profile": "SINGLE_LINK_ALIAS_SAFE_REPOSITORY_TARGETS_V1"
}
```

The future exact effect commit SHA is not a request-digest input because that would be circular: it depends on the decision record, which depends on admitted Human review metadata. The Human instead binds the closed deterministic commit-construction profile and the reflog rule that uses that exact derived SHA.

## 17. HumanDecisionRequestBindingV7

```text
HumanDecisionRequestBindingV7 = {
  "schema_version": "scriptops-x1b-human-decision-request/v7",
  "repository": "FJ899/scriptops",
  "repository_head_at_request": <40 lowercase hex>,
  "repository_ref_at_request": "refs/heads/main",
  "request_created_at": <exact timestamp>,
  "task_id": <exact task ID>,
  "scene_id": <exact scene ID>,
  "candidate_path": <exact path>,
  "candidate_file_sha256": <exact digest>,
  "impact_report_path": <exact path>,
  "impact_report_sha256": <exact digest>,
  "canonical_target": "scenes/<scene_id>.fountain",
  "canonical_ref": "refs/heads/main",
  "main_reflog_prestate": <MainReflogPreStateV1>,
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect": <PresentedMaterialEffectV7>
}
```

`request_digest = sha256_canonical(binding)` and `decision_request_id = "x1b:" + request_digest`.

## 18. Decision proposal PR and V7 Human review

Proposal construction remains one-file and acyclic:

```text
request_path = decisions/x1b/<request_digest>.json
request_branch = decision/x1b/<request_digest>
proposal parent = exact repository_head_at_request
changed set = exactly request_path added
```

Authoritative Human actor remains:

```text
litrgratis-pixel
```

Exact manual GitHub UI APPROVE body is four LF-separated lines with no trailing LF:

```text
X1B-HUMAN-DECISION-V7
decision_request_id=<exact x1b:<request_digest>>
decision_request_sha256=<exact request_digest>
why=<Human rationale>
```

V6 or earlier review markers are invalid for V7.

## 19. Trusted GitHub evidence and review semantics

Public GitHub evidence transport, exact-origin TLS, no proxy/redirect/auth fallback, complete pagination, current-head binding, duplicate ambiguity, active CHANGES_REQUESTED handling, no-latest-wins semantics and exact PR envelope remain frozen from R4R6 with V7 schema names.

A selected decision is active only while every exact PR/request/review/local-ref/raw-object/object-store/hook/Git-dir/physical-ref/reflog-prestate/applicability predicate remains true.

Age alone does not stale consent:

```text
NO WALL-CLOCK TTL
AGE ALONE != STALE
```

## 20. Hook closure preserved and tightened

R4R7 preserves:

```text
ambient effective hook.* census with includes/origin/scope
verified private empty traditional hook directory
-c hook.reference-transaction.enabled=false
-c hook.post-index-change.enabled=false
```

However, the V7 effect path performs no Git ref-mutating command at all.

Forbidden during effect:

```text
git update-ref
git symbolic-ref write
git branch mutation
git checkout/switch/reset ref mutation
git pack-refs
git refs migrate/write
any porcelain or plumbing command that mutates a ref
```

Thus no Git `reference-transaction` event or implicit Git reflog write is part of the commitment path.

Index-changing Git plumbing remains bounded and `post-index-change` remains disabled at command scope.

## 21. Sanitized Git subprocess profile V7

Every authority-critical Git subprocess retains:

```text
absolute resolved system Git
shell=false
explicit minimal environment
LC_ALL=C
TZ=UTC
GIT_NO_REPLACE_OBJECTS=1
GIT_NO_LAZY_FETCH=1
GIT_CONFIG_NOSYSTEM=1
GIT_CONFIG_SYSTEM=/dev/null
GIT_CONFIG_GLOBAL=/dev/null
GIT_TERMINAL_PROMPT=0
GCM_INTERACTIVE=never
GIT_PROTOCOL_FROM_USER=0
```

Caller `GIT_*`, loader, SSH, askpass, alternate-object and config-injection variables remain stripped as in R4R6.

Global Git options remain:

```text
--no-replace-objects
--no-lazy-fetch
```

Command-scope controls remain at minimum:

```text
-c core.hooksPath=<verified empty private hook directory>
-c hook.reference-transaction.enabled=false
-c hook.post-index-change.enabled=false
-c core.fsmonitor=false
-c commit.gpgSign=false
-c credential.helper=
-c core.fsync=all
-c core.fsyncMethod=fsync
```

Object/index writes retain Git fsync-all hardening. Ref/reflog writes are performed by the closed OS helpers below, not by Git.

## 22. COMPLETE_LOCAL_OBJECT_STORE_V1 preserved

Reject shallow/graft/partial/promisor/alternate object-store topology as in R4R6.

No lazy fetch or transport fallback is permitted.

## 23. NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2 preserved

Raw request-base authority remains exact local commit bytes, with replacement refs disabled and missing objects failing locally.

## 24. CLOSED_RAW_COMMIT_OBJECT_V1 preserved

The effect commit is constructed from exact raw bytes with only:

```text
tree
parent
author
committer
```

headers, exact deterministic author/committer and request-derived epoch, exact message:

```text
scriptops x1b: accept <scene_id>\n
```

No `commit-tree`, encoding, signature, mergetag, extra parent or unknown header.

Independent SHA-1 and Git `hash-object -w -t commit --stdin` must match exactly. Object writes remain under Git fsync-all hardening.

## 25. Private temporary index and new tree

Before ref commitment, the real index tree equals the raw parent tree.

Accepted scene and decision-log blobs, private temporary index, `read-tree`, `update-index --cacheinfo`, `write-tree`, raw commit construction and exact two-path tree verification remain as R4R6.

The new tree differs from the parent at exactly:

```text
scenes/<scene_id>.fountain
.scriptops/decision-log.ndjson
```

## 26. X1BDecisionRecordV7

```text
X1BDecisionRecordV7 = {
  "schema_version": "scriptops-x1b-decision-record/v7",
  "result": "REF_COMMITTED",
  "result_scope": "PHYSICAL_LOOSE_REFS_HEADS_MAIN_POINTS_TO_EXACT_EFFECT_COMMIT",
  "decision_type": "scene_acceptance_ref_committed",
  "decision_request_id": <exact ID>,
  "request_digest": <exact digest>,
  "decision_pr_number": <positive integer>,
  "decision_pr_head": <exact head>,
  "human_review_numeric_id": <canonical decimal string>,
  "human_review_node_id": <exact node ID>,
  "human_actor": "litrgratis-pixel",
  "human_review_commit": <exact PR head>,
  "human_review_body_sha256": <exact digest>,
  "human_review_submitted_at": <exact timestamp>,
  "human_rationale": <exact rationale>,
  "admission_id": <exact admission ID>,
  "final_effect_gate_digest": <exact digest>,
  "complete_review_set_digest": <exact digest>,
  "task_id": <exact task>,
  "scene_id": <exact scene>,
  "candidate_path": <exact path>,
  "candidate_file_sha256": <exact digest>,
  "impact_report_path": <exact path>,
  "impact_report_sha256": <exact digest>,
  "canonical_target": "scenes/<scene_id>.fountain",
  "canonical_ref": "refs/heads/main",
  "ref_before": <exact request base>,
  "main_reflog_prestate": <MainReflogPreStateV1>,
  "canonical_before": <CanonicalPreStateV1>,
  "canonical_after_file_sha256": <exact digest>,
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect_digest": <exact digest>,
  "gitdir_profile": "SINGLE_WORKTREE_REAL_GITDIR_V1",
  "physical_main_ref_profile": "PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1",
  "raw_object_profile": "NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2",
  "object_store_profile": "COMPLETE_LOCAL_OBJECT_STORE_V1",
  "hook_profile": "NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1",
  "commit_object_profile": "CLOSED_RAW_COMMIT_OBJECT_V1",
  "ref_cas_profile": "ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V1",
  "reflog_projection_profile": "DETERMINISTIC_MAIN_REFLOG_PROJECTION_V1",
  "durability_profile": "CRASH_DURABLE_OBJECT_AND_ALIAS_SAFE_REF_V2",
  "success_commitment_profile": "ALIAS_SAFE_MAIN_REF_COMMITMENT_V3",
  "canonical_instance_scope": "LOCAL_PHYSICAL_MAIN_REF_WORKTREE_DECISION_LOG_REFLOG_V7"
}
```

The record intentionally says `REF_COMMITTED`, not generic `SUCCESS` and not `COMPLETE`. Reflog/worktree/index completion is proved after the ref commitment.

## 27. R4R7 correction F001 — ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V1

The V7 commitment primitive is not a Git command.

With held `.git/refs/heads` directory descriptor:

### 27.1 Lock acquisition

Acquire exactly leaf `main.lock` using descriptor-relative create:

```text
O_WRONLY | O_CREAT | O_EXCL | O_NOFOLLOW | O_CLOEXEC
```

with a frozen supported regular-ref mode.

`main.lock` is the same conventional lock pathname used by the files backend, so cooperative Git writers cannot simultaneously acquire the main-ref lock.

If `main.lock` already exists, block before commitment.

### 27.2 Post-lock old-value proof

After acquiring the lock and before writing it, revalidate:

```text
held root/.git/refs/heads identities stable
HEAD bytes exact ref: refs/heads/main LF
main is exact regular single-link direct loose ref
main bytes = request base + LF
packed-refs still contains no main entry
raw object/gate/replay predicates still exact
```

### 27.3 Lockfile write and durability

Write exactly:

```text
<effect_commit_sha>\n
```

No other bytes.

Then:

```text
fsync(main.lock fd)
fstat exact regular-file properties
re-read written bytes from fd or no-follow reopen
```

### 27.4 Final pre-rename proof

Immediately before rename, re-read the existing `main` leaf through the held heads descriptor and require the request-base bytes still exact.

Revalidate held directory identities and packed-main absence.

If old-value proof fails, delete/rollback only the uncommitted lockfile and return `BLOCKED_PRE_COMMIT`.

### 27.5 Commitment rename

Perform one same-directory descriptor-relative atomic replacement:

```text
renameat(held_heads_fd, "main.lock", held_heads_fd, "main")
```

or exact Python `os.rename(..., src_dir_fd=held_heads_fd, dst_dir_fd=held_heads_fd)` equivalent.

Then:

```text
fsync(held_heads_fd)
```

Normal durable commitment requires both rename and directory fsync to succeed.

### 27.6 Immediate post-rename proof

Reopen `main` via held heads descriptor with `O_NOFOLLOW` and require:

```text
regular file
single link
exact effect SHA + LF
supported frozen mode
```

Re-open the root -> .git -> refs -> heads chain from the retained root descriptor and prove it resolves to the same held directory identities.

Logical Git no-replace/no-lazy read of `refs/heads/main` must equal the same effect SHA, but logical Git equality is corroboration, not physical authority.

## 28. CAS uncertainty semantics

A nonzero syscall result is not automatically `no effect`.

After any rename/fsync interruption or exception, inspect the physical main leaf through the retained descriptor and the canonical hierarchy when possible.

Classify:

```text
physical main = old SHA and canonical hierarchy stable:
  BLOCKED_PRE_COMMIT

physical main = effect SHA but ref-file or directory fsync completion not proven:
  REF_COMMITTED_DURABILITY_UNCERTAIN

held heads contains effect SHA but canonical hierarchy no longer resolves to held heads:
  REF_COMMITTED_TOPOLOGY_UNCERTAIN

state unreadable/ambiguous:
  COMMITMENT_STATE_UNKNOWN
```

Never silently restore/overwrite main after a visible or possible commitment.

## 29. R4R7 correction F002 — DETERMINISTIC_MAIN_REFLOG_PROJECTION_V1

R4R7 does not allow Git to create the reflog implicitly.

The reflog is instead an explicit Human-bound post-ref projection.

Required Git metadata topology under held `.git` descriptor:

```text
logs = real directory
logs/refs = real directory
logs/refs/heads = real directory
```

Each directory must be non-symlink and descriptor-stable. R4R7 does not create missing reflog parent directories; missing/aliased parents block before effect.

`logs/refs/heads/main` may be:

```text
absent
OR
regular non-symlink single-link file whose exact bytes match MainReflogPreStateV1
```

Any symlink/redirect/unsupported file is blocked.

## 30. Exact V7 reflog line

After exact effect commit SHA `C` is known and only after durable physical main-ref commitment, construct exactly one UTF-8/ASCII-compatible line:

```text
<request_base_sha> SP <C> SP ScriptOps X1B <scriptops-x1b@local.invalid> SP <request_epoch> SP +0000 TAB scriptops x1b: accept <scene_id> LF
```

No wall-clock-at-execution field is permitted.

No ambient `user.name`, `user.email`, `GIT_COMMITTER_*`, locale, timezone or `GIT_REFLOG_ACTION` may contribute.

The new reflog bytes are exactly:

```text
if prestate exists:
    exact prior bytes + exact V7 line
else:
    exact V7 line
```

Before projection, the reflog prestate is re-read and must still equal the Human-bound prestate. If it changed after ref commitment, return committed recovery state rather than overwriting unbound bytes.

## 31. Alias-safe reflog projection

Projection uses the same alias-safe target discipline as canonical scene/decision-log materialization:

```text
held/revalidated parent descriptor
fresh same-directory exclusive temporary regular file
O_NOFOLLOW
write exact complete after-bytes
fsync temp file
fstat/revalidate
atomic descriptor-relative rename onto main reflog leaf
fsync reflog parent directory
reopen no-follow and verify exact bytes/hash/link identity
```

No in-place append is used. This prevents a torn partial reflog line from becoming the normal successful state.

A reflog projection failure after durable ref commitment is:

```text
DURABLY_REF_COMMITTED_RECOVERY_REQUIRED
```

The ref is never silently rewritten to compensate.

## 32. Why the reflog projection is acyclic

The Human request binds:

```text
request-base old OID
reflog prestate
fixed committer identity
request-time source
fixed timezone
fixed message
new OID source = exact deterministic V7 effect commit
```

It does not place the future effect SHA inside the request digest.

The effect SHA is computed only after admission because the V7 decision record includes exact Human review metadata. Once computed, the reflog line is uniquely determined by already Human-bound inputs plus that uniquely derived effect SHA.

This is the same non-circular treatment already used for the future effect commit identity itself.

## 33. CRASH_DURABLE_OBJECT_AND_ALIAS_SAFE_REF_V2

Before ref commitment:

```text
all new Git objects are written under core.fsync=all + core.fsyncMethod=fsync
new_object_closure is locally exact and no-lazy/no-replace readable
```

Ref durability is then established independently by:

```text
fsync exact main.lock contents
atomic same-directory rename
fsync held refs/heads directory
exact physical reread
stable canonical hierarchy proof
```

Reflog/worktree/index are post-ref projections and are not prerequisites for truth of `REF_COMMITTED`; they are prerequisites for complete zero-exit success.

## 34. FinalEffectGateV7

Immediately before local effect-object preparation, while the existing same-worktree exclusive X1B lock is held, freshly validate:

```text
exact V7 PR/request/review envelope
Human currentness/conflicts
CompleteReviewSetV7 digest
raw main logical SHA = request base
SINGLE_WORKTREE_REAL_GITDIR_V1
PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1
MainReflogPreStateV1 exact
Git 2.55.x
files ref format
NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2
COMPLETE_LOCAL_OBJECT_STORE_V1
NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1
Git object/index fsync-all capability
zero refs/replace
raw parent commit/tree
candidate/impact/canonical pre-state
accepted preview
PresentedMaterialEffectV7
replay state
real index tree = raw parent tree
alias-safe worktree target preconditions
physical Git-dir/ref/reflog descriptor topology
verified empty hook directory
system Git/OS primitives
```

FinalEffectGateV7 is in-memory one-shot state, not a reusable credential.

After gate:

```text
no user interaction
no network
no sleep/wait
no unrelated blocking operation
no proposal/review mutation
no untrusted subprocess
no Git ref-mutating command
```

## 35. Exact local effect sequence V7

With lock held after FinalEffectGateV7:

```text
A. re-prove raw-object, complete-local-store, hook, Git-dir, physical-ref and reflog-prestate profiles

B. construct X1BDecisionRecordV7 bytes in memory

C. create accepted-scene and decision-log blobs under Git fsync-all profile

D. build exact new_tree in private temporary index
   prove exact two-path delta

E. construct/write/readback CLOSED_RAW_COMMIT_OBJECT_V1 under Git fsync-all
   independently compute exact effect SHA

F. enumerate and verify exact new_object_closure locally

G. final pre-ref checks:
   physical main exact old SHA
   packed main absent
   descriptor hierarchy exact
   reflog prestate exact
   hook census empty
   object closure exact/local
   real index still parent tree

H. acquire descriptor-relative main.lock O_EXCL/O_NOFOLLOW
   repeat old-value/topology proof

I. write exact effect SHA + LF to main.lock
   fsync lock file
   final old-main proof

J. descriptor-relative atomic rename main.lock -> main
   fsync held refs/heads directory
   classify physical ref result

K. only after normal durable ref commitment, construct and materialize exact deterministic main reflog after-bytes

L. materialize canonical scene bytes

M. materialize canonical decision-log bytes

N. update real index to exact committed new_tree under bounded hook-disabled Git plumbing

O. verify physical ref, logical ref, raw commit/tree/object closure, reflog, worktree/index and all profile identities exact

P. release X1B lock only after final outcome class is determined
```

No canonical worktree, canonical decision log, reflog or real-index mutation occurs before the physical main-ref commitment.

## 36. Outcome classes V7

Implementation must distinguish at least:

```text
DENIED
BLOCKED_PRE_COMMIT
REF_COMMITTED_DURABILITY_UNCERTAIN
REF_COMMITTED_TOPOLOGY_UNCERTAIN
COMMITMENT_STATE_UNKNOWN
DURABLY_REF_COMMITTED_RECOVERY_REQUIRED
DURABLY_REF_COMMITTED_COMPLETE
```

Semantics:

```text
DENIED / BLOCKED_PRE_COMMIT:
  physical canonical main remains old SHA
  no canonical worktree/index/reflog effect
  no V7 record reachable from canonical main

REF_COMMITTED_DURABILITY_UNCERTAIN:
  physical main visibly equals effect SHA
  file/directory durability completion not proven
  no claim of complete durable success
  no silent rollback

REF_COMMITTED_TOPOLOGY_UNCERTAIN:
  a descriptor-relative write may have committed in the held ref directory
  canonical hierarchy identity is no longer proven
  no success/no-effect claim
  preserve evidence

COMMITMENT_STATE_UNKNOWN:
  ref transaction outcome cannot be proven
  preserve evidence
  no rollback

DURABLY_REF_COMMITTED_RECOVERY_REQUIRED:
  physical canonical main durably equals effect SHA
  exact object truth is proven
  one or more reflog/worktree/index projections are incomplete/unproven
  no history rewrite

DURABLY_REF_COMMITTED_COMPLETE:
  durable physical main commitment
  exact deterministic reflog projection
  exact worktree scene + decision log
  exact real index
  complete post-effect verification
```

User-visible wording must never collapse uncertainty/recovery states into either `no effect` or `complete success`.

## 37. Zero-exit post-effect truth

Zero exit requires all:

```text
root/.git/refs/heads physical hierarchy identities exact
HEAD file exact ref: refs/heads/main LF
physical loose main regular single-link no-symlink
physical main bytes = expected effect SHA + LF
packed-refs has no main entry
logical no-replace/no-lazy HEAD/main = expected effect SHA
Git version/ref format exact
zero refs/replace
complete local object store
hook census empty/private hook dir exact
raw effect commit exact
one parent = request base
raw tree exact new_tree
raw changed set exactly two tracked paths
both tracked modes 100644
new object closure exact/local
main reflog bytes = exact Human-bound prestate + exact deterministic V7 line
canonical filesystem bytes exact
candidate source unchanged
exactly one V7 decision record line in committed tree/filesystem
record result = REF_COMMITTED
real index tree = raw HEAD tree
worktree clean relative to raw HEAD
lock held until verification complete
```

`GREEN COMMAND EXIT != POST-EFFECT TRUTH`.

## 38. Physical-ref alias regression suite

Mandatory tests include:

```text
refs/heads/main real symlink -> refs/heads/other
refs/heads/main symlink -> outside path
refs directory symlink
refs/heads directory symlink
.git symlink/gitfile/external common-dir
linked worktree
main symbolic-ref file contents
main regular hardlink with st_nlink > 1
packed-refs contains main
packed-refs symlink
main.lock preexists
core.preferSymlinkRefs=true
ref parent substituted before FinalEffectGateV7
ref parent substituted after gate before main.lock
ref parent substituted after main.lock before rename
ref parent substituted immediately after rename before post-check
```

Expected result:

```text
pre-commit alias/topology mismatch => DENY/BLOCKED
post-commit topology uncertainty => explicit uncertainty/recovery state
no logical-only PASS is permitted
```

A direct regression must reproduce the PR #127 counterexample and prove that the V7 physical profile rejects it before effect.

## 39. Reflog regression suite

Mandatory tests include:

```text
existing main reflog exact prestate
absent main reflog with real parent dirs
reflog symlink
reflog hardlink
reflog parent symlink
reflog bytes changed after request
reflog bytes changed after FinalEffectGateV7 before ref CAS
reflog bytes changed after ref CAS before projection
ambient user.name/user.email
ambient GIT_COMMITTER_NAME/EMAIL/DATE
ambient GIT_REFLOG_ACTION
core.logAllRefUpdates=true/false/always
existing Git reflog behavior that would normally append wall-clock identity
```

Because no Git ref-mutating command runs, none of those ambient Git reflog controls may create an entry during commitment.

The only permitted reflog change is the exact deterministic V7 projection.

Tests prove exact final bytes and no wall-clock execution-time dependence.

## 40. CAS/durability fault suite

Mandatory fault points include:

```text
object write/fsync failure
private-index/tree failure
main.lock acquisition failure
main.lock write failure
main.lock fsync failure
old main changed while lock held
rename failure before replacement
rename returns/raises ambiguously
refs/heads directory fsync failure
kill immediately before rename
kill immediately after rename before directory fsync
kill after directory fsync before reflog projection
reflog temp write/fsync/rename/dir-fsync failure
canonical scene projection failure
decision-log projection failure
real-index projection failure
```

No pre-commit failure may leave canonical worktree/index/reflog mutation.

Any visible/possible main-ref commitment is never silently rewritten.

## 41. Prior security regression suites remain mandatory

Preserve all earlier mandatory suites for:

```text
configured/traditional hooks
filters/helpers/config injection
lazy fetch / partial clones / promisor state
replacement refs / grafts / shallow state
commit encoding / extra headers
candidate/impact substitution
hardlink/symlink worktree targets
freshness/supersession/replay
Human-authorship attacks
legacy/defect acceptance routes
```

## 42. Trusted-origin claim

For this exact bounded profile only:

```text
manual Human APPROVE by litrgratis-pixel
+
exact public GitHub evidence
+
exact V7 request/PR/review/effect binding
+
independent admission
+
fresh FinalEffectGateV7
+
NO_REPLACE + NO_LAZY_FETCH raw SHA-1 semantics
+
COMPLETE_LOCAL_OBJECT_STORE_V1
+
NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1
+
SINGLE_WORKTREE_REAL_GITDIR_V1
+
PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1
+
CLOSED_RAW_COMMIT_OBJECT_V1
+
ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V1
+
DETERMINISTIC_MAIN_REFLOG_PROJECTION_V1
+
CRASH_DURABLE_OBJECT_AND_ALIAS_SAFE_REF_V2
+
post-ref alias-safe reflog/worktree/index projection
=
bounded trusted Human decision effect
```

No claim is made that GitHub metadata proves private Human mental state.

## 43. Implementation responsibility split

`phase6/scriptops-v2-hardening.py`:

```text
expose only approve --decision-pr
reject defect-era acceptance forms
obtain V7 admission
execute only final-gated V7 effect
never invent Human attribution
never invoke Git ref mutation
surface every uncertainty/recovery outcome distinctly
```

`legacy/scriptops-v2-single.py`:

```text
disable direct approve
disable direct accepted promotion
```

`phase6/x1b_human_decision.py`:

```text
V7 schemas/canonical JSON
pure accepted preview
trusted GitHub evidence transport
review pagination/currentness
admission/replay/lock
raw object/ref checks
FinalEffectGateV7
Git 2.55 profile
single-worktree real-gitdir verifier
physical loose-main-ref verifier
held descriptor identity helpers
packed-main absence parser
alias-safe main.lock CAS
CAS outcome classifier
reflog prestate binder
exact deterministic reflog-line constructor
alias-safe reflog projection
complete-local-object-store detector
no-replace/no-lazy helpers
closed raw commit writer/verifier
Git object/index fsync-all profile
alias-safe canonical worktree materialization
post-effect verifier
```

## 44. Independent implementation-review obligations

Later implementation review must prove, not infer:

```text
changed surface authorized
no third acceptance route
legacy/defect paths deny
V7 request identity acyclic
one-file decision PR exact
trusted transport exact
review currentness complete
main exact operative logical ref
single-worktree real .git enforced
common-dir cannot escape repository
refs and refs/heads physical identities enforced
main is direct regular single-link loose ref
packed main absent
real ref symlink counterexample rejected
parent-dir symlink counterexample rejected
all ref CAS syscalls descriptor-relative/no-follow where applicable
main.lock exact and old-value rechecked after acquisition
lockfile fsync + rename + directory fsync ordering exact
no Git ref-mutating command reachable
no implicit Git reflog write reachable
reflog prestate Human-bound
reflog new entry deterministic from bound inputs + exact derived effect SHA
reflog projection alias-safe and crash-aware
all Git object/index writes fsync-all
replacement/lazy/partial/promisor closure preserved
configured/traditional hook closure preserved
no canonical worktree/index/reflog mutation before ref commitment
post-ref failures never silently rewrite history
Human attribution only from validated review
no circular evidence
```

## 45. Separately authorized positive controls

A later live positive control requires fresh Human authorization and a disposable ScriptOps execution instance with inert/synthetic content.

Human must see exact V7 material effect including:

```text
canonical before/after hash
physical and logical refs/heads/main effect
single-worktree real-gitdir restriction
no Git update-ref
alias-safe loose-ref CAS
main reflog prestate and deterministic one-line projection rule
exact two-path one-parent commit
Git 2.55 semantics profile
no-replace/no-lazy profile
complete-local-object-store profile
hook profile
raw commit profile
combined durability profile
post-ref alias-safe worktree/index projection
```

A separately authorized fault-injection control must also exercise at least:

```text
post-rename pre-fsync interruption
post-ref reflog projection failure
post-ref worktree/index projection failure
```

and prove truthful uncertainty/recovery classifications.

## 46. Corrective closure composition

X1B cannot be closed by brief review, implementation, green CI or positive control alone.

Minimum later closure remains accepted design + independent design review + implementation authority + exact implementation + independent implementation review + fresh corrective verification + required negatives + separately authorized real Human positive control + exact post-effect truth + independent closure review + final Human closure acceptance + durable evidence freeze.

Preserve:

```text
GREEN TESTS != CORRECTIVE CLOSURE
IMPLEMENTATION REVIEW PASS != CORRECTIVE CLOSURE
LIVE POSITIVE CONTROL PASS != CORRECTIVE CLOSURE
TECHNICAL VERIFICATION PASS != HUMAN CLOSURE ACCEPTANCE
X1B CLOSED != V1 AUTHORITY
```

## 47. Successor-review adversarial checklist

Independent R4R7 brief review must explicitly attack at least:

```text
Can `.git` be a gitfile or external common-dir while checks pass?
Can a real symlink main ref evade the physical profile?
Can refs/heads parent redirection evade held descriptor checks?
Can packed main coexist and change authority?
Can core.preferSymlinkRefs alter behavior?
Can main.lock CAS overwrite a ref whose old value changed after lock acquisition?
Can a topology swap after descriptor acquisition redirect the fd-relative rename?
Can a topology swap after rename make canonical main differ while being reported complete?
Does lockfile fsync + same-directory rename + directory fsync establish the claimed bounded durability?
Can any Git command in V7 still mutate a ref or append a reflog?
Can an existing reflog or core.logAllRefUpdates cause an implicit change despite no Git ref mutation?
Is the deterministic reflog line fully specified and free of ambient wall-clock/user identity?
Can reflog projection introduce circular dependence on future effect SHA?
Can reflog prestate drift be overwritten after ref commitment?
Can V6 evidence authorize V7 semantics?
Can replacement refs, lazy fetch, partial clones or alternates reappear?
Can configured hooks or filesystem target aliases reappear?
Is any core authority/security choice still left to implementer?
```

Any credible counterexample freezes a finding and returns `NOT PASS`.

## 48. Explicit non-authority

This brief does not authorize:

```text
ScriptOps source mutation
Human decision PR creation
Human review creation
live positive control
canonical screenplay mutation
decision-log mutation
refs/heads/main effect
main reflog effect
recovery operation
merge
X1B closure
V1 entry
release
deployment
tag
```

R4R7 review PASS, if later obtained, establishes only that this brief is acceptable for a separately Human-authorized implementation stage.

## 49. STOP

Required next stage after durable R4R7 freeze:

```text
INDEPENDENT AK-CANON X1B R4R7 IMPLEMENTATION-BRIEF REVIEW
```

Only fresh separate Human authorization may create that review artifact.

```text
R4R7 BRIEF != IMPLEMENTATION AUTHORITY
R4R7 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R7 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
STOP
```
