# X1B V2 corrective-verification execution substrate finding — 2026-09-04

## Status

```text
X1B V2 CORRECTIVE VERIFICATION EXECUTION REVIEW = NOT PASS
FIRST CREDIBLE COUNTEREXAMPLE = STOP
X1B = OPEN
V1 AUTHORITY = NO
```

This artifact records one bounded finding discovered after the authorized real positive-control effect while checking the execution against the exact frozen corrective-verification packet.

It is a review/finding artifact only. It authorizes no repair, retry, merge, deployment, release, tag, or X1B closure.

## Frozen packet and reviewed implementation

Corrective-verification packet:

```text
FJ899/8 PR #171
HEAD = 70a0374b55f002667d057ab6190faf7dcb65aeb9
PATH = experiments/X1B_V2_CORRECTIVE_VERIFICATION_PACKET_FINAL_2026-09-03.md
BLOB = 0f6ac0e6956225cba80e180cb9ff3febd3df8683
```

Reviewed ScriptOps implementation:

```text
FJ899/scriptops PR #35
I = 7c40a92165714023743e91c63b5b11b102fadd92
```

The evidence-repository recovery state had been separately Human-re-anchored before the fresh decision request. No claim here treats the earlier evidence-main commit identity as unchanged.

## Positive-control identities actually exercised

```text
scene_id = SCN-999
B0 = e325d3e6a347d684ec0b751bdb83098de6bdf87e
D = 1f8d7fa4d4df2cac16853b273198f1146ce5cb6821e2d699badb0f7d3bdf7856
fresh evidence PR = FJ899/8 PR #173
H = f704c498aaa14199260ce3b11215feecbe9f8798
Human review numeric id = 5109428377
Human GitHub user.id = 226907434
Human review state = APPROVED
C = 05bef859c907a4f3ec8904f7cdc7db536f85f1a4
```

Pre-effect reconstructed admission:

```text
admission_id = x1b:v2:10695474806b1fe35c5933d312a779e9310b6dabf15b42eba39420ede9bb450a
admission_digest = 67bc3ddd40372786af5311e192c47902c5dbcfb80caff7877529cdcd70b6bc55d
```

## What passed

The local real positive-control runtime itself produced:

```text
Accepted: /workspaces/scriptops/scenes/SCN-999.fountain
HumanDecision=TRUE
request=D
canonical commit=C
admission=<exact preread admission_id>
exit status = 0
```

Independent post-effect reads in the same isolated verification clone established:

```text
refs/heads/main = C
parent(C) = B0
C != B0
changed tracked paths B0..C exactly:
  .scriptops/decision-log.ndjson
  scenes/SCN-999.fountain
scene mode = 100644
decision-log mode = 100644
real index = C
worktree/index clean
scene raw SHA-256 = 829d88c932b20de5c9a1e469c4b657a38ea2fb1eadd842392aa6edd4f6cee3ab
machine author = ScriptOps X1B Executor <scriptops-x1b@example.invalid>
machine committer = ScriptOps X1B Executor <scriptops-x1b@example.invalid>
```

The durable `X1BDecisionRecordV2` was parsed and checked against the preread admission and established:

```text
schema = scriptops-x1b-decision/v2
status = committed
human_decision = true
human_github_user_id = 226907434
request_sha256 = D
decision_pr = 173
human_review_numeric_id = 5109428377
human_review_commit_id = H
scriptops_base_head = B0
accepted_scene_sha256 = 829d88c932b20de5c9a1e469c4b657a38ea2fb1eadd842392aa6edd4f6cee3ab
admission_id = exact preread admission_id
admission_digest = exact preread admission_digest
review_response_digest = exact preread value
human_review_set_digest = exact preread value
material_effect_digest = exact preread value
```

The syscall/process trace showed the required runtime operations:

```text
flock(..., LOCK_EX|LOCK_NB) = 0
fresh Python child with --_x1b-github-reader-child
git commit-tree ... -p B0 ...
git update-ref --no-deref refs/heads/main C B0
flock(..., LOCK_UN) = 0
```

Remote `FJ899/scriptops main` was separately re-read after the effect and remained:

```text
2f22843ac570498b506101addeba5453ab777f08
```

Thus the observed effect remained local to the isolated verification clone; no remote ScriptOps main deployment occurred.

## Finding

```text
X1B-V2-CV-F001 — EXECUTION SUBSTRATE WAS A CODESPACE, NOT THE FROZEN READ-ONLY GITHUB ACTIONS EFFECT JOB = BLOCKER
```

The frozen packet requires in Section 22:

```text
supported-host effect job
permissions: contents: read
persist-credentials: false for checkouts
ScriptOps effect process receives no GitHub write credential
```

It also requires Section 21 durable preservation through a Git bundle plus textual evidence uploaded as a GitHub Actions workflow artifact before the supported runner exits.

The actual real effect was executed interactively in a GitHub Codespace. Immediately before the preflight and effect, the effect shell explicitly removed all frozen GitHub-token/proxy variables, the runtime parent guard passed, the isolated network child reported no credential/proxy authority inputs, and the effect process performed only public credential-free GitHub authority reads plus local Git operations.

However, a Codespace is not the preregistered GitHub Actions job configuration. The run therefore did not establish the packet's exact executor-substrate property:

```text
permissions: contents: read
checkout persist-credentials: false
```

A GitHub credential had also been observable in the Codespace environment in an earlier shell before cleansing; its value is intentionally not reproduced here. Although the effect shell was cleansed and the effect process did not receive that environment variable, this does not retroactively turn the Codespace into the frozen read-only Actions job.

Therefore the exact preregistered corrective-verification procedure cannot be declared PASS from this run.

This is a verification-procedure / executor-substrate blocker. It is not evidence that the V2 Human-authorship runtime property failed: the real local runtime, Human review binding, admission, CAS, durable record, and post-effect truth all passed in the observed Codespace run.

## First-counterexample STOP

This review applies:

```text
FIRST CREDIBLE COUNTEREXAMPLE = STOP FURTHER CLOSURE SEARCH IN THIS RUN
```

No independent corrective-closure review is authorized or performed from this state.

The missing GitHub Actions workflow-artifact preservation is not silently waived. Because the Section-22 substrate blocker already prevents PASS, this artifact does not promote later preservation questions into additional independently enumerated blockers in this run.

## Disposition

```text
LOCAL POSITIVE-CONTROL RUNTIME RESULT = PASS
EXACT PR #171 CORRECTIVE-VERIFICATION PROCEDURE = NOT PASS
X1B = OPEN
V1 AUTHORITY = NO
```

The successful local digest `D` has already produced a committed local verification effect and must not be reused as though unconsumed.

Any repeat intended to satisfy the exact frozen executor-substrate requirement must not silently reuse this Human decision. At minimum it requires a separately authorized bounded successor verification procedure with a fresh request nonce/digest and a fresh Human GitHub review, executed in a job whose read-only permissions / checkout credential handling and artifact preservation are established before effect.

Whether B0 itself may be reused or must be replaced is a successor-procedure design decision and is not authorized or selected by this finding.

## Next legal stage

```text
HUMAN DISPOSITION ON X1B-V2-CV-F001
```

No repair or retry is authorized by this artifact.
