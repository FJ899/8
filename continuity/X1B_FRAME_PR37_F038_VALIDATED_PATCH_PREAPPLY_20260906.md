# F038 validated patch — pre-apply evidence

## Exact input binding

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `5d07e181c1a9d43f4bfca000962790b087b6fe15`
- OLD TREE: `bdbc73b06bb29c5b334cb2cd4bca0d49b68df63b`
- OLD verifier blob: `b29df53ab96596ac075118943b364d9b47eda6cd`
- F038 finding: `FJ899/8 PR #343`
- Human repair authority: `FJ899/8 PR #344`
- preservation/design: `FJ899/8 PR #345`

## Prepared patch

- target path: `scripts/verify_repository.py` only
- additions: `315`
- deletions: `0`
- SHA-256: `dede3ea00dd066c0ee7b6bbd5416a31043cbd0bde7aebb7c13c4ac5b185bbcd3`

## Bounded implementation

The patch adds bounded CommonMark HTML-block handling for paragraph-interrupting types 1 through 6, literal raw-block state, top-level/list-item ownership handling, and the necessary block-quote lazy-continuation interaction. Type 7 remains deliberately non-interrupting. No generic HTML parser is introduced.

The patch adds F038 regression coverage for the representative type-6 boundary, type-1 through type-5 endings, type-6 blank/EOF behavior, list and quote ownership, raw HTML payload self-promotion, Markdown-looking literal content inside HTML, four-column/escaped lookalikes, and type-7 non-interruption.

## Pre-apply validation performed

- patch parses as a Git unified patch;
- synthetic exact-context `git apply --check`: PASS;
- offset/context relocation `git apply --check` against a mock file with large varying hunk offsets: PASS;
- `git apply --numstat`: `315  0  scripts/verify_repository.py`;
- synthetic post-apply `git diff --check`: PASS;
- standalone F038 parser/security harness: PASS for all bounded boundary/rejection/helper cases;
- CommonMark cross-check with markdown-it CommonMark mode: representative type-1..6 cases render as paragraph + HTML block as expected, type-6 ends at blank/EOF, and type-7/four-column forms remain in the open paragraph.

## Still mandatory before mutation/push

The exact Human worktree at OLD HEAD must independently confirm clean topology, patch SHA-256, real `git apply --check`, and exact verifier-only numstat. Only after that check may the patch be applied locally. Full Python compile and the complete repository verifier must PASS before any replacement amend. Both existing GitHub Actions workflows must later PASS on the exact repaired remote HEAD.

No ScriptOps mutation or push is performed by this evidence record. No merge/main/deploy/release/tag/canonical/status/X1B/V1 authority is granted.
