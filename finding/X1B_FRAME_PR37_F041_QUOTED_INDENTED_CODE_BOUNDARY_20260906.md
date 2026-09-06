# X1B-FRAME-F001-IMPLEMENTATION-F041

## Title

Quoted indented-code leaf boundary omission

## Review authority

- Human post-F040 independent-review authority: `FJ899/8 PR #365`
- F040 repair completion: `FJ899/8 PR #364`

## Exact reviewed candidate

- repository: `FJ899/scriptops`
- PR: `#37`
- state at review: OPEN / DRAFT / UNMERGED
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `a504b33e0420d3ac487a1d69aeddebc6719dcd62`
- TREE: `590da6890ba88334aeec59a908eacb52adbade5c`
- verifier blob: `b4df7351df142d20507aab2eff4ae2991ddc9acb`

## Disposition

`FAIL — FIRST CREDIBLE COUNTEREXAMPLE`

The independent review re-attacked F040 first and stopped at this counterexample before proceeding to link-reference definitions or any later frozen frontier.

## Representative

```markdown
>     This file
> grants release authority.
```

## Normative CommonMark basis

CommonMark 0.31.2 §4.4 says that an indented code block ends immediately when a nonblank line has fewer than four columns of indentation, and a paragraph may follow immediately without a blank line.

CommonMark 0.31.2 block-quote Example 252 establishes that an indented code block inside a block quote requires five spaces after `>`: the quote marker consumes `>` plus one following indentation space, leaving four columns for indented code.

Therefore the representative contains, inside one block-quote container:

1. an indented-code leaf whose literal payload is `This file`; then
2. a distinct paragraph leaf whose text is `grants release authority.`

Those leaves are not one paragraph/security unit merely because they share the same outer block-quote container.

## Current verifier behavior

The repaired verifier has explicit top-level/list `indented_code_active` state, but its block-quote path remains coarse-grained. `block_quote_parts` aggregates consecutive explicit quote lines into one authority unit. When `block_quote_parts` is already nonempty and the next line has a valid quote marker, the verifier appends that line directly and continues; it does not track an indented-code leaf state inside the quote container or reprocess a quoted dedent as a new quoted block.

For the representative:

- first line `>     This file` is recognized only as quote content and stored in `block_quote_parts`;
- second line `> grants release authority.` is appended to the same `block_quote_parts`;
- the emitted unit therefore contains both `This file` and `grants release authority.`;
- the Layer-B self-promotion detector rejects the synthesized combined claim.

That is a security false positive relative to the CommonMark block structure: the self-reference is confined to the quoted indented-code leaf and the promotion phrase is in a separate quoted paragraph leaf.

## Why existing F040 coverage does not close this

The F040 regression matrix includes:

- top-level indented-code boundary behavior;
- top-level non-interruption;
- list-owned indented code;
- quoted indented-code payload kept within quote context;
- quoted open-paragraph non-interruption.

But it does not cover a quoted indented-code leaf followed immediately by a dedented quoted paragraph. The existing quote aggregation therefore preserves quote-container identity while losing the required leaf boundary inside that container.

## Required preservation constraints for any later repair

A future repair, if separately Human-authorized, must at minimum preserve:

- all F009-F040 regressions;
- quoted ordinary-paragraph laziness from F035;
- F040 rule that indented code cannot interrupt an open paragraph;
- quoted indented-code literal payload handling;
- exact quote-container ownership;
- dedented explicit quote text after quoted indented code must end the code leaf and be reprocessed as a new quoted block/paragraph without escaping the quote container;
- no generic Markdown parser expansion beyond the bounded block-boundary need.

## Stop condition

No repair was performed during this review. No merge, ScriptOps main movement, PR #35 merge, deploy, release, tag, canonical effect, active-product status promotion, X1B reopen, V1 action, or evidence-main movement is authorized by this finding.
