# X1B Human Decision Authorship — Independent AK-CANON R4R13 Implementation-Brief Review

Status: `INDEPENDENT REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: `2026-09-02`

## 1. Verdict

`AK-CANON X1B R4R13 IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

R4R13 is a material improvement over R4R12. The exact prior counterexamples frozen by PR #139 are addressed at brief level:

1. a generic `/dev/<name>` ext4 filesystem on zram/ramdisk is no longer admitted merely because ext4, barriers and `fsync()` succeed. V13 deliberately narrows the supported primary-storage profile to a direct whole `/dev/pmem<N>` whose guest-visible Linux topology must look like one ACPI NFIT LIBNVDIMM PMEM namespace/region;
2. ext4 journal location is no longer inferred from `journal_task`. V13 requires an internal reserved-inode journal from raw primary-superblock fields and rejects the external-journal topology.

The explicit `EXT4_RUNTIME_OPTION_TABLE_V13` also closes the R4R12 implementation-discretion note about an unspecified option allowlist.

However, independent adversarial review found two new blockers in the persistence authority below those improvements:

1. `ACPI_NFIT_PMEM_PERSISTENT_BLOCK_V1` does not bind the Linux NVDIMM region persistence-domain / deep-flush contract that current libnvdimm exposes specifically to describe how writes become persistent. V13 binds provider, mappings and NVDIMM identity/health fields, but it never reads `regionX/persistence_domain` or `regionX/deep_flush`. Current Linux can therefore reach a no-explicit-flush path by assuming a platform persistence mechanism such as ADR when no explicit flush method/hints are present. That assumption is outside the Human-bound V13 request even though it is authority-critical to the claimed power-loss durability;
2. guest-visible ACPI NFIT provenance is not proof of non-virtual persistent backing. Current QEMU can expose a standard ACPI0012/NFIT virtual NVDIMM whose guest storage may be backed by `memory-backend-file` or `memory-backend-ram`. QEMU documents that only the reviewed DAX/PMEM backend conditions guarantee guest write persistence; other backends may have no persistence guarantee, those conditions are ignored for compatibility, and `unarmed` is merely recommended for such backends. QEMU can separately advertise `nvdimm-persistence=cpu` or `mem-ctrl` to the guest. Thus even adding a guest `persistence_domain` check would not establish the host/backend persistence that V13 claims unless the execution environment itself is authenticated as non-virtual or the backend is independently attested.

Either new finding independently prevents implementation authority.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R13 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R13 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#140`

```text
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
BASE TREE = df807db7003dfd201e9be4d5927472e515a2e737
HEAD = d0e420ffa08384f4f11efc6edcd042ebb21b4280
TREE = 66fb4a95313287a5715143b64cfa47e0025e6e6e
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R13.md
BLOB = 6da06d21b05c8acbe6a6a39793ec0b1e54396204
```

Immediately before review write, PR #140 remained:

```text
state = OPEN
merged = false
draft = true
mergeable = true
commits = 1
changed_files = 1
additions = 1571
deletions = 0
```

`FJ899/8 main` remained exactly:

```text
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

The exact R4R13 file was freshly reread from the reviewed HEAD before this artifact was written.

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
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_DESIGN_AK_CANON_REVIEW_R2.md
BLOB = 439109e104244552a5ac1f3f08988dba283733d0
VERDICT = AK-CANON X1B CORRECTIVE DESIGN REVIEW R2 = PASS
```

### 3.3 R4R12 predecessor

```text
FJ899/8 PR #138
HEAD = b960778d5f33ba0b3a5beb74a5bb08107afa40f9
TREE = 112129e06f5484e33984521816b0aec52ae69d63
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R12.md
BLOB = 6e1dfb2342a7a97d5a3adbc2992bb8bb19fb121d
```

### 3.4 Binding R4R12 NOT-PASS review

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

PR #139 also recorded that the PR #137 procfs-provenance and ext4-option-state findings were addressed at brief level.

## 4. Review method

This review attacks the exact R4R13 artifact rather than assuming that a narrower storage name/topology is itself a persistence proof.

The adversarial pass inspected at least:

```text
exact PR/base/head/blob freeze
ACPI NFIT provider provenance
/sys/dev/block major/minor binding
whole pmem block rule
namespace / region / mapping ancestry
ACPI0012 ancestry rule
NVDIMM health flags
NVDIMM control-region identity fields
Linux persistence-domain semantics
Linux NVDIMM flush semantics
PMEM REQ_PREFLUSH / REQ_FUA path
virtual ACPI NFIT implementations
QEMU vNVDIMM backend choices
QEMU unarmed semantics
QEMU NFIT platform-persistence advertisement
QEMU NFIT control-region format semantics
raw ext4 primary-superblock read
internal versus external journal selection
mount-time journal override behavior
closed ext4 nodefs option rendering
prior procfs / userns / idmap corrections
loose-object mtime and staging preservation
raw ref/index/reflog/worktree commitment preservation
V13 schema migration
Human currentness / replay / no-substitution boundaries
```

## 5. Current external semantics checked

The review checked current public source rather than relying on historical behavior.

Linux source commit used for semantic inspection:

```text
89a312991dc6e638a36adc43ccb91dbc25504c04
```

Relevant Linux sources:

```text
include/linux/libnvdimm.h
drivers/nvdimm/region_devs.c
drivers/nvdimm/pmem.c
drivers/acpi/nfit/core.c
fs/ext4/super.c
```

Current QEMU source/docs used for the virtual-NVDIMM counterexample:

```text
a925240509d1b4b656cc480f1cc79ba4d7c8bc08
```

Relevant QEMU sources/docs:

```text
docs/nvdimm.txt
docs/specs/acpi_nvdimm.rst
hw/acpi/nvdimm.c
hw/mem/nvdimm.c
```

## 6. PR #139 F001 disposition — generic backing-device class

Disposition for the exact prior counterexample: `ADDRESSED AT BRIEF LEVEL`.

R4R12 allowed any direct `/dev/<kernel-devname>` and therefore admitted concrete RAM-backed examples such as:

```text
/dev/zram*
/dev/ram*
```

R4R13 now supports only:

```text
/dev/pmem<N>
whole device
exact mounted sb_dev major/minor
exact /sys/dev/block/M:m identity
LIBNVDIMM nd_pmem region
provider = ACPI.NFIT
positive region nfit/range_index
explicit region mappings
raw PMEM namespace personality
empty nfit/flags for all mapped nmem devices
```

and explicitly rejects zram, ramdisk, loop, device-mapper, md, network block, virtio/xen block, NVMe, SCSI/SATA, CXL, E820/manual/test PMEM, DAX character devices, BTT/PFN personalities, partitions and unknown stacks.

That closes the exact R4R12 path-name/classification defect.

It does not prove that every environment capable of producing the accepted guest-visible ACPI NFIT shape has a persistent physical backing medium. That is the subject of new findings F001/F002 below.

## 7. PR #139 F002 disposition — external ext4 journal

Disposition: `ADDRESSED AT BRIEF LEVEL`.

R4R13 requires from the raw primary ext4 superblock:

```text
HAS_JOURNAL set
s_journal_inum > 0
s_journal_uuid = zero
s_journal_dev = 0
INCOMPAT_JOURNAL_DEV absent
```

The independent review specifically tested whether mount-time `journal_dev=` / `journal_path=` could silently override that raw internal-journal selection.

Current ext4 source does not permit the dangerous combination.

`ext4_load_journal()` first derives a possible external `journal_dev` from the mount override or superblock. It then rejects:

```text
journal_inum != 0 AND journal_dev != 0
```

with `EINVAL` before choosing the journal implementation.

If `journal_inum` is nonzero, current ext4 opens the inode journal. Only the zero-inum branch calls the external-device journal path.

Therefore the V13 predicate `s_journal_inum > 0` plus zero external fields cannot be silently converted into a mounted external-journal filesystem by a mount override.

Current source checked:

```text
https://github.com/torvalds/linux/blob/89a312991dc6e638a36adc43ccb91dbc25504c04/fs/ext4/super.c
```

The old PR #139 external-JBD2-write-domain attack is therefore not reopened.

## 8. Explicit ext4 option table disposition

PR #139 noted that R4R12 referred to a reviewed option table without actually freezing the table.

R4R13 corrects that omission with `EXT4_RUNTIME_OPTION_TABLE_V13`.

The review compared the table against current `_ext4_show_options(..., nodefs=1)` / `ext4_seq_options_show()` behavior.

Current source confirms the full nodefs view renders state classes and explicit values including:

```text
rw / ro
positive/negative ext4 mount flags
resuid / resgid
errors policy
commit interval
batch times
stripe
data mode
inode_readahead_blks
init_itable
max_dir_size_kb
DAX mode
mb_optimize_scan where applicable
prefetch state
emergency_ro
shutdown
quota state
```

R4R13 freezes accepted and rejected classes rather than delegating an allowlist to implementation discretion.

No independent blocker is raised here in this review.

## 9. Finding X1B-R4R13-IBR-F001 — NVDIMM persistence-domain / deep-flush authority is not bound

Severity: `BLOCKER`.

### 9.1 V13 proves identity and health, not the kernel persistence domain

`ACPI_NFIT_PMEM_PERSISTENT_BLOCK_V1` binds many useful fields:

```text
ACPI.NFIT provider
ACPI0012 ancestry
region devtype nd_pmem
range_index
mapping topology
namespace personality
NVDIMM IDs
NVDIMM nfit/flags
```

But it never reads or binds the current Linux region attributes:

```text
regionX/persistence_domain
regionX/deep_flush
```

The exact R4R13 artifact contains no normative occurrence of either authority source.

### 9.2 Linux exposes persistence domain as first-class state

Current libnvdimm defines distinct region persistence flags.

`ND_REGION_PERSIST_CACHE` means the platform ensures the entire CPU-store path is flushed to PMEM on system power loss.

`ND_REGION_PERSIST_MEMCTRL` means the platform automatically flushes outstanding memory-controller writes to PMEM on system power loss, i.e. the ADR-style domain.

Current Linux exposes those flags through region sysfs:

```text
persistence_domain = cpu_cache
persistence_domain = memory_controller
```

and hides the attribute when neither persistence-domain flag is established.

Sources checked:

```text
https://github.com/torvalds/linux/blob/89a312991dc6e638a36adc43ccb91dbc25504c04/include/linux/libnvdimm.h
https://github.com/torvalds/linux/blob/89a312991dc6e638a36adc43ccb91dbc25504c04/drivers/nvdimm/region_devs.c
```

### 9.3 ACPI NFIT platform capabilities drive those flags

Current ACPI NFIT source maps firmware platform-capability state into the libnvdimm persistence-domain flags.

Conceptually:

```text
ACPI_NFIT_CAPABILITY_CACHE_FLUSH
    -> ND_REGION_PERSIST_CACHE

else ACPI_NFIT_CAPABILITY_MEM_FLUSH
    -> ND_REGION_PERSIST_MEMCTRL
```

Source checked:

```text
https://github.com/torvalds/linux/blob/89a312991dc6e638a36adc43ccb91dbc25504c04/drivers/acpi/nfit/core.c
```

Thus the persistence-domain state is not redundant with:

```text
provider = ACPI.NFIT
range_index > 0
nfit/flags empty
```

It answers a different question: which power-fail persistence domain the platform actually claims.

### 9.4 Current deep-flush behavior contains a compatibility assumption

Current `nvdimm_has_flush()` determines whether explicit NVDIMM flushing is needed.

It returns a positive result if there is an explicit asynchronous flush function or if any mapped NVDIMM exposes flush hints.

But when neither is present, current source states that the platform is assumed to provide a persistence mechanism such as ADR, and the function returns that no explicit flush is required.

Current region sysfs exposes this through `deep_flush`.

Current PMEM block I/O handles `REQ_PREFLUSH` / `REQ_FUA` by calling `nvdimm_flush()`.

Therefore the eventual storage guarantee depends on one of two classes:

```text
explicit flush mechanism/hints
OR
platform persistence-domain assumption
```

V13 binds neither the current `deep_flush` state nor the current `persistence_domain` state.

Sources checked:

```text
https://github.com/torvalds/linux/blob/89a312991dc6e638a36adc43ccb91dbc25504c04/drivers/nvdimm/region_devs.c
https://github.com/torvalds/linux/blob/89a312991dc6e638a36adc43ccb91dbc25504c04/drivers/nvdimm/pmem.c
```

### 9.5 Concrete false-authority class

Consider an ACPI NFIT PMEM region for which all V13 identity and `nfit/flags` predicates pass, but:

```text
no explicit NFIT/platform persistence-domain capability is bound by V13
no explicit flush method/hint is bound by V13
```

Linux may still expose a functioning PMEM block device and allow the filesystem to perform successful flush/FUA operations while the no-explicit-flush path rests on the kernel's compatibility assumption that the platform provides persistence such as ADR.

That is not a Human-bound V13 fact.

The accepted higher-level design requires:

```text
no core authority/security choice left implicit
```

The power-loss persistence domain is core durability authority, not optional diagnostics.

### 9.6 Why `nfit/flags` does not substitute

The V13 health gate correctly rejects:

```text
save_fail
restore_fail
flush_fail
not_armed
smart_event
map_fail
smart_notify
```

Those are device/mapping health signals.

They do not encode the region's CPU-cache or memory-controller persistence domain and do not prove whether an explicit deep flush is required.

Empty health flags therefore do not close this finding.

### 9.7 Why successful filesystem fsync does not substitute

Successful ext4/JBD2 synchronization proves that the filesystem completed its synchronization contract through the block layer.

For PMEM, the final block-layer persistence semantics depend on the platform persistence/flush contract just described.

V13 cannot use successful `fsync()` to prove the premise that determines what the PMEM driver's flush completion means.

That would be circular.

### 9.8 Required successor correction

A successor must freeze a complete persistence-domain/flush predicate rather than inheriting libnvdimm's fallback assumption invisibly.

At minimum the successor must Human-bind and repeatedly revalidate exact current region state sufficient to distinguish, as applicable:

```text
persistence_domain = cpu_cache
persistence_domain = memory_controller
persistence_domain unavailable/empty
explicit deep flush required
explicit deep flush not required
flush capability indeterminate
```

The supported positive path must be reviewably defined.

A simple narrow successor may accept only one explicitly exposed persistence domain and reject absent/ambiguous persistence-domain state.

If an explicit flush-hint path is supported, the exact flush topology and `deep_flush` semantics must also be bound.

Until then:

```text
X1B-R4R13-IBR-F001 = BLOCKER
```

## 10. Finding X1B-R4R13-IBR-F002 — guest ACPI NFIT provenance does not attest virtual-NVDIMM backing persistence

Severity: `BLOCKER`.

### 10.1 V13 treats guest-visible ACPI NFIT shape as physical provenance

V13 labels its narrow profile:

```text
ACPI_NFIT_PMEM_PERSISTENT_BLOCK_V1
```

and attempts to exclude nonphysical stacks with rules including:

```text
provider = ACPI.NFIT
ACPI0012 ancestry
not nfit_test
not pmem-region test provider
not /sys/devices/virtual
not virtio/xen block
whole /dev/pmem<N>
```

Those checks distinguish several Linux software/test paths.

They do not prove that the executing Linux kernel is running on bare metal or that ACPI/NFIT was produced by physical platform firmware rather than a hypervisor.

### 10.2 QEMU exposes standard ACPI NVDIMM/NFIT

Current QEMU documentation states that virtual NVDIMM uses ACPI and the standard NVDIMM root device with:

```text
_HID = ACPI0012
```

QEMU constructs NFIT structures for its vNVDIMMs.

Current QEMU source builds a PMEM System Physical Address Range, Memory Device Mapping and NVDIMM Control Region structure.

The PMEM SPA is explicitly marked with the PMEM type GUID.

The control-region structure provides vendor/device/revision/serial identity fields.

QEMU therefore does not appear to Linux as the V13-rejected virtio-pmem path or as the in-kernel `nfit_test` provider. It exercises the normal ACPI NFIT guest path.

Sources checked:

```text
https://github.com/qemu/qemu/blob/a925240509d1b4b656cc480f1cc79ba4d7c8bc08/docs/specs/acpi_nvdimm.rst
https://github.com/qemu/qemu/blob/a925240509d1b4b656cc480f1cc79ba4d7c8bc08/hw/acpi/nvdimm.c
```

### 10.3 QEMU vNVDIMM storage can be nonpersistent

Current QEMU `docs/nvdimm.txt` states explicitly that vNVDIMM storage may be supplied by:

```text
memory-backend-file
memory-backend-ram
```

and that a guest with the NVDIMM driver detects the resulting device in persistent-memory mode.

The same documentation states that the only Linux backend classes that can guarantee guest write persistence are the reviewed DAX-device / DAX-file cases, with the required `pmem`, `share`, host-kernel and MAP_SYNC conditions for files.

If those conditions are not satisfied, guest write persistence is not guaranteed after system crash.

For compatibility reasons QEMU ignores unmet persistence conditions rather than refusing the configuration, and the documentation says there is no current way to test those conditions from this configuration path.

For other backend types QEMU merely suggests setting `unarmed=on`.

Source checked:

```text
https://github.com/qemu/qemu/blob/a925240509d1b4b656cc480f1cc79ba4d7c8bc08/docs/nvdimm.txt
```

### 10.4 `unarmed` is not a mandatory safeguard

Current QEMU source defines the NVDIMM `unarmed` property default as `false`.

Its NFIT builder sets the ACPI `NOT_ARMED` state bit only when the operator explicitly configures `unarmed`.

Therefore a virtual NVDIMM using a backend without crash-persistence guarantees can still present an empty `not_armed` health state to the guest.

Sources checked:

```text
https://github.com/qemu/qemu/blob/a925240509d1b4b656cc480f1cc79ba4d7c8bc08/hw/mem/nvdimm.c
https://github.com/qemu/qemu/blob/a925240509d1b4b656cc480f1cc79ba4d7c8bc08/hw/acpi/nvdimm.c
```

This directly defeats the inference:

```text
empty guest nfit/flags
=> physically persistent backing
```

### 10.5 QEMU can independently advertise a guest persistence domain

Current QEMU supports the machine option:

```text
nvdimm-persistence=cpu
nvdimm-persistence=mem-ctrl
```

which populates the ACPI NFIT Platform Capabilities Structure presented to the guest.

The QEMU documentation describes these as guest-visible CPU-cache or memory-controller persistence claims.

Crucially, this advertisement is separate from the backend-persistence conditions described elsewhere in the same documentation.

Thus a successor that fixes only F001 by requiring guest-visible:

```text
persistence_domain = cpu_cache
```

or:

```text
persistence_domain = memory_controller
```

still does not establish that the host virtual-NVDIMM backend is crash-persistent.

Source checked:

```text
https://github.com/qemu/qemu/blob/a925240509d1b4b656cc480f1cc79ba4d7c8bc08/docs/nvdimm.txt
```

This is why F002 is independent of F001.

### 10.6 V13 omits a kernel-exposed NFIT format field

Current Linux exposes the NFIT control-region Format Interface Code as:

```text
nfit/format
```

from the control-region `code` field.

R4R13 requires multiple NFIT identity attributes but does not bind `nfit/format`.

Current QEMU sets its virtual-NVDIMM control-region code to `0x0301` and comments that interface as byte-addressable with no energy backing.

Sources checked:

```text
https://github.com/torvalds/linux/blob/89a312991dc6e638a36adc43ccb91dbc25504c04/drivers/acpi/nfit/core.c
https://github.com/qemu/qemu/blob/a925240509d1b4b656cc480f1cc79ba4d7c8bc08/hw/acpi/nvdimm.c
```

This omitted field is not by itself the entire virtualization finding, because platform persistence can involve broader power-fail semantics.

It is nevertheless concrete evidence that V13's claimed closed NFIT identity profile omits a current kernel-exposed interface-semantics field while relying on surrounding NFIT identity as persistence authority.

### 10.7 Concrete counterexample shape

A supported QEMU configuration can conceptually combine:

```text
-machine pc,nvdimm=on,nvdimm-persistence=cpu
-object memory-backend-file,...,pmem=off
-device nvdimm,...,unarmed=off
```

with a backend not meeting the DAX/PMEM persistence requirements documented by QEMU.

Inside the guest, the ACPI NFIT path can provide:

```text
ACPI0012 root
ACPI.NFIT provider
PMEM SPA
/dev/pmem<N> namespace
positive NFIT range index
mapping/control-region identities
no NOT_ARMED flag
advertised CPU-cache persistence capability
```

while QEMU's own documentation states that the backend write-persistence guarantee is absent unless the separate host-side conditions are met.

Formatting that guest `/dev/pmem<N>` as ext4 does not add missing host-backend persistence.

The V13 predicates are all guest-visible and contain no host/backend attestation that distinguishes this configuration from the intended physical PMEM profile.

### 10.8 Why the V13 claim-boundary exclusion does not close this

R4R13 excludes from its durability claim:

```text
ACPI/firmware deliberately falsifying NFIT persistent-memory description
```

The QEMU counterexample is not malicious kernel modification and does not require corrupt or adversarial physical firmware.

It is a supported virtual-machine configuration in which QEMU intentionally emulates the standard ACPI NVDIMM interface and documents the distinction between guest vNVDIMM identity and host backend persistence.

Treating every hypervisor-generated ACPI NFIT environment as “firmware deliberately falsifying” would simply move the core execution-environment authentication choice into an unchecked exclusion.

That is incompatible with the higher-level rule:

```text
no core authority/security choice left implicit
```

### 10.9 Required successor correction

A successor must make the execution-environment trust boundary explicit.

Acceptable directions include one separately reviewable narrow path such as:

```text
prove the supported positive environment is bare metal through a reviewed non-virtual platform-attestation profile
```

or:

```text
if virtualization is supported, bind an independently authenticated host/hypervisor backend persistence attestation that cannot be synthesized solely from guest ACPI/NFIT state
```

Merely adding more guest-visible NFIT fields is not sufficient if the hypervisor controls all of them.

At minimum, a successor must include negative regressions showing that a QEMU ACPI vNVDIMM on:

```text
memory-backend-ram
ordinary non-DAX memory-backend-file
file backend with persistence prerequisites absent
```

cannot satisfy the positive durability profile, even when:

```text
unarmed=off
nvdimm-persistence=cpu or mem-ctrl
```

is advertised to the guest.

Until then:

```text
X1B-R4R13-IBR-F002 = BLOCKER
```

## 11. Internal-journal adversarial check

The review specifically does **not** freeze a false finding about `journal_dev=` overriding an internal journal.

Current ext4 behavior was checked directly.

The decisive sequence is:

```text
journal_inum = on-disk s_journal_inum
journal_dev = mount override or on-disk s_journal_dev

if journal_inum && journal_dev:
    reject mount

if journal_inum:
    open inode journal
else:
    open device journal
```

Therefore a mounted filesystem satisfying the V13 internal-journal raw predicate cannot simultaneously be using a nonzero external journal override under the reviewed current ext4 semantics.

This review records:

```text
R4R12 F002 EXTERNAL JOURNAL WRITE DOMAIN = ADDRESSED AT BRIEF LEVEL IN R4R13
```

No successor should weaken that raw-superblock predicate.

## 12. Preservation of earlier corrections

The independent pass found no reason in the two new findings to reopen the established brief-level corrections for:

```text
procfs current-task provenance
single-file bind/submount rejection
initial user namespace identity
uid_map/gid_map binding
execution credential stability
non-ID-mapped ext4 mount
casefold/inode semantic flags
full ext4 option source authentication
barrier/data-mode restrictions
Human-bound loose-object mtime
bounded object staging namespace
pre-ref canonical object residue
single-file raw index / no split-index
physical loose main ref
reflog replacement metadata
raw worktree projection
replacement refs
hooks/configured hooks
lazy fetch/promisor behavior
ref CAS and post-effect projection
request/review/currentness/replay binding
```

This statement is limited to interactions inspected in the R4R13 review. It is not a blanket proof of future implementation correctness.

## 13. Mandatory successor regressions implied by this review

A successor review must attack at least the following additional cases.

### 13.1 Persistence-domain / flush authority

```text
explicit accepted persistence_domain -> positive candidate
persistence_domain absent -> BLOCK unless a separately reviewed explicit-flush profile proves persistence
persistence_domain unexpected -> BLOCK
deep_flush unavailable/indeterminate -> BLOCK
deep_flush state changes between gates -> BLOCK/uncertainty
flush-hint topology changes -> BLOCK/uncertainty
nfit flags empty but persistence domain unresolved -> BLOCK
successful fsync with persistence domain unresolved -> never success proof
```

### 13.2 Virtual ACPI NFIT

```text
QEMU vNVDIMM + memory-backend-ram -> BLOCK
QEMU vNVDIMM + ordinary non-DAX file backend -> BLOCK
QEMU vNVDIMM + pmem=off -> BLOCK
QEMU vNVDIMM + share/persistence prerequisites missing -> BLOCK
QEMU vNVDIMM + unarmed=off -> still BLOCK without independent backend attestation
QEMU vNVDIMM + nvdimm-persistence=cpu -> still BLOCK without independent backend attestation
QEMU vNVDIMM + nvdimm-persistence=mem-ctrl -> still BLOCK without independent backend attestation
guest ACPI0012 + ACPI.NFIT shape alone -> never bare-metal proof
guest nfit/flags empty alone -> never host-backend proof
```

### 13.3 NFIT semantics

If the successor continues to use NFIT identity as authority, review at least:

```text
nfit/format exact value and semantics
persistence_domain exact value
region deep_flush exact value/availability
all mapped-nmem health state
range/mapping identity drift
namespace personality drift
provider/ACPI ancestry drift
```

### 13.4 Preserve R4R13 internal-journal negatives

```text
internal journal raw predicate -> supported candidate
s_journal_inum = 0 -> BLOCK
s_journal_uuid nonzero -> BLOCK
s_journal_dev nonzero -> BLOCK
INCOMPAT_JOURNAL_DEV -> BLOCK
mount journal_dev/path against internal-inode fs -> mount must fail / never admitted
external journal otherwise valid -> BLOCK
raw device != mounted sb_dev -> BLOCK
```

## 14. Review verdict matrix

```text
PR #139 F001 generic /dev-backed persistence class       = ADDRESSED AT BRIEF LEVEL FOR EXACT PRIOR COUNTEREXAMPLES
PR #139 F002 external ext4 journal write domain          = ADDRESSED AT BRIEF LEVEL
PR #139 ext4 option-table implementation discretion      = ADDRESSED AT BRIEF LEVEL

X1B-R4R13-IBR-F001 persistence-domain/deep-flush proof   = BLOCKER
X1B-R4R13-IBR-F002 virtual ACPI NFIT backend attestation = BLOCKER

AK-CANON X1B R4R13 IMPLEMENTATION-BRIEF REVIEW           = NOT PASS
IMPLEMENTATION AUTHORITY                                  = NOT ESTABLISHED
X1B                                                       = OPEN
V1 AUTHORITY                                              = NOT ESTABLISHED
```

## 15. No implementation authority

This artifact is review evidence only.

It does not authorize:

```text
R4R14 or another successor correction
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
   X1B-R4R13-IBR-F001
   X1B-R4R13-IBR-F002
```

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
REVIEW PASS WOULD STILL != IMPLEMENTATION AUTHORITY
AI PROPOSES != HUMAN DECIDES
```
