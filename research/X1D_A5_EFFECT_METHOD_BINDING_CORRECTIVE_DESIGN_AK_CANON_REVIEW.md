# X1D-A5 Effect-Method Binding Corrective Design — AK-CANON Review

## Status

`AK-CANON CORRECTIVE DESIGN REVIEW = PASS`

`IMPLEMENTATION = NOT AUTHORIZED`

`FINDING CLOSED = NO`

This is an independent CANON review of the exact frozen design-only corrective candidate in `FJ899/scriptops PR #31`. It does not modify, repair, implement, activate, or close the candidate or the accepted finding.

## 1. Exact bound review target

```text
FJ899/scriptops PR #31
BASE = 30095c3170d16263e2db553a2b199bd6e33feace
HEAD = eda29d9b2916425cfa4048c8eff989b5f767ee58
TREE = 4cd9ab6d457d3496d76a47c3a6d031ea5e6cde83
PATH = governance/X1D_A5_EFFECT_METHOD_BINDING_CORRECTIVE_CANDIDATE.md
BLOB = 1247088730cbf5dddb2aea667c9842f8cc8bf980
STATE = OPEN / DRAFT / NOT MERGED
```

The candidate is one commit over the exact ScriptOps base and changes only the design artifact above.

## 2. Bound accepted finding

The review is bound to:

```text
FJ899/8 PR #91 = TERMINAL TECHNICAL FAIL
HEAD = 82ab66b00f97d3a24f02b632e4e40c6fb7a73c78
TREE = 6526249d6a5e5b530bdfed1df2471faf4e83d6ce
BLOB = 772503e7c1faecb462a3dbbafbb58b70d9c6d5b4

FJ899/8 PR #92 = HUMAN ACCEPTANCE
HEAD = d68226c57c39254c1a5a796ef69bd5428dbf1229
TREE = 1bc5c0bc3016da599605a4350d7421a151a2c66c
BLOB = d174e7445ac6f9f13c062fc934920d007590e1b5
```

Accepted finding preserved exactly:

`EFFECT METHOD NOT BOUND TO THE EXACT HUMAN DECISION`

Observed counterexample preserved exactly:

```text
D0 AUTHORIZES MERGE ONLY
SQUASH EFFECT REMAINS AVAILABLE UNDER THE SAME D0
```

## 3. CANON review criteria

The review asks whether the frozen design is internally consistent, executable as a corrective design, and sufficient in scope to address the accepted effect-method attack class without silently redefining the finding.

Classification vocabulary is preserved:

```text
DESIGN FINDING
IMPLEMENTATION BLOCKER
VALIDATION-CONTRACT PROBLEM
POSSIBLE FREEZE REOPEN
```

No frozen contradiction may be silently repaired.

## 4. Platform premise verification

The design's platform closure depends on the semantics of GitHub branch rulesets.

On 2026-08-31, authoritative GitHub documentation was checked for the relevant rule semantics:

- GitHub REST rules documentation defines `pull_request.parameters.allowed_merge_methods` as the array of allowed merge methods, with supported values `merge`, `squash`, and `rebase`, and requires at least one method.
- GitHub ruleset documentation states that a pull-request rule may require a merge type and that targeted branches may only be merged using the allowed type.
- GitHub merge-method documentation separately confirms that repository merge settings and branch/ruleset method restrictions can constrain which merge method is executable.

Therefore the proposed protected-branch invariant:

```text
allowed_merge_methods = { merge }
```

is a representable GitHub ruleset state and is sufficient at the platform-policy layer to exclude `squash` and `rebase` as allowed pull-request merge types for the governed canonical branch, subject to the separately frozen no-bypass and applicability predicates.

This directly addresses the accepted UI/API alternate-effect path rather than relying only on D0 text or application-side checks.

## 5. C1-C10 review

### C1 — exact authorized method in admission

PASS.

`OperationAdmission.merge_method` is mandatory and is required to equal the exact D0 method. The merge-only profile fixes both to `merge`; unknown or missing method is DENY.

### C2 — executor cannot substitute method

PASS.

The executor derives the transport method only from the validated admission and must reject any caller-selected override before the GitHub merge call.

### C3 — alternate UI/API paths cannot satisfy the same authorization

PASS.

The design does not treat the broker/executor as the only enforcement boundary. It separately requires the protected canonical branch ruleset to admit only `merge`, and it requires both UI and API-path closure evidence. This is the necessary correction to the accepted T4 counterexample.

### C4 — exact referent/effect binding

PASS for the stated corrective scope.

Admission binds repository, PR, candidate HEAD, canonical ref, merge method, and expected post tree; the representation also carries base HEAD/tree, candidate tree, path-set digest, Q_K identity fields, and a canonical-operation digest. Changed referent/effect fields invalidate admission.

### C5 — changed method requires new authority

PASS.

A changed method invalidates the current admission. Under this minimum merge-only profile, even a new D0 naming `squash` or `rebase` is insufficient unless the governance envelope is separately authorized and revalidated. This avoids turning ordinary D0 issuance into implicit Q_K mutation authority.

### C6 — AI/process cannot broaden Human decision

PASS.

The design explicitly separates Human decision evidence, machine admission, executor capability, and Q_K governance. No AI/process credential may reinterpret the method or mutate Q_K to make another method available.

### C7 — authorized-method positive control

PASS as a future validation requirement.

The design requires a fresh valid merge-only D0/admission and exact pre-effect state before one authorized `merge` positive control.

### C8 — negative controls for squash and rebase

PASS.

Both methods are independently covered at the application layer and the live GitHub method-specific layer. The design correctly forbids executing an unauthorized canonical effect merely as a negative probe and uses `BLOCKED` rather than false PASS when non-destructive platform evidence is insufficient.

### C9 — exact post-effect verification

PASS.

The design does not equate merge command success with effect truth. It requires the generated merge commit, exact tree, exact parent1/parent2, exact expected content, and no extra canonical change.

### C10 — fail closed on ambiguity

PASS.

Unknown method, stale D0/admission, candidate drift, main drift, policy drift, method mismatch, or unresolved method-specific state cannot become PASS. Pre-effect ambiguity is DENY/BLOCKED; post-effect uncertainty is INDETERMINATE.

## 6. Broker / executor separation

PASS.

The design preserves the required separation:

```text
Human D0 = decision evidence
OperationAdmission = proof-bearing machine admission
Executor credential = effect capability
Q_K = platform enforcement envelope
```

The broker creates admission from independently observed trusted state. The executor cannot submit its own authorization proof and cannot independently choose the merge method.

`EXECUTOR CAPABILITY != AUTHORITY TO SELECT EFFECT METHOD`

## 7. Merge-only Q_K profile and governance authority

PASS.

The design deliberately does not mutate `allowed_merge_methods` dynamically per Human D0. Instead it defines a bounded merge-only governance profile:

```text
Q_K@v_next.allowed_merge_methods = { merge }
```

This is the minimum correction for the accepted finding. Supporting `squash` or `rebase` later is explicitly outside this profile and requires separate governance authorization/design plus fresh validation.

That preserves the established rule:

`CAPABILITY TO MODIFY RULE REPRESENTATION != AUTHORITY TO MODIFY NORMATIVE RULE`

The ruleset change itself remains governance-bearing and is not authorized by the design candidate or by this review.

## 8. Acceptance-test executability

PASS.

AT0-AT10 form an executable future validation sequence:

```text
AT0 preregister exact implementation/governance/test identities
AT1 verify merge-only live Q_K and no bypass
AT2 construct exact merge-only admission
AT3 reject squash substitution before transport
AT4 reject rebase substitution before transport
AT5 verify live UI squash unavailable
AT6 verify live UI rebase unavailable
AT7 establish direct API-path platform closure non-destructively or BLOCKED
AT8 reject admission for changed method under merge-only Q_K
AT9 execute one separately authorized merge positive control
AT10 independently establish exact merge-method post-effect truth
```

The validation contract does not require an unsafe destructive negative merge. It has a defined `BLOCKED` disposition if direct API-path closure cannot be established with trusted non-destructive evidence.

## 9. Implementation details intentionally left for a later bounded phase

The design leaves exact `OperationAdmission` serialization/hash encoding as an implementation detail, but requires it to be frozen before implementation testing. That does not change the semantic requirement and is not a design-level contradiction.

Likewise, this review does not claim that the ruleset change, broker, executor, admission format, or tests already exist. Those are future implementation/verification obligations under separate Human authority.

`DESIGN EXECUTABLE != IMPLEMENTATION PRESENT`

## 10. Problem classification

```text
DESIGN FINDING = NONE
IMPLEMENTATION BLOCKER = NONE AT DESIGN-REVIEW STAGE
VALIDATION-CONTRACT PROBLEM = NONE
POSSIBLE FREEZE REOPEN = NONE
```

No silent redesign or contract repair was required to reach this result.

## 11. Verdict

`AK-CANON CORRECTIVE DESIGN REVIEW = PASS`

The exact frozen PR #31 design is internally consistent and sufficient in scope to address the Human-accepted effect-method-binding attack class:

```text
valid merge-only Human decision
+
exact OperationAdmission method binding
+
executor no-substitution
+
protected-branch merge-only platform envelope
+
non-destructive squash/rebase negative controls
+
separately authorized merge positive control
+
exact post-effect truth
```

This PASS is a design-review result only.

It does not authorize implementation, ruleset change, CODEOWNERS change, PR #31 merge, PR #30 mutation, remediation execution, corrective verification, Human closure, V1, release, deployment, or tag.

`AK-CANON DESIGN PASS != IMPLEMENTATION AUTHORITY`

`DESIGN PASS != FINDING CLOSED`

`SPECIFICATION != IMPLEMENTATION != EXECUTION != ACCEPTANCE`

`AI PROPOSES != HUMAN DECIDES`
