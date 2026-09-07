# X1B-FRAME — post-F043 adversarial review finding

Date: 2026-09-07

## Exact reviewed candidate

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `3521a6c9f9c0db1103c49274d979766de1abfefa`
- TREE: `6d2a5dbcceb5fd41f9988ef63d64c77bba45b8c1`
- verifier overlay blob: `61bf107ad59da33a6576032d341b41c538d0453a`
- pinned frozen F041 core blob: `be645c1a3ee49a04d700a3ef7fde86a92e413a14`
- review authority: `FJ899/8 PR #374`

## Disposition

`FAIL — FIRST CREDIBLE COUNTEREXAMPLE`

The review re-attacked F043 first and stopped at the first credible counterexample, as authorized. No repair was performed.

Known findings F042 and F044 remain `OPEN / UNREPAIRED`; they were not reclassified or repaired by this review.

## Finding — F043 multiline link-reference-definition extraction remains incomplete

Finding id: `X1B-FRAME-F001-IMPLEMENTATION-F043-MULTILINE`

Representative:

```markdown
[
This file
]: /url
grants release authority.
```

### CommonMark semantics

CommonMark 0.31.2 §4.7 permits link reference definitions to span physical lines. The grammar allows line endings around destination/title, and normative Example 208 shows a link label itself spanning multiple lines:

```markdown
[
foo
]: /url
bar
```

That input contains one link reference definition followed by a paragraph containing only `bar`.

The same semantics apply to the review representative: the first three physical lines are one link reference definition; `grants release authority.` is the following paragraph.

Under the candidate's conservative security policy, definition metadata may remain security-relevant as its own authority unit. Even then, the definition unit contains the self-reference but no promotion, while the following paragraph contains the promotion but no self-reference. They must not be fused into one self-promotion claim.

### Current verifier behavior

The F043 recognizer `_markdown_link_reference_definition_layout(raw_line, ...)` accepts exactly one physical `raw_line`. It therefore cannot recognize a definition whose label, destination, or title continues across physical lines.

At top level, definition extraction is attempted only against the current physical line while `paragraph` is empty. For the representative:

1. `[` is not recognized as a complete definition and starts an ordinary paragraph candidate;
2. `This file` is appended to that paragraph;
3. `]: /url` is appended to that paragraph;
4. `grants release authority.` is appended to the same paragraph.

The emitted authority unit is therefore equivalent to:

```text
[ This file ]: /url grants release authority.
```

The frozen self-promotion validator sees both `THIS FILE` and a positive release-authority promotion in that single unit and rejects it.

This is a **false positive** caused by incomplete CommonMark §4.7 extraction, not a new F042/F044 mechanism.

### Same-root-cause family

The same single-line recognizer is also incomplete for other normative §4.7 multiline forms, including:

- line ending between `:` and destination (CommonMark Example 193/198);
- title on a following physical line (Examples 193, 195, 217);
- multiline title without a blank line (Example 196).

These variants were not pursued further because the authorized review stops at the first credible counterexample.

## Review boundary

No change was made to `FJ899/scriptops`.

No repair, merge, ScriptOps `main` movement, deploy/release/tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority was performed or inferred.

`REVIEW FINDING != REPAIR AUTHORITY`
