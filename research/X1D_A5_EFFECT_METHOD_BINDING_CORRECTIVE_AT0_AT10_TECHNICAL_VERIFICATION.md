# X1D-A5 Effect-Method Binding Corrective AT0–AT10 Technical Verification

## Status

`DURABLE TECHNICAL VERIFICATION EVIDENCE`

`FORMAL AT0 = PASS`

`AT1 = PASS`

`AT2 = PASS`

`AT3 = PASS`

`AT4 = PASS`

`AT5 = PASS`

`AT6 = PASS`

`AT7 = PASS`

`AT8 = PASS`

`AT9 = PASS`

`AT10 = PASS`

`X1D-A5 CORRECTIVE TECHNICAL VERIFICATION AT0–AT10 = PASS`

This artifact freezes the already-observed X1D-A5 corrective verification evidence. It does not reopen testing, authorize another canonical effect, declare corrective closure, or substitute for Human closure acceptance.

`TECHNICAL CORRECTIVE VERIFICATION PASS != CORRECTIVE CLOSURE`

`TECHNICAL CORRECTIVE VERIFICATION PASS != HUMAN CLOSURE ACCEPTANCE`

`AI PROPOSES != HUMAN DECIDES`

## 1. Governing corrective design binding

Repository:

`FJ899/scriptops`

Corrective design PR:

`#31`

Observed state at evidence preparation:

`OPEN / DRAFT / UNMERGED`

HEAD:

`eda29d9b2916425cfa4048c8eff989b5f767ee58`

TREE:

`4cd9ab6d457d3496d76a47c3a6d031ea5e6cde83`

PATH:

`governance/X1D_A5_EFFECT_METHOD_BINDING_CORRECTIVE_CANDIDATE.md`

BLOB:

`1247088730cbf5dddb2aea667c9842f8cc8bf980`

Accepted finding preserved by the governing design:

`EFFECT METHOD NOT BOUND TO THE EXACT HUMAN DECISION`

The corrective design requires exact `OperationAdmission` method binding, executor no-substitution, merge-only protected-branch platform closure, non-destructive negatives, and exact post-effect two-parent merge truth.

## 2. Reviewed implementation under test

Repository:

`FJ899/scriptops`

Implementation PR:

`#32`

Exact reviewed candidate HEAD:

`a80d7714d90213c4f3e5aa514a0119560067dc01`

Exact reviewed candidate TREE:

`31e4ad15bd7257dc95890dafbae41c234d03c431`

Implementation code:

`phase6/x1d_a5_github_boundary.py`

Code BLOB:

`9de6b6931563ac686e3b4440c623f5522653c61e`

Tests:

`tests/test_phase6_x1d_a5_github_boundary.py`

Test BLOB:

`1c1f9070b626784d8c8810378402d310935a5d84`

The validation harness used byte-identical reviewed implementation code. No implementation mutation was performed by AT0–AT10.

After the canonical positive-control merge advanced `main`, GitHub reported PR #32 as still `OPEN / DRAFT / UNMERGED` on the same exact HEAD, while its derived `mergeable` state became `false`. This was observed as a consequence of canonical-base advance and was not repaired or represented as a candidate mutation.

`DERIVED POST-MAIN MERGEABILITY STATE != IMPLEMENTATION MUTATION`

## 3. Live Q_K binding

Repository:

`FJ899/scriptops`

Ruleset ID:

`21147233`

Ruleset name:

`CANONICAL_MAIN_PROTECTION_V1`

Target:

`branch`

Enforcement:

`active`

Conditions:

```text
include = ["~DEFAULT_BRANCH"]
exclude = []
```

Frozen freshness:

`updated_at = 2026-08-31T23:32:45.564+02:00`

Required and observed method envelope:

```text
allowed_merge_methods = ["merge"]
```

Observed bypass state:

```text
bypass_actors = []
current_user_can_bypass = never
```

Observed pull-request parameters:

```text
required_approving_review_count = 1
dismiss_stale_reviews_on_push = false
required_reviewers = []
require_code_owner_review = true
require_last_push_approval = true
required_review_thread_resolution = true
require_extra_approval_for_unattributed_changes = false
```

Observed rules:

```text
deletion
non_fast_forward
pull_request
```

The repository-level merge settings still permitted merge commits, squash, and rebase generally; the protected default-branch ruleset supplied the narrower canonical merge-only envelope. The ruleset remained byte-for-byte semantically merge-only after AT9/AT10, with the same `updated_at` and no bypass.

## 4. Fresh inert acceptance candidate and Human D0

Acceptance PR:

`FJ899/scriptops PR #33`

Pre-effect required state:

`OPEN / READY / UNMERGED`

Base HEAD:

`30095c3170d16263e2db553a2b199bd6e33feace`

Base TREE:

`7ba16fab7879d7640801c410f171a08f79c8168b`

Candidate branch:

`acceptance/x1d-a5-effect-method-binding-live-positive-control-20260831`

Candidate HEAD:

`2f2dc1aaa9a775f37e778e8a735cf8ef5b8a9660`

Candidate TREE:

`4215d9306392070e64c6fd74a6cfb813ca9d0601`

Candidate parent:

`30095c3170d16263e2db553a2b199bd6e33feace`

Complete changed-path set:

`acceptance/X1D_A5_EFFECT_METHOD_BINDING_LIVE_POSITIVE_CONTROL.md`

Artifact BLOB:

`f02e37a7f97b5b91dd875690de089452853c4e98`

Artifact content SHA-256:

`0f5bae0790818891952e8c6f63b25b1c6f6ba3858031c9f5f545b70041a2880e`

Path-set digest:

`417391fbac38b23240a5f5dcfd6cff4f1012b4ea1c74280e458117540ec68dc5`

Expected post-effect TREE:

`4215d9306392070e64c6fd74a6cfb813ca9d0601`

### Human D0

Decision ID:

`X1D-A5-CORRECTIVE-D0-PR33-20260901`

Human actor:

`litrgratis-pixel`

GitHub review node ID:

`PRR_kwDOTlowk88AAAABLnKQnQ`

GitHub review numeric ID:

`5074227357`

Review state:

`APPROVED`

Review commit:

`2f2dc1aaa9a775f37e778e8a735cf8ef5b8a9660`

Submitted at:

`2026-09-01T05:14:04Z`

Human review body SHA-256:

`e69adfda303a457f95ebfb373666806e2c7641c630d5c04095ab6a6434f692ff`

Immediately before AT9, the complete GitHub review set contained exactly this one bound approval on page 1 and an empty page 2. No active conflicting same-Human/same-candidate decision existed.

`CURRENT HUMAN D0 = EXACT BOUND APPROVAL + COMPLETE NON-CONFLICTING ACTIVE DECISION SET`

## 5. Formal AT0 freeze

The exact admission identity reconstructed from fresh trusted state matched the preregistered values:

```text
admission_version = x1d-a5-operation-admission/v1

admission_id =
x1d-a5:97622878f3c4895b26688e56c93399104e2b014dc5deecd648ea0fa8b4dd1110

human_decision_id =
X1D-A5-CORRECTIVE-D0-PR33-20260901

human_review_id =
PRR_kwDOTlowk88AAAABLnKQnQ

human_actor =
litrgratis-pixel

repository =
FJ899/scriptops

pr =
33

base_head =
30095c3170d16263e2db553a2b199bd6e33feace

base_tree =
7ba16fab7879d7640801c410f171a08f79c8168b

candidate_head =
2f2dc1aaa9a775f37e778e8a735cf8ef5b8a9660

candidate_tree =
4215d9306392070e64c6fd74a6cfb813ca9d0601

path_set_digest =
417391fbac38b23240a5f5dcfd6cff4f1012b4ea1c74280e458117540ec68dc5

canonical_ref =
refs/heads/main

merge_method =
merge

expected_post_tree =
4215d9306392070e64c6fd74a6cfb813ca9d0601

qk_ruleset_id =
21147233

qk_ruleset_updated_at =
2026-08-31T23:32:45.564+02:00

qk_allowed_merge_methods_digest =
39c596909e5372a870034c2f8679b9c8492290764ec6c330d694b71f61bf65df

canonical_operation_digest =
b34af3ee6e8464e8d01c76eca4627d21d5f77456769b918c9d5d2cd35247978a

admission_digest =
c4bf9ba3c00179e27a92ce98f82adb05da3b005ceb8379fac0a2e0eb73273287
```

Canonical serialized `OperationAdmission` SHA-256:

`5000e3a5a001aca7585b52f49a9fb934efd41e3b87f1edbc07d69b912814ba1c`

Result:

`FORMAL AT0 = PASS`

## 6. AT1–AT8 non-destructive verification

### AT1 — live Q_K method envelope

Fresh live ruleset read established exactly merge-only canonical policy, no bypass actors, and no process bypass.

Result:

`AT1 = PASS`

### AT2 — exact-method admission positive construction

Using fresh trusted state and the exact Human D0, the reviewed broker constructed one in-memory admission with:

```text
D0.merge_method = merge
admission.merge_method = merge
admission_id = exact frozen AT0 value
canonical_operation_digest = exact frozen AT0 value
admission_digest = exact frozen AT0 value
serialized-admission SHA-256 = exact frozen AT0 value
```

No GitHub effect transport was invoked.

Result:

`AT2 = PASS`

### AT3 — executor substitution negative: squash

Using the exact valid merge-only admission and a non-mutating capture/spy transport:

```text
caller_method = squash
result = DENY BEFORE TRANSPORT
transport_call_count = 0
```

Result:

`AT3 = PASS`

### AT4 — executor substitution negative: rebase

Using the exact valid merge-only admission and the same non-mutating transport boundary:

```text
caller_method = rebase
result = DENY BEFORE TRANSPORT
transport_call_count = 0
```

Result:

`AT4 = PASS`

### AT5 — live GitHub UI squash negative

The Human-supplied live PR #33 UI evidence after the exact approval showed the single `Merge pull request` action without an alternate merge-method dropdown. Under the exact live merge-only Q_K, `Squash and merge` was not exposed as an executable canonical action.

Result:

`AT5 = PASS`

### AT6 — live GitHub UI rebase negative

The same live PR #33 UI evidence did not expose `Rebase and merge` as an executable canonical action.

Result:

`AT6 = PASS`

### AT7 — direct API-path closure

The live protected-default-branch ruleset targeted `~DEFAULT_BRANCH` and allowed exactly `merge`. GitHub platform semantics for ruleset pull-request merge types therefore supplied the protected-branch API-path method envelope. No destructive unauthorized squash/rebase probe was executed.

Result:

`AT7 = PASS`

### AT8 — changed-decision method negative

Synthetic non-mutating decision tuples naming `squash` and `rebase` were presented to the reviewed broker while Q_K remained merge-only.

Both produced:

`NO ADMISSION`

No Human review was changed or created.

Result:

`AT8 = PASS`

## 7. AT9 — single live merge positive control

Immediately before the live effect, fresh read-only checks established:

- PR #33 remained `OPEN / READY / UNMERGED`;
- candidate HEAD remained `2f2dc1aaa9a775f37e778e8a735cf8ef5b8a9660`;
- complete Human review set remained exact and non-conflicting;
- canonical `main` remained `30095c3170d16263e2db553a2b199bd6e33feace` / TREE `7ba16fab7879d7640801c410f171a08f79c8168b`;
- Q_K remained merge-only at the exact frozen freshness;
- implementation PR #32 remained on exact reviewed HEAD/TREE.

The byte-identical reviewed executor was first run against a capture-only transport. With no caller method override it generated exactly:

```text
repository = FJ899/scriptops
pr = 33
merge_method = merge
expected_head_sha = 2f2dc1aaa9a775f37e778e8a735cf8ef5b8a9660
```

Exactly one connected GitHub live transport call was then issued with that envelope.

GitHub returned:

```text
merged = true
sha = 2f22843ac570498b506101addeba5453ab777f08
message = Pull Request successfully merged
```

No retry, auto-merge, direct ref update, squash, rebase, or second effect path was used.

Result:

`AT9 = PASS`

## 8. AT10 — exact post-effect method truth

Independent read-back after the single AT9 effect established:

```text
PR #33 = MERGED

main HEAD =
2f22843ac570498b506101addeba5453ab777f08

main HEAD TREE =
4215d9306392070e64c6fd74a6cfb813ca9d0601

parent1 =
30095c3170d16263e2db553a2b199bd6e33feace

parent2 =
2f2dc1aaa9a775f37e778e8a735cf8ef5b8a9660
```

The generated canonical commit is therefore a two-parent merge commit with the exact pre-main as parent 1 and the exact candidate as parent 2.

Canonical artifact after effect:

`acceptance/X1D_A5_EFFECT_METHOD_BINDING_LIVE_POSITIVE_CONTROL.md`

Canonical artifact BLOB:

`f02e37a7f97b5b91dd875690de089452853c4e98`

The post-effect canonical TREE equals the exact candidate TREE. Comparing the exact pre-main to the generated merge commit shows exactly one canonical file change: addition of the inert acceptance artifact above. No extra canonical content change was observed.

The GitHub-generated merge commit was verified by GitHub and had the exact expected parent order and TREE.

Q_K remained merge-only after effect with the same exact ruleset freshness and no bypass.

Implementation PR #32 retained exact reviewed HEAD `a80d7714d90213c4f3e5aa514a0119560067dc01` and TREE `31e4ad15bd7257dc95890dafbae41c234d03c431`. Its post-main-advance `mergeable=false` state was observed only as derived state and was not repaired.

Result:

`AT10 = PASS`

`COMMAND SUCCESS != EFFECT TRUTH`

The PASS is based on independent post-effect commit/tree/parent/path/BLOB truth, not on the merge command response alone.

## 9. Final technical disposition

```text
FORMAL AT0 = PASS
AT1 = PASS
AT2 = PASS
AT3 = PASS
AT4 = PASS
AT5 = PASS
AT6 = PASS
AT7 = PASS
AT8 = PASS
AT9 = PASS
AT10 = PASS

X1D-A5 CORRECTIVE TECHNICAL VERIFICATION AT0–AT10 = PASS
```

This is a technical verification record only.

It does not declare the accepted X1D-A5 finding closed.

A separately authorized independent corrective-closure review must assess this frozen evidence against the governing design, and Human closure acceptance remains a subsequent independent gate.

`AT9 PASS != CORRECTIVE CLOSURE`

`AT10 PASS != CORRECTIVE CLOSURE`

`TECHNICAL CORRECTIVE VERIFICATION PASS != HUMAN CLOSURE ACCEPTANCE`

`AI PROPOSES != HUMAN DECIDES`
