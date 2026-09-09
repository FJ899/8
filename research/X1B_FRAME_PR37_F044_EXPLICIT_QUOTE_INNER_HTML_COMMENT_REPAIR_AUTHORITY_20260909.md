# X1B-FRAME PR #37 — F044 explicit quote / inner HTML-comment repair authority

Human authorization: bounded repair only for the reproducible `EXPLICIT QUOTE / INNER HTML-COMMENT BOUNDARY` finding.

## Frozen ScriptOps target before repair

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `9c8c866131272ece7b292d9cc86a9e07c152000f`
- TREE: `08d76ac49e2fc5557540fce1a85bedd53e856d3e`
- verifier blob: `b4597fcaa8466ac5cb3368c0471589189a9325bd`

## Runtime finding evidence

External exact-runtime harness `FJ899/8 PR #524`, closed without merge, verified the exact HEAD/TREE/verifier binding before execution and a clean target checkout before and after execution.

Control:

```markdown
> This file
> # neutral heading
> grants release authority.
```

Result: 3 leaves, structural PASS.

Test — ONLY DELTA `ATX -> complete HTML comment`:

```markdown
> This file
> <!-- neutral comment -->
> grants release authority.
```

Runtime result:

```text
TEST_UNITS=1
TEST_UNIT_1='> This file > <!-- neutral comment --> > grants release authority.'
TEST_STRUCTURAL_OK=False
RESULT=FAIL_REPRODUCIBLE_EXPLICIT_QUOTE_INNER_HTML_COMMENT_BOUNDARY
```

## Authorized repair scope

Repair only:

```text
EXPLICIT QUOTE
+
INNER COMPLETE HTML COMMENT
+
LEAF-BOUNDARY LIFECYCLE
```

The repair may make the complete HTML-comment boundary flush/separate the active source-column-zero explicit-quote paragraph leaf. It must use existing HTML block/comment recognition and must not widen into generic HTML handling or generic block-transition handling.

## Required validation

1. Exact HTML-comment reproduction PASS.
2. Structural result is exactly 3 leaves: pre-comment quoted paragraph, complete quoted HTML comment, post-comment quoted paragraph.
3. Frozen ATX control remains GREEN with the same 3-leaf semantics.
4. Existing ATX repair remains semantically unchanged.
5. Position/depth/multiple-parent/outer-sibling regressions remain GREEN.
6. All inherited F042/F043/F044 regressions remain GREEN.
7. No generic `all HTML` / `all block transitions` widening.
8. No special case dependent on the exact comment text.
9. After validation, freeze exact HEAD/TREE/verifier and STOP.

Any failure of these conditions requires recording the failure and STOP.

## Explicit non-authority

No interaction testing, no additional block-boundary variant, no parent-count sweep, no generic block repair, no merge of ScriptOps PR #37, no movement of ScriptOps `main`, no deploy/release/tag, no canonical effect/status promotion, no X1B reopen, no V1.
