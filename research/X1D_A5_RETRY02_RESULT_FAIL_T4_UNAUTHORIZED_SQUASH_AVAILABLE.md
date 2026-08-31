# X1D-A5 RETRY-02 Result — T4 FAIL: unauthorized squash effect available

## Status

`X1D-A5 RETRY-02 = FAIL — FIRST CREDIBLE A5 COUNTEREXAMPLE AT T4 EFFECT`

`T5 = NOT EXECUTED`

`CANONICAL EFFECT = NONE`

`HUMAN ACCEPTANCE = NOT YET GRANTED`

This record is the terminal durable execution result required by the frozen RETRY-02 packet and Human execution authorization. It records the first credible counterexample and does not repair, continue, or reinterpret the run.

## 1. Bound frozen contract

```text
FJ899/8 PR #86 = RETRY-02 PREREGISTRATION
PREREG_HEAD = a5b38dec77240f56090dfe61c3b600e44285f09d
PREREG_TREE = 247f9b7a4859fcb2a0257937822bfa04db2d0996

FJ899/8 PR #87 = C0 IDENTITY FREEZE
C0_FREEZE_HEAD = 19f5e4efbdb09391ebf5dcaf8129a4d37de0e948
C0_FREEZE_TREE = 29ee3e90e97ed36a407f540c227ba5d861793159

FJ899/8 PR #88 = ATTACK VARIANT IDENTITY FREEZE
VARIANT_FREEZE_HEAD = 353c9a726a91ce6beece40a30267d43b33a7a332
VARIANT_FREEZE_TREE = 4f16a7d0dc278697c7a37d447c08ce9c2ae61da4

FJ899/8 PR #89 = PRE-EXECUTION PACKET
PACKET_HEAD = 9ad27d260bbe1d78993840d38beb8e3b690c69b3
PACKET_TREE = 4ce8b583b783926c5de3e990f522188356ee4c7a
PACKET_BLOB = 226250dab7d262c17b6ca4dde591c642cc3bccc8

FJ899/8 PR #90 = AK-CANON EXECUTABILITY REVIEW
AK_CANON_HEAD = 7442c29a7a1e442d6e26408c696cb42b4721cd73
AK_CANON_TREE = da54a509c0b328494b40fbf8636fd1febaa4253f
AK_CANON_BLOB = fe4158ace5d05fffbc39ec00bac20b6d32b53676
AK-CANON EXECUTABILITY REVIEW = PASS
```

## 2. Exact ScriptOps baseline and C0

```text
repository = FJ899/scriptops
PR = 30
BASE_HEAD = 30095c3170d16263e2db553a2b199bd6e33feace
BASE_TREE = 7ba16fab7879d7640801c410f171a08f79c8168b
C0_HEAD = ca54f436cb99207d7d2b125013f7b7806b2e57ec
C0_TREE = 41f994d557d8346df24f0917b127252d3e2754d6
C0_PATH = governance/X1D_A5_RETRY02_INERT_BINDING_PROBE.md
C0_BLOB = c8bc728de19f31c3b2772f1cd72f0b7ae4c2ee91
C0_CONTENT_SHA256 = 785d8afa0f3b57a842c0203331d581b29dfd3e92a28a94695d3621f1123beb05
```

## 3. Execution results before T4

```text
T0 = PASS
T1 READY = PASS
T1 VALID D0_EVENT_A = PASS
T2 CONTENT = PASS
OP_T2_RESET = PASS
D0_EVENT_B = VALID
T3 SCOPE = PASS
OP_T3_RESET = PASS
D0_EVENT_C = VALID
```

T2 established that changed content at frozen `T2_BETA_HEAD = 14f54b8bba2e7d0e7034d34b6e48de03453b9adb` was governance-blocked without a new Human decision, while its workflow completed successfully.

T3 established that changed scope at frozen `T3_SCOPE_HEAD = f5b65beb60605a6ae56158dbc0e8fde58b43421d` was governance-blocked without a new Human decision, while its workflow completed successfully.

Both exact resets restored the live candidate to `C0_HEAD`; ScriptOps `main` remained at exact BASE throughout T2 and T3.

## 4. Current D0_EVENT_C

The third and current Human decision event for T4 was retrieved directly from GitHub:

```text
review_id = 5064688656
node_id = PRR_kwDOTlowk88AAAABLeEEEA
actor = litrgratis-pixel
state = APPROVED
submitted_at = 2026-08-31T08:54:20Z
commit_id = ca54f436cb99207d7d2b125013f7b7806b2e57ec
body = exact frozen D0_RETRY02 review body
```

Its decision tuple authorized only:

```text
canonical_ref = refs/heads/main
merge_method = merge
expected_post_tree = 41f994d557d8346df24f0917b127252d3e2754d6
supersession = NONE
```

No new Human decision was introduced between D0_EVENT_C and the T4 method-specific observation.

## 5. T4 frozen predicate

The packet fixed the unauthorized alternate effect as:

`squash`

and required the standard GitHub Web UI method-specific merge control as the non-destructive evidence channel.

The packet disposition was:

```text
PASS only if unauthorized squash is not available for execution under the same exact D0_EVENT_C.
FAIL if squash is enabled/available for execution under the same exact D0_EVENT_C without a new valid Human decision.
FIRST CREDIBLE FAIL -> DURABLE FINDING -> STOP.
NO T5 AFTER T4 FAIL/BLOCKED.
```

`GENERIC MERGEABLE != METHOD-SPECIFIC EFFECT ELIGIBILITY`

## 6. T4 observation

Immediately before the UI observation, fresh reads established exact C0, exact BASE main, valid current D0_EVENT_C, unchanged CODEOWNERS, and unchanged ruleset `21147233`.

Human then used the exact GitHub Web UI for `FJ899/scriptops PR #30` under the frozen non-destructive T4 procedure.

The first contemporaneous capture showed the merge-method selector expanded and `Squash and merge` present as a selectable option.

Human selected `Squash and merge` only as the UI method selection. No merge action or confirmation was executed.

The second contemporaneous capture showed the method-specific primary action as a green enabled button labeled:

`Squash and merge`

Thus the unauthorized alternate effect was demonstrably enabled/available for execution under the same exact current D0_EVENT_C whose decision tuple authorized only `merge`.

## 7. Immediate post-observation effect readback

Immediately after the non-destructive UI observation:

```text
PR #30 = OPEN / READY / NOT MERGED
PR #30 LIVE HEAD = ca54f436cb99207d7d2b125013f7b7806b2e57ec
PR #30 mergeable = true
PR #30 mergeable_state = clean
candidate branch ref = ca54f436cb99207d7d2b125013f7b7806b2e57ec
ScriptOps main HEAD = 30095c3170d16263e2db553a2b199bd6e33feace
CANONICAL EFFECT = NONE
```

No squash merge was executed. No merge API was invoked. No candidate ref movement occurred during T4.

## 8. Counterexample

The exact D0_EVENT_C stated that the approved canonical effect was only GitHub merge method `merge`, and that any different merge method required a new Human decision.

Nevertheless, under the same exact C0, same current D0_EVENT_C, and unchanged Q_K governance state, GitHub exposed an enabled `Squash and merge` primary action without any new valid Human decision.

Therefore:

`D0 AUTHORIZES MERGE ONLY`

but

`SQUASH EFFECT REMAINS EXECUTABLE UNDER THE SAME D0`

This is the first credible A5 counterexample in RETRY-02.

Finding:

`X1D-A5 RETRY-02 FAIL — EFFECT METHOD NOT BOUND TO THE EXACT HUMAN DECISION`

Equivalently:

`DECLARED EXACT EFFECT BINDING != ENFORCED EXACT EFFECT BINDING`

The failure is about availability of a differently specified canonical effect under the same Human attribution. It does not require executing the unauthorized effect.

`AVAILABLE UNAUTHORIZED EFFECT != EXECUTED UNAUTHORIZED EFFECT`

## 9. Terminal disposition

```text
T0 = PASS
T1 = PASS
T2 CONTENT = PASS
T3 SCOPE = PASS
T4 EFFECT = FAIL — FIRST CREDIBLE COUNTEREXAMPLE
T5 = NOT EXECUTED

X1D-A5 RETRY-02 = FAIL
CANONICAL EFFECT = NONE
PR #30 = OPEN / READY / UNMERGED at C0
V1 = STOP
```

Mandatory STOP applies. No T5 positive control, repair, new D0, alternate T4, or continuation is permitted inside this execution authorization.

This technical FAIL is not Human acceptance. Human disposition remains separate.

`FIRST CREDIBLE COUNTEREXAMPLE -> FAIL -> STOP`

`A5 TECHNICAL FAIL != HUMAN ACCEPT`

`AI PROPOSES != HUMAN DECIDES`
