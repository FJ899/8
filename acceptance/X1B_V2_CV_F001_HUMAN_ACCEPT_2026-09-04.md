# X1B V2 corrective-verification F001 Human acceptance — 2026-09-04

## Human act

The Human response to the exact pending gate on `X1B-V2-CV-F001` was:

```text
accept
```

## Accepted finding

The Human accepts the bounded finding frozen in:

```text
FJ899/8 PR #174
HEAD = 1a85010cf693aafab9fb9dbce3be345d7ba73a5e
TREE = 2237777c46e2c74dd77342e59f5179dc4d2e7804
PATH = research/X1B_V2_CORRECTIVE_VERIFICATION_EXECUTION_SUBSTRATE_FINDING_2026-09-04.md
BLOB = eb405b7277df248fd545e95d2293e427b2b99082
```

Accepted finding:

```text
X1B-V2-CV-F001 — EXECUTION SUBSTRATE WAS A CODESPACE, NOT THE FROZEN READ-ONLY GITHUB ACTIONS EFFECT JOB = BLOCKER
```

The acceptance preserves the finding's scope classification:

- the local V2 Human-review / admission / CAS / durable-record / post-effect runtime result remains evidence of a successful local positive control;
- that result does not satisfy the exact preregistered corrective-verification procedure because the effect ran in a Codespace rather than the frozen read-only GitHub Actions effect job and did not obtain the required Actions artifact preservation;
- this is a verification-procedure / executor-substrate blocker, not a finding that the reviewed X1B Human-authorship runtime property itself failed.

## Bounded successor-verification authority

This Human act authorizes exactly one bounded successor corrective-verification attempt whose purpose is to close `X1B-V2-CV-F001` without reopening the reviewed runtime implementation.

The authorized successor may:

1. keep the exact reviewed ScriptOps implementation candidate:

```text
I = 7c40a92165714023743e91c63b5b11b102fadd92
FJ899/scriptops PR #35
```

2. reuse the already-frozen remote verification fixture base only if the successor packet independently verifies it remains exact and unchanged:

```text
B0 = e325d3e6a347d684ec0b751bdb83098de6bdf87e
parent(B0) = I
```

3. create a verification-only GitHub Actions harness/branch/PR as needed, provided it does not alter production runtime source or remote `scriptops/main`;
4. run the fresh complete deterministic negative matrix before any new effect;
5. generate a fresh request nonce and fresh request digest `D2`;
6. create one fresh two-file Human decision-evidence PR in `FJ899/8`;
7. request one fresh GitHub `APPROVED` review from trusted Human durable GitHub user ID `226907434`, bound to exact new evidence commit `H2` and exact `D2`;
8. after that Human review, execute exactly one real positive-control approval in a GitHub Actions job that proves:

```text
permissions: contents: read
checkout persist-credentials: false
no GitHub write credential in the ScriptOps effect process
no frozen credential/proxy authority input in the parent effect environment
```

9. observe the effect with `strace` as previously preregistered;
10. preserve the resulting local canonical commit and evidence with a Git bundle plus textual evidence uploaded as a GitHub Actions workflow artifact with an explicit retention period;
11. freeze the resulting verification evidence in `FJ899/8`;
12. if and only if the successor corrective verification passes, proceed to the already-required independent corrective-closure review.

## Freshness / replay rule

The prior successful Codespace request digest is consumed and must not be reused:

```text
D1 = 1f8d7fa4d4df2cac16853b273198f1146ce5cb6821e2d699badb0f7d3bdf7856
```

The successor must use a new random request nonce, a new request digest `D2`, a new evidence commit `H2`, and a new Human review.

The prior local effect commit:

```text
C1 = 05bef859c907a4f3ec8904f7cdc7db536f85f1a4
```

is historical verification evidence only. It is not remote deployment state and must not be used as the successor canonical base.

## Explicit non-authority

This Human acceptance does **not** authorize:

```text
merge of FJ899/scriptops PR #35
push of any verification effect to remote FJ899/scriptops main
merge of any Human decision-evidence PR
merge of a verification-only harness PR into product main
release / deployment / tag
runtime implementation changes outside a separately accepted new finding
reuse of D1 or the PR #173 Human review
X1B closure without an independent corrective-closure review and a later separate Human closure acceptance
V1 authority
```

If the successor exposes a new concrete runtime, authority, harness, or verification defect, execution authority terminates at that first credible blocker and the process returns to a new Human disposition gate.

## Governance

```text
AI PROPOSES != HUMAN DECIDES
REVIEW FINDING != REPAIR AUTHORITY
HUMAN DECISION EVIDENCE != MACHINE ADMISSION != EXECUTOR CAPABILITY
```

## Current state after this acceptance

```text
X1B-V2-CV-F001 = HUMAN ACCEPTED
ONE BOUNDED SUCCESSOR CORRECTIVE VERIFICATION = AUTHORIZED
REVIEWED RUNTIME IMPLEMENTATION CHANGE = NOT AUTHORIZED
REMOTE SCRIPTOPS MAIN EFFECT = NOT AUTHORIZED
X1B = OPEN
V1 AUTHORITY = NO
```
