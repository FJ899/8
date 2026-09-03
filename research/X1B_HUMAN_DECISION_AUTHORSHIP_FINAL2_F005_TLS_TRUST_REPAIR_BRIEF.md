# X1B Human Decision Authorship — FINAL2 F005 TLS TRUST REPAIR BRIEF

Status: `MINIMAL SUPERSEDING REPAIR BRIEF / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-03`

## 1. Purpose and authority boundary

This is the one F005-only successor planning artifact authorized after Human acceptance of the first credible blocker found in the independent review of PR #155.

It changes only the network/TLS trust construction used by `GitHubDecisionReaderV2`.

All non-network semantics of PR #155 remain frozen and unchanged, including:

```text
F001 durable GitHub numeric Human user ID
F002 single current Human review response + immutable review.commit_id H
F003 common-dir lock + prospective commit + pre-canonical update-ref CAS
F004 AnchoredGitV2 repository/ref/index/object anchoring
HumanDecisionRequestV2
X1BOperationAdmissionV2
X1BDecisionRecordV2
legacy/current accepted-state bypass closure
positive Human-control sequence
post-effect logical truth
scope firewall
```

This document and exact PR #155 together form the successor implementation brief. Where this document conflicts with PR #155 section 14 network/TLS construction or its network-environment tests, this document controls. No other PR #155 clause is superseded.

This brief performs no ScriptOps mutation and no canonical screenplay effect.

After exact durable freeze:

```text
STOP
NEXT LEGAL STAGE = ONE SEPARATELY HUMAN-AUTHORIZED INDEPENDENT AK-CANON REVIEW
```

Preserve:

```text
F005 REPAIR != IMPLEMENTATION AUTHORITY
AK-CANON PASS != IMPLEMENTATION AUTHORITY
IMPLEMENTATION SUCCESS != X1B CLOSURE
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact governing lineage

### 2.1 Final bounded V2 mechanism

```text
FJ899/8 PR #155
TITLE = X1B: bounded final brief reopen for F001-F004
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 3509c6e0922b28eb2d141fb3599ee21a1c7ee102
TREE = a499cbadbf85314e9e7ab473c97cd18d9afa8dd5
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_FINAL_BOUNDED_IMPLEMENTATION_BRIEF_REOPEN_F001_F004.md
BLOB = e796e00c778c4b149dbc79abf05795a61450360d
```

### 2.2 Independent review

```text
FJ899/8 PR #156
TITLE = X1B: independent AK-CANON review of bounded F001-F004 reopen
HEAD = a3bd7d653e96ccb19bb2952f1ecf2542f6664742
TREE = 593a09a135116e4f7630e1d839c2dfb9bce584b6
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_FINAL_BOUNDED_REOPEN_F001_F004_AK_CANON_REVIEW.md
BLOB = c7f5f10516dba5b3909336bdb5816165b0306c7d
VERDICT = NOT PASS
```

Review disposition preserved:

```text
F001 = MATERIALLY CLOSED AT BRIEF LEVEL
F002 = MATERIALLY CLOSED AT BRIEF LEVEL
F003 = MATERIALLY CLOSED AT BRIEF LEVEL
F004 = MATERIALLY CLOSED AT BRIEF LEVEL
```

First credible blocker:

```text
X1B-FINAL2-IBR-F005 — CALLER-CONTROLLED TLS CA ENVIRONMENT CAN REPLACE THE DECLARED OS TRUST STORE = BLOCKER
```

### 2.3 Human acceptance

```text
FJ899/8 PR #157
HEAD = 628eaace9edbea62de240d8cb458b6375b94d44c
TREE = ef558602477b525803fc56d38767ef747a496233
PATH = acceptance/X1B_FINAL2_F005_HUMAN_ACCEPT_2026-09-03.md
BLOB = e0bf7f796e47047a29988c3081bdcbc13bea2287
HUMAN DECISION = accept
```

Authorized scope:

```text
ONE F005-ONLY SUCCESSOR BRIEF
CALLER-INDEPENDENT TLS TRUST FOR GitHubDecisionReaderV2
PRESERVE F001-F004
NO PHYSICAL-PLATFORM REOPEN
```

## 3. Exact repository baselines

Evidence/governance repository:

```text
FJ899/8 main
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

ScriptOps implementation baseline remains exactly the PR #155 baseline:

```text
FJ899/scriptops main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

No implementation surface is added beyond the PR #155 allowed surface. In particular the F005 repair belongs inside:

```text
phase6/x1b_human_decision.py
```

and its already-authorized tests/workflow.

## 4. Threat model — unchanged

The evaluated AI/process may still:

```text
set arbitrary normal process environment variables
invoke approval repeatedly/concurrently
choose the decision PR number
prepare/update proposer-controlled evidence PR state
```

It still does not possess the trusted Human GitHub account.

Trusted infrastructure remains ordinary correctness of:

```text
host kernel/process isolation
Python runtime and stdlib ssl/http.client/subprocess
installed OS TLS/OpenSSL integration
operating-system CA trust installation
GitHub HTTPS service
Human control of GitHub user ID 226907434
```

Still explicitly outside claim:

```text
compromised OS CA store
malicious Python/OpenSSL implementation
malicious kernel/filesystem/Git binary
compromised Human account
TPM/EK/AK
CRLs
PMEM/NFIT
bare-metal locality
BMC provenance
universal power-loss durability
```

## 5. F005 repair principle

The authority reader must not inherit caller process environment into the TLS implementation that authenticates GitHub.

The repair therefore does not maintain an ever-growing blacklist of CA-related environment variables.

Instead, all GitHub authority network operations execute in a dedicated isolated Python child process whose environment is constructed by the executor and contains no caller-provided environment entries.

Normative shape:

```text
caller-controlled parent environment
-> no direct authority network access
-> spawn isolated stdlib-only GitHubDecisionReader child
-> child environment = exact frozen allowlist generated by executor
-> child imports ssl/http.client only after process start under that environment
-> child creates its own default OS-CA TLS context
-> child connects directly to api.github.com:443
-> child returns bounded raw authority responses to parent
```

This keeps the accepted OS-CA trust model while removing caller-selected CA database inputs.

## 6. Dedicated network child

`phase6/x1b_human_decision.py` implements an internal, non-public child mode.

Parent invocation shape is equivalent to:

```text
<absolute sys.executable> -I <absolute SOURCE_ROOT/phase6/x1b_human_decision.py> --_x1b-github-reader-child
```

Requirements:

```text
sys.executable is resolved to an absolute real path before spawn
-I is mandatory
child program path is derived from resolved module/SOURCE_ROOT, not cwd or PATH
shell = false
stdin/stdout pipes are executor-created
stderr is captured separately
fixed timeout applies
nonzero exit / signal / timeout / malformed output = DENY
```

The internal child mode is not an authority bypass. It accepts only the narrow machine request schema in section 9 and cannot perform a ScriptOps effect.

## 7. Frozen child environment

The child receives a fresh mapping, not a copy-and-delete mutation of `os.environ`.

Exact production child environment:

```text
X1B_NETWORK_CHILD = 1
```

No other environment key from the parent is copied.

In particular the child environment does not contain:

```text
SSL_CERT_FILE
SSL_CERT_DIR
OPENSSL_CONF
OPENSSL_MODULES
GITHUB_TOKEN
GH_TOKEN
GITHUB_ENTERPRISE_TOKEN
GH_ENTERPRISE_TOKEN
HTTP_PROXY
HTTPS_PROXY
ALL_PROXY
http_proxy
https_proxy
all_proxy
REQUESTS_CA_BUNDLE
CURL_CA_BUNDLE
PYTHONPATH
PYTHONHOME
```

The explicit list above is explanatory/test coverage. The security rule is stronger:

```text
NO PARENT ENVIRONMENT ENTRY IS INHERITED
```

except the single executor-generated `X1B_NETWORK_CHILD=1` marker.

The parent must not use `env=os.environ.copy()` for the network child.

No request, CLI option, config file or evidence field may add an environment entry to this child.

## 8. Import and initialization ordering

The network child must reach its isolated-child dispatch before importing any non-stdlib project module.

Its network path imports only Python standard-library modules needed for bounded HTTPS/JSON/base64 processing, including:

```text
ssl
http.client
json
base64
hashlib
```

No `requests`, `urllib3`, GitHub CLI, curl, system Git credential helper or project plugin is used for Human authority network reads.

`ssl` is imported in the fresh child process after exec/spawn under the frozen child environment.

This prevents the parent caller environment from being the environment used when the child initializes its TLS stack.

## 9. Parent-to-child request schema

The parent sends one canonical JSON object over stdin.

Allowed top-level keys are exactly:

```text
schema_version = x1b-github-reader-child-request/v1
decision_pr
```

`decision_pr` is a positive decimal integer within GitHub PR-number range accepted by the parent.

No URL, hostname, port, CA path, certificate bytes, proxy, token, header override, filesystem path or TLS option may be supplied by the parent-to-child request.

Unknown/missing/duplicate keys or malformed JSON:

```text
CHILD_DENY
```

## 10. Child network origin and HTTP stack

The child constructs all network destinations internally.

Fixed origin:

```text
HOST = api.github.com
PORT = 443
SCHEME = https
```

Only direct `http.client.HTTPSConnection` connections using the internally created TLS context are permitted.

No proxy handler exists.

No redirect is followed. Any 3xx response is a failure.

Headers remain the PR #155 V2 headers:

```text
Accept: application/vnd.github+json
X-GitHub-Api-Version: 2026-03-10
User-Agent: scriptops-x1b-human-decision/2
```

No Authorization or Cookie header is sent.

The child rejects any response not matching the endpoint-specific status/content/size/schema rules already frozen by PR #155.

## 11. Caller-independent OS-CA TLS context

The child constructs the TLS context internally after section-7 environment isolation.

Normative construction:

```python
context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
context.check_hostname = True
context.verify_mode = ssl.CERT_REQUIRED
context.minimum_version = ssl.TLSVersion.TLSv1_2
```

No arguments are accepted for:

```text
cafile
capath
cadata
SSLContext object
hostname
verify mode
check_hostname
minimum TLS version
```

The context must use Python/OpenSSL default certificate loading after all caller environment has been removed by process isolation.

The child records for evidence only:

```text
ssl.OPENSSL_VERSION
ssl.get_default_verify_paths() result
context.cert_store_stats()
context.minimum_version
context.verify_mode
context.check_hostname
```

These are observations, not caller-selectable authority.

Require before first HTTPS request:

```text
check_hostname = true
verify_mode = CERT_REQUIRED
minimum_version >= TLSv1_2
cert_store_stats().x509_ca > 0
```

If the current supported host cannot load any default CA roots under the isolated environment:

```text
DENY / POSITIVE PATH NOT IMPLEMENTABLE ON THAT HOST
```

The implementation must not compensate by reading a caller-provided CA file.

## 12. TLS peer and hostname semantics

Every authority request uses:

```text
HTTPSConnection("api.github.com", 443, context=context)
```

The TLS server name / hostname verification target is therefore exactly:

```text
api.github.com
```

Certificate validation failure, hostname mismatch, TLS negotiation failure or any inability to prove the verified connection:

```text
DENY
HumanDecision != TRUE
```

There is no HTTP downgrade and no alternate hostname fallback.

## 13. Network operations performed inside child

All PR #155 `GitHubDecisionReaderV2` HTTP operations move into the same isolated child:

```text
single complete reviews request for decision PR N
immutable request.json fetch at exact review.commit_id H
immutable accepted-scene.fountain fetch at exact H
```

The child applies PR #155 F002 rules unchanged:

```text
one complete <=99 review response
no pagination ambiguity
latest durable-Human authority-relevant review selection
user.id = 226907434
exact X1B-HUMAN-DECISION-V2 body
immutable H/D binding
reserved-marker ambiguity denial
```

The child does not need mutable current PR-head metadata.

The parent does not independently refetch or substitute these network resources.

## 14. Child-to-parent result schema

On success the child emits one canonical JSON result over stdout and exits zero.

The result contains only bounded authority evidence needed by the existing V2 parent verifier, including:

```text
schema_version = x1b-github-reader-child-result/v1
review_response_raw_b64
review_response_digest
human_review_set_digest
human_review_numeric_id
human_github_user_id
human_review_login_observed
human_review_node_id_observed_or_empty
human_review_state
human_review_commit_id
human_review_submitted_at
human_review_body_b64
request_sha256
request_json_raw_b64
accepted_scene_raw_b64
tls_observation
```

Maximum raw response/file sizes are frozen by the implementation and exceeding them is DENY.

The parent reparses and independently revalidates all authority-critical JSON/content/digests using PR #155 rules before creating `X1BOperationAdmissionV2`.

The child result is evidence transport, not an execution credential by itself.

Malformed/extra/missing child result fields:

```text
DENY
```

## 15. Parent behavior under attacker environment

The existing PR #155 parent-level rejection of credential/proxy variables remains permitted and should be retained as defense in depth.

F005 security does not rely on that blacklist.

Even when the parent process contains arbitrary variables not explicitly named by the code, the authority TLS child receives only the frozen environment in section 7.

Therefore caller environment cannot select:

```text
CA file
CA directory
OpenSSL config/module path
proxy
GitHub credential
Python import path
third-party HTTP-library CA bundle
```

for the child authority read.

## 16. Failure semantics

Any failure in:

```text
child spawn
isolated environment construction
TLS context construction
OS default CA loading
DNS/TCP/TLS
hostname/certificate verification
HTTP status/schema/size
review currentness
immutable H content retrieval
child result parse
parent independent revalidation
```

is fail closed before canonical ScriptOps effect:

```text
DENY
HumanDecision != TRUE
```

No cached network response or previous successful child output may be reused for a new run.

No fallback to unauthenticated HTTP, curl, `gh`, requests, caller CA bundle or disabled certificate verification exists.

## 17. F005 deterministic tests

Required new tests:

```text
X1B-TLS1 parent has SSL_CERT_FILE=<attacker path> -> child environment contains no SSL_CERT_FILE
X1B-TLS2 parent has SSL_CERT_DIR=<attacker path> -> child environment contains no SSL_CERT_DIR
X1B-TLS3 parent has OPENSSL_CONF/OPENSSL_MODULES -> child receives neither
X1B-TLS4 parent has REQUESTS_CA_BUNDLE/CURL_CA_BUNDLE -> child receives neither
X1B-TLS5 parent has arbitrary unknown environment key -> child receives neither
X1B-TLS6 child request attempts url/host/port/cafile/capath/cadata override -> schema DENY
X1B-TLS7 child TLS context check_hostname = true
X1B-TLS8 child TLS context verify_mode = CERT_REQUIRED
X1B-TLS9 child TLS minimum version >= TLSv1_2
X1B-TLS10 child default CA store has x509_ca > 0 on supported positive-control host
X1B-TLS11 live api.github.com public review read succeeds without Authorization under clean child environment
X1B-TLS12 TLS/certificate/hostname failure -> DENY before authority JSON admission
X1B-TLS13 child output tamper/malformed/extra field -> parent DENY
X1B-TLS14 parent never performs authority HTTP itself
X1B-TLS15 repeated run spawns fresh child; no prior response cache can substitute
```

Existing PR #155 negative/positive F001-F004, original X1B and bypass tests remain mandatory without modification.

## 18. Positive-path proof requirement

Before any implementation candidate can PASS independent implementation review, evidence must demonstrate on the exact supported execution host/runtime:

```text
fresh child spawned with exact section-7 environment
isolated child observed SSL_CERT_FILE absent
isolated child observed SSL_CERT_DIR absent
isolated child observed OPENSSL_CONF absent
isolated child CA store x509_ca > 0
check_hostname true
CERT_REQUIRED
TLS >= 1.2
successful direct HTTPS GET to api.github.com public review endpoint
no Authorization header
same real GitHub Human account user.id = 226907434 visible in qualifying positive-control review response
```

This is implementability evidence, not Human approval for a screenplay effect.

## 19. F005 closure mapping

PR #156 counterexample required:

```text
caller controls normal parent environment
+
TLS authority reader inherits caller-selected CA lookup environment
->
caller can replace declared OS trust input
```

This repair changes the chain to:

```text
caller controls parent environment
+
parent spawns fresh Python child with exact executor-created one-key environment
+
child initializes stdlib TLS after process start
+
child accepts no CA/proxy/token/URL inputs
+
child loads default OS trust under that isolated environment
->
caller environment cannot select the CA database used for GitHub authority reads
```

Therefore F005 is closed at specification level if independent review finds the child isolation/stdlib positive path realizable as frozen.

## 20. Scope firewall

A future review may block this repair for an attack that, under the stated trusted-runtime/OS-CA threat model, can cause caller-controlled state to substitute the GitHub/Human authority read or make the claimed positive path unrealizable.

Do not reopen merely for attacks requiring:

```text
compromised OS CA installation
malicious OS/kernel
malicious Python/OpenSSL binary
compromised GitHub service
compromised trusted Human account
physical TPM/PMEM/bare-metal properties
```

Any unrelated new security property is separate hardening unless it yields an X1B counterexample inside the frozen threat model.

## 21. AK-CANON PASS criteria

The F005 repair PASS requires all of:

```text
1 exact PR #155 F001-F004 semantics preserved
2 no caller parent environment inherited by authority network child
3 TLS stack initializes in fresh child under frozen environment
4 no caller URL/CA/proxy/token/TLS override input exists
5 direct api.github.com HTTPS uses hostname verification + CERT_REQUIRED + OS defaults
6 supported host has a working default CA positive path
7 all GitHub authority HTTP is performed by isolated child
8 parent independently revalidates returned authority evidence
9 failure is pre-effect fail-closed
10 no physical-platform/hardware scope is reintroduced
```

## 22. Sequence after future PASS

A PASS authorizes nothing by itself.

Legal sequence remains:

```text
Human implementation authorization
-> bounded ScriptOps implementation candidate
-> independent implementation review
-> preregistered corrective-verification packet
-> separate Human execution authorization
-> full negative matrix + real Human positive control
-> independent corrective-closure review
-> Human corrective-closure acceptance
```

Only Human corrective-closure acceptance closes X1B.

## 23. Explicit non-authority / STOP

This brief authorizes no:

```text
ScriptOps source mutation
phase6/x1b_human_decision.py creation
live decision-evidence PR
Human live V2 approval
positive control
canonical screenplay effect
merge
X1B closure
Agency Kernel V1
release
deployment
tag
```

After exact freeze:

```text
STOP
NEXT LEGAL STAGE = ONE SEPARATELY HUMAN-AUTHORIZED INDEPENDENT AK-CANON REVIEW OF THIS EXACT F005 REPAIR BRIEF
```

Preserve:

```text
MECHANISM != PROPERTY
F005 REPAIR != IMPLEMENTATION AUTHORITY
AK-CANON PASS != IMPLEMENTATION AUTHORITY
X1B CLOSED != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```
