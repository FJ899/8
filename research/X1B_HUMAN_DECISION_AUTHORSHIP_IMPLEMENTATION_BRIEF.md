# X1B Human Decision Authorship — Implementation Brief

Status: `IMPLEMENTATION BRIEF / NOT IMPLEMENTATION AUTHORITY`

Date: 2026-09-01

## 1. Purpose and authority boundary

This brief concretizes the accepted X1B corrective design for the real ScriptOps false-Human-decision boundary.

Accepted finding:

`X1B FAIL — FALSE HUMAN DECISION`

The live defect remains the Phase-6 `cmd_approve` path where possession of the effect-capable CLI plus a non-empty caller rationale can cause the canonical scene effect and a durable record with hard-coded `"approver": "human"` without a separately established Human decision event.

This document selects and specifies a bounded implementation mechanism. It does not authorize any code write, Human decision creation, canonical scene effect, corrective verification run, merge, X1B closure, Agency Kernel v1 work, release, deployment, or tag.

`IMPLEMENTATION BRIEF != IMPLEMENTATION AUTHORITY`

`IMPLEMENTATION BRIEF PASS != X1B CLOSED`

`X1B CLOSED != V1 AUTHORITY`

`AI PROPOSES != HUMAN DECIDES`

## 2. Exact normative bindings

### 2.1 Corrective design

Repository: `FJ899/scriptops`

PR: `#34`

BASE: `2f22843ac570498b506101addeba5453ab777f08`

HEAD: `d7a5065c87e9a4b49fb608235c908bceac42b4b1`

TREE: `3140d0ac95c120a7b1532942bae2e0dad38b4839`

PATH: `governance/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_CANDIDATE.md`

BLOB: `dac16f109d1414a2208c2ed9a166ae9e9a329216`

### 2.2 Independent corrective-design review

Repository: `FJ899/8`

PR: `#109`

HEAD: `132d65be48331a822039262b707c47a81d02a64d`

TREE: `a8bdc363d293beb7b15ae8b787cc3ebdd694fd99`

PATH: `research/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_DESIGN_AK_CANON_REVIEW_R2.md`

BLOB: `439109e104244552a5ac1f3f08988dba283733d0`

Verdict: `AK-CANON X1B CORRECTIVE DESIGN REVIEW R2 = PASS`

The earlier pre-existing review-like commit `d7c28ce73c1d2916904acbd8b801ded2d6f7b0f2` is not normative review authority.

### 2.3 Current ScriptOps baseline

Repository: `FJ899/scriptops`

Canonical baseline HEAD: `2f22843ac570498b506101addeba5453ab777f08`

Canonical baseline TREE: `4215d9306392070e64c6fd74a6cfb813ca9d0601`

Affected path: `phase6/scriptops-v2-hardening.py`

Affected BLOB: `4f379960ed5677634dd234af6aa39626782b6133`

The implementation candidate must be based on this exact baseline unless a fresh Human authorization explicitly changes the base.

## 3. Bounded mechanism selection

The selected bounded mechanism is a **manual GitHub APPROVE review by the established Human actor `litrgratis-pixel` on a dedicated ScriptOps decision PR**, consumed by ScriptOps only through a read-only GitHub verification adapter.

The mechanism is accepted only because the implementation must establish the following properties, not because the product name is GitHub:

1. the evaluated ScriptOps effect process cannot create the Human review it consumes;
2. the review is bound to an exact decision-request PR HEAD and request digest;
3. the complete relevant Human review set is collected and evaluated fail-closed;
4. the Human attribution and Human rationale are derived from the validated Human review event;
5. the resulting machine admission binds one exact local effect and allows no caller substitution;
6. the real positive control requires a manual Human UI review and an isolated/disposable ScriptOps effect target.

`MECHANISM != PROPERTY`

`GITHUB IDENTITY ALONE != HUMAN DECISION ACT`

## 4. Threat-model and capability boundary

For this bounded implementation, the evaluated ScriptOps approval process consists of:

- the local ScriptOps effect-capable command;
- the X1B Human-decision verifier/admission module;
- its GitHub read adapter;
- the resulting local Git commit capability inside the chosen ScriptOps worktree/clone.

The evaluated process must not possess any capability that can create or alter the Human decision event. In particular, the verifier and effect command must not be provisioned with a GitHub credential capable of:

- creating PR reviews;
- approving or requesting changes;
- dismissing reviews;
- posting or editing issue/PR comments;
- creating or editing decision PR content;
- merging PRs;
- updating Git refs;
- mutating repository rules or settings.

A read-only GitHub credential may be consumed out of band if authentication is required for reliable API reads. Credential provisioning is outside the implementation and must not be logged or surfaced by ScriptOps.

The implementation must expose only a read interface for Human-decision verification.

Required separation:

```text
SCRIPTOPS EFFECT CAPABILITY
!=
GITHUB HUMAN REVIEW CREATION CAPABILITY
```

```text
HUMAN DECISION EVIDENCE
!=
EXECUTION CREDENTIAL
```

```text
POSSESSION OF EFFECT CAPABILITY
!=
AUTHORITY TO CREATE HUMAN DECISION EVIDENCE
```

The positive-control governance procedure additionally requires the established Human actor to submit the bound APPROVE review manually through the GitHub Human UI. The machine verifier does not claim that a GitHub review record by itself proves private Human mental state; X1B tests false system attribution, not private cognition.

## 5. Decision-request lifecycle

### 5.1 Proposal artifact

Before any Human decision, the system creates a proposal artifact named `HumanDecisionRequestV1` or an equivalent exact representation.

The request is an AI/process proposal and is never itself a Human decision.

`DECISION REQUEST != HUMAN DECISION`

The request must be committed on a dedicated ScriptOps decision-request branch and presented in a dedicated ScriptOps decision PR. That PR is the Human review surface.

### 5.2 Required request binding payload

The canonical request binding payload must contain exactly these logical fields:

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

Required constant values/constraints:

```text
schema_version = scriptops-x1b-human-decision-request/v1
repository = FJ899/scriptops
effect_type = ACCEPT_SCENE_CANDIDATE
canonical_target = scenes/<scene_id>.fountain
```

`repository_head_at_request` is the exact ScriptOps commit on which the request is based.

`request_created_at` is an offset-aware UTC timestamp used for provenance. This implementation does not use a wall-clock expiry rule. Freshness is state/binding based as defined below.

`presented_material_effect` must describe, in deterministic structured form, that approval will:

- transition the exact candidate from candidate semantics to accepted canonical scene content;
- write/update exactly the canonical scene target;
- append exactly one durable decision-log record;
- create a local Git commit containing the canonical effect and decision-log update.

The positive Human review must be presented with these material effect facts.

### 5.3 Canonical request identity

Canonical JSON rules:

- UTF-8;
- JSON object;
- keys sorted lexicographically;
- separators exactly `,` and `:` with no extra whitespace;
- no NaN/Infinity;
- strings used exactly as validated, with no Unicode normalization performed by the verifier.

Define:

```text
request_binding_json = canonical_json(binding_payload)
request_digest = sha256(request_binding_json UTF-8 bytes)
decision_request_id = "x1b:" + request_digest
```

The committed request object contains the binding payload plus:

```text
decision_request_id
request_digest
```

On read, the verifier recomputes both values and requires exact equality.

`SHAPE MATCH != TRUSTED ORIGIN`

## 6. Decision PR contract

A valid decision PR must satisfy all of the following at verification time:

- repository exactly `FJ899/scriptops`;
- state exactly `OPEN`;
- not merged;
- head SHA equals the SHA named by the Human review event;
- the PR HEAD contains exactly the request object selected by the caller/operation;
- the request object recomputes to the exact `decision_request_id` and `request_digest`;
- request `repository_head_at_request` equals the local ScriptOps pre-effect HEAD required by the operation;
- candidate/impact/scene/effect identities recompute from the local worktree and match the request exactly.

The implementation brief does not require the decision PR to be merged. It is an approval/evidence surface, not the canonical ScriptOps effect path.

A PR head change invalidates reviews on prior heads for purposes of this implementation. A new exact current-head Human decision is required.

## 7. Exact Human review-body contract

The Human review state must be exactly `APPROVED`.

The Human review body must be exact UTF-8 text with LF line endings and exactly four logical lines:

```text
X1B-HUMAN-DECISION-V1
decision_request_id=<exact decision_request_id>
decision_request_sha256=<exact request_digest>
why=<non-empty Human rationale>
```

Rules:

- no leading/trailing blank lines;
- no extra fields;
- `decision_request_id` and `decision_request_sha256` must match the request exactly;
- `why` is trimmed for outer ASCII space/tab only and must remain non-empty;
- `why` must be one logical line and no more than 512 UTF-8 bytes after trimming;
- the exact validated rationale string is the Human rationale recorded by ScriptOps;
- caller-provided `--why` must not be used as Human evidence or Human rationale.

A later implementation may remove `approve --why` or retain caller text only under a clearly non-Human field such as `executor_note`. It must not label caller text as Human rationale.

## 8. Established Human actor

For this bounded corrective implementation, the only Human decision authority is:

`litrgratis-pixel`

The verifier must compare the GitHub review actor login exactly.

Different-actor reviews cannot create, supersede, or satisfy the bound Human decision. They are retained as observable repository context but are not Human authority under this bounded policy.

`KNOWN DIFFERENT ACTOR != AUTHORIZED HUMAN ACTOR`

Changing the authoritative Human actor requires a new Human-governance decision and is not an implementation parameter.

## 9. Complete GitHub review collection

The GitHub adapter must collect the complete PR review submission set using paginated read-only API calls.

Required algorithmic contract:

1. request review pages with `per_page=100`;
2. continue page-by-page until an empty page or a page with fewer than 100 records establishes completion;
3. preserve every returned review record relevant to validation;
4. require stable parseable fields for review ID/node ID, actor login, state, commit ID, body, and submitted time;
5. reject duplicate review IDs/node IDs;
6. if any page read fails, is rate-limited without successful completion, is ambiguous, or cannot be proven complete, return `DENY/BLOCKED` before effect.

No local caller assertion such as `human_reviews_complete=True` may substitute for actual adapter completion in production code.

## 10. Review-state semantics

The implementation uses the following explicit review-state semantics for reviews by the authoritative Human actor:

```text
APPROVED          = active positive decision-bearing review
CHANGES_REQUESTED = active negative/conflicting decision-bearing review
COMMENTED         = nondecision
DISMISSED         = inactive
```

Any unknown or unparseable state from the authoritative Human actor is fail-closed.

The relevant decision set for the current operation consists of authoritative-Human decision-bearing reviews whose `commit_id` equals the exact current decision PR HEAD.

Reviews on a different commit do not authorize the current PR HEAD. They are historical for the current operation. Candidate/PR-head drift is independently a freshness failure until a new current-head decision exists.

For the exact current PR HEAD, require:

- exactly one valid active `APPROVED` review from `litrgratis-pixel` whose body matches the exact Human review-body contract and request identity;
- zero other active decision-bearing reviews by `litrgratis-pixel` on that same current PR HEAD.

Therefore:

- a second active `APPROVED` on the current head is ambiguous and denies;
- any active `CHANGES_REQUESTED` on the current head conflicts and denies;
- a malformed active `APPROVED` on the current head denies;
- `COMMENTED` reviews are ignored as decisions;
- `DISMISSED` reviews are inactive;
- reviews by another actor do not authorize or supersede this Human actor.

There is no implicit chronology-only latest-wins rule.

## 11. Freshness, staleness, replay, and consumption

A Human decision is valid only for the exact current operation bound by the request.

Evidence is stale and must deny if any of these differ from the request/admission:

- ScriptOps repository identity;
- local pre-effect repository HEAD;
- task ID;
- scene/scope;
- candidate path or SHA-256;
- impact-report path or SHA-256;
- canonical target;
- effect type;
- presented material-effect identity;
- decision PR HEAD;
- decision request digest/ID;
- authoritative Human review actor/state/body/commit.

No fixed wall-clock TTL is used in v1 of this bounded mechanism. `request_created_at` and review `submitted_at` are provenance fields, while operative freshness is exact-state based.

Replay rule:

- one `decision_request_id` may authorize at most one successful canonical ScriptOps acceptance effect;
- before effect, the current decision log must contain no successful active acceptance record with the same `decision_request_id`;
- after success, the durable decision record consumes that request ID;
- a repeated invocation with the same request is `DENY` before effect.

The machine admission is one-shot, in-memory, process-local, and valid only within the same `approve` command invocation. It is not persisted as a reusable bearer credential.

Currentness is evaluated when the admission is issued. A later GitHub state change does not retroactively rewrite an already-issued process-local one-shot admission. This is the explicit bounded revocation semantics; the implementation makes no claim of distributed atomic revocation between GitHub and the local filesystem after admission issuance.

## 12. Trusted adapter boundary

Define a read-only adapter interface equivalent to:

```text
read_decision_pr(repository, pr_number) -> TrustedDecisionPrSnapshot
```

The snapshot must include at minimum:

```text
repository
pr_number
pr_open
pr_merged
pr_head_sha
pr_base_ref
request_file_path
request_file_bytes
reviews_complete
reviews[]
```

Each review record must include:

```text
review_node_id
review_numeric_id
actor
state
commit_id
body
submitted_at
```

The adapter is responsible for authenticated/read-only transport and pagination completeness. The verifier is responsible for semantic validation.

Production code must not accept caller-created `TrustedDecisionPrSnapshot` as trusted evidence unless it came from the configured read-only adapter during the current invocation.

Unit tests may use explicit fake adapters because those tests are not production trust evidence.

## 13. Human-decision admission

After all request, local-state, PR-state, review-set, and replay checks pass, the verifier creates exactly one in-memory `HumanDecisionAdmissionV1`.

Required logical fields:

```text
admission_version
admission_id
repository
repository_head_at_request
decision_pr_number
decision_pr_head
decision_request_id
request_digest
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
```

Required constant:

`admission_version = scriptops-x1b-human-decision-admission/v1`

Define an identity payload consisting of all fields above except `admission_id`, canonicalize it with the same canonical JSON rules, and define:

```text
admission_id = "x1b-admit:" + sha256(canonical_json(identity_payload))
```

The executor must validate the admission structure and exact local pre-effect state before writing canonical content.

No caller override may replace or reinterpret:

- Human actor;
- decision result;
- Human rationale;
- request identity;
- task ID;
- scene/scope;
- candidate;
- impact report;
- canonical target;
- effect type.

`ADMISSION != CALLER PREFERENCE`

## 14. Corrected `cmd_approve` behavior

The implementation candidate must change the approval boundary so that a canonical acceptance effect cannot begin from `why != ""`.

Planned CLI contract:

```text
approve --scene <SCENE_ID> --decision-pr <PR_NUMBER>
```

The current `--why` argument is removed from the authoritative approval path.

If an optional executor note is retained, it must be named separately, e.g.:

```text
--executor-note <text>
```

and must never populate Human-attributed fields.

Required command sequence:

```text
require clean local pre-state
->
resolve exact staged candidate and exact impact report
->
build/recompute expected HumanDecisionRequest binding from local state
->
read complete decision PR state through read-only adapter
->
validate exact committed request bytes/digest
->
validate exact complete Human review set
->
validate no replay/consumption
->
issue one in-memory HumanDecisionAdmissionV1
->
revalidate exact local pre-effect state against admission
->
perform canonical scene write
->
append evidence-derived decision-log record
->
commit exactly the authorized local effect paths
->
verify post-effect truth
```

Any failure before the canonical write returns non-zero and produces no canonical scene or decision-log mutation.

## 15. Durable decision-log contract

The corrected durable decision record must no longer hard-code Human attribution.

It must include at minimum:

```text
id
timestamp
scope
status
type
human_actor
human_decision_review_node_id
human_decision_review_numeric_id
human_decision_pr
human_decision_pr_head
decision_request_id
decision_request_sha256
human_review_body_sha256
human_rationale
task_id
impact_report
impact_report_sha256
candidate_file_sha256
scene_hash
artifact_hash
scene_version
admission_id
```

Required values are derived from validated Human evidence and admission.

The old unconditional field:

```text
"approver": "human"
```

must be removed or replaced by explicit provenance fields above. If a compatibility `approver` field is retained temporarily, its value must be derived from the validated `human_actor` and must not be a hard-coded constant; the independent implementation review must treat such compatibility as a surface requiring justification.

`HUMAN ATTRIBUTION = DERIVED CLAIM`

## 16. Exact planned implementation surfaces

The bounded implementation candidate is expected to change exactly these surfaces unless the implementation authority later narrows them further:

```text
phase6/scriptops-v2-hardening.py
phase6/x1b_human_decision.py
tests/test_x1b_human_decision.py
.github/workflows/x1b-human-decision.yml
```

Responsibilities:

### `phase6/scriptops-v2-hardening.py`

- integrate `--decision-pr` approval flow;
- remove `--why` as Human-authorship authority;
- build local expected decision-request binding inputs;
- consume validated admission;
- write evidence-derived decision log;
- preserve existing Phase-6 clean-tree/checkpoint behavior outside the bounded approval correction.

### `phase6/x1b_human_decision.py`

- canonical request serialization/digest;
- exact review-body parser;
- trusted snapshot/review data structures;
- read-only adapter protocol;
- complete review-set semantic validation;
- Human-decision admission generation/validation;
- replay/freshness checks that do not require canonical effect writes.

The module must not contain GitHub review-write, merge, comment-write, ref-write, or governance-write operations.

### `tests/test_x1b_human_decision.py`

- deterministic unit/regression suite with fake read-only adapters and isolated temporary Git repositories/worktrees where needed;
- no real Human review creation;
- no user screenplay canon access.

### `.github/workflows/x1b-human-decision.yml`

- run deterministic X1B unit/regression tests;
- no GitHub write token requirement;
- no live positive Human control in CI;
- no canonical scene effect against user canon.

The existing `legacy/scriptops-v2-single.py` remains unchanged under the intended candidate. Any need to modify legacy requires a new Human decision before implementation.

## 17. Negative verification matrix

The implementation candidate tests must preregister and map at least the following executable negatives.

### Original X1B attacks

`X1B-N01` — AI/process marks its own proposal accepted without Human review -> `DENY`, no canonical effect.

`X1B-N02` — caller continuation/`Continue` without review -> `DENY`.

`X1B-N03` — silence/no Human review -> `DENY`.

`X1B-N04` — old review/request reused for changed candidate/head -> `DENY`.

`X1B-N05` — Human approved content A, operative candidate becomes A-prime -> `DENY`.

`X1B-N06` — parameter/candidate hash changes after approval -> `DENY`.

`X1B-N07` — scope/scene expands after approval -> `DENY`.

`X1B-N08` — Human approves general request but executor supplies specific unbound values -> `DENY`.

`X1B-N09` — AI-generated review-shaped JSON/local artifact without trusted GitHub origin -> `DENY`.

`X1B-N10` — AI/caller-filled rationale/value attempts to become Human-chosen field -> Human attribution must not be created; `DENY` where Human rationale is required.

### Real accepted regression

`X1B-N11` — invoke corrected effect path with only scene + non-empty caller rationale and no trusted Human review -> `DENY`; canonical target and decision log unchanged.

### Additional trusted-evidence negatives

`X1B-N12` — wrong actor APPROVED -> `DENY`.

`X1B-N13` — right actor, wrong PR head commit -> `DENY`.

`X1B-N14` — right actor/head, wrong request digest -> `DENY`.

`X1B-N15` — malformed review body -> `DENY`.

`X1B-N16` — active CHANGES_REQUESTED by authoritative Human on current head -> `DENY`.

`X1B-N17` — two active authoritative APPROVED reviews on current head -> `DENY` as ambiguous.

`X1B-N18` — incomplete pagination or adapter read failure -> `DENY/BLOCKED`.

`X1B-N19` — duplicate review IDs -> `DENY`.

`X1B-N20` — unknown authoritative-Human review state -> `DENY`.

`X1B-N21` — dismissed approval only -> `DENY`.

`X1B-N22` — COMMENTED review only -> `DENY`.

`X1B-N23` — decision request already consumed in decision log -> `DENY`.

`X1B-N24` — local repository HEAD differs from request `repository_head_at_request` -> `DENY`.

`X1B-N25` — impact-report bytes/hash drift -> `DENY`.

`X1B-N26` — canonical target/effect substitution attempt -> `DENY` before write.

`X1B-N27` — executor attempts to override Human actor, rationale, candidate, scope, target, or effect after admission -> `DENY`, no effect.

`X1B-N28` — caller supplies local snapshot marked complete without production adapter provenance -> production verifier rejects/non-constructible trust path.

Every negative must establish both the decision result and effect truth. A mere exception is insufficient if a canonical path changed.

## 18. Positive Human control contract

The corrective verification stage, not CI and not implementation development, must contain one separately Human-authorized live positive control.

The positive control must use:

- an inert/synthetic X1B scene with no user screenplay canon content;
- an isolated/disposable clone or worktree based on the exact implementation candidate;
- a dedicated ScriptOps decision PR containing the exact HumanDecisionRequestV1;
- manual GitHub APPROVE by `litrgratis-pixel` through the Human UI using the exact body contract;
- the actual corrected ScriptOps approval path with `--decision-pr`;
- read-only GitHub verification from the effect process.

No test credential available to the ScriptOps process may create the Human review.

Before the effect, freeze:

```text
implementation HEAD/TREE/BLOB set
disposable worktree pre-HEAD
scene/task/candidate/impact identities
decision PR number and exact HEAD
request bytes/digest/ID
complete Human review set
exact Human review identity/body/state/commit
expected canonical target and expected accepted content
```

Post-effect truth must independently establish:

```text
executed content = Human-bound content
executed scope = Human-bound scope
executed candidate = Human-bound candidate
executed effect = Human-bound effect
durable Human actor = exact validated review actor
Human rationale = exact review-bound rationale
decision request = exact validated request
admission = exact validated admission
```

It must also establish that no AI/process-created substitute Human evidence was accepted and no stale/conflicting Human event became operative.

A command exit code alone is not positive-control PASS.

`COMMAND SUCCESS != EFFECT TRUTH`

## 19. Post-effect verification

After any authorized acceptance effect, the executor/observer must verify at minimum:

- canonical scene path exists and has the expected accepted content/hash;
- only expected canonical effect paths were committed by the approval command;
- the decision-log record exists exactly once for the request ID;
- the record references the exact Human review and request identities;
- the recorded Human rationale equals the exact validated review rationale;
- the resulting Git commit contains the expected scene and decision-log delta;
- the working tree is clean.

Unexpected additional canonical changes are failure.

## 20. Error and fail-closed behavior

The production implementation must fail closed before canonical effect for:

- unavailable GitHub review state;
- incomplete pagination;
- authentication/read errors;
- missing decision PR;
- closed/merged/changed decision PR where current exact semantics are not satisfied;
- malformed request;
- request digest mismatch;
- candidate/impact/local-HEAD drift;
- missing, malformed, stale, conflicting, duplicate, or ambiguous Human review evidence;
- wrong Human actor;
- replay/consumption;
- admission mismatch;
- attempted executor substitution.

There is no fallback to:

- caller assertion;
- cached Human approval;
- local review-shaped JSON;
- `--why`;
- a Human username string;
- a non-empty rationale;
- `Continue`;
- silence;
- an alternate effect path.

`UNKNOWN TRUSTED EVIDENCE => DENY`

## 21. CI and secret discipline

The X1B workflow must run deterministic non-live tests only.

CI must not require or expose a Human review-write credential.

CI must not perform the real positive Human control.

If read-only GitHub API behavior requires integration coverage, use either contract fixtures or separately authorized read-only checks; do not make a write-capable token a test prerequisite.

Secrets must never appear in test output, durable evidence, exceptions, or decision logs.

## 22. Acceptance-stage evidence obligations

Before corrective execution, a future preregistration must freeze:

- exact implementation candidate HEAD/TREE and complete changed-path/BLOB set;
- independent implementation review identity/verdict;
- exact negative test matrix and expected outputs/effect invariants;
- exact disposable positive-control target;
- exact decision-request serialization and review-body contract;
- exact authoritative Human actor;
- exact read-only adapter interface and credential capability assumptions;
- exact complete-review collection semantics;
- exact admission serialization/digest rules;
- exact post-effect observation method;
- explicit STOP conditions.

The first credible false-Human-decision counterexample terminates the corrective-verification run and must be durably recorded before repair.

## 23. Implementation candidate success criteria

A future implementation candidate is eligible for independent implementation review only if:

1. its changed paths remain within the separately authorized implementation surface;
2. the accepted real regression no longer allows caller effect capability + non-empty rationale to create Human attribution/effect;
3. all deterministic negative tests pass with no unauthorized effect;
4. positive-path unit construction requires exact trusted Human evidence rather than caller labels;
5. production GitHub adapter is read-only by interface and contains no mutation action;
6. durable Human attribution/rationale are derived from the validated Human review;
7. exact request/admission binding and replay rules are implemented;
8. CI is green without live Human credentials;
9. implementation review finds no authority/capability collapse.

Green tests alone are not X1B closure.

## 24. Explicit non-claims and STOP boundary

This brief does not establish:

- universal Human identity or private mental state;
- phishing resistance;
- hardware-backed Human presence;
- production-grade distributed revocation;
- that any GitHub account action is always performed by a flesh-and-blood Human;
- X1B closure;
- Agency Kernel v1 authority.

It establishes a bounded implementation contract in which the evaluated ScriptOps effect process is incapable, under the frozen capability model, of manufacturing the exact Human review event that authorizes its own effect.

After this brief is frozen:

`STOP`

A separate independent AK-CANON implementation-brief review is required before any implementation code write.

Preserve:

```text
IMPLEMENTATION BRIEF PASS != IMPLEMENTATION AUTHORITY
IMPLEMENTATION CANDIDATE != X1B CLOSED
GREEN TESTS != X1B CLOSED
HUMAN REVIEW IDENTITY != HUMAN ACT BY ITSELF
EXECUTOR CAPABILITY != HUMAN DECISION AUTHORITY
AI PROPOSES != HUMAN DECIDES
X1B REMAINS OPEN
```
