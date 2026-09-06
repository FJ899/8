# X1B-FRAME PR37 F040 attempt-2 local verifier failure — 2026-09-06

## Binding

- ScriptOps target: `FJ899/scriptops PR #37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `e8e745b5787f7f98c5e2df3fd03934acee332413`
- OLD TREE: `6363566d5b36f4669e234f31cd4660a1687c0597`
- OLD verifier blob: `73504fe6897a5b6a038da39b14478a37aa36bbc7`
- F040 finding: `FJ899/8 PR #355`
- Human F040 repair authority: `FJ899/8 PR #356`
- preservation/design audit: `FJ899/8 PR #357`
- attempt-1 pre-apply evidence: `FJ899/8 PR #358`
- attempt-1 local verifier failure: `FJ899/8 PR #359`
- attempt-2 correction pre-apply evidence: `FJ899/8 PR #360`

## Local attempt-2 result

The correction delta was applied only to the already-dirty attempt-1 worktree. No ScriptOps commit, amend, or push was performed.

Observed bounded surface after correction remained:

- only `scripts/verify_repository.py`
- combined diff `+189/-2`
- `git diff --check` PASS
- Python compile PASS

The full verifier then failed before F040 completion. The first failure was a previously accepted F021 control whose source text is:

```markdown
    - This file contains background notes.

    - Release authority belongs to a separate Human gate.
```

The verifier now folds the two indented chunks into one literal indented-code block and therefore produces one security unit containing both strings. The old F021 control expected acceptance because its purpose was to prove that a four-space bullet-looking line is not a top-level list marker.

## Diagnosis

This failure is not evidence that the F040 parser should split the two chunks. CommonMark 0.31.2 §4.4 defines an indented code block as one or more indented chunks separated by blank lines; blank lines therefore do not split those chunks into distinct code blocks. The same section also establishes that ambiguity between indentation-as-code and list-item ownership is resolved in favor of an actual list item, while a standalone four-space bullet-looking line is code rather than a top-level list.

Therefore the former F021 benign expectation is structurally stale under the newly explicit F040 leaf semantics. Preserving F021 means preserving the invariant `standalone four-space bullet-looking text != top-level list`, not preserving an accidental blank-line split that CommonMark does not define.

A bounded correction may change only this regression expectation so that the same representative is required to fail as one literal code-block security unit. That strengthens rather than weakens the original F021 classification invariant: if the two lines were incorrectly parsed as separate top-level list siblings, the self-reference and authority phrase would again be split and the rejection would disappear.

No parser broadening, link-reference work, merge, main movement, deploy, release, tag, canonical effect, active-product status promotion, X1B reopen, or V1 authority is granted.

## Disposition

`F040 ATTEMPT 2 = LOCAL VERIFIER FAIL — NO SCRIPTOPS COMMIT / NO PUSH`

Continue only inside the existing Human-bounded F040 repair authority, with the smallest verifier-only expectation correction and another full local verifier run before any amend or push.
