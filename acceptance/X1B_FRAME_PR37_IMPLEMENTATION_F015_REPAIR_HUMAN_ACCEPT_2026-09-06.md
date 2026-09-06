# X1B-FRAME PR #37 — Human acceptance of F015 and bounded repair authority

Date: `2026-09-06`

## Human response

```text
accept
```

This records Human acceptance of exactly the implementation-review finding in:

```text
FJ899/8 PR #231
FINDING = X1B-FRAME-F001-IMPLEMENTATION-F015
CLASSIFICATION = F014 REPAIR INCOMPLETE / NEGATION-SCOPE DELIMITER BYPASS / FALSE NEGATIVE
```

The accepted counterexample is:

```text
This document does not authorize merge (this file grants canonical X1B authority).
```

The accepted finding is that the current Layer-B self-promotion validator can allow a later positive self-promotion to inherit an earlier negation when a new self-referential authority clause is embedded through a delimiter that the clause splitter does not enumerate. Parentheses are the demonstrated case.

## Exact repair target

```text
REPOSITORY = FJ899/scriptops
PR = #37
BASE = 2f22843ac570498b506101addeba5453ab777f08
PRE-REPAIR HEAD = 2fab77397cceda52725c86f3c7f4ea071174d5b0
PRE-REPAIR TREE = b18df96e569c1b61065c4389dc143e7bd5db5e16
STATE = OPEN / DRAFT / UNMERGED
COMMITS = 1
BASE-RELATIVE CHANGED PATHS = 12
```

## Authorized action

Exactly one bounded replacement repair of PR #37 is authorized, exclusively to correct F015.

Mandatory bounds:

```text
1. Parent remains the frozen BASE 2f22843ac570498b506101addeba5453ab777f08.
2. Final PR #37 remains exactly one commit ahead / zero behind the frozen BASE.
3. Base-relative changed paths remain exactly the frozen twelve-path implementation surface from plan PR #201.
4. Relative to PRE-REPAIR HEAD, only scripts/verify_repository.py may change.
5. The repair must preserve the F014/F013/F012/F011/F010/F009 protections and the earlier F008/F007/F006 protections.
6. The repair must not merely add one literal parenthesis counterexample to a finite allow/deny phrase list. Negation scope must reset structurally when a later independent self-reference introduces a new authority-promotion subject, so unenumerated delimiters cannot let the earlier negation mask that later promotion.
7. Positive self-promotion such as a later `this file grants ...` or equivalent independent self-reference must remain rejected even when preceded by a negated claim about another self-reference.
8. Legitimate single-subject negations such as `This document does not itself authorize ...` and benign inert technical `binding` wording must remain accepted.
9. Non-vacuous regressions must include the exact F015 parenthetical counterexample plus at least one delimiter-independent new-self-reference masking case and benign negated controls through the production validator.
10. Existing repository verification and Phase-6 regression must be executed on the replacement HEAD.
```

If verification fails, no second repair is authorized. Record the next durable finding and STOP.

If verification succeeds, the repair authority is exhausted. Any independent post-repair re-review requires a separate Human authorization.

## Explicit non-authority

This acceptance does not authorize:

```text
merge
FJ899/scriptops main movement
PR #35 integration/rebase/merge
deployment
release
tag
canonical effect
active-product status promotion
X1B reopen
V1 authority
post-repair independent re-review
```

Preserve:

```text
AI PROPOSES != HUMAN DECIDES
REPAIR AUTHORITY != REVIEW AUTHORITY
IMPLEMENTATION CANDIDATE != MERGE AUTHORITY
CURRENTNESS_UNESTABLISHED != FALSE
CURRENTNESS_UNESTABLISHED != TRUE
PR HEAD != ACTIVE DEFAULT BRANCH
```
