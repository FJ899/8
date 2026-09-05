# X1B-FRAME F001 — Superseding Plan Review — First Finding F002

Status: `PLAN REVIEW FAIL / FIRST CREDIBLE COUNTEREXAMPLE / STOP / NO PLAN-REPAIR AUTHORITY`

Date: `2026-09-04`

## 1. Exact review target and authority

Superseding plan under review:

```text
FJ899/8 PR #187
HEAD = 1ceb7a7d56437d794a0f2eb280f98eeb92e40026
TREE = 7b34f50a01bb4b27b2c8eb89915fd27b5f586a3f
PATH = research/X1B_FRAME_F001_SUPERSEDING_STATUS_PROPAGATION_PLAN_REOPEN_PLAN_F001_2026-09-04.md
BLOB = d7744c1cc2a51e9bcb17e5b9a95ded3bebcaef1c
```

The earlier review was paused after an evidence-main tooling incident. Human recovery acceptance and resume authority are recorded in:

```text
FJ899/8 PR #189
HEAD = 730989c1c2d7b994245590e5a2da4fe201e1f1ad
HUMAN RESPONSE = accept
```

Accepted evidence-main re-anchor for this resumed review:

```text
FJ899/8 refs/heads/main
HEAD = 0b516edb210fd4029972e932fec0206d8a6df1cb
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

The resumed review is exactly one independent read-only review of unchanged PR #187.

Review rule:

```text
FIRST CREDIBLE COUNTEREXAMPLE = DURABLE FINDING + STOP
```

## 2. First credible counterexample

```text
X1B-FRAME-F001-PLAN-F002 — BOOLEAN ACTIVE_PRODUCT_REMEDIATED=NO
COLLAPSES "NOT YET ESTABLISHED" INTO "FALSE" AND THE PLAN EXPLICITLY
ALLOWS THAT FALSE CURRENT-STATE CLAIM TO PERSIST AFTER A FUTURE V2
RUNTIME INTEGRATION UNTIL A LATER STATUS-PROMOTION PROCEDURE
```

Primary classification:

```text
STATUS SEMANTIC COLLAPSE
NOT ESTABLISHED != FALSE
```

Preregistered review attack classes reached by this finding:

```text
P4 — is the current plan safely conservative if runtime changes but status remains NO?
P7 — can active-main currentness be confused with last-observed provenance?
```

No further P1-P8 attack discovery is performed after this first credible counterexample.

## 3. Why this is a plan blocker

The plan correctly repairs the earlier PR-local false-positive path by forbidding the offline verifier from establishing:

```text
X1B_ACTIVE_PRODUCT_REMEDIATED = YES
```

However, it then freezes the authoritative current-state field as:

```text
X1B_ACTIVE_PRODUCT_REMEDIATED: NO
```

and explicitly states:

```text
The current status may conservatively remain NO even after a future runtime
integration until a separately authorized post-activation/currentness procedure
promotes it.

A conservative false negative is allowed.
A premature false positive is not.
```

The required Human-readable README wording is stronger still:

```text
The active ScriptOps product is not X1B-remediated.
```

Therefore the plan intentionally permits a future state in which:

```text
actual refs/heads/main may contain the V2 runtime
BUT
current authoritative docs continue to assert
X1B_ACTIVE_PRODUCT_REMEDIATED = NO
and
"The active ScriptOps product is not X1B-remediated"
```

until a later evidence/acceptance/promotion sequence completes.

That is not merely a conservative absence of a positive claim. It is an explicit negative factual claim about the active product.

## 4. Minimal counterexample trace

The plan itself defines the future transition ordering:

```text
1. integrate a separately reviewed V2 runtime candidate into refs/heads/main
   WITHOUT pre-claiming active remediation YES;
2. perform external post-activation readback;
3. bind active-main identity to expected V2 runtime identity;
4. freeze durable activation/currentness evidence;
5. obtain Human acceptance;
6. only then prepare a later status-promotion candidate that may propose YES.
```

Now consider the interval immediately after step 1 and before steps 2-6.

By the plan's own rule, the current-state surfaces are allowed to remain:

```text
X1B_ACTIVE_PRODUCT_REMEDIATED: NO
X1B_ACTIVE_RUNTIME_LAST_OBSERVED_CLASS: LEGACY_PRE_X1B
```

while the actual active default branch may already contain the V2 runtime.

The plan even requires the current verifier to fail closed if its checkout contains V2 under the legacy-bound contract, which correctly prevents a PR-local `YES`; but it does not prevent the already-published current-state documents from retaining the categorical `NO` assertion after the active branch changes.

Thus the plan creates this semantic collapse:

```text
POST-ACTIVATION EVIDENCE NOT YET HUMAN-ACCEPTED
=>
ACTIVE PRODUCT REMEDIATED = NO
```

when the only justified epistemic statement is bounded to something like:

```text
ACTIVE PRODUCT REMEDIATION = NOT YET ESTABLISHED / NOT YET PROMOTED
```

The distinction matters because:

```text
LACK OF ACCEPTED CURRENTNESS EVIDENCE
!=
EVIDENCE THAT THE ACTIVE PRODUCT IS NOT REMEDIATED
```

## 5. Current baseline does not save the plan

At review time, the independently re-read active ScriptOps default branch is still:

```text
FJ899/scriptops refs/heads/main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
```

and the active runtime is presently legacy/pre-X1B.

So `NO` is defensible for the current exact baseline.

The blocker is not the present value. The blocker is the plan's frozen semantics for the future transition that it explicitly specifies and expects the correction to survive.

A status-propagation correction cannot claim durable current-state truth while intentionally allowing an authoritative boolean negative to become false after the branch changes.

## 6. Violated frame invariant

The frame work began from:

```text
X1B CLOSED != ACTIVE PRODUCT REMEDIATED
```

The superseding plan correctly protects against one unsafe collapse:

```text
PR/CHECKOUT V2 != ACTIVE PRODUCT REMEDIATED YES
```

but introduces a second collapse:

```text
ACTIVE PRODUCT REMEDIATION NOT YET ESTABLISHED
=
ACTIVE PRODUCT REMEDIATED NO
```

That is not equivalent.

A current-state surface may be conservative about authority, but it must remain semantically truthful about what is known versus what is false.

## 7. Why this is not an X1B property reopen

```text
X1B PROPERTY FALSIFIED = NO
X1B CLOSURE REOPENED = NO
```

This finding concerns the status model around deployment/currentness after the already-accepted X1B corrective research closure.

It does not challenge:

```text
PR #35 runtime/security review result
the X1B corrective verification
the Human corrective-closure acceptance
```

It challenges only the superseding frame/status correction plan's proposed boolean semantics.

## 8. Review disposition

```text
X1B-FRAME F001 SUPERSEDING PLAN REVIEW = FAIL
X1B-FRAME-F001-PLAN-F002 = OPEN
FIRST CREDIBLE COUNTEREXAMPLE = STOP
PR #187 = NOT PASS
SCRIPTOPS IMPLEMENTATION AUTHORITY = NO
PR #35 MERGE AUTHORITY = NO
DEPLOYMENT / RELEASE / TAG = NO
V1 AUTHORITY = NO
X1B = REMAINS CLOSED AT ACCEPTED RESEARCH/CORRECTIVE SCOPE
```

This finding authorizes no plan repair and no ScriptOps mutation.

The next legal stage is a separate Human disposition of this exact finding. Only after such acceptance may one bounded superseding-plan repair be prepared.

Preserve:

```text
NOT ESTABLISHED != FALSE
CHECKED_OUT_RUNTIME_CLASS != ACTIVE_PRODUCT_STATE
PLAN REVIEW FINDING != PLAN-REPAIR AUTHORITY
PLAN REVIEW PASS != IMPLEMENTATION AUTHORITY
AI PROPOSES != HUMAN DECIDES
```
