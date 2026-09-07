# X1B-FRAME — POST-F043 ADVERSARIAL REVIEW FINDING

Finding ID: `X1B-FRAME-F001-IMPLEMENTATION-F043-PARENTHESIZED-TITLE`

Review authority: `FJ899/8 PR #394`.

Exact reviewed target:
- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `96cec000860a18f01a9d3bae733a552eaff22559`
- TREE: `7ec2f777dac3bf9629019801a58ba7bc69ef8d9c`
- verifier entrypoint blob: `8dc5d3e207f3b1e82fc6384609ccc67c9c41495a`
- pinned prior bare-destination escape overlay: `e20d7b4036c13d9cb74152e57c6242aad90415f0`
- pinned destination-newline overlay: `277eb91bbcf46dfb766e39ed23962b5179450c87`
- pinned list-lazy overlay: `040365f5825c386b1e74405ca51c63edd2ca55ac`
- pinned multiline overlay: `c2b5a356e744be802d204ab8eaea901e76aa1219`
- pinned single-line overlay: `61bf107ad59da33a6576032d341b41c538d0453a`
- pinned F041 core: `be645c1a3ee49a04d700a3ef7fde86a92e413a14`

## FIRST CREDIBLE COUNTEREXAMPLE

```markdown
[This file]: /url (foo(bar)
grants release authority.
```

## Normative CommonMark semantics

A parenthesized link title is delimited by matching parentheses and may contain `(` or `)` only when those characters are backslash-escaped. Therefore `(foo(bar)` is not a valid link title. The first physical line above is not a valid link-reference definition, so the two lines remain ordinary paragraph content rather than definition metadata followed by a separate paragraph.

A local CommonMark 0.31.2 parser oracle confirms that the entire source renders as one paragraph. The escaped control `(foo\\(bar\\))` remains a valid definition, establishing that the failing boundary is specifically unescaped parenthesis grammar in a parenthesized title.

## Current implementation behavior

The pinned F043 recognizer chooses `)` as the closing delimiter when title opener is `(`, then scans until the first unescaped closing `)` but does not reject an unescaped `(` inside the title. Thus `(foo(bar)` is accepted as a title even though CommonMark forbids that internal unescaped `(`.

The invalid first line can therefore be extracted as a link-reference-definition authority unit, leaving `grants release authority.` as a separate paragraph. That creates a security-relevant F043 false negative by splitting self-reference from promotion where CommonMark keeps them in one paragraph/security unit.

## Classification

- F042: OPEN / unrepaired / not implicated by this finding.
- F043: FAIL — parenthesized link-title grammar incomplete.
- F044: OPEN / unrepaired / not implicated by this finding.

## STOP

The read-only review stops at this first credible counterexample. No repair, merge, `main` movement, deploy, release, tag, canonical effect, status promotion, X1B reopen, or V1 action was performed or authorized.
