# X1B-FRAME PR #37 — F032 preservation audit and bounded repair design

Target: `FJ899/scriptops PR #37` at OLD HEAD `841ecbf18f346becb4baf4bb11a31eaf391975eb`, verifier blob `5fb041541b4c80c00f94b8c32ec2a3aa96389864`.

Finding: `X1B-FRAME-F001-IMPLEMENTATION-F032` / `FJ899/8 PR #308`.

## Root cause

`_authority_soft_wrapped_units()` resolves blank-line ownership and list markers, but it has no higher-precedence CommonMark thematic-break recognition. With an active `list_frames` path, any nonblank line that is neither resolved as a list marker nor ownership-unwound is appended to the current leaf as lazy continuation. Thus:

```markdown
- This file
---
grants release authority.
```

is folded into one authority unit even though the thematic break closes the list before the final paragraph.

## Bounded design

1. Add a small thematic-break shape parser. It recognizes only matching `-`, `_`, or `*`, at least three markers, with spaces/tabs allowed between/after and no other content.
2. The parser reports expanded leading indentation and whether a dash-only line is also a possible setext underline.
3. In `_authority_soft_wrapped_units()`, resolve thematic-break precedence before list-marker parsing.
4. When an active list exists, find the deepest owning list frame using the same container-relative window `content_indent <= leading <= content_indent + 3`.
5. If no owner exists and the thematic break is valid at top level (0–3 columns), emit/close the active list path, discard the thematic-break line as block structure, and resume ordinary top-level paragraph parsing.
6. If an owner exists and the line is an unambiguous thematic break, consume it before list-marker parsing, close any deeper descendants, and mark a block boundary so the next dedented line must re-resolve ownership rather than using F031 lazy continuation.
7. If a dash-only line in the current open leaf is also a possible setext underline, do not reinterpret it as a thematic break in this bounded repair. This preserves setext precedence and avoids silently broadening F032.
8. Deep thematic-looking lines more than three columns beyond every owner remain ordinary paragraph/code-like content; existence of a list frame alone is not enough to manufacture a thematic break.

## Preservation matrix

Must remain positive/rejecting:
- F031 unindented, partially dedented, and nested lazy paragraph continuation;
- F028 nested non-one ordered lazy continuation;
- F027 indented-code list ownership;
- F020/F021 parent-to-descendant subject/predicate joining;
- all F017–F026 positive regressions.

Must remain benign/separated:
- F030 same-level family/bullet/delimiter boundaries;
- F029 ancestor-level sibling boundary;
- F022 post-blank ownership/code-like separation;
- ordinary top-level and nested siblings.

New F032 controls:
- top-level `---`, `***`, `___`, `- - -`, `* * *`, `_ _ _` after an active list close that list and prevent context donation;
- 1–3-column top-level thematic breaks behave likewise when not owned by the active item;
- owned unambiguous thematic breaks take precedence over possible list-marker interpretation and force subsequent dedented text to re-resolve ownership;
- fewer than three markers, mixed markers, or lines with non-whitespace payload do not become thematic breaks;
- dash-only current-leaf setext candidates are explicitly left to existing behavior in this bounded repair.

## Invariants

Only `scripts/verify_repository.py` may change relative to OLD HEAD. Final candidate remains one replacement commit over BASE `2f22843ac570498b506101addeba5453ab777f08` and the exact frozen 12-path BASE-relative surface. Full verifier and both existing GitHub Actions workflows must pass before completion evidence. Then STOP before independent post-repair review.