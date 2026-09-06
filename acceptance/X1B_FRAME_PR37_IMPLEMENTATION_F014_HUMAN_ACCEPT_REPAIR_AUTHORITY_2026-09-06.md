# X1B-FRAME PR37 — Human Acceptance of F014 and Bounded Repair Authority

Date: `2026-09-06`

Status: `HUMAN ACCEPTED / EXACTLY ONE BOUNDED REPAIR AUTHORIZED / NO EFFECT AUTHORITY`

## Human response

```text
accept
```

This response is bound only to the exact F014 finding recorded in `FJ899/8 PR #228`:

```text
FINDING = X1B-FRAME-F001-IMPLEMENTATION-F014
CLASS = NEGATION-SCOPE PUNCTUATION BYPASS / NON-COMMA CLAUSE-BOUNDARY FALSE NEGATIVE
```

Exact pre-repair ScriptOps target:

```text
FJ899/scriptops PR #37
BASE = 2f22843ac570498b506101addeba5453ab777f08
HEAD = d47b7525f3bcd8f36b1242d905ee60bef2a0514e
TREE = 4364cc9f787bcfcb9b9d9e3452ed407d66625a7f
STATE = OPEN / DRAFT / UNMERGED
COMMITS AHEAD = 1
CHANGED PATHS = 12
```

The Human acceptance authorizes exactly one replacement repair of PR #37 for F014.

## Repair boundary

The replacement candidate must remain:

```text
PARENT = frozen BASE 2f22843ac570498b506101addeba5453ab777f08
COMMITS AHEAD = exactly 1
CHANGED PATHS RELATIVE TO BASE = exactly the frozen twelve-path surface
```

Relative to the pre-repair HEAD `d47b7525f3bcd8f36b1242d905ee60bef2a0514e`, only:

```text
scripts/verify_repository.py
```

may change.

The bounded correction must:

1. prevent an earlier negation from masking a later positive Layer-B self-promotion across ordinary non-comma clause boundaries, including at least colon and dash-style boundaries;
2. preserve the F013 comma/asydetic fix;
3. preserve F012, F011, F010, F009 and the earlier F008/F007/F006 regressions;
4. add non-vacuous synthetic regression coverage for representative F014 colon and dash counterexamples through the same production validator;
5. avoid converting ordinary punctuation inside benign technical prose into a general authority false positive;
6. keep the verifier offline and preserve the frozen two-layer/currentness model.

If this one repair fails CI or produces a new credible defect, STOP and record a durable finding. No second repair is authorized by this acceptance.

## Authority boundary

This acceptance does not authorize:

```text
PR #37 merge
ScriptOps main movement
PR #35 merge/rebase/replacement
canonical effect
deployment
release
tag
active-product status promotion
X1B reopen
V1 authority
independent post-repair re-review
```

A successful repair and green CI remain candidate evidence only. A later independent re-review requires separate Human authorization.

```text
AI PROPOSES != HUMAN DECIDES
REPAIR AUTHORITY != REVIEW AUTHORITY
GREEN CI != MERGE AUTHORITY
PR HEAD != ACTIVE DEFAULT BRANCH
```