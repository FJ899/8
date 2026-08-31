# X1D-A5 — Effect Method Binding Implementation Exact Frozen-HEAD Replay

## Status

`EXACT FROZEN-HEAD REPLAY = PASS`

`DIRECT FROZEN-HEAD EXECUTION PROVENANCE = ESTABLISHED`

`VALIDATION-EVIDENCE REQUIREMENT: EXACT FROZEN-HEAD TEST REPLAY = SATISFIED`

`AK-CANON IMPLEMENTATION REVIEW = NOT DETERMINED BY THIS ARTIFACT`

`CORRECTIVE CLOSURE = NOT AUTHORIZED / NOT DETERMINED`

`STOP`

This record freezes only the Human-authorized direct replay evidence. It does not authorize or perform implementation repair, GitHub merge, Human D0 mutation, Q_K/ruleset/CODEOWNERS mutation, credential provisioning, canonical effect, live AT0–AT10 execution, corrective closure, V1, release, deployment, or tag.

---

## 1. Exact implementation candidate under test

Repository:

`FJ899/scriptops`

Pull request:

`PR #32`

Candidate BASE:

`30095c3170d16263e2db553a2b199bd6e33feace`

Candidate branch:

`candidate/x1d-a5-bounded-app-boundary-20260831`

Frozen candidate HEAD:

`de4c1891ae759a056c124768d41b20d85fc566e5`

Frozen candidate TREE:

`0bcd0a8aadf58425e7953b445f0e5e3223402f71`

Frozen candidate paths and blobs:

- `phase6/x1d_a5_github_boundary.py`
  - BLOB `c108a0ce419b14d01f7401199458af0cc400039d`
- `tests/test_phase6_x1d_a5_github_boundary.py`
  - BLOB `db9a2b5f212183335526de319501f16cea83bd96`

Post-replay read-only verification confirmed:

- `FJ899/scriptops main = 30095c3170d16263e2db553a2b199bd6e33feace`
- `candidate/x1d-a5-bounded-app-boundary-20260831 = de4c1891ae759a056c124768d41b20d85fc566e5`
- PR #32 = `OPEN / DRAFT / UNMERGED`
- PR #32 base SHA = `30095c3170d16263e2db553a2b199bd6e33feace`
- PR #32 head SHA = `de4c1891ae759a056c124768d41b20d85fc566e5`

No ScriptOps ref was moved by this replay.

---

## 2. Validation harness identity

Validation repository:

`FJ899/8`

Validation BASE:

`b2c92ec5cd8fbb7272d701d229adc8a8019f951e`

Validation branch:

`research/x1d-a5-exact-head-replay-20260831`

Draft PR:

`FJ899/8 PR #101`

Temporary workflow path used solely for replay execution:

`.github/workflows/x1d-a5-exact-head-replay.yml`

Replay workflow run:

`run_id = 33418874687`

Replay job:

`job_id = 99576062142`

Workflow run event:

`pull_request`

Workflow run conclusion:

`success`

The workflow declared only:

`permissions: contents: read`

The GitHub Actions log recorded token permissions:

- `Contents: read`
- `Metadata: read`

Checkout used:

- repository `FJ899/scriptops`
- exact ref `de4c1891ae759a056c124768d41b20d85fc566e5`
- `fetch-depth: 1`
- `persist-credentials: false`

The checkout log shows GitHub fetched the exact SHA directly:

`git ... fetch ... origin de4c1891ae759a056c124768d41b20d85fc566e5`

and then checked out exactly:

`git checkout --progress --force de4c1891ae759a056c124768d41b20d85fc566e5`

Git reported detached HEAD state.

This was not `refs/pull/32/merge` and was not the synthetic PR merge commit `133b3fad423ceeb7128e151e4ff649f0355f82fa` used by ordinary pull-request CI in ScriptOps.

`SAME TREE != DIRECT FROZEN-HEAD EXECUTION PROVENANCE`

The direct frozen-HEAD provenance requirement is satisfied here by exact-SHA checkout plus explicit post-checkout identity verification.

---

## 3. Pre-test identity observations

Before any authorized test command, the validation step observed exactly:

`REPLAY_CHECKOUT_HEAD=de4c1891ae759a056c124768d41b20d85fc566e5`

`REPLAY_CHECKOUT_TREE=0bcd0a8aadf58425e7953b445f0e5e3223402f71`

`REPLAY_CODE_BLOB=c108a0ce419b14d01f7401199458af0cc400039d`

`REPLAY_TEST_BLOB=db9a2b5f212183335526de319501f16cea83bd96`

`REPLAY_SYMBOLIC_REF=DETACHED`

The interval between:

`REPLAY_STATUS_PORCELAIN_BEGIN`

and:

`REPLAY_STATUS_PORCELAIN_END`

was empty.

Therefore:

`WORKTREE CLEAN = YES`

The validation step then emitted:

`REPLAY_IDENTITY=PASS`

All HEAD/TREE/BLOB/clean-worktree/detached-HEAD prerequisites passed before test execution.

---

## 4. Execution environment and provenance

GitHub-hosted runner:

- OS: `Ubuntu 24.04.4 LTS`
- runner image: `ubuntu-24.04`
- runner image version: `20260823.283.1`
- runner version: `2.337.0`
- Azure region: `westus3`
- kernel: `Linux 6.17.0-1022-azure`
- architecture: `x86_64`
- Git: `2.55.0`
- Python: `3.11.16`
- Python executable: `/opt/hostedtoolcache/Python/3.11.16/x64/bin/python`

Runtime provenance step independently re-observed:

`HEAD = de4c1891ae759a056c124768d41b20d85fc566e5`

`TREE = 0bcd0a8aadf58425e7953b445f0e5e3223402f71`

Authorized environment preparation installed:

`pyyaml 6.0.3`

No persistent ScriptOps credential was provisioned. Checkout authentication was removed by `actions/checkout` after the exact read-only checkout, consistent with `persist-credentials: false`.

---

## 5. Exact replay commands and results

### 5.1 Environment preparation

Command:

```text
python -m pip install pyyaml
```

Result:

`PASS / exit status 0`

Observed package result:

`Successfully installed pyyaml-6.0.3`

### 5.2 Compile

Command:

```text
python -m compileall -q phase6 scripts/verify_repository.py tests/test_phase6_scriptops_smoke.py
```

Result:

`PASS / exit status 0`

### 5.3 Repository semantic/currentness verifier

Command:

```text
python scripts/verify_repository.py
```

Result:

`PASS / exit status 0`

The verifier emitted all expected `[PASS]` lines, including repository self-containment, Phase 6 authority boundaries, currentness reconciliation, historical v2 identity, bounded proposal evidence, and cold-start evidence checks.

### 5.4 Bounded X1D-A5 deterministic module

Command:

```text
python -m unittest tests.test_phase6_x1d_a5_github_boundary -v
```

Result:

`PASS / exit status 0`

Observed summary:

```text
Ran 25 tests in 0.009s
OK
```

The passing module includes the clarified Human-D0 currency cases, including complete decision-set revalidation, identical approval order-independence, conflicting approval/CHANGES_REQUESTED denial, dismissed historical evidence behavior, completeness failure, duplicate review identity failure, no-substitution, digest integrity, Q_K/bypass checks, stale-state zero transport, and read-only/merge-only boundary checks.

### 5.5 Full deterministic Phase 6 regression

Command:

```text
python -m unittest discover -s tests -p 'test_phase6_*.py' -v
```

Result:

`PASS / exit status 0`

Observed summary:

```text
Ran 42 tests in 7.815s
OK
```

The run also emitted preserved authority-boundary markers including:

`CANONICAL_EFFECT=NOT_APPLIED`

and:

`HUMAN_APPROVAL=NOT_REQUESTED`

for the historical Phase 6 workloads where applicable.

---

## 6. Ordinary PR CI versus this replay

The earlier ScriptOps PR #32 pull-request workflow was associated with candidate HEAD `de4c1891ae759a056c124768d41b20d85fc566e5`, but `actions/checkout` actually executed the synthetic merge ref:

`133b3fad423ceeb7128e151e4ff649f0355f82fa`

That evidence was useful for byte/content regression but did not establish direct frozen-HEAD execution provenance.

This replay closes that specific provenance gap because the workflow fetched and checked out the candidate SHA itself and verified its exact HEAD, TREE, two frozen BLOBs, detached state, and clean worktree before running the deterministic commands.

---

## 7. Prior accidental ScriptOps dangling-object incident

Before the successful harness path was established, an earlier tooling error accidentally invoked GitHub Git-data `create_commit` operations in `FJ899/scriptops` instead of the intended read-only inspection.

The following four commit objects were created without moving any ref:

- `cb3e9378a074c0cff09ca6d5cbecf5d55ee55daf`
- `2655516240c69357f2c86cdfaf828d595fbb2d06`
- `9e40637eda6ba4caca8d7ce2065b07ca16dde478`
- `37338fbce1078669d2d6c61a1f8deccdfd2b4e1f`

They were created against:

- parent `de4c1891ae759a056c124768d41b20d85fc566e5`
- tree `0bcd0a8aadf58425e7953b445f0e5e3223402f71`

No `update_ref`, merge, PR update, ruleset mutation, or canonical effect accompanied those object creations.

Subsequent read-only incident verification established:

- full observed ScriptOps refs contained none of those four SHA values;
- `refs/heads/main` remained `30095c3170d16263e2db553a2b199bd6e33feace`;
- `refs/heads/candidate/x1d-a5-bounded-app-boundary-20260831` remained `de4c1891ae759a056c124768d41b20d85fc566e5`;
- PR #32 remained bound to the same BASE and HEAD and remained open/draft/unmerged.

Accordingly, the incident changed ScriptOps object storage but did not change reachable/canonical/ref state.

`UNAUTHORIZED DANGLING GIT OBJECT CREATION = RECORDED`

`SCRIPTOPS REF/CANONICAL STATE MOVED = NO`

---

## 8. Validation-branch preparation anomalies

While preparing the temporary validation harness in `FJ899/8`, several accidental placeholder files were created on the dedicated validation branch and immediately deleted before the replay PR was opened or before the replay run was used as evidence. These files never reached `FJ899/8 main` and were absent from the effective BASE-to-replay-head diff.

The temporary paths were:

- `research/.x1d-a5-replay-placeholder`
- `research/.do-not-use`
- `research/.pr-sentinel`
- `research/.this-should-not-exist`
- `research/.accidental-again`
- `research/.final-accident`

Immediately before PR creation, a BASE comparison established that the only effective changed file was:

`.github/workflows/x1d-a5-exact-head-replay.yml`

These preparation anomalies are recorded for provenance transparency. They do not alter the replayed ScriptOps checkout or test result.

---

## 9. Replay disposition

All required exact identity prerequisites passed.

All authorized deterministic commands completed successfully on the direct detached frozen candidate HEAD.

Therefore:

`EXACT FROZEN-HEAD REPLAY = PASS`

`DIRECT FROZEN-HEAD EXECUTION PROVENANCE = ESTABLISHED`

`VALIDATION-EVIDENCE REQUIREMENT: EXACT FROZEN-HEAD TEST REPLAY = SATISFIED`

This disposition means only that the previously open direct-execution evidence requirement is satisfied for the exact frozen candidate identified above.

It does not mean:

`AK-CANON IMPLEMENTATION REVIEW = PASS`

It does not mean:

`CORRECTIVE CLOSURE = PASS`

It does not authorize any live effect.

`REPLAY PASS != IMPLEMENTATION REVIEW PASS`

`IMPLEMENTATION REVIEW PASS != CORRECTIVE CLOSURE`

`AI PROPOSES != HUMAN DECIDES`

`STOP`
