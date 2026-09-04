# X1B V2 CORRECTIVE VERIFICATION RECOVERY RE-ANCHOR — HUMAN ACCEPT

Date: 2026-09-04

## Human act

The Human response in the controlling chat was exactly:

```text
accept
```

## Accepted recovery disposition

This acceptance is limited to recovery from the accidental evidence-repository main write that occurred during preparation of the X1B V2 corrective-verification positive-control decision evidence.

The Human accepts exactly the following disposition:

1. Re-anchor the evidence-repository execution state from the preregistered `FJ899/8 main = 1e4114e3f7ab6383af2549383b25329bed21eef9` to the recovered state:

```text
FJ899/8 main HEAD = 7c1d191f47b40728fa4c11b6e598afb0f8efe701
FJ899/8 main TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

2. Treat the accidentally materialized prior request as VOID and unusable for Human review, admission, effect, replay, or closure:

```text
request_nonce = 8f980004652b270e8d0092c438319d887fcd8ee32e9fa43adb39e5dd389e7a71
request_sha256 = 897b31ab05fc46688bfcf2e7b4e5eb280e1a220bd9cace613c91f6a82a103d5a
```

3. Keep the already frozen ScriptOps positive-control base unchanged:

```text
I  = 7c40a92165714023743e91c63b5b11b102fadd92
B0 = e325d3e6a347d684ec0b751bdb83098de6bdf87e
B0 TREE = e948b07d4d9fb3c629cdb43eda3d1579640c3fce
```

4. Generate exactly one fresh V2 decision request with a new 32-byte cryptographically secure nonce, bound to the same B0 / SCN-999 / candidate / impact / accepted-scene bytes.

5. Create one fresh non-draft, unmerged evidence PR in `FJ899/8` containing exactly two changed files:

```text
decisions/x1b/requests/<fresh-D>/request.json
decisions/x1b/requests/<fresh-D>/accepted-scene.fountain
```

6. Stop before the real Human GitHub review. No `approve`, admission, Git CAS, screenplay effect, push of an effect commit, merge, or X1B closure is authorized by this acceptance alone.

## Scope preservation

This recovery acceptance does not reopen the X1B design, implementation review, F001-F005 closure, hardware/platform scope, or the frozen ScriptOps implementation candidate. It changes only the evidence-repository execution anchor required after the accidental write/recovery sequence.

The recovered evidence tree is byte-identical to the preregistered evidence tree; the commit identity changed and is therefore explicitly re-anchored here rather than silently treated as equivalent.

```text
AI PROPOSES != HUMAN DECIDES
RECOVERY TREE EQUALITY != SILENT COMMIT-ID EQUIVALENCE
REVIEW FINDING != REPAIR AUTHORITY
```
