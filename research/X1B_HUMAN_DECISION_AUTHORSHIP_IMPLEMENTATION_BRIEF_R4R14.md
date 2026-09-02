# X1B HUMAN DECISION AUTHORSHIP — CLEAN IMPLEMENTATION BRIEF R4R14

Status: `CLEAN R4R14 CORRECTIVE BRIEF / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-02`

## 1. Authority, purpose, and STOP boundary

This document is the self-contained successor implementation brief after independent AK-CANON review PR #141 returned `NOT PASS` on R4R13.

R4R14 preserves the accepted X1B corrective-design properties and every R4R13 mechanism not rejected by PR #141, while correcting the two exact blockers frozen by that review:

1. `X1B-R4R13-IBR-F001`: R4R13 bound ACPI NFIT provider/topology and NVDIMM identity/health, but did not bind the Linux NVDIMM region persistence-domain / deep-flush authority that determines whether the kernel relies on an explicit flush path or a platform power-fail persistence domain;
2. `X1B-R4R13-IBR-F002`: R4R13 treated guest-visible ACPI NFIT shape as physical provenance. Current QEMU can synthesize the same ACPI0012/NFIT/pmem shape while using a backend whose host crash-persistence prerequisites are absent.

R4R14 deliberately chooses two narrow corrections:

```text
ACPI_NFIT_PMEM_PERSISTENT_BLOCK_V2
NVDIMM_CPU_CACHE_PERSISTENCE_DOMAIN_V1
OUT_OF_BAND_PLATFORM_PERSISTENCE_ATTESTATION_V1
PLATFORM_ATTESTATION_CURRENTNESS_V1
```

There is no guest-only positive path in V14.

Guest-visible ACPI/NFIT/sysfs state remains necessary consistency evidence, but it is never sufficient to establish bare-metal or host-backend persistence. A separately authenticated, Human-authored, out-of-band platform-persistence attestation is mandatory for every positive V14 effect.

This document is an implementation brief only. It authorizes no ScriptOps source mutation, no independent R4R14 review, no Human decision evidence creation, no Human platform-attestation creation, no positive control, no canonical screenplay effect, no recovery mutation, no merge, no X1B closure, no Agency Kernel v1, no release, deployment, or tag.

```text
R4R14 BRIEF != IMPLEMENTATION AUTHORITY
R4R14 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R14 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
AI CANNOT CREATE HUMAN PLATFORM ATTESTATION
GUEST STATE != HOST/BACKEND ATTESTATION
```

After durable freeze of this brief, STOP. The next legal stage is one separately Human-authorized independent AK-CANON R4R14 implementation-brief review.

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

### 2.3 R4R13 predecessor

```text
FJ899/8 PR #140
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = d0e420ffa08384f4f11efc6edcd042ebb21b4280
TREE = 66fb4a95313287a5715143b64cfa47e0025e6e6e
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R13.md
BLOB = 6da06d21b05c8acbe6a6a39793ec0b1e54396204
```

### 2.4 Binding R4R13 NOT-PASS review

```text
FJ899/8 PR #141
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = e048a3827c6dbef04b14560ce6fdd8f8531264e3
TREE = 5c241d6bd68e3c90ab92337b37d211f07f6780e5
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R13_AK_CANON_REVIEW.md
BLOB = 195583f876922f662176977dc51338aac7b36121
VERDICT = AK-CANON X1B R4R13 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #141 froze:

```text
X1B-R4R13-IBR-F001 — NVDIMM persistence-domain / deep-flush authority is not bound
X1B-R4R13-IBR-F002 — guest ACPI NFIT provenance does not attest virtual-NVDIMM backend persistence
```

PR #141 also recorded:

```text
PR #139 F001 generic /dev-backed persistence class = ADDRESSED AT BRIEF LEVEL FOR EXACT PRIOR COUNTEREXAMPLES
PR #139 F002 external ext4 journal write domain    = ADDRESSED AT BRIEF LEVEL
PR #139 ext4 option-table discretion              = ADDRESSED AT BRIEF LEVEL
```

No R4R14 correction may weaken the raw internal-journal predicate or the explicit ext4 option table.

## 3. Exact repository state before R4R14 preparation

Immediately before R4R14 preparation:

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

## 4. Normative precedence and V14 migration

```text
R4R14 TEXT = CURRENT IMPLEMENTATION-BRIEF AUTHORITY
R4R13 AND EARLIER IMPLEMENTATION BRIEFS = HISTORICAL INPUT ONLY
CORRECTIVE DESIGN PR #34 = HIGHER-LEVEL PROPERTY CONTRACT
```

Authority-critical changes in V14:

```text
NVDIMM FIC semantics are explicit
only byte-addressable energy-backed FIC 0x0101 is supported
only explicit cpu_cache persistence_domain is supported
only visible deep_flush=0 is supported
persistence-domain and deep-flush drift is authority-relevant
guest-visible ACPI NFIT is never bare-metal proof
positive effect requires separate out-of-band platform persistence attestation
platform attestation must be a distinct trusted Human GitHub review
platform attestation is request-bound, snapshot-bound, current, unique, active and explicitly referenced by final Human decision evidence
standard QEMU vNVDIMM remains blocked without trusted out-of-band attestation even if guest-visible NFIT/persistence-domain fields look acceptable
```

Therefore:

```text
V13 REQUEST/REVIEW/ADMISSION/GATE != V14 AUTHORITY
V13 HUMAN REVIEW MARKER != V14 HUMAN DECISION
V13 PLATFORM STATE != V14 PLATFORM STATE
V14 EFFECT PROFILE REQUIRES FRESH V14 HUMAN-BOUND REQUEST
V14 EFFECT PROFILE REQUIRES FRESH V14 PLATFORM ATTESTATION
```

No V13 or earlier Human evidence may authorize a V14 effect.

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

No new daemon, attestor private key, platform-control-plane credential, or Human credential may be added to the ScriptOps repository.

The V14 executor only validates externally created GitHub review evidence. It never creates, signs, edits, refreshes, or requests the Human platform attestation.

Any additional tracked path requires STOP and fresh Human authorization before mutation.

## 6. Core Human-decision rule

```text
HumanDecision = TRUE
ONLY IF
separate trusted Human decision evidence
for exact current content + scope + candidate + material effect + exact current platform-attestation review
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
guest ACPI/NFIT shape
CPUID no-hypervisor hint
DMI bare-metal-looking strings
successful fsync
platform-attestation marker text without trusted Human review origin
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
PLATFORM ATTESTATION TEXT != TRUSTED PLATFORM ATTESTATION
GUEST OBSERVATION != OUT-OF-BAND HOST/BACKEND ATTESTATION
```

## 7. Exactly one current effect-capable acceptance interface

After future implementation, the only current effect-capable Human-decision acceptance interface remains:

```text
python phase6/scriptops-v2-hardening.py approve --decision-pr <positive-integer>
```

PR number is a locator only, never authority.

The executor discovers request, Human platform-attestation review and final Human decision review from trusted GitHub state. No caller-controlled field may supply:

```text
Human actor
Human decision result
Human rationale
platform-attestation actor
platform-attestation review id
platform-attestation body
platform snapshot identity
request identity
candidate identity
effect identity
proc/sysfs provenance
storage topology
block-device identity
NVDIMM FIC
persistence_domain
deep_flush
ext4 journal state
mount-option state
loose-object mtime
Git ref/index/object topology
effect commit metadata
```

# PART I — V14 PLATFORM AND PRESERVED KERNEL AUTHORITY

## 8. V14 supported platform

Git semantic compatibility remains:

```text
2.55.0 <= parsed Git version < 2.56.0
object format = sha1
ref storage format = files
```

V14 platform is deliberately narrow:

```text
OS = Linux
repository filesystem = ext4
repository source = direct whole /dev/pmem<N> block device only
primary backing profile = ACPI_NFIT_PMEM_PERSISTENT_BLOCK_V2
NVDIMM control-region format = 0x0101 byte-addressable energy-backed only
region persistence_domain = cpu_cache only
region deep_flush = 0 only
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
positive platform trust = separate current OUT_OF_BAND_PLATFORM_PERSISTENCE_ATTESTATION_V1
```

If a required primitive/source is unavailable, unreadable, unsupported, ambiguous, blocked by seccomp/LSM/containerization, inconsistent, or cannot be independently revalidated, V14 is `BLOCKED`.

V14 MUST NOT acquire privilege, use `sudo`, call `setns`/`unshare`, mount/remount anything, alter block topology, reconfigure NVDIMMs, clear NVDIMM health state, trigger deep flush, alter ext4 journal/options, clear ext4 errors, or modify procfs/sysfs.

## 9. AUTHENTIC_CURRENT_TASK_PROCFS_V1 preserved

Authority begins from a held genuine `/proc` descriptor:

```text
open("/proc", O_PATH|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC)
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

No credential transition may be performed to manufacture proof.

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

# PART II — PR #141 F001: CLOSED NVDIMM PERSISTENCE DOMAIN

## 13. Correction strategy

R4R14 distinguishes three separate concepts that R4R13 partially conflated:

```text
NVDIMM identity / topology
NVDIMM interface energy-backing semantics
platform persistence / flush semantics
```

A positive V14 candidate must pass all three.

The supported kernel-visible positive state is deliberately only:

```text
nfit/format = 0x0101
persistence_domain = cpu_cache
deep_flush = 0
```

No fallback assumption is accepted.

## 14. AUTHENTIC_BLOCK_DEVICE_SYSFS_V2

Authenticate and retain a held genuine `/sys` root:

```text
open("/sys", O_PATH|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC)
fstatfs(sys_root_fd).f_type = SYSFS_MAGIC
unique sysfs mount ID exact
statmount(unique-id).fs_type = sysfs
```

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

Semantic identity is major/minor, not pathname spelling.

Read `/sys/dev/block/M:m` from the authenticated sysfs root. Resolve its relative target beneath `devices/` with:

```text
RESOLVE_BENEATH
RESOLVE_NO_XDEV
RESOLVE_NO_SYMLINKS
```

Every authority-critical descendant subsequently read must remain on the same authenticated sysfs mount.

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

## 15. Exact source spelling / whole-device rule

Require exactly:

```text
sb_source = /dev/pmem<N>
```

where `<N>` is canonical unsigned decimal with no sign and no leading zero except exactly `0`.

The canonical sysfs block basename must equal `pmem<N>`.

Reject partitions and all aliases, including `/dev/pmem<N>p<M>`.

## 16. ACPI_NFIT_PMEM_PERSISTENT_BLOCK_V2 provider provenance

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

These guest-visible provenance checks remain necessary but are not bare-metal proof. Positive V14 authority also requires Part III.

## 17. Namespace personality rule

The namespace producing `pmem<N>` must be a direct raw PMEM block namespace.

The canonical block ancestry MUST NOT pass through or terminate at:

```text
btt*
pfn*
dax*
partition object
```

Bind namespace devtype/personality/mode attributes when exposed. If personality cannot be proven exactly, V14 is `BLOCKED`.

The ext4 mount must independently remain non-DAX.

## 18. Region mappings

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

A region with zero explicit mappings is unsupported.

## 19. NFIT NVDIMM health gate preserved and strengthened

For every mapped `nmem<X>`, read authenticated:

```text
nmem<X>/nfit/flags
```

V14 accepts only the kernel empty-state representation: after stripping exactly one final LF, the content must be the empty byte string.

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

No flag may be cleared/acknowledged by the executor.

## 20. NFIT control-region identity and FIC

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
nfit/format
nfit/flags
```

If a required field is absent/unreadable, V14 is `BLOCKED`.

Current Linux defines the reviewed format-interface codes including:

```text
0x0101 = byte-addressable energy backed
0x0201 = block-addressable non-energy backed
0x0301 = byte-addressable non-energy backed
```

V14 supports exactly:

```text
nfit/format raw bytes = "0x0101\n"
parsed FIC = 0x0101
```

Any other FIC is `BLOCKED`.

This explicitly rejects the standard QEMU vNVDIMM FIC observed by PR #141 (`0x0301`) before the independent out-of-band attestation gate is even considered.

FIC is not used as bare-metal proof. A hypervisor can synthesize guest-visible fields; Part III remains mandatory.

## 21. NVDIMM_CPU_CACHE_PERSISTENCE_DOMAIN_V1

Read authenticated region attributes from the exact region bound above:

```text
regionX/persistence_domain
regionX/deep_flush
```

Both attributes must exist and remain on the authenticated sysfs mount.

V14 supports exactly:

```text
persistence_domain raw bytes = "cpu_cache\n"
deep_flush raw bytes = "0\n"
```

Interpretation for this profile:

```text
cpu_cache = kernel-visible platform claim that the entire CPU-store persistence path is covered on system power loss
0 deep_flush = current libnvdimm reports no explicit deep-flush operation required
```

V14 deliberately rejects:

```text
persistence_domain = memory_controller
persistence_domain absent
persistence_domain empty
persistence_domain unknown
deep_flush = 1
deep_flush absent
deep_flush indeterminate
any parse ambiguity
```

The `memory_controller` domain may be valid on real systems but is not reviewed in V14.

A visible `deep_flush=1` may be valid on real systems but requires a separately reviewed explicit-flush topology and is not supported in V14.

No executor write to `deep_flush` is authorized.

## 22. PrimaryStoragePreStateV2

Human-request-bound platform snapshot includes at least:

```text
repository sb_source
repository sb_dev major/minor
/dev source fstat + st_rdev
raw /sys/dev/block/M:m symlink target
canonical sysfs physical target and component identities
sysfs mount ID
block basename and whole-device/no-partition result
block size/ro/queue fields required by V14
ndbus identity
provider = ACPI.NFIT
ndbus nfit/revision
ACPI ancestry
region identity
region devtype = nd_pmem
region nfit/range_index exact positive value
region mappings count
all mapping raw bytes + parsed tuples
namespace identity/personality
all mapped nmem identities
required NFIT identity fields
all nfit/format raw bytes = 0x0101
all nfit/flags raw bytes = empty-state
region persistence_domain raw bytes = cpu_cache
region deep_flush raw bytes = 0
profile = ACPI_NFIT_PMEM_PERSISTENT_BLOCK_V2
persistence_profile = NVDIMM_CPU_CACHE_PERSISTENCE_DOMAIN_V1
```

Canonical snapshot serialization is an ordered UTF-8 LF-terminated record with no optional reordering. Each variable-length raw value is represented as lowercase SHA-256 plus exact byte length; parsed semantic values are also included.

Define:

```text
platform_snapshot_sha256 = SHA256(canonical PlatformSnapshotV14 bytes)
```

Revalidate the exact current snapshot at:

```text
request creation
platform-attestation admission
Human-decision admission
FinalEffectGateV14
immediately before object preparation
immediately before main-ref lock
immediately before main-ref rename
post-effect verification
```

Any topology/health/FIC/persistence-domain/deep-flush/source change is not normalized. It blocks the effect or makes the outcome uncertain under the existing uncertainty rules.

## 23. Unsupported storage classes

V14 blocks:

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
NFIT FIC 0x0201
NFIT FIC 0x0301
memory_controller-only persistence domain
explicit deep-flush profile
```

A successor may independently review another class. V14 does not.

# PART III — PR #141 F002: OUT-OF-BAND HOST/BACKEND ATTESTATION

## 24. Correction strategy

V14 makes the trust boundary explicit:

```text
NO PURE GUEST SOFTWARE TEST CAN ESTABLISH BARE-METAL BACKING AGAINST A HYPERVISOR THAT CONTROLS GUEST ACPI/NFIT STATE.
```

Therefore V14 does not attempt to prove bare metal by absence of guest virtualization fingerprints.

Positive authority requires a distinct trusted Human GitHub review whose content explicitly attests, from an out-of-band non-guest observation channel, that the exact request-bound platform snapshot corresponds to bare-metal physical ACPI NFIT NVDIMM backing with the required power-loss persistence property.

This is a separate act from the final Human decision review.

The platform attestation is an authenticated statement of an external environmental premise. It is not synthesized from guest state and is not writable by the executor.

## 25. OUT_OF_BAND_PLATFORM_PERSISTENCE_ATTESTATION_V1 origin

The platform attestation must be one GitHub pull-request review fetched directly from trusted GitHub state for the exact decision PR.

It MUST satisfy the same trusted-Human-origin controls used for Human decision evidence:

```text
review object fetched from GitHub, not caller body
review author = exact authorized Human principal under current X1B trust policy
review author is not a bot/app/AI identity
review state = APPROVED
review not dismissed
review id = positive immutable GitHub review id
review submitted_at present
review body bytes fetched from GitHub
```

The platform-attestation review MUST be distinct from the final Human decision review:

```text
platform_attestation_review_id != human_decision_review_id
```

The same trusted Human principal may perform both acts, but the two review objects, timestamps, markers and semantics must remain separate.

Rationale: V14 requires independence from guest-controlled ACPI/NFIT state, not necessarily a second natural person. A future design may require separate-person dual control, but V14 does not invent that policy.

The executor MUST NOT create, edit, submit, approve, dismiss, refresh or supersede the platform-attestation review.

## 26. Exact platform-attestation marker

The only accepted marker is exact V1 shape:

```text
X1B-PLATFORM-PERSISTENCE-ATTESTATION-V1
decision_request_id=<exact x1b:<request_digest>>
decision_request_sha256=<exact request_digest>
platform_snapshot_sha256=<exact V14 platform snapshot digest>
environment_class=bare-metal
virtualization_layer=none
backend_class=physical-acpi-nfit-nvdimm
power_loss_persistence=affirmed
persistence_domain=cpu_cache
deep_flush=0
nfit_format=0x0101
observation_channel=out-of-band-non-guest
why=<Human one-line rationale / observation basis>
```

Parser rules:

```text
UTF-8 only
LF only
exact marker first line
exact field order
exactly one occurrence of each field
no extra field
no blank line
exactly one final LF
why must be nonempty single line
request digest lowercase 64 hex
platform snapshot digest lowercase 64 hex
```

No semantic alias, whitespace normalization, alternate spelling, JSON conversion, Markdown extraction or partial marker is accepted.

## 27. What the platform attestation means

The trusted Human is explicitly attesting all of the following environmental facts for the exact request-bound snapshot:

```text
the executing environment is bare metal for the purpose of this effect
there is no hypervisor/VM layer mediating the repository PMEM backend
/dev/pmem<N> corresponds to physical ACPI NFIT NVDIMM media, not vNVDIMM emulation
host/backend is not memory-backend-ram
host/backend is not ordinary non-DAX memory-backend-file
host/backend is not a QEMU file backend missing pmem/share/MAP_SYNC persistence prerequisites
power-loss persistence is affirmed for the exact physical backing described by platform_snapshot_sha256
the Human observation basis is external to the guest ACPI/NFIT data used by the executor
```

The attestation is a trusted external premise, not an automated derivation.

If the Human cannot independently establish these facts, the correct outcome is no platform-attestation review and therefore `BLOCKED`.

## 28. PLATFORM_ATTESTATION_CURRENTNESS_V1

At request creation the executor records the exact decision PR locator and `platform_snapshot_sha256`, but no platform attestation exists yet.

A valid sequence is exactly:

```text
1. immutable V14 decision request is published
2. trusted Human independently inspects the exact request and out-of-band platform/backend state
3. trusted Human submits one exact X1B-PLATFORM-PERSISTENCE-ATTESTATION-V1 APPROVED review
4. trusted Human later submits one exact X1B-HUMAN-DECISION-V14 review that explicitly references the platform-attestation review id and body digest
5. executor refetches and validates both reviews before any material effect
```

Platform attestation must satisfy:

```text
submitted_at >= request published_at
submitted_at < Human decision review submitted_at
review remains APPROVED and not dismissed
review body SHA-256 remains exact
request remains active
platform_snapshot_sha256 remains exact
no later conflicting platform-attestation marker exists for same request
no superseding request exists
```

Freshness window:

```text
GitHub-server-time - platform_attestation.submitted_at <= 900 seconds
```

Freshness authority is the HTTPS GitHub response `Date` time observed while refetching the review set, not caller time and not a caller-supplied timestamp.

Require nonnegative age. Missing/unparseable server time is `BLOCKED`.

Recheck the 900-second window at:

```text
Human-decision admission
FinalEffectGateV14
immediately before main-ref lock
immediately before main-ref rename
```

If the window expires before the material commitment, STOP and require a new platform-attestation review plus a new final Human decision review referencing it.

The executor may not ask GitHub to mutate the review; it only refetches trusted read state.

## 29. Platform-attestation uniqueness / conflict rule

For the exact current request, scan all GitHub review bodies from trusted Human principals.

Classify exact platform-attestation markers.

Success requires exactly one current non-dismissed matching platform attestation referenced by the final Human decision review.

Block on:

```text
zero matching attestation
more than one active attestation with different body digest
later contradictory platform marker
attestation for a different request digest
attestation for a different platform snapshot digest
attestation state not APPROVED
attestation dismissed
attestation actor not trusted Human
attestation body shape-only from comment/issue/commit/AI record
attestation too old
```

A top-level PR comment is never platform authority.

## 30. Final Human decision marker V14

The only accepted final Human decision marker is:

```text
X1B-HUMAN-DECISION-V14
decision_request_id=<exact x1b:<request_digest>>
decision_request_sha256=<exact request_digest>
platform_attestation_review_id=<exact positive GitHub review id>
platform_attestation_sha256=<sha256 of exact platform-attestation review body bytes>
why=<Human one-line decision rationale>
```

The final decision review must be separately fetched and validated under existing Human-origin/currentness rules.

It is invalid unless the referenced platform-attestation review independently validates first.

The platform attestation does not imply Human approval of the effect.

The final Human decision does not imply a platform attestation.

Both are mandatory.

## 31. Guest virtualization hints are negative-only diagnostics

V14 may record direct guest hints such as:

```text
CPUID hypervisor-present bit
/sys/hypervisor presence
known virtualization DMI markers when available
```

If a definitive virtualization indication is present, V14 MUST `BLOCK` even if a platform-attestation review claims `bare-metal`.

Absence of such hints is never positive authority.

No command such as `systemd-detect-virt` may replace the out-of-band attestation.

This prevents the design from quietly reverting to guest fingerprinting.

## 32. Mandatory QEMU negative semantics

The future implementation and independent review must prove all of these remain blocked without a valid out-of-band attestation:

```text
QEMU vNVDIMM + memory-backend-ram
QEMU vNVDIMM + ordinary non-DAX memory-backend-file
QEMU vNVDIMM + pmem=off
QEMU vNVDIMM + share/persistence prerequisites missing
QEMU vNVDIMM + unarmed=off
QEMU vNVDIMM + nvdimm-persistence=cpu
QEMU vNVDIMM + nvdimm-persistence=mem-ctrl
```

Even a synthetic guest state modified to present:

```text
nfit/format=0x0101
persistence_domain=cpu_cache
deep_flush=0
empty nfit/flags
ACPI0012
provider=ACPI.NFIT
/dev/pmem0
```

remains `BLOCKED` without the exact trusted platform-attestation review.

This is the decisive F002 correction.

## 33. PlatformAttestationPreStateV1

Bind in the V14 request/effect gate at least:

```text
decision PR repository/id
platform attestation review id
platform attestation review author identity
platform attestation review state
platform attestation review submitted_at
exact review body bytes SHA-256
request id/digest parsed from body
platform snapshot digest parsed from body
environment_class
virtualization_layer
backend_class
power_loss_persistence
persistence_domain
deep_flush
nfit_format
observation_channel
why bytes SHA-256
GitHub server time used for freshness
computed attestation age
```

The final Human decision record additionally binds the exact platform-attestation review id and body digest.

## 34. Trust-boundary statement

V14's durability claim depends on three classes of truth:

```text
kernel-visible current state verified by the executor
trusted Human decision about the material effect
trusted Human out-of-band platform persistence attestation about the host/backend environment
```

The executor does not prove bare metal from software-visible guest state alone.

A deliberately false statement by the trusted Human platform attestor is outside the executor's ability to detect, just as a deliberately false Human decision is outside authorship verification. The important V14 correction is that this environmental premise is explicit, authenticated, request-bound, current and separately reviewed rather than hidden inside guest ACPI/NFIT inference.

# PART IV — INTERNAL EXT4 JOURNAL AND CLOSED RUNTIME STATE

## 35. Raw primary-device read authority preserved

Use the authenticated exact primary block-device fd from `AUTHENTIC_BLOCK_DEVICE_SYSFS_V2`.

Require the fd read-only and `st_rdev` exactly equal to repository `statmount` `sb_dev` major/minor.

No helper (`dumpe2fs`, `tune2fs`, `lsblk`, `blkid`, `ndctl`, shell pipeline) is an authority source.

## 36. Primary ext4 superblock location

V14 supports only the primary ext4 superblock beginning at byte offset `1024`.

The authenticated full ext4 runtime option set must contain no alternate-superblock `sb=*` configuration.

Read exactly 1024 bytes from primary device offset 1024 with positional read semantics. Short read/error is `BLOCKED`.

Require ext4 magic at superblock offset `0x38` equal little-endian `0xEF53`.

The raw primary block identity and mounted `statmount` block identity must be exact same `st_rdev`/major/minor.

## 37. EXT4_INTERNAL_JOURNAL_SUPERBLOCK_V1 preserved

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

Any external-journal topology is unsupported.

Current reviewed ext4 semantics reject a mount-time nonzero journal device override when an internal journal inode is present. V14 preserves that predecessor finding and never relies on `journal_task` for journal-location authority.

## 38. Raw-superblock stability

At every journal-topology gate:

```text
pread authority superblock
parse exact V14 journal authority fields
immediately repeat read
require authority slices/parsed values match
```

Do not require the entire ext4 superblock to be byte-stable because legitimate dynamic fields exist.

Bind exact authority fields, volume UUID and feature words used by V14.

## 39. AUTHENTIC_EXT4_RUNTIME_STATE_V1 preserved

Require both:

```text
A. exact statmount MNT_OPTS + OPT_ARRAY for reviewed repository mount
B. authenticated /proc/fs/ext4/<pmemN>/options full nodefs=1 runtime view
```

Also require authenticated ext4 sysfs under the held genuine sysfs root.

All raw bytes and parsed forms are request-bound and repeatedly revalidated.

## 40. EXT4_RUNTIME_OPTION_TABLE_V13 preserved

The full `/proc/fs/ext4/<pmemN>/options` parser remains closed.

Require exact semantic states:

```text
rw
barrier
data=ordered OR data=journal
errors=remount-ro
auto_da_alloc
```

Accepted state classes remain exactly:

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

Accepted canonical numeric/string tokens remain:

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

Accepted optional standalone tokens remain only:

```text
user_xattr
acl
nouid32
i_version
noquota
noinit_itable
dax=never
```

Explicitly forbidden remains:

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

## 41. EXT4_BARRIERED_FSYNC_DURABILITY_V3

Supported durability is exactly the conjunction:

```text
AUTHENTIC_CURRENT_TASK_PROCFS_V1 PASS
AUTHENTIC_BLOCK_DEVICE_SYSFS_V2 PASS
ACPI_NFIT_PMEM_PERSISTENT_BLOCK_V2 PASS
NVDIMM_CPU_CACHE_PERSISTENCE_DOMAIN_V1 PASS
OUT_OF_BAND_PLATFORM_PERSISTENCE_ATTESTATION_V1 PASS
PLATFORM_ATTESTATION_CURRENTNESS_V1 PASS
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
primary storage = exact V14 PMEM profile
NVDIMM FIC = 0x0101
persistence_domain = cpu_cache
deep_flush = 0
trusted out-of-band Human platform attestation = current and exact
all required file/directory fsync calls return success
all authority state remains unchanged through commitment
```

## 42. Durability claim boundary

V14 claims bounded crash/reboot/power-loss persistence only under the exact kernel/filesystem/storage profile plus the exact current out-of-band Human platform attestation.

It does not claim to defeat:

```text
malicious kernel modification
trusted Human platform attestor deliberately making a false environmental statement
physical media failure after acknowledged persistence
post-effect administrator destruction of the storage device
```

It does not silently classify a virtual environment as firmware falsification. Virtualization is explicitly within the F002 gate and requires the platform attestation to say `bare-metal` / `none` plus no contradictory guest virtualization evidence.

# PART V — PRESERVED BYTE-NAMESPACE / INODE SECURITY CONTROLS

## 43. LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1 preserved

All authority-critical repository paths are resolved descriptor-relatively from held repository-root / Git-dir descriptors.

Require byte-exact filename semantics and no casefold directory state on authority paths.

No Unicode/case normalization is authorized.

Every path traversal uses nofollow/beneath/no-cross-mount controls appropriate to the primitive.

## 44. LINUX_INODE_SEMANTIC_FLAGS_V1 preserved

For every authority-critical regular file/directory, inspect and bind semantic inode flags through the reviewed ioctl/stat interfaces.

Reject casefold and all unreviewed semantic flags.

No security-significant inode flag may be altered to manufacture acceptance.

## 45. Security metadata / alias rules preserved

For every authority-critical leaf:

```text
no symlink
no unexpected hardlink alias
expected uid/gid
expected file type
expected mode
reviewed inode flags
reviewed xattr/ACL/security state
```

Any alias or security-metadata ambiguity is `BLOCKED`.

# PART VI — HUMAN-BOUND LOOSE-OBJECT MTIME AND CLOSED OBJECT STORE

## 46. HUMAN_BOUND_LOOSE_OBJECT_MTIME_V1 preserved

The fixed Human-visible loose-object mtime remains:

```text
mtime_iso8601 = 2038-01-18T00:00:00.000000000Z
mtime_tv_sec = 2147385600
mtime_tv_nsec = 0
```

Require `CLOCK_REALTIME < 2147385600` at request, admission, final gate and immediately before sealing.

After the horizon:

```text
BLOCKED_PROFILE_HORIZON
```

No Human evidence TTL is inferred from this mtime.

The sentinel applies to every canonical loose leaf in `new_object_closure`:

```text
newly staged/installed object
pre-existing exact loose object
exact concurrent EEXIST winner
```

For a pre-existing/winner object:

```text
descriptor-relative nofollow open
verify exact object/security metadata
futimens(fd,[UTIME_OMIT,{2147385600,0}])
verify exact readback
fsync(fd) AFTER mtime
reopen canonical and reverify
```

For a new staged object:

```text
create 0600
write exact zlib bytes
verify object bytes
fchmod 0444
futimens sentinel
verify content/mode/uid/gid/nlink/security/mtime
fsync(file_fd) AFTER final fchmod+mtime
RENAME_NOREPLACE canonical
fsync destination fanout + source staging root
reopen canonical and verify
```

## 47. BOUND_OBJECT_STAGING_NAMESPACE_V3

V14 request-specific staging root is:

```text
.git/.x1b-stage-v14-<request_digest>
```

The executor accepts no caller path.

Before a new V14 effect, any residue matching:

```text
.git/.x1b-stage-v*
```

is `BLOCKED_STAGING_RESIDUE` unless an independently authorized recovery stage has classified it.

No automatic cleanup is authorized.

Successful pre-ref state requires zero staging residue outside the exact active root and zero unfinished object preparation.

## 48. ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V4 preserved

Objects are staged under the bounded namespace, fully finalized, metadata-verified and fsynced before canonical installation.

Canonical installation uses `RENAME_NOREPLACE`.

On `EEXIST`, open the exact canonical winner descriptor-relatively and require exact expected object identity/security/mtime before continuing.

No replace-existing rename is authorized.

## 49. COMPLETE_LOCAL_OBJECT_STORE_V4 preserved

All objects needed for the exact candidate/effect must already be present and validated locally.

No network fetch is allowed to satisfy object existence.

Reject promisor/lazy-fetch dependency.

Replacement refs are disabled and absent under the closed profile.

## 50. NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2 preserved

Require:

```text
object format = sha1
no replace refs
no graft replacement
no promisor remote dependency
no partial-clone missing object
no alternates object store
no unbound object directory
```

Primary object-store physical topology remains exact and no-alias.

# PART VII — RAW TREE / COMMIT / INDEX / REF / REFLOG / WORKTREE

## 51. CLOSED_RAW_TREE_REWRITE_V1 preserved

Candidate tree construction is byte-defined from the Human-bound screenplay payload and exact frozen base tree.

No porcelain mutation is authority.

Every tree object is constructed/hashed/verified as raw Git SHA-1 object bytes under the closed object profile.

## 52. CLOSED_RAW_COMMIT_OBJECT_V1 preserved

Commit object construction remains closed and deterministic except Human-bound fields explicitly present in the request.

No caller-controlled author/committer identity, timezone, encoding or hook result may enter authority-critical commit bytes.

The V14 Human marker is carried in the exact approved commit-message projection only if specified by the current request schema.

## 53. FULL_SINGLE_FILE_INDEX_V1 preserved

The supported index is exactly:

```text
DIRC version 2
single physical index file
no extensions
no split index
no sharedindex
```

Unknown extension/state is `BLOCKED`.

## 54. CLOSED_FULL_INDEX_V2_REWRITE_V1 preserved

Build the full replacement index from the exact target tree and exact reviewed metadata.

Do not call Git index-writing commands to produce authority-critical index state.

## 55. ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1 preserved

Write replacement index to a bound temporary leaf in the exact index directory.

Finalize metadata, `fsync(file)` after final metadata, verify no alias, atomically install, then `fsync(parent directory)`.

Post-install reopen and byte/hash/metadata verification are mandatory.

## 56. PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1 preserved

The supported `refs/heads/main` topology is one physical loose ref with no symlink/hardlink/packed-ref ambiguity.

Ref/reflog paths and replacement metadata remain explicitly bound.

## 57. ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V3 preserved

Main-ref effect is an exact compare-and-swap against Human-bound old OID.

No Git writer is authorized for authority-critical ref replacement.

Use nofollow descriptor-relative lock/temp mechanics, exact old-value verification, final file metadata before fsync, atomic replacement and directory fsync.

## 58. DETERMINISTIC_MAIN_REFLOG_PROJECTION_V2 preserved

The exact reflog append/replacement bytes are computed before effect and Human-bound.

No `git update-ref` generated reflog text is accepted.

Ref/reflog success is one bound projection; ambiguous partial state is uncertainty, never reported as clean Human success.

## 59. ALIAS_SAFE_WORKTREE_PROJECTION_V2 preserved

The exact worktree projection is Human-bound and built through the reviewed raw path.

No unbound checkout hook/filter/smudge/clean execution may affect authority-critical bytes.

Worktree post-state is reverified descriptor-relatively.

## 60. NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1 preserved

No traditional `.git/hooks` hook and no config-defined hook command is executed in the authority path.

Unknown future hook mechanism is unsupported.

## 61. Git subprocess profile preserved

Any Git subprocess retained only for read-only semantic checks must use a closed environment and at least:

```text
-c gc.auto=0
-c maintenance.auto=false
```

No Git subprocess may write object/ref/index/reflog authority state.

No subprocess may trigger maintenance, lazy fetch, configured hooks, filters, signing or helper-defined authority.

# PART VIII — V14 REQUEST, REVIEW, ADMISSION AND EFFECT BINDING

## 62. DecisionRequestV14

The immutable request must bind at least:

```text
schema = X1B-DECISION-REQUEST-V14
request id = x1b:<request_digest>
request digest
repository identity
exact ScriptOps baseline HEAD/TREE and security BLOB set
exact candidate screenplay content digest and bytes identity
exact scope
exact old main OID
exact candidate commit/tree/object closure
exact target index bytes digest
exact target ref bytes digest
exact target reflog bytes digest
exact target worktree projection digest
exact primary-storage profile
exact platform_snapshot_sha256
required nfit_format = 0x0101
required persistence_domain = cpu_cache
required deep_flush = 0
required platform marker = X1B-PLATFORM-PERSISTENCE-ATTESTATION-V1
platform attestation freshness max = 900 seconds
exact Human decision marker version = V14
material-effect digest
```

Request digest is SHA-256 over canonical request bytes.

No caller field may override any authority-critical value after request creation.

## 63. Request publication and immutability

The request is published on the decision PR as immutable evidence under the existing trusted request mechanism.

After a Human platform-attestation review exists, any change to request content invalidates that attestation.

After a Human decision review exists, any change to request content invalidates both reviews.

No normalization from a later request revision is allowed.

## 64. Platform-attestation admission

Admission order is exact:

```text
validate request identity/currentness
recompute current PlatformSnapshotV14
require exact request platform_snapshot_sha256
fetch all GitHub reviews from trusted source
select/validate unique current platform-attestation review
validate exact marker/body/origin/state
validate request/snapshot binding
validate GitHub-server-time freshness <= 900s
validate no conflict/supersession
recompute current PlatformSnapshotV14 again
require unchanged
```

Only then may final Human decision evidence be considered.

## 65. Human-decision admission V14

Fetch all reviews again from trusted GitHub state.

Select exact current Human decision review under the existing Human-origin rules.

Require exact marker:

```text
X1B-HUMAN-DECISION-V14
decision_request_id=<exact x1b:<request_digest>>
decision_request_sha256=<exact request_digest>
platform_attestation_review_id=<exact platform review id>
platform_attestation_sha256=<exact body sha256>
why=<Human rationale>
```

Require:

```text
decision review state = APPROVED
decision review later than platform attestation
decision request id/digest exact
referenced platform review id exact
referenced platform review body digest exact
platform review still active/current/fresh
no later conflicting Human decision
no superseding request
no replay/consumption
```

## 66. Freshness / activity / supersession / conflict preserved

A request is effect-capable only while exact current trusted GitHub state has one unambiguous active V14 decision and one unambiguous active referenced V14 platform attestation.

Block on:

```text
dismissal
conflicting later review
new request superseding old request
request body drift
platform snapshot drift
platform-attestation body drift
platform-attestation expiry
decision marker mismatch
already consumed effect
```

No latest-looking heuristic is authority.

## 67. Executor no-substitution preserved

The executor may not substitute:

```text
candidate content
scope
old OID
new OID
platform snapshot
platform attestation review
platform attestation body
Human decision review
Human rationale
mtime
object bytes
index bytes
ref/reflog bytes
worktree bytes
```

Any mismatch is `BLOCKED`, not auto-corrected.

# PART IX — FINAL EFFECT GATE AND MATERIAL SEQUENCE

## 68. FinalEffectGateV14

Immediately before material preparation/commitment, recompute and compare all authority-critical state.

Gate requires at least:

```text
exact repository baseline still valid
exact request still active/current
exact candidate/scope/effect still exact
exact proc/userns/credential state unchanged
exact repository mount unchanged
exact authenticated sysfs/block/NFIT topology unchanged
all nfit/format remain 0x0101
persistence_domain remains cpu_cache
deep_flush remains 0
platform_snapshot_sha256 remains exact
platform-attestation review still exact/APPROVED/not dismissed
platform-attestation age <= 900 seconds by GitHub server time
final Human decision review still exact/APPROVED/current and references exact platform attestation
ext4 internal journal still exact
ext4 option state still exact
ext4 errors_count = 0
mtime profile within horizon
object/ref/index/reflog/worktree topology unchanged
no staging residue except exact active staging root
no conflicting effect already committed
```

Any failed predicate blocks before the next material step.

## 69. Material sequence

The supported sequence remains ref-CAS-first with prepared durable prerequisites:

```text
1. validate request
2. validate platform snapshot
3. validate fresh platform attestation
4. validate final Human decision bound to that attestation
5. FinalEffectGateV14
6. prepare all new loose objects in bounded staging
7. seal object metadata/mtime + file fsync
8. install canonical loose objects with RENAME_NOREPLACE and directory fsync
9. require zero staging residue and exact object closure
10. prepare exact raw index replacement bytes
11. prepare exact ref/reflog/worktree projections
12. revalidate full authority state including platform attestation freshness
13. acquire exact main-ref commitment lock/CAS mechanism
14. revalidate immediately before ref rename, including fresh GitHub platform review/current decision
15. commit exact main ref + reflog projection under reviewed atomicity rules
16. fsync ref/reflog files and parent directories as required
17. install exact raw index projection and fsync
18. install exact worktree projection and fsync as specified
19. post-effect full verification
20. record success only after post-effect truth equals Human-bound effect
```

No pre-ref SUCCESS record is authoritative.

## 70. Failure / crash classification preserved

Before main-ref commitment:

```text
no Human-attributed success
staging residue = recovery-required/blocking state
canonical new loose object residue may exist only in states already classified by predecessor object-store rules
```

After main-ref commitment begins:

```text
any ambiguous ref/reflog/index/worktree completion = UNCERTAIN / RECOVERY REQUIRED
never roll back and call the operation cleanly failed unless exact durable prestate is proven
never report SUCCESS until exact post-effect truth is proven
```

No recovery mutation is authorized by this brief.

## 71. CRASH_DURABLE_OBJECT_REF_INDEX_V9

The V14 durability profile is the predecessor crash-durable object/ref/index profile plus:

```text
NVDIMM FIC bound to 0x0101
persistence_domain bound to cpu_cache
deep_flush bound to 0
current Human out-of-band platform-persistence attestation bound to exact request/snapshot
platform attestation revalidated through material commitment
```

Any one missing component removes success authority.

## 72. ALIAS_SAFE_MAIN_REF_COMMITMENT_V10

Preserve predecessor main-ref CAS, physical topology, no-alias and fsync ordering.

Add to the pre-rename authority gate:

```text
platform_snapshot unchanged
platform attestation current/fresh
Human decision still references exact attestation
```

If GitHub read state cannot be refreshed at this gate, do not rename main ref.

## 73. REF_CAS_FIRST_ALIAS_SAFE_RAW_GIT_METADATA_V12

The aggregate V14 effect profile is:

```text
raw SHA-1 objects
closed object store
bounded staging
Human-bound mtime
full single-file raw index
physical loose main ref
exact deterministic reflog projection
exact worktree projection
ref CAS first
closed hook/filter/config behavior
authenticated proc/userns/mount/sysfs/ext4 state
energy-backed NFIT FIC
explicit CPU-cache persistence domain
no deep flush requirement
fresh out-of-band Human platform persistence attestation
fresh final Human decision bound to that attestation
post-effect truth before SUCCESS
```

# PART X — SUCCESS RECORD AND HUMAN ATTRIBUTION

## 74. Success record V14

A durable success record must include at least:

```text
schema version V14
request id/digest
Human decision review id/body digest/author
platform attestation review id/body digest/author
platform snapshot digest
nfit format profile
persistence_domain profile
deep_flush profile
old main OID
new main OID
candidate/effect digest
object closure digest
index/ref/reflog/worktree projection digests
post-effect verification result
```

No success record may claim that the executor proved bare metal from guest software.

It records that a trusted Human out-of-band platform attestation was an explicit prerequisite.

## 75. Human attribution rule

The final attributed proposition is narrowly:

```text
A trusted Human made the exact V14 decision for the exact effect,
after/with explicit reference to a distinct trusted Human platform-persistence attestation
for the exact request-bound platform snapshot.
```

It is not:

```text
the AI decided
the executor inferred Human intent
the executor inferred physical hardware solely from ACPI/NFIT
the platform attestation itself authorized the effect
```

# PART XI — MANDATORY REGRESSIONS

## 76. PR #141 F001 regressions

At minimum:

```text
nfit/format=0x0101 + persistence_domain=cpu_cache + deep_flush=0 -> kernel-state positive candidate only
nfit/format=0x0301 -> BLOCK
nfit/format=0x0201 -> BLOCK
nfit/format absent -> BLOCK
persistence_domain=memory_controller -> BLOCK
persistence_domain absent -> BLOCK
persistence_domain unknown -> BLOCK
deep_flush=1 -> BLOCK
deep_flush absent -> BLOCK
deep_flush indeterminate -> BLOCK
nfit flags empty but persistence_domain unresolved -> BLOCK
successful fsync with persistence_domain unresolved -> never success proof
FIC/persistence/deep_flush drift between gates -> BLOCK/UNCERTAIN according to material stage
```

## 77. PR #141 F002 regressions

At minimum:

```text
QEMU vNVDIMM + memory-backend-ram -> BLOCK without trusted platform attestation
QEMU vNVDIMM + ordinary non-DAX memory-backend-file -> BLOCK without trusted platform attestation
QEMU vNVDIMM + pmem=off -> BLOCK without trusted platform attestation
QEMU vNVDIMM + share/MAP_SYNC prerequisites absent -> BLOCK without trusted platform attestation
QEMU vNVDIMM + unarmed=off -> still BLOCK without trusted platform attestation
QEMU vNVDIMM + nvdimm-persistence=cpu -> still BLOCK without trusted platform attestation
QEMU vNVDIMM + nvdimm-persistence=mem-ctrl -> still BLOCK without trusted platform attestation
guest ACPI0012 + ACPI.NFIT shape alone -> never positive authority
guest nfit/flags empty alone -> never positive authority
guest FIC spoofed to 0x0101 -> still BLOCK without platform attestation
guest persistence_domain spoofed to cpu_cache -> still BLOCK without platform attestation
guest deep_flush spoofed to 0 -> still BLOCK without platform attestation
platform marker in PR comment -> BLOCK
AI-authored platform marker -> BLOCK
caller-provided platform marker text -> BLOCK
platform review body exact but review not APPROVED -> BLOCK
platform review dismissed -> BLOCK
platform review older than 900s -> BLOCK
platform review request digest mismatch -> BLOCK
platform snapshot digest mismatch -> BLOCK
multiple conflicting current platform attestations -> BLOCK
Human decision not referencing exact platform review id/body digest -> BLOCK
```

## 78. Platform-attestation sequencing regressions

```text
platform review before request publication -> BLOCK
platform review after final decision review -> BLOCK
platform review changed/superseded after decision -> BLOCK
new platform review without new final decision -> BLOCK
new final decision referencing stale platform review -> BLOCK
GitHub server time unavailable -> BLOCK
attestation fresh at admission but expired before ref lock -> BLOCK before ref commitment
```

## 79. Preserve R4R13 internal-journal regressions

```text
internal journal raw predicate -> supported candidate
s_journal_inum = 0 -> BLOCK
s_journal_uuid nonzero -> BLOCK
s_journal_dev nonzero -> BLOCK
INCOMPAT_JOURNAL_DEV -> BLOCK
external journal otherwise valid -> BLOCK
raw device != mounted sb_dev -> BLOCK
```

## 80. Preserve prior procfs/mount regressions

```text
/proc authority file bind-overmount -> BLOCK via no-cross-mount provenance
noninitial user namespace hidden by substituted /proc path -> BLOCK
uid_map/gid_map substitution -> BLOCK
ID-mapped repository mount -> BLOCK
statmount unavailable/inconsistent -> BLOCK
casefold namespace -> BLOCK
unreviewed inode semantic flag -> BLOCK
```

## 81. Preserve prior object/index/ref regressions

```text
stale staging residue -> BLOCK
split index/sharedindex -> BLOCK
object alternates/promisor/lazy fetch -> BLOCK
pre-existing object wrong mtime -> reseal+fsync or BLOCK under exact profile
object EEXIST wrong bytes/security/mtime -> BLOCK
physical main ref alias -> BLOCK
replacement refs -> BLOCK
configured hook/filter writer -> BLOCK
ref CAS loses race -> no success
post-ref uncertain projection -> UNCERTAIN, never clean success
```

# PART XII — REVIEW BASIS AND SOURCE SEMANTICS

## 82. Current Linux semantics independently checked for R4R14

The R4R14 correction is grounded against current Linux source state reviewed on 2026-09-02, including commit:

```text
89a312991dc6e638a36adc43ccb91dbc25504c04
```

Relevant paths include:

```text
drivers/nvdimm/region_devs.c
drivers/nvdimm/pmem.c
drivers/acpi/nfit/core.c
drivers/acpi/nfit/nfit.h
include/linux/libnvdimm.h
fs/ext4/super.c
```

Semantics used by this brief include:

```text
persistence_domain exposes cpu_cache / memory_controller when corresponding region flags exist
deep_flush renders nvdimm_has_flush() as 0/1 and is unavailable when capability is indeterminate
NFIT_FIC_BYTE = 0x0101 byte-addressable energy backed
NFIT_FIC_BLK = 0x0201 block-addressable non-energy backed
NFIT_FIC_BYTEN = 0x0301 byte-addressable non-energy backed
nfit/format exposes the control-region code
```

## 83. Current QEMU semantics independently checked for R4R14

The F002 correction is grounded against current QEMU source/docs reviewed on 2026-09-02, including commit:

```text
a925240509d1b4b656cc480f1cc79ba4d7c8bc08
```

Relevant paths include:

```text
docs/nvdimm.txt
docs/specs/acpi_nvdimm.rst
hw/acpi/nvdimm.c
hw/mem/nvdimm.c
```

The reviewed counterexample remains that QEMU can present standard ACPI0012/NFIT vNVDIMM guest state while backend persistence depends on separate host-side conditions.

V14 therefore makes a trusted out-of-band platform attestation mandatory instead of attempting to distinguish all hypervisors from guest state.

# PART XIII — EXACT REVIEW CHECKLIST

## 84. Independent R4R14 review must answer at least

```text
Does V14 really bind current nfit/format for every mapped nmem?
Is 0x0101 correctly treated as the only reviewed energy-backed FIC?
Can any accepted path omit persistence_domain?
Can any accepted path omit deep_flush?
Can deep_flush=1 sneak through a parser alias?
Can memory_controller sneak through an alias/default?
Can guest ACPI/NFIT alone ever satisfy platform authority?
Can a PR comment or AI-authored review satisfy platform attestation?
Can caller-supplied review id/body select authority?
Can stale/dismissed/conflicting platform attestation survive?
Can a new platform attestation be used without a new final Human decision?
Does the final Human decision bind exact platform review id and exact body digest?
Can standard QEMU vNVDIMM with memory-backend-ram pass without trusted platform review?
Can QEMU with nvdimm-persistence=cpu pass without trusted platform review?
Can synthetic 0x0101/cpu_cache/deep_flush=0 guest state pass without trusted platform review?
Does the 900-second freshness recheck occur before ref lock and ref rename?
Does any GitHub outage cause effect rather than BLOCK?
Are R4R13 internal-journal rules preserved exactly?
Are prior object/ref/index/reflog/worktree durability controls preserved?
```

## 85. Expected finding disposition target

R4R14 is intended to permit an independent reviewer to conclude, if no new blocker is found:

```text
R4R13 F001 NVDIMM PERSISTENCE-DOMAIN / DEEP-FLUSH = ADDRESSED AT BRIEF LEVEL
R4R13 F002 VIRTUAL ACPI NFIT BACKEND ATTESTATION   = ADDRESSED AT BRIEF LEVEL
```

This target is not a predeclared PASS. Independent review must decide.

# PART XIV — STOP BOUNDARY

## 86. Explicit non-authority

This brief does not authorize:

```text
independent R4R14 review under the same Human authorization
ScriptOps implementation
creation/submission of platform-attestation review
creation/submission of Human decision review
positive Human control
canonical screenplay effect
recovery mutation
merge
X1B closure
Agency Kernel v1 authority
release
deployment
tag
```

## 87. Next legal step

After this exact R4R14 brief is durably frozen in one draft PR, STOP.

The next legal step is:

```text
fresh Human authorization
-> exactly one independent AK-CANON adversarial review
   of the exact frozen R4R14 implementation brief
```

Preserve:

```text
AI PROPOSES != HUMAN DECIDES
REVIEW FINDING != REPAIR AUTHORITY
R4R14 BRIEF != IMPLEMENTATION AUTHORITY
R4R14 REVIEW PASS != IMPLEMENTATION AUTHORITY
X1B OPEN != V1 AUTHORITY
```
