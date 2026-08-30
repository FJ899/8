# X1D-F001 — INDEPENDENT POST-BOOTSTRAP T1–T10 AUDIT

Status: AUDIT RESULT ONLY / NO REPAIR / NO CLOSURE

Audited frozen source:
- FJ899/8 PR #66
- freeze HEAD: `6b75f31951f688c556c0d92d5f3774eed09d4b0f`
- frozen ScriptOps PR: `FJ899/scriptops#26`
- ScriptOps base: `68a1bb996e1345e2a8f86813042ff7b40109ae74`
- ScriptOps HEAD: `d7a09cd593094a1846974269c27e4a51ccb831b8`
- ScriptOps TREE: `7ba16fab7879d7640801c410f171a08f79c8168b`
- candidate CODEOWNERS blob: `5dd686893d265217d921c352df033ff72fdf910e`
- live ruleset: `CANONICAL_MAIN_PROTECTION_V1`, id `21147233`

No mutation of ScriptOps, PR #26, PR #25, A5, V1, release, deployment or ruleset was performed by this audit.

## Evidence boundary

The audit distinguishes:

`CANDIDATE ARTIFACT != LIVE ENFORCEMENT EFFECT`

GitHub evaluates CODEOWNERS for a pull request from the pull request base branch. The frozen ScriptOps base `main@68a1bb996e1345e2a8f86813042ff7b40109ae74` does not contain `.github/CODEOWNERS` (read returned 404). The CODEOWNERS file exists only on the unmerged PR #26 head.

Therefore the candidate contains the intended ownership mapping, but the frozen live main branch does not yet supply that mapping to GitHub's code-owner enforcement for PRs targeting main.

## T1–T10

### T1 — exact candidate HEAD/TREE established
PASS.

Frozen identity is exact:
- HEAD `d7a09cd593094a1846974269c27e4a51ccb831b8`
- TREE `7ba16fab7879d7640801c410f171a08f79c8168b`
- one changed file `.github/CODEOWNERS`.

### T2 — authoritative Human approval realization identified
PASS.

Bound realization from preregistration:
`C_H_APPROVE = authoritative GitHub approval capability exercised as @litrgratis-pixel`.

### T3 — Human approval capability remains outside frozen B_AI
PASS relative to the frozen B_AI threat model.

The previously established separation and Human root assertion remain the governing evidence. No new capability evidence observed in this audit supersedes that freeze.

### T4 — CODEOWNERS binds the frozen rule-bearing paths to Human approval authority
FAIL as an effective live binding.

Candidate HEAD #26 contains mappings for:
- `/DECISION_LOG.md`
- `/phase6/scriptops-v2-hardening.py`
- `/legacy/scriptops-v2-single.py`
- `/.github/`
- `/governance/`
all to `@litrgratis-pixel`.

However, the base branch `main@68a1bb...` contains no `.github/CODEOWNERS`. Because GitHub uses CODEOWNERS from the PR base branch, the frozen live target does not yet make those paths effective code-owner bindings for PRs targeting main.

### T5 — live ruleset requires at least one approving review
PASS.

Live ruleset `21147233` has `required_approving_review_count = 1`.

### T6 — live ruleset requires code-owner review
PASS at configuration level.

Live ruleset has `require_code_owner_review = true`.

This does not cure T4: a code-owner-review requirement cannot enforce the intended `@litrgratis-pixel` mapping for main-targeting PRs when main lacks the CODEOWNERS file.

### T7 — live ruleset requires last-push approval
PASS.

Live ruleset has `require_last_push_approval = true`.

### T8 — no bypass path permits frozen B_AI to evade Human authorization requirement
PASS for the live ruleset's explicit bypass configuration, relative to frozen B_AI.

Live ruleset has `bypass_actors = []` and `current_user_can_bypass = never` for the evaluated connector read.

This does not substitute for T4/T10 Human-specific binding.

### T9 — policy/ruleset mutation authority remains outside frozen B_AI and under established Human control
PASS relative to frozen B_AI.

The governing realization remains:
`C_H_POLICY = Human-operated FJ899 GitHub Web UI/admin session`, with Human root assertion and previously established technical separation from frozen B_AI.

No evidence observed in this audit supersedes that boundary.

### T10 — controlled rule-bearing PR cannot become merge-eligible without required Human authorization
FAIL / NOT ESTABLISHED for the frozen target.

The live ruleset enforces one general approving review, but the intended Human-specific code-owner mapping exists only in unmerged PR #26 and not on the base branch used by GitHub for CODEOWNERS evaluation. Therefore the frozen state does not establish that a rule-bearing PR targeting main is gated specifically by the established `C_H_APPROVE = @litrgratis-pixel` capability.

A general review requirement is not equivalent to the preregistered Human-authority requirement.

No merge-eligibility mutation/probe was performed because this audit is read-only with respect to the frozen ScriptOps target.

## Verdict

`X1D-F001 POST-BOOTSTRAP T1–T10 AUDIT = FAIL`

Primary failure:

`CANDIDATE CODEOWNERS BINDING != LIVE BASE-BRANCH CODEOWNER ENFORCEMENT`

The controlled bootstrap produced the intended CODEOWNERS artifact on PR #26 and the intended live ruleset parameters, but the frozen enforcement state is incomplete because `.github/CODEOWNERS` has not become part of the base branch used by GitHub to evaluate code ownership.

Therefore:
- `X1D-F001 VERIFIED CLOSED` — NOT ESTABLISHED
- A5 — STOP
- V1 — STOP
- PR #26 — DO NOT MERGE under this audit result unless separately authorized through a newly defined corrective/bootstrap step
- PR #25 — STOP
- release/deployment — NOT AUTHORIZED

This audit authorizes no repair and proposes no automatic state mutation.