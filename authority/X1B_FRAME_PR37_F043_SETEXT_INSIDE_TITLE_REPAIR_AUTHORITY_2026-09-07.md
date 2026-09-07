# X1B-FRAME PR #37 F043 setext-inside-title repair authority

Human standing authorization: continue autonomous bounded non-consequential review/repair loops until a consequential or ambiguous gate is reached.

This record binds that standing instruction to exactly one bounded verifier-only repair of the F043 finding recorded in `FJ899/8 PR #411`.

Exact repair target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- failing HEAD: `913abc1d01425dea44325ba5d34f794197e5d92d`
- failing TREE: `e7b6aa2a02f510b975e0d42e65cd5b8ea4e878b6`
- verifier entrypoint blob: `d84ec2ead5cddea796bfbaa8a372faa92efce471`
- finding: `X1B-FRAME-F001-IMPLEMENTATION-F043-QUOTED-SETEXT-INSIDE-MULTILINE-TITLE`

Authorized repair boundary:

1. Permit an equals-style setext-looking line to remain in an in-progress quoted multiline reference-definition candidate when no complete definition prefix exists yet, so a later line may close the label/title.
2. If a complete definition prefix already exists before the equals-style line, preserve that line as a separate block and do not absorb it.
3. Preserve all higher-precedence real interrupters and all previous F009-F043 regressions.
4. Add the exact reproducer `> [This file]: /url "\n===\n> "\n> grants release authority.` plus a complete-definition-before-`===` negative control.
5. F042 and F044 remain OPEN / unrepaired.

Allowed completion actions are limited to one replacement implementation commit on PR #37, the existing verifier/smoke workflows, and non-consequential completion evidence if green.

No merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is authorized.
