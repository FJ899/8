# X1B-FRAME-F001-IMPLEMENTATION-F032

Date: 2026-09-06

Disposition: **CREDIBLE COUNTEREXAMPLE — STOP BEFORE REPAIR**

## Review binding

Independent post-repair review authorized by Human `accept` and durably recorded in `FJ899/8 PR #306`.

Exact reviewed candidate:

- repository: `FJ899/scriptops`
- PR: `#37`
- state: OPEN / DRAFT / UNMERGED
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `841ecbf18f346becb4baf4bb11a31eaf391975eb`
- TREE: `c127542b6aaac202ac4fa7a96a4026b76455efca`
- verifier blob: `5fb041541b4c80c00f94b8c32ec2a3aa96389864`
- exactly 1 commit over BASE
- exactly the frozen 12-path BASE-relative surface
- pre-review GitHub Actions: `Verify repository state` PASS; `Phase 6 ScriptOps smoke` PASS

## Required review order performed

1. F031 was re-attacked first. The repaired verifier correctly folds ordinary unindented / partially dedented / nested lazy paragraph continuation back into the owning list item and rejects the positive self-promotion.
2. F030 / F029 / F028 representative controls were re-attacked and remained preserved:
   - same-level cross-family/delimiter structural boundary remains separated;
   - ancestor-level structural sibling remains separated;
   - nested non-one ordered-looking lines that cannot interrupt the open item paragraph remain lazy continuation.
3. The review then continued to the next container-structure adversarial attack.

The candidate itself also contains and executes regressions F009-F031, and CI passed them at the exact reviewed HEAD. Green CI is evidence of preservation, not a substitute for this independent attack.

## F032 counterexample

Representative Markdown:

```markdown
> - This file contains background notes.
> - grants release authority.
```

### CommonMark structure

The unquoted content is a bullet list with two sibling list items. Under the CommonMark block-quote basic rule, prefixing each line with a block-quote marker produces a block quote containing those same blocks. Therefore the quoted document contains one block quote whose child is a bullet list with **two distinct sibling list items**:

1. `This file contains background notes.`
2. `grants release authority.`

The first item contains a self-reference but no authority promotion. The second item contains an authority-promotion phrase but no self-reference. They must not donate context to each other.

### Observed verifier behavior

The reviewed verifier recognizes list markers only when `_markdown_list_item_layout()` sees them at the beginning of the raw physical line. It does not peel or track block-quote container prefixes before list parsing.

For the exact counterexample above, independent execution of the reviewed parsing logic produced:

```text
units: ['> - This file contains background notes. > - grants release authority.']
claim: > - This file contains background notes. > - grants release authority.
```

Thus the two CommonMark sibling list items are collapsed into one logical authority unit. `_normalized_authority_line()` later removes `>` punctuation, so the collapsed unit contains both `THIS FILE` and `GRANTS ... AUTHORITY`. `layer_b_self_promotion_claim()` therefore reports a forbidden self-promotion.

This is a **false positive / structural context-donation bug**: a benign block-quoted list of two sibling items is rejected as if one item self-promoted.

## Why this is distinct from F020-F031

F020-F031 harden list-item ownership, paragraph interruption, indentation, marker validity, and sibling/ancestor boundaries **only for list syntax visible at the raw line start after indentation**. F032 composes the same authority-boundary problem with the other CommonMark container type: block quotes.

The current parser models list-item container paths but not block-quote container prefixes. Therefore the earlier list boundary guarantees do not survive ordinary CommonMark container composition.

## Security/correctness impact

Layer-B validation is intended to classify logical Markdown authority units rather than arbitrary physical lines. A valid supporting document can contain quoted list examples, quoted historical material, or quoted provenance where a self-reference in one sibling item and an authority phrase in another sibling item are semantically separate. The verifier currently merges them and rejects the document.

This is credible because it is caused by a generic parser-model gap, not a literal-string edge case. Equivalent variants include nested block quotes, ordered sibling lists inside quotes, and mixed quote/list container compositions.

## Stop rule

This is the first credible counterexample found after the required F031 re-attack and regression-preservation checks.

Per the Human-authorized review contract:

- **STOP review here**;
- no repair during review;
- no mutation of `FJ899/scriptops PR #37`;
- no merge of PR #37 or PR #35;
- no ScriptOps main movement;
- no deploy/release/tag;
- no canonical effect;
- no active-product status promotion;
- no X1B reopen;
- no V1.

Any F032 repair requires a fresh explicit Human gate.

`F032 FINDING != REPAIR AUTHORITY`
