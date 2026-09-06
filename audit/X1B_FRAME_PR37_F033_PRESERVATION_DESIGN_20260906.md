# X1B-FRAME PR #37 — F033 preservation audit and bounded repair design

Target: `FJ899/scriptops PR #37`

Exact repair input:

- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `5c32af7127000e86f33e9f0e79ac09de8441b49d`
- OLD TREE: `456ef9210d74a24f8702c15b6c28c244328e02ad`
- OLD verifier blob: `f3d196b6712037b4fda08fc6f40888c6c663c3ca`
- F033 finding: `FJ899/8 PR #313`
- Human repair authority: `FJ899/8 PR #314`

## Root cause

`_markdown_thematic_break_layout()` recognizes valid CommonMark thematic-break syntax at top level, but `_authority_soft_wrapped_units()` currently applies the resulting structural boundary only under `if list_frames and thematic is not None:`. With no active list, a line such as `***` therefore falls through to ordinary paragraph folding and can donate a self-reference across a real block boundary.

Representative false join:

```markdown
This file
***
grants release authority.
```

The current verifier joins all three nonblank physical lines into one authority unit although the thematic break separates the two paragraphs.

## Bounded repair design

Add top-level thematic/setext block-boundary handling immediately after `_markdown_thematic_break_layout()` and before list-specific thematic handling:

1. If `thematic is not None` and `list_frames` is empty, flush the current ordinary paragraph and consume the marker line as a block boundary.
2. This applies to valid 0–3-column `*`, `_`, spaced thematic markers, and dash-only helper candidates.
3. A dash-only candidate after an open top-level paragraph is a setext underline rather than an ordinary soft wrap; flushing the paragraph still produces the correct security-unit separation from the following paragraph.
4. Invalid thematic lookalikes remain ordinary paragraph text and must continue to join subject/predicate across the physical newline.
5. Keep all F032 list-context logic unchanged. In particular, current-leaf dash-only setext ambiguity inside an owned list item stays exactly as frozen by F032.
6. Do not introduce generic Markdown block parsing, HTML/fence parsing, unrelated cleanup, or runtime changes.

## Preservation matrix

Must remain rejecting / joined:

- F031 unindented and partially dedented lazy continuation;
- F028 nested non-one ordered lazy continuation;
- F023 marker-only/non-interrupting paragraph controls;
- F017/F018 ordinary soft-wrap and false-sentence-tail joins;
- invalid top-level thematic lookalikes such as `**`, `*-*`, and `***payload`.

Must remain separated / benign:

- F032 list -> top-level thematic break -> following paragraph;
- F032 owned unambiguous thematic break handling;
- F030 same-level cross-family/delimiter boundaries;
- F029 ancestor-level sibling boundary;
- F022 blank-line ownership and code-like controls;
- top-level valid thematic break between a self-reference paragraph and an unrelated authority paragraph;
- top-level dash-only setext underline between heading text and following paragraph.

Marker validity remains unchanged:

- thematic break requires at least three matching `-`, `_`, or `*` markers;
- spaces/tabs may separate markers;
- mixed markers or payload invalidate thematic-break recognition;
- top-level indentation >3 columns remains non-thematic in this parser.

## Completion invariants

- only `scripts/verify_repository.py` differs relative to OLD HEAD;
- exactly one replacement commit over BASE;
- frozen 12-path BASE-relative surface unchanged;
- full verifier PASS including new F033 regression and F032–F009 preservation;
- both existing GitHub Actions workflows green on exact NEW HEAD;
- freeze completion evidence, then STOP before independent post-repair review.
