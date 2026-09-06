# X1B-FRAME-F001-IMPLEMENTATION-F022

## Review binding

Independent post-F021 implementation review authorized by `FJ899/8 PR #261`.

Exact ScriptOps target:

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `33b6691cdebb4a5ba07d38a492976cc84230fecb`
- TREE: `af96d8bbdcdc5b579a438c945ded90061890a07d`
- verifier blob: `0a468ba609df2a3484e2fbdea57b2f7d07e7c591`

## First credible counterexample

```text
10)  This file contains background notes.

    - Release authority belongs to a separate Human gate.
```

This is benign content split across structurally separate Markdown blocks.

For the ordered item `10)  ...`, the list marker width is 3 columns and the two following spaces make the item content indentation 5 columns. After the blank line, the four-space-indented `- Release authority ...` line is therefore not contained by that ordered list item. At top level, a four-space-indented bullet-like line is an indented code block, not a top-level list item.

The F021 implementation nevertheless calls `_markdown_list_item_layout(..., allow_deep_indent=bool(list_frames))` before any blank-line dedent / active-item ownership check. Because an ordered-list frame is still active, the four-space marker is accepted as a deep list marker. Its `marker_indent=4` is greater than the current frame marker indent `0`, so the parser adopts it as a descendant and inherits the parent text.

The resulting authority unit is effectively:

```text
10)  This file contains background notes. - Release authority belongs to a separate Human gate.
```

That unit now contains the self-reference `This file` from the first block and the promotion token `authority` from the separate benign code block. The whole-unit fallback therefore reports forbidden self-promotion even though neither block independently makes such a claim.

This is a false-positive structural-boundary failure introduced by the F021 deep-indent relaxation. The F021 regression explicitly preserves a standalone four-space bullet-like code block as non-list, but does not cover the same block immediately after a list item whose required content indentation exceeds four columns.

## Disposition

`X1B-FRAME-F001-IMPLEMENTATION-F022 = OPEN FINDING`

Per the authorized review rule, review STOPPED at F021 immediately after this first credible counterexample.

- F020 through F006 were not reviewed after F022.
- Q5-Q15 were not reviewed.
- no repair was attempted.
- no merge, ScriptOps main movement, deployment, release, tag, canonical effect, active-product status promotion, PR35 integration, X1B reopen, V1 action, or further-review authority is created by this finding.
