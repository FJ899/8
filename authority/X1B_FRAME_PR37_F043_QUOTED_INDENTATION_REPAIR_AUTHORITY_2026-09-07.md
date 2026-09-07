# X1B-FRAME PR #37 F043 quoted-indentation repair authority

Human authorization: continue autonomously for bounded non-consequential review/repair work until a consequential or ambiguous gate is reached.

This record binds that standing instruction to exactly one bounded verifier-only repair of the F043 finding recorded in `FJ899/8 PR #405`.

Exact repair target:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- failing HEAD: `38224167a9e056f5bcfd8def79c1c62f916ca798`
- failing TREE: `55ba29b70be4ead7eb362f14f2985aef16f87930`
- verifier entrypoint blob: `36eeadeddd7cc255ff2d8d67020938d662456eeb`
- finding: `X1B-FRAME-F001-IMPLEMENTATION-F043-BLOCKQUOTE-LAZY-INDENTATION-ERASURE`

Authorized repair boundary:

1. Preserve source indentation when deciding whether a quoted multiline definition continuation is structurally interrupting.
2. Keep normalized/trimmed payload only for the already-reviewed single-line definition grammar oracle.
3. Add the exact reproducer `> [This file]:\n    #\n> grants release authority.` as a regression.
4. Preserve all earlier F009-F043 regressions and frozen overlays.
5. F042 and F044 remain OPEN / unrepaired.

Allowed completion actions are limited to one replacement implementation commit on PR #37, the existing verifier/smoke workflows, and non-consequential completion evidence if green.

No merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action is authorized.
