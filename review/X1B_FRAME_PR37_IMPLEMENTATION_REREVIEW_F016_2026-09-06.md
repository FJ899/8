# X1B-FRAME PR37 Implementation Re-review — F016

Date: `2026-09-06`

Status: `INDEPENDENT READ-ONLY RE-REVIEW / FAIL / STOP`

## Exact review target

```text
REPO = FJ899/scriptops
PR = #37
BASE = 2f22843ac570498b506101addeba5453ab777f08
HEAD = c85359755605c9ac2981ff7207fb5996f33ca29d
TREE = da6188644eaf83ea532fe7f005e14ddf1f108da2
VERIFIER PATH = scripts/verify_repository.py
VERIFIER BLOB = 8fe1250b04ff817f40e746a147d300896a69c007
STATE = OPEN / DRAFT / UNMERGED
```

Human re-review authority:

```text
FJ899/8 PR #233
HEAD = 72ac2b5cfad071f6eb1b7f36e10b14759a61f881
```

Governing frozen plan/review:

```text
FJ899/8 PR #201 = superseding two-layer census plan
FJ899/8 PR #202 = independent plan-review PASS
```

## Finding

```text
X1B-FRAME-F001-IMPLEMENTATION-F016 — THE AUTHORITY CLAUSE SPLITTER CAN SEVER A SELF-REFERENTIAL GRAMMATICAL SUBJECT FROM ITS POSITIVE AUTHORITY PREDICATE: A COMMA-DELIMITED PARENTHETICAL CAUSES `THIS FILE` AND `GRANTS RELEASE AUTHORITY` TO BE CHECKED IN DIFFERENT FRAGMENTS, SO EXPLICIT LAYER-B SELF-PROMOTION PASSES.
```

Classification:

```text
F015 REPAIR INCOMPLETE / AUTHORITY-PARSER FRAGMENTATION / FALSE NEGATIVE
```

## First credible counterexample

```text
This file, therefore, grants release authority.
```

This is an unambiguously positive self-promotion claim by a Layer-B document. It uses terms already inside the verifier's own grammar:

```text
self-reference = THIS FILE
promotion = GRANTS + AUTHORITY
```

It is not one of the verifier's exact `POSITIVE_AUTHORITY_MARKERS`.

## Why the current verifier accepts it

Current `_authority_clauses()` splits every comma before self-reference/promotion conjunction is evaluated.

The counterexample becomes effectively:

```text
THIS FILE
THEREFORE
GRANTS RELEASE AUTHORITY
```

`layer_b_self_promotion_claim()` then checks each fragment independently and only rejects a fragment when both are true inside that same fragment:

```text
self_referential == TRUE
AND
promotion == TRUE
```

For the three fragments:

```text
THIS FILE                 -> self_reference YES / promotion NO
THEREFORE                 -> self_reference NO  / promotion NO
GRANTS RELEASE AUTHORITY  -> self_reference NO  / promotion YES
```

Therefore no fragment satisfies the rejection conjunction and the function returns no self-promotion claim.

The exact-marker fallback also does not reject this sentence because `GRANTS RELEASE AUTHORITY` is not equal to any `POSITIVE_AUTHORITY_MARKER` such as `RELEASE AUTHORITY = YES`.

This is not a punctuation-only cosmetic issue. The parser has separated a grammatical subject from its predicate and thereby destroyed the semantic relation the validator is intended to detect.

## Relation to F015

F015 repaired one class of negation masking by identifying later independent self-reference subjects inside a normalized fragment. That repair does not help when `_authority_clauses()` has already split the subject away from the promotion predicate.

Thus F015 is not sufficient to establish Layer-B semantic non-authority enforcement.

## Frozen-review disposition

This was the first credible counterexample in the ordered post-F015 re-review.

Per frozen rule:

```text
FIRST CREDIBLE COUNTEREXAMPLE = DURABLE FINDING + STOP
```

Therefore:

```text
F015 RE-ATTACK = FAIL / F016
F014-F006 = NOT CONTINUED
Q5-Q15 = NOT CONTINUED
REVIEW PASS = NO
STOP = YES
```

No ScriptOps mutation was performed during this re-review.

## Authority boundary

This finding does not authorize:

```text
repair
merge
main movement
PR #35 integration
deployment
release
tag
canonical effect
active-product status promotion
X1B reopen
V1 authority
```

Next legal stage is Human acceptance or rejection of exact F016. Only a separate Human acceptance may authorize any bounded repair.

`FINDING != REPAIR AUTHORITY`
`AI PROPOSES != HUMAN DECIDES`
