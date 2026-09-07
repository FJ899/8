# X1B-FRAME — F043 list-lazy multiline bounded repair completion

Human repair authority: `FJ899/8 PR #380`.
Finding source: `FJ899/8 PR #379`.

Final `FJ899/scriptops PR #37` binding:

- BASE `2f22843ac570498b506101addeba5453ab777f08`
- HEAD `9422be98cf86bc889c2663aed4437e11a0f62cf2`
- TREE `9df5a0a95c3e0ff3d105d391ce58a13f5fc1906f`
- exactly 1 commit ahead / 0 behind
- exactly 15 changed paths
- verifier entrypoint blob `040365f5825c386b1e74405ca51c63edd2ca55ac`
- pinned prior F043 multiline overlay `scripts/verify_repository_f043_multiline.py` blob `c2b5a356e744be802d204ab8eaea901e76aa1219`
- pinned prior F043 single-line overlay `scripts/verify_repository_f043_singleline.py` blob `61bf107ad59da33a6576032d341b41c538d0453a`
- pinned F041 core `scripts/verify_repository_f041_core.py` blob `be645c1a3ee49a04d700a3ef7fde86a92e413a14`

Repair scope remained verifier-only and F043-only. The new layer changes only list-marker multiline definition collection so legal CommonMark list-item lazy continuation may omit some or all list content indentation while preserving the frozen block-interrupt precedence gate. F042 and F044 remain OPEN and unrepaired.

Pre-apply checks:

- exact finding reproduced by the pinned multiline collector;
- CommonMark oracle confirmed the finding shape parses as an empty list item followed by a separate promotion paragraph;
- benign controls covered full/partial indentation deletion, destination on a lazy line, multiline title, wide ordered markers, and nested list-owned definitions;
- security controls preserved `definition cannot interrupt an already-open paragraph`, authority-bearing definition metadata, and structural block boundaries;
- new entrypoint `py_compile` PASS;
- local Git blob SHA matched GitHub upload exactly.

Replacement topology:

- replacement commit `9422be98cf86bc889c2663aed4437e11a0f62cf2` has parent exact frozen BASE `2f22843ac570498b506101addeba5453ab777f08`;
- compare reports exactly 1 ahead / 0 behind;
- prior candidate tree was used as the base tree, with only the new verifier entrypoint and pinned copy of the preceding F043 multiline overlay added in the new layer;
- guarded ref update was performed only after confirming PR #37 still pointed to old HEAD `3a9bac7b36be067999717b0819137c6a9524b063`.

Required workflow evidence on exact HEAD `9422be98cf86bc889c2663aed4437e11a0f62cf2`:

- `Verify repository state` run `34093120149`: COMPLETED / SUCCESS;
- verifier log explicitly PASSes synthetic R1-R24, F009-F041, F043 single-line, F043 multiline, and `F043 list-lazy multiline link-reference-definition regression`;
- `Phase 6 ScriptOps smoke` run `34093120147`: COMPLETED / SUCCESS;
- smoke passed `Run full deterministic Phase 6 regression`.

Outstanding findings intentionally preserved:

- F042 — block-quote tab-stop/source-column loss — OPEN / unrepaired;
- F044 — nonrecursive quote-content block parsing/laziness — OPEN / unrepaired.

Disposition: F043 list-lazy multiline bounded repair COMPLETE / GREEN on the exact candidate above.

STOP before any next review/repair-mode transition. No merge, ScriptOps main movement, deploy/release/tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority is granted by this completion record.
