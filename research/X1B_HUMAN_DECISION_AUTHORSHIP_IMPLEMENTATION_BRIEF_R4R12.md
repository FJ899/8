# X1B HUMAN DECISION AUTHORSHIP — CLEAN IMPLEMENTATION BRIEF R4R12

Status: `CLEAN R4R12 CORRECTIVE BRIEF / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-02`

## 1. Authority, purpose, and STOP boundary

This document is the self-contained successor to R4R11 after independent AK-CANON review PR #137 returned `NOT PASS`.

It preserves the accepted X1B corrective design and every R4R11 property not rejected by PR #137, while correcting exactly the two blockers frozen by that review:

1. R4R11 specified correct initial-user-namespace and uid/gid-map values but trusted pathname reads below `/proc/self/...` without proving that those authority sources were genuine current-task procfs objects rather than file/directory overmounts or pinned namespace-file substitutions;
2. R4R11 narrowed the repository filesystem to ext4 and checked generic mount/superblock state, but did not bind the filesystem-specific ext4 option state that controls journal/write-barrier durability.

R4R12 therefore changes both the kernel authority-source provenance contract and the ext4 durability contract.

New exact profiles:

```text
AUTHENTIC_CURRENT_TASK_PROCFS_V1
AUTHENTIC_EXT4_RUNTIME_STATE_V1
LINUX_INITIAL_USER_NAMESPACE_V2
LINUX_EXECUTION_CREDENTIAL_STATE_V2
LINUX_NON_IDMAPPED_EXT4_MOUNT_V2
EXT4_BARRIERED_FSYNC_DURABILITY_V1
CRASH_DURABLE_OBJECT_REF_INDEX_V7
ALIAS_SAFE_MAIN_REF_COMMITMENT_V8
REF_CAS_FIRST_ALIAS_SAFE_RAW_GIT_METADATA_V10
```

Preserved exact profiles include:

```text
LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1
LINUX_INODE_SEMANTIC_FLAGS_V1
FSYNC_AFTER_FINAL_METADATA_V1
HUMAN_BOUND_LOOSE_OBJECT_MTIME_V1
BOUND_OBJECT_STAGING_NAMESPACE_V2
ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V4
COMPLETE_LOCAL_OBJECT_STORE_V4
FULL_SINGLE_FILE_INDEX_V1
CLOSED_FULL_INDEX_V2_REWRITE_V1
ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1
ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V3
DETERMINISTIC_MAIN_REFLOG_PROJECTION_V2
ALIAS_SAFE_WORKTREE_PROJECTION_V2
PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1
CLOSED_RAW_TREE_REWRITE_V1
NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2
NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1
CLOSED_RAW_COMMIT_OBJECT_V1
```

Because the provenance and storage-durability surfaces are authority-critical, all request/review/admission/gate/material-effect/decision-record schemas are V12.

This document is an implementation brief only. It authorizes no ScriptOps source mutation, no Human decision PR/review, no positive control, no canonical screenplay effect, no recovery, no merge, no X1B closure, no Agency Kernel v1, no release, deployment, or tag.

```text
R4R12 BRIEF != IMPLEMENTATION AUTHORITY
R4R12 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R12 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

After durable freeze of this brief, STOP.

The next legal stage is one separately Human-authorized independent AK-CANON R4R12 implementation-brief review.

## 2. Exact governance lineage

### 2.1 Accepted corrective design

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

### 2.2 Independent corrective-design review

```text
FJ899/8 PR #109
HEAD = 132d65be48331a822039262b707c47a81d02a64d
TREE = a8bdc363d293beb7b15ae8b787cc3ebdd694fd99
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_DESIGN_AK_CANON_REVIEW_R2.md
BLOB = 439109e104244552a5ac1f3f08988dba283733d0
VERDICT = AK-CANON X1B CORRECTIVE DESIGN REVIEW R2 = PASS
```

### 2.3 R4R11 predecessor

```text
FJ899/8 PR #136
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 0f5c5ed3406404942cafbffd7d1161d7f96e32a2
TREE = 24800c2bcaa9d1f9f2b380f8579ff40016a42c74
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R11.md
BLOB = 9ea872947b6e38ed0cf188f55aca522667e579bb
```

### 2.4 Binding R4R11 NOT-PASS review

```text
FJ899/8 PR #137
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = ae35d3778023e8076eaff57634089aa0f2cc7e3c
TREE = 27bdd393639b225a8654ba6ee20db8f7419fa7d2
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R11_AK_CANON_REVIEW.md
BLOB = f0c3b2822c075920af9565aaa18fed65a47992a2
VERDICT = AK-CANON X1B R4R11 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #137 froze:

```text
X1B-R4R11-IBR-F001 — procfs authority-source provenance is not bound
X1B-R4R11-IBR-F002 — ext4 durability-affecting mount options are not bound
```

PR #137 also recorded that R4R11 addressed at brief level:

```text
X1B-R4R10-IBR-F001 user/mount ID-mapping values
X1B-R4R10-IBR-F002 loose-object mtime / Git pruning semantics
```

and found no reason to reopen the prior casefold/inode-flag, object-staging, fsync ordering, split-index/sharedindex, loose-ref, reflog, worktree, replacement-ref, hook, lazy-fetch, raw-index, freshness, currentness, or replay corrections.

`REVIEW FINDING != REPAIR AUTHORITY`; R4R12 exists only under fresh Human authorization for this successor brief.

## 3. Exact evidence-repository base

```text
FJ899/8 main
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

No history rewrite is part of R4R12.

## 4. Frozen ScriptOps baseline

```text
FJ899/scriptops main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Security-relevant baseline BLOBs remain:

```text
phase6/scriptops-v2-hardening.py
4f379960ed5677634dd234af6aa39626782b6133

legacy/scriptops-v2-single.py
9baa7b3a1eb746e34b79207a382eea1f5dd4ec55

phase6/bounded-proposal-view.py
27f50f0df85fe6b66cfd3c33be00c6d975762b45

scripts/restore_v2.py
fa2099d7d4530bce2256051690935625dab0e927

scripts/verify_repository.py
a61278086b92824d7e442b390c951e918c88517b

sources/prototype/RESTORE.md
8a79aca4c93b23c4842792bea9ecaae146e1fc48

SOURCE_MANIFEST.md
2acf2ece298bfcf89254087c9e747fcb808ab241

README.md
c52f515dd3d736c749eca75cf319b514f8427c5a

PROJECT_STATE.md
dea1d11c847765026f8766fa70aa111c3f77c7bd

HANDOFF.md
2e0c3be2a9bdebfeac161773ca9631f8312f42f6

tests/test_phase6_scriptops_smoke.py
d6065047268cee5591883a3065ce49886ec85bcf

.github/workflows/phase6-scriptops-smoke.yml
a811dc75b4d3c7a1ebd8375c24fc71c74586ddf5

.github/workflows/verify-repository.yml
7d896d425012479c97bf1e6539f9a861a4a17aa5
```

Historical prototype reconstruction remains immutable evidence with SHA-256 `881dade6c6c506b9a9d41ebfbf68afb18b66db7583d35f746fb29ed7b36ac596`, size `51980` bytes.

## 5. Normative precedence and V12 migration

```text
R4R12 TEXT = CURRENT IMPLEMENTATION-BRIEF AUTHORITY
R4R11 / R4R10 / R4R9 / R4R8 / R4R7 / R4R6 / R4R5 / R4R4 / R4R3 / R4R2 / R4R1 / R4 / R3 / R2 / R1 = HISTORICAL INPUT ONLY
CORRECTIVE DESIGN PR #34 = HIGHER-LEVEL PROPERTY CONTRACT
```

R4R12 changes authority-critical surfaces:

```text
current-task procfs source provenance becomes explicit
/proc/self pathname trust is removed from the authority proof
numeric current PID/TID binding is proven against genuine procfs thread-self
all proc authority reads are held-fd, descriptor-relative and no-cross-mount
user namespace identity is read from a proven current-thread procfs namespace entry
uid/gid maps are read from a proven current-process procfs entry
repository ext4 mount options become Human-bound durability state
STATMOUNT_MNT_OPTS and STATMOUNT_OPT_ARRAY are mandatory
full effective ext4 option state is cross-proved through authenticated /proc/fs/ext4/<dev>/options
journal presence/error state is cross-proved through authenticated ext4 sysfs state
barrier-disabled ext4 is unsupported
writeback data mode is unsupported
journal_async_commit is unsupported
filesystem/runtime durability state drift is authority-relevant
```

Therefore:

```text
V11 REQUEST/REVIEW/ADMISSION/GATE != R4R12 AUTHORITY
V11 HUMAN REVIEW MARKER != V12 HUMAN DECISION
V12 EFFECT PROFILE REQUIRES FRESH V12 HUMAN-BOUND REQUEST
```

No V11 or earlier Human evidence may authorize a V12 effect.

## 6. Future bounded implementation surface

Expected implementation surface remains:

```text
phase6/scriptops-v2-hardening.py
legacy/scriptops-v2-single.py
phase6/x1b_human_decision.py
scripts/restore_v2.py
scripts/verify_repository.py
sources/prototype/RESTORE.md
SOURCE_MANIFEST.md
README.md
PROJECT_STATE.md
HANDOFF.md
tests/test_phase6_scriptops_smoke.py
tests/test_x1b_human_decision.py
.github/workflows/x1b-human-decision.yml
```

Expected unchanged:

```text
phase6/bounded-proposal-view.py
.github/workflows/phase6-scriptops-smoke.yml
.github/workflows/verify-repository.yml
sources/prototype/scriptops-v2-single.py.part01..part07
```

Any additional tracked path requires STOP and fresh Human authorization before mutation.

## 7. Core Human-decision rule preserved

```text
HumanDecision = TRUE
ONLY IF
separate trusted Human decision evidence
for exact current content + scope + candidate + material effect
is independently validated and admitted.
```

Never sufficient by itself:

```text
approval command possession
non-empty --why
caller rationale
continuation
silence
AI-created proposal/PR/comment/record
identity label
hard-coded approver="human"
CI success
green tests
mergeability
effect credential
```

Preserve:

```text
AI PROPOSED != HUMAN DECIDED
APPROVAL COMMAND POSSESSION != HUMAN DECISION AUTHORSHIP
NON-EMPTY WHY != HUMAN ACT
IDENTITY != CREDENTIAL != CHANNEL != CAPABILITY != AUTHORITY
HUMAN DECISION EVIDENCE != EXECUTION CREDENTIAL
EFFECT CAPABILITY != AUTHORITY TO CREATE HUMAN DECISION EVIDENCE
SHAPE MATCH != TRUSTED ORIGIN
```

## 8. Exactly one current acceptance interface

After implementation, the only current effect-capable Human-decision acceptance interface remains:

```text
python phase6/scriptops-v2-hardening.py approve --decision-pr <positive-integer>
```

PR number is a locator only, never authority.

No caller-controlled field may supply Human actor/result/rationale, request path/digest, task/scene/candidate/impact identities, canonical target/ref, procfs provenance, PID/TID source identity, user namespace, uid/gid mapping, execution credentials, repository mount identity, ext4 option state, filesystem durability profile, inode semantic state, physical Git-dir/ref/object/index topology, staging namespace, loose-object mtime, metadata policy, reflog semantics, effect type, material effect, raw-object profile, hook profile, commitment profile, or effect commit metadata.

Defect-era direct approval/promotion routes remain disabled and non-effect-capable.

## 9. Git/runtime/OS profile V12

Git semantic compatibility remains bounded to:

```text
2.55.0 <= parsed Git version < 2.56.0
object format = sha1
ref storage format = files
```

R4R12 authority platform remains deliberately narrow:

```text
OS = Linux
repository filesystem = ext4
repository source profile = direct /dev/<kernel-devname> only
one reviewed repository mount for all authority-critical repository paths
byte-exact case-sensitive authority directories
no unsupported Linux inode semantic flags
caller user namespace = Linux initial user namespace
reviewed repository mount = not ID-mapped
current-task proc authority = authenticated genuine procfs only
ext4 journal = present
ext4 data mode = ordered or journal
ext4 JBD write barriers = configured enabled
ext4 journal_async_commit = disabled
ext4 filesystem has no recorded error state accepted by V12
```

Required primitives now include:

```text
getpid
gettid
getresuid/getresgid
getgroups
capget or equivalent current-thread capability read
openat2
RESOLVE_BENEATH
RESOLVE_NO_XDEV
RESOLVE_NO_SYMLINKS
O_PATH
O_NOFOLLOW
O_DIRECTORY
O_EXCL
O_CLOEXEC
fstat/fstatfs/statfs/statx
STATX_MNT_ID_UNIQUE where supported/required
statmount
STATMOUNT_SB_BASIC
STATMOUNT_MNT_BASIC
STATMOUNT_FS_TYPE
STATMOUNT_MNT_NS_ID
STATMOUNT_MNT_UIDMAP
STATMOUNT_MNT_GIDMAP
STATMOUNT_SUPPORTED_MASK
STATMOUNT_MNT_OPTS
STATMOUNT_OPT_ARRAY
STATMOUNT_SB_SOURCE
STATMOUNT_MNT_ROOT
readlinkat
fchmod
futimens
fsync regular file
fsync directory
listxattr
POSIX ACL inspection
FS_IOC_GETFLAGS
FS_IOC_FSGETXATTR
```

If any required primitive is unavailable or blocked by kernel support, seccomp, LSM, containerization, privilege restrictions, or another cause, V12 is `BLOCKED`.

V12 MUST NOT acquire privilege, invoke `sudo`, call `setns`, `unshare`, `mount`, `mount_setattr`, remount the repository, toggle an ext4 option, alter block-cache policy, modify procfs/sysfs, or delegate the authority proof to an unreviewed helper.

## 10. Current semantics grounding

R4R12 is designed against current Linux/Git semantics verified during preparation.

Current `openat2(2)` specifies:

```text
RESOLVE_NO_XDEV = disallow traversal of mount points, including bind mounts
crossing such a boundary = EXDEV
```

Current `statfs(2)` defines:

```text
PROC_SUPER_MAGIC = 0x9fa0
SYSFS_MAGIC       = 0x62656572
NSFS_MAGIC        = 0x6e736673
EXT4_SUPER_MAGIC  = 0xef53
```

Current `statmount(2)` exposes independent fields for:

```text
mount basics
filesystem type
mount namespace ID
mount options
filesystem option array
superblock source
mount uid/gid mappings
supported field mask
```

Current ext4 documentation states:

```text
barrier=0 / nobarrier disables JBD write barriers
barrier=1 / barrier enables them
write barriers enforce proper on-disk ordering of journal commits
write barriers make volatile disk write caches safe to use
```

Current ext4 source implements:

```text
Opt_barrier   -> set EXT4_MOUNT_BARRIER
Opt_nobarrier -> clear EXT4_MOUNT_BARRIER
```

Current ext4 full runtime options interface `/proc/fs/ext4/<devname>/options` is produced by `ext4_seq_options_show()`, which invokes `_ext4_show_options(..., nodefs=1)`. Under `nodefs=1`, current option values are emitted rather than omitting values merely because they equal per-superblock defaults.

Current ext4 source also exposes runtime states including:

```text
rw / ro
data=journal / data=ordered / data=writeback
barrier / nobarrier
emergency_ro
shutdown
```

Current ext4 sysfs `journal_task` returns `<none>` when no journal is attached and otherwise returns the journal task PID.

Current ext4 sysfs exposes `errors_count` from the superblock error counter.

Current Git 2.55 semantics relied on by R4R11 remain:

```text
loose-object mtime is prune/freshness state
gc.auto=0 disables automatic gc heuristics
maintenance.auto=false disables command-triggered automatic maintenance
```

Authoritative implementation references checked during preparation include:

```text
https://man7.org/linux/man-pages/man2/openat2.2.html
https://man7.org/linux/man-pages/man2/statfs.2.html
https://man7.org/linux/man-pages/man2/statmount.2.html
https://cdn.kernel.org/doc/html/latest/admin-guide/ext4.html
https://github.com/torvalds/linux/blob/master/fs/ext4/super.c
https://github.com/torvalds/linux/blob/master/fs/ext4/sysfs.c
https://github.com/torvalds/linux/blob/master/Documentation/filesystems/ext4/super.rst
https://github.com/git/git/blob/v2.55.0/object-file.c
https://github.com/git/git/blob/v2.55.0/builtin/prune.c
```

These are design groundings, not ambient runtime assumptions.

## 11. PR #137 F001 correction — AUTHENTIC_CURRENT_TASK_PROCFS_V1

R4R12 does not trust `/proc/self` as an authority source.

The profile begins by opening exactly `/proc` itself:

```text
open("/proc", O_PATH|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC)
```

Retain this descriptor for the whole effect interval.

Require:

```text
fstatfs(proc_root_fd).f_type = PROC_SUPER_MAGIC
statx(proc_root_fd, "", AT_EMPTY_PATH, STATX_MNT_ID_UNIQUE) succeeds
proc_mount_id = exact request-bound unique mount ID
statmount(proc_mount_id) reports fs_type = "proc"
```

If the exact proc mount cannot be identified, V12 is `BLOCKED`.

A procfs-looking path on any other filesystem is invalid.

## 12. Bind the procfs instance to the actual current task

A genuine procfs mounted for another PID namespace is not sufficient.

Obtain kernel values directly:

```text
tgid_syscall = getpid()
tid_syscall  = gettid()
```

From the held proc root, inspect the final `thread-self` directory entry without following it.

Require:

```text
entry type = symlink
entry statx mount ID = proc_mount_id
readlinkat(proc_root_fd, "thread-self") =
    "<tgid_syscall>/task/<tid_syscall>"
```

The target is parsed as ASCII decimal components only, with no sign, leading `+`, dot component, slash injection, overflow, or alternate form.

If the genuine procfs `thread-self` target does not equal the direct syscall PID/TID pair, this procfs instance is not accepted as the current-task authority source.

This closes the case where a genuine procfs instance belongs to a different PID namespace.

## 13. Descriptor-relative numeric current-task path

After the `thread-self` equality proof, do not follow `thread-self` for authority reads.

Construct the exact relative numeric paths from the syscall values:

```text
<tgid>/
<tgid>/task/<tid>/
```

Open them from held `proc_root_fd` using `openat2()` with:

```text
RESOLVE_BENEATH
RESOLVE_NO_XDEV
RESOLVE_NO_SYMLINKS
```

and `O_PATH|O_DIRECTORY|O_CLOEXEC`.

Require every opened component to have:

```text
mount ID = proc_mount_id
filesystem = procfs
expected file type
```

`RESOLVE_NO_XDEV` is security-mandatory here. An `EXDEV` result is `BLOCKED`, not a compatibility fallback.

This rule rejects:

```text
bind-mounted numeric process directory
bind-mounted task directory
submount on ns
file bind mount on ns/user
file bind mount on uid_map
file bind mount on gid_map
file bind mount on status
any unreviewed mount crossing beneath the authority path
```

## 14. Current-task status and credential source

From the authenticated current thread/process directories, read `status` through held-fd, no-cross-mount, no-symlink resolution.

Require the source object itself to remain on `proc_mount_id`.

Cross-check the kernel direct-syscall credential values with authenticated status fields.

At minimum bind:

```text
Uid: real effective saved fs
Gid: real effective saved fs
Groups:
CapInh
CapPrm
CapEff
CapBnd
CapAmb
NoNewPrivs
NSpid / process identity fields needed to confirm current task
```

Direct syscall and authenticated procfs values must agree where they overlap.

A value mismatch is `BLOCKED`, not normalized.

## 15. LINUX_INITIAL_USER_NAMESPACE_V2

V2 preserves R4R11's semantic values but obtains them only through `AUTHENTIC_CURRENT_TASK_PROCFS_V1`.

From the authenticated current thread `ns` directory, inspect `ns/user` without following it across a mount.

Require:

```text
source entry = symlink on exact proc_mount_id
readlinkat(ns_dir_fd, "user") = "user:[4026531837]"
```

where:

```text
USER_NS_INIT_INO = 4026531837 = 0xEFFFFFFD
```

The symlink target string is accepted only because its source entry has already been proven to be the genuine current-thread procfs namespace entry.

No arbitrary namespace-file path and no bind-mounted namespace file may substitute for this source.

## 16. Authenticated uid_map / gid_map

Read exact raw bytes from authenticated numeric current-process paths:

```text
<tgid>/uid_map
<tgid>/gid_map
```

Require both files to remain on `proc_mount_id` and to be genuine procfs regular pseudo-files reached with `RESOLVE_NO_XDEV|RESOLVE_BENEATH|RESOLVE_NO_SYMLINKS`.

Require the parsed semantic maps to contain exactly one range each:

```text
uid_map = (inside_start=0, outside_start=0, length=4294967295)
gid_map = (inside_start=0, outside_start=0, length=4294967295)
```

Store both raw bytes and parsed tuple sets in the physical prestate.

Any extra range, partial map, remap, unreadability, source mount drift, or raw-source ambiguity is `BLOCKED`.

## 17. Authenticated mount-namespace identity

The current mount namespace identity is also derived through the authenticated current-thread procfs path.

Inspect:

```text
<tgid>/task/<tid>/ns/mnt
```

Require the source symlink to be on `proc_mount_id`, and record the exact kernel-generated `mnt:[<ns_inode>]` target.

Do not use an unverified `/proc/self/ns/mnt` path.

R4R12 no longer depends on `/proc/self/mountinfo` as an authority source for the repository mount. Repository mount identity is established through `statx` + `statmount`.

If mountinfo is used diagnostically, it must be read through the same authenticated numeric current-task procfs path and may not override `statmount`.

## 18. Proc authority physical-prestate record

`ProcAuthorityPreStateV1` records at least:

```text
proc root fstat identity
PROC_SUPER_MAGIC
proc unique mount ID
proc statmount fs type and mount identity
getpid value
gettid value
raw thread-self target
numeric process-dir identity
numeric thread-dir identity
raw authenticated status bytes + digest
raw authenticated uid_map bytes + parsed map + digest
raw authenticated gid_map bytes + parsed map + digest
raw authenticated ns/user target
raw authenticated ns/mnt target
source mount ID for every authority entry
```

Every field is request-bound.

Revalidation is mandatory at:

```text
request creation
admission
FinalEffectGateV12
immediately before pre-ref object preparation
immediately before ref CAS
post-effect verification
```

Any source mount change, task-link change, authority path crossing, or unreadability is `PROC_AUTHORITY_STATE_UNCERTAIN` or `BLOCKED` before commitment.

## 19. LINUX_EXECUTION_CREDENTIAL_STATE_V2

V2 preserves R4R11 credential constraints and adds authenticated-source cross-checking.

Bind and revalidate:

```text
ruid
euid
suid
fsuid
rgid
egid
sgid
fsgid
sorted supplementary groups
CapInh
CapPrm
CapEff
CapBnd
CapAmb
NoNewPrivs
authenticated current-task procfs state digest
initial user namespace state digest
```

Success path requires:

```text
ruid = euid = suid = fsuid = execution_uid
rgid = egid = sgid = fsgid = execution_gid
```

No capability, group, UID/GID, namespace, or NoNewPrivs transition is authorized during the effect.

Capability possession remains execution capability, never Human-decision authority.

## 20. LINUX_NON_IDMAPPED_EXT4_MOUNT_V2

V2 preserves the R4R11 non-ID-mapped requirements and expands the exact `statmount()` query.

Obtain repository mount identity from an authority-root descriptor using `statx` unique mount ID and query exactly that mount.

Request at least:

```text
STATMOUNT_SB_BASIC
STATMOUNT_MNT_BASIC
STATMOUNT_FS_TYPE
STATMOUNT_MNT_NS_ID
STATMOUNT_MNT_UIDMAP
STATMOUNT_MNT_GIDMAP
STATMOUNT_SUPPORTED_MASK
STATMOUNT_MNT_OPTS
STATMOUNT_OPT_ARRAY
STATMOUNT_SB_SOURCE
STATMOUNT_MNT_ROOT
```

Require every requested authority field to be present in the returned mask and supported mask where applicable.

Require:

```text
fs_type = "ext4"
sb_magic = EXT4_SUPER_MAGIC
exact unique mount ID = request-bound mount ID
exact mount namespace ID = request-bound mount namespace ID
MOUNT_ATTR_RDONLY = 0
MOUNT_ATTR_IDMAP = 0
SB_RDONLY = 0
SB_LAZYTIME = 0
mnt_uidmap_num = 0
mnt_gidmap_num = 0
```

No mountinfo-only fallback is authorized.

## 21. Direct block-source narrowing

R4R12 deliberately narrows the supported ext4 source mapping so that the ext4 runtime-state path can be selected without guessing aliases.

Require `statmount()` `sb_source` to have exact form:

```text
/dev/<kernel-devname>
```

where `<kernel-devname>`:

```text
is non-empty
contains only ASCII letters, digits, dot, underscore, plus, or hyphen
contains no slash
contains no dot-dot component
is copied exactly as returned
```

Unsupported examples include:

```text
UUID=...
LABEL=...
/dev/disk/by-...
/dev/mapper/...
relative sources
network/fuse/virtual sources
unresolvable aliases
```

This is a deliberate fail-closed compatibility restriction, not an invitation to canonicalize an alias.

Bind exact `sb_dev_major` and `sb_dev_minor` from `statmount` to the physical prestate.

## 22. PR #137 F002 correction — AUTHENTIC_EXT4_RUNTIME_STATE_V1

Generic `statmount` option output is necessary but not sufficient because filesystem `show_options()` may omit values equal to defaults.

R4R12 therefore requires two exact option views:

```text
A. statmount MNT_OPTS + OPT_ARRAY for the exact reviewed mount
B. authenticated /proc/fs/ext4/<kernel-devname>/options full ext4 runtime view
```

Both raw byte representations and parsed forms are request-bound.

The two views are complementary; neither silently overrides a contradiction in the other.

## 23. Authenticated ext4 proc runtime options

Use the same held `proc_root_fd` from `AUTHENTIC_CURRENT_TASK_PROCFS_V1`.

Construct exactly:

```text
fs/ext4/<kernel-devname>/options
```

Open through `openat2(proc_root_fd, ...)` with:

```text
RESOLVE_BENEATH
RESOLVE_NO_XDEV
RESOLVE_NO_SYMLINKS
```

Require:

```text
all components remain on proc_mount_id
final object is a regular procfs pseudo-file
raw bytes are finite, newline-terminated and parseable under V12 grammar
```

A bind-mounted replacement, directory overmount, or alternate filesystem produces `EXDEV`/mount-ID mismatch and is `BLOCKED`.

## 24. Full ext4 option semantics

The authenticated proc options file is expected to be generated by current ext4 `ext4_seq_options_show()` with the full current-state (`nodefs=1`) view.

V12 parser treats each nonempty line after the initial `rw`/`ro` state as one exact option token.

Require:

```text
rw exactly once
barrier exactly once
nobarrier absent
data=ordered XOR data=journal exactly once
data=writeback absent
journal_async_commit absent
noload absent
abort absent
emergency_ro absent
shutdown absent
dax / dax=always / dax=inode absent
```

`dax=never` is permitted.

If current ext4 emits a semantically equivalent barrier-disabled representation other than the exact currently reviewed forms, it is unknown and therefore `BLOCKED` until separately reviewed.

## 25. Closed option parsing rule

V12 does not implement a substring check.

The parser must:

```text
parse exact newline token boundaries
reject embedded NUL
reject duplicate mutually exclusive tokens
reject conflicting positive/negative forms
reject malformed numeric values
record every token, not only security-interesting tokens
classify every token through a reviewed V12 option table
reject unknown tokens whose semantics could affect durability, ordering, journaling, DAX, recovery, or source mapping
```

The minimum durability-sensitive rejected set includes:

```text
nobarrier
barrier=0 if ever emitted by the reviewed interface
data=writeback
journal_async_commit
noload
abort
emergency_ro
shutdown
dax
dax=always
dax=inode
```

A future ext4 option not present in the reviewed table is not assumed benign.

## 26. Why both statmount and full ext4 proc options are required

`STATMOUNT_MNT_OPTS` and `STATMOUNT_OPT_ARRAY` are mandatory because PR #137 identified their omission as part of the durability gap.

The authenticated ext4 proc full-state view is additionally mandatory because current ext4 normal `show_options()` may omit options equal to per-superblock defaults.

The ext4 on-disk default mount-options field can itself encode `EXT4_DEFM_NOBARRIER`.

Therefore:

```text
absence of "nobarrier" from a normal nondefault-only option string != proof that barriers are active
```

The full `nodefs=1` ext4 runtime view closes that omission class under the supported current-kernel profile.

## 27. Authenticated ext4 sysfs runtime state

R4R12 additionally requires a genuine ext4 sysfs state source so the durability profile does not silently accept a no-journal or already-error-recorded filesystem.

Open exactly `/sys`:

```text
O_PATH|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC
```

Require:

```text
fstatfs(sys_root_fd).f_type = SYSFS_MAGIC
unique sysfs mount ID bound
statmount reports fs_type = "sysfs"
```

Open:

```text
fs/ext4/<kernel-devname>/
```

through `openat2()` with:

```text
RESOLVE_BENEATH
RESOLVE_NO_XDEV
RESOLVE_NO_SYMLINKS
```

Every authority file must remain on the exact authenticated sysfs mount.

## 28. Journal presence and error-state gate

From authenticated ext4 sysfs require:

```text
journal_task != "<none>\n"
journal_task parses as a positive decimal PID
authenticated errors_count parses exactly as unsigned decimal zero
```

If the journal is absent, V12 is unsupported.

If ext4 reports a recorded filesystem error, V12 is unsupported until a separately authorized recovery/administrative process establishes a fresh supported state.

V12 does not clear ext4 errors or remount the filesystem.

## 29. EXT4_BARRIERED_FSYNC_DURABILITY_V1

The supported durability contract is exactly:

```text
filesystem = ext4
mount writable
journal present
current ext4 runtime option = barrier
current ext4 runtime option != nobarrier
data mode = ordered or journal
journal_async_commit = absent
noload = absent
abort/emergency_ro/shutdown = absent
SB_LAZYTIME = 0
ID-mapped mount = false
ext4 errors_count = 0
all authority file/dir fsync calls required by the effect return success
all option/provenance state remains unchanged through commitment
```

Battery-backed storage is not used as an alternate proof path.

A `nobarrier` filesystem is simply unsupported by V12 even if an administrator believes the storage cache is safe.

No block-device cache setting is changed by V12.

## 30. Durability claim boundary

R4R12's durability claim is the kernel/filesystem contract under the exact reviewed barrier-enabled ext4 configuration and successful synchronization syscalls.

It does not claim to defeat:

```text
hardware/firmware that falsely acknowledges durable flush/FUA completion
malicious privileged kernel modification
physical media failure after acknowledged durable completion
external administrator intentionally changing mount/storage policy mid-effect
```

However, configuration and state that the kernel exposes to userspace are not excluded as “hardware.” They are bound and checked.

Any observed:

```text
fsync error
sync-related EIO/EROFS
mount becoming read-only
ext4 emergency_ro/shutdown
ext4 errors_count becoming nonzero
barrier state change
option-state change
mount-ID/source change
```

prevents `DURABLY_REF_COMMITTED_COMPLETE` and is classified as durability uncertainty or block according to whether commitment may already have happened.

## 31. Barrier runtime caveat is explicit

Current ext4 documentation notes that JBD can disable barriers after a barrier-write error and emit a warning.

R4R12 does not silently redefine that private kernel transition as impossible.

The implementation must treat any filesystem I/O error surfaced to the bounded operation, any ext4 recorded error-state change, any read-only/emergency/shutdown transition, or any configured barrier-state drift as durability failure/uncertainty.

The brief does not authorize scraping untrusted logs as a substitute for kernel state.

An independent R4R12 review must determine whether the exposed runtime contract is sufficient for the claimed bounded durability class; ambiguity remains fail-closed at review time.

## 32. Ext4 durability physical-prestate record

`Ext4DurabilityPreStateV1` records at least:

```text
repository unique mount ID
mount namespace ID
sb_dev_major
sb_dev_minor
exact sb_source
exact mount root
exact mnt_attr
exact sb_flags
statmount supported mask
raw MNT_OPTS bytes
raw OPT_ARRAY bytes + exact token array
full authenticated /proc/fs/ext4/<dev>/options raw bytes
full parsed ext4 option token set
authenticated proc source mount ID
authenticated sysfs source mount ID
journal_task raw bytes + parsed PID
errors_count raw bytes + parsed value
durability profile = EXT4_BARRIERED_FSYNC_DURABILITY_V1
```

This record is Human-request-bound.

Revalidate it at:

```text
request creation
admission
FinalEffectGateV12
immediately before object preparation
immediately before main-ref lock acquisition
immediately before main-ref rename
post-effect verification
```

A changed digest is not normalized.

## 33. LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1 preserved

Repository root and every authority-critical repository directory component still require:

```text
ext4
same exact reviewed repository mount
stable mount namespace
real directory
no nested/bind mount
LINUX_INODE_SEMANTIC_FLAGS_V1 PASS
FS_CASEFOLD_FL = 0
FS_ENCRYPT_FL = 0
FS_IMMUTABLE_FL = 0
FS_APPEND_FL = 0
FS_DIRSYNC_FL = 0
FS_SYNC_FL = 0
FS_NOCOW_FL = 0
FS_DAX_FL = 0
FS_VERITY_FL = 0
FS_PROJINHERIT_FL = 0
```

R4R12 nests `EXT4_BARRIERED_FSYNC_DURABILITY_V1` under this repository namespace profile.

## 34. LINUX_INODE_SEMANTIC_FLAGS_V1 preserved

Mandatory exact checks remain:

```text
FS_IOC_GETFLAGS
FS_IOC_FSGETXATTR
required statx semantic attributes
```

Allowed inode flags remain exactly:

```text
regular file: subset of {FS_EXTENT_FL}
directory: subset of {FS_EXTENT_FL, FS_INDEX_FL}
```

All other returned inode flag bits are unsupported.

`fsx_xflags`, `fsx_extsize`, `fsx_projid`, and `fsx_cowextsize` remain zero.

Required `statx` semantic attributes remain supported and absent:

```text
IMMUTABLE
APPEND
ENCRYPTED
VERITY
DAX
```

## 35. POSIX metadata profile preserved

Exact modes remain:

```text
repository root directory                          = 0755
.git directory                                     = 0755
.git/objects directory                             = 0755
.git/objects/info directory if present             = 0755
.git/objects/pack directory if present             = 0755
.git/refs directory                                = 0755
.git/refs/heads directory                          = 0755
.git/logs directory                                = 0755
.git/logs/refs directory                           = 0755
.git/logs/refs/heads directory                     = 0755
refs/heads/main                                    = 0644
logs/refs/heads/main if present/new                 = 0644
.git/index                                         = 0644
canonical scene filesystem target                  = 0644
.scriptops/decision-log.ndjson                     = 0644
new loose-object final file                        = 0444
new canonical loose-object fanout directory        = 0755
V12 object staging root                            = 0700
staging temporary object file before final chmod   = 0600
```

Also require exact request-bound uid/gid, empty arbitrary xattrs, mode-only POSIX ACL, no default ACL on writable authority directories, and no setuid/setgid/sticky bits.

The effect process uses exactly:

```text
umask = 0077
```

## 36. HUMAN_BOUND_LOOSE_OBJECT_MTIME_V1 preserved

The exact Human-bound loose-object retention timestamp remains:

```text
mtime_iso8601 = 2038-01-18T00:00:00.000000000Z
mtime_tv_sec  = 2147385600
mtime_tv_nsec = 0
```

Runtime applicability still requires:

```text
CLOCK_REALTIME < 2147385600
```

at request creation, admission, FinalEffectGateV12, and immediately before mtime sealing.

No wall-clock TTL is introduced for Human-decision evidence.

## 37. Loose-object mtime seal preserved

Every canonical loose representation in `new_object_closure` remains sealed, including:

```text
newly staged/installed object
pre-existing exact loose object
exact concurrent RENAME_NOREPLACE EEXIST winner
```

For existing/winner leaf:

```text
open no-follow through held fanout fd
verify exact object/security/topology/durability profile
futimens(atime=UTIME_OMIT, mtime=2147385600.0)
verify exact mtime
fsync(file) AFTER mtime mutation
reopen and verify
```

No other existing object metadata normalization is authorized.

## 38. BOUND_OBJECT_STAGING_NAMESPACE_V2 preserved

Exact staging root remains:

```text
.git/.x1b-stage-v11-<request_digest>
```

R4R12 intentionally preserves the already-Human-visible V11 staging namespace format because PR #137 did not reject its naming or residue semantics. The V12 request schema binds this preserved profile explicitly.

Global negative census remains:

```text
zero raw .git entries whose basename starts with ".x1b-stage-v"
```

before request creation, admission, gate, and staging creation.

No auto-cleanup is authorized.

## 39. Staging fanout and object ordering preserved

New fanout:

```text
create staged 0700
open no-follow
fchmod 0755
verify final metadata + V12 repository durability profile
fsync staged directory after final metadata
RENAME_NOREPLACE -> canonical .git/objects/<xx>
fsync .git/objects
fsync staging root
reopen canonical fanout and verify
```

New staged object:

```text
create 0600
write exact zlib stream
reread/verify canonical object/OID
fchmod 0444
futimens exact V11/V12-preserved sentinel
verify final metadata + mtime + V12 repository durability profile
fsync file AFTER final metadata/mtime
RENAME_NOREPLACE -> canonical fanout leaf
fsync destination fanout
fsync source staging root
reopen canonical leaf and verify
```

No hard-link installation is permitted.

## 40. COMPLETE_LOCAL_OBJECT_STORE_V4 preserved under V12 durability

Reject at least:

```text
shallow repository
grafts
replacement refs
partial clone
promisor configuration/promisor sidecars
lazy fetch requirement
objects/info/alternates
caller object-directory / alternate injection
external common object directory
symlinked primary objects directory
nested/bind-mounted object store
ID-mapped reviewed repository mount
noninitial caller user namespace
unauthenticated proc authority source
casefolded authority directory
unsupported inode semantic flags
unsupported pack metadata topology
unexpected .x1b-stage-v* residue
unsupported ext4 durability state
```

For every `new_object_closure` member before ref commitment require:

```text
physically contained canonical loose representation
exact object bytes/OID
exact mode/uid/gid/nlink/security metadata
exact V12 userns/mount semantics
exact Human-bound mtime sentinel
file fsync completed after final mtime/security metadata
canonical parent namespace fsync completed
EXT4_BARRIERED_FSYNC_DURABILITY_V1 still exact
```

Equivalent packed objects do not remove the required canonical loose representation.

## 41. SINGLE_WORKTREE_REAL_GITDIR_V1 preserved

Required:

```text
repository root = exact canonical physical directory R
R/.git = real directory, not symlink/gitfile/redirect
absolute Git dir = R/.git
Git common dir = R/.git
Git worktree top level = R
repository non-bare
.git/worktrees absent
core.worktree absent
extensions.worktreeConfig absent/false
```

Entire repository authority closure must pass V12 namespace, inode, userns/mount, and ext4 durability profiles.

## 42. PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1 preserved

Required:

```text
HEAD = regular 0644 exact bytes "ref: refs/heads/main\n"
refs = real 0755 directory
refs/heads = real 0755 directory
refs/heads/main = direct regular single-link 0644 loose ref
packed-refs contains no refs/heads/main
main.lock absent before acquisition
core.preferSymlinkRefs absent/false
exact uid/gid/mode-only metadata
same reviewed non-ID-mapped ext4 mount
byte-exact case-sensitive hierarchy
EXT4_BARRIERED_FSYNC_DURABILITY_V1 exact
```

## 43. ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V3 preserved under V12

Acquire `refs/heads/main.lock` descriptor-relative with:

```text
O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC
initial mode 0600
```

Then:

```text
repeat old-main / packed-main / hierarchy proof
write exact effect SHA + LF
reread exact bytes
fchmod 0644
verify POSIX/Linux/userns/mount/ext4-durability metadata
fsync main.lock AFTER final metadata
reread old main exact request base + LF
revalidate packed-main absence + hierarchy
revalidate authenticated proc/current-task state
revalidate repository mount + ext4 runtime durability state
atomic same-directory rename main.lock -> main
fsync held refs/heads directory
reopen final main no-follow and verify
```

No Git ref writer is permitted.

## 44. CLOSED_RAW_TREE_REWRITE_V1 preserved

Raw parent-tree bytes are parsed and reconstructed in memory.

Only tracked changed paths remain:

```text
scenes/<scene_id>.fountain
.scriptops/decision-log.ndjson
```

Every unrelated semantic tree entry is preserved exactly.

Tracked effect modes remain `100644`.

## 45. CLOSED_RAW_COMMIT_OBJECT_V1 preserved

Effect commit contains only exact:

```text
tree
parent
author
committer
```

Message:

```text
scriptops x1b: accept <scene_id>\n
```

Identity/time remain deterministic from Human-bound request state.

No Git commit writer is permitted.

## 46. FULL_SINGLE_FILE_INDEX_V1 preserved

Canonical `.git/index` prestate remains:

```text
regular single-link mode 0644
exact uid/gid + V12 metadata
DIRC
version exactly 2
valid SHA-1 trailer
canonical entries
stage = 0
extended flag = 0
no extensions
semantic (path,mode,oid) set exactly raw parent tree
```

Split index, sparse index, fsmonitor, untracked cache, and all optional extensions remain unsupported.

## 47. Shared-index closure preserved

Under byte-exact `.git` namespace require:

```text
zero raw entries whose basename starts with "sharedindex."
core.splitIndex absent/false
all splitIndex.* config absent
GIT_INDEX_FILE stripped
```

No authority-critical Git command reads or writes the canonical index before the raw replacement step.

## 48. CLOSED_FULL_INDEX_V2_REWRITE_V1 preserved

Final extension-free index-v2 bytes are derived entirely in memory from exact prestate plus derived new tree.

Existing entries preserve exact stat-cache fields and assume-valid bit; changed OID/mode follow the new tree.

New entries use zero stat-cache fields.

Trailing index SHA-1 is recomputed exactly.

## 49. ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1 preserved under V12 durability

After durable ref commitment:

```text
require index.lock absent
require no sharedindex.*
acquire .git/index.lock 0600
reread exact Human-bound index prestate
write exact derived v2 bytes
reread/validate checksum/semantics
fchmod 0644
verify V12 metadata + repository durability profile
fsync index.lock AFTER final metadata
atomic rename -> index
fsync .git
reopen/verify exact final index
require no sharedindex.*
```

`GIT_REAL_INDEX_MUTATING_COMMAND = NONE`.

## 50. Reflog and worktree projections preserved

Only after normal durable physical main-ref commitment:

```text
DETERMINISTIC_MAIN_REFLOG_PROJECTION_V2
ALIAS_SAFE_WORKTREE_PROJECTION_V2
```

retain the exact prior ordering:

```text
prove prestate
create private temp 0600
write final bytes
reread
fchmod 0644
verify V12 metadata/durability profile
fsync temp after final metadata
atomic descriptor-relative rename
fsync parent
reopen exact final and verify
```

No in-place decision-log append is used.

## 51. Hook, replacement-ref, and Git subprocess closure preserved

`NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1` remains mandatory.

V12 still has:

```text
GIT REF WRITER = NONE
GIT PRIMARY OBJECT WRITER = NONE
GIT REAL INDEX WRITER = NONE
```

Every authority-critical Git subprocess remains read-only and uses the previously frozen sanitized profile including:

```text
LC_ALL=C
TZ=UTC
GIT_NO_REPLACE_OBJECTS=1
GIT_NO_LAZY_FETCH=1
GIT_CONFIG_NOSYSTEM=1
GIT_CONFIG_SYSTEM=/dev/null
GIT_CONFIG_GLOBAL=/dev/null
GIT_TERMINAL_PROMPT=0
GCM_INTERACTIVE=never
GIT_PROTOCOL_FROM_USER=0
--no-replace-objects
--no-lazy-fetch
-c core.hooksPath=<verified empty private hook dir>
-c core.fsmonitor=false
-c core.splitIndex=false
-c commit.gpgSign=false
-c credential.helper=
-c core.sharedRepository=false
-c gc.auto=0
-c maintenance.auto=false
```

No V12 durability claim relies on Git mutating the repository.

## 52. PhysicalPreStateV12

Request-time physical prestate digest covers at least:

```text
repository root
candidate/impact/target parent components
.git
.git/objects
objects/info and pack if present
.git/refs
.git/refs/heads
refs/heads/main
.git/logs hierarchy
main reflog if present
.git/index
sharedindex negative census
.x1b-stage-v* negative census
AUTHENTIC_CURRENT_TASK_PROCFS_V1 record
LINUX_INITIAL_USER_NAMESPACE_V2 record
LINUX_EXECUTION_CREDENTIAL_STATE_V2 record
LINUX_NON_IDMAPPED_EXT4_MOUNT_V2 record
AUTHENTIC_EXT4_RUNTIME_STATE_V1 record
EXT4_BARRIERED_FSYNC_DURABILITY_V1 record
```

Each repository inode record retains the V10/V11 mode/uid/gid/nlink/xattr/ACL/inode-flag/statx fields.

No omitted provenance or durability field is interpreted as benign.

## 53. PresentedMaterialEffectV12

Closed schema includes at least:

```text
PresentedMaterialEffectV12 = {
  "schema_version": "scriptops-x1b-presented-material-effect/v12",
  "repository": "FJ899/scriptops",
  "scene_id": <exact scene ID>,
  "candidate_path": <exact repo-relative path>,
  "candidate_file_sha256": <exact digest>,
  "execution_identity": {
    "uid": <exact uid>,
    "gid": <exact gid>,
    "umask": "0077",
    "credential_profile": "LINUX_EXECUTION_CREDENTIAL_STATE_V2",
    "user_namespace_profile": "LINUX_INITIAL_USER_NAMESPACE_V2",
    "proc_authority_profile": "AUTHENTIC_CURRENT_TASK_PROCFS_V1"
  },
  "filesystem_authority": {
    "namespace_profile": "LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1",
    "inode_semantic_profile": "LINUX_INODE_SEMANTIC_FLAGS_V1",
    "mount_mapping_profile": "LINUX_NON_IDMAPPED_EXT4_MOUNT_V2",
    "runtime_state_profile": "AUTHENTIC_EXT4_RUNTIME_STATE_V1",
    "durability_profile": "EXT4_BARRIERED_FSYNC_DURABILITY_V1",
    "filesystem_type": "ext4",
    "casefold_allowed": false,
    "idmapped_mount_allowed": false,
    "barrier_required": true,
    "allowed_data_modes": ["ordered", "journal"]
  },
  "canonical_scene_effect": {
    "target_path": "scenes/<scene_id>.fountain",
    "before": <CanonicalPreStateV1>,
    "after_file_sha256": <accepted canonical SHA256>,
    "git_mode_after": "100644",
    "filesystem_mode_after": "0644",
    "projection_profile": "ALIAS_SAFE_WORKTREE_PROJECTION_V2"
  },
  "decision_log_effect": {
    "target_path": ".scriptops/decision-log.ndjson",
    "append_count": 1,
    "record_schema_version": "scriptops-x1b-decision-record/v12",
    "record_result": "REF_COMMITTED",
    "append_semantics": "EXACT_PRIOR_BYTES_PLUS_ONE_CANONICAL_RECORD_PLUS_LF",
    "git_mode_after": "100644",
    "filesystem_mode_after": "0644",
    "projection_profile": "ALIAS_SAFE_WORKTREE_PROJECTION_V2"
  },
  "local_git_effect": {
    "target_ref": "refs/heads/main",
    "ref_before": <request base>,
    "commit_count": 1,
    "commit_message": "scriptops x1b: accept <scene_id>",
    "git_semantics_profile": "GIT_2_55_X1B_V1",
    "ref_storage_format": "files",
    "object_store_profile": "COMPLETE_LOCAL_OBJECT_STORE_V4",
    "object_install_profile": "ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V4",
    "object_staging_profile": "BOUND_OBJECT_STAGING_NAMESPACE_V2",
    "loose_object_mtime_profile": "HUMAN_BOUND_LOOSE_OBJECT_MTIME_V1",
    "loose_object_mtime_tv_sec": 2147385600,
    "loose_object_mtime_tv_nsec": 0,
    "durability_order_profile": "FSYNC_AFTER_FINAL_METADATA_V1",
    "repository_durability_profile": "EXT4_BARRIERED_FSYNC_DURABILITY_V1",
    "index_prestate_profile": "FULL_SINGLE_FILE_INDEX_V1",
    "index_projection_profile": "CLOSED_FULL_INDEX_V2_REWRITE_V1",
    "index_install_profile": "ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1",
    "raw_object_profile": "NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2",
    "hook_profile": "NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1",
    "commit_object_profile": "CLOSED_RAW_COMMIT_OBJECT_V1",
    "ref_cas_profile": "ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V3",
    "crash_durability_profile": "CRASH_DURABLE_OBJECT_REF_INDEX_V7",
    "success_commitment_profile": "ALIAS_SAFE_MAIN_REF_COMMITMENT_V8",
    "effect_transport_profile": "REF_CAS_FIRST_ALIAS_SAFE_RAW_GIT_METADATA_V10",
    "git_ref_mutating_command": "NONE",
    "git_primary_object_mutating_command": "NONE",
    "git_real_index_mutating_command": "NONE",
    "exact_changed_paths": [
      "scenes/<scene_id>.fountain",
      ".scriptops/decision-log.ndjson"
    ]
  }
}
```

## 54. HumanDecisionRequestBindingV12

```text
HumanDecisionRequestBindingV12 = {
  "schema_version": "scriptops-x1b-human-decision-request/v12",
  "repository": "FJ899/scriptops",
  "repository_head_at_request": <40 lowercase hex>,
  "repository_ref_at_request": "refs/heads/main",
  "request_created_at": <exact timestamp>,
  "execution_uid": <exact uid>,
  "execution_gid": <exact gid>,
  "proc_authority_state": <ProcAuthorityPreStateV1>,
  "execution_credential_state": <LinuxExecutionCredentialStateV2>,
  "user_namespace_state": <LinuxInitialUserNamespaceStateV2>,
  "mount_mapping_state": <LinuxNonIdmappedExt4MountStateV2>,
  "ext4_runtime_state": <AuthenticExt4RuntimeStateV1>,
  "ext4_durability_state": <Ext4DurabilityPreStateV1>,
  "task_id": <exact task>,
  "scene_id": <exact scene>,
  "candidate_path": <exact path>,
  "candidate_file_sha256": <exact digest>,
  "impact_report_path": <exact path>,
  "impact_report_sha256": <exact digest>,
  "canonical_target": "scenes/<scene_id>.fountain",
  "canonical_ref": "refs/heads/main",
  "main_reflog_prestate": <MainReflogPreStateV2>,
  "full_index_prestate": <FullIndexPreStateV1>,
  "physical_git_metadata_prestate_digest": <exact digest>,
  "loose_object_mtime_profile": "HUMAN_BOUND_LOOSE_OBJECT_MTIME_V1",
  "loose_object_mtime_tv_sec": 2147385600,
  "loose_object_mtime_tv_nsec": 0,
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect": <PresentedMaterialEffectV12>
}
```

```text
request_digest = sha256_canonical(binding)
decision_request_id = "x1b:" + request_digest
```

## 55. Proposal PR and V12 Human marker

Proposal remains one-file and acyclic:

```text
request_path = decisions/x1b/<request_digest>.json
request_branch = decision/x1b/<request_digest>
proposal parent = exact repository_head_at_request
changed set = exactly request_path added
```

Authoritative Human actor remains:

```text
litrgratis-pixel
```

Exact manual GitHub UI APPROVE body:

```text
X1B-HUMAN-DECISION-V12
decision_request_id=<exact x1b:<request_digest>>
decision_request_sha256=<exact request_digest>
why=<Human rationale>
```

Four LF-separated lines, no trailing LF.

V11 or earlier markers are invalid for V12.

## 56. Trusted GitHub evidence and freshness preserved

Public exact-origin GitHub evidence transport, complete review pagination, current-head binding, duplicate ambiguity, active `CHANGES_REQUESTED` handling, no-latest-wins semantics, exact proposal envelope, replay lock, and freshness/supersession rules remain as previously frozen with V12 schema identities.

```text
NO WALL-CLOCK TTL FOR HUMAN REVIEW CURRENTNESS
AGE ALONE != STALE
```

The loose-object mtime profile horizon remains a distinct implementation applicability predicate.

## 57. X1BDecisionRecordV12

Record includes at least:

```text
schema_version = scriptops-x1b-decision-record/v12
result = REF_COMMITTED
result_scope = PHYSICAL_LOOSE_REFS_HEADS_MAIN_POINTS_TO_EXACT_EFFECT_COMMIT
exact request/review/admission/currentness identities
exact scene/candidate/impact identities
ref_before
execution uid/gid + credential state digest
proc authority provenance digest
initial user namespace state digest
non-ID-mapped ext4 mount state digest
ext4 runtime option state digest
ext4 durability state digest
main reflog prestate
full index prestate
canonical before/after digests
presented material effect digest
filesystem_namespace_profile = LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1
inode_semantic_profile = LINUX_INODE_SEMANTIC_FLAGS_V1
proc_authority_profile = AUTHENTIC_CURRENT_TASK_PROCFS_V1
mount_mapping_profile = LINUX_NON_IDMAPPED_EXT4_MOUNT_V2
ext4_runtime_state_profile = AUTHENTIC_EXT4_RUNTIME_STATE_V1
repository_durability_profile = EXT4_BARRIERED_FSYNC_DURABILITY_V1
object_store_profile = COMPLETE_LOCAL_OBJECT_STORE_V4
object_staging_profile = BOUND_OBJECT_STAGING_NAMESPACE_V2
object_install_profile = ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V4
loose_object_mtime_profile = HUMAN_BOUND_LOOSE_OBJECT_MTIME_V1
loose_object_mtime_tv_sec = 2147385600
loose_object_mtime_tv_nsec = 0
durability_order_profile = FSYNC_AFTER_FINAL_METADATA_V1
index profiles from prior accepted brief levels
ref/reflog/worktree profiles from prior accepted brief levels
crash_durability_profile = CRASH_DURABLE_OBJECT_REF_INDEX_V7
success_commitment_profile = ALIAS_SAFE_MAIN_REF_COMMITMENT_V8
canonical_instance_scope = LOCAL_AUTHENTIC_PROC_INITIAL_USERNS_NONIDMAPPED_BARRIERED_EXT4_MAIN_OBJECT_DB_FULL_INDEX_WORKTREE_DECISION_LOG_REFLOG_V12
```

The record still says `REF_COMMITTED`, not generic success.

## 58. FinalEffectGateV12

Immediately before deterministic record/object derivation, while the same-worktree exclusive X1B lock is held, freshly validate:

```text
exact V12 PR/request/review envelope
Human currentness/conflicts
CompleteReviewSetV12 digest
raw logical main SHA = request base
SINGLE_WORKTREE_REAL_GITDIR_V1
AUTHENTIC_CURRENT_TASK_PROCFS_V1
LINUX_INITIAL_USER_NAMESPACE_V2
LINUX_EXECUTION_CREDENTIAL_STATE_V2
LINUX_NON_IDMAPPED_EXT4_MOUNT_V2
AUTHENTIC_EXT4_RUNTIME_STATE_V1
EXT4_BARRIERED_FSYNC_DURABILITY_V1
LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1 over full repository authority closure
LINUX_INODE_SEMANTIC_FLAGS_V1 over full repository authority closure
PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1
COMPLETE_LOCAL_OBJECT_STORE_V4
FSYNC_AFTER_FINAL_METADATA_V1 capability
CLOCK_REALTIME < 2147385600
FULL_SINGLE_FILE_INDEX_V1 exact
no sharedindex.*
zero .x1b-stage-v* entries
core.splitIndex absent/false
MainReflogPreStateV2 exact
Git 2.55.x
files ref format
NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2
NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1
zero refs/replace
raw parent commit/tree
candidate/impact/canonical prestate
accepted preview
PresentedMaterialEffectV12
replay state
raw full-index semantic tree = raw parent tree
verified empty hook directory
renameat2(RENAME_NOREPLACE) supported
openat2 provenance controls supported
```

After gate:

```text
no user interaction
no network
no sleep/wait unrelated to required kernel I/O completion
no proposal/review mutation
no untrusted subprocess
no namespace transition
no credential/capability/group transition
no mount/remount transition by V12
no ext4 option mutation by V12
no Git ref mutation
no Git primary object mutation
no Git real-index read or mutation
```

## 59. Exact local effect sequence V12

With X1B lock held after FinalEffectGateV12:

```text
A. re-prove authenticated current-task procfs,
   initial userns, exact credentials,
   non-ID-mapped ext4 mount,
   authenticated ext4 runtime state,
   barriered ext4 durability,
   byte-exact namespace, inode semantics,
   complete-local-store, ref/reflog/index profiles,
   zero stale staging

B. construct X1BDecisionRecordV12 bytes in memory

C. construct exact accepted-scene and decision-log payloads in memory
   compute exact blob canonical bytes/OIDs

D. execute CLOSED_RAW_TREE_REWRITE_V1
   derive exact affected tree payloads/OIDs
   prove exact two-path semantic delta

E. construct exact CLOSED_RAW_COMMIT_OBJECT_V1 in memory
   compute exact effect commit SHA

F. derive exact new_object_closure tuples

G. create exact request-bound staging root
   verify V12 repository metadata/durability profile
   fsync staging root and .git

H. for each missing canonical fanout:
   build/finalize/fsync under staging root
   RENAME_NOREPLACE into .git/objects/<xx>
   fsync objects + staging root
   verify canonical fanout

I. for each new_object_closure member:
   if exact canonical loose leaf exists:
       verify exact object/security/topology
       seal mtime to 2147385600.0
       fsync leaf after mtime
   else:
       build staged object
       fchmod 0444
       set mtime 2147385600.0
       verify
       fsync file after final metadata
       RENAME_NOREPLACE into canonical fanout
       on EEXIST verify + mtime-seal winner
       fsync destination fanout + source staging root
   verify exact canonical leaf + sentinel mtime

J. verify every closure member exact/contained/durable/mtime-sealed
   require staging root empty
   fsync staging root
   rmdir exact staging root
   fsync .git
   require zero .x1b-stage-v* entries

K. cross-check installed commit/tree/object closure with read-only Git plumbing
   gc.auto=0
   maintenance.auto=false
   no index access

L. derive exact deterministic final raw index bytes in memory

M. final pre-ref checks:
   main exact old SHA
   packed main absent
   authenticated proc/current-task state exact
   initial userns + credentials exact
   repository non-ID-mapped mount exact
   ext4 runtime options exact
   barriered ext4 durability exact
   every closure object exact/contained/durable/mtime-sealed
   no staging residue
   reflog prestate exact
   raw full index exact unchanged
   no sharedindex.*
   hook census empty

N. acquire main.lock descriptor-relative O_EXCL/O_NOFOLLOW
   repeat old-value/topology/provenance/durability proof

O. write exact effect SHA + LF
   fchmod 0644
   verify V12 metadata
   fsync main.lock AFTER final metadata
   final old-main + proc + mount + ext4-durability proof

P. atomic descriptor-relative rename main.lock -> main
   fsync refs/heads
   classify physical ref result

Q. after normal durable ref commitment:
   deterministic main reflog V2

R. project canonical scene through worktree projection V2

S. project decision log through worktree projection V2

T. replace raw canonical full v2 index through ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1

U. verify ref, raw commit/tree/object closure,
   authenticated proc/current-task state,
   initial userns, credentials, non-ID-mapped ext4,
   full ext4 runtime option state, barriered durability,
   byte-exact namespace, inode semantics,
   every closure mtime sentinel,
   zero staging residue, reflog, worktree, full index, zero sharedindex

V. release X1B lock only after final outcome class is determined
```

No canonical worktree, decision-log, reflog, or real-index mutation occurs before physical main-ref commitment.

Object/fanout preparation and mtime sealing may occur before ref commitment and remain truthfully classified as preparation effects.

## 60. CRASH_DURABLE_OBJECT_REF_INDEX_V7

V7 preserves the R4R11 file/directory ordering and adds a prerequisite that every durability barrier is executed while `EXT4_BARRIERED_FSYNC_DURABILITY_V1` remains exact.

Normal durable new fanout requires:

```text
final metadata under staging
staged directory fsync success
EXT4_BARRIERED_FSYNC_DURABILITY_V1 exact
RENAME_NOREPLACE to canonical name
objects directory fsync success
staging-root fsync success
canonical exact reread
ext4 durability state exact after operation
```

Normal durable new object requires:

```text
complete exact object write
final fchmod 0444
exact Human-bound mtime
security/provenance verification
file fsync success AFTER final metadata/mtime
EXT4_BARRIERED_FSYNC_DURABILITY_V1 exact
RENAME_NOREPLACE into canonical fanout
fanout fsync success
staging-root fsync success
canonical exact reread
ext4 durability state exact after operation
```

Normal durable pre-existing/winner mtime sealing requires:

```text
exact object/security/topology proof
exact mtime set
mtime verification
file fsync success AFTER mtime
exact path reread
ext4 durability state exact
```

A successful syscall is necessary but no longer the only durability precondition; the reviewed ext4 runtime state must also remain exact.

## 61. ALIAS_SAFE_MAIN_REF_COMMITMENT_V8

Truthful `REF_COMMITTED` requires:

```text
exact effect object closure physically contained
all closure loose leaves exact + mtime-sealed
all new fanouts/objects durable under V7
zero X1B staging residue at ref commitment
AUTHENTIC_CURRENT_TASK_PROCFS_V1 exact
initial user namespace proof exact
execution credential state unchanged
reviewed mount non-ID-mapped ext4 proof exact
AUTHENTIC_EXT4_RUNTIME_STATE_V1 exact
EXT4_BARRIERED_FSYNC_DURABILITY_V1 exact
byte-exact namespace + inode semantics exact
main physical loose ref = exact effect SHA
main file + refs/heads durability barriers complete
canonical ref hierarchy still resolves to held identities
```

Post-ref reflog/worktree/index remain prerequisites for complete zero exit, not for the narrower truthful `REF_COMMITTED` record scope.

## 62. Outcome classes V12

Implementation must distinguish at least:

```text
DENIED
BLOCKED_PROFILE_HORIZON
BLOCKED_PRE_COMMIT_NO_OBJECT_PREP
BLOCKED_PRE_COMMIT_OBJECT_MTIME_SEALED_ONLY
BLOCKED_PRE_COMMIT_OBJECT_PREPARED_CLEAN
BLOCKED_PRE_COMMIT_BOUND_STAGING_RESIDUE
BLOCKED_PRE_COMMIT_REF_LOCK_RESIDUE
OBJECT_STAGING_STATE_UNKNOWN
OBJECT_RETENTION_METADATA_UNCERTAIN
OBJECT_STORE_DURABILITY_UNCERTAIN
OBJECT_STORE_TOPOLOGY_UNCERTAIN
PROC_AUTHORITY_STATE_UNCERTAIN
USER_NAMESPACE_STATE_UNCERTAIN
MOUNT_IDMAP_STATE_UNCERTAIN
EXT4_RUNTIME_STATE_UNCERTAIN
EXT4_DURABILITY_STATE_UNCERTAIN
FILESYSTEM_SEMANTICS_UNCERTAIN
REF_COMMITTED_DURABILITY_UNCERTAIN
REF_COMMITTED_TOPOLOGY_UNCERTAIN
COMMITMENT_STATE_UNKNOWN
DURABLY_REF_COMMITTED_RECOVERY_REQUIRED
DURABLY_REF_COMMITTED_COMPLETE
```

## 63. Proc authority outcome semantics

```text
PROC_AUTHORITY_STATE_UNCERTAIN:
  one or more proc authority source identities, mount IDs,
  current-task bindings, namespace-link targets, or map/status sources
  cannot be proven exact and current

  if before possible ref commitment:
      no commitment is authorized

  if after possible ref commitment:
      complete success is forbidden and commitment must be classified separately
```

No automatic attempt to “fix” procfs or enter another namespace is authorized.

## 64. Ext4 durability outcome semantics

```text
EXT4_RUNTIME_STATE_UNCERTAIN:
  exact full ext4 option/journal/error state cannot be read or has drifted

EXT4_DURABILITY_STATE_UNCERTAIN:
  barrier/data-mode/journal/error policy or required fsync result
  cannot support the V12 durability claim
```

Before possible ref commitment these block the effect.

After possible ref commitment they prevent a complete-success claim and require physical ref-state classification plus separate recovery if needed.

## 65. Pre-ref preparation truth preserved

Pre-ref failure may leave:

```text
exact unreferenced closure objects/fanouts
exact V12-preserved mtime sentinel applied to pre-existing/winner objects
request-bound staging residue
```

The implementation must never report these as “no filesystem effect”.

No automatic cleanup on restart is authorized.

## 66. No rollback rule preserved

After visible or possible ref commitment:

```text
NO AUTOMATIC HISTORY ROLLBACK
```

Recovery authority remains separate.

## 67. Mandatory regressions — PR #137 F001 proc authority provenance

Future implementation and independent review must attack at least:

```text
/proc not procfs -> BLOCK
/proc genuine procfs for wrong PID namespace -> BLOCK by thread-self/getpid/gettid mismatch
/proc thread-self source overmounted -> BLOCK
/proc numeric current-PID directory hidden by bind/submount -> BLOCK
/proc/<pid>/task hidden by bind/submount -> BLOCK
/proc/<pid>/task/<tid> hidden by bind/submount -> BLOCK
/proc/<pid>/task/<tid>/ns hidden by bind/submount -> BLOCK
/proc/<pid>/task/<tid>/ns/user overmounted with pinned initial-userns file -> BLOCK
/proc/<pid>/uid_map overmounted with regular identity-map text -> BLOCK
/proc/<pid>/gid_map overmounted with regular identity-map text -> BLOCK
/proc/<pid>/status overmounted -> BLOCK
namespace/map/status path crossing any mount boundary -> BLOCK
proc unique mount ID drift -> BLOCK/uncertainty
thread-self target drift -> BLOCK/uncertainty
getpid/gettid mismatch with authenticated proc source -> BLOCK
proc authority unreadable -> BLOCK
```

Positive control must show that a genuine current-task procfs instance is accepted.

## 68. Mandatory regressions — PR #137 F002 ext4 durability

At minimum test:

```text
supported ext4 barrier-enabled data=ordered -> PASS profile gate
supported ext4 barrier-enabled data=journal -> PASS profile gate
ext4 nobarrier -> BLOCK
ext4 barrier=0 equivalent -> BLOCK
per-superblock default NOBARRIER with normal statmount omission -> BLOCK via full proc options
ext4 data=writeback -> BLOCK
ext4 journal_async_commit -> BLOCK
ext4 noload -> BLOCK
ext4 abort -> BLOCK
ext4 emergency_ro -> BLOCK
ext4 shutdown -> BLOCK
ext4 without journal -> BLOCK via journal_task=<none>
ext4 errors_count nonzero -> BLOCK
STATMOUNT_MNT_OPTS unavailable -> BLOCK
STATMOUNT_OPT_ARRAY unavailable -> BLOCK
STATMOUNT_SB_SOURCE unavailable -> BLOCK
normal statmount option view disagrees materially with full ext4 runtime view -> BLOCK
/proc/fs/ext4/<dev>/options overmounted -> BLOCK
/sys not sysfs -> BLOCK
/sys/fs/ext4/<dev> overmounted -> BLOCK
journal_task overmounted -> BLOCK
errors_count overmounted -> BLOCK
sb_source not direct /dev/<kernel-devname> -> BLOCK
ext4 runtime option state drift during effect -> uncertainty/block
ext4 error state becomes nonzero during effect -> uncertainty/block
fsync(file) fails -> durability uncertainty
fsync(parent) fails -> durability uncertainty
mount becomes read-only -> durability uncertainty
```

Battery-backed+nobarrier is intentionally not a supported alternate positive case.

## 69. Mandatory preserved regressions

Also rerun prior attack classes:

```text
child/noninitial user namespace
ID-mapped repository mount
credential/fsuid/fsgid/group/capability drift
casefolded .git/objects/refs/logs/worktree parents
unsupported inode flags/xflags/statx attributes
stale/malformed .x1b-stage-v* residue
crash at every staging fanout/object namespace barrier
loose object hardlink
real refs/heads/main symlink
refs/heads directory symlink
.git gitfile / linked worktree / external common-dir
main hardlink
packed main
packed-refs symlink
core.preferSymlinkRefs=true
parent-directory substitution
.git/objects symlink/outside redirect
objects nested bind mount
alternate/promisor/lazy-fetch escape
replacement refs
commit encoding
configured hooks
ambient identity/time/reflog variables
reflog symlink/hardlink/parent redirect
reflog prestate drift
worktree target hardlink/symlink
split index / link extension / sharedindex.*
raw index corruption/unsupported extensions
post-fchmod/futimens durability ordering
loose-object mtime pruning semantics
freshness/supersession/conflict/replay
Human review author/currentness/body binding
```

R4R12 does not reopen any earlier closed property.

## 70. Required implementation helpers

Expected bounded helpers include conceptually:

```text
canonical JSON/hash/time helpers
trusted GitHub evidence pagination/currentness
admission/replay lock
openat2 exact resolver
procfs root provenance verifier
current-task thread-self/PID/TID binder
procfs numeric-task authority reader
initial user namespace V2 verifier
uid_map/gid_map parser
execution credential V2 binder
sysfs root provenance verifier
statx unique mount-ID verifier
statmount repository mount verifier
ext4 full proc options reader/parser
ext4 sysfs journal/error-state reader
EXT4_BARRIERED_FSYNC_DURABILITY_V1 verifier
FS_IOC_GETFLAGS verifier
FS_IOC_FSGETXATTR verifier
statx semantic-attribute verifier
LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1 walker
held descriptor identity helpers
POSIX mode/uid/gid/xattr/ACL verifier
HUMAN_BOUND_LOOSE_OBJECT_MTIME_V1 sealer
single-worktree real-gitdir verifier
physical loose-main-ref verifier
COMPLETE_LOCAL_OBJECT_STORE_V4 verifier
raw object parser/hasher
closed raw tree rewrite
closed raw commit writer/verifier
BOUND_OBJECT_STAGING_NAMESPACE_V2 manager
ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V4
raw Git index-v2 parser
FULL_SINGLE_FILE_INDEX_V1 verifier
CLOSED_FULL_INDEX_V2_REWRITE_V1 builder
ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1
main reflog prestate binder
DETERMINISTIC_MAIN_REFLOG_PROJECTION_V2
ALIAS_SAFE_WORKTREE_PROJECTION_V2
alias-safe ref CAS V3
staging residue read-only classifier
outcome classifier
post-effect verifier
```

No helper may silently broaden proc source provenance, ext4 source mapping, user namespace, mount mapping, inode, mtime, or durability profiles.

## 71. Documentation obligations

Authority documentation must state at minimum:

```text
current Human route = approve --decision-pr <N> only
direct legacy approve/promotion disabled
canonical effect ref = refs/heads/main
Git ref mutation = NONE
Git primary object mutation = NONE
Git real-index mutation = NONE
supported authority OS = Linux
supported repository filesystem = ext4 only
proc authority = genuine current-task procfs proven descriptor-relative
/proc/self is not accepted as an unverified authority shortcut
proc authority mount crossings / bind substitutions = forbidden
caller user namespace = initial user namespace only
ID-mapped repository mounts = unsupported
statmount proof = mandatory
ext4 source = direct /dev/<kernel-devname> only
STATMOUNT_MNT_OPTS + OPT_ARRAY = mandatory
full /proc/fs/ext4/<dev>/options state = mandatory and authenticated
ext4 journal = mandatory
ext4 barriers = mandatory
nobarrier/barrier=0 = unsupported
data=writeback = unsupported
journal_async_commit = unsupported
ext4 recorded error state = unsupported
casefold authority directories = forbidden
Linux inode semantic flags = explicitly gated
object staging = request-bound .git namespace only
canonical fanout/object names = final-only
new-closure loose-object mtime = exact 2038-01-18 sentinel
pre-existing/winner closure leaves are mtime-sealed before commitment
failure mtime sealing is a truthful preparation side effect
successful pre-ref preparation leaves zero staging residue
failure staging residue blocks future effects and needs separate recovery
final security/mtime metadata precedes file fsync
file and parent fsync success are mandatory
split index unsupported
sharedindex.* forbidden
V12 Human marker required
```

## 72. No new implementation authority

```text
CLEAN BRIEF != IMPLEMENTATION AUTHORITY
REVIEW PASS != IMPLEMENTATION AUTHORITY
REVIEW PASS != HUMAN DECISION
IMPLEMENTATION GREEN != X1B CLOSED
X1B OPEN != V1 AUTHORITY
```

## 73. Next legal step

After this R4R12 brief is durably frozen as exactly one evidence artifact, STOP.

Next legal step:

```text
fresh Human authorization
-> one independent AK-CANON R4R12 implementation-brief review
```

That review may return PASS or NOT PASS.

It must not implement ScriptOps, create Human decision evidence, run positive control, perform canonical effect, recover state, merge, close X1B, authorize V1, release, deploy, or tag.

## 74. R4R12 acceptance checklist for future independent review

A PASS review must establish all of:

```text
PR #137 F001 procfs authority-source provenance blocker addressed
PR #137 F002 ext4 durability mount-option blocker addressed
all prior blockers remain closed
proc root is genuine procfs
procfs instance is bound to actual getpid/gettid current task
thread-self is used only as an authenticated kernel source, not blindly followed
numeric current-task path is descriptor-relative
RESOLVE_NO_XDEV rejects bind/submount substitutions
ns/user source is authenticated current-thread procfs
uid_map/gid_map sources are authenticated current-process procfs
proc source state is request-bound and repeatedly revalidated
initial-userns semantic values remain exact
execution credential state remains exact
statmount exact repository mount proof remains fail-closed
MOUNT_ATTR_IDMAP remains absent
mount uid/gid maps remain zero
STATMOUNT_MNT_OPTS is required and bound
STATMOUNT_OPT_ARRAY is required and bound
full current ext4 runtime option state is independently authenticated
per-superblock NOBARRIER default cannot hide behind omitted normal show_options output
barrier disabled state cannot pass
writeback data mode cannot pass
journal_async_commit cannot pass
journal absence cannot pass
recorded ext4 error state cannot pass
runtime option drift cannot yield complete success
all required fsync calls remain checked
R4R11 mtime correction remains exact
R4R10 user/mount ID-map correction remains exact
R4R9 staging/casefold/inode correction remains exact
V9 raw-index/split-index correction remains exact
ref/reflog/worktree durability corrections remain exact
Human evidence remains separate/current/exact
```

Any ambiguity is NOT PASS.

## 75. Final R4R12 invariant summary

```text
AI PROPOSES != HUMAN DECIDES

V12 HUMAN DECISION EVIDENCE
= separate trusted current GitHub Human review
  bound to exact V12 request + exact presented material effect

V12 KERNEL AUTHORITY SOURCE
= held genuine procfs root
+ PROC_SUPER_MAGIC
+ exact proc mount identity
+ thread-self target == getpid()/task/gettid
+ numeric current-task paths only
+ openat2 RESOLVE_BENEATH|NO_XDEV|NO_SYMLINKS
+ no bind/submount substitution

V12 EXECUTION OWNERSHIP SEMANTICS
= authenticated current-task procfs
+ Linux initial user namespace only
+ full identity uid_map/gid_map
+ exact stable execution credentials
+ exact statmount proof of non-ID-mapped ext4 mount

V12 EXT4 DURABILITY
= exact reviewed ext4 mount
+ STATMOUNT_MNT_OPTS + OPT_ARRAY
+ authenticated full ext4 runtime options
+ journal present
+ rw
+ barrier enabled
+ no nobarrier
+ data=ordered OR data=journal
+ no data=writeback
+ no journal_async_commit
+ no noload/abort/emergency_ro/shutdown
+ zero accepted ext4 error count
+ every required file/dir fsync succeeds

V12 OBJECT PREPARATION
= preserved request-bound staging namespace
+ final-only canonical object/fanout names
+ exact Human-bound loose-object mtime sentinel
+ pre-existing/winner/new closure leaves all mtime-sealed
+ final metadata + mtime -> file fsync -> RENAME_NOREPLACE -> parent fsync
+ staging root durably removed before ref commitment

V12 LOOSE OBJECT RETENTION METADATA
= 2038-01-18T00:00:00Z exactly
= 2147385600.000000000
= Human-bound, not ambient execution time

V12 COMMITMENT
= exact descriptor-relative loose-main replacement
+ authenticated proc/current-task state exact
+ repository ext4 durability state exact
+ final metadata -> file fsync -> rename -> refs/heads fsync

V12 POST-REF PROJECTIONS
= deterministic reflog
+ alias-safe scene/log materialization
+ deterministic extension-free full index-v2 replacement

SPLIT INDEX
= unsupported

sharedindex.*
= forbidden

GIT REF WRITER
= NONE

GIT PRIMARY OBJECT WRITER
= NONE

GIT REAL INDEX WRITER
= NONE

R4R12 BRIEF
= REVIEW TARGET ONLY
```
