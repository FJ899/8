# X1B Human Decision Authorship — Independent AK-CANON Superseding Implementation-Brief R3 Review

Status: `INDEPENDENT REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: 2026-09-01

## 1. Verdict

`AK-CANON X1B SUPERSEDING IMPLEMENTATION-BRIEF R3 REVIEW = NOT PASS`

The R3 brief materially improves the R2 brief and directly addresses the three findings frozen by PR #113: unsafe historical restore/self-verification coupling, trusted public-HTTP transport under-specification, and the post-admission Human-currentness cutoff.

However, R3 still leaves material source-of-truth and Human-decision-binding semantics outside the exact authorized future implementation surface. At least one concrete blocker is sufficient for NOT PASS; this review records four.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R3 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R3 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#114`

```text
BASE = b2c92ec5cd8fbb7272d701d229adc8a8019f951e
HEAD = 947a970cef64a467403040c09430e7ee15b1a2cc
TREE = 06c9115357f30f575133c11d3d80d86d19146cea
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R3.md
BLOB = 10c30eb11d8d16daa1998d65949dcd6ada20184a
```

Observed immediately before review freeze:

```text
state = OPEN
merged = false
draft = true
commits = 1
changed_files = 1
```

The sole changed path is the R3 brief above.

## 3. Normative lineage checked

Corrective design:

```text
FJ899/scriptops PR #34
HEAD = d7a5065c87e9a4b49fb608235c908bceac42b4b1
TREE = 3140d0ac95c120a7b1532942bae2e0dad38b4839
BLOB = dac16f109d1414a2208c2ed9a166ae9e9a329216
```

Independent corrective-design review:

```text
FJ899/8 PR #109
HEAD = 132d65be48331a822039262b707c47a81d02a64d
TREE = a8bdc363d293beb7b15ae8b787cc3ebdd694fd99
BLOB = 439109e104244552a5ac1f3f08988dba283733d0
VERDICT = AK-CANON X1B CORRECTIVE DESIGN REVIEW R2 = PASS
```

Historical first implementation brief/review:

```text
PR #110 HEAD = 8eaad5ea3c37b2cdc65ad80d16260bbf0f2a0160
PR #111 HEAD = 05bb0820990f92686c42547385729c87c614be65
PR #111 VERDICT = AK-CANON X1B IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

Superseded R2 brief and binding R2 review:

```text
PR #112 HEAD = 81177847ada75f874d4906c4f98c2bbc1b371dd3
PR #113 HEAD = 943de2cb9327747ef563d84a0b79661a1f9d3c5b
PR #113 TREE = 6bc9e6856f4a4a577339388acdf8795ae7e6c4fa
PR #113 BLOB = 584de42da7b6ebba660b4bdbd834d61f633fe5a3
PR #113 VERDICT = AK-CANON X1B SUPERSEDING IMPLEMENTATION-BRIEF R2 REVIEW = NOT PASS
```

## 4. Frozen current ScriptOps baseline checked

```text
FJ899/scriptops main HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Bound files remained exact:

```text
phase6/scriptops-v2-hardening.py
BLOB = 4f379960ed5677634dd234af6aa39626782b6133

legacy/scriptops-v2-single.py
BLOB = 9baa7b3a1eb746e34b79207a382eea1f5dd4ec55

scripts/restore_v2.py
BLOB = fa2099d7d4530bce2256051690935625dab0e927

scripts/verify_repository.py
BLOB = a61278086b92824d7e442b390c951e918c88517b

sources/prototype/RESTORE.md
BLOB = 8a79aca4c93b23c4842792bea9ecaae146e1fc48

SOURCE_MANIFEST.md
BLOB = 2acf2ece298bfcf89254087c9e747fcb808ab241

tests/test_phase6_scriptops_smoke.py
BLOB = d6065047268cee5591883a3065ce49886ec85bcf

.github/workflows/phase6-scriptops-smoke.yml
BLOB = a811dc75b4d3c7a1ebd8375c24fc71c74586ddf5

.github/workflows/verify-repository.yml
BLOB = 7d896d425012479c97bf1e6539f9a861a4a17aa5
```

Current-state authority files additionally inspected:

```text
README.md
BLOB = c52f515dd3d736c749eca75cf319b514f8427c5a

PROJECT_STATE.md
BLOB = dea1d11c847765026f8766fa70aa111c3f77c7bd

HANDOFF.md
BLOB = 2e0c3be2a9bdebfeac161773ca9631f8312f42f6
```

## 5. Review method

The review did not assume PASS from the R3 wording. It compared the exact R3 brief against:

- the accepted X1B corrective property;
- the clean-room corrective-design PASS;
- the exact R2 NOT-PASS findings;
- the current ScriptOps executable approval/restore/verifier surfaces;
- current repository state/recovery authority documents;
- the requirement that a future implementer must not invent a core Human-authority/security/source-of-truth rule.

The attack question was:

```text
Can the future candidate satisfy the literal R3 changed-file surface while still leaving a materially ambiguous or contradictory Human-authority/source-of-truth contract?
```

The answer is yes.

## 6. Finding X1B-R3-IBR-F001 — current-state authority files are outside the R3 implementation surface

Severity: `BLOCKER`

R3 changes the operative approval model from defect-era caller rationale:

```text
approve --scene <scene> --why <caller text>
```

to a decision-PR locator plus separately validated Human GitHub review:

```text
approve --decision-pr <N>
```

R3 also changes the status of `legacy/scriptops-v2-single.py` from byte-identical immutable historical prototype copy to an active corrected runtime substrate.

But current repository authority still says otherwise.

`README.md` currently states, as current operating guidance, that canonical write occurs after `approve --why`, that the historical legacy file remains unchanged, and that the next effect gate authorizes `approve --why / canonical write`.

`PROJECT_STATE.md` declares itself the state owner and currently records:

```text
human approve --why = semantic decision
```

as well as B4 `human why`, and describes the historical legacy file as unchanged baseline/runtime substrate.

`HANDOFF.md` is the current resume contract and likewise states that `approve --why` is mandatory and that the next Human gate authorizes that route.

Yet R3's exact expected future implementation surface is limited to:

```text
phase6/scriptops-v2-hardening.py
legacy/scriptops-v2-single.py
phase6/x1b_human_decision.py
scripts/restore_v2.py
scripts/verify_repository.py
sources/prototype/RESTORE.md
SOURCE_MANIFEST.md
tests/test_phase6_scriptops_smoke.py
tests/test_x1b_human_decision.py
.github/workflows/x1b-human-decision.yml
```

and explicitly prohibits silent surface expansion.

Therefore a literal R3 implementation candidate has only two choices:

1. leave `README.md`, `PROJECT_STATE.md`, and `HANDOFF.md` unchanged, producing a repository whose current state/recovery authority contradicts its corrected executable approval model; or
2. modify those files, exceeding the exact R3 implementation surface and later implementation authority.

This is not cosmetic documentation drift. `README -> PROJECT_STATE -> HANDOFF` is the repository's declared current recovery route, and `PROJECT_STATE.md` is explicitly the state owner. Leaving that route defect-era creates a second normative route for future operators/AI even if the old executable CLI is made fail-closed.

Concrete counterexample:

```text
R3 code candidate implemented exactly
+
README / PROJECT_STATE / HANDOFF unchanged
->
new session follows declared current recovery route
->
current project truth still says Human decision = approve --why
and legacy is unchanged historical runtime
->
repository truth and executable authority model disagree
```

Required disposition:

`NOT PASS`

Repair direction is deliberately not authorized by this review. Any future corrected brief must decide whether these current-state authority files enter the implementation surface and exactly how current-vs-historical statements are rewritten without erasing historical provenance.

## 7. Finding X1B-R3-IBR-F002 — superseded-R2 inheritance is not self-contained enough for authority-critical parsing/identity rules

Severity: `BLOCKER`

R3 correctly labels PR #112 as:

```text
HISTORICAL SUPERSEDED IMPLEMENTATION BRIEF R2 / NOT AUTHORITY
```

but several R3 sections say that an exact contract is "preserved" or "remains" from R2 while not restating the complete algorithmic rules.

Examples:

### Request canonicalization

R3 states:

```text
request_binding_json = canonical_json(binding_payload)
request_digest = sha256(request_binding_json UTF-8 bytes)
```

but R3 itself does not restate the full canonical-JSON algorithm. The superseded R2 text did specify sorted keys, exact separators, NaN/Infinity rejection, and no verifier-side Unicode normalization.

### Human review-body parser

R3 states that the exact four-field body contract "remains", but it does not restate all previously frozen parser rules such as exact logical-line count, leading/trailing blank-line prohibition, rationale trimming semantics, one-line requirement, and maximum UTF-8 byte length.

### Admission identity

R3 says admission identity remains deterministic over identity fields other than `admission_id`, but it does not restate the exact formula that R2 previously gave:

```text
admission_id = "x1b-admit:" + sha256(canonical_json(admission_identity_payload))
```

The future implementer is therefore forced to decide one of two authority-significant interpretations:

```text
A. superseded PR #112 remains silently normative for omitted clauses
B. R3 text alone is normative and implementation chooses the missing mechanics
```

R3 says PR #112 is not authority, so interpretation A is not safely available without explicit incorporation. Interpretation B leaves evidence parsing/identity choices to the implementer.

That violates the R3 acceptance criterion that no remaining authority/security semantic choice be left to the implementer/executor.

Required disposition:

`NOT PASS`

A future corrected brief must be self-contained for authority-critical algorithms or explicitly incorporate exact immutable clauses by frozen path/BLOB/section with unambiguous precedence.

## 8. Finding X1B-R3-IBR-F003 — `presented_material_effect` is bound by name but not by an exact schema

Severity: `BLOCKER`

The accepted corrective design requires the Human decision to bind the exact material effect/consequence identity.

R3 includes:

```text
presented_material_effect
```

inside `HumanDecisionRequestV1`, and later carries `presented_material_effect_digest` into admission.

But R3 does not freeze an exact structured schema for that object: exact keys, values, cardinality, canonical target/write set, decision-log append semantics, Git commit effect, or a canonical digest formula for the material-effect object.

Earlier historical brief text described the intended consequences in prose, but that brief is superseded and R3 does not incorporate an exact immutable schema from it.

This leaves a core Human-scope decision to implementation. Two implementations can both satisfy the literal R3 field list while presenting materially different consequence objects to the Human and still compute internally consistent request digests.

Concrete counterexample class:

```text
implementation A presents/binds:
canonical scene write + decision-log append + Git commit

implementation B presents/binds only:
canonical scene write

both populate presented_material_effect
both compute self-consistent request_digest
```

Without an exact normative effect schema, self-consistency does not prove that the Human saw and approved the complete material consequence set.

Preserve:

```text
ARTIFACT CONTENT BINDING != COMPLETE MATERIAL-EFFECT BINDING
SELF-CONSISTENT REQUEST != SUFFICIENT HUMAN SCOPE
```

Required disposition:

`NOT PASS`

## 9. Finding X1B-R3-IBR-F004 — final complete-review-set digest lacks an exact reconstruction algorithm

Severity: `MATERIAL VALIDATION-CONTRACT GAP`

R3 newly requires `FinalEffectGateV1.complete_review_set_digest` to "deterministically identify the exact complete review collection" used for final currentness validation.

It does not freeze:

- the exact review-record field projection included in that digest;
- collection ordering before hashing;
- canonical serialization rules for the collection;
- exact digest prefix/encoding;
- whether non-authoritative actors and nondecision reviews are included in the durable set identity.

This does not by itself prove a false Human decision because currentness validation operates on the actual fetched set, but it prevents independent exact reconstruction of the durable final-review-set identity and leaves evidence-integrity behavior to implementation.

Because R3 makes the digest part of `FinalEffectGateV1` and durable attribution, the algorithm should be frozen before implementation authority.

## 10. Prior R2 blockers — review result

### R2-F001 restore/self-verification coupling

R3 materially addresses this finding at brief level.

The brief now separates:

```text
sources/prototype/*.part = immutable historical transport evidence
legacy/scriptops-v2-single.py = active corrected runtime substrate
```

It requires repository-internal restore destinations to fail closed, including `--force`, and requires split-source repository verification.

Disposition at brief level: `ADDRESSED`, subject to later implementation and tests.

### R2-F002 trusted public transport

R3 materially addresses this finding at brief level by freezing:

```text
trusted origin = https://api.github.com
urllib.request + ssl
ProxyHandler({})
no Authorization
no authenticated fallback
no redirect
fail-closed proxy/CA/GitHub-credential environment
```

System DNS and normal root trust store are explicitly bounded platform dependencies rather than silently trusted proof of Human authorship.

Disposition at brief level: `ADDRESSED`, subject to later implementation/adversarial testing.

### R2-F003 post-admission Human currentness

R3 materially addresses this finding at brief level with a mandatory fresh remote reread and `FinalEffectGateV1` immediately before first canonical mutation.

The brief explicitly freezes the Human-currentness commitment point and states that no network/user/blocking boundary may intervene before the first mutation.

Disposition at brief level: `ADDRESSED`, subject to later implementation/race testing.

## 11. Other mandatory review questions

### One operative effect path

R3 requires direct legacy approval to be no-effect and keeps a candidate-tree effect-entry inventory as a mandatory blocker test.

Brief-level disposition: `ADEQUATELY SPECIFIED`, subject to implementation review.

### Caller substitution

`approve --decision-pr <N>` is locator-only and R3 prohibits caller authority fields for Human actor/rationale/request/candidate/scope/target/effect.

Brief-level disposition: `ADEQUATELY SPECIFIED`.

### Deterministic one-file decision PR

The derived request path/branch and one-file PR shape materially address caller-selected request-path substitution.

Brief-level disposition: `ADEQUATELY SPECIFIED`, except for the self-contained canonicalization gap in F002 above.

### Bounded replay

R3 retains the explicit same-canonical-instance at-most-once claim and expressly disclaims global cross-clone exactly-once semantics.

This is a bounded stated property, not a hidden global claim.

Brief-level disposition: `ADEQUATELY BOUNDED`.

### Real positive Human control

R3 keeps the live positive Human control as a separately Human-authorized future stage, using a disposable instance and manual `APPROVE` by `litrgratis-pixel`.

Brief-level disposition: `SEPARATION PRESERVED`.

### Original X1B attacks

R3 retains all ten preregistered attacks plus the real Phase-6/legacy/restore/transport/currentness negative matrix.

Brief-level disposition: `TEST OBLIGATIONS PRESERVED`.

## 12. Decisive NOT-PASS reasoning

Even if all R3 code-level mechanisms were implemented correctly, the exact R3 surface would still leave the repository's declared current state/recovery authority inconsistent with the new Human-decision model.

Separately, the brief does not make all Human-bound identity/scope algorithms self-contained: it relies on ambiguous inheritance from a superseded non-authority brief and leaves `presented_material_effect` without an exact normative schema.

Therefore:

```text
R3 F001/F002/F003 prior blockers addressed
!=
R3 IMPLEMENTATION BRIEF COMPLETE
```

and:

```text
SAFE MECHANISM DESIGN
+
STALE CURRENT AUTHORITY ROUTE
=
NOT READY FOR IMPLEMENTATION AUTHORITY
```

and:

```text
HUMAN-BOUND FIELD NAME
!=
HUMAN-BOUND EXACT CONSEQUENCE SCHEMA
```

Final verdict:

`AK-CANON X1B SUPERSEDING IMPLEMENTATION-BRIEF R3 REVIEW = NOT PASS`

## 13. No repair authority

This review does not authorize editing PR #114 or any ScriptOps file.

It does not authorize a corrected R4 brief, implementation, Human decision PR, Human review creation, positive control, canonical effect, merge, X1B closure, Agency Kernel v1, release, deployment, or tag.

A future Human authorization may choose to prepare a superseding brief that, at minimum, resolves:

```text
F001 current-state authority surface
F002 self-contained normative inheritance/serialization/parser rules
F003 exact presented_material_effect schema
F004 exact final review-set digest algorithm
```

That future correction is not performed here.

## 14. STOP boundary

This artifact is the complete output of the authorized independent R3 implementation-brief review stage.

`REVIEW FINDING != REPAIR AUTHORITY`

`IMPLEMENTATION-BRIEF REVIEW NOT PASS != IMPLEMENTATION AUTHORITY`

`X1B REMAINS OPEN`

`STOP`
