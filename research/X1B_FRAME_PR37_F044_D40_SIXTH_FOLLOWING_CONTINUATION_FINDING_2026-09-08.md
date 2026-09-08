# X1B-FRAME PR #37 F044-D40 finding

Disposition: **FAIL — REPRODUCIBLE SIXTH-POSITION ADJACENT CASE**

Exact reviewed GREEN predecessor:

- repository: `FJ899/scriptops`
- pull request: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `f750b6ee5dcb7e55d0815b232220f6559c9df033`
- TREE: `46db54cbc6c0ebeb139f77c818a66e78c0990e5a`
- verifier entrypoint blob: `14a99f1bce97a08c84eb1cee2c1245af93b7fab3`

Finding ID: `F044-D40-SIXTH-FOLLOWING-CONTINUATION`

Representative family:

- the D39 fifth following sibling owns a two-line ordinary continuation run;
- a sixth following sibling then owns exactly one ordinary continuation line;
- a later same-level sibling carries `grants release authority.`;
- the target self-reference remains earlier in the same quoted-list family.

D39 deliberately leaves sixth/later following continuation outside its repair boundary. The exact source therefore remains unchanged by D39's pre-normalizer; the predecessor still fuses the earlier self-reference with the later promotion-bearing sibling and produces a false-positive forbidden-self-promotion rejection.

This finding confirms that the exact-position D30-D39 sequence has reached another position boundary. It does **not** authorize another positional repair or a position-generic tail-sibling refactor. Continuing the positional overlay ladder would widen the current bounded repair program and requires a separate Human scope decision.

Isolated probe `FJ899/scriptops PR #85` retained the exact GREEN D39 verifier byte-for-byte as `scripts/verify_repository_probe_base.py`. Verify run `34271663409` completed/success and explicitly printed `[PASS] F044-D40 probe reproduces sixth-following-continuation false positive`; smoke run `34271663364` completed/success including the deterministic regression. Probe closed without merge.

No repair is recorded by this finding. No merge, main movement, deployment, release, tag, canonical effect, status promotion, X1B reopen or V1 action is recorded.
