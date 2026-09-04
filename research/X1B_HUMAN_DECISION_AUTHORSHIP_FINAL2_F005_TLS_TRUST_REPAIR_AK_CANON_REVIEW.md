# X1B Human Decision Authorship — Independent AK-CANON Review of FINAL2 F005 TLS Trust Repair

Status: `INDEPENDENT AK-CANON REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: `2026-09-03`

## 1. Verdict

```text
AK-CANON X1B FINAL2 F005 TLS TRUST REPAIR BRIEF REVIEW = PASS
```

The exact F005-only successor in `FJ899/8 PR #158` closes the first-credible blocker frozen by PR #156 at specification level without reopening the R4R17 physical-platform lineage and without changing the already-reviewed F001-F004 semantics.

No credible counterexample was established inside the frozen X1B threat model that allows caller-controlled parent environment to substitute the CA/trust input used for GitHub Human-authority reads.

Preserve:

```text
AK-CANON PASS != IMPLEMENTATION AUTHORITY
IMPLEMENTATION SUCCESS != X1B CLOSURE
PASS != LIVE HUMAN DECISION AUTHORITY
PASS != CANONICAL EFFECT AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#158`

```text
TITLE = X1B: minimal FINAL2 F005 TLS trust repair brief
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = e188a452b0960d846479a975fc2d9f2c76aac50d
TREE = 83263b8c297eca72cca8bb35fe6c3c9338dc700b
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_FINAL2_F005_TLS_TRUST_REPAIR_BRIEF.md
BLOB = ff06a772275bc861de9211375e8bda08d67ead3e
STATE = OPEN / DRAFT / UNMERGED
COMMITS = 1
CHANGED FILES = 1
ADDITIONS = 697
```

The exact artifact was reread from candidate HEAD during this review.

Current evidence/governance baseline remained:

```text
FJ899/8 main
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

The composite normative brief is:

```text
PR #155 = F001-F004 and all non-network V2 semantics
PR #158 = F005-only supersession of PR #155 network/TLS construction and corresponding network-environment tests
```

## 3. Governing authority and scope

This review is Human-authorized by the `accept` following exact freeze of PR #158.

It remains bound by:

```text
PR #150 = convergence/scope review
PR #151 = Human acceptance of convergence disposition
PR #153 = independent review freezing F001-F004
PR #154 = Human acceptance of F001-F004 repair authority
PR #155 = bounded final F001-F004 successor
PR #156 = independent review: F001-F004 materially closed, F005 blocker
PR #157 = Human acceptance of F005 and F005-only repair authority
```

The accepted F005 blocker was:

```text
X1B-FINAL2-IBR-F005 — CALLER-CONTROLLED TLS CA ENVIRONMENT CAN REPLACE THE DECLARED OS TRUST STORE
```

This review therefore tested only whether the selected F005 repair establishes caller-independent TLS trust under the already-frozen trusted-runtime/OS-CA model and whether it regresses F001-F004.

It did not reopen:

```text
TPM/EK/AK
vendor CRLs
PMEM/NFIT
bare-metal locality
BMC console provenance
universal power-loss durability
hostile kernel/filesystem/Git binary
compromised OS CA installation
compromised trusted Human account
```

## 4. Review method

The independent review checked:

```text
exact PR #158 identity and one-file freeze
composite relationship to PR #155
fresh-child process environment semantics
Python isolated-mode semantics
Python default CA loading semantics
hostname verification and CERT_REQUIRED semantics
fixed GitHub origin / no caller URL/CA/proxy/token inputs
parent-to-child and child-to-parent authority boundaries
parent independent revalidation
F001-F004 non-network preservation
failure-before-effect behavior
positive-path realizability at specification level
```

The review also executed a local adversarial process-isolation probe with a deliberately contaminated parent environment.

## 5. F005 repair — environment isolation

PR #158 does not attempt to enumerate every possible CA-related environment variable and then delete selected names.

Instead it freezes a stronger construction:

```text
parent environment = caller controlled
child env mapping = newly constructed by executor
child env mapping contains only executor-generated X1B_NETWORK_CHILD=1
no parent environment entry is copied
```

Python `subprocess` documentation states that when `env` is supplied, the supplied mapping defines the new process environment instead of inheriting the current process environment.

Reference:

```text
https://docs.python.org/3/library/subprocess.html
```

This directly closes the PR #156 mechanism in which `SSL_CERT_FILE` and `SSL_CERT_DIR` were inherited by the authority TLS stack.

Disposition:

```text
X1B-FINAL2-IBR-F005 ENVIRONMENT-INHERITANCE COMPONENT = CLOSED AT BRIEF LEVEL
```

## 6. Isolated Python startup

The child is invoked from absolute, resolved executor-controlled paths with:

```text
<absolute sys.executable> -I <absolute x1b_human_decision.py> --_x1b-github-reader-child
```

and:

```text
shell = false
```

Python documents `-I` as isolated mode and states that it implies `-E`, `-P`, and `-s`; `PYTHON*` variables are ignored and script-directory/user-site path injection is removed.

Reference:

```text
https://docs.python.org/3/using/cmdline.html#cmdoption-I
```

Because the process is also spawned with a fresh environment mapping, F005 does not depend merely on `-I`; the fresh child environment is the primary boundary and `-I` is an additional interpreter-startup boundary.

Disposition:

```text
CALLER PYTHON-ENVIRONMENT INJECTION = CLOSED AT BRIEF LEVEL
```

## 7. TLS context construction

PR #158 freezes:

```python
context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
context.check_hostname = True
context.verify_mode = ssl.CERT_REQUIRED
context.minimum_version = ssl.TLSVersion.TLSv1_2
```

with no accepted caller argument for:

```text
cafile
capath
cadata
SSLContext
hostname
verify mode
minimum TLS version
```

Python documents that `create_default_context()` with `SERVER_AUTH` uses certificate verification and default CA certificates when no explicit CA parameters are supplied, and recommends it for loading system trusted CA certificates with hostname checking.

Reference:

```text
https://docs.python.org/3/library/ssl.html#ssl.create_default_context
https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_default_certs
```

The previously dangerous OpenSSL default-path environment selectors remain visible through `ssl.get_default_verify_paths()`, but because the child did not inherit the caller environment, caller values cannot select them.

Disposition:

```text
CALLER CA-FILE / CA-DIR SELECTION = CLOSED AT BRIEF LEVEL
```

## 8. Fixed authority network origin

The child constructs the authority destination internally:

```text
HOST = api.github.com
PORT = 443
HTTPSConnection("api.github.com", 443, context=context)
```

The parent-to-child schema contains only:

```text
schema_version
decision_pr
```

and cannot carry:

```text
URL
hostname
port
proxy
CA path
CA bytes
Authorization credential
TLS option
```

No redirect is followed and no HTTP downgrade/fallback exists.

Therefore the caller cannot repair the loss of environment-based CA control by moving authority reads to a caller-selected origin.

Disposition:

```text
CALLER NETWORK-ORIGIN / CA OVERRIDE = CLOSED AT BRIEF LEVEL
```

## 9. Parent/child authority separation

All authority HTTP is required to execute in the child.

The child returns bounded raw evidence and derived metadata, but the parent must independently reparse and revalidate all authority-critical content and digests before constructing `X1BOperationAdmissionV2`.

The result channel is therefore:

```text
child output = evidence transport
child output != execution credential by itself
```

Malformed, missing, or extra result fields fail closed.

No cached child output may substitute for a fresh run.

No parent-side alternate HTTP path is authorized.

Disposition:

```text
NETWORK CHILD != EFFECT CAPABILITY
PARENT REVALIDATION = PRESERVED
```

## 10. Adversarial runtime probe

A local probe was executed on the review runtime using a parent process deliberately populated with attacker-style variables including:

```text
SSL_CERT_FILE=/tmp/attacker.pem
SSL_CERT_DIR=/tmp/attacker-ca
OPENSSL_CONF=/tmp/evil.cnf
OPENSSL_MODULES=/tmp/evilmods
PYTHONPATH=/tmp/evil
```

The parent spawned an absolute Python executable using:

```text
-I
fresh env mapping = {"X1B_NETWORK_CHILD":"1"}
```

Observed child state included:

```text
SSL_CERT_FILE absent
SSL_CERT_DIR absent
OPENSSL_CONF absent
OPENSSL_MODULES absent
PYTHONPATH absent
```

The interpreter itself added:

```text
LC_CTYPE=C.UTF-8
```

This value was not inherited from the hostile parent and is not a CA/proxy/credential selector. The security invariant in PR #158 is therefore understood as the exact spawn environment mapping plus no inherited parent entry, rather than a claim that CPython can never create an internal runtime environment entry after exec.

The same probe observed:

```text
OpenSSL default cafile = /usr/lib/ssl/cert.pem
OpenSSL default capath = /usr/lib/ssl/certs
context.cert_store_stats().x509_ca = 150
check_hostname = true
verify_mode = CERT_REQUIRED
minimum_version = TLSv1.2
```

This establishes local specification-level realizability of fresh-environment default-CA loading.

## 11. Live HTTPS observation limitation

The review attempted a direct stdlib `HTTPSConnection` to the public GitHub review endpoint under the isolated environment.

The review execution container could not resolve `api.github.com` by DNS.

A control probe using the normal process environment failed DNS in the same way. Therefore the failure is an outbound/DNS limitation of this review execution environment rather than evidence that the PR #158 isolation construction breaks DNS or TLS.

The review does not claim that the exact future supported ScriptOps host has already completed the PR #158 live positive control.

PR #158 already requires the later implementation-review evidence to demonstrate on the exact supported host/runtime:

```text
nonempty default CA roots
successful direct HTTPS GET to api.github.com
no Authorization header
real Human user.id = 226907434 visible in the qualifying review response
```

That implementation evidence remains mandatory.

This unresolved review-host network limitation is not promoted to a blocker because no incompatibility with the specified positive path was established.

## 12. Non-blocking Python `site` observation

Python documentation states that `-I` implies `-E`, `-P`, and `-s`, but not `-S`.

Python also documents that the `site` module is normally imported automatically and can load `sitecustomize`; automatic site processing is suppressed by `-S`.

References:

```text
https://docs.python.org/3/using/cmdline.html#cmdoption-I
https://docs.python.org/3/using/cmdline.html#cmdoption-S
https://docs.python.org/3/library/site.html
```

On the review runtime, an `-I` child still had installation-specific paths in `sys.path` and the installed runtime had a system `sitecustomize` hook.

This does not create a blocker under the frozen PR #158 threat model because:

```text
Python runtime/installation correctness is trusted
malicious Python/OpenSSL implementation is explicitly outside claim
no caller parent environment entry is inherited
user-site and PYTHON* injection are disabled
```

It is nevertheless an implementation-review check worth preserving:

```text
implementation must demonstrate that the exact supported Python runtime is within the declared trusted-runtime boundary
```

Using `-S` in addition to mandatory `-I` is compatible hardening if the implementation elects to make the phrase `stdlib-only` literal at Python startup, but this review does not require or authorize that implementation choice.

No new X1B finding is opened from this observation.

## 13. F001-F004 regression check

PR #158 explicitly preserves all non-network semantics of PR #155.

No F005 repair clause changes:

```text
F001 durable numeric GitHub user ID 226907434
F002 one complete Human review response + immutable review.commit_id H
F003 common-dir lock + prospective commit + pre-CAS verification + update-ref CAS
F004 AnchoredGitV2 repository/ref/index/object anchoring
HumanDecisionRequestV2 schema
X1BOperationAdmissionV2
X1BDecisionRecordV2
legacy/current accepted-state bypass closure
replay/currentness/base binding
post-effect HumanDecision truth
```

No regression was identified from moving the already-frozen GitHub authority reads into the isolated child because the parent is required to independently revalidate the returned raw authority evidence under the same PR #155 rules.

Disposition:

```text
F001-F004 PRESERVATION = PASS AT BRIEF LEVEL
```

## 14. F005 deterministic-test review

The new negative tests directly target the accepted blocker:

```text
SSL_CERT_FILE inheritance
SSL_CERT_DIR inheritance
OPENSSL_CONF / OPENSSL_MODULES inheritance
third-party CA-bundle environment
unknown parent environment key
caller URL/host/port/CA override attempts
TLS verify/hostname/minimum-version properties
TLS/certificate failure
child result tamper
parent HTTP bypass
response-cache reuse
```

The required positive tests include both default-CA loading and a real direct GitHub API read on the exact supported execution host.

No test-level gap was found that permits the original F005 mechanism to survive while the matrix passes.

Disposition:

```text
F005 TEST MATRIX = SUFFICIENT AT BRIEF LEVEL
```

## 15. PASS-criteria disposition

Against PR #158 section-21 criteria:

```text
1 exact PR #155 F001-F004 semantics preserved
  = PASS

2 no caller parent environment inherited by authority network child
  = PASS

3 TLS stack initializes in fresh child under frozen environment
  = PASS at specification level; exact implementation host evidence remains mandatory

4 no caller URL/CA/proxy/token/TLS override input exists
  = PASS

5 direct api.github.com HTTPS uses hostname verification + CERT_REQUIRED + OS defaults
  = PASS at specification level

6 supported host has a working default CA positive path
  = PASS for specification realizability; exact live GitHub endpoint proof remains a mandatory implementation gate

7 all GitHub authority HTTP is performed by isolated child
  = PASS

8 parent independently revalidates returned authority evidence
  = PASS

9 failure is pre-effect fail-closed
  = PASS

10 no physical-platform/hardware scope is reintroduced
  = PASS
```

Overall:

```text
AK-CANON X1B FINAL2 F005 TLS TRUST REPAIR BRIEF REVIEW = PASS
```

## 16. Closure mapping

The PR #156 attack was:

```text
caller controls parent environment
+
GitHub authority TLS inherits SSL_CERT_FILE / SSL_CERT_DIR
->
caller can substitute the declared OS CA trust input
```

The reviewed PR #158 chain is:

```text
caller controls parent environment
+
executor constructs fresh child env instead of inheriting parent env
+
absolute Python child starts with -I
+
child accepts no CA/proxy/token/origin input
+
child creates default SERVER_AUTH context after process isolation
+
child verifies api.github.com with CERT_REQUIRED + hostname verification
+
parent independently revalidates returned authority evidence
->
caller parent environment cannot select the CA database used for Human-authority reads
```

Therefore:

```text
X1B-FINAL2-IBR-F005 = MATERIALLY CLOSED AT IMPLEMENTATION-BRIEF LEVEL
```

## 17. Convergence assessment

```text
CONVERGENCE STRATEGY = VALID
F001-F004 = MATERIALLY CLOSED AT BRIEF LEVEL
F005 = MATERIALLY CLOSED AT BRIEF LEVEL
R4R17 PHYSICAL-PLATFORM LINEAGE = NOT REOPENED
FINAL COMPOSITE X1B IMPLEMENTATION BRIEF = AK-CANON PASS
```

No additional security class is added by this review.

The next stage is implementation, but only after a separate Human implementation authorization.

## 18. Explicit non-authority / STOP

This PASS review authorizes no:

```text
ScriptOps source mutation
phase6/x1b_human_decision.py creation
legacy approve mutation
restore/verifier/documentation mutation
CODEOWNERS/ruleset mutation
live decision-evidence PR
Human live V2 approval
positive-control execution
canonical screenplay effect
merge
X1B closure
Agency Kernel V1
release
deployment
tag
```

After durable freeze of this exact review:

```text
STOP
NEXT LEGAL STAGE = HUMAN IMPLEMENTATION AUTHORIZATION FOR THE AK-CANON-PASSED COMPOSITE PR #155 + PR #158 BRIEF
```

Preserve:

```text
AK-CANON PASS != IMPLEMENTATION AUTHORITY
IMPLEMENTATION SUCCESS != CORRECTIVE CLOSURE
X1B CLOSED != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```
