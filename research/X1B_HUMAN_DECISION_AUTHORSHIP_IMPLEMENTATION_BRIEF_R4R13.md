# X1B HUMAN DECISION AUTHORSHIP — CLEAN IMPLEMENTATION BRIEF R4R13

Status: `CLEAN R4R13 CORRECTIVE BRIEF / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-02`

## 1. Authority, purpose, and STOP boundary

This document is the self-contained successor implementation brief after independent AK-CANON review PR #139 returned `NOT PASS` on R4R12.

It preserves the accepted X1B corrective-design properties and every R4R12 mechanism not rejected by PR #139, while correcting the two exact blockers frozen by that review:

1. `X1B-R4R12-IBR-F001`: R4R12 proved ext4 mount/runtime durability state but did not prove that the primary block device below ext4 belongs to a reviewed persistent-storage class. RAM-backed devices such as zram/ramdisk could satisfy filesystem-level predicates while remaining volatile across reboot or power loss;
2. `X1B-R4R12-IBR-F002`: R4R12 required an ext4 journal but did not prove that the journal is internal. An external ext4 journal creates a second JBD2 write/durability domain that R4R12 did not identify or bind.

R4R13 deliberately chooses narrow positive profiles rather than attempting to classify every Linux block stack:

```text
AUTHENTIC_BLOCK_DEVICE_SYSFS_V1
ACPI_NFIT_PMEM_PERSISTENT_BLOCK_V1
EXT4_INTERNAL_JOURNAL_SUPERBLOCK_V1
EXT4_RUNTIME_OPTION_TABLE_V13
EXT4_BARRIERED_FSYNC_DURABILITY_V2
CRASH_DURABLE_OBJECT_REF_INDEX_V8
ALIAS_SAFE_MAIN_REF_COMMITMENT_V9
REF_CAS_FIRST_ALIAS_SAFE_RAW_GIT_METADATA_V11
```

Preserved profiles include:

```text
AUTHENTIC_CURRENT_TASK_PROCFS_V1
LINUX_INITIAL_USER_NAMESPACE_V2
LINUX_EXECUTION_CREDENTIAL_STATE_V2
LINUX_NON_IDMAPPED_EXT4_MOUNT_V2
AUTHENTIC_EXT4_RUNTIME_STATE_V1
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

Because storage persistence class, raw journal topology and ext4 option classification are authority-critical, all request/review/admission/gate/material-effect/decision-record schemas are V13.

This document is an implementation brief only. It authorizes no ScriptOps source mutation, no independent R4R13 review, no Human decision evidence creation, no positive control, no canonical screenplay effect, no recovery mutation, no merge, no X1B closure, no Agency Kernel v1, no release, deployment, or tag.

```text
R4R13 BRIEF != IMPLEMENTATION AUTHORITY
R4R13 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R13 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

After durable freeze of this brief, STOP. The next legal stage is one separately Human-authorized independent AK-CANON R4R13 implementation-brief review.

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

### 2.3 R4R12 predecessor

```text
FJ899/8 PR #138
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = b960778d5f33ba0b3a5beb74a5bb08107afa40f9
TREE = 112129e06f5484e33984521816b0aec52ae69d63
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R12.md
BLOB = 6e1dfb2342a7a97d5a3adbc2992bb8bb19fb121d
```

### 2.4 Binding R4R12 NOT-PASS review

```text
FJ899/8 PR #139
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 7fecd3dccd436ea916c3f460eaa4e3bb0f3a7eec
TREE = edd0cad9f9eefb3c310b45c1a29af465613dd824
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R12_AK_CANON_REVIEW.md
BLOB = 9168c241d3c40e5eb4e34dc4baa6792af4b352da
VERDICT = AK-CANON X1B R4R12 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #139 froze:

```text
X1B-R4R12-IBR-F001 — backing block-device persistence topology is not bound
X1B-R4R12-IBR-F002 — external ext4 journal write domain is not bound
```

PR #139 also recorded:

```text
PR #137 F001 procfs authority provenance   = ADDRESSED AT BRIEF LEVEL
PR #137 F002 ext4 durability mount options = ADDRESSED AT BRIEF LEVEL
```

PR #139 noted that R4R12 referred to a reviewed ext4 option table without enumerating that table. R4R13 freezes an explicit V13 table below; implementation may not invent a broader allowlist.

## 3. Exact frozen repository state

Immediately before R4R13 preparation:

```text
FJ899/8 main
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

Frozen ScriptOps baseline:

```text
FJ899/scriptops main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Security-relevant baseline BLOBs remain:

```text
phase6/scriptops-v2-hardening.py                  4f379960ed5677634dd234af6aa39626782b6133
legacy/scriptops-v2-single.py                     9baa7b3a1eb746e34b79207a382eea1f5dd4ec55
phase6/bounded-proposal-view.py                   27f50f0df85fe6b66cfd3c33be00c6d975762b45
scripts/restore_v2.py                             fa2099d7d4530bce2256051690935625dab0e927
scripts/verify_repository.py                      a61278086b92824d7e442b390c951e918c88517b
sources/prototype/RESTORE.md                      8a79aca4c93b23c4842792bea9ecaae146e1fc48
SOURCE_MANIFEST.md                                2acf2ece298bfcf89254087c9e747fcb808ab241
README.md                                         c52f515dd3d736c749eca75cf319b514f8427c5a
PROJECT_STATE.md                                  dea1d11c847765026f8766fa70aa111c3f77c7bd
HANDOFF.md                                        2e0c3be2a9bdebfeac161773ca9631f8312f42f6
tests/test_phase6_scriptops_smoke.py              d6065047268cee5591883a3065ce49886ec85bcf
.github/workflows/phase6-scriptops-smoke.yml      a811dc75b4d3c7a1ebd8375c24fc71c74586ddf5
.github/workflows/verify-repository.yml           7d896d425012479c97bf1e6539f9a861a4a17aa5
```

Historical prototype reconstruction remains immutable evidence with SHA-256 `881dade6c6c506b9a9d41ebfbf68afb18b66db7583d35f746fb29ed7b36ac596`, size `51980` bytes.

## 4. Normative precedence and V13 migration

```text
R4R13 TEXT = CURRENT IMPLEMENTATION-BRIEF AUTHORITY
R4R12 AND EARLIER IMPLEMENTATION BRIEFS = HISTORICAL INPUT ONLY
CORRECTIVE DESIGN PR #34 = HIGHER-LEVEL PROPERTY CONTRACT
```

Authority-critical changes in V13:

```text
primary repository storage class is explicit
primary block-device sysfs provenance is explicit
only one narrow ACPI NFIT PMEM block profile is supported
RAM-backed and other unreviewed block stacks are unsupported
ext4 journal location is raw-superblock-bound
external ext4 journals are unsupported
full ext4 runtime option classification is frozen
storage topology/health drift is authority-relevant
```

Therefore:

```text
V12 REQUEST/REVIEW/ADMISSION/GATE != V13 AUTHORITY
V12 HUMAN REVIEW MARKER != V13 HUMAN DECISION
V13 EFFECT PROFILE REQUIRES FRESH V13 HUMAN-BOUND REQUEST
```

No V12 or earlier Human evidence may authorize a V13 effect.

## 5. Future bounded implementation surface

Expected implementation surface remains exactly:

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

## 6. Core Human-decision rule

```text
HumanDecision = TRUE
ONLY IF
separate trusted Human decision evidence
for exact current content + scope + candidate + material effect
is independently validated and admitted.
```

Never sufficient by itself:

```text
approval-command possession
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
storage capability
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

## 7. Exactly one current acceptance interface

After future implementation, the only current effect-capable Human-decision acceptance interface remains:

```text
python phase6/scriptops-v2-hardening.py approve --decision-pr <positive-integer>
```

PR number is a locator only, never authority.

No caller-controlled field may supply Human actor/result/rationale, request identity, candidate identity, effect identity, proc/sysfs provenance, storage topology, block-device identity, NFIT health, ext4 raw-superblock journal identity, mount-option state, loose-object mtime, Git ref/index/object topology, or effect commit metadata.

# PART I — V13 PLATFORM AND PRESERVED KERNEL AUTHORITY

## 8. V13 supported platform

Git semantic compatibility remains:

```text
2.55.0 <= parsed Git version < 2.56.0
object format = sha1
ref storage format = files
```

V13 platform is deliberately narrow:

```text
OS = Linux
repository filesystem = ext4
repository source = direct whole /dev/pmem<N> block device only
primary backing profile = ACPI_NFIT_PMEM_PERSISTENT_BLOCK_V1
no partition
no loop/device-mapper/md/network/virtio/xen/zram/ramdisk/NVMe/SCSI/SATA/CXL/E820/manual-memmap/test PMEM
one reviewed repository mount for all authority-critical repository paths
caller user namespace = Linux initial user namespace
repository mount = not ID-mapped
current-task proc authority = authenticated genuine procfs
sysfs authority = authenticated genuine sysfs
ext4 journal = internal reserved inode on primary filesystem only
ext4 barrier = enabled
ext4 data mode = ordered or journal
ext4 journal_async_commit = disabled
ext4 DAX = disabled
ext4 error state = zero
```

If a required primitive/source is unavailable, unreadable, unsupported, ambiguous, blocked by seccomp/LSM/containerization, or inconsistent, V13 is `BLOCKED`.

V13 MUST NOT acquire privilege, use `sudo`, call `setns`/`unshare`, mount/remount anything, alter block topology, reconfigure NVDIMMs, clear NVDIMM health state, alter ext4 journal/options, clear ext4 errors, or modify procfs/sysfs.

## 9. AUTHENTIC_CURRENT_TASK_PROCFS_V1 preserved

Authority begins from a held genuine `/proc` descriptor:

```text
fstatfs = PROC_SUPER_MAGIC
unique proc mount ID exact
statmount fs_type = proc
```

Bind direct kernel `getpid()` and `gettid()` values and require genuine procfs `thread-self` target exactly `<tgid>/task/<tid>`.

All current-task authority reads use numeric descriptor-relative paths from the held proc root with:

```text
RESOLVE_BENEATH
RESOLVE_NO_XDEV
RESOLVE_NO_SYMLINKS
```

Every authority object remains on the same procfs mount ID. Any bind/submount crossing or source drift is `BLOCKED`/uncertain.

## 10. LINUX_INITIAL_USER_NAMESPACE_V2 preserved

From authenticated current-thread procfs `ns/user` require exact initial user-namespace identity:

```text
USER_NS_INIT_INO = 4026531837
```

Authenticated current-process `uid_map` and `gid_map` must each semantically equal exactly one range:

```text
0 0 4294967295
```

No substituted namespace/map file is accepted.

## 11. LINUX_EXECUTION_CREDENTIAL_STATE_V2 preserved

Bind/revalidate:

```text
ruid/euid/suid/fsuid
rgid/egid/sgid/fsgid
supplementary groups
CapInh
CapPrm
CapEff
CapBnd
CapAmb
NoNewPrivs
```

Require:

```text
ruid = euid = suid = fsuid = execution_uid
rgid = egid = sgid = fsgid = execution_gid
```

Direct-syscall and authenticated-proc views must agree.

## 12. LINUX_NON_IDMAPPED_EXT4_MOUNT_V2 preserved

Obtain exact repository unique mount ID from authority-root descriptors and `statx`, then query that mount using `statmount` with at least:

```text
SB_BASIC
MNT_BASIC
FS_TYPE
MNT_NS_ID
MNT_UIDMAP
MNT_GIDMAP
SUPPORTED_MASK
MNT_OPTS
OPT_ARRAY
SB_SOURCE
MNT_ROOT
```

Require:

```text
fs_type = ext4
sb_magic = EXT4_SUPER_MAGIC
MOUNT_ATTR_RDONLY = 0
MOUNT_ATTR_IDMAP = 0
SB_RDONLY = 0
SB_LAZYTIME = 0
mnt_uidmap_num = 0
mnt_gidmap_num = 0
```

No mountinfo-only fallback is authorized.

# PART II — PR #139 F001: PRIMARY PERSISTENT STORAGE

## 13. Correction strategy

R4R13 does not infer persistence from a `/dev` name, ext4, barriers or successful `fsync` alone.

The only supported positive primary-storage class is:

```text
ACPI_NFIT_PMEM_PERSISTENT_BLOCK_V1
```

All other block-device classes are unsupported in V13 even if they may be durable in real deployments.

## 14. AUTHENTIC_BLOCK_DEVICE_SYSFS_V1

R4R12 already authenticates a held `/sys` root using:

```text
open("/sys", O_PATH|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC)
fstatfs(sys_root_fd).f_type = SYSFS_MAGIC
unique sysfs mount ID exact
statmount(unique-id).fs_type = sysfs
```

Retain this descriptor throughout the effect.

For repository `statmount` values:

```text
sb_dev_major = M
sb_dev_minor = m
sb_source = /dev/pmem<N>
```

open the exact source path read-only with `O_NOFOLLOW|O_CLOEXEC` and require:

```text
final object = block special
fstat(source_fd).st_rdev major = M
fstat(source_fd).st_rdev minor = m
```

A same-looking path with different `st_rdev` is invalid. Semantic identity is major/minor, not pathname spelling.

## 15. Exact block identity through authenticated sysfs

Read `/sys/dev/block/M:m` from the authenticated sysfs root. The symlink source itself must be on the authenticated sysfs mount.

Parse its target canonically as a relative target resolving beneath `devices/`. Resolve/open the resulting physical object from held sysfs root with:

```text
RESOLVE_BENEATH
RESOLVE_NO_XDEV
RESOLVE_NO_SYMLINKS
```

Every authority-critical descendant subsequently read must remain on that same authenticated sysfs mount.

Bind at least:

```text
raw /sys/dev/block/M:m link target
canonical devices/... target
block basename
major/minor
size
ro
queue/logical_block_size
queue/physical_block_size
queue/write_cache when exposed
queue/fua when exposed
queue/dax when exposed
```

Submount/bind replacement, unresolved symlink ambiguity, alternate filesystem or identity drift is `BLOCKED`.

## 16. Exact source spelling / whole-device rule

Require exactly:

```text
sb_source = /dev/pmem<N>
```

where `<N>` is canonical unsigned decimal with no sign and no leading zero except exactly `0`.

The canonical sysfs block basename must equal `pmem<N>`.

Reject partitions and all aliases, including `/dev/pmem<N>p<M>`.

## 17. ACPI_NFIT_PMEM_PERSISTENT_BLOCK_V1 provider provenance

The physical block target must belong to one LIBNVDIMM PMEM namespace and region under an ACPI NFIT bus.

Require exact current-kernel authority fields:

```text
region devtype raw semantic value = nd_pmem
region nfit/range_index exists
region nfit/range_index = canonical positive u32
region nfit/range_index != 0
ndbus nfit/revision exists and parses canonically
ndbus provider raw semantic value = ACPI.NFIT
```

There is no alternative “SPA index” field in V13 authority. `regionX/nfit/range_index` is the one reviewed NFIT address-range identifier.

The canonical physical sysfs ancestry for the ndbus must be under:

```text
/sys/devices/LNXSYSTM:00/
```

and contain an ACPI NVDIMM root device whose component matches canonical `ACPI0012:<two-decimal-instance>`.

Explicitly reject ancestry containing/descending from:

```text
/sys/devices/platform/nfit_test.*
/sys/devices/platform/pmem-region.*
/sys/devices/virtual/*
```

Reject any provider other than exact `ACPI.NFIT`.

## 18. Namespace personality rule

The namespace producing `pmem<N>` must be a direct raw PMEM block namespace.

The canonical block ancestry MUST NOT pass through or terminate at:

```text
btt*
pfn*
dax*
partition object
```

Bind namespace devtype/personality/mode attributes when exposed. If personality cannot be proven exactly, V13 is `BLOCKED`.

The ext4 mount must independently remain non-DAX; PMEM backing does not authorize filesystem DAX.

## 19. Region mappings

Require region `mappings` to parse as canonical positive decimal `K > 0`.

Require exactly:

```text
mapping0 ... mapping(K-1)
```

and no extra `mappingK` entry beyond the declared count.

Each mapping is parsed according to the current LIBNVDIMM mapping ABI into at least:

```text
nmem identity
DPA start
defined length
position when exported
```

Each mapping length must be positive and each referenced `nmem<X>` must belong to the same exact ndbus.

A region with zero explicit mappings is unsupported in V13.

## 20. NFIT NVDIMM health gate

For every mapped `nmem<X>`, read authenticated:

```text
nmem<X>/nfit/flags
```

V13 accepts only the kernel empty-state representation: after stripping exactly one final LF, the content must be the empty byte string.

Any nonempty token is `BLOCKED`, including:

```text
save_fail
restore_fail
flush_fail
not_armed
smart_event
map_fail
smart_notify
unknown token
```

No flag may be cleared/acknowledged by the effect executor.

## 21. NFIT identity binding

For every mapped `nmem<X>`, require/read/bind the reviewed NFIT identity attributes exposed by the current ACPI NFIT ABI:

```text
nfit/handle
nfit/id
nfit/serial
nfit/phys_id
nfit/vendor
nfit/device
nfit/rev_id
nfit/subsystem_vendor
nfit/subsystem_device
nfit/subsystem_rev_id
nfit/flags
```

If a required identity field is absent/unreadable in a profile claiming to be the supported ACPI NFIT class, V13 is `BLOCKED`.

Also bind raw region mappings, namespace identity, block major/minor, ndbus identity/provider/revision, exact ACPI ancestry, and authenticated sysfs mount ID.

## 22. PrimaryStoragePreStateV1

Human-request-bound record includes at least:

```text
repository sb_source
repository sb_dev major/minor
/dev source fstat + st_rdev
raw /sys/dev/block/M:m symlink target
canonical sysfs physical target and component identities
sysfs mount ID
block basename and whole-device/no-partition result
block size/ro/queue fields required by V13
ndbus identity
provider = ACPI.NFIT
ndbus nfit/revision
ACPI ancestry
region identity
devtype = nd_pmem
region nfit/range_index exact positive value
region mappings count
all mapping raw bytes + parsed tuples
namespace identity/personality
all mapped nmem identities
required NFIT identity fields
all nfit/flags raw bytes = empty-state
profile = ACPI_NFIT_PMEM_PERSISTENT_BLOCK_V1
```

Revalidate at request creation, admission, `FinalEffectGateV13`, immediately before object preparation, immediately before main-ref lock, immediately before main-ref rename, and post-effect verification.

Any topology/health/source change is not normalized.

## 23. Unsupported storage classes

V13 blocks:

```text
zram
ramdisk
loop
DM/device-mapper including crypt/LVM
md RAID
nbd/rbd/network block
virtio/xen virtual block
NVMe
SCSI/SATA generic disks
CXL PMEM
PAPR PMEM
E820 legacy PMEM
manual memmap PMEM
nfit_test
RAMDAX / pmem-region test providers
DAX character devices
BTT/PFN personalities
partitions
unknown block stacks
```

A successor may independently review another class. V13 does not.

# PART III — PR #139 F002: INTERNAL EXT4 JOURNAL ONLY

## 24. Correction strategy

V13 supports exactly:

```text
ext4 journal stored as an internal reserved inode on the same primary filesystem device
```

External journal topology is unsupported. `journal_task` is only a liveness cross-check and never journal-location authority.

## 25. Raw primary-device read authority

Use the already authenticated exact primary block-device fd from `AUTHENTIC_BLOCK_DEVICE_SYSFS_V1`.

Require the fd read-only and `st_rdev` exactly equal to repository `statmount` `sb_dev` major/minor.

No helper (`dumpe2fs`, `tune2fs`, `lsblk`, `blkid`, `ndctl`, shell pipeline) is an authority source.

## 26. Primary ext4 superblock location

V13 supports only the primary ext4 superblock beginning at byte offset `1024`.

The authenticated full ext4 runtime option set must contain no alternate-superblock `sb=*` configuration.

Read exactly 1024 bytes from primary device offset 1024 with positional read semantics. Short read/error is `BLOCKED`.

Require ext4 magic at superblock offset `0x38` equal little-endian `0xEF53`.

The raw primary block identity and mounted `statmount` block identity must be exact same `st_rdev`/major/minor.

## 27. EXT4_INTERNAL_JOURNAL_SUPERBLOCK_V1

Parse exact raw primary-superblock fields:

```text
0x38  s_magic
0x5C  s_feature_compat
0x60  s_feature_incompat
0x68  s_uuid[16]
0xD0  s_journal_uuid[16]
0xE0  s_journal_inum
0xE4  s_journal_dev
```

Require exactly:

```text
s_magic = 0xEF53
(s_feature_compat & 0x0004) != 0          # EXT4_FEATURE_COMPAT_HAS_JOURNAL
s_journal_inum > 0
s_journal_uuid = 16 zero bytes
s_journal_dev = 0
(s_feature_incompat & 0x0008) = 0        # EXT4_FEATURE_INCOMPAT_JOURNAL_DEV
```

These rules deliberately select the internal reserved-inode journal path and reject the external-journal path.

## 28. External-journal negative proof

Any one of the following blocks V13:

```text
s_journal_inum = 0
s_journal_uuid != all-zero
s_journal_dev != 0
EXT4_FEATURE_COMPAT_HAS_JOURNAL absent
EXT4_FEATURE_INCOMPAT_JOURNAL_DEV present
raw journal topology unavailable/ambiguous
primary raw device identity != mounted sb_dev
```

If a `journal_dev=*` or `journal_path=*` mount override is visible in any authenticated mount-option surface, it also blocks.

V13 does not rely on absence of those strings from `/proc/fs/ext4/.../options`: current full ext4 option rendering is not the sole journal-location authority. The raw internal-journal predicate above is mandatory.

An external journal remains unsupported even if it is on the same physical medium or another apparently durable device.

## 29. Raw-superblock stability

At every journal-topology gate:

1. `pread` the primary 1024-byte superblock;
2. parse the exact V13 journal authority fields;
3. immediately repeat the read;
4. require the authority slices/parsed values to match.

Do not require the entire ext4 superblock to be byte-stable because legitimate dynamic fields exist.

Bind exact authority fields, volume UUID and feature words used by V13.

Revalidate at request, admission, final gate, immediately before object preparation, immediately before ref lock, immediately before ref rename and post-effect verification.

## 30. Runtime journal cross-check

From authenticated ext4 sysfs require:

```text
journal_task != "<none>\n"
journal_task parses as positive decimal PID
errors_count parses exactly as zero
```

This must agree with raw internal-journal proof. Journal task present with unknown/raw-invalid topology is `BLOCKED`.

# PART IV — CLOSED EXT4 RUNTIME OPTION CLASSIFICATION

## 31. AUTHENTIC_EXT4_RUNTIME_STATE_V1 preserved

Require both:

```text
A. exact statmount MNT_OPTS + OPT_ARRAY for reviewed repository mount
B. authenticated /proc/fs/ext4/<pmemN>/options full nodefs=1 runtime view
```

Also require authenticated ext4 sysfs under the held genuine sysfs root. All proc/sysfs authority paths are descriptor-relative, same-mount and no-cross-mount.

All raw bytes and parsed forms are request-bound and repeatedly revalidated.

## 32. EXT4_RUNTIME_OPTION_TABLE_V13 global grammar

The full `/proc/fs/ext4/<pmemN>/options` parser is closed:

```text
ASCII only
exact newline token boundaries
exactly one final LF
no embedded NUL
no leading/trailing token whitespace
no comma-containing quota continuation
no duplicate token unless the table expressly defines a mutually-exclusive state class
no unrecognized token
```

Every nonempty line must match one V13 table entry. Unknown token = `BLOCKED`, regardless of whether implementation believes it harmless.

## 33. Required ext4 state

Require exact semantic states:

```text
rw
barrier
data=ordered OR data=journal
errors=remount-ro
auto_da_alloc
```

Reject contradictory members.

For the following current ext4 state classes, when the full nodefs=1 interface emits the class, exactly one member is accepted and request-bound:

```text
bsddf | minixdf
grpid | nogrpid
block_validity | noblock_validity
dioread_lock | dioread_nolock
discard | nodiscard
delalloc | nodelalloc
warn_on_error | nowarn_on_error
journal_checksum | nojournal_checksum
prefetch_block_bitmaps | no_prefetch_block_bitmaps
```

## 34. Accepted canonical numeric/string tokens

Only canonical decimal grammar, no sign or leading zero except value zero where allowed:

```text
resuid=<u32>
resgid=<u32>
commit=<positive-u32>
min_batch_time=<u32>
max_batch_time=<u32>
stripe=<u64>
inode_readahead_blks=<u32>
init_itable=<u32>
max_dir_size_kb=<u32>
mb_optimize_scan=0
mb_optimize_scan=1
```

`init_itable=<n>` and `noinit_itable` are mutually exclusive. `noinit_itable` is an explicitly accepted V13 token.

`mb_optimize_scan` may be absent if the exact reviewed kernel state does not emit that class; if emitted it must be 0 or 1.

## 35. Accepted optional exact tokens

Only these additional standalone tokens are accepted; presence/absence is Human-bound:

```text
user_xattr
acl
nouid32
i_version
noquota
noinit_itable
dax=never
```

`noquota` is the only accepted quota-state token. Active quota tokens (`usrjquota`, `grpjquota`, `jqfmt`, `usrquota`, `grpquota`, `prjquota`, or other quota continuation) are unsupported.

## 36. Explicitly forbidden ext4 runtime states/tokens

Block any occurrence of:

```text
ro
nobarrier
barrier=0
data=writeback
journal_async_commit
noload
norecovery
abort
emergency_ro
shutdown
data_err=abort
dax
dax=always
dax=inode
inlinecrypt
test_dummy_encryption
journal_dev=*
journal_path=*
sb=*
debug
nombcache
fc_debug_force
fc_debug_max_replay=*
any active quota token
any unknown token
```

The raw internal-journal proof remains mandatory even if no external-journal option token appears.

## 37. EXT4_BARRIERED_FSYNC_DURABILITY_V2

Supported durability is exactly the conjunction:

```text
AUTHENTIC_CURRENT_TASK_PROCFS_V1 PASS
AUTHENTIC_BLOCK_DEVICE_SYSFS_V1 PASS
ACPI_NFIT_PMEM_PERSISTENT_BLOCK_V1 PASS
LINUX_INITIAL_USER_NAMESPACE_V2 PASS
LINUX_EXECUTION_CREDENTIAL_STATE_V2 PASS
LINUX_NON_IDMAPPED_EXT4_MOUNT_V2 PASS
AUTHENTIC_EXT4_RUNTIME_STATE_V1 PASS
EXT4_INTERNAL_JOURNAL_SUPERBLOCK_V1 PASS
EXT4_RUNTIME_OPTION_TABLE_V13 PASS
filesystem = ext4
mount writable
internal journal present on same primary filesystem
barrier enabled
nobarrier absent
data mode = ordered or journal
journal_async_commit absent
noload absent
abort/emergency_ro/shutdown absent
DAX disabled
SB_LAZYTIME = 0
ID-mapped mount = false
ext4 errors_count = 0
primary storage = healthy ACPI NFIT PMEM exact profile
all required file/directory fsync calls return success
all authority state remains unchanged through commitment
```

Battery-backed ordinary disks, external journal devices and other storage classes are not alternate proof paths.

## 38. Durability claim boundary

V13 claims bounded crash/reboot persistence only under the exact kernel/filesystem/storage profile above and successful synchronization calls.

It does not claim to defeat:

```text
malicious kernel modification
ACPI/firmware deliberately falsifying NFIT persistent-memory description
NVDIMM hardware falsely reporting its energy-source/flush health
physical media failure after acknowledged persistence
post-effect administrator destruction of the storage device
```

Intentionally volatile software storage such as zram/ramdisk is not hidden in that exclusion; it is explicitly rejected.

# PART V — PRESERVED REPOSITORY / GIT AUTHORITY

## 39. LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1 preserved

Repository root and every authority-critical directory component must be:

```text
same exact reviewed ext4 mount
real directory
no nested/bind mount
casefold disabled
encryption disabled
DAX disabled
no unsupported inode semantic flag
```

Path resolution remains descriptor-relative, alias-safe, no-symlink, byte-exact and case-sensitive.

## 40. LINUX_INODE_SEMANTIC_FLAGS_V1 preserved

Mandatory checks:

```text
FS_IOC_GETFLAGS
FS_IOC_FSGETXATTR
statx semantic attributes
```

Allowed inode flags:

```text
regular file: subset of {FS_EXTENT_FL}
directory: subset of {FS_EXTENT_FL, FS_INDEX_FL}
```

All other returned inode flags are unsupported. `fsx_xflags`, `fsx_extsize`, `fsx_projid`, `fsx_cowextsize` remain zero. Required `statx` immutable/append/encrypted/verity/DAX attributes must be supported and absent.

## 41. POSIX metadata profile

Exact final modes remain:

```text
repository root                                    0755
.git                                                0755
.git/objects                                        0755
.git/objects/info if present                        0755
.git/objects/pack if present                        0755
.git/refs                                           0755
.git/refs/heads                                     0755
.git/logs                                           0755
.git/logs/refs                                      0755
.git/logs/refs/heads                                0755
refs/heads/main                                     0644
logs/refs/heads/main if present/new                 0644
.git/index                                          0644
canonical scene target                              0644
.scriptops/decision-log.ndjson                      0644
new loose-object final file                        0444
new loose-object fanout                             0755
V13 staging root                                    0700
staging temporary object before final metadata      0600
```

No unexpected xattrs or POSIX ACLs are accepted on authority-critical paths in the V13 positive profile.

## 42. Git object-store closure preserved

Preserve:

```text
NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2
COMPLETE_LOCAL_OBJECT_STORE_V4
BOUND_OBJECT_STAGING_NAMESPACE_V2
ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V4
```

Reject replace refs, grafts, alternates, promisor/lazy fetch, partial clone completion, unknown object topology, hardlink/symlink aliases and packed-only authority where loose representation is required.

All effect-commit closure objects are locally verified by raw SHA-1 loose-object semantics before ref commitment.

## 43. Bound object staging

Exact V13 staging root:

```text
.git/.x1b-stage-v13-<request_digest>
```

Staged data is never canonical until reviewed no-replace install. A stale `.x1b-stage-v*` census is performed at request, admission, final gate, current staging creation and post-cleanup. Unexpected residue blocks.

## 44. Loose-object install ordering

For a new object:

```text
create staging file 0600
write exact zlib loose bytes
verify decompressed type/size/content/OID
fchmod final 0444
futimens exact Human-bound mtime
verify final security/POSIX/inode metadata + mtime
fsync(file) AFTER final metadata/mtime
renameat2(RENAME_NOREPLACE) into canonical fanout
fsync destination fanout
fsync source staging root
reopen canonical leaf and verify
```

For new fanout directory, final mode/semantic metadata is completed and fsynced before move; after cross-parent move the canonical moved directory and both relevant parent directories are fsynced before durable declaration.

EEXIST is accepted only for an exact verified winner. No unrelated destination is overwritten/deleted.

## 45. HUMAN_BOUND_LOOSE_OBJECT_MTIME_V1 preserved

Exact mtime:

```text
2038-01-18T00:00:00.000000000Z
tv_sec = 2147385600
tv_nsec = 0
```

It applies to every canonical loose closure object relied upon by the effect: new, pre-existing exact, or exact EEXIST winner.

Use `futimens`, exact readback, then file `fsync` after the mtime mutation. Mtime sealing is truthful durable pre-ref preparation effect.

## 46. Pre-ref residue/failure truth

At minimum retain:

```text
BLOCKED_PRE_COMMIT_NO_CANONICAL_EFFECT
BLOCKED_PRE_COMMIT_OBJECT_PREPARED_CLEAN
BLOCKED_PRE_COMMIT_OBJECT_MTIME_SEALED_ONLY
BLOCKED_PRE_COMMIT_STAGING_RESIDUE_BOUND
OBJECT_RETENTION_METADATA_UNCERTAIN
OBJECT_STORAGE_DURABILITY_UNCERTAIN
```

No failed operation is represented as successful canonical Human-attributed screenplay effect.

## 47. FULL_SINGLE_FILE_INDEX_V1 preserved

Real index requirements:

```text
DIRC version 2
complete single-file index
no extensions
no split index
no sharedindex dependency
```

Any `.git/sharedindex.*` presence or split-index config/state blocks. Git does not read/write real index during effect preparation; replacement bytes are deterministic raw bytes.

## 48. Ref / reflog / worktree authority preserved

`refs/heads/main` must be physical loose files-ref topology: no packed-main authority, no symbolic main, no symlink/hardlink alias, exact metadata, same reviewed mount.

Main update remains raw alias-safe lock/CAS-first, not `git update-ref`.

Preserve:

```text
DETERMINISTIC_MAIN_REFLOG_PROJECTION_V2
ALIAS_SAFE_WORKTREE_PROJECTION_V2
CLOSED_RAW_TREE_REWRITE_V1
CLOSED_RAW_COMMIT_OBJECT_V1
```

Reflog identity/timestamps/message, commit bytes, tree bytes, parent, author/committer, encoding and worktree projection are deterministic Human-bound material. Ambient hooks, filters, signing, editor/config or `i18n.commitEncoding` cannot influence effect bytes.

# PART VI — V13 REQUEST, HUMAN EVIDENCE AND FINAL GATES

## 49. DecisionRequestV13

A V13 request binds at minimum:

```text
schema = DecisionRequestV13
request_id = x1b:<sha256>
request_digest
exact repository identity
exact ScriptOps HEAD/TREE
exact task/scene/candidate/scope identities
exact canonical target
exact old main SHA
exact intended new tree/commit bytes and digests
exact material effect
exact object closure
exact loose-object mtime profile/value
exact proc/user/credential profile digests
exact mount identity/idmap digest
exact ext4 runtime-state bytes/tokens digest
exact primary block rdev/sysfs identity
exact ACPI NFIT provider/range/mapping/nmem-health digest
exact internal-journal raw-superblock authority digest
exact filesystem durability profile
exact Git object/index/ref/reflog/worktree profiles
```

No effect-critical field is supplied later by the executor.

## 50. PresentedMaterialEffectV13

Human-visible material effect explicitly includes that execution is conditional on:

```text
healthy exact ACPI NFIT PMEM primary storage
same exact primary block identity
internal ext4 journal only
barrier-enabled closed V13 ext4 option profile
Human-bound loose-object mtime
exact Git object/ref/index/reflog/worktree result
```

Persistence/journal constraints are not hidden as nonmaterial implementation detail.

## 51. Exact Human review marker V13

Accepted body:

```text
X1B-HUMAN-DECISION-V13
decision_request_id=<exact x1b:<request_digest>>
decision_request_sha256=<exact request_digest>
why=<Human rationale>
```

Exactly four LF-separated lines and no trailing LF.

Any V12/earlier marker is invalid for V13. The Human rationale may not be synthesized/substituted by executor or AI.

## 52. Freshness/currentness/conflict/replay

Preserve accepted design semantics:

```text
request current
review targets exact request digest
superseded request invalid
conflicting current approvals invalidate effect
replayed evidence invalid
consumed request cannot authorize another effect
ambiguous current review set -> BLOCK
```

No continuation/silence or wall-clock inference substitutes for exact currentness rules.

## 53. AdmissionV13

Admission re-derives every authority-critical field instead of trusting request serialization, including:

```text
current raw main SHA
Human review set
proc provenance
user namespace
credentials
mount identity/idmap
ext4 runtime options
primary block rdev/sysfs identity
ACPI NFIT provider/range/mappings/nmem health
raw internal-journal superblock fields
object/index/ref/reflog/worktree prestates
staging census
```

Mismatch = no authority.

## 54. FinalEffectGateV13

Immediately before canonical preparation and again before main-ref CAS require exact PASS for:

```text
Human decision current/unconsumed
request digest exact
raw old main SHA unchanged
AUTHENTIC_CURRENT_TASK_PROCFS_V1
LINUX_INITIAL_USER_NAMESPACE_V2
LINUX_EXECUTION_CREDENTIAL_STATE_V2
LINUX_NON_IDMAPPED_EXT4_MOUNT_V2
AUTHENTIC_BLOCK_DEVICE_SYSFS_V1
ACPI_NFIT_PMEM_PERSISTENT_BLOCK_V1
AUTHENTIC_EXT4_RUNTIME_STATE_V1
EXT4_INTERNAL_JOURNAL_SUPERBLOCK_V1
EXT4_RUNTIME_OPTION_TABLE_V13
EXT4_BARRIERED_FSYNC_DURABILITY_V2
LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1
LINUX_INODE_SEMANTIC_FLAGS_V1
COMPLETE_LOCAL_OBJECT_STORE_V4
FULL_SINGLE_FILE_INDEX_V1
physical loose main-ref topology
no replace refs/alternates/promisor/lazy fetch
zero unexpected X1B staging residue
```

## 55. Canonical commitment and post-effect truth

The main loose-ref CAS remains the canonical screenplay commitment point.

No success/decision-log claim precedes proof of durable ref commitment to the exact Human-bound commit.

After ref commitment, complete and durably verify reflog, worktree, full real index, decision log and other explicitly bound projections using final-metadata-before-file-fsync plus parent-directory fsync ordering.

`DURABLY_REF_COMMITTED_COMPLETE` additionally requires exact post-effect storage/NFIT/internal-journal/ext4-option state and all prior object/index/ref/worktree truth.

## 56. Storage uncertainty after possible commitment

If storage, NFIT health, internal-journal state, mount option state or proc/sysfs provenance becomes uncertain before ref commitment, block with no ref effect.

If uncertainty is detected after ref may already be committed, do not blindly roll back or claim clean failure. Record durability uncertainty and require separately authorized recovery/inspection.

Extended classes include:

```text
STORAGE_TOPOLOGY_UNCERTAIN
NVDIMM_HEALTH_UNCERTAIN
EXT4_JOURNAL_TOPOLOGY_UNCERTAIN
EXT4_DURABILITY_STATE_UNCERTAIN
OBJECT_STORAGE_DURABILITY_UNCERTAIN
DURABLY_REF_COMMITTED_PROJECTION_INCOMPLETE
DURABLY_REF_COMMITTED_COMPLETE
```

## 57. No automatic remediation

V13 never automatically remounts ext4, changes barrier/data mode, switches journal, clears filesystem errors, reconfigures NVDIMM namespaces, clears NFIT health flags, changes block queue cache/FUA state, or performs storage administration.

Failing platform = unsupported, not self-healed.

# PART VII — MANDATORY REGRESSIONS

## 58. PR #139 F001 backing-storage regressions

Mandatory negatives:

```text
ext4 on /dev/zram0 -> BLOCK
ext4 on /dev/ram0 -> BLOCK
loop -> BLOCK
device-mapper/LVM/dm-crypt -> BLOCK
md -> BLOCK
nbd/rbd/network -> BLOCK
virtio/xen -> BLOCK
NVMe/SCSI/SATA -> BLOCK in V13
CXL PMEM -> BLOCK in V13
E820/manual memmap PMEM -> BLOCK
nfit_test -> BLOCK
pmem-region/RAMDAX -> BLOCK
pmem partition -> BLOCK
/dev/pmem name whose rdev != mounted sb_dev -> BLOCK
/sys/dev/block source missing/overmounted -> BLOCK
provider != ACPI.NFIT -> BLOCK
region devtype != nd_pmem -> BLOCK
region nfit/range_index missing/zero/malformed -> BLOCK
region mappings = 0 -> BLOCK
mapping references nmem outside same bus -> BLOCK
nonempty nmem nfit/flags -> BLOCK
unknown nmem health token -> BLOCK
block/sysfs/NFIT topology drift -> BLOCK or durability uncertainty
```

Mandatory positive storage class:

```text
whole direct /dev/pmem<N>
mounted sb_dev exact rdev match
authenticated sysfs block object
real ACPI.NFIT provider under ACPI device tree
nd_pmem region
positive exact region nfit/range_index
explicit mapped nmem devices
all required NFIT identity present
all nfit/flags empty
direct raw PMEM namespace
no BTT/PFN/DAX/partition
-> storage profile expected PASS
```

## 59. PR #139 F002 journal-topology regressions

Mandatory negatives:

```text
s_journal_inum = 0 -> BLOCK
s_journal_uuid nonzero -> BLOCK
s_journal_dev nonzero -> BLOCK
HAS_JOURNAL absent -> BLOCK
INCOMPAT_JOURNAL_DEV present -> BLOCK
external journal override if observable -> BLOCK
raw primary device unreadable -> BLOCK
raw rdev differs from statmount sb_dev -> BLOCK
alternate superblock selected -> BLOCK
raw journal authority fields unstable between double reads -> BLOCK
journal_task exists but internal-journal raw proof absent -> BLOCK
external journal on same physical medium -> BLOCK
external journal on separate persistent device -> BLOCK
external journal on volatile device -> BLOCK
```

Mandatory positive journal case:

```text
HAS_JOURNAL set
s_journal_inum > 0
s_journal_uuid all zero
s_journal_dev = 0
INCOMPAT_JOURNAL_DEV absent
journal_task present
-> internal-journal profile expected PASS
```

## 60. V13 ext4 option-table regressions

Mandatory:

```text
unknown ext4 token -> BLOCK
comma quota continuation -> BLOCK
nobarrier/barrier=0 -> BLOCK
data=writeback -> BLOCK
journal_async_commit -> BLOCK
noload/norecovery -> BLOCK
external-journal token -> BLOCK if visible
alternate sb token -> BLOCK
DAX enabled -> BLOCK
debug/test encryption -> BLOCK
emergency_ro/shutdown -> BLOCK
noinit_itable -> accepted and bound
init_itable=N -> accepted and bound, mutually exclusive with noinit_itable
runtime token-set drift -> BLOCK/uncertainty
```

## 61. Preserve R4R12/R4R11 attack regressions

At minimum rerun:

```text
/proc not procfs -> BLOCK
/proc current PID dir submount -> BLOCK
ns/user bind substitution -> BLOCK
uid_map/gid_map bind substitution -> BLOCK
proc mount drift -> BLOCK
noninitial user namespace -> BLOCK
nonidentity uid/gid map -> BLOCK
ID-mapped ext4 mount -> BLOCK
statmount uid/gid map unavailable -> BLOCK
barrier-disabled ext4 -> BLOCK
ext4 option proc source overmount -> BLOCK
ext4 sysfs source overmount -> BLOCK
errors_count nonzero -> BLOCK
journal absent -> BLOCK
ambient loose-object mtime -> regression failure
post-mtime fsync ordering violation -> regression failure
```

## 62. Preserve historical Git attack regressions

At minimum rerun:

```text
local ref substitution
replacement refs
i18n.commitEncoding
traditional/config-defined hooks
clean/smudge/filter/signing/editor/config influence
hardlink/symlink Git-dir aliases
promisor/lazy-fetch network completion
pre-CAS success reporting
fsync-before-final-metadata ordering
loose-ref topology substitution
unbound reflog metadata
primary ODB physical alias
split-index/sharedindex
casefold/inode semantic flags
pre-ref staging/canonical object residue
object mtime/pruning
user/mount ID mapping
procfs authority spoof
ext4 barrier/mount-option drift
```

# PART VIII — FUTURE POSITIVE CONTROL / EVIDENCE / STOP

## 63. Positive-control boundary

No positive control is authorized by this brief.

A future positive control requires separate fresh Human authorization after an independent R4R13 brief review passes and after a separately authorized implementation is frozen/reviewed.

The real positive environment must satisfy the exact ACPI NFIT PMEM/internal-journal profile. `nfit_test`, RAMDAX or another synthetic provider is not authority-equivalent.

## 64. Future evidence requirements

When separately authorized later, evidence must capture at least:

```text
exact ScriptOps candidate HEAD/TREE
exact V13 request digest
exact Human decision evidence identity
exact proc/user/credential records
exact statmount record
exact primary block rdev
exact sysfs block target
exact ACPI NFIT ancestry/provider/range_index
exact region mappings
all mapped nmem identity + flags
raw relevant ext4 primary-superblock bytes/digests
internal-journal parsed fields
full ext4 runtime option bytes/tokens
journal_task/errors_count
object/index/ref/reflog/worktree prestates
raw command stdout/stderr and exit status
post-effect rereads
cryptographic hashes of evidence artifacts
```

Evidence capture itself does not create Human authority.

## 65. No implementation-time broadening

Implementation MUST NOT broaden:

```text
block-device classes
PMEM providers
accepted NFIT health states
journal topology
ext4 option allowlist
DAX mode
user/mount mapping semantics
Git storage topology
```

Any broadening requires a new Human-authorized successor brief and independent review.

## 66. STOP boundary

This artifact authorizes only itself as a proposed successor corrective implementation brief.

It does not authorize:

```text
R4R13 independent review
R4R14 or another successor
ScriptOps implementation
Human decision evidence
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

Required next legal step after durable freeze:

```text
fresh Human authorization
-> one independent AK-CANON R4R13 implementation-brief review
```

Preserve:

```text
BRIEF != REVIEW AUTHORITY
REVIEW FINDING != REPAIR AUTHORITY
PASS != IMPLEMENTATION AUTHORITY
AI PROPOSES != HUMAN DECIDES
```
