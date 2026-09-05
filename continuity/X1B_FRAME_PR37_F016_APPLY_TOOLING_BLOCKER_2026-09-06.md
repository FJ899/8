# X1B-FRAME PR37 F016 — APPLY TOOLING BLOCKER CHECKPOINT

Status: `F016 HUMAN-ACCEPTED / REPAIR PREPARED / REPAIR NOT APPLIED / PR #235 AUTHORITY UNCONSUMED`

Date: `2026-09-06`

## Durable authority

```text
FJ899/8 PR #235
HUMAN RESPONSE = accept
AUTHORIZED = exactly one bounded F016 replacement repair of FJ899/scriptops PR #37
```

## Exact still-live pre-repair target

```text
FJ899/scriptops PR #37
BASE = 2f22843ac570498b506101addeba5453ab777f08
HEAD = c85359755605c9ac2981ff7207fb5996f33ca29d
TREE = da6188644eaf83ea532fe7f005e14ddf1f108da2
VERIFIER BLOB = 8fe1250b04ff817f40e746a147d300896a69c007
STATE = OPEN / DRAFT / UNMERGED
```

`FJ899/scriptops refs/heads/main` remains:

```text
2f22843ac570498b506101addeba5453ab777f08
```

## Prepared F016 repair

A focused verifier-only repair was prepared and locally regression-checked.

Intended behavior:

```text
1. retain the existing fragment-local authority checks used to preserve F013/F014 negation boundaries;
2. add a normalized whole-line fallback so punctuation/parenthetical splitting cannot sever a self-referential subject from its positive authority predicate;
3. reject examples including:
   This file, therefore, grants release authority.
   This document, for clarity, authorizes merge.
   This file, however, grants canonical X1B authority.
4. preserve negative examples including:
   This file, however, does not grant release authority.
   This document, for clarity, does not authorize merge.
5. preserve F015 through F006 regressions.
```

Exact locally computed post-repair verifier Git blob SHA:

```text
d7153ccdf4469c7355e9b6aa0926228a91e74c00
```

Exact unified-diff SHA-256:

```text
064c80828833ffef86fa3a3a1be66f8a9522ede90d3a0faf6e740cf5e510aa03
```

## Tooling blocker

The available GitHub connector write operations in this session accept complete replacement file content rather than a unified patch or mounted local file. A transfer attempt returned a blob SHA that did not match the locally verified expected SHA; that blob was deliberately left unreferenced and was not used in any tree, commit, or ref update.

Observed mismatched unreferenced blob from the failed transfer path:

```text
2fbc7bcf58b27edacb7cd9607e18b7a6afaf0e93
```

Safety rule applied:

```text
TRANSFERRED BLOB SHA != EXPECTED BLOB SHA
=> DO NOT CREATE FINAL TREE
=> DO NOT CREATE FINAL REPLACEMENT COMMIT
=> DO NOT MOVE PR #37 REF
```

Therefore no F016 replacement candidate currently exists on the PR branch, and there is no F017 finding: no replacement candidate was executed or failed CI.

## Exact continuation contract

Resume only with a write path capable of applying the prepared patch or uploading the exact local file without transcription drift.

Before any ref movement, require:

```text
new verifier blob == d7153ccdf4469c7355e9b6aa0926228a91e74c00
```

Then:

```text
1. create a tree from old candidate TREE da618864... replacing only scripts/verify_repository.py;
2. inspect a temporary old-HEAD-parented commit/diff to prove only verifier changed;
3. create the final replacement commit with parent frozen BASE 2f22843...;
4. force-update only impl/x1b-frame-f001-two-layer-status-correction-20260905;
5. prove BASE->HEAD = ahead 1 / behind 0 and exactly twelve base-relative paths;
6. prove scriptops/main remains 2f22843...;
7. run Verify repository state and Phase 6 ScriptOps smoke on the exact new HEAD;
8. if CI passes, STOP before independent re-review; if CI fails, record a durable finding and STOP.
```

No additional Human repair authority is needed to resume this exact still-unconsumed F016 repair under PR #235. No re-review, merge, main movement, PR35 integration, deployment/release/tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority is granted.

Preserve:

```text
AI PROPOSES != HUMAN DECIDES
PREPARED PATCH != APPLIED REPAIR
UNREFERENCED BLOB != CANDIDATE
IMPLEMENTATION REPAIR AUTHORITY != RE-REVIEW AUTHORITY
PR HEAD != ACTIVE DEFAULT BRANCH
```
