# X1B Human Decision Authorship — Independent AK-CANON R4R10 Implementation-Brief Review

Status: `INDEPENDENT REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: `2026-09-02`

## 1. Verdict

`AK-CANON X1B R4R10 IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

R4R10 materially improves R4R9 and addresses both findings frozen in PR #133 at brief level:

1. the filesystem authority profile is now narrowed to Linux/ext4 and explicitly gates casefold plus Linux inode semantic flags through `FS_IOC_GETFLAGS`, `FS_IOC_FSGETXATTR`, `statx`, mode/uid/gid, xattr and ACL proof;
2. nonfinal object/fanout preparation is moved out of canonical `.git/objects/<xx>` names into one request-bound staging namespace, and clean preparation requires durable staging-root removal before ref commitment.

The V10 schema migration also correctly prevents V9 or earlier Human evidence from authorizing the changed V10 preparation/effect surface.

However, independent adversarial review found two new blockers:

1. R4R10 binds visible uid/gid and a mount ID, but it does not bind or reject Linux user-namespace and mount ID-mapping semantics. An ext4 idmapped mount, or a caller in a nonidentity user namespace, can satisfy the current ext4/type/inode-flag/mode/uid/gid checks while the kernel translates ownership, ACL and permission semantics. Current `/proc/self/mountinfo` does not expose the mount uid/gid mapping, while current `statmount(2)` has dedicated mount uidmap/gidmap fields. Therefore the V10 physical ownership/security proof is not closed;
2. R4R10 does not bind or deterministically set loose-object `mtime`. A newly created loose object therefore durably inherits ambient execution wall-clock time. Git 2.55 explicitly treats loose-object mtime as pruning state: its object writer freshens stale mtimes because stale objects may be pruned, and `git prune` compares `st_mtime` with the expiry threshold. This is especially material for V10's intentionally persistent pre-ref failed-preparation objects, which remain unreachable and whose retention under Git maintenance depends on that unbound timestamp.

Either finding independently prevents implementation authority.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R10 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R10 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#134`

```text
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
BASE TREE = df807db7003dfd201e9be4d5927472e515a2e737
HEAD = b2824d95e15ae5de782eeb5d59ffc784b1a116b1
TREE = d9c9003746f3ccafb97157e6e37ce12395d12709
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R10.md
BLOB = f3a7e5b5c163de995078d96682c822e5ec15567c
```

Immediately before review write, PR #134 remained:

```text
state = OPEN
merged = false
draft = true
mergeable = true
commits = 1
changed_files = 1
additions = 2173
deletions = 0
```

`FJ899/8 main` also remained exactly:

```text
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

The exact R4R10 file was freshly reread from the reviewed HEAD.

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

### 3.3 R4R9 predecessor and binding review

```text
FJ899/8 PR #132
HEAD = 5a05f995b296cd550e853211739be926626ee607
TREE = 68888b64ca9fa122d133279b92aa8779f4c31e67
BLOB = ee61ca5d540120861f4cc9f5731242cb86554c01
```

```text
FJ899/8 PR #133
HEAD = ae8d7841c0f6bbc9caebe07cd6afe56b17f453ba
TREE = 3eb96ee09f6a74a3f731893b7e874292205f2983
BLOB = 855895be58e8b3d0eff569a1b5a37f0bc7904304
VERDICT = AK-CANON X1B R4R9 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #133 froze:

```text
X1B-R4R9-IBR-F001 Linux inode semantic flags / casefold namespace are not bound
X1B-R4R9-IBR-F002 pre-ref object-store crash residue is not closed
```

## 4. Review method and current semantics checked

The review attacked the exact R4R10 successor rather than inferring PASS from its stronger filesystem and staging profiles.

The review inspected at least:

```text
Linux/ext4 filesystem narrowing
FS_IOC_GETFLAGS allowed-bit policy
FS_IOC_FSGETXATTR policy
statx attribute-mask policy
casefold negative proof
mount namespace and mount-ID binding
Linux user and mount ID mappings
request-bound object staging root
cross-directory RENAME_NOREPLACE ordering
source/destination directory fsync barriers
staging-root cleanup and crash residue classes
loose-object physical metadata
Git 2.55 loose-object freshness/pruning semantics
V10 Human/request/effect schema migration
```

Current external semantics checked included the sources below.

### 4.1 Linux idmappings

Kernel documentation explains that filesystem ownership and permission processing can involve multiple mappings and that idmapped mounts expose the same dentries with translated ownership semantics.

Source checked:

```text
https://docs.kernel.org/filesystems/idmappings.html
https://cdn.kernel.org/doc/html/latest/filesystems/idmappings.html
```

The documentation distinguishes userspace IDs, kernel IDs and mount/VFS IDs and explains that idmapped mounts translate ownership for VFS operations.

### 4.2 ID-mapped mounts and ext4

Current `mount_setattr(2)` documentation defines:

```text
MOUNT_ATTR_IDMAP
```

and states that the mapping from the supplied user namespace is attached to the mount.

It also lists ext4 as supporting idmapped mounts.

Source checked:

```text
https://man7.org/linux/man-pages/man2/mount_setattr.2.html
```

### 4.3 `/proc/self/mountinfo` does not close the mapping proof

Current `proc_pid_mountinfo(5)` documents mount ID, parent ID, root, mount point, mount options, filesystem type, source and superblock options.

Its currently documented optional fields cover mount propagation state such as:

```text
shared
master
propagate_from
unbindable
```

They do not expose the mount uid/gid ID mapping used by `MOUNT_ATTR_IDMAP`.

Source checked:

```text
https://man7.org/linux/man-pages/man5/proc_pid_mountinfo.5.html
```

Thus R4R10's current `mountinfo + mount ID + ext4` proof is insufficient to establish identity ownership semantics.

### 4.4 Current explicit mount-map query surface

Current `statmount(2)` documents dedicated fields and masks for mount mappings, including:

```text
STATMOUNT_MNT_UIDMAP
STATMOUNT_MNT_GIDMAP
mnt_uidmap_num
mnt_uidmap
mnt_gidmap_num
mnt_gidmap
```

Source checked:

```text
https://man7.org/linux/man-pages/man2/statmount.2.html
```

The current R4R10 brief does not require this or an equivalent proof, nor does it fail closed on inability to establish that the reviewed mount uses an identity mapping.

### 4.5 Git 2.55 loose-object freshness semantics

Exact Git `v2.55.0` source was checked.

`object-file.c` contains `freshen_file()` using `utime()` and explicitly states that an object with stale mtime may be subject to pruning.

Source checked:

```text
https://github.com/git/git/blob/v2.55.0/object-file.c
```

Exact Git `v2.55.0` `builtin/prune.c` checks loose-object `st_mtime` against the expiry timestamp before removal.

Source checked:

```text
https://github.com/git/git/blob/v2.55.0/builtin/prune.c
```

The public `git-prune` documentation likewise states:

```text
--expire <time> = only expire loose objects older than <time>
```

and notes no relevant documentation change through Git 2.55.0.

Source checked:

```text
https://git-scm.com/docs/git-prune
```

## 5. PR #133 finding F001 — inode flags / casefold

Disposition: `ADDRESSED AT BRIEF LEVEL` for the exact casefold/inode-flag mechanism frozen in PR #133.

R4R10 now requires:

```text
OS = Linux
filesystem = ext4
one reviewed mount
FS_CASEFOLD_FL = 0 on every authority lookup directory
FS_ENCRYPT_FL = 0
FS_IMMUTABLE_FL = 0
FS_APPEND_FL = 0
FS_DIRSYNC_FL = 0
FS_SYNC_FL = 0
FS_NOCOW_FL = 0
FS_DAX_FL = 0
FS_VERITY_FL = 0
FS_PROJINHERIT_FL = 0
unknown inode flags = BLOCK
FS_IOC_FSGETXATTR exact zero semantic state
required statx semantic attributes supported and absent
```

This addresses the concrete V9 casefold-alias counterexample under ordinary identity ownership semantics.

The blocker below is different: R4R10 proves inode flags but still does not prove the identity mapping under which inode ownership, ACL and permission semantics are observed and applied.

## 6. PR #133 finding F002 — pre-ref canonical ODB residue

Disposition: `ADDRESSED AT BRIEF LEVEL` for the exact V9 nonfinal-canonical-name mechanism.

R4R10 now uses one exact request-derived staging root:

```text
.git/.x1b-stage-v10-<request_digest>
```

and keeps nonfinal fanout/object states there.

A new canonical fanout is exposed only after its final mode/security state and directory fsync.

A new canonical loose object is exposed only after exact content verification, final mode/security state and file fsync.

Cross-directory rename is followed by source and destination parent-directory fsyncs.

Clean preparation requires an empty staging root, root fsync, `rmdir`, `.git` fsync and a zero-staging census before ref commitment.

Stale, malformed or unknown staging residue blocks new effects and has a separate recovery boundary.

The second blocker below is not the old V9 residue bug. It concerns an authority-relevant metadata field of the final canonical loose objects themselves.

## 7. Finding X1B-R4R10-IBR-F001 — Linux user/mount ID mapping is unbound

Severity: `BLOCKER`.

### 7.1 Current V10 proof

R4R10 records and checks fields such as:

```text
execution uid/gid
inode uid/gid
mount ID
filesystem type ext4
mode
xattrs
ACL
FS_IOC_GETFLAGS
FS_IOC_FSGETXATTR
statx attributes
```

It also records `/proc/self/ns/mnt` and mountinfo identity.

It does not bind or reject:

```text
/proc/self/ns/user identity
caller uid_map/gid_map
mount uid mapping
mount gid mapping
MOUNT_ATTR_IDMAP state
filesystem/caller/mount cross-mapping relationship
```

No `statmount` uidmap/gidmap proof or equivalent is required.

### 7.2 Concrete counterexample class

An ext4 filesystem may be exposed through an ID-mapped mount.

That path can still satisfy:

```text
statfs = EXT4_SUPER_MAGIC
mountinfo filesystem type = ext4
same mount ID throughout the effect
FS_CASEFOLD_FL = 0
all currently allowed inode flags
mode = expected mode
stat-visible uid/gid = expected execution uid/gid
xattrs empty
ACL mode-only
```

while the VFS applies a mount ID mapping to ownership and permission operations.

Likewise a caller in a nonidentity user namespace can observe userspace IDs that differ from the underlying kernel/filesystem ownership representation.

The same numeric `uid=1000` or `uid=0` appearing in the current record therefore does not by itself establish which physical/VFS ownership mapping produced it.

### 7.3 Why this matters to X1B

R4R10 treats ownership and permission metadata as authority/security-critical.

ID mapping changes exactly that semantic layer:

```text
reported inode owner
owner used by permission checks
owner applied to newly created inodes
ACL user/group interpretation
capability-root-ID interpretation where applicable
cross-namespace ownership visibility
```

A Human-bound effect that claims an exact physical/security prestate cannot leave this translation choice ambient.

Two executions with identical V10 request fields and visible numeric uid/gid may therefore correspond to different underlying ownership/security mappings.

That violates:

```text
exact material effect binding
no core security choice implicit
```

### 7.4 Why mount ID is not sufficient

A stable mount ID proves identity of the mount instance, not the semantic contents of its ID mapping.

Current `/proc/self/mountinfo` does not expose that mapping.

A stable mount ID can therefore remain stable while the review has never established whether the mount is identity-mapped or ID-mapped.

### 7.5 Correction class required before PASS

A successor must freeze one exact supported ownership-mapping profile.

A conservative correction class is:

```text
initial/identity caller user namespace only
non-idmapped reviewed mount only
exact uid/gid identity mapping proof
current user-namespace identity bound in request and final gate
current mount uidmap/gidmap proof bound in physical prestate
stat-visible owner and underlying identity semantics proven equivalent
```

If using current `statmount` mapping fields, inability to obtain a complete mapping proof must fail closed.

If another kernel interface is chosen, the brief must specify its exact semantics and negative tests.

At minimum regressions must cover:

```text
ext4 idmapped mount -> BLOCK
nonidentity uid map -> BLOCK unless explicitly reviewed
nonidentity gid map -> BLOCK unless explicitly reviewed
unreadable/unsupported mount mapping query -> BLOCK
mount mapping changes/replacement -> BLOCK/uncertainty
same numeric visible uid under different mapping -> never treated as equivalent authority state
```

## 8. Finding X1B-R4R10-IBR-F002 — loose-object mtime remains ambient but Git 2.55 treats it as pruning state

Severity: `BLOCKER`.

### 8.1 Current V10 loose-object construction

For a new object V10 does conceptually:

```text
create staged file
write compressed canonical object
verify canonical object/OID
fchmod 0444
verify uid/gid/mode/xattr/ACL/inode flags
fsync file
rename into canonical fanout
fsync source/destination directories
```

No V10 section requires:

```text
futimens/futimes
fixed mtime
request-bound mtime
mtime prestate/effect record
mtime verification
```

The physical metadata record also omits mtime.

Thus the final loose object mtime is determined by ambient execution/write time and is made durable by the file fsync.

### 8.2 Git 2.55 explicitly uses this field

Exact Git 2.55 source does not treat loose-object mtime as irrelevant decoration.

`object-file.c` says that an existing loose object with stale mtime may be subject to pruning and contains a `freshen_file()` helper that updates the timestamp.

`builtin/prune.c` performs:

```text
lstat(fullpath, &st)
if (st.st_mtime > expire)
    keep object
otherwise, if unreachable, prune it
```

Public Git documentation exposes the same contract through `git prune --expire` and `gc.pruneExpire`.

### 8.3 Why this is material in V10 specifically

V10 intentionally permits a pre-ref failure to leave exact canonical unreferenced loose objects/fanouts:

```text
BLOCKED_PRE_COMMIT_OBJECT_PREPARED_CLEAN
BLOCKED_PRE_COMMIT_BOUND_STAGING_RESIDUE
```

Those canonical loose objects are unreachable while `main` remains at the old SHA.

Their future survival under ordinary Git maintenance therefore depends in part on their mtime.

Under the current brief, two executions authorized by the same exact Human evidence but occurring at different wall-clock times can leave otherwise byte-identical canonical preparation residue with different Git pruning eligibility.

The effect process then calls `fsync`, making that ambient time durable.

This is not equivalent to an inode number or ctime that Git never consults for this purpose.

### 8.4 Normal-success interval also uses the same state

Before physical main-ref commitment, newly installed closure objects are also temporarily unreachable.

R4R10 verifies them before commitment, but their loose-object freshness semantics are still determined by ambient mtime during that interval.

The accepted design cannot call a Git-consumed durability field non-authority without an explicit reviewed argument.

### 8.5 Correction class required before PASS

A successor must make loose-object time semantics explicit.

A conservative correction class is:

```text
choose deterministic new-loose-object mtime source
bind it to request/Human-presented material effect
apply it before the final object file fsync
verify exact final mtime after canonical install
include it in object physical metadata/effect record
bind or classify pre-existing object mtime where authority relies on an existing loose representation
```

A natural deterministic candidate may be the exact Human-bound `request_created_at`, but selecting the value is a successor design decision and is not authorized by this review.

If the design instead argues that a class of timestamps is intentionally non-authority, it must separately prove that Git 2.55 maintenance semantics cannot vary as a result. Current source contradicts such a blanket claim for loose-object mtime.

Mandatory regressions must include at least:

```text
same V10 request executed at different wall-clock times -> identical authority-bound loose-object mtime
pre-ref failed prepared object -> deterministic pruning-age state
object fsync occurs after deterministic timestamp mutation
post-install mtime exact
mtime drift -> BLOCK/uncertainty
Git 2.55 prune-expiry boundary around object mtime
Git 2.55 freshen semantics do not introduce ambient unbound state
```

## 9. R4R10 properties that remain materially stronger

This NOT PASS does not reopen already corrected properties without evidence.

The review found no new blocker in the following design choices themselves:

```text
casefold/inode-flag gate as a concept
Linux/ext4 narrowing as a concept
request-bound staging namespace derivation
nonfinal fanout state outside canonical ODB names
nonfinal object temp state outside canonical fanouts
RENAME_NOREPLACE no-overwrite policy
source + destination parent fsync requirement
staging-root durable cleanup before ref commitment
extension-free full index v2
zero sharedindex under proven byte-exact namespace
no Git real-index writer
no Git ref writer
no Git primary object writer
post-fchmod file-fsync ordering
V10 Human marker/schema migration
no automatic recovery/rollback
```

These remain subject to implementation-level verification if implementation is ever separately authorized.

## 10. Required successor-review attacks

Any successor corrective brief must be attacked at minimum for:

```text
ID-mapped ext4 mount
noninitial caller user namespace
uid_map/gid_map translation
mount uidmap/gidmap query unavailable
identity vs nonidentity mapping equivalence
ACL ownership mapping
visible uid/gid equality under different kernel/VFS mapping
mount replacement with different ID map

new loose object at two execution wall-clock times
new loose object deterministic mtime application ordering
mtime mutation after fsync
mtime verification after rename
pre-existing loose object mtime treatment
failed pre-ref prepared-object prune eligibility
Git prune --expire boundary
Git gc prune expiry interaction
Git object freshen behavior

all PR #133 casefold/inode-flag regressions
all PR #133 staging/crash-residue regressions
all earlier ref/object/index/reflog/hook/replace/lazy/freshness attacks
```

## 11. Exact dispositions

```text
R4R9 IBR F001 LINUX INODE FLAGS / CASEFOLD = ADDRESSED AT BRIEF LEVEL IN R4R10
R4R9 IBR F002 PRE-REF NONFINAL CANONICAL ODB RESIDUE = ADDRESSED AT BRIEF LEVEL IN R4R10

R4R10 IBR F001 USER/MOUNT ID-MAPPING SEMANTICS = BLOCKER
R4R10 IBR F002 LOOSE-OBJECT MTIME / GIT PRUNING SEMANTICS = BLOCKER

AK-CANON X1B R4R10 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
IMPLEMENTATION AUTHORITY = NOT ESTABLISHED
X1B = OPEN
V1 AUTHORITY = NOT ESTABLISHED
```

## 12. Authority boundary

This review authorizes no repair.

Specifically it does not authorize:

```text
R4R11 successor brief
ScriptOps source mutation
Human decision request creation
Human decision/review
positive control
canonical effect
state recovery
merge
X1B closure
Agency Kernel V1
release
deployment
tag
```

`REVIEW FINDING != REPAIR AUTHORITY`.

## 13. Final review statement

R4R10 successfully closes the exact PR #133 casefold/inode-flag and malformed canonical ODB staging mechanisms at brief level.

It still does not close the complete Linux ownership-mapping semantics of the filesystem view, and it persists an ambient loose-object timestamp that Git 2.55 itself uses for pruning/freshness decisions.

Therefore:

```text
AK-CANON X1B R4R10 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
IMPLEMENTATION AUTHORITY = NOT ESTABLISHED
X1B = OPEN
V1 AUTHORITY = NOT ESTABLISHED
```
