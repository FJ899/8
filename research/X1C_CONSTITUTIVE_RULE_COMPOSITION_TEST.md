# X1C — Constitutive-Rule Composition Test

Date: 2026-08-30
Status: RESEARCH ARTIFACT / NO X1D / NO V1 / NO IMPLEMENTATION / NO NOVELTY CLAIM

## Research question

Test whether the following composition is sufficient to justify a public decision-attribution predicate without claiming access to private Human mental state:

```text
Security Ceremony
+ independently justified Counts-As / Constitutive Rule
+ Injective Agreement / Correspondence
+ Exact Referent / Execution Binding
+ Provenance / Non-Repudiation
=> HumanDecisionAttributionJustified(C,S,I) = TRUE
```

Then attack the composition using observationally equivalent counterhistories.

The test intentionally does **not** introduce new formal primitives.

## Epistemic target

The previous predicate:

```text
HumanDecision(C,S,I)=TRUE
```

is stronger than the evidence model can responsibly claim because it may be read as asserting a private psychological state.

This test therefore uses the narrower public/normative predicate:

```text
HumanDecisionAttributionJustified(C,S,I)=TRUE
```

Meaning:

> the system has sufficient public, observable and normatively justified grounds to attribute the bounded act to the Human as a decision concerning exact content C, scope S and decision instance I.

This does **not** claim direct knowledge of private Human intent.

## Existing formal pieces

### 1. Security ceremony

Defines roles, interaction surfaces, Human-visible presentation, observable Human actions, machine actions and communication paths.

### 2. Counts-As / constitutive rule

Existing institutional-action literature formalizes contextual rules of the form:

```text
X counts as Y in context K
```

The key point is that the physical/observable act X need not itself possess the institutional meaning Y outside the relevant context. The context and constitutive rule supply the public institutional semantics.

Relevant prior art includes Grossi, Meyer and Dignum's formal analyses of counts-as and institutional-action logics.

Important consequence:

```text
EVENT LABEL != DECISION SEMANTICS
```

does not imply that decision semantics are impossible to formalize. It implies that the semantics must be grounded by an independently justified constitutive rule rather than by naming the low-level event `HumanAccept`.

### 3. Injective agreement / correspondence

Binds a completed System-side attribution to a unique corresponding Human-side ceremony run and agreed data.

Candidate agreement data:

```text
M = (C,S,I,DecisionType)
```

This provides exact referent/instance correspondence and anti-replay structure.

### 4. Referent / execution binding

Ensures that the content and scope later treated as authorized are the same content and scope covered by the Human decision-attribution event.

### 5. Provenance / non-repudiation

Preserves durable evidence of the relevant principal/event relationship under the assumed security model.

### 6. Observational-equivalence attack

For any candidate attribution rule, search for:

```text
H1: HumanDecisionAttributionJustified(C,S,I)
H0: attribution is NOT justified
```

such that the System observes the same relevant trace and all adopted structural properties still hold.

If such H0 exists, the composition is insufficient.

## The constitutive rule under test

Do not use the trivial rule:

```text
click_accept counts-as HumanDecision
```

because that merely renames the event-label problem.

Instead, test a schema:

```text
ObservableHumanAct A
counts-as
ValidHumanDecisionAct(C,S,I)
in domain/context K
iff independently justified validity conditions Q_K hold.
```

Then:

```text
ValidHumanDecisionAct(C,S,I)
+ injective agreement on (C,S,I)
+ preserved binding/provenance
=> HumanDecisionAttributionJustified(C,S,I)
```

## Candidate cross-domain validity families

The literature suggests recurring public validity families rather than a single proven universal rule:

```text
Q-PRESENTATION
  the interaction presents that a decision is being requested;

Q-REFERENT
  exact relevant content/scope/decision instance is made available and bound;

Q-AFFIRMATIVE-ACT
  the Human performs an affirmative act whose public function is acceptance/decision rather than mere presence, navigation or continuation;

Q-CHOICE
  a meaningful refusal / alternative path exists where the domain requires voluntariness;

Q-NO-SILENT-DEFAULT
  silence, inactivity, preselection or unrelated continuation are not silently promoted to decision;

Q-NO-MATERIAL-MISREPRESENTATION
  the decision surface does not materially misstate the act/referent being attributed;

Q-CONTINUITY
  later mutation/supersession cannot inherit the attribution silently.
```

These are candidate recurring families only. This artifact does **not** claim that they are universally necessary/sufficient.

## Attack 1 — arbitrary constitutive declaration

Rule:

```text
pressing Continue counts-as Decision(A)
```

No independent domain or normative justification is supplied.

H0:

Human presses Continue to move to the next screen and the system attributes acceptance of A because the designer declared the rule.

All later agreement/binding/provenance can be perfect.

Result:

```text
FAIL
CONSTITUTIVE DECLARATION != JUSTIFIED CONSTITUTIVE RULE
```

Therefore `counts-as` alone is insufficient.

## Attack 2 — clear affirmative act but hidden/misrepresented referent

Human performs a genuine affirmative decision-shaped act, but the presented content is incomplete or materially different from operative C/S.

Agreement may bind the machine record to the wrong/misrepresented C/S.

Result:

```text
FAIL unless presentation/referent validity is independently constrained.
```

This is covered structurally only after `Q-PRESENTATION + Q-REFERENT + binding` are explicit.

## Attack 3 — exact referent but no meaningful decision semantics

Exact C,S,I are visible somewhere in the interaction, but the Human act is a generic continuation gesture whose public function is not clearly acceptance.

Result:

```text
FAIL unless Q-AFFIRMATIVE-ACT / decision semantics are part of the constitutive conditions.
```

Thus exact binding does not itself create a decision act.

## Attack 4 — affirmative acceptance under coercive/non-voluntary context

In domains where voluntariness is constitutive of valid consent, a Human may press a clear Accept control for exact C,S,I while lacking a meaningful refusal path or being subject to a prohibited manipulative design.

The trace can still satisfy origin, agreement, binding and provenance.

Result:

```text
ATTRIBUTION VALIDITY BECOMES DOMAIN-NORMATIVE.
```

A universal security trace cannot determine on its own whether the act is valid consent where the domain requires freedom/voluntariness.

## Attack 5 — domain transfer

Assume one universal Q-set derived from payment confirmation.

Apply it unchanged to:

```text
medical consent
Git code approval
privacy consent
creative canon acceptance
employment decision
financial transfer
```

Counterexample:

A condition constitutive in one domain is irrelevant or insufficient in another. For example, payment authorization can be strongly parameter-bound without satisfying disclosure/understanding duties characteristic of informed medical consent; privacy-consent voluntariness constraints do not map mechanically to every Git approval.

Result:

```text
UNIVERSAL Q-SET NOT ESTABLISHED.
```

## Key hypothesis tested

> There may be no domain-independent complete set `Q1...Qn`; there may instead be a domain-independent constitutive schema whose validity conditions are supplied by the relevant domain.

The reviewed counts-as literature strongly supports the contextual nature of constitutive rules: `X counts as Y in context K` is explicitly context-relative rather than universally valid.

Therefore the current evidence favors:

```text
UNIVERSAL SCHEMA
+
DOMAIN-SPECIFIC / DOMAIN-JUSTIFIED VALIDITY CONDITIONS
```

rather than:

```text
ONE UNIVERSAL COMPLETE Q-SET
```

This is a research conclusion, not yet a theorem that no universal Q-set can exist.

## Reconstructed composition

The strongest no-new-primitive model supported by the present research is:

```text
1. Domain K supplies independently justified constitutive validity conditions Q_K.

2. Security ceremony exposes the relevant presentation/context and observable Human act A.

3. If Q_K is observably satisfied:
      A counts-as ValidHumanDecisionAct_K(C,S,I)

4. Injective agreement/correspondence establishes a unique matching Human/System run on (C,S,I).

5. Binding establishes that later operative content/scope equals the accepted referent or requires observable supersession.

6. Provenance/non-repudiation preserves attribution evidence.

7. Only then:
      HumanDecisionAttributionJustified_K(C,S,I)=TRUE
```

## Observational-equivalence re-test

### H1

All domain-valid Q_K conditions hold, Human performs the relevant observable act, ceremony/agreement/binding/provenance all hold.

### H0-A — private mental difference only

Human performs the same publicly valid act under the same valid context but internally experiences uncertainty, regret or a different private feeling.

Trace is the same.

This H0 no longer falsifies the **public attribution** predicate because the predicate intentionally does not claim private mental-state truth. The public act counts-as the institutional/normative decision under Q_K.

Therefore:

```text
PRIVATE-MENTAL-STATE EQUIVALENCE
DOES NOT BY ITSELF FALSIFY
HumanDecisionAttributionJustified_K
```

This resolves the previous false target.

### H0-B — invalid context hidden from system observation

Suppose some condition constitutive of Q_K is not observable in the trace used by the attribution system — for example, prohibited manipulation, missing mandatory disclosure, or a domain-specific invalidating condition outside coverage.

Then H1 and H0 can produce the same system-visible trace while attribution validity differs.

Result:

```text
INSUFFICIENT OBSERVATION COVERAGE
```

The composition is sufficient only relative to an explicitly defined observation/coverage boundary for all constitutive conditions the domain claims are necessary.

### H0-C — arbitrary Q_K

If Q_K is simply authored by the system designer without independent normative/domain justification, the same trace can be declared valid by definition.

Result:

```text
FORMAL PROOF WOULD BE CIRCULAR.
```

Therefore the provenance of the constitutive rule itself matters.

## Verdict

The previous verdict:

```text
BLOCKED — SEMANTICS CANNOT BE GROUNDED FROM THE TESTED TRACE MODEL
```

is no longer the strongest supported conclusion.

Semantic grounding **can** be represented using existing counts-as / constitutive-rule machinery without proving private Human intent.

However, the composition is not universally sufficient from security structure alone because validity depends on context/domain constitutive conditions and on observation coverage of those conditions.

Current verdict:

```text
COMPOSITION CONDITIONALLY SUFFICIENT
— RELATIVE TO INDEPENDENTLY JUSTIFIED DOMAIN RULE Q_K
— AND COMPLETE OBSERVATION OF ITS REQUIRED CONDITIONS
```

Equivalently:

```text
NO NEW DECISION-SEMANTICS PRIMITIVE DEMONSTRATED AS NECESSARY.
NO UNIVERSAL COMPLETE Q-SET ESTABLISHED.
```

## Exact remaining gap candidate

The candidate gap has narrowed from decision semantics to governance/composition:

> How should an AI-assisted system identify, version, apply and evidence the authoritative domain-specific constitutive rule `Q_K` under which an observable Human act counts as a valid public decision act, without letting the AI/system invent or silently change those rules?

This is **not yet a novelty claim**.

It may already be addressed by normative systems, policy/authorization logics, governance frameworks, legal-computational models or institutional rule systems.

## Revised status

```text
SEMANTIC-GROUNDING: STRONG PRIOR ART / COMPOSITION AVAILABLE
UNIVERSAL Q-SET: NOT ESTABLISHED
DOMAIN-INDEPENDENT SCHEMA: STRONGLY SUPPORTED
POTENTIAL GAP: AUTHORITATIVE DOMAIN-RULE GOVERNANCE + EVIDENCE COMPOSITION
NOVELTY: NOT ESTABLISHED
```

## Consequence for Project 8

Do not build X1D.
Do not build V1.
Do not implement an authentication/broker/signature system.
Do not invent a new decision logic.

The current research increasingly suggests that Project 8 should **compose existing formalisms** rather than introduce a new foundational primitive.

The next decision should be whether to:

```text
A. stop formal-novelty exploration and adopt the composition as the theoretical basis;

or

B. perform one final literature pass specifically on authoritative policy / constitutive-rule governance and provenance before closing the novelty question.
```
