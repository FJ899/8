# X1B-FRAME — Human acceptance of F022 bounded repair authority

HumanDecision accepted exactly one bounded F022 repair for `FJ899/scriptops PR #37`.

Exact pre-repair target:
- BASE `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD `33b6691cdebb4a5ba07d38a492976cc84230fecb`
- OLD TREE `af96d8bbdcdc5b579a438c945ded90061890a07d`
- OLD verifier blob `0a468ba609df2a3484e2fbdea57b2f7d07e7c591`

Finding: `X1B-FRAME-F001-IMPLEMENTATION-F022` from `FJ899/8 PR #262`.

Bounded repair authority:
1. keep the candidate exactly one commit over frozen BASE;
2. keep BASE-relative changed surface exactly the frozen 12 paths;
3. relative to OLD HEAD, change only `scripts/verify_repository.py`;
4. repair blank-line ownership ordering so a deep-indented marker is treated as a descendant only when the active Markdown list path actually owns that indentation;
5. preserve legitimate F021 deep descendants/siblings and same-item continuations;
6. preserve F020-F006 behavior;
7. add non-vacuous F022 regressions, including the wide ordered-item / four-space block counterexample and positive security controls;
8. complete local verification, guarded replacement commit, force-with-lease update of the existing PR37 branch, required CI, and durable completion evidence.

No authority is granted for post-repair independent review, merge, ScriptOps main movement, deployment, release, tag, canonical effect, active-product status promotion, PR35 integration, X1B reopen, or V1 action.

`AI PROPOSES != HUMAN DECIDES`
`REPAIR AUTHORITY != POST-REPAIR REVIEW AUTHORITY`
