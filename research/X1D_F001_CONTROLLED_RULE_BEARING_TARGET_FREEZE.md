# X1D-F001 — CONTROLLED RULE-BEARING TARGET FREEZE

Status: TARGET FREEZE ONLY / NO T1–T10 AUDIT

This artifact records the exact controlled rule-bearing PR created after bootstrap boundary activation. It does not perform or imply any T1–T10 verdict.

## Exact base boundary

- repository: `FJ899/scriptops`
- base branch: `main`
- exact base HEAD: `30095c3170d16263e2db553a2b199bd6e33feace`
- exact base TREE: `7ba16fab7879d7640801c410f171a08f79c8168b`
- `.github/CODEOWNERS` blob on base: `5dd686893d265217d921c352df033ff72fdf910e`

Relevant CODEOWNERS binding on base:

- `/governance/ @litrgratis-pixel`

## Controlled rule-bearing PR

- PR: `FJ899/scriptops #27`
- title: `X1D-F001: post-bootstrap controlled rule-bearing test`
- state at freeze: `OPEN / DRAFT / NOT MERGED`
- base: `main@30095c3170d16263e2db553a2b199bd6e33feace`
- head branch: `test/x1d-f001-post-bootstrap-rule-bearing`
- exact HEAD: `291cf48a4a6556cfaaee215abc4a47b8ab345d3f`
- exact TREE: `0b70a929f3035321240bb2aaad56f45ce2a10da9`
- parent: `30095c3170d16263e2db553a2b199bd6e33feace`
- changed file: `governance/X1D_F001_POST_BOOTSTRAP_CONTROLLED_RULE_BEARING_TEST.md`
- changed file blob: `3d666bea44acf1607e3421cb42b048ed4b3583b8`
- commits: `1`
- changed files: `1`

The candidate intentionally changes one path inside the activated `/governance/` CODEOWNERS scope and changes no production behavior.

## Live enforcement state at freeze

Ruleset:

- repository: `FJ899/scriptops`
- name: `CANONICAL_MAIN_PROTECTION_V1`
- id: `21147233`
- source type: `Repository`
- source: `FJ899/scriptops`
- target: `branch`
- enforcement: `active`
- applies to: `~DEFAULT_BRANCH`
- required approving review count: `1`
- require code-owner review: `true`
- require last-push approval: `true`
- required reviewers: `[]`
- required review-thread resolution: `true`
- bypass actors: `[]`
- current user can bypass: `never`
- ruleset updated_at: `2026-08-30T18:30:51.689+02:00`

## Bound authority model

This target remains bound to the previously frozen `B_AI` and established Human authority model:

- `C_H_APPROVE = @litrgratis-pixel approval capability`
- `C_H_POLICY = Human-operated FJ899 GitHub Web UI/admin session`

No new authority claim is introduced here.

## STOP state

- PR #27: `DO NOT MERGE`
- T1–T10: `NOT EXECUTED`
- X1D-F001: `OPEN`
- A5: `STOP`
- V1: `STOP`
- release/deployment/tag: `NOT AUTHORIZED`

Any mutation of PR #27 head, base, CODEOWNERS, or live ruleset creates a different audit target and requires a new freeze before independent T1–T10 evaluation.
