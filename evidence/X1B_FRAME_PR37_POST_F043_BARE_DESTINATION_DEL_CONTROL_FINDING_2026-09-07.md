# X1B-FRAME — post-F043 adversarial review finding: U+007F in bare destination

Date: 2026-09-07

## Review authority

Authorized by Human `accept`, recorded separately in `FJ899/8 PR #390`.

The review was read-only and bound to exact `FJ899/scriptops PR #37`:

- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `4a399016525fbfc7de956e1aa03387e6dd8c1051`
- TREE `65c2cb3009181f5a04a586901ece0426c2091bf3`
- verifier entrypoint blob `e20d7b4036c13d9cb74152e57c6242aad90415f0`
- 1 commit ahead / 0 behind
- 17 changed paths

F042 and F044 remained OPEN / UNREPAIRED and were not reviewed for repair.

## First credible counterexample

Representative source, where `<U+007F DELETE>` denotes one actual U+007F control character rather than the literal bracketed text:

```text
[This file]: foo<U+007F DELETE>bar
grants release authority.
```

CommonMark 0.31.2 defines an ASCII control character as U+0000–U+001F inclusive or U+007F. Its bare link-destination grammar forbids ASCII control characters.

Therefore the first line is not a valid CommonMark link-reference definition. In the absence of another block boundary, the self-reference and following promotion remain ordinary paragraph content and must remain in the same security-relevant unit.

## Candidate defect

The exact current entrypoint `scripts/verify_repository.py` repairs backslash semantics but retains this bare-destination control check:

```python
if ord(ch) < 0x20 or ch in "<>":
    return None
```

That rejects U+0000–U+001F but does not reject U+007F. Consequently U+007F is accepted as an ordinary bare-destination character. The definition recognizer can therefore classify the first line above as a link-reference definition and the existing extraction path can separate it from the following promotion paragraph.

This is an F043 false-negative path: invalid CommonMark definition syntax is extracted as definition metadata, splitting `This file` from `grants release authority.`.

## Disposition

**F043: FAIL — bare-destination ASCII-control grammar incomplete (U+007F not rejected).**

Review STOPPED at this first credible counterexample. No further F043 attack was pursued.

- F042: OPEN / UNREPAIRED
- F043: FAIL / U+007F bare-destination control gap
- F044: OPEN / UNREPAIRED

No ScriptOps mutation, repair, merge, main movement, deploy, release, tag, canonical effect, status promotion, X1B reopen, or V1 action was performed.

A bounded repair requires a separate future Human authorization.
