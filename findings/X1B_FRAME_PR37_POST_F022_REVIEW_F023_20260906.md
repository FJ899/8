# X1B-FRAME-F001-IMPLEMENTATION-F023

## Status

`OPEN FINDING / FIRST COUNTEREXAMPLE / REVIEW STOP`

## Review authority

Human-authorized independent post-F022 review recorded in `FJ899/8 PR #266`.

## Exact reviewed target

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `0e86039856a97af04a7c0c06e5ffdf061abd1ada`
- TREE: `dcc8b80cfe0d863fe29f981c0527fe8a70d23dbd`
- verifier blob: `7043d154d8fde33e0f2452a74422a2d5ba4cb50a`
- state: `OPEN / DRAFT / UNMERGED`, exactly one commit over frozen BASE and frozen 12-path implementation surface.

## First credible counterexample

```md
- This file contains background notes.
-

  Release authority belongs to a separate Human gate.
```

CommonMark permits an empty bullet list item consisting of the marker alone. In this text the first line is the first list item, the bare `-` is a second empty list item, and the final text after the additional blank line is an ordinary paragraph outside that empty item. Thus the self-reference in the first item and the word `authority` in the later paragraph are structurally separate.

## Exact implementation cause

`_markdown_list_item_layout()` requires the marker to be followed by one or more spaces or tabs:

```python
r"^(?P<indent>[ \\t]*)(?:[-+*]|\\d{1,9}[.)])(?P<gap>[ \\t]+)"
```

Therefore a valid empty marker line `-` returns `None` instead of starting a new list item. With an active prior list frame, the bare marker is appended as ordinary continuation text. The following blank line sets `blank_seen = True`; the later two-space-indented paragraph has `leading == 2`, equal to the stale prior item's `content_indent == 2`, so F022's ownership check does not pop the stale frame. The later paragraph is then appended to the first item.

The resulting authority unit is effectively:

```text
- This file contains background notes. - Release authority belongs to a separate Human gate.
```

The whole-unit F016 fallback sees `THIS FILE` plus `AUTHORITY` and falsely reports forbidden self-promotion.

## Why this defeats F022

F022 claims that after a blank line ownership is resolved before interpreting subsequent content. That resolution assumes the active frame is still the structurally correct list item. A valid empty sibling marker is invisible to the parser, so ownership remains bound to the wrong prior item and F022 still merges separate Markdown blocks.

The existing F019-F022 regression matrix has sibling and deep-nesting controls but no bare empty list-item boundary control.

## Disposition

`X1B-FRAME-F001-IMPLEMENTATION-F023 = OPEN`

Per the Human review gate, review stopped immediately at F022. `F021 -> F006` and `Q5-Q15` were not reviewed in this run.

No repair, merge, ScriptOps main movement, deployment, release, tag, canonical effect, active-product status promotion, PR #35 integration, X1B reopen, V1, or further-review authority is created by this finding.
