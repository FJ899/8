# X1B-FRAME PR37 F041 repair — Human authority

Date: 2026-09-06
Disposition: HUMAN ACCEPT — EXACTLY ONE BOUNDED F041 REPAIR

The Human explicitly said `Accept` after instructing that the already-started conservative cycle be finished first, with faster batched review only afterwards.

This authority is bound to:

- repository: `FJ899/scriptops`
- PR: `#37`
- exact repair input HEAD: `a504b33e0420d3ac487a1d69aeddebc6719dcd62`
- exact input TREE: `590da6890ba88334aeec59a908eacb52adbade5c`
- exact verifier blob: `b4df7351df142d20507aab2eff4ae2991ddc9acb`
- base: `2f22843ac570498b506101addeba5453ab777f08`
- finding: `FJ899/8 PR #366`, `X1B-FRAME-F001-IMPLEMENTATION-F041 — quoted indented-code leaf boundary omission`
- independent review authority: `FJ899/8 PR #365`

Authorized work is exactly one conservative bounded F041 repair cycle:

1. audit preservation constraints before repair;
2. modify only the minimum F041 surface, expected to remain `scripts/verify_repository.py` only;
3. preserve F040 and all earlier regressions F039..F006 and the frozen 12-path PR37 candidate surface;
4. keep one replacement commit over the frozen base;
5. require local compile/full verifier PASS;
6. require both remote workflows PASS on the exact replacement HEAD;
7. freeze completion evidence;
8. STOP before the next review mode transition.

The Human also expressed a preference to accelerate subsequent review by batching attacks after this conservative F041 cycle is complete. That preference is not repair authority for unknown future findings and does not waive any required Human gate for writes.

Not authorized: merge of PR #37 or PR #35, ScriptOps `main` movement, deploy, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority.
