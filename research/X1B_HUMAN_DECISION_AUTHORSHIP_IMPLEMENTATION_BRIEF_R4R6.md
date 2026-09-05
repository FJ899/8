# X1B HUMAN DECISION AUTHORSHIP — CLEAN IMPLEMENTATION BRIEF R4R6

Status: `CLEAN R4R6 CORRECTIVE BRIEF / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-01`

## 1. Authority, purpose, and STOP boundary

This document is the self-contained successor to R4R5 after independent AK-CANON review PR #125 returned `NOT PASS`.

It preserves the accepted X1B corrective design and every R4R5 property not rejected by PR #125, while correcting exactly the two blockers frozen by that review:

1. traditional hook-path isolation alone is insufficient on current Git because configured hooks may be defined by `hook.<friendly-name>.command` plus `hook.<friendly-name>.event` and may execute during `reference-transaction` or `post-index-change`;
2. process-level successful CAS is not by itself a crash-durable Human-effect commitment unless object and reference writes are hardened under an exact non-ambient fsync profile.

R4R6 introduces the following new exact profiles:

```text
NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1
CRASH_DURABLE_GIT_FSYNC_ALL_V1
CRASH_DURABLE_REFS_HEADS_MAIN_CAS_COMMITMENT_V2
```

The material effect profile therefore changes again and all authority-critical schemas/review markers are bumped to V6.

This document is an implementation brief only. It authorizes no ScriptOps implementation, no Human decision PR/review, no live positive control, no canonical screenplay effect, no recovery, no merge, no X1B closure, no Agency Kernel v1, no release, deployment, or tag.

```text
R4R6 BRIEF != IMPLEMENTATION AUTHORITY
R4R6 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R6 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

After durable freeze of this brief, STOP. The next stage is a separately Human-authorized independent AK-CANON R4R6 implementation-brief review.

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

### 2.3 R4R5 predecessor

```text
FJ899/8 PR #124
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 306bd9061a002f3615456dcb87c4cb9c7cd0d5b0
TREE = 42409e267506d97194abf0a9569d463285655e26
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R5.md
BLOB = ef67f2060cfe2593ef59a97ecab26aafcd46d4f8
```

### 2.4 Binding R4R5 NOT-PASS review

```text
FJ899/8 PR #125
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 4a39aa7bc02d53928bb0f2a7c69a107d3623a953
TREE = 67e2e048d00a8bec02aa31bdb3e45e95733e108f
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R5_AK_CANON_REVIEW.md
BLOB = d6e30fc22c204a1b7c18fb747878df265b501660
VERDICT = AK-CANON X1B R4R5 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #125 froze:

```text
X1B-R4R5-IBR-F001 — configuration-defined Git hooks bypass core.hooksPath=/dev/null
X1B-R4R5-IBR-F002 — unfrozen Git fsync / crash durability
```

PR #125 also recorded that R4R5 addressed at brief level:

```text
X1B-R4R4-IBR-F001 promisor lazy fetch
X1B-R4R4-IBR-F002 pre-CAS false-success canonical record
```

and preserved prior replacement-ref, commit-encoding, local-ref, hardlink/write-target-alias and freshness/supersession corrections.

`REVIEW FINDING != REPAIR AUTHORITY`; R4R6 exists only under the fresh Human authorization for successor brief preparation.

## 3. Exact evidence-repository base

```text
FJ899/8 main
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

No history rewrite is part of R4R6.

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

Historical prototype parts remain immutable and historical reconstruction remains SHA-256 `881dade6c6c506b9a9d41ebfbf68afb18b66db7583d35f746fb29ed7b36ac596`, size `51980` bytes.

## 5. Normative precedence and V6 migration

```text
R4R6 TEXT = CURRENT IMPLEMENTATION-BRIEF AUTHORITY
R4R5 / R4R4 / R4R3 / R4R2 / R4R1 / R4 / R3 / R2 / R1 = HISTORICAL INPUT ONLY
CORRECTIVE DESIGN PR #34 = HIGHER-LEVEL PROPERTY CONTRACT
```

No authority/security rule depends on implicit inheritance. R4R6 restates the current contract.

R4R6 materially changes the Human-presented local Git effect by adding:

```text
configured-hook execution closure
crash-durable Git object/reference hardening
V2 commitment semantics distinguishing process-visible ref state from durability-proven completion
```

Therefore all authority-critical request/evidence/admission/gate/record schemas are V6.

```text
V5 REQUEST/REVIEW/ADMISSION/GATE != R4R6 AUTHORITY
V5 HUMAN REVIEW MARKER != V6 HUMAN DECISION
V6 EFFECT PROFILE REQUIRES FRESH V6 HUMAN-BOUND REQUEST
```

No V5 or earlier Human evidence may authorize a V6 effect.

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

No caller-controlled field may supply Human actor/result/rationale, request path/digest, task/scene/candidate/impact identities, canonical target/ref, effect type, material effect, Git ref, raw-object profile, object-store profile, hook profile, commit-object profile, durability profile, commitment profile, or effect commit metadata.

Defect-era Phase-6 `approve --scene ... --why ...`, direct legacy `approve --scene ...`, and direct legacy `scene-promote --to accepted` remain disabled and non-effect-capable.

## 9. Historical transport, restore, verifier and docs

Historical prototype reconstruction remains evidence only. Active corrected runtime identity is distinct from historical prototype byte identity.

`scripts/restore_v2.py` may reconstruct historical bytes only outside the ScriptOps repository and may not restore an unsafe current approval path into the active repository.

Authority documentation must state at minimum:

```text
defect-era approve --why = historical provenance only
current Human-decision route = approve --decision-pr <N> only
direct legacy approve = disabled
direct legacy scene-promote --to accepted = disabled
canonical local effect ref = refs/heads/main only
raw Git object profile = NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2
object-store profile = COMPLETE_LOCAL_OBJECT_STORE_V1
hook profile = NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1
commit object profile = CLOSED_RAW_COMMIT_OBJECT_V1
durability profile = CRASH_DURABLE_GIT_FSYNC_ALL_V1
success commitment profile = CRASH_DURABLE_REFS_HEADS_MAIN_CAS_COMMITMENT_V2
effect transport profile = REF_CAS_FIRST_ALIAS_SAFE_GIT_PLUMBING_V4
file identity profile = SINGLE_LINK_ALIAS_SAFE_REPOSITORY_TARGETS_V1
```

## 10. Canonical JSON and hashes

All authority-critical canonical objects use exact UTF-8 JSON with:

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

File digests bind exact bytes. No Unicode or newline normalization is permitted where byte identity is specified.

## 11. Exact timestamps and raw Git time

Authority-critical local UTC timestamps use exactly:

```text
YYYY-MM-DDTHH:MM:SSZ
```

No fractional seconds, local timezone, offset form or fuzzy parser.

The raw effect commit author/committer timestamp remains deterministic Unix seconds derived from `request_created_at` plus exact offset `+0000`.

## 12. Deterministic accepted preview and CanonicalPreStateV1

```text
CanonicalPreStateV1 = {
  "exists": <true|false>,
  "file_sha256": <64 lowercase hex or null>
}
```

A pure production helper derives exact accepted canonical bytes from exact candidate bytes and is reused by request generation and execution. It has no write, Git, network, Human-evidence or time side effect.

## 13. R4R6 Git/runtime platform profile

The bounded production Git semantics profile is current Git 2.55.x.

```text
2.55.0 <= parsed Git version < 2.56.0
```

Any other Git series is `BLOCKED` pending fresh review of hook/event/fsync semantics.

The system Git executable must be resolved from the runtime system-default executable search domain, not caller PATH, must be an absolute regular executable outside the repository, and must retain stable stat identity through the effect.

Required Git capabilities include:

```text
--no-replace-objects
--no-lazy-fetch
git config --includes --show-origin --show-scope
hook.<event>.enabled command-scope override semantics
hash-object -w --stdin --no-filters
hash-object -w -t commit --stdin
cat-file
read-tree
update-index --cacheinfo
write-tree
ls-tree
rev-list or equivalent exact object-closure enumeration
update-ref with exact old value
rev-parse --show-ref-format
for-each-ref
```

Object format must be SHA-1.

Reference storage format must be exactly:

```text
files
```

`reftable` or unknown ref storage format is `BLOCKED` for this brief.

The OS/filesystem contract must provide successful `fsync`/equivalent semantics for regular repository files and reference updates as invoked by Git. R4R6 claims durability only within the platform contract where a successful fsync means the OS/filesystem has accepted responsibility for surviving an unclean system shutdown. Hardware/firmware/filesystem implementations that lie about successful fsync are outside this bounded claim.

## 14. PresentedMaterialEffectV6

Closed schema:

```text
PresentedMaterialEffectV6 = {
  "schema_version": "scriptops-x1b-presented-material-effect/v6",
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
    "record_schema_version": "scriptops-x1b-decision-record/v6",
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
    "raw_object_profile": "NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2",
    "object_store_profile": "COMPLETE_LOCAL_OBJECT_STORE_V1",
    "hook_profile": "NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1",
    "commit_object_profile": "CLOSED_RAW_COMMIT_OBJECT_V1",
    "durability_profile": "CRASH_DURABLE_GIT_FSYNC_ALL_V1",
    "success_commitment_profile": "CRASH_DURABLE_REFS_HEADS_MAIN_CAS_COMMITMENT_V2",
    "effect_transport_profile": "REF_CAS_FIRST_ALIAS_SAFE_GIT_PLUMBING_V4",
    "post_cas_materialization": "WORKTREE_AND_REAL_INDEX_FROM_DURABLY_COMMITTED_TREE",
    "exact_changed_paths": [
      "scenes/<scene_id>.fountain",
      ".scriptops/decision-log.ndjson"
    ]
  },
  "file_identity_profile": "SINGLE_LINK_ALIAS_SAFE_REPOSITORY_TARGETS_V1"
}
```

No request-digest input contains request digest/ID, PR number/head, review ID, admission ID, final gate digest or future effect commit SHA.

## 15. HumanDecisionRequestBindingV6

```text
HumanDecisionRequestBindingV6 = {
  "schema_version": "scriptops-x1b-human-decision-request/v6",
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
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect": <PresentedMaterialEffectV6>
}
```

Construction remains acyclic. `request_digest = sha256_canonical(binding)` and `decision_request_id = "x1b:" + request_digest`.

## 16. Deterministic decision request and one-file proposal PR

```text
request_path = decisions/x1b/<request_digest>.json
request_branch = decision/x1b/<request_digest>
decision_request_id = x1b:<request_digest>
```

Proposal commit parent equals exact `repository_head_at_request`; changed set is exactly one added request file. The effect invocation cannot create/edit proposal artifacts, PRs, comments, reviews or GitHub refs/settings.

## 17. Decision PR envelope

Valid decision PR requires exactly:

```text
repository = FJ899/scriptops
state = open
merged = false
base.ref = main
base.sha = request.repository_head_at_request
head.ref = decision/x1b/<request_digest>
head SHA = exact one-parent request commit
head repository = FJ899/scriptops
complete BASE->HEAD file set = exactly one added request_path
request bytes/schema/digest exact
```

Any ambiguity or extra path is DENY.

## 18. Human authority profile and V6 review body

Authoritative Human actor:

```text
litrgratis-pixel
```

Exact manual GitHub UI APPROVE body is four LF-separated lines with no trailing LF:

```text
X1B-HUMAN-DECISION-V6
decision_request_id=<exact x1b:<request_digest>>
decision_request_sha256=<exact request_digest>
why=<Human rationale>
```

Rationale is 1..2000 Unicode code points, strip-equal, with no C0/C1-style control characters specified by prior profile including CR/LF/TAB/NUL.

Human rationale and attribution derive only from this trusted review.

## 19. Trusted GitHub evidence transport

Production verifier uses unauthenticated public GitHub REST reads only from exactly `https://api.github.com` with explicit TLS default context, no proxy, no redirect, no Authorization header and no alternate origin.

Proxy/CA/GitHub credential overrides remain DENY before evidence acquisition.

## 20. CompleteReviewSetV6

All PR files/reviews are completely paginated. Review normalization, duplicate rejection, exact current-head review binding and no-latest-wins conflict semantics remain as R4R5 but schema names are V6.

For `litrgratis-pixel` on exact current PR HEAD there must be exactly one active syntactically and semantically valid V6 APPROVED and no active CHANGES_REQUESTED. Second current-head APPROVED is ambiguous DENY. Old-commit APPROVED is historical only.

## 21. Candidate, impact, raw tree and applicability

Before admission and again at FinalEffectGateV6:

```text
logical repository identity = FJ899/scriptops
HEAD symbolic ref = refs/heads/main
raw HEAD SHA = raw refs/heads/main SHA = request.repository_head_at_request
Git version = bounded 2.55.x profile
Git object format = sha1
Git ref storage format = files
NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2 satisfied
COMPLETE_LOCAL_OBJECT_STORE_V1 satisfied
NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1 satisfied
CRASH_DURABLE_GIT_FSYNC_ALL_V1 capability satisfied
no refs/replace/*
raw parent tree derived from raw request-base commit bytes
real index write-tree = raw parent tree
no tracked/index delta
candidate regular non-symlink exact path/hash/status
impact regular non-symlink exact path/hash/status REVIEW_REQUIRED
canonical pre-state exact in filesystem and raw tree
accepted preview exact
PresentedMaterialEffectV6 exact
request unconsumed
```

Candidate source is preserved.

## 22. Freshness, activation, supersession and replay

Age alone does not stale consent:

```text
NO WALL-CLOCK TTL
AGE ALONE != STALE
```

Selected decision is active only while every exact PR/request/review/local-ref/raw-object/object-store/hook/durability/applicability predicate remains true.

Another approved PR does not chronology-supersede the selected PR. The first successful same-base local main commitment invalidates other old-base requests by exact ref mismatch.

Replay claim remains bounded to one canonical local `refs/heads/main` worktree execution instance. Same-worktree exclusive lock is held from before admission through final post-commit status determination.

## 23. Exact local effect ref

Only:

```text
refs/heads/main
```

is operative.

Side branch, detached HEAD, unborn/ambiguous ref or raw ref drift is DENY.

Final ref mutation is exact old-value CAS only.

## 24. R4R6 correction F001 — NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1

Current Git 2.55 supports two hook sources:

```text
traditional hook path
configured hooks from hook.<friendly-name>.command + hook.<friendly-name>.event
```

R4R6 closes both sources independently.

### 24.1 Traditional hook closure

Before the effect begins, create one private empty hook directory outside the repository and outside any Git-controlled path.

Requirements:

```text
absolute path
owned by current process user
mode 0700 or platform equivalent
regular real directory
not symlink
empty
stable st_dev/st_ino through effect
not writable by group/other
```

Every authority-critical Git command receives command-scope:

```text
-c core.hooksPath=<exact verified empty private hook directory>
```

The directory is revalidated before FinalEffectGateV6, pre-CAS and post-effect. Mutation/substitution is DENY/BLOCKED before CAS or committed-recovery state after CAS.

### 24.2 Configured-hook census

At request creation, preliminary admission, FinalEffectGateV6, immediately before effect-object preparation, immediately before CAS and post-effect, perform an effective configured-hook census under the sanitized Git environment.

The census command explicitly enables config includes and inspects config origins/scopes equivalent to:

```text
git config --includes --show-origin --show-scope --null --get-regexp '^hook\.'
```

System/global config are already disabled by environment. Caller command config injection is removed. Therefore any effective `hook.*` key from local, worktree, included-local or other repository-effective scope is DENY/BLOCKED.

The census itself is a read-only config operation and is invoked without process-provided `hook.*` values so zero configured-hook output means exactly zero ambient configured-hook entries.

`extensions.worktreeConfig` does not bypass the census: worktree-scope `hook.*` is included and rejected.

An included file contributing `hook.*` is also rejected because includes are explicitly enabled.

### 24.3 Event-level command-scope hard disable

The exact R4R6 plumbing sequence can trigger only the hook events relevant to reference transactions and index writes:

```text
reference-transaction
post-index-change
```

Every authority-critical Git command, including private-index and real-index operations, receives both:

```text
-c hook.reference-transaction.enabled=false
-c hook.post-index-change.enabled=false
```

Current Git 2.55 defines event-level `hook.<event>.enabled=false` as disabling all hooks for that event regardless of per-hook enabled settings. This command-scope setting has higher precedence than repository-local/worktree configuration.

This closes the TOCTOU window where a `hook.*` entry is inserted after the last census but before `update-ref` or an index write: the configured command still cannot execute for either reachable event.

### 24.4 No other hook event authority

R4R6 is bounded to the exact Git 2.55.x command set listed in this brief. Any implementation use of a Git command capable of firing an additional hook event is out of authority and requires STOP unless the event is added to the closed command-scope disable set and independently reviewed.

No porcelain mutation command is permitted.

### 24.5 Required configured-hook regressions

Mandatory tests include:

```text
local hook.evil.command + hook.evil.event=reference-transaction
local hook.evil.command + hook.evil.event=post-index-change
worktree-scope configured hook
included-local configured hook
configured hook with shell one-liner
configured hook with network sentinel
configured hook with filesystem sentinel
local hook.reference-transaction.enabled=true
local hook.post-index-change.enabled=true
configured hook inserted after admission before FinalEffectGateV6
configured hook inserted after FinalEffectGateV6 before pre-CAS census
configured hook inserted after pre-CAS census immediately before update-ref
traditional reference-transaction hook in repository hookdir
traditional post-index-change hook in repository hookdir
caller custom core.hooksPath
```

Expected outcomes:

```text
ambient configured-hook state discovered at a frozen census => DENY/BLOCKED before CAS
race insertion after census => event-level hard disable prevents execution
traditional hookdir => private empty core.hooksPath prevents execution
sentinel never executes
no extra network/filesystem/ref side effect
```

## 25. Sanitized Git subprocess profile V6

Every authority-critical Git subprocess uses:

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

Remove caller values for all `GIT_CONFIG_*`, `GIT_DIR`, `GIT_WORK_TREE`, `GIT_COMMON_DIR`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_EXEC_PATH`, `GIT_EXTERNAL_DIFF`, `GIT_ASKPASS`, `SSH_ASKPASS`, `GIT_SSH`, `GIT_SSH_COMMAND`, `GIT_REPLACE_REF_BASE`, `GIT_NO_LAZY_FETCH`, loader-injection variables and unapproved caller `GIT_*` values.

Global options before subcommand:

```text
--no-replace-objects
--no-lazy-fetch
```

Command-scope security config on every authority-critical Git invocation:

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

No fallback command lacking any required control is permitted.

## 26. COMPLETE_LOCAL_OBJECT_STORE_V1 preserved

Reject shallow/graft/partial/promisor/alternate object-store topology exactly as R4R5.

Required markers remain absent:

```text
extensions.partialClone
remote.*.promisor
remote.*.partialclonefilter
*.promisor pack sidecar
objects/info/alternates
repository-configured alternate object store
caller GIT_OBJECT_DIRECTORY
caller GIT_ALTERNATE_OBJECT_DIRECTORIES
```

Missing object under no-lazy-fetch is BLOCKED and never fetched.

## 27. NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2 preserved

Every authority-critical commit/tree/diff/object read uses both replacement and lazy-fetch disabling controls.

Raw request-base authority remains exact local `cat-file commit` bytes and `raw_parent_tree` is parsed from that raw content.

Repository remains non-shallow, no graft source, zero refs/replace namespace.

## 28. CLOSED_RAW_COMMIT_OBJECT_V1 preserved

The operative effect commit is constructed from exact raw bytes, not `commit-tree`.

Exact headers remain:

```text
tree
parent
author
committer
```

in exact order, followed by blank line and exact one-line message plus final LF.

Forbidden headers include encoding, signatures, mergetag, extra parent and unknown/duplicate header.

Independent SHA-1 is computed over `commit <len>\0<raw-content>`, Git `hash-object -w -t commit --stdin` must return the same ID, and exact no-replace/no-lazy readback must be byte-identical.

All object-writing commands now additionally run under `CRASH_DURABLE_GIT_FSYNC_ALL_V1`.

## 29. Private temporary index and exact new tree

Before CAS, real index tree equals raw parent tree.

Exact accepted-scene and decision-log blobs are written with `hash-object -w --stdin --no-filters` under V6 Git controls.

Private index is created inside worktree-specific Git directory with exclusive mode 0600 and is used only through process-set `GIT_INDEX_FILE`.

`read-tree`, `update-index --cacheinfo`, and `write-tree` all run under:

```text
no-replace
no-lazy-fetch
configured-hook closure
core.fsync=all
core.fsyncMethod=fsync
```

`new_tree` must differ from raw parent tree at exactly two tracked paths:

```text
scenes/<scene_id>.fountain
.scriptops/decision-log.ndjson
```

No candidate/request/impact/third path changes.

## 30. X1BDecisionRecordV6

Before CAS construct exact record bytes only in memory/unreferenced object preparation.

```text
X1BDecisionRecordV6 = {
  "schema_version": "scriptops-x1b-decision-record/v6",
  "result": "REF_COMMITTED",
  "result_scope": "REFS_HEADS_MAIN_POINTS_TO_EXACT_EFFECT_COMMIT",
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
  "canonical_before": <CanonicalPreStateV1>,
  "canonical_after_file_sha256": <exact digest>,
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect_digest": <exact digest>,
  "raw_object_profile": "NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2",
  "object_store_profile": "COMPLETE_LOCAL_OBJECT_STORE_V1",
  "hook_profile": "NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1",
  "commit_object_profile": "CLOSED_RAW_COMMIT_OBJECT_V1",
  "durability_profile": "CRASH_DURABLE_GIT_FSYNC_ALL_V1",
  "success_commitment_profile": "CRASH_DURABLE_REFS_HEADS_MAIN_CAS_COMMITMENT_V2",
  "canonical_instance_scope": "LOCAL_REFS_HEADS_MAIN_WORKTREE_DECISION_LOG_V6"
}
```

The record intentionally says `REF_COMMITTED`, not generic `SUCCESS` and not `DURABLE_COMPLETE`. It becomes canonical only if main points to the exact prepared commit. Durability-complete status is an execution outcome proved outside the self-referential commit content.

## 31. R4R6 correction F002 — CRASH_DURABLE_GIT_FSYNC_ALL_V1

Git documents that `core.fsync` selects repository components to harden and that `core.fsyncMethod=fsync` uses fsync/platform equivalents. It also documents that the common default may leave recent loose objects vulnerable to unclean shutdown.

R4R6 does not accept ambient defaults.

Every Git command capable of creating/modifying repository object, index or reference data receives command-scope:

```text
-c core.fsync=all
-c core.fsyncMethod=fsync
```

This includes at minimum:

```text
hash-object -w
write-tree
private-index read-tree/update-index writes
real-index update writes
update-ref CAS
```

The process separately rejects effective repository/worktree durability keys at the same frozen checkpoints used for hook census:

```text
core.fsync
core.fsyncMethod
core.fsyncObjectFiles
```

Ambient values such as `core.fsync=none`, `core.fsyncMethod=writeout-only`, `core.fsyncMethod=batch`, deprecated `core.fsyncObjectFiles=false`, or include/worktree equivalents are DENY/BLOCKED rather than silently normalized.

The command-scope `all + fsync` remains present even after this rejection as defense in depth.

### 31.1 Required object durability ordering

Before any ref CAS, all objects reachable from the prepared effect commit but not required solely from the raw parent must have been created/read under the hardening profile.

Define:

```text
new_object_closure = exact local object IDs reachable from prepared effect commit
                     that are not reachable from raw request parent
```

The set includes at least the exact prepared effect commit, changed blobs, and every newly required tree object.

Before CAS:

```text
every object in new_object_closure is locally readable no-lazy/no-replace
every object type is expected
effect commit/tree/blob bytes and IDs are exact
all object-writing commands that introduced any member returned success under core.fsync=all + fsync
```

If this proof cannot be made, do not CAS.

### 31.2 Required reference durability ordering

The `refs/heads/main` CAS itself runs under the same `core.fsync=all + core.fsyncMethod=fsync` profile with ref storage format `files`.

Normal durability-proven commitment requires all:

```text
update-ref exact old-SHA CAS returns zero
immediate raw refs/heads/main reread equals exact effect commit
prepared effect commit and new_object_closure remain locally readable and exact
no hook executed
no replacement/lazy-fetch semantics
```

A zero return is accepted as the Git-level hardening completion only within the bounded platform fsync contract in section 13.

### 31.3 Nonzero/uncertain update-ref outcome

A failed or interrupted `update-ref` is not automatically classified as pre-commit.

Immediately inspect raw main under no-replace/no-lazy semantics when possible:

```text
if ref remains old request SHA:
    BLOCKED_PRE_COMMIT

if ref equals exact prepared effect commit but update-ref did not return success:
    REF_COMMITTED_DURABILITY_UNCERTAIN
    do not roll back silently
    do not claim DURABLY_COMMITTED_COMPLETE
    preserve ref/object truth for separately authorized recovery

if ref state is unreadable/ambiguous:
    COMMITMENT_STATE_UNKNOWN
    do not roll back silently
    preserve evidence and require recovery
```

This prevents a late fsync failure or process interruption from being falsely reported as `no effect`.

### 31.4 Crash-durability regression class

Mandatory tests include:

```text
repository core.fsync=none
repository core.fsyncMethod=writeout-only
repository core.fsyncMethod=batch
repository core.fsyncObjectFiles=false
worktree/include-sourced durability override
caller GIT_CONFIG_COUNT trying to set core.fsync=none
object-write fsync failure injection
write-tree fsync failure injection
reference fsync failure injection during update-ref
process kill before CAS
process kill during update-ref
process kill immediately after successful update-ref return
```

Expected proof:

```text
ambient durability override => DENY/BLOCKED before CAS
object hardening failure => no CAS
update-ref hardening failure with old ref => BLOCKED_PRE_COMMIT
update-ref nonzero/interrupted with new ref => REF_COMMITTED_DURABILITY_UNCERTAIN
normal zero-return CAS under fsync-all profile => durability-proven ref commitment
```

A test harness may instrument fsync only in disposable tests. Production loader injection remains prohibited.

## 32. FinalEffectGateV6

Immediately before local effect-object preparation, while lock is held, freshly reread trusted GitHub PR/review evidence and revalidate:

```text
exact PR/request/review envelope
Human currentness/conflicts
CompleteReviewSetV6 digest
raw main/ref identity
Git 2.55.x semantics profile
files ref format
NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2
COMPLETE_LOCAL_OBJECT_STORE_V1
NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1
CRASH_DURABLE_GIT_FSYNC_ALL_V1 capability
zero refs/replace
raw parent commit/tree
candidate/impact/canonical pre-state
accepted preview
PresentedMaterialEffectV6
replay state
real-index tree = raw parent tree
alias-safe target preconditions
verified empty private hook directory
system Git/platform preconditions
```

FinalEffectGateV6 is in-memory one-shot state, not a reusable credential.

After gate:

```text
no user interaction
no network
no sleep/wait
no unrelated blocking operation
no proposal/review mutation
no untrusted subprocess
```

Only bounded local effect preparation, configured-hook/durability census rechecks and exact pre-CAS checks may proceed.

## 33. Exact local effect sequence V6

With lock held after FinalEffectGateV6:

```text
A. re-prove raw-object, complete-local-store, hook and fsync profiles

B. construct X1BDecisionRecordV6 bytes in memory

C. create exact accepted-scene and decision-log blobs under fsync-all profile

D. build exact new_tree in private temporary index under fsync-all profile
   prove exact two-path delta

E. construct exact CLOSED_RAW_COMMIT_OBJECT_V1
   independently compute SHA-1
   write/readback under fsync-all profile

F. enumerate and verify exact new_object_closure locally

G. final local pre-CAS recheck:
   main/ref still old SHA
   configured-hook census empty
   hook dir exact/empty
   durability ambient-key census empty
   command event disables fixed
   object closure exact/local
   target identities exact
   real index still parent tree

H. execute exact old-value update-ref CAS under:
   no-replace
   no-lazy-fetch
   private hook dir
   reference-transaction disabled
   post-index-change disabled
   core.fsync=all
   core.fsyncMethod=fsync

I. classify CAS result using command status + raw ref state

J. only after a normal zero-return exact-ref commitment, materialize canonical scene

K. materialize canonical decision-log bytes

L. update real index to committed tree under hook-disabled fsync-all plumbing

M. verify raw ref/commit/tree/object closure/worktree/index exact

N. release lock only after durable outcome class is determined
```

No canonical filesystem or real-index mutation occurs before H.

## 34. Alias-safe post-CAS materialization

Existing and absent target protections from R4R5 remain.

Existing target must be regular, non-symlink, single link, exact prior bytes and exact stable inode identity before CAS.

After normal committed CAS, writes use fresh same-directory exclusive no-follow temporary inode, file fsync, identity revalidation, protected descriptor-relative atomic replace, directory fsync, reopen no-follow, exact hash/link verification.

Decision-log target uses equivalent semantics.

Any post-CAS alias/race/materialization failure is committed-recovery state; ref history is never silently rewritten.

## 35. Outcome classes V6

Implementation must distinguish at least:

```text
DENIED
BLOCKED_PRE_COMMIT
REF_COMMITTED_DURABILITY_UNCERTAIN
COMMITMENT_STATE_UNKNOWN
DURABLY_COMMITTED_RECOVERY_REQUIRED
DURABLY_COMMITTED_COMPLETE
```

Semantics:

```text
DENIED / BLOCKED_PRE_COMMIT:
  main remains old SHA
  no canonical worktree/index effect
  no canonical record reachable from main

REF_COMMITTED_DURABILITY_UNCERTAIN:
  main visibly equals exact effect SHA
  update-ref durable completion was not proven
  record REF_COMMITTED is truthful about visible ref state
  no claim of durability-complete success
  no silent ref rollback

COMMITMENT_STATE_UNKNOWN:
  effect transaction outcome cannot be proven
  no success/no-effect claim
  preserve evidence

DURABLY_COMMITTED_RECOVERY_REQUIRED:
  update-ref returned success under fsync-all profile
  exact ref/object truth is proven
  worktree/index completion not proven
  no silent history rewrite

DURABLY_COMMITTED_COMPLETE:
  durability-proven ref/object commitment plus exact worktree/index materialization verified
```

User-visible wording must not collapse uncertainty/recovery states into either `no effect` or `complete success`.

## 36. Post-effect truth for zero-exit completion

Zero exit requires:

```text
raw HEAD == raw refs/heads/main == exact expected effect commit
Git version still bounded profile
ref format = files
zero refs/replace
complete-local-object-store still true
configured-hook census empty
private hook dir exact/empty
no hook sentinel executed
no ambient durability override
raw effect commit exact
raw effect commit one parent = request base
raw effect tree exact new_tree
raw changed set exactly two paths
both modes 100644
all committed object IDs exact/local
canonical filesystem bytes exact
candidate source unchanged
exactly one V6 decision record line in tree/filesystem
record result = REF_COMMITTED
record request/review/admission/gate/profile identities exact
real index tree = resulting raw HEAD tree
worktree clean relative to raw HEAD
lock held until verification complete
```

`GREEN COMMAND EXIT != POST-EFFECT TRUTH`.

## 37. Hook/filter/config attack suite

Preserve prior hook/filter/config attacks and add current configured-hook attacks from section 24.

Mandatory sentinel proof must demonstrate that neither traditional nor configured `reference-transaction`/`post-index-change` commands execute during the exact production plumbing path.

Any executable helper or filter outside the frozen profile is a blocker.

## 38. Lazy-fetch / partial-clone suite

Preserve all R4R5 negatives:

```text
partial clone markers
promisor remote/filter
promisor pack sidecar
alternates
caller object-directory injection
caller GIT_NO_LAZY_FETCH=0
missing promised commit/tree/blob
marker insertion after admission/final gate
```

No fetch transport may execute.

## 39. Replacement-ref/raw-object suite

Preserve all prior replacement-ref and graft/shallow negatives.

Raw parent identity remains original raw object bytes regardless of installed replacement refs, while any nonempty replacement namespace causes effect denial.

## 40. CAS and durability fault suite

Mandatory sequence/fault tests include:

```text
main moved before CAS
CAS exact old-SHA mismatch
private-index failure
object-write failure
configured hook inserted before CAS
fsync durability override inserted before CAS
kill before CAS
update-ref forced nonzero before ref change
update-ref failure after visible ref change
kill during update-ref with old ref outcome
kill during update-ref with new ref outcome
kill immediately after successful zero-return CAS before worktree writes
post-CAS canonical scene materialization failure
post-CAS decision-log materialization failure
post-CAS real-index failure
```

No pre-CAS test may leave canonical worktree/index mutation.

Any visible ref commitment is never silently rewritten as rollback.

## 41. Freshness/supersession suite

Preserve:

```text
age alone + all currentness exact => applicable
PR closed/merged => DENY
approval dismissed => DENY
active CHANGES_REQUESTED => DENY
second current-head APPROVED => DENY ambiguous
old-commit APPROVED only => DENY
incomplete review pagination => DENY
another approved PR does not chronology-supersede selected PR
first same-base commitment invalidates second old-base request
changed candidate/effect/profile + old review => DENY
V5 or earlier review marker/request => DENY for V6 effect
```

## 42. Original X1B preregistered attacks remain mandatory

All original Human-authorship attacks remain mandatory, including AI self-acceptance, Continue-as-consent, silence-as-consent, stale Human consent reuse, A-to-A-prime substitution, parameter/scope changes, generic-direction over-attribution, AI-shaped Human artifact and AI-filled Human choice.

The real current Phase-6 defect-era path and both direct legacy paths remain real-boundary negatives.

## 43. Trusted-origin claim

For this exact bounded profile only:

```text
manual Human APPROVE by litrgratis-pixel
+
exact public GitHub review evidence
+
credential-free exact-origin acquisition
+
exact V6 request/PR/review/effect/ref binding
+
independent admission
+
fresh FinalEffectGateV6
+
NO_REPLACE + NO_LAZY_FETCH raw SHA-1 semantics
+
COMPLETE_LOCAL_OBJECT_STORE_V1
+
NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1
+
CLOSED_RAW_COMMIT_OBJECT_V1
+
CRASH_DURABLE_GIT_FSYNC_ALL_V1
+
CRASH_DURABLE_REFS_HEADS_MAIN_CAS_COMMITMENT_V2
+
post-CAS alias-safe worktree/index materialization
=
bounded trusted Human decision effect
```

No claim is made that GitHub metadata proves private Human mental state.

## 44. Implementation responsibility split

`phase6/scriptops-v2-hardening.py`:

```text
expose only approve --decision-pr
reject defect-era approve --scene/--why
obtain V6 admission
execute only final-gated V6 effect
never invent Human attribution
distinguish pre-commit, durability-uncertain, committed-recovery and complete states
```

`legacy/scriptops-v2-single.py`:

```text
disable direct approve
disable direct accepted promotion
```

`phase6/x1b_human_decision.py`:

```text
V6 schemas/canonical JSON
pure accepted preview
public GitHub evidence transport
review pagination/currentness
admission/replay/lock
raw ref/object checks
FinalEffectGateV6
system-Git 2.55 profile
configured-hook census
private hook-dir verifier
reference-transaction/post-index-change hard disables
complete-local-object-store detector
no-replace/no-lazy helpers
closed raw commit writer/verifier
fsync-all command profile
ambient durability-key census
new-object-closure verifier
CAS/durability outcome classifier
alias-safe post-CAS materialization
post-effect verifier
```

## 45. Independent implementation-review obligations

Later implementation review must prove, not infer:

```text
changed surface authorized
no third acceptance route
legacy/defect paths deny
V6 request identity acyclic
one-file decision PR exact
trusted transport exact
review set/currentness complete
freshness/supersession exact
admission no canonical mutation
lock/replay bounded honestly
main exact operative ref
Git 2.55.x semantics profile enforced
files ref format enforced
all authority Git reads no-replace/no-lazy
partial/promisor/alternates rejected
configured hook census complete across include/local/worktree scopes
traditional hooks redirected to verified empty directory
reference-transaction disabled at command scope
post-index-change disabled at command scope
no configured/traditional hook sentinel executes
raw commit construction exact
commit headers closed
all object writes core.fsync=all + core.fsyncMethod=fsync
ambient durability keys rejected
new object closure local/exact before CAS
update-ref uses exact old SHA + hook closure + fsync-all
nonzero/interrupted update-ref classified by raw ref truth
no canonical worktree/index mutation before CAS
post-CAS failures never silently rewrite history
Human attribution only from validated review
no circular evidence
```

## 46. Separately authorized positive controls

A later live positive control requires fresh Human authorization and a disposable ScriptOps execution instance with inert/synthetic content.

Human must see exact V6 material effect including:

```text
canonical before/after hash
refs/heads/main exact ref
V6 REF_COMMITTED decision record
exact two-path one-parent commit
Git 2.55 semantics profile
NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2
COMPLETE_LOCAL_OBJECT_STORE_V1
NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1
CLOSED_RAW_COMMIT_OBJECT_V1
CRASH_DURABLE_GIT_FSYNC_ALL_V1
CRASH_DURABLE_REFS_HEADS_MAIN_CAS_COMMITMENT_V2
REF_CAS_FIRST_ALIAS_SAFE_GIT_PLUMBING_V4
SINGLE_LINK_ALIAS_SAFE_REPOSITORY_TARGETS_V1
```

A separate authorized fault-injection control should force a post-CAS materialization failure and prove `DURABLY_COMMITTED_RECOVERY_REQUIRED`, and another should force an update-ref durability/interrupt ambiguity and prove it is not reported as complete success or no effect.

## 47. Corrective closure composition

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

## 48. Successor-review adversarial checklist

Independent R4R6 brief review must explicitly attack at least:

```text
Can configured hook.* from local/worktree/include scope evade census?
Can hook config be inserted after census and execute anyway?
Does command-scope hook.reference-transaction.enabled=false suppress every configured/traditional reference-transaction hook in bounded Git 2.55.x?
Does command-scope hook.post-index-change.enabled=false suppress every index hook in bounded Git 2.55.x?
Can any used Git command trigger a third hook event?
Can caller PATH/GIT_CONFIG/loader injection substitute executor?
Can repository core.fsync=none or method override weaken object/ref hardening?
Can write-tree create an unhardened intermediate tree object?
Is every new object reachable from effect commit locally exact before CAS?
Can update-ref return failure after ref became new SHA?
Is that state classified without false no-effect or durable-success claim?
Can successful zero-return update-ref under fsync-all still leave an unfrozen object/ref component inside the bounded Git/platform contract?
Can a process kill between object hardening and CAS produce canonical Human success?
Can a process kill during CAS produce ambiguous state that is silently rolled back?
Can V5 evidence authorize V6 effect semantics?
Can replacement refs/lazy fetch/partial clones/alternates reappear?
Can hardlink/symlink target substitution reappear?
Is any core authority/security choice still left to implementer?
```

Any credible counterexample freezes a finding and returns `NOT PASS`.

## 49. Explicit non-authority

This brief does not authorize:

```text
ScriptOps source mutation
Human decision PR creation
Human review creation
live positive control
canonical screenplay mutation
decision-log mutation
refs/heads/main effect
recovery operation
merge
X1B closure
V1 entry
release
deployment
tag
```

R4R6 review PASS, if later obtained, establishes only that this brief is acceptable for a separately Human-authorized implementation stage.

## 50. STOP

Required next stage after durable R4R6 freeze:

```text
INDEPENDENT AK-CANON X1B R4R6 IMPLEMENTATION-BRIEF REVIEW
```

Only fresh separate Human authorization may create that review artifact.

```text
R4R6 BRIEF != IMPLEMENTATION AUTHORITY
R4R6 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R6 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
STOP
```
