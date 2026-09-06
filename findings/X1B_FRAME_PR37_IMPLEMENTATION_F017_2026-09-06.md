# X1B-FRAME-F001-IMPLEMENTATION-F017

Date: 2026-09-06

## Review authority

Human-authorized independent read-only re-review recorded in `FJ899/8 PR #237`.

Exact target:

- repository: `FJ899/scriptops`
- PR: `#37`
- base: `2f22843ac570498b506101addeba5453ab777f08`
- head: `a94a4018b469ae864e4715157f00b9d765df11c0`
- tree: `420faf0b06f4b53228770735f1504b3f58d5c580`
- verifier: `scripts/verify_repository.py`
- verifier blob: `d7153ccdf4469c7355e9b6aa0926228a91e74c00`

The authorized order began at F016 and required the first credible counterexample to be recorded durably followed by STOP.

## Finding

**F017 — multiline subject/predicate fragmentation bypasses the F016 Layer-B self-promotion repair.**

A Layer-B Markdown document can contain the positive self-promotion sentence:

```text
This file,
therefore grants release authority.
```

This is ordinary Markdown line wrapping: the semantic sentence is continuous, but the verifier evaluates it as two independent physical lines.

## Mechanism

`layer_b_self_promotion_claim(text)` iterates over `text.splitlines()` and performs both the clause-local logic and the F016 normalized fallback separately for each `raw_line`.

For the counterexample above:

1. physical line 1 normalizes to `THIS FILE` and contains a self-reference but no promotion term;
2. physical line 2 normalizes to `THEREFORE GRANTS RELEASE AUTHORITY` and contains promotion terms but no self-reference term;
3. the F016 whole-line fallback is still scoped to one physical line at a time;
4. therefore no evaluated line contains both halves of the positive authority claim and `layer_b_self_promotion_claim()` returns no claim;
5. `validate_layer_b_non_authority_text()` consequently accepts the Layer-B document even though the document semantically says that the file grants release authority.

This is the same security property addressed by F016, but the repair closes punctuation/parenthetical fragmentation only within one physical line and does not close newline fragmentation.

## Classification

- authority-parser fragmentation;
- false negative;
- F016 repair incomplete;
- normal Markdown soft-line-wrap bypass;
- production Layer-B validator affected.

## Review disposition

**FAIL / STOP at F016.**

The authorized review did not proceed to F015, F014, F013, F012, F011, F010, F009, F008, F007, F006, or Q5-Q15 after this first credible counterexample.

No repair was performed.

## Required next gate

A separate Human decision is required before any bounded repair of F017. A repair gate, if granted, should remain limited to closing multiline subject/predicate fragmentation without reopening F016 through F006 and should add non-vacuous production-path regressions for positive multiline self-promotion plus benign multiline negation.

This finding grants no merge, ScriptOps main movement, PR35 integration, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen, V1 authority, or further review authority.

`AI PROPOSES != HUMAN DECIDES`

`FINDING != REPAIR AUTHORITY`
