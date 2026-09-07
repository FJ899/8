# X1B-FRAME PR #37 F043 quoted setext-destination repair authority

Human standing authorization: continue autonomous bounded non-consequential review/repair loops until a consequential or ambiguous gate is reached.

This record binds that standing instruction to exactly one bounded verifier-only repair of the F043 finding recorded in `FJ899/8 PR #408`.

Exact repair target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- failing HEAD: `2a06399264dbeefadd32be5196e98c8d37937933`
- failing TREE: `a56b44a5f398595d57539fd573d0bba153f07ae0`
- verifier entrypoint blob: `3534b2551e1c9d82d1665464529d42e615dfc94d`
- finding: `X1B-FRAME-F001-IMPLEMENTATION-F043-QUOTED-SETEXT-LIKE-DESTINATION`

Authorized repair boundary:

1. In quoted multiline reference-definition collection, allow a setext-looking continuation line to be considered when it completes a valid reference definition.
2. Preserve higher-precedence real interrupters such as thematic breaks, headings, fences, HTML blocks, block quotes and interrupting lists.
3. Add the exact reproducer `> [This file]:\n===\n> grants release authority.` as a regression.
4. Preserve every previous F009-F043 regression and pinned overlay.
5. F042 and F044 remain OPEN / unrepaired.

Allowed completion actions are limited to one replacement implementation commit on PR #37, the existing verifier/smoke workflows, and non-consequential completion evidence if green.

No merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is authorized.
