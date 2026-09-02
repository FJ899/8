# X1B HUMAN DECISION AUTHORSHIP — CLEAN IMPLEMENTATION BRIEF R4R10

Status: `CLEAN R4R10 CORRECTIVE BRIEF / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-02`

## 1. Authority, purpose, and STOP boundary

This document is the self-contained successor to R4R9 after independent AK-CANON review PR #133 returned `NOT PASS`.

It preserves the accepted X1B corrective design and every R4R9 property not rejected by PR #133, while correcting exactly the two blockers frozen by that review:

1. R4R9 constrained ordinary POSIX mode/uid/gid/xattr/ACL metadata but did not bind Linux inode semantic flags or prove byte-exact case-sensitive lookup semantics. A casefolded ext4 authority directory could therefore pass the V9 metadata checks while still resolving case-equivalent names, defeating exact pathname/no-alias and negative-namespace proofs such as `sharedindex.*`;
2. R4R9 correctly ordered successful loose-object installation but could still leave nonfinal canonical object-store residue after a crash: a missing `.git/objects/<xx>` fanout was created directly as mode `0700` before final `0755`, and private temp object leaves lived inside the canonical fanout before `RENAME_NOREPLACE`. The V9 outcome model did not completely classify those malformed/nonfinal ODB residues.

R4R10 therefore narrows the filesystem contract and changes object preparation again.

New exact profiles:

```text
LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1
LINUX_INODE_SEMANTIC_FLAGS_V1
BOUND_OBJECT_STAGING_NAMESPACE_V1
ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V3
COMPLETE_LOCAL_OBJECT_STORE_V3
CRASH_DURABLE_OBJECT_REF_INDEX_V5
ALIAS_SAFE_MAIN_REF_COMMITMENT_V6
REF_CAS_FIRST_ALIAS_SAFE_RAW_GIT_METADATA_V8
```

Preserved exact profiles include:

```text
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

The material effect and bounded failure/preparation surface change. All authority-critical schemas, request/review markers, admission identities, final-gate identities and records are therefore V10.

This document is an implementation brief only. It authorizes no ScriptOps source mutation, no Human decision PR/review, no live positive control, no canonical screenplay effect, no recovery, no merge, no X1B closure, no Agency Kernel v1, no release, deployment, or tag.

```text
R4R10 BRIEF != IMPLEMENTATION AUTHORITY
R4R10 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R10 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

After durable freeze of this brief, STOP. The next stage is one separately Human-authorized independent AK-CANON R4R10 implementation-brief review.

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

### 2.3 R4R9 predecessor

```text
FJ899/8 PR #132
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 5a05f995b296cd550e853211739be926626ee607
TREE = 68888b64ca9fa122d133279b92aa8779f4c31e67
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R9.md
BLOB = ee61ca5d540120861f4cc9f5731242cb86554c01
```

### 2.4 Binding R4R9 NOT-PASS review

```text
FJ899/8 PR #133
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = ae8d7841c0f6bbc9caebe07cd6afe56b17f453ba
TREE = 3eb96ee09f6a74a3f731893b7e874292205f2983
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R9_AK_CANON_REVIEW.md
BLOB = 855895be58e8b3d0eff569a1b5a37f0bc7904304
VERDICT = AK-CANON X1B R4R9 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #133 froze:

```text
X1B-R4R9-IBR-F001 — Linux inode semantic flags / casefold namespace are not bound
X1B-R4R9-IBR-F002 — pre-ref object-store crash residue is not closed
```

PR #133 also recorded that R4R9 addressed at brief level:

```text
X1B-R4R8-IBR-F001 post-fchmod metadata durability
X1B-R4R8-IBR-F002 split-index/sharedindex durable effect
```

and preserved all prior ref topology, primary ODB topology, hook, lazy-fetch, replacement-ref, commit-encoding, reflog, write-target alias and freshness/supersession corrections.

`REVIEW FINDING != REPAIR AUTHORITY`; R4R10 exists only under fresh Human authorization for successor brief preparation.

## 3. Exact evidence-repository base

```text
FJ899/8 main
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

No history rewrite is part of R4R10.

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

## 5. Normative precedence and V10 migration

```text
R4R10 TEXT = CURRENT IMPLEMENTATION-BRIEF AUTHORITY
R4R9 / R4R8 / R4R7 / R4R6 / R4R5 / R4R4 / R4R3 / R4R2 / R4R1 / R4 / R3 / R2 / R1 = HISTORICAL INPUT ONLY
CORRECTIVE DESIGN PR #34 = HIGHER-LEVEL PROPERTY CONTRACT
```

R4R10 changes two authority-critical surfaces:

```text
filesystem authority is narrowed to a proven Linux ext4 byte-exact namespace subset
Linux inode semantic flags and statx semantic attributes become authority-critical
canonical object-store fanout/object names are never used as nonfinal staging paths
all pre-final object bytes/directories live under one request-bound .git staging root
complete pre-ref success requires removal and durable disappearance of that staging root
crash/failure staging residue has explicit outcome and separate recovery semantics
```

Therefore:

```text
V9 REQUEST/REVIEW/ADMISSION/GATE != R4R10 AUTHORITY
V9 HUMAN REVIEW MARKER != V10 HUMAN DECISION
V10 EFFECT PROFILE REQUIRES FRESH V10 HUMAN-BOUND REQUEST
```

No V9 or earlier Human evidence may authorize a V10 effect.

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

No caller-controlled field may supply Human actor/result/rationale, request path/digest, task/scene/candidate/impact identities, canonical target/ref, filesystem namespace profile, inode semantic state, physical Git-dir/ref/object/index topology, staging namespace, metadata policy, reflog semantics, effect type, material effect, raw-object profile, hook profile, durability profile, commitment profile, or effect commit metadata.

Defect-era direct approval/promotion routes remain disabled and non-effect-capable.

## 9. Git/runtime/OS profile V10

Git semantic compatibility remains bounded to:

```text
2.55.0 <= parsed Git version < 2.56.0
object format = sha1
ref storage format = files
```

R4R10 intentionally narrows filesystem authority to:

```text
OS = Linux
filesystem = ext4
one reviewed mount for repository root and every authority-critical path
byte-exact case-sensitive authority directories
no unsupported Linux inode semantic flags
```

Required runtime primitives include:

```text
dir_fd relative open/mkdir/rmdir/unlink/rename
renameat2(RENAME_NOREPLACE)
O_NOFOLLOW
O_DIRECTORY
O_EXCL
O_CLOEXEC
fstat/lstat
statfs
statx with mount ID and semantic attribute mask
FS_IOC_GETFLAGS
FS_IOC_FSGETXATTR
fchmod
fsync regular file
fsync directory
listxattr
POSIX ACL inspection capability
/proc/self/ns/mnt
/proc/self/mountinfo
```

A platform/filesystem lacking any required proof primitive is `BLOCKED`.

No fallback to overlayfs, btrfs, xfs, tmpfs, NFS, CIFS, FUSE, vfat, ntfs, network filesystems, case-insensitive filesystems or an unknown filesystem is permitted by V10.

Successful `fsync` remains trusted only within the bounded Linux/ext4 storage contract. Hardware/firmware that falsely reports durable completion remains outside the claim.

## 10. Current semantics grounding

R4R10 freezes design around current Linux semantics checked during preparation:

```text
https://man7.org/linux/man-pages/man2/FS_IOC_SETFLAGS.2const.html
https://man7.org/linux/man-pages/man2/statx.2.html
https://www.kernel.org/doc/html/latest/admin-guide/ext4.html
https://github.com/torvalds/linux/blob/master/tools/include/uapi/linux/fs.h
https://man7.org/linux/man-pages/man2/rename.2.html
https://man7.org/linux/man-pages/man2/fsync.2.html
```

Relevant facts are treated as bounded implementation prerequisites, not as implicit runtime assumptions:

```text
FS_IOC_GETFLAGS exposes inode flags changing file/directory semantics
ext4 casefold is per-directory and changes lookup equivalence
RENAME_NOREPLACE is filesystem-dependent and fail-closed if unsupported
fsync(file) persists file data/metadata but not by itself the containing directory entry
cross-directory staging rename changes both source and destination parent namespaces
```

## 11. LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1

This is the primary correction for PR #133 F001.

For repository root and every authority-critical directory component, V10 requires all of:

```text
statfs filesystem type = EXT4_SUPER_MAGIC
/proc/self/mountinfo filesystem type = ext4
same exact reviewed mount ID
mount namespace identity stable
real directory, not symlink/reparse/redirect
no nested/bind mount at or below any authority-critical subtree
LINUX_INODE_SEMANTIC_FLAGS_V1 = PASS
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

The filesystem may have the ext4 casefold feature enabled globally; that is not sufficient to block by itself. The authority-critical requirement is that every directory participating in lookup has the casefold inode flag absent.

When `FS_CASEFOLD_FL = 0` on this bounded ext4 profile, V10 treats directory lookup as byte-exact/case-sensitive for authority proof.

No application-level `core.ignoreCase` assumption substitutes for this kernel-level proof.

## 12. Authority-critical directory closure

The byte-exact namespace proof covers every directory component needed to reach or mutate:

```text
repository root
.git
.git/objects
.git/objects/info if present
.git/objects/pack if present
all authority-relevant loose-object fanout dirs
.git/refs
.git/refs/heads
.git/logs
.git/logs/refs
.git/logs/refs/heads
candidate path parents
impact-report path parents
canonical scenes target parents
.scriptops and decision-log parent
all parents of the exact two tracked effect paths
V10 object staging root while it exists
```

If any path component lacks proof, V10 is `BLOCKED` before Human-attributed commitment.

## 13. LINUX_INODE_SEMANTIC_FLAGS_V1

Every authority-critical inode is inspected through all required Linux interfaces.

### 13.1 FS_IOC_GETFLAGS

`FS_IOC_GETFLAGS` must succeed.

For regular files, the only permitted inode-flag bit is:

```text
FS_EXTENT_FL
```

and it may be present or absent.

For directories, the only permitted inode-flag bits are:

```text
FS_EXTENT_FL
FS_INDEX_FL
```

and either/both may be present or absent.

Every other returned inode-flag bit is unsupported and therefore `BLOCKED`, including but not limited to:

```text
FS_SECRM_FL
FS_UNRM_FL
FS_COMPR_FL
FS_SYNC_FL
FS_IMMUTABLE_FL
FS_APPEND_FL
FS_NODUMP_FL
FS_NOATIME_FL
FS_DIRTY_FL
FS_COMPRBLK_FL
FS_NOCOMP_FL
FS_ENCRYPT_FL
FS_IMAGIC_FL
FS_JOURNAL_DATA_FL
FS_NOTAIL_FL
FS_DIRSYNC_FL
FS_TOPDIR_FL
FS_HUGE_FILE_FL
FS_VERITY_FL
FS_EA_INODE_FL
FS_EOFBLOCKS_FL
FS_NOCOW_FL
FS_DAX_FL
FS_INLINE_DATA_FL
FS_PROJINHERIT_FL
FS_CASEFOLD_FL
FS_RESERVED_FL
```

This deliberately chooses a narrow ext4 subset rather than trying to prove arbitrary flags benign.

### 13.2 FS_IOC_FSGETXATTR

`FS_IOC_FSGETXATTR` must succeed for every authority-critical inode.

Require exactly:

```text
fsx_xflags = 0
fsx_extsize = 0
fsx_projid = 0
fsx_cowextsize = 0
```

Read-only informational fields may be recorded but cannot broaden the profile.

Any project inheritance, DAX, realtime, extsize/COW allocation policy or unknown xflag state blocks V10.

### 13.3 statx semantic attributes

`statx` must return a usable `stx_attributes_mask` covering at least:

```text
STATX_ATTR_IMMUTABLE
STATX_ATTR_APPEND
STATX_ATTR_ENCRYPTED
STATX_ATTR_VERITY
STATX_ATTR_DAX
```

All of those supported attributes must be absent.

If the kernel/filesystem does not report whether any required attribute is supported, V10 is `BLOCKED` rather than assuming absence.

`STATX_ATTR_MOUNT_ROOT` is operational and may be present where structurally correct; it is not a permission/lookup semantic flag.

## 14. Existing POSIX metadata profile retained and nested

The R4R9 POSIX mode-only values remain mandatory in addition to the new Linux semantic proof:

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
V10 object staging root                            = 0700
staging temporary object file before final chmod   = 0600
```

Also require:

```text
uid = exact request-bound effective uid
gid = exact request-bound effective gid
no setuid/setgid/sticky bits
listxattr empty
POSIX access ACL equivalent to mode bits only
POSIX default ACL absent on writable authority-critical directories
no security capabilities / labels / arbitrary xattrs
```

The effect process sets exactly:

```text
umask = 0077
```

before any staging/effect inode creation.

## 15. Physical metadata record V10

Each authority-critical inode identity record now includes at least:

```text
path_role
st_dev
st_ino
mount_id
file_type
mode
uid
gid
nlink where meaningful
xattr_result
acl_result
fs_ioc_getflags
fsx_xflags
fsx_projid
fsx_extsize
fsx_cowextsize
statx_attributes_mask
statx_attributes
filesystem_type = ext4
byte_exact_namespace_result where directory
```

The request binds a canonical digest of this closed physical-prestate record.

No omission may be interpreted as “default benign”.

## 16. Namespace-name exactness

All authority names are raw bytes under the proven ext4 case-sensitive namespace.

V10 rejects:

```text
casefolded authority directory
Unicode-normalizing/case-insensitive lookup domain
ambiguous byte spelling
case-equivalent alias where an exact negative namespace proof is required
unknown filesystem lookup semantics
```

This applies to:

```text
refs/heads/main
logs/refs/heads/main
index
sharedindex.* negative census
objects/<two-hex>/<38-hex>
V10 staging names
scene/log target names
```

## 17. SINGLE_WORKTREE_REAL_GITDIR_V1 preserved

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

R4R10 additionally requires the entire authority closure to pass `LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1`.

## 18. PHYSICAL_PRIMARY_OBJECT_DB profile V10

The primary object database remains:

```text
.git/objects = real direct directory
held objects descriptor
same exact ext4 mount ID as .git and repository root
no nested/bind mount
no symlink/reparse redirect
GIT_OBJECT_DIRECTORY absent
GIT_ALTERNATE_OBJECT_DIRECTORIES absent
objects/info/alternates absent
no partial/promisor/lazy-fetch escape
real no-follow authority-relevant fanout directories
real no-follow regular single-link authority-relevant loose leaves
real no-follow pack/info dirs if present
```

R4R10 additionally requires:

```text
objects directory and every used fanout = byte-exact case-sensitive
all object-store inodes pass LINUX_INODE_SEMANTIC_FLAGS_V1
no unknown non-Git V10 staging entry below .git/objects
no V10 private temp leaf is ever created inside a canonical fanout
```

## 19. COMPLETE_LOCAL_OBJECT_STORE_V3

V3 preserves V2 and adds namespace/semantic-state closure.

Reject:

```text
shallow repository
grafts
replacement refs
partial clone
promisor configuration
promisor sidecars
lazy fetch requirement
objects/info/alternates
caller object-directory / alternate injection
external common object directory
symlinked primary objects directory
nested/bind-mounted object store
casefolded object-store directory
unsupported inode semantic flags
unsupported pack metadata topology
unexpected V10 staging residue
```

No fetch, deepen, repair, repack, prune or normalization is authorized.

## 20. FSYNC_AFTER_FINAL_METADATA_V1 preserved

For every file inode newly created/replaced by the V10 success path:

```text
write exact final bytes
apply every final authority-relevant inode metadata value
verify bytes + mode + uid + gid + xattr/ACL + Linux semantic flags
fsync(file_fd) AFTER the last authority-relevant inode metadata mutation
perform only a reviewed namespace operation that does not change Human-bound inode state
fsync every containing directory whose namespace changed
reopen final path no-follow and verify exact poststate
```

Directory fsync is additional to file fsync, never a substitute.

## 21. CLOSED_RAW_TREE_REWRITE_V1 preserved

The exact effect tree is derived in memory from raw parent-tree bytes.

The helper:

```text
parses canonical raw tree entries
rejects malformed / duplicate / noncanonical / unsorted entries
uses Git 2.55 tree-name ordering
rewrites only exact two target paths
uses tracked mode 100644 for both effect leaves
preserves every unrelated semantic tree entry
recursively reconstructs affected ancestor trees only
computes every tree SHA-1 from exact canonical object bytes
```

Only changed tracked paths:

```text
scenes/<scene_id>.fountain
.scriptops/decision-log.ndjson
```

## 22. CLOSED_RAW_COMMIT_OBJECT_V1 preserved

The effect commit is exact raw bytes with only:

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

Identity/time remain deterministic from the Human-bound request.

No Git commit writer is permitted.

## 23. Canonical object bytes preserved

For object type `T` and payload `P`:

```text
canonical_object_bytes = ASCII(T) + SP + ASCII(decimal(len(P))) + NUL + P
object_oid = lowercase_hex(SHA1(canonical_object_bytes))
```

Supported new object types:

```text
blob
tree
commit
```

Loose zlib representation remains storage-only/non-authority-semantic, while the production compressor/runtime identity is recorded as execution evidence.

## 24. PR #133 F002 correction — BOUND_OBJECT_STAGING_NAMESPACE_V1

R4R10 never uses a canonical `.git/objects/<xx>` directory or `<38hex>` leaf as a nonfinal staging pathname.

All nonfinal object-preparation names exist only below one request-bound staging root directly under held `.git`.

Exact staging-root derivation rule:

```text
staging_root_basename = ".x1b-stage-v10-" + request_digest
```

The request does not contain a self-referential literal pathname. It binds exactly the derivation rule:

```text
STAGING_NAME_DERIVATION_V1 = PREFIX_DOT_X1B_STAGE_V10_PLUS_REQUEST_DIGEST
```

Once `request_digest` is known, the staging name is uniquely determined.

## 25. Global staging precondition

Before request creation, admission, FinalEffectGateV10 and immediately before creating the current request's staging root, enumerate held `.git` under the byte-exact namespace and require:

```text
zero entries whose raw basename starts with ".x1b-stage-v10-"
```

Any pre-existing V10 staging residue blocks a new effect and requires separately authorized recovery/classification.

No “latest staging wins” or automatic cleanup exists.

## 26. Staging-root creation

Only after admitted Human evidence and FinalEffectGateV10:

```text
mkdirat(held_git_fd, staging_root_basename, 0700)
```

under effect umask `0077`.

`0700` is the final staging-root mode, so there is no `0700 -> 0755` metadata transition for the root itself.

Immediately:

```text
open staging root O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC
verify exact uid/gid/mode 0700
verify empty xattrs / mode-only ACL
verify LINUX_INODE_SEMANTIC_FLAGS_V1
verify ext4 mount ID exact
fsync(staging_root_fd)
fsync(held_git_fd)
```

If crash occurs before the `.git` directory fsync, the staging root may or may not survive; either state is explicitly a preparation-residue classification problem, never acceptance success.

## 27. Staging-root namespace

Only exact names are allowed inside the current staging root:

```text
fanout.<two-lowercase-hex>
object.<40-lowercase-hex>
```

No other entry is permitted.

The staging root is not part of Git's object lookup namespace.

Git commands are never pointed at it as `GIT_OBJECT_DIRECTORY` or alternate object storage.

## 28. Canonical fanout creation V10

If canonical `.git/objects/<prefix>` already exists, verify it under the existing-fanout rule and use it.

If it is absent, do NOT create it in place.

Instead:

```text
A. mkdirat(staging_root_fd, "fanout.<prefix>", 0700)
B. open staged fanout no-follow
C. fchmod(staged_fanout_fd, 0755)
D. verify exact uid/gid/mode/xattr/ACL/Linux inode flags
E. fsync(staged_fanout_fd) AFTER final metadata
F. renameat2(staging_root_fd, "fanout.<prefix>",
             held_objects_fd, "<prefix>",
             RENAME_NOREPLACE)
```

If F succeeds:

```text
fsync(held_objects_fd)
fsync(staging_root_fd)
open canonical fanout from held objects fd
verify exact 0755/ext4/flags/mount identity
```

Because the source directory reached final canonical metadata and was fsynced before rename, a crash can never expose a `0700` canonical `<prefix>` created by V10.

The only pre-rename nonfinal fanout lives below the bound staging root.

## 29. Fanout RENAME_NOREPLACE EEXIST

If final `<prefix>` appears concurrently and `RENAME_NOREPLACE` returns `EEXIST`:

```text
open/verify the winner through the existing-fanout rule
require exact byte-exact namespace and metadata profile
if winner is valid:
    rmdir exact private staged fanout
    fsync(staging_root_fd)
else:
    do not alter winner
    preserve staged residue
    return BLOCKED_PRE_COMMIT_BOUND_STAGING_RESIDUE or uncertainty
```

No canonical fanout is overwritten.

## 30. Existing fanout rule

Canonical fanout `<prefix>` must be:

```text
real directory
basename exactly two lowercase hex bytes
mode 0755
exact uid/gid
empty xattrs
mode-only ACL
same ext4 mount
LINUX_INODE_SEMANTIC_FLAGS_V1 PASS
FS_CASEFOLD_FL = 0
no nested mount
stable held objects->fanout identity
```

Any mismatch is `BLOCKED`.

## 31. Existing loose-object rule

If exact canonical `<38hex>` leaf already exists:

```text
open relative to held fanout fd O_NOFOLLOW
require regular file
st_nlink = 1
mode 0444
exact uid/gid
empty xattrs / mode-only ACL
LINUX_INODE_SEMANTIC_FLAGS_V1 PASS
same ext4 mount
inflate one complete stream with no trailing garbage
require exact canonical type/length/payload
require SHA1 = path OID
```

No overwrite or metadata normalization of a pre-existing object is authorized.

## 32. ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V3 — new object staging

If final OID leaf is absent, create only under the held staging root:

```text
staging_name = "object." + exact_40_lowercase_oid
openat(staging_root_fd, staging_name,
       O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC,
       0600)
```

Then:

```text
write one complete zlib stream inflating to exact canonical object bytes
reread/verify exact canonical bytes/type/length/OID
fchmod(temp_fd, 0444)
verify regular single-link 0444 exact uid/gid
verify xattrs/ACL
verify LINUX_INODE_SEMANTIC_FLAGS_V1
fsync(temp_fd) AFTER final metadata
```

The private staged object is now in final inode state before it is exposed at a Git object pathname.

## 33. New-object final install

Install across directories on the same reviewed ext4 mount:

```text
renameat2(staging_root_fd, "object.<oid>",
          held_fanout_fd, "<38hex>",
          RENAME_NOREPLACE)
```

On successful rename:

```text
fsync(held_fanout_fd)
fsync(staging_root_fd)
reopen final leaf O_NOFOLLOW
verify regular single-link 0444 exact uid/gid/xattr/ACL
verify Linux semantic flags
verify exact canonical object content/OID
verify canonical fanout hierarchy identity
```

Both source and destination parent namespaces are fsynced because the rename changes both.

No private temp name ever exists inside the canonical fanout.

## 34. New-object EEXIST

If `RENAME_NOREPLACE` returns `EEXIST`:

```text
do not alter winner
open/verify winner through existing-object rule
if winner exact:
    unlink exact private staged object
    fsync(staging_root_fd)
else:
    preserve staged object
    return bound-staging-residue or uncertainty
```

No overwrite is permitted.

## 35. Staging-root successful removal

Before ref commitment, after every required closure object has an exact canonical durable loose representation:

```text
enumerate staging root
require empty
fsync(staging_root_fd)
close child descriptors as appropriate
rmdirat(held_git_fd, staging_root_basename)
fsync(held_git_fd)
re-enumerate .git
require zero .x1b-stage-v10-* entries
```

Complete pre-ref preparation success requires durable disappearance of the staging root.

Thus a normal successful V10 pre-ref preparation leaves:

```text
canonical exact loose objects/fanouts only
no private staging names
no malformed canonical ODB names
```

## 36. Staging residue truth

A crash/failure before staging-root removal may leave:

```text
staging root only
staged fanout 0700 before final chmod
staged fanout 0755 before rename
staged object 0600 before final chmod
staged object 0444 after final fsync before rename
mixture of already installed exact canonical objects + remaining staged items
```

These are not Human-attributed acceptance effects because canonical `refs/heads/main` remains old.

They are persistent preparation residue and must be classified truthfully.

No new X1B effect may proceed while any `.x1b-stage-v10-*` residue exists.

## 37. Staging residue recovery boundary

The normal effect path has no generic crash-residue deletion routine.

After restart, a classifier may inspect but not mutate:

```text
exact staging-root basename
request digest encoded in basename
entry set
entry type
mode/uid/gid
Linux inode flags
object bytes where complete
corresponding canonical OID/fanout state
main ref state
```

Only separately authorized recovery may remove or complete residue.

Unknown basename, ownership, type, symlink, hardlink, unsupported flag, mount or malformed object yields:

```text
OBJECT_STAGING_STATE_UNKNOWN
```

never automatic cleanup.

## 38. New-object closure V10

Derive exact:

```text
new_object_closure = every blob/tree/commit reachable from effect commit
                     not reachable from raw request-base parent
```

Each member is exact tuple:

```text
(type, payload_length, payload_sha256, oid)
```

Every member must have an exact physically contained canonical loose representation under V3 before ref commitment.

Equivalent packed objects do not remove this requirement.

## 39. PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1 preserved under V10 namespace

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
same reviewed ext4 mount
all involved directories byte-exact case-sensitive
all involved inodes pass Linux semantic flags profile
```

## 40. ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V3 preserved

Acquire `main.lock` under held refs/heads fd:

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
verify POSIX + Linux inode semantic metadata
fsync main.lock AFTER final metadata
reread old main exact request base + LF
revalidate packed-main absence + byte-exact hierarchy
atomic descriptor-relative rename main.lock -> main
fsync held refs/heads directory
reopen main O_NOFOLLOW
verify exact final ref + metadata + inode flags + hierarchy
```

No Git ref-mutating command is permitted.

## 41. Main-ref crash residue truth preserved

A crash before ref rename may leave `refs/heads/main.lock`.

Classifier distinguishes at least:

```text
main old + main.lock absent
main old + V10-shaped main.lock present
main new
ambiguous/unreadable
```

No automatic deletion of ambiguous lock residue is authorized.

## 42. DETERMINISTIC_MAIN_REFLOG_PROJECTION_V2 preserved

Only after normal durable physical main-ref commitment:

```text
revalidate exact Human-bound reflog prestate
construct exact prior bytes + V10 line
create private temp 0600
write complete bytes
reread
fchmod 0644
verify POSIX + Linux semantic metadata
fsync temp AFTER final metadata
atomic descriptor-relative rename -> main reflog
fsync reflog parent
reopen/verify exact bytes/hash/metadata/flags
```

Exact line:

```text
<request_base_sha> <effect_commit_sha> ScriptOps X1B <scriptops-x1b@local.invalid> <request_epoch> +0000\tscriptops x1b: accept <scene_id>\n
```

## 43. FULL_SINGLE_FILE_INDEX_V1 preserved

Canonical real index prestate remains restricted to:

```text
regular single-link .git/index
mode 0644 exact uid/gid
POSIX + Linux semantic metadata profile PASS
DIRC
version exactly 2
valid trailing SHA-1
all entries canonical
stage = 0
extended flag = 0
canonical unique pathname order
no malformed padding
NO EXTENSIONS AT ALL
semantic (path,mode,oid) set exactly raw parent tree
```

No split index, sparse index, fsmonitor, untracked cache or optional extension is supported.

## 44. Shared-index negative proof V10

Under the now-proven byte-exact `.git` namespace:

```text
zero raw directory entries whose basename starts with "sharedindex."
```

Because `.git` must be ext4 case-sensitive with `FS_CASEFOLD_FL = 0`, byte enumeration and lookup now share the authority assumption that was missing in V9.

Also require:

```text
core.splitIndex absent/false
all splitIndex.* config absent
GIT_INDEX_FILE stripped
-c core.splitIndex=false for remaining Git subprocesses
```

No authority-critical Git command reads or writes the real index.

## 45. CLOSED_FULL_INDEX_V2_REWRITE_V1 preserved

Final index bytes are derived in memory from:

```text
exact Human-bound raw prestate index bytes
parsed extension-free v2 entries
exact derived new_tree
exact two changed paths
```

Existing entries preserve exact stat-cache fields and assume-valid bit while mode/OID follow new tree.

New entries use zero stat-cache fields.

Output is one extension-free v2 index with exact network-byte-order fields, NUL/padding and trailing SHA-1.

## 46. ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1 under V10 namespace

Only after durable ref commitment and exact index-prestate revalidation:

```text
require index.lock absent
require no sharedindex.*
acquire .git/index.lock 0600 under held .git fd
reread .git/index exact prestate
write exact deterministic final v2 bytes
reread/validate exact structure/checksum/new-tree semantics
fchmod 0644
verify POSIX + Linux inode semantic metadata
fsync index.lock AFTER final metadata
atomic descriptor-relative rename index.lock -> index
fsync held .git directory
reopen final index no-follow
verify exact bytes/profile/flags
require no sharedindex.*
```

`GIT_REAL_INDEX_MUTATING_COMMAND = NONE`.

## 47. ALIAS_SAFE_WORKTREE_PROJECTION_V2 under V10 namespace

Canonical scene and decision-log projections use:

```text
prove parent ext4 byte-exact topology and exact prestate
create private temp 0600 in held target parent
write complete final bytes
reread
fchmod 0644
verify POSIX + Linux inode semantic metadata
fsync temp AFTER final metadata
atomic descriptor-relative rename -> final target
fsync held parent
reopen final no-follow
verify exact bytes/hash/metadata/flags/topology
```

No in-place append is used for decision log.

## 48. Hook closure preserved

`NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1` remains mandatory.

V10 has:

```text
Git ref mutation = NONE
Git primary object mutation = NONE
Git real-index mutation = NONE
```

Remaining Git subprocesses are read-only cross-checks only.

## 49. Sanitized Git subprocess profile V10

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

Command-scope controls retain:

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
```

## 50. PresentedMaterialEffectV10

Closed schema includes at least:

```text
PresentedMaterialEffectV10 = {
  "schema_version": "scriptops-x1b-presented-material-effect/v10",
  "repository": "FJ899/scriptops",
  "scene_id": <exact scene ID>,
  "candidate_path": <exact repo-relative path>,
  "candidate_file_sha256": <exact digest>,
  "execution_identity": {
    "uid": <exact uid>,
    "gid": <exact gid>,
    "umask": "0077"
  },
  "filesystem_authority": {
    "namespace_profile": "LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1",
    "inode_semantic_profile": "LINUX_INODE_SEMANTIC_FLAGS_V1",
    "filesystem_type": "ext4",
    "casefold_allowed": false
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
    "record_schema_version": "scriptops-x1b-decision-record/v10",
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
    "gitdir_profile": "SINGLE_WORKTREE_REAL_GITDIR_V1",
    "physical_main_ref_profile": "PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1",
    "object_store_profile": "COMPLETE_LOCAL_OBJECT_STORE_V3",
    "object_install_profile": "ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V3",
    "object_staging_profile": "BOUND_OBJECT_STAGING_NAMESPACE_V1",
    "staging_name_derivation": "PREFIX_DOT_X1B_STAGE_V10_PLUS_REQUEST_DIGEST",
    "durability_order_profile": "FSYNC_AFTER_FINAL_METADATA_V1",
    "index_prestate_profile": "FULL_SINGLE_FILE_INDEX_V1",
    "index_projection_profile": "CLOSED_FULL_INDEX_V2_REWRITE_V1",
    "index_install_profile": "ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1",
    "raw_object_profile": "NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2",
    "hook_profile": "NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1",
    "commit_object_profile": "CLOSED_RAW_COMMIT_OBJECT_V1",
    "ref_cas_profile": "ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V3",
    "durability_profile": "CRASH_DURABLE_OBJECT_REF_INDEX_V5",
    "success_commitment_profile": "ALIAS_SAFE_MAIN_REF_COMMITMENT_V6",
    "effect_transport_profile": "REF_CAS_FIRST_ALIAS_SAFE_RAW_GIT_METADATA_V8",
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

## 51. PhysicalPreStateV10

Request-time physical prestate digest covers:

```text
repository root
all candidate/impact/target parent directory components
.git
.git/objects
objects/info and objects/pack if present
.git/refs
.git/refs/heads
refs/heads/main
.git/logs
.git/logs/refs
.git/logs/refs/heads
main reflog if present
.git/index
all sharedindex.* negative census evidence
all .x1b-stage-v10-* negative census evidence
```

Each record contains the V10 Linux inode semantic fields from section 15.

## 52. HumanDecisionRequestBindingV10

```text
HumanDecisionRequestBindingV10 = {
  "schema_version": "scriptops-x1b-human-decision-request/v10",
  "repository": "FJ899/scriptops",
  "repository_head_at_request": <40 lowercase hex>,
  "repository_ref_at_request": "refs/heads/main",
  "request_created_at": <exact timestamp>,
  "execution_uid": <exact uid>,
  "execution_gid": <exact gid>,
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
  "filesystem_namespace_profile": "LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1",
  "inode_semantic_profile": "LINUX_INODE_SEMANTIC_FLAGS_V1",
  "object_staging_profile": "BOUND_OBJECT_STAGING_NAMESPACE_V1",
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect": <PresentedMaterialEffectV10>
}
```

```text
request_digest = sha256_canonical(binding)
decision_request_id = "x1b:" + request_digest
```

## 53. Proposal PR and V10 Human review marker

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
X1B-HUMAN-DECISION-V10
decision_request_id=<exact x1b:<request_digest>>
decision_request_sha256=<exact request_digest>
why=<Human rationale>
```

Four LF-separated lines, no trailing LF.

V9 or earlier review markers are invalid for V10.

## 54. Trusted GitHub evidence and freshness preserved

Public exact-origin GitHub evidence transport, complete review pagination, current-head binding, duplicate ambiguity, active CHANGES_REQUESTED handling, no-latest-wins semantics, exact proposal envelope, replay lock and freshness/supersession rules remain as R4R9 with V10 schema identities.

```text
NO WALL-CLOCK TTL
AGE ALONE != STALE
```

## 55. X1BDecisionRecordV10

Record includes at least:

```text
schema_version = scriptops-x1b-decision-record/v10
result = REF_COMMITTED
result_scope = PHYSICAL_LOOSE_REFS_HEADS_MAIN_POINTS_TO_EXACT_EFFECT_COMMIT
decision_type = scene_acceptance_ref_committed
exact request/review/admission/currentness identities
exact scene/candidate/impact identities
ref_before
execution uid/gid
main reflog prestate
full index prestate
canonical before/after digests
presented material effect digest
filesystem_namespace_profile = LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1
inode_semantic_profile = LINUX_INODE_SEMANTIC_FLAGS_V1
object_store_profile = COMPLETE_LOCAL_OBJECT_STORE_V3
object_staging_profile = BOUND_OBJECT_STAGING_NAMESPACE_V1
object_install_profile = ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V3
durability_order_profile = FSYNC_AFTER_FINAL_METADATA_V1
index profiles from V9
ref/reflog/worktree profiles from V9
durability_profile = CRASH_DURABLE_OBJECT_REF_INDEX_V5
success_commitment_profile = ALIAS_SAFE_MAIN_REF_COMMITMENT_V6
canonical_instance_scope = LOCAL_EXT4_BYTE_EXACT_MAIN_OBJECT_DB_FULL_INDEX_WORKTREE_DECISION_LOG_REFLOG_V10
```

The record still says `REF_COMMITTED`, not generic success.

## 56. FinalEffectGateV10

Immediately before deterministic record/object derivation, while the same-worktree exclusive X1B lock is held, freshly validate:

```text
exact V10 PR/request/review envelope
Human currentness/conflicts
CompleteReviewSetV10 digest
raw logical main SHA = request base
SINGLE_WORKTREE_REAL_GITDIR_V1
LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1 over full authority closure
LINUX_INODE_SEMANTIC_FLAGS_V1 over full authority closure
PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1
COMPLETE_LOCAL_OBJECT_STORE_V3
FSYNC_AFTER_FINAL_METADATA_V1 capability
FULL_SINGLE_FILE_INDEX_V1 exact
no sharedindex.*
zero .x1b-stage-v10-* entries
core.splitIndex absent/false
MainReflogPreStateV2 exact
mount namespace/mountinfo ext4 containment exact
Git 2.55.x
files ref format
NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2
NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1
zero refs/replace
raw parent commit/tree
candidate/impact/canonical prestate
accepted preview
PresentedMaterialEffectV10
replay state
raw full-index semantic tree = raw parent tree
verified empty hook directory
renameat2(RENAME_NOREPLACE) supported on reviewed ext4 mount
```

After gate:

```text
no user interaction
no network
no sleep/wait
no unrelated blocking operation
no proposal/review mutation
no untrusted subprocess
no Git ref mutation
no Git primary object mutation
no Git real-index read or mutation
```

## 57. Exact local effect sequence V10

With X1B lock held after FinalEffectGateV10:

```text
A. re-prove raw-object, ext4 byte-exact namespace, Linux inode semantic,
   complete-local-store, ref/reflog/index profiles and zero stale staging

B. construct X1BDecisionRecordV10 bytes in memory

C. construct exact accepted-scene and decision-log payloads in memory
   compute exact blob canonical bytes/OIDs

D. execute CLOSED_RAW_TREE_REWRITE_V1
   derive exact affected tree payloads/OIDs
   prove exact two-path semantic delta

E. construct exact CLOSED_RAW_COMMIT_OBJECT_V1 in memory
   compute exact effect commit SHA

F. derive exact new_object_closure tuples

G. create exact request-bound .git staging root 0700
   verify ext4 byte-exact + Linux inode semantic profile
   fsync staging root and .git

H. for each missing canonical fanout:
   build/finalize/fsync fanout under staging root
   RENAME_NOREPLACE into .git/objects/<xx>
   fsync objects and staging root
   verify canonical fanout

I. for each missing closure object:
   build/finalize/fsync object under staging root
   RENAME_NOREPLACE into held canonical fanout
   fsync fanout and staging root
   verify canonical object

J. verify every closure member exact/contained/durable
   require staging root empty
   fsync staging root
   rmdir exact staging root
   fsync .git
   require zero .x1b-stage-v10-* entries

K. cross-check installed commit/tree/object closure with object-only read-only Git plumbing
   no index access

L. derive exact deterministic final raw index bytes in memory

M. final pre-ref checks:
   physical main exact old SHA
   packed main absent
   byte-exact ref hierarchy exact
   ext4/Linux semantic flags exact
   every closure object exact/contained/durable
   no staging residue
   reflog prestate exact
   raw full index exact unchanged
   no sharedindex.*
   mount namespace/mount IDs exact
   hook census empty

N. acquire main.lock descriptor-relative O_EXCL/O_NOFOLLOW
   repeat old-value/topology/metadata/flag proof

O. write exact effect SHA + LF
   fchmod 0644
   verify POSIX + Linux semantic metadata
   fsync main.lock AFTER final metadata
   final old-main proof

P. atomic descriptor-relative rename main.lock -> main
   fsync refs/heads
   classify physical ref result

Q. after normal durable ref commitment:
   execute deterministic main reflog V2

R. project canonical scene through worktree projection V2

S. project decision log through worktree projection V2

T. replace raw canonical full v2 index through ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1

U. verify physical/logical ref, raw commit/tree/object closure,
   ext4 byte-exact namespace, Linux inode semantic states,
   zero staging residue, reflog, worktree, full index, zero sharedindex,
   mount identity and security metadata

V. release X1B lock only after final outcome class is determined
```

No canonical worktree, decision-log, reflog or real-index mutation occurs before physical main-ref commitment.

Exact loose objects/fanouts may become canonical before ref commitment and are reported as preparation effects.

## 58. CRASH_DURABLE_OBJECT_REF_INDEX_V5

Normal durable new-fanout preparation requires:

```text
staged fanout reaches final 0755 + Linux semantic profile
staged fanout fsync after final metadata
RENAME_NOREPLACE into canonical objects namespace
objects directory fsync
staging-root directory fsync
canonical fanout exact reread
```

Normal durable new-object preparation requires:

```text
staged object complete write
exact content reread
final fchmod 0444
exact POSIX + Linux semantic metadata verification
file fsync after final metadata
RENAME_NOREPLACE into canonical fanout
fanout fsync
staging-root fsync
final exact no-follow reread
```

Normal clean preparation additionally requires:

```text
staging root empty
staging root fsync
rmdir staging root
.git directory fsync
zero staging namespace entries
```

Ref/reflog/worktree/index durability ordering remains V9.

## 59. ALIAS_SAFE_MAIN_REF_COMMITMENT_V6

Truthful `REF_COMMITTED` requires:

```text
exact effect object closure physically contained
all canonical new objects/fanouts durable under V5
zero V10 staging residue at the instant of ref commitment
full ext4 byte-exact authority namespace proof still valid
Linux inode semantic flags proof still valid
main physical loose ref = exact effect SHA
main file + refs/heads dir durability barriers complete
canonical ref hierarchy still resolves to held identities
```

Post-ref reflog/worktree/index remain prerequisites for complete zero exit, not for the narrower `REF_COMMITTED` record scope.

## 60. Outcome classes V10

Implementation must distinguish at least:

```text
DENIED
BLOCKED_PRE_COMMIT_NO_OBJECT_PREP
BLOCKED_PRE_COMMIT_OBJECT_PREPARED_CLEAN
BLOCKED_PRE_COMMIT_BOUND_STAGING_RESIDUE
BLOCKED_PRE_COMMIT_REF_LOCK_RESIDUE
OBJECT_STAGING_STATE_UNKNOWN
OBJECT_STORE_DURABILITY_UNCERTAIN
OBJECT_STORE_TOPOLOGY_UNCERTAIN
FILESYSTEM_SEMANTICS_UNCERTAIN
REF_COMMITTED_DURABILITY_UNCERTAIN
REF_COMMITTED_TOPOLOGY_UNCERTAIN
COMMITMENT_STATE_UNKNOWN
DURABLY_REF_COMMITTED_RECOVERY_REQUIRED
DURABLY_REF_COMMITTED_COMPLETE
```

## 61. Outcome semantics — pre-ref

```text
DENIED:
  gate/admission denied before preparation
  main old

BLOCKED_PRE_COMMIT_NO_OBJECT_PREP:
  main old
  no canonical new closure object/fanout durably installed
  no V10 staging residue

BLOCKED_PRE_COMMIT_OBJECT_PREPARED_CLEAN:
  main old
  one or more exact canonical unreferenced closure objects/fanouts may remain
  staging root durably removed
  no canonical worktree/index/reflog effect

BLOCKED_PRE_COMMIT_BOUND_STAGING_RESIDUE:
  main old
  exact request-bound .x1b-stage-v10-<request_digest> may remain
  canonical exact objects may also have been installed
  residue shape is readable and attributable to this V10 request
  no acceptance-success claim
  next effect blocked until separate recovery

OBJECT_STAGING_STATE_UNKNOWN:
  main old unless separately proven otherwise
  staging namespace exists but identity/content/topology cannot be classified exactly
  no cleanup
  preserve evidence

OBJECT_STORE_DURABILITY_UNCERTAIN:
  canonical fanout/object visible but one or more required source/destination directory fsync barriers not proven
  main old unless separately proven otherwise
  no acceptance-success claim

OBJECT_STORE_TOPOLOGY_UNCERTAIN:
  object preparation target/canonical hierarchy relationship uncertain
  preserve evidence

FILESYSTEM_SEMANTICS_UNCERTAIN:
  ext4/type/casefold/inode-flag/statx proof became unavailable or changed
  no complete-success claim
```

## 62. Post-ref outcome semantics preserved

```text
REF_COMMITTED_DURABILITY_UNCERTAIN:
  physical main visibly equals effect SHA
  ref durability barrier not proven
  no complete success

REF_COMMITTED_TOPOLOGY_UNCERTAIN:
  descriptor-relative ref effect may have occurred
  canonical hierarchy relationship unproven

COMMITMENT_STATE_UNKNOWN:
  exact ref state cannot be classified
  preserve evidence

DURABLY_REF_COMMITTED_RECOVERY_REQUIRED:
  main durably exact effect SHA
  one or more reflog/worktree/index projections incomplete/drifted/failed/ambiguous
  no rollback

DURABLY_REF_COMMITTED_COMPLETE:
  durable main exact
  deterministic reflog exact
  canonical scene exact
  decision log exact
  full extension-free index v2 exact new_tree
  zero sharedindex.*
  zero V10 staging residue
  ext4 byte-exact namespace proof exact
  Linux inode semantic state exact
  all durability/security profiles exact
```

## 63. No rollback preserved

After visible or possible ref commitment:

```text
NO AUTOMATIC HISTORY ROLLBACK
```

Recovery authority remains separate.

## 64. Mandatory regressions — PR #133 F001

Future independent review must attack at least:

```text
repository on overlayfs -> BLOCK
repository on btrfs -> BLOCK
repository on xfs -> BLOCK
repository on tmpfs -> BLOCK
repository on NFS/CIFS/FUSE/vfat -> BLOCK
unknown filesystem type -> BLOCK
FS_IOC_GETFLAGS unsupported -> BLOCK
FS_IOC_FSGETXATTR unsupported -> BLOCK
required statx attribute mask incomplete -> BLOCK

ext4 .git with FS_CASEFOLD_FL -> BLOCK
ext4 objects with FS_CASEFOLD_FL -> BLOCK
ext4 refs/heads with FS_CASEFOLD_FL -> BLOCK
ext4 logs/refs/heads with FS_CASEFOLD_FL -> BLOCK
ext4 worktree target parent with FS_CASEFOLD_FL -> BLOCK
casefold alias SHAREDINDEX.<hash> vs sharedindex.<hash> -> BLOCK before authority

FS_IMMUTABLE_FL -> BLOCK
FS_APPEND_FL -> BLOCK
FS_SYNC_FL -> BLOCK
FS_DIRSYNC_FL -> BLOCK
FS_NOCOW_FL -> BLOCK
FS_DAX_FL -> BLOCK
FS_VERITY_FL -> BLOCK
FS_ENCRYPT_FL -> BLOCK
FS_PROJINHERIT_FL -> BLOCK
FS_INLINE_DATA_FL -> BLOCK
unknown FS_IOC_GETFLAGS bit -> BLOCK
nonzero fsx_xflags -> BLOCK
nonzero fsx_projid -> BLOCK
nonzero fsx_extsize/cowextsize -> BLOCK
STATX_ATTR_IMMUTABLE/APPEND/ENCRYPTED/VERITY/DAX -> BLOCK
```

Allowed ordinary ext4 storage flags must be tested exactly:

```text
regular file: subset of {FS_EXTENT_FL}
directory: subset of {FS_EXTENT_FL, FS_INDEX_FL}
```

No other bit is silently tolerated.

## 65. Mandatory regressions — PR #133 F002

Must fault-inject at least:

```text
crash after staging-root mkdir before .git fsync
crash after staging-root fsync before first child
crash after staged fanout mkdir 0700 before fchmod
crash after staged fanout fchmod before staged-fanout fsync
crash after staged-fanout fsync before rename
crash after fanout rename before objects fsync
crash after objects fsync before staging-root fsync
concurrent canonical fanout EEXIST valid winner
concurrent canonical fanout EEXIST invalid winner

crash after staged object create 0600 before write
crash during staged object write
crash after write before fchmod
crash after fchmod before file fsync
crash after file fsync before final rename
crash after object rename before fanout fsync
crash after fanout fsync before staging-root fsync
object EEXIST exact concurrent winner
object EEXIST malformed concurrent winner

crash while staging root nonempty
crash after staging root becomes empty before rmdir
crash after rmdir before .git fsync
stale .x1b-stage-v10-* before new request
malformed staging basename
staging symlink
staging hardlinked file
staging unknown child
staging inode semantic flag mismatch
```

Expected:

```text
never expose V10-created canonical fanout as 0700
never expose private object temp name inside canonical fanout
normal clean pre-ref state has zero staging residue
all surviving staging residue is explicit outcome/recovery state
unknown residue is never auto-deleted
no new effect starts over stale staging
```

## 66. Mandatory preserved regressions

Also rerun all earlier attack classes:

```text
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
post-fchmod crash barriers
freshness/supersession/conflict/replay
Human review author/currentness/body binding
```

R4R10 does not reopen any earlier closed property.

## 67. Required implementation helpers

Expected bounded helpers include conceptually:

```text
canonical JSON/hash/time helpers
trusted GitHub evidence pagination/currentness
admission/replay lock
Linux mount namespace/mountinfo verifier
ext4 statfs/type verifier
FS_IOC_GETFLAGS verifier
FS_IOC_FSGETXATTR verifier
statx semantic-attribute verifier
LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1 walker
held descriptor identity helpers
POSIX mode/uid/gid/xattr/ACL verifier
single-worktree real-gitdir verifier
physical loose-main-ref verifier
COMPLETE_LOCAL_OBJECT_STORE_V3 verifier
raw object parser/hasher
closed raw tree rewrite
closed raw commit writer/verifier
BOUND_OBJECT_STAGING_NAMESPACE_V1 manager
ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V3
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

No helper may silently broaden the ext4 or inode-flag profile.

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
casefold authority directories = forbidden
Linux inode semantic flags = explicitly gated
object staging = request-bound .git namespace only
canonical fanout/object names are final-only
successful pre-ref preparation leaves zero staging residue
failure staging residue blocks future effects and needs separate recovery
final security metadata precedes file fsync
split index unsupported
sharedindex.* forbidden
V10 Human marker required
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

After this R4R10 brief is durably frozen as exactly one evidence artifact, STOP.

Next legal step:

```text
fresh Human authorization
-> one independent AK-CANON R4R10 implementation-brief review
```

That review may return PASS or NOT PASS.

It must not implement ScriptOps, create Human decision evidence, run positive control, perform canonical effect, recover state, merge, close X1B, authorize V1, release, deploy or tag.

## 71. R4R10 acceptance checklist for future independent review

A PASS review must establish all of:

```text
PR #133 F001 inode-semantic/casefold blocker addressed
PR #133 F002 pre-ref ODB crash-residue blocker addressed
all prior blockers remain closed
filesystem narrowing to ext4 is explicit and enforceable
case-sensitive byte-exact directory semantics proven for every authority component
FS_IOC_GETFLAGS allowed-bit policy complete/fail-closed
FS_IOC_FSGETXATTR policy complete/fail-closed
statx semantic attributes complete/fail-closed
no casefold alias can bypass sharedindex/object/ref negative census
no private temp lives under canonical ODB fanout
no V10-created canonical fanout is visible before final metadata+fsync
cross-directory source and destination parents both get durability barriers
staging name uniquely request-bound
clean preparation removes staging root durably before ref commitment
all crash residue outcome classes truthful
stale/unknown staging blocks new effects
recovery remains separately authorized
raw index V9 corrections remain exact
ref/reflog/worktree durability corrections remain exact
Human evidence remains separate/current/exact
```

Any ambiguity is NOT PASS.

## 72. Final R4R10 invariant summary

```text
AI PROPOSES != HUMAN DECIDES

V10 HUMAN DECISION EVIDENCE
= separate trusted current GitHub Human review
  bound to exact V10 request + exact presented material effect

V10 FILESYSTEM AUTHORITY
= Linux ext4 only
+ byte-exact case-sensitive authority directories
+ explicit FS_IOC_GETFLAGS / FSGETXATTR / statx semantic proof

V10 OBJECT PREPARATION
= one request-bound staging root under .git
+ nonfinal fanout/object names only inside staging
+ final metadata -> file/dir fsync
+ RENAME_NOREPLACE into canonical ODB
+ source and destination parent fsync
+ exact final reread
+ staging root durably removed before ref commitment

V10 COMMITMENT
= exact descriptor-relative loose-main replacement
  final metadata -> file fsync -> rename -> refs/heads fsync

V10 POST-REF PROJECTIONS
= deterministic reflog
+ alias-safe scene/log materialization
+ deterministic extension-free full index-v2 replacement

SPLIT INDEX
= unsupported

sharedindex.*
= forbidden under proven byte-exact namespace

GIT REF WRITER
= NONE

GIT PRIMARY OBJECT WRITER
= NONE

GIT REAL INDEX WRITER
= NONE

R4R10 BRIEF
= REVIEW TARGET ONLY
```
