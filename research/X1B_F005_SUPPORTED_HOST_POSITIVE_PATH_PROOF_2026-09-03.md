# X1B F005 — Supported-Host GitHub/TLS Positive-Path Proof

Status: `PROOF COMPLETE / NO SCRIPTOPS EFFECT AUTHORITY`

Date: `2026-09-03`

## 1. Purpose

This artifact freezes the Human-authorized inert supported-host positive-path proof required by the F005 implementation brief and identified as missing by independent implementation re-review R2.

It proves only that the exact isolated GitHub authority reader from the frozen ScriptOps implementation candidate can, on a supported GitHub Actions host/runtime:

- start from the candidate implementation at the exact reviewed commit;
- spawn its isolated network child with the executor-created environment;
- load a nonempty default OS CA store;
- perform verified direct HTTPS reads to public `api.github.com` endpoints without caller-selected authority inputs;
- observe the qualifying real trusted-Human review by durable GitHub user ID `226907434`;
- retrieve the exact immutable Human-reviewed evidence commit and evidence files;
- return the expected bounded child result.

This proof does not invoke ScriptOps `approve`, does not construct local ScriptOps admission/effect state, does not execute Git CAS, and does not mutate any ScriptOps canonical screenplay state.

Preserve:

```text
PROOF REVIEW != SCRIPTOPS EFFECT AUTHORITY
PROOF PASS != IMPLEMENTATION REVIEW PASS
PROOF PASS != X1B CLOSURE
AI PROPOSES != HUMAN DECIDES
```

## 2. Governing authority

Independent implementation re-review R2:

```text
FJ899/8 PR #162
VERDICT = NOT PASS
BLOCKER = X1B-V2-IMPL-R2-F001
          F005 SUPPORTED-HOST LIVE GITHUB AUTHORITY POSITIVE-PATH EVIDENCE IS ABSENT
```

Human authorization for exactly this inert proof:

```text
FJ899/8 PR #163
HEAD = 4de175b38f37cf3da76381da565c657bd2e87b6d
HUMAN RESPONSE = accept
```

The authority permits deliberately non-executable proof evidence, one real trusted-Human GitHub review of that inert proof content, and supported-host execution of the exact isolated network reader.

It does not authorize ScriptOps approve/effect, canonical CAS, merge, closure, V1, release, deployment or tag.

## 3. Exact ScriptOps implementation candidate under proof

```text
REPOSITORY = FJ899/scriptops
PR = #35
BASE = 2f22843ac570498b506101addeba5453ab777f08
CANDIDATE HEAD = b281383be083be24d7e4b9f6c9411d3cc1c317f2
CANDIDATE TREE = aa2b974efa01f55e0f909a0de60fcbde2b7e6a3f
```

The proof runner checked out that exact immutable candidate SHA in detached-HEAD mode before importing the authority module.

No ScriptOps branch or ref was updated by the proof runner.

## 4. Inert Human-review evidence

Evidence PR:

```text
FJ899/8 PR #164
TITLE = X1B F005: inert supported-host GitHub/TLS proof evidence
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD / immutable reviewed H = a9326fc3524f9c1073785901df24520aa9d0a364
COMMITS = 1
CHANGED FILES = 2
```

Exact request digest:

```text
d7820bee447aea43861f097d21da8133c41157deac360d8ec2e250729222a8d8
```

Exact two changed paths:

```text
decisions/x1b/requests/d7820bee447aea43861f097d21da8133c41157deac360d8ec2e250729222a8d8/request.json
decisions/x1b/requests/d7820bee447aea43861f097d21da8133c41157deac360d8ec2e250729222a8d8/accepted-scene.fountain
```

The request is deliberately non-executable for ScriptOps:

```text
scriptops_base_head = 0000000000000000000000000000000000000000
```

No real ScriptOps ref can equal the all-zero non-object ID. The proof runner never invoked ScriptOps parent admission or effect execution with this request.

## 5. Exact real Human review evidence

The qualifying GitHub REST review record is:

```text
review numeric ID = 5106168696
review node ID = PRR_kwDOUG1uSM8AAAABMFnzeA
user.login = litrgratis-pixel
user.id = 226907434
user.node_id = U_kgDODYZVKg
state = APPROVED
submitted_at = 2026-09-03T19:51:17Z
commit_id = a9326fc3524f9c1073785901df24520aa9d0a364
```

Exact review body:

```text
X1B-HUMAN-DECISION-V2
request_sha256=d7820bee447aea43861f097d21da8133c41157deac360d8ec2e250729222a8d8
decision=APPROVE
```

No trailing text is part of the returned body.

The review is intentionally proof-only and is not authority for any ScriptOps screenplay effect.

## 6. Supported-host proof runner

Proof harness repository/branch:

```text
FJ899/8
branch = proof-runner/x1b-f005-supported-host-proof-20260903
workflow = .github/workflows/x1b-f005-supported-host-proof.yml
harness commit = caabaa62cb88f45ac9284a5b3a384c9bfb56ba0a
```

GitHub Actions execution:

```text
workflow = x1b-f005-supported-host-proof
run ID = 33799081048
job ID = 100793781612
job name = proof
conclusion = success
started_at = 2026-09-03T19:53:46Z
completed_at = 2026-09-03T19:53:53Z
runner label = ubuntu-latest
runner image = ubuntu-24.04
runner OS = Ubuntu 24.04.4 LTS
runner image version = 20260831.293.1
```

The proof step called only:

```python
result = x1b.run_network_child(164)
```

from the exact checked-out candidate `b281383be083be24d7e4b9f6c9411d3cc1c317f2`.

It did not call:

```text
approve_scene
local_preflight for a real ScriptOps request
admission effect execution
execute_admission
cas_main
update-ref on ScriptOps
```

## 7. Exact successful child result summary

The proof job emitted:

```json
{
  "decision_pr": 164,
  "human_github_user_id": 226907434,
  "proof": "PASS",
  "request_sha256": "d7820bee447aea43861f097d21da8133c41157deac360d8ec2e250729222a8d8",
  "review_commit_id": "a9326fc3524f9c1073785901df24520aa9d0a364",
  "review_numeric_id": 5106168696,
  "review_state": "APPROVED",
  "scriptops_candidate": "b281383be083be24d7e4b9f6c9411d3cc1c317f2"
}
```

These values were asserted by the workflow and the job exited successfully.

Therefore the exact network child successfully completed:

```text
public reviews GET for PR #164
+
trusted-Human current review selection
+
immutable request.json fetch at exact H
+
immutable accepted-scene.fountain fetch at exact H
```

A failure in any of those operations would have caused `run_network_child(164)` to return nonzero/raise and the job to fail.

## 8. TLS and default-CA observations

The child returned:

```text
check_hostname = true
verify_mode = 2 = ssl.CERT_REQUIRED
minimum_version = 771 = TLSv1.2
OpenSSL = OpenSSL 3.0.13 30 Jan 2024
cert_store_stats.x509 = 121
cert_store_stats.x509_ca = 121
cert_store_stats.crl = 0
```

Observed default verify paths:

```text
cafile = /usr/lib/ssl/cert.pem
capath = /usr/lib/ssl/certs
OpenSSL env key names reported by ssl.get_default_verify_paths():
  SSL_CERT_FILE
  SSL_CERT_DIR
```

The presence of the *names* `SSL_CERT_FILE` and `SSL_CERT_DIR` in `ssl.get_default_verify_paths()` describes OpenSSL's conventional override-variable names; it does not mean those variables were present in the child environment.

The child environment observation after Python startup was exactly:

```text
LC_CTYPE
X1B_NETWORK_CHILD
```

`LC_CTYPE` is runtime locale state synthesized/observed after Python process startup. None of the forbidden authority-input variables was present:

```text
SSL_CERT_FILE
SSL_CERT_DIR
OPENSSL_CONF
OPENSSL_MODULES
GITHUB_TOKEN
GH_TOKEN
HTTP_PROXY
HTTPS_PROXY
ALL_PROXY
PYTHONPATH
PYTHONHOME
```

The candidate's parent constructs the child process environment as:

```text
{"X1B_NETWORK_CHILD": "1"}
```

and the supported-host execution confirms that no forbidden caller authority input appeared in the child TLS observation.

## 9. No Authorization header in authority HTTP

The exact candidate `_github_get()` implementation constructs the authority HTTP request internally and supplies only:

```text
Accept: application/vnd.github+json
X-GitHub-Api-Version: 2026-03-10
User-Agent: scriptops-x1b-human-decision/2
```

It does not construct an `Authorization` or `Cookie` header.

The isolated child environment contained no `GITHUB_TOKEN` or `GH_TOKEN`.

The GitHub Actions checkout step used its own temporary checkout credential before the proof step; `persist-credentials=false` removed that checkout header after the exact candidate was fetched. That credential is not used by `http.client.HTTPSConnection` inside the isolated authority child and is not part of the authority request path.

Thus the successful public reviews/content reads are the credential-free authority path frozen by F005.

## 10. F005 positive-path requirement disposition

The F005 brief required, before implementation-review PASS, supported-host evidence of:

```text
fresh child spawned under the isolated construction
SSL_CERT_FILE absent
SSL_CERT_DIR absent
OPENSSL_CONF absent
nonempty default CA store
check_hostname true
CERT_REQUIRED
TLS >= 1.2
successful direct HTTPS GET to api.github.com public review endpoint
no Authorization header in the authority reader
real trusted Human user.id = 226907434 visible in qualifying review response
```

Disposition from this proof:

```text
fresh isolated child = PROVEN
forbidden TLS CA/config variables absent = PROVEN
default CA x509_ca > 0 = PROVEN (121)
check_hostname = PROVEN TRUE
CERT_REQUIRED = PROVEN
TLS >= 1.2 = PROVEN
real direct public GitHub authority read = PROVEN
trusted user.id 226907434 = PROVEN
qualifying APPROVED review on immutable H = PROVEN
immutable request/scene reads at H = PROVEN
credential-free authority HTTP construction = PROVEN by exact candidate source + isolated env + successful run
```

Therefore:

```text
X1B-V2-IMPL-R2-F001
F005 SUPPORTED-HOST LIVE GITHUB AUTHORITY POSITIVE-PATH EVIDENCE IS ABSENT
=
MATERIALLY SATISFIED BY THIS PROOF
```

This is a proof-evidence disposition only. Only a separately authorized independent implementation re-review may convert the implementation-candidate review disposition to PASS.

## 11. Explicit non-effect statement

During this proof:

```text
no ScriptOps approve command was invoked
no real ScriptOps HumanDecisionRequestV2 was admitted
no X1BOperationAdmissionV2 for a real ScriptOps effect was consumed
no prospective ScriptOps commit was constructed for execution
no ScriptOps refs/heads/main CAS occurred
no canonical scene changed
no ScriptOps decision-log record was committed
no HumanDecision=TRUE screenplay effect was emitted
no merge occurred
```

The only Human act was the explicitly proof-only GitHub APPROVED review on inert PR #164.

## 12. Next legal stage

After this proof is frozen:

```text
STOP
NEXT LEGAL STAGE = ONE SEPARATELY HUMAN-AUTHORIZED INDEPENDENT AK-CANON IMPLEMENTATION RE-REVIEW
```

That re-review must target the exact repaired ScriptOps candidate:

```text
FJ899/scriptops PR #35
HEAD = b281383be083be24d7e4b9f6c9411d3cc1c317f2
TREE = aa2b974efa01f55e0f909a0de60fcbde2b7e6a3f
```

and consume this supported-host proof as evidence for the previously missing F005 positive-path criterion.

If that re-review returns PASS, the legal sequence remains:

```text
fresh preregistered corrective-verification packet
-> separate Human execution authorization
-> negative matrix + real Human positive control
-> independent corrective-closure review
-> Human corrective-closure acceptance
```

No later stage is authorized by this proof alone.
