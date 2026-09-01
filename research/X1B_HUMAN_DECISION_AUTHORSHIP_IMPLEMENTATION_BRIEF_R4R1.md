# X1B HUMAN DECISION AUTHORSHIP — CLEAN IMPLEMENTATION BRIEF R4R1

Status: `CLEAN R4R1 REMATERIALIZATION / BRIEF ONLY / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-01`

## 1. Authority, purpose, and STOP boundary

This document is a clean rematerialization of the X1B Human Decision Authorship implementation brief after recovery from the R4 execution-trace deviation.

It is prepared under explicit Human authorization and is bound to the recovered `FJ899/8` repository state.

This artifact is an implementation brief only.

It authorizes no ScriptOps implementation, no Human decision PR, no GitHub review creation, no live positive control, no canonical screenplay effect, no merge, no X1B closure, no Agency Kernel v1, no release, no deployment, and no tag.

Preserve:

```text
R4R1 BRIEF != IMPLEMENTATION AUTHORITY
R4R1 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R1 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

After durable freeze of this brief, STOP. The next stage is a separately Human-authorized independent AK-CANON R4R1 implementation-brief review.

## 2. Exact governance lineage

### 2.1 Accepted corrective design

```text
FJ899/scriptops PR #34
HEAD = d7a5065c87e9a4b49fb608235c908bceac42b4b1
TREE = 3140d0ac95c120a7b1532942bae2e0dad38b4839
PATH = governance/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_CANDIDATE.md
BLOB = dac16f109d1414a2208c2ed9a166ae9e9a329216
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

### 2.3 Binding R3 implementation-brief NOT-PASS review

```text
FJ899/8 PR #115
HEAD = 0d984b97a88f6ee9d4267a88a3fbddca2168002e
TREE = f3092635c6f018fead19c364c0014e2478b88a3a
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R3_AK_CANON_REVIEW.md
BLOB = 24aa423dad9ce181dc239fa616be6ea34ce6d2aa
VERDICT = AK-CANON X1B SUPERSEDING IMPLEMENTATION-BRIEF R3 REVIEW = NOT PASS
```

R4R1 directly addresses the four findings frozen there:

```text
R3-F001 CURRENT-STATE AUTHORITY SURFACE INCOMPLETE
R3-F002 NORMATIVE INHERITANCE AMBIGUOUS
R3-F003 PRESENTED MATERIAL EFFECT SCHEMA UNDEFINED
R3-F004 COMPLETE REVIEW SET DIGEST UNDER-SPECIFIED
```

### 2.4 Historical R4 provenance candidate — not authority

The pre-recovery R4 candidate is preserved unchanged only as provenance/input:

```text
FJ899/8
branch = brief/x1b-human-decision-authorship-implementation-brief-r4-20260901
HEAD = c0bbaaa568215fa1d53b36acfacb4bce5d3c1fcc
TREE = 2bbbe3dbe86c4aed726581103122eb57bf4a2e3e
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4.md
BLOB = 34f21ead0e72c21ad3e98b72fe7503ceb9330c29
```

It has no implementation authority and is not adopted as the R4R1 contract.

R4R1 intentionally corrects material problems in that provenance artifact, including:

- the wrong runtime decision-log target `DECISION_LOG.md` instead of `.scriptops/decision-log.ndjson`;
- a circular request object that attempted to include decision-PR number/HEAD before the proposal PR could exist;
- incomplete preservation of the previously reviewed transport, replay, Human review, and admission semantics;
- use of an accepted-after hash definition that did not match the actual candidate-to-accepted rendering operation.

## 3. Recovered evidence-repository base

R4R1 is prepared from exact recovered `FJ899/8` base:

```text
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

The recovered TREE equals the pre-deviation TREE, while the recovered HEAD is intentionally a new forward-recovery commit.

```text
RECOVERED TREE == PRE-DEVIATION TREE
DOES NOT MEAN
RECOVERED HEAD == PRE-DEVIATION HEAD
```

The unauthorized deviation and its forward recovery remain visible in repository history. R4R1 does not rewrite that history.

## 4. Frozen ScriptOps defect baseline

The implementation described by this brief is bound to exact current ScriptOps baseline:

```text
FJ899/scriptops main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Security-relevant current BLOBs:

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

Historical prototype transport parts are immutable under the future implementation:

```text
sources/prototype/scriptops-v2-single.py.part01 e002ab21b5b353c269e6d14e0d333916b3d07818
sources/prototype/scriptops-v2-single.py.part02 35906edee1f2c1b75d70bbb0cb9ead0199e443c8
sources/prototype/scriptops-v2-single.py.part03 c4b8fa5ada556a997734cf0ff42ebd4e8eaf31dd
sources/prototype/scriptops-v2-single.py.part04 94a6685337d340fc76cdd6ecc3a2ff02c0041220
sources/prototype/scriptops-v2-single.py.part05 d25574f78a44295333558ac00c40891da1f998de
sources/prototype/scriptops-v2-single.py.part06 86201706c82bca912a77187330e84b2b5c1f461a
sources/prototype/scriptops-v2-single.py.part07 e9e67feb2e9f42f34301853845ffcafa9ea27f5f
```

Their reconstructed historical artifact remains:

```text
SHA-256 = 881dade6c6c506b9a9d41ebfbf68afb18b66db7583d35f746fb29ed7b36ac596
SIZE = 51980 bytes
```

## 5. Normative precedence — R4R1 is self-contained

The exact precedence rule is:

```text
R4R1 TEXT = CURRENT IMPLEMENTATION-BRIEF AUTHORITY
R4 / R3 / R2 / R1 = HISTORICAL INPUT ONLY
```

No authority/security rule may be inferred merely because an older brief said that a requirement was preserved, remained unchanged, or was previously frozen.

Every authority-critical requirement needed to implement X1B is restated in R4R1.

If R4R1 conflicts with an earlier implementation brief, R4R1 controls for the future implementation candidate, while the accepted corrective design PR #34 remains the higher-level normative property contract.

`HISTORICAL INPUT != CURRENT IMPLEMENTATION AUTHORITY`

## 6. Exact future implementation surface

Any later implementation authorization based on this brief must be bounded to the following expected paths:

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

Expected unchanged paths include:

```text
.github/workflows/phase6-scriptops-smoke.yml
.github/workflows/verify-repository.yml
sources/prototype/scriptops-v2-single.py.part01..part07
```

A later independent implementation review may find that a smaller final changed-file set satisfies every R4R1 obligation. Silent expansion beyond the R4R1 implementation surface is prohibited.

If an additional path becomes technically necessary, implementation must STOP and obtain new Human authorization before changing it.

## 7. Core Human-decision property

The operative rule is:

```text
HumanDecision = TRUE
ONLY IF
separate trusted Human decision evidence
for the exact current content + scope + candidate + material effect
is independently validated and admitted.
```

The following are individually insufficient and must never establish Human decision authorship:

```text
approval command possession
non-empty --why
caller-provided rationale
continuation
silence
AI-authored decision record
AI-created proposal artifact
AI-created PR
AI-created comment
identity label
hard-coded approver="human"
CI success
mergeability
green tests
presence of an effect credential
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

## 8. One operative current acceptance path

After the future implementation, the only current effect-capable Human-decision acceptance interface is:

```text
python phase6/scriptops-v2-hardening.py approve --decision-pr <positive-integer>
```

The PR number is a locator only. It is not authority.

The command accepts no caller-controlled semantic authority field for:

```text
Human actor
Human decision result
Human rationale
request path
request digest
task ID
scene ID
candidate path
candidate hash
impact-report path/hash
canonical target
effect type
material effect
```

The defect-era `approve --scene ... --why ...` path must be rejected as an obsolete current approval interface.

Caller text may not be relabeled as Human rationale. If any non-authoritative operator note is retained in a future CLI, it must be clearly named and recorded as non-Human metadata and must not affect admission. R4R1 does not require such a note.

Required invariant:

```text
ONE OPERATIVE ACCEPTANCE EFFECT PATH
=
X1B-VALIDATED PHASE6 PATH
```

## 9. Direct legacy approval is permanently fail-closed

The current executable legacy substrate contains a direct `approve --scene` path that can write a canonical scene, append `.scriptops/decision-log.ndjson`, commit the effect, and hard-code `approver = "human"` without trusted Human-decision evidence.

The future implementation must make that direct legacy `approve` path deterministically non-effect-capable.

An invocation equivalent to:

```text
python legacy/scriptops-v2-single.py approve --scene SCN-XYZ
```

must terminate nonzero before any:

```text
canonical scene write
candidate status/effect transition
.scriptops/decision-log.ndjson append
Human attribution
Git staging
Git commit
```

Legacy must not delegate this direct invocation into the current effect path without the full R4R1 decision-PR/admission/final-gate path.

The compatibility error may point the operator to the Phase-6 `approve --decision-pr` interface.

Required regression:

```text
SAFE NEW PATH + EXECUTABLE UNSAFE LEGACY PATH = NOT CLOSED
```

## 10. Historical transport and active runtime are different authorities

R4R1 freezes:

```text
sources/prototype/scriptops-v2-single.py.part01..part07
=
IMMUTABLE HISTORICAL TRANSPORT / RECONSTRUCTION EVIDENCE

legacy/scriptops-v2-single.py
=
ACTIVE REVIEWED RUNTIME SUBSTRATE
```

The active runtime is not required to remain byte-identical to the historical 51980-byte artifact after X1B correction.

Historical reproducibility is preserved separately from active-runtime safety.

```text
HISTORICAL TRANSPORT REPRODUCIBLE
+
ACTIVE RUNTIME CORRECTED
```

not:

```text
ACTIVE RUNTIME == HISTORICAL UNSAFE BYTES
```

## 11. Restore contract — historical bytes can never reactivate active unsafe code

Future `scripts/restore_v2.py` must retain exact reconstruction and integrity validation of the seven immutable historical parts.

It must not have a default output inside the ScriptOps repository.

Write-mode historical reconstruction must require an explicit output path.

Before opening, truncating, creating, or writing the selected output, the tool must resolve the repository root and destination and prove that the destination is outside the repository root.

The following must fail closed with no target modification, including under `--force`:

```text
python scripts/restore_v2.py --output legacy/scriptops-v2-single.py --force
```

The same prohibition applies to:

```text
absolute repository-internal paths
relative aliases
.. traversal resolving into the repository
symlink-mediated destinations resolving into the repository
repository root itself
```

If destination safety cannot be established unambiguously, deny.

`--check-only` may reconstruct and validate historical bytes in memory without writing them.

Explicit reconstruction to a path outside the repository remains allowed as a historical recovery operation.

That reconstructed file is historical evidence, not active ScriptOps runtime authority.

```text
HISTORICAL RESTORABILITY != AUTHORITY TO RESTORE UNSAFE ACTIVE CODE
```

## 12. Repository verifier split-source contract

Future `scripts/verify_repository.py` must verify historical transport and active runtime separately.

Historical transport checks must prove:

```text
all seven historical part files exist
reconstructed SHA-256 = 881dade6c6c506b9a9d41ebfbf68afb18b66db7583d35f746fb29ed7b36ac596
reconstructed size = 51980 bytes
historical bytes are UTF-8
historical source compiles as Python
```

Active runtime checks must prove:

```text
legacy/scriptops-v2-single.py exists
active runtime is valid UTF-8/Python
current direct legacy approve is fail-closed
current Phase-6 authority model is R4R1-compliant
```

The verifier must not require active legacy bytes/hash/size to equal the historical reconstructed artifact.

It must remove defect-era executable requirements such as current `approve --why` and `test_approve_requires_explicit_why` markers.

It must also verify current-state documentation consistency and R4R1-specific deterministic tests described below.

The existing `.github/workflows/verify-repository.yml` is expected to remain structurally unchanged and to continue running the corrected verifier.

## 13. Current-state authority files

Future implementation must update:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
```

so that their current/recovery truth agrees with the corrected executable model.

They may preserve historical Phase-6 provenance, but their current operational rule must state unambiguously:

```text
defect-era approve --why = historical provenance only
current Human-decision route = approve --decision-pr <N> only
direct legacy approve = disabled for current Human-decision attribution
"legacy unchanged" = historical baseline statement, not current active-runtime byte identity
```

No current recovery/resume route may instruct an operator or AI process to treat `approve --why` as the current Human-decision mechanism.

Historical provenance must not be erased or rewritten to claim that the defect never existed.

## 14. SHA-256 field convention

Unless a field is explicitly described as a legacy prefixed hash, every R4R1 field whose name ends in `_sha256` contains exactly 64 lowercase hexadecimal SHA-256 characters and no `sha256:` prefix.

Raw file SHA-256 values are computed over exact file bytes.

Current legacy helpers may expose prefixed values such as:

```text
sha256:<64 lowercase hex>
```

Where a current impact report contains such a legacy-prefixed value, the verifier must require exact equality to:

```text
"sha256:" + <R4R1 64-hex value>
```

No Unicode normalization, newline normalization, or semantic reserialization is permitted when a byte digest is specified.

## 15. Canonical JSON contract

All R4R1 authority-critical canonical objects use this exact serialization contract:

```text
encoding = UTF-8
root/child objects = JSON objects as defined by the relevant schema
object keys = sorted lexicographically by Unicode code point
separators = ',' and ':'
insignificant whitespace = none
indentation = none
trailing newline = none
NaN = forbidden
Infinity = forbidden
floating point values = forbidden
booleans/null/integers = normal JSON literals
strings = standard JSON escaping
Unicode normalization = none
```

Equivalent implementation expression:

```text
canonical_json_bytes(X)
=
UTF-8 bytes of JSON serialization of X
with sort_keys=True, separators=(",", ":"), ensure_ascii=False,
allow_nan=False, and no trailing newline,
subject to the R4R1 closed-schema/type checks.
```

The serialization library is not authority; conformance to these exact output bytes is authority.

Define:

```text
sha256_hex_bytes(B) = lowercase hex SHA-256(B)
sha256_canonical(X) = sha256_hex_bytes(canonical_json_bytes(X))
```

Golden-vector tests must freeze exact bytes and digests.

## 16. HumanDecisionRequestV1 — non-circular binding payload

A Human decision request must exist before Human review and before the decision PR number can be authority-bearing evidence.

Therefore the request digest MUST NOT contain:

```text
decision PR number
decision PR HEAD SHA
review identity
admission identity
final effect gate identity
```

The exact binding payload is:

```text
HumanDecisionRequestBindingV1 = {
  "schema_version": "scriptops-x1b-human-decision-request/v1",
  "repository": "FJ899/scriptops",
  "repository_head_at_request": <40 lowercase hex commit SHA>,
  "request_created_at": <offset-aware UTC timestamp string>,
  "task_id": <exact task ID>,
  "scene_id": <exact scene ID>,
  "candidate_path": <exact repo-relative candidate path>,
  "candidate_file_sha256": <64 lowercase hex>,
  "impact_report_path": <exact repo-relative impact-report path>,
  "impact_report_sha256": <64 lowercase hex>,
  "canonical_target": "scenes/<scene_id>.fountain",
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect": <PresentedMaterialEffectV1>
}
```

Request identity is:

```text
request_binding_json = canonical_json_bytes(HumanDecisionRequestBindingV1)
request_digest = sha256_hex_bytes(request_binding_json)
decision_request_id = "x1b:" + request_digest
```

The committed request object is exactly:

```text
HumanDecisionRequestV1 = {
  <all HumanDecisionRequestBindingV1 fields>,
  "decision_request_id": <exact decision_request_id>,
  "request_digest": <exact request_digest>
}
```

The verifier reconstructs the binding payload from the committed object, recomputes the digest/ID, and requires exact equality.

`DECISION REQUEST != HUMAN DECISION`

## 17. Candidate and impact binding rules

The request-building/validation contract must prove from the exact local ScriptOps worktree:

```text
repository identity = FJ899/scriptops
working tree clean
local HEAD = repository_head_at_request
candidate_path is normalized repo-relative POSIX path
candidate_path has no leading slash, '.', '..', or symlink substitution
candidate is a regular non-symlink file
candidate lives under staging/scenes/
candidate scene_id = request scene_id
candidate status = candidate
candidate exact bytes SHA-256 = candidate_file_sha256
impact_report_path = tasks/<task_id>/impact-report.json
impact report is regular non-symlink file
impact report exact bytes SHA-256 = impact_report_sha256
impact report status = REVIEW_REQUIRED
impact report task_id/scene_id/candidate path/candidate hash match the request
canonical_target = scenes/<scene_id>.fountain
effect_type = ACCEPT_SCENE_CANDIDATE
```

For the current Phase-6 impact schema, if `impact.candidate.file_sha256` uses legacy `sha256:<hex>` notation, it must equal:

```text
"sha256:" + candidate_file_sha256
```

Any mismatch is DENY before HumanDecisionAdmission.

## 18. Deterministic accepted-scene preview

The Human must bind the actual canonical after-content identity, not merely the candidate source identity.

R4R1 therefore requires one deterministic pure accepted-scene rendering function used by both preview/binding and the later canonical write.

For the frozen current ScriptOps substrate, its required semantics are exactly equivalent to:

```text
1. decode candidate as UTF-8 and parse with the same front-matter semantics used by current legacy.parse_front_matter;
2. require front matter status == "candidate";
3. preserve the candidate body bytes/text semantics;
4. copy front matter and set status = "accepted";
5. remove existing "hash" from a copy used for scene-hash computation;
6. canonical-for-scene-hash = legacy.yaml_dump(front_matter_without_hash, sort_keys=False) + body;
7. accepted_scene_hash = legacy.compute_sha256(canonical-for-scene-hash);
8. set front matter hash = accepted_scene_hash;
9. accepted_text = "---\n" + legacy.yaml_dump(accepted_front_matter, sort_keys=False) + "---" + body;
10. accepted_bytes = UTF-8 bytes of accepted_text.
```

The implementation may refactor this into a pure helper, but preview and effect MUST consume the same helper/result rather than independently reimplementing the transformation.

Define:

```text
accepted_canonical_file_sha256 = SHA-256 of exact accepted_bytes
```

The canonical target pre-state is represented exactly as:

```text
CanonicalPreStateV1 = {
  "exists": <true|false>,
  "file_sha256": <64 lowercase hex or JSON null>
}
```

If the canonical target exists, its exact bytes are hashed. If absent, `exists=false` and `file_sha256=null`.

## 19. PresentedMaterialEffectV1 — exact real ScriptOps consequence schema

The Human-bound material effect object is closed and exactly:

```text
PresentedMaterialEffectV1 = {
  "schema_version": "scriptops-x1b-presented-material-effect/v1",
  "repository": "FJ899/scriptops",
  "scene_id": <exact scene ID>,
  "candidate_path": <exact candidate path>,
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
    "record_schema_version": "scriptops-x1b-decision-record/v1"
  },
  "local_git_effect": {
    "commit_count": 1,
    "commit_message": "scriptops x1b: accept <scene_id> via <decision_request_id>",
    "exact_changed_paths": [
      "scenes/<scene_id>.fountain",
      ".scriptops/decision-log.ndjson"
    ]
  }
}
```

The array order shown above is normative.

No additional material-effect field may be silently added and no required field may be omitted.

The material-effect digest is:

```text
presented_material_effect_digest = sha256_canonical(PresentedMaterialEffectV1)
```

The material effect therefore binds the real runtime decision log:

```text
.scriptops/decision-log.ndjson
```

and explicitly does NOT substitute repository-level historical `DECISION_LOG.md`.

The Human decision request file contains the full `PresentedMaterialEffectV1`, so the manual Human review can inspect the exact consequences before approving.

## 20. Deterministic one-file decision-request branch

After computing the request digest, proposal preparation derives:

```text
request_path = decisions/x1b/<request_digest>.json
proposal_branch = decision/x1b/<request_digest>
```

`<request_digest>` is exactly 64 lowercase hexadecimal characters.

The proposal branch must originate from exact `repository_head_at_request`.

The request commit must:

```text
have exactly one parent = repository_head_at_request
add exactly request_path
contain exact HumanDecisionRequestV1 bytes
introduce no second changed path
```

Proposal preparation may be performed by a separately authorized proposal-writing actor/process.

Proposal creation capability is not Human decision authority.

```text
PROPOSAL PR CREATION != HUMAN DECISION
```

The evaluated Phase-6 effect invocation must not create or edit the proposal branch, request file, decision PR, review, comment, ref, repository rule, or repository setting.

## 21. Decision PR external envelope — PR identity is not circular request content

The decision PR number and current PR HEAD are external evidence about the already-created request proposal. They are NOT part of `request_digest`.

A valid decision PR must satisfy all of the following at preliminary admission and again where marked for final-gate currentness:

```text
repository = FJ899/scriptops
state = OPEN
merged = false
base.ref = main
base.sha = request.repository_head_at_request
head.ref = decision/x1b/<request_digest>
head repository = FJ899/scriptops
head SHA = exact one-commit request commit
```

The verifier must fetch the head Git commit and require:

```text
exactly one parent
parent SHA = repository_head_at_request
```

Complete paginated PR-file enumeration must prove exactly:

```text
changed_files = 1
status = added
filename = decisions/x1b/<request_digest>.json
```

No caller-provided request path or digest may select the artifact.

The adapter itself derives the sole path from the verified PR file set, reads the file at the exact PR HEAD, recomputes request identity, and requires equality among:

```text
filename digest
computed request_digest
request.request_digest
decision_request_id suffix
head-ref digest
```

Any extra file, hidden pagination remainder, rename, deletion, wrong base, wrong parent, wrong branch, fork substitution, request mismatch, or ambiguous API state is DENY.

## 22. Established Human decision authority

For this bounded X1B corrective profile, the established Human decision actor is exactly:

```text
litrgratis-pixel
```

Changing that actor is a Human-governance change and is not an implementation parameter.

Different actors are observable context but cannot create or supersede Human authority under this profile.

```text
KNOWN DIFFERENT ACTOR != AUTHORIZED HUMAN ACTOR
```

R4R1 does not claim that account identity alone proves private Human mental state.

The later live positive-control governance procedure must require the established Human actor to submit the bound APPROVE review manually through GitHub's Human UI.

The machine mechanism establishes trusted bounded evidence through exact GitHub review provenance plus capability separation; it does not claim to cryptographically prove flesh-and-blood presence.

## 23. Exact Human review-body contract

The authoritative Human review state must be exactly:

```text
APPROVED
```

The review body must contain exactly four LF-separated logical lines and no trailing LF:

```text
X1B-HUMAN-DECISION-V1
decision_request_id=<exact x1b:<request_digest>>
decision_request_sha256=<exact request_digest>
why=<Human rationale>
```

Parser rules are exact:

```text
UTF-8 text
LF separators only
no CR
exactly four logical lines
no leading blank line
no trailing blank line
no extra field/line
exact marker spelling
exact decision_request_id equality
exact decision_request_sha256 equality
```

For the value after `why=`:

```text
trim only outer ASCII space U+0020 and tab U+0009
result must be non-empty
result must remain one logical line
result UTF-8 length <= 512 bytes
```

The exact trimmed result is the Human rationale used in durable attribution.

The raw review body SHA-256 is always computed over the exact UTF-8 bytes returned by the trusted GitHub adapter before rationale trimming.

Caller `--why` or any caller note is never Human evidence.

## 24. Trusted public GitHub transport profile

Production Human-decision evidence acquisition is valid only while exact repository `FJ899/scriptops` remains publicly readable without authentication.

The only trusted API origin is:

```text
https://api.github.com
```

The production adapter must use Python standard-library HTTP/TLS primitives based on:

```text
urllib.request
ssl
```

It must construct an explicit opener using:

```text
ProxyHandler({})
HTTPSHandler(context=ssl.create_default_context())
a redirect handler that rejects every redirect
```

No configurable API base URL is permitted.

The adapter may construct requests only below exact REST namespace:

```text
https://api.github.com/repos/FJ899/scriptops/...
```

Production requests must send no `Authorization` or `Cookie` header.

The allowed explicit header set is limited to protocol metadata such as:

```text
Accept: application/vnd.github+json
X-GitHub-Api-Version: 2022-11-28
User-Agent: scriptops-x1b/1
```

No caller-supplied header is accepted.

The adapter must not invoke or read authentication from:

```text
gh
.netrc
GitHub CLI auth config
Git credential helpers
browser state
caller tokens
cached local review JSON
```

There is no authenticated fallback.

Every HTTP redirect, including same-origin redirect, is DENY/BLOCKED.

The adapter must verify request and effective response scheme/host remain exactly HTTPS/api.github.com with the default HTTPS port semantics.

System DNS and the host/Python default root CA store are explicit bounded platform dependencies.

```text
NO AUTH CREDENTIAL != TRUSTED REMOTE ORIGIN BY ITSELF
REVIEW-SHAPED JSON != TRUSTED GITHUB REVIEW EVIDENCE
```

## 25. Transport/auth environment fail-closed gate

Before trusted remote evidence acquisition and before canonical effect, the production approval invocation must deny if any of the following environment variables has a non-empty value:

```text
HTTP_PROXY
HTTPS_PROXY
ALL_PROXY
http_proxy
https_proxy
all_proxy

SSL_CERT_FILE
SSL_CERT_DIR
REQUESTS_CA_BUNDLE
CURL_CA_BUNDLE

GH_TOKEN
GITHUB_TOKEN
GH_ENTERPRISE_TOKEN
GITHUB_ENTERPRISE_TOKEN
GITHUB_PAT
```

No caller override is permitted.

A future implementation may add more fail-closed ambient credential/transport variables; it may not weaken this minimum.

If `FJ899/scriptops` ceases to be publicly readable, R4R1 verification becomes BLOCKED. Adding authenticated verification requires a separately reviewed mechanism revision and new Human authorization.

## 26. Exact GitHub read operations and completion discipline

The production adapter must independently read the evidence required for validation. The bounded API operations include equivalents of:

```text
GET /repos/FJ899/scriptops/pulls/<N>
GET /repos/FJ899/scriptops/pulls/<N>/files?per_page=100&page=<p>
GET /repos/FJ899/scriptops/contents/<derived-request-path>?ref=<exact-head-sha>
GET /repos/FJ899/scriptops/git/commits/<exact-head-sha>
GET /repos/FJ899/scriptops/pulls/<N>/reviews?per_page=100&page=<p>
```

For every paginated collection:

```text
per_page = 100
page starts at 1
continue page-by-page
completion is proven only by an empty page or a page containing fewer than 100 records
```

A page failure, HTTP ambiguity, rate limit that prevents completion, malformed JSON, unexpected response shape, duplicate record identity, or inability to prove completion is DENY/BLOCKED before effect.

The production caller cannot assert `reviews_complete=true`, inject a trusted snapshot, or choose a test fake adapter.

Fake adapters are permitted only through explicitly test-only construction surfaces not reachable from the production CLI.

## 27. Complete review record validation

Every review used in the complete review set must expose parseable:

```text
numeric review ID
review node ID
actor login
state
commit ID or null
body string
submitted_at
```

Duplicate numeric IDs or duplicate node IDs are DENY.

Recognized review states are exactly:

```text
APPROVED
CHANGES_REQUESTED
COMMENTED
DISMISSED
```

An unknown/unparseable review state is DENY rather than implementation-defined behavior.

State semantics are:

```text
APPROVED = active positive decision-bearing review
CHANGES_REQUESTED = active negative/conflicting decision-bearing review
COMMENTED = nondecision
DISMISSED = inactive
```

For the established Human actor on the exact current decision-PR HEAD, the decision set must contain:

```text
exactly one valid matching active APPROVED
zero other active decision-bearing reviews on that same HEAD
```

Therefore:

```text
second APPROVED on current HEAD => ambiguous => DENY
active CHANGES_REQUESTED on current HEAD => conflict => DENY
malformed active APPROVED on current HEAD => DENY
APPROVED on old commit => historical, not authority for current HEAD
COMMENTED => nondecision
DISMISSED => inactive
reviews by another actor => not Human authority for this profile
```

There is no chronology-only latest-wins rule.

## 28. CompleteReviewSetV1 — exact normalized projection

For every submitted review returned by the complete review collection, construct exactly:

```text
NormalizedReviewV1 = {
  "schema_version": "scriptops-x1b-normalized-review/v1",
  "review_numeric_id": <decimal string>,
  "review_node_id": <exact node-id string>,
  "actor_login": <exact login>,
  "state": <one recognized state>,
  "commit_id": <40 lowercase hex or JSON null>,
  "body_sha256": <64 lowercase hex of exact UTF-8 body bytes>,
  "submitted_at": <exact GitHub timestamp string>
}
```

The complete set includes reviews by all actors and all recognized states, not merely the admitted Human review.

No avatar, display name, email, URL, reaction, requested-reviewer state, or unrelated metadata is included.

## 29. CompleteReviewSetV1 ordering and digest

Sort `NormalizedReviewV1` objects by exact tuple:

```text
(submitted_at ASC as exact timestamp string after successful timestamp validation,
 review_numeric_id ASC as arbitrary-precision decimal integer)
```

If either field cannot be validated, DENY.

Construct exactly:

```text
CompleteReviewSetV1 = {
  "schema_version": "scriptops-x1b-complete-review-set/v1",
  "repository": "FJ899/scriptops",
  "decision_pr_number": <positive integer>,
  "decision_pr_head": <40 lowercase hex>,
  "reviews": [<NormalizedReviewV1 in normative order>]
}
```

Then:

```text
complete_review_set_digest = sha256_canonical(CompleteReviewSetV1)
```

This field projection, collection membership, ordering, serialization, and digest formula are normative.

Golden-vector tests must freeze exact reconstruction behavior.

## 30. Preliminary HumanDecisionAdmissionV1

Only after request, PR envelope, complete reviews, Human review semantics, local state, transport environment, replay state, and material-effect bindings all pass may the verifier create one process-local preliminary admission.

The exact admission identity payload is:

```text
HumanDecisionAdmissionIdentityV1 = {
  "schema_version": "scriptops-x1b-human-decision-admission/v1",
  "repository": "FJ899/scriptops",
  "repository_head_at_request": <exact local/request HEAD>,
  "decision_pr_number": <positive integer>,
  "decision_pr_head": <exact PR HEAD>,
  "decision_request_id": <x1b:<digest>>,
  "request_digest": <64 lowercase hex>,
  "request_file_path": "decisions/x1b/<request_digest>.json",
  "human_review_numeric_id": <decimal string>,
  "human_review_node_id": <exact node ID>,
  "human_actor": "litrgratis-pixel",
  "human_review_body_sha256": <64 lowercase hex>,
  "human_review_submitted_at": <exact timestamp string>,
  "human_rationale": <validated rationale>,
  "task_id": <exact task ID>,
  "scene_id": <exact scene ID>,
  "candidate_path": <exact path>,
  "candidate_file_sha256": <64 lowercase hex>,
  "impact_report_path": <exact path>,
  "impact_report_sha256": <64 lowercase hex>,
  "canonical_target": "scenes/<scene_id>.fountain",
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect_digest": <64 lowercase hex>,
  "canonical_instance_scope": "LOCAL_WORKTREE_DECISION_LOG_V1"
}
```

Admission ID is exactly:

```text
admission_id = "x1b-admit:" + sha256_canonical(HumanDecisionAdmissionIdentityV1)
```

The in-memory admission contains the identity payload plus `admission_id`.

It is:

```text
process-local
one-shot
not caller-constructible in production
not serializable/reloadable as a bearer credential
not authority to manufacture a Human review
```

```text
HUMAN DECISION ADMISSION != FINAL EFFECT COMMITMENT
```

## 31. Canonical repository-instance scope and concurrency lock

R4R1's replay property is deliberately local and bounded.

One canonical execution instance is the exact verified ScriptOps worktree in which the approval command is executing, with replay evidence read from that worktree's `.scriptops/decision-log.ndjson`.

To prevent concurrent same-worktree approval invocations from both passing the pre-consumption check, the production approval path must acquire an exclusive worktree-local lock before preliminary admission validation.

The required lock is an atomically created directory under the worktree-specific Git directory, conceptually:

```text
<git rev-parse --git-dir>/scriptops-x1b-approve.lock
```

Requirements:

```text
atomic mkdir/create-or-fail semantics
lock acquired before replay/admission checks
lock held through FinalEffectGate and final Git commit/post-effect verification
second concurrent invocation => DENY/BLOCKED before effect
clean successful/ordinary-failure exit removes its own lock
crash-stale lock is fail-closed; no automatic age-based stealing
```

Automatic stale-lock takeover based on time is prohibited because it could create two concurrent effect owners.

The lock is runtime coordination metadata under Git state, not repository content and not Human decision evidence.

Separate clones/worktrees are outside the claimed globally atomic replay scope.

## 32. Bounded replay/consumption semantics

The exact claim is:

```text
one decision_request_id
may cause at most one successful X1B acceptance effect
within one canonical local worktree execution instance
```

Before effect, the complete local `.scriptops/decision-log.ndjson` must contain no successful R4R1 X1B decision record consuming the same `decision_request_id`.

After successful effect, exactly one appended `X1BDecisionRecordV1` consumes that request ID in that same instance.

A repeated invocation against that same instance must DENY before canonical effect.

If an X1B-looking record is malformed such that safe replay determination is impossible, DENY rather than ignore it.

Explicit non-claim:

```text
NO GLOBAL CROSS-CLONE EXACTLY-ONCE CLAIM
NO GLOBAL CROSS-WORKTREE EXACTLY-ONCE CLAIM
```

Any changed repository HEAD, task, scene, candidate path/bytes, impact report, canonical target, material-effect object, effect type, request bytes/digest, or decision-PR HEAD requires a new exact Human decision.

```text
OLD CONSENT + CHANGED OPERATION = DENY
```

A future requirement for global cross-instance atomic consumption requires a separate shared-authority design and separate Human authorization.

## 33. FinalEffectGateV1 — mandatory fresh currentness reread

A preliminary admission cannot itself start canonical mutation.

Immediately before the first canonical mutation, while the exclusive local lock is still held, the production verifier must perform a fresh trusted GitHub read of at least:

```text
decision PR metadata/state/base/head
complete paginated review set
```

It must require again:

```text
PR OPEN
PR unmerged
base/ref/SHA still exact
head/ref/SHA still exact
admitted Human review still exists on exact current HEAD
review still APPROVED
review body/actor/commit still exact
no second approval/conflict/ambiguity
complete review set successfully reconstructed
```

It must also freshly revalidate local state:

```text
exclusive X1B lock still owned
local HEAD unchanged
working tree clean
candidate exact path/bytes/status unchanged
impact report exact bytes/semantic bindings unchanged
request exact identity unchanged
canonical target pre-state unchanged
accepted-scene preview exact after hash unchanged
material-effect object/digest unchanged
request remains unconsumed in local decision log
```

Any ambiguity, network/rate-limit failure, review drift, PR closure/merge, HEAD drift, local drift, or replay drift is DENY before mutation.

## 34. FinalEffectGateV1 exact structure and digest

A successful final validation produces one in-memory process-local gate:

```text
FinalEffectGateV1 = {
  "schema_version": "scriptops-x1b-final-effect-gate/v1",
  "admission_id": <exact admission_id>,
  "decision_request_id": <exact decision_request_id>,
  "request_digest": <exact request_digest>,
  "presented_material_effect_digest": <exact digest>,
  "decision_pr_number": <positive integer>,
  "decision_pr_head": <exact head>,
  "human_review_numeric_id": <decimal string>,
  "human_review_node_id": <exact node ID>,
  "human_actor": "litrgratis-pixel",
  "human_review_body_sha256": <exact body digest>,
  "complete_review_set_digest": <exact final CompleteReviewSetV1 digest>,
  "repository_head_before_effect": <exact local HEAD>,
  "scene_id": <exact scene ID>,
  "candidate_path": <exact candidate path>,
  "candidate_file_sha256": <exact candidate digest>,
  "impact_report_sha256": <exact impact digest>,
  "canonical_target": "scenes/<scene_id>.fountain",
  "canonical_before": <exact CanonicalPreStateV1>,
  "canonical_after_file_sha256": <exact accepted after digest>,
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "canonical_instance_scope": "LOCAL_WORKTREE_DECISION_LOG_V1",
  "current_human_decision_valid": true,
  "observed_at": <offset-aware UTC timestamp string>
}
```

Its digest is:

```text
final_effect_gate_digest = sha256_canonical(FinalEffectGateV1)
```

The gate is in-memory, one-shot, process-local, not caller-supplied, and not persisted as a reusable credential.

The durable decision record later stores its digest and reconstructable identity fields.

## 35. Human-currentness commitment point

The exact authority linearization rule is:

```text
Human-currentness commitment point
=
successful completion of FinalEffectGateV1 validation
immediately before the first canonical mutation
```

Before that point, a Human/GitHub decision state change that is visible through the trusted source must revoke/conflict with the effect according to the final reread rules.

After that commitment point, a later remote state change does not retroactively revoke the already-authorized one-shot same-process effect.

This is explicitly not a claim of distributed atomicity with GitHub.

After final-gate success and before the first canonical mutation, the implementation must perform no:

```text
user interaction
network operation
sleep/wait
unrelated subprocess
unrelated filesystem operation
other intentionally blocking operation
```

Only deterministic in-process gate-integrity checks and the immediate first canonical write may intervene.

If the implementation cannot preserve this immediate transition, it must not claim R4R1 currentness satisfaction.

## 36. Exact durable X1B decision record

The successful decision-log append uses target:

```text
.scriptops/decision-log.ndjson
```

and schema:

```text
X1BDecisionRecordV1 = {
  "schema_version": "scriptops-x1b-decision-record/v1",
  "result": "SUCCESS",
  "decision_type": "scene_accepted",
  "decision_request_id": <exact decision_request_id>,
  "request_digest": <exact request_digest>,
  "decision_pr_number": <positive integer>,
  "decision_pr_head": <exact head>,
  "human_review_numeric_id": <decimal string>,
  "human_review_node_id": <exact node ID>,
  "human_actor": "litrgratis-pixel",
  "human_review_commit": <exact decision PR HEAD>,
  "human_review_body_sha256": <64 lowercase hex>,
  "human_review_submitted_at": <exact GitHub timestamp>,
  "human_rationale": <validated Human rationale>,
  "admission_id": <exact x1b-admit:...>,
  "final_effect_gate_digest": <64 lowercase hex>,
  "complete_review_set_digest": <64 lowercase hex>,
  "task_id": <exact task ID>,
  "scene_id": <exact scene ID>,
  "candidate_path": <exact candidate path>,
  "candidate_file_sha256": <64 lowercase hex>,
  "impact_report_path": <exact path>,
  "impact_report_sha256": <64 lowercase hex>,
  "canonical_target": "scenes/<scene_id>.fountain",
  "canonical_before": <CanonicalPreStateV1>,
  "canonical_after_file_sha256": <64 lowercase hex>,
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect_digest": <64 lowercase hex>,
  "canonical_instance_scope": "LOCAL_WORKTREE_DECISION_LOG_V1"
}
```

The record is canonicalized for tests/audit as R4R1 JSON, but the NDJSON line may be written as exact canonical JSON plus one terminating LF.

The record contains no hard-coded `approver="human"` substitute.

If a compatibility `approver` field is retained for downstream tooling, it must be derived from validated `human_actor` and must equal the exact actor login, not the generic string `human`.

Caller text never enters `human_rationale`.

## 37. No circular resulting-commit self-binding

The decision record is itself part of the local Git effect commit. Therefore it MUST NOT contain the SHA of that same resulting commit as a field whose bytes contribute to that commit.

Preserve:

```text
ARTIFACT CONTENT BINDING != ARTIFACT SELF-HASH BINDING
```

The resulting effect commit SHA is established by independent post-effect Git truth and frozen in later verification evidence.

The Human-bound material effect commits to:

```text
commit_count = 1
exact changed paths
exact precomputed commit-message template
```

not to an impossible self-referential future SHA.

## 38. Effect execution and non-substitution

The executor may only consume the exact operation bound by the admission and final gate.

No caller or later process step may substitute:

```text
Human actor
Human result
Human rationale
request identity
task
scene
candidate
impact report
canonical target
accepted after bytes
effect type
material effect
```

The accepted canonical bytes written to `scenes/<scene_id>.fountain` must be the exact bytes whose SHA-256 is bound in `PresentedMaterialEffectV1` and FinalEffectGateV1.

The decision-log append must be exactly one R4R1 `X1BDecisionRecordV1` line.

The Git staging set must contain exactly:

```text
scenes/<scene_id>.fountain
.scriptops/decision-log.ndjson
```

The local Git commit message must be exactly the material-effect-bound message with concrete scene ID and decision request ID substituted before the Human request was finalized.

No `git add .` is allowed on the operative X1B effect path.

## 39. Local Git capability isolation

The approval invocation performs no network Git operation.

Permitted Git operations are local repository identity/state/diff/staging/commit checks needed for the bounded effect.

It must not invoke:

```text
fetch
pull
push
ls-remote
remote submodule operation
any other network Git command
```

Every local Git subprocess in the approval path must receive an explicitly constructed environment that removes denied GitHub credential variables and disables interactive/helper credential acquisition.

At minimum:

```text
GIT_TERMINAL_PROMPT=0
GCM_INTERACTIVE=never
```

and every Git command must disable credential helpers for that process, equivalent to:

```text
git -c credential.helper= ...
```

The approval path must not invoke `gh`.

## 40. Failure after first mutation

The implementation must compute and validate both exact output payloads before the first canonical mutation:

```text
accepted canonical scene bytes
one X1BDecisionRecordV1 NDJSON line
```

Technical success exists only if both files are written as bound, exactly the two paths are committed in one local Git commit, and post-effect verification passes.

If an exception occurs after the first filesystem mutation but before successful effect commit, the invocation must return nonzero and attempt deterministic restoration of the exact pre-effect bytes/state while still holding the local X1B lock.

It must never report X1B success for a partial effect.

If exact restoration cannot be proven, the invocation must leave an explicit fail-closed dirty/error state and report `BLOCKED`; it must not synthesize Human success evidence.

Later implementation review must actively test injected failures between scene write, decision-log append, staging, and commit.

## 41. Post-effect truth requirements

A successful invocation must independently verify from local Git/filesystem truth:

```text
new HEAD has exactly one parent = repository_head_before_effect
exactly one new effect commit exists
commit message matches PresentedMaterialEffectV1
commit changed-file set is exactly:
  scenes/<scene_id>.fountain
  .scriptops/decision-log.ndjson
canonical scene exact bytes SHA-256 = bound canonical_after_file_sha256
canonical front matter status = accepted
exactly one new X1BDecisionRecordV1 line was appended
record decision_request_id/admission/gate/review/material-effect identities match
working tree is clean after commit
request is now consumed in local decision log
```

Exit code alone is never sufficient evidence of success.

The later independent verification artifact records the resulting local Git commit SHA externally, avoiding self-hash circularity.

## 42. Current Phase-6 smoke-test supersession

Current `tests/test_phase6_scriptops_smoke.py` contains defect-era positive approval semantics using `approve --scene ... --why ...` and a requirement for explicit caller `--why`.

Future implementation must update that test surface so unrelated Phase-6 B1/B2/B3/B5 behavior remains covered while defect-era caller rationale is no longer treated as Human authority.

The obsolete current safety expectation:

```text
test_approve_requires_explicit_why
```

must cease to be a normative Human-decision requirement.

Positive X1B admission behavior belongs in the dedicated deterministic X1B test suite with fake read-only adapters. No CI test may create a live Human review or canonical user screenplay effect.

## 43. Mandatory executable negative matrix

The future implementation candidate must contain executable tests for all preregistered X1B attack classes:

```text
X1B-N01 AI marks own proposal accepted
X1B-N02 continuation treated as decision
X1B-N03 silence/no response treated as consent
X1B-N04 old consent reused
X1B-N05 Human accepts A but A-prime becomes operative
X1B-N06 parameters changed after acceptance
X1B-N07 scope expanded after acceptance
X1B-N08 general direction attributed as specific Human parameters
X1B-N09 AI artifact impersonates Human decision
X1B-N10 AI-filled value recorded Human-chosen
```

Exact real regression:

```text
caller invokes approval with scene/caller rationale but no trusted Human review
=> DENY
=> no canonical mutation
=> no decision-log mutation
=> no Human attribution
=> no Git effect commit
```

Direct legacy regression:

```text
python legacy/scriptops-v2-single.py approve --scene <scene>
=> DENY / nonzero / no effect
```

Additional mandatory negatives include at least:

```text
wrong Human actor
wrong review commit ID
wrong decision PR HEAD
wrong PR base SHA
wrong PR head ref
forked head repository
extra decision-PR changed file
renamed request file
caller request-path substitution
filename/request digest mismatch
self-consistent request with wrong local candidate
candidate drift
impact-report drift
canonical pre-state drift
material-effect substitution
wrong real decision-log target
old DECISION_LOG.md substitution
malformed four-line review body
empty rationale
oversized rationale
CR/line-ending substitution
second active Human approval
active CHANGES_REQUESTED
only COMMENTED
only DISMISSED
unknown review state
duplicate review numeric ID
duplicate review node ID
incomplete review pagination
incomplete PR-file pagination
HTTP read failure
rate-limit ambiguity
redirect
proxy environment injection
CA override environment injection
GitHub token environment injection
authenticated fallback attempt
custom API-host attempt
caller-created trusted snapshot in production path
consumed request replay in same worktree
concurrent same-worktree approval while lock held
crash-stale lock => fail closed
local HEAD mismatch
old Human decision after changed operation
review dismissed after preliminary admission but before final gate
CHANGES_REQUESTED after preliminary admission but before final gate
PR closed/merged after preliminary admission
PR HEAD changed after preliminary admission
remote final reread failure
candidate drift after preliminary admission
canonical pre-state drift after preliminary admission
executor substitution after final gate
out-of-scope staged file
second decision-log append
second effect commit
injected failure after first file mutation
injected failure before commit
```

Every negative must prove no unauthorized successful effect, not merely that an exception was raised.

## 44. Deterministic golden-vector tests

The implementation must freeze deterministic golden vectors for at least:

```text
canonical_json_bytes
request_binding_json
request_digest
decision_request_id
PresentedMaterialEffectV1 bytes/digest
Human review raw-body SHA-256
HumanDecisionAdmissionIdentityV1 bytes/admission_id
NormalizedReviewV1 projection
CompleteReviewSetV1 ordering/bytes/digest
FinalEffectGateV1 bytes/digest
X1BDecisionRecordV1 canonical NDJSON line
accepted-scene preview bytes/hash
```

Tests must verify exact bytes, not merely equivalent parsed objects.

## 45. Production adapter / test adapter separation

`phase6/x1b_human_decision.py` may define a protocol/interface allowing deterministic fake adapters in tests.

Production CLI construction must internally instantiate the trusted public GitHub adapter and must expose no CLI option, environment variable, request field, config field, or deserialization route that lets a caller provide a trusted snapshot/fake adapter.

Test fakes are explicitly non-production evidence.

```text
TEST FAKE != TRUSTED PRODUCTION ORIGIN
```

## 46. Workflow requirements

Future `.github/workflows/x1b-human-decision.yml` must run deterministic X1B tests only.

It must not:

```text
create a decision PR
create/submit/dismiss a Human review
write user screenplay canon
merge
change repository rules/settings
claim that CI equals Human approval
```

The workflow must require no GitHub write credential for the X1B tests.

Production public-read transport tests should use deterministic mocked HTTP at unit level; live Human control remains a separately authorized stage.

```text
CI PASS != HUMAN DECISION
```

## 47. Current-state and repository-verifier tests

The implementation verification suite must prove that current repository truth and executable truth agree.

At minimum:

```text
README current route = approve --decision-pr
PROJECT_STATE current route = approve --decision-pr
HANDOFF current/resume route = approve --decision-pr
defect-era approve --why retained only as historical provenance
legacy historical-byte identity not claimed as current active-runtime requirement
verify_repository accepts split historical/current source model
verify_repository rejects reintroduced current approve --why authority
verify_repository rejects active legacy byte-identity requirement
restore documentation cannot direct historical bytes into active legacy path
```

## 48. Historical evidence is preserved, not rewritten

R4R1 correction must not rewrite historical evidence files to pretend earlier Phase-6 behavior used the new mechanism.

Historical evidence may accurately say that caller `--why`, unchanged legacy, or prior gates were used at that time.

Current-state files must clearly label those statements as historical when relevant.

```text
CORRECT CURRENT AUTHORITY != ERASE HISTORICAL PROVENANCE
```

## 49. Real positive Human control — later separately authorized

R4R1 does not authorize the positive control.

A later Human-authorized positive-control stage must freeze before execution:

```text
exact reviewed implementation HEAD/TREE
one disposable ScriptOps repository/worktree instance
one inert/synthetic X1B scene/task/candidate
candidate exact path/bytes/hash
impact report exact path/bytes/hash
repository_head_at_request
HumanDecisionRequestV1 bytes/digest/id
one dedicated one-file decision PR
exact decision PR HEAD
PresentedMaterialEffectV1 bytes/digest
expected canonical before/after identities
expected decision-log target/effect
```

The established Human actor `litrgratis-pixel` must manually submit the exact four-line APPROVED review through GitHub Human UI.

The actual corrected Phase-6 `approve --decision-pr <N>` path must then consume evidence using the credential-free trusted public adapter.

The evaluated effect process must have no GitHub review-create credential/capability mounted for the control.

No user screenplay canon may be used.

Post-effect independent truth must prove exact Human-bound content/scope/candidate/effect, exact actor/rationale/review/request/admission/final-gate provenance, exact two-path effect commit, and no unauthorized substitution.

Exit code alone is not PASS.

## 50. Bounded trusted-origin claim

R4R1 claims only the following bounded composition:

```text
manual Human APPROVE governance act by established Human actor
+
exact authoritative-Human GitHub review record
+
effect process that does not create/edit GitHub review evidence
+
credential-free public trusted GitHub evidence acquisition
+
exact request/PR/review/current-state/material-effect binding
+
independent admission
+
fresh FinalEffectGate currentness check
=
trusted Human decision evidence for this bounded X1B profile
```

It does not claim:

```text
GitHub metadata alone proves browser/UI origin
GitHub account identity alone proves private Human mental state
hardware-backed physical presence
phishing resistance
global distributed revocation atomicity
global cross-clone exactly-once consumption
```

Those are outside R4R1's claim.

## 51. Planned implementation responsibilities

### `phase6/scriptops-v2-hardening.py`

Must:

```text
replace current caller-rationale approval interface with approve --decision-pr
acquire/release exact local X1B lock
perform clean/local prechecks
resolve candidate/impact/current operation from trusted local state
invoke trusted Human-decision verification/admission
invoke fresh FinalEffectGate
write only exact bound accepted scene + decision-log record
stage only exact two effect paths
commit exactly one local effect commit
post-verify exact effect truth
```

### `legacy/scriptops-v2-single.py`

Must:

```text
remain the non-approval substrate where still needed
make direct legacy approve non-effect-capable
not recreate generic approver="human" acceptance
```

### `phase6/x1b_human_decision.py`

Must contain the bounded security mechanism, including:

```text
closed canonical schemas/serialization
request identity
accepted-scene pure preview helper
material-effect identity
trusted public GitHub adapter
PR/request envelope validation
review-body parser
complete pagination/review semantics
complete-review-set digest
local request/currentness validation
replay validation
admission identity
FinalEffectGate identity/currentness
X1BDecisionRecordV1 construction/integrity helpers
```

### `scripts/restore_v2.py`

Must preserve historical reconstruction but prohibit repository-internal historical restore writes.

### `scripts/verify_repository.py`

Must split historical transport validation from corrected active runtime validation and enforce current R4R1 repository truth.

### `sources/prototype/RESTORE.md` and `SOURCE_MANIFEST.md`

Must preserve historical provenance while removing historical-byte restoration as active-runtime authority.

### `README.md`, `PROJECT_STATE.md`, `HANDOFF.md`

Must make current/recovery authority agree with R4R1 and preserve old behavior only as historical provenance.

### `tests/test_phase6_scriptops_smoke.py`

Must retain unrelated Phase-6 smoke coverage while removing caller `--why` as current Human authority.

### `tests/test_x1b_human_decision.py`

Must contain the deterministic adversarial/golden-vector suite.

### `.github/workflows/x1b-human-decision.yml`

Must run deterministic tests without becoming Human authority or live effect machinery.

## 52. Independent implementation-review obligations

A later independently authorized implementation review must not accept `tests green` as sufficient.

It must inspect at least:

```text
complete candidate tree effect-entry inventory
all direct/indirect acceptance paths
actual changed-file set vs authorized surface
legacy direct-approve denial
restore path and symlink/traversal handling
repository verifier semantics
current README/STATE/HANDOFF truth
canonical JSON exactness
non-circular request construction
PR envelope validation
GitHub transport origin/redirect/credential behavior
review-body exactness
complete pagination and state semantics
review-set digest reconstruction
admission integrity
worktree lock/concurrency behavior
replay behavior
FinalEffectGate race/currentness semantics
material-effect actual .scriptops/decision-log.ndjson target
accepted-scene preview/effect byte identity
failure injection/rollback behavior
Git exact two-path commit truth
durable attribution provenance
absence of resulting-commit self-hash circularity
```

Any material authority/security ambiguity is NOT PASS.

## 53. Closure sequence after implementation authority

Even a future implementation-review PASS does not close X1B.

Required later stages remain separately governed:

```text
bounded implementation authorization
implementation candidate
independent implementation review
fresh deterministic negative/adversarial verification
separately Human-authorized live positive control
independent post-effect verification
durable corrective verification freeze
independent closure review
Human closure acceptance
```

Only after those stages can X1B corrective closure be considered Human accepted.

```text
GREEN TESTS != CORRECTIVE CLOSURE
IMPLEMENTATION REVIEW PASS != CORRECTIVE CLOSURE
POSITIVE CONTROL PASS != CORRECTIVE CLOSURE
TECHNICAL VERIFICATION PASS != HUMAN CLOSURE ACCEPTANCE
```

## 54. R4R1 preparation disposition boundary

The R4R1 preparation stage may conclude only with one of:

```text
X1B CLEAN R4R1 REMATERIALIZATION = PASS
X1B CLEAN R4R1 REMATERIALIZATION = NOT PASS
X1B CLEAN R4R1 REMATERIALIZATION = BLOCKED
```

A preparation PASS means only that the exact R4R1 brief artifact was durably materialized inside its authorized evidence-repository surface.

It does not mean the brief has passed independent review.

It does not authorize ScriptOps code changes.

## 55. Final invariants

Preserve throughout all later work:

```text
AI PROPOSES != HUMAN DECIDES
USER SAW != USER DECIDED
USER CONTINUED != USER ACCEPTED
AI-FILLED VALUE != HUMAN-CHOSEN VALUE
APPROVAL COMMAND POSSESSION != HUMAN DECISION AUTHORSHIP
NON-EMPTY WHY != HUMAN ACT
SHAPE MATCH != TRUSTED ORIGIN
KNOWN DIFFERENT ACTOR != UNKNOWN ACTOR
KNOWN DIFFERENT COMMIT != UNKNOWN COMMIT
MALFORMED TRUSTED EVIDENCE => DENY
HUMAN DECISION EVIDENCE != EXECUTION CREDENTIAL
EFFECT CAPABILITY != AUTHORITY TO CREATE HUMAN DECISION EVIDENCE
OLD CONSENT + CHANGED OPERATION = DENY
ARTIFACT CONTENT BINDING != ARTIFACT SELF-HASH BINDING
NO GLOBAL CROSS-CLONE EXACTLY-ONCE CLAIM
R4R1 BRIEF != IMPLEMENTATION AUTHORITY
R4R1 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R1 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
```
