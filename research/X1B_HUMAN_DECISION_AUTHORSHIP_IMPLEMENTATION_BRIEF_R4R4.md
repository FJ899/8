# X1B HUMAN DECISION AUTHORSHIP — CLEAN IMPLEMENTATION BRIEF R4R4

Status: `CLEAN R4R4 CORRECTIVE BRIEF / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-01`

## 1. Authority, purpose, and STOP boundary

This document is the self-contained successor to R4R3 after independent AK-CANON review PR #121 returned `NOT PASS`.

It preserves the accepted X1B corrective design and every R4R3 property not rejected by PR #121, while correcting exactly the two residual Git-isolation blockers frozen by that review:

1. authority-critical Git object/revision semantics must be raw and replacement-object-free, so `refs/replace/*` cannot reinterpret the exact Human-bound parent SHA/tree;
2. the durable effect commit must be a closed exact raw commit object whose bytes cannot be altered by repository-local `i18n.commitEncoding` or any other ambient commit-header configuration.

This document is an implementation brief only. It authorizes no ScriptOps implementation, no Human decision PR/review, no live positive control, no canonical screenplay effect, no merge, no X1B closure, no Agency Kernel v1, no release, deployment, or tag.

```text
R4R4 BRIEF != IMPLEMENTATION AUTHORITY
R4R4 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R4 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

After durable freeze of this brief, STOP. The next stage is a separately Human-authorized independent AK-CANON R4R4 implementation-brief review.

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

### 2.3 R4R3 predecessor

```text
FJ899/8 PR #120
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = df095fc822f6b454bc69e24e727c9b9dcfe64844
TREE = ad625ba054ba0c38d3dfd1baf3b7980753c553a2
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R3.md
BLOB = 17521e2f3616bdc356c4dca4c13c96fcd5114117
```

### 2.4 Binding R4R3 NOT-PASS review

```text
FJ899/8 PR #121
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 4c2f553b5caa82684ab01ad9ff4dc426c25f4821
TREE = 88724b607d497c72bfdf7b46a68ec0e10e09fabc
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R3_AK_CANON_REVIEW.md
BLOB = 113cd77025d9f57261417300be01d98507f90a0a
VERDICT = AK-CANON X1B R4R3 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

R4R4 directly addresses:

```text
X1B-R4R3-IBR-F001 — replacement-ref / raw-object substitution
X1B-R4R3-IBR-F002 — local commit-encoding config / extra commit header
```

PR #121 also recorded that the following predecessor findings were addressed at brief level and are preserved here:

```text
R4R2 IBR F001 LOCAL EFFECT REF = ADDRESSED
R4R2 IBR F003 HARDLINK / WRITE-TARGET ALIAS = ADDRESSED
R4R2 IBR F004 FRESHNESS / SUPERSESSION = ADDRESSED
```

`REVIEW FINDING != REPAIR AUTHORITY`; this correction exists only under the fresh Human authorization for R4R4 brief preparation.

## 3. Exact evidence-repository base

```text
FJ899/8 main
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

The earlier unauthorized R4-main write and forward recovery remain visible in history. No history rewrite is part of R4R4.

## 4. Frozen ScriptOps baseline

```text
FJ899/scriptops main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Security-relevant baseline BLOBs remain frozen as reviewed in R4R3:

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

## 5. Normative precedence and V4 migration

```text
R4R4 TEXT = CURRENT IMPLEMENTATION-BRIEF AUTHORITY
R4R3 / R4R2 / R4R1 / R4 / R3 / R2 / R1 = HISTORICAL INPUT ONLY
CORRECTIVE DESIGN PR #34 = HIGHER-LEVEL PROPERTY CONTRACT
```

No authority/security rule depends on implicit inheritance. R4R4 restates the current contract.

Because R4R4 changes the Human-presented material Git effect profile, all authority-critical request/evidence/admission/gate/record schemas are bumped from V3 to V4.

```text
V3 REQUEST/REVIEW/ADMISSION/GATE != R4R4 AUTHORITY
V3 HUMAN REVIEW MARKER != V4 HUMAN DECISION
V4 EFFECT PROFILE REQUIRES FRESH V4 HUMAN-BOUND REQUEST
```

No hypothetical V3 request/review may be reused for a V4 effect.

## 6. Future bounded implementation surface

Expected implementation surface:

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

A smaller final changed set is permitted only if independent implementation review proves every R4R4 obligation satisfied. Any additional tracked path requires STOP and fresh Human authorization before mutation.

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

No caller-controlled field may supply Human actor/result/rationale, request path/digest, task/scene/candidate/impact identities, canonical target/ref, effect type, material effect, Git ref, raw-object profile, commit-object profile, or effect commit metadata.

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

Required real regressions begin with a real staged candidate and prove nonzero exit plus no canonical scene, accepted transition, decision-log mutation, Human attribution, index mutation, `refs/heads/main` mutation or commit.

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

Repository verification must separately prove historical reconstruction and current active-runtime authority. It must not treat prototype byte identity or old `approve --why` semantics as current authority.

`README.md`, `PROJECT_STATE.md`, `HANDOFF.md`, `sources/prototype/RESTORE.md`, and `SOURCE_MANIFEST.md` must state at minimum:

```text
defect-era approve --why = historical provenance only
current Human-decision route = approve --decision-pr <N> only
direct legacy approve = disabled
direct legacy scene-promote --to accepted = disabled
canonical local effect ref = refs/heads/main only
raw Git object profile = NO_REPLACE_RAW_SHA1_OBJECTS_V1
commit object profile = CLOSED_RAW_COMMIT_OBJECT_V1
historical prototype byte identity != current active runtime identity
historical prototype parts != current active runtime authority
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
FinalEffectGateV4.observed_at
```

GitHub `submitted_at` used by R4R4 must validate exactly to this UTC `Z` form; otherwise DENY rather than normalize.

For the raw effect commit only:

```text
request_created_epoch = exact signed decimal Unix seconds corresponding to request_created_at UTC
```

Conversion must be deterministic and range-checked. The raw Git author/committer timestamp field is exactly:

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

Admission, FinalEffectGateV4 and effect preparation must re-render and prove exact byte/hash equality.

## 14. R4R4 platform profile

The local effect remains bounded to a platform providing equivalent semantics for:

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
hash-object -w --stdin --no-filters
hash-object -w -t commit --stdin
cat-file of exact raw objects
read-tree
update-index --cacheinfo
write-tree
ls-tree
update-ref with exact old value
```

Object format must be SHA-1. If equivalent guarantees are unavailable, acceptance returns `BLOCKED` before canonical mutation.

## 15. PresentedMaterialEffectV4

Closed schema:

```text
PresentedMaterialEffectV4 = {
  "schema_version": "scriptops-x1b-presented-material-effect/v4",
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
    "record_schema_version": "scriptops-x1b-decision-record/v4",
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
    "raw_object_profile": "NO_REPLACE_RAW_SHA1_OBJECTS_V1",
    "commit_object_profile": "CLOSED_RAW_COMMIT_OBJECT_V1",
    "effect_transport_profile": "RAW_OBJECT_ALIAS_SAFE_GIT_PLUMBING_V2",
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
presented_material_effect_digest = sha256_canonical(PresentedMaterialEffectV4)
```

## 16. HumanDecisionRequestBindingV4 — acyclic request identity

```text
HumanDecisionRequestBindingV4 = {
  "schema_version": "scriptops-x1b-human-decision-request/v4",
  "repository": "FJ899/scriptops",
  "repository_head_at_request": <40 lowercase hex>,
  "repository_ref_at_request": "refs/heads/main",
  "request_created_at": <exact R4R4 timestamp>,
  "task_id": <exact task ID>,
  "scene_id": <exact scene ID>,
  "candidate_path": <exact repo-relative candidate path>,
  "candidate_file_sha256": <64 lowercase hex>,
  "impact_report_path": <exact repo-relative impact path>,
  "impact_report_sha256": <64 lowercase hex>,
  "canonical_target": "scenes/<scene_id>.fountain",
  "canonical_ref": "refs/heads/main",
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect": <PresentedMaterialEffectV4>
}
```

Construction order:

```text
1 validate raw refs/heads/main and request base under NO_REPLACE profile
2 validate candidate/impact/canonical pre-state
3 render accepted preview bytes/hash
4 construct PresentedMaterialEffectV4
5 construct HumanDecisionRequestBindingV4
6 request_binding_json = canonical_json_bytes(binding)
7 request_digest = sha256_hex_bytes(request_binding_json)
8 decision_request_id = "x1b:" + request_digest
9 construct committed HumanDecisionRequestV4
```

```text
HumanDecisionRequestV4 = {
  <all HumanDecisionRequestBindingV4 fields>,
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

Request bytes are exactly `canonical_json_bytes(HumanDecisionRequestV4)` with no trailing LF.

Proposal commit:

```text
branch = decision/x1b/<request_digest>
parent = repository_head_at_request
changed-file set = exactly one added request_path
request blob = exact committed HumanDecisionRequestV4 bytes
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

## 19. Human authority profile and exact V4 Human review body

Authoritative Human actor for this bounded profile:

```text
litrgratis-pixel
```

A later positive control requires a manual Human GitHub UI `APPROVE` governance act by this actor.

Exact review body is four LF-separated lines with no trailing LF:

```text
X1B-HUMAN-DECISION-V4
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
body = exact four-line V4 body
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

Non-empty proxy/CA/GitHub credential overrides, including at minimum:

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

cause DENY before evidence acquisition.

Redirect, alternate origin, rate limit, visibility change, malformed/incomplete response or ambiguity => DENY/BLOCKED before effect.

## 21. Exact GitHub reads, pagination, and CompleteReviewSetV4

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
NormalizedReviewV4 = {
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
CompleteReviewSetV4 = {
  "schema_version": "scriptops-x1b-complete-review-set/v4",
  "repository": "FJ899/scriptops",
  "decision_pr_number": <positive integer>,
  "decision_pr_head": <40 lowercase hex>,
  "reviews": [<all normalized reviews in normative order>]
}
```

```text
complete_review_set_digest = sha256_canonical(CompleteReviewSetV4)
```

For `litrgratis-pixel` on exact current PR HEAD there must be exactly one active syntactically/semantically valid V4 APPROVED and no active CHANGES_REQUESTED. Second current-head APPROVED => ambiguous DENY. Old-commit APPROVED => historical only. No latest-wins chronology rule.

## 22. Candidate, impact, local Git-tree, and applicability checks

Before preliminary admission and again at FinalEffectGateV4 where applicable:

```text
logical repository identity = FJ899/scriptops
repository_ref_at_request = refs/heads/main
HEAD symbolic ref = refs/heads/main
raw HEAD SHA = raw refs/heads/main SHA = request.repository_head_at_request
Git object format = sha1
NO_REPLACE_RAW_SHA1_OBJECTS_V1 satisfied
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
PresentedMaterialEffectV4 object/digest match request
request unconsumed in this canonical local instance
```

If an effect target is absent from the raw parent tree, filesystem path must also be absent before effect. If present, filesystem bytes and raw Git blob/mode must agree with validated pre-state. Ignored/untracked substitute at an effect path is DENY.

Candidate source is preserved and final Git effect may not alter/remove it.

## 23. Explicit activation, age, deactivation, multiple decisions, supersession

A selected decision is active only while all exact PR/request/review/local-ref/raw-object/applicability predicates remain true.

Age policy remains deliberately:

```text
NO WALL-CLOCK TTL
AGE ALONE != STALE
```

Selected decision becomes inactive/inapplicable upon PR close/merge, identity drift, approval dismissal, active authoritative CHANGES_REQUESTED, ambiguity/conflict, incomplete evidence, raw local ref mismatch, raw-object-profile failure, candidate/impact/canonical/preview/effect drift, or same-instance consumption.

Each decision PR is a separate Human decision domain. Another approved decision PR does not implicitly supersede, revoke or chronology-win over the selected PR.

Two separately Human-approved same-base requests may coexist. The first successful local effect that atomically advances `refs/heads/main` makes every still-unconsumed old-base request inapplicable by exact raw ref/base mismatch.

```text
NO CHRONOLOGY-ONLY WINNER
OLD CONSENT + CHANGED OPERATION = DENY
NO GLOBAL CROSS-CLONE EXACTLY-ONCE CLAIM
```

## 24. HumanDecisionAdmissionIdentityV4

```text
HumanDecisionAdmissionIdentityV4 = {
  "schema_version": "scriptops-x1b-human-decision-admission/v4",
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
  "raw_object_profile": "NO_REPLACE_RAW_SHA1_OBJECTS_V1",
  "commit_object_profile": "CLOSED_RAW_COMMIT_OBJECT_V1",
  "canonical_instance_scope": "LOCAL_REFS_HEADS_MAIN_WORKTREE_DECISION_LOG_V4"
}
```

```text
admission_id = "x1b-admit:" + sha256_canonical(HumanDecisionAdmissionIdentityV4)
```

Admission is in-memory one-shot machine state, not Human evidence or execution credential. Preliminary admission cannot mutate canonical scene, decision log, real index or `refs/heads/main`.

## 25. Bounded replay and same-worktree lock

Bounded claim:

```text
one decision_request_id may cause at most one successful X1B acceptance effect
within one canonical local refs/heads/main worktree execution instance
```

Complete local `.scriptops/decision-log.ndjson` must contain no prior object carrying exact `decision_request_id`. Malformed non-empty line => DENY.

Worktree-specific lock:

```text
<worktree-specific git-dir>/scriptops-x1b-approve.lock
```

Create exclusively before admission. Existing lock => DENY/BLOCKED. No automatic stale-lock deletion. Hold through post-effect verification/cleanup.

A second independent clone is a separate canonical execution instance.

## 26. Exact local canonical Git ref

The only operative local effect ref is:

```text
refs/heads/main
```

At request creation, admission and FinalEffectGateV4:

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

## 27. FinalEffectGateV4

Immediately before first canonical filesystem mutation, while lock is held, freshly reread PR metadata and complete reviews through trusted public transport.

Revalidate:

```text
exact PR/request envelope
selected Human review/currentness/conflicts
CompleteReviewSetV4 digest
repository logical identity
raw symbolic/ref identity = refs/heads/main + exact request SHA
NO_REPLACE_RAW_SHA1_OBJECTS_V1
no refs/replace/*
raw request-base commit/tree identity
candidate/impact/canonical pre-state
accepted preview
PresentedMaterialEffectV4
replay state
real-index tree = raw parent tree
file-identity target preconditions
Git executable/platform preconditions
```

```text
FinalEffectGateV4 = {
  "schema_version": "scriptops-x1b-final-effect-gate/v4",
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
  "raw_object_profile": "NO_REPLACE_RAW_SHA1_OBJECTS_V1",
  "commit_object_profile": "CLOSED_RAW_COMMIT_OBJECT_V1",
  "canonical_instance_scope": "LOCAL_REFS_HEADS_MAIN_WORKTREE_DECISION_LOG_V4",
  "current_human_decision_valid": true,
  "observed_at": <exact R4R4 UTC timestamp>
}
```

```text
final_effect_gate_digest = sha256_canonical(FinalEffectGateV4)
```

Gate is in-memory one-shot state and not a reusable credential.

## 28. Human-currentness commitment point

```text
Human-currentness commitment point
=
successful FinalEffectGateV4 validation
immediately before first canonical filesystem mutation
```

Before it, visible review/PR/ref/raw-object/applicability drift revokes or conflicts with admission.

After it, later remote change does not retroactively revoke the already-authorized same-process one-shot effect; no distributed atomicity claim is made.

Between gate and first canonical mutation:

```text
no user interaction
no network
no sleep/wait
no unrelated blocking operation
no proposal/review mutation
no untrusted subprocess
```

Only precomputed local effect preparation using the validated runtime may proceed.

## 29. Exact X1BDecisionRecordV4 before mutation

Before first filesystem mutation compute exact accepted scene bytes and one exact canonical decision record.

```text
X1BDecisionRecordV4 = {
  "schema_version": "scriptops-x1b-decision-record/v4",
  "result": "SUCCESS",
  "decision_type": "scene_accepted",
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
  "raw_object_profile": "NO_REPLACE_RAW_SHA1_OBJECTS_V1",
  "commit_object_profile": "CLOSED_RAW_COMMIT_OBJECT_V1",
  "canonical_instance_scope": "LOCAL_REFS_HEADS_MAIN_WORKTREE_DECISION_LOG_V4"
}
```

NDJSON append bytes:

```text
canonical_json_bytes(X1BDecisionRecordV4) + exactly one LF
```

Effect commit SHA remains absent from this record to avoid a self-hash cycle. Existing non-empty decision log not ending in LF => DENY before mutation.

## 30. System Git executable and subprocess profile

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
GIT_CONFIG_NOSYSTEM=1
GIT_CONFIG_SYSTEM=/dev/null
GIT_CONFIG_GLOBAL=/dev/null
GIT_TERMINAL_PROMPT=0
GCM_INTERACTIVE=never
```

and invokes global option:

```text
--no-replace-objects
```

immediately after the Git executable and before the subcommand.

Command-level config at minimum:

```text
-c core.hooksPath=/dev/null
-c core.fsmonitor=false
-c commit.gpgSign=false
-c credential.helper=
```

Remove caller values for all `GIT_CONFIG_*`, `GIT_DIR`, `GIT_WORK_TREE`, `GIT_COMMON_DIR`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_EXEC_PATH`, `GIT_EXTERNAL_DIFF`, `GIT_ASKPASS`, `SSH_ASKPASS`, `GIT_SSH`, `GIT_SSH_COMMAND`, `GIT_REPLACE_REF_BASE`, loader-injection variables and other caller `GIT_*` overrides unless R4R4 explicitly constructs a bounded replacement for a specific subprocess.

No acceptance Git subprocess may be a network operation.

## 31. R4R4 correction F001 — NO_REPLACE_RAW_SHA1_OBJECTS_V1

Replacement-object semantics are forbidden, not merely ignored opportunistically.

At request creation, preliminary admission, FinalEffectGateV4, immediately before raw effect-object construction, immediately before ref CAS, and post-effect verification:

```text
git --no-replace-objects for-each-ref --format=<exact refname format> refs/replace/
```

must enumerate zero refs. Any `refs/replace/*` => DENY/BLOCKED before successful Human-attributed effect.

Every authority-critical Git command also runs with both:

```text
GIT_NO_REPLACE_OBJECTS=1
git --no-replace-objects <subcommand> ...
```

No command may rely on default replacement behavior.

Raw request-base commit identity is established from exact object bytes, not replace-aware revision interpretation:

```text
raw_base = request.repository_head_at_request
object type(raw_base) = commit
raw_base_content = exact bytes from no-replace cat-file commit raw_base
raw_base tree header = exactly one 40-hex tree ID
raw_base parent headers are parsed only as raw content when needed
no encoding/replacement interpretation may alter raw_base_content
```

The exact parent tree used for all effect comparison is:

```text
raw_parent_tree = tree header parsed from raw_base_content
```

The implementation may additionally cross-check:

```text
git --no-replace-objects rev-parse <raw_base>^{tree} == raw_parent_tree
```

but raw commit content is the authority.

All authority-critical operations that inspect commits/trees/diffs use no-replace semantics, including equivalents of:

```text
cat-file
rev-parse
ls-tree
read-tree
write-tree
diff-tree
show / log if used at all
post-effect parent/tree verification
```

No replace-aware command output may be used as an authority fact.

Defense-in-depth repository-history ambiguity checks:

```text
repository must not be shallow
legacy .git/info/grafts or worktree-equivalent graft source must be absent
```

If implementation cannot prove these conditions for the canonical worktree/git-dir topology, return BLOCKED.

Mandatory regression:

```text
request base H = exact refs/heads/main
create replacement commit R with same relevant target state but unrelated third-path delta
install refs/replace/H -> R
attempt approval
=> DENY/BLOCKED before canonical mutation
```

A second direct unit-level regression must prove raw/no-replace parent tree remains the original H tree regardless of installed replacement ref.

## 32. R4R4 correction F002 — CLOSED_RAW_COMMIT_OBJECT_V1

R4R4 does not use `git commit-tree` to create the operative effect commit.

Repository-local `i18n.commitEncoding`, signing settings, templates, cleanup settings, hooks or other commit-construction configuration therefore cannot choose commit headers/message representation.

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

There are exactly four headers, in exactly this order:

```text
tree
parent
author
committer
```

Forbidden headers include, without limitation:

```text
encoding
gpgsig
gpgsig-sha256
mergetag
extra parent
any unknown/duplicate header
```

The logical message has exactly one terminating LF in the raw commit object and no additional bytes.

Before writing the object, compute independently in Python or equivalent trusted in-process SHA-1:

```text
expected_effect_commit_sha1 =
SHA1(
  ASCII("commit ")
  + ASCII(decimal byte length of raw_commit_content)
  + NUL
  + raw_commit_content
)
```

Then write exactly the prepared content with plumbing equivalent to:

```text
git --no-replace-objects hash-object -w -t commit --stdin
```

The returned object ID MUST equal `expected_effect_commit_sha1`.

Immediately read the exact object back under no-replace semantics:

```text
git --no-replace-objects cat-file commit <expected_effect_commit_sha1>
```

and prove byte-for-byte equality with `raw_commit_content`.

Also parse the returned raw bytes with a closed parser and independently prove:

```text
exact four-header order
exact tree T
exact one parent P
exact author identity + E +0000
exact committer identity + E +0000
no encoding header
no signature header
no extra header
exact UTF-8 message bytes + one LF
```

Any mismatch => DENY before filesystem/index/ref mutation.

Repository-local `i18n.commitEncoding` may be present, but it is not allowed to affect the raw object. A regression must set it to a non-UTF-8 value and prove the produced/prepared raw object remains exactly closed with no `encoding` header; alternatively implementation may choose to DENY on presence, but it may not silently allow a changed commit object.

## 33. Exact output blobs and temporary index

Before modifying real index:

```text
real_index_tree = no-replace git write-tree
raw_parent_tree = parsed raw base tree
real_index_tree == raw_parent_tree
```

Compute exact output blobs:

```text
accepted_scene_blob = git --no-replace-objects hash-object -w --stdin --no-filters
  over exact accepted canonical bytes

decision_log_blob = git --no-replace-objects hash-object -w --stdin --no-filters
  over exact post-append decision-log bytes
```

Read each object back and prove exact bytes. Independently compute SHA-1 object IDs from `blob <len>\0<bytes>` and require equality with Git output.

Create a fresh private temporary index inside worktree-specific Git directory with exclusive creation/mode 0600. Set `GIT_INDEX_FILE` only for temporary-index commands.

Initialize from exact `raw_parent_tree`:

```text
read-tree <raw_parent_tree>
```

Update exactly:

```text
update-index --add --cacheinfo 100644,<accepted_scene_blob>,scenes/<scene_id>.fountain
update-index --add --cacheinfo 100644,<decision_log_blob>,.scriptops/decision-log.ndjson
```

Then:

```text
new_tree = write-tree
```

Prove under no-replace/raw semantics:

```text
new_tree differs from raw_parent_tree only at exact two paths
ls-tree(new_tree, exact paths) = mode 100644 + expected blob IDs
no candidate/request/impact/third path changed
```

Only after this proof may CLOSED_RAW_COMMIT_OBJECT_V1 construct the exact effect commit.

## 34. Repository-contained parent directories and alias-safe targets

Both parents must already exist:

```text
scenes/
.scriptops/
```

Every parent-chain component used by an effect target must be repository-contained, real directory, non-symlink, opened via protected descriptor/equivalent, contain no lexical `..` escape and resolve nowhere outside repository.

Existing effect target:

```text
lstat => regular file
not symlink
st_nlink == 1
bytes match validated pre-state/raw parent blob
open O_NOFOLLOW/equivalent
fstat identity == validated st_dev + st_ino
still regular + st_nlink == 1
```

Never truncate/write validated existing inode in place. Write a fresh same-directory exclusive no-follow temporary inode, fsync, require single link/mode 0644, revalidate old inode, atomically replace through protected directory descriptor, fsync directory, reopen new target no-follow and prove exact bytes/hash/single link.

Absent target must use verified parent descriptor and exclusive no-follow creation. Existence race, symlink, hardlink count >1, nonregular target, parent substitution or ambiguous identity => DENY/BLOCKED.

Mandatory negatives preserve canonical/decision-log hardlink aliases, symlinks, inode substitution, absence race, parent substitution and unsupported platform primitives.

## 35. Exact local effect sequence

After FinalEffectGateV4 success, with lock held and all authority bytes precomputed:

```text
A. prove NO_REPLACE_RAW_SHA1_OBJECTS_V1 again and raw parent tree exact

B. construct/verify exact output blobs + temporary-index new_tree
   with no worktree, real-index or refs/heads/main mutation

C. construct exact CLOSED_RAW_COMMIT_OBJECT_V1 content
   compute expected SHA-1 independently
   write raw commit with hash-object -t commit
   read back raw bytes and prove exact equality

D. recheck zero refs/replace/* and raw refs/heads/main/HEAD still exact request base

E. materialize exact accepted scene bytes through alias-safe target helper

F. materialize exact post-append decision-log bytes through alias-safe target helper

G. verify both filesystem targets exact and single-link

H. update real index to exact verified new_tree using hook-disabled no-replace plumbing read-tree
   without -u / without worktree filtering

I. prove real index write-tree == exact new_tree

J. recheck zero refs/replace/* and raw old ref exact

K. atomically compare-and-swap:
   refs/heads/main: exact request base -> exact prepared raw effect commit SHA
   using update-ref with exact old value

L. verify raw HEAD/ref == exact effect commit

M. verify raw commit bytes/header schema/tree/one-parent and exact raw changed set

N. verify exact clean worktree/index state and target bytes
```

No `git add .`, no porcelain commit, no `commit-tree`, no replace-aware authority read.

## 36. Index/ref rollback boundary

Before successful `refs/heads/main` CAS, the effect is not successful.

Failure after filesystem/index mutation but before successful ref update:

```text
return nonzero
attempt deterministic restoration of exact pre-effect target presence/bytes/mode
restore real index to exact raw parent tree through hook-disabled no-replace plumbing
prove raw refs/heads/main still exact parent
prove working tree/index exact pre-effect state
never emit SUCCESS Human attribution
```

If restoration cannot be proven, leave explicit fail-closed dirty/error state and report BLOCKED; do not synthesize Human success evidence or destructively reset unrelated state.

If ref update succeeds but post-commit verification fails, do not silently reset/rewrite history. Preserve ref/commit for forensic truth, report BLOCKED and require separately authorized recovery.

## 37. Post-effect truth

Successful effect requires all:

```text
raw HEAD == raw refs/heads/main == exact expected raw effect commit SHA
zero refs/replace/*
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
exactly one new X1BDecisionRecordV4 line
record request/admission/gate/review/effect/ref/profile identities exact
worktree/index clean relative to resulting raw HEAD
real index write-tree = resulting raw HEAD tree
lock held until verification completes
```

No replace-aware result can satisfy post-effect truth.

```text
GREEN COMMAND EXIT != POST-EFFECT TRUTH
```

## 38. Git hook/filter/config attack regressions

Mandatory injections include, individually and in meaningful combinations:

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

Tests prove injection is rejected before effect or cannot execute/transform the bounded effect. Sentinel hooks/filters/helpers must not execute. Exact raw blob/tree/commit/ref identities remain exact.

For `i18n.commitEncoding`, the resulting raw effect commit must contain no `encoding` header and must equal the independently precomputed CLOSED_RAW_COMMIT_OBJECT_V1 bytes.

## 39. Raw-object / replacement-ref regressions

Mandatory negatives:

```text
refs/replace/<request-base> -> alternate commit with unrelated third-path delta
replacement ref introduced before admission
replacement ref introduced after admission but before FinalEffectGateV4
replacement ref introduced after FinalEffectGateV4 but before pre-CAS recheck
nonempty refs/replace namespace unrelated to request base
caller GIT_REPLACE_REF_BASE injection
replace-aware Git command accidentally used in authority helper
shallow repository
graft source present
```

All fail closed before successful Human-attributed effect.

Mandatory positive unit proof:

```text
raw no-replace cat-file of exact SHA returns original exact object bytes
regardless of installed replacement ref
```

No test may accept replace-aware changed-set proof as authority.

## 40. Ref-binding regressions

Mandatory negatives preserve:

```text
side branch at exact request SHA
detached HEAD at exact request SHA
HEAD symbolic ref not main
main moved after admission
main moved after FinalEffectGateV4 but before update-ref
CAS old-SHA mismatch
prepared raw commit parent wrong
prepared tree targets another ref
```

All fail closed without successful Human-attributed effect.

## 41. Freshness/supersession regressions

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
first same-base successful effect advances main -> second old-base request DENY
changed candidate/effect/profile with old Human review -> DENY
V3 review marker/request -> DENY for V4 effect
```

## 42. Original X1B preregistered attacks remain mandatory

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

## 43. Request/review/transport negative suite

At minimum:

```text
caller request-path substitution
wrong filename/request/head-ref digest
wrong PR base/ref/head repository
wrong request-commit parent
extra/renamed/deleted request path
malformed/extra-field V4 request
request digest/ID mismatch
attempted request self-reference
candidate/impact/canonical/preview/effect drift
V3 request/review substitution
no review
wrong Human actor
wrong review commit
malformed four-line V4 body
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

All deny before canonical effect where applicable.

## 44. Replay/concurrency/final-currentness negative suite

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
out-of-scope path in prepared raw tree
second decision-log append
malformed existing local decision-log line
raw commit extra header
raw commit second parent
raw commit altered message bytes
raw commit wrong timestamp/offset
raw commit SHA mismatch vs independent SHA-1
```

## 45. Bounded trusted-origin claim

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
exact V4 request/PR/review/currentness/effect/ref binding
+
independent admission
+
fresh FinalEffectGateV4
+
NO_REPLACE raw SHA-1 Git object semantics
+
closed exact raw commit object
+
hook/filter-safe alias-safe exact refs/heads/main effect
=
bounded trusted Human decision evidence
```

No claim is made that GitHub review metadata by itself proves Human private mental state.

## 46. Implementation responsibility split

`phase6/scriptops-v2-hardening.py`:

```text
expose only approve --decision-pr current acceptance interface
reject defect-era approve --scene/--why
obtain validated V4 admission
execute only exact V4 final-gated effect
never invent Human attribution
```

`legacy/scriptops-v2-single.py`:

```text
preserve non-approval substrate
disable direct approve
disable direct scene-promote -> accepted at parser and command layers
```

`phase6/x1b_human_decision.py`:

```text
V4 schemas/canonical JSON
pure accepted preview helper
non-circular request identity
public GitHub transport
PR/review pagination/currentness
CompleteReviewSetV4
freshness/supersession policy
admission/replay/lock
refs/heads/main raw checks
FinalEffectGateV4
system-Git isolation
NO_REPLACE_RAW_SHA1_OBJECTS_V1 helpers
raw commit-content/SHA-1 helpers
CLOSED_RAW_COMMIT_OBJECT_V1 writer/parser/verifier
temporary-index exact tree helpers
alias-safe target helpers
record construction
post-effect/rollback fail-closed helpers
```

Restore/verifier/docs/tests/workflow responsibilities remain as frozen above.

## 47. Independent implementation-review obligations

Later independent implementation review must inspect the complete candidate tree and prove, not infer:

```text
changed-file set within authorized surface
no third acceptance route
old Phase-6 and legacy routes deny
restore/verifier/docs coherent
V4 request identity acyclic
V4 schemas internally exact
one-file decision PR enforced
public transport credential-free/exact-origin
review set/currentness/conflicts complete
freshness/supersession matches R4R4
admission does not mutate canon
lock/replay claim bounded honestly
refs/heads/main exact effect ref
all authority Git reads are no-replace/raw
refs/replace state rejected at all frozen checkpoints
raw base tree derived from raw base commit bytes
no replace-aware changed-set authority
output blobs independently SHA-1 checked
new tree exact two-path delta from raw parent tree
raw commit content independently constructed
raw commit SHA-1 independently computed
commit object written without commit-tree
raw commit read-back byte-identical
closed header set contains no encoding/signature/extra parent
local i18n.commitEncoding cannot transform object
alias-safe filesystem target contract enforceable
FinalEffectGateV4 leaves no unauthorized substitution choice
result raw commit exact two-path one-parent effect
Human attribution only from validated evidence
no self-hash/circular evidence
failure/rollback never misreported as success
```

```text
TESTS GREEN != IMPLEMENTATION REVIEW PASS
IMPLEMENTATION REVIEW PASS != X1B CLOSED
```

## 48. Separately authorized live positive control

A later positive control requires fresh Human authorization and exactly one disposable ScriptOps repository execution instance with no user screenplay canon.

It must include:

```text
inert/synthetic scene
exact staged candidate
exact impact report
one HumanDecisionRequestV4
one dedicated one-file decision PR
one manual GitHub UI APPROVE by litrgratis-pixel
exact four-line V4 review body
one corrected Phase-6 approve --decision-pr invocation
local HEAD symbolically on refs/heads/main
zero refs/replace/*
non-shallow/no-graft raw profile
no GitHub review-write credential in effect process
```

Human must see exact candidate/content/scope and material effect including:

```text
canonical before/after hash
canonical local ref refs/heads/main
decision-log target + one append
exact two-path one-parent local effect commit
logical commit message
NO_REPLACE_RAW_SHA1_OBJECTS_V1
CLOSED_RAW_COMMIT_OBJECT_V1
RAW_OBJECT_ALIAS_SAFE_GIT_PLUMBING_V2
SINGLE_LINK_ALIAS_SAFE_REPOSITORY_TARGETS_V1
```

Positive result requires exact post-effect raw truth and Human-evidence-derived attribution.

```text
LIVE POSITIVE CONTROL PASS != CORRECTIVE CLOSURE
```

## 49. Corrective closure composition

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

## 50. Successor-review adversarial checklist

The independent R4R4 brief review must explicitly attack at least:

```text
Can any replacement ref reinterpret a Human-bound SHA/tree?
Can a replace ref inserted after admission survive final/pre-CAS checks?
Can any authority helper accidentally omit --no-replace-objects?
Can local graft/shallow semantics alter the claimed parent relationship?
Can local i18n.commitEncoding add an encoding header?
Can any config add gpgsig/mergetag/extra headers?
Can hash-object write bytes different from independently prepared commit content?
Can Git-returned object SHA differ from independent raw-object SHA-1?
Can raw commit contain a second parent or altered tree/message/time?
Can changed-set proof compare against anything other than raw parent tree?
Can V3 Human evidence be reused after V4 effect-profile change?
Can side/detached refs or hardlink/symlink targets become operative?
Can post-gate local substitution occur before CAS?
Is any core security/authority choice still left to implementer?
```

Any credible counterexample freezes a finding and returns `NOT PASS`.

## 51. Explicit non-authority

This brief does not authorize:

```text
ScriptOps source mutation
Human decision PR creation
Human review creation
live positive control
canonical screenplay mutation
decision-log mutation
refs/heads/main effect
merge
X1B closure
V1 entry
release
deployment
tag
```

R4R4 review PASS, if later obtained, would establish only that this implementation brief is acceptable for a separately Human-authorized implementation stage.

## 52. STOP

Required next stage after durable R4R4 freeze:

```text
INDEPENDENT AK-CANON X1B R4R4 IMPLEMENTATION-BRIEF REVIEW
```

Only fresh separate Human authorization may create that review artifact.

```text
R4R4 BRIEF != IMPLEMENTATION AUTHORITY
R4R4 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R4 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
STOP
```
