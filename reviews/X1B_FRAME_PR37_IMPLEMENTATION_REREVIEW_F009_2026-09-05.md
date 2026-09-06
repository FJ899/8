# X1B-FRAME — PR #37 implementation re-review F009

Date: `2026-09-05`

## Review authority

Human authorization is recorded in `FJ899/8 PR #214` for exactly one independent read-only implementation re-review of:

```text
FJ899/scriptops PR #37
BASE = 2f22843ac570498b506101addeba5453ab777f08
HEAD = 99594940f18df99e68865835ce551fa983c07474
TREE = 7f4a4b722a65b8e97c8617b518309b4e29ed07fc
STATE = OPEN / DRAFT / UNMERGED
```

Review order was frozen as F008 first, then preserve F007 and F006, then continue the remaining PR #201 attacks until first credible counterexample or PASS.

## Prior findings re-attacked

### F008

`R14` now starts from the real correctly fenced `sources/ScriptOps_Main_Theme_Summary.md`, appends the exact forbidden Human-authorship promotion assertion, and requires the specific failure reason `publishes forbidden Human-authorship promotion`.

Disposition: `F008 CORRECTED NON-VACUOUSLY`.

### F007

`R12` starts from the real correctly fenced `SOURCES.md`, appends `ACCESS CHECK REQUIRED = CURRENT NEXT`, and requires the specific stale-current-next rejection reason.

Disposition: `F007 REGRESSION PRESERVED`.

### F006

Both recognized runtime profiles are accepted only through the same full `validate_runtime_profile()` path with `CURRENTNESS_UNESTABLISHED`; a V2 label over legacy blobs is explicitly rejected.

Disposition: `F006 REGRESSION PRESERVED`.

## Frozen attack continuation

The PR #201 independent-review matrix requires, among other attacks:

```text
Q1 is Layer-A enumeration exactly executable and exactly 13 on the frozen baseline?
Q2 can any nested file change Layer-A cardinality through recursion or special casing?
Q3 can a nested Markdown file outside allowed path prefixes evade fail-closed classification?
Q4 can a path-classed file self-promote despite registry/path denial?
```

Q1-Q3 are not falsified by the inspected implementation:

- Layer A is explicitly root `*.md` plus direct `sources/*.md`, non-recursive, with exact 13-member equality/cardinality checks.
- nested Markdown is enumerated separately and never added to the Layer-A census.
- unknown nested Markdown locations outside the allowed prefixes raise `UNCLASSIFIED_MARKDOWN_LOCATION`.

## First credible counterexample

`X1B-FRAME-F001-IMPLEMENTATION-F009 — LAYER-B PATH DENIAL IS NOT SEMANTIC NON-AUTHORITY ENFORCEMENT: A DOCUMENT UNDER AN ALLOWED LAYER-B PREFIX CAN SELF-PROMOTE WITH EQUIVALENT CURRENT-AUTHORITY WORDING THAT IS NOT ONE OF THE VERIFIER'S SMALL LITERAL POSITIVE_AUTHORITY_MARKERS, AND THE VERIFIER ACCEPTS IT.`

The relevant implementation behavior is:

```text
classify_nonregistry_markdown_path(path)
  known prefix -> DENIED_BY_PATH_CLASS

check_provenance_surfaces()
  for every Layer-B Markdown document:
    reject only if one of POSITIVE_AUTHORITY_MARKERS occurs literally
```

`POSITIVE_AUTHORITY_MARKERS` is a finite exact-string list such as:

```text
MERGE AUTHORITY = YES
DEPLOYMENT AUTHORITY = YES
RELEASE AUTHORITY = YES
V1 AUTHORITY = YES
CURRENT X1B AUTHORITY = YES
```

A path-classed document can therefore retain an allowed Layer-B location and publish semantically equivalent authority using wording outside that literal list, for example:

```text
THIS DOCUMENT IS THE CURRENT X1B AUTHORITY
```

or:

```text
MERGE IS AUTHORIZED BY THIS DOCUMENT
```

Neither sentence changes Layer-A cardinality, neither uses an unknown path prefix, and neither contains any currently forbidden literal marker. The document therefore remains accepted by the implemented verifier even though the frozen Q4 contract requires path denial to prevent self-promotion.

This is not merely a missing synthetic test. The implementation's production `check_provenance_surfaces()` uses the same incomplete literal allow/deny mechanism for every Layer-B Markdown document.

## Classification

`AUTHORITY-SEMANTICS BYPASS / LAYER-B SELF-PROMOTION FALSE NEGATIVE`

## Review disposition

```text
F008 = CORRECTED NON-VACUOUSLY
F007 = PRESERVED
F006 = PRESERVED
Q1-Q3 = NO COUNTEREXAMPLE FOUND
Q4 = FAIL
REVIEW = STOP AT FIRST CREDIBLE COUNTEREXAMPLE
```

No remaining frozen attacks are executed after F009.

## No mutation / no effect

No ScriptOps repair was performed. No PR #37 merge, PR #35 merge/rebase/cherry-pick, ScriptOps main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action was performed or authorized.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
FIRST CREDIBLE COUNTEREXAMPLE = DURABLE FINDING + STOP
IMPLEMENTATION CANDIDATE != MERGE AUTHORITY
AI PROPOSES != HUMAN DECIDES
```
