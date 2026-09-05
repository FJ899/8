# X1B Human Decision Authorship — Independent AK-CANON R4R8 Implementation-Brief Review

Status: `INDEPENDENT REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: `2026-09-02`

## 1. Verdict

`AK-CANON X1B R4R8 IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

R4R8 materially improves R4R7 and addresses both findings frozen in PR #129 at brief level:

1. the primary object database is no longer trusted through logical Git resolution alone; R4R8 requires a real contained `.git/objects` hierarchy, held descriptors, mount containment, no alternates/promisor escape, raw in-memory object derivation and descriptor-relative loose-object installation;
2. ref/reflog and other authority-critical filesystem modes are no longer left as an unspecified implementation choice; R4R8 assigns numeric modes, exact uid/gid, fixed umask, rejects non-mode ACL/xattr metadata and neutralizes `core.sharedRepository`.

The V8 schema migration also correctly prevents V7 Human evidence from authorizing the changed V8 material effect.

However, independent adversarial review found two new blockers:

1. R4R8 changes final mode metadata **after** the only file `fsync()` that it requires. The object installer, main-ref CAS and reflog projection all use `write -> fsync(file) -> fchmod(final-mode) -> install/rename -> fsync(directory)` without a second file `fsync()` after `fchmod`. Linux `fsync(2)` flushes file metadata that is dirty at the time of the call; a later `fchmod` dirties inode metadata again. Directory `fsync` makes the namespace entry durable but does not retroactively flush the file's later mode change. R4R8 therefore does not prove its exact `0444`/`0644` metadata across crash/reboot while claiming `CRASH_DURABLE_OBJECT_AND_ALIAS_SAFE_REF_V3`;
2. R4R8 still delegates the real-index projection to Git after ref commitment, but does not reject or Human-bind **split index**. A valid prestate can have an ordinary `.git/index` that references `$GIT_DIR/sharedindex.<SHA-1>`. Git split-index semantics may write a new shared index, rename it into place, delete expired shared indexes, and freshen shared-index mtimes. Those durable files and metadata are outside `PresentedMaterialEffectV8`, outside the physical-prestate record, and outside the final path list. The same index mode can also produce pre-ref shared-index mtime mutation merely while the index is read.

Either finding independently prevents implementation authority.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R8 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R8 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#130`

```text
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
BASE TREE = df807db7003dfd201e9be4d5927472e515a2e737
HEAD = 6427f07347fedfcf8c2b719e16b67c37b2a7e296
TREE = ac93196b3d04e2b607c6aeeadd3485dc6c32dd6f
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R8.md
BLOB = 87c9bb4f57a33ea0d7c3b41c8305b04e8f9283f2
```

Immediately before review write, PR #130 remained:

```text
state = OPEN
merged = false
draft = true
mergeable = true
commits = 1
changed_files = 1
additions = 1879
deletions = 0
```

`FJ899/8 main` also remained exactly:

```text
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

The exact candidate file was freshly reread from the reviewed HEAD.

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

### 3.3 R4R7 predecessor and binding review

```text
FJ899/8 PR #128
HEAD = 6879b3f551a0eff674002509b3c31925ce639ac7
TREE = 0e515d1d121869e3ec2d437e630d67b24b5dc63f
BLOB = 01dbb04f7f238bebc3565f779d074ca3824e74ad
```

```text
FJ899/8 PR #129
HEAD = 7ac626a9ab0b01eb07cf5ece1f444f3b0e23cb14
TREE = 714f48826e36634190fd275506ee5d29e6176dfd
BLOB = 5af7e4cb6310666f544f8556c5242d4e0f8ec9d4
VERDICT = AK-CANON X1B R4R7 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #129 froze:

```text
X1B-R4R7-IBR-F001 primary object database physical topology is not bound
X1B-R4R7-IBR-F002 ref/reflog replacement metadata remains implicit
```

## 4. Review method and current external semantics checked

The review attacked the exact R4R8 successor checklist and its new Linux/POSIX durability claim rather than inferring PASS from stronger object-store and metadata language.

The review inspected at least:

```text
physical .git/objects containment
fanout creation and held-dirfd discipline
existing-object and EEXIST behavior
new loose-object temp/write/fchmod/link/fsync ordering
main.lock write/fchmod/rename/fsync ordering
reflog temp/write/fchmod/rename/fsync ordering
post-ref real-index mutation surface
split-index/shared-index semantics
whether exact modes are merely visible or crash-durable
whether any persistent Git metadata exists outside the V8 Human-bound effect
```

Current Linux man-pages semantics checked:

```text
fsync(fd) flushes modified file data and associated file metadata
fsync(file) does not itself guarantee durability of the containing directory entry
directory durability therefore requires an explicit directory fsync
```

The important ordering consequence is equally direct:

```text
fsync(file)
then fchmod(file)
```

does not make the later `fchmod` retroactively part of the already completed `fsync`.

Current Git split-index semantics checked:

```text
split index uses $GIT_DIR/index plus $GIT_DIR/sharedindex.<SHA-1>
new shared-index files may be written
old shared-index files may be deleted by expiry policy
shared-index mtime is refreshed when split-index state is created/read
```

Current Git source also states that when split index is in use, index writing writes the shared index to a temporary file, adjusts permissions and renames it into place before writing the split index to the normal index lockfile.

The Git update-index documentation records no semantic change for this split-index behavior through Git 2.55.0.

No ScriptOps implementation, Human evidence, canonical screenplay content, ScriptOps local ref, object store, reflog or recovery state was mutated by this review.

## 5. PR #129 finding F001 — primary object database physical topology

Disposition: `ADDRESSED AT BRIEF LEVEL`.

R4R8 now requires:

```text
real single-worktree .git
real .git/objects
held .git/objects descriptor
same reviewed mount as .git
no nested/bind mount under objects
no GIT_OBJECT_DIRECTORY
no alternates
no promisor/lazy-fetch escape
real contained fanout directories
no-follow leaf operations
no-replace object installation
exact object inflate/type/payload/OID verification
physical contained loose copy for every new_object_closure member
```

It also removes Git primary-object-writing commands from the bounded effect path.

This closes the exact PR #129 `.git/objects -> outside` write-redirection counterexample at brief level.

## 6. PR #129 finding F002 — implicit replacement metadata

Disposition: `ADDRESSED AT BRIEF LEVEL` as to **selection of metadata values**.

R4R8 now explicitly chooses:

```text
refs/heads/main = 0644
logs/refs/heads/main = 0644
.git/index = 0644
canonical scene filesystem target = 0644
decision log filesystem target = 0644
new loose-object final file = 0444
critical directories = 0755
temporary files = 0600
execution umask = 0077
exact execution uid/gid
no xattrs
mode-only ACL
core.sharedRepository rejected and forced false for Git commands
```

Thus R4R7's undefined `frozen supported mode` is no longer present.

The new blocker below is different: the selected metadata values are explicit, but their **crash durability is not correctly ordered**.

## 7. Finding X1B-R4R8-IBR-F001 — final mode metadata is changed after the file fsync

Severity: `BLOCKER`.

### 7.1 Loose-object sequence

R4R8 section 23 requires for a newly installed object:

```text
write complete compressed object
fsync(temp_fd)
re-read and verify
fchmod(temp_fd, 0444)
link temp inode to final OID name
fsync fanout directory
unlink temp name
fsync fanout directory
```

There is no second `fsync(temp_fd)` after `fchmod(0444)`.

The durability profile repeats the same order:

```text
temp file full write
file fsync
exact content reread
explicit final mode 0444
final-name creation
directory fsync
```

### 7.2 Main-ref sequence

R4R8 section 27 and the exact effect sequence require:

```text
write effect SHA to main.lock
fsync(main.lock fd)
fchmod(main.lock fd, 0644)
verify metadata
rename main.lock -> main
fsync refs/heads directory
```

There is no second file fsync after the `0644` mode change.

### 7.3 Reflog sequence

R4R8 section 28 says the reflog projection temp is:

```text
fully written
fsynced
then fchmod(0644)
metadata verified
then renamed
then parent-directory fsynced
```

Again, the final mode change occurs after the only file fsync.

### 7.4 Linux durability consequence

On the bounded Linux profile, `fsync()` flushes file data and file metadata that are pending at that call.

`fchmod()` after that call changes inode metadata and dirties it again.

`fsync(parent_directory)` is necessary for the directory entry, but it is not a substitute for synchronizing a later modification of the file inode itself.

Therefore a crash window exists after the final-name operation in which:

```text
object/ref/reflog content may be durable
final directory entry may be durable
but the requested 0444/0644 inode mode is not proven durable
```

A filesystem may persist it incidentally, but R4R8 claims a bounded crash-durability proof and cannot rely on incidental journaling behavior that the profile did not bind.

### 7.5 Why visible post-check is insufficient

R4R8 verifies the final mode before zero exit.

That proves the current in-memory/on-disk namespace view, not that the post-`fsync` chmod metadata has reached the durability state claimed for crash/reboot survival.

Thus:

```text
VISIBLE MODE = 0644/0444
```

is not equivalent to:

```text
MODE CHANGE INCLUDED IN COMPLETED FSYNC BARRIER
```

### 7.6 Real-index extension of the same issue

R4R8 also allows Git to write `.git/index` after ref commitment and then says index metadata is restored/verified to `0644` before complete success.

If that restoration is a post-write `chmod/fchmod`, the brief likewise does not require an explicit file fsync after the restoration.

The exact correction must cover every post-write metadata change, not only the three explicit temp-file paths.

### 7.7 Violated properties

The gap violates:

```text
CRASH_DURABLE_OBJECT_AND_ALIAS_SAFE_REF_V3
exact metadata effect binding
post-effect truth across the stated crash boundary
no false complete-success claim
no core durability choice left to filesystem accident
```

### 7.8 Required successor correction class

A successor must freeze exact write/metadata/durability ordering.

At minimum, for an inode whose final security metadata is part of the effect:

```text
write exact contents
apply every final inode metadata change
verify metadata
fsync(file fd) AFTER the final metadata change
install/link/rename final name
fsync(containing directory)
reopen and verify
```

If any metadata is modified again after installation, another appropriate file fsync must occur before complete durable success.

Mandatory fault regressions must include crashes immediately:

```text
after fchmod before second file fsync
after second file fsync before link/rename
after link/rename before directory fsync
after directory fsync
```

for object, main ref and reflog, plus the real-index metadata-restoration path.

This review does not authorize the repair mechanism.

## 8. Finding X1B-R4R8-IBR-F002 — split-index/sharedindex durable effects are not bound

Severity: `BLOCKER`.

### 8.1 R4R8 binds only the ordinary index path

R4R8 Human-binds and physically records:

```text
.git/index
```

and requires it to be a regular, single-link, mode-0644 file with exact uid/gid and metadata profile.

But R4R8 does not state any rejection or binding for:

```text
split-index LINK extension
core.splitIndex
splitIndex.maxPercentChange
splitIndex.sharedIndexExpire
.git/sharedindex.<SHA-1>
```

A split index can therefore satisfy the stated `.git/index` file-type/mode/tree checks.

### 8.2 Current Git split-index is multi-file state

Current Git documents split-index mode as:

```text
$GIT_DIR/index
+
$GIT_DIR/sharedindex.<SHA-1>
```

The ordinary index contains a `link` extension naming the shared index OID.

Changes are accumulated in the split index, and Git can push changes into a newly written shared-index file when the configured threshold is reached.

Git also documents that old shared-index files can be deleted according to `splitIndex.sharedIndexExpire` and that a shared index's modification time is updated to keep in-use files from expiry.

Current Git source further states that `write_locked_index()` in split-index mode writes the shared index to a temporary file, adjusts its permissions, renames it into place, and then writes the split index to the ordinary index lockfile.

### 8.3 Concrete admissible prestate

A repository can have:

```text
.git/index = regular single-link 0644 exact uid/gid
index semantic tree = raw request-base tree
index contains split-index link extension
.git/sharedindex.<OID> = valid shared index
```

Nothing in R4R8's FinalEffectGateV8 explicitly rejects that state.

### 8.4 Pre-ref hidden write surface

R4R8 repeatedly reads/proves the real index before ref commitment.

Git's documented split-index behavior may freshen the shared-index mtime when the split index/shared index is read or newly based on it.

Therefore an operation described by the brief as an index read/proof can produce durable metadata mutation at:

```text
.git/sharedindex.<OID>
```

before ref commitment.

That path is not in `PresentedMaterialEffectV8` and is not covered by the object-preparation outcome classes.

### 8.5 Post-ref expansion of the effect

After durable ref commitment, R4R8 delegates real-index projection to Git.

Under split-index semantics, that write can additionally:

```text
create a new .git/sharedindex.<OID>
rename a shared-index tempfile into place
change shared-index permissions/mtime
remove expired old sharedindex files
change .git/index link-extension state
```

R4R8 zero-exit verification checks the semantic index tree and `.git/index` metadata, but it does not Human-bind or verify the complete `sharedindex.*` before/after set.

Complete success can therefore include durable Git metadata that the Human never approved.

### 8.6 Why `core.sharedRepository=false` does not close this

R4R8 correctly neutralizes shared-repository permission widening.

That does not disable split index and does not remove the extra shared-index files from Git's index implementation.

Likewise `core.fsmonitor=false` addresses fsmonitor, not split-index storage.

### 8.7 Violated properties

The gap violates:

```text
exact material-effect binding
no hidden durable Git metadata effect
executor no-expansion/no-substitution
post-effect truth
no core effect choice left implicit
```

### 8.8 Required successor correction class

A successor must explicitly close the index representation, not only the semantic index tree.

One acceptable correction class would require before any authority read/write:

```text
full non-split index only
no split-index link extension
git rev-parse --shared-index-path = empty
no active shared-index dependency
core.splitIndex absent/false under exact effective-config census
splitIndex.* policy either rejected or proven inert
no unbound .git/sharedindex.* create/delete/freshen effect
```

and every index-writing command must be command-scope constrained so it cannot re-enable split-index behavior.

Alternatively, if split index is to remain supported, its complete shared-index file set, mtimes/metadata, creation/deletion policy and post-effect bytes must be Human-bound and verified.

The successor review should also inspect other index representations/extensions so the correction does not merely move the hidden-write boundary again.

This review does not authorize a repair mechanism.

## 9. R4R8 properties that remain materially stronger than R4R7

The two new blockers do not undo the following improvements:

```text
physical primary object store containment
no Git primary-object writer in effect preparation
raw blob/tree/commit derivation in memory
no-follow/no-replace loose-object install
mount-bound object/ref/log hierarchy
explicit unreferenced-object preparation outcomes
numeric ref/reflog/object/worktree modes
fixed umask
exact uid/gid
no xattrs / mode-only ACL profile
core.sharedRepository closure
V8-only Human decision marker
physical main-ref CAS
explicit deterministic Human-bound main reflog
```

Those properties should be preserved by any successor.

## 10. Mandatory successor regression additions

In addition to all R4R8 suites, a successor must add at least:

### Durability ordering

```text
object fchmod then crash before post-chmod fsync
object post-chmod fsync then crash before link
main.lock fchmod then crash before post-chmod fsync
main ref rename after durable post-chmod fsync then crash before directory fsync
reflog fchmod then crash before post-chmod fsync
real-index chmod/restoration then crash before index fsync
```

Expected:

```text
no complete durable claim before the post-metadata file fsync barrier
```

### Split-index boundary

```text
valid split index with sharedindex dependency
core.splitIndex=true
splitIndex.maxPercentChange forcing new shared index
expired old sharedindex eligible for deletion
pre-ref read that freshens sharedindex mtime
post-ref index projection that would write new sharedindex
sharedindex symlink/hardlink/outside-mount alias if split index is encountered
```

Expected:

```text
split-index state is blocked before Human effect
OR
its complete material effect is explicitly Human-bound by a separately reviewed profile
```

## 11. Review disposition

```text
R4R7 IBR F001 PRIMARY OBJECT DATABASE PHYSICAL TOPOLOGY = ADDRESSED IN R4R8
R4R7 IBR F002 IMPLICIT REF/REFLOG REPLACEMENT METADATA = ADDRESSED IN R4R8 AS TO VALUE SELECTION

R4R8 IBR F001 POST-FSYNC FCHMOD / METADATA DURABILITY = BLOCKER
R4R8 IBR F002 SPLIT-INDEX / SHAREDINDEX UNBOUND DURABLE EFFECT = BLOCKER

AK-CANON X1B R4R8 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
IMPLEMENTATION AUTHORITY = NOT ESTABLISHED
X1B = OPEN
V1 AUTHORITY = NOT ESTABLISHED
```

## 12. Non-authority

This review authorizes no:

```text
successor corrective brief
ScriptOps source mutation
Human decision PR creation
Human review creation
positive control
canonical screenplay mutation
decision-log mutation
object-store mutation
refs/heads/main effect
reflog effect
recovery operation
merge
X1B closure
V1 entry
release
deployment
tag
```

`REVIEW FINDING != REPAIR AUTHORITY`.

## 13. STOP

R4R8 is not implementation authority.

Required next stage, only under fresh separate Human authorization:

```text
SUCCESSOR CORRECTIVE X1B IMPLEMENTATION BRIEF
```

The successor must at minimum close:

```text
X1B-R4R8-IBR-F001 post-fsync fchmod / metadata durability
X1B-R4R8-IBR-F002 split-index / sharedindex unbound durable effect
```

Preserve:

```text
R4R8 REVIEW NOT PASS != REPAIR AUTHORITY
R4R8 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
STOP
```
