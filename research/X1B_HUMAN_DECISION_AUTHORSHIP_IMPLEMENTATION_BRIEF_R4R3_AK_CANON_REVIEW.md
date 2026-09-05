# X1B Human Decision Authorship — Independent AK-CANON R4R3 Implementation-Brief Review

Status: `INDEPENDENT REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: `2026-09-01`

## 1. Verdict

`AK-CANON X1B R4R3 IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

R4R3 materially improves R4R2 and directly repairs the previously frozen local-ref, write-target-alias, and freshness/supersession gaps at brief level. It also replaces the prior porcelain effect path with substantially stronger plumbing, hook, filter, signing, environment, exact-blob/tree/commit and rollback requirements.

However, independent adversarial review found two residual material Git-isolation blockers inside the claimed `HOOK_FILTER_SAFE_GIT_PLUMBING_V1` effect boundary:

1. Git replacement refs (`refs/replace/*`) remain enabled by default and can substitute the object/tree meaning of the exact Human-bound parent SHA while preserving `HEAD == refs/heads/main == request.repository_head_at_request`;
2. repository-local Git config remains active for `git commit-tree`, and `i18n.commitEncoding` can add an unbound `encoding` header to the resulting commit object despite the claimed deterministic exact commit metadata.

The first finding can expand the raw resulting commit beyond the exact two Human-bound paths while local replace-aware verification still reports only those two paths. The second finding permits ambient repository-local config to transform the durable commit object after `FinalEffectGateV3` without violating the currently enumerated commit checks.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R3 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R3 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#120`

```text
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
BASE TREE = df807db7003dfd201e9be4d5927472e515a2e737
HEAD = df095fc822f6b454bc69e24e727c9b9dcfe64844
TREE = ad625ba054ba0c38d3dfd1baf3b7980753c553a2
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R3.md
BLOB = 17521e2f3616bdc356c4dca4c13c96fcd5114117
```

Immediately before review write, PR #120 remained:

```text
state = OPEN
merged = false
draft = true
commits = 1
changed_files = 1
```

The reviewed HEAD and one-file candidate identity were freshly re-read before this review branch was created.

## 3. Normative lineage

### 3.1 Accepted corrective design

```text
FJ899/scriptops PR #34
HEAD = d7a5065c87e9a4b49fb608235c908bceac42b4b1
TREE = 3140d0ac95c120a7b1532942bae2e0dad38b4839
PATH = governance/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_CANDIDATE.md
BLOB = dac16f109d1414a2208c2ed9a166ae9e9a329216
```

The higher-level accepted design requires, among other things:

```text
exact content/scope/candidate/effect binding
fresh/current Human evidence semantics
executor no-substitution
fail closed on ambiguity
no core authority/security choice left implicit
post-effect truth matching the Human-bound effect
```

### 3.2 Independent corrective-design review

```text
FJ899/8 PR #109
HEAD = 132d65be48331a822039262b707c47a81d02a64d
TREE = a8bdc363d293beb7b15ae8b787cc3ebdd694fd99
BLOB = 439109e104244552a5ac1f3f08988dba283733d0
VERDICT = AK-CANON X1B CORRECTIVE DESIGN REVIEW R2 = PASS
```

### 3.3 R4R2 predecessor and binding review

```text
FJ899/8 PR #118
HEAD = b2c5de19ef678b18899751915060df5397edeb1b
TREE = 90848115ac15d0611e87f9bcb6bb9b16f69c6d5a
BLOB = 80a2b6326d0d021a7b7a2ebf9306f7e1853c2fcb
```

```text
FJ899/8 PR #119
HEAD = 3df7b2700ce4fd845e3505398aa24dbb0730e7f7
TREE = f58ceb359259b0d9a630cf5ff90a8235da13e2b6
BLOB = fa974d4a2f6f3e25e428591571000de8e8f2df86
VERDICT = AK-CANON X1B R4R2 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #119 froze:

```text
X1B-R4R2-IBR-F001 local effect Git ref not bound
X1B-R4R2-IBR-F002 ambient Git hooks/filters/signing/config can expand or transform effect
X1B-R4R2-IBR-F003 hardlink aliasing of write targets not excluded
X1B-R4R2-IBR-F004 freshness/supersession policy partly implicit
```

## 4. Review method

This review did not infer PASS from R4R3 being longer, self-contained, or explicitly labelled as correcting all four R4R2 findings.

The adversarial questions included:

```text
Does refs/heads/main mean the same raw Git object graph that the Human-bound SHA identifies?
Can local repository metadata reinterpret that SHA without moving the ref?
Can replace-aware Git verification prove a false exact-two-path result?
Can any local Git config still alter the durable commit object?
Are exact commit headers closed, or only selected fields checked?
Can side/detached refs still become operative?
Can hardlink/symlink aliasing still expand named filesystem scope?
Are activation, age, deactivation, conflict and cross-PR semantics explicit?
Can FinalEffectGateV3 still be followed by an unauthorized local substitution?
```

Two Git semantics were independently reproduced in disposable local temporary repositories only; no ScriptOps repository or canonical screenplay content was mutated:

1. a `refs/replace/<H>` commit replacement changes the default result of `HEAD^{tree}`, `cat-file`, and replace-aware commit comparison for the exact SHA `H`;
2. `i18n.commitEncoding` in repository-local `.git/config` causes `git commit-tree` to write an `encoding` header into the commit object.

These are established Git behaviors and are directly relevant because R4R3 leaves replacement-object semantics enabled and leaves repository-local config active except for an enumerated set of overridden keys.

## 5. R4R2 finding F001 — R4R3 disposition

`ADDRESSED AT BRIEF LEVEL`.

R4R3 now binds:

```text
repository_ref_at_request = refs/heads/main
canonical_ref = refs/heads/main
PresentedMaterialEffectV3.local_git_effect.target_ref = refs/heads/main
FinalEffectGateV3.target_ref = refs/heads/main
```

and requires, at request creation, admission and final gate:

```text
git symbolic-ref -q HEAD == refs/heads/main
HEAD == refs/heads/main == request.repository_head_at_request
```

The final ref mutation is specified as an old-SHA compare-and-swap from exact request base to exact effect commit, with side branch, detached HEAD and ref drift negative tests.

This closes the literal R4R2 F001 branch/detached ambiguity.

## 6. R4R2 finding F003 — R4R3 disposition

`ADDRESSED AT BRIEF LEVEL`.

R4R3 now requires a bounded POSIX-style alias-safe platform, protected parent-directory descriptors, no-follow semantics, `st_dev + st_ino + st_nlink`, `st_nlink == 1`, non-in-place replacement of existing targets, exclusive creation for absent targets, directory fsync, post-write reopen/identity checks and mandatory symlink/hardlink/substitution negatives.

The previously frozen pre-existing-hardlink counterexample is directly excluded by the brief.

## 7. R4R2 finding F004 — R4R3 disposition

`ADDRESSED AT BRIEF LEVEL`.

R4R3 explicitly selects:

```text
NO WALL-CLOCK TTL
AGE ALONE != STALE
```

and freezes activation/deactivation predicates, selected-PR review-state semantics, no chronology-only winner, no implicit cross-PR supersession, coexistence of separately approved same-base PRs, and old-base invalidation after the first successful local `refs/heads/main` advance.

This is an explicit normative choice rather than an implementation inference.

## 8. Finding X1B-R4R3-IBR-F001 — Git replacement refs can substitute the raw Human-bound parent tree

Severity: `BLOCKER`.

R4R3 requires exact SHA equality:

```text
HEAD == refs/heads/main == request.repository_head_at_request
```

and then derives/validates local parent-tree state through ordinary Git object/revision commands such as the normative equivalent of:

```text
git rev-parse HEAD^{tree}
git read-tree <HEAD_tree>
git ls-tree ...
git cat-file / commit inspection
git diff-tree or equivalent changed-set proof
```

R4R3 removes many caller `GIT_*` variables, disables hooks and selected local/global behaviors, but it does not require replacement-object semantics to be disabled and it does not require absence/rejection of `refs/replace/*`.

Git replacement refs are local refs in `refs/replace/`. By default, ordinary Git commands resolve a replaced object name to its replacement object. `git --no-replace-objects ...` or `GIT_NO_REPLACE_OBJECTS=1` disables that behavior, but R4R3 does not freeze either requirement.

Therefore an exact SHA can remain unchanged while its locally observed commit/tree meaning changes.

Concrete counterexample class:

```text
H = exact Human-bound request base commit
T_H = raw tree of H

construct local replacement commit R with tree T_R
where:
  candidate/impact/canonical/decision-log relevant state remains compatible
  one unrelated tracked path P differs from T_H

create:
  refs/replace/H -> R

make real index/worktree match T_R

refs/heads/main remains H
HEAD remains H
symbolic HEAD remains refs/heads/main
```

Under default replace-aware Git semantics:

```text
HEAD^{tree} == T_R
real_index_tree == HEAD^{tree}
```

so the R4R3 clean/index-tree check can pass against the replacement tree.

The effect preparation then starts from `T_R`, changes only:

```text
scenes/<scene_id>.fountain
.scriptops/decision-log.ndjson
```

and creates effect commit `C` with explicit parent header `H`.

A local replace-aware changed-set check can report only those two paths because its view of parent `H` is replacement tree `T_R`.

The same synthetic Git state was reproduced independently with these observations:

```text
replace-aware HEAD^{tree} = replacement tree
raw/no-replace HEAD^{tree} = original H tree

replace-aware changed paths H..C:
  .scriptops/decision-log.ndjson
  scenes/S.fountain

raw/no-replace changed paths H..C:
  .scriptops/decision-log.ndjson
  scenes/S.fountain
  third.txt
```

Thus the raw resulting commit has a third path relative to its actual parent object `H`, while the local verification regime can still report the exact two Human-bound paths.

This violates:

```text
HUMAN-BOUND EFFECT = OPERATIVE EFFECT
EXACT TWO-PATH ONE-PARENT EFFECT
EXECUTOR NO-SUBSTITUTION
FAIL CLOSED ON AMBIGUOUS / SUBSTITUTE GIT OBJECT STATE
```

The replacement ref can also be introduced after preliminary admission without changing `refs/heads/main` itself. A simple ref-SHA CAS does not detect it.

A successor brief must freeze raw-object semantics for every authority-critical Git command, not merely the branch ref name/SHA. A suitable mechanism may be `--no-replace-objects`, `GIT_NO_REPLACE_OBJECTS=1`, explicit rejection/inventory of replacement refs, or an equivalently strong construction, but the exact security contract must prevent replacement-object interpretation from entering request checks, final gate, tree construction, commit inspection, changed-set proof and post-effect verification.

Disposition: `NOT PASS`.

## 9. Finding X1B-R4R3-IBR-F002 — repository-local i18n.commitEncoding can transform the exact commit object

Severity: `BLOCKER`.

R4R3 correctly disables system/global Git config and overrides several command-level keys:

```text
core.hooksPath=/dev/null
core.fsmonitor=false
commit.gpgSign=false
credential.helper=
```

It also removes caller `GIT_CONFIG_*` injections.

However, repository-local `.git/config` remains active for the effect commands except where individual keys are overridden.

Current Git `commit-tree` semantics use repository-local:

```text
i18n.commitEncoding
```

and, when configured for a non-default encoding, add an `encoding <value>` header to the created commit object.

A minimal reproduction with otherwise fixed tree, parent, author, committer, timestamps and message produces a commit object containing, for example:

```text
encoding ISO-8859-1
```

R4R3's deterministic commit section freezes:

```text
tree
one parent
logical message
fixed author identity
fixed committer identity
request_created_at time semantics
```

but it does not explicitly freeze the allowed complete commit-header set, require absence/exact value of an `encoding` header, or override `i18n.commitEncoding`.

The resulting effect commit SHA is deliberately not part of the Human request, so this ambient local-config transformation is not caught by a pre-bound commit SHA.

A literal implementation can therefore satisfy the currently enumerated checks while producing different durable commit objects from the same Human-bound material effect solely because repository-local config differs.

This is directly contrary to the stated R4R3 correction goal:

```text
ambient Git ... configuration ... must not expand or transform the post-FinalEffectGate effect
```

and to the claimed deterministic exact commit-object profile.

A successor brief must either neutralize `i18n.commitEncoding` for `commit-tree` or define and verify a closed exact commit-object/header schema that rejects any ambient header/config transformation. The corresponding local-config regression must be mandatory.

Disposition: `NOT PASS`.

## 10. R4R2 finding F002 — overall R4R3 disposition

`NOT FULLY ADDRESSED` because of X1B-R4R3-IBR-F001 and X1B-R4R3-IBR-F002.

R4R3 substantially fixes the originally identified hook/filter/signing/porcelain mechanisms:

```text
no git add / git commit / checkout / reset for effect
system Git resolution
shell=false
minimal environment
hooks disabled
fsmonitor disabled
signing disabled
credential helper empty
no network Git commands
hash-object --no-filters
update-index --cacheinfo
explicit temporary index
exact tree/path/blob checks
commit-tree
update-ref old-SHA CAS
post-effect verification
```

Those are meaningful corrections.

But the ambient Git object/config interpretation boundary is still not closed because replacement refs and commit-encoding config survive the frozen profile.

## 11. Mandatory adversarial question matrix

### Q1 — exact local effect ref

`PASS AT BRIEF LEVEL`.

`refs/heads/main` is now explicit and CAS-bound; side/detached states are denied.

### Q2 — replacement-object/raw-parent identity

`FAIL`.

The exact parent SHA can be locally reinterpreted through `refs/replace/*` without changing the SHA/ref equality checks.

### Q3 — exact two-path resulting tree

`FAIL` under X1B-R4R3-IBR-F001.

Replace-aware verification can report two paths while the raw commit differs from its actual raw parent at an additional unrelated path.

### Q4 — hook/filter/signing isolation

`PASS AS TO THE EXPLICITLY FROZEN MECHANISMS`.

The plumbing and command-level protections substantially neutralize the original R4R2 hook/filter/signing counterexamples.

### Q5 — complete local Git config determinism

`FAIL` under X1B-R4R3-IBR-F002.

Repository-local `i18n.commitEncoding` can alter the commit object.

### Q6 — hardlink/symlink target aliasing

`PASS AT BRIEF LEVEL`.

Single-link/no-follow/descriptor-relative/atomic-replacement semantics directly address the frozen R4R2 alias finding.

### Q7 — freshness/activity/supersession

`PASS AT BRIEF LEVEL`.

No TTL, explicit deactivation, selected-PR domain, no latest-wins and same-base coexistence semantics are frozen.

### Q8 — request identity circularity

`PASS AT BRIEF LEVEL`.

V3 retains the acyclic binding/digest/request construction introduced in R4R2.

### Q9 — known legacy acceptance bypasses

`PASS AT BRIEF LEVEL`.

Direct legacy approve and direct `scene-promote --to accepted` remain explicitly disabled at multiple layers with real regressions required.

### Q10 — FinalEffectGateV3 no-substitution guarantee

`NOT PASS`.

A replacement ref can alter the local object/tree interpretation after Human evidence is fixed while the Human-bound branch SHA remains unchanged.

### Q11 — deterministic durable commit truth

`NOT PASS`.

Local `i18n.commitEncoding` can change the commit object and its SHA unless additional unstated handling is invented by the implementer.

### Q12 — core authority/security choice left to implementer

`FAIL`.

At minimum the implementation must still choose, without a frozen R4R3 rule:

```text
how replacement refs/objects are disabled or rejected
how raw parent/tree identity is proven independently of replacement semantics
how repository-local commit encoding config is neutralized
whether extra commit headers are forbidden and how that closed schema is verified
```

These are effect-identity and executor-substitution choices, not cosmetic implementation details.

## 12. What R4R3 successfully preserves or improves

This NOT PASS does not erase the substantial R4R3 progress.

At brief level R4R3 preserves or improves:

```text
separate trusted Human decision event
exact Human actor + strict review body
credential-free public GitHub evidence
one-file decision PR
acyclic request identity
complete selected-PR review reconstruction
explicit no-TTL activity policy
explicit deactivation/conflict semantics
no chronology-only supersession
bounded replay claim
same-worktree invocation lock
exact refs/heads/main Human/effect binding
old-SHA ref compare-and-swap
side/detached/ref-drift denials
no porcelain effect commit
hook isolation
filter-safe blob construction
signing disablement
credential-helper disablement
exact temporary-index tree construction
single-link hardlink-safe target replacement
symlink/no-follow protections
rollback / BLOCKED distinction
legacy approve denial
legacy scene-promote accepted denial
historical-vs-active runtime split
real separately authorized Human positive-control requirement
closure/V1 separation
```

These properties are not reopened merely because the residual Git-isolation findings exist.

## 13. Required successor-brief acceptance obligations

This review does not authorize a repair.

A separately Human-authorized successor brief would need to preserve all R4R3 improvements and additionally freeze, at minimum:

```text
A. RAW GIT OBJECT SEMANTICS
   - replacement refs/objects cannot reinterpret request base, HEAD tree,
     commit parents, tree comparison or post-effect verification;
   - every authority-critical Git read/write uses no-replace semantics or an
     equivalently strong raw-object proof;
   - regression injects refs/replace/<request-base> with an unrelated-path
     tree delta and proves DENY / exact raw two-path truth.

B. CLOSED COMMIT CONFIG / HEADER SEMANTICS
   - repository-local i18n.commitEncoding cannot add/change commit headers;
   - deterministic commit object has a closed allowed header set or an
     equivalent exact-object contract;
   - regression sets local i18n.commitEncoding and proves it is rejected or
     neutralized without changing the exact effect commit profile.
```

The exact mechanism remains a future Human-authorized brief decision, not authority granted by this review.

## 14. Final disposition

```text
R4R2 IBR F001 LOCAL EFFECT REF = ADDRESSED IN R4R3
R4R2 IBR F003 HARDLINK / WRITE-TARGET ALIAS = ADDRESSED IN R4R3
R4R2 IBR F004 FRESHNESS / SUPERSESSION = ADDRESSED IN R4R3
R4R2 IBR F002 AMBIENT GIT EXECUTION CONFIG = NOT FULLY ADDRESSED

R4R3 IBR F001 REPLACEMENT-REF / RAW-OBJECT SUBSTITUTION = BLOCKER
R4R3 IBR F002 LOCAL COMMIT-ENCODING CONFIG / EXTRA HEADER = BLOCKER

AK-CANON X1B R4R3 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
IMPLEMENTATION AUTHORITY = NOT ESTABLISHED
X1B = OPEN
V1 AUTHORITY = NOT ESTABLISHED
```

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R3 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R3 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 15. STOP

No ScriptOps implementation, repair, Human decision PR/review, live positive control, canonical effect, merge, closure, V1, release, deployment or tag is authorized by this review artifact.

`STOP`
