# X1B V2 — Runtime Defect Exposed by R3 Test-Matrix Completion

Status: `INDEPENDENT TEST-EVIDENCE FINDING / NOT REPAIR AUTHORITY`

Date: `2026-09-03`

## 1. Verdict

```text
X1B-V2-R3T-F001 — FORBIDDEN PARENT GITHUB CREDENTIAL / PROXY ENVIRONMENT REACHES THE AUTHORITY-CHILD INVOCATION INSTEAD OF FAILING CLOSED = RUNTIME BLOCKER
```

This finding was exposed by the first newly added mandatory regression under the Human-authorized test-matrix-completion authority. Per the frozen stop rule, no production runtime repair was made and no further missing-matrix tests were added after the runtime defect was established.

## 2. Governing Human authority

Independent R3 review:

```text
FJ899/8 PR #166
HEAD = 03c27ab4be20462b343746e79146f693d58879c9
FINDING = X1B-V2-IMPL-R3-F001
```

Human acceptance / test-only repair authority:

```text
FJ899/8 PR #167
HEAD = 5c601ceca94ccef106133d0a743e3095086a9263
HUMAN RESPONSE = accept
```

That authority explicitly froze:

```text
TEST COMPLETION AUTHORITY != RUNTIME REPAIR AUTHORITY
```

and required STOP if a newly added mandatory regression exposed a production-runtime defect.

## 3. Exact ScriptOps target when defect was exposed

Repository / PR:

```text
FJ899/scriptops PR #35
BASE = 2f22843ac570498b506101addeba5453ab777f08
```

Previously reviewed implementation HEAD:

```text
b281383be083be24d7e4b9f6c9411d3cc1c317f2
```

Test-only head after adding the first mandatory retained regression:

```text
e1f669bb02b16c5eec3c91faad5d25708fde8ed9
```

The only new change relative to `b281383...` is in the Human-authorized test/evidence surface:

```text
.github/workflows/x1b-human-decision.yml
```

No production runtime source was modified by the test-completion attempt.

## 4. Frozen requirement being tested

The accepted PR #155 implementation brief retains the explicit fail-closed regression:

```text
GitHub token/proxy environment -> DENY
```

PR #158 states that the existing PR #155 negative/positive tests remain mandatory without modification. Its child-isolation repair also says the existing parent-level credential/proxy rejection should be retained as defense in depth, while making clear that F005 TLS security does not rely on the blacklist.

Therefore this is not a newly invented requirement.

## 5. Exact executable regression

The new workflow step sets, one at a time:

```text
GITHUB_TOKEN
GH_TOKEN
HTTP_PROXY
HTTPS_PROXY
ALL_PROXY
```

and invokes the real `approve_scene()` control flow with repository/preflight objects mocked only to isolate the parent environment boundary.

`run_network_child()` is replaced with an assertion that it must not be reached while a forbidden parent authority variable is present.

Expected contract:

```text
forbidden parent credential/proxy environment
-> X1BError / DENY
-> authority child not invoked
-> no effect
```

## 6. Exact observed failure

GitHub Actions:

```text
workflow = x1b-human-decision
run ID = 33800463714
job ID = 100798450352
head = e1f669bb02b16c5eec3c91faad5d25708fde8ed9
conclusion = failure
```

The first case, `GITHUB_TOKEN`, failed with the real stack:

```text
phase6/x1b_human_decision.py: approve_scene
    result = run_network_child(decision_pr)

AssertionError:
authority child was reached while forbidden parent env GITHUB_TOKEN was set
```

The regression stopped at the first forbidden variable, so no claim is made that the later proxy variables were separately executed in this run.

## 7. Root cause in the reviewed runtime

Current `approve_scene()` performs:

```text
AnchoredGitV2.discover
x1b_lock
local_preflight
run_network_child(decision_pr)
...
```

without a parent-environment guard rejecting the frozen credential/proxy keys.

`run_network_child()` does correctly spawn the authority child with a fresh one-key environment:

```text
{"X1B_NETWORK_CHILD": "1"}
```

so this finding does **not** invalidate the already proven F005 child TLS/CA isolation. The supported-host proof in PR #165 remains evidence that those parent values are not inherited by the authority child.

The defect is narrower:

```text
accepted retained fail-closed contract says parent token/proxy env -> DENY
but runtime continues to authority-child invocation
```

## 8. Security/scope disposition

This finding is inside the frozen implementation contract and must block implementation-review PASS until repaired or the governing brief is separately reopened by Human authority.

It does not reopen:

```text
TPM / PMEM / NFIT / BMC / CRL / bare-metal locality
```

It also does not establish that a parent `GITHUB_TOKEN` can alter the isolated child HTTP request under the current F005 design. The child isolation remains intact.

## 9. Bounded repair recommendation — not authority

The smallest conforming runtime repair is to add one explicit parent authority-environment guard in:

```text
phase6/x1b_human_decision.py
```

before the final authority read / `run_network_child()` call.

At minimum reject any non-empty inherited value for the already-frozen keys:

```text
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
```

The exact frozen retained list from the governing brief should control the implementation; do not expand it into a new general environment-security subsystem.

Then the mandatory regression should remain executable and the rest of the R3 test matrix may continue.

## 10. Explicit non-authority / STOP

This finding authorizes no:

```text
production runtime repair
additional test-matrix completion beyond this STOP
live executable Human-decision evidence PR
Human screenplay approval
ScriptOps approve
real refs/heads/main CAS
canonical screenplay effect
merge
X1B closure
V1
release / deployment / tag
```

Next legal stage:

```text
SEPARATE HUMAN ACCEPTANCE OF X1B-V2-R3T-F001
+
BOUNDED RUNTIME REPAIR AUTHORITY FOR THIS PARENT-ENV DENY ONLY
```

Preserve:

```text
TEST COMPLETION AUTHORITY != RUNTIME REPAIR AUTHORITY
REVIEW FINDING != REPAIR AUTHORITY
AI PROPOSES != HUMAN DECIDES
```
