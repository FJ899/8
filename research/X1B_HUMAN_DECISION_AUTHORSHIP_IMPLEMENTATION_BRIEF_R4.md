# X1B HUMAN DECISION AUTHORSHIP — SUPERSEDING IMPLEMENTATION BRIEF R4

Status: `R4 CORRECTIVE REVISION / BRIEF ONLY / IMPLEMENTATION NOT AUTHORIZED`
Date: `2026-09-01`

## 1. Authority and purpose

This R4 brief is prepared under explicit Human authorization following the durable independent NOT-PASS review recorded in:

```text
FJ899/8 PR #115
HEAD = 0d984b97a88f6ee9d4267a88a3fbddca2168002e
TREE = f3092635c6f018fead19c364c0014e2478b88a3a
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R3_AK_CANON_REVIEW.md
BLOB = 24aa423dad9ce181dc239fa616be6ea34ce6d2aa
VERDICT = AK-CANON X1B SUPERSEDING IMPLEMENTATION-BRIEF R3 REVIEW = NOT PASS
```

R4 corrects all four material findings identified by that review without reinterpreting them away.

This document is an implementation brief only.

`R4 BRIEF != IMPLEMENTATION AUTHORITY`

No ScriptOps implementation, Human decision PR, Human APPROVE, positive control, canonical effect, merge, X1B closure, V1 authority, release, deployment, or tag is authorized by this artifact.

## 2. Supersession and normative precedence

R4 is the complete current implementation-brief authority for the X1B Human Decision Authorship correction described here.

The precedence rule is exact:

```text
R4 TEXT = CURRENT IMPLEMENTATION-BRIEF AUTHORITY
R2/R3 = HISTORICAL INPUT EXCEPT WHERE EXACT CLAUSE
        IS EXPLICITLY REPRODUCED OR INCORPORATED BY
        PATH + BLOB + SECTION
```

An implementer MUST NOT infer normative requirements from R2 or R3 merely because R4 uses words such as `remains`, `preserves`, `unchanged`, `same`, or `as before`.

If a requirement is authority-critical, it MUST appear in R4 text or be incorporated by an exact immutable reference containing:

```text
repository
path
blob
section identifier
```

If R4 conflicts with R2 or R3, R4 controls.

## 3. Findings resolved by R4

R4 resolves:

```text
R3-F001 CURRENT-STATE AUTHORITY SURFACE INCOMPLETE
R3-F002 NORMATIVE INHERITANCE AMBIGUOUS
R3-F003 PRESENTED MATERIAL EFFECT SCHEMA UNDEFINED
R3-F004 COMPLETE REVIEW SET DIGEST UNDER-SPECIFIED
```

R4 does not reopen the R2 findings already addressed in R3:

```text
R2 RESTORE BLOCKER     = ADDRESSED
R2 TRANSPORT BLOCKER   = ADDRESSED
R2 CURRENTNESS BLOCKER = ADDRESSED
```

Those earlier corrections are preserved only insofar as their operative requirements are explicitly restated below.

## 4. Corrected implementation surface

Any future implementation authorized from this brief MUST be limited to the following surface unless a separate Human authorization expands it:

```text
phase6/scriptops-v2-hardening.py
legacy/scriptops-v2-single.py
phase6/x1b_human_decision.py

scripts/restore_v2.py
scripts/verify_repository.py

sources/prototype/RESTORE.md
SOURCE_MANIFEST.md

README.md
PROJECT_STATE.md
HANDOFF.md

tests/test_phase6_scriptops_smoke.py
tests/test_x1b_human_decision.py

.github/workflows/x1b-human-decision.yml
```

Historical prototype parts outside this surface remain immutable.

No implementation may silently enlarge this surface.

## 5. Current-state authority correction

The operative Human-decision route MUST become exactly:

```text
approve --decision-pr <N>
```

The defect-era route:

```text
approve --why <TEXT>
```

MUST remain available only as historical provenance describing the Phase-6 defect-era baseline. It MUST NOT remain an operative Human-decision route.

The active runtime MUST reject or disable direct legacy approval through `approve --why` for current Human-decision attribution.

The following current/recovery truth files are therefore part of the authorized implementation surface and MUST be updated consistently:

```text
README.md
PROJECT_STATE.md
HANDOFF.md
```

Their normative current-state rule MUST state, in substance and without contradiction:

```text
defect-era `approve --why` = historical provenance only
current Human-decision route = `approve --decision-pr <N>` only
direct legacy approve = disabled for current Human-decision attribution
"legacy unchanged" = historical Phase-6 baseline statement, not current active-runtime byte identity
```

No current-state or recovery document may continue to describe `why` as the operative Human decision mechanism after implementation.

## 6. Historical transport/runtime split

The implementation MUST preserve a distinction between:

```text
historical artifact provenance
!=
current active runtime identity
```

`legacy/scriptops-v2-single.py` may be changed only where necessary to prevent a historical transport/runtime artifact from remaining an operative path that can create current Human-decision attribution contrary to this brief.

Historical prototype source artifacts outside the authorized implementation surface remain immutable.

Restore tooling and source manifests MUST reconstruct the corrected current runtime, not silently restore the defect-era approval route as active authority.

## 7. Human decision admission model

A current Human decision is not established by possession of an approval command, by a non-empty reason, by continuation, by silence, by a comment, or by an AI-created record.

The operative route MUST require a Human decision PR selected explicitly by number:

```text
approve --decision-pr <N>
```

The implementation MUST validate the referenced Human decision PR and construct a deterministic decision-admission record before any current Human-decision attribution is accepted.

`AI PROPOSED != HUMAN DECIDED`

`APPROVAL COMMAND POSSESSION != HUMAN DECISION AUTHORSHIP`

`VISIBLE REVIEW != VALID DECISION ADMISSION`

## 8. Canonical JSON contract

All authority-critical digests defined by R4 MUST use this exact canonical JSON contract.

### 8.1 Encoding

```text
character encoding = UTF-8
JSON text encoding = UTF-8 bytes
object member ordering = lexicographic ascending by Unicode code point of member name
array ordering = semantic ordering defined by the relevant R4 section
whitespace outside JSON string values = NONE
indentation = NONE
separator after object member name = ':'
separator between members/elements = ','
trailing newline = NONE
```

### 8.2 Scalars

```text
null = JSON null
boolean = JSON true / false
integers = base-10 JSON numbers with no leading zero except 0
strings = JSON strings with standard JSON escaping
```

Floating-point numbers are forbidden in authority-critical canonical objects.

Unknown or omitted authority-critical fields are not silently defaulted. A missing required field is validation failure.

### 8.3 Digest formula

For any R4 canonical object `X`:

```text
canonical_json_bytes(X) = UTF-8 bytes of exact canonical JSON defined above
sha256_hex(X) = lowercase hexadecimal SHA-256(canonical_json_bytes(X))
```

No implementation-specific serializer options may replace this contract.

## 9. Exact Human review-body parser

A Human decision PR is admissible only if the review used for decision admission satisfies the exact parser below.

### 9.1 Review source

The parser consumes a GitHub pull-request review object, not a chat statement, PR conversation comment, issue comment, commit message, screenshot text, label, or external assertion.

### 9.2 Required normalized fields

The review object MUST normalize to exactly these authority-relevant fields:

```text
review_id
actor_login
state
commit_id
body_utf8
submitted_at
pull_request_number
repository_full_name
```

### 9.3 Required semantics

```text
state = APPROVED
actor_login = expected Human decision authority
commit_id = exact decision-PR HEAD required by the admission request
repository_full_name = exact expected repository
pull_request_number = exact decision PR number supplied to `approve --decision-pr <N>`
body_utf8 = non-empty exact decision statement required by the referenced decision request
```

The parser MUST preserve review-body bytes after GitHub retrieval except for the transport-level UTF-8 decoding necessary to obtain the API-returned string. It MUST NOT trim, collapse whitespace, normalize punctuation, normalize Unicode, substitute line endings, infer omitted content, or accept semantically similar text.

If the exact expected statement is frozen as a single paragraph, the observed review body MUST equal that statement byte-for-byte when encoded as UTF-8.

Any mismatch is invalid admission.

## 10. Decision request canonical object

Before Human review, the system MUST deterministically construct the decision request object:

```text
DecisionRequestV1 = {
  "version": "X1B-DecisionRequestV1",
  "repository": <repository_full_name>,
  "scene_id": <exact scene identifier>,
  "candidate_id": <exact candidate identifier>,
  "candidate_digest": <exact candidate content digest>,
  "canonical_target": <exact canonical target identifier>,
  "presented_material_effect": <PresentedMaterialEffectV1 object>,
  "presented_material_effect_digest": <sha256_hex(PresentedMaterialEffectV1)>,
  "decision_pr_number": <integer>,
  "decision_pr_head": <exact commit SHA>
}
```

Its digest is:

```text
decision_request_digest = sha256_hex(DecisionRequestV1)
```

## 11. Exact `presented_material_effect` schema

R4 freezes the consequence schema as `PresentedMaterialEffectV1`.

The exact canonical object is:

```text
PresentedMaterialEffectV1 = {
  "version": "X1B-PresentedMaterialEffectV1",
  "repository": <repository_full_name>,
  "scene": {
    "scene_id": <exact scene identifier>,
    "candidate_id": <exact candidate identifier>,
    "candidate_content_sha256": <SHA-256 of exact candidate bytes>
  },
  "canonical_target": {
    "path": <exact canonical scene path>,
    "expected_before_sha256": <SHA-256 of exact pre-effect canonical bytes>,
    "expected_after_sha256": <SHA-256 of exact candidate bytes>
  },
  "accepted_content_transition": {
    "from": "NOT_ACCEPTED",
    "to": "ACCEPTED"
  },
  "decision_log_effect": {
    "append_count": 1,
    "target": "DECISION_LOG.md"
  },
  "local_git_effect": {
    "commit_count": 1,
    "scope": [
      <exact canonical scene path>,
      "DECISION_LOG.md"
    ]
  }
}
```

The schema is closed. No additional material effect field may be silently added to the authority-bearing object. No required field may be omitted.

The presented material effect MUST bind at minimum:

```text
exact scene/candidate
exact canonical target
transition to accepted content
exactly one durable decision-log append
exactly one local Git effect commit
```

The digest is exactly:

```text
presented_material_effect_digest = sha256_hex(PresentedMaterialEffectV1)
```

A Human approval that binds a different object or an object produced under a different schema version is not admission for this request.

## 12. Exact `admission_id` formula

R4 freezes admission identity independently of implementation language.

Construct:

```text
AdmissionIdentityV1 = {
  "version": "X1B-AdmissionIdentityV1",
  "decision_request_digest": <decision_request_digest>,
  "decision_pr": {
    "repository": <repository_full_name>,
    "number": <decision PR number>,
    "head": <decision PR exact HEAD>
  },
  "review": {
    "review_id": <GitHub review id as decimal string>,
    "actor_login": <exact login>,
    "state": "APPROVED",
    "commit_id": <exact anchored commit SHA>,
    "body_sha256": <SHA-256 of exact UTF-8 review body bytes>,
    "submitted_at": <exact GitHub timestamp string>
  }
}
```

Then:

```text
admission_id = sha256_hex(AdmissionIdentityV1)
```

There is no alternate admission-id formula.

## 13. Review normalization for complete review-set reconstruction

R4 freezes `NormalizedReviewV1` as the only review projection used by `complete_review_set_digest`.

For every submitted review returned by GitHub for the relevant decision PR, construct exactly:

```text
NormalizedReviewV1 = {
  "version": "X1B-NormalizedReviewV1",
  "review_id": <GitHub review id as decimal string>,
  "actor_login": <exact GitHub login>,
  "state": <exact normalized GitHub review state>,
  "commit_id": <exact commit SHA or JSON null if GitHub reports null>,
  "body_sha256": <SHA-256 of exact UTF-8 review body bytes>,
  "submitted_at": <exact GitHub timestamp string>
}
```

No avatar, display name, email, node id, URL, reaction, UI text, requested-reviewer state, or unrelated metadata is part of this normalized projection.

## 14. Complete review-set ordering

The complete review set MUST include every submitted review object returned for the decision PR at the FinalEffectGateV1 observation point.

Sort `NormalizedReviewV1` objects by the exact tuple:

```text
(submitted_at ASC, review_id ASC as decimal integer)
```

If two records have identical `submitted_at`, numeric `review_id` breaks the tie.

No implementation-dependent API-return order may be used as authority.

## 15. Exact `complete_review_set_digest` formula

Construct:

```text
CompleteReviewSetV1 = {
  "version": "X1B-CompleteReviewSetV1",
  "repository": <repository_full_name>,
  "decision_pr_number": <integer>,
  "decision_pr_head": <exact HEAD observed at gate>,
  "reviews": [<NormalizedReviewV1 objects in Section 14 order>]
}
```

Then:

```text
complete_review_set_digest = sha256_hex(CompleteReviewSetV1)
```

The field projection, ordering, canonical serialization, and SHA-256 formula are fixed by this brief and MUST NOT be invented by the implementer.

## 16. FinalEffectGateV1

The exact gate version constant is:

```text
FINAL_EFFECT_GATE_VERSION = "X1B-FinalEffectGateV1"
```

Before any canonical effect, the runtime MUST construct a durable gate record containing at minimum:

```text
FinalEffectGateV1 = {
  "version": "X1B-FinalEffectGateV1",
  "admission_id": <exact admission_id>,
  "decision_request_digest": <exact decision_request_digest>,
  "presented_material_effect_digest": <exact presented_material_effect_digest>,
  "decision_pr": {
    "repository": <repository_full_name>,
    "number": <decision PR number>,
    "head": <exact current decision PR HEAD>
  },
  "admitted_review": {
    "review_id": <exact admitted review id>,
    "actor_login": <exact Human authority login>,
    "commit_id": <exact decision PR HEAD>,
    "body_sha256": <exact body digest>
  },
  "complete_review_set_digest": <Section 15 digest>,
  "candidate_currentness": {
    "candidate_id": <exact candidate identifier>,
    "candidate_content_sha256": <exact current candidate digest>
  },
  "canonical_pre_state": {
    "path": <exact canonical scene path>,
    "sha256": <exact current pre-effect bytes digest>
  }
}
```

Its durable record digest is:

```text
final_effect_gate_digest = sha256_hex(FinalEffectGateV1)
```

The gate MUST be re-evaluated immediately before effect. A stale admission or stale candidate MUST NOT be carried through by cache or prior validation.

## 17. Currentness rules

At FinalEffectGateV1, all of the following MUST still hold:

```text
decision PR HEAD = exact admitted decision PR HEAD
admitted review still exists and remains APPROVED
admitted review actor = exact Human authority
admitted review commit_id = exact decision PR HEAD
admitted review body = exact frozen statement
complete review set reconstructed and digestible
candidate identity/content = exact DecisionRequestV1 candidate
presented material effect = exact approved PresentedMaterialEffectV1
canonical pre-state = exact expected before-state
no superseding Human decision exists for the same request
```

Any mismatch blocks effect.

## 18. Effect cardinality

For a successful approval execution under this brief:

```text
accepted-content transition count = exactly 1
durable DECISION_LOG append count = exactly 1
local Git effect commit count = exactly 1
```

The local Git commit MUST contain no effect outside the closed scope defined in `PresentedMaterialEffectV1.local_git_effect.scope`.

A partially applied effect, duplicate append, duplicate commit, or out-of-scope path is not acceptable success.

## 19. Decision log evidence

The durable decision-log append MUST contain enough exact fields to reconstruct at minimum:

```text
FinalEffectGateV1 version
admission_id
decision_request_digest
presented_material_effect_digest
complete_review_set_digest
decision PR repository/number/head
admitted review id/actor/commit_id/body_sha256
candidate id/content sha256
canonical target path
canonical before sha256
canonical after sha256
resulting local Git commit SHA
```

A later verifier MUST be able to recompute all R4-defined digests from repository/GitHub evidence without relying on process memory.

## 20. Restore contract

`scripts/restore_v2.py`, `sources/prototype/RESTORE.md`, and `SOURCE_MANIFEST.md` MUST be updated so that repository recovery reconstructs the corrected current authority model.

The restore contract MUST NOT reactivate direct `approve --why` as the current Human-decision route.

Historical source provenance may still record that the Phase-6 baseline used `approve --why`.

The recovery distinction is exact:

```text
HISTORICAL BASELINE PRESERVED
!=
DEFECT-ERA ROUTE RESTORED AS CURRENT AUTHORITY
```

## 21. Repository verification contract

`scripts/verify_repository.py` MUST verify at minimum:

```text
current operative route is approve --decision-pr <N>
direct approve --why cannot create current Human decision attribution
README.md current-state description matches corrected route
PROJECT_STATE.md current-state description matches corrected route
HANDOFF.md recovery/current-state description matches corrected route
restore path reconstructs corrected authority model
historical prototype parts outside authorized surface remain unchanged
FinalEffectGateV1 version constant exact
canonical JSON contract tests pass
admission_id formula tests pass
PresentedMaterialEffectV1 schema/digest tests pass
complete_review_set_digest reconstruction tests pass
```

## 22. Test requirements

`tests/test_x1b_human_decision.py` MUST cover at minimum:

```text
reject empty review body
reject whitespace-modified body
reject semantically equivalent but byte-different body
reject wrong actor
reject wrong review commit_id
reject wrong decision PR HEAD
reject stale decision after candidate change
reject direct approve --why as current Human decision
reject altered PresentedMaterialEffectV1
reject omitted material-effect field
reject extra material-effect field
verify canonical JSON byte output
verify exact admission_id vector
verify complete-review-set ordering
verify complete_review_set_digest vector
verify FinalEffectGateV1 version
reject changed review set between admission and final effect
reject duplicate decision-log append
reject second local Git effect commit
reject out-of-scope local Git path
```

`tests/test_phase6_scriptops_smoke.py` MUST be updated only as needed for the corrected current route and must not normalize away the distinction between historical provenance and current authority.

## 23. Workflow requirements

`.github/workflows/x1b-human-decision.yml` MUST run the X1B authority-specific verification and tests on changes to the authorized X1B implementation surface.

The workflow is evidence support, not Human decision authority.

`CI PASS != HUMAN DECISION`

## 24. Explicit non-authorities

The implementation MUST NOT infer Human decision from any of the following alone:

```text
non-empty --why
command invocation
AI-authored text
PR conversation comment
issue comment
approval with empty body
approval on wrong commit
approval by wrong actor
old approval after candidate change
old approval after decision PR head change
successful CI
green mergeability state
presence of decision-log entry
presence of Git commit
```

## 25. Failure discipline

Future implementation and verification MUST preserve:

```text
CLAIM != EVIDENCE
AI RECOMMENDS != HUMAN DECIDES
USER CONTINUED != USER ACCEPTED
VISIBLE APPROVAL != VALID DECISION ADMISSION
STALE APPROVAL != CURRENT HUMAN DECISION
SELF-CONSISTENT DIGEST != NORMATIVELY COMPLETE EFFECT DESCRIPTION
```

Missing authority-critical evidence is not PASS.

## 26. Implementation completion conditions

A future implementation may be proposed as implementation-complete only if all of the following are demonstrated against the exact authorized implementation candidate:

```text
1. implementation remains inside authorized R4 surface;
2. current/recovery truth files are corrected and mutually consistent;
3. approve --decision-pr <N> is the only operative current Human-decision route;
4. direct approve --why is disabled for current Human-decision attribution;
5. R4 canonical JSON contract is implemented exactly;
6. exact review-body parser is implemented exactly;
7. admission_id formula is implemented exactly;
8. PresentedMaterialEffectV1 schema and digest are implemented exactly;
9. CompleteReviewSetV1 reconstruction and digest are implemented exactly;
10. FinalEffectGateV1 exact version and record are implemented exactly;
11. currentness is rechecked immediately before effect;
12. effect cardinality is exactly one accepted transition, one decision-log append, one local Git commit;
13. restore reconstructs corrected current authority;
14. repository verifier checks corrected authority model;
15. all required tests and workflow checks pass;
16. historical prototype parts outside authorized surface remain unchanged.
```

Implementation completion does not itself establish Human acceptance, X1B closure, or V1 authority.

## 27. Expected future review focus

The separately authorized independent AK-CANON R4 review should attack at minimum:

```text
current-state authority completeness
normative self-containment
canonical JSON determinism
review-body exactness
admission identity determinism
material-effect normative completeness
review-set reconstruction determinism
FinalEffectGate currentness
restore correctness
historical/current authority separation
implementation-surface closure
```

## 28. STOP boundary

This R4 artifact authorizes no implementation.

After durable freeze of this brief:

```text
X1B SUPERSEDING IMPLEMENTATION BRIEF R4 PREPARATION
= PASS / NOT PASS / BLOCKED
```

and STOP.

The next stage, if separately Human-authorized, is:

```text
INDEPENDENT AK-CANON X1B
SUPERSEDING IMPLEMENTATION-BRIEF R4 REVIEW
```

No ScriptOps mutation is permitted under this brief-preparation authority.
