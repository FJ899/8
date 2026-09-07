# X1B-FRAME — PR #37 F043 multiline bounded repair completion evidence

## Authority and finding binding

Human authorization: `accept`.

Repair authority: `FJ899/8 PR #376`.

Finding source: `FJ899/8 PR #375` — post-F043 read-only adversarial review found the first credible counterexample in the same F043 root cause: CommonMark §4.7 multiline link-reference definitions were not recognized by the single-physical-line F043 recognizer.

No authority was granted for F042, F044, merge, main movement, deploy, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1.

## Exact ScriptOps candidate binding

Repository: `FJ899/scriptops`

PR: `#37`

Frozen BASE:

`2f22843ac570498b506101addeba5453ab777f08`

Pre-repair candidate:

- OLD HEAD `3521a6c9f9c0db1103c49274d979766de1abfefa`
- OLD TREE `6d2a5dbcceb5fd41f9988ef63d64c77bba45b8c1`
- OLD F043 entrypoint blob `61bf107ad59da33a6576032d341b41c538d0453a`
- pinned F041 core blob `be645c1a3ee49a04d700a3ef7fde86a92e413a14`
- 1 commit ahead / 0 behind
- 13 changed paths

Completed replacement candidate:

- NEW HEAD `3a9bac7b36be067999717b0819137c6a9524b063`
- NEW TREE `3402de92c468cd90b0b82c8bb48e63b2c15e408f`
- NEW verifier entrypoint blob `c2b5a356e744be802d204ab8eaea901e76aa1219`
- pinned prior F043 single-line overlay blob `61bf107ad59da33a6576032d341b41c538d0453a`
- pinned F041 core blob `be645c1a3ee49a04d700a3ef7fde86a92e413a14`
- 1 commit ahead / 0 behind
- 14 changed paths

The replacement commit parent is exactly the frozen BASE `2f22843ac570498b506101addeba5453ab777f08`.

## OLD → NEW verifier-only delta

All top-level subtree/blob identities outside `scripts/` are unchanged from OLD TREE to NEW TREE.

Inside `scripts/`:

- `restore_v2.py` remains unchanged at blob `fa2099d7d4530bce2256051690935625dab0e927`;
- `verify_repository_f041_core.py` remains unchanged at blob `be645c1a3ee49a04d700a3ef7fde86a92e413a14`;
- the old F043 entrypoint blob `61bf107ad59da33a6576032d341b41c538d0453a` is retained byte-for-byte as `verify_repository_f043_singleline.py`;
- `verify_repository.py` becomes the new bounded multiline overlay, blob `c2b5a356e744be802d204ab8eaea901e76aa1219`.

No runtime, test, workflow, protected sentinel, restore mechanism, product-state document, canonical material, or unrelated repository surface was changed by this repair relative to the preceding PR #37 candidate.

## Repair semantics

The multiline overlay runs before the already-reviewed single-line F043 parser and folds only confirmed CommonMark §4.7 multiline link-reference-definition candidates to a single physical line while retaining all security-visible metadata text.

The repair covers the finding family rather than only the literal counterexample:

- multiline labels, including the CommonMark Example-208 shape;
- destination on the following line;
- titles on the following line;
- titles spanning multiple nonblank lines;
- consecutive definitions where a preceding definition may acquire a legal following title;
- direct list-item and nested-list definition candidates;
- explicit block-quote definition candidates.

Longest-valid-definition-prefix selection prevents a complete destination from prematurely terminating a definition when a legal title follows, while invalid would-be title text remains later paragraph content.

Frozen block precedence is mirrored while collecting multiline candidates, and the already-open paragraph rule remains authoritative after folding. Therefore a multiline definition still cannot interrupt an open top-level, list-item, or quoted paragraph.

Definition metadata remains security-relevant as one authority unit.

F042 and F044 are deliberately not repaired or reinterpreted.

## Pre-apply evidence

The new entrypoint compiled successfully with Python 3.

Local Git object identity for the entrypoint was computed as:

`c2b5a356e744be802d204ab8eaea901e76aa1219`

GitHub `create_blob` returned the exact same SHA, closing the transfer-integrity gate.

A CommonMark-compatible parser oracle was used against the multiline families before ref movement. It confirmed that the benign multiline label/destination/title, direct list, nested list and quote representatives parse as link reference definitions followed by separate promotion paragraphs, while the `cannot interrupt paragraph` control remains one paragraph.

The known F042/F044 representatives are not transformed by the F043 multiline folding path.

## Guarded replacement topology

Before ref movement, `FJ899/scriptops PR #37` still pointed to exact OLD HEAD `3521a6c9f9c0db1103c49274d979766de1abfefa`.

The unreferenced replacement commit `3a9bac7b36be067999717b0819137c6a9524b063` was verified as exactly 1 commit ahead / 0 behind the frozen BASE.

The PR branch was then force-moved from the OLD sibling commit to the NEW sibling commit because both have the same exact frozen parent. After the guarded update PR #37 reports:

- HEAD `3a9bac7b36be067999717b0819137c6a9524b063`;
- BASE `2f22843ac570498b506101addeba5453ab777f08`;
- 1 commit;
- 14 changed paths.

## Required workflow evidence

Exact NEW HEAD: `3a9bac7b36be067999717b0819137c6a9524b063`.

1. `Verify repository state`
   - run id `34091149064`
   - conclusion `success`
   - verifier log explicitly records PASS for:
     - synthetic rejection matrix R1-R24;
     - every frozen F009 through F041 regression;
     - existing `F043 CommonMark link-reference-definition extraction regression`;
     - new `F043 multiline CommonMark link-reference-definition regression`;
     - final X1B checkout-local coherence checks.

2. `Phase 6 ScriptOps smoke`
   - run id `34091149011`
   - conclusion `success`
   - repository semantic/currentness verifier PASS;
   - `Run full deterministic Phase 6 regression` PASS.

Thus the replacement candidate has full workflow integration evidence on the exact NEW HEAD.

## Outstanding findings and STOP

State after this bounded repair:

- F042 — OPEN / unrepaired;
- F043 multiline finding from PR #375 — REPAIRED / regression GREEN on the current candidate;
- F044 — OPEN / unrepaired.

This completion record does not authorize a post-repair adversarial review, any additional repair, merge, default-branch movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1 action.

STOP before the next review-mode or repair-mode transition. A new Human gate is required.
