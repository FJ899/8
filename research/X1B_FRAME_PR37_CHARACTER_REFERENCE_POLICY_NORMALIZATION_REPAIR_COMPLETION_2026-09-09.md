# X1B-FRAME PR37 bounded character-reference policy normalization repair completion

Completion evidence for the Human-authorized repair under `FJ899/8 PR #539`, following the fresh independent final-review finding in `FJ899/8 PR #538`.

## Final frozen ScriptOps PR #37 candidate

- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `2fe2867eec5a5e8e0efb71d9b41f729cd1170fa8`
- TREE: `a1bdf5fe152f5a62151364a5d57d335b8b84a05c`
- verifier blob: `60d050b76673e2aa27bd778a8765fcd65b8b9c02`
- exactly 1 replacement commit ahead / 0 behind
- exactly 81 changed paths

The previous GREEN verifier is retained byte-for-byte at `scripts/verify_repository_fresh_final_lazy_quote_html.py`, blob `d82237f6ab6546dbf1a5c4eeddc9e26c906cdf05`.

## Repair semantics

Raw Markdown is parsed first by the unchanged block/ownership parser. Character-reference decoding is applied only to already-extracted authority-unit text for self-promotion policy matching. The existing self-reference/promotion/negation grammar remains the policy grammar.

Structural invariance was explicitly checked: parser binding and authority-unit membership remain unchanged for literal, encoded, malformed and inert samples.

## Validation

- isolated ScriptOps probe PR #95: closed without merge;
- probe Verify `34393015663`: PASS;
- probe Smoke `34393015679`: PASS;
- final PR37 Verify `34393146013`: PASS;
- final PR37 Smoke `34393146022`: PASS;
- full external known-regression replay `FJ899/8 PR #540`, run `34393314904`, job `102606759731`: PASS;
- full deterministic Phase 6 replay: 17 tests / OK;
- external recursion x multiple quoted parents controls/test: PASS;
- external nested block-quote depth 2->3 control/test: PASS;
- external character-reference semantic-equivalence guard: PASS;
- replay checkout clean before and after.

Targeted verifier evidence explicitly confirms:

- exact `This&#32;file grants release authority.` bypass repaired;
- legal character-reference spellings decoding to the same semantic literal yield identical policy rejection;
- policy decoding occurs after raw authority-unit extraction;
- block/ownership/unit structure is preserved;
- malformed/unknown references are not silently over-normalized;
- repair remains bounded to policy semantics.

## Disposition

`CHARACTER-REFERENCE POLICY NORMALIZATION GAP = REPAIRED / GREEN`

`KNOWN-FINDING REGRESSION STATE = GREEN`

`RAW MARKDOWN STRUCTURE = UNCHANGED BY REPAIR`

`FRESH INDEPENDENT FINAL REVIEW OF THE NEW CANDIDATE = NOT RESTARTED`

`P0-P9 = NOT STARTED`

`MERGE READINESS = NOT ESTABLISHED`

STOP before fresh independent final-review restart. No merge/main/deploy/release/tag/canonical/status/X1B/P0-P9/V1 action is authorized by this completion record.
