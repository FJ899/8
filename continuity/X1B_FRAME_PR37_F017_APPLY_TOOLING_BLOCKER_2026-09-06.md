# X1B-FRAME — F017 repair apply tooling blocker

Date: 2026-09-06

## Authority

Human repair authority is durably recorded in `FJ899/8 PR #239` for exactly one bounded F017 repair of `FJ899/scriptops PR #37`.

## Exact live pre-repair target

- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `a94a4018b469ae864e4715157f00b9d765df11c0`
- TREE `420faf0b06f4b53228770735f1504b3f58d5c580`
- verifier blob `d7153ccdf4469c7355e9b6aa0926228a91e74c00`
- PR state `OPEN / DRAFT / UNMERGED`
- exactly one commit above BASE and exactly twelve base-relative changed paths.

## Prepared F017 repair

A minimal unified diff has been prepared against the exact verifier blob above.

Patch identity:

- filename: `X1B_FRAME_PR37_F017_REPAIR.patch`
- byte length: `4838`
- SHA-256: `54f64f127653a83e8da7a908540ce1708f4fca7f3bdbc92209f3356338575eb8`

The patch is limited to `scripts/verify_repository.py` and:

1. folds Markdown physical soft wraps into logical authority units before the existing Layer-B parser evaluates subject/predicate relationships;
2. preserves hard sentence and blank-line boundaries;
3. adds non-vacuous F017 positive regressions for two-line, three-line and fresh-subject multiline fragmentation;
4. adds benign multiline negation regressions, including a negated infinitive whose self-reference is an object rather than a fresh subject;
5. adds the F017 PASS marker.

A standalone behavior matrix verified the intended F017 rejection cases, benign multiline negation cases, and representative F015/F016/F010 boundaries. Patch syntax/context structure was also checked against the exact fetched verifier regions.

## Tooling boundary

The available GitHub write connector can replace a complete UTF-8 file or create Git objects, but it does not expose a patch-apply operation and cannot consume the prepared local diff as a file input. Replacing the 45KB verifier through manual whole-file transfer would recreate the previously identified transport/integrity risk and is not accepted.

Therefore no ScriptOps tree, commit, ref, PR head, or `main` mutation has been made for F017 in this session.

## Authorized resume sequence

No new Human acceptance is required for the already-authorized F017 repair. Resume in the retained exact-byte local clone:

1. fetch and verify PR #37 still points to `a94a4018b469ae864e4715157f00b9d765df11c0` and `origin/main` still points to frozen BASE;
2. reset the dedicated local checkout to exact HEAD with LF bytes and clean index/worktree;
3. verify pre-repair verifier blob `d7153ccdf4469c7355e9b6aa0926228a91e74c00`;
4. apply the exact patch and run `git diff --check` and full `python scripts/verify_repository.py`;
5. record the resulting verifier blob and tree;
6. create a replacement commit whose sole parent is frozen BASE, preserving exactly one commit / twelve paths and changing only the verifier relative to the pre-repair HEAD;
7. force-update the PR #37 branch once using stale-head protection;
8. require `Verify repository state` and `Phase 6 ScriptOps smoke` to succeed;
9. confirm `scriptops/main` remains frozen BASE;
10. freeze exact repaired HEAD/TREE/verifier blob and STOP.

A separate Human gate remains required for post-F017 independent re-review. No merge/effect/status authority exists.