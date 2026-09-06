# X1B-FRAME PR37 F018 repair apply continuity

The F018 repair is already Human-authorized under `FJ899/8 PR #243`.

Exact live pre-repair target remains:

- `FJ899/scriptops PR #37`
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `467a4d1be44f11cbfa8ada85885397b4c7283d40`
- TREE `d7ab8679065844e93d979b0712f5eadb4b73758a`
- verifier blob `178881c7fe485b054a265462b908d69ff44bb9a6`

Prepared patch:

- file: `X1B_FRAME_PR37_F018_REPAIR.patch`
- bytes: `3647`
- SHA-256: `d34123fd1372212883856a89e8364ebdabe5b730475bcbf736eb02156bf3826d`
- intended relative change: only `scripts/verify_repository.py`

Repair behavior:

- physical nonblank Markdown lines are folded by paragraph before authority parsing;
- punctuation at a physical line end is not trusted as a security boundary;
- exact F018 ellipsis bypass, abbreviation-tail and period-tail variants must reject through the production validator;
- benign multiline negative variants must still pass;
- existing F017-F006 regressions must remain green.

The current connector does not provide a safe patch-apply/file-upload route to mutate the existing ScriptOps PR branch while preserving the exact one-commit-over-BASE replacement shape. No ScriptOps ref/tree/commit/main mutation was attempted by this record.

No new Human acceptance is required to execute this exact already-authorized repair in the retained local clone. Post-repair independent re-review still requires a separate Human gate.
