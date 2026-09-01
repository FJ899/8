# X1B HUMAN DECISION AUTHORSHIP — CLEAN IMPLEMENTATION BRIEF R4R5

Status: `CLEAN R4R5 CORRECTIVE BRIEF / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-01`

## 1. Authority, purpose, and STOP boundary

This document is the self-contained successor to R4R4 after independent AK-CANON review PR #123 returned `NOT PASS`.

It preserves the accepted X1B corrective design and every R4R4 property not rejected by PR #123, while correcting exactly the two blockers frozen by that review:

1. authority-critical Git commands must never perform implicit promisor/partial-clone lazy fetches;
2. no canonical filesystem/index state or Human-attributed success record may become operative before the exact `refs/heads/main` compare-and-swap that commits the Human-bound effect.

R4R5 therefore introduces two explicit profiles:

```text
COMPLETE_LOCAL_OBJECT_STORE_V1
REFS_HEADS_MAIN_CAS_COMMITMENT_V1
```

and changes the Human-bound material effect profile accordingly.

This document is an implementation brief only. It authorizes no ScriptOps implementation, no Human decision PR/review, no live positive control, no canonical screenplay effect, no merge, no X1B closure, no Agency Kernel v1, no release, deployment, or tag.

```text
R4R5 BRIEF != IMPLEMENTATION AUTHORITY
R4R5 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R5 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

After durable freeze of this brief, STOP. The next stage is a separately Human-authorized independent AK-CANON R4R5 implementation-brief review.

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

### 2.3 R4R4 predecessor

```text
FJ899/8 PR #122
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 7727407eef42447509eae2e60ef2d1e1892c0105
TREE = ce8c4e636ab036fedfca1a2a1bff88c7fdbd020a
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R4.md
BLOB = 23817f0823898d0c857483c2fa5d64c2c261ba06
```

### 2.4 Binding R4R4 NOT-PASS review

```text
FJ899/8 PR #123
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = b4b42c2724a116ee8fa1fb791986c7ded7060ccc
TREE = dd45821ec8e6f0fb3b9471ac539f5d6afb23d6dc
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R4_AK_CANON_REVIEW.md
BLOB = 4f3a9456ed62590de0a07482f114ffd972ea3122
VERDICT = AK-CANON X1B R4R4 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #123 froze:

```text
X1B-R4R4-IBR-F001 — promisor lazy fetch can perform implicit network I/O after FinalEffectGateV4
X1B-R4R4-IBR-F002 — pre-CAS canonical SUCCESS record can survive an unprovable rollback
```

PR #123 also recorded that R4R4 addressed at brief level:

```text
X1B-R4R3-IBR-F001 replacement-ref / raw-object substitution
X1B-R4R3-IBR-F002 local commit-encoding config / extra commit header
```

and preserved the earlier local-ref, hardlink/write-target-alias, and freshness/supersession corrections.

`REVIEW FINDING != REPAIR AUTHORITY`; R4R5 exists only under the fresh Human authorization for successor brief preparation.

## 3. Exact evidence-repository base

```text
FJ899/8 main
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

The earlier unauthorized R4-main write and forward recovery remain visible in history. No history rewrite is part of R4R5.

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

Historical prototype parts remain immutable:

```text
part01 e002ab21b5b353c269e6d14e0d333916b3d07818
part02 35906edee1f2c1b75d70bbb0cb9ead0199e443c8
part03 c4b8fa5ada556a997734cf0ff42ebd4e8eaf31dd
part04 94a6685337d340fc76cdd6ecc3a2ff02c0041220
part05 d25574f78a44295333558ac00c40891da1f998de
part06 86201706c82bca912a77187330e84b2b5c1f461a
part07 e9e67feb2e9f42f34301853845ffcafa9ea27f5f
```

Historical reconstruction remains SHA-256 `881dade6c6c506b9a9d41ebfbf68afb18b66db7583d35f746fb29ed7b36ac596`, size `51980` bytes.

## 5. Normative precedence and V5 migration

```text
R4R5 TEXT = CURRENT IMPLEMENTATION-BRIEF AUTHORITY
R4R4 / R4R3 / R4R2 / R4R1 / R4 / R3 / R2 / R1 = HISTORICAL INPUT ONLY
CORRECTIVE DESIGN PR #34 = HIGHER-LEVEL PROPERTY CONTRACT
```

No authority/security rule depends on implicit inheritance. R4R5 restates the current contract.

R4R5 changes the Human-presented material effect in two material ways:

```text
Git object access is NO-LAZY-FETCH and complete-local-store only
refs/heads/main CAS is the durable Human-effect commitment point before worktree/index materialization
```

Therefore all authority-critical request/evidence/admission/gate/record schemas are bumped from V4 to V5.

```text
V4 REQUEST/REVIEW/ADMISSION/GATE != R4R5 AUTHORITY
V4 HUMAN REVIEW MARKER != V5 HUMAN DECISION
V5 EFFECT PROFILE REQUIRES FRESH V5 HUMAN-BOUND REQUEST
```

No hypothetical V4 or earlier request/review may be reused for a V5 effect.

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

A smaller final changed set is permitted only if independent implementation review proves every R4R5 obligation satisfied. Any additional tracked path requires STOP and fresh Human authorization before mutation.

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

No caller-controlled field may supply Human actor/result/rationale, request path/digest, task/scene/candidate/impact identities, canonical target/ref, effect type, material effect, Git ref, raw-object profile, object-store profile, commit-object profile, commitment profile, or effect commit metadata.

Defect-era Phase-6:

```text
approve --scene ... --why ...
```

must terminate nonzero before Human attribution or canonical effect.

```text
ONE OPERATIVE ACCEPTANCE EFFECT PATH
=
X1B-VALIDATED PHASE6 APPROVE --DECISION-PR PATH
```

## 9. Direct legacy acceptance paths are disabled

```text
python legacy/scriptops-v2-single.py approve --scene <scene>
```

MUST terminate nonzero before canonical scene write, accepted-state transition, decision-log append, Human attribution, Git index/ref mutation, or commit.

```text
python legacy/scriptops-v2-single.py scene-promote --id <scene> --to accepted
```

MUST also be non-effect-capable.

Exact implementation obligations:

```text
remove accepted from direct CLI scene-promote choices
independent internal guard for target_status == "accepted"
legacy approve does not delegate to current authority path
legacy scene-promote does not delegate to acceptance
only Phase-6 approve --decision-pr may create accepted canonical truth
```

Required real regressions begin with a real staged candidate and prove nonzero exit plus no canonical scene, accepted transition, decision-log mutation, Human attribution, real-index mutation, `refs/heads/main` mutation or commit.

Verifier and implementation review must inventory the complete candidate tree and forbid any other executable accepted-state/canonical-effect route.

```text
SAFE NEW PATH + ANY EXECUTABLE UNSAFE ACCEPTANCE PATH = NOT CLOSED
```

## 10. Historical transport, restore, verifier, and authority documentation

```text
sources/prototype/scriptops-v2-single.py.part01..part07
= immutable historical reconstruction evidence

legacy/scriptops-v2-single.py
= active corrected runtime substrate
```

Active legacy is not required to equal the historical 51980-byte source after X1B correction.

`scripts/restore_v2.py` may reconstruct historical bytes only outside the ScriptOps repository. Repository-internal output, relative aliases/traversal, symlink-mediated internal output, repository root, or active legacy target are DENY even under `--force`.

Repository verification must separately prove historical reconstruction and current active-runtime authority.

Authority documentation must state at minimum:

```text
defect-era approve --why = historical provenance only
current Human-decision route = approve --decision-pr <N> only
direct legacy approve = disabled
direct legacy scene-promote --to accepted = disabled
canonical local effect ref = refs/heads/main only
raw Git object profile = NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2
object-store profile = COMPLETE_LOCAL_OBJECT_STORE_V1
commit object profile = CLOSED_RAW_COMMIT_OBJECT_V1
success commitment profile = REFS_HEADS_MAIN_CAS_COMMITMENT_V1
effect transport profile = REF_CAS_FIRST_ALIAS_SAFE_GIT_PLUMBING_V3
historical prototype byte identity != current active runtime identity
```

## 11. Canonical JSON and hash functions

All authority-critical canonical objects use:

```text
canonical_json_bytes(X) = UTF-8 JSON bytes with:
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

File digests bind exact bytes. No Unicode/newline normalization or semantic reserialization where byte identity is specified.

## 12. Exact timestamp profile and raw Git time conversion

Authority-critical locally-created UTC timestamps use exactly:

```text
YYYY-MM-DDTHH:MM:SSZ
```

Requirements:

```text
20 ASCII characters
UTC Z
4-digit year
2-digit month/day/hour/minute/second
no fractional seconds
no offset form
valid calendar/time
```

Applies at least to:

```text
request_created_at
FinalEffectGateV5.observed_at
```

GitHub `submitted_at` used by R4R5 must validate exactly to this UTC `Z` form; otherwise DENY rather than normalize.

For the raw effect commit only:

```text
request_created_epoch = exact signed decimal Unix seconds corresponding to request_created_at UTC
```

Raw Git author/committer timestamp field is exactly:

```text
<request_created_epoch> +0000
```

No local timezone, locale, wall-clock-at-effect, fuzzy Git date parser, or ambient `date` command may choose commit time.

## 13. CanonicalPreStateV1 and deterministic accepted preview

```text
CanonicalPreStateV1 = {
  "exists": <true|false>,
  "file_sha256": <64 lowercase hex or JSON null>
}
```

`exists=false` requires null hash; `exists=true` requires exact current canonical byte hash. Symlink/nonregular/ambiguous target is DENY.

Before Human request finalization, one pure production helper derives exact accepted canonical bytes from exact candidate bytes. It has no write, Git, network, Human-evidence or time side effect and is reused for execution.

```text
accepted_canonical_file_sha256 = SHA256(exact accepted canonical bytes)
```

Admission, FinalEffectGateV5 and effect preparation must re-render and prove exact byte/hash equality.

## 14. R4R5 platform profile

The local effect is bounded to a platform providing equivalent semantics for:

```text
lstat/fstat
st_dev + st_ino + st_nlink
O_NOFOLLOW
O_CREAT | O_EXCL
O_DIRECTORY or equivalent directory-descriptor protection
descriptor-relative open/stat/rename/unlink or equivalent
fsync for files and effect directories
```

The Git executable must support:

```text
--no-replace-objects
--no-lazy-fetch
hash-object -w --stdin --no-filters
hash-object -w -t commit --stdin
cat-file of exact raw objects
read-tree
update-index --cacheinfo
write-tree
ls-tree
update-ref with exact old value
config --local
for-each-ref
```

Object format must be SHA-1. If equivalent guarantees are unavailable, acceptance returns `BLOCKED` before canonical mutation.

## 15. PresentedMaterialEffectV5

Closed schema:

```text
PresentedMaterialEffectV5 = {
  "schema_version": "scriptops-x1b-presented-material-effect/v5",
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
    "record_schema_version": "scriptops-x1b-decision-record/v5",
    "record_result": "COMMITTED",
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
    "raw_object_profile": "NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2",
    "object_store_profile": "COMPLETE_LOCAL_OBJECT_STORE_V1",
    "commit_object_profile": "CLOSED_RAW_COMMIT_OBJECT_V1",
    "success_commitment_profile": "REFS_HEADS_MAIN_CAS_COMMITMENT_V1",
    "effect_transport_profile": "REF_CAS_FIRST_ALIAS_SAFE_GIT_PLUMBING_V3",
    "post_cas_materialization": "WORKTREE_AND_REAL_INDEX_FROM_COMMITTED_TREE",
    "exact_changed_paths": [
      "scenes/<scene_id>.fountain",
      ".scriptops/decision-log.ndjson"
    ]
  },
  "file_identity_profile": "SINGLE_LINK_ALIAS_SAFE_REPOSITORY_TARGETS_V1"
}
```

`<exact scene_id>` and `ref_before` are concrete before request hashing.

No request-digest input may directly or indirectly contain:

```text
request_digest
decision_request_id
PR number
PR head
review ID
admission ID
final gate digest
future effect commit SHA
```

```text
presented_material_effect_digest = sha256_canonical(PresentedMaterialEffectV5)
```

## 16. HumanDecisionRequestBindingV5 — acyclic request identity

```text
HumanDecisionRequestBindingV5 = {
  "schema_version": "scriptops-x1b-human-decision-request/v5",
  "repository": "FJ899/scriptops",
  "repository_head_at_request": <40 lowercase hex>,
  "repository_ref_at_request": "refs/heads/main",
  "request_created_at": <exact R4R5 timestamp>,
  "task_id": <exact task ID>,
  "scene_id": <exact scene ID>,
  "candidate_path": <exact repo-relative candidate path>,
  "candidate_file_sha256": <64 lowercase hex>,
  "impact_report_path": <exact repo-relative impact path>,
  "impact_report_sha256": <64 lowercase hex>,
  "canonical_target": "scenes/<scene_id>.fountain",
  "canonical_ref": "refs/heads/main",
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect": <PresentedMaterialEffectV5>
}
```

Construction order:

```text
1 validate raw refs/heads/main and request base under V2 raw-object + complete-local-store profile
2 validate candidate/impact/canonical pre-state
3 render accepted preview bytes/hash
4 construct PresentedMaterialEffectV5
5 construct HumanDecisionRequestBindingV5
6 request_binding_json = canonical_json_bytes(binding)
7 request_digest = sha256_hex_bytes(request_binding_json)
8 decision_request_id = "x1b:" + request_digest
9 construct committed HumanDecisionRequestV5
```

```text
HumanDecisionRequestV5 = {
  <all HumanDecisionRequestBindingV5 fields>,
  "decision_request_id": <exact x1b:digest>,
  "request_digest": <exact digest>
}
```

Same exact pre-request bindings must produce the same digest/ID without fixed-point search or self-reference.

## 17. Deterministic decision-request artifact and proposal branch

```text
request_path = decisions/x1b/<request_digest>.json
request_branch = decision/x1b/<request_digest>
decision_request_id = x1b:<request_digest>
```

Request bytes are exactly `canonical_json_bytes(HumanDecisionRequestV5)` with no trailing LF.

Proposal commit:

```text
branch = decision/x1b/<request_digest>
parent = repository_head_at_request
changed-file set = exactly one added request_path
request blob = exact committed HumanDecisionRequestV5 bytes
no second path
```

Proposal creation requires separate proposal-writing authority. The evaluated effect invocation must not create/edit proposal branch/file/PR, GitHub review/comment, or GitHub ref/rule/setting.

```text
PROPOSAL PR CREATION != HUMAN DECISION
```

## 18. Decision PR envelope

Effect CLI accepts only a positive integer decision PR locator.

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
request file bytes/schema/digest exact
```

No caller request path/digest is trusted. Equality required among filename digest, computed binding digest, request field digest, decision-request-ID suffix and head-ref digest. Any extra/renamed/deleted path, wrong base/head/repository, hidden pagination remainder or ambiguity is DENY.

## 19. Human authority profile and exact V5 Human review body

Authoritative Human actor for this bounded profile:

```text
litrgratis-pixel
```

A later positive control requires a manual Human GitHub UI `APPROVE` governance act by this actor.

Exact review body is four LF-separated lines with no trailing LF:

```text
X1B-HUMAN-DECISION-V5
decision_request_id=<exact x1b:<request_digest>>
decision_request_sha256=<exact request_digest>
why=<Human rationale>
```

Rationale validation:

```text
1..2000 Unicode code points inclusive
value == value.strip()
no U+0000..U+001F
no U+007F
therefore no CR/LF/TAB/NUL/control characters
```

Review must be:

```text
actor = litrgratis-pixel
state = APPROVED
commit_id = exact current decision PR HEAD
body = exact four-line V5 body
```

Human rationale/attribution derive only from that review, never from CLI input.

## 20. Public trusted GitHub evidence transport

Production verifier for this public repository uses unauthenticated public GitHub REST reads only from exactly:

```text
https://api.github.com
```

Transport profile:

```text
urllib.request
ProxyHandler({})
HTTPSHandler(context=ssl.create_default_context())
redirect handler rejects every redirect
fixed User-Agent
Accept: application/vnd.github+json
X-GitHub-Api-Version: 2022-11-28
no Authorization header
```

No configurable API base, authenticated fallback, `gh`, `.netrc`, browser session, caller token, cached review JSON or Git credential helper may obtain Human decision evidence.

Non-empty proxy/CA/GitHub credential overrides cause DENY before evidence acquisition, including at minimum:

```text
HTTP_PROXY HTTPS_PROXY ALL_PROXY
http_proxy https_proxy all_proxy
SSL_CERT_FILE SSL_CERT_DIR
REQUESTS_CA_BUNDLE CURL_CA_BUNDLE
GIT_SSL_CAINFO GIT_SSL_CAPATH
GH_TOKEN GITHUB_TOKEN
GH_ENTERPRISE_TOKEN GITHUB_ENTERPRISE_TOKEN
GITHUB_PAT
```

Redirect, alternate origin, rate limit, visibility change, malformed/incomplete response or ambiguity => DENY/BLOCKED before effect.

## 21. Exact GitHub reads, pagination, and CompleteReviewSetV5

Bounded reads equivalent to:

```text
GET /repos/FJ899/scriptops/pulls/<N>
GET /repos/FJ899/scriptops/pulls/<N>/files?per_page=100&page=<p>
GET /repos/FJ899/scriptops/contents/<derived-request-path>?ref=<exact-head-sha>
GET /repos/FJ899/scriptops/git/commits/<exact-head-sha>
GET /repos/FJ899/scriptops/pulls/<N>/reviews?per_page=100&page=<p>
```

Every collection begins page 1 with `per_page=100`, advances sequentially and continues until completion is unambiguous.

```text
NormalizedReviewV5 = {
  "numeric_id": <canonical decimal string>,
  "node_id": <non-empty exact string>,
  "actor": <exact login>,
  "state": <APPROVED|CHANGES_REQUESTED|COMMENTED|DISMISSED>,
  "commit_id": <40 lowercase hex or JSON null>,
  "body_sha256": <SHA256 of exact UTF-8 body bytes>,
  "submitted_at": <exact validated timestamp or JSON null>
}
```

Order ascending `(numeric_id as integer, node_id)`. Duplicate numeric or node ID => DENY. Unknown state => DENY.

```text
CompleteReviewSetV5 = {
  "schema_version": "scriptops-x1b-complete-review-set/v5",
  "repository": "FJ899/scriptops",
  "decision_pr_number": <positive integer>,
  "decision_pr_head": <40 lowercase hex>,
  "reviews": [<all normalized reviews in normative order>]
}
```

```text
complete_review_set_digest = sha256_canonical(CompleteReviewSetV5)
```

For `litrgratis-pixel` on exact current PR HEAD there must be exactly one active syntactically/semantically valid V5 APPROVED and no active CHANGES_REQUESTED. Second current-head APPROVED => ambiguous DENY. Old-commit APPROVED => historical only. No latest-wins chronology rule.

## 22. Candidate, impact, local Git-tree, and applicability checks

Before preliminary admission and again at FinalEffectGateV5 where applicable:

```text
logical repository identity = FJ899/scriptops
repository_ref_at_request = refs/heads/main
HEAD symbolic ref = refs/heads/main
raw HEAD SHA = raw refs/heads/main SHA = request.repository_head_at_request
Git object format = sha1
NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2 satisfied
COMPLETE_LOCAL_OBJECT_STORE_V1 satisfied
no refs/replace/*
raw parent tree derived from raw request-base commit object
real index write-tree = raw parent tree
no tracked/index delta
candidate regular non-symlink exact repo-relative path
candidate bytes/hash/status=candidate exact
candidate tracked identity at raw parent tree exact
impact path = tasks/<task_id>/impact-report.json
impact regular non-symlink exact bytes/hash
impact tracked identity at raw parent tree exact
impact status=REVIEW_REQUIRED
impact task/scene/candidate path/hash match request
canonical target = scenes/<scene_id>.fountain
effect type = ACCEPT_SCENE_CANDIDATE
canonical filesystem/raw-tree pre-state matches request
accepted preview bytes/hash match request
PresentedMaterialEffectV5 object/digest match request
request unconsumed in this canonical local instance
```

If an effect target is absent from the raw parent tree, filesystem path must also be absent before effect. If present, filesystem bytes and raw Git blob/mode must agree with validated pre-state. Ignored/untracked substitute at an effect path is DENY.

Candidate source is preserved and final Git effect may not alter/remove it.

## 23. Explicit activation, age, deactivation, multiple decisions, supersession

A selected decision is active only while all exact PR/request/review/local-ref/raw-object/object-store/applicability predicates remain true.

Age policy remains deliberately:

```text
NO WALL-CLOCK TTL
AGE ALONE != STALE
```

Selected decision becomes inactive/inapplicable upon PR close/merge, identity drift, approval dismissal, active authoritative CHANGES_REQUESTED, ambiguity/conflict, incomplete evidence, raw local ref mismatch, raw-object failure, object-store-profile failure, candidate/impact/canonical/preview/effect drift, or same-instance consumption.

Each decision PR is a separate Human decision domain. Another approved decision PR does not implicitly supersede, revoke or chronology-win over the selected PR.

Two separately Human-approved same-base requests may coexist. The first successful local ref CAS makes every still-unconsumed old-base request inapplicable by exact raw ref/base mismatch.

```text
NO CHRONOLOGY-ONLY WINNER
OLD CONSENT + CHANGED OPERATION = DENY
NO GLOBAL CROSS-CLONE EXACTLY-ONCE CLAIM
```

## 24. HumanDecisionAdmissionIdentityV5

```text
HumanDecisionAdmissionIdentityV5 = {
  "schema_version": "scriptops-x1b-human-decision-admission/v5",
  "repository": "FJ899/scriptops",
  "repository_head_at_request": <exact SHA>,
  "repository_ref_at_request": "refs/heads/main",
  "decision_pr_number": <positive integer>,
  "decision_pr_head": <exact head>,
  "decision_request_id": <x1b:digest>,
  "request_digest": <64 lowercase hex>,
  "request_file_path": "decisions/x1b/<request_digest>.json",
  "human_review_numeric_id": <canonical decimal string>,
  "human_review_node_id": <exact node ID>,
  "human_actor": "litrgratis-pixel",
  "human_review_body_sha256": <64 lowercase hex>,
  "human_review_submitted_at": <exact timestamp>,
  "human_rationale": <validated exact rationale>,
  "complete_review_set_digest": <exact digest>,
  "task_id": <exact task>,
  "scene_id": <exact scene>,
  "candidate_path": <exact path>,
  "candidate_file_sha256": <exact digest>,
  "impact_report_path": <exact path>,
  "impact_report_sha256": <exact digest>,
  "canonical_target": "scenes/<scene_id>.fountain",
  "canonical_ref": "refs/heads/main",
  "canonical_before": <CanonicalPreStateV1>,
  "canonical_after_file_sha256": <exact digest>,
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect_digest": <exact digest>,
  "raw_object_profile": "NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2",
  "object_store_profile": "COMPLETE_LOCAL_OBJECT_STORE_V1",
  "commit_object_profile": "CLOSED_RAW_COMMIT_OBJECT_V1",
  "success_commitment_profile": "REFS_HEADS_MAIN_CAS_COMMITMENT_V1",
  "canonical_instance_scope": "LOCAL_REFS_HEADS_MAIN_WORKTREE_DECISION_LOG_V5"
}
```

```text
admission_id = "x1b-admit:" + sha256_canonical(HumanDecisionAdmissionIdentityV5)
```

Admission is in-memory one-shot machine state, not Human evidence or execution credential. Preliminary admission cannot mutate canonical scene, decision log, real index or `refs/heads/main`.

## 25. Bounded replay and same-worktree lock

Bounded claim:

```text
one decision_request_id may cause at most one successful X1B ref commitment
within one canonical local refs/heads/main worktree execution instance
```

Before effect, complete local `.scriptops/decision-log.ndjson` must contain no prior V5/V4/V3 record carrying exact `decision_request_id`. Malformed non-empty line => DENY.

Worktree-specific lock:

```text
<worktree-specific git-dir>/scriptops-x1b-approve.lock
```

Create exclusively before admission. Existing lock => DENY/BLOCKED. No automatic stale-lock deletion. Hold through post-CAS materialization/post-effect verification/cleanup.

A second independent clone is a separate canonical execution instance.

## 26. Exact local canonical Git ref

The only operative local effect ref is:

```text
refs/heads/main
```

At request creation, admission, FinalEffectGateV5 and pre-CAS recheck:

```text
symbolic HEAD == refs/heads/main
raw HEAD ref value == raw refs/heads/main value == request.repository_head_at_request
```

Side branch, detached HEAD, unborn/ambiguous symbolic ref, non-main ref or drift => DENY.

Final ref mutation is compare-and-swap only:

```text
refs/heads/main:
exact old request SHA -> exact prepared effect commit SHA
ONLY IF current raw old ref still equals exact request SHA
```

No force update, alternate ref or detached-only success.

## 27. R4R5 correction F001 — COMPLETE_LOCAL_OBJECT_STORE_V1

R4R5 forbids acceptance from a partial/promisor object-store topology.

At request creation, preliminary admission, FinalEffectGateV5, immediately before effect-object preparation, immediately before CAS and post-effect verification, the implementation must prove all of:

```text
repository is not shallow
legacy graft source absent
refs/replace namespace empty
extensions.partialClone absent from repository-local config
no repository-local remote.*.promisor key
no repository-local remote.*.partialclonefilter key
no *.promisor pack sidecar in the operative object database
objects/info/alternates absent
no repository-configured alternate object-store path
caller GIT_OBJECT_DIRECTORY absent/ignored
caller GIT_ALTERNATE_OBJECT_DIRECTORIES absent/ignored
all authority-required objects can be read locally under no-lazy-fetch semantics
```

Presence of any partial/promisor/alternate-store marker is DENY/BLOCKED before successful Human-attributed effect, even if currently required objects happen to be cached.

Rationale:

```text
PROMISOR CONFIG + CURRENTLY PRESENT OBJECTS != COMPLETE LOCAL STORE
NO NETWORK COMMAND INTENT != NO IMPLICIT LAZY FETCH
```

The effect process never repairs, deepens, fetches or converts such a repository. Repository normalization is a separate administrative action outside X1B approval authority.

## 28. System Git executable and exact subprocess profile

The operative effect MUST NOT use porcelain mutation commands:

```text
git add
git commit
git checkout
git reset
```

Resolve a system Git executable from runtime system-default executable search domain, not caller PATH. Require strict real path, absolute regular executable outside repository and stable stat identity for the effect. No unambiguous system Git => BLOCKED.

Every authority-critical Git subprocess uses:

```text
absolute resolved Git executable
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

and invokes global options in this order before the subcommand:

```text
--no-replace-objects
--no-lazy-fetch
```

Command-level config at minimum:

```text
-c core.hooksPath=/dev/null
-c core.fsmonitor=false
-c commit.gpgSign=false
-c credential.helper=
```

Remove caller values for all `GIT_CONFIG_*`, `GIT_DIR`, `GIT_WORK_TREE`, `GIT_COMMON_DIR`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_EXEC_PATH`, `GIT_EXTERNAL_DIFF`, `GIT_ASKPASS`, `SSH_ASKPASS`, `GIT_SSH`, `GIT_SSH_COMMAND`, `GIT_REPLACE_REF_BASE`, `GIT_NO_LAZY_FETCH`, loader-injection variables and other caller `GIT_*` overrides unless R4R5 explicitly constructs a bounded replacement for a specific subprocess.

The implementation itself sets `GIT_NO_LAZY_FETCH=1`; caller `0` cannot override it.

No acceptance Git subprocess may intentionally or implicitly perform network I/O.

Any missing object under `--no-lazy-fetch` is BLOCKED. The effect process must not retry without the option and must not invoke fetch.

## 29. NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2

Replacement-object semantics remain forbidden.

Every authority-critical Git command runs with both:

```text
GIT_NO_REPLACE_OBJECTS=1
--no-replace-objects
```

and both no-lazy controls:

```text
GIT_NO_LAZY_FETCH=1
--no-lazy-fetch
```

Raw request-base commit identity is established from exact local object bytes:

```text
raw_base = request.repository_head_at_request
object type(raw_base) = commit
raw_base_content = exact bytes from no-replace/no-lazy cat-file commit raw_base
raw_base tree header = exactly one 40-hex tree ID
raw_base parent headers parsed only as raw content when needed
```

The exact parent tree for all effect comparison is:

```text
raw_parent_tree = tree header parsed from raw_base_content
```

All authority-critical operations inspecting commits/trees/diffs use no-replace/no-lazy semantics, including equivalents of:

```text
cat-file
rev-parse
ls-tree
read-tree
write-tree
diff-tree
show / log if used
post-effect parent/tree verification
```

No replace-aware or lazy-fetch-enabled output may become an authority fact.

## 30. CLOSED_RAW_COMMIT_OBJECT_V1 preserved

R4R5 does not use `git commit-tree` to create the operative effect commit.

After `new_tree` is proven exact, construct exact raw commit content bytes in memory.

Let:

```text
T = exact 40-lowercase-hex new_tree
P = exact request.repository_head_at_request
E = exact canonical decimal request_created_epoch
M = UTF-8 bytes of "scriptops x1b: accept <exact scene_id>"
LF = byte 0x0A
```

Exact raw commit content is:

```text
ASCII("tree " + T) + LF
+ ASCII("parent " + P) + LF
+ UTF8("author ScriptOps X1B <scriptops-x1b@local.invalid> " + E + " +0000") + LF
+ UTF8("committer ScriptOps X1B <scriptops-x1b@local.invalid> " + E + " +0000") + LF
+ LF
+ M + LF
```

There are exactly four headers, in this order:

```text
tree
parent
author
committer
```

Forbidden headers include:

```text
encoding
gpgsig
gpgsig-sha256
mergetag
extra parent
unknown/duplicate header
```

Before writing the object, independently compute:

```text
expected_effect_commit_sha1 =
SHA1(
  ASCII("commit ")
  + ASCII(decimal byte length of raw_commit_content)
  + NUL
  + raw_commit_content
)
```

Write exactly prepared content using no-replace/no-lazy plumbing equivalent to:

```text
git --no-replace-objects --no-lazy-fetch hash-object -w -t commit --stdin
```

Returned object ID must equal `expected_effect_commit_sha1`.

Read back exact object under no-replace/no-lazy semantics and prove byte-for-byte equality plus closed header schema.

Repository-local `i18n.commitEncoding` may not affect this object.

## 31. Exact output blobs and private temporary index

Before any canonical filesystem, real-index or ref mutation:

```text
real_index_tree = no-replace/no-lazy git write-tree
raw_parent_tree = parsed raw base tree
real_index_tree == raw_parent_tree
```

Compute exact output blobs:

```text
accepted_scene_blob = hash-object -w --stdin --no-filters
  over exact accepted canonical bytes

decision_log_blob = hash-object -w --stdin --no-filters
  over exact post-append decision-log bytes
```

Each command uses no-replace/no-lazy profile. Read each object back and prove exact bytes. Independently compute SHA-1 object IDs from `blob <len>\0<bytes>` and require equality with Git output.

Create a fresh private temporary index inside worktree-specific Git directory with exclusive creation/mode 0600. Set `GIT_INDEX_FILE` only for these private-index commands.

Initialize from exact `raw_parent_tree`:

```text
read-tree <raw_parent_tree>
```

Under `--no-lazy-fetch`, missing promised/local objects fail locally; no fetch is permitted.

Update exactly:

```text
update-index --add --cacheinfo 100644,<accepted_scene_blob>,scenes/<scene_id>.fountain
update-index --add --cacheinfo 100644,<decision_log_blob>,.scriptops/decision-log.ndjson
```

Then:

```text
new_tree = write-tree
```

Prove under no-replace/no-lazy/raw semantics:

```text
new_tree differs from raw_parent_tree only at exact two paths
ls-tree(new_tree, exact paths) = mode 100644 + expected blob IDs
no candidate/request/impact/third path changed
```

Only after this proof may CLOSED_RAW_COMMIT_OBJECT_V1 construct the exact effect commit.

Private temp index and unreferenced object-database writes are preparation only. They are not canonical Human-attributed success.

## 32. Repository-contained parent directories and alias-safe targets

Both parents must already exist:

```text
scenes/
.scriptops/
```

Every parent-chain component used by an effect target must be repository-contained, real directory, non-symlink, opened via protected descriptor/equivalent, contain no lexical `..` escape and resolve nowhere outside repository.

Before CAS, acquire and validate protected parent descriptors and exact pre-state identities, but do not replace/create canonical target files.

Existing effect target precondition:

```text
lstat => regular file
not symlink
st_nlink == 1
bytes match validated pre-state/raw parent blob
open O_NOFOLLOW/equivalent
fstat identity == validated st_dev + st_ino
still regular + st_nlink == 1
```

After CAS, materialization never truncates/writes a validated existing inode in place. It writes a fresh same-directory exclusive no-follow temporary inode, fsyncs, revalidates the old target identity, atomically replaces through protected directory descriptor, fsyncs directory, reopens new target no-follow and proves exact bytes/hash/single link.

Absent target uses verified parent descriptor and exclusive no-follow creation after CAS only.

Existence race, symlink, hardlink count >1, nonregular target, parent substitution or ambiguous identity before CAS => DENY without effect. Such interference detected after CAS => `COMMITTED_RECOVERY_REQUIRED`; the ref is not silently rolled back.

## 33. FinalEffectGateV5

Immediately before local effect-object preparation, while lock is held, freshly reread PR metadata and complete reviews through trusted public transport.

Revalidate:

```text
exact PR/request envelope
selected Human review/currentness/conflicts
CompleteReviewSetV5 digest
repository logical identity
raw symbolic/ref identity = refs/heads/main + exact request SHA
NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2
COMPLETE_LOCAL_OBJECT_STORE_V1
no refs/replace/*
raw request-base commit/tree identity
candidate/impact/canonical pre-state
accepted preview
PresentedMaterialEffectV5
replay state
real-index tree = raw parent tree
file-identity target preconditions
protected parent-directory descriptors acquired and validated
Git executable/platform preconditions
```

```text
FinalEffectGateV5 = {
  "schema_version": "scriptops-x1b-final-effect-gate/v5",
  "admission_id": <exact admission_id>,
  "decision_request_id": <exact decision_request_id>,
  "request_digest": <exact request_digest>,
  "presented_material_effect_digest": <exact digest>,
  "decision_pr_number": <positive integer>,
  "decision_pr_head": <exact head>,
  "human_review_numeric_id": <canonical decimal string>,
  "human_review_node_id": <exact node ID>,
  "human_actor": "litrgratis-pixel",
  "human_review_body_sha256": <exact digest>,
  "complete_review_set_digest": <exact digest>,
  "target_ref": "refs/heads/main",
  "ref_before": <exact request base>,
  "raw_parent_tree": <exact 40 lowercase hex>,
  "canonical_before": <CanonicalPreStateV1>,
  "canonical_after_file_sha256": <exact digest>,
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "raw_object_profile": "NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2",
  "object_store_profile": "COMPLETE_LOCAL_OBJECT_STORE_V1",
  "commit_object_profile": "CLOSED_RAW_COMMIT_OBJECT_V1",
  "success_commitment_profile": "REFS_HEADS_MAIN_CAS_COMMITMENT_V1",
  "canonical_instance_scope": "LOCAL_REFS_HEADS_MAIN_WORKTREE_DECISION_LOG_V5",
  "current_human_decision_valid": true,
  "observed_at": <exact R4R5 UTC timestamp>
}
```

```text
final_effect_gate_digest = sha256_canonical(FinalEffectGateV5)
```

Gate is in-memory one-shot state and not a reusable credential.

After gate:

```text
no user interaction
no network
no sleep/wait
no unrelated blocking operation
no proposal/review mutation
no untrusted subprocess
```

Only bounded local no-replace/no-lazy effect preparation and exact pre-CAS revalidation may proceed.

## 34. X1BDecisionRecordV5 — exact committed-result semantics

Before CAS, construct exact decision-record bytes in memory only.

```text
X1BDecisionRecordV5 = {
  "schema_version": "scriptops-x1b-decision-record/v5",
  "result": "COMMITTED",
  "result_scope": "REFS_HEADS_MAIN_CAS_COMMITMENT",
  "decision_type": "scene_acceptance_committed",
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
  "human_rationale": <exact validated rationale>,
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
  "commit_object_profile": "CLOSED_RAW_COMMIT_OBJECT_V1",
  "success_commitment_profile": "REFS_HEADS_MAIN_CAS_COMMITMENT_V1",
  "canonical_instance_scope": "LOCAL_REFS_HEADS_MAIN_WORKTREE_DECISION_LOG_V5"
}
```

NDJSON record bytes are:

```text
canonical_json_bytes(X1BDecisionRecordV5) + exactly one LF
```

Effect commit SHA remains absent to avoid a self-hash cycle.

Critical semantics:

```text
IN-MEMORY RECORD BYTES != COMMITTED RESULT
UNREFERENCED BLOB/TREE/COMMIT OBJECT != CANONICAL DECISION LOG
RESULT=COMMITTED BECOMES TRUE ONLY AT SUCCESSFUL refs/heads/main CAS
```

Before CAS, the record may exist only in memory, an unreferenced blob, a private temporary index/tree, and the prepared unreferenced commit object. It must not exist at canonical filesystem path, real index, or any canonical ref.

## 35. R4R5 correction F002 — REFS_HEADS_MAIN_CAS_COMMITMENT_V1

The durable Human-effect commitment point is exactly:

```text
successful atomic compare-and-swap of refs/heads/main
from exact request base SHA
to exact preverified effect commit SHA
using update-ref with exact old value
```

Immediately before this CAS, while the same X1B lock is held, revalidate locally with no-replace/no-lazy semantics:

```text
HEAD symbolic ref still refs/heads/main
raw HEAD/ref still exact request base
COMPLETE_LOCAL_OBJECT_STORE_V1 still satisfied
refs/replace namespace still empty
prepared effect commit object byte-identical and locally readable
prepared commit parent exact request base
prepared commit tree exact new_tree
new_tree exact two-path delta
canonical filesystem targets still exact pre-effect identities/bytes
real index still raw parent tree
protected parent descriptors still valid
```

No network reread is permitted here; Human currentness was frozen by FinalEffectGateV5 and no network is allowed afterward.

If any pre-CAS check fails:

```text
DO NOT CAS
DO NOT WRITE CANONICAL SCENE
DO NOT WRITE CANONICAL DECISION LOG
DO NOT MUTATE REAL INDEX
DO NOT EMIT COMMITTED/SUCCESS HUMAN ATTRIBUTION
return DENY/BLOCKED
```

Unreferenced prepared Git objects may remain for normal Git garbage collection. Their presence does not constitute canonical Human-attributed success.

## 36. Exact local effect sequence

After FinalEffectGateV5 success, with lock held:

```text
A. prove NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2 and COMPLETE_LOCAL_OBJECT_STORE_V1

B. construct exact X1BDecisionRecordV5 bytes in memory

C. construct/verify exact accepted-scene + decision-log blobs
   write only Git object-database objects; no canonical filesystem or real-index mutation

D. build exact new_tree in private temporary index from raw_parent_tree
   prove exact two-path delta

E. construct exact CLOSED_RAW_COMMIT_OBJECT_V1 content
   independently compute SHA-1
   write raw commit object
   read back and prove exact equality

F. perform full pre-CAS local recheck from section 35

G. atomic CAS:
   refs/heads/main: exact request base -> exact prepared effect commit SHA
   using update-ref with exact old value

H. immediately reread raw refs/heads/main and exact effect commit
   if CAS command did not succeed or ref never became exact effect SHA: no commitment
   if exact effect SHA is observed after successful CAS: effect is COMMITTED

I. only after committed ref is established, materialize exact accepted scene bytes
   through alias-safe target helper using held/revalidated parent descriptor

J. only after committed ref is established, materialize exact committed decision-log bytes
   through alias-safe target helper

K. update real index to exact committed new_tree using hook-disabled no-replace/no-lazy plumbing
   without `-u` and without worktree filters

L. prove real index write-tree == exact committed tree

M. verify worktree/index/targets/raw commit/raw changed set/profile identities exact

N. release lock only after completion status has been durably determined
```

No canonical filesystem or real-index mutation occurs in A-F.

No `git add .`, no porcelain commit, no `commit-tree`, no replace-aware authority read, no lazy-fetch-enabled authority read.

## 37. Pre-CAS failure boundary

Before successful CAS:

```text
canonical scene filesystem = pre-effect state
canonical decision-log filesystem = pre-effect state
real index = raw parent tree
refs/heads/main = request base
no durable Human result record reachable from canonical ref
```

Therefore a pre-CAS failure requires no semantic rollback of canonical state.

Cleanup may remove private temp index/files. Failure to remove unreferenced prepared Git objects is not a canonical effect and must not be presented as Human success.

This replaces the R4R4 model that first wrote canonical files and then attempted rollback.

## 38. Post-CAS committed state and materialization

After successful CAS, the exact effect commit is canonical Git truth. Its tree atomically contains both:

```text
accepted canonical scene blob
X1BDecisionRecordV5 with result=COMMITTED
```

At that point the Human-bound repository effect has committed exactly once to `refs/heads/main`.

Worktree and real index are then materialized to that already-committed tree.

Normal zero-exit completion requires:

```text
raw main ref exact effect commit
raw effect commit exact
worktree targets exact committed blobs
real index exact committed tree
worktree clean relative to raw main
post-effect verification complete
```

If materialization or post-verification fails after CAS:

```text
DO NOT claim no effect occurred
DO NOT roll back/rewrite refs/heads/main silently
DO NOT create a second success record
DO NOT create a second effect commit
return nonzero distinct status COMMITTED_RECOVERY_REQUIRED
preserve exact committed ref/objects for forensic truth
```

A separately authorized recovery procedure may later reconcile worktree/index to the already-committed tree. Recovery is outside this brief's implementation authority unless separately authorized.

The V5 record says `COMMITTED`, not generic `SUCCESS`, so it remains truthful even when post-CAS materialization requires recovery.

## 39. Post-effect truth for zero-exit completion

Zero-exit successful completion requires all:

```text
raw HEAD == raw refs/heads/main == exact expected effect commit SHA
zero refs/replace/*
COMPLETE_LOCAL_OBJECT_STORE_V1 still satisfied
raw effect commit bytes == precomputed CLOSED_RAW_COMMIT_OBJECT_V1 bytes
raw effect commit has exactly one parent = request base
raw effect commit tree = exact preverified new_tree
raw changed set from actual raw parent = exactly:
  scenes/<scene_id>.fountain
  .scriptops/decision-log.ndjson
both tree modes = 100644
both committed blob IDs = exact precomputed output blob IDs
canonical filesystem bytes hash = bound after hash
canonical status = accepted
candidate source unchanged
exactly one new X1BDecisionRecordV5 line in committed tree and filesystem
record result = COMMITTED
record request/admission/gate/review/effect/ref/profile identities exact
worktree/index clean relative to resulting raw HEAD
real index write-tree = resulting raw HEAD tree
lock held until verification completes
```

No replace-aware or lazy-fetch-enabled result can satisfy post-effect truth.

```text
GREEN COMMAND EXIT != POST-EFFECT TRUTH
COMMITTED REF != ZERO-EXIT MATERIALIZATION COMPLETE
```

## 40. Exact outcome classes

Implementation must distinguish at least:

```text
DENIED
BLOCKED_PRE_COMMIT
COMMITTED_RECOVERY_REQUIRED
COMMITTED_COMPLETE
```

Semantics:

```text
DENIED / BLOCKED_PRE_COMMIT:
  refs/heads/main never committed effect SHA
  no canonical filesystem/index effect
  no canonical COMMITTED record

COMMITTED_RECOVERY_REQUIRED:
  refs/heads/main successfully committed exact effect SHA
  record COMMITTED is truthful
  worktree/index completion not proven
  no silent history rewrite

COMMITTED_COMPLETE:
  ref commitment plus exact post-CAS worktree/index materialization verified
```

User-visible wording and logs must never collapse `COMMITTED_RECOVERY_REQUIRED` into either `no effect` or `complete success`.

## 41. Git hook/filter/config attack regressions

Mandatory injections include individually and in meaningful combinations:

```text
pre-commit hook
prepare-commit-msg hook
commit-msg hook
post-commit hook
post-index-change hook
reference-transaction hook
custom core.hooksPath
clean filter
process filter
core.attributesFile override
repository .gitattributes transformation rule
commit.gpgSign=true
gpg.program helper
core.fsmonitor external command
caller GIT_CONFIG_COUNT / GIT_CONFIG_KEY_* injection
caller GIT_INDEX_FILE / GIT_OBJECT_DIRECTORY injection
caller PATH containing fake git
LD_PRELOAD / equivalent loader injection where test platform permits
repository-local i18n.commitEncoding=ISO-8859-1
repository-local i18n.commitEncoding=<other non-UTF-8 value>
```

Tests prove injection is rejected before commitment or cannot execute/transform the bounded effect. Sentinel hooks/filters/helpers must not execute. Exact raw blob/tree/commit/ref identities remain exact.

## 42. Lazy-fetch / partial-clone regressions

Mandatory negatives include:

```text
partial clone with extensions.partialClone
remote.origin.promisor=true
remote.origin.partialclonefilter present
pack *.promisor sidecar present
objects/info/alternates present
caller GIT_ALTERNATE_OBJECT_DIRECTORIES injection
caller GIT_OBJECT_DIRECTORY injection
caller GIT_NO_LAZY_FETCH=0
missing promised parent tree object
missing promised subtree required by read-tree
missing promised blob required by verification
partial/promisor markers introduced after admission before FinalEffectGateV5
partial/promisor markers introduced after FinalEffectGateV5 before pre-CAS recheck
```

Every such case is DENY/BLOCKED before CAS.

Mandatory sentinel regression:

```text
construct partial/promisor repository with a missing promised object
configure promisor remote/transport so any lazy fetch leaves an unmistakable sentinel
attempt approval under production path
=> command fails locally before CAS
=> sentinel proves no fetch/transport executed
=> refs/heads/main unchanged
=> canonical filesystem/index unchanged
```

Mandatory helper regression proves every authority-critical Git argv begins with both global options before subcommand:

```text
--no-replace-objects
--no-lazy-fetch
```

and every subprocess environment contains:

```text
GIT_NO_REPLACE_OBJECTS=1
GIT_NO_LAZY_FETCH=1
```

No fallback without `--no-lazy-fetch` is permitted.

## 43. Raw-object / replacement-ref regressions

Mandatory negatives preserve:

```text
refs/replace/<request-base> -> alternate commit with unrelated third-path delta
replacement ref introduced before admission
replacement ref introduced after admission but before FinalEffectGateV5
replacement ref introduced after FinalEffectGateV5 but before pre-CAS recheck
nonempty refs/replace namespace unrelated to request base
caller GIT_REPLACE_REF_BASE injection
replace-aware Git command accidentally used in authority helper
shallow repository
graft source present
```

All fail closed before CAS.

Mandatory positive unit proof:

```text
raw no-replace/no-lazy cat-file of exact SHA returns original exact local object bytes
regardless of installed replacement ref
```

## 44. CAS-first / false-success regressions

Mandatory tests include:

```text
prepared objects then main moved before CAS
=> CAS not attempted or fails old-value check
=> no canonical filesystem/index mutation
=> no canonical COMMITTED record

CAS command forced to fail
=> no canonical filesystem/index mutation
=> no canonical COMMITTED record

failure while building private temp index
=> no canonical mutation

failure while writing prepared blob/tree/commit objects
=> no canonical mutation

failure during final pre-CAS target identity recheck
=> no canonical mutation

process terminated immediately before CAS
=> no canonical mutation

process terminated immediately after successful CAS but before worktree writes
=> exact effect commit remains on main
=> committed tree contains exact V5 COMMITTED record
=> restart/inspection reports committed-recovery state, never "no effect"

post-CAS canonical scene materialization failure
=> ref remains exact effect commit
=> no second commit/record
=> COMMITTED_RECOVERY_REQUIRED

post-CAS decision-log filesystem materialization failure
=> same committed truth and recovery-required status

post-CAS real-index update failure
=> same committed truth and recovery-required status
```

A regression must prove no V4-style durable filesystem `result=SUCCESS` can survive a failed pre-CAS attempt, because no canonical target is written before CAS and V5 uses `result=COMMITTED`.

## 45. Ref-binding regressions

Mandatory negatives preserve:

```text
side branch at exact request SHA
detached HEAD at exact request SHA
HEAD symbolic ref not main
main moved after admission
main moved after FinalEffectGateV5 but before CAS
CAS old-SHA mismatch
prepared raw commit parent wrong
prepared tree targets another ref
```

All pre-CAS cases fail without canonical filesystem/index Human-attributed effect.

## 46. Freshness/supersession regressions

Required tests include:

```text
old age alone + every other currentness predicate exact -> remains applicable
PR closed -> DENY
PR merged -> DENY
approval dismissed -> DENY
active authoritative CHANGES_REQUESTED -> DENY
second current-head APPROVED -> DENY ambiguous
old-commit APPROVED only -> DENY
selected PR incomplete review pagination -> DENY
another approved PR does not chronology-supersede selected PR
first same-base successful ref CAS -> second old-base request DENY
changed candidate/effect/profile with old Human review -> DENY
V4 review marker/request -> DENY for V5 effect
```

## 47. Original X1B preregistered attacks remain mandatory

Corrective verification still executes every original class:

```text
1 AI marks its own proposal accepted
2 Continue treated as Human decision
3 no Human response treated as consent
4 old Human consent reused for new decision
5 Human accepts A but A-prime becomes operative
6 AI changes parameters after Human acceptance
7 AI expands scope after Human acceptance
8 Human accepts general direction but AI attributes specific parameters
9 AI creates artifact that merely looks like Human decision
10 AI-filled value recorded as Human-chosen
```

The real current Phase-6 `cmd_approve` counterexample and both direct legacy acceptance routes remain mandatory real-boundary regressions.

## 48. Request/review/transport negative suite

At minimum:

```text
caller request-path substitution
wrong filename/request/head-ref digest
wrong PR base/ref/head repository
wrong request-commit parent
extra/renamed/deleted request path
malformed/extra-field V5 request
request digest/ID mismatch
attempted request self-reference
candidate/impact/canonical/preview/effect drift
V4 request/review substitution
no review
wrong Human actor
wrong review commit
malformed four-line V5 body
invalid rationale
COMMENTED only
DISMISSED only
unknown review state
duplicate numeric/node review ID
incomplete pagination
API error/rate limit
redirect
alternate API origin
proxy/CA override
authenticated fallback attempt
GitHub credential-bearing effect environment
```

All deny before CAS where applicable.

## 49. Replay/concurrency/final-currentness negative suite

At minimum:

```text
same request replay
same-worktree concurrent invocation
stale lock
raw local ref/HEAD drift
old Human decision with changed operation
review dismissed after preliminary admission
CHANGES_REQUESTED after preliminary admission
PR closed/merged/head drift after admission
remote final reread failure
candidate/impact/canonical/preview/effect drift after admission
request consumed after admission
executor substitution after final gate
replacement-ref insertion after admission
partial/promisor marker insertion after admission
out-of-scope path in prepared raw tree
second decision-log record
malformed existing local decision-log line
raw commit extra header
raw commit second parent
raw commit altered message bytes
raw commit wrong timestamp/offset
raw commit SHA mismatch vs independent SHA-1
```

## 50. Bounded trusted-origin claim

For this exact X1B profile only:

```text
manual Human APPROVE governance act by litrgratis-pixel
+
exact authoritative public GitHub review record
+
effect process unable to create/edit Human review evidence
+
credential-free exact-origin evidence acquisition
+
exact V5 request/PR/review/currentness/effect/ref binding
+
independent admission
+
fresh FinalEffectGateV5
+
NO_REPLACE + NO_LAZY_FETCH raw SHA-1 semantics
+
COMPLETE_LOCAL_OBJECT_STORE_V1
+
closed exact raw commit object
+
CAS-first refs/heads/main commitment
+
post-CAS alias-safe worktree/index materialization
=
bounded trusted Human decision effect
```

No claim is made that GitHub review metadata by itself proves Human private mental state.

## 51. Implementation responsibility split

`phase6/scriptops-v2-hardening.py`:

```text
expose only approve --decision-pr current acceptance interface
reject defect-era approve --scene/--why
obtain validated V5 admission
execute only exact V5 final-gated effect
never invent Human attribution
distinguish pre-commit failure from committed-recovery state
```

`legacy/scriptops-v2-single.py`:

```text
preserve non-approval substrate
disable direct approve
disable direct scene-promote -> accepted at parser and command layers
```

`phase6/x1b_human_decision.py`:

```text
V5 schemas/canonical JSON
pure accepted preview helper
non-circular request identity
public GitHub transport
PR/review pagination/currentness
CompleteReviewSetV5
freshness/supersession policy
admission/replay/lock
refs/heads/main raw checks
FinalEffectGateV5
system-Git isolation
NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2 helpers
COMPLETE_LOCAL_OBJECT_STORE_V1 detector/checker
raw commit-content/SHA-1 helpers
CLOSED_RAW_COMMIT_OBJECT_V1 writer/parser/verifier
private temporary-index exact tree helpers
CAS-first commitment helper
alias-safe post-CAS target materialization helpers
outcome-state classifier
post-effect/recovery-required helpers
```

Restore/verifier/docs/tests/workflow responsibilities remain as frozen above.

## 52. Independent implementation-review obligations

Later independent implementation review must inspect the complete candidate tree and prove, not infer:

```text
changed-file set within authorized surface
no third acceptance route
old Phase-6 and legacy routes deny
restore/verifier/docs coherent
V5 request identity acyclic
V5 schemas internally exact
one-file decision PR enforced
public transport credential-free/exact-origin
review set/currentness/conflicts complete
freshness/supersession matches R4R5
admission does not mutate canon
lock/replay claim bounded honestly
refs/heads/main exact effect ref
all authority Git reads are no-replace/no-lazy
partial/promisor/alternate object stores rejected
GIT_NO_LAZY_FETCH=1 cannot be caller-disabled
missing object fails locally without network
refs/replace state rejected at frozen checkpoints
raw base tree derived from raw base commit bytes
output blobs independently SHA-1 checked
new tree exact two-path delta from raw parent tree
raw commit content independently constructed
raw commit SHA-1 independently computed
commit object written without commit-tree
raw commit read-back byte-identical
closed header set contains no encoding/signature/extra parent
no canonical filesystem or real-index mutation before CAS
no canonical COMMITTED record before CAS
CAS old-value equality is success commitment point
pre-CAS failure leaves canonical state unchanged
post-CAS failure classified COMMITTED_RECOVERY_REQUIRED
no silent ref rollback after successful CAS
post-CAS materialization alias-safe and exact
result raw commit exact two-path one-parent effect
Human attribution only from validated evidence
no self-hash/circular evidence
```

```text
TESTS GREEN != IMPLEMENTATION REVIEW PASS
IMPLEMENTATION REVIEW PASS != X1B CLOSED
```

## 53. Separately authorized live positive control

A later positive control requires fresh Human authorization and exactly one disposable ScriptOps repository execution instance with no user screenplay canon.

It must include:

```text
inert/synthetic scene
exact staged candidate
exact impact report
one HumanDecisionRequestV5
one dedicated one-file decision PR
one manual GitHub UI APPROVE by litrgratis-pixel
exact four-line V5 review body
one corrected Phase-6 approve --decision-pr invocation
local HEAD symbolically on refs/heads/main
zero refs/replace/*
non-shallow/no-graft repository
COMPLETE_LOCAL_OBJECT_STORE_V1
no partial/promisor/alternate object store
no GitHub review-write credential in effect process
```

Human must see exact candidate/content/scope and material effect including:

```text
canonical before/after hash
canonical local ref refs/heads/main
decision-log target + one V5 COMMITTED append
exact two-path one-parent local effect commit
logical commit message
NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2
COMPLETE_LOCAL_OBJECT_STORE_V1
CLOSED_RAW_COMMIT_OBJECT_V1
REFS_HEADS_MAIN_CAS_COMMITMENT_V1
REF_CAS_FIRST_ALIAS_SAFE_GIT_PLUMBING_V3
SINGLE_LINK_ALIAS_SAFE_REPOSITORY_TARGETS_V1
```

Positive result requires exact post-effect raw truth and Human-evidence-derived attribution.

A separately authorized fault-injection control should also demonstrate an after-CAS materialization failure and prove truthful `COMMITTED_RECOVERY_REQUIRED` classification without history rewrite or duplicate record.

```text
LIVE POSITIVE CONTROL PASS != CORRECTIVE CLOSURE
```

## 54. Corrective closure composition

X1B cannot be closed by brief review, implementation, green CI or positive control alone.

Minimum later closure remains:

```text
accepted corrective design
+
independent design review
+
bounded implementation authority
+
exact implementation candidate
+
independent implementation review
+
fresh preregistered corrective verification
+
all required negative controls
+
separately authorized real Human positive control
+
exact post-effect raw truth
+
independent corrective-closure review
+
final Human corrective-closure acceptance
+
durable final evidence freeze
```

Preserve:

```text
GREEN TESTS != CORRECTIVE CLOSURE
IMPLEMENTATION REVIEW PASS != CORRECTIVE CLOSURE
LIVE POSITIVE CONTROL PASS != CORRECTIVE CLOSURE
TECHNICAL VERIFICATION PASS != HUMAN CLOSURE ACCEPTANCE
X1B CLOSED != V1 AUTHORITY
```

## 55. Successor-review adversarial checklist

The independent R4R5 brief review must explicitly attack at least:

```text
Can any partial/promisor repository trigger implicit fetch under an authority-critical command?
Can caller GIT_NO_LAZY_FETCH=0 or local config defeat the frozen no-lazy profile?
Can a missing promised tree/blob cause network I/O after FinalEffectGateV5?
Can repository object alternates bypass the complete-local-store claim?
Can any authority helper omit --no-lazy-fetch or --no-replace-objects?
Can replacement refs reinterpret a Human-bound SHA/tree?
Can local graft/shallow semantics alter the raw parent relationship?
Can i18n.commitEncoding or another config add commit headers?
Can any canonical filesystem target or real index mutate before CAS?
Can a pre-CAS failure leave a canonical Human-attributed COMMITTED/SUCCESS record?
Can an unreferenced prepared object be mistaken for canonical success?
Does successful CAS atomically make the exact two-path effect commit canonical?
Can post-CAS failure be misreported as no effect or complete success?
Can post-CAS recovery silently rewrite/reforge Human history?
Can V4 Human evidence be reused after V5 effect-profile change?
Can side/detached refs or hardlink/symlink targets become operative?
Is any core security/authority choice still left to implementer?
```

Any credible counterexample freezes a finding and returns `NOT PASS`.

## 56. Explicit non-authority

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

R4R5 review PASS, if later obtained, would establish only that this implementation brief is acceptable for a separately Human-authorized implementation stage.

## 57. STOP

Required next stage after durable R4R5 freeze:

```text
INDEPENDENT AK-CANON X1B R4R5 IMPLEMENTATION-BRIEF REVIEW
```

Only fresh separate Human authorization may create that review artifact.

```text
R4R5 BRIEF != IMPLEMENTATION AUTHORITY
R4R5 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R5 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
STOP
```
