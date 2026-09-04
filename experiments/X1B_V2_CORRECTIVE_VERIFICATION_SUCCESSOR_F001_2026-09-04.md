# X1B V2 corrective-verification successor for F001 — 2026-09-04

## Status

```text
HUMAN AUTHORITY = PR #175 / response "accept"
PURPOSE = CLOSE X1B-V2-CV-F001 ONLY
RUNTIME IMPLEMENTATION CHANGE = NO
ONE FRESH HUMAN POSITIVE CONTROL = AUTHORIZED
REMOTE SCRIPTOPS MAIN PUSH/MERGE = FORBIDDEN
X1B = OPEN
V1 AUTHORITY = NO
```

This is the bounded successor verification authorized after the Human accepted `X1B-V2-CV-F001` from PR #174.

It does not reopen the reviewed X1B V2 implementation and does not create deployment authority.

## 1. Frozen antecedents

Finding:

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
Human response = accept
```

Reviewed implementation:

```text
FJ899/scriptops PR #35
I = 7c40a92165714023743e91c63b5b11b102fadd92
TREE(I) = 31e1f15a2e667811b9617bbb10bf6af2242961b0
```

Current production remote baseline remains:

```text
FJ899/scriptops main = 2f22843ac570498b506101addeba5453ab777f08
```

No successor step may move that remote ref.

## 2. Narrow finding being repaired

The first attempt proved the real local V2 Human-review/admission/CAS/postverify path but ran in a Codespace.

The accepted blocker is exactly:

```text
X1B-V2-CV-F001 — EXECUTION SUBSTRATE WAS A CODESPACE, NOT THE FROZEN READ-ONLY GITHUB ACTIONS EFFECT JOB = BLOCKER
```

The successor therefore changes the verification substrate and preservation path only.

It does **not** change:

```text
Human authority semantics
request schema
review marker
trusted user.id
network child
admission algorithm
AnchoredGitV2
lock
prospective commit
CAS
postverify
legacy bypass closure
```

## 3. Reuse of B0 is selected and bounded

The successor explicitly reuses the immutable remote verification fixture commit:

```text
B0 = e325d3e6a347d684ec0b751bdb83098de6bdf87e
TREE(B0) = e948b07d4d9fb3c629cdb43eda3d1579640c3fce
parent(B0) = I
```

The remote branch currently naming it is:

```text
verification/x1b-v2-positive-b0-20260903
```

Before creating any fresh Human request, re-read and require that branch still equals exact B0 and that `I..B0` is exactly one commit containing only:

```text
scenes/SCN-999.fountain
staging/scenes/SCN-999-v2-candidate.fountain
tasks/TASK-X1B-POSITIVE-001/impact-report.json
```

Why reuse is valid here:

- B0 is a remote immutable fixture commit, not the previous Codespace effect commit;
- previous local `C1` was never pushed to any ScriptOps remote ref;
- B0 contains no committed X1B decision-log record for the new request;
- the successor uses a fresh random nonce and fresh digest `D2`;
- the prior digest `D1` and PR #173 Human review are forbidden from reuse.

Previous consumed values remain historical only:

```text
D1 = 1f8d7fa4d4df2cac16853b273198f1146ce5cb6821e2d699badb0f7d3bdf7856
C1 = 05bef859c907a4f3ec8904f7cdc7db536f85f1a4
```

## 4. Verification-only Actions harness

Create one verification-only branch in `FJ899/scriptops` from exact B0:

```text
verification/x1b-v2-actions-successor-20260904
```

Create a draft PR targeting the existing implementation branch:

```text
base = impl/x1b-human-decision-v2-20260903
```

The harness PR is never to be merged.

Initial harness delta from B0 is limited to verification-control files only:

```text
.github/workflows/x1b-v2-successor-positive.yml
verification/x1b-v2-successor-control.json
```

No production runtime source file may change.

The initial control is inert:

```json
{
  "schema_version": "x1b-v2-successor-control/v1",
  "armed": false,
  "decision_pr": 0,
  "expected_request_sha256": "",
  "expected_evidence_head": "",
  "expected_review_numeric_id": 0
}
```

The workflow trigger is only:

```text
pull_request activity type = synchronize
```

Opening the harness PR must not execute the real effect.

The actual effect run is triggered only by one post-Human-review update of the control file from `armed=false` to exact fresh values.

## 5. Frozen Actions job authority profile

The successor effect job must declare:

```yaml
permissions:
  contents: read
```

Checkout must use:

```text
actions/checkout
persist-credentials: false
fetch-depth: 0
```

Action identities are pinned for this successor to the commits currently resolved from the official major tags:

```text
actions/checkout v4 = 11d5960a326750d5838078e36cf38b85af677262
actions/setup-python v5 = a26af69be951a213d495a4c3e4e4022e16d87065
actions/upload-artifact v4 = ea165f8d65b6e75b540449e92b4886f43607fa02
```

The job must additionally prove before effect:

```text
checkout .git/config contains no GitHub http extraheader credential
no nonempty GITHUB_TOKEN / GH_TOKEN / enterprise-token variables in effect parent
no frozen HTTP(S)/ALL proxy variables in effect parent
strace exists before effect
```

The ScriptOps effect process receives no GitHub write credential.

## 6. Dedicated isolated run repository

The workflow checkout is the verification harness carrier only.

The real ScriptOps effect must execute in a separate local Git repository created inside the runner from exact B0, not on the harness branch head.

Required construction:

```text
fresh local git init in runner temp directory
fetch exact B0 from the credential-free local harness checkout
checkout/create local refs/heads/main exactly at B0
HEAD = refs/heads/main
worktree/index clean
refs/replace empty
```

Before tests or authority reading require:

```text
HEAD = B0
parent(B0) = I
I..B0 exact three fixture paths
critical production source bytes at B0 equal I
```

The effect job never pushes this local `main` anywhere.

## 7. Fresh negative verification before effect

Before any fresh Human-positive effect, the Actions run must execute the complete deterministic X1B verification surface on exact B0/runtime I.

At minimum capture successful output for:

```text
python -m unittest -v tests.test_x1b_human_decision tests.test_phase6_scriptops_smoke
python scripts/verify_repository.py
python scripts/restore_v2.py --check-only
```

The verifier must retain all mandatory frozen matrix mappings, including:

```text
A1..A10
RB1..RB5
ID1..ID5
CUR1..CUR13
CAS1..CAS9
GIT1..GIT6
PU1..PU6
TLS1..TLS15
```

Any unexpected acceptance or test failure stops before effect.

## 8. Fresh Human request

Generate a new random 32-byte lowercase-hex request nonce with the exact reviewed implementation on B0.

The new request must retain the same exact SCN-999 candidate/impact/accepted-scene binding and B0, but must produce a fresh digest:

```text
D2 != D1
```

Create one fresh `FJ899/8` PR containing exactly:

```text
decisions/x1b/requests/<D2>/request.json
decisions/x1b/requests/<D2>/accepted-scene.fountain
```

It must be open, non-draft and unmerged.

## 9. Required fresh Human act

The trusted Human must inspect both files at exact fresh evidence commit `H2` and submit one GitHub APPROVED review from:

```text
user.id = 226907434
```

Review body exactly:

```text
X1B-HUMAN-DECISION-V2
request_sha256=<D2>
decision=APPROVE
```

No old review, chat acceptance, comment, merge, label, reaction or `proposal_rationale` is sufficient.

## 10. One-shot arming after Human review

Only after the fresh Human review exists and is independently read back may process update the harness control file once to:

```json
{
  "schema_version": "x1b-v2-successor-control/v1",
  "armed": true,
  "decision_pr": <fresh PR number>,
  "expected_request_sha256": "<D2>",
  "expected_evidence_head": "<H2>",
  "expected_review_numeric_id": <fresh review id>
}
```

That single commit is the intended `pull_request/synchronize` trigger.

The job must require:

```text
github.run_attempt == 1
armed == true
control values syntactically exact
harness head is the expected verification-only branch
base branch is the expected implementation branch
```

A rerun attempt (`github.run_attempt > 1`) must stop before effect.

## 11. Fresh authority/admission preflight in Actions

After fresh negative verification and before effect, use exact reviewed `run_network_child()` and reconstruct admission from the fresh PR.

Require and preserve:

```text
current trusted-Human authority state = APPROVED
user.id = 226907434
review id = control expected review id
review.commit_id = H2
request_sha256 = D2
immutable H2 request bytes exact
immutable H2 scene bytes exact
TLS hostname verification true
CERT_REQUIRED
TLS >= 1.2
isolated child environment free of forbidden authority inputs
admission_id/admission_digest freshly reconstructed
```

The preread performs no canonical effect.

The actual effect invocation must perform its own fresh network-child read again.

## 12. Exact effect invocation

Only after all previous gates pass, invoke once:

```text
python phase6/scriptops-v2-hardening.py approve --scene SCN-999 --decision-pr <fresh PR>
```

Observe it without semantic modification using:

```text
strace -f -s 4096 -e trace=process,flock,fcntl
```

Capture at minimum:

```text
LOCK_EX|LOCK_NB acquisition
fresh --_x1b-github-reader-child
commit-tree with parent B0
update-ref --no-deref refs/heads/main C2 B0
LOCK_UN
```

No monkeypatching or runtime source editing is allowed.

## 13. Post-CAS truth

Success requires all of:

```text
EFFECT_RC = 0
HumanDecision = TRUE
refs/heads/main = C2
C2 != B0
parent(C2) = B0
changed tracked paths exactly:
  .scriptops/decision-log.ndjson
  scenes/SCN-999.fountain
modes both 100644
scene bytes = exact Human-reviewed accepted scene
log bytes = base log + exactly one V2 decision row
real index tree = C2 tree
worktree/index clean
machine author/committer exact
durable record user.id/review/H2/D2/admission bindings exact
```

Any post-CAS uncertainty is `RECOVERY_REQUIRED` and not PASS.

## 14. Durable preservation before runner exit

On successful effect, create a Git bundle containing at least:

```text
refs/heads/main = C2
history through B0 and I
```

Preserve textual evidence including:

```text
runner OS / Python / Git versions
anchor checks
negative-matrix output
preflight raw child result
canonical admission bytes
Human review/body/request/scene raw bytes or bounded canonical encodings
CLI stdout/stderr
strace
commit/tree/path/mode evidence
durable decision-log row
post-effect status
SHA256SUMS for the evidence directory
bundle verification output
```

Upload the entire evidence directory as one GitHub Actions artifact using the pinned `actions/upload-artifact` action with:

```text
retention-days = 90
if-no-files-found = error
```

A successful effect without successful bundle creation and artifact upload is not successor PASS.

## 15. No remote product effect

The job must not execute any `git push`.

After the run, independently re-read and require:

```text
FJ899/scriptops main = 2f22843ac570498b506101addeba5453ab777f08
```

The harness PR, Human evidence PR and local C2 remain non-deployment evidence.

## 16. Successor evidence freeze and next gate

If the Actions run succeeds, freeze a one-file corrective-verification evidence artifact in `FJ899/8` containing the exact run/job/artifact IDs, hashes and all critical identities.

Then perform one independent corrective-closure review against the accepted X1B scope firewall.

Even a successful successor verification does not itself close X1B.

Required final sequence remains:

```text
SUCCESSOR CORRECTIVE VERIFICATION PASS
-> INDEPENDENT CORRECTIVE-CLOSURE REVIEW
-> SEPARATE HUMAN CORRECTIVE-CLOSURE ACCEPTANCE
-> only then X1B closure may be established
```

## 17. Failure / first-counterexample rule

Any new concrete defect or mismatch terminates this successor authority at the first credible blocker:

```text
FIRST CREDIBLE COUNTEREXAMPLE = STOP
NO SILENT REPAIR
NO SECOND EFFECT ATTEMPT
```

A new repair requires a new Human disposition.

## 18. Explicit non-authority

This successor does not authorize:

```text
runtime implementation changes
merge of PR #35
merge of harness PR
merge of Human evidence PR
push of C2 to remote scriptops/main
release/deployment/tag
reusing D1 / PR #173 review
second effect attempt
X1B closure before independent closure review + Human closure acceptance
V1 authority
```

## 19. Governance

```text
AI PROPOSES != HUMAN DECIDES
REVIEW FINDING != REPAIR AUTHORITY
HUMAN DECISION EVIDENCE != MACHINE ADMISSION != EXECUTOR CAPABILITY
```

## 20. Current gate

The Human has already accepted PR #174 F001 and authorized this one bounded successor verification through PR #175.

Therefore preparation may proceed autonomously through harness creation, fresh request creation and all inert checks.

Execution stops for the required fresh Human GitHub review of the new two-file decision PR.

After that exact Human review is supplied, the already-authorized one-shot Actions effect may proceed without another generic chat `accept`, provided no identity or scope gate has drifted.
