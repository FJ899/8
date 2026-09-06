# X1B-FRAME PR #37 — F032 bounded repair Human authority

Human authorization: `accept`.

This authorizes exactly one bounded repair of `X1B-FRAME-F001-IMPLEMENTATION-F032` against the exact repaired candidate:

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `841ecbf18f346becb4baf4bb11a31eaf391975eb`
- OLD TREE: `c127542b6aaac202ac4fa7a96a4026b76455efca`
- OLD verifier blob: `5fb041541b4c80c00f94b8c32ec2a3aa96389864`
- finding evidence: `FJ899/8 PR #308`

## Authorized repair boundary

The repair may change only `scripts/verify_repository.py` relative to OLD HEAD and must address the F032 CommonMark thematic-break structural boundary without weakening F031 lazy-continuation behavior.

Required preservation:

- F031 indentation-loss lazy continuation remains joined when CommonMark still treats the line as the same paragraph/list item;
- F030 same-level cross-family/delimiter list boundary remains separated;
- F029 ancestor-level list boundary remains separated;
- F028 nested non-one ordered lazy continuation remains joined when it cannot interrupt the paragraph;
- F017–F027 and all earlier frozen regression behavior remains preserved;
- thematic-break recognition must follow CommonMark shape: 0–3 leading columns, at least three matching `-`, `_`, or `*` markers, spaces/tabs allowed between/after markers, no other non-whitespace characters;
- thematic break must take precedence over a possible list-item interpretation;
- indented thematic-looking content owned by a list item must not be reclassified as top-level solely because a list frame exists;
- setext-heading precedence must not be silently generalized into an unrelated repair; if a candidate repair cannot safely distinguish an ambiguous dash line, STOP and record a finding rather than broaden scope.

## Candidate invariants

After repair:

- the candidate must remain exactly one replacement commit over BASE;
- the BASE-relative changed-path surface must remain exactly the frozen 12 paths;
- relative to OLD HEAD, only `scripts/verify_repository.py` may differ;
- full repository verifier must PASS;
- `Verify repository state` GitHub Actions workflow must PASS;
- `Phase 6 ScriptOps smoke` GitHub Actions workflow must PASS;
- completion evidence must be frozen in `FJ899/8`;
- STOP before independent post-repair review.

No authority is granted for merge of PR #37 or PR #35, ScriptOps main movement, deploy/release/tag, canonical effect, active-product status promotion, X1B reopen, or V1.