# X1B Human Decision Authorship — Independent AK-CANON R4R1 Implementation-Brief Review

Status: `INDEPENDENT REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: `2026-09-01`

## 1. Verdict

`AK-CANON X1B R4R1 IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

R4R1 materially improves the prior implementation briefs. It correctly rematerializes from the recovered evidence-repository base, is self-contained for many previously ambiguous contracts, uses the real `.scriptops/decision-log.ndjson` effect target, separates the historical prototype transport from the active runtime, freezes public GitHub evidence transport, defines complete-review-set reconstruction, and introduces a final Human-currentness gate.

However, independent adversarial review found two material blockers before implementation authority can be granted:

1. the exact Human request/effect identity is circular because the Human-bound material effect requires a concrete `decision_request_id` inside the local Git commit message while that `decision_request_id` is itself derived from a digest of the request binding that contains that material-effect object;
2. the exact current legacy substrate exposes a second direct accepted-state canonical-effect route, `scene-promote --to accepted`, while R4R1 concretely freezes denial/regression semantics only for direct legacy `approve`; the known parallel accepted-state path is left to future implementer interpretation rather than being frozen as a specific DENY/reroute contract.

Either blocker independently requires `NOT PASS`.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R1 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R1 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#116`

```text
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
BASE TREE = df807db7003dfd201e9be4d5927472e515a2e737
HEAD = 0319b13cbe85675db0b40d36f5940cbfba36c130
TREE = 55dc82a52117d7234915a0b84193a4b2a26c226a
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R1.md
BLOB = 0fc30617ae7c378bdd90e7f9c5e1ab37a59661a4
```

Observed immediately before review write:

```text
state = OPEN
merged = false
draft = true
commits = 1
changed_files = 1
complete changed-file set =
  research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R1.md
```

## 3. Normative lineage checked

### 3.1 Accepted corrective design

```text
FJ899/scriptops PR #34
HEAD = d7a5065c87e9a4b49fb608235c908bceac42b4b1
TREE = 3140d0ac95c120a7b1532942bae2e0dad38b4839
PATH = governance/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_CANDIDATE.md
BLOB = dac16f109d1414a2208c2ed9a166ae9e9a329216
```

The design requires a separate trusted Human decision event, exact content/scope/candidate/effect binding, trusted Human-authoritative origin, fail-closed currentness/conflict/replay handling, and no executor substitution.

### 3.2 Independent design review

```text
FJ899/8 PR #109
HEAD = 132d65be48331a822039262b707c47a81d02a64d
TREE = a8bdc363d293beb7b15ae8b787cc3ebdd694fd99
BLOB = 439109e104244552a5ac1f3f08988dba283733d0
VERDICT = AK-CANON X1B CORRECTIVE DESIGN REVIEW R2 = PASS
```

### 3.3 Binding predecessor implementation-brief review

```text
FJ899/8 PR #115
HEAD = 0d984b97a88f6ee9d4267a88a3fbddca2168002e
TREE = f3092635c6f018fead19c364c0014e2478b88a3a
BLOB = 24aa423dad9ce181dc239fa616be6ea34ce6d2aa
VERDICT = AK-CANON X1B SUPERSEDING IMPLEMENTATION-BRIEF R3 REVIEW = NOT PASS
```

R4R1 materially addresses the R3 findings concerning current-state authority files, self-contained normative mechanics, material-effect schema, and complete-review-set digest. The present `NOT PASS` is based on new concrete R4R1 issues, not a repetition of those closed-at-brief-level findings.

## 4. Current ScriptOps baseline checked

```text
FJ899/scriptops main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Security-relevant baseline includes:

```text
phase6/scriptops-v2-hardening.py
BLOB = 4f379960ed5677634dd234af6aa39626782b6133

legacy/scriptops-v2-single.py
BLOB = 9baa7b3a1eb746e34b79207a382eea1f5dd4ec55
```

The historical R4 provenance branch remains unchanged and non-authoritative:

```text
branch = brief/x1b-human-decision-authorship-implementation-brief-r4-20260901
HEAD = c0bbaaa568215fa1d53b36acfacb4bce5d3c1fcc
TREE = 2bbbe3dbe86c4aed726581103122eb57bf4a2e3e
BLOB = 34f21ead0e72c21ad3e98b72fe7503ceb9330c29
```

It was not adopted as review authority.

## 5. Review method

This review did not infer PASS from R4R1's length, self-contained wording, or prior correction history.

The adversarial question was:

```text
Can a future implementer obey the literal R4R1 contract only by
inventing/changing a core authority-binding rule, or can a known current
canonical acceptance effect survive without the exact Human-decision path?
```

The review inspected:

- exact request identity and canonical serialization rules;
- exact `PresentedMaterialEffectV1` fields;
- exact one-file decision-PR envelope;
- Human review-body and actor semantics;
- complete pagination/review-state semantics;
- public GitHub transport and credential separation;
- admission, replay, worktree locking and `FinalEffectGateV1`;
- exact effect paths and durable attribution;
- failure/rollback and post-effect truth;
- the current executable legacy state machine and CLI;
- the required negative/regression matrix;
- the future implementation surface and implementation-review obligations.

## 6. Finding X1B-R4R1-IBR-F001 — `decision_request_id` is circular through the Human-bound Git commit message

Severity: `BLOCKER`

R4R1 defines request identity as:

```text
request_binding_json = canonical_json_bytes(HumanDecisionRequestBindingV1)
request_digest = sha256_hex_bytes(request_binding_json)
decision_request_id = "x1b:" + request_digest
```

The exact `HumanDecisionRequestBindingV1` includes:

```text
"presented_material_effect": <PresentedMaterialEffectV1>
```

The exact Human-bound `PresentedMaterialEffectV1` includes:

```text
"local_git_effect": {
  "commit_count": 1,
  "commit_message": "scriptops x1b: accept <scene_id> via <decision_request_id>",
  "exact_changed_paths": [
    "scenes/<scene_id>.fountain",
    ".scriptops/decision-log.ndjson"
  ]
}
```

R4R1 then removes any possible placeholder interpretation by requiring:

```text
The local Git commit message must be exactly the material-effect-bound
message with concrete scene ID and decision request ID substituted before
the Human request was finalized.
```

The dependency therefore is:

```text
decision_request_id
=
"x1b:" + SHA256(canonical_json(HumanDecisionRequestBindingV1))

HumanDecisionRequestBindingV1
contains
PresentedMaterialEffectV1

PresentedMaterialEffectV1.commit_message
contains
concrete decision_request_id
```

Equivalently, the requested identity requires an unstated fixed point of the form:

```text
R = SHA256(binding-containing("x1b:" + R))
```

R4R1 defines no fixed-point search, placeholder-preimage, two-stage digest, excluded-field rule, or pre-request identifier distinct from `decision_request_id`.

This is not merely difficult to implement. The specified construction order cannot deterministically produce the exact Human-bound request bytes using the stated formulas.

The implementer would have to invent or change one of the authority-critical rules, for example by changing the commit-message binding, excluding a field from request identity, introducing a separate pre-request identifier, or adopting a placeholder canonicalization rule. R4R1 authorizes none of those choices.

This directly violates the implementation-brief acceptance requirement:

```text
NO CORE AUTHORITY / SECURITY SEMANTIC CHOICE LEFT TO IMPLEMENTER
```

It also prevents a valid positive control under the literal contract because the exact request/effect object to be shown to the Human cannot first be finalized as specified.

Disposition:

`NOT PASS`

## 7. Finding X1B-R4R1-IBR-F002 — known parallel legacy `scene-promote --to accepted` canonical-effect path is not concretely frozen as DENY

Severity: `BLOCKER`

R4R1 correctly identifies and requires denial of the direct legacy command:

```text
python legacy/scriptops-v2-single.py approve --scene <scene>
```

and freezes the high-level invariant:

```text
ONE OPERATIVE ACCEPTANCE EFFECT PATH
=
X1B-VALIDATED PHASE6 PATH
```

However, independent inspection of the exact current legacy BLOB shows another direct accepted-state route.

The current state machine permits:

```text
candidate -> accepted
```

The current CLI exposes:

```text
scene-promote --id <scene> --to accepted
```

The current `cmd_scene_promote` logic sets:

```text
fm["status"] = target_status
```

and, when `target_status == "accepted"`, selects:

```text
PROJECT_ROOT / "scenes" / f"{scene_id}.fountain"
```

then writes the promoted scene and performs a local Git commit.

For a scene whose candidate is in staging and has no existing canonical scene, the current legacy substrate can therefore perform a direct candidate-to-accepted canonical transition without the R4R1 decision PR, Human review, admission, or final gate.

R4R1's concrete legacy correction, verifier rule, current-state documentation rule and mandatory direct-legacy regression all name `approve`, not this known `scene-promote --to accepted` route.

R4R1 does require a later implementation review to inventory `all direct/indirect acceptance paths`, which is a useful defense-in-depth check. But an implementation review checklist is not a substitute for freezing the security semantics of a known current bypass before implementation authority.

Under the present wording, the future implementer must decide how to interpret `scene-promote` relative to the one-operative-path invariant. Materially different choices include:

```text
remove accepted from scene-promote choices
reject candidate -> accepted in direct legacy invocation
route accepted promotion through the complete X1B decision-PR path
retain it as a supposedly non-Human state transition
```

The last interpretation would preserve the same canonical `accepted` effect without the Human-decision path, while the other choices change runtime semantics differently.

Because this exact existing path is known before implementation and concerns the same canonical accepted-state effect, leaving its disposition implicit is a core security/authority choice left to the implementer.

The mandatory negative matrix also lacks a direct regression equivalent to:

```text
python legacy/scriptops-v2-single.py scene-promote --id <candidate-scene> --to accepted
=> DENY / nonzero / no canonical accepted effect
```

Disposition:

`NOT PASS`

## 8. R3 findings — R4R1 review result

The prior R3 blockers were rechecked rather than assumed closed.

### R3-F001 current-state authority surface

R4R1 includes:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
```

inside the expected future implementation surface and requires them to identify `approve --decision-pr <N>` as the only current Human-decision route while preserving defect-era routes as historical provenance.

Brief-level disposition: `ADDRESSED`.

### R3-F002 normative inheritance ambiguity

R4R1 explicitly states:

```text
R4R1 TEXT = CURRENT IMPLEMENTATION-BRIEF AUTHORITY
R4 / R3 / R2 / R1 = HISTORICAL INPUT ONLY
```

and restates the authority-critical serialization, review, admission, replay, transport and gate contracts.

Brief-level disposition: `ADDRESSED`, except for the new internal circularity in F001.

### R3-F003 material-effect schema

R4R1 defines a closed `PresentedMaterialEffectV1` with the real canonical target, accepted-scene preview hash, `.scriptops/decision-log.ndjson` append and exact two-path local Git effect.

Brief-level disposition: `ADDRESSED AS TO SCHEMA COMPLETENESS`; the commit-message field inside that schema causes F001.

### R3-F004 complete-review-set digest

R4R1 freezes normalized review fields, membership, ordering, canonical serialization and digest formula and requires golden vectors.

Brief-level disposition: `ADDRESSED`.

## 9. Mandatory adversarial question matrix

### Q1 — Material-effect/request circularity

`FAIL — F001`.

The concrete decision-request ID inside the Human-bound commit message depends on its own request digest.

### Q2 — Fully non-circular request bytes

`FAIL — F001`.

PR number and PR HEAD were correctly removed from the request digest, but the effect commit-message cycle remains.

### Q3 — Exact Human-visible content/scope/material-effect binding

`ADEQUATE EXCEPT F001`.

Candidate, impact, canonical before/after and real decision-log target are otherwise explicitly bound.

### Q4 — Accepted-scene preview/effect determinism

`ADEQUATELY SPECIFIED AT BRIEF LEVEL`.

R4R1 requires exact preview bytes/hash and byte equality at effect time, subject to later implementation/golden-vector verification.

### Q5 — Real effect targets

`PASS AT BRIEF LEVEL`.

The operative paths are correctly stated as:

```text
scenes/<scene_id>.fountain
.scriptops/decision-log.ndjson
```

### Q6 — Direct legacy denial without parallel bypass

`FAIL — F002`.

Current `scene-promote --to accepted` is a known second accepted-state effect path not concretely dispositioned by R4R1.

### Q7 — Historical transport vs active runtime

`ADEQUATELY SPECIFIED AT BRIEF LEVEL`.

Historical parts remain immutable evidence; active legacy becomes corrected runtime; repository-internal restore is prohibited and verifier semantics are split.

### Q8 — README / PROJECT_STATE / HANDOFF authority

`ADEQUATELY SPECIFIED AT BRIEF LEVEL`.

All are now in the future surface with a current-vs-historical rule.

### Q9 — Exact Human review parser

`ADEQUATELY SPECIFIED AT BRIEF LEVEL`.

The four-line body, LF rules, exact request ID/digest, Human rationale restrictions and no caller-rationale substitution are frozen.

### Q10 — Human actor policy vs identity-alone proof

`BOUNDED / REQUIRES LIVE HUMAN CONTROL`.

R4R1 freezes `litrgratis-pixel` as the Human authority profile, explicitly disclaims account identity as proof of private mental state, and requires a separately authorized manual Human UI act for the positive control. This review does not treat that as a separate new blocker under the accepted bounded design, but live positive control remains mandatory.

### Q11 — Complete PR-files/reviews pagination

`ADEQUATELY SPECIFIED AT BRIEF LEVEL`.

`per_page=100`, page-by-page completion and read/rate-limit failure semantics are fail-closed.

### Q12 — Review states/conflicts/duplicates

`ADEQUATELY SPECIFIED AT BRIEF LEVEL`.

APPROVED / CHANGES_REQUESTED / COMMENTED / DISMISSED, wrong commit, duplicate IDs, second approval and conflicts have explicit fail-closed behavior.

### Q13 — CompleteReviewSetV1 exact reconstruction

`ADEQUATELY SPECIFIED AT BRIEF LEVEL`.

Projection, membership, ordering and digest are fixed; later tests must freeze exact vectors.

### Q14 — Trusted public GitHub transport

`ADEQUATELY SPECIFIED AT BRIEF LEVEL`.

Exact `api.github.com` origin, standard-library TLS, disabled proxy, rejected redirects, no Authorization/auth fallback, and ambient credential/CA denials are frozen.

### Q15 — Local Git does not become remote GitHub authority

`ADEQUATELY BOUNDED AT BRIEF LEVEL / IMPLEMENTATION REVIEW REQUIRED`.

R4R1 prohibits network Git commands and `gh`, strips/denies specified credential paths and disables Git credential helpers. Later implementation review must still inspect actual subprocess behavior and local environment effects.

### Q16 — Same-worktree concurrency lock

`ADEQUATELY SPECIFIED AT BRIEF LEVEL`.

The lock is worktree-local, exclusive and fail-closed on stale/crash ambiguity.

### Q17 — Replay scope

`ADEQUATELY BOUNDED`.

R4R1 claims at-most-once only within one canonical local worktree execution instance and explicitly makes no global cross-clone exactly-once claim. Changed operation identity requires new Human evidence.

### Q18 — FinalEffectGate Human-currentness commitment point

`ADEQUATELY SPECIFIED AT BRIEF LEVEL`.

Fresh PR/review reread and exact final gate are required immediately before first mutation.

### Q19 — Post-final-gate substitution window

`ADEQUATELY CONSTRAINED AT BRIEF LEVEL`.

No network/user/sleep/unrelated blocking operation is permitted between final gate success and first canonical mutation; local identities are revalidated.

### Q20 — Durable record self-hash/circularity

`ADEQUATELY SPECIFIED FOR RESULTING COMMIT SHA`.

The effect record does not require the resulting effect commit SHA inside content that determines that same commit; resulting commit truth is frozen externally by later verification.

This does not cure F001, which is a distinct request-ID/material-effect cycle.

### Q21 — Partial write / rollback semantics

`ADEQUATELY FAIL-CLOSED AT BRIEF LEVEL`.

Success requires the exact two-path commit and post-effect truth. Failure after first mutation must attempt deterministic restoration under lock; unprovable restoration becomes dirty `BLOCKED`, never Human success.

### Q22 — Original X1B attacks and real regressions

`NOT COMPLETE — F002`.

The ten preregistered attacks, original `cmd_approve`, direct legacy approve, restore, transport, replay/concurrency and final-gate races are included, but the concrete currently executable `scene-promote --to accepted` parallel acceptance route is not frozen as a mandatory negative.

### Q23 — Future implementation surface completeness

`SURFACE IS CAPABLE OF CORRECTION, CONTRACT IS NOT COMPLETE`.

`legacy/scriptops-v2-single.py` is inside the allowed surface, so F002 can be corrected without expanding paths, but R4R1 does not decide the required behavior of that path. F001 also requires a contract change, not merely coding inside the surface.

### Q24 — Any remaining core authority/security choice

`YES — F001 AND F002`.

Therefore implementation authority is not established.

## 10. Findings not converted into automatic repair

This review intentionally does not modify PR #116 and does not choose corrected formulas or runtime behavior.

It records only the minimum necessary correction classes:

```text
F001: remove the request-ID/material-effect identity cycle while preserving
      exact Human-visible effect binding and deterministic request identity.

F002: freeze the exact disposition and regression semantics for the existing
      legacy scene-promote candidate->accepted canonical-effect route so no
      parallel accepted-state path remains outside X1B admission.
```

Those are review findings, not authority to produce the corrected brief.

`REVIEW FINDING != REPAIR AUTHORITY`

## 11. Implementation-authority disposition

Because R4R1 has material unresolved authority/security semantics:

```text
R4R1 BRIEF PREPARED = TRUE
R4R1 INDEPENDENT REVIEW PASS = FALSE
IMPLEMENTATION AUTHORITY = NOT ESTABLISHED
X1B = OPEN
V1 AUTHORITY = NOT ESTABLISHED
```

No ScriptOps implementation may proceed from this review.

## 12. Final verdict

`AK-CANON X1B R4R1 IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

`R4R1 REVIEW NOT PASS != REPAIR AUTHORITY`

`R4R1 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY`

`AI PROPOSES != HUMAN DECIDES`

`STOP`
