# X1B Human Decision Authorship Corrective Design — Independent AK-CANON Review

Status: `INDEPENDENT CORRECTIVE DESIGN REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: 2026-09-01

Verdict:

`AK-CANON X1B CORRECTIVE DESIGN REVIEW = PASS`

This review evaluates the design-only X1B corrective candidate against the frozen X1B preregistration, the accepted real ScriptOps false-attribution finding, the current affected ScriptOps boundary, and the relevant X1C/X1D supporting lineage.

This review is not a Human decision, does not authorize implementation, does not close X1B, and does not create V1 authority.

`AK-CANON DESIGN PASS != IMPLEMENTATION AUTHORITY`

`AK-CANON DESIGN PASS != X1B CLOSED`

`X1B CLOSED != V1 AUTHORITY`

`AI PROPOSES != HUMAN DECIDES`

## 1. Exact design candidate under review

Repository: `FJ899/scriptops`

PR: `#34`

Required review-time state: `OPEN / DRAFT / UNMERGED`

BASE:

`2f22843ac570498b506101addeba5453ab777f08`

HEAD:

`d7a5065c87e9a4b49fb608235c908bceac42b4b1`

TREE:

`3140d0ac95c120a7b1532942bae2e0dad38b4839`

PATH:

`governance/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_CANDIDATE.md`

BLOB:

`dac16f109d1414a2208c2ed9a166ae9e9a329216`

The candidate contains exactly one commit and exactly one changed path relative to its frozen BASE.

## 2. Frozen normative X1B source

Repository: `FJ899/8`

Commit:

`daa9a6a8bc0bb9be8d5cdbd025e95d66d81ed601`

TREE:

`aa812bfa8fe9f482b06a7445caef52ffabdb3535`

PATH:

`experiments/X1B_PREREGISTRATION.md`

BLOB:

`6b65a2656ae254e9223e9065da20ef7443ab13cb`

Normative X1B claim preserved by the corrective candidate:

> No AI recommendation, proposal or plan may be treated as a Human decision without a separate, unambiguous Human acceptance act referring to that exact content and scope.

Required separations preserved:

```text
AI PROPOSED != HUMAN DECIDED
USER SAW != USER DECIDED
USER CONTINUED != USER ACCEPTED
AI-FILLED VALUE != HUMAN-CHOSEN VALUE
```

The preregistered ten attack classes and real positive Human control remain normative future verification inputs.

## 3. Accepted real-boundary finding

Repository: `FJ899/scriptops`

Finding PR: `#22`

Finding HEAD:

`d5455821ef183b677a06597a6496e15e58926921`

Finding TREE:

`b6f15f3ab6dbead42840c72e4d19ebeedc88ccfe`

Finding PATH:

`evidence/X1B_FALSE_HUMAN_DECISION_2026-08-30.md`

Finding BLOB:

`d8efe6139520438251eaf8c85c736b17b10d260a`

Accepted failure:

`X1B FAIL — FALSE HUMAN DECISION`

The concrete counterexample remains:

```text
AI/process possesses approve capability
+
non-empty --why
+
cmd_approve invocation
->
canonical scene write
+
durable record approver="human"
without a separately established Human decision act
```

Preserved finding principles:

`APPROVAL COMMAND POSSESSION != HUMAN DECISION AUTHORSHIP`

`NON-EMPTY WHY != HUMAN ACT`

## 4. Current affected ScriptOps boundary confirmed before review write

Canonical ScriptOps `main` remained:

`2f22843ac570498b506101addeba5453ab777f08`

TREE:

`4215d9306392070e64c6fd74a6cfb813ca9d0601`

Affected source:

`phase6/scriptops-v2-hardening.py`

Current BLOB:

`4f379960ed5677634dd234af6aa39626782b6133`

The current `cmd_approve` path still:

1. accepts a caller-supplied `--why` string if non-empty;
2. validates candidate/impact state but does not establish a separate trusted Human decision event;
3. performs the canonical scene write;
4. constructs a decision record containing hard-coded `"approver": "human"`;
5. appends the decision record and commits the effect.

Therefore the corrective candidate is still aimed at the same live failure mechanism. The current vulnerability is expected at this design-only stage and is not evidence that the design has failed; the candidate explicitly does not authorize implementation.

## 5. Supporting X1C/X1D lineage

### 5.1 X1C

`FJ899/8 PR #59`

HEAD:

`569044f65b7b64331d70c65357cf011177b7bc98`

Recorded conclusion:

`EXISTING FORMALISMS COMPOSITIONALLY SUFFICIENT — NO NEW LOGIC REQUIRED`

Relevant dimensions:

```text
authority
provenance / version / time
applicability / domain binding
change control
```

The X1B corrective candidate correctly treats this as supporting research, not implementation authority and not proof that a particular mechanism is sufficient.

### 5.2 X1D-F001

`FJ899/8 PR #73`

HEAD:

`af7e1d871c5fcf524ba23234b72389173795ca9d`

Reusable separation:

`CAPABILITY TO MODIFY RULE REPRESENTATION != AUTHORITY TO MODIFY NORMATIVE RULE`

The X1B design reuses the authority/capability distinction without claiming that X1D-F001 closure automatically closes X1B.

### 5.3 X1D-A5

`FJ899/8 PR #107`

HEAD:

`282468aee423371f265cfc8606321b36a254fa67`

Reusable separation:

```text
Human decision evidence
!=
machine admission
!=
executor capability
```

The X1B design uses the separation as a structural lesson only. It does not inherit X1D-A5 closure or treat GitHub review as an automatically selected X1B mechanism.

## 6. Independent review method

The review did not assume PASS from the candidate wording. It actively tested the design against the following possible failure modes:

1. **Circular trust label** — whether calling an event "trusted" is sufficient without an authoritative origin rule.
2. **Identity substitution** — whether a username/account label could be mistaken for a Human decision act.
3. **Credential collapse** — whether effect capability or an execution credential could also manufacture the Human evidence it consumes.
4. **Content drift** — whether acceptance of `A` could authorize `A'`.
5. **Scope drift** — whether acceptance of `S` could authorize `S'`.
6. **Candidate/effect drift** — whether a different candidate or effect could be substituted after Human acceptance.
7. **Old-consent replay** — whether historical consent could silently become current authorization.
8. **Conflict ambiguity** — whether conflicting Human events could be normalized or selected by an unstated chronology rule.
9. **Incomplete event-set acceptance** — whether admission could occur without establishing the complete relevant active decision state.
10. **Hard-coded attribution** — whether `"approver": "human"` or an equivalent caller-supplied label could remain sufficient.
11. **Synthetic-only verification** — whether the real ScriptOps failure could be replaced by a test-only substrate.
12. **Positive-control weakness** — whether a positive control could succeed without a separate real Human act and post-effect identity proof.
13. **Responsibility collapse** — whether the executor could reinterpret, replace, or create the Human decision.
14. **Mechanism smuggling** — whether GitHub review, MFA, signatures, a ledger, UI confirmation, or another product was silently made normative before properties were frozen.
15. **Premature closure/V1 leakage** — whether design review could be interpreted as implementation, closure, or V1 authority.

No contradiction was found that prevents this design from serving as the normative corrective design layer.

## 7. Review finding A — separate Human decision event is substantive, not a label

**PASS.**

The candidate requires that `HumanDecision = TRUE` arise only from a separate trusted Human decision event concerning the exact operative decision content and scope.

It expressly declares insufficient by themselves:

- command possession;
- API/process credentials;
- approval-function invocation;
- non-empty rationale;
- `Continue`;
- silence;
- AI-generated approval artifacts;
- caller-selected Human labels;
- hard-coded Human attribution;
- mere proposal visibility;
- technical effect capability.

The design additionally requires that trusted evidence be traceable to Human-authoritative origin and states:

`SHAPE MATCH != TRUSTED ORIGIN`

This defeats the principal circularity concern: an object is not trusted merely because it looks like a Human event.

## 8. Review finding B — Human-authoritative origin is separated from effect capability

**PASS.**

The design requires:

```text
AI/PROCESS EFFECT CAPABILITY
!=
HUMAN DECISION-AUTHORITY CAPABILITY
```

and:

```text
POSSESSION OF EFFECT CAPABILITY
!=
AUTHORITY TO CREATE HUMAN DECISION EVIDENCE
```

It also rejects identity-only reasoning:

```text
IDENTITY
!=
CREDENTIAL
!=
CHANNEL
!=
CAPABILITY
!=
AUTHORITY
```

A future mechanism therefore cannot satisfy the design merely by exposing a Human username or account label.

The design also requires denial when evidence is generated solely by the evaluated AI/process. This closes the specific possibility that the executor could manufacture a structurally valid event and have its own output accepted as Human evidence.

### Non-blocking implementation obligation

The phrase "Human-authoritative origin" is intentionally abstract at design stage. A later implementation brief must identify the exact source/channel/capability and demonstrate origin validation strong enough that the evaluated AI/process cannot forge or self-authorize the event. If an implementation brief fails to do that, implementation authority must not be granted.

This is a required concretization step, not a defect in the property-level design.

## 9. Review finding C — exact content/scope/candidate/effect binding

**PASS.**

The trusted Human evidence minimum includes:

```text
decision_event_id
human_actor_or_authority_identity
decision_type
exact_content_identity
exact_scope
candidate_or_proposal_identity
presented_material_effect_or_consequence_identity
decision_result
event_time_or_freshness_identity
applicable_normative_policy_identity_where_required
```

The candidate requires deterministic future identity/binding rules and the invariant:

```text
HUMAN-BOUND CONTENT/SCOPE/CANDIDATE/EFFECT
=
OPERATIVE CONTENT/SCOPE/CANDIDATE/EFFECT
```

Material mismatch is `DENY`.

This directly addresses X1B attacks involving `A -> A'`, parameter changes, scope expansion, and general-direction-to-specific-parameter substitution.

## 10. Review finding D — freshness, completeness, supersession, conflict, and replay

**PASS at the corrective-design layer.**

The candidate requires the future implementation contract to define:

- activation;
- deactivation;
- supersession;
- staleness;
- replay validity;
- multiple active-event evaluation;
- conflicting-event detection;
- the complete event set that must be considered before effect.

It explicitly rejects a silent chronology-only winner rule and requires unknown or ambiguous current decision state to fail closed.

The fail-closed list additionally covers stale, inactive, revoked, dismissed, superseded, replayed-outside-policy, ambiguous, conflicting, and incompletely enumerable evidence.

### Non-blocking implementation obligation

The design deliberately does not choose exact time windows, review APIs, supersession syntax, or collection protocols. Section 17 requires those exact rules to be frozen in the future implementation brief before implementation authority. This is an appropriate design/implementation boundary.

A future brief that leaves any of these semantics implicit would not satisfy this design review PASS.

## 11. Review finding E — Human attribution is a derived claim

**PASS.**

The candidate forbids the root defect class explicitly, including:

```text
"approver": "human" because an approval function ran
```

and:

```text
HumanDecision = TRUE because why != ""
```

It requires the durable record to reference exact trusted Human decision evidence or a stable identity sufficient for independent reconstruction.

The design therefore replaces hard-coded attribution with evidence-derived attribution.

## 12. Review finding F — decision evidence and execution credentials remain separate

**PASS.**

The design preserves:

```text
HUMAN DECISION EVIDENCE != EXECUTION CREDENTIAL
HUMAN DECISION EVIDENCE != EFFECT CAPABILITY
EFFECT CAPABILITY != AUTHORITY TO CREATE DECISION EVIDENCE
```

A process may possess canonical effect capability but still lack authority to establish the Human decision required for admission.

Conversely, a valid Human event does not grant arbitrary executor authority beyond the admitted exact action.

This is the correct response to the original ScriptOps failure, which collapsed possession of the approval/effect path into Human authorship.

## 13. Review finding G — admission boundary is sufficiently constrained

**PASS.**

Before canonical effect, the future admission boundary must validate at minimum:

- trusted origin;
- Human authority identity under applicable policy;
- event type/result;
- exact content;
- exact scope;
- exact candidate/proposal;
- material effect/consequence identity where required;
- freshness/current activity;
- applicable normative-policy identity where required;
- absence of disqualifying conflict;
- absence of unauthorized admitted/executed effect substitution.

Admission must produce machine-verifiable state/artifact that the executor consumes without reinterpreting the Human decision.

This is strong enough at design level to prevent "approve command possession" from being used as the Human-authorship predicate.

## 14. Review finding H — original X1B attack suite remains complete

**PASS.**

The candidate keeps all original attack classes normative:

1. AI marks its own proposal accepted.
2. `Continue` becomes decision.
3. silence/no response becomes consent.
4. old consent is reused for a new decision.
5. Human accepts `A`; `A'` becomes operative.
6. AI changes parameters after acceptance.
7. AI expands scope after acceptance.
8. general direction is converted into Human-attributed specific parameters.
9. AI-generated artifact impersonates a Human decision.
10. AI-filled value becomes Human-chosen value.

The candidate also makes the current real ScriptOps `cmd_approve` failure a mandatory regression and prohibits replacing it with synthetic-only testing.

This satisfies the most important continuity requirement from the original falsification.

## 15. Review finding I — acceptance-test semantics are observable

**PASS.**

The design requires the future verification packet to define PASS/FAIL/BLOCKED before execution and mandates at minimum:

- negative attacks demonstrate `HumanDecision != TRUE` and no unauthorized canonical effect;
- positive control demonstrates `HumanDecision = TRUE` only after trusted Human evidence and exact admission;
- current-event completeness is established before effect;
- malformed/unknown/conflicting evidence denies;
- accepted content/scope/candidate/effect equals operative content/scope/candidate/effect;
- Human attribution is reconstructable from the exact trusted event;
- executor cannot replace or create trusted Human evidence using its effect credential;
- real ScriptOps boundary is included.

The design also preserves the original falsification discipline: the first credible counterexample must be durably recorded before repair and terminate that run.

## 16. Review finding J — real positive Human control is not a fake success path

**PASS.**

The required positive control includes:

```text
exact proposal/content/scope/effect information
+
separate real Human decision act
+
trusted exact Human decision event
+
machine validation of that event
+
exact matching operative candidate
->
HumanDecision = TRUE
->
authorized effect
```

Post-effect verification must prove content, scope, candidate, effect, attribution provenance, absence of AI-created substitute evidence, and absence of stale/conflicting evidence becoming operative.

This is materially stronger than merely obtaining a green command result.

## 17. Review finding K — responsibility separation is explicit

**PASS.**

The candidate separates conceptual responsibilities:

```text
Human authority channel
trusted Human decision evidence
Human decision evidence verifier
operation/effect admission boundary
effect executor
canonical target
independent observer / post-effect verification
durable audit record
```

It expressly states that the executor must not be the authority that creates the Human evidence it needs.

The architecture therefore preserves the core X1B authorship boundary instead of placing all trust decisions inside `cmd_approve`.

## 18. Review finding L — future implementation brief is sufficiently constrained

**PASS.**

Before implementation authority, the future brief must freeze at least:

- exact repository/surfaces;
- exact trusted Human authority source/channel;
- concrete event representation;
- complete event collection semantics;
- origin validation;
- deterministic content/scope/candidate/effect identities;
- freshness/supersession;
- conflict;
- replay;
- machine admission artifact/state;
- executor no-substitution rule;
- durable attribution/provenance;
- positive control method;
- all ten attacks plus current real `cmd_approve` regression;
- independent replay/evidence strategy;
- STOP conditions.

This is enough to prevent an implementation brief from silently substituting a product name or account identity for Human decision authorship.

No implementation authority follows from this review; the implementation brief itself must later be independently reviewed.

## 19. Review finding M — property is frozen before mechanism

**PASS.**

The candidate intentionally refuses to normatively select GitHub review, account identity, MFA, signatures, hardware keys, external approval services, database events, ledgers, hashes, UI confirmation, email, Slack, or an identity provider.

This is correct for the current stage because X1B failed on a property boundary: possession of the effect path was mistaken for Human authorship.

`MECHANISM != PROPERTY`

A future mechanism is acceptable only if it demonstrates satisfaction of the frozen property set.

## 20. Review finding N — supporting research is not misused as proof

**PASS.**

The candidate uses X1C and X1D as supporting structural inputs only.

It does not claim:

- X1C formal sufficiency automatically implements X1B;
- X1D-F001 closure closes Human authorship;
- X1D-A5 Human D0/GitHub review must be reused as the X1B mechanism;
- a prior governance PASS supplies implementation authority.

This avoids circular inheritance of unrelated closure decisions.

## 21. Review finding O — V1 boundary is preserved

**PASS.**

The candidate states:

`X1B OPEN != V1 ENTRY AUTHORITY`

and denies Agency Kernel v1 design, implementation, branch creation, version declaration, migration, release planning, release, deployment, and tag.

It permits a future V1 entry decision only after X1B closure or by a separately explicit Human decision that intentionally treats unresolved X1B as a blocker/input without falsely calling it closed.

No V1 authority is inherited from this design or this review.

## 22. Contradictory-evidence search and disposition

The following potential contradictions were specifically evaluated.

### 22.1 "Trusted event" could be merely a renamed AI artifact

**Not supported.**

The design requires authoritative origin, traceability, origin validation, and denies evidence generated solely by the evaluated AI/process. It explicitly says shape match is not trusted origin.

### 22.2 A Human account label could be treated as proof of a Human act

**Not supported.**

The design separates identity, credential, channel, capability, and authority and says a username/account label is insufficient without the complete authority/event-binding contract.

### 22.3 The executor could create its own approval evidence through a second interface

**Normatively denied, implementation proof still required.**

The design forbids the executor/evaluated process from manufacturing the trusted evidence it consumes and requires a distinguishable Human-authority capability/channel. A future implementation brief must prove the selected source satisfies this property.

### 22.4 Freshness/conflict/replay are under-specified

**Acceptably deferred, not omitted.**

The property-level design requires these semantics, fail-closed ambiguity, complete event-set evaluation, and explicit implementation-brief freeze. It does not yet choose mechanism-specific rules, which is appropriate before implementation authorization.

### 22.5 The material-consequence requirement could disappear

**Not supported.**

The minimum trusted-evidence binding includes `presented_material_effect_or_consequence_identity`, and the positive control requires exact proposal/content/scope/effect information plus post-effect equality.

### 22.6 The real failure could be replaced with a synthetic test

**Not supported.**

The design explicitly mandates the real ScriptOps `cmd_approve` regression in addition to the original ten attack classes.

### 22.7 Current ScriptOps is still vulnerable, so design should fail

**Incorrect interpretation.**

The current vulnerability confirms target relevance. This stage is design-only and explicitly forbids implementation. Design PASS cannot mean implementation PASS or closure.

### 22.8 X1D-A5 closure could be read as X1B closure

**Not supported.**

The design expressly says X1D closure does not itself close X1B and retains the full X1B corrective closure composition.

### 22.9 Design review could leak into V1 authority

**Not supported.**

The candidate and this review both explicitly deny that inference.

No unresolved contradiction was found that requires `NOT PASS` or `BLOCKED` at the corrective-design layer.

## 23. Required review questions — final answers

1. **Does the design preserve the exact original X1B Human-authorship claim?**  
   `YES / PASS`.

2. **Does it directly address the real `cmd_approve` false-Human-decision mechanism?**  
   `YES / PASS`.

3. **Does it require a separate Human decision event rather than command possession or rationale text?**  
   `YES / PASS`.

4. **Is trusted origin distinguished from shape, identity label, execution credential, and effect capability?**  
   `YES / PASS`.

5. **Are exact content, scope, candidate, and effect identities bound?**  
   `YES / PASS`.

6. **Are freshness, activity, supersession, conflict, replay, and event-set completeness required and fail-closed?**  
   `YES / PASS at design layer`; exact mechanism rules remain mandatory implementation-brief work.

7. **Is Human attribution derived from validated trusted evidence rather than hard-coded?**  
   `YES / PASS`.

8. **Are all ten original X1B attacks preserved?**  
   `YES / PASS`.

9. **Is the real current ScriptOps boundary a mandatory regression surface?**  
   `YES / PASS`.

10. **Does the positive control require a real separate Human decision act and exact post-effect truth?**  
    `YES / PASS`.

11. **Are verifier, admission, executor, observer, canonical target, and durable attribution responsibilities separated?**  
    `YES / PASS`.

12. **Is the future implementation brief constrained enough to prevent silent mechanism assumptions?**  
    `YES / PASS`.

13. **Does the candidate avoid prematurely selecting a concrete authentication/approval product?**  
    `YES / PASS`.

14. **Does the candidate avoid claiming access to private Human mental state?**  
    `YES / PASS`; it evaluates trusted observable decision evidence and attribution justification.

15. **Does any unresolved condition prevent progression to a separately authorized implementation-brief stage?**  
    `NO`.

## 24. Verdict

`AK-CANON X1B CORRECTIVE DESIGN REVIEW = PASS`

The exact PR #34 corrective design is coherent with the frozen X1B preregistration and accepted real-boundary finding. It closes the design-level ambiguity that allowed effect-path possession and a non-empty rationale to stand in for Human decision authorship. It defines a non-circular trusted-origin property, exact decision binding, fail-closed current-event requirements, evidence-derived attribution, real regression obligations, a real positive Human control, responsibility separation, and a sufficiently constrained future implementation-brief contract.

The review found no design-level blocker requiring correction before a separately authorized implementation-brief stage.

The following remain mandatory and unresolved because they belong to later stages:

- selection of an exact Human-authority mechanism/channel;
- proof that the selected channel cannot be forged/self-authorized by the evaluated process;
- exact event representation;
- exact collection/completeness protocol;
- exact freshness, supersession, conflict, and replay rules;
- deterministic identity algorithms;
- concrete admission artifact/state;
- implementation surfaces;
- independent implementation review;
- fresh preregistered corrective verification;
- all negative attacks;
- real positive Human control;
- post-effect truth;
- independent corrective-closure review;
- Human corrective-closure acceptance.

Those unresolved implementation/verification obligations do not make the property-level design incomplete; the design explicitly requires them to be frozen before implementation authority and closure.

## 25. Non-authority and STOP

This PASS authorizes nothing beyond recording this review.

It does not authorize:

- implementation brief creation;
- `cmd_approve` modification;
- legacy ScriptOps modification;
- Human decision event creation;
- canonical scene mutation;
- decision-log mutation;
- X1B corrective execution;
- PR #34 modification or merge;
- Q_K or CODEOWNERS mutation;
- Agency Kernel v1;
- release;
- deployment;
- tag.

Next stage, if Human-authorized separately:

`X1B CORRECTIVE IMPLEMENTATION BRIEF PREPARATION`

`AK-CANON DESIGN PASS != IMPLEMENTATION AUTHORITY`

`AK-CANON DESIGN PASS != IMPLEMENTATION REVIEW PASS`

`AK-CANON DESIGN PASS != X1B CLOSED`

`X1B CLOSED != V1 AUTHORITY`

`AI PROPOSES != HUMAN DECIDES`
