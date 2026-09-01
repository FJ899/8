# X1B Human Decision Authorship — Independent AK-CANON Superseding Implementation-Brief R2 Review

Status: `INDEPENDENT R2 IMPLEMENTATION-BRIEF REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: 2026-09-01

Verdict:

`AK-CANON X1B SUPERSEDING IMPLEMENTATION-BRIEF R2 REVIEW = NOT PASS`

This review is bound only to the exact Human-authorized artifacts and live baseline below. It does not modify or repair PR #112 and does not authorize implementation, Human decision creation, corrective execution, canonical effect, merge, X1B closure, Agency Kernel v1, release, deployment, or tag.

`REVIEW FINDING != REPAIR AUTHORITY`

`R2 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY`

`X1B OPEN != V1 AUTHORITY`

`AI PROPOSES != HUMAN DECIDES`

## 1. Frozen review target

Repository: `FJ899/8`

PR: `#112`

Review-time state: `OPEN / DRAFT / UNMERGED`

BASE: `b2c92ec5cd8fbb7272d701d229adc8a8019f951e`

HEAD: `81177847ada75f874d4906c4f98c2bbc1b371dd3`

TREE: `2e1f9b469034decfe9c62bed161e065ffb29330b`

PATH: `research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R2.md`

BLOB: `40e4732f94152a9f46aa8fb158749dcf0bce3a26`

Complete BASE->HEAD changed-file set:

```text
research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R2.md
```

Exactly one changed path was independently reconfirmed.

## 2. Exact normative lineage

### 2.1 Corrective design

Repository: `FJ899/scriptops`

PR: `#34`

HEAD: `d7a5065c87e9a4b49fb608235c908bceac42b4b1`

TREE: `3140d0ac95c120a7b1532942bae2e0dad38b4839`

PATH: `governance/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_CANDIDATE.md`

BLOB: `dac16f109d1414a2208c2ed9a166ae9e9a329216`

The design requires a separate Human act, trusted Human-authoritative origin, exact content/scope/candidate/effect binding, explicit freshness/conflict/replay rules, fail-closed admission, executor non-substitution, and evidence-derived Human attribution.

### 2.2 Independent design review

Repository: `FJ899/8`

PR: `#109`

HEAD: `132d65be48331a822039262b707c47a81d02a64d`

TREE: `a8bdc363d293beb7b15ae8b787cc3ebdd694fd99`

PATH: `research/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_DESIGN_AK_CANON_REVIEW_R2.md`

BLOB: `439109e104244552a5ac1f3f08988dba283733d0`

Verdict: `AK-CANON X1B CORRECTIVE DESIGN REVIEW R2 = PASS`

### 2.3 Historical superseded brief

Repository: `FJ899/8`

PR: `#110`

HEAD: `8eaad5ea3c37b2cdc65ad80d16260bbf0f2a0160`

TREE: `a7978803db0e1f0f87fb84ac54f44b8c5bc33a09`

PATH: `research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF.md`

BLOB: `385bcc8620619b91986ff44211a428913b228ba2`

PR #110 remains historical and is not implementation authority.

### 2.4 Binding first implementation-brief review

Repository: `FJ899/8`

PR: `#111`

HEAD: `05bb0820990f92686c42547385729c87c614be65`

TREE: `9147295a388906a07898e9d09d62c5ac53912997`

PATH: `research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_AK_CANON_REVIEW.md`

BLOB: `35af188a5475b745294bcfa22fd3aa18b666decd`

Verdict: `AK-CANON X1B IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

The present review independently tested whether PR #112 actually resolves the prior findings rather than accepting its self-description.

## 3. Current ScriptOps baseline reconfirmed

Canonical ScriptOps `main` at review time:

```text
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Bound Phase-6 path:

```text
phase6/scriptops-v2-hardening.py
BLOB = 4f379960ed5677634dd234af6aa39626782b6133
```

Bound legacy path:

```text
legacy/scriptops-v2-single.py
BLOB = 9baa7b3a1eb746e34b79207a382eea1f5dd4ec55
```

Repository visibility at review time: `public`.

The accepted real X1B defect is still present on the frozen baseline and therefore this review concerns the same defect.

## 4. R2 improvements independently confirmed

PR #112 materially improves PR #110 in several ways.

It correctly:

- brings `legacy/scriptops-v2-single.py` into the stated implementation surface;
- requires direct legacy `approve` to deny before canonical or durable effect;
- removes caller `--why` as Human authority input from the operative Phase-6 path;
- makes the decision PR number only a locator;
- derives all semantic operation identity from the decision request;
- freezes a deterministic request path `decisions/x1b/<request_digest>.json`;
- freezes a deterministic request branch `decision/x1b/<request_digest>`;
- requires one BASE->HEAD added request file and rejects extra changed files;
- binds filename, head ref, request digest, request ID, PR HEAD and base state;
- retains complete paginated Human-review collection and fail-closed conflict semantics;
- explicitly removes the unsupported global cross-clone exactly-once claim;
- bounds replay to one canonical repository execution instance;
- requires credential-free public GitHub evidence reads with no authenticated fallback;
- derives Human actor/rationale from validated evidence;
- retains a separately Human-authorized real positive control;
- preserves `X1B OPEN != V1 AUTHORITY`.

Those corrections are substantial, but they are not sufficient for an implementation-authority PASS because the adversarial review found new concrete blockers below.

## 5. Finding X1B-R2-IBR-F001 — repository restore/self-verification path can reintroduce the unsafe legacy approval and conflicts with the proposed implementation surface

Classification: `IMPLEMENTATION BLOCKER / EFFECT-SURFACE BLOCKER`

This finding alone is sufficient for `NOT PASS`.

The current repository contains executable maintenance path:

```text
scripts/restore_v2.py
BLOB = fa2099d7d4530bce2256051690935625dab0e927
```

That script defines:

```text
CANONICAL_FILE = ROOT / "legacy/scriptops-v2-single.py"
DEFAULT_OUTPUT = CANONICAL_FILE
```

and reconstructs the historical legacy implementation from:

```text
sources/prototype/scriptops-v2-single.py.part01
...
sources/prototype/scriptops-v2-single.py.part07
```

It freezes the historical reconstructed content at:

```text
EXPECTED_SIZE = 51980
EXPECTED_SHA256 = 881dade6c6c506b9a9d41ebfbf68afb18b66db7583d35f746fb29ed7b36ac596
```

Most importantly, its normal write mode supports:

```text
python scripts/restore_v2.py --force
```

which overwrites the existing output with the historical reconstructed bytes.

Therefore the R2 plan:

```text
modify legacy/scriptops-v2-single.py
-> make direct legacy approve fail closed
```

is not durable within the current repository contract while `scripts/restore_v2.py` and the historical prototype parts remain unchanged.

Concrete reintroduction path:

```text
R2 implementation changes legacy/scriptops-v2-single.py so approve is disabled
->
python scripts/restore_v2.py --force
->
historical unsafe legacy/scriptops-v2-single.py restored
->
python legacy/scriptops-v2-single.py approve --scene <SCENE>
->
legacy canonical acceptance path is effect-capable again
```

This is not merely a test artifact or documentation issue. It is a repository-provided executable path that can recreate the exact effect path R2 intends to make non-operative.

### 5.1 Existing repository verifier makes the R2 surface internally inconsistent

Current file:

```text
scripts/verify_repository.py
BLOB = a61278086b92824d7e442b390c951e918c88517b
```

imports the restoration contract and its `check_prototype()` requires the active `legacy/scriptops-v2-single.py` bytes to equal the reconstructed historical bytes and exact historical SHA-256/size.

The current repository workflow:

```text
.github/workflows/verify-repository.yml
BLOB = 7d896d425012479c97bf1e6539f9a861a4a17aa5
```

runs:

```text
python scripts/verify_repository.py
```

on pull requests.

Consequently, an implementation candidate that changes `legacy/scriptops-v2-single.py` as R2 requires, while remaining inside the five stated R2 implementation surfaces, conflicts with the existing repository self-verification contract.

The R2 expected surface is:

```text
phase6/scriptops-v2-hardening.py
legacy/scriptops-v2-single.py
phase6/x1b_human_decision.py
tests/test_x1b_human_decision.py
.github/workflows/x1b-human-decision.yml
```

It does not freeze a disposition for:

```text
scripts/restore_v2.py
scripts/verify_repository.py
sources/prototype/scriptops-v2-single.py.part01..part07
.github/workflows/verify-repository.yml
```

A future implementer would therefore have to invent a core repository/source-of-truth decision, for example whether to:

- stop treating `legacy/scriptops-v2-single.py` as the byte-identical reconstructed historical prototype;
- relocate the historical immutable reconstruction target;
- update or disable the restoration write path;
- update the historical prototype parts;
- change repository verification semantics;
- introduce a separate corrected runtime copy while preserving historical legacy bytes.

This review does not choose among those repairs.

That choice is not ordinary coding detail because it determines whether the unsafe legacy acceptance effect can be regenerated and which artifact is normative executable substrate.

Required invariant remains:

```text
ONE OPERATIVE ACCEPTANCE EFFECT PATH
=
X1B-VALIDATED PHASE6 PATH
```

As written, PR #112 does not establish a bounded implementation plan that can satisfy that invariant while preserving the current restore/self-verification system.

`DISABLED LEGACY + RESTORABLE UNSAFE LEGACY != CLOSED EFFECT SURFACE`

## 6. Finding X1B-R2-IBR-F002 — public-read credential exclusion does not fully freeze trusted transport origin

Classification: `VALIDATION-CONTRACT PROBLEM`

The R2 mechanism's use of unauthenticated public GitHub reads is technically feasible for the current public repository. GitHub's REST contract permits unauthenticated requests for public resources, including pull-request review listing, subject to unauthenticated rate limits. The R2 fail-closed response to rate limiting is therefore implementable.

The remaining problem is not API feasibility. It is transport trust.

R2 correctly prohibits:

- an `Authorization` header;
- authenticated fallback;
- `gh`;
- `.netrc` authentication;
- GitHub CLI config authentication;
- Git credential helpers for evidence reads;
- caller-supplied headers/tokens;
- several known GitHub credential environment variables.

However, the implementation brief does not freeze the complete trusted HTTP transport boundary. In particular it does not normatively fix:

- the exact API origin/host used for trusted evidence requests;
- whether an environment-configurable API base URL is prohibited;
- whether ambient HTTP/HTTPS proxy configuration is ignored;
- whether environment-provided TLS CA/trust-store overrides are ignored;
- redirect host/origin rules for public evidence requests;
- whether HTTP client `trust_env`-style behavior is prohibited;
- which response origin/TLS properties must be established before JSON is treated as GitHub evidence.

The effect-runtime threat model already treats environment injection as security-relevant because R2 explicitly denies credential-bearing environment variables. Under the same threat model, leaving proxy/CA/API-origin behavior to the implementation means a future implementation could satisfy the literal "no Authorization header" rule while still obtaining supposedly trusted review-shaped data through caller/environment-influenced transport configuration.

The implementation can be made safe, but PR #112 does not freeze how.

Examples of transport/environment classes that require an explicit disposition include, as applicable to the selected HTTP stack:

```text
HTTPS_PROXY / ALL_PROXY / HTTP_PROXY
SSL_CERT_FILE / SSL_CERT_DIR
REQUESTS_CA_BUNDLE / CURL_CA_BUNDLE
custom GitHub API base URL environment/configuration
cross-origin redirect behavior
```

This review does not prescribe the repair or a specific HTTP library.

Required property:

```text
NO AUTH CREDENTIAL
!=
TRUSTED REMOTE ORIGIN BY ITSELF
```

and:

```text
REVIEW-SHAPED JSON
!=
TRUSTED GITHUB REVIEW EVIDENCE
```

The R2 brief must freeze the transport-origin policy sufficiently that the implementer does not invent a core trusted-origin security rule.

## 7. Finding X1B-R2-IBR-F003 — post-admission Human-review currentness/revocation cutoff is not explicitly frozen

Classification: `AUTHORITY-SEMANTICS / VALIDATION-CONTRACT PROBLEM`

R2 validates the current decision PR and complete Human review set before constructing `HumanDecisionAdmissionV1`.

It then specifies that immediately before canonical write the executor revalidates:

- admission structure/integrity;
- local HEAD;
- clean worktree;
- candidate and impact bytes;
- scene/scope/target/effect;
- canonical repository instance;
- same-instance consumption state.

The immediate pre-write list does not require a fresh public GitHub PR/review read.

R2 also does not explicitly declare an admission-time cutoff such as:

```text
currentness is evaluated when admission is issued;
a later GitHub review-state change does not revoke the same-process one-shot admission
```

Nor does it declare the opposite rule:

```text
review/PR currentness must be re-read immediately before canonical write
```

Therefore the following race has no frozen disposition in the superseding brief:

```text
valid APPROVED review observed
->
HumanDecisionAdmissionV1 issued
->
Human review dismissed / CHANGES_REQUESTED submitted / decision PR closed
->
executor reaches canonical write
```

Whether the effect proceeds or denies is a Human-authority/currentness semantic choice.

The corrective design requires the future implementation contract to define when decision evidence ceases to be active and how freshness/current activity is evaluated. PR #112 must therefore freeze the commitment/revocation boundary rather than leaving it to executor implementation choice.

This review does not choose whether admission issuance or immediate pre-effect reread should be the commitment point.

## 8. Required review-question answers

### Q1. Does legacy disablement actually leave one operative canonical-effect path?

`NO AS CURRENTLY BOUNDED.`

Direct legacy denial is correctly required, but `scripts/restore_v2.py --force` can recreate the unsafe historical legacy implementation, and repository self-verification currently requires that historical identity. See R2-F001.

### Q2. Does `approve --decision-pr <N>` eliminate caller semantic substitutions?

`YES AT THE BRIEF-CONTRACT LEVEL.`

The PR number is only a locator and request path, digest, Human actor, scene, task, candidate, impact, target and effect are not caller authority inputs.

### Q3. Does the deterministic one-file decision-PR contract close the original F003 path-selection ambiguity?

`YES, SUBSTANTIALLY.`

The request path, branch, filename digest, request digest, request ID, head-ref digest, base state and complete one-file diff are normatively linked. No caller-provided request path is trusted.

### Q4. Is proposal preparation sufficiently separated from effect invocation and Human decision authority?

`YES AT THE CONTRACT LEVEL.`

Proposal outputs remain untrusted and are fully revalidated. Proposal creation is explicitly not Human decision authority.

### Q5. Is public unauthenticated GitHub review acquisition technically feasible for the bounded public repository?

`YES.`

Current repository visibility is public and GitHub's public REST review endpoint supports unauthenticated access to public resources. Rate-limit/incomplete-read failure is correctly fail-closed.

### Q6. Does manual Human UI governance plus lack of effect-process review-write capability satisfy trusted origin?

`PARTLY, BUT NOT YET SUFFICIENTLY FROZEN.`

The model correctly does not claim that metadata proves private Human UI origin. For this design, separation from the evaluated effect capability can satisfy the origin property, but only if the evidence transport itself is trusted and the effect process cannot manufacture/redirect the evidence stream. R2-F002 leaves part of that transport-origin contract to implementation choice.

### Q7. Do the credential-variable checks and sanitized local-Git boundary completely close F005?

`NO.`

They materially improve F005 and remove authenticated GitHub evidence fallback. They do not freeze the full public HTTP transport trust/environment boundary. See R2-F002.

### Q8. Are complete review pagination/state/conflict semantics fail-closed?

`YES AT THE CONTRACT LEVEL.`

Incomplete pagination, duplicate review IDs, malformed authoritative-Human states and conflicts deny.

### Q9. Can a self-consistent malicious proposal become operative without Human approval merely by controlling request content/path?

`NO UNDER THE NEW REQUEST CONTRACT.`

The proposal may be AI-created, but it remains a proposal. Exact current Human review is still required for the exact digest/head.

### Q10. Is bounded replay compatible with the normative X1B design and does it still reject old consent for changed operations?

`YES AT THE STATED POLICY LEVEL.`

The corrective design required replay semantics to be explicitly defined; it did not require global distributed exactly-once. R2 explicitly scopes same-request consumption to one canonical repository execution instance and preserves exact binding such that changed operations require a new Human decision.

### Q11. Is the absence of a global cross-clone exactly-once claim honest rather than a hidden correctness claim?

`YES.`

R2 expressly disclaims global cross-instance atomic consumption and requires a new design if that property is later needed.

### Q12. Does admission/executor revalidation block post-Human content/scope/candidate/impact/target/effect substitution?

`YES FOR LOCAL OPERATION SUBSTITUTION, BUT CURRENTNESS CUTOFF IS INCOMPLETE.`

Local semantic substitution is strongly bound. External Human-review/PR state change after admission but before effect lacks a frozen disposition. See R2-F003.

### Q13. Is durable Human attribution evidence-derived?

`YES ON THE INTENDED CORRECTED PHASE-6 PATH.`

It is not system-wide durable while the repository can restore the historical unsafe legacy approval path. See R2-F001.

### Q14. Are the complete original X1B and R2 regressions executable and sufficient?

`NOT YET.`

The matrix correctly includes direct legacy invocation but does not require the concrete repository-native sequence:

```text
apply corrected legacy disablement
-> scripts/restore_v2.py --force
-> attempt legacy approve
```

nor does it resolve the existing `scripts/verify_repository.py` identity contract that would reject a changed legacy implementation.

### Q15. Does the brief leave no core authority/security semantic choice to the implementer?

`NO.`

At minimum:

- historical-prototype restoration/self-verification disposition (R2-F001);
- trusted public-HTTP transport origin policy (R2-F002);
- post-admission review-currentness/revocation cutoff (R2-F003)

remain security/authority decisions rather than ordinary coding details.

## 9. Independent tree-surface observation

The exact canonical ScriptOps tree was read recursively during review.

Relevant executable/runtime paths include at minimum:

```text
legacy/scriptops-v2-single.py
phase6/scriptops-v2-hardening.py
phase6/bounded-proposal-view.py
scripts/restore_v2.py
scripts/verify_repository.py
```

The tree also retains historical prototype source parts under:

```text
sources/prototype/scriptops-v2-single.py.part01..part07
```

The tree response was complete (`truncated=false`).

This is why R2-F001 is not speculative: the restore/reconstruction mechanism is part of the exact frozen repository baseline.

## 10. Public API feasibility observation

GitHub's documented REST model supports unauthenticated requests when fetching public data, with a lower unauthenticated rate limit. The pull-request Reviews REST endpoint specifically states that public resources may be requested without authentication.

Therefore:

```text
PUBLIC UNAUTHENTICATED REVIEW READ = TECHNICALLY AVAILABLE
```

The R2-F002 problem is instead:

```text
UNAUTHENTICATED != FULLY SPECIFIED TRUSTED TRANSPORT
```

The R2 fail-closed behavior on rate-limit/incomplete reads remains appropriate.

## 11. Verdict

`AK-CANON X1B SUPERSEDING IMPLEMENTATION-BRIEF R2 REVIEW = NOT PASS`

Minimum decisive basis:

```text
R2-F001:
current repository restore/self-verification semantics can restore the unsafe historical legacy approval path and conflict with the proposed legacy modification
```

Additional material basis:

```text
R2-F002:
trusted public-read transport origin is not fully frozen
+
R2-F003:
post-admission Human-review currentness/revocation cutoff is not frozen
```

PR #112 is therefore not precise enough to support bounded implementation authority without additional Human-governed brief correction.

No repair is authorized or supplied by this review.

## 12. Required STOP boundary

Do not implement from PR #112 under this review result.

Do not modify PR #112 under this authorization.

Do not modify PR #111, #110, #109, or ScriptOps PR #34.

Do not modify ScriptOps.

Do not create a Human decision PR or Human APPROVE.

Do not execute corrective verification or canonical scene effect.

Do not merge, close X1B, begin Agency Kernel v1, release, deploy, or tag.

A separate Human authorization is required for any superseding brief correction.

`REVIEW FINDING != REPAIR AUTHORITY`

`R2 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY`

`AI PROPOSES != HUMAN DECIDES`

`STOP`
