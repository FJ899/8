# X1B V2 corrective-verification successor evidence — PASS — 2026-09-04

## Status

```text
X1B V2 SUCCESSOR CORRECTIVE VERIFICATION = PASS
X1B-V2-CV-F001 = VERIFIED CLOSED
X1B = OPEN
V1 AUTHORITY = NO
NEXT REQUIRED STAGE = INDEPENDENT CORRECTIVE-CLOSURE REVIEW
```

This artifact freezes the evidence from the one bounded successor corrective-verification attempt authorized by the Human acceptance of `X1B-V2-CV-F001`.

It is verification evidence only. It does not merge or deploy ScriptOps, does not move remote `FJ899/scriptops main`, does not grant V1 authority, and does not itself close X1B.

## 1. Authority and frozen predecessor chain

Accepted finding:

```text
FJ899/8 PR #174
HEAD = 1a85010cf693aafab9fb9dbce3be345d7ba73a5e
TREE = 2237777c46e2c74dd77342e59f5179dc4d2e7804
BLOB = eb405b7277df248fd545e95d2293e427b2b99082
finding = X1B-V2-CV-F001
```

Human acceptance:

```text
FJ899/8 PR #175
HEAD = 2ff57a2e176b4a3d1e365b2eaf7cd3db5214980b
Human response = accept
```

The accepted Human authority allowed exactly one bounded successor corrective-verification attempt, with fresh Human-decision evidence, no reviewed runtime implementation change, a read-only GitHub Actions effect substrate, retained artifact preservation, and no remote product effect.

Frozen successor packet:

```text
FJ899/8 PR #176
HEAD = aa7cc251038a1441f707d9101ac741f97b49515b
TREE = 1a5e47ad99d17b3cc2cb817a881c4a53951d53a5
PATH = experiments/X1B_V2_CORRECTIVE_VERIFICATION_SUCCESSOR_F001_2026-09-04.md
BLOB = 8bac80be03f541acf31890ba0d65007248e2137a
```

Reviewed ScriptOps implementation remained unchanged:

```text
FJ899/scriptops PR #35
I = 7c40a92165714023743e91c63b5b11b102fadd92
TREE(I) = 31e1f15a2e667811b9617bbb10bf6af2242961b0
```

Reused immutable remote fixture:

```text
B0 = e325d3e6a347d684ec0b751bdb83098de6bdf87e
TREE(B0) = e948b07d4d9fb3c629cdb43eda3d1579640c3fce
parent(B0) = I
remote fixture branch = verification/x1b-v2-positive-b0-20260903
```

## 2. Verification-only Actions harness

Harness PR:

```text
FJ899/scriptops PR #36
state = open
mode = draft
merged = false
base = impl/x1b-human-decision-v2-20260903
head branch = verification/x1b-v2-actions-successor-20260904
armed HEAD = f64350fbdb47288b6fb1b8db9939657b90b1f6c3
merge ref observed for run = 4048db60c01deac25fe0e1651af2caa376da60f6
```

Verification workflow:

```text
PATH = .github/workflows/x1b-v2-successor-positive.yml
BLOB = 29f610ce9d7b0509b86591235c449565fe9d2940
permissions.contents = read
checkout persist-credentials = false
checkout fetch-depth = 0
checkout action = 11d5960a326750d5838078e36cf38b85af677262
setup-python action = a26af69be951a213d495a4c3e4e4022e16d87065
upload-artifact action = ea165f8d65b6e75b540449e92b4886f43607fa02
artifact retention-days = 90
```

The one-shot control was armed only after the fresh Human review was read back:

```text
PATH = verification/x1b-v2-successor-control.json
armed blob = b99fd0e52d1f36f44a08f0bf0b579e8d4a817af7
armed = true
decision_pr = 177
expected_request_sha256 = ceb0f11a527b99629d172e353e2f41f49faf874cb9a1795f166fe4e93b4486d2
expected_evidence_head = bbd013160f9ef5e464855aaa317f57aa1591145a
expected_review_numeric_id = 5117204074
```

The arming commit was exactly:

```text
f64350fbdb47288b6fb1b8db9939657b90b1f6c3
```

No runtime source file was modified by the arming step.

## 3. Fresh Human decision evidence

Fresh request digest:

```text
D2 = ceb0f11a527b99629d172e353e2f41f49faf874cb9a1795f166fe4e93b4486d2
D2 != prior consumed D1
```

Fresh evidence PR:

```text
FJ899/8 PR #177
state = open
mode = non-draft
merged = false
HEAD / H2 = bbd013160f9ef5e464855aaa317f57aa1591145a
changed files = exactly 2
```

Files:

```text
decisions/x1b/requests/D2/request.json
decisions/x1b/requests/D2/accepted-scene.fountain
```

The canonical SHA-256 recomputed from the exact `request.json` content equals `D2`.

Fresh qualifying Human review:

```text
review numeric id = 5117204074
state = APPROVED
user.login = litrgratis-pixel
user.id = 226907434
user.node_id = U_kgDODYZVKg
submitted_at = 2026-09-04T19:46:12Z
review.commit_id = H2
```

Exact review body:

```text
X1B-HUMAN-DECISION-V2
request_sha256=ceb0f11a527b99629d172e353e2f41f49faf874cb9a1795f166fe4e93b4486d2
decision=APPROVE
```

Human review body SHA-256 captured in the retained artifact:

```text
58134e49b03facbbf1b6ddcfe8fb3fb0cd437c162ec1745356d67d3fbcc527d8
```

## 4. Exact GitHub Actions run

Authorized effect run:

```text
repository = FJ899/scriptops
workflow = x1b-v2-successor-positive
workflow run id = 33913039129
run number = 1
run attempt = 1
job id = 101153753596
job name = successor-positive
result = success
```

Every substantive step completed successfully, including:

```text
checkout verification harness without persisted credentials = success
Python 3.12 setup = success
one-shot control / runner authority profile = success
construct isolated exact-B0 repository = success
fresh complete deterministic X1B matrix = success
fresh post-Human authority/admission preflight = success
one observed real positive-control effect = success
post-CAS truth and strace verification = success
bundle preservation / remote-main proof = success
artifact upload = success
```

Runner identity evidence states:

```text
github_repository = FJ899/scriptops
github_run_id = 33913039129
github_run_attempt = 1
github_head_ref = verification/x1b-v2-actions-successor-20260904
github_base_ref = impl/x1b-human-decision-v2-20260903
permissions_contents = read
checkout_persist_credentials = false
```

The harness also required and passed before effect:

```text
no GitHub HTTP extraheader credential retained by checkout
no non-empty frozen GitHub token variables in effect parent
no non-empty frozen proxy variables in effect parent
strace present
```

## 5. Fresh deterministic matrix

The run executed:

```text
python -m unittest -v tests.test_x1b_human_decision tests.test_phase6_scriptops_smoke
python scripts/verify_repository.py
python scripts/restore_v2.py --check-only
```

Observed result:

```text
unittest: 42 tests, all OK
verify_repository: PASS
mandatory frozen matrix mappings retained: 82 cases
restore_v2 --check-only: PASS
```

This included the frozen A1..A10, RB1..RB5, ID, currentness, CAS, Git-environment, positive-chain and TLS regression surface required by the accepted implementation chain.

## 6. Fresh authority and admission preflight

Immediately before effect, the Actions runner independently reconstructed fresh authority/admission and captured:

```text
PREFLIGHT = PASS
B0 = e325d3e6a347d684ec0b751bdb83098de6bdf87e
REVIEW_ID = 5117204074
HUMAN_USER_ID = 226907434
REVIEW_COMMIT_H = bbd013160f9ef5e464855aaa317f57aa1591145a
REQUEST_SHA256 = ceb0f11a527b99629d172e353e2f41f49faf874cb9a1795f166fe4e93b4486d2
ADMISSION_ID = x1b:v2:a9b433a76f26a6f6aa6558902c26f2a7053d61db8f80ebd9aa53876c683277e7
ADMISSION_DIGEST = f0908a2b855bdc1b4a33a2cc80f2675b3099340238081170a10ab2f1c075f2e7
```

Retained raw/canonical evidence digests include:

```text
preflight-child-result.json SHA-256 = 9008c243f5c488a3f584ba4b99d8ef90722b227c53f0fede232ec5e3c6dd8ebf
preflight-admission-canonical.json SHA-256 = ea9bf3e6adfc30b06b4339ffb9d2b54d9650de44f94c0e2b2b2f33c0135b925f
review-response.raw SHA-256 = 0f77e1a603e4783b11e8fc7da4872ab31cb0f7358743e6c16ba31aa42e11bb95
request.json.raw SHA-256 = 4ea06db74545377a14ea80cd791abefb2fb365c7aa721c02113edd734b92b3a0
accepted-scene.fountain.raw SHA-256 = 829d88c932b20de5c9a1e469c4b657a38ea2fb1eadd842392aa6edd4f6cee3ab
human-review-body.raw SHA-256 = 58134e49b03facbbf1b6ddcfe8fb3fb0cd437c162ec1745356d67d3fbcc527d8
```

The actual effect invocation then performed its own fresh authority-child read as required by the reviewed runtime.

## 7. Real effect and post-CAS truth

Effect output:

```text
HumanDecision=TRUE
request = D2
canonical commit / C2 = e3bdfc70d1cdc2ba1388d76fc8f879d28ea5aa32
admission = x1b:v2:a9b433a76f26a6f6aa6558902c26f2a7053d61db8f80ebd9aa53876c683277e7
EFFECT_RC = 0
```

Postverify:

```text
POSTVERIFY = PASS
C2 = e3bdfc70d1cdc2ba1388d76fc8f879d28ea5aa32
TREE(C2) = 2ac0892a3fc488ebb5835cb8bab87414e9d059ed
parent(C2) = B0
C2 != B0
changed paths exactly:
  .scriptops/decision-log.ndjson
  scenes/SCN-999.fountain
scene mode = 100644
decision-log mode = 100644
scene SHA-256 = 829d88c932b20de5c9a1e469c4b657a38ea2fb1eadd842392aa6edd4f6cee3ab
real index tree = C2 tree
worktree/index clean = true
human_decision = true
review id = 5117204074
review commit = H2
request digest = D2
admission id/digest = exact fresh preflight values
```

Machine commit identity:

```text
author = ScriptOps X1B Executor <scriptops-x1b@example.invalid>
committer = ScriptOps X1B Executor <scriptops-x1b@example.invalid>
subject = scriptops x1b v2: accept SCN-999 via ceb0f11a527b
```

The durable `scriptops-x1b-decision/v2` row contains and binds:

```text
status = committed
kind = scene_accepted
human_decision = true
human_github_user_id = 226907434
human_actor = github-user-id:226907434
human_review_numeric_id = 5117204074
human_review_commit_id = H2
request_sha256 = D2
scriptops_base_head = B0
accepted_scene_sha256 = 829d88c932b20de5c9a1e469c4b657a38ea2fb1eadd842392aa6edd4f6cee3ab
admission_id = x1b:v2:a9b433a76f26a6f6aa6558902c26f2a7053d61db8f80ebd9aa53876c683277e7
admission_digest = f0908a2b855bdc1b4a33a2cc80f2675b3099340238081170a10ab2f1c075f2e7
```

## 8. Strace execution observation

Retained trace evidence proves:

```text
flock(..., LOCK_EX|LOCK_NB) = 0
fresh isolated Python --_x1b-github-reader-child
commit-tree TREE(C2) -p B0
update-ref --no-deref refs/heads/main C2 B0
flock(..., LOCK_UN) = 0
```

The exact observed CAS was:

```text
git update-ref --no-deref refs/heads/main \
  e3bdfc70d1cdc2ba1388d76fc8f879d28ea5aa32 \
  e325d3e6a347d684ec0b751bdb83098de6bdf87e
```

## 9. Durable GitHub Actions artifact

GitHub Actions artifact:

```text
artifact id = 9952081992
name = x1b-v2-successor-positive-33913039129
size = 239684 bytes
expired = false
created_at = 2026-09-04T19:48:38Z
expires_at = 2026-12-03T19:48:25Z
GitHub artifact digest = sha256:0c8f2cce9f1ffd47dae845ee40fcb0106e049dd68bcdd028ec277072d4d5b062
artifact head branch = verification/x1b-v2-actions-successor-20260904
artifact head SHA = f64350fbdb47288b6fb1b8db9939657b90b1f6c3
```

The artifact ZIP was independently downloaded after the successful run. Its locally recomputed SHA-256 was exactly:

```text
0c8f2cce9f1ffd47dae845ee40fcb0106e049dd68bcdd028ec277072d4d5b062
```

which equals the GitHub artifact digest.

The archive contains 43 retained evidence files including the Git bundle, raw Human/request evidence, admission, test logs, postverify, complete strace, runner identity, and `SHA256SUMS`.

Independent `sha256sum -c SHA256SUMS` over the extracted archive returned OK for every listed evidence file.

## 10. Independent Git bundle verification

Retained bundle:

```text
x1b-v2-successor.bundle
```

The runner's own bundle verification reported complete history and:

```text
refs/heads/main = e3bdfc70d1cdc2ba1388d76fc8f879d28ea5aa32
```

The downloaded bundle was also independently verified in a fresh local Git repository after artifact download.

Independent result:

```text
bundle = OK
bundle refs/heads/main = C2
parent(C2) = B0
changed paths exactly the two approved logical paths
scene SHA-256 = 829d88c932b20de5c9a1e469c4b657a38ea2fb1eadd842392aa6edd4f6cee3ab
decision-log non-empty row count = 1
```

## 11. No remote product effect

The Actions run captured remote ScriptOps main after the local effect as:

```text
2f22843ac570498b506101addeba5453ab777f08 refs/heads/main
```

A separate post-run GitHub API read independently confirmed:

```text
FJ899/scriptops refs/heads/main = 2f22843ac570498b506101addeba5453ab777f08
```

Therefore `C2` is retained verification evidence only. It was not pushed to production `scriptops/main`.

PR #36 remains open/draft/unmerged and PR #177 remains open/unmerged.

## 12. Disposition of X1B-V2-CV-F001

The accepted blocker required replacing the prior Codespace execution with the exact frozen read-only Actions substrate plus durable Actions artifact preservation.

The successor established all of the missing properties:

```text
actual GitHub Actions effect job
permissions: contents: read
checkout persist-credentials: false
no checkout HTTP extraheader credential
no frozen token/proxy variables in effect parent
fresh Human request and fresh Human APPROVED review
fresh complete deterministic matrix before effect
fresh authority/admission preflight
one real observed effect
exact direct-ref CAS and post-effect truth
retained Git bundle
retained textual/raw evidence
GitHub Actions artifact upload with 90-day retention
independent artifact digest verification
independent bundle verification
remote ScriptOps main unchanged
```

Therefore:

```text
X1B-V2-CV-F001 = VERIFIED CLOSED
SUCCESSOR CORRECTIVE VERIFICATION = PASS
```

No additional effect attempt is authorized or required by this verification result.

## 13. Governance and next legal stage

This PASS is not X1B closure by itself.

Required chain now advances exactly to:

```text
INDEPENDENT CORRECTIVE-CLOSURE REVIEW
```

That review must evaluate the complete accepted X1B chain under the convergence/scope firewall and must not reopen mechanism-external hardware/platform claims merely because they were explored in prior R4 iterations.

Only if that independent closure review passes may the process ask for a separate Human corrective-closure acceptance.

Until that separate Human act:

```text
X1B = OPEN
V1 AUTHORITY = NO
REMOTE PRODUCT DEPLOYMENT AUTHORITY = NO
```

Governance invariants remain:

```text
AI PROPOSES != HUMAN DECIDES
REVIEW FINDING != REPAIR AUTHORITY
HUMAN DECISION EVIDENCE != MACHINE ADMISSION != EXECUTOR CAPABILITY
```
