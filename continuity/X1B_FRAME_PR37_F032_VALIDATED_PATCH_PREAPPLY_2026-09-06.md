# X1B-FRAME PR #37 — F032 validated patch pre-apply evidence

Bound repair authority: `FJ899/8 PR #309`.
Preservation/design audit: `FJ899/8 PR #310`.
Finding: `FJ899/8 PR #308` / `X1B-FRAME-F001-IMPLEMENTATION-F032`.

Exact ScriptOps input:
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `841ecbf18f346becb4baf4bb11a31eaf391975eb`
- OLD TREE `c127542b6aaac202ac4fa7a96a4026b76455efca`
- OLD verifier blob `5fb041541b4c80c00f94b8c32ec2a3aa96389864`

Prepared patch artifact:
- file `X1B_FRAME_PR37_F032_REPAIR.patch`
- SHA-256 `16db59ccfc18467d26a523d61491c19e3b25ce92bf1672ad44c91f1b66f36cda`
- parsed diff surface: only `scripts/verify_repository.py`
- parsed diff size: 165 insertions / 0 deletions

Patch design:
- adds a bounded CommonMark thematic-break shape parser;
- resolves thematic-break precedence before list-marker parsing only in active list context;
- closes an active list when a valid 0–3-column thematic break is outside every active owner;
- consumes owned unambiguous thematic breaks before possible list-marker parsing and forces the following line to re-resolve ownership;
- preserves dash-only current-leaf setext ambiguity rather than silently broadening F032;
- leaves deep thematic-looking text non-structural when it is more than three columns beyond every owning content indent.

Pre-apply semantic checks performed on an isolated model of the exact authority-folding logic:
- F031 unindented / partially dedented / nested lazy continuation remained rejecting;
- F028 nested non-one ordered lazy continuation remained rejecting;
- F029 ancestor sibling and F030 same-level boundary controls remained separated;
- representative F032 `---`, `***`, `___`, spaced dash, one-column dash and owned-star thematic boundaries stopped donating list context;
- invalid short/mixed/payload thematic lookalikes remained non-boundaries;
- current-leaf dash-only setext control remained rejecting;
- deep code-like thematic-looking control remained rejecting.

A CommonMark-compatible parser (`markdown-it` commonmark mode) was also used to confirm the representative block structures: the F032 top-level thematic breaks close the list, the owned `* * *` break remains inside the list item while subsequent unindented text exits, and the owned dash-only line is a setext heading rather than a thematic break.

This is pre-apply evidence only. The patch has not yet been applied to `FJ899/scriptops`. Full repository verifier, full Phase 6 smoke, one-replacement-commit/frozen-12-path guards, remote lease check, GitHub Actions and completion evidence are still required before repair completion.

No merge/main/deploy/release/tag/canonical/status/X1B/V1 authority.