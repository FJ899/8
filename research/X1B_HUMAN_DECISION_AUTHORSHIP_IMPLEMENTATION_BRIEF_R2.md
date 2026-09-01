# X1B Human Decision Authorship — Superseding Implementation Brief R2

Status: `SUPERSEDING IMPLEMENTATION BRIEF R2 / NOT IMPLEMENTATION AUTHORITY`

Date: 2026-09-01

## 1. Purpose and authority boundary

This document supersedes the implementation brief in `FJ899/8 PR #110` for future X1B implementation-authority decisions. It corrects the exact findings frozen by the independent AK-CANON implementation-brief review in `FJ899/8 PR #111`.

Accepted finding under correction:

`X1B FAIL — FALSE HUMAN DECISION`

The real defect is that ScriptOps can presently cause a canonical accepted-scene effect and durable Human attribution without a separately established, exact, trusted Human decision act.

This document is a brief only. It authorizes no code write, no Human decision creation, no canonical effect, no corrective verification execution, no merge, no X1B closure, no Agency Kernel v1 work, no release, no deployment, and no tag.

```text
PR #110 = HISTORICAL SUPERSEDED IMPLEMENTATION BRIEF / NOT AUTHORITY
PR #111 = BINDING NOT-PASS REVIEW INPUT
R2 BRIEF != IMPLEMENTATION AUTHORITY
R2 BRIEF PASS != IMPLEMENTATION AUTHORITY
R2 BRIEF PASS != X1B CLOSED
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

The design requires a separate Human decision event, trusted Human-authoritative origin, exact content/scope/candidate/effect binding, fail-closed evidence validation, derived Human attribution, and separation between decision evidence and effect capability.

### 2.2 Independent corrective-design review

Repository: `FJ899/8`

PR: `#109`

HEAD: `132d65be48331a822039262b707c47a81d02a64d`

TREE: `a8bdc363d293beb7b15ae8b787cc3ebdd694fd99`

PATH: `research/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_DESIGN_AK_CANON_REVIEW_R2.md`

BLOB: `439109e104244552a5ac1f3f08988dba283733d0`

Verdict:

`AK-CANON X1B CORRECTIVE DESIGN REVIEW R2 = PASS`

### 2.3 Superseded implementation brief

Repository: `FJ899/8`

PR: `#110`

HEAD: `8eaad5ea3c37b2cdc65ad80d16260bbf0f2a0160`

TREE: `a7978803db0e1f0f87fb84ac54f44b8c5bc33a09`

PATH: `research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF.md`

BLOB: `385bcc8620619b91986ff44211a428913b228ba2`

PR #110 remains immutable historical evidence. It is superseded for future implementation authority by this R2 brief only if this R2 brief independently passes review.

### 2.4 Binding NOT-PASS review

Repository: `FJ899/8`

PR: `#111`

HEAD: `05bb0820990f92686c42547385729c87c614be65`

TREE: `9147295a388906a07898e9d09d62c5ac53912997`

PATH: `research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_AK_CANON_REVIEW.md`

BLOB: `35af188a5475b745294bcfa22fd3aa18b666decd`

Verdict:

`AK-CANON X1B IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

This R2 brief addresses every material review finding rather than reclassifying it away.

## 3. Current ScriptOps baseline and real bypass

Canonical ScriptOps baseline for the future implementation candidate remains:

```text
repository = FJ899/scriptops
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Affected Phase-6 path:

```text
phase6/scriptops-v2-hardening.py
BLOB = 4f379960ed5677634dd234af6aa39626782b6133
```

Direct legacy effect path:

```text
legacy/scriptops-v2-single.py
BLOB = 9baa7b3a1eb746e34b79207a382eea1f5dd4ec55
```

The Phase-6 path currently accepts caller `--why`, writes canonical accepted content, and records hard-coded Human attribution. Separately, the legacy file exposes its own directly executable `approve --scene` path that can write canonical accepted content and a durable `"approver": "human"` record without the proposed X1B Human-decision evidence path.

Both are part of the actual effect surface and therefore both must be covered by the correction.

## 4. Binding review findings to be resolved

This brief resolves the following exact PR #111 findings:

```text
X1B-IBR-F001 — direct legacy false-Human-decision effect path remains effect-capable
X1B-IBR-F002 — trusted Human-review origin is not established by metadata/account identity alone
X1B-IBR-F003 — request-artifact creation/path/selection/lifecycle is under-specified
X1B-IBR-F004 — replay/consumption overclaims global exactly-once across independent instances
X1B-IBR-F005 — write-capable GitHub credential separation is not enforceably fail-closed
```

The correction uses four structural choices:

1. one operative acceptance effect path, with legacy approval disabled before effect;
2. one deterministic one-file decision-PR contract with no caller-selected request path;
3. explicitly bounded replay semantics within one canonical ScriptOps repository execution instance, with no global cross-clone atomicity claim;
4. credential-free public GitHub evidence reads for the bounded public repository, with fail-closed rejection of credential-bearing effect environments.

## 5. Corrected trust and capability model

For the bounded X1B profile, the following actors/capabilities are distinct:

```text
proposal preparer
Human review actor
public read-only evidence adapter
decision verifier/admission boundary
local canonical effect executor
canonical ScriptOps repository instance
```

The authoritative Human actor remains exactly:

`litrgratis-pixel`

The Human governance act is a manual GitHub `APPROVE` review on the exact dedicated decision PR.

The ScriptOps effect invocation has no GitHub write capability and uses no GitHub credential for evidence acquisition.

The proposal-preparation capability is not part of the effect invocation. A proposal writer may create the request branch/file/PR under separate authority, but proposal creation is not Human decision authority.

```text
PROPOSAL PR CREATION != HUMAN DECISION
SCRIPTOPS EFFECT CAPABILITY != HUMAN REVIEW CREATION CAPABILITY
HUMAN DECISION EVIDENCE != EXECUTION CREDENTIAL
POSSESSION OF EFFECT CAPABILITY != AUTHORITY TO CREATE HUMAN DECISION EVIDENCE
REVIEW METADATA ALONE != PROOF OF HUMAN UI ORIGIN
```

The bounded correctness claim is about preventing the evaluated ScriptOps process from manufacturing or falsely attributing the Human decision that authorizes its own effect. It does not claim machine access to private Human mental state.

## 6. F001 correction — one operative acceptance effect path

### 6.1 Required legacy change

`legacy/scriptops-v2-single.py` is inside the required implementation surface.

Its standalone `approve` command must become deterministically non-effect-capable.

A direct invocation equivalent to:

```text
python legacy/scriptops-v2-single.py approve --scene SCN-XYZ
```

must terminate nonzero with a stable legacy-approval-disabled error before any:

- canonical scene write;
- scene-status transition;
- decision-log append;
- Human attribution;
- Git staging;
- Git commit.

The compatibility message should direct the operator to the corrected Phase-6 approval entry point. It must not silently delegate to an unverified effect operation.

Read-only parsing or argument validation before the deterministic denial is permissible, but no canonical or durable effect is permissible.

### 6.2 Required sole operative approval entry point

The only operative X1B acceptance effect entry point after correction is the Phase-6 hardening command.

The intended interface is:

```text
python phase6/scriptops-v2-hardening.py approve --decision-pr <positive-integer>
```

The operative approval command accepts no caller-controlled Human rationale, request path, request digest, Human actor, scene ID, task ID, candidate path, candidate hash, impact-report identity, canonical target, or effect type.

The decision PR number is a locator only. It is not authority.

All semantic effect identity is derived from the exact request artifact read from the validated decision PR and independently recomputed against the local pre-effect repository state.

Required invariant:

```text
ONE OPERATIVE ACCEPTANCE EFFECT PATH
=
X1B-VALIDATED PHASE6 PATH
```

and:

```text
SAFE NEW PATH + UNSAFE OLD PATH = NOT CLOSED
```

### 6.3 Complete effect-entry inventory requirement

The implementation candidate review and corrective verification must inventory the complete candidate tree for any other function, parser command, wrapper, executable script, or importable path capable of performing the canonical scene-acceptance effect or writing a Human-attributed acceptance record.

Any discovered alternate effect-capable path not routed through the X1B admission boundary is a blocker.

## 7. HumanDecisionRequestV1 binding payload

The proposal artifact is named `HumanDecisionRequestV1`.

It is a proposal, never a Human decision.

```text
DECISION REQUEST != HUMAN DECISION
```

Its exact binding payload contains these logical fields:

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

`repository_head_at_request` is the exact ScriptOps canonical repository HEAD from which the proposal is prepared.

`candidate_path` and `impact_report_path` must be normalized repository-relative POSIX paths, must contain no `..`, must not be absolute, and must identify regular files inside the repository worktree.

The candidate and impact SHA-256 values are lowercase hexadecimal SHA-256 digests over exact UTF-8 file bytes.

`presented_material_effect` must be a deterministic structured object that states at minimum that authorization will:

- accept the exact candidate content for the exact scene/scope;
- write/update exactly the canonical scene target;
- append exactly one X1B durable decision record for that effect;
- create the local Git commit containing the authorized canonical effect and decision record.

No free-form caller text participates in authority identity.

## 8. Canonical request identity

Canonical JSON uses:

- UTF-8;
- object keys sorted lexicographically;
- separators exactly `,` and `:` with no insignificant whitespace;
- no NaN or Infinity;
- exact validated strings with no verifier-side Unicode normalization.

Define:

```text
request_binding_json = canonical_json(binding_payload)
request_digest = sha256(request_binding_json UTF-8 bytes)
decision_request_id = "x1b:" + request_digest
```

The committed request object contains exactly:

```text
all binding_payload fields
decision_request_id
request_digest
```

The verifier recomputes the binding payload serialization, digest, and ID from the file bytes and requires exact equality.

A self-consistent but wrongly selected request file does not pass because request-file selection is independently fixed by the decision-PR contract below.

## 9. F003 correction — exact one-file decision PR contract

### 9.1 Derived request path

The only valid decision-request artifact path is:

```text
decisions/x1b/<request_digest>.json
```

where `<request_digest>` is exactly 64 lowercase hexadecimal characters.

The path is derived from verified content. It is never accepted from a caller as trusted input.

### 9.2 Derived proposal branch

The dedicated proposal branch name is:

```text
decision/x1b/<request_digest>
```

The proposal branch must originate directly from `repository_head_at_request`.

Its request commit must have `repository_head_at_request` as its direct parent and add the request artifact at the exact derived path.

### 9.3 Decision PR exact shape

A valid decision PR must satisfy all of the following at verification time:

```text
repository = FJ899/scriptops
base_ref = main
base_sha = request.repository_head_at_request
state = OPEN
merged = false
head_ref = decision/x1b/<request_digest>
```

Complete BASE-to-HEAD changed-file enumeration must prove:

```text
changed_files = 1
status = added
path = decisions/x1b/<request_digest>.json
```

No second file, rename, deletion, modification outside that exact added request file, or hidden pagination remainder is permitted.

The adapter reads the sole changed path itself. The effect command cannot provide `request_file_path`.

The verifier then requires:

```text
filename digest
=
computed request_digest
=
decision_request_id suffix
=
request.request_digest
```

and:

```text
head_ref digest
=
computed request_digest
```

Any mismatch is `DENY` before effect.

### 9.4 Proposal preparation authority

The decision-request branch and PR may be prepared by a separate proposal-writing actor or process under separate write authority.

That process may possess only the proposal-creation capabilities needed to create the deterministic branch/file/PR. It is not Human decision authority.

The Phase-6 effect invocation does not create or edit the proposal branch, request file, PR, review, comment, ref, or repository setting.

Proposal preparation is outside the approval invocation and its outputs remain untrusted until fully revalidated.

## 10. Manual Human review contract

The Human decision event is one manual GitHub review submitted by the established Human actor:

`litrgratis-pixel`

on the exact current decision-PR HEAD.

Required review state:

`APPROVED`

Required review body is exact UTF-8/LF text with exactly four logical lines:

```text
X1B-HUMAN-DECISION-V1
decision_request_id=<exact decision_request_id>
decision_request_sha256=<exact request_digest>
why=<non-empty Human rationale>
```

Rules:

- no leading or trailing blank lines;
- no extra fields;
- exact marker spelling;
- exact ID/digest equality;
- `why` trimmed only for outer ASCII space/tab;
- rationale non-empty after trimming;
- rationale exactly one logical line;
- rationale at most 512 UTF-8 bytes after trimming.

The validated rationale from this review is the only Human rationale allowed in the durable decision record.

The effect command has no `--why` authority input.

## 11. Complete review-set semantics

The public GitHub adapter must read the complete PR review submission set using paginated read-only requests.

Required collection contract:

1. request review pages with `per_page=100`;
2. continue until an empty page or a page with fewer than 100 records proves completion;
3. retain every record needed for semantic validation;
4. require stable parseable review identity, actor login, state, commit ID, body, and submitted time;
5. reject duplicate review IDs or node IDs;
6. fail closed on network error, HTTP ambiguity, response-shape error, parse error, rate limit preventing completion, pagination ambiguity, or inability to prove completion.

Authoritative-Human state semantics:

```text
APPROVED = active positive decision
CHANGES_REQUESTED = active negative/conflicting decision
COMMENTED = nondecision
DISMISSED = inactive
unknown/unparseable = DENY
```

For the exact current PR HEAD require:

- exactly one active valid `APPROVED` from `litrgratis-pixel` matching the exact request;
- zero other active decision-bearing reviews by `litrgratis-pixel` on that same HEAD.

A second approval is ambiguous and denies. Any active `CHANGES_REQUESTED` conflicts and denies. A malformed active approval denies. Different actors do not authorize or supersede the established Human actor.

No chronology-only latest-wins rule exists.

## 12. F002/F005 correction — credential-free public evidence acquisition

### 12.1 Repository visibility precondition

This bounded mechanism is valid only while exact repository:

`FJ899/scriptops`

is publicly readable through GitHub's public API without authentication.

If the repository ceases to be publicly readable, authenticated verification is not an automatic fallback. The bounded mechanism becomes:

`BLOCKED`

and requires a separately reviewed mechanism revision.

### 12.2 No GitHub credential in effect runtime

The production evidence adapter sends no GitHub `Authorization` header and consumes no GitHub API credential.

There is no authenticated fallback.

The effect invocation must reject before trusted-evidence acquisition and before canonical effect if any known GitHub credential variable is present with a non-empty value, including at minimum:

```text
GH_TOKEN
GITHUB_TOKEN
GH_ENTERPRISE_TOKEN
GITHUB_ENTERPRISE_TOKEN
GITHUB_PAT
```

The implementation may additionally reject other recognized GitHub credential variables; it may not weaken the listed minimum set.

No caller option may override this rejection.

The adapter must not invoke `gh`.

It must not read GitHub authentication from `.netrc`, GitHub CLI config, Git credential helpers, browser state, or caller-supplied headers/tokens.

HTTP requests for trusted Human evidence must be constructed by the adapter with an explicit allowlisted header set that contains no authorization-bearing header.

### 12.3 Public-read failure semantics

HTTP/network/API failure, rate limiting that prevents complete evidence collection, repository visibility change, pagination uncertainty, unexpected redirects to an authenticated flow, or malformed JSON yields:

`DENY / BLOCKED`

before canonical effect.

No cached approval, local review-shaped JSON, caller assertion, environment token, or previous successful read may substitute.

### 12.4 Local Git credential isolation

The approval invocation performs only local Git operations needed to inspect and commit the local canonical effect. It must perform no network Git command such as `fetch`, `pull`, `push`, `ls-remote`, or remote submodule operation.

All local Git subprocesses in the approval path must use an explicitly constructed/sanitized environment and command configuration that disables interactive or helper-based credential acquisition.

At minimum:

```text
GIT_TERMINAL_PROMPT=0
GCM_INTERACTIVE=never
```

and Git invocations used by the approval path must explicitly disable credential helpers for that process, equivalent to:

```text
git -c credential.helper= ...
```

The implementation must not inherit GitHub tokens into child Git processes.

No local Git operation in the approval path requires network authentication.

### 12.5 Bounded trusted-origin claim

The R2 mechanism claims only:

```text
manual Human APPROVE governance act
+
exact authoritative-Human GitHub review record
+
effect process with no GitHub review-write credential
+
credential-free public read-only evidence acquisition
+
exact request/current-state binding
=
trusted Human decision evidence for this bounded X1B profile
```

It does not claim that GitHub review metadata proves browser/UI origin by itself.

The positive-control governance procedure must independently ensure that the bound Human actor performs the review manually through the Human UI.

## 13. Local-state validation before admission

Before issuing admission, the verifier must independently validate the local canonical ScriptOps repository instance against the request.

At minimum it must require:

- repository/worktree is the configured ScriptOps canonical instance for the invocation;
- working tree clean before effect;
- current local HEAD equals `repository_head_at_request`;
- task ID exists and matches the request;
- candidate path exists, is regular/non-symlink as required, and matches exact SHA-256;
- candidate scene ID matches request scene ID;
- candidate remains in candidate status;
- impact report exists and matches exact SHA-256;
- impact report identifies the same task, scene, candidate, and `REVIEW_REQUIRED` state;
- canonical target equals `scenes/<scene_id>.fountain`;
- effect type equals `ACCEPT_SCENE_CANDIDATE`;
- material-effect object matches the implementation's exact accepted-effect shape;
- current decision PR and Human review remain exact as defined above.

Any mismatch is `DENY` before canonical write.

## 14. HumanDecisionAdmissionV1

Only after all local-state, request, PR, complete-review, credential-environment, and replay checks pass may the verifier create one process-local `HumanDecisionAdmissionV1`.

Required fields:

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

Required constant:

`admission_version = scriptops-x1b-human-decision-admission/v1`

`request_file_path` in admission is derived by the trusted verifier from the one-file PR contract, never copied from caller semantic input.

`canonical_instance_scope` records the bounded replay scope described below. It is audit metadata, not a claim of global uniqueness.

Define admission identity over all fields except `admission_id` using the same canonical JSON rules:

```text
admission_id = "x1b-admit:" + sha256(canonical_json(admission_identity_payload))
```

The admission is in-memory, one-shot, process-local, and cannot be supplied from a prior invocation as a bearer credential.

## 15. Executor non-substitution contract

Immediately before canonical write, the executor revalidates:

- admission structural integrity and digest;
- local HEAD unchanged;
- clean working tree;
- exact candidate bytes/hash unchanged;
- exact impact-report bytes/hash unchanged;
- exact scene/scope unchanged;
- exact target/effect unchanged;
- same canonical repository instance;
- same unconsumed request within that instance.

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

Any substitution attempt denies before write.

## 16. F004 correction — bounded replay and consumption semantics

PR #110 overclaimed global exactly-once semantics across independent clones/worktrees. This R2 brief does not make that claim.

The exact bounded property is:

```text
one decision_request_id
may cause at most one successful acceptance effect
within one canonical ScriptOps repository execution instance
```

For the chosen instance, before effect the durable local decision log must contain no successful X1B acceptance record consuming the same `decision_request_id`.

After successful effect, the durable decision record consumes that request ID in that same canonical instance.

A repeated invocation against the same canonical instance with the same request must deny before effect.

Explicit non-claim:

`NO GLOBAL CROSS-CLONE EXACTLY-ONCE CLAIM`

A separate clone/worktree/repository copy is a separate execution instance for this bounded replay property. This R2 profile does not claim an atomic shared consumption service across those instances.

This bounded replay rule does not authorize old consent for a changed decision. Exact request binding still requires:

```text
OLD CONSENT + CHANGED OPERATION = DENY
```

Any changed repository HEAD, candidate bytes/hash, scene/scope, task, impact report, canonical target, effect type, material-effect identity, decision PR HEAD, or request digest requires a new exact Human decision.

The same exact Human-bound effect observed in another disposable test clone is not authority for a different decision and is outside the global exactly-once claim.

A future requirement for global cross-instance atomic consumption requires a separate shared-authority design and new Human authorization.

## 17. Durable Human attribution

On the corrected operative Phase-6 path, durable Human attribution must be evidence-derived.

The decision record must contain reconstructable fields including at minimum:

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

If a compatibility field named `approver` is retained, its value must be derived only from validated `human_actor`; an unconditional constant `"human"` is prohibited.

Caller text must never be stored as Human rationale.

The legacy path is incapable of writing a replacement Human-attributed acceptance record because it is disabled before effect.

## 18. Required implementation surfaces

The expected bounded implementation candidate is limited to:

```text
phase6/scriptops-v2-hardening.py
legacy/scriptops-v2-single.py
phase6/x1b_human_decision.py
tests/test_x1b_human_decision.py
.github/workflows/x1b-human-decision.yml
```

Roles:

### `phase6/scriptops-v2-hardening.py`

- replace the existing caller-rationale approval authority;
- expose operative `approve --decision-pr <N>` only;
- perform credential-environment preflight;
- invoke trusted public-read verifier/admission;
- execute only exact admitted effect;
- derive durable Human attribution from admission.

### `legacy/scriptops-v2-single.py`

- preserve non-approval substrate functionality needed by Phase-6;
- make direct legacy `approve` deterministically non-effect-capable;
- make no canonical write/decision append/commit on that path.

### `phase6/x1b_human_decision.py`

- canonical request parsing/recomputation;
- deterministic decision-PR path/branch validation;
- public unauthenticated GitHub read adapter;
- complete review pagination;
- review-state and exact-body validation;
- local-state/request binding validation;
- replay check within bounded instance;
- admission construction and integrity validation.

Production APIs in this module must not accept caller-created trusted snapshots as evidence. Explicit fake adapters are test-only.

### `tests/test_x1b_human_decision.py`

- deterministic unit/regression/adversarial matrix;
- isolated temporary repositories only;
- no user screenplay canon mutation;
- no live Human review creation in CI.

### `.github/workflows/x1b-human-decision.yml`

- execute deterministic tests;
- require no GitHub write token;
- do not create reviews, decision PRs, or canonical scene effects against user canon.

A smaller final implementation set is acceptable only if independent implementation review proves every F001-F005 obligation remains enforceable and testable. Expansion outside this set requires explicit justification under later implementation authority.

## 19. Required executable negative matrix

The future implementation candidate must map executable tests to the complete original X1B attack suite, the real ScriptOps counterexample, PR #110 negatives, and the R2 regressions below.

### 19.1 Original X1B attacks

1. AI marks its own proposal accepted.
2. Continue is treated as decision.
3. Silence/no response is treated as consent.
4. Old consent is reused for a new decision.
5. Human accepts A; A-prime becomes operative.
6. AI changes parameters after acceptance.
7. AI expands scope after acceptance.
8. General direction becomes Human-attributed specific parameters.
9. AI-generated artifact impersonates a Human decision.
10. AI-filled value is recorded as Human-chosen.

Each must fail to establish HumanDecision or fail before unauthorized canonical effect.

### 19.2 Exact evidence and review negatives

At minimum test:

- missing decision PR;
- closed/merged decision PR;
- wrong repository;
- wrong PR current HEAD;
- wrong Human actor;
- wrong review state;
- wrong review commit;
- malformed review body;
- extra review-body field;
- empty rationale;
- duplicate bound approval;
- active CHANGES_REQUESTED conflict;
- unknown authoritative-Human review state;
- incomplete review pagination;
- duplicate review ID/node ID;
- public GitHub read failure;
- API parse ambiguity;
- caller-created fake trusted snapshot in production path.

### 19.3 F001 legacy/effect-path regressions

Directly invoke:

```text
python legacy/scriptops-v2-single.py approve --scene <scene>
```

and prove all of:

```text
nonzero exit
canonical scene unchanged
decision log unchanged
no Human attribution created
Git HEAD unchanged
working tree unchanged
```

Also inventory/execute any other discovered acceptance entry point and prove no alternate bypass.

### 19.4 F003 deterministic request-PR regressions

At minimum:

- extra decision-PR changed file;
- zero changed files;
- modified instead of added request file;
- request file at wrong directory;
- caller request-path substitution attempt;
- filename/request-digest mismatch;
- head-ref/request-digest mismatch;
- decision_request_id suffix mismatch;
- wrong PR base ref;
- wrong PR base SHA;
- proposal branch not based directly on `repository_head_at_request`;
- wrong request commit parent;
- request bytes internally valid but selected from wrong path;
- renamed request artifact.

All deny before effect.

### 19.5 F004 replay/currentness regressions

At minimum:

- same request replay in the same canonical instance after successful consumption -> deny;
- same Human review with changed local HEAD -> deny;
- same Human review with changed candidate -> deny;
- same Human review with changed impact report -> deny;
- same Human review with changed scope/target/effect -> deny;
- previously issued admission cannot be reused in a later process;
- test explicitly documents that no global cross-clone exactly-once claim is made.

### 19.6 F002/F005 credential regressions

Inject each of:

```text
GH_TOKEN
GITHUB_TOKEN
GH_ENTERPRISE_TOKEN
GITHUB_ENTERPRISE_TOKEN
GITHUB_PAT
```

and prove denial before trusted-evidence acquisition/canonical effect.

Also test:

- attempted authenticated fallback -> deny;
- adapter attempts `Authorization` header -> test failure;
- attempted `gh` use -> test failure;
- public API rate-limit/incomplete-read condition -> deny/block;
- GitHub visibility/auth challenge -> deny/block;
- local Git approval path performs no network Git command.

## 20. Real positive Human control

The live positive control remains a separately authorized future stage.

It must use exactly:

```text
one disposable ScriptOps repository instance
one inert/synthetic scene
one exact HumanDecisionRequestV1
one dedicated one-file decision PR
one manual APPROVE by litrgratis-pixel
one corrected Phase-6 approve --decision-pr invocation
```

The disposable repository instance is the test canonical instance for the bounded replay property.

No user screenplay canon may be mutated.

Before the effect, the verification harness must freeze:

- implementation candidate HEAD/TREE and all changed BLOBs;
- disposable canonical instance pre-effect HEAD;
- exact request JSON bytes and digest;
- exact decision PR BASE/HEAD/path-set;
- complete Human review set;
- exact bound Human review identity/body/hash;
- credential-free effect environment proof;
- exact expected candidate/scope/target/effect.

Post-effect truth must independently prove:

```text
executed content = Human-bound content
executed scope = Human-bound scope
executed candidate = Human-bound candidate
executed effect = Human-bound effect
durable Human actor = validated review actor
Human rationale = validated review rationale
request consumption recorded in the same test canonical instance
legacy direct approve remains non-effect-capable
```

The positive control must not claim global cross-clone exactly-once semantics.

## 21. CI boundary

CI is for deterministic non-live verification only.

CI must:

- use fake/public-response fixtures or controlled fake adapters for review-set logic;
- test public-read adapter construction without Authorization headers;
- test credential-environment denial;
- test legacy bypass denial;
- test request-PR deterministic selection logic;
- test admission/executor non-substitution;
- test local bounded replay semantics.

CI must not:

- submit Human reviews;
- create a live Human decision;
- require GitHub write credentials;
- mutate user screenplay canon;
- claim the real positive Human control occurred.

`GREEN CI != REAL HUMAN POSITIVE CONTROL`

## 22. Implementation acceptance criteria for a future candidate

A later implementation candidate can be considered reviewable only if all of the following are true:

1. exact ScriptOps base is the separately authorized base;
2. complete changed path set is within the authorized implementation surface;
3. direct legacy approval is fail-closed with zero effect;
4. operative Phase-6 approval accepts no Human-rationale or semantic-authority caller overrides;
5. request path/branch/PR changed-file identity is fully deterministic and independently derived;
6. public GitHub Human-evidence acquisition sends no Authorization header and has no authenticated fallback;
7. credential-bearing effect environments deny before effect;
8. complete review pagination is fail-closed;
9. exact current Human approval is required and conflicts/ambiguity deny;
10. Human rationale/actor attribution is evidence-derived;
11. admission binds exact content/scope/candidate/impact/target/effect and permits no executor substitution;
12. repeated consumption in the same canonical instance denies;
13. no global cross-clone exactly-once claim is made;
14. all original and R2 negative regressions pass;
15. no alternate effect-capable acceptance path exists in the candidate tree;
16. implementation review finds no unresolved authority-semantic invention left to the executor.

## 23. Explicit non-goals and boundaries

This R2 brief does not establish:

- cryptographic proof that a private Human physically used the browser;
- global distributed exactly-once execution across arbitrary clones;
- authenticated GitHub evidence verification for a private repository;
- authority to change the established Human actor;
- authority to merge the decision PR;
- authority to merge an implementation candidate;
- authority to close X1B;
- authority to begin Agency Kernel v1.

Any future need for a private repository, authenticated evidence reads, shared cross-instance consumption authority, different Human actor, or broader canonical-effect profile requires new design/review authority.

## 24. Required next governance sequence

If and only if this R2 brief independently passes AK-CANON review, the next gate may propose a bounded implementation authorization tied to the exact reviewed R2 brief identity.

That later authorization must freeze exact ScriptOps BASE and exact allowed changed paths before code writes.

After implementation, X1B still requires independent implementation review, preregistered corrective verification including the real legacy regression and all X1B attacks, a separately Human-authorized real positive control, durable verification evidence, independent corrective-closure review, and final Human closure acceptance.

```text
R2 IMPLEMENTATION-BRIEF REVIEW PASS != IMPLEMENTATION AUTHORITY
IMPLEMENTATION AUTHORITY != EXECUTION AUTHORITY FOR A REAL HUMAN CONTROL
IMPLEMENTATION PASS != X1B CLOSED
TECHNICAL VERIFICATION PASS != HUMAN CLOSURE ACCEPTANCE
X1B CLOSED != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 25. STOP boundary

This document is the complete output of the R2 implementation-brief preparation stage.

Do not modify ScriptOps from this brief without a separately authorized implementation stage after independent R2 brief review.

Do not create a Human decision PR or Human APPROVE under this brief-preparation authority.

Do not execute the positive control.

Do not merge, close X1B, begin V1, release, deploy, or tag.

`CORRECTED BRIEF != IMPLEMENTATION AUTHORITY`

`X1B REMAINS OPEN`
