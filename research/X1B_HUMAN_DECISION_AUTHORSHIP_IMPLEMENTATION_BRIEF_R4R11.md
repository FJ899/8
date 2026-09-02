# X1B HUMAN DECISION AUTHORSHIP — CLEAN IMPLEMENTATION BRIEF R4R11

Status: `CLEAN R4R11 CORRECTIVE BRIEF / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-02`

## 1. Authority, purpose, and STOP boundary

This document is the self-contained successor to R4R10 after independent AK-CANON review PR #135 returned `NOT PASS`.

It preserves the accepted X1B corrective design and every R4R10 property not rejected by PR #135, while correcting exactly the two blockers frozen by that review:

1. R4R10 bound visible uid/gid, ext4, one mount ID, inode flags, xattrs and ACLs, but did not bind or reject the Linux user-namespace / mount-ID-mapping layer. An ext4 ID-mapped mount or a noninitial caller user namespace could therefore preserve the visible R4R10 checks while the VFS translated ownership, ACL and permission semantics;
2. R4R10 did not bind or deterministically set loose-object mtime. Newly created loose objects inherited ambient execution wall-clock mtime, and pre-existing exact loose winners retained ambient historical mtime, even though Git 2.55 treats loose-object mtime as pruning/freshness state.

R4R11 therefore changes both the execution/mount identity contract and the physical loose-object metadata contract.

New exact profiles:

```text
LINUX_INITIAL_USER_NAMESPACE_V1
LINUX_IDENTITY_MAPPED_EXT4_MOUNT_V1
LINUX_EXECUTION_CREDENTIAL_STATE_V1
HUMAN_BOUND_LOOSE_OBJECT_MTIME_V1
BOUND_OBJECT_STAGING_NAMESPACE_V2
ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V4
COMPLETE_LOCAL_OBJECT_STORE_V4
CRASH_DURABLE_OBJECT_REF_INDEX_V6
ALIAS_SAFE_MAIN_REF_COMMITMENT_V7
REF_CAS_FIRST_ALIAS_SAFE_RAW_GIT_METADATA_V9
```

Preserved exact profiles include:

```text
LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1
LINUX_INODE_SEMANTIC_FLAGS_V1
FSYNC_AFTER_FINAL_METADATA_V1
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

The material effect and authority-relevant runtime identity change again. All authority-critical schemas, request/review markers, admission identities, final-gate identities and records are therefore V11.

This document is an implementation brief only. It authorizes no ScriptOps source mutation, no Human decision PR/review, no live positive control, no canonical screenplay effect, no recovery, no merge, no X1B closure, no Agency Kernel v1, no release, deployment, or tag.

```text
R4R11 BRIEF != IMPLEMENTATION AUTHORITY
R4R11 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R11 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

After durable freeze of this brief, STOP. The next stage is one separately Human-authorized independent AK-CANON R4R11 implementation-brief review.

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

### 2.3 R4R10 predecessor

```text
FJ899/8 PR #134
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = b2824d95e15ae5de782eeb5d59ffc784b1a116b1
TREE = d9c9003746f3ccafb97157e6e37ce12395d12709
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R10.md
BLOB = f3a7e5b5c163de995078d96682c822e5ec15567c
```

### 2.4 Binding R4R10 NOT-PASS review

```text
FJ899/8 PR #135
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = c5fee5d7979d8dcf3e4c9628c578a257a89d913c
TREE = de73cfbcef715a2c1bc2ca27e169aceedc72685e
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R10_AK_CANON_REVIEW.md
BLOB = 306a68095ca584ef918324bbc83b227dc23eabf2
VERDICT = AK-CANON X1B R4R10 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #135 froze:

```text
X1B-R4R10-IBR-F001 — Linux user/mount ID mapping is unbound
X1B-R4R10-IBR-F002 — loose-object mtime / Git pruning semantics are unbound
```

PR #135 also recorded that R4R10 addressed at brief level:

```text
X1B-R4R9-IBR-F001 Linux inode semantic flags / casefold namespace
X1B-R4R9-IBR-F002 pre-ref object-store crash residue
```

and preserved prior fsync, split-index/sharedindex, ref topology, primary ODB topology, hook, lazy-fetch, replacement-ref, commit-encoding, reflog, write-target alias and freshness/supersession corrections.

`REVIEW FINDING != REPAIR AUTHORITY`; R4R11 exists only under fresh Human authorization for successor brief preparation.

## 3. Exact evidence-repository base

```text
FJ899/8 main
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

No history rewrite is part of R4R11.

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

## 5. Normative precedence and V11 migration

```text
R4R11 TEXT = CURRENT IMPLEMENTATION-BRIEF AUTHORITY
R4R10 / R4R9 / R4R8 / R4R7 / R4R6 / R4R5 / R4R4 / R4R3 / R4R2 / R4R1 / R4 / R3 / R2 / R1 = HISTORICAL INPUT ONLY
CORRECTIVE DESIGN PR #34 = HIGHER-LEVEL PROPERTY CONTRACT
```

R4R11 changes authority-critical surfaces:

```text
caller user namespace must be the Linux initial user namespace
uid_map/gid_map must be the initial full identity maps
reviewed repository mount must be provably non-ID-mapped
statmount MOUNT_ATTR_IDMAP/uidmap/gidmap state becomes authority-critical
execution credential state becomes request-bound and stable
loose-object mtime becomes Human-bound authority-relevant retention metadata
all new-closure canonical loose leaves are sealed to one exact mtime
pre-existing exact loose closure leaves and concurrent winners are also sealed
V11 staging namespace prefix changes to V11
```

Therefore:

```text
V10 REQUEST/REVIEW/ADMISSION/GATE != R4R11 AUTHORITY
V10 HUMAN REVIEW MARKER != V11 HUMAN DECISION
V11 EFFECT PROFILE REQUIRES FRESH V11 HUMAN-BOUND REQUEST
```

No V10 or earlier Human evidence may authorize a V11 effect.

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

No caller-controlled field may supply Human actor/result/rationale, request path/digest, task/scene/candidate/impact identities, canonical target/ref, user namespace, uid/gid mapping, mount ID mapping, filesystem namespace profile, inode semantic state, physical Git-dir/ref/object/index topology, staging namespace, loose-object mtime, metadata policy, reflog semantics, effect type, material effect, raw-object profile, hook profile, durability profile, commitment profile, or effect commit metadata.

Defect-era direct approval/promotion routes remain disabled and non-effect-capable.

## 9. Git/runtime/OS profile V11

Git semantic compatibility remains bounded to:

```text
2.55.0 <= parsed Git version < 2.56.0
object format = sha1
ref storage format = files
```

R4R11 authority filesystem remains deliberately narrow:

```text
OS = Linux
filesystem = ext4
one reviewed mount for repository root and every authority-critical path
byte-exact case-sensitive authority directories
no unsupported Linux inode semantic flags
caller user namespace = Linux initial user namespace
reviewed mount = not ID-mapped
```

Required runtime proof primitives now include:

```text
dir_fd relative open/mkdir/rmdir/unlink/rename
renameat2(RENAME_NOREPLACE)
O_NOFOLLOW
O_DIRECTORY
O_EXCL
O_CLOEXEC
fstat/lstat
statfs
statx including unique mount ID where available
statmount with MNT_BASIC + FS_TYPE + MNT_UIDMAP + MNT_GIDMAP + SUPPORTED_MASK
/proc/self/ns/user descriptor + fstat
/proc/self/uid_map
/proc/self/gid_map
Linux nsfs UAPI USER_NS_INIT_INO
FS_IOC_GETFLAGS
FS_IOC_FSGETXATTR
fchmod
futimens
fsync regular file
fsync directory
listxattr
POSIX ACL inspection capability
/proc/self/ns/mnt
/proc/self/mountinfo
```

If `statmount()` cannot be called because of kernel support, privilege, seccomp, LSM, containerization or any other reason, V11 is `BLOCKED`.

V11 MUST NOT acquire privilege, invoke `sudo`, enter another namespace, call `setns`, call `unshare`, create an ID-mapped mount, call `mount_setattr`, or delegate the mapping proof to an unreviewed helper.

No fallback to `mountinfo` alone is authorized for ID-mapping proof.

## 10. Current semantics grounding

R4R11 freezes design around current Linux/Git semantics checked during preparation.

Current Linux UAPI defines:

```text
USER_NS_INIT_INO = 0xEFFFFFFD
                 = 4026531837
MOUNT_ATTR_IDMAP = 0x00100000
STATMOUNT_MNT_UIDMAP
STATMOUNT_MNT_GIDMAP
STATMOUNT_SUPPORTED_MASK
```

Current Linux namespace documentation states that the initial user namespace exposes dummy full-range identity mappings:

```text
/proc/self/uid_map = 0 0 4294967295
/proc/self/gid_map = 0 0 4294967295
```

Current `statmount(2)` exposes mount attributes plus mount uid/gid maps; current `mount_setattr(2)` defines `MOUNT_ATTR_IDMAP` as the state that attaches a user-namespace mapping to a mount.

Current exact Git 2.55 source establishes:

```text
object-file.c freshen_file() uses utime()
stale loose-object mtime may make an object subject to pruning
builtin/prune.c compares loose-object st_mtime with expiry
```

Public Git 2.55-compatible documentation states:

```text
git prune --expire <time> only expires loose objects older than <time>
gc.pruneExpire defaults to a time-based grace period
gc.auto=0 disables automatic gc heuristics
maintenance.auto=false disables command-triggered auto maintenance
```

These facts are implementation prerequisites, not ambient assumptions.

## 11. PR #135 F001 correction — LINUX_INITIAL_USER_NAMESPACE_V1

V11 does not accept a child/nested user namespace even if its visible IDs happen to look harmless.

Open `/proc/self/ns/user` with `O_RDONLY|O_CLOEXEC` and retain the descriptor for the effect interval.

Require:

```text
namespace type = CLONE_NEWUSER
fstat(nsfd).st_ino = USER_NS_INIT_INO
                     = 0xEFFFFFFD
                     = 4026531837
```

Also read exact raw mapping files and require canonical semantic content:

```text
uid_map = one mapping range only:
          inside_start = 0
          outside_start = 0
          length = 4294967295

gid_map = one mapping range only:
          inside_start = 0
          outside_start = 0
          length = 4294967295
```

Whitespace may be parsed semantically, but the canonical physical-prestate record stores exact raw bytes plus the parsed tuple set.

Any extra map range, partial map, remap, unmapped execution uid/gid, unreadable mapping or namespace-identity drift is `BLOCKED`.

`NS_GET_PARENT` is not used as the sole initial-namespace proof because `EPERM` can also arise when an ancestor is outside the caller's namespace scope.

## 12. LINUX_EXECUTION_CREDENTIAL_STATE_V1

Request creation records the exact execution credential state needed for authority proofs.

At minimum bind and freshly revalidate:

```text
ruid
euid
suid
fsuid
rgid
egid
sgid
fsgid
sorted supplementary group list
CapInh
CapPrm
CapEff
CapBnd
CapAmb
NoNewPrivs
user namespace identity
uid_map digest + parsed identity mapping
gid_map digest + parsed identity mapping
```

For the V11 success path require:

```text
ruid = euid = suid = fsuid = execution_uid
rgid = egid = sgid = fsgid = execution_gid
```

The exact supplementary group list and capability masks are Human-request-bound and must remain unchanged through the effect.

V11 does not silently add/drop capabilities or groups.

The process must already have whatever authority is required to make the read-only `statmount` proof succeed. Inability to prove the mount is `BLOCKED`.

Capability possession is never Human decision authority.

## 13. LINUX_IDENTITY_MAPPED_EXT4_MOUNT_V1

This is the binding correction for the mount-ID-mapping half of PR #135 F001.

For the exact reviewed repository mount, obtain a unique mount ID from the authority-root descriptor through `statx` and query that exact mount with `statmount`.

Request at least:

```text
STATMOUNT_SB_BASIC
STATMOUNT_MNT_BASIC
STATMOUNT_FS_TYPE
STATMOUNT_MNT_NS_ID
STATMOUNT_MNT_UIDMAP
STATMOUNT_MNT_GIDMAP
STATMOUNT_SUPPORTED_MASK
```

Require the returned `mask` to establish every field needed by V11.

Require:

```text
fs_type = "ext4"
sb_magic = EXT4_SUPER_MAGIC
exact mount ID = request-bound reviewed mount ID
exact mount namespace ID = request-bound mount namespace ID
(mnt_attr & MOUNT_ATTR_IDMAP) = 0
```

The kernel must report support for both:

```text
STATMOUNT_MNT_UIDMAP
STATMOUNT_MNT_GIDMAP
```

Under the required initial caller user namespace and `MOUNT_ATTR_IDMAP = 0`, V11 requires:

```text
mnt_uidmap_num = 0
mnt_gidmap_num = 0
```

Any nonzero mapping, unresolved/inconsistent mapping result, missing requested mask bit, missing supported-mask bit, `MOUNT_ATTR_IDMAP`, or inability to query the exact mount is `BLOCKED`.

V11 records the exact returned mount mapping fields and digests in the physical prestate.

## 14. Mount-state narrowing

R4R11 additionally records exact `statmount` mount/superblock attributes used by the durability claim.

Required:

```text
MOUNT_ATTR_RDONLY = 0
MOUNT_ATTR_IDMAP = 0
SB_RDONLY = 0
SB_LAZYTIME = 0
```

`SB_SYNCHRONOUS` and `SB_DIRSYNC` may be present or absent and are recorded.

Atime-policy mount attributes are operational because V11 does not use atime as authority state.

If a future kernel returns an unknown mount-attribute bit that can affect ownership, lookup or durability semantics and the implementation has no reviewed rule for it, V11 is `BLOCKED`.

## 15. LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1 preserved

For repository root and every authority-critical directory component retain:

```text
ext4 type
same exact reviewed mount
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

R4R11 nests the new initial-userns/non-ID-mapped proof underneath this namespace profile.

## 16. LINUX_INODE_SEMANTIC_FLAGS_V1 preserved

`FS_IOC_GETFLAGS`, `FS_IOC_FSGETXATTR` and required `statx` semantic attributes remain mandatory.

Allowed inode flags remain exactly:

```text
regular file: subset of {FS_EXTENT_FL}
directory: subset of {FS_EXTENT_FL, FS_INDEX_FL}
```

All other returned inode flag bits are unsupported and `BLOCKED`.

`fsx_xflags`, `fsx_extsize`, `fsx_projid` and `fsx_cowextsize` remain exactly zero.

Required `statx` semantic attributes remain supported and absent:

```text
IMMUTABLE
APPEND
ENCRYPTED
VERITY
DAX
```

## 17. POSIX metadata profile preserved

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
V11 object staging root                            = 0700
staging temporary object file before final chmod   = 0600
```

Also require exact request-bound uid/gid, empty arbitrary xattrs, mode-only POSIX ACL, no default ACL on writable authority directories, and no setuid/setgid/sticky bits.

The effect process uses exactly:

```text
umask = 0077
```

## 18. Timestamp authority taxonomy V11

R4R11 makes timestamp treatment explicit.

For canonical loose object files belonging to `new_object_closure`:

```text
mtime = AUTHORITY-RELEVANT RETENTION METADATA
```

For those same files:

```text
atime = excluded operational metadata
ctime = excluded operational metadata
btime = excluded operational metadata
```

Directory atime/mtime/ctime/btime remain operational unless another profile explicitly binds them.

Object content/OID, mode, uid/gid, nlink, semantic flags and V11 mtime remain authority-critical.

## 19. PR #135 F002 correction — HUMAN_BOUND_LOOSE_OBJECT_MTIME_V1

V11 selects one exact, Human-visible retention timestamp for every canonical loose leaf in the V11 `new_object_closure`.

Exact value:

```text
profile = HUMAN_BOUND_LOOSE_OBJECT_MTIME_V1
mtime_iso8601 = 2038-01-18T00:00:00.000000000Z
mtime_tv_sec = 2147385600
mtime_tv_nsec = 0
```

This value is fixed by the V11 profile itself and is therefore known when the Human reviews the V11 request.

It is deliberately below the signed 32-bit Unix time limit while remaining in the future relative to the V11 profile's 2026 operating epoch.

V11 runtime applicability requires:

```text
CLOCK_REALTIME < 2147385600
```

at request creation, admission, FinalEffectGateV11 and immediately before loose-object mtime sealing.

If that condition is false, V11 is `BLOCKED_PROFILE_HORIZON`; the Human evidence is not declared stale merely because of age.

Preserve:

```text
NO WALL-CLOCK TTL FOR HUMAN EVIDENCE
AGE ALONE != HUMAN DECISION STALE
```

The sentinel is an implementation/storage-retention profile horizon, not a Human-decision TTL.

## 20. Why every new-closure loose leaf is sealed

The V11 mtime rule applies to all exact canonical loose representations of `new_object_closure`, including:

```text
newly staged/installed object
pre-existing exact loose object that already occupies the OID path
exact concurrent RENAME_NOREPLACE EEXIST winner
```

A pre-existing exact leaf is not allowed to carry an arbitrary stale historical mtime into the V11 commitment proof.

For a qualifying pre-existing/winner leaf, V11 is authorized to mutate exactly one existing-file field before ref commitment:

```text
mtime -> exact V11 sentinel
```

That metadata mutation is part of the Human-presented V11 preparation effect.

No content, mode, uid/gid, xattr, ACL, inode flag, hardlink, pathname or object identity normalization is authorized.

## 21. Descriptor-relative loose-object mtime seal

For an exact canonical loose object leaf already present:

```text
1. open relative to held canonical fanout descriptor with O_NOFOLLOW|O_CLOEXEC
2. require regular file, st_nlink=1, mode 0444, exact uid/gid
3. require exact Linux semantic flag/xattr/ACL/ext4/non-ID-mapped profile
4. inflate and verify one exact canonical object stream, no trailing garbage
5. require SHA-1 = pathname OID
6. futimens(fd, [UTIME_OMIT, {2147385600, 0}])
7. fstat/statx exact mtime = sentinel
8. reverify authority metadata
9. fsync(fd) AFTER mtime sealing
10. reopen exact canonical path no-follow and reverify object + mtime
```

If the exact mtime cannot be set or read back exactly, V11 is `BLOCKED` before ref commitment.

The seal may update ctime; ctime is explicitly operational and not Human authority state.

## 22. Staged new object ordering V11

For a newly created staged object under the request-bound staging root:

```text
create private staged leaf 0600
write exact zlib stream
reread and verify canonical object bytes/OID
fchmod 0444
futimens(atime=UTIME_OMIT, mtime=V11 sentinel)
verify content/mode/uid/gid/nlink/xattrs/ACL/inode flags/mtime
fsync(file_fd) AFTER final fchmod + mtime
RENAME_NOREPLACE into canonical fanout
fsync destination fanout
fsync source staging root
reopen canonical loose leaf
verify exact object + sentinel mtime + all authority metadata
```

No authority-relevant loose-object field changes after the final file fsync on the successful rename path.

## 23. Git pruning/freshness consequence is explicitly bound

V11 does not classify loose-object mtime as cosmetic.

The Human-presented effect explicitly states:

```text
new_object_closure_loose_mtime_after = 2038-01-18T00:00:00Z
retention_semantics = FUTURE_SENTINEL_TO_PREVENT_NORMAL_CURRENT-TIME-BASED_PRUNE_EXPIRY_BEFORE_PROFILE_HORIZON
```

All V11-owned Git subprocesses additionally receive:

```text
-c gc.auto=0
-c maintenance.auto=false
```

so the bounded read-only Git cross-check path does not trigger automatic maintenance.

V11 does not claim to defeat an external administrator intentionally deleting object paths or deliberately invoking maintenance with an expiry threshold at/after the sentinel. Such noncooperative external mutation is not silently accepted: the final pre-ref physical object proof must still pass immediately before ref CAS, and any observed loss/drift blocks commitment.

## 24. BOUND_OBJECT_STAGING_NAMESPACE_V2

All nonfinal object-preparation names remain outside canonical Git object lookup paths.

Exact V11 staging root:

```text
staging_root_basename = ".x1b-stage-v11-" + request_digest
```

Global precondition before request creation, admission, FinalEffectGateV11 and staging creation:

```text
zero raw .git entries whose basename starts with ".x1b-stage-v"
```

Thus stale V10, V11 or unknown future/past X1B staging residue blocks a new V11 effect instead of being ignored.

No auto-cleanup is authorized.

## 25. Staging-root creation V11

Only after admitted Human evidence and FinalEffectGateV11:

```text
mkdirat(held_git_fd, staging_root_basename, 0700)
open no-follow directory descriptor
verify exact uid/gid/mode 0700
verify initial-userns/non-ID-mapped ext4 profile
verify empty xattrs/mode-only ACL/inode flags
fsync(staging_root_fd)
fsync(held_git_fd)
```

Allowed children remain exact:

```text
fanout.<two-lowercase-hex>
object.<40-lowercase-hex>
```

No other staging entry is authorized.

## 26. Canonical fanout creation V11

If canonical `.git/objects/<prefix>` exists, verify exact V11 fanout profile and use it.

If absent:

```text
mkdir staged fanout 0700 under staging root
open staged fanout no-follow
fchmod 0755
verify uid/gid/mode/xattr/ACL/inode flags/ext4/non-ID-mapped mount
fsync staged fanout AFTER final metadata
RENAME_NOREPLACE staging/fanout.<prefix> -> objects/<prefix>
fsync held .git/objects directory
fsync staging root
reopen canonical fanout and verify exact final profile
```

A V11-created canonical fanout is never exposed as 0700.

## 27. Fanout EEXIST handling

On concurrent `RENAME_NOREPLACE` EEXIST:

```text
verify exact canonical winner
if exact:
    rmdir exact private staged fanout
    fsync staging root
else:
    do not alter winner
    preserve staging residue
    return bound-staging-residue / uncertainty
```

No canonical fanout overwrite is permitted.

## 28. Existing canonical loose-object rule V11

Before mtime sealing, an existing loose object must satisfy:

```text
exact lowercase OID pathname
real regular non-symlink file
st_nlink = 1
mode = 0444
exact uid/gid
empty arbitrary xattrs
mode-only ACL
LINUX_INODE_SEMANTIC_FLAGS_V1 PASS
same exact non-ID-mapped ext4 mount
exact canonical type/length/payload
SHA-1 = pathname OID
```

Then execute the exact V11 mtime seal from section 21.

Any mismatch is `BLOCKED`; no content/security normalization is authorized.

## 29. ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V4

For each missing closure OID:

```text
staging_name = "object." + exact_40_lowercase_oid
create only under held V11 staging root
O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC
initial mode 0600 under umask 0077
```

Then perform the ordering in section 22.

Final install:

```text
renameat2(staging_root_fd, staging_name,
          held_fanout_fd, exact_38hex_leaf,
          RENAME_NOREPLACE)
```

On success, fsync both destination fanout and source staging root.

On EEXIST, verify winner through section 28, including V11 mtime sealing, then unlink the private staged object and fsync staging root.

No hard-link installation is permitted.

## 30. COMPLETE_LOCAL_OBJECT_STORE_V4

V4 preserves all prior rejection conditions and adds mapping/mtime closure.

Reject:

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
ID-mapped reviewed mount
noninitial caller user namespace
casefolded authority directory
unsupported inode semantic flags
unsupported pack metadata topology
unexpected .x1b-stage-v* residue
```

For every `new_object_closure` member before ref commitment require:

```text
physically contained canonical loose representation
exact object bytes/OID
exact mode/uid/gid/nlink/security metadata
exact non-ID-mapped ext4 ownership semantics
exact V11 loose-object mtime sentinel
file fsync completed after final mtime/security metadata
canonical parent namespace durability proved
```

Equivalent packed objects do not remove the required canonical loose representation.

## 31. New-object closure V11

Derive exactly:

```text
new_object_closure = every blob/tree/commit reachable from effect commit
                     not reachable from raw request-base parent
```

Each member is recorded as:

```text
(type, payload_length, payload_sha256, oid, loose_mtime_profile)
```

with:

```text
loose_mtime_profile = HUMAN_BOUND_LOOSE_OBJECT_MTIME_V1
```

Every member must pass V11 physical closure before ref commitment.

## 32. Staging-root successful removal

After every required closure member is canonical, durable and mtime-sealed:

```text
enumerate staging root
require empty
fsync staging root
rmdir exact V11 staging root
fsync .git
re-enumerate .git
require zero .x1b-stage-v* entries
```

Normal pre-ref success leaves no staging residue.

## 33. Staging residue truth preserved

Crash/failure may leave request-bound staged directories/files.

Possible residue includes:

```text
staging root only
staged fanout 0700
staged fanout 0755
staged object 0600 partial/complete
staged object 0444 with or without final mtime/fsync
mix of installed canonical mtime-sealed objects + remaining staged items
```

No new X1B effect may proceed while `.x1b-stage-v*` residue exists.

Read-only classification is allowed; deletion/completion requires separate recovery authority.

## 34. Preparation side-effect truth V11

Pre-ref failure outcomes may leave two Human-bound classes of canonical preparation metadata:

```text
exact unreferenced closure loose objects/fanouts
exact mtime sentinel applied to qualifying pre-existing/winner closure loose objects
```

The implementation must not report such a state as “no filesystem effect”.

Object mtime sealing is a persistent preparation effect even when the object content pre-existed.

## 35. SINGLE_WORKTREE_REAL_GITDIR_V1 preserved

Required:

```text
repository root = exact canonical physical directory R
R/.git = real directory, not symlink/gitfile/reparse redirect
absolute Git dir = R/.git
Git common dir = R/.git
Git worktree top level = R
repository non-bare
.git/worktrees absent
core.worktree absent
extensions.worktreeConfig absent/false
```

Entire authority closure must pass V11 initial-userns/non-ID-mapped ext4 proof.

## 36. PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1 preserved

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
```

## 37. ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V3 preserved

Acquire `refs/heads/main.lock` under held refs/heads descriptor:

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
verify POSIX + Linux semantic + identity-mapped mount metadata
fsync main.lock AFTER final metadata
reread old main exact request base + LF
revalidate packed-main absence + hierarchy + userns/mount mapping state
atomic same-directory rename main.lock -> main
fsync held refs/heads directory
reopen final main no-follow and verify exact ref + metadata
```

No Git ref writer is permitted.

## 38. Main-ref crash residue truth preserved

Classifier distinguishes at least:

```text
main old + main.lock absent
main old + V11-shaped main.lock present
main new
ambiguous/unreadable
```

No automatic deletion of ambiguous lock residue is authorized.

## 39. CLOSED_RAW_TREE_REWRITE_V1 preserved

Raw parent-tree bytes are parsed and reconstructed in memory.

Only tracked changed paths remain:

```text
scenes/<scene_id>.fountain
.scriptops/decision-log.ndjson
```

Every unrelated semantic tree entry is preserved exactly.

Tracked effect modes remain 100644.

## 40. CLOSED_RAW_COMMIT_OBJECT_V1 preserved

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

## 41. Canonical object bytes preserved

For object type `T` and payload `P`:

```text
canonical_object_bytes = ASCII(T) + SP + ASCII(decimal(len(P))) + NUL + P
object_oid = lowercase_hex(SHA1(canonical_object_bytes))
```

Supported new types remain blob/tree/commit.

Loose zlib representation remains storage-only/non-authority-semantic; production compressor/runtime identity is execution evidence.

## 42. FULL_SINGLE_FILE_INDEX_V1 preserved

Canonical `.git/index` prestate remains:

```text
regular single-link mode 0644
exact uid/gid + V11 mount/userns metadata
DIRC
version exactly 2
valid SHA-1 trailer
canonical entries
stage = 0
extended flag = 0
no extensions
semantic (path,mode,oid) set exactly raw parent tree
```

Split index, sparse index, fsmonitor, untracked cache and all optional extensions remain unsupported.

## 43. Shared-index closure V11

Under byte-exact `.git` namespace require:

```text
zero raw entries whose basename starts with "sharedindex."
core.splitIndex absent/false
all splitIndex.* config absent
GIT_INDEX_FILE stripped
```

No authority-critical Git command reads or writes canonical index.

## 44. CLOSED_FULL_INDEX_V2_REWRITE_V1 preserved

Final extension-free index-v2 bytes are derived entirely in memory from exact prestate plus derived new tree.

Existing entries preserve exact stat-cache fields and assume-valid bit; changed OID/mode follow new tree.

New entries use zero stat-cache fields.

Trailing index SHA-1 is recomputed exactly.

## 45. ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1 preserved under V11 identity mapping

After durable ref commitment:

```text
require index.lock absent
require no sharedindex.*
acquire .git/index.lock 0600
reread exact Human-bound index prestate
write exact derived v2 bytes
reread/validate checksum/semantics
fchmod 0644
verify POSIX/Linux/userns/mount metadata
fsync index.lock AFTER final metadata
atomic rename -> index
fsync .git
reopen/verify exact final index
require no sharedindex.*
```

`GIT_REAL_INDEX_MUTATING_COMMAND = NONE`.

## 46. DETERMINISTIC_MAIN_REFLOG_PROJECTION_V2 preserved

Only after normal durable physical main-ref commitment:

```text
revalidate exact Human-bound reflog prestate
construct exact prior bytes + exact V11 reflog line
create private temp 0600
write complete bytes
reread
fchmod 0644
verify V11 metadata/mapping profile
fsync temp AFTER final metadata
atomic rename -> main reflog
fsync reflog parent
reopen/verify exact bytes/hash/metadata
```

Exact line:

```text
<request_base_sha> <effect_commit_sha> ScriptOps X1B <scriptops-x1b@local.invalid> <request_epoch> +0000\tscriptops x1b: accept <scene_id>\n
```

## 47. ALIAS_SAFE_WORKTREE_PROJECTION_V2 preserved

Canonical scene and decision-log materialization use:

```text
prove exact Human-bound prestate and V11 parent topology
create temp 0600 in held parent
write final bytes
reread
fchmod 0644
verify V11 metadata/mapping profile
fsync temp AFTER final metadata
atomic descriptor-relative rename -> final
fsync parent
reopen final no-follow and verify exact bytes/hash/metadata
```

No in-place decision-log append is used.

## 48. Hook closure preserved

`NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1` remains mandatory.

V11 still has:

```text
Git ref mutation = NONE
Git primary object mutation = NONE
Git real-index mutation = NONE
```

Remaining Git subprocesses are read-only cross-checks only.

## 49. Sanitized Git subprocess profile V11

Every authority-critical Git subprocess uses:

```text
absolute resolved system Git
shell=false
explicit minimal environment
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
```

Strip caller config, loader, executable, object-directory, alternates, askpass, SSH, replacement and index-file variables.

Command-scope controls include:

```text
--no-replace-objects
--no-lazy-fetch
-c core.hooksPath=<verified empty private hook dir>
-c hook.reference-transaction.enabled=false
-c hook.post-index-change.enabled=false
-c core.fsmonitor=false
-c core.splitIndex=false
-c commit.gpgSign=false
-c credential.helper=
-c core.sharedRepository=false
-c gc.auto=0
-c maintenance.auto=false
```

No V11 durability or retention claim relies on Git mutating the repository.

## 50. PhysicalPreStateV11

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
current user namespace identity
raw uid_map/gid_map
execution credential state
exact reviewed mount statmount record
```

Each inode record retains V10 mode/uid/gid/nlink/xattr/ACL/inode flags/statx fields.

The mount record includes:

```text
unique mount ID
mount namespace ID
fs type / superblock magic
mnt_attr
sb_flags
supported_mask
uidmap count/data
gidmap count/data
```

No omitted mapping field is interpreted as benign.

## 51. PresentedMaterialEffectV11

Closed schema includes at least:

```text
PresentedMaterialEffectV11 = {
  "schema_version": "scriptops-x1b-presented-material-effect/v11",
  "repository": "FJ899/scriptops",
  "scene_id": <exact scene ID>,
  "candidate_path": <exact repo-relative path>,
  "candidate_file_sha256": <exact digest>,
  "execution_identity": {
    "uid": <exact uid>,
    "gid": <exact gid>,
    "umask": "0077",
    "credential_profile": "LINUX_EXECUTION_CREDENTIAL_STATE_V1",
    "user_namespace_profile": "LINUX_INITIAL_USER_NAMESPACE_V1"
  },
  "filesystem_authority": {
    "namespace_profile": "LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1",
    "inode_semantic_profile": "LINUX_INODE_SEMANTIC_FLAGS_V1",
    "mount_mapping_profile": "LINUX_IDENTITY_MAPPED_EXT4_MOUNT_V1",
    "filesystem_type": "ext4",
    "casefold_allowed": false,
    "idmapped_mount_allowed": false
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
    "record_schema_version": "scriptops-x1b-decision-record/v11",
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
    "staging_name_derivation": "PREFIX_DOT_X1B_STAGE_V11_PLUS_REQUEST_DIGEST",
    "loose_object_mtime_profile": "HUMAN_BOUND_LOOSE_OBJECT_MTIME_V1",
    "loose_object_mtime_tv_sec": 2147385600,
    "loose_object_mtime_tv_nsec": 0,
    "durability_order_profile": "FSYNC_AFTER_FINAL_METADATA_V1",
    "index_prestate_profile": "FULL_SINGLE_FILE_INDEX_V1",
    "index_projection_profile": "CLOSED_FULL_INDEX_V2_REWRITE_V1",
    "index_install_profile": "ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1",
    "raw_object_profile": "NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2",
    "hook_profile": "NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1",
    "commit_object_profile": "CLOSED_RAW_COMMIT_OBJECT_V1",
    "ref_cas_profile": "ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V3",
    "durability_profile": "CRASH_DURABLE_OBJECT_REF_INDEX_V6",
    "success_commitment_profile": "ALIAS_SAFE_MAIN_REF_COMMITMENT_V7",
    "effect_transport_profile": "REF_CAS_FIRST_ALIAS_SAFE_RAW_GIT_METADATA_V9",
    "git_ref_mutating_command": "NONE",
    "git_primary_object_mutating_command": "NONE",
    "git_real_index_mutating_command": "NONE",
    "successful_staging_residue": "NONE",
    "pre_ref_failure_staging_residue": "BOUND_AND_EXPLICITLY_CLASSIFIED",
    "exact_changed_paths": [
      "scenes/<scene_id>.fountain",
      ".scriptops/decision-log.ndjson"
    ]
  }
}
```

## 52. HumanDecisionRequestBindingV11

```text
HumanDecisionRequestBindingV11 = {
  "schema_version": "scriptops-x1b-human-decision-request/v11",
  "repository": "FJ899/scriptops",
  "repository_head_at_request": <40 lowercase hex>,
  "repository_ref_at_request": "refs/heads/main",
  "request_created_at": <exact timestamp>,
  "execution_uid": <exact uid>,
  "execution_gid": <exact gid>,
  "execution_credential_state": <LinuxExecutionCredentialStateV1>,
  "user_namespace_state": <LinuxInitialUserNamespaceStateV1>,
  "mount_mapping_state": <LinuxIdentityMappedExt4MountStateV1>,
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
  "presented_material_effect": <PresentedMaterialEffectV11>
}
```

```text
request_digest = sha256_canonical(binding)
decision_request_id = "x1b:" + request_digest
```

## 53. Proposal PR and V11 Human review marker

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
X1B-HUMAN-DECISION-V11
decision_request_id=<exact x1b:<request_digest>>
decision_request_sha256=<exact request_digest>
why=<Human rationale>
```

Four LF-separated lines, no trailing LF.

V10 or earlier markers are invalid for V11.

## 54. Trusted GitHub evidence and freshness preserved

Public exact-origin GitHub evidence transport, complete review pagination, current-head binding, duplicate ambiguity, active CHANGES_REQUESTED handling, no-latest-wins semantics, exact proposal envelope, replay lock and freshness/supersession rules remain as R4R10 with V11 schema identities.

```text
NO WALL-CLOCK TTL FOR HUMAN REVIEW CURRENTNESS
AGE ALONE != STALE
```

The V11 mtime profile horizon is a distinct implementation applicability predicate.

## 55. X1BDecisionRecordV11

Record includes at least:

```text
schema_version = scriptops-x1b-decision-record/v11
result = REF_COMMITTED
result_scope = PHYSICAL_LOOSE_REFS_HEADS_MAIN_POINTS_TO_EXACT_EFFECT_COMMIT
exact request/review/admission/currentness identities
exact scene/candidate/impact identities
ref_before
execution uid/gid + credential state digest
initial user namespace state digest
non-ID-mapped ext4 mount state digest
main reflog prestate
full index prestate
canonical before/after digests
presented material effect digest
filesystem_namespace_profile = LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1
inode_semantic_profile = LINUX_INODE_SEMANTIC_FLAGS_V1
mount_mapping_profile = LINUX_IDENTITY_MAPPED_EXT4_MOUNT_V1
object_store_profile = COMPLETE_LOCAL_OBJECT_STORE_V4
object_staging_profile = BOUND_OBJECT_STAGING_NAMESPACE_V2
object_install_profile = ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V4
loose_object_mtime_profile = HUMAN_BOUND_LOOSE_OBJECT_MTIME_V1
loose_object_mtime_tv_sec = 2147385600
loose_object_mtime_tv_nsec = 0
durability_order_profile = FSYNC_AFTER_FINAL_METADATA_V1
index profiles from V9
ref/reflog/worktree profiles from prior accepted brief levels
durability_profile = CRASH_DURABLE_OBJECT_REF_INDEX_V6
success_commitment_profile = ALIAS_SAFE_MAIN_REF_COMMITMENT_V7
canonical_instance_scope = LOCAL_INITIAL_USERNS_NONIDMAPPED_EXT4_MAIN_OBJECT_DB_FULL_INDEX_WORKTREE_DECISION_LOG_REFLOG_V11
```

The record still says `REF_COMMITTED`, not generic success.

## 56. FinalEffectGateV11

Immediately before deterministic record/object derivation, while the same-worktree exclusive X1B lock is held, freshly validate:

```text
exact V11 PR/request/review envelope
Human currentness/conflicts
CompleteReviewSetV11 digest
raw logical main SHA = request base
SINGLE_WORKTREE_REAL_GITDIR_V1
LINUX_INITIAL_USER_NAMESPACE_V1
LINUX_EXECUTION_CREDENTIAL_STATE_V1
LINUX_IDENTITY_MAPPED_EXT4_MOUNT_V1
LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1 over full authority closure
LINUX_INODE_SEMANTIC_FLAGS_V1 over full authority closure
PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1
COMPLETE_LOCAL_OBJECT_STORE_V4
FSYNC_AFTER_FINAL_METADATA_V1 capability
CLOCK_REALTIME < 2147385600
FULL_SINGLE_FILE_INDEX_V1 exact
no sharedindex.*
zero .x1b-stage-v* entries
core.splitIndex absent/false
MainReflogPreStateV2 exact
mount namespace/mount ID/userns/mapping state exact
Git 2.55.x
files ref format
NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2
NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1
zero refs/replace
raw parent commit/tree
candidate/impact/canonical prestate
accepted preview
PresentedMaterialEffectV11
replay state
raw full-index semantic tree = raw parent tree
verified empty hook directory
renameat2(RENAME_NOREPLACE) supported
```

After gate:

```text
no user interaction
no network
no sleep/wait
no unrelated blocking operation
no proposal/review mutation
no untrusted subprocess
no namespace transition
no credential/capability/group transition
no Git ref mutation
no Git primary object mutation
no Git real-index read or mutation
```

## 57. Exact local effect sequence V11

With X1B lock held after FinalEffectGateV11:

```text
A. re-prove raw-object, initial userns, exact credentials,
   non-ID-mapped ext4 mount, byte-exact namespace, Linux inode semantics,
   complete-local-store, ref/reflog/index profiles and zero stale staging

B. construct X1BDecisionRecordV11 bytes in memory

C. construct exact accepted-scene and decision-log payloads in memory
   compute exact blob canonical bytes/OIDs

D. execute CLOSED_RAW_TREE_REWRITE_V1
   derive exact affected tree payloads/OIDs
   prove exact two-path semantic delta

E. construct exact CLOSED_RAW_COMMIT_OBJECT_V1 in memory
   compute exact effect commit SHA

F. derive exact new_object_closure tuples

G. create exact request-bound .git/.x1b-stage-v11-<request_digest> root
   verify V11 userns/mount/namespace/inode profile
   fsync staging root and .git

H. for each missing canonical fanout:
   build/finalize/fsync fanout under staging root
   RENAME_NOREPLACE into .git/objects/<xx>
   fsync objects + staging root
   verify canonical fanout

I. for each new_object_closure member:
   if exact canonical loose leaf already exists:
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
   verify exact canonical leaf + V11 mtime

J. verify every closure member exact/contained/durable/mtime-sealed
   require staging root empty
   fsync staging root
   rmdir exact staging root
   fsync .git
   require zero .x1b-stage-v* entries

K. cross-check installed commit/tree/object closure with object-only read-only Git plumbing
   -c gc.auto=0
   -c maintenance.auto=false
   no index access

L. derive exact deterministic final raw index bytes in memory

M. final pre-ref checks:
   physical main exact old SHA
   packed main absent
   initial userns + exact credential state unchanged
   non-ID-mapped ext4 mapping proof unchanged
   byte-exact ref/object hierarchy exact
   every closure object exact/contained/durable/mtime-sealed
   no staging residue
   reflog prestate exact
   raw full index exact unchanged
   no sharedindex.*
   mount namespace/mount IDs exact
   hook census empty

N. acquire main.lock descriptor-relative O_EXCL/O_NOFOLLOW
   repeat old-value/topology/metadata/mapping proof

O. write exact effect SHA + LF
   fchmod 0644
   verify V11 metadata
   fsync main.lock AFTER final metadata
   final old-main + mapping proof

P. atomic descriptor-relative rename main.lock -> main
   fsync refs/heads
   classify physical ref result

Q. after normal durable ref commitment:
   deterministic main reflog V2

R. project canonical scene through worktree projection V2

S. project decision log through worktree projection V2

T. replace raw canonical full v2 index through ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1

U. verify ref, raw commit/tree/object closure,
   initial userns, credential state, non-ID-mapped ext4 mount,
   byte-exact namespace, inode semantics, every closure mtime sentinel,
   zero staging residue, reflog, worktree, full index, zero sharedindex

V. release X1B lock only after final outcome class is determined
```

No canonical worktree, decision-log, reflog or real-index mutation occurs before physical main-ref commitment.

Object/fanout preparation and V11 mtime sealing may occur before ref commitment and are reported as preparation effects.

## 58. CRASH_DURABLE_OBJECT_REF_INDEX_V6

Normal durable new fanout requires:

```text
final 0755/security/mapping metadata under staging
staged directory fsync
RENAME_NOREPLACE to canonical name
objects directory fsync
staging-root fsync
canonical exact reread
```

Normal durable new object requires:

```text
complete exact object write
final fchmod 0444
exact V11 mtime set
security + mapping + mtime verification
file fsync AFTER final metadata/mtime
RENAME_NOREPLACE into canonical fanout
fanout fsync
staging-root fsync
canonical exact reread including mtime
```

Normal durable pre-existing/winner closure leaf sealing requires:

```text
exact object/security/topology proof
exact V11 mtime set
mtime verification
file fsync AFTER mtime mutation
exact path reread
```

Normal clean preparation additionally requires durable staging-root disappearance.

Ref/reflog/worktree/index ordering remains as previously frozen.

## 59. ALIAS_SAFE_MAIN_REF_COMMITMENT_V7

Truthful `REF_COMMITTED` requires:

```text
exact effect object closure physically contained
all closure loose leaves exact + mtime-sealed under V11
all new fanouts/objects durable under V6
zero X1B staging residue at ref commitment
initial user namespace proof exact
execution credential state unchanged
reviewed mount non-ID-mapped ext4 proof exact
byte-exact namespace + inode semantics exact
main physical loose ref = exact effect SHA
main file + refs/heads durability barriers complete
canonical ref hierarchy still resolves to held identities
```

Post-ref reflog/worktree/index remain prerequisites for complete zero exit, not for the narrower truthful `REF_COMMITTED` record scope.

## 60. Outcome classes V11

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
USER_NAMESPACE_STATE_UNCERTAIN
MOUNT_IDMAP_STATE_UNCERTAIN
FILESYSTEM_SEMANTICS_UNCERTAIN
REF_COMMITTED_DURABILITY_UNCERTAIN
REF_COMMITTED_TOPOLOGY_UNCERTAIN
COMMITMENT_STATE_UNKNOWN
DURABLY_REF_COMMITTED_RECOVERY_REQUIRED
DURABLY_REF_COMMITTED_COMPLETE
```

## 61. Pre-ref outcome semantics V11

```text
DENIED:
  admission/final gate denies before preparation
  main old

BLOCKED_PROFILE_HORIZON:
  V11 mtime sentinel profile no longer applicable
  no Human-review staleness inference
  main old

BLOCKED_PRE_COMMIT_NO_OBJECT_PREP:
  main old
  no canonical new closure object/fanout installed
  no existing closure loose mtime changed
  no staging residue

BLOCKED_PRE_COMMIT_OBJECT_MTIME_SEALED_ONLY:
  main old
  one or more exact pre-existing/winner closure loose objects had mtime set to V11 sentinel
  no canonical new object/fanout necessarily installed
  no acceptance-success claim

BLOCKED_PRE_COMMIT_OBJECT_PREPARED_CLEAN:
  main old
  one or more exact unreferenced canonical closure objects/fanouts may remain
  closure leaves may carry V11 sentinel mtime
  staging root durably removed
  no worktree/index/reflog acceptance effect

BLOCKED_PRE_COMMIT_BOUND_STAGING_RESIDUE:
  main old
  exact request-bound V11 staging root may remain
  exact canonical objects + mtime seals may also exist
  residue attributable and readable
  next effect blocked pending separate recovery

OBJECT_RETENTION_METADATA_UNCERTAIN:
  loose-object content/path may be exact but V11 mtime or its file-fsync durability cannot be proven
  no ref commitment

USER_NAMESPACE_STATE_UNCERTAIN:
  initial-userns/uid_map/gid_map/credential state cannot be proven stable
  no complete-success claim

MOUNT_IDMAP_STATE_UNCERTAIN:
  exact reviewed mount ID-mapping state cannot be proven
  no complete-success claim
```

Other uncertainty states retain prior meanings.

## 62. Post-ref outcomes preserved

```text
REF_COMMITTED_DURABILITY_UNCERTAIN:
  physical main visibly equals effect SHA
  ref durability barrier not proven

REF_COMMITTED_TOPOLOGY_UNCERTAIN:
  descriptor-relative ref effect may have occurred
  canonical hierarchy relation unproven

COMMITMENT_STATE_UNKNOWN:
  exact ref state cannot be classified

DURABLY_REF_COMMITTED_RECOVERY_REQUIRED:
  main durably exact effect SHA
  one or more post-ref reflog/worktree/index projections incomplete/drifted/failed/ambiguous

DURABLY_REF_COMMITTED_COMPLETE:
  durable main exact
  every new-closure loose object exact + V11 sentinel mtime
  initial userns/credentials/mount mapping exact
  deterministic reflog exact
  canonical scene exact
  decision log exact
  full extension-free index v2 exact new_tree
  zero sharedindex.*
  zero .x1b-stage-v* residue
  all durability/security profiles exact
```

## 63. No rollback rule preserved

After visible or possible ref commitment:

```text
NO AUTOMATIC HISTORY ROLLBACK
```

Recovery authority remains separate.

## 64. Mandatory regressions — PR #135 F001 user/mount mapping

Future independent review must attack at least:

```text
child user namespace with uid_map 0 1000 1 -> BLOCK
child user namespace with apparent uid 0 -> BLOCK
noninitial user namespace with broad/identity-like map -> BLOCK by USER_NS_INIT_INO
uid_map unreadable -> BLOCK
gid_map unreadable -> BLOCK
extra uid/gid map ranges -> BLOCK
user namespace inode drift during effect -> uncertainty/block
fsuid differs from euid -> BLOCK
fsgid differs from egid -> BLOCK
credential state drift after request -> BLOCK
supplementary group list drift -> BLOCK
capability set drift -> BLOCK

statmount unsupported -> BLOCK
statmount EPERM -> BLOCK
required statmount mask missing -> BLOCK
STATMOUNT_MNT_UIDMAP unsupported -> BLOCK
STATMOUNT_MNT_GIDMAP unsupported -> BLOCK
MOUNT_ATTR_IDMAP set -> BLOCK
nonzero uid mapping -> BLOCK
nonzero gid mapping -> BLOCK
unresolved/inconsistent map report -> BLOCK
reviewed mount ID drift -> BLOCK
mount namespace ID drift -> BLOCK
filesystem not ext4 -> BLOCK
SB_RDONLY -> BLOCK
SB_LAZYTIME -> BLOCK
```

Expected: no V11 authority unless caller identity and mount identity mapping are both proven exact and stable.

## 65. Mandatory regressions — PR #135 F002 loose-object mtime

Must test at minimum:

```text
new staged object inherits current mtime before sealing
new staged object futimens -> exact sentinel
crash after fchmod before mtime seal
crash after mtime seal before file fsync
crash after file fsync before canonical rename
final canonical new loose leaf mtime exact sentinel

pre-existing exact closure loose object stale mtime -> seal to sentinel
pre-existing exact closure loose object future/other mtime -> seal to sentinel
pre-existing exact closure loose object mtime change fails -> BLOCK
pre-existing exact closure loose object fsync after mtime fails -> retention uncertainty

concurrent EEXIST exact winner arbitrary mtime -> seal to sentinel
concurrent EEXIST malformed winner -> preserve residue/block

CLOCK_REALTIME >= sentinel -> BLOCKED_PROFILE_HORIZON
atime changes do not substitute for mtime proof
ctime change from futimens is operational only
final post-effect every closure loose leaf mtime exact sentinel
```

Also regression-test exact Git 2.55 behavior relied upon by the review:

```text
stale loose-object mtime is prune-relevant
git prune compares st_mtime with expiry
bounded Git subprocess profile has gc.auto=0
bounded Git subprocess profile has maintenance.auto=false
```

## 66. Mandatory preserved regressions

Also rerun prior attack classes:

```text
casefolded .git/objects/refs/logs/worktree parents
unsupported inode flags/xflags/statx attributes
stale/malformed .x1b-stage-v* residue
crash at every staging fanout/object namespace barrier
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
loose object hardlink
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
post-fchmod durability barriers
freshness/supersession/conflict/replay
Human review author/currentness/body binding
```

R4R11 does not reopen any earlier closed property.

## 67. Required implementation helpers

Expected bounded helpers include conceptually:

```text
canonical JSON/hash/time helpers
trusted GitHub evidence pagination/currentness
admission/replay lock
Linux namespace FD identity helper
initial user namespace verifier
uid_map/gid_map canonical parser
execution credential state binder
Linux mount namespace/mountinfo verifier
statx unique mount-ID verifier
statmount non-ID-mapped mount verifier
ext4 statfs/type verifier
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

No helper may silently broaden user namespace, mount mapping, ext4, inode-flag or mtime profiles.

## 68. Documentation obligations

Authority documentation must state at minimum:

```text
current Human route = approve --decision-pr <N> only
direct legacy approve/promotion disabled
canonical effect ref = refs/heads/main
Git ref mutation = NONE
Git primary object mutation = NONE
Git real-index mutation = NONE
supported authority filesystem = Linux ext4 only
caller user namespace = initial user namespace only
ID-mapped mounts = unsupported
statmount proof required / no mountinfo-only fallback
casefold authority directories = forbidden
Linux inode semantic flags = explicitly gated
object staging = request-bound .git V11 namespace only
canonical fanout/object names = final-only
new-closure loose-object mtime = exact 2038-01-18 sentinel
pre-existing/winner closure leaves are mtime-sealed before commitment
failure mtime sealing is a truthful preparation side effect
successful pre-ref preparation leaves zero staging residue
failure staging residue blocks future effects and needs separate recovery
final security/mtime metadata precedes file fsync
split index unsupported
sharedindex.* forbidden
V11 Human marker required
```

## 69. No new implementation authority

```text
CLEAN BRIEF != IMPLEMENTATION AUTHORITY
REVIEW PASS != IMPLEMENTATION AUTHORITY
REVIEW PASS != HUMAN DECISION
IMPLEMENTATION GREEN != X1B CLOSED
X1B OPEN != V1 AUTHORITY
```

## 70. Next legal step

After this R4R11 brief is durably frozen as exactly one evidence artifact, STOP.

Next legal step:

```text
fresh Human authorization
-> one independent AK-CANON R4R11 implementation-brief review
```

That review may return PASS or NOT PASS.

It must not implement ScriptOps, create Human decision evidence, run positive control, perform canonical effect, recover state, merge, close X1B, authorize V1, release, deploy or tag.

## 71. R4R11 acceptance checklist for future independent review

A PASS review must establish all of:

```text
PR #135 F001 user/mount ID-mapping blocker addressed
PR #135 F002 loose-object mtime/pruning blocker addressed
all prior blockers remain closed
initial user namespace proof is exact and not spoofed by nested namespace mappings
uid_map/gid_map proof is complete
execution fsuid/fsgid/credential state is bound and stable
statmount exact mount proof is complete/fail-closed
MOUNT_ATTR_IDMAP is explicitly absent
mount uidmap/gidmap state is explicitly proved
no privilege/namespace transition is hidden in the proof
mtime sentinel is Human-visible and exact
sentinel representability/readback is tested
new staged objects set mtime before final file fsync
pre-existing exact closure leaves are mtime-sealed and fsynced
EEXIST winners are mtime-sealed and fsynced
all pre-ref mtime side effects are truthfully classified
Git 2.55 prune/freshen semantics are correctly modeled
bounded Git cross-checks cannot auto-maintain the repository
V10 staging/casefold/inode-flag corrections remain exact
V9 raw-index/split-index corrections remain exact
ref/reflog/worktree durability corrections remain exact
Human evidence remains separate/current/exact
```

Any ambiguity is NOT PASS.

## 72. Final R4R11 invariant summary

```text
AI PROPOSES != HUMAN DECIDES

V11 HUMAN DECISION EVIDENCE
= separate trusted current GitHub Human review
  bound to exact V11 request + exact presented material effect

V11 EXECUTION OWNERSHIP SEMANTICS
= Linux initial user namespace only
+ full identity uid_map/gid_map
+ exact stable execution credentials
+ exact statmount proof of non-ID-mapped ext4 mount

V11 FILESYSTEM AUTHORITY
= ext4 byte-exact case-sensitive authority directories
+ explicit Linux inode semantic flags
+ no unsupported mount mapping

V11 OBJECT PREPARATION
= one request-bound .git/.x1b-stage-v11-<digest> namespace
+ final-only canonical object/fanout names
+ exact Human-bound loose-object mtime sentinel
+ pre-existing/winner/new closure leaves all mtime-sealed
+ final metadata + mtime -> file fsync -> RENAME_NOREPLACE -> parent fsync
+ staging root durably removed before ref commitment

V11 LOOSE OBJECT RETENTION METADATA
= 2038-01-18T00:00:00Z exactly
= 2147385600.000000000
= Human-bound, not ambient execution time

V11 COMMITMENT
= exact descriptor-relative loose-main replacement
  final metadata -> file fsync -> rename -> refs/heads fsync

V11 POST-REF PROJECTIONS
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

R4R11 BRIEF
= REVIEW TARGET ONLY
```
