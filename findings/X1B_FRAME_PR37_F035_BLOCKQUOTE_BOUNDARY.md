# X1B-FRAME-F001-IMPLEMENTATION-F035 — block-quote paragraph-interruption boundary

Date: 2026-09-06

Independent post-F034 adversarial review authority: `FJ899/8 PR #324`.
F034 repair completion evidence: `FJ899/8 PR #323`.

## Exact reviewed candidate

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `74e11cdf52a8a0857d727030b6a6f44e40127b1b`
- TREE: `260a7d09077af0fafdb679a41e124ac87f02cdfa`
- verifier blob: `4e51a52af9e0f7c579f13a5faca804a9caaf912b`
- PR state at review: OPEN / DRAFT / UNMERGED
- topology: exactly one commit over BASE; frozen 12-path BASE-relative surface
- authoritative workflows on exact HEAD: `Verify repository state` run `34046736199` success; `Phase 6 ScriptOps smoke` run `34046736226` success

## Required re-attack/preservation before continuing

F034 was re-attacked first. The exact repaired verifier recognizes 1–6-hash ATX openings with at most three leading columns, separates top-level headings from the preceding paragraph, closes a list when a top-level heading appears, preserves owned headings inside their list-item security context, and includes positive/negative F034 regression shapes. F033/F032/F031/F030/F029 and prior regressions remain present on the exact verifier and the full exact-HEAD verifier workflow is green.

## First credible counterexample after F034

Representative Markdown:

```markdown
This file
> grants release authority.
```

CommonMark 0.31.2 block-quote rules explicitly permit a block quote to interrupt an ordinary paragraph without a blank line (Example 245 has the shape `foo` followed immediately by `> bar`, producing a paragraph and then a block quote).

Expected security-unit structure for the representative input:

1. ordinary paragraph: `This file`
2. distinct block quote containing paragraph: `grants release authority.`

The second block must not inherit the first paragraph's self-reference merely because there is no blank line.

## Exact verifier failure mechanism

In `_authority_soft_wrapped_units()` on the reviewed verifier:

- F034 handles ATX headings;
- F032/F033 handle thematic breaks;
- list-item parsing handles list boundaries;
- there is no block-quote opener/container handling before the generic paragraph fallback;
- with no active list, every remaining nonblank line is appended to the same `paragraph` list.

Therefore the representative input is folded into one synthetic authority unit equivalent to:

```text
This file > grants release authority.
```

`_authority_clauses()` does not split on `>`, while `_normalized_authority_line()` removes `>` as punctuation. The normalized whole becomes equivalent to:

```text
THIS FILE GRANTS RELEASE AUTHORITY
```

That creates a false self-promotion claim even though CommonMark places the self-reference and authority phrase in separate blocks.

This is a credible structural-boundary counterexample of the same authority-unit class previously exercised by F032–F034, but it is not covered by those repairs.

## Disposition

`FAIL — FIRST CREDIBLE COUNTEREXAMPLE`

Assign finding ID: `X1B-FRAME-F001-IMPLEMENTATION-F035`.

Immediate STOP before repair. This finding grants no repair authority and no merge of PR #37 or PR #35, ScriptOps main movement, deploy/release/tag, canonical effect, active-product status promotion, X1B reopen, or V1.
