# X1B-FRAME — PR #37 F043 bounded repair completion

Date: 2026-09-07

## Disposition

`F043 = BOUNDED REPAIR COMPLETE / VERIFIED GREEN`

This record freezes completion evidence for the Human-authorized F043-only repair of `FJ899/scriptops PR #37`. It does not authorize a new review, F042 repair, F044 repair, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1 action.

## Exact repaired candidate

```text
REPO = FJ899/scriptops
PR = #37
BASE = 2f22843ac570498b506101addeba5453ab777f08
HEAD = 3521a6c9f9c0db1103c49274d979766de1abfefa
TREE = 6d2a5dbcceb5fd41f9988ef63d64c77bba45b8c1
COMMITS_AHEAD_OF_BASE = 1
CHANGED_PATHS = 13
```

The replacement commit has the exact frozen BASE as parent. PR #37 remains open, draft, unmerged, and one commit ahead of that BASE.

## Verifier binding

```text
scripts/verify_repository.py
BLOB = 61bf107ad59da33a6576032d341b41c538d0453a

scripts/verify_repository_f041_core.py
BLOB = be645c1a3ee49a04d700a3ef7fde86a92e413a14
```

The F041 verifier is retained byte-for-byte as the pinned core. The F043 entrypoint runtime-checks that exact core blob SHA before invoking it. The overlay replaces only the authority-unit parser seam needed for F043 and then runs the complete frozen regression matrix before its F043 additions.

## F043 repaired semantics

The bounded repair adds CommonMark link-reference-definition recognition/extraction with the following security properties:

1. A valid definition at the beginning of a paragraph candidate is extracted from the following paragraph authority unit.
2. Up to three columns of leading indentation remain valid at top level.
3. Consecutive definitions remain definitions without requiring a blank line.
4. A link-reference definition cannot interrupt an already-open paragraph; such syntax remains paragraph text in that state.
5. List-item definitions are resolved relative to the owning item content container instead of absolute source indentation.
6. Fresh quoted definitions are extracted within their quote container.
7. Definition metadata remains security-relevant as its own unit and cannot hide a self-promotion inside the label/title/destination text.
8. F042 and F044 behavior is deliberately not repaired or reinterpreted by this change.

## Preservation / scope audit

The candidate tree was constructed from the exact frozen pre-repair tree `425683ac0db4e1811f57ef10c5b9f75050846b55`.

All top-level tree entries outside `scripts/` remain byte-identical to that frozen tree. Inside `scripts/`, `restore_v2.py` remains byte-identical. The only F043-specific tree changes relative to the frozen pre-repair candidate are:

- `scripts/verify_repository.py` — bounded F043 overlay;
- `scripts/verify_repository_f041_core.py` — byte-identical retained copy of the frozen F041 verifier blob.

No runtime implementation, tests directory, workflow, restore mechanism, acceptance artifact, canonical data, or deployment surface was modified for the repair.

## Pre-push bounded validation

A focused parser-state harness covered F043 representatives plus neighboring F019/F020/F031/F035/F041 invariants. Result:

```text
F043/neighbor focused matrix = PASS 19/19
python py_compile overlay = PASS
```

The known-outstanding oracle representatives remained unrepaired before push:

```text
F042 quote tab-stop/source-column representative = still current miss
F044 nested/nonrecursive quote representative = still current miss
```

This confirmed the Human-authorized F043-only scope was not expanded into F042/F044.

## First replacement attempt and correction

The first replacement candidate was:

```text
HEAD = ab1ff16fd583a35c802e6552aab28d1f47fcdd26
```

Both workflows failed at the repository verifier because one newly added F043 fixture encoded two backslashes rather than the intended single escaped closing bracket. The logs showed that all frozen R1-R24 and F009-F041 regressions had already passed before the fixture failure.

That fixture-only mistake was corrected without changing the repair semantics. A new replacement commit was created directly over the same frozen BASE, preserving the one-commit topology.

## Required workflow evidence on final HEAD

Exact final HEAD: `3521a6c9f9c0db1103c49274d979766de1abfefa`

### Verify repository state

```text
RUN_ID = 34090111008
RUN_NUMBER = 163
CONCLUSION = success
VERIFY_SELF_CONTAINED_STATE = success
```

The run executes the full frozen R1-R24 / F009-F041 matrix and the new F043 regression matrix through the real `scripts/verify_repository.py` entrypoint.

### Phase 6 ScriptOps smoke

```text
RUN_ID = 34090111022
RUN_NUMBER = 109
CONCLUSION = success
REPOSITORY_SEMANTIC_CURRENTNESS_VERIFIER = success
FULL_DETERMINISTIC_PHASE6_REGRESSION = success
```

The smoke workflow therefore reached and passed the full deterministic Phase-6 regression after the repaired verifier passed.

## Current unresolved findings

The post-F041 batch review findings remain partitioned as follows:

```text
F042 = OPEN / UNREPAIRED
F043 = REPAIRED / GREEN
F044 = OPEN / UNREPAIRED
```

F042 concerns block-quote tab-stop/source-column loss. F044 concerns nonrecursive quote-content block parsing/laziness. This completion record grants no authority to repair either finding.

## Authority boundary / STOP

```text
REPAIR COMPLETE != REVIEW AUTHORITY
GREEN CI != MERGE AUTHORITY
PR HEAD != ACTIVE DEFAULT BRANCH
CURRENTNESS_UNESTABLISHED != FALSE
CURRENTNESS_UNESTABLISHED != TRUE
```

STOP before any next review-mode transition. A later independent/adversarial review of the repaired F043 candidate requires separate Human authority bound to the exact new HEAD/TREE/verifier identities. No merge or other consequential effect is authorized by this record.
