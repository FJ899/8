# X1C — Q_K Authority & Governance Pass

Date: 2026-08-30
Status: FINAL LITERATURE PASS / NO X1D / NO V1 / NO CODE / NO NOVELTY CLAIM

## Research question

Can existing normative-systems, trust-management, policy, and rule-governance formalisms establish, version, bind, and audibly apply an authoritative domain rule `Q_K` without allowing the evaluated AI/process to define or alter the rule under which its own result is validated?

Target composition:

```text
Authority(Q_K)
+ ProvenanceVersion(Q_K, v, t)
+ Applicable(Q_K, K, request/context)
+ AuthorizedChangeControl(Q_K)
=> AuthoritativeRuleFor(Q_K, K, v, t)
```

The pass is intentionally limited to four dimensions:

1. authority — who may establish `Q_K`;
2. provenance/versioning — which rule/version was in force;
3. applicability/binding — why that rule applies to domain/context `K`;
4. change control — who may create/modify/delete the rule and who may change the authority to do so.

## 1. Authority — who may establish Q_K

### Normative power

Normative-systems literature already models institutional/normative power: an agent or role may have the recognized power to create, modify, or delete norms. Oren, Luck & Miles explicitly define powers governing creation, deletion, and modification of norms, and extend the model so powers themselves may be modified.

Representative source:
- Nir Oren, Michael Luck, Simon Miles, *A Model of Normative Power*.

This gives a direct formal analogue of:

```text
Principal P has institutional power to establish/change Q_K
```

rather than merely:

```text
P can technically edit a file containing Q_K.
```

### Delegation / root of trust

Trust-management systems such as KeyNote and Delegation Logic separately formalize who is authorized to issue policy or credentials and how authority may be delegated. KeyNote uses a distinguished `POLICY` principal as a root of trust and policy assertions to delegate authority. Delegation Logic treats authorization as proof of compliance relative to policy plus credentials and provides explicit delegation constructs.

Representative sources:
- RFC 2704, KeyNote Trust-Management System v2.
- Ninghui Li, Benjamin Grosof, Joan Feigenbaum, *Delegation Logic*.

### Result for authority

Existing formal machinery is sufficient to represent:

```text
WHO MAY ESTABLISH Q_K
WHO MAY DELEGATE THAT POWER
WHO DOES NOT POSSESS THAT POWER
```

No new foundational authority primitive is indicated.

## 2. Provenance / versioning — which Q_K governed the decision

### LegalRuleML

LegalRuleML provides particularly strong prior art for authoritative rule provenance and temporal applicability.

It models:

- textual/source provenance;
- rule creators/authors;
- authority and jurisdiction;
- temporal validity;
- entry into force;
- efficacy;
- applicability;
- rule histories and temporal change.

The specification explicitly treats authority as the person/organization empowered to create, endorse, or enforce legal norms, and models temporal dimensions because rules change over time.

Representative source:
- OASIS LegalRuleML Core Specification v1.0.

This is a strong analogue of:

```text
Q_K version v
issued/endorsed by authority A
valid/applicable during interval T
source/provenance P
```

### Temporal policy state

Trust-management/policy-analysis literature also models changing policy state over time. SPKI/SDSI policy analysis uses temporal logic to reason over policy states, which is enough to show that policy version/state at a given time is a standard formal concern rather than a new Project-8 requirement.

Representative source:
- Eamani & Sistla, *Language based policy analysis in a SPKI Trust Management System*.

### Result for provenance/versioning

Existing standards/formalisms support the evidence model needed to determine which authoritative rule/version was in force for a historical decision.

Implementation details such as Git SHA, signed bundle, append-only ledger, or database revision remain mechanism choices, not missing logic.

## 3. Applicability / binding — why this Q_K applies to domain K

### Policy targets and context

XACML explicitly models applicability through policy/policy-set `Target` conditions. A policy is evaluated only when its target matches the request context; otherwise it is `NotApplicable` or indeterminate.

Representative sources:
- OASIS XACML 3.0 / ITU-T X.1144.

This gives a direct formal pattern for:

```text
Q_K applies iff request/context matches K-specific target conditions.
```

XACML also supports policy issuers, policy sets, references, combining algorithms, delegation depth, obligations, and scoped defaults.

### Jurisdiction and context

LegalRuleML adds another domain-oriented applicability model through authority, jurisdiction, source, and temporal applicability metadata.

### Generic schema + domain extensions

RFC 3198 is especially relevant to the current hypothesis: the Policy Core Information Model is deliberately generic and cannot be used operationally without domain-specific extensions such as QoS or IPsec.

That strongly supports the current conclusion:

```text
UNIVERSAL POLICY / COUNTS-AS SCHEMA
+
DOMAIN-SPECIFIC APPLICABILITY CONDITIONS
```

rather than one universal complete `Q` set.

### Result for applicability

Existing policy frameworks already distinguish generic policy structure from domain-specific applicability and provide formal/request-context binding mechanisms.

No Project-8-specific applicability logic is required by the current evidence.

## 4. Change control — who may alter Q_K

### Normative powers over norms and powers

The strongest direct prior art is again normative-power theory.

A Model of Normative Power provides explicit semantics for agents/roles empowered to:

```text
CREATE norm
DELETE norm
MODIFY norm
```

and also to modify normative powers themselves.

That is directly relevant to the meta-governance problem:

```text
who may change Q_K?
who may change the authority model governing changes to Q_K?
```

### Procedural norms / delegated institutional roles

Normative multi-agent-systems literature distinguishes substantive, constitutive, and procedural norms. Procedural norms govern agents acting in institutional roles that recognize violations, apply sanctions, or operate the normative system. Formal work on delegation of power models agents acting on behalf of a normative system rather than as unconstrained self-authorizing actors.

Representative source:
- Boella & van der Torre, *Substantive and procedural norms in normative multiagent systems*.

### Policy trust roots and delegation

KeyNote/Delegation Logic complement this by requiring policy authority to be rooted in recognized policy/credential authority and by representing delegation explicitly.

This means a design can formally require:

```text
AI may evaluate under Q_K
AI may propose Q_K changes
AI may NOT cause Q_K to become authoritative
unless an independently authorized principal/path grants that normative power.
```

### Normative change

Separate formal work on normative change models revision, contraction, replacement, validity, and effects of changed constitutive/regulative rules. This confirms that temporal rule change is itself established prior art.

Representative source:
- *Normative change: an AGM approach* and related input/output-logic work.

## Attack the composition

The critical Project-8 attack is:

```text
Can the evaluated AI/process modify Q_K,
modify the applicability of Q_K,
or modify the authority relation that makes Q_K authoritative,
and then use that modified rule to validate itself?
```

The reviewed composition can reject this without a new logic if the model includes:

```text
A1 Authority root / normative power relation
A2 Explicit delegated powers and limits
A3 Authoritative rule provenance + version/time
A4 Applicability conditions bound to domain/request context
A5 Separate normative power for rule modification
A6 Historical preservation of superseded rule states
A7 Validation against the authoritative rule state effective for that decision instance
```

Under those conditions, an AI lacking the relevant normative power may technically propose/edit a candidate rule artifact but cannot thereby make it authoritative.

This reproduces the desired meta-principle:

```text
CAPABILITY TO MODIFY REPRESENTATION
!=
AUTHORITY TO MODIFY NORMATIVE RULE
```

and more specifically:

```text
EVALUATED ACTOR
MUST NOT BECOME RULE AUTHORITY
MERELY BY MODIFYING THE RULE ARTIFACT.
```

## Remaining implementation obligations

The literature does not choose a concrete implementation for Project 8. A real system still needs mechanisms that preserve the formal distinctions, for example:

- authoritative source/reference for Q_K;
- stable rule/version identifier;
- effective-from/effective-until or equivalent state transition;
- principal/role with normative power;
- explicit applicability/domain binding;
- auditable supersession/change record;
- enforcement that candidate/evaluated AI lacks self-authorizing change power.

Those are engineering obligations implementing established formal properties, not evidence of a missing foundational logic.

## Binary exit

### A. Existing composition found

**YES.**

The four required dimensions have established formal counterparts that compose coherently:

```text
AUTHORITY
  -> normative power + trust-management delegation/root of trust

PROVENANCE / VERSION / TIME
  -> LegalRuleML + temporal policy-state models

APPLICABILITY / DOMAIN BINDING
  -> XACML Targets + jurisdiction/context + domain extensions

CHANGE CONTROL
  -> normative powers over norms/powers + procedural norms + delegated policy authority
```

Therefore the binary exit is:

```text
A — EXISTING FORMALISMS COMPOSITIONALLY SUFFICIENT
```

and X1C can be closed at the formalism-search level as:

```text
EXISTING FORMALISMS COMPOSITIONALLY SUFFICIENT — NO NEW LOGIC REQUIRED
```

This is not a claim that one single standard implements the entire Project-8 workflow. It is a claim that no missing foundational logic has been demonstrated: the needed properties already exist across mature formal families and can be composed without inventing a new decision logic.

## Consequence for Project 8

The research line should now stop rather than continue searching for new formal primitives.

The strongest current model is:

```text
DOMAIN K
  -> authoritative constitutive rule Q_K
     established by a recognized normative authority
     with explicit provenance/version/time
     bound to K/request context
     changeable only by principals holding the corresponding normative power

OBSERVABLE HUMAN ACT
  -> counts-as under Q_K
  -> injective agreement / exact referent / unique instance
  -> provenance / binding / supersession
  -> HumanDecisionAttributionJustified_K(C,S,I)
```

No new Project-8-specific foundational logic is currently justified.

## Final status

```text
X1C FORMALISM SEARCH: CLOSED

VERDICT:
EXISTING FORMALISMS COMPOSITIONALLY SUFFICIENT — NO NEW LOGIC REQUIRED

NOVELTY CLAIM:
NONE

X1D:
NOT AUTHORIZED / NOT REQUIRED BY THIS RESULT

V1 / CODE:
NOT AUTHORIZED BY THIS RESULT

NEXT:
RETURN TO A REAL DOMAIN BOUNDARY (SCRIPTOPS)
AND TEST WHETHER THE EXISTING SYSTEM ACTUALLY PRESERVES THESE PROPERTIES.
```
