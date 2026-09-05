# X1B Human Decision Authorship — Superseding Implementation Brief R3

Status: `SUPERSEDING IMPLEMENTATION BRIEF R3 / NOT IMPLEMENTATION AUTHORITY`

Date: 2026-09-01

## 1. Purpose and authority boundary

This document supersedes the implementation brief R2 in `FJ899/8 PR #112` for future X1B implementation-authority decisions. It corrects the exact blockers frozen by the independent AK-CANON R2 implementation-brief review in `FJ899/8 PR #113` while preserving the accepted X1B corrective design and its clean-room independent review.

Accepted finding under correction:

`X1B FAIL — FALSE HUMAN DECISION`

The real defect remains that ScriptOps can currently cause a canonical accepted-scene effect and durable Human attribution without a separately established, exact, trusted Human decision act.

This document is a brief only. It authorizes no code write, no Human decision creation, no canonical effect, no corrective verification execution, no merge, no X1B closure, no Agency Kernel v1 work, no release, no deployment, and no tag.

```text
PR #110 = HISTORICAL SUPERSEDED IMPLEMENTATION BRIEF / NOT AUTHORITY
PR #111 = HISTORICAL BINDING NOT-PASS REVIEW INPUT
PR #112 = HISTORICAL SUPERSEDED IMPLEMENTATION BRIEF R2 / NOT AUTHORITY
PR #113 = BINDING R2 NOT-PASS REVIEW INPUT
R3 BRIEF != IMPLEMENTATION AUTHORITY
R3 BRIEF PASS != IMPLEMENTATION AUTHORITY
R3 BRIEF PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact normative lineage

### 2.1 Corrective design

Repository: `FJ899/scriptops`

PR: `#34`

BASE: `2f22843ac570498b506101addeba5453ab777f08`

HEAD: `d7a5065c87e9a4b49fb608235c908bceac42b4b1`

TREE: `3140d0ac95c120a7b1532942bae2e0dad38b4839`

PATH: `governance/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_CANDIDATE.md`

BLOB: `dac16f109d1414a2208c2ed9a166ae9e9a329216`

The design requires a separate Human decision event, Human-authoritative origin distinct from the evaluated effect capability, exact content/scope/candidate/effect binding, explicit currentness/conflict/replay rules, evidence-derived Human attribution, fail-closed admission, executor non-substitution, all original X1B attacks, the real ScriptOps regression, and a real Human positive control.

### 2.2 Independent corrective-design review

Repository: `FJ899/8`

PR: `#109`

HEAD: `132d65be48331a822039262b707c47a81d02a64d`

TREE: `a8bdc363d293beb7b15ae8b787cc3ebdd694fd99`

PATH: `research/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_DESIGN_AK_CANON_REVIEW_R2.md`

BLOB: `439109e104244552a5ac1f3f08988dba283733d0`

Verdict:

`AK-CANON X1B CORRECTIVE DESIGN REVIEW R2 = PASS`

### 2.3 Historical implementation brief and first NOT-PASS review

Implementation brief PR `#110`:

```text
HEAD = 8eaad5ea3c37b2cdc65ad80d16260bbf0f2a0160
TREE = a7978803db0e1f0f87fb84ac54f44b8c5bc33a09
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF.md
BLOB = 385bcc8620619b91986ff44211a428913b228ba2
```

Independent review PR `#111`:

```text
HEAD = 05bb0820990f92686c42547385729c87c614be65
TREE = 9147295a388906a07898e9d09d62c5ac53912997
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_AK_CANON_REVIEW.md
BLOB = 35af188a5475b745294bcfa22fd3aa18b666decd
VERDICT = AK-CANON X1B IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

These remain immutable historical evidence.

### 2.4 Superseded implementation brief R2

Repository: `FJ899/8`

PR: `#112`

BASE: `b2c92ec5cd8fbb7272d701d229adc8a8019f951e`

HEAD: `81177847ada75f874d4906c4f98c2bbc1b371dd3`

TREE: `2e1f9b469034decfe9c62bed161e065ffb29330b`

PATH: `research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R2.md`

BLOB: `40e4732f94152a9f46aa8fb158749dcf0bce3a26`

R2 materially improved the first brief but did not independently pass review and therefore is not implementation authority.

### 2.5 Binding independent R2 NOT-PASS review

Repository: `FJ899/8`

PR: `#113`

HEAD: `943de2cb9327747ef563d84a0b79661a1f9d3c5b`

TREE: `6bc9e6856f4a4a577339388acdf8795ae7e6c4fa`

PATH: `research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R2_AK_CANON_REVIEW.md`

BLOB: `584de42da7b6ebba660b4bdbd834d61f633fe5a3`

Verdict:

`AK-CANON X1B SUPERSEDING IMPLEMENTATION-BRIEF R2 REVIEW = NOT PASS`

R3 must resolve, not reinterpret away, these exact material findings:

```text
X1B-R2-IBR-F001 — restore/self-verification contract can reintroduce unsafe legacy and conflicts with changing active legacy
X1B-R2-IBR-F002 — public-read trusted HTTP transport origin is under-specified
X1B-R2-IBR-F003 — post-admission Human-review currentness/revocation cutoff is not frozen
```

## 3. Frozen current ScriptOps baseline

Repository: `FJ899/scriptops`

Canonical baseline for any later implementation candidate:

```text
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Bound current files:

```text
phase6/scriptops-v2-hardening.py
BLOB = 4f379960ed5677634dd234af6aa39626782b6133

legacy/scriptops-v2-single.py
BLOB = 9baa7b3a1eb746e34b79207a382eea1f5dd4ec55

scripts/restore_v2.py
BLOB = fa2099d7d4530bce2256051690935625dab0e927

scripts/verify_repository.py
BLOB = a61278086b92824d7e442b390c951e918c88517b

sources/prototype/RESTORE.md
BLOB = 8a79aca4c93b23c4842792bea9ecaae146e1fc48

SOURCE_MANIFEST.md
BLOB = 2acf2ece298bfcf89254087c9e747fcb808ab241

tests/test_phase6_scriptops_smoke.py
BLOB = d6065047268cee5591883a3065ce49886ec85bcf

.github/workflows/phase6-scriptops-smoke.yml
BLOB = a811dc75b4d3c7a1ebd8375c24fc71c74586ddf5

.github/workflows/verify-repository.yml
BLOB = 7d896d425012479c97bf1e6539f9a861a4a17aa5
```

The current real defect remains materially present on this frozen baseline. The current Phase-6 approval path accepts caller `--why`, and the legacy single-file runtime exposes a separate direct approval effect path.

## 4. R3 source-of-truth decision

R3 resolves the R2 repository-source ambiguity by separating immutable historical transport evidence from the active corrected runtime substrate.

Normative split:

```text
sources/prototype/scriptops-v2-single.py.part01..part07
=
IMMUTABLE HISTORICAL TRANSPORT EVIDENCE
```

and:

```text
legacy/scriptops-v2-single.py
=
ACTIVE CORRECTED RUNTIME SUBSTRATE
```

The seven historical parts continue to reconstruct exactly the historical ScriptOps v2 artifact:

```text
SHA-256 = 881dade6c6c506b9a9d41ebfbf68afb18b66db7583d35f746fb29ed7b36ac596
SIZE = 51980 bytes
```

Those historical identity values no longer define the required byte identity of the active corrected runtime file.

The historical part files themselves are outside the future X1B implementation mutation surface and must remain byte-for-byte unchanged.

Required separation:

```text
HISTORICAL TRANSPORT IDENTITY != ACTIVE RUNTIME IDENTITY
HISTORICAL EVIDENCE != AUTHORITY TO REINTRODUCE UNSAFE EXECUTABLE CODE
```

## 5. F001 correction — historical reconstruction cannot target active repository runtime

### 5.1 Corrected restore purpose

Future `scripts/restore_v2.py` remains a historical transport verifier/reconstructor. It may:

- enumerate the seven historical transport parts;
- reconstruct their bytes in memory;
- validate exact historical SHA-256 and size;
- validate UTF-8 and Python syntax;
- perform check-only historical verification;
- reconstruct the historical artifact only to an explicit destination outside the ScriptOps repository root.

It must not be a mechanism for restoring executable active repository code.

### 5.2 No active-runtime default output

The corrected restore tool must have no default output equal to:

`legacy/scriptops-v2-single.py`

and no implicit repository-internal output.

A write-mode invocation must require an explicit output path.

### 5.3 Repository-root exclusion

Before any write, the restore tool must resolve the requested destination path and the repository root and require that the destination is outside the repository root.

Any destination equal to the root or contained anywhere beneath the root is denied before opening/truncating/writing the target.

This denial is not bypassable by `--force`.

At minimum the following must deny with no file modification:

```text
python scripts/restore_v2.py \
  --output legacy/scriptops-v2-single.py \
  --force
```

The same must hold for syntactic aliases, relative paths, `..` paths that resolve into the repository, and symlink-mediated destinations that resolve into the repository where the selected implementation can determine the target safely.

If destination safety cannot be established unambiguously, deny.

Required invariant:

```text
HISTORICAL RESTORABILITY != AUTHORITY TO RESTORE UNSAFE ACTIVE CODE
```

### 5.4 Outside-repository reconstruction

Explicit reconstruction to a path outside the repository remains permitted as a historical recovery operation, for example an operator-selected temporary directory.

That reconstructed historical file is not active runtime authority and is not accepted by the X1B approval path merely because it has the historical hash.

## 6. F001 correction — repository verification becomes split-source verification

Future `scripts/verify_repository.py` must separately validate two different things.

### 6.1 Historical transport validation

The verifier must require the seven historical part files and reconstruct them in memory.

It must prove:

```text
historical reconstructed SHA-256 = 881dade6c6c506b9a9d41ebfbf68afb18b66db7583d35f746fb29ed7b36ac596
historical reconstructed size = 51980
historical bytes decode as UTF-8
historical source compiles as Python
```

The historical transport remains fully auditable and reproducible.

### 6.2 Active runtime validation

Separately, the verifier must require `legacy/scriptops-v2-single.py` to exist as the active runtime substrate and be valid UTF-8/Python source.

It must not require active-runtime bytes, hash, or size to equal the historical reconstructed artifact.

It must not fail merely because X1B correction changes active legacy code while historical transport remains unchanged.

Repository X1B safety is instead established by the corrected executable tests and repository safety checks.

Required invariant:

```text
HISTORICAL TRANSPORT REPRODUCIBLE
+
ACTIVE RUNTIME CORRECTED
```

not:

```text
ACTIVE RUNTIME == HISTORICAL UNSAFE BYTES
```

### 6.3 Remove obsolete approval markers

The corrected repository verifier must remove any requirement that the current Phase-6 runtime contain:

```text
approve --why
```

or that the current smoke suite contain:

```text
test_approve_requires_explicit_why
```

Those are historical Phase-6 proof markers, not current Human-authority safety requirements after X1B correction.

Historical documentation/evidence may still preserve them as historical text; current executable verification must not require their continued operability.

### 6.4 Existing repository workflow

`.github/workflows/verify-repository.yml` is expected to remain structurally unchanged and continue running:

```text
python scripts/verify_repository.py
```

The corrected verifier must pass under that existing workflow.

If a later implementation concludes a workflow change is technically necessary, that is outside the expected R3 implementation surface and requires explicit justification plus independent implementation review before being treated as allowed.

## 7. F001 correction — historical documentation no longer creates unsafe runtime authority

The future implementation surface includes:

```text
sources/prototype/RESTORE.md
SOURCE_MANIFEST.md
```

They must preserve historical provenance while removing statements that make `legacy/scriptops-v2-single.py` the byte-identical canonical historical copy.

They must instead state clearly:

```text
sources/prototype/*.part = immutable historical transport/reconstruction evidence
legacy/scriptops-v2-single.py = active runtime substrate and may contain reviewed safety corrections
```

They must no longer instruct operators to run a command that writes historical bytes into active legacy runtime.

Historical reconstruction instructions must point only to explicit destinations outside the repository and must state that reconstruction does not make the resulting file an active trusted ScriptOps runtime.

## 8. F001 correction — direct legacy acceptance remains permanently fail-closed

`legacy/scriptops-v2-single.py` remains inside the implementation surface because Phase-6 loads it as substrate.

Its direct standalone `approve` command must become deterministically non-effect-capable.

An invocation equivalent to:

```text
python legacy/scriptops-v2-single.py approve --scene SCN-XYZ
```

must terminate nonzero before any:

- canonical scene write;
- scene status transition;
- decision-log append;
- Human attribution;
- Git staging;
- Git commit.

The compatibility message may direct the operator to the corrected Phase-6 decision-PR path, but legacy must not delegate an unverified effect.

Because historical reconstruction can no longer overwrite active repository files, the corrected denial cannot be reversed through the repository-provided restore command.

Required invariant:

```text
ONE OPERATIVE ACCEPTANCE EFFECT PATH
=
X1B-VALIDATED PHASE6 PATH
```

and:

```text
SAFE NEW PATH + RESTORABLE UNSAFE OLD PATH = NOT CLOSED
```

R3 removes the second term by removing repository-internal historical restoration authority.

## 9. Phase-6 approval interface and smoke-test supersession

The sole operative X1B acceptance effect interface remains:

```text
python phase6/scriptops-v2-hardening.py approve --decision-pr <positive-integer>
```

The command accepts no caller-controlled Human rationale, request path, request digest, Human actor, scene ID, task ID, candidate path, candidate hash, impact-report identity, canonical target, or effect type.

The decision PR number is a locator only, never authority.

The existing `tests/test_phase6_scriptops_smoke.py` must be updated because its current happy path executes:

```text
approve --scene SCN-001 --why <text>
```

and therefore encodes the defect-era authority contract.

The corrected smoke suite must preserve unrelated Phase-6 B1–B5 behavior but must not treat caller `--why` as Human authority.

The obsolete test:

`test_approve_requires_explicit_why`

must cease to be a current normative safety requirement.

Approval-positive coverage may be moved to the dedicated X1B test suite using controlled trusted-evidence fixtures, while the Phase-6 smoke suite can preserve deterministic non-live coverage for review/preflight/context/candidate/impact stages and explicit denial of legacy/obsolete approval forms.

The existing `.github/workflows/phase6-scriptops-smoke.yml` is expected to remain structurally unchanged and to continue running the corrected repository verifier and the `test_phase6_*.py` suite.

## 10. HumanDecisionRequestV1 — preserved exact binding

R3 preserves the corrected deterministic request contract from R2.

`HumanDecisionRequestV1` is a proposal artifact, never a Human decision.

Required conceptual binding payload:

```text
schema_version
repository
repository_head_at_request
request_created_at
task_id
scene_id
candidate_path
candidate_file_sha256
impact_report_path
impact_report_sha256
canonical_target
effect_type
presented_material_effect
```

Required constants:

```text
schema_version = scriptops-x1b-human-decision-request/v1
repository = FJ899/scriptops
effect_type = ACCEPT_SCENE_CANDIDATE
canonical_target = scenes/<scene_id>.fountain
```

Canonical request identity remains:

```text
request_binding_json = canonical_json(binding_payload)
request_digest = sha256(request_binding_json UTF-8 bytes)
decision_request_id = "x1b:" + request_digest
```

The verifier recomputes all identities and rejects mismatch.

`DECISION REQUEST != HUMAN DECISION`

## 11. Exact one-file decision-PR contract — preserved

The only valid request artifact path remains:

```text
decisions/x1b/<request_digest>.json
```

The only valid proposal branch form remains:

```text
decision/x1b/<request_digest>
```

The proposal branch must originate directly from `repository_head_at_request`, and its request commit must have that exact SHA as direct parent.

A valid decision PR must target `main`, bind the exact base SHA, remain `OPEN / UNMERGED`, and have the exact derived head ref.

Complete BASE-to-HEAD changed-file enumeration must prove exactly one added file at the derived request path.

No caller-supplied request path is accepted.

Require exact equality among:

```text
filename digest
computed request_digest
decision_request_id suffix
request.request_digest
head-ref digest
```

Any mismatch, additional changed file, rename, deletion, wrong base, wrong parent, hidden pagination remainder, or ambiguous changed-file state denies.

Proposal preparation remains separate from Human decision authority and separate from the effect invocation.

## 12. Manual Human review contract — preserved

The authoritative Human actor for this bounded correction remains exactly:

`litrgratis-pixel`

The Human governance act is one manual GitHub `APPROVE` review on the exact current decision-PR HEAD.

Required review state:

`APPROVED`

Required exact body contract remains:

```text
X1B-HUMAN-DECISION-V1
decision_request_id=<exact decision_request_id>
decision_request_sha256=<exact request_digest>
why=<non-empty Human rationale>
```

The validated rationale from that exact Human review is the only Human rationale that may enter durable attribution.

Caller `--why` is not Human evidence and is not an operative approval parameter.

## 13. Complete Human-review set semantics — preserved

The trusted adapter must enumerate the complete review set with fail-closed pagination.

At minimum:

1. request pages with `per_page=100`;
2. continue until completion is proven by an empty page or fewer than 100 records;
3. retain all fields required for validation;
4. require stable review identity, actor, state, commit ID, body, and submitted time;
5. reject duplicate IDs/node IDs;
6. deny on network/API/parse/pagination ambiguity or inability to prove completeness.

State semantics remain:

```text
APPROVED = active positive decision
CHANGES_REQUESTED = active negative/conflicting decision
COMMENTED = nondecision
DISMISSED = inactive
unknown/unparseable = DENY
```

For the exact current PR HEAD, require exactly one active valid matching approval from `litrgratis-pixel` and zero other active decision-bearing reviews by that actor on the same HEAD.

No chronology-only latest-wins rule exists.

## 14. F002 correction — exact public trusted transport origin

R3 freezes the production trusted evidence transport rather than leaving transport-origin semantics to the implementer.

### 14.1 Exact trusted API origin

The only trusted GitHub API origin for this bounded mechanism is:

```text
https://api.github.com
```

The production effect verifier constructs only exact REST paths for repository:

`FJ899/scriptops`

No caller option, repository config, environment variable, or request artifact may select or override the API host/base URL.

Environment-configured GitHub API endpoints are not read.

### 14.2 Standard-library transport profile

The production adapter must use Python standard-library HTTP/TLS primitives based on:

```text
urllib.request
ssl
```

It must construct an explicit opener that includes:

```text
ProxyHandler({})
```

so ambient HTTP/HTTPS proxy configuration is not used for trusted evidence acquisition.

It must use an explicit HTTPS handler/context based on:

```text
ssl.create_default_context()
```

using the host operating system/Python normal default root trust configuration after the environment checks below.

System DNS and the normal host root trust store are explicit bounded platform dependencies of this mechanism.

### 14.3 Environment fail-closed gate

Before trusted remote evidence acquisition and before canonical effect, the approval invocation must deny if any of these variables has a non-empty value:

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

The implementation may expand this fail-closed deny list if independent review determines additional standard ambient transport/auth variables are relevant; it may not weaken the listed minimum.

There is no caller override.

### 14.4 No credential or authenticated fallback

The trusted public evidence adapter sends no `Authorization` header and consumes no GitHub API credential.

There is no authenticated fallback.

It must not invoke `gh`, read GitHub CLI authentication, use `.netrc`, use Git credential helpers for HTTP evidence acquisition, accept caller-provided headers, or consume browser state.

### 14.5 Redirect policy

Trusted evidence requests must reject every HTTP redirect rather than following it.

A 3xx response is fail-closed.

The adapter must not accept a response whose effective trusted origin is anything other than the exact requested `https://api.github.com` origin.

Cross-origin redirects are always denied; same-origin redirects are also denied under the simpler bounded R3 policy.

### 14.6 Response and failure semantics

Network error, TLS error, DNS error, HTTP ambiguity, rate limiting preventing complete evidence collection, malformed JSON, unexpected content shape, repository visibility/authentication challenge, pagination uncertainty, redirect, or inability to establish the exact expected public API response yields:

`DENY / BLOCKED`

before canonical effect.

No cached approval, local review-shaped JSON, caller assertion, prior read, or alternate endpoint may substitute.

Preserve:

```text
NO AUTH CREDENTIAL != TRUSTED REMOTE ORIGIN BY ITSELF
REVIEW-SHAPED JSON != TRUSTED GITHUB REVIEW EVIDENCE
```

## 15. Local Git and effect-runtime capability isolation

The approval invocation performs no network Git operation.

It may use local Git only for repository identity/state checks and the exact local effect commit.

Local Git subprocesses in the approval path must use an explicitly constructed environment that removes denied GitHub credential variables and disables interactive/helper credential acquisition.

At minimum:

```text
GIT_TERMINAL_PROMPT=0
GCM_INTERACTIVE=never
```

and local Git commands must explicitly disable credential helpers for that process, equivalent to:

```text
git -c credential.helper= ...
```

The approval path must not invoke `fetch`, `pull`, `push`, `ls-remote`, remote submodule operations, or other network Git commands.

The evaluated ScriptOps effect runtime therefore has no Human-review creation capability and no authenticated GitHub evidence capability.

## 16. Preliminary HumanDecisionAdmissionV1

R3 preserves `HumanDecisionAdmissionV1` as a preliminary process-local proof-bearing admission created after complete request, PR, Human review, local state, transport-environment, and bounded replay validation.

Required fields include at minimum:

```text
admission_version
admission_id
repository
repository_head_at_request
decision_pr_number
decision_pr_head
decision_request_id
request_digest
request_file_path
human_review_node_id
human_review_numeric_id
human_actor
human_review_body_sha256
human_review_submitted_at
human_rationale
task_id
scene_id
candidate_path
candidate_file_sha256
impact_report_path
impact_report_sha256
canonical_target
effect_type
presented_material_effect_digest
canonical_instance_scope
```

Required version:

`scriptops-x1b-human-decision-admission/v1`

Admission identity remains deterministic over all identity fields other than `admission_id`.

The admission is process-local, one-shot, not serializable as a bearer credential, and cannot be supplied by a later caller as trusted evidence.

R3 makes explicit:

`HUMAN DECISION ADMISSION != FINAL EFFECT COMMITMENT`

## 17. F003 correction — FinalEffectGateV1 and Human-currentness linearization point

R3 resolves the unresolved post-admission revocation/currentness race by introducing an explicit final effect gate.

### 17.1 Mandatory fresh remote reread

Immediately before the first canonical mutation, after preliminary `HumanDecisionAdmissionV1` exists, the executor/verifier must perform a fresh trusted public GitHub read of:

- the decision PR state;
- the exact current decision PR HEAD;
- the complete paginated review set.

It must rerun the same current Human-decision validity/conflict rules against the exact request and preliminary admission.

This final remote validation is mandatory even if preliminary admission was issued moments earlier.

### 17.2 FinalEffectGateV1

Only a successful final validation may produce a process-local one-shot `FinalEffectGateV1` or equivalent final-gate state.

The final gate must bind at minimum:

```text
final_gate_version
admission_id
decision_pr_number
decision_pr_head
human_review_node_id
human_review_numeric_id
human_actor
human_review_body_sha256
complete_review_set_digest
current_human_decision_valid = true
local_head
scene_id
task_id
candidate_file_sha256
impact_report_sha256
canonical_target
effect_type
canonical_instance_scope
observed_at
```

The complete review-set digest must deterministically identify the exact complete review collection used for final currentness validation.

The final gate is in-memory, one-shot, process-local, and cannot be supplied by a caller.

### 17.3 Mandatory deny cases before final gate

The final gate must deny if, before it is issued:

```text
bound approval was dismissed
CHANGES_REQUESTED became active
another conflicting/ambiguous authoritative-Human decision appeared
decision PR was closed
decision PR was merged
decision PR HEAD changed
bound approval became malformed or mismatched
complete review set cannot be obtained
network/rate-limit/API state is ambiguous
local HEAD changed
candidate/impact/scope/target/effect identity changed
bounded request consumption already occurred
```

### 17.4 Exact Human-currentness commitment point

R3 freezes the authority linearization rule:

```text
Human-currentness commitment point
=
successful completion of FinalEffectGateV1 validation
immediately before the first canonical mutation
```

Before this commitment point, a Human/GitHub state change can revoke or conflict with the proposed effect and must be observed by the final reread when it is visible through the trusted source.

After this commitment point, a later Human/GitHub state change does not retroactively revoke the already-authorized one-shot same-process effect.

This is a bounded linearization contract, not a claim of distributed atomicity with GitHub.

### 17.5 No intervening blocking boundary

After successful final-gate creation and before the first canonical mutation, the implementation must perform no:

- user interaction;
- network operation;
- sleep/wait;
- unrelated subprocess;
- unrelated filesystem operation;
- other intentionally blocking operation.

Only deterministic in-process final gate integrity checks and the immediate canonical mutation sequence may intervene.

If the implementation cannot preserve this immediate transition, it must not claim the R3 currentness cutoff is satisfied.

## 18. Executor non-substitution after final gate

Immediately before and during the canonical effect sequence, the executor must consume exactly the final-gate/admission-bound operation.

No caller override may replace or reinterpret:

```text
Human actor
Human decision result
Human rationale
request identity
scene/scope
task ID
candidate
impact report
canonical target
effect type
```

The executor must verify final gate structural integrity and that it corresponds to the exact preliminary admission and current local operation identity.

Any mismatch denies before the first mutation.

After the first mutation begins, the effect sequence must not substitute another candidate/scope/target/effect.

## 19. Bounded replay semantics — preserved

R3 preserves the explicit bounded replay rule:

```text
one decision_request_id
may cause at most one successful acceptance effect
within one canonical ScriptOps repository execution instance
```

The durable local decision log must contain no successful X1B acceptance record consuming that exact request before effect.

After successful effect, the exact request ID is consumed in that same canonical instance.

Repeated invocation in the same canonical instance denies.

Explicit non-claim:

`NO GLOBAL CROSS-CLONE EXACTLY-ONCE CLAIM`

A changed repository HEAD, candidate, scene/scope, task, impact report, target, effect, material-effect identity, decision PR HEAD, request bytes, or request digest requires a new Human decision.

`OLD CONSENT + CHANGED OPERATION = DENY`

## 20. Evidence-derived durable Human attribution

The corrected Phase-6 durable decision record must derive Human attribution only from the validated Human review/final gate.

It must contain reconstructable provenance including at minimum:

```text
decision_request_id
request_digest
decision_pr_number
decision_pr_head
human_review_node_id
human_review_numeric_id
human_actor
human_review_commit
human_review_body_sha256
human_review_submitted_at
human_rationale
admission_id
final_review_set_digest
task_id
scene_id
candidate_file_sha256
impact_report_path
impact_report_sha256
scene_hash
artifact_hash
scene_version
effect_type
canonical_instance_scope
```

If a compatibility field named `approver` remains, its value must be derived from validated `human_actor`; unconditional `"human"` is prohibited.

Caller text is never stored as Human rationale.

Direct legacy approval cannot emit a Human-attributed acceptance record because it denies before effect.

## 21. Exact future implementation surface

The expected bounded R3 implementation candidate is limited to:

```text
phase6/scriptops-v2-hardening.py
legacy/scriptops-v2-single.py
phase6/x1b_human_decision.py

scripts/restore_v2.py
scripts/verify_repository.py

sources/prototype/RESTORE.md
SOURCE_MANIFEST.md

tests/test_phase6_scriptops_smoke.py
tests/test_x1b_human_decision.py

.github/workflows/x1b-human-decision.yml
```

Expected roles:

### `phase6/scriptops-v2-hardening.py`

- expose only `approve --decision-pr <N>` for operative acceptance;
- remove caller rationale/semantic-authority inputs;
- perform environment preflight;
- invoke trusted request/review verification;
- create preliminary admission;
- perform final-gate currentness reread immediately before effect;
- execute only final-gate-bound operation;
- derive durable Human attribution from validated evidence.

### `legacy/scriptops-v2-single.py`

- remain active runtime substrate for non-approval functions needed by Phase-6;
- make direct legacy `approve` deterministically no-effect/nonzero;
- no Human attribution/canonical mutation on the disabled path.

### `phase6/x1b_human_decision.py`

- canonical request parsing and identity recomputation;
- deterministic decision-PR validation;
- exact trusted public HTTP transport implementation;
- complete review pagination/state validation;
- local-state binding validation;
- bounded replay check;
- preliminary admission construction/integrity;
- final currentness reread and `FinalEffectGateV1` construction.

Production APIs must not accept caller-created trusted snapshots/admissions/final gates as evidence. Explicit fake adapters may exist only behind test-only construction paths.

### `scripts/restore_v2.py`

- verify/reconstruct immutable historical transport;
- never write historical reconstruction into any repository-internal path;
- no active-legacy default output.

### `scripts/verify_repository.py`

- split historical transport verification from active runtime verification;
- stop requiring active legacy byte identity with historical transport;
- stop requiring obsolete `approve --why` / explicit-why test markers.

### `sources/prototype/RESTORE.md` and `SOURCE_MANIFEST.md`

- preserve historical provenance;
- document split historical transport vs active runtime;
- remove unsafe restore-to-active instructions.

### `tests/test_phase6_scriptops_smoke.py`

- preserve non-X1B Phase-6 deterministic smoke behavior;
- supersede defect-era approval expectations;
- never use caller `--why` as Human authority.

### `tests/test_x1b_human_decision.py`

- deterministic unit/regression/adversarial matrix;
- temporary/disposable local repositories only;
- controlled fake remote adapters for non-live tests;
- no user screenplay canon mutation.

### `.github/workflows/x1b-human-decision.yml`

- deterministic CI only;
- no live Human decision creation;
- no GitHub write credential requirement;
- no user-canon effect.

Expected unchanged unless an independent later review proves technical necessity:

```text
.github/workflows/verify-repository.yml
.github/workflows/phase6-scriptops-smoke.yml
sources/prototype/scriptops-v2-single.py.part01..part07
```

No silent surface expansion is permitted under a later implementation authorization.

## 22. Mandatory R3 executable regressions — source-of-truth and restore

Future implementation tests must prove all of:

1. historical seven-part reconstruction still yields exact historical SHA-256 and size;
2. historical parts themselves are unchanged;
3. corrected active legacy is not required to equal historical reconstructed bytes;
4. `restore_v2.py --check-only` validates historical transport without writing active runtime;
5. reconstruction to explicit outside-repository path succeeds where otherwise valid;
6. reconstruction targeting active legacy denies;
7. reconstruction targeting any other repository-internal path denies;
8. `--force` does not bypass repository-root exclusion;
9. relative/`..` path resolving into repo denies;
10. no denied restore attempt modifies target or Git state;
11. corrected `verify_repository.py` passes the split-source contract;
12. existing verify workflow remains compatible with corrected verifier.

## 23. Mandatory R3 executable regressions — Phase-6/legacy effect surface

At minimum:

- direct `legacy ... approve --scene` returns nonzero;
- canonical scene unchanged;
- decision log unchanged;
- no Human attribution created;
- Git HEAD unchanged;
- worktree unchanged;
- obsolete Phase-6 `approve --scene ... --why ...` is not an operative Human-authority path;
- caller `--why` cannot establish HumanDecision;
- corrected Phase-6 smoke suite remains green for unrelated B1–B5 behavior;
- complete candidate tree is inventoried for alternate canonical scene-acceptance or Human-attribution write paths;
- any alternate operative effect path not routed through X1B admission/final gate is a blocker.

## 24. Mandatory R3 executable regressions — trusted transport

Tests must inject or simulate at minimum:

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

Each non-empty denied variable must cause fail-closed termination before trusted remote evidence acquisition/canonical effect.

Also test:

- attempted Authorization-header construction -> test failure/deny;
- attempted authenticated fallback -> deny;
- attempted `gh` use -> test failure;
- custom API-host/base-url injection -> impossible or deny;
- HTTP redirect -> deny;
- cross-origin redirect -> deny;
- same-origin redirect -> deny under R3 policy;
- proxy configuration cannot influence the trusted opener;
- malformed/untrusted review-shaped response -> deny;
- rate limit/incomplete pagination -> deny/block;
- public visibility/auth challenge -> deny/block;
- local Git effect path performs no network Git command.

## 25. Mandatory R3 executable regressions — final currentness gate

Tests must prove:

```text
valid preliminary admission
+
review dismissed before final gate
-> DENY
```

```text
valid preliminary admission
+
CHANGES_REQUESTED before final gate
-> DENY
```

```text
valid preliminary admission
+
decision PR closed before final gate
-> DENY
```

```text
valid preliminary admission
+
decision PR HEAD drift before final gate
-> DENY
```

Also require:

- second conflicting authoritative-Human review before final gate -> deny;
- malformed changed approval before final gate -> deny;
- remote read failure at final gate -> deny;
- incomplete final review pagination -> deny;
- local HEAD/candidate/impact/scope/target/effect drift before final gate -> deny;
- final gate cannot be reused in later process/invocation;
- final gate cannot be supplied by caller;
- successful final gate is followed immediately by first canonical mutation with no additional network/user/blocking operation;
- test records the exact linearization rule and does not claim retroactive revocation after commitment.

## 26. Original X1B attack suite and prior negative matrix remain mandatory

R3 does not replace prior verification obligations.

The future candidate must still cover all ten original X1B attack classes:

1. AI marks its own proposal accepted.
2. Continue is treated as decision.
3. Silence/no response is treated as consent.
4. Old Human consent is reused for a new decision.
5. Human accepts A but A-prime becomes operative.
6. AI changes parameters after acceptance.
7. AI expands scope after acceptance.
8. General direction becomes Human-attributed specific parameters.
9. AI-generated artifact impersonates a Human decision.
10. AI-filled value is recorded as Human-chosen.

It must also preserve the deterministic request/PR negatives, review-state/conflict/pagination negatives, credential negatives, replay negatives, local substitution negatives, and real current ScriptOps regression established by prior briefs/reviews.

## 27. Real positive Human control — still separately authorized

The live positive control remains a later separately Human-authorized stage.

It must use exactly one disposable ScriptOps repository execution instance, one inert/synthetic scene, one exact HumanDecisionRequestV1, one dedicated one-file decision PR, one manual `APPROVE` by `litrgratis-pixel`, and one corrected Phase-6 `approve --decision-pr` invocation.

The effect invocation must use the exact production trusted public-read transport and final currentness gate.

No user screenplay canon may be mutated.

Before effect, freeze at minimum:

- exact implementation candidate HEAD/TREE/BLOB set;
- disposable canonical-instance pre-effect HEAD;
- exact request bytes/digest/PR shape;
- complete Human review set;
- exact Human review identity/body/hash;
- environment/transport preflight;
- expected content/scope/candidate/target/effect.

Post-effect truth must prove:

```text
executed content = Human-bound content
executed scope = Human-bound scope
executed candidate = Human-bound candidate
executed effect = Human-bound effect
durable Human actor = validated review actor
Human rationale = validated review rationale
same-instance request consumption recorded
legacy direct approve remains non-effect-capable
historical restore cannot reintroduce unsafe active legacy
```

The positive control does not establish global cross-clone exactly-once semantics.

## 28. CI boundary

CI is deterministic non-live verification only.

CI may use controlled fake adapters/responses to exercise request/review/final-gate logic, but production code paths must not accept caller-provided trusted snapshots.

CI must not:

- submit Human reviews;
- create a live Human decision;
- require GitHub write credentials;
- mutate user screenplay canon;
- claim the real positive Human control occurred.

`GREEN CI != REAL HUMAN POSITIVE CONTROL`

## 29. Future implementation candidate acceptance criteria

A later implementation candidate may be considered independently reviewable only if all are true:

1. exact separately authorized ScriptOps BASE is used;
2. complete changed-file set is within the exact authorized R3 implementation surface;
3. historical source parts remain unchanged;
4. historical transport still reconstructs exact historical SHA/size;
5. historical restore cannot write into repository root;
6. active corrected legacy is no longer required to equal historical bytes;
7. repository verifier implements split-source semantics;
8. repository and Phase-6 existing workflows remain coherent with corrected tests/verifier, unless a separately justified authorized change exists;
9. direct legacy approval is no-effect;
10. obsolete caller `--why` cannot establish Human authority;
11. operative Phase-6 approval accepts only decision PR locator as caller input;
12. deterministic request/PR contract is exact and fail-closed;
13. production public evidence transport uses exact api.github.com origin with no proxy/auth/custom-CA/env-host/redirect substitution;
14. complete review set semantics are fail-closed;
15. preliminary admission binds exact operation identity;
16. final Human currentness is freshly reread immediately before effect;
17. `FinalEffectGateV1` is the exact currentness linearization point;
18. no blocking/network/user interaction occurs between final-gate success and first mutation;
19. durable Human attribution is evidence-derived;
20. bounded same-instance replay denies repeated consumption;
21. all original, prior, and R3 negative regressions pass;
22. candidate-tree effect-entry inventory finds no unadmitted alternate canonical acceptance path;
23. implementation review finds no remaining authority/security semantic choice left to the implementer/executor.

## 30. Explicit non-goals and bounded dependencies

R3 does not claim:

- cryptographic proof of private Human mental state;
- cryptographic proof that the Human physically used a particular browser;
- global distributed exactly-once across arbitrary clones;
- authenticated GitHub evidence verification for private repositories;
- atomic revocation synchronized with GitHub after the final-gate commitment point;
- authority to change the established Human actor;
- authority to merge a decision PR or implementation candidate;
- X1B closure;
- Agency Kernel v1 authority.

Bounded platform dependencies include:

- public availability of exact `FJ899/scriptops` through `https://api.github.com`;
- system DNS;
- Python/OS normal TLS root trust store;
- GitHub public API semantics sufficient to read exact PR/review state completely.

If the repository becomes private or those bounded prerequisites cannot establish trusted complete evidence, the mechanism is `BLOCKED`; it does not fall back to authenticated reads.

## 31. Required governance sequence after R3

This R3 brief must receive an independent AK-CANON superseding implementation-brief R3 review before any code write.

If and only if that review yields PASS, a later Human Authorization may define a bounded implementation candidate with exact ScriptOps BASE and exact allowed changed paths.

After implementation, X1B still requires:

```text
independent implementation review
+
fresh preregistered corrective verification
+
all original/real/R3 negative controls
+
separately Human-authorized real positive Human control
+
exact post-effect truth
+
durable technical evidence
+
independent corrective-closure review
+
Human corrective-closure acceptance
```

Preserve:

```text
R3 IMPLEMENTATION-BRIEF REVIEW PASS != IMPLEMENTATION AUTHORITY
IMPLEMENTATION AUTHORITY != LIVE HUMAN CONTROL AUTHORITY
IMPLEMENTATION PASS != X1B CLOSED
TECHNICAL VERIFICATION PASS != HUMAN CLOSURE ACCEPTANCE
X1B CLOSED != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 32. STOP boundary

This document is the complete output of the superseding implementation-brief R3 preparation stage.

Do not modify ScriptOps from this brief without a separately authorized implementation stage after independent R3 brief review.

Do not create a Human decision PR or Human APPROVE under brief-preparation authority.

Do not execute the positive control.

Do not modify historical prototype transport parts under this brief.

Do not merge, close X1B, begin Agency Kernel v1, release, deploy, or tag.

`R3 BRIEF != IMPLEMENTATION AUTHORITY`

`R3 BRIEF PASS != X1B CLOSED`

`X1B REMAINS OPEN`
