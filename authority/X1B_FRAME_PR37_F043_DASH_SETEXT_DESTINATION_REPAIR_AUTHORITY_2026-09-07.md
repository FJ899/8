# X1B-FRAME PR #37 F043 dash-setext destination repair authority

Human standing authorization: continue autonomous bounded non-consequential review/repair loops until a consequential or ambiguous gate is reached.

This record binds that standing instruction to exactly one bounded verifier-only repair of the F043 finding recorded in `FJ899/8 PR #414`.

Exact repair target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- failing HEAD: `af4ac1af91a4d0e6790b60021a72b58575f58dbc`
- failing TREE: `e75da49daba0ada67a5783eff5607cdc61e5291a`
- verifier entrypoint blob: `1601a04573f3151a60ef861f4cb0757907173805`
- finding: `X1B-FRAME-F001-IMPLEMENTATION-F043-QUOTED-DASH-SETEXT-DESTINATION`

Authorized repair boundary:

1. Admit dash-family setext-looking continuation only when it is not independently an interrupting list item or thematic break and the reference-definition candidate is still incomplete.
2. Preserve single `-` as an empty list-item boundary and `---`/longer thematic-break forms as real boundaries.
3. Preserve the existing equals-family handling, source indentation, and all prior F009-F043 regressions.
4. Add exact reproducer `> [This file]:\n--\n> grants release authority.` plus `-` and `---` negative controls.
5. F042 and F044 remain OPEN / unrepaired.

Allowed completion actions are limited to one replacement implementation commit on PR #37, the existing verifier/smoke workflows, and non-consequential completion evidence if green.

No merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is authorized.
