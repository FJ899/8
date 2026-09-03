# X1B FINAL2 — Human Acceptance of F005

Status: `HUMAN-AUTHORIZED DURABLE ACCEPTANCE FREEZE`

Date: `2026-09-03`

## 1. Human decision

The Human replied exactly:

```text
accept
```

to the independent AK-CANON review frozen in:

```text
FJ899/8 PR #156
TITLE = X1B: independent AK-CANON review of bounded F001-F004 reopen
HEAD = a3bd7d653e96ccb19bb2952f1ecf2542f6664742
TREE = 593a09a135116e4f7630e1d839c2dfb9bce584b6
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_FINAL_BOUNDED_REOPEN_F001_F004_AK_CANON_REVIEW.md
BLOB = c7f5f10516dba5b3909336bdb5816165b0306c7d
VERDICT = AK-CANON X1B FINAL BOUNDED REOPEN F001-F004 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

## 2. Accepted finding

```text
X1B-FINAL2-IBR-F005 — CALLER-CONTROLLED TLS CA ENVIRONMENT CAN REPLACE THE DECLARED OS TRUST STORE = BLOCKER
```

The accepted scope classification is:

```text
CORE X1B / TRUSTED HUMAN ORIGIN / SELECTED GITHUB HTTPS MECHANISM
```

The Human acceptance also preserves the review disposition that:

```text
F001 = MATERIALLY CLOSED AT BRIEF LEVEL
F002 = MATERIALLY CLOSED AT BRIEF LEVEL
F003 = MATERIALLY CLOSED AT BRIEF LEVEL
F004 = MATERIALLY CLOSED AT BRIEF LEVEL
CONVERGENCE STRATEGY = STILL VALID
R4R17 PHYSICAL-PLATFORM LINEAGE = STILL OUT OF SCOPE
```

## 3. Authorized repair scope

This acceptance authorizes exactly one successor planning artifact that may change only what is necessary to close F005 while preserving PR #155 semantics for F001-F004.

The successor may freeze a caller-independent TLS trust configuration for `GitHubDecisionReaderV2`, including deterministic rejection and/or neutralization of documented process-environment inputs that can select a non-OS CA database.

The successor must not reopen or add requirements for:

```text
TPM/EK/AK
vendor CRLs
PMEM/NFIT
bare-metal locality
BMC console origin
universal power-loss durability
hostile kernel/filesystem/Git binary
compromised trusted Human account
```

## 4. Explicit non-authority

This acceptance does not authorize:

```text
ScriptOps source mutation
implementation candidate
CODEOWNERS/ruleset mutation
live X1B decision-evidence PR
Human live V2 approval
positive control
canonical screenplay effect
merge
X1B corrective closure
Agency Kernel V1
release
deployment
tag
```

After one F005-only successor brief is durably frozen:

```text
STOP
NEXT LEGAL STAGE = ONE SEPARATELY HUMAN-AUTHORIZED INDEPENDENT AK-CANON REVIEW OF THAT EXACT SUCCESSOR BRIEF
```

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
HUMAN ACCEPTANCE OF F005 = F005-ONLY BRIEF-REPAIR AUTHORITY
F005 REPAIR != IMPLEMENTATION AUTHORITY
AI PROPOSES != HUMAN DECIDES
```
