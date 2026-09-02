# X1B Human Decision Authorship — Independent AK-CANON R4R11 Implementation-Brief Review

Status: `INDEPENDENT REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: `2026-09-02`

## 1. Verdict

`AK-CANON X1B R4R11 IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

R4R11 materially improves R4R10 and addresses both findings frozen in PR #135 at brief level:

1. user/mount ID-mapping is no longer treated as an implicit property. V11 requires the Linux initial user namespace, full identity uid/gid mappings, stable execution credential state, and a `statmount()` proof that the reviewed ext4 mount is not ID-mapped;
2. loose-object mtime is no longer ambient. V11 makes mtime Human-visible retention metadata and seals every canonical loose leaf in `new_object_closure` to one exact timestamp before ref commitment, including pre-existing exact leaves and exact concurrent winners, with file `fsync()` after the timestamp mutation.

The V11 schema migration correctly prevents V10 or earlier Human evidence from authorizing the changed runtime-identity and retention-metadata effect surface.

However, independent adversarial review found two new blockers:

1. the initial-user-namespace and mapping proof trusts pathname reads below `/proc/self/...` without proving that those procfs authority sources themselves are genuine and un-overmounted. Linux permits single-file bind mounts and namespace files are explicitly designed to be pinned by bind mounts. A preconfigured mount namespace can therefore substitute a valid initial-user-namespace handle at the path used by V11 and substitute identity-looking uid/gid map files while the task itself remains in a different user namespace. R4R11 contains no procfs provenance, no mount-ID closure for those authority paths, and no no-cross-mount resolution rule;
2. the crash-durability proof narrows to ext4 and checks generic mount/superblock attributes, but it does not bind ext4 filesystem-specific durability options. The V11 `statmount()` request omits `STATMOUNT_MNT_OPTS` / `STATMOUNT_OPT_ARRAY`. Current ext4 supports `barrier=0` / `nobarrier`, which disables the JBD write barriers that the kernel documentation says enforce on-disk ordering of journal commits and make volatile write caches safe. Thus an ext4 mount can pass the current V11 type/ID-map/SB_LAZYTIME checks while the durability semantics assumed by `CRASH_DURABLE_OBJECT_REF_INDEX_V6` are weaker than the brief claims.

Either finding independently prevents implementation authority.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R11 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R11 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#136`

```text
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
BASE TREE = df807db7003dfd201e9be4d5927472e515a2e737
HEAD = 0f5c5ed3406404942cafbffd7d1161d7f96e32a2
TREE = 24800c2bcaa9d1f9f2b380f8579ff40016a42c74
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R11.md
BLOB = 9ea872947b6e38ed0cf188f55aca522667e579bb
```

Immediately before review write, PR #136 remained:

```text
state = OPEN
merged = false
draft = true
mergeable = true
commits = 1
changed_files = 1
additions = 2208
deletions = 0
```

`FJ899/8 main` also remained exactly:

```text
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

The exact R4R11 file was freshly reread from the reviewed HEAD before this artifact was written.

## 3. Normative lineage

### 3.1 Accepted corrective design

```text
FJ899/scriptops PR #34
HEAD = d7a5065c87e9a4b49fb608235c908bceac42b4b1
TREE = 3140d0ac95c120a7b1532942bae2e0dad38b4839
PATH = governance/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_CANDIDATE.md
BLOB = dac16f109d1414a2208c2ed9a166ae9e9a329216
```

Higher-level normative properties remain:

```text
separate trusted Human decision act
exact content/scope/candidate/effect binding
explicit freshness/activity/supersession/conflict/replay semantics
executor no-substitution
fail closed on ambiguity
real-boundary negative regressions
real separately authorized positive Human control
post-effect truth matching the Human-bound effect
no failed operation durably misreported as successful Human-attributed effect
no core authority/security choice left implicit
```

### 3.2 Independent corrective-design review

```text
FJ899/8 PR #109
HEAD = 132d65be48331a822039262b707c47a81d02a64d
TREE = a8bdc363d293beb7b15ae8b787cc3ebdd694fd99
BLOB = 439109e104244552a5ac1f3f08988dba283733d0
VERDICT = AK-CANON X1B CORRECTIVE DESIGN REVIEW R2 = PASS
```

### 3.3 R4R10 predecessor and binding review

```text
FJ899/8 PR #134
HEAD = b2824d95e15ae5de782eeb5d59ffc784b1a116b1
TREE = d9c9003746f3ccafb97157e6e37ce12395d12709
BLOB = f3a7e5b5c163de995078d96682c822e5ec15567c
```

```text
FJ899/8 PR #135
HEAD = c5fee5d7979d8dcf3e4c9628c578a257a89d913c
TREE = de73cfbcef715a2c1bc2ca27e169aceedc72685e
BLOB = 306a68095ca584ef918324bbc83b227dc23eabf2
VERDICT = AK-CANON X1B R4R10 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #135 froze:

```text
X1B-R4R10-IBR-F001 — Linux user/mount ID mapping is unbound
X1B-R4R10-IBR-F002 — loose-object mtime / Git pruning semantics are unbound
```

## 4. Review method

The review attacked the exact R4R11 artifact rather than treating a stronger successor profile as presumptively correct.

The adversarial pass inspected at least:

```text
initial user namespace identity proof
/proc/self/ns/user source provenance
/proc/self/uid_map and gid_map source provenance
mount namespace source provenance
single-file and namespace-file bind-mount semantics
execution credential binding
statx unique mount-ID use
statmount exact mount / uidmap / gidmap semantics
ext4 type and generic mount/superblock attributes
ext4 filesystem-specific durability options
fsync and journal ordering assumptions
Human-bound loose-object mtime sentinel
pre-existing/winner mtime sealing
file-fsync ordering after mtime mutation
staging/root cleanup and crash classifications
V11 request/review/effect schema migration
prior casefold/inode/index/ref/reflog/worktree corrections
```

## 5. Current external semantics checked

### 5.1 Initial user namespace and identity mappings

Current Linux documentation states that the initial user namespace uses the full identity mapping:

```text
0 0 4294967295
```

for both UID and GID mapping, leaving `(uid_t)-1` / `(gid_t)-1` unmapped.

Sources checked:

```text
https://man7.org/linux/man-pages/man7/user_namespaces.7.html
https://cdn.kernel.org/doc/html/latest/filesystems/idmappings.html
```

Current Linux UAPI exposes the initial user-namespace inode constant used by V11:

```text
USER_NS_INIT_INO = 0xEFFFFFFD
```

Source checked:

```text
https://github.com/torvalds/linux/blob/master/include/uapi/linux/nsfs.h
```

### 5.2 Namespace files and bind mounts

Linux namespace files under `/proc/pid/ns/*` may be opened directly or through a pathname that is a bind mount of one of those namespace files; bind mounting such files is a documented mechanism for pinning a namespace.

Sources checked:

```text
https://man7.org/linux/man-pages/man7/namespaces.7.html
https://man7.org/linux/man-pages/man1/nsenter.1.html
```

Linux bind mounts can remount a single file onto a single file, not only whole directory trees.

Sources checked:

```text
https://man7.org/linux/man-pages/man8/mount.8.html
https://man7.org/linux/man-pages/man2/mount.2.html
```

Therefore pathname reads below `/proc/self/...` are not, by themselves, a proof that the returned namespace/map object is the kernel-generated procfs object for the calling task.

### 5.3 `statmount()` and unique mount IDs

Current `statmount(2)` supports querying mount state by a unique mount ID obtained from `statx(STATX_MNT_ID_UNIQUE)`; current Linux also has `STATMOUNT_BY_FD` on sufficiently new kernels.

Current `statmount()` can return:

```text
STATMOUNT_MNT_BASIC
STATMOUNT_MNT_OPTS
STATMOUNT_OPT_ARRAY
STATMOUNT_MNT_UIDMAP
STATMOUNT_MNT_GIDMAP
STATMOUNT_SUPPORTED_MASK
```

and `sb_flags` contains only generic flags such as:

```text
SB_RDONLY
SB_SYNCHRONOUS
SB_DIRSYNC
SB_LAZYTIME
```

Source checked:

```text
https://man7.org/linux/man-pages/man2/statmount.2.html
```

Thus filesystem-specific ext4 options are not represented merely by the V11 generic `sb_flags` checks; `statmount` exposes separate mount-option/option-array surfaces that R4R11 does not request.

### 5.4 ext4 barrier semantics

Current ext4 kernel documentation defines:

```text
barrier=<0|1>
barrier
nobarrier
```

and states that `barrier=0` disables JBD write barriers while barriers enforce proper on-disk ordering of journal commits and make volatile disk write caches safe to use.

Source checked:

```text
https://cdn.kernel.org/doc/html/latest/admin-guide/ext4.html
```

The documentation notes that disabling barriers may be safe when storage is battery-backed. R4R11 does not prove such a storage property either.

### 5.5 Git 2.55 loose-object mtime semantics

The mtime correction itself was cross-checked against exact Git 2.55 semantics.

Git 2.55 `object-file.c` freshens loose-object mtime because stale objects can become pruning candidates, and Git 2.55 `builtin/prune.c` compares loose-object `st_mtime` against the expiry threshold.

Sources checked:

```text
https://github.com/git/git/blob/v2.55.0/object-file.c
https://github.com/git/git/blob/v2.55.0/builtin/prune.c
https://git-scm.com/docs/git-prune
```

Current Git documentation also confirms that `maintenance.auto=false` disables command-triggered auto maintenance, which is consistent with V11's bounded Git subprocess profile.

Source checked:

```text
https://git-scm.com/docs/git-maintenance
```

## 6. PR #135 finding F001 — user/mount ID mapping

Disposition: `ADDRESSED AT BRIEF LEVEL` for the exact R4R10 mechanism.

R4R11 now requires:

```text
caller user namespace = Linux initial user namespace
fstat(nsfd).st_ino = USER_NS_INIT_INO
uid_map = one full identity range
gid_map = one full identity range
ruid=euid=suid=fsuid
rgid=egid=sgid=fsgid
supplementary groups bound
capability sets bound
NoNewPrivs bound
statmount exact reviewed mount
MOUNT_ATTR_IDMAP = 0
mnt_uidmap_num = 0
mnt_gidmap_num = 0
```

It also fails closed when `statmount()` cannot prove the exact mount and forbids privilege or namespace transitions used merely to manufacture a passing proof.

These are material corrections to the R4R10 finding.

The new finding below is different: the values themselves are now well specified, but the pathname transport used to obtain part of that authority state is not physically authenticated.

## 7. Finding X1B-R4R11-IBR-F001 — procfs authority-source provenance is not bound

Severity: `BLOCKER`.

### 7.1 Authority sources trusted by V11

R4R11 obtains authority-critical state from paths including:

```text
/proc/self/ns/user
/proc/self/uid_map
/proc/self/gid_map
/proc/self/ns/mnt
/proc/self/mountinfo
```

The initial-userns proof explicitly opens `/proc/self/ns/user` and accepts the returned namespace object when `fstat(...).st_ino` equals `USER_NS_INIT_INO`.

The mapping proof reads `/proc/self/uid_map` and `/proc/self/gid_map` and accepts the full identity tuples.

But R4R11 does not require any of:

```text
/proc root is genuine procfs
PROC_SUPER_MAGIC on held procfs authority root
held descriptor-relative resolution from a verified procfs root
no nested mount / overmount on the current PID directory
no nested mount / overmount on ns/user
no nested mount / overmount on uid_map or gid_map
mount-ID equality between expected procfs source and each authority file
openat2 RESOLVE_NO_XDEV / equivalent no-cross-mount rule for authority reads
```

No physical-prestate record proves the procfs source objects themselves.

### 7.2 Concrete counterexample class

Linux permits a single file to be bind-mounted onto another file.

Linux namespace files are explicitly valid bind-mount sources and opening a bind-mounted namespace file returns a handle for that bound namespace.

Therefore a mount namespace can be prepared before ScriptOps starts such that the task is actually in a noninitial user namespace while a pathname that V11 later reaches as `/proc/self/ns/user` resolves through an overmount to a pinned initial-user-namespace file.

Likewise, the paths V11 later reads as:

```text
/proc/self/uid_map
/proc/self/gid_map
```

can be hidden by file/directory overmounts that expose identity-looking text instead of the current task's kernel-generated mapping files.

This environment can be constructed by a more privileged parent before launching the effect process; the effect process need not perform any forbidden mount or namespace transition itself.

The V11 rules:

```text
no setns
no unshare
no mount_setattr
no privilege acquisition
```

therefore do not close the counterexample.

### 7.3 Why the inode constant does not close the spoof

`USER_NS_INIT_INO` is a sound identity for the initial namespace object that is actually opened.

The problem is not the constant.

If the pathname is overmounted with a bind-mounted initial-userns namespace file, then the opened object legitimately *is* the initial namespace object and legitimately reports the initial namespace inode. The proof has established the identity of the substituted file, not the identity of the calling task's actual user namespace.

The missing property is provenance between:

```text
current task
-> genuine current-task procfs entry
-> namespace/map object
```

### 7.4 Why the mapping files do not close the spoof

The mapping tuple checks are likewise semantically correct for a genuine current-task procfs source.

But V11 reads by pathname without proving the mount/source of those paths. A substituted regular file with the expected identity-map text is not rejected by the current brief.

Even if an implementation additionally checks that the file is readable and the bytes parse canonically, that still does not establish procfs provenance.

### 7.5 Security consequence

R4R11 uses the initial-userns proof as a prerequisite for interpreting:

```text
uid/gid ownership
ACL identities
filesystem permission semantics
statmount uid/gid mapping output
execution credential state
```

A spoofed proc authority source can therefore cause the implementation to claim `LINUX_INITIAL_USER_NAMESPACE_V1 = PASS` when the current task is not in that namespace.

That reopens the exact semantic layer PR #135 required the successor to close.

### 7.6 Required disposition

```text
X1B-R4R11-IBR-F001 = BLOCKER
```

No R4R11 implementation authority exists while current-task namespace/map identity depends on unbound `/proc` pathname provenance.

A successor may choose a stricter procfs-origin/no-overmount proof or another kernel-bound method, but this review does not authorize or implement that repair.

## 8. PR #135 finding F002 — loose-object mtime / pruning semantics

Disposition: `ADDRESSED AT BRIEF LEVEL` for the exact R4R10 mechanism.

R4R11 now makes loose-object mtime explicit Human-bound retention metadata:

```text
profile = HUMAN_BOUND_LOOSE_OBJECT_MTIME_V1
mtime = 2038-01-18T00:00:00.000000000Z
```

It applies this to:

```text
newly staged/installed closure leaves
pre-existing exact closure leaves
exact concurrent EEXIST winners
```

and requires:

```text
futimens(... exact sentinel ...)
exact readback
file fsync AFTER mtime mutation
exact final reread
```

The request/effect schema binds the profile and timestamp, pre-ref failure classes truthfully admit persistent mtime-sealing side effects, and the profile blocks after its explicit horizon.

This addresses the exact ambient-mtime problem identified in PR #135.

The new blocker below is not an mtime regression. It concerns the ext4 durability contract on which the entire file/ref/index/object crash-durability proof relies.

## 9. Finding X1B-R4R11-IBR-F002 — ext4 durability-affecting mount options are not bound

Severity: `BLOCKER`.

### 9.1 Current V11 mount proof

R4R11 requires `statmount()` fields including:

```text
STATMOUNT_SB_BASIC
STATMOUNT_MNT_BASIC
STATMOUNT_FS_TYPE
STATMOUNT_MNT_NS_ID
STATMOUNT_MNT_UIDMAP
STATMOUNT_MNT_GIDMAP
STATMOUNT_SUPPORTED_MASK
```

It then constrains at least:

```text
filesystem = ext4
MOUNT_ATTR_RDONLY = 0
MOUNT_ATTR_IDMAP = 0
SB_RDONLY = 0
SB_LAZYTIME = 0
```

and records `SB_SYNCHRONOUS` / `SB_DIRSYNC` if present.

But it does not request or bind:

```text
STATMOUNT_MNT_OPTS
STATMOUNT_OPT_ARRAY
```

and does not freeze ext4-specific journal/barrier durability options.

### 9.2 Concrete ext4 counterexample

An ext4 repository mount can use:

```text
barrier=0
```

or equivalently:

```text
nobarrier
```

while still satisfying the current V11 conditions:

```text
filesystem = ext4
mount writable
MOUNT_ATTR_IDMAP = 0
SB_RDONLY = 0
SB_LAZYTIME = 0
byte-exact namespace
inode semantic flags allowed
```

`barrier=0` is an ext4/JBD policy, not a generic `SB_LAZYTIME` or `MOUNT_ATTR_IDMAP` bit.

Current kernel documentation states that disabling barriers disables JBD write barriers; write barriers are what enforce proper on-disk journal-commit ordering and make volatile write caches safe.

### 9.3 Why this is authority-relevant

R4R11 defines profiles whose names and acceptance conditions make a crash-durability claim:

```text
FSYNC_AFTER_FINAL_METADATA_V1
CRASH_DURABLE_OBJECT_REF_INDEX_V6
ALIAS_SAFE_MAIN_REF_COMMITMENT_V7
```

The local sequence relies on statements of the form:

```text
file fsync completed
parent directory fsync completed
therefore prepared object/ref/index state is crash-durable
```

That implication depends on the filesystem/storage ordering contract actually in force.

On an ext4 configuration where journal write barriers are disabled, the kernel's own documentation says volatile cache safety and commit ordering are weaker.

A Human-bound effect cannot silently equate:

```text
ext4
```

with:

```text
ext4 configured for the durability ordering assumed by V11
```

### 9.4 Hardware/firmware exclusion does not close this

R4R11 says hardware/firmware that falsely reports durable completion is outside the claim.

That exclusion does not address this finding.

`nobarrier` is an explicit kernel/filesystem policy that can intentionally avoid the ordering mechanism needed to make an ordinary volatile write cache safe. The hardware need not lie about command completion for the V11 on-disk ordering assumption to be weaker than claimed.

The ext4 documentation explicitly distinguishes the battery-backed-storage case as a reason disabling barriers may be safe. V11 does not prove battery-backed/nonvolatile cache semantics either.

### 9.5 `statmount()` already exposes a stronger query surface

Current `statmount(2)` provides separate fields for mount options and filesystem option arrays:

```text
STATMOUNT_MNT_OPTS
STATMOUNT_OPT_ARRAY
```

while `sb_flags` is only a small generic set.

R4R11 uses the new syscall for ID-map proof but omits the option surfaces relevant to the new ext4 durability claim.

This is a core security/durability choice left implicit.

### 9.6 Required disposition

```text
X1B-R4R11-IBR-F002 = BLOCKER
```

A successor must establish a closed filesystem/storage durability profile instead of treating all writable non-lazytime ext4 mounts as equivalent. This review does not authorize or implement a repair.

## 10. Cross-check of V11 mtime ordering

No blocker was found in the normal V11 ordering of the specific PR #135 mtime correction.

For a new staged object, the brief requires:

```text
write
verify canonical bytes/OID
fchmod 0444
futimens exact sentinel
verify authority metadata + mtime
fsync(file) AFTER final metadata/mtime
RENAME_NOREPLACE
fsync destination fanout
fsync source staging root
final reread
```

For a qualifying pre-existing or EEXIST winner leaf, it requires:

```text
verify exact object/security/topology
futimens exact sentinel
verify mtime
fsync(file) AFTER mtime
reopen and verify
```

That ordering addresses the prior post-metadata-fsync class for the mtime mutation itself.

The review therefore does not manufacture an mtime finding merely because the successor changed this surface.

## 11. Cross-check of V11 ID-map semantics apart from proc provenance

No blocker was found in the semantic values V11 requires once the authority source is assumed genuine.

The following are materially stronger than R4R10:

```text
USER_NS_INIT_INO exact
full identity uid/gid maps
fsuid/fsgid binding
supplementary groups binding
capability-state binding
statx unique mount identity
statmount MOUNT_ATTR_IDMAP absence
zero mount UID/GID maps
fail closed on statmount inability
```

The review also checked that current `statmount()` distinguishes mount uid/gid mapping state and has a supported-mask mechanism.

Again, the blocker is source provenance, not the arithmetic of the mapping rules.

## 12. Prior corrections preserved at brief level

The independent pass found no reason in these two new findings to reopen the previously corrected mechanisms for:

```text
casefold / Linux inode semantic flags
request-bound object staging namespace
nonfinal canonical fanout avoidance
post-fchmod/futimens file-fsync ordering
hardlink-free loose-object install
split-index/sharedindex rejection
raw extension-free index-v2 replacement
physical loose main ref topology
packed-main rejection
reflog deterministic projection
worktree/log alias-safe projection
replacement refs / commit encoding
hook closure
lazy-fetch/promisor/alternates
Human currentness/conflict/replay binding
```

This is not a blanket PASS for every historical line. The review verdict remains NOT PASS because either new blocker is sufficient.

## 13. Mandatory regressions implied by this review

A successor review must attack at least the following additional cases.

### 13.1 Proc authority provenance

```text
/proc not procfs -> BLOCK
/proc current-PID directory hidden by submount -> BLOCK
/proc/<self-pid>/ns hidden by submount -> BLOCK
/proc/<self-pid>/ns/user overmounted with pinned initial-userns file -> BLOCK
/proc/<self-pid>/uid_map overmounted with regular identity-map text -> BLOCK
/proc/<self-pid>/gid_map overmounted with regular identity-map text -> BLOCK
namespace/map authority path crosses a mount boundary not explicitly authorized -> BLOCK
procfs mount/source identity changes between request and FinalEffectGate -> BLOCK
procfs authority provenance becomes unreadable/uncertain -> no effect
```

A positive control must prove that a genuine current-task procfs path is accepted without broadening to arbitrary proc-like filesystems or bind-mounted substitutes.

### 13.2 ext4 durability options

At minimum attack:

```text
ext4 default/barrier-enabled reviewed profile -> expected supported case
ext4 barrier=0 -> BLOCK unless a separately frozen equivalent durability proof exists
ext4 nobarrier -> BLOCK unless a separately frozen equivalent durability proof exists
required ext4 mount-option query unavailable -> BLOCK
STATMOUNT_MNT_OPTS unavailable when relied upon -> BLOCK
STATMOUNT_OPT_ARRAY unavailable when relied upon -> BLOCK
mount options drift during effect -> durability uncertainty / block
unknown ext4 option that can weaken journal/cache ordering -> BLOCK
```

If a successor chooses another storage contract instead of requiring barriers, that contract must itself be explicit, Human-bound and independently reviewable.

## 14. Required review verdict matrix

```text
PR #135 F001 user/mount ID mapping values        = ADDRESSED AT BRIEF LEVEL
PR #135 F002 loose-object mtime/pruning          = ADDRESSED AT BRIEF LEVEL

R4R11 IBR F001 procfs authority provenance       = BLOCKER
R4R11 IBR F002 ext4 durability mount options     = BLOCKER

AK-CANON X1B R4R11 IMPLEMENTATION-BRIEF REVIEW  = NOT PASS
IMPLEMENTATION AUTHORITY                          = NOT ESTABLISHED
X1B                                               = OPEN
V1 AUTHORITY                                      = NOT ESTABLISHED
```

## 15. STOP boundary

This artifact is review evidence only.

It does not authorize:

```text
R4R12 or other successor correction
ScriptOps source mutation
Human decision evidence creation
positive control
canonical screenplay effect
recovery mutation
merge
X1B closure
Agency Kernel v1
release
deployment
tag
```

Required next legal step after this review is durably frozen:

```text
fresh Human authorization
-> successor corrective implementation brief addressing
   X1B-R4R11-IBR-F001
   X1B-R4R11-IBR-F002
```

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
NOT PASS != AUTHORITY TO FIX
AI PROPOSES != HUMAN DECIDES
```
