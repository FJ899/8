# X1B-FRAME PR #37 — POST-F041 BATCHED ADVERSARIAL REVIEW FINDINGS

Date: 2026-09-06
Disposition: **FAIL — BATCH COMPLETED / THREE CREDIBLE ROOT-CAUSE FINDINGS**

## Exact review binding

Repository: `FJ899/scriptops`
PR: `#37`
State at fresh read: OPEN / DRAFT / UNMERGED

- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `6579dbccb2dbccc54875d51f377ce1c574e4bce6`
- TREE: `425683ac0db4e1811f57ef10c5b9f75050846b55`
- verifier: `scripts/verify_repository.py`
- verifier blob: `be645c1a3ee49a04d700a3ef7fde86a92e413a14`
- one commit over frozen BASE
- frozen BASE-relative surface: 12 paths

Human batch-review authority: `FJ899/8 PR #371`.
F041 completion evidence: `FJ899/8 PR #370`.

No ScriptOps write, repair, merge, main movement, deploy/release/tag, canonical effect, status promotion, X1B reopen, or V1 action occurred during this review.

## Review method

The authorized batch was completed instead of stopping at the first counterexample. It covered:

1. F041 re-attack and F040 preservation;
2. quoted indented-code threshold and tab-stop cases;
3. nested and explicit block-quote internal block boundaries;
4. list/quote ownership controls;
5. CommonMark 0.31.2 §4.7 link reference definitions, including paragraph interruption/non-interruption and container implications;
6. blank, dedent, and EOF controls around those structures.

Normative reference: CommonMark 0.31.2, especially §2.2 Tabs, §4.4 Indented code blocks, §4.7 Link reference definitions, §4.8 Paragraphs, and §5.1 Block quotes.

## Preserved controls — PASS

The repaired F041 representative remains correctly separated:

```markdown
>     This file
> grants release authority.
```

The first line is quoted indented code; the second is a dedented quoted paragraph. The current F041 state flushes the code leaf before starting the paragraph.

The following existing security controls remain conceptually preserved by the inspected code and by the completed repository verifier/workflow regression:

```markdown
>     This file
>     grants release authority.
```

Both lines remain in one quoted code leaf and therefore remain one security unit.

```markdown
> This file
>     grants release authority.
```

Indented code cannot interrupt an already-open quoted paragraph, so this remains one quoted paragraph/security unit and must reject.

```markdown
    This file
grants release authority.
```

Top-level F040 code dedent remains a real leaf boundary.

## F042 — block-quote tab-stop column reset permits a false negative

Finding id: `X1B-FRAME-F001-IMPLEMENTATION-F042`

Representative input, where `\t` denotes one literal tab:

```text
> \tThis file
> grants release authority.
```

### CommonMark semantics

CommonMark §2.2 states that tabs behave as tab-stop-aware indentation in block-structure contexts. §5.1 defines a block-quote marker as `>` plus a following space of indentation when present.

For the first line above, the literal space after `>` belongs to the quote marker. The following tab is therefore evaluated at its original source column, not from column zero. At this position it contributes only two content-indentation columns. The content is therefore an ordinary quoted paragraph line, not quoted indented code. The second quoted line is paragraph continuation. The semantic result is one quoted paragraph containing both `This file` and `grants release authority.` and it must be rejected as self-promotion.

### Current verifier behavior

`_markdown_block_quote_layout()` strips all leading container indentation, removes `>`, then removes one following space/tab character and returns only the remaining string. `_markdown_leading_columns()` is subsequently run on that detached string.

For `> <space><tab>This file`, the detached content begins with a tab at synthetic column zero, so the verifier counts it as four columns and sets `block_quote_indented_code = True`. F041 then flushes the first line as a code leaf when the next quoted line dedents. The self-reference and promotion land in separate authority units, so the forbidden claim is missed.

This is a **false negative / security bypass**, not merely an over-conservative rejection.

Controls:

- `>\tThis file` remains non-code under both normative and current parsing after the quote marker consumes part of the tab expansion.
- `>\t\tThis file` remains quoted indented code under both.
- the defect is specifically loss of original tab-stop column context after quote-marker normalization.

Root cause: quote-marker normalization destroys source-column information before indentation classification.

## F043 — link-reference-definition boundary omission creates false joins

Finding id: `X1B-FRAME-F001-IMPLEMENTATION-F043`

Representative:

```markdown
[This file]: /url
grants release authority.
```

### CommonMark semantics

CommonMark §4.7 parses a valid link reference definition from the beginning of a paragraph candidate and removes that definition from the paragraph content. A definition may be followed directly by ordinary paragraph text without a blank line. The definition itself does not interrupt an already-open paragraph, but when it occurs at the beginning it is extracted before the remaining paragraph is formed.

Thus this input has a link reference definition followed by a paragraph whose visible/content text is only `grants release authority.`. Even under a conservative security policy where definition metadata remains security-relevant, the definition and following paragraph are distinct security units: the definition has the self-reference but no promotion; the paragraph has the promotion but no self-reference.

### Current verifier behavior

The exact verifier contains no link-reference-definition recognizer in its Markdown block precedence path. There is no §4.7 extraction step. Both nonblank lines fall through to ordinary paragraph accumulation, producing one authority unit equivalent to:

```text
[This file]: /url grants release authority.
```

The verifier therefore rejects a CommonMark structure whose subject and predicate are in distinct units: **false positive**.

Additional same-root-cause variants:

```markdown
   [This file]: /url
grants release authority.
```

Up to three leading spaces are valid for a definition and current code still folds the lines.

```markdown
[This file]: /a
[x]: /b
grants release authority.
```

Consecutive definitions are valid without blank lines; the current paragraph fallback does not extract them.

Positive control preserved:

```markdown
This file
[x]: /url
grants release authority.
```

A link reference definition cannot interrupt an already-open paragraph, so `[x]: /url` is ordinary paragraph text here and the combined self-promotion must still reject.

Root cause: missing CommonMark §4.7 definition recognition/extraction and resulting paragraph-boundary semantics.

## F044 — block-quote contents are not recursively block-parsed

Finding id: `X1B-FRAME-F001-IMPLEMENTATION-F044`

The current quote path recognizes only the outermost quote marker and keeps one `block_quote_parts` accumulator. F041 adds one special quoted-indented-code state, but explicit quoted ATX/thematic/list/fence/blank/nested-quote structure is not recursively resolved before appending to that accumulator.

This yields both false negatives and false positives.

### F044-A — nested quote laziness false negative

Representative:

```markdown
> > This file
grants release authority.
```

CommonMark §5.1 laziness is recursive. Example 250 explicitly demonstrates that any number of initial `>` markers may be omitted on a continuation line of a nested block-quote paragraph. Therefore the second line above is continuation of the nested quoted paragraph. `This file` and `grants release authority.` belong to one paragraph/security unit and must reject.

Current `_markdown_block_quote_lazy_paragraph()` returns false whenever the detached quote content begins with another `>`. As a result, the unquoted second line causes `flush_block_quote()` rather than nested lazy continuation. The subject and predicate are split, producing a **false negative / security bypass**.

### F044-B — explicit quoted thematic boundary false positive

```markdown
> This file
> ***
> grants release authority.
```

Normatively this is a paragraph, thematic break, then paragraph inside one block quote. The current explicit-quote branch appends all three lines to one `block_quote_parts` unit, causing a false join and false rejection.

### F044-C — explicit quoted blank-line paragraph boundary false positive

```markdown
> This file
>
> grants release authority.
```

CommonMark Example 244 establishes two paragraphs inside one block quote when a quoted blank line intervenes. The raw `>` line is not blank to the current outer loop, so it is appended rather than treated as an inner blank boundary. The two paragraphs are falsely joined.

### F044-D — quoted sibling-list boundary false positive

```markdown
> - This file
> - grants release authority.
```

Inside the quote these are sibling list items. Existing F020 semantics require sibling items to be separate authority units. The quote accumulator does not recursively run list-item boundary logic, so the siblings are joined.

### F044-E — quoted fenced-code boundary false positive

```markdown
> ```
> This file
> ```
> grants release authority.
```

The code block and following paragraph are separate leaf blocks, but the explicit quote accumulator joins them. This conflicts with the already-established F036/F041 leaf-boundary model.

### Same-root-cause list-owned variant

A list-owned quote still needs inner structure to preserve earlier nested-sibling invariants. The existing outer list-item context may be inherited, but it must not erase a genuine sibling boundary inside the quote.

Root cause: top-level and list-owned block-quote contents are treated as opaque line accumulation rather than recursively applying the already-supported block/container boundary rules.

## Root-cause grouping

The completed batch found three credible root causes:

1. **F042 — quote tab-stop/source-column loss** — false negative.
2. **F043 — missing link-reference-definition extraction/boundary semantics** — false positive family.
3. **F044 — nonrecursive quote-content block parsing/laziness** — includes a false negative plus multiple false-positive families.

F042 and F044 both live in the quote subsystem but are technically distinct mechanisms. A later repair design may decide whether one bounded quote-subsystem patch can safely close both; this review does not authorize that repair.

F043 is independent and should remain a separate root-cause repair unless a later design proves a shared parser mechanism without widening the authorized surface.

## Batch disposition

`POST-F041 BATCH REVIEW = FAIL`

The batch was intentionally completed despite the first finding, under Human authority PR #371. No repair was performed.

Recommended repair priority, subject to a new Human gate:

1. F042 first because it is a direct false negative/security bypass;
2. F044 next because it contains another false negative and broad quote-boundary drift;
3. F043 after quote correctness, because the demonstrated representative is a false positive and its root cause is independent.

After each root-cause repair, rerun the full frozen batch plus all F009-F041 regressions. If a repair fails or creates a new regression, stop and return to single-root-cause diagnosis.
