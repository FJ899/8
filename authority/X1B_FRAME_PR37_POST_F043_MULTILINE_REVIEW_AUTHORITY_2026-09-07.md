# X1B-FRAME — Human authority for post-F043-multiline adversarial review

Date: 2026-09-07

Human authorization in the controlling session: `accept`.

This authorizes exactly one read-only adversarial review of the current bounded implementation candidate:

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `3a9bac7b36be067999717b0819137c6a9524b063`
- TREE: `3402de92c468cd90b0b82c8bb48e63b2c15e408f`
- verifier entrypoint blob: `c2b5a356e744be802d204ab8eaea901e76aa1219`
- pinned prior F043 overlay blob: `61bf107ad59da33a6576032d341b41c538d0453a`
- pinned F041 core blob: `be645c1a3ee49a04d700a3ef7fde86a92e413a14`

Review order and stopping rule:

1. Re-attack F043 first, including the multiline repair surface and paragraph/container precedence.
2. Preserve F042 and F044 as known OPEN/unrepaired findings; do not silently reclassify or repair them.
3. Continue only until the first credible counterexample on the declared review frontier or PASS.
4. On a credible counterexample, STOP and record exactly that finding/root cause.

This authority is read-only with respect to `FJ899/scriptops PR #37`.

Not authorized:

- repair or replacement commit;
- merge or movement of ScriptOps `main`;
- deployment, release, tag;
- canonical effect;
- active-product status promotion;
- X1B reopen;
- V1 authority or new capability.

`REVIEW AUTHORITY != REPAIR AUTHORITY`
