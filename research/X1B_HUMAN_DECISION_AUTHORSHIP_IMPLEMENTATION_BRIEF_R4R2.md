# X1B HUMAN DECISION AUTHORSHIP — CLEAN IMPLEMENTATION BRIEF R4R2

Status: `CLEAN R4R2 CORRECTIVE BRIEF / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-01`

## 1. Authority, purpose, and STOP boundary

This document is the self-contained successor to the clean R4R1 implementation brief after independent AK-CANON review PR #117 returned `NOT PASS`.

It corrects exactly the two new R4R1 blockers while preserving every R4R1 security/authority contract not rejected by PR #117:

1. request/effect identity must not be circular through its own `decision_request_id`;
2. the known legacy `scene-promote --to accepted` path must be concretely disabled as a direct canonical-acceptance path.

This artifact is an implementation brief only. It authorizes no ScriptOps implementation, no Human decision PR/review, no live positive control, no canonical screenplay effect, no merge, no X1B closure, no Agency Kernel v1, no release, deployment, or tag.

```text
R4R2 BRIEF != IMPLEMENTATION AUTHORITY
R4R2 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R2 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

After durable freeze of this brief, STOP. The next stage is a separately Human-authorized independent AK-CANON R4R2 implementation-brief review.

## 2. Exact governance lineage

### 2.1 Accepted corrective design

```text
FJ899/scriptops PR #34
HEAD = d7a5065c87e9a4b49fb608235c908bceac42b4b1
TREE = 3140d0ac95c120a7b1532942bae2e0dad38b4839
PATH = governance/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_CANDIDATE.md
BLOB = dac16f109d1414a2208c2ed9a166ae9e9a329216
```

### 2.2 Independent design review

```text
FJ899/8 PR #109
HEAD = 132d65be48331a822039262b707c47a81d02a64d
TREE = a8bdc363d293beb7b15ae8b787cc3ebdd694fd99
BLOB = 439109e104244552a5ac1f3f08988dba283733d0
VERDICT = AK-CANON X1B CORRECTIVE DESIGN REVIEW R2 = PASS
```

### 2.3 Clean R4R1 predecessor

```text
FJ899/8 PR #116
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 0319b13cbe85675db0b40d36f5940cbfba36c130
TREE = 55dc82a52117d7234915a0b84193a4b2a26c226a
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R1.md
BLOB = 0fc30617ae7c378bdd90e7f9c5e1ab37a59661a4
```

### 2.4 Binding R4R1 NOT-PASS review

```text
FJ899/8 PR #117
HEAD = a40187f1fd05193ad562551b3e332af574725e32
TREE = 799ad0f23c6b45cf985d35d0062ec0d916a32e09
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R1_AK_CANON_REVIEW.md
BLOB = ceafb1b8a01d5044ed5e1e0feea5d62cfe6ac7e0
VERDICT = AK-CANON X1B R4R1 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

R4R2 directly addresses:

```text
X1B-R4R1-IBR-F001 — request/effect identity circular through commit message
X1B-R4R1-IBR-F002 — legacy scene-promote --to accepted parallel effect path
```

`REVIEW FINDING != REPAIR AUTHORITY`; this correction exists only under the fresh Human authorization for R4R2 brief preparation.

## 3. Exact evidence-repository base

```text
FJ899/8 main
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

The earlier unauthorized R4-main write and forward recovery remain visible in history. No history rewrite is part of R4R2.

## 4. Frozen ScriptOps baseline

```text
FJ899/scriptops main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Frozen security-relevant BLOBs:

```text
phase6/scriptops-v2-hardening.py
4f379960ed5677634dd234af6aa39626782b6133

legacy/scriptops-v2-single.py
9baa7b3a1eb746e34b79207a382eea1f5dd4ec55

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

## 5. Normative precedence

```text
R4R2 TEXT = CURRENT IMPLEMENTATION-BRIEF AUTHORITY
R4R1 / R4 / R3 / R2 / R1 = HISTORICAL INPUT ONLY
```

No authority/security rule depends on implicit inheritance. Corrective design PR #34 remains the higher-level normative property contract.

## 6. Future implementation surface

Expected bounded implementation surface:

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
.github/workflows/phase6-scriptops-smoke.yml
.github/workflows/verify-repository.yml
sources/prototype/scriptops-v2-single.py.part01..part07
```

A smaller changed set is permitted only if independent implementation review proves all obligations satisfied. Any additional path requires STOP and fresh Human authorization before mutation.

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

PR number is locator only, not authority.

No caller-controlled field may supply Human actor/result/rationale, request path/digest, task/scene/candidate/impact identities, canonical target, effect type, or material effect.

Defect-era Phase-6 `approve --scene ... --why ...` MUST terminate nonzero before any effect.

```text
ONE OPERATIVE ACCEPTANCE EFFECT PATH
=
X1B-VALIDATED PHASE6 APPROVE --DECISION-PR PATH
```

## 9. Direct legacy approve is disabled

```text
python legacy/scriptops-v2-single.py approve --scene <scene>
```

MUST terminate nonzero before canonical scene write, accepted-state transition, decision-log append, Human attribution, staging, or commit. It must not delegate directly to an acceptance effect.

## 10. F002 correction — direct legacy scene-promote accepted is disabled

Known current path:

```text
python legacy/scriptops-v2-single.py scene-promote --id <scene> --to accepted
```

MUST become non-effect-capable.

Exact implementation contract:

1. remove `accepted` from CLI choices exposed for direct `scene-promote --to`;
2. add an independent guard in `cmd_scene_promote` so `target_status == "accepted"` terminates nonzero before mutation even when called programmatically or parser checks are bypassed;
3. do not delegate direct legacy scene promotion to the acceptance effect path;
4. only Phase-6 `approve --decision-pr` may create the accepted canonical effect.

Required real regression uses a staged candidate with no canonical scene and proves:

```text
exit != 0
no scenes/<scene>.fountain creation/change
no accepted transition
no .scriptops/decision-log.ndjson mutation
no Human attribution
no staging
no commit
```

Verifier and implementation review must forbid both:

```text
legacy approve --scene
legacy scene-promote --to accepted
```

```text
SAFE NEW PATH + ANY EXECUTABLE UNSAFE ACCEPTANCE PATH = NOT CLOSED
```

## 11. Historical transport vs active runtime

```text
sources/prototype/scriptops-v2-single.py.part01..part07
= immutable historical reconstruction evidence

legacy/scriptops-v2-single.py
= active corrected runtime substrate
```

Active legacy is not required to equal historical 51980-byte source after X1B correction.

## 12. Restore contract

`scripts/restore_v2.py` preserves historical reconstruction/checking but can never restore historical bytes inside the ScriptOps repository.

Write mode requires explicit output. Before opening/truncating/creating/writing, resolve repository root and destination and prove destination is outside repository root.

Must DENY without modification, including under `--force`, for:

```text
repository-internal absolute path
relative alias into repository
.. traversal into repository
symlink-mediated destination resolving into repository
repository root itself
legacy/scriptops-v2-single.py
```

Ambiguity is DENY. `--check-only` may reconstruct in memory. Explicit outside-repository reconstruction remains historical evidence only.

## 13. Repository verifier split-source contract

Historical transport checks prove all seven parts, exact reconstructed SHA/size, UTF-8 and Python syntax.

Active runtime checks prove:

```text
legacy exists and is valid Python
direct legacy approve disabled
direct legacy scene-promote --to accepted disabled
Phase-6 authority route is R4R2-compliant
```

Verifier must not require active legacy byte identity with historical prototype and must not treat `approve --why` as current safety requirement.

## 14. Current-state authority documentation

`README.md`, `PROJECT_STATE.md`, `HANDOFF.md`, `sources/prototype/RESTORE.md`, and `SOURCE_MANIFEST.md` must state current truth:

```text
defect-era approve --why = historical provenance only
current Human-decision route = approve --decision-pr <N> only
direct legacy approve = disabled
direct legacy scene-promote --to accepted = disabled
legacy historical byte identity = historical baseline, not current runtime identity
historical prototype parts != current active runtime authority
```

No current recovery/resume route may direct operator or AI to old approval semantics. Historical evidence itself is not rewritten.

## 15. Exact canonical JSON and hashes

All authority-critical canonical objects:

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

File digests bind exact file bytes. No Unicode/newline normalization or semantic reserialization where byte identity is specified.

## 16. Exact timestamp strings

Authority-critical locally-created UTC timestamps (`request_created_at`, `FinalEffectGateV1.observed_at`) MUST use exactly:

```text
YYYY-MM-DDTHH:MM:SSZ
```

20 ASCII characters, UTC `Z`, four-digit year, two-digit month/day/hour/minute/second, no fractional seconds, no offset form, and calendar/time validation required.

GitHub `submitted_at` values used by R4R2 must also validate to exactly this UTC `Z` form; otherwise DENY rather than normalize.

This makes lexicographic timestamp ordering identical to chronological second-level ordering for accepted R4R2 values.

## 17. CanonicalPreStateV1

```text
CanonicalPreStateV1 = {
  "exists": <true|false>,
  "file_sha256": <64 lowercase hex or JSON null>
}
```

`exists=false` requires null hash; `exists=true` requires exact current canonical byte hash. Symlink/nonregular/ambiguous target is DENY.

## 18. Deterministic accepted preview

Before Human request finalization, proposal preparation derives exact accepted canonical bytes from exact candidate bytes using the same production rendering helper later used for effect.

```text
accepted_canonical_file_sha256 = SHA256(exact accepted canonical bytes)
```

At final gate/effect, re-rendered bytes MUST equal exact bound preview bytes/hash. Mismatch DENY before mutation.

## 19. PresentedMaterialEffectV2 — non-circular material effect

Closed schema:

```text
PresentedMaterialEffectV2 = {
  "schema_version": "scriptops-x1b-presented-material-effect/v2",
  "repository": "FJ899/scriptops",
  "scene_id": <exact scene ID>,
  "candidate_path": <exact repo-relative candidate path>,
  "candidate_file_sha256": <64 lowercase hex>,
  "canonical_scene_effect": {
    "target_path": "scenes/<scene_id>.fountain",
    "before": <CanonicalPreStateV1>,
    "after_file_sha256": <accepted_canonical_file_sha256>,
    "source_status": "candidate",
    "canonical_status_after": "accepted",
    "candidate_source_preserved": true
  },
  "decision_log_effect": {
    "target_path": ".scriptops/decision-log.ndjson",
    "append_count": 1,
    "record_schema_version": "scriptops-x1b-decision-record/v2"
  },
  "local_git_effect": {
    "commit_count": 1,
    "commit_message": "scriptops x1b: accept <exact scene_id>",
    "exact_changed_paths": [
      "scenes/<scene_id>.fountain",
      ".scriptops/decision-log.ndjson"
    ]
  }
}
```

`<exact scene_id>` is replaced by the concrete bound scene ID before request hashing.

No field used to compute request digest may contain request digest/ID or any later-derived identifier such as PR number/head, review ID, admission ID, final gate digest, or future effect commit SHA.

```text
presented_material_effect_digest = sha256_canonical(PresentedMaterialEffectV2)
```

## 20. HumanDecisionRequestBindingV2 — F001 correction

Closed binding:

```text
HumanDecisionRequestBindingV2 = {
  "schema_version": "scriptops-x1b-human-decision-request/v2",
  "repository": "FJ899/scriptops",
  "repository_head_at_request": <40 lowercase hex>,
  "request_created_at": <exact R4R2 UTC timestamp>,
  "task_id": <exact task ID>,
  "scene_id": <exact scene ID>,
  "candidate_path": <exact repo-relative candidate path>,
  "candidate_file_sha256": <64 lowercase hex>,
  "impact_report_path": <exact repo-relative impact path>,
  "impact_report_sha256": <64 lowercase hex>,
  "canonical_target": "scenes/<scene_id>.fountain",
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect": <PresentedMaterialEffectV2>
}
```

Exact construction order:

```text
1 canonical pre-state
2 accepted preview bytes/hash
3 PresentedMaterialEffectV2 with concrete scene-id-only commit message
4 HumanDecisionRequestBindingV2
5 request_binding_json = canonical_json_bytes(binding)
6 request_digest = sha256_hex_bytes(request_binding_json)
7 decision_request_id = "x1b:" + request_digest
8 HumanDecisionRequestV2
```

Committed request object:

```text
HumanDecisionRequestV2 = {
  <all HumanDecisionRequestBindingV2 fields>,
  "decision_request_id": <exact decision_request_id>,
  "request_digest": <exact request_digest>
}
```

Request file bytes MUST be exactly `canonical_json_bytes(HumanDecisionRequestV2)` with no trailing LF.

Verifier reconstructs binding from committed object and recomputes digest/ID exactly.

Forbidden self-reference:

```text
NO request_digest INPUT FIELD
MAY CONTAIN
request_digest, decision_request_id,
OR ANY VALUE DERIVED FROM THEM
```

Golden vector MUST prove same exact binding inputs produce same binding bytes/digest/ID without fixed-point search or placeholder-preimage semantics.

## 21. Proposal path/branch and one-file commit

After digest exists:

```text
request_path = decisions/x1b/<request_digest>.json
proposal_branch = decision/x1b/<request_digest>
decision_request_id = x1b:<request_digest>
```

Digest is exactly 64 lowercase hex.

Proposal branch originates from exact `repository_head_at_request`.

Request commit:

```text
exactly one parent = repository_head_at_request
adds exactly request_path
request blob = exact canonical HumanDecisionRequestV2 bytes
no second changed path
```

Proposal creation may be done by separately authorized proposal writer. Proposal write capability is not Human authority. Evaluated effect invocation must not create/edit proposal branch/file/PR/review/comment/ref/rule/setting.

## 22. Decision PR envelope

PR number/head are external evidence, never request-digest inputs.

Valid PR requires:

```text
repo = FJ899/scriptops
state=open
merged=false
base.ref=main
base.sha=request.repository_head_at_request
head.ref=decision/x1b/<request_digest>
head repo=FJ899/scriptops
head SHA=exact one-commit request commit
```

Verifier fetches head Git commit and complete BASE→HEAD file set; requires exactly one added `request_path`, exact one parent, exact request bytes/schema.

No caller request path is trusted. Exact equality required among filename digest, computed digest, request field, decision ID suffix, and head-ref digest.

Any extra/renamed/deleted file, wrong base/parent/ref/repository, hidden pagination remainder, mismatch, or ambiguity is DENY.

## 23. Human authority profile and exact review body

Authoritative Human actor for this bounded profile:

```text
litrgratis-pixel
```

Account identity alone is not claimed to prove private Human mental state. Later live control requires manual Human UI APPROVE by this actor.

Exact review body: four LF-separated lines and no trailing LF:

```text
X1B-HUMAN-DECISION-V2
decision_request_id=<exact x1b:<request_digest>>
decision_request_sha256=<exact request_digest>
why=<Human rationale>
```

Exact rationale validation:

```text
value after why= is 1..2000 Unicode code points inclusive
value == value.strip()
no U+0000..U+001F
no U+007F
therefore no CR/LF/TAB/NUL/control characters
```

The body itself must be valid Unicode supplied by GitHub API, contain exactly 4 logical lines, LF separators only, no CR, no leading/trailing blank line, no trailing LF, no extra field/line, exact marker and exact request identities.

`human_review_body_sha256` = SHA-256 of exact UTF-8 body bytes.

Caller `--why` or operator note is never substituted for Human rationale.

## 24. Complete review collection and state semantics

Complete reviews must be enumerated. Duplicate numeric ID or node ID DENY.

Recognized states exactly:

```text
APPROVED
CHANGES_REQUESTED
COMMENTED
DISMISSED
```

Unknown state DENY.

Semantics:

```text
APPROVED = active positive decision-bearing
CHANGES_REQUESTED = active negative/conflicting
COMMENTED = nondecision
DISMISSED = inactive
```

For `litrgratis-pixel` on exact current PR HEAD: exactly one active syntactically/semantically valid APPROVED and no active CHANGES_REQUESTED.

Second current-head APPROVED => ambiguous DENY. Old-commit APPROVED => historical only. No latest-wins chronology rule.

## 25. Public trusted GitHub transport

Production evidence transport is unauthenticated public read to exact origin:

```text
https://api.github.com
```

Use explicit Python standard-library opener equivalent to:

```text
ProxyHandler({})
HTTPSHandler(context=ssl.create_default_context())
redirect handler rejecting every redirect
```

No configurable API base, Authorization header, authenticated fallback, `gh`, `.netrc`, GitHub CLI auth config, credential helper, browser state, caller token, or cached local review JSON.

Non-empty values in at least these variables => DENY before evidence acquisition:

```text
HTTP_PROXY HTTPS_PROXY ALL_PROXY
http_proxy https_proxy all_proxy
SSL_CERT_FILE SSL_CERT_DIR
REQUESTS_CA_BUNDLE CURL_CA_BUNDLE
GH_TOKEN GITHUB_TOKEN
GH_ENTERPRISE_TOKEN GITHUB_ENTERPRISE_TOKEN GITHUB_PAT
```

System DNS and normal OS root trust store are explicit bounded platform dependencies. Redirect/alternate origin/public read failure/rate-limit/visibility/incomplete evidence => DENY/BLOCKED before effect.

## 26. Exact GitHub read operations and pagination

Bounded reads equivalent to:

```text
GET /repos/FJ899/scriptops/pulls/<N>
GET /repos/FJ899/scriptops/pulls/<N>/files?per_page=100&page=<p>
GET /repos/FJ899/scriptops/contents/<derived-request-path>?ref=<exact-head-sha>
GET /repos/FJ899/scriptops/git/commits/<exact-head-sha>
GET /repos/FJ899/scriptops/pulls/<N>/reviews?per_page=100&page=<p>
```

Every collection starts page 1, `per_page=100`, sequential pages until completion is unambiguous. Malformed page, duplicate required identity, inconsistent paging, error/rate limit, or inability to prove completion => DENY.

## 27. NormalizedReviewV2 and complete-review digest

For every submitted review:

```text
NormalizedReviewV2 = {
  "review_numeric_id": <canonical decimal string: "0" or no leading zero>,
  "review_node_id": <exact nonempty node-id string>,
  "actor_login": <exact login>,
  "state": <recognized state>,
  "commit_id": <40 lowercase hex or null>,
  "body_sha256": <64 lowercase hex exact UTF-8 body digest>,
  "submitted_at": <exact R4R2 UTC timestamp>
}
```

Complete set includes all actors and recognized states.

Sort by:

```text
(submitted_at ASC lexicographically,
 review_numeric_id ASC as arbitrary-precision decimal integer)
```

Construct:

```text
CompleteReviewSetV2 = {
  "schema_version": "scriptops-x1b-complete-review-set/v2",
  "repository": "FJ899/scriptops",
  "decision_pr_number": <positive integer>,
  "decision_pr_head": <40 lowercase hex>,
  "reviews": [<normalized reviews in normative order>]
}
```

```text
complete_review_set_digest = sha256_canonical(CompleteReviewSetV2)
```

Golden vectors freeze exact projection/order/bytes/digest.

## 28. Candidate/impact/applicability checks

Before admission:

```text
local repository identity bound to FJ899/scriptops
local HEAD = request.repository_head_at_request
tracked worktree/index clean
candidate regular non-symlink exact path and exact hash
candidate status=candidate
impact path = tasks/<task_id>/impact-report.json
impact regular non-symlink exact bytes/hash
impact status=REVIEW_REQUIRED
impact task/scene/candidate path/hash match request
canonical_target=scenes/<scene_id>.fountain
effect_type=ACCEPT_SCENE_CANDIDATE
canonical pre-state matches request
accepted preview bytes/hash match request
material-effect object/digest match request
```

If current impact hash uses `sha256:<hex>`, exact equality with `"sha256:" + candidate_file_sha256` is required.

All are revalidated at final gate.

## 29. HumanDecisionAdmissionIdentityV2

Closed identity:

```text
HumanDecisionAdmissionIdentityV2 = {
  "schema_version": "scriptops-x1b-human-decision-admission/v2",
  "repository": "FJ899/scriptops",
  "repository_head_at_request": <exact HEAD>,
  "decision_pr_number": <positive integer>,
  "decision_pr_head": <exact head>,
  "decision_request_id": <x1b:<digest>>,
  "request_digest": <64 lowercase hex>,
  "request_file_path": "decisions/x1b/<request_digest>.json",
  "human_review_numeric_id": <canonical decimal string>,
  "human_review_node_id": <exact node ID>,
  "human_actor": "litrgratis-pixel",
  "human_review_body_sha256": <64 lowercase hex>,
  "human_review_submitted_at": <exact timestamp>,
  "human_rationale": <validated exact rationale>,
  "task_id": <exact task>,
  "scene_id": <exact scene>,
  "candidate_path": <exact path>,
  "candidate_file_sha256": <exact hash>,
  "impact_report_path": <exact path>,
  "impact_report_sha256": <exact hash>,
  "canonical_target": "scenes/<scene_id>.fountain",
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect_digest": <exact hash>,
  "canonical_instance_scope": "LOCAL_WORKTREE_DECISION_LOG_V1"
}
```

```text
admission_id = "x1b-admit:" + sha256_canonical(HumanDecisionAdmissionIdentityV2)
```

Admission is process-local, one-shot, not caller-constructible, not reloadable bearer authority, and not authority to manufacture Human review.

## 30. Bounded replay and worktree lock

Exact claim:

```text
one decision_request_id may cause at most one successful X1B acceptance effect
within one canonical local worktree execution instance
```

Before effect, complete local `.scriptops/decision-log.ndjson` has no successful R4R2 record consuming request ID. After success exactly one new record consumes it. Replay in same instance DENY.

```text
NO GLOBAL CROSS-CLONE EXACTLY-ONCE CLAIM
OLD CONSENT + CHANGED OPERATION = DENY
```

Acquire exclusive atomically-created directory before preliminary admission:

```text
<worktree-specific git-dir>/scriptops-x1b-approve.lock
```

Already exists => DENY/BLOCKED. No automatic stale-lock deletion. Hold through post-effect verification/cleanup. Lock has no Human authority.

## 31. FinalEffectGateV2

Preliminary admission cannot mutate canon.

Immediately before first canonical mutation, while lock held, freshly reread PR metadata and complete reviews via trusted transport; revalidate exact PR/request/current Human review/conflicts/CompleteReviewSet digest/local HEAD/candidate/impact/canonical pre-state/accepted preview/material effect/replay.

Closed gate:

```text
FinalEffectGateV2 = {
  "schema_version": "scriptops-x1b-final-effect-gate/v2",
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
  "complete_review_set_digest": <exact final digest>,
  "repository_head_before_effect": <exact local HEAD>,
  "scene_id": <exact scene>,
  "candidate_path": <exact path>,
  "candidate_file_sha256": <exact digest>,
  "impact_report_sha256": <exact digest>,
  "canonical_target": "scenes/<scene_id>.fountain",
  "canonical_before": <CanonicalPreStateV1>,
  "canonical_after_file_sha256": <exact digest>,
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "canonical_instance_scope": "LOCAL_WORKTREE_DECISION_LOG_V1",
  "current_human_decision_valid": true,
  "observed_at": <exact R4R2 UTC timestamp>
}
```

```text
final_effect_gate_digest = sha256_canonical(FinalEffectGateV2)
```

Gate is in-memory one-shot and not reusable credential.

## 32. Human-currentness commitment point

```text
Human-currentness commitment point
=
successful FinalEffectGateV2 validation
immediately before first canonical mutation
```

Before it, visible review/PR drift revokes/conflicts. After it, later remote change does not retroactively revoke the already-authorized same-process one-shot effect; no distributed atomicity claim.

Between gate success and first mutation: no user interaction, network, sleep/wait, unrelated blocking operation, proposal/review mutation.

## 33. Exact outputs and decision record before mutation

Before first mutation compute/validate exact:

```text
accepted canonical scene bytes
one canonical X1BDecisionRecordV2 NDJSON line
commit message "scriptops x1b: accept <exact scene_id>"
exact two-path staging set
```

Closed record:

```text
X1BDecisionRecordV2 = {
  "schema_version": "scriptops-x1b-decision-record/v2",
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
  "canonical_before": <CanonicalPreStateV1>,
  "canonical_after_file_sha256": <exact digest>,
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect_digest": <exact digest>,
  "canonical_instance_scope": "LOCAL_WORKTREE_DECISION_LOG_V1"
}
```

NDJSON append = exact canonical JSON bytes plus exactly one LF.

No resulting effect commit SHA appears in the record; later independent evidence records it externally.

## 34. Exact effect and local Git capability

After final gate:

```text
write exact accepted bytes -> scenes/<scene_id>.fountain
append exactly one X1BDecisionRecordV2 -> .scriptops/decision-log.ndjson
stage exactly those two paths
commit exactly once with message "scriptops x1b: accept <exact scene_id>"
new commit exactly one parent = repository_head_before_effect
```

No `git add .`.

Approval performs no network Git command: no fetch/pull/push/ls-remote/submodule network/`gh`.

Every local Git subprocess uses explicit sanitized environment removing denied GitHub credentials, with at least:

```text
GIT_TERMINAL_PROMPT=0
GCM_INTERACTIVE=never
git -c credential.helper= ...
```

## 35. Failure after first mutation

Both output payloads are precomputed.

If failure after first filesystem mutation but before successful effect commit: nonzero, attempt deterministic restoration of exact pre-effect bytes/state while lock held. Never report X1B success for partial effect.

If exact restoration cannot be proven: leave explicit fail-closed dirty/error state and report `BLOCKED`; do not synthesize Human success evidence. No automatic destructive reset of unrelated state.

If a local effect commit was created but post-commit verification fails, do not silently rewrite/reset Git history; report `BLOCKED` with the commit preserved for forensic truth and require separately authorized recovery.

## 36. Post-effect truth

Success requires:

```text
new HEAD exactly one parent = repository_head_before_effect
exactly one new effect commit
exact commit message
commit changed set exactly:
  scenes/<scene_id>.fountain
  .scriptops/decision-log.ndjson
canonical exact bytes hash = bound after hash
canonical status=accepted
exactly one new X1BDecisionRecordV2 line
record request/admission/gate/review/effect identities match
working tree/index clean after commit
request consumed in local decision log
```

Exit code alone is not evidence.

## 37. Mandatory regression/negative matrix

### Current and legacy real-boundary attacks

```text
old Phase-6 approve --scene/--why without trusted Human evidence => DENY/no effect
legacy approve --scene => DENY/no effect
legacy scene-promote --to accepted => DENY/no effect
```

For scene-promote, use real staged candidate and prove absent canonical file remains absent.

### Request/PR attacks

```text
caller request-path substitution
wrong filename/request/head-ref digest
wrong PR base/ref/head repo
wrong head parent
extra/renamed/deleted request path
malformed/extra-field request
request digest/ID mismatch
candidate/impact/canonical/preview/material-effect drift
attempted request self-reference via request ID/digest
```

Golden vector explicitly proves no F001 fixed-point/self-reference.

### Human/review attacks

```text
no review
wrong actor
wrong commit
malformed four-line body
empty/trim-violating/control-containing/over-2000 rationale
second active approval
active CHANGES_REQUESTED
COMMENTED only
DISMISSED only
unknown state
duplicate numeric/node ID
incomplete pagination
API error/rate limit
```

### Transport/capability attacks

```text
credential env present
proxy env present
CA override env present
custom API origin
any redirect/cross-origin redirect
authenticated fallback
Authorization construction
public read failure
network Git or gh attempt
```

### Replay/concurrency/final-currentness attacks

```text
same request replay
same-worktree concurrent invocation
stale lock
local HEAD drift
old Human decision with changed operation
review dismissed after preliminary admission
CHANGES_REQUESTED after preliminary admission
PR closed/merged/HEAD drift
remote final reread failure
candidate/impact/canonical/preview/material-effect drift
request consumed after admission
executor substitution after final gate
out-of-scope staged file
second log append
second effect commit
```

### Failure injection

```text
after first file mutation
before second mutation
before staging
before commit
during commit
post-commit verification mismatch
```

Every negative proves no unauthorized successful Human-attributed effect, not merely an exception.

## 38. Original preregistered X1B attacks remain mandatory

All ten original attacks remain normative: AI self-acceptance; Continue-as-decision; silence-as-consent; old-consent reuse; A→A-prime substitution; parameter change; scope expansion; general-direction-to-specific-Human attribution; AI-generated Human-looking artifact; AI-filled value recorded Human-chosen.

The real `cmd_approve` defect and both direct legacy acceptance paths are mandatory real-boundary regressions.

## 39. Bounded trusted-origin claim

Only this bounded composition is claimed:

```text
manual Human APPROVE by established actor
+ exact authoritative GitHub review record
+ effect process unable to create/edit Human review evidence
+ credential-free exact-origin public evidence acquisition
+ exact request/PR/review/current-state/material-effect binding
+ independent admission
+ fresh FinalEffectGateV2
+ exact no-substitution effect
= bounded trusted Human decision evidence for this X1B profile
```

No claim that review metadata alone proves Human UI origin or private mental state.

## 40. Implementation-path responsibilities

`phase6/scriptops-v2-hardening.py`: only current `approve --decision-pr`; reject old Phase-6 approve; derive Human attribution only from evidence; execute admitted/final-gated effect.

`legacy/scriptops-v2-single.py`: preserve non-approval substrate but disable both direct `approve` and direct `scene-promote --to accepted`, including internal guard.

`phase6/x1b_human_decision.py`: schemas, canonical JSON, non-circular request, PR/review transport/validation, CompleteReviewSetV2, admission, replay/lock, FinalEffectGateV2, preview/effect binding, record construction, fail-closed helpers.

`restore_v2.py`: historical reconstruction only outside repo.

`verify_repository.py`: split-source validation and direct-path safety assertions.

Current docs: current route and historical-vs-active truth.

Tests/workflow: deterministic R4R2 tests without GitHub write credential and without creating Human evidence/canonical effects.

## 41. Independent implementation-review obligations

Later implementation review must inspect complete candidate tree effect-entry inventory, all accepted-state paths, exact changed-file set, old Phase-6/legacy path denials, restore/verifier/docs, canonical serialization, request non-circularity, exact schemas, PR envelope, transport, review parser/completeness/conflicts, admission, lock/replay, final-gate currentness, preview byte identity, actual decision-log target, rollback/failure, exact two-path commit, durable attribution, and no self-hash/circular evidence.

```text
TESTS GREEN != IMPLEMENTATION REVIEW PASS
```

Any material authority/security ambiguity = NOT PASS.

## 42. Separately authorized live positive control

Only after implementation review and fresh negative verification, use one disposable ScriptOps execution instance and inert/synthetic scene.

Human must see exact request/material effect including:

```text
exact candidate/content/scope
exact canonical before/after hash
decision-log target .scriptops/decision-log.ndjson
one append
one two-path local Git commit
commit message "scriptops x1b: accept <scene_id>"
```

`litrgratis-pixel` manually submits exact R4R2 four-line APPROVED review through GitHub Human UI. Evaluated effect process has no review-create capability and consumes evidence via credential-free adapter.

No user screenplay canon.

## 43. Closure sequence

After independent R4R2 brief PASS only:

```text
bounded Human-authorized implementation
exact implementation candidate
independent implementation review
fresh preregistered corrective verification
all negative controls
separately authorized real Human positive control
post-effect independent verification
corrective-closure review
Human closure acceptance
durable final freeze
```

```text
GREEN TESTS != CORRECTIVE CLOSURE
IMPLEMENTATION REVIEW PASS != CORRECTIVE CLOSURE
LIVE POSITIVE CONTROL PASS != CORRECTIVE CLOSURE
TECHNICAL VERIFICATION PASS != HUMAN CLOSURE ACCEPTANCE
X1B CLOSED != V1 AUTHORITY
```

## 44. STOP

This brief authorizes no implementation.

After durable freeze report:

```text
X1B CLEAN R4R2 CORRECTIVE BRIEF PREPARATION = PASS / NOT PASS / BLOCKED
```

Then STOP for fresh Human authorization of independent R4R2 implementation-brief review.
