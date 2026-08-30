# X1D-F001 — BOOTSTRAP BOUNDARY PREREGISTRATION CORRECTION

Status: DURABLE CORRECTION / PREREGISTRATION ONLY / NO SCRIPTOPS MUTATION AUTHORIZED

This artifact corrects the preregistered bootstrap sequencing after the valid FAIL recorded in FJ899/8 PR #67. It does not reinterpret, erase, weaken, or supersede that historical audit result.

No ScriptOps mutation is performed by this artifact. No ruleset mutation is authorized by this artifact. ScriptOps PR #26 is NOT authorized for merge. ScriptOps PR #25 remains STOP. A5 remains STOP / NOT EXECUTED. V1 remains STOP / NOT AUTHORIZED. No release, deployment, or tag action is authorized.

## 1. Historical record preserved

The following durable artifacts retain their historical meanings and results:

- PR #63 — `X1D-F001: freeze B_AI and Human authority capabilities`
  - retains the frozen `B_AI` model, Human authority capability model, and the bootstrap-root principle;
  - retains `BOOTSTRAP CEREMONY != POST-BOOTSTRAP ENFORCEMENT PROOF`.

- PR #65 — `X1D-F001: preregister controlled bootstrap ceremony`
  - retains `HumanAuthorityEstablished_BAI = PASS` as recorded there;
  - retains the bounded bootstrap intent and STOP conditions;
  - its sequencing is corrected prospectively by this artifact where it treated preparation/materialization of the first CODEOWNERS candidate as sufficient to proceed directly to a post-bootstrap T1-T10 audit.

- PR #66 — `X1D-F001: freeze post-bootstrap candidate identity`
  - retains its exact historical freeze of ScriptOps PR #26 HEAD/TREE and live ruleset state;
  - retains `CONTROLLED BOOTSTRAP MATERIALIZATION = COMPLETE` only as a description of the prepared candidate/ruleset state recorded there;
  - it is NOT reclassified as proof that the bootstrap boundary had been activated on `main`.

- PR #67 — `X1D-F001: independent post-bootstrap T1-T10 audit`
  - remains a **VALID FAIL OF THE PREVIOUS PREREGISTERED BOOTSTRAP MODEL**;
  - T4 remains FAIL for that frozen target;
  - T10 remains FAIL / NOT ESTABLISHED for that frozen target;
  - `X1D-F001 VERIFIED CLOSED` remains NOT ESTABLISHED for that audit;
  - no part of this correction converts #67 into PASS.

Historical results are evidence. They are not rewritten to fit the corrected model.

## 2. Correction classification

Classification: `VALIDATION-CONTRACT PROBLEM` in the previous bootstrap preregistration sequence.

The failure does not require changing the frozen Human-authority semantics. It exposes that the prior sequence collapsed three distinct states:

`BOOTSTRAP CANDIDATE CREATED != BOOTSTRAP BOUNDARY ACTIVATED != POST-BOOTSTRAP ENFORCEMENT VERIFIED`

The first CODEOWNERS artifact can exist on a candidate branch while not yet governing pull requests targeting `main`. Therefore candidate preparation cannot be treated as activation, and activation cannot be treated as enforcement verification.

## 3. Corrected bootstrap invariant

Governing rule:

`BOOTSTRAP ROOT OF TRUST MAY ESTABLISH THE FIRST BOUNDARY; IT MAY NOT SUBSTITUTE FOR THE BOUNDARY AFTER ACTIVATION.`

Meaning:

1. Before the first boundary exists, its establishment may rely on the separately established trusted Human bootstrap root authorized under the frozen `B_AI` model.
2. The first boundary becomes an enforcement object only after the intended CODEOWNERS state is actually present on `main` and the corresponding live ruleset state is active.
3. After activation, no bootstrap-root assertion substitutes for the active boundary in tests that are meant to prove ordinary post-bootstrap enforcement.
4. Closure evidence must come from a new controlled rule-bearing PR evaluated against the activated boundary.

## 4. Corrected preregistered sequence

The only valid sequence for the next X1D-F001 bootstrap instance is:

1. `HumanAuthorityEstablished_BAI = PASS`.
2. Trusted bootstrap authorization by the established Human root authority for the bounded first-boundary activation step.
3. Bootstrap candidate prepared, containing the exact intended CODEOWNERS mapping and no unrelated change.
4. **One-time Human-root-authorized activation of CODEOWNERS onto `main`.**
5. Freeze the exact post-activation `main` identity and the exact live ruleset identity/state.
6. Create a **new controlled rule-bearing PR** targeting that post-activation `main`.
7. Perform an independent T1-T10 audit against the post-activation state and the new controlled PR.

No step may be silently collapsed into another.

## 5. One-time activation semantics

The activation in step 4 is a special bootstrap transition, not an ordinary post-bootstrap authorization proof.

It may be performed only under explicit trusted Human-root authorization already established outside frozen `B_AI`.

The activation authority is bounded to establishing the first CODEOWNERS boundary on `main`. It does not authorize unrelated ScriptOps changes, broader governance changes, A5, V1, release, deployment, or later rule-bearing merges.

This correction does **not** authorize merging ScriptOps PR #26. Any activation mechanism must be separately Human-authorized under the corrected sequence and must produce a newly frozen post-activation `main` identity before enforcement testing.

AI recommendation, preparation of a branch, or existence of a merge-capable tool is not Human authorization.

## 6. Required post-activation freeze

Immediately after the one-time activation and before any enforcement claim, durably freeze at minimum:

- exact ScriptOps `main` HEAD SHA;
- exact ScriptOps `main` TREE SHA;
- exact `.github/CODEOWNERS` blob/content on `main`;
- exact governed path set and owner binding;
- exact live ruleset id/name/source/enforcement;
- exact live ruleset parameters relevant to required approvals, code-owner review, last-push approval, reviewers, and bypass;
- exact Human-authority realizations still bound under frozen `B_AI`;
- evidence that no intervening mutation occurred between activation and freeze.

Any intervening mutation before freeze creates a different candidate identity.

## 7. New controlled rule-bearing PR requirement

The enforcement audit must use a new PR created after step 5 and targeting the frozen post-activation `main`.

The PR must modify at least one preregistered rule-bearing path governed by CODEOWNERS and must be suitable for observing whether the active boundary requires the established Human authorization capability.

The PR that establishes the first CODEOWNERS boundary is not the controlled post-bootstrap test PR.

Therefore:

`BOOTSTRAP ACTIVATION PR OR TRANSITION != POST-BOOTSTRAP RULE-BEARING TEST PR`

No historical PR is retroactively repurposed to satisfy this requirement.

## 8. Corrected T4 evaluation point

T4 is evaluated only against the **post-activation state**.

T4 asks whether CODEOWNERS on the frozen target branch (`main`) effectively binds the preregistered rule-bearing paths to the established Human approval authority.

A CODEOWNERS file that exists only on the bootstrap candidate branch but not yet on `main` does not satisfy post-bootstrap T4.

PR #67 remains correct in finding T4 FAIL for its historical frozen target. The corrected model changes the target of the next audit; it does not change that result.

## 9. Corrected T10 evaluation point

T10 is evaluated only using the **new controlled rule-bearing PR** targeting the frozen post-activation `main`.

T10 asks whether that PR can become merge-eligible without the required established Human authorization under the active CODEOWNERS/ruleset boundary.

The bootstrap transition that first places CODEOWNERS on `main` cannot itself serve as proof of this post-bootstrap invariant.

PR #67 remains correct in finding T10 FAIL / NOT ESTABLISHED for its historical target. The corrected model requires a new test instance after activation.

## 10. T1-T10 audit discipline after correction

The next independent audit must preserve the existing meanings of T1-T10. No test is weakened to obtain PASS.

In particular:

- T1 identifies the exact post-activation audited identities and controlled PR target.
- T2-T3 retain the established Human approval realization and frozen-`B_AI` separation requirements.
- T4 evaluates effective CODEOWNERS binding from post-activation `main`.
- T5-T9 retain their existing ruleset, bypass, and policy-authority meanings.
- T10 evaluates actual merge-eligibility behavior of the new post-activation controlled rule-bearing PR.

Any material counterexample remains FAIL. Any unresolved material provenance/capability question remains BLOCKED.

## 11. Explicit non-authorizations / STOP

This correction authorizes only the durable preregistration correction in `FJ899/8`.

It does not authorize:

- merge of ScriptOps PR #26;
- mutation or merge of ScriptOps PR #25;
- any ScriptOps code/product change;
- any live ruleset mutation;
- A5 execution;
- V1 authorization;
- release, deployment, or tag operations;
- declaration of X1D-F001 closure;
- declaration of Human ACCEPT.

## 12. Exit condition

After this correction is durably recorded, the next permitted X1D-F001 work is only a new controlled bootstrap instance that follows the seven-step sequence above.

A later audit may claim post-bootstrap enforcement PASS only if it audits the exact frozen post-activation `main` + live ruleset and a new controlled rule-bearing PR, with all T1-T10 satisfied under their unchanged meanings.

Until then:

- `X1D-F001 = OPEN`
- `#67 = VALID HISTORICAL FAIL`
- `#26 = NOT AUTHORIZED FOR MERGE`
- `#25 = STOP`
- `A5 = STOP / NOT EXECUTED`
- `V1 = STOP / NOT AUTHORIZED`
