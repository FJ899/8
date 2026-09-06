# X1B-FRAME PR37 F027 repair completion evidence — 2026-09-06

This record freezes completion evidence for the already Human-authorized bounded F027 repair of `FJ899/scriptops PR #37`.

It grants no new authority.

## Authority / finding chain

- Finding: `X1B-FRAME-F001-IMPLEMENTATION-F027` — `FJ899/8 PR #287`.
- Bounded repair HumanDecision authority: `FJ899/8 PR #288`.
- Patch continuity: `FJ899/8 PR #289`.
- The F027 repair authority is consumed by the completed repair recorded here.

No post-repair review, merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, PR35 integration, X1B reopen or V1 authority is created by this record.

## Exact ScriptOps repaired binding

Repository: `FJ899/scriptops`

PR: `#37`

Branch: `impl/x1b-frame-f001-two-layer-status-correction-20260905`

Frozen BASE / sole parent:

`2f22843ac570498b506101addeba5453ab777f08`

Pre-F027 OLD HEAD:

`72f1e00c45a58c107a4e4f2a90cccd92fa76cbe9`

Pre-F027 OLD TREE:

`9b9f858d2b505809332e85c6cbf506d8f031a441`

Pre-F027 verifier blob:

`914ff100f03b23268a0a96db57103727e912a569`

Post-F027 NEW HEAD:

`0f7d34476c33fdc0e530f22e3168791c600c17e1`

Post-F027 NEW TREE:

`615af6e036dd1f6beaa818713984a2c18b1ee475`

Post-F027 verifier blob:

`9292d0e637229c0d87b57519a6a10fd3cb5d8df3`

Commit message:

`X1B-FRAME: bounded F027 repair over frozen base`

Remote commit readback shows exactly one parent, the frozen BASE above.

## Exact PR topology / frozen implementation surface

Remote PR #37 remains:

- OPEN;
- DRAFT;
- UNMERGED;
- exactly one commit over frozen BASE;
- exactly twelve changed paths relative to BASE.

Those twelve paths are exactly:

1. `DECISION_LOG.md`
2. `HANDOFF.md`
3. `PROJECT_STATE.md`
4. `README.md`
5. `RECONSTRUCTION_REPORT.md`
6. `SOURCES.md`
7. `SOURCE_AUDIT_SUMMARY.md`
8. `SOURCE_MANIFEST.md`
9. `scripts/verify_repository.py`
10. `sources/Decision_Summary_Current_State.md`
11. `sources/RC1_SCOPE_LOCK.md`
12. `sources/ScriptOps_Main_Theme_Summary.md`

No runtime, workflow, test, restore, acceptance, evidence or other supporting path entered the BASE-relative PR37 surface.

## F026 -> F027 verifier-only proof

Because F026 and F027 replacement commits are siblings with the same frozen BASE, an ordinary GitHub commit comparison reports the shared BASE-relative candidate surface and is not the proof of the repair boundary.

The repair boundary is frozen by direct tree/blob readback:

- OLD root tree: `9b9f858d2b505809332e85c6cbf506d8f031a441`;
- NEW root tree: `615af6e036dd1f6beaa818713984a2c18b1ee475`.

Every top-level entry SHA is identical between those trees except the `scripts` subtree.

OLD `scripts` tree:

`81c62714dc7e735eea7a03fc9fcc9f416078e7b9`

NEW `scripts` tree:

`031336864bc37a18a820598a29d41ef0a3933a8d`

Inside those trees:

- `scripts/restore_v2.py` remains exactly `fa2099d7d4530bce2256051690935625dab0e927`;
- only `scripts/verify_repository.py` changes:
  - OLD `914ff100f03b23268a0a96db57103727e912a569`
  - NEW `9292d0e637229c0d87b57519a6a10fd3cb5d8df3`.

Therefore F026 -> F027 is verifier-only.

## F027 repair behavior

The bounded repair corrects the CommonMark list-item ownership case in which a nonempty list item starts with indented code after more than four columns of post-marker whitespace.

For that special case, ownership indentation follows the CommonMark `W+1` rule instead of treating the full physical post-marker whitespace width as the list item's continuation indent.

Ordinary one-through-four-column list indentation remains unchanged.

The repair includes non-vacuous regressions covering the exact ordered-list finding plus bullet/nested cases and boundary/dedent/sibling controls, while preserving prior F026 through F006 behavior.

## Local verifier result supplied during execution

On the exact repaired worktree, the full verifier completed successfully and printed PASS for:

- required bounded/protected paths;
- immutable protected sentinels;
- Layer A exact registry;
- Layer B path-class denial;
- current bootstrap agreement;
- provenance fences;
- runtime separation;
- historical decision preservation;
- rejection matrix R1-R24;
- F009 through F027 regressions, including:
  - `[PASS] F026 ASCII-only ordered-list marker regression`
  - `[PASS] F027 indented-code list-item ownership regression`;
- runtime transition positives P7/P8;
- checkout-local X1B frame/status coherence;
- `ACTIVE PRODUCT REMEDIATION ASSERTION = CURRENTNESS_UNESTABLISHED`;
- no active-product promotion from recognized runtime profiles;
- `offline verification != remote-main/deployment proof`.

The exact locally observed NEW verifier blob was:

`9292d0e637229c0d87b57519a6a10fd3cb5d8df3`

## Exact-head GitHub Actions result

Both required PR-triggered workflows completed successfully on exact NEW HEAD `0f7d34476c33fdc0e530f22e3168791c600c17e1`:

1. `Verify repository state`
   - run number: `150`
   - run ID: `34035206872`
   - status: `completed`
   - conclusion: `success`
   - head SHA: `0f7d34476c33fdc0e530f22e3168791c600c17e1`
   - head tree: `615af6e036dd1f6beaa818713984a2c18b1ee475`

2. `Phase 6 ScriptOps smoke`
   - run number: `96`
   - run ID: `34035206874`
   - status: `completed`
   - conclusion: `success`
   - head SHA: `0f7d34476c33fdc0e530f22e3168791c600c17e1`
   - head tree: `615af6e036dd1f6beaa818713984a2c18b1ee475`

## ScriptOps main isolation

After the F027 replacement push and workflow completion, `FJ899/scriptops main` remains exactly:

`2f22843ac570498b506101addeba5453ab777f08`

Therefore this repair did not move ScriptOps main and did not create deployment, release, canonical-effect or active-product-state evidence.

## Disposition

F027 bounded repair: COMPLETE.

F027 repair authority: CONSUMED.

Current repaired candidate for any future separately authorized review is exactly:

- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `0f7d34476c33fdc0e530f22e3168791c600c17e1`
- TREE `615af6e036dd1f6beaa818713984a2c18b1ee475`
- verifier blob `9292d0e637229c0d87b57519a6a10fd3cb5d8df3`

STOP before any independent post-F027 review.

A separate explicit HumanDecision gate is required for one post-F027 independent read-only review. If later authorized, the review order is expected to be:

`F027 -> F026 -> F025 -> F024 -> ... -> F006 -> Q5-Q15`

First credible counterexample => durable finding + immediate STOP.
