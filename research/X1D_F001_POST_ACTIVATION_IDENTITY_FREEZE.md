# X1D-F001 — POST-ACTIVATION IDENTITY FREEZE

Status: IDENTITY FREEZE ONLY / NO POST-ACTIVATION TEST / NO T1-T10 AUDIT / NO CLOSURE

This artifact records the exact ScriptOps state produced by the one-time Human-root-authorized bootstrap boundary activation performed under the corrected preregistration in FJ899/8 PR #68.

It preserves PR #67 as the valid FAIL of the previous bootstrap model and does not reinterpret any historical result as PASS.

## 1. Activation authorization boundary

Human authorization was explicitly limited to materializing the exact `.github/CODEOWNERS` state from ScriptOps PR #26 onto `main`, with no additional ScriptOps change, ruleset change, A5, V1, release, deployment, tag, or X1D-F001 closure authorization.

The authorization also required an immediate freeze after activation and a STOP before creation of the new controlled rule-bearing PR and before any T1-T10 audit.

## 2. Pre-activation identities

- repository: `FJ899/scriptops`
- pre-activation `main` HEAD: `68a1bb996e1345e2a8f86813042ff7b40109ae74`
- pre-activation `main` TREE: `2001e2c501fc92197e8b59f18693b3bbf6d7e7cd`
- bootstrap PR: `#26`
- bootstrap candidate HEAD: `d7a09cd593094a1846974269c27e4a51ccb831b8`
- bootstrap candidate TREE: `7ba16fab7879d7640801c410f171a08f79c8168b`
- bootstrap changed file: `.github/CODEOWNERS`

Immediately before activation, `main` still matched the preregistered PR #26 base HEAD `68a1bb996e1345e2a8f86813042ff7b40109ae74`.

## 3. Human approval event bound to the exact bootstrap candidate

The activation PR was approved through the established Human approval realization:

- principal: `@litrgratis-pixel`
- review state: `APPROVED`
- review id: `5061392052`
- approved commit: `d7a09cd593094a1846974269c27e4a51ccb831b8`
- submitted_at: `2026-08-30T16:58:29Z`

This section records the observed GitHub event. The governing Human-control interpretation remains the root statement and frozen B_AI model already preregistered in the earlier X1D-F001 artifacts.

## 4. Activation transition

ScriptOps PR #26 was merged with an expected-head guard bound to:

`d7a09cd593094a1846974269c27e4a51ccb831b8`

GitHub reported successful merge.

Resulting merge commit / new `main` HEAD:

`30095c3170d16263e2db553a2b199bd6e33feace`

Merge parents:

- previous `main`: `68a1bb996e1345e2a8f86813042ff7b40109ae74`
- exact bootstrap candidate: `d7a09cd593094a1846974269c27e4a51ccb831b8`

## 5. Exact post-activation ScriptOps identity

Frozen post-activation target:

- repository: `FJ899/scriptops`
- branch: `main`
- HEAD: `30095c3170d16263e2db553a2b199bd6e33feace`
- TREE: `7ba16fab7879d7640801c410f171a08f79c8168b`
- activation PR: `#26`
- PR state after activation: `MERGED / CLOSED`

The resulting `main` TREE equals the prepared bootstrap candidate TREE `7ba16fab7879d7640801c410f171a08f79c8168b`.

## 6. Active CODEOWNERS on main

Exact file:

- path: `.github/CODEOWNERS`
- ref: `30095c3170d16263e2db553a2b199bd6e33feace`
- blob SHA: `5dd686893d265217d921c352df033ff72fdf910e`

Exact content:

```text
# X1D-F001 controlled bootstrap — rule-bearing paths require Human approval authority.
/DECISION_LOG.md @litrgratis-pixel
/phase6/scriptops-v2-hardening.py @litrgratis-pixel
/legacy/scriptops-v2-single.py @litrgratis-pixel
/.github/ @litrgratis-pixel
/governance/ @litrgratis-pixel
```

Therefore the intended CODEOWNERS artifact is now present on the target base branch. This identity freeze does not itself claim T4 PASS; T4 remains reserved for the later independent post-activation audit.

## 7. Exact live ruleset identity/state

Live repository ruleset after activation:

- repository: `FJ899/scriptops`
- name: `CANONICAL_MAIN_PROTECTION_V1`
- id: `21147233`
- source type: `Repository`
- source: `FJ899/scriptops`
- target: `branch`
- enforcement: `active`
- target condition: default branch
- required approving reviews: `1`
- required reviewers: `[]`
- require code-owner review: `true`
- require last-push approval: `true`
- require review-thread resolution: `true`
- bypass actors: `[]`
- connector-observed `current_user_can_bypass`: `never`
- ruleset updated_at: `2026-08-30T18:30:51.689+02:00`

No ruleset mutation was performed during this activation step.

## 8. Intervening-mutation check

Two separate post-activation reads of ScriptOps `main`, taken around the CODEOWNERS/ruleset freeze reads, both returned:

- HEAD `30095c3170d16263e2db553a2b199bd6e33feace`
- TREE `7ba16fab7879d7640801c410f171a08f79c8168b`

No intervening ScriptOps `main` mutation was observed within this freeze-read window.

This is bounded evidence for the recorded freeze window, not a claim that future mutation is impossible.

## 9. Corrected bootstrap state

`BOOTSTRAP CANDIDATE CREATED != BOOTSTRAP BOUNDARY ACTIVATED != POST-BOOTSTRAP ENFORCEMENT VERIFIED`

For the state frozen here:

- `BOOTSTRAP CANDIDATE CREATED = COMPLETE`
- `BOOTSTRAP BOUNDARY ACTIVATED = COMPLETE`
- `POST-BOOTSTRAP ENFORCEMENT VERIFIED = NOT YET TESTED`

The governing rule from PR #68 remains:

`BOOTSTRAP ROOT OF TRUST MAY ESTABLISH THE FIRST BOUNDARY; IT MAY NOT SUBSTITUTE FOR THE BOUNDARY AFTER ACTIVATION.`

## 10. STOP state

This freeze performs no post-activation enforcement test.

No new controlled rule-bearing PR has been created by this artifact.

No T1-T10 audit has been performed against this post-activation state.

Therefore:

- `X1D-F001 = OPEN`
- `X1D-F001 VERIFIED CLOSED = NO`
- `#67 = VALID HISTORICAL FAIL`
- `#26 = MERGED ONLY AS THE AUTHORIZED ONE-TIME BOOTSTRAP ACTIVATION`
- `#25 = STOP`
- `A5 = STOP / NOT EXECUTED`
- `V1 = STOP / NOT AUTHORIZED`

Next step, only if separately authorized under the corrected sequence: create a NEW controlled rule-bearing PR targeting this exact frozen post-activation `main`, then route that new target to an independent T1-T10 audit.
