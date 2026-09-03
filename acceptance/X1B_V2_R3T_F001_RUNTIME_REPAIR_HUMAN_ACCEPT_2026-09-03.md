# X1B V2 — Human acceptance of R3T-F001 bounded runtime repair

Status: `HUMAN REPAIR AUTHORITY / EXACTLY ONE RUNTIME DEFECT`

Date: `2026-09-03`

Human response in controlling conversation:

```text
accept
```

Accepted finding:

```text
X1B-V2-R3T-F001 — FORBIDDEN PARENT GITHUB CREDENTIAL / PROXY ENVIRONMENT REACHES THE AUTHORITY-CHILD INVOCATION INSTEAD OF FAILING CLOSED = RUNTIME BLOCKER
```

Finding source:

```text
FJ899/8 PR #168
HEAD = 9bdf2453225e4bd9a26deca0f707e5249ea8cfe7
```

Exact ScriptOps state that exposed the defect:

```text
FJ899/scriptops PR #35
HEAD = e1f669bb02b16c5eec3c91faad5d25708fde8ed9
workflow run = 33800463714
job = 100798450352
first failing retained case = GITHUB_TOKEN
```

## Authorized repair

Human authorizes one bounded production-runtime repair for this defect only:

```text
phase6/x1b_human_decision.py
```

Required behavior: before the Human-authority network child is used, the parent must fail closed if any frozen forbidden credential/proxy environment variable is present and non-empty:

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

The already-added deterministic retained regression may remain and must pass after repair.

After this exact repair passes, the previously granted test/evidence-completion authority in FJ899/8 PR #167 resumes. If any later mandatory regression exposes a different production-runtime defect, STOP for separate Human repair authority.

## Explicit non-authority

This acceptance does not authorize:

```text
other production-runtime repairs
new X1B mechanism or scope
live executable screenplay decision evidence
Human screenplay approval
ScriptOps approve
prospective screenplay commit / refs/heads/main CAS
canonical screenplay effect
merge
X1B closure
V1 authority
release / deployment / tag
```

Preserve:

```text
TEST COMPLETION AUTHORITY != UNBOUNDED RUNTIME REPAIR AUTHORITY
REVIEW FINDING != REPAIR AUTHORITY
AI PROPOSES != HUMAN DECIDES
```
