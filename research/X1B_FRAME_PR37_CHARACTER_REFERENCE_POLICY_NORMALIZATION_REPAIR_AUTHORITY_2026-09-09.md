# X1B-FRAME PR37 bounded character-reference policy normalization repair authority

Human authorization grants exactly one bounded verifier-only repair for the fresh independent final-review finding recorded in `FJ899/8 PR #538`.

## Frozen ScriptOps target before repair

- HEAD: `5e80aef5262c21e79c8518936c74cae0ce1be5f0`
- TREE: `8d95d16bf6c3a5b5acf72323fcda77bba1fa4172`
- verifier blob: `d82237f6ab6546dbf1a5c4eeddc9e26c906cdf05`

## Authorized pipeline

`RAW MARKDOWN -> existing block/ownership parsing -> extracted authority-unit text -> strict legal character-reference decoding for policy text -> existing self-promotion grammar`

The repair MUST NOT decode raw Markdown before Markdown/block/ownership parsing.

## Structural invariance

Policy character-reference decoding MUST NOT alter:

- block boundaries;
- ownership;
- quote/list structure;
- interpretive-unit membership.

For each repaired sample, structure is taken from the existing raw parser unchanged; only the extracted unit text used for self-promotion policy matching may be character-reference decoded.

## Required proof

1. Exact `This&#32;file grants release authority.` reproduction is rejected.
2. Literal `This file grants release authority.` remains rejected.
3. Decoded-equivalent legal character-reference spellings yield the same self-promotion claim result without a special case for `&#32;`.
4. Character-reference decoding occurs only after authority-unit extraction.
5. Malformed/non-semantic character-reference spellings are not silently decoded.
6. Existing Markdown parser, ownership, lifecycle, whitespace policy and Unicode normalization are unchanged.
7. Inherited F042/F043/F044 and current verifier corpus remain GREEN.
8. Verify and Smoke remain GREEN.
9. Freeze a replacement exact HEAD/TREE/verifier.
10. Run full known-regression replay on the frozen replacement candidate.
11. STOP before any fresh independent final-review restart.

## Explicitly not authorized

- generic HTML normalization;
- Unicode NFC/NFKC or other Unicode normalization overhaul;
- whitespace-policy rewrite;
- Markdown parser refactor;
- ownership or lifecycle changes;
- new interaction testing;
- P0-P9;
- merge, main movement, deploy, release, tag, canonical effect, status promotion, X1B reopen or V1.
