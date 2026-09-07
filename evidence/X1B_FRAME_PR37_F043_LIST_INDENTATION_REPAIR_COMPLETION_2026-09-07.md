# X1B-FRAME PR #37 F043 list multiline indentation repair completion

Authority: `FJ899/8 PR #424`
Finding: `FJ899/8 PR #423`
Disposition: **REPAIR COMPLETE / GREEN**

Exact final binding: BASE `2f22843ac570498b506101addeba5453ab777f08`, HEAD `4e533f4dffe08142c614eff0292744d68e57e52e`, TREE `8ab5a76cf6930897fc7edd3fb985c58cf5a9486a`, verifier `dc3ffcdf59fb23dffa20cffbdafe18bdef7ce659`, frozen prior plain setext-title verifier `7ccdfe7500ffb342396b0883918a9b4cf403d554`, one replacement commit, 28 changed paths.

The repair preserves indentation remaining after the owning list content indent for block-precedence testing; lazy indentation omission still uses the physical line; normalized payload remains the grammar input. Exact reproducer `- [This file]:\n      #\n  grants release authority.` and a real list-owned ATX negative control are pinned. All previous F009-F043 regressions remain chained. F042/F044 remain OPEN/unrepaired.

Verification: `Verify repository state` run `34165647659` completed/success and explicitly PASSes `F043 list multiline source-indentation regression`; `Phase 6 ScriptOps smoke` run `34165647660` completed/success including repository verifier and full deterministic Phase-6 regression.

No merge, main movement, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 authority is granted.
