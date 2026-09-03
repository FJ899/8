# X1B V2 F001 — Human bounded repair authorization

Status: `HUMAN REPAIR AUTHORIZATION / NOT EXECUTION AUTHORITY`

Date: `2026-09-03`

## Human act

The Human response in the controlling conversation was exactly:

```text
accept
```

That response was solicited for exactly this proposition: accept the blocker recorded by `FJ899/8 PR #160` and authorize one bounded implementation repair only for `X1B-V2-IMPL-F001`.

## Bound finding

Independent review artifact:

- repository: `FJ899/8`
- PR: `#160`
- HEAD: `0e57cc2aeb35f561bdf83094bfd88a0eb1b7625a`
- TREE: `6b3b8871527ed03dc9dfa572ce50d37b67ad9990`
- PATH: `research/X1B_HUMAN_DECISION_AUTHORSHIP_V2_IMPLEMENTATION_AK_CANON_REVIEW.md`
- BLOB: `590f1be0c83c3044114fc857fb81227297a048d0`
- finding: `X1B-V2-IMPL-F001 — MAIN-REF CAS DEREFERENCES A CONCURRENT SYMBOLIC refs/heads/main AND CAN MUTATE AN UNBOUND TARGET REF = BLOCKER`

Reviewed implementation candidate:

- repository: `FJ899/scriptops`
- PR: `#35`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- BASE TREE: `4215d9306392070e64c6fd74a6cfb813ca9d0601`
- reviewed HEAD: `4f6cb09f7d6b103afb06d511b261ac68fd9c4494`
- reviewed TREE: `02bffae1d24278590bbb8e82c4584d9ff5bb5906`

## Authorized repair

Exactly one bounded repair iteration is authorized to remove the F001 counterexample while preserving the already frozen X1B V2 mechanism and implementation surface.

The repair may change only these already-authorized implementation paths, and only as needed for F001:

```text
phase6/x1b_human_decision.py
tests/test_x1b_human_decision.py
scripts/verify_repository.py
```

The intended property is:

```text
THE CAS THAT CANONICALIZES THE EFFECT MUST UPDATE THE NAMED REF refs/heads/main ITSELF,
MUST NOT FOLLOW A SYMBOLIC refs/heads/main TO ANOTHER REF,
AND MUST FAIL CLOSED IF THE NAMED REF IS NOT THE EXPECTED DIRECT B0 REF AT CAS TIME.
```

A repair may therefore use Git's non-dereferencing ref-update semantics and direct-ref verification, and must add a deterministic regression for the exact symref-substitution counterexample.

No other implementation behavior or scope expansion is authorized.

## Required post-repair sequence

After the bounded repair:

1. freeze the repaired ScriptOps candidate against the same exact baseline;
2. retain the exact 13-path implementation firewall overall;
3. run the full existing X1B, Phase-6, and repository-verifier CI on the exact repaired HEAD;
4. conduct an independent AK-CANON re-review of the repaired candidate;
5. if and only if that review passes, prepare a fresh corrective-verification/prereg packet;
6. stop before any live decision-evidence PR, Human V2 approval, positive control, canonical screenplay effect, or other execution requiring separate Human execution authorization.

## Explicit non-authority

This `accept` does **not** authorize:

- a live X1B decision-evidence pull request;
- submitting a Human V2 approval review;
- the real positive control;
- any canonical screenplay effect;
- merging `FJ899/scriptops PR #35`;
- merging this acceptance artifact;
- X1B closure;
- V1 authority;
- release, deployment, or tag;
- repair of any finding other than `X1B-V2-IMPL-F001`;
- expansion into TPM, PMEM/NFIT, PKI/CRL, bare-metal, BMC/console, or other C-class platform hardening.

`AI PROPOSES != HUMAN DECIDES`

`REVIEW FINDING != REPAIR AUTHORITY`

`THIS HUMAN ACT = BOUNDED F001 REPAIR AUTHORITY ONLY`
