# X1D-F001 — T10 DIFFERENTIAL SUPPLEMENTAL AUDIT

Status: SUPPLEMENTAL AUDIT ONLY. Historical PR #71 remains valid and unchanged.

This supplemental audit re-opens only T10 for the exact frozen target recorded by PR #70. It does not rewrite PR #71 and does not authorize Human ACCEPT, X1D-F001 closure, A5, V1, merge, release, deployment, or tag.

## Exact candidate identity

- repository: `FJ899/scriptops`
- PR: `#27`
- base: `30095c3170d16263e2db553a2b199bd6e33feace`
- HEAD: `291cf48a4a6556cfaaee215abc4a47b8ab345d3f`
- TREE: `0b70a929f3035321240bb2aaad56f45ce2a10da9`
- candidate mutation: NONE
- main remained: `30095c3170d16263e2db553a2b199bd6e33feace`

## Preserved prior result

FJ899/8 PR #71 remains the valid historical result:

`BLOCKED at T10 evidence attribution`

Reason at that time: observed `mergeable_state=blocked` could not yet be attributed specifically to missing Human authorization because PR #27 was still DRAFT.

## Newly available differential evidence

### Pre-approval state

For the same candidate HEAD/base after PR #27 became READY and before any submitted review:

- `draft=false`
- submitted reviews: `0`
- `mergeable_state=blocked`
- GitHub UI: `Review required`
- GitHub UI: `Merging is blocked`

### Human authorization event

- principal: `@litrgratis-pixel`
- state: `APPROVED`
- review id: `5061543975`
- submitted_at: `2026-08-30T18:11:58Z`
- bound candidate HEAD: `291cf48a4a6556cfaaee215abc4a47b8ab345d3f`

The observed review event is the established `C_H_APPROVE` realization under the frozen B_AI model.

### Post-approval state

For the same candidate HEAD/base after that approval:

- `draft=false`
- `mergeable_state=clean`
- merge UI enabled
- no merge performed

## Stable enforcement context

ScriptOps main remained exactly:

`30095c3170d16263e2db553a2b199bd6e33feace`

Live ruleset remained:

- name: `CANONICAL_MAIN_PROTECTION_V1`
- id: `21147233`
- enforcement: active
- required approvals: `1`
- require code-owner review: `true`
- require last-push approval: `true`
- bypass actors: `[]`
- current user can bypass: `never`

Base CODEOWNERS remained active and binds `/governance/` to `@litrgratis-pixel`.

## T10 evaluation

T10 asks whether a controlled rule-bearing PR can become merge-eligible without Human authorization.

Observed differential:

`same candidate + READY + zero reviews -> mergeable_state=blocked`

then

`same candidate + @litrgratis-pixel APPROVED -> mergeable_state=clean`

No candidate HEAD, base, main, CODEOWNERS, or ruleset mutation occurred between the compared enforcement states.

Therefore the observed transition is attributable to the established Human authorization event rather than to candidate or policy mutation.

### T10 verdict

`T10 = PASS`

The exact controlled rule-bearing candidate was blocked before the established Human approval and became merge-eligible only after that approval.

No merge was required or performed to establish this differential.

## Resulting T1-T10 verdict

PR #71 established:

- T1 PASS
- T2 PASS
- T3 PASS relative to frozen B_AI
- T4 PASS
- T5 PASS
- T6 PASS
- T7 PASS
- T8 PASS relative to frozen B_AI
- T9 PASS relative to frozen B_AI / C_H_POLICY
- T10 BLOCKED pending attributable differential evidence

This supplement supplies that missing T10 evidence.

Result for the exact frozen target:

`T1-T10 = PASS`

This is an AUDIT PASS only. It is not Human ACCEPT and does not close X1D-F001.

## STOP state

- PR #27: `DO NOT MERGE`
- Human ACCEPT: `NOT DECLARED`
- X1D-F001 closure: `NOT AUTHORIZED`
- X1D-F001: `OPEN`
- A5: `STOP`
- V1: `STOP`
- release/deployment/tag: `NOT AUTHORIZED`
- repair: `NONE`

Historical PR #67 remains the valid FAIL of the previous bootstrap model. Historical PR #71 remains the valid BLOCKED result before the differential evidence became available.