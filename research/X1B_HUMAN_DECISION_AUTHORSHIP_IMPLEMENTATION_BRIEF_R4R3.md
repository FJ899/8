# X1B HUMAN DECISION AUTHORSHIP — CLEAN IMPLEMENTATION BRIEF R4R3

Status: `CLEAN R4R3 CORRECTIVE BRIEF / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-01`

## 1. Authority, purpose, and STOP boundary

This document is the self-contained successor to R4R2 after independent AK-CANON review PR #119 returned `NOT PASS`.

It corrects exactly the four R4R2 review findings while preserving every earlier X1B property and R4R2 contract not rejected by PR #119:

1. the local canonical Git ref must be Human-bound and admission-bound;
2. ambient Git hooks, filters, signing/configuration, and porcelain behavior must not expand or transform the post-FinalEffectGate effect;
3. authority-critical write targets must be protected against symlink/hardlink/alias substitution;
4. freshness, deactivation, multiple-active-decision, and supersession semantics must be explicit rather than inferred.

This document is an implementation brief only. It authorizes no ScriptOps implementation, no Human decision PR/review, no live positive control, no canonical screenplay effect, no merge, no X1B closure, no Agency Kernel v1, no release, deployment, or tag.

```text
R4R3 BRIEF != IMPLEMENTATION AUTHORITY
R4R3 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R3 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

After durable freeze of this brief, STOP. The next stage is a separately Human-authorized independent AK-CANON R4R3 implementation-brief review.

## 2. Exact governance lineage

### 2.1 Accepted corrective design

```text
FJ899/scriptops PR #34
HEAD = d7a5065c87e9a4b49fb608235c908bceac42b4b1
TREE = 3140d0ac95c120a7b1532942bae2e0dad38b4839
PATH = governance/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_CANDIDATE.md
BLOB = dac16f109d1414a2208c2ed9a166ae9e9a329216
```

Design requirements remain higher-level normative constraints, including trusted Human origin, exact content/scope/candidate/effect binding, explicit freshness/activity/supersession/conflict/replay semantics, executor no-substitution, fail-closed ambiguity, real-boundary regressions, and a real positive Human control.

### 2.2 Independent corrective-design review

```text
FJ899/8 PR #109
HEAD = 132d65be48331a822039262b707c47a81d02a64d
TREE = a8bdc363d293beb7b15ae8b787cc3ebdd694fd99
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_DESIGN_AK_CANON_REVIEW_R2.md
BLOB = 439109e104244552a5ac1f3f08988dba283733d0
VERDICT = AK-CANON X1B CORRECTIVE DESIGN REVIEW R2 = PASS
```

### 2.3 R4R2 predecessor

```text
FJ899/8 PR #118
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = b2c5de19ef678b18899751915060df5397edeb1b
TREE = 90848115ac15d0611e87f9bcb6bb9b16f69c6d5a
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R2.md
BLOB = 80a2b6326d0d021a7b7a2ebf9306f7e1853c2fcb
```

### 2.4 Binding R4R2 NOT-PASS review

```text
FJ899/8 PR #119
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 3df7b2700ce4fd845e3505398aa24dbb0730e7f7
TREE = f58ceb359259b0d9a630cf5ff90a8235da13e2b6
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R2_AK_CANON_REVIEW.md
BLOB = fa974d4a2f6f3e25e428591571000de8e8f2df86
VERDICT = AK-CANON X1B R4R2 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

R4R3 directly addresses:

```text
X1B-R4R2-IBR-F001 — local effect Git ref not bound
X1B-R4R2-IBR-F002 — ambient Git hooks/filters/signing/config can expand or transform effect
X1B-R4R2-IBR-F003 — hardlink aliasing of write targets not excluded
X1B-R4R2-IBR-F004 — freshness/supersession policy partly implicit
```

`REVIEW FINDING != REPAIR AUTHORITY`; this correction exists only under the fresh Human authorization for R4R3 brief preparation.

## 3. Exact evidence-repository base

```text
FJ899/8 main
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

The earlier unauthorized R4-main write and its forward recovery remain visible in history. No history rewrite is part of R4R3.

## 4. Frozen ScriptOps baseline

```text
FJ899/scriptops main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Freshly rechecked security-relevant BLOBs:

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

## 5. Normative precedence

```text
R4R3 TEXT = CURRENT IMPLEMENTATION-BRIEF AUTHORITY
R4R2 / R4R1 / R4 / R3 / R2 / R1 = HISTORICAL INPUT ONLY
CORRECTIVE DESIGN PR #34 = HIGHER-LEVEL PROPERTY CONTRACT
```

No authority/security rule depends on implicit inheritance. R4R3 is self-contained.

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

A smaller final changed set is permitted only if independent implementation review proves every R4R3 obligation satisfied. Any additional tracked path requires STOP and fresh Human authorization before mutation.

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

No caller-controlled field may supply Human actor/result/rationale, request path/digest, task/scene/candidate/impact identities, canonical target/ref, effect type, material effect, Git ref, or effect commit metadata.

Defect-era Phase-6:

```text
approve --scene ... --why ...
```

must terminate nonzero before any Human attribution or canonical effect.

```text
ONE OPERATIVE ACCEPTANCE EFFECT PATH
=
X1B-VALIDATED PHASE6 APPROVE --DECISION-PR PATH
```

## 9. Direct legacy approve is disabled

```text
python legacy/scriptops-v2-single.py approve --scene <scene>
```

MUST terminate nonzero before canonical scene write, accepted-state transition, decision-log append, Human attribution, Git index/ref mutation, or commit.

It must not delegate directly to the current Phase-6 effect path.

## 10. Direct legacy scene-promote accepted is disabled

```text
python legacy/scriptops-v2-single.py scene-promote --id <scene> --to accepted
```

MUST be non-effect-capable.

Exact future implementation contract:

1. remove `accepted` from direct CLI choices for `scene-promote --to`;
2. independently guard `cmd_scene_promote` so `target_status == "accepted"` terminates nonzero before mutation even if parser validation is bypassed;
3. do not delegate direct legacy scene promotion to acceptance;
4. only Phase-6 `approve --decision-pr` may create accepted canonical truth.

Required regression starts with a real staged candidate and proves:

```text
exit != 0
no scenes/<scene>.fountain creation/change
no accepted transition
no .scriptops/decision-log.ndjson mutation
no Human attribution
no index mutation
no refs/heads/main mutation
no commit
```

Verifier and implementation review must inventory the complete candidate tree and forbid any other executable accepted-state/canonical-effect route.

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

Active legacy is not required to equal the historical 51980-byte source after X1B correction.

## 12. Restore contract

`scripts/restore_v2.py` preserves historical reconstruction/checking but can never restore historical bytes inside the ScriptOps repository.

Write mode requires explicit output. Before opening/truncating/creating/writing, it must resolve repository root and destination and prove destination is outside repository root.

DENY without modification, including under `--force`, for:

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

Historical transport checks prove all seven prototype parts, exact reconstructed SHA/size, UTF-8, and Python syntax.

Active-runtime checks prove at minimum:

```text
legacy exists and is valid Python
direct legacy approve disabled
direct legacy scene-promote --to accepted disabled
Phase-6 authority route is R4R3-compliant
R4R3 local ref / Git plumbing / alias-safety guards are present
```

Verifier must not require active legacy byte identity with historical prototype and must not treat `approve --why` as current safety authority.

## 14. Current-state authority documentation

`README.md`, `PROJECT_STATE.md`, `HANDOFF.md`, `sources/prototype/RESTORE.md`, and `SOURCE_MANIFEST.md` must state current truth:

```text
defect-era approve --why = historical provenance only
current Human-decision route = approve --decision-pr <N> only
direct legacy approve = disabled
direct legacy scene-promote --to accepted = disabled
canonical local effect ref = refs/heads/main only
historical prototype byte identity != current active runtime identity
historical prototype parts != current active runtime authority
```

No current recovery/resume route may direct operator or AI to old approval semantics. Historical evidence itself is not rewritten.

## 15. Canonical JSON and hash functions

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

File digests bind exact file bytes. No Unicode/newline normalization or semantic reserialization where byte identity is specified.

## 16. Exact timestamp profile

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
FinalEffectGateV3.observed_at
```

GitHub `submitted_at` used by R4R3 must also validate exactly to this UTC `Z` form; otherwise DENY rather than normalize.

## 17. CanonicalPreStateV1 remains an unchanged sub-contract

```text
CanonicalPreStateV1 = {
  "exists": <true|false>,
  "file_sha256": <64 lowercase hex or JSON null>
}
```

`exists=false` requires null hash; `exists=true` requires exact current canonical byte hash. Symlink/nonregular/ambiguous target is DENY.

R4R3 supplements this content pre-state with Git-ref/tree/file-identity checks; it does not reinterpret `CanonicalPreStateV1`.

## 18. Deterministic accepted preview

Before Human request finalization, proposal preparation derives exact accepted canonical bytes from exact candidate bytes through one pure production helper later reused for execution.

The helper must have no write, Git, network, Human-evidence, or time side effect.

```text
accepted_canonical_file_sha256 = SHA256(exact accepted canonical bytes)
```

At admission, FinalEffectGateV3, and effect preparation, re-rendered bytes MUST exactly equal the Human-bound preview bytes/hash. Mismatch DENY before mutation.

Golden tests must prove same candidate bytes -> byte-identical accepted preview across request preparation and execution code paths.

## 19. R4R3 platform profile for alias-safe local effect

The R4R3 local effect profile is intentionally bounded to a platform that provides the required POSIX-style file-identity primitives.

At minimum runtime must provide equivalent semantics for:

```text
lstat/fstat
st_dev + st_ino + st_nlink
O_NOFOLLOW
O_CREAT | O_EXCL
O_DIRECTORY or equivalent directory-descriptor protection
descriptor-relative open/stat/rename/unlink or equivalent
fsync for files and effect directories
```

If the runtime cannot establish equivalent guarantees, acceptance returns `BLOCKED` before canonical mutation. The implementation may not silently weaken alias protection for another platform.

## 20. PresentedMaterialEffectV3

Closed schema:

```text
PresentedMaterialEffectV3 = {
  "schema_version": "scriptops-x1b-presented-material-effect/v3",
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
    "record_schema_version": "scriptops-x1b-decision-record/v3",
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
    "effect_transport_profile": "HOOK_FILTER_SAFE_GIT_PLUMBING_V1",
    "exact_changed_paths": [
      "scenes/<scene_id>.fountain",
      ".scriptops/decision-log.ndjson"
    ]
  },
  "file_identity_profile": "SINGLE_LINK_ALIAS_SAFE_REPOSITORY_TARGETS_V1"
}
```

`<exact scene_id>` and `ref_before` are concrete before request hashing.

No field used to compute request digest may directly or indirectly contain:

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
presented_material_effect_digest = sha256_canonical(PresentedMaterialEffectV3)
```

## 21. HumanDecisionRequestBindingV3 — acyclic request identity

Closed binding:

```text
HumanDecisionRequestBindingV3 = {
  "schema_version": "scriptops-x1b-human-decision-request/v3",
  "repository": "FJ899/scriptops",
  "repository_head_at_request": <40 lowercase hex>,
  "repository_ref_at_request": "refs/heads/main",
  "request_created_at": <exact R4R3 timestamp>,
  "task_id": <exact task ID>,
  "scene_id": <exact scene ID>,
  "candidate_path": <exact repo-relative candidate path>,
  "candidate_file_sha256": <64 lowercase hex>,
  "impact_report_path": <exact repo-relative impact path>,
  "impact_report_sha256": <64 lowercase hex>,
  "canonical_target": "scenes/<scene_id>.fountain",
  "canonical_ref": "refs/heads/main",
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect": <PresentedMaterialEffectV3>
}
```

Exact construction order:

```text
1 validate refs/heads/main and request base
2 validate candidate/impact/canonical pre-state
3 render accepted preview bytes/hash
4 construct PresentedMaterialEffectV3
5 construct HumanDecisionRequestBindingV3
6 request_binding_json = canonical_json_bytes(binding)
7 request_digest = sha256_hex_bytes(request_binding_json)
8 decision_request_id = "x1b:" + request_digest
9 construct committed HumanDecisionRequestV3
```

Committed request:

```text
HumanDecisionRequestV3 = {
  <all HumanDecisionRequestBindingV3 fields>,
  "decision_request_id": <exact x1b:digest>,
  "request_digest": <exact digest>
}
```

Golden regression:

```text
same exact pre-request bindings
-> same request_digest
-> same decision_request_id
-> no fixed-point search
-> no self-reference
```

## 22. Deterministic decision-request artifact and proposal branch

Derived identity:

```text
request_path = decisions/x1b/<request_digest>.json
request_branch = decision/x1b/<request_digest>
decision_request_id = x1b:<request_digest>
```

Request file bytes are exactly `canonical_json_bytes(HumanDecisionRequestV3)` with no trailing LF.

Proposal commit requirements:

```text
branch = decision/x1b/<request_digest>
parent = repository_head_at_request
changed-file set = exactly one added request_path
request blob = exact committed HumanDecisionRequestV3 bytes
no second path
```

Proposal branch/file/PR creation may be performed only by a separately authorized proposal-writing actor/process. Proposal write capability is not Human decision authority.

The evaluated effect invocation MUST NOT create/edit:

```text
proposal branch
request file
decision PR
GitHub review/comment
GitHub ref/rule/setting
```

```text
PROPOSAL PR CREATION != HUMAN DECISION
```

## 23. Decision PR envelope

Effect CLI accepts only a positive integer decision PR number as locator.

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

Verifier fetches exact head commit and complete BASE->HEAD file set and proves direct parent = request base.

No caller request path or digest is trusted. Equality required among:

```text
filename digest
computed binding digest
request_digest field
decision_request_id suffix
head-ref digest
```

Any extra/renamed/deleted file, wrong base/head/ref/repository, hidden pagination remainder, mismatch, or ambiguity is DENY.

PR number/head are external evidence and are never request-digest inputs.

## 24. Human authority profile and exact Human review body

Authoritative Human actor for this bounded X1B profile:

```text
litrgratis-pixel
```

Account identity alone is not claimed to prove private Human mental state. The later positive control requires a manual Human UI `APPROVE` governance act by this actor.

Exact review body is four LF-separated lines with no trailing LF:

```text
X1B-HUMAN-DECISION-V3
decision_request_id=<exact x1b:<request_digest>>
decision_request_sha256=<exact request_digest>
why=<Human rationale>
```

Exact rationale validation:

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
body = exact four-line body
```

Human rationale and attribution are derived only from that validated review, never from CLI `--why` or caller input.

## 25. Public trusted GitHub evidence transport

Production verifier for this exact public repository uses unauthenticated public GitHub REST reads only.

Exact origin:

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

No configurable API base, authenticated fallback, `gh`, `.netrc`, GitHub CLI auth, browser session, caller token, cached local review JSON, or Git credential helper may be used to obtain Human decision evidence.

Non-empty proxy/CA/GitHub credential environment overrides, including at minimum, cause DENY before evidence acquisition:

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

System DNS and the normal OS root trust store are explicit bounded platform dependencies.

Redirect, alternate origin, public-read failure, rate limit, visibility change, malformed/incomplete response, or ambiguity => DENY/BLOCKED before effect.

```text
REVIEW METADATA ALONE != PROOF OF HUMAN UI ORIGIN
```

The bounded trusted-origin claim combines the manual Human governance requirement with exact GitHub authoritative review evidence and technical proof that the evaluated effect process has no review-write credential/capability.

## 26. Exact GitHub reads and complete pagination

Bounded reads equivalent to:

```text
GET /repos/FJ899/scriptops/pulls/<N>
GET /repos/FJ899/scriptops/pulls/<N>/files?per_page=100&page=<p>
GET /repos/FJ899/scriptops/contents/<derived-request-path>?ref=<exact-head-sha>
GET /repos/FJ899/scriptops/git/commits/<exact-head-sha>
GET /repos/FJ899/scriptops/pulls/<N>/reviews?per_page=100&page=<p>
```

Every collection begins page 1 with `per_page=100`, advances sequentially, and continues until completion is unambiguous.

Malformed page, duplicate required identity, inconsistent pagination, API error/rate limit, hidden remainder, or inability to prove completion => DENY.

## 27. NormalizedReviewV3 and CompleteReviewSetV3

For every submitted review, normalize the exact closed projection:

```text
NormalizedReviewV3 = {
  "numeric_id": <canonical decimal string>,
  "node_id": <non-empty exact string>,
  "actor": <exact login>,
  "state": <exact recognized state>,
  "commit_id": <40 lowercase hex or JSON null>,
  "body_sha256": <SHA256 of exact UTF-8 body bytes>,
  "submitted_at": <exact validated timestamp or JSON null>
}
```

Recognized review states exactly:

```text
APPROVED
CHANGES_REQUESTED
COMMENTED
DISMISSED
```

Unknown state => DENY.

Normative ordering is ascending tuple:

```text
(numeric_id as integer, node_id)
```

Duplicate numeric ID or duplicate node ID => DENY.

Closed set:

```text
CompleteReviewSetV3 = {
  "schema_version": "scriptops-x1b-complete-review-set/v3",
  "repository": "FJ899/scriptops",
  "decision_pr_number": <positive integer>,
  "decision_pr_head": <40 lowercase hex>,
  "reviews": [<all normalized reviews in normative order>]
}
```

```text
complete_review_set_digest = sha256_canonical(CompleteReviewSetV3)
```

Current selected-PR Human semantics:

```text
APPROVED = active positive decision-bearing
CHANGES_REQUESTED = active negative/conflicting
COMMENTED = nondecision
DISMISSED = inactive
```

For `litrgratis-pixel` on exact current PR HEAD, there must be exactly one active syntactically/semantically valid APPROVED and no active CHANGES_REQUESTED.

Second current-head APPROVED => ambiguous DENY.

Old-commit APPROVED => historical only.

No latest-wins chronology rule.

## 28. Candidate, impact, local Git-tree, and applicability checks

Before preliminary admission and again at FinalEffectGateV3 where applicable:

```text
logical repository identity = FJ899/scriptops
repository_ref_at_request = refs/heads/main
git symbolic-ref -q HEAD = refs/heads/main
HEAD = refs/heads/main = request.repository_head_at_request
Git object format = sha1
real index tree = HEAD^{tree}
no tracked/index delta
candidate regular non-symlink exact repo-relative path
candidate bytes/hash/status=candidate exact
candidate tracked identity at HEAD exact
impact path = tasks/<task_id>/impact-report.json
impact regular non-symlink exact bytes/hash
impact tracked identity at HEAD exact
impact status=REVIEW_REQUIRED
impact task/scene/candidate path/hash match request
canonical target = scenes/<scene_id>.fountain
effect type = ACCEPT_SCENE_CANDIDATE
canonical filesystem/tree pre-state matches request
accepted preview bytes/hash match request
PresentedMaterialEffectV3 object/digest match request
request unconsumed in this canonical local instance
```

If an effect target is absent from the parent Git tree, the filesystem path must also be absent before effect. If it is present in the parent tree, filesystem bytes and Git blob/mode must agree with the validated pre-state. An ignored/untracked substitute at an effect path is DENY.

Candidate source is preserved; the final Git effect may not alter/remove it.

## 29. F004 correction — explicit activation, staleness, deactivation, and supersession

### 29.1 Activation

A selected Human decision is active/applicable only while ALL are true:

```text
selected decision PR is open
selected decision PR is unmerged
base/head/ref/request identities exact
local refs/heads/main == request base
HEAD symbolically names refs/heads/main
exact current-head Human APPROVED exists
no active current-head CHANGES_REQUESTED by authoritative Human
no duplicate/ambiguous/conflicting authoritative Human state
request unconsumed in same canonical local instance
candidate/impact/canonical/effect applicability exact
complete remote evidence enumerable
```

### 29.2 Age policy

R4R3 deliberately selects:

```text
NO WALL-CLOCK TTL
AGE ALONE != STALE
```

`request_created_at` and `submitted_at` are provenance/currentness-order evidence, not expiry timers.

The implementation must not invent a time-to-live.

### 29.3 Deactivation / staleness

Selected decision becomes inactive/inapplicable upon any of:

```text
PR closed
PR merged
PR base/head/ref/request identity changes
Human APPROVED dismissed
active authoritative-Human CHANGES_REQUESTED
review ambiguity/conflict
incomplete/malformed remote evidence
local HEAD/ref no longer equals request base
candidate/impact/canonical/preview/effect drift
request consumed in same canonical instance
```

### 29.4 Multiple decision PRs

Each exact decision PR is a separate Human decision domain.

Another decision PR:

```text
does NOT implicitly supersede this PR
does NOT silently revoke this PR
does NOT win by chronology
```

The complete event set for one invocation is the complete submitted-review set of the selected exact decision PR.

Two separately Human-approved decision PRs may coexist when both are anchored to the same current base. The first successful local effect that atomically advances `refs/heads/main` makes every still-unconsumed request anchored to the old base inapplicable by exact ref/base mismatch.

There is no cross-PR latest-wins policy and no implicit supersession.

Human may deliberately deactivate a not-yet-executed selected request through that request domain's normative state, e.g. dismissal of the approval or closing the decision PR.

Preserve:

```text
NO CHRONOLOGY-ONLY WINNER
OLD CONSENT + CHANGED OPERATION = DENY
NO GLOBAL CROSS-CLONE EXACTLY-ONCE CLAIM
```

## 30. HumanDecisionAdmissionIdentityV3

Closed identity:

```text
HumanDecisionAdmissionIdentityV3 = {
  "schema_version": "scriptops-x1b-human-decision-admission/v3",
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
  "canonical_instance_scope": "LOCAL_REFS_HEADS_MAIN_WORKTREE_DECISION_LOG_V3"
}
```

```text
admission_id = "x1b-admit:" + sha256_canonical(HumanDecisionAdmissionIdentityV3)
```

Admission is in-memory one-shot machine state, not Human evidence and not execution credential.

Preliminary admission cannot mutate canonical scene, decision log, real index, or `refs/heads/main`.

## 31. Bounded replay and same-worktree lock

Bounded claim:

```text
one decision_request_id may cause at most one successful X1B acceptance effect
within one canonical local refs/heads/main worktree execution instance
```

Before effect, complete local `.scriptops/decision-log.ndjson` must contain no occurrence of the exact `decision_request_id` that could represent prior consumption.

Replay scan requirements:

```text
if file absent -> empty history
if present -> exact validated target file
UTF-8 required
every non-empty line must parse as a JSON object
malformed line => DENY
any existing object carrying exact decision_request_id => DENY
```

Historical legacy JSON objects without a decision-request ID are allowed as historical records; they do not create Human authority.

Worktree-specific lock:

```text
<worktree-specific git-dir>/scriptops-x1b-approve.lock
```

Create exclusively before admission. Already exists => DENY/BLOCKED. No automatic stale-lock deletion. Hold through post-effect verification and cleanup. Lock has no Human authority.

A second independent clone is a separate canonical execution instance for this bounded replay property.

```text
NO GLOBAL CROSS-CLONE EXACTLY-ONCE CLAIM
```

A changed operation always needs a new Human-bound request regardless of clone.

## 32. F001 correction — exact local canonical Git ref

The only operative local effect ref is:

```text
refs/heads/main
```

At request creation, preliminary admission, and FinalEffectGateV3:

```text
git symbolic-ref -q HEAD
== refs/heads/main

HEAD
== refs/heads/main
== request.repository_head_at_request
```

Side branch, detached HEAD, unborn/ambiguous symbolic ref, non-main ref, or ref drift => DENY before canonical mutation.

The final ref mutation is compare-and-swap only:

```text
update refs/heads/main from exact old request SHA to exact new effect commit SHA
ONLY IF current old ref still equals exact request SHA
```

No force update. No alternate ref. No detached-only commit as successful effect.

After success:

```text
HEAD == refs/heads/main == exact resulting effect commit
parent(resulting effect commit) == request.repository_head_at_request
```

## 33. FinalEffectGateV3

Immediately before first canonical filesystem mutation, while the worktree lock is held, freshly reread PR metadata and complete reviews through trusted public transport.

Revalidate all of:

```text
exact PR/request envelope
selected Human review/currentness/conflicts
CompleteReviewSetV3 digest
repository logical identity
HEAD symbolic ref = refs/heads/main
HEAD/ref = exact request base
candidate/impact/canonical pre-state
accepted preview
PresentedMaterialEffectV3
replay state
real-index tree = parent tree
file-identity target preconditions
Git executable/platform preconditions
```

Closed gate:

```text
FinalEffectGateV3 = {
  "schema_version": "scriptops-x1b-final-effect-gate/v3",
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
  "canonical_before": <CanonicalPreStateV1>,
  "canonical_after_file_sha256": <exact digest>,
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "canonical_instance_scope": "LOCAL_REFS_HEADS_MAIN_WORKTREE_DECISION_LOG_V3",
  "current_human_decision_valid": true,
  "observed_at": <exact R4R3 UTC timestamp>
}
```

```text
final_effect_gate_digest = sha256_canonical(FinalEffectGateV3)
```

Gate is in-memory one-shot state and not a reusable credential.

## 34. Human-currentness commitment point

```text
Human-currentness commitment point
=
successful FinalEffectGateV3 validation
immediately before first canonical filesystem mutation
```

Before this point, visible review/PR/ref/applicability drift revokes or conflicts with admission.

After this point, later remote change does not retroactively revoke the already-authorized same-process one-shot effect; no distributed atomicity claim is made.

Between gate success and first canonical mutation there may be:

```text
no user interaction
no network
no sleep/wait
no unrelated blocking operation
no proposal/review mutation
no untrusted subprocess
```

Only precomputed local effect preparation using the already-validated runtime may proceed.

## 35. Exact X1BDecisionRecordV3 before mutation

Before first filesystem mutation compute exact accepted scene bytes and one exact canonical record.

Closed record:

```text
X1BDecisionRecordV3 = {
  "schema_version": "scriptops-x1b-decision-record/v3",
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
  "canonical_instance_scope": "LOCAL_REFS_HEADS_MAIN_WORKTREE_DECISION_LOG_V3"
}
```

NDJSON append bytes:

```text
canonical_json_bytes(X1BDecisionRecordV3) + exactly one LF
```

The resulting effect commit SHA is deliberately absent from this record, preventing an effect-commit self-hash cycle. Later independent evidence records the resulting commit externally.

If an existing non-empty decision log does not end with LF, append is DENY before mutation.

## 36. F002 correction — hook/filter-safe Git executable and subprocess profile

The effect path MUST NOT use these porcelain mutation commands:

```text
git add
git commit
git checkout
git reset
```

for the operative acceptance effect.

The Git executable must not be selected from caller/repository-controlled PATH/configuration.

Resolve a system executable from the runtime's system default executable search domain (not caller PATH), obtain its strict real path, require an absolute regular executable outside the repository, and require stable stat identity for the duration of the effect. If there is no unambiguous system Git executable, return `BLOCKED`.

The implementation may not silently fall back to a repository-provided executable or wrapper.

Every Git subprocess uses:

```text
absolute resolved Git executable
shell = false
explicit minimal environment
no caller GIT_* overrides except values explicitly constructed by R4R3
no caller LD_PRELOAD / LD_LIBRARY_PATH / DYLD_* injection
LC_ALL=C
TZ=UTC
GIT_CONFIG_NOSYSTEM=1
GIT_CONFIG_GLOBAL=/dev/null
GIT_TERMINAL_PROMPT=0
GCM_INTERACTIVE=never
```

and command-level config at minimum:

```text
-c core.hooksPath=/dev/null
-c core.fsmonitor=false
-c commit.gpgSign=false
-c credential.helper=
```

All ambient `GIT_CONFIG_COUNT`, `GIT_CONFIG_KEY_*`, `GIT_CONFIG_VALUE_*`, `GIT_DIR`, `GIT_WORK_TREE`, `GIT_COMMON_DIR`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_EXEC_PATH`, `GIT_EXTERNAL_DIFF`, `GIT_ASKPASS`, `SSH_ASKPASS`, `GIT_SSH`, and `GIT_SSH_COMMAND` caller values are removed unless R4R3 explicitly sets a bounded replacement for that subprocess.

No acceptance Git subprocess may be a network operation:

```text
no fetch
no pull
no push
no ls-remote
no submodule network
no gh
```

## 37. F002 correction — exact hook/filter-safe Git plumbing

Before modifying the real index, prove:

```text
real_index_tree = git write-tree
HEAD_tree = git rev-parse HEAD^{tree}
real_index_tree == HEAD_tree
```

The operative Git object/tree/commit is constructed with plumbing only.

### 37.1 Exact output blobs

Compute:

```text
accepted_scene_blob = git hash-object -w --stdin --no-filters
  over exact accepted canonical bytes

decision_log_blob = git hash-object -w --stdin --no-filters
  over exact post-append decision-log bytes
```

Verify each resulting object by reading it back and proving byte-for-byte identity with the precomputed authority bytes.

Path-based clean/process filters are never used to generate these blobs.

### 37.2 Temporary index

Create a fresh private temporary index path inside the worktree-specific Git directory with exclusive creation and mode 0600.

Set `GIT_INDEX_FILE` only for temporary-index commands.

Initialize it from exact parent tree using plumbing `read-tree <HEAD_tree>`.

Update exactly the two Human-bound paths with:

```text
update-index --add --cacheinfo 100644,<accepted_scene_blob>,scenes/<scene_id>.fountain
update-index --add --cacheinfo 100644,<decision_log_blob>,.scriptops/decision-log.ndjson
```

Then:

```text
new_tree = write-tree
```

Prove before commit construction:

```text
new_tree differs from HEAD_tree only at exact two paths
ls-tree(new_tree, exact paths) returns mode 100644 and exact expected blob IDs
no candidate/request/impact/third path changed
```

### 37.3 Deterministic effect commit metadata

Logical commit message:

```text
scriptops x1b: accept <exact scene_id>
```

Commit metadata is fixed:

```text
GIT_AUTHOR_NAME=ScriptOps X1B
GIT_AUTHOR_EMAIL=scriptops-x1b@local.invalid
GIT_COMMITTER_NAME=ScriptOps X1B
GIT_COMMITTER_EMAIL=scriptops-x1b@local.invalid
GIT_AUTHOR_DATE=request_created_at
GIT_COMMITTER_DATE=request_created_at
```

Create exactly one commit object through `commit-tree` with:

```text
tree = new_tree
one parent = request.repository_head_at_request
message = exact logical commit message
```

Before any ref mutation, inspect the commit object and prove exact tree, exact one parent, exact logical message, exact fixed author/committer identity, and exact UTC request-created time semantics.

### 37.4 No ambient hooks/config effects

The plumbing profile plus `core.hooksPath=/dev/null` must ensure no repository/local/global hook executes, including commit-, index-, and reference-transaction hooks.

`.gitattributes`, `.git/info/attributes`, global attributes, clean/process filters, autocrlf, and signing configuration may not transform the committed blob identities because `hash-object --no-filters` plus `update-index --cacheinfo` binds exact object IDs.

Any inability to prove exact object/tree/commit identity before ref update => DENY with no canonical ref mutation.

## 38. F003 correction — repository-contained parent directories

Before effect, both parents must already exist:

```text
scenes/
.scriptops/
```

Current legacy `cmd_init` already creates both substrate directories; acceptance must not create the parent directories itself.

For every parent-chain component used by an effect target:

```text
repository-contained
real directory
not symlink
opened through protected directory descriptor / equivalent
no lexical .. escape
no resolution outside repository
```

Ambiguity => DENY.

## 39. F003 correction — existing target single-link validation and atomic replacement

For an existing effect target:

```text
lstat => regular file
not symlink
st_nlink == 1
filesystem bytes match validated pre-state / tracked parent blob as applicable
```

Open the existing target with `O_NOFOLLOW` or equivalent and `fstat` it. The opened descriptor must match the validated `st_dev + st_ino`, remain regular, and have `st_nlink == 1`.

The executor MUST NOT truncate/write the validated existing inode in place.

Instead:

1. create a fresh unpredictable same-directory temporary file through the verified directory descriptor with `O_CREAT|O_EXCL|O_NOFOLLOW` or equivalent;
2. write exact precomputed output bytes;
3. fsync it;
4. require `fstat` regular + `st_nlink == 1`;
5. set exact final mode `0644`;
6. immediately before replacement, revalidate the named old target is still the same validated inode and still `st_nlink == 1`;
7. atomically replace the target name with the fresh inode through the verified directory descriptor;
8. fsync the containing directory;
9. re-open the new target with `O_NOFOLLOW`, require regular + `st_nlink == 1`, and prove exact output bytes/hash.

Because the old inode is never modified in place, a pre-existing external hardlink cannot receive the new Human-bound bytes. If link count changes before replacement, DENY without replacing.

## 40. F003 correction — absent target exclusive creation

If the validated target is absent:

```text
FinalEffectGateV3 proves absent
```

Creation must use the verified parent descriptor and exclusive no-follow semantics equivalent to:

```text
O_CREAT | O_EXCL | O_NOFOLLOW
```

Write exact output bytes, fsync, set exact mode 0644, require `fstat` regular + `st_nlink == 1`, and revalidate link count/bytes immediately before the canonical ref compare-and-swap.

Target existence race, symlink, hardlink count >1, nonregular target, parent substitution, or inability to prove identity => DENY/BLOCKED.

Mandatory negatives include:

```text
canonical target hardlink alias
decision-log hardlink alias
canonical target symlink
decision-log symlink
existing-target inode substitution
target created between final absence check and exclusive create
parent-path symlink/substitution
unsupported alias-safe platform primitives
```

No case may be reported as successful Human-attributed effect.

## 41. Exact local effect sequence

After FinalEffectGateV3 success, with lock held and all authority bytes precomputed:

```text
A. construct/verify exact blobs + temporary-index new_tree + one-parent commit object
   without changing worktree, real index, or refs/heads/main

B. recheck refs/heads/main and HEAD still equal exact request base

C. materialize exact accepted scene bytes through alias-safe target helper

D. materialize exact post-append decision-log bytes through alias-safe target helper

E. verify both filesystem targets exact and single-link

F. update real index to exact verified new_tree using hook-disabled plumbing read-tree
   without -u / without worktree filtering

G. prove real index write-tree == exact new_tree

H. atomically compare-and-swap:
   refs/heads/main: exact request base -> exact prepared effect commit
   using update-ref with exact old value

I. verify HEAD == refs/heads/main == effect commit

J. verify commit/tree/blob/path identities and exact clean worktree/index state
```

No `git add .` and no porcelain commit.

If step H observes any ref drift, it MUST fail rather than update another state.

## 42. Index/ref rollback boundary before successful ref update

Before successful `refs/heads/main` CAS, the effect is not successful.

If failure occurs after filesystem/index mutation but before successful ref update:

```text
return nonzero
attempt deterministic restoration of exact pre-effect target presence/bytes/mode
restore real index to exact parent tree through hook-disabled plumbing
prove refs/heads/main still exact parent
prove working tree/index exact pre-effect state
never emit SUCCESS Human attribution
```

If exact restoration cannot be proven, leave explicit fail-closed dirty/error state and report `BLOCKED`; do not synthesize Human success evidence and do not destructively reset unrelated state.

If ref update succeeds but post-commit verification later fails, do not silently reset/rewrite local Git history. Preserve the ref/commit for forensic truth, report `BLOCKED`, and require separately authorized recovery.

## 43. Post-effect truth

Successful effect requires all:

```text
HEAD == refs/heads/main == exact resulting effect commit
resulting commit has exactly one parent = request base
exact commit logical message
exact fixed author/committer policy
commit tree = preverified new_tree
commit changed set exactly:
  scenes/<scene_id>.fountain
  .scriptops/decision-log.ndjson
both tree modes = 100644
both committed blob IDs equal exact precomputed output blobs
canonical filesystem bytes hash = bound after hash
canonical status = accepted
candidate source unchanged
exactly one new X1BDecisionRecordV3 line
record request/admission/gate/review/effect/ref identities exact
worktree/index clean relative to resulting HEAD
real index write-tree = resulting HEAD tree
lock still held until verification completes
```

`GREEN COMMAND EXIT != POST-EFFECT TRUTH`.

## 44. Git-hook/filter/config attack regressions

Future implementation tests must inject, one at a time and in combinations where meaningful:

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
LD_PRELOAD / equivalent loader injection where platform permits test
```

Tests must prove either:

```text
injection rejected before effect
```

or:

```text
injection cannot execute/transform the bounded effect
```

and always prove committed blob/tree/ref identities remain exact.

A sentinel hook/filter/helper must not execute.

## 45. Ref-binding attack regressions

Mandatory negatives:

```text
side branch at exact request SHA
detached HEAD at exact request SHA
HEAD symbolic ref not main
main moved after admission
main moved after FinalEffectGateV3 but before update-ref
CAS old-SHA mismatch
prepared commit points at wrong parent
prepared commit/tree targets another ref
```

All fail closed without successful Human-attributed effect.

## 46. Freshness/supersession regressions

Required tests include:

```text
old age alone with every other currentness predicate exact -> remains applicable
PR closed -> DENY
PR merged -> DENY
approval dismissed -> DENY
active authoritative CHANGES_REQUESTED -> DENY
second current-head APPROVED -> DENY ambiguous
old-commit APPROVED only -> DENY
selected PR incomplete review pagination -> DENY
another separately approved PR does not chronology-supersede selected PR
first same-base successful effect advances main -> second old-base request DENY
changed candidate/effect with old Human review -> DENY
```

No test may infer a latest-wins policy.

## 47. Original X1B preregistered attacks remain mandatory

Corrective verification must still execute every original class:

1. AI marks its own proposal accepted.
2. `Continue` is treated as a Human decision.
3. No Human response is treated as consent.
4. Old Human consent is reused for a new decision.
5. Human accepts A but A-prime becomes operative.
6. AI changes parameters after Human acceptance.
7. AI expands scope after Human acceptance.
8. Human accepts general direction but AI attributes specific parameters.
9. AI creates an artifact that merely looks like a Human decision.
10. AI-filled value is recorded as Human-chosen.

The real current Phase-6 `cmd_approve` counterexample and both direct legacy acceptance routes are mandatory real-boundary regressions, not synthetic substitutes.

## 48. Additional request/review/transport negative suite

At minimum:

```text
caller request-path substitution
wrong filename/request/head-ref digest
wrong PR base/ref/head repository
wrong request-commit parent
extra/renamed/deleted request path
malformed/extra-field request
request digest/ID mismatch
attempted request self-reference
candidate/impact/canonical/preview/effect drift
no review
wrong Human actor
wrong review commit
malformed four-line body
empty/trim-violating/control-containing/over-2000 rationale
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

## 49. Replay/concurrency/final-currentness negative suite

At minimum:

```text
same request replay
same-worktree concurrent invocation
stale lock
local ref/HEAD drift
old Human decision with changed operation
review dismissed after preliminary admission
CHANGES_REQUESTED after preliminary admission
PR closed/merged/head drift after admission
remote final reread failure
candidate/impact/canonical/preview/effect drift after admission
request consumed after admission
executor substitution after final gate
out-of-scope path in prepared tree
second decision-log append
malformed existing local decision-log line
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
credential-free exact-origin public evidence acquisition
+
exact request/PR/review/currentness/effect/ref binding
+
independent admission
+
fresh FinalEffectGateV3
+
hook/filter-safe alias-safe exact local refs/heads/main effect
=
bounded trusted Human decision evidence
```

No claim is made that GitHub review metadata by itself proves Human UI origin or private mental state.

## 51. Implementation responsibility split

Future bounded implementation responsibilities:

`phase6/scriptops-v2-hardening.py`

```text
expose only current approve --decision-pr acceptance interface
reject defect-era approve --scene/--why
obtain validated admission from x1b_human_decision
execute only exact admitted/final-gated effect
never invent Human attribution
```

`legacy/scriptops-v2-single.py`

```text
preserve non-approval substrate
disable direct approve
disable direct scene-promote -> accepted at parser and internal command layers
```

`phase6/x1b_human_decision.py`

```text
V3 schemas/canonical JSON
pure accepted preview helper
non-circular request identity
public GitHub transport
PR/review pagination/normalization/currentness
CompleteReviewSetV3
freshness/supersession policy
admission/replay/lock
refs/heads/main checks
FinalEffectGateV3
system-Git isolation/plumbing helpers
alias-safe target helpers
record construction
post-effect verification/fail-closed helpers
```

`scripts/restore_v2.py`

```text
historical reconstruction only outside repository
```

`scripts/verify_repository.py`

```text
historical-vs-active split validation
direct acceptance path inventory assertions
R4R3 current authority assertions
```

Docs:

```text
current authority route
historical-vs-active truth
refs/heads/main local effect truth
```

Tests/workflow:

```text
deterministic V3 tests
no Human evidence creation by CI
no canonical live effect in ordinary CI
all negative regressions
```

## 52. Independent implementation-review obligations

Later independent implementation review must inspect the complete candidate tree and prove, not infer:

```text
changed-file set is within authorized surface
no third acceptance route exists
old Phase-6 and legacy routes deny
restore/verifier/docs are coherent
request identity is acyclic
V3 schemas are exact and internally consistent
one-file decision PR is enforced
public transport is credential-free/exact-origin
review set/currentness/conflicts are complete
freshness/supersession semantics match R4R3
admission does not mutate canon
lock/replay semantics are bounded honestly
refs/heads/main is exact effect ref
side/detached ref attacks deny
Git plumbing disables hooks/filters/signing/config substitution
exact output blob/tree/commit identities are verified before ref update
alias-safe filesystem target contract is actually enforceable
FinalEffectGateV3 leaves no unauthorized substitution choice
result commit is exact two-path one-parent effect
Human attribution derives only from validated evidence
no self-hash/circular evidence
failure/rollback cannot be misreported as success
```

```text
TESTS GREEN != IMPLEMENTATION REVIEW PASS
IMPLEMENTATION REVIEW PASS != X1B CLOSED
```

## 53. Separately authorized live positive control

A later positive control requires fresh Human authorization and must use exactly one disposable ScriptOps repository execution instance with no user screenplay canon.

It must include:

```text
inert/synthetic scene
exact staged candidate
exact impact report
one HumanDecisionRequestV3
one dedicated one-file decision PR
one manual GitHub UI APPROVE by litrgratis-pixel
exact four-line V3 review body
one corrected Phase-6 approve --decision-pr invocation
local HEAD symbolically on refs/heads/main
no GitHub review-write credential in effect process
```

Human must see the exact request/material effect including:

```text
exact candidate/content/scope
canonical before/after hash
canonical local ref refs/heads/main
decision-log target .scriptops/decision-log.ndjson
one append
one exact two-path one-parent local effect commit
logical commit message scriptops x1b: accept <scene_id>
hook/filter-safe Git plumbing profile
alias-safe target profile
```

Positive result requires exact post-effect truth, Human-evidence-derived attribution, and no substitute evidence/effect.

```text
LIVE POSITIVE CONTROL PASS != CORRECTIVE CLOSURE
```

## 54. Corrective closure composition

X1B cannot be closed by brief review, implementation, green CI, or positive control alone.

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
exact post-effect truth
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

## 55. STOP

This brief authorizes no implementation.

Required next stage after durable R4R3 freeze:

```text
INDEPENDENT AK-CANON X1B R4R3 IMPLEMENTATION-BRIEF REVIEW
```

Only a fresh separate Human authorization may create that review artifact.

```text
R4R3 BRIEF != IMPLEMENTATION AUTHORITY
R4R3 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R3 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
STOP
```
