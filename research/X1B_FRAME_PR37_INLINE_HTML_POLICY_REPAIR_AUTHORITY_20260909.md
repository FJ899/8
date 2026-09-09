# X1B-FRAME PR37 bounded inline-HTML policy-semantic repair authority

Human authorization: `accept`.

Finding evidence: `FJ899/8 PR #544`.

Frozen ScriptOps target before repair:
- HEAD `2fe2867eec5a5e8e0efb71d9b41f729cd1170fa8`
- TREE `a1bdf5fe152f5a62151364a5d57d335b8b84a05c`
- verifier blob `60d050b76673e2aa27bd778a8765fcd65b8b9c02`

Authorized semantic pipeline only:

`RAW MARKDOWN -> existing block/ownership parsing -> extracted authority unit -> bounded inline-HTML visible-text canonicalization -> existing character-reference decoding -> existing self-promotion matcher`.

Mandatory structural invariance:
- no block-boundary change;
- no ownership change;
- no quote/list-structure change;
- no interpretive-unit membership change;
- no raw-Markdown pre-normalization.

Required proof:
1. exact `<span>file</span>` reproduction becomes policy-equivalent to literal control;
2. small bounded alternate set using structurally different well-formed inline markup, not a broad HTML sweep;
3. malformed / non-equivalent markup is not blindly stripped;
4. existing character-reference semantic equivalence remains GREEN;
5. existing THIS FILE / promotion / negation grammar remains delegated unchanged;
6. accumulated inherited corpus remains GREEN;
7. Verify / Smoke GREEN;
8. replacement exact HEAD/TREE/verifier freeze;
9. full known-regression replay;
10. STOP before restarting fresh independent final review.

Not authorized:
- regex/generic strip-tags behavior;
- raw-Markdown HTML stripping;
- generic HTML sanitizer/parser rewrite;
- Markdown block parser changes;
- ownership/lifecycle changes;
- Unicode normalization expansion;
- whitespace-policy rewrite;
- new interaction matrix;
- P0-P9;
- merge/main/deploy/release/tag/canonical/status/X1B/V1 action.
