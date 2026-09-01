# X1B Human Decision Authorship Implementation Brief — Independent AK-CANON Review

Status: `INDEPENDENT IMPLEMENTATION-BRIEF REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: 2026-09-01

Verdict:

`AK-CANON X1B IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

This review is bound only to the Human-authorized exact artifacts and current live baseline below. It does not modify or repair PR #110 and does not authorize implementation, Human decision creation, canonical effect, merge, X1B closure, Agency Kernel v1, release, deployment, or tag.

`REVIEW FINDING != REPAIR AUTHORITY`

`IMPLEMENTATION-BRIEF REVIEW NOT PASS != IMPLEMENTATION AUTHORITY`

`X1B OPEN != V1 AUTHORITY`

`AI PROPOSES != HUMAN DECIDES`

## 1. Frozen review target

Repository: `FJ899/8`

PR: `#110`

Review-time state: `OPEN / DRAFT / UNMERGED`

BASE: `b2c92ec5cd8fbb7272d701d229adc8a8019f951e`

HEAD: `8eaad5ea3c37b2cdc65ad80d16260bbf0f2a0160`

TREE: `a7978803db0e1f0f87fb84ac54f44b8c5bc33a09`

PATH: `research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF.md`

BLOB: `385bcc8620619b91986ff44211a428913b228ba2`

Complete BASE->HEAD changed-file set:

```text
research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF.md
```

Exactly one changed path was independently reconfirmed.

## 2. Bound normative corrective design

Repository: `FJ899/scriptops`

PR: `#34`

Review-time state: `OPEN / DRAFT / UNMERGED`

HEAD: `d7a5065c87e9a4b49fb608235c908bceac42b4b1`

TREE: `3140d0ac95c120a7b1532942bae2e0dad38b4839`

PATH: `governance/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_CANDIDATE.md`

BLOB: `dac16f109d1414a2208c2ed9a166ae9e9a329216`

The design requires, among other things:

```text
separate Human decision act
-> trusted Human decision evidence
-> independent validation/admission
-> authorized effect
```

and preserves:

```text
AI/PROCESS EFFECT CAPABILITY != HUMAN DECISION-AUTHORITY CAPABILITY
POSSESSION OF EFFECT CAPABILITY != AUTHORITY TO CREATE HUMAN DECISION EVIDENCE
SHAPE MATCH != TRUSTED ORIGIN
```

## 3. Bound independent design review

Repository: `FJ899/8`

PR: `#109`

Review-time state: `OPEN / DRAFT / UNMERGED`

HEAD: `132d65be48331a822039262b707c47a81d02a64d`

TREE: `a8bdc363d293beb7b15ae8b787cc3ebdd694fd99`

PATH: `research/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_DESIGN_AK_CANON_REVIEW_R2.md`

BLOB: `439109e104244552a5ac1f3f08988dba283733d0`

Verdict: `AK-CANON X1B CORRECTIVE DESIGN REVIEW R2 = PASS`

The historical pre-existing `d7c28ce...` review-like artifact is not treated as normative authority.

## 4. Current real-defect baseline reconfirmed

Immediately before durable review write, canonical ScriptOps `main` was independently re-read as:

HEAD: `2f22843ac570498b506101addeba5453ab777f08`

TREE: `4215d9306392070e64c6fd74a6cfb813ca9d0601`

Affected path: `phase6/scriptops-v2-hardening.py`

BLOB: `4f379960ed5677634dd234af6aa39626782b6133`

The accepted X1B defect premise remains materially present. The live `cmd_approve` path still accepts caller `--why`, performs the canonical scene write, and records hard-coded `"approver": "human"` without separately validated Human decision evidence.

Therefore this review concerns the same accepted X1B defect, not a substituted defect.

## 5. Independent adversarial review result

The brief contains substantial correct binding work: deterministic request hashing, current PR-head binding, strict review-body syntax, complete review pagination intent, explicit conflict handling, in-memory admission, removal of caller `--why` as Human authority, evidence-derived durable attribution, and a real Human positive-control requirement.

Those strengths are insufficient for PASS because concrete executable and authority-contract gaps remain.

## 6. Finding X1B-IBR-F001 — untouched direct legacy acceptance path remains effect-capable

Classification: `IMPLEMENTATION BLOCKER`

The frozen ScriptOps baseline contains a directly executable `legacy/scriptops-v2-single.py` with its own `approve --scene` command. That command:

1. resolves a staged candidate;
2. writes the canonical `scenes/<scene_id>.fountain` target as accepted;
3. appends a durable decision record with hard-coded `"approver": "human"`;
4. commits the effect;
5. requires no separate Human decision evidence.

PR #110 explicitly states that `legacy/scriptops-v2-single.py` remains unchanged under the intended implementation candidate and limits the planned implementation surface to:

```text
phase6/scriptops-v2-hardening.py
phase6/x1b_human_decision.py
tests/test_x1b_human_decision.py
.github/workflows/x1b-human-decision.yml
```

The brief also states that there is to be no alternate effect path, but it does not make the already-existing legacy acceptance entry point non-operative, unreachable, or incapable of canonical effect.

Concrete counterexample path:

```text
AI/process with local ScriptOps effect capability
-> directly invoke legacy/scriptops-v2-single.py approve --scene <SCENE>
-> canonical scene write
-> durable approver="human"
-> commit
without HumanDecisionRequestV1
without GitHub Human review
without HumanDecisionAdmissionV1
```

This is sufficient by itself to make the implementation brief `NOT PASS`.

The review does not authorize a repair or choose whether the legacy path must be removed, gated, made non-effect-capable, or otherwise controlled.

## 7. Finding X1B-IBR-F002 — Human-review trusted origin is asserted by capability discipline but not fully established by the verifier contract

Classification: `VALIDATION-CONTRACT PROBLEM`

The brief correctly states that the effect process must not possess GitHub capability to create or alter the Human review and that the positive Human control uses a manual GitHub UI review. However, the production evidence verifier consumes GitHub review metadata consisting of actor/state/commit/body/timestamps and does not define a machine-verifiable property that distinguishes a manually created Human UI review from a review created through another write-capable path under the same authoritative account.

The brief partly scopes this by requiring credential separation, but credential provisioning is declared outside the implementation and the implementation contract does not specify a fail-closed runtime control proving that the ScriptOps process cannot inherit or obtain a write-capable GitHub credential.

Therefore a GitHub username plus a review-shaped event remains insufficient by itself to establish the exact required Human act unless the deployment/capability boundary is frozen and independently evidenced.

This is material because the frozen design explicitly requires trusted Human-authoritative origin and says a username/account label alone is insufficient.

## 8. Finding X1B-IBR-F003 — decision-request artifact creation, location, and selection remain under-specified

Classification: `VALIDATION-CONTRACT PROBLEM`

The brief requires a `HumanDecisionRequestV1` committed on a dedicated ScriptOps decision-request branch and presented in a dedicated decision PR, but it does not freeze:

- the exact repository path or deterministic path derivation for the request artifact;
- whether exactly one request artifact may exist in the decision PR;
- who or which bounded process creates the decision-request branch and PR;
- the exact selection rule by which `request_file_path` is chosen;
- the exact changed-file contract for the decision PR;
- the lifecycle rule preventing an attacker from supplying a different caller-selected request file that is internally self-consistent.

The verifier snapshot contains caller/adapter-visible `request_file_path` and the PR contract says the PR HEAD must contain the request object selected by the caller/operation. Without a frozen deterministic path/selection contract, core trusted-origin and substitution semantics are left for implementation invention.

Because the Human review body binds the digest of whichever request object becomes selected, request-file selection is part of the authority boundary and cannot remain implicit.

## 9. Finding X1B-IBR-F004 — replay/consumption is only local and does not establish one-Human-event/one-canonical-effect semantics

Classification: `VALIDATION-CONTRACT PROBLEM`

The brief states:

```text
one decision_request_id may authorize at most one successful canonical ScriptOps acceptance effect
```

but defines consumption by checking only the current local decision log and then recording the request ID in that same local repository state.

No cross-clone, cross-worktree, or canonical shared consumption authority is defined. Two isolated clones at the same pre-effect HEAD can each observe the same still-valid GitHub Human review and each see no local prior consumption, causing the same Human event to authorize two acceptance effects in separate execution instances.

The brief explicitly uses isolated/disposable clones/worktrees for the positive control, so clone-locality is not merely hypothetical.

The contract therefore overclaims global one-shot semantics relative to the mechanism actually specified. Either the scope of one-shot consumption must be explicitly bounded to a single canonical execution state, or a shared authoritative consumption mechanism must be defined. This review does not choose a repair.

## 10. Finding X1B-IBR-F005 — effect-process GitHub credential inheritance is prohibited normatively but not made enforceably fail-closed

Classification: `IMPLEMENTATION BLOCKER`

The brief says the verifier/effect command must not be provisioned with write-capable GitHub credentials and may consume a read-only credential out of band. It does not specify:

- how inherited environment credentials are excluded;
- how credential helpers or ambient GitHub credentials are excluded;
- how the production adapter proves read-only capability rather than merely promising read-only method usage;
- what exact startup/pre-effect check fails closed if a write-capable credential is present;
- what evidence demonstrates separation during corrective verification.

Therefore the proposed implementation can satisfy the code-interface shape while the effect-capable process still inherits a credential capable of creating the Human review it later consumes.

This directly affects the selected mechanism’s core origin property and cannot be left to deployment convention in a brief that is supposed to authorize a bounded implementation.

## 11. Required review questions

1. **Does the selected GitHub-review mechanism satisfy the frozen property rather than merely relying on a GitHub username?**  
`NOT YET.` Exact binding is strong, but trusted Human-act origin remains dependent on capability assumptions not fully evidenced by the verifier/deployment contract. See F002/F005.

2. **Is the effect-capable ScriptOps process actually separated from Human review-creation authority?**  
`NOT FULLY SPECIFIED.` The brief requires separation but does not freeze enforceable exclusion of ambient/write-capable credentials. See F005.

3. **Is the read-only adapter boundary concrete enough that production code cannot accept caller-created trusted snapshots?**  
`LARGELY YES IN-PROCESS.` Caller-created production snapshots are prohibited and test fakes are scoped to tests. This does not cure credential-origin gaps or the legacy bypass.

4. **Is HumanDecisionRequestV1 deterministic and strongly bound to exact content, scope, candidate, impact, canonical target and effect?**  
`YES FOR THE SELECTED OBJECT.` Payload and digest binding are strong. Request-file selection/origin remains under-specified. See F003.

5. **Are request-digest and decision_request_id derivations non-circular and reproducible?**  
`YES.` Digest is over the binding payload; derived ID and stored digest are then checked against recomputation.

6. **Is the decision PR lifecycle sufficiently exact, including current HEAD binding?**  
`PARTLY.` Current HEAD and review commit binding are explicit. Request artifact path/creation/changed-file lifecycle is not exact enough. See F003.

7. **Is the review-body parser deterministic and resistant to extra/malformed fields?**  
`YES AT CONTRACT LEVEL.` Exact four-line body, LF, no extras, bounded rationale.

8. **Is Human rationale derived only from the bound Human review?**  
`YES ON THE NEW PATH.` Caller `--why` is excluded from Human rationale. The untouched legacy path still manufactures Human attribution without this evidence. See F001.

9. **Are complete pagination and review-set completeness specified fail-closed?**  
`YES AT CONTRACT LEVEL.` Full pagination, duplicate rejection, and read failure -> deny/block are explicit.

10. **Are review states, duplicates, actors and chronology handled without hidden latest-wins assumptions?**  
`MOSTLY YES.` One current-head active APPROVED, zero other decision-bearing authoritative-Human reviews, no chronology-only winner. Unknown states fail closed.

11. **Can old approval, wrong commit, changed PR HEAD, changed candidate or changed impact become operative?**  
`DENIED ON THE NEW PATH.` Exact local/head/digest/hash bindings address these cases.

12. **Is replay/consumption strong enough to prevent one Human event authorizing multiple canonical effects?**  
`NO.` Consumption is local-repository-state based and is not cross-clone authoritative. See F004.

13. **Does one-shot admission prevent caller/executor substitution after Human review?**  
`YES ON THE NEW PATH, SUBJECT TO IMPLEMENTATION.` Admission fields are bound and caller override is prohibited.

14. **Is removal of --why as Human authority sufficient to close the original real cmd_approve regression?**  
`NO.` It closes the hardening-shim regression only if that is the sole effect path. The direct legacy approve path remains effect-capable. See F001.

15. **Is durable human_actor/rationale/review attribution genuinely evidence-derived?**  
`YES ON THE NEW PATH.` Not system-wide while the legacy bypass remains.

16. **Are all ten original attacks plus the real counterexample executable as future regressions?**  
`THE MATRIX EXISTS, BUT IT OMITS THE DIRECT LEGACY BYPASS AS A REQUIRED EFFECT-PATH REGRESSION.` Therefore insufficient.

17. **Do additional negative controls cover malformed, incomplete, conflicting, wrong-actor and wrong-binding evidence?**  
`YES, SUBSTANTIALLY.`

18. **Is the real positive control genuinely Human-created and isolated from user screenplay canon?**  
`PROCEDURALLY REQUIRED, YES.` Its Human-created character still depends on capability assumptions noted in F002/F005.

19. **Does CI avoid Human review-write credentials and live Human decision creation?**  
`YES BY CONTRACT.`

20. **Are implementation surfaces sufficient and minimal?**  
`NO.` The explicit exclusion of `legacy/scriptops-v2-single.py` leaves a direct false-Human-decision effect path. See F001.

21. **Is decision-request artifact creation/location/lifecycle specified enough to implement without inventing security semantics?**  
`NO.` See F003.

22. **Does omitted request-file/path-selection create substitution ambiguity?**  
`YES.` See F003.

23. **Are cross-system admission/revocation semantics explicit without falsely claiming atomic GitHub/filesystem revocation?**  
`YES FOR POST-ADMISSION REVOCATION.` The brief correctly disclaims distributed atomic revocation. That does not solve cross-clone replay consumption. See F004.

24. **Could the ScriptOps process obtain or inherit write-capable GitHub credential?**  
`THE BRIEF DOES NOT CLOSE THIS.` It prohibits such provisioning but does not define enforceable fail-closed exclusion of inherited/ambient write capability. See F005.

25. **Does any caller-controlled field still become Human-attributed state?**  
`NOT ON THE NEW ADMISSION PATH AS WRITTEN.` The direct legacy path still creates Human-attributed state without any Human evidence. See F001.

26. **Is the brief precise enough for bounded implementation authorization without implementer invention of a core authority rule?**  
`NO.` F001, F003, F004 and F005 require security-semantic choices beyond ordinary implementation detail.

27. **Does the brief preserve X1B OPEN != V1 AUTHORITY?**  
`YES.` It repeatedly preserves `X1B REMAINS OPEN`, `IMPLEMENTATION BRIEF PASS != X1B CLOSED`, and `X1B CLOSED != V1 AUTHORITY`.

## 12. Verdict

`AK-CANON X1B IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

Minimum decisive basis:

```text
F001 direct legacy false-Human-decision effect path remains in the authorized implementation surface model
+
F003 request-artifact path/selection/lifecycle authority semantics are not frozen
+
F004 replay consumption does not establish one Human event -> one canonical effect across execution instances
+
F005 Human-review creation capability separation is not enforceably fail-closed against ambient/inherited credentials
```

F002 additionally records the trusted-origin validation gap between “manual Human UI act” and metadata available to the production verifier.

No correction is authorized or supplied.

## 13. STOP boundary

Do not implement from PR #110 under this review result.

Do not modify PR #110 under this authorization.

Do not modify ScriptOps.

Do not create a Human decision PR or Human APPROVE.

Do not perform corrective verification or canonical scene effect.

Do not merge, close X1B, begin V1 work, release, deploy, or tag.

A separate Human authorization is required for any correction or superseding implementation brief.

`REVIEW FINDING != REPAIR AUTHORITY`

`IMPLEMENTATION-BRIEF REVIEW NOT PASS != IMPLEMENTATION AUTHORITY`

`AI PROPOSES != HUMAN DECIDES`

`STOP`
