# X1B-FRAME — Human acceptance of PR #37 F011 and bounded repair authority

Date: `2026-09-05`

Human input in the active project session:

```text
accept
```

This accepts the exact F011 finding recorded in `FJ899/8 PR #219` against:

```text
FJ899/scriptops PR #37
BASE = 2f22843ac570498b506101addeba5453ab777f08
HEAD = 9abf9c847604631d16ea2ae573bf06258b4e3cbe
TREE = 18be3bc04421e09abfce1f74943eed4dbb17c7f8
STATE = OPEN / DRAFT / UNMERGED
```

Accepted finding:

`X1B-FRAME-F001-IMPLEMENTATION-F011 — NEGATION GRAMMAR TOO NARROW / VALID NON-AUTHORITY WORDING FALSE POSITIVE`.

Exactly one bounded replacement repair of existing `FJ899/scriptops PR #37` is authorized, exclusively for F011.

Repair constraints:

- keep exactly one commit over frozen BASE `2f22843ac570498b506101addeba5453ab777f08`;
- preserve the same frozen twelve-path base-relative implementation surface;
- relative to current PR #37 HEAD `9abf9c847604631d16ea2ae573bf06258b4e3cbe`, only `scripts/verify_repository.py` may change;
- preserve F009 free-form Layer-B self-promotion rejection;
- preserve the F010 correction that ordinary technical `binding` wording alone is not authority promotion;
- correct the F011 false positive so clear negative forms such as `does not itself authorize` remain accepted;
- preserve F008/F007/F006 regressions;
- run verification before any independent re-review.

If verification or re-review produces a first credible counterexample, record a durable finding and STOP.

This authority does not authorize PR #37 merge, ScriptOps main movement, PR #35 merge/rebase/cherry-pick, deployment, release, tag, canonical effect, active-product status promotion, X1B reopen or V1 action.

`AI PROPOSES != HUMAN DECIDES`
`REVIEW FINDING != REPAIR AUTHORITY`
`IMPLEMENTATION CANDIDATE != MERGE AUTHORITY`
