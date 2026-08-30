# X1C Semantic Grounding Pass

Date: 2026-08-30
Status: RESEARCH ARTIFACT / NO NOVELTY CLAIM / NO X1D AUTHORIZATION / NO IMPLEMENTATION

## Research question

Can an observable Human-origin interaction be treated as a Human decision without claiming access to a private mental state, by using existing public-act semantics rather than inventing a new primitive?

Target form:

```text
ObservableAct(A, H, Ctx, C, S, I)
+ PublicGroundingConditions(Ctx, presentation, role, action)
=> CountsAs(A, HumanDecision(C,S,I), Ctx)
```

The test is whether existing literature already supplies this kind of bridge.

## Key finding

A strong pre-existing formal family does exist: **constitutive / counts-as rules for institutional actions**.

The central idea is not that a physical action is intrinsically a decision. Instead, under specified contextual and role conditions, a physical or lower-level action can **count as** an institutional action.

A representative formalization is Herzig, Lorini & Troquard, *A Dynamic Logic of Institutional Actions* (2011), which explicitly distinguishes physical actions, institutional actions, causality, counts-as and institutional power. Its formalism allows an action performed by an agent in a role to count as an institutional action in a normative context.

Relevant source:
- https://doi.org/10.1007/978-3-642-22359-4_21

This directly attacks the X1C semantic-grounding problem:

```text
EVENT LABEL != DECISION SEMANTICS
```

can be replaced by:

```text
observable action X
COUNTS AS
institutional decision act Y
ONLY IN CONTEXT K AND UNDER CONSTITUTIVE CONDITIONS Q
```

The semantic bridge therefore need not be an assertion embedded in the event label.

## Legal consent provides a domain-specific public-grounding rule

GDPR Article 4(11), Recital 32 and Court of Justice case law define consent through publicly assessable conditions: a freely given, specific, informed and unambiguous indication of wishes, expressed through a statement or clear affirmative action. Silence, inactivity and pre-ticked boxes do not qualify.

Sources:
- https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:62019CJ0061
- https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=uriserv:OJ.L_.2016.119.01.0001.01.ENG

The ICO states the point especially clearly: validity of consent is assessed using an **objective test based on facts or observable behaviour**, not private feelings, interpretations or assumptions.

Source:
- https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/consent/what-is-valid-consent/

This is highly relevant to X1C because it demonstrates an existing mature normative pattern:

```text
private mental state is not directly proven
```

but a public act can nevertheless be validly classified as consent when externally observable conditions are satisfied.

## Objective manifestation of assent

Contract law likewise commonly distinguishes private subjective intention from an objectively manifested act of assent. The objective theory of contracts treats the external manifestation as the operative basis for assent rather than attempting to prove an inaccessible internal state.

Representative source:
- Wayne Barnes, *The Objective Theory of Contracts*: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2330663

Clickwrap doctrine similarly relies on presentation/notice plus a clear affirmative manifestation such as an `I agree` action, while weaker browsewrap designs often fail because notice and assent are ambiguous.

This is another strong domain-specific precedent for:

```text
presentation + context + affirmative act
=> public assent status
```

rather than:

```text
click alone => private intent proven
```

## HCI evidence: the context cannot be treated as decorative

Consent-interface research shows that the same nominal action can be produced under materially different choice architectures. Dark patterns, defaults, obstruction and visual manipulation can change consent rates and may undermine meaningful choice.

Examples:
- Nouwens et al., *Dark Patterns after the GDPR*: https://doi.org/10.1145/3313831.3376321
- Gray et al., *Dark Patterns and the Legal Requirements of Consent Banners*: https://arxiv.org/abs/2009.10194
- Martini & Drews, *Making Choice Meaningful*: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4257979

This supports a critical consequence for the counts-as bridge:

```text
ACTION TYPE ALONE IS NOT ENOUGH
```

The constitutive context must include properties of presentation and choice conditions, otherwise the system can still classify a manipulated or ambiguous interaction as a decision.

## Consent ontologies and records

Existing consent ontologies such as GConsent/CDMM and standards such as ISO/IEC TS 27560 model consent state, context, provenance, purpose, parties, timestamps and lifecycle. They are useful for representation and evidence preservation, but their own scope generally assumes that a consent state/event has already been validly established; they do not independently solve the constitutive grounding test.

Sources:
- https://openscience.adaptcentre.ie/ontologies/gconsent/main.html
- https://www.w3.org/community/reports/dpvcg/CG-FINAL-guide-27560-20240801/
- https://journals.sagepub.com/doi/10.3233/SW-210438

Status relative to X1C:

```text
GOOD REPRESENTATION / PROVENANCE SUBSTRATE
NOT THE SEMANTIC-GROUNDING RULE ITSELF
```

## Revised composition

The previous composition was:

```text
security ceremony
+ injective agreement / correspondence
+ referent binding
+ provenance / non-repudiation
+ observational-equivalence attack
```

The literature now identifies an existing candidate bridge that was missing:

```text
constitutive COUNTS-AS rule
```

A no-new-primitive composition therefore becomes:

```text
1. Security ceremony
   establishes observable roles, surfaces, presentation and actions.

2. Constitutive / counts-as rule
   states when observable Human action X in context K counts as a public DecisionAct(C,S,I).

3. Injective agreement / correspondence
   binds that DecisionAct to the exact C,S,I and unique matching system run.

4. Referent / execution binding
   preserves the same C,S,I through later operative use.

5. Provenance / non-repudiation
   preserves attributable evidence for the public act and its context.

6. Observational-equivalence attack
   attempts to construct H0 with the same admissible evidence but without a valid counts-as decision act.
```

No new logic primitive is introduced by this composition.

## What changes in the H1/H0 counterhistory

The earlier counterhistory relied on:

```text
H1: Human performs observable action and treats it as decision.
H0: Human performs same observable action but internally treats it as continue/acknowledgement.
Trace(H1) = Trace(H0)
```

Under a public-act / counts-as semantics, **private internal interpretation alone is no longer the truth criterion**.

If the public grounding rule is validly defined and its externally testable conditions are satisfied, the act may count as the institutional decision in both H1 and H0 even if the Human later reports a different private interpretation.

That is not a proof of mental intent. It is a different claim:

```text
VALID PUBLIC DECISION ACT occurred
```

This is analogous to legal manifestation of assent or valid consent standards.

Therefore the earlier H0 no longer automatically falsifies the composition. It only falsifies it if the purported decision context fails the constitutive conditions — e.g. ambiguous presentation, misleading wording, no meaningful alternative, hidden scope, coerced action, generic `continue`, or another reason why the observable action should not count as a decision.

## Important semantic correction

This suggests that the predicate itself may need narrowing.

`HumanDecision(C,S,I)=TRUE` can be read too strongly as a claim about private psychological authorship.

The observable/formal system can more defensibly establish something like:

```text
ValidHumanDecisionAct(C,S,I) = TRUE
```

or:

```text
HumanDecisionAttributionJustified(C,S,I) = TRUE
```

where truth means that a Human-origin observable action satisfied a public constitutive rule for decision status, not that the system read the Human's mind.

This is not yet a naming decision; it is an epistemic-ceiling finding.

## Does this close the gap?

Not fully, but it substantially changes it.

The semantic-grounding problem is **not an empty research space**. Existing institutional-action logic and legal/objective consent doctrines provide the exact conceptual architecture for turning observable acts into public normative acts.

Therefore Project 8 should not claim:

```text
NO EXISTING WAY TO GROUND DECISION SEMANTICS
```

The remaining question is narrower:

> Can a domain-independent set of constitutive conditions for AI-assisted decisions be specified without merely importing domain-specific legal consent rules or smuggling the desired conclusion into the context predicate?

This is now the candidate gap.

## Strongest current attack

A counts-as rule can become circular:

```text
click X counts as HumanDecision
```

if context K is defined only by the system designer's declaration.

To avoid merely renaming the event-label problem, the grounding conditions must themselves be independently justified and observable.

Candidate condition families already strongly precedented in consent/HCI include:

- Human-origin action;
- clear affirmative action;
- explicit decision semantics in the presentation;
- exact content/scope/instance visible or otherwise reliably presented;
- specificity;
- intelligibility / clarity;
- meaningful ability to refuse or choose alternatives;
- absence of prohibited manipulation/coercion where relevant;
- no silent default / inactivity-as-consent;
- preserved binding between presented and operative referent.

The open research problem is whether these can be generalized into a stable AI-assisted-decision ceremony without creating a new bespoke decision institution.

## Revised gap status

Previous:

```text
PLAUSIBLE SEMANTIC-GROUNDING / FORMALIZATION GAP
```

After this pass:

```text
SEMANTIC-GROUNDING HAS STRONG PRIOR ART
PLAUSIBLE DOMAIN-INDEPENDENT CONSTITUTIVE-RULE GAP
NOT YET NOVELTY
```

More cautiously:

> Existing counts-as / institutional-action logic plus objective consent/assent doctrine already provides a principled way to ground public decision semantics without proving private intention. What remains unresolved in this pass is whether a domain-independent constitutive rule for arbitrary AI-assisted decisions already exists, and how its contextual validity conditions should be justified.

## Consequence for Project 8

Do not build X1D yet.

Do not invent a decision-semantics primitive.

Next step should be a **re-run of the composition test with COUNTS-AS added as existing prior art**, using externally grounded consent/meaningful-choice conditions rather than an arbitrary `HumanAccept` label.

Possible verdicts for that re-run:

```text
COMPOSITION SUFFICIENT FOR PUBLIC DECISION ATTRIBUTION
```

or

```text
COMPOSITION INSUFFICIENT — EXACT CONSTITUTIVE CONDITION GAP
```

or

```text
BLOCKED — DOMAIN-INDEPENDENT COUNTS-AS CONDITIONS CANNOT BE JUSTIFIED
```

No novelty claim is authorized by this artifact.
