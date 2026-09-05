# X1B Human Decision Authorship — Independent AK-CANON R4R7 Implementation-Brief Review

Status: `INDEPENDENT REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: `2026-09-01`

## 1. Verdict

`AK-CANON X1B R4R7 IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

R4R7 materially improves R4R6 and directly addresses both findings frozen in PR #127 at brief level:

1. the main ref is no longer authorized merely by logical Git resolution; R4R7 restricts execution to a normal single-worktree real `.git` directory, direct real `refs/` / `refs/heads/` directories, a direct regular single-link loose `refs/heads/main`, no packed copy of main, retained directory descriptors and an fd-relative no-follow lockfile CAS;
2. `git update-ref` is removed from the commitment path, so Git cannot implicitly create an ambient reflog entry; the main branch reflog is instead represented in `PresentedMaterialEffectV7`, its exact prestate is bound, and its one new line is deterministic from Human-bound inputs plus the uniquely derived effect commit SHA.

The V7 schema migration also correctly prevents V6 Human evidence from silently authorizing the changed V7 material effect.

However, independent adversarial review found two new material blockers outside the now-closed main-ref path:

1. R4R7 physically closes the reference store but not the **primary Git object database**. `COMPLETE_LOCAL_OBJECT_STORE_V1` rejects shallow/promisor/alternate mechanisms, but it does not require `.git/objects` itself, or the loose-object path hierarchy beneath it, to be a real in-repository no-alias directory topology. Git writes new accepted-scene, decision-log, tree and commit objects before ref commitment. A symlinked primary `.git/objects` can redirect those durable writes outside the repository while logical object reads, object IDs, no-lazy checks and the later ref CAS all still succeed;
2. the new manual loose-ref/reflog replacement path does not freeze the exact resulting filesystem metadata. R4R7 requires `refs/heads/main mode = frozen implementation-supported regular-ref mode` and creates `main.lock` with a `frozen supported regular-ref mode`, but no concrete mode or preservation rule is actually specified. The atomic rename replaces the old ref inode with the lock inode. Therefore final ref permissions are an implementation/umask/shared-repository choice, and the same issue applies to the temp-and-rename reflog projection. At minimum mode bits are unbound; on platforms where ACL/xattr/security-label metadata is operative, replacement can also drop or alter that metadata without Human binding.

Either finding independently prevents implementation authority.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R7 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R7 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#128`

```text
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
BASE TREE = df807db7003dfd201e9be4d5927472e515a2e737
HEAD = 6879b3f551a0eff674002509b3c31925ce639ac7
TREE = 0e515d1d121869e3ec2d437e630d67b24b5dc63f
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R7.md
BLOB = 01dbb04f7f238bebc3565f779d074ca3824e74ad
```

Immediately before review write, PR #128 remained:

```text
state = OPEN
merged = false
draft = true
mergeable = true
commits = 1
changed_files = 1
additions = 1581
deletions = 0
```

`FJ899/8 main` also remained exactly:

```text
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

The exact candidate file set was freshly reread and remained exactly one added R4R7 brief file.

## 3. Normative lineage

### 3.1 Accepted corrective design

```text
FJ899/scriptops PR #34
HEAD = d7a5065c87e9a4b49fb608235c908bceac42b4b1
TREE = 3140d0ac95c120a7b1532942bae2e0dad38b4839
PATH = governance/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_CANDIDATE.md
BLOB = dac16f109d1414a2208c2ed9a166ae9e9a329216
```

Higher-level properties remain:

```text
separate trusted Human decision evidence
exact content/scope/candidate/effect binding
executor no-substitution
fail closed on ambiguity
no core authority/security choice left implicit
current activity/conflict/replay semantics
real-boundary negative controls
post-effect truth matching the Human-bound effect
no failed operation durably misreported as successful Human-attributed effect
```

### 3.2 Independent corrective-design review

```text
FJ899/8 PR #109
HEAD = 132d65be48331a822039262b707c47a81d02a64d
TREE = a8bdc363d293beb7b15ae8b787cc3ebdd694fd99
BLOB = 439109e104244552a5ac1f3f08988dba283733d0
VERDICT = AK-CANON X1B CORRECTIVE DESIGN REVIEW R2 = PASS
```

### 3.3 R4R6 predecessor and binding review

```text
FJ899/8 PR #126
HEAD = 8cbe07b7e48379a49fdb6d154ffa56d489a45b5e
TREE = af54604cb1deb19e016a44e96efc5ee290be6d8e
BLOB = 8d9be9d8d2e481f990c90e63ed7de85320317cbb
```

```text
FJ899/8 PR #127
HEAD = d91ff8eb13fe3cf5eb4269320a014c730084aecd
TREE = 14ea92ce702dc0719f19d61355a753d387b06b7a
BLOB = 2a096efe585c0f06fcc8da3bc7b049f357cf7240
VERDICT = AK-CANON X1B R4R6 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #127 froze:

```text
X1B-R4R6-IBR-F001 physical files-ref topology is not bound
X1B-R4R6-IBR-F002 update-ref reflog is an unbound durable effect
```

## 4. Review method

The review attacked the exact R4R7 successor checklist rather than inferring PASS from the stronger physical-ref and reflog language.

The review specifically tested or inspected:

```text
whether real main-ref symlink and refs-parent redirects remain possible
whether packed main can coexist with the authorized loose ref
whether held dirfd + O_NOFOLLOW closes ref-write redirection
whether update-ref or another Git ref-mutating command remains reachable
whether main reflog prestate and exact after-bytes are Human-bound
whether execution-time user/time can enter the reflog
whether physical alias controls stop at refs or cover the primary object database too
whether hash-object/write-tree/commit object writes can escape through .git/objects topology
whether the manual ref lockfile replacement freezes final ref inode metadata
whether umask/core.sharedRepository can affect final permissions
whether reflog temp-and-rename projection freezes final reflog metadata
whether any new core security/effect choice remains left to implementation
```

Current Git documentation and current upstream source were checked for repository object layout and file-mode creation semantics. Disposable local reproductions were used as supporting counterexamples where ordinary filesystem behavior is stable and not dependent on a newer ref backend.

No ScriptOps implementation, Human evidence, canonical screenplay content, ScriptOps local ref, reflog or recovery state was mutated by this review.

## 5. PR #127 finding F001 — physical files-ref topology

Disposition: `ADDRESSED AT BRIEF LEVEL`.

R4R7 now freezes all of the following:

```text
normal single-worktree real .git directory only
Git common dir = .git
real refs directory
real refs/heads directory
direct loose regular single-link refs/heads/main
exact HEAD symbolic-file bytes
packed-refs contains no main
held root/.git/refs/heads descriptors
O_NOFOLLOW leaf operations
main.lock O_EXCL acquisition
old main reread after lock
old main reread immediately before rename
same-directory descriptor-relative rename
refs/heads directory fsync
post-rename physical no-follow reread
canonical hierarchy identity revalidation
```

A logical-only post-check is explicitly insufficient.

This closes the exact PR #127 real-ref-symlink and parent-directory-redirection counterexamples at brief level.

## 6. PR #127 finding F002 — unbound update-ref reflog

Disposition: `ADDRESSED AT BRIEF LEVEL`.

R4R7 removes every Git ref-mutating command from the effect path.

The branch reflog is now a separately described Human-bound effect with:

```text
exact target = logs/refs/heads/main
exact prestate exists/hash/byte-length
exact old OID source = request base
exact new OID source = uniquely derived V7 effect commit
fixed ScriptOps identity
request_created_at-derived epoch
fixed +0000 timezone
fixed message
exact append count = 1
exact prior bytes + exact deterministic line
alias-safe post-ref temp/write/fsync/rename/dir-fsync projection
```

Ambient `user.name`, `user.email`, `GIT_COMMITTER_*`, `GIT_REFLOG_ACTION` and `core.logAllRefUpdates` cannot generate an implicit entry because no Git ref mutation is allowed.

This closes the exact PR #127 ambient `git update-ref` reflog counterexample at brief level.

## 7. Finding X1B-R4R7-IBR-F001 — primary object database physical topology is not bound

Severity: `BLOCKER`.

### 7.1 R4R7 physically closes refs, not objects

R4R7 introduces strong physical identity profiles for:

```text
repository root
.git
.git/refs
.git/refs/heads
.git/refs/heads/main
.git/logs/refs/heads/main
```

But its object-store requirement remains `COMPLETE_LOCAL_OBJECT_STORE_V1`, whose stated purpose is rejecting logical object incompleteness and alternate/promisor topology:

```text
shallow/graft state
partial clone markers
promisor configuration
.promisor pack sidecars
objects/info/alternates
caller alternate/object-directory injection
lazy fetch
```

R4R7 does not state a physical no-alias requirement for:

```text
.git/objects
.git/objects/<fanout>
.git/objects/pack
.git/objects/info
```

and does not retain/open/revalidate a primary object-database directory descriptor analogous to the ref-store descriptors.

### 7.2 Current Git defines the primary object store at `$GIT_DIR/objects`

Current `gitrepository-layout` documentation defines `objects` as the repository object store and loose objects as files below `objects/<two-hex>/<remaining-hex>`.

Current Git object-writing code derives object paths from the repository object-directory path and performs ordinary filesystem creation/rename operations. The frozen R4R7 controls sanitize `GIT_OBJECT_DIRECTORY` and alternates, but they do not change the physical semantics of the default `.git/objects` path itself.

Therefore:

```text
NO ALTERNATE OBJECT STORE
```

does not imply:

```text
PRIMARY OBJECT STORE PHYSICALLY CONTAINED AND NON-ALIASED
```

### 7.3 Concrete counterexample

A disposable repository can be transformed from:

```text
.git/objects = real directory
```

into:

```text
.git/objects -> /outside/object-store
```

while leaving:

```text
.git = real directory
GIT_COMMON_DIR unset
GIT_OBJECT_DIRECTORY unset
GIT_ALTERNATE_OBJECT_DIRECTORIES unset
objects/info/alternates absent
partial/promisor markers absent
```

A supporting reproduction then executed ordinary:

```text
git hash-object -w <blob>
```

and Git returned the expected object ID while the resulting loose object file appeared under the outside target directory.

The same redirection applies to the R4R7 pre-CAS object writes for accepted-scene blob, decision-log blob, newly required tree objects and the exact raw effect commit.

### 7.4 Why R4R7 checks can still pass

With an outside symlinked primary object store, Git still sees those files as its normal object database.

Thus the following can all remain true:

```text
hash-object returns exact independently predicted object ID
cat-file readback is byte-exact
new_object_closure is locally readable
no lazy fetch occurs
no alternate mechanism is configured
object format = sha1
commit/tree/blob identities are exact
main ref is later committed through the safe descriptor-relative CAS
```

Yet durable object writes occurred outside the Human-understood repository metadata topology.

This is the same class of physical-target substitution that R4R7 correctly eliminated for `refs/heads/main`, now one layer earlier in the effect.

### 7.5 Security consequence

The Human-bound effect is presented as a bounded local `FJ899/scriptops` Git effect.

Under this counterexample the implementation can durably mutate an external object directory before commitment while all object IDs remain cryptographically correct.

That violates:

```text
exact material-effect binding
executor no-substitution
bounded repository effect
no hidden durable side effect
physical-target integrity
no core security choice left implicit
```

It also creates a negative-control problem: a later pre-CAS denial can still leave externally redirected loose objects even though no canonical ref was committed.

R4R5/R4R6 already treated unreferenced object writes as permissible preparation only inside the bounded repository object database. Physical redirection changes the affected storage boundary and therefore is material.

### 7.6 Required successor correction class

A successor brief must bind the physical primary object database, not merely reject logical alternates.

At minimum it must freeze a fail-closed profile covering:

```text
.git/objects direct real-directory identity
no symlink/reparse/redirect at primary object root
physical containment under the exact held .git directory
stable st_dev/st_ino identity through object preparation and ref commitment
loose-object fanout creation/write topology
pack/info paths to the extent they are read or written
no object-directory mount/path substitution that can redirect a write
post-write proof that newly created object files belong to the authorized primary object database
```

The successor must add a direct `.git/objects -> outside` regression and prove that no authority-critical object writer can create an external file.

This review does not authorize the correction mechanism.

## 8. Finding X1B-R4R7-IBR-F002 — ref/reflog replacement metadata remains implicit

Severity: `BLOCKER`.

### 8.1 R4R7 replaces the main ref inode

The commitment sequence is:

```text
create refs/heads/main.lock
write new SHA + LF
fsync lock
rename main.lock -> main
fsync refs/heads directory
```

An atomic rename onto an existing file replaces the target directory entry with the source inode. It does not transform the old `main` inode in place.

Therefore the resulting physical `refs/heads/main` metadata comes from the newly created lockfile, not automatically from the old ref file.

### 8.2 The mode is named but not frozen

R4R7 requires before effect:

```text
refs/heads/main owner = current execution user
refs/heads/main mode = frozen implementation-supported regular-ref mode
```

and lock acquisition specifies:

```text
O_WRONLY | O_CREAT | O_EXCL | O_NOFOLLOW | O_CLOEXEC
with a frozen supported regular-ref mode
```

But the brief never states the actual numeric mode, an exact prestate-to-poststate preservation rule, or an exact post-open `fchmod` rule.

The phrase:

```text
frozen implementation-supported regular-ref mode
```

is therefore a placeholder for an implementation decision, not a frozen value.

That conflicts directly with R4R7's own higher-level requirement:

```text
no core authority/security choice left implicit
```

### 8.3 Ambient process/repository policy can affect creation mode

POSIX `open(..., O_CREAT, mode)` is subject to the process umask.

Git's own current tempfile documentation likewise states that requested mode can be further modified by umask and possibly `core.sharedRepository`.

R4R7's ref CAS is not using Git's tempfile helper, so `core.sharedRepository` does not automatically normalize the OS-created lockfile for it. Conversely, unless the implementation explicitly freezes and applies a concrete mode after creation, caller/process umask can change the new inode mode.

Two executions with identical V7 Human evidence, identical old ref bytes and identical effect commit can therefore produce different final ref permissions.

### 8.4 Reflog projection has the same replacement issue

R4R7 projects the main reflog by writing exact complete after-bytes to a fresh temporary inode and atomically renaming it onto `logs/refs/heads/main`.

The brief binds reflog bytes but not exact final filesystem metadata.

So an existing reflog can have exact Human-bound bytes but, after a successful V7 projection, receive different permissions from the newly created temporary inode.

The same concern extends, where the platform exposes them, to metadata carried by the replaced inode rather than file contents, such as:

```text
POSIX ACLs
extended attributes
security labels
file flags
```

The brief does not require these to be absent, bound, preserved, rejected or reproduced.

The blocker does not depend on those optional features: unspecified POSIX mode alone is sufficient.

### 8.5 Human-presented effect is incomplete

`PresentedMaterialEffectV7` binds ref and reflog content semantics but does not bind a concrete final ref/reflog mode or metadata transition.

Thus Human approval does not determine whether the effect leaves, for example:

```text
main mode 0644
main mode 0600
main mode 0660
```

where those modes are permitted by ambient umask/implementation policy.

Permissions on Git reference metadata are security-relevant because they determine which local principals can read or modify repository control state.

This is a durable material effect, not an in-memory implementation detail.

### 8.6 Required successor correction class

A successor brief must make the physical metadata transition exact.

It must choose and review one closed policy, for example:

```text
bind exact allowed prestate mode and require exact same mode after replacement
```

or:

```text
bind one exact V8 poststate mode and explicitly authorize the mode transition
```

with an implementation mechanism that is independent of ambient umask.

It must also freeze treatment of security-relevant inode metadata that exists on the bounded platform:

```text
reject unsupported ACL/xattr/security-label state
OR
bind and preserve it exactly
OR
explicitly Human-bind its deterministic replacement
```

The same policy must cover both:

```text
refs/heads/main
logs/refs/heads/main
```

and any other temp-and-rename Git metadata target introduced by the successor.

Mandatory regressions must include multiple umask values and an existing ref/reflog with a deliberately different valid mode, proving deterministic outcome or fail-closed rejection.

This review does not authorize the correction mechanism.

## 9. Supporting Git behavior checked

The review checked current Git behavior relevant to these findings:

### 9.1 Object store layout

Current `gitrepository-layout` states that the repository object store is `$GIT_DIR/objects`, and loose objects are stored in fanout directories beneath it.

This confirms that R4R7's Git object writers operate against the physical primary object path that is currently not covered by its fd-relative no-alias profile.

### 9.2 Git object writer path

Current upstream `object-file.c` constructs loose-object paths from the repository object directory and performs ordinary file creation/rename behavior. R4R7 does not introduce an OS-level no-follow wrapper around those Git object writes.

### 9.3 Tempfile permissions

Current upstream `tempfile.h` explicitly documents that a requested file mode may be modified by umask and `core.sharedRepository`.

Current `git-init` documentation likewise describes repository file creation permissions as dependent on `core.sharedRepository` and/or umask.

These sources reinforce that file mode is an actual repository policy input and cannot be left as an unnamed "supported mode" while claiming an exact physical effect.

## 10. R4R7 properties preserved by this review

No finding was established against the following R4R7 corrections at brief level:

```text
V7 schema/review-marker freshness
one-file Human decision request envelope
trusted public GitHub evidence route
current review-set conflict semantics
no-replace raw-object authority
no-lazy-fetch local-only object reads
partial/promisor/alternate rejection
configured-hook census and event disables
closed raw effect commit bytes
CAS-first no-canonical-worktree-before-ref ordering
real .git / real refs / real heads restriction
direct loose single-link main restriction
packed-main rejection
held refs/heads descriptor discipline
main.lock O_EXCL/O_NOFOLLOW old-value CAS
lock fsync + rename + refs/heads directory fsync
explicit ref durability/topology uncertainty states
removal of Git ref mutation from the effect path
Human-bound deterministic main branch reflog bytes
post-ref recovery-required semantics
alias-safe canonical scene/decision-log writes
no silent history rollback after possible commitment
```

These dispositions remain bounded to the implementation-brief review. They are not an implementation proof.

## 11. Frozen successor obligations

Any successor implementation brief must preserve every accepted R4R7 property and close both new blockers without reopening prior findings.

### Obligation A — physical primary object-store closure

Freeze a physical object database profile that proves authority-critical object writes cannot escape or alias outside the authorized Git metadata store.

At minimum:

```text
primary objects directory exact and real
physical containment exact
no symlink/reparse/redirect root
stable descriptor identity
no alternate/promisor/lazy-fetch regression
new-object physical location proof
external-object-directory sentinel regression
```

### Obligation B — exact ref/reflog metadata transition

Freeze exact mode and security-metadata semantics for every manually replaced Git metadata file.

At minimum:

```text
exact numeric mode policy
ambient umask cannot alter outcome
prestate/poststate mode relation explicit
ref and reflog both covered
ACL/xattr/security-label treatment explicit where supported
post-effect metadata verification
multiple-umask regression
```

### Obligation C — preserve all prior corrections

Do not reopen:

```text
configured hooks
Git fsync object hardening
lazy fetch / partial/promisor closure
replacement refs
raw commit header closure
physical main-ref alias closure
packed-main closure
implicit update-ref reflog
pre-CAS canonical filesystem mutation
false no-effect after a visible commitment
Human evidence freshness/binding
```

## 12. Successor review attack obligations

A successor AK-CANON review must explicitly attack at least:

```text
Can .git/objects be a symlink while all logical object checks pass?
Can an object fanout directory be redirected after object-root validation?
Can a newly written object land outside the held primary object DB?
Can object-root topology change after FinalEffectGate but before hash-object/write-tree/commit write?
Does no-lazy/no-alternate logic accidentally get treated as physical containment?
Can umask change main.lock final mode?
Can core.sharedRepository or process policy create divergent manual-ref permissions?
Does rename replace rather than preserve target inode metadata?
Can main reflog mode change even when bytes are exact?
Are ACL/xattr/security labels either rejected or deterministically handled?
Can V7 evidence authorize any successor material-effect change without a version bump?
Can prior ref symlink/reflog/hook/fsync findings reappear?
```

Any credible counterexample freezes a finding and returns `NOT PASS`.

## 13. Non-authority

This review authorizes no:

```text
successor brief repair
ScriptOps source mutation
Human decision PR
Human review
positive control
canonical screenplay effect
decision-log effect
refs/heads/main effect
reflog effect
recovery
merge
X1B closure
V1 entry
release
deployment
tag
```

Preserve:

```text
R4R7 IBR F001 PRIMARY OBJECT-STORE PHYSICAL ALIAS = BLOCKER
R4R7 IBR F002 REF/REFLOG METADATA MODE = BLOCKER

AK-CANON X1B R4R7 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
IMPLEMENTATION AUTHORITY = NOT ESTABLISHED
X1B = OPEN
V1 AUTHORITY = NOT ESTABLISHED
```

## 14. STOP

The next legal stage is a separately Human-authorized successor corrective implementation brief that closes exactly the frozen R4R7 findings while preserving all prior corrections.

```text
REVIEW COMPLETE
REPAIR NOT AUTHORIZED
IMPLEMENTATION NOT AUTHORIZED
CANONICAL EFFECT NOT AUTHORIZED
STOP
```
