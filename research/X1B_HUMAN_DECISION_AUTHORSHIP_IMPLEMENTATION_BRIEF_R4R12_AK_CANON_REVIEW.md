# X1B Human Decision Authorship — Independent AK-CANON R4R12 Implementation-Brief Review

Status: `INDEPENDENT REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: `2026-09-02`

## 1. Verdict

`AK-CANON X1B R4R12 IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

R4R12 materially improves R4R11 and addresses both findings frozen in PR #137 at brief level:

1. procfs authority-source provenance is no longer based on unverified `/proc/self/...` pathnames. V12 authenticates a held procfs root, binds the procfs instance to direct `getpid()` / `gettid()` values through the genuine `thread-self` entry, then resolves numeric current-task authority paths with descriptor-relative `openat2()` plus `RESOLVE_BENEATH|RESOLVE_NO_XDEV|RESOLVE_NO_SYMLINKS`;
2. ext4 durability-affecting mount-option state is no longer inferred from filesystem type plus generic superblock flags. V12 requires `STATMOUNT_MNT_OPTS`, `STATMOUNT_OPT_ARRAY`, a full authenticated `/proc/fs/ext4/<dev>/options` runtime view, and authenticated ext4 sysfs journal/error state.

The V12 schema migration correctly prevents V11 or earlier Human evidence from authorizing the changed proc-authority and durability profile.

However, independent adversarial review found two new blockers below the ext4 mount-option layer:

1. `EXT4_BARRIERED_FSYNC_DURABILITY_V1` does not bind or restrict the persistence class and backing topology of the repository block device. V12 accepts any exact `sb_source` shaped as `/dev/<kernel-devname>` and binds only the device major/minor plus ext4-visible state. Linux intentionally provides RAM-backed block devices such as `/dev/zram*` and `/dev/ram*`; current kernel documentation explicitly shows creating and mounting ext4 on zram. Such devices satisfy the V12 source-name grammar while their contents are stored in system memory and are not persistent across reboot/power loss. No V12 predicate distinguishes a durable storage device from a volatile RAM-backed block device;
2. V12 requires that an ext4 journal exist but neither rejects nor binds an external ext4 journal device. Current ext4 supports a journal on a separate block device, and current JBD2 explicitly distinguishes `j_dev` (journal storage device) from `j_fs_dev` (filesystem device). R4R12 binds only the repository filesystem `sb_source` / `sb_dev_major` / `sb_dev_minor` and reads `journal_task`; it does not establish whether the journal is internal, identify an external journal device, or apply the durability profile to that second write domain.

Either finding independently prevents implementation authority.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R12 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R12 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#138`

```text
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
BASE TREE = df807db7003dfd201e9be4d5927472e515a2e737
HEAD = b960778d5f33ba0b3a5beb74a5bb08107afa40f9
TREE = 112129e06f5484e33984521816b0aec52ae69d63
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R12.md
BLOB = 6e1dfb2342a7a97d5a3adbc2992bb8bb19fb121d
```

Immediately before review write, PR #138 remained:

```text
state = OPEN
merged = false
draft = true
mergeable = true
commits = 1
changed_files = 1
additions = 2494
deletions = 0
```

`FJ899/8 main` also remained exactly:

```text
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

The exact R4R12 file was freshly reread from the reviewed HEAD before this artifact was written.

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

### 3.3 R4R11 predecessor and binding review

```text
FJ899/8 PR #136
HEAD = 0f5c5ed3406404942cafbffd7d1161d7f96e32a2
TREE = 24800c2bcaa9d1f9f2b380f8579ff40016a42c74
BLOB = 9ea872947b6e38ed0cf188f55aca522667e579bb
```

```text
FJ899/8 PR #137
HEAD = ae35d3778023e8076eaff57634089aa0f2cc7e3c
TREE = 27bdd393639b225a8654ba6ee20db8f7419fa7d2
BLOB = f0c3b2822c075920af9565aaa18fed65a47992a2
VERDICT = AK-CANON X1B R4R11 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #137 froze:

```text
X1B-R4R11-IBR-F001 — procfs authority-source provenance is not bound
X1B-R4R11-IBR-F002 — ext4 durability-affecting mount options are not bound
```

## 4. Review method

The review attacked the exact R4R12 artifact rather than treating stronger provenance and mount-option checks as sufficient by construction.

The adversarial pass inspected at least:

```text
/proc root provenance
proc unique mount identity
thread-self to direct getpid/gettid binding
numeric current-process/current-thread descriptor resolution
RESOLVE_NO_XDEV bind/submount rejection
user namespace identity source
uid_map/gid_map source
mount-namespace source
execution credential cross-checking
statx/statmount repository mount identity
STATMOUNT_MNT_OPTS / OPT_ARRAY use
full ext4 /proc runtime option source
ext4 sysfs journal/error source
barrier/data/journal_async_commit constraints
filesystem source grammar
underlying block-device persistence class
RAM-backed block devices
loop/device-mapper/network-style block-device classes
external ext4 journal support
JBD2 filesystem-device versus journal-device split
fsync durability claim boundary
Human-bound loose-object mtime preservation
request-bound object staging and crash classifications
V12 request/review/effect schema migration
prior index/ref/reflog/worktree corrections
```

## 5. Current external semantics checked

### 5.1 `openat2()` no-cross-mount semantics

Current Linux `openat2(2)` documents that:

```text
RESOLVE_NO_XDEV
```

disallows traversal across mount points, including bind mounts, and returns `EXDEV` on such a crossing.

Source checked:

```text
https://man7.org/linux/man-pages/man2/openat2.2.html
```

This supports the V12 correction for the exact PR #137 procfs-overmount attack class.

### 5.2 Linux fsync durability semantics

Current Linux `fsync(2)` describes synchronization to a disk or other permanent storage device so changed information remains retrievable after system crash or reboot.

Source checked:

```text
https://man7.org/linux/man-pages/man2/fsync.2.html
```

Thus successful `fsync()` calls are not, by themselves, a proof that an arbitrary Linux block device represents nonvolatile/persistent storage.

### 5.3 RAM-backed Linux block devices

Current kernel documentation states that zram creates RAM-based block devices:

```text
/dev/zram<id>
```

whose pages are compressed and stored in memory itself.

The current kernel zram documentation explicitly gives this supported activation example:

```text
mkfs.ext4 /dev/zram1
mount /dev/zram1 /tmp
```

Sources checked:

```text
https://cdn.kernel.org/doc/html/latest/admin-guide/blockdev/zram.html
https://docs.kernel.org/admin-guide/blockdev/zram.html
```

Current kernel RAM-disk documentation likewise states that `/dev/ram*` uses main system memory as a block device and that its contents are erased on reboot.

Source checked:

```text
https://cdn.kernel.org/doc/html/latest/admin-guide/blockdev/ramdisk.html
```

These device names satisfy the R4R12 `/dev/<kernel-devname>` syntax.

### 5.4 ext4 external journals

Current ext4 documentation states that an ext4 filesystem may use an external journal device rather than an internal journal inode.

Sources checked:

```text
https://cdn.kernel.org/doc/html/latest/filesystems/ext4/journal.html
https://cdn.kernel.org/doc/html/latest/admin-guide/ext4.html
https://man7.org/linux/man-pages/man5/ext4.5.html
```

The current ext4 mount interface includes:

```text
journal_path=path
journal_dev=devnum
```

for locating an external journal device when its identity changes.

Current ext4 source selects an external journal when the filesystem has no internal journal inode and opens it through `ext4_open_dev_journal()`.

Current source calls conceptually:

```text
jbd2_journal_init_dev(external_journal_bdev,
                      filesystem_bdev,
                      ...)
```

and current JBD2 defines distinct fields:

```text
j_dev    = device where the journal is stored
j_fs_dev = filesystem device
```

Sources checked:

```text
https://github.com/torvalds/linux/blob/master/fs/ext4/super.c
https://github.com/torvalds/linux/blob/master/include/linux/jbd2.h
```

Therefore “journal present” is not equivalent to “journal stored on the already-bound repository device.”

### 5.5 ext4 full option view

Current ext4 source confirms that `/proc/fs/ext4/<dev>/options` is produced through `ext4_seq_options_show()` and `_ext4_show_options(..., nodefs=1)`, so current mount state is more complete than the ordinary nondefault-only mount-option rendering.

Source checked:

```text
https://github.com/torvalds/linux/blob/master/fs/ext4/super.c
```

This supports the R4R12 correction for the exact PR #137 `nobarrier` / filesystem-default omission class. It does not expose the persistence guarantees of the underlying block-device class and does not, by itself, establish internal-versus-external journal location.

## 6. PR #137 finding F001 — procfs authority-source provenance

Disposition: `ADDRESSED AT BRIEF LEVEL` for the exact R4R11 mechanism.

R4R12 now requires:

```text
held /proc descriptor
PROC_SUPER_MAGIC
unique proc mount ID
statmount fs_type=proc
direct getpid/gettid
thread-self target exactly matching direct PID/TID
numeric current-process/current-thread paths
RESOLVE_BENEATH
RESOLVE_NO_XDEV
RESOLVE_NO_SYMLINKS
same proc mount ID for every authority source
authenticated current-thread ns/user
authenticated current-process uid_map/gid_map
authenticated current-thread ns/mnt
request-bound proc authority record
revalidation through the effect interval
```

The independent review found no remaining version of the PR #137 single-file bind-mount substitution attack that survives the exact no-cross-mount numeric-path rules as written.

This is not a blanket assertion about arbitrary procfs designs. It is the disposition of the exact prior finding.

## 7. PR #137 finding F002 — ext4 durability-affecting mount options

Disposition: `ADDRESSED AT BRIEF LEVEL` for the exact R4R11 mechanism.

R4R12 now requires:

```text
STATMOUNT_MNT_OPTS
STATMOUNT_OPT_ARRAY
authenticated full /proc/fs/ext4/<dev>/options
rw
barrier
not nobarrier
data=ordered XOR data=journal
not data=writeback
not journal_async_commit
not noload
not emergency_ro
not shutdown
journal_task present
errors_count = 0
```

It also request-binds raw option views and revalidates their digests before commitment.

Those are material corrections to PR #137 F002.

The new findings below are deeper than mount-option state: they concern the storage domains to which the journal/filesystem synchronization contract is applied.

## 8. Finding X1B-R4R12-IBR-F001 — backing block-device persistence topology is not bound

Severity: `BLOCKER`.

### 8.1 Current V12 source narrowing

R4R12 requires the repository superblock source to have exact form:

```text
/dev/<kernel-devname>
```

with a restricted basename character set, and records:

```text
sb_dev_major
sb_dev_minor
sb_source
```

It then proves ext4 state for that mounted filesystem.

But V12 does not require any reviewed block-device class or persistence topology below that major/minor identity.

No rule rejects or separately models at least:

```text
/dev/zram*
/dev/ram*
/dev/loop*
software device-mapper targets
network-backed block devices
other kernel virtual block devices
```

The finding does not require every listed class to be unsafe. The defect is that persistence is not classified at all despite being part of the claimed crash-durability contract.

### 8.2 Concrete RAM-backed counterexample class

The kernel explicitly documents zram as RAM-based block devices and explicitly documents creating ext4 on `/dev/zram1`.

`/dev/zram1` satisfies the exact V12 source-name grammar:

```text
prefix = /dev/
basename = zram1
allowed characters only
```

A normally journaled ext4 filesystem on that device has an ext4 superblock, ext4 mount options, an ext4 journal task, ext4 sysfs state, inode semantics and all of the other filesystem-level structures V12 inspects.

Yet the kernel documentation states that zram stores the device's pages in system memory itself.

Similarly, the kernel RAM-disk documentation states that `/dev/ram*` is main-memory-backed and its contents are erased on reboot.

Thus:

```text
EXT4 + barrier + successful fsync
```

is not a proof of:

```text
persistent backing medium across crash/reboot
```

when the block-device class itself is intentionally volatile.

### 8.3 Why the hardware-failure exclusion does not close this

R4R12 excludes:

```text
hardware/firmware that falsely acknowledges durable flush/FUA
physical media failure after acknowledged durable completion
```

A RAM-backed Linux block device does not fit that exclusion.

It is an intentional kernel storage class whose persistence semantics are part of the software/device topology, not dishonest firmware and not a physical-medium failure.

There may be no persistent medium at all.

### 8.4 Why `fsync()` success does not close this

The V12 contract treats success of its required file and directory `fsync()` calls as part of the crash-durability proof.

Current `fsync(2)` describes persistence in terms of a disk or other permanent storage device.

V12 has not established that the block device beneath ext4 is such a device.

The missing property is therefore before the `fsync()` return-value reasoning:

```text
repository block identity
-> reviewed nonvolatile persistence class/topology
-> filesystem/barrier/fsync semantics
```

V12 starts at the final arrow without proving the middle property.

### 8.5 Security consequence

The implementation can satisfy the V12-visible ext4 contract on a storage domain that is designed to disappear at reboot.

It can therefore label an effect:

```text
DURABLY_REF_COMMITTED_COMPLETE
```

while the entire repository backing device lacks the persistence property the durability class implies.

This is not merely an availability difference. It changes the truth of the Human-presented material effect and the post-effect commitment claim.

### 8.6 Required disposition

```text
X1B-R4R12-IBR-F001 = BLOCKER
```

A successor must either:

```text
reject all block-device classes outside one explicitly reviewed persistent-storage profile
```

or establish and Human-bind a complete backing-device/topology persistence proof.

A pathname grammar alone is not that proof.

This review does not authorize a repair.

## 9. Finding X1B-R4R12-IBR-F002 — external ext4 journal device is an unbound write/durability domain

Severity: `BLOCKER`.

### 9.1 Current V12 journal proof

R4R12 proves journal presence by requiring:

```text
journal_task != <none>
```

and applies barrier/data-mode checks to the mounted ext4 filesystem.

It does not require:

```text
journal is internal
s_journal_inum != 0
s_journal_dev = 0
j_dev == j_fs_dev
```

and it does not bind an external journal device if present.

The exact R4R12 text contains no `journal_dev` rule and no external-journal profile.

### 9.2 Current ext4 permits the omitted state

Current ext4 supports external journals.

On an external-journal filesystem, the journal is a distinct block device. Current ext4 source opens that device and initializes JBD2 with both:

```text
journal device
filesystem device
```

Current JBD2 explicitly keeps those as separate `j_dev` and `j_fs_dev` fields.

Therefore the V12 filesystem `sb_source` / `sb_dev_major` / `sb_dev_minor` record is not necessarily the identity of all persistent write domains used by the filesystem transaction protocol.

### 9.3 Why mount-option capture is insufficient

The ext4 `journal_dev=` / `journal_path=` mount options are relocation/override inputs for an external journal location.

An ext4 filesystem can already carry its external-journal identity in filesystem metadata and use the external device without requiring a fresh user-supplied override on every mount.

R4R12 does not parse the ext4 on-disk journal-location fields or otherwise establish internal-journal status.

Its full `/proc/fs/ext4/<dev>/options` view therefore does not close the journal-device topology by itself.

### 9.4 Why `journal_task` is insufficient

`journal_task` proves that an ext4/JBD2 journal thread is attached.

It does not identify the block device on which journal records are stored.

Both an internal journal and an external journal have a journal task.

### 9.5 Durability consequence

For an external journal, transaction durability depends on writes and ordering involving a second block device.

V12 currently binds only:

```text
repository filesystem source
repository filesystem device major/minor
repository mount options
repository ext4 proc/sysfs state
```

It does not bind for the external journal:

```text
block-device identity
persistence class/backing topology
read-only state
flush/FUA domain
hotplug/replacement identity
storage-stack semantics
```

The effect can therefore write authority-critical journal state outside the Human-bound physical storage domain.

This violates both:

```text
exact presented material effect binding
no core authority/security choice left implicit
```

### 9.6 Strong combined counterexample

The two new findings can combine.

For example, a persistent ext4 filesystem can be configured with an external journal on a volatile or otherwise unsupported second block device.

V12 can bind the primary filesystem device while remaining unaware that the journal commit record is stored elsewhere.

Even a future repair that rejects RAM-backed primary repository devices would therefore not close F002 unless it also rejects or binds external journal topology.

### 9.7 Required disposition

```text
X1B-R4R12-IBR-F002 = BLOCKER
```

A successor must either:

```text
prove internal journal only
```

or independently bind and apply the complete persistence/durability contract to every external journal device and its relationship to the filesystem device.

This review does not authorize a repair.

## 10. Cross-check of V12 proc authority correction

No blocker was found in the exact normal V12 ordering for PR #137 F001.

The important closure is:

```text
verified /proc root
-> exact proc mount identity
-> direct getpid/gettid
-> genuine thread-self target match
-> numeric paths
-> RESOLVE_NO_XDEV / RESOLVE_NO_SYMLINKS / RESOLVE_BENEATH
-> same proc mount ID for each authority object
```

That is materially different from R4R11's unverified `/proc/self/...` path trust.

The new storage findings do not reopen this correction.

## 11. Cross-check of V12 ext4 option correction

No blocker was found in the specific correction that full ext4 runtime options must be authenticated and that `nobarrier`, writeback mode and async journal commit are unsupported.

Current ext4 source supports the premise that the `nodefs=1` proc option view is fuller than normal nondefault-only mount display.

The new findings instead show that:

```text
correct ext4 option state
```

is not sufficient to establish:

```text
complete persistent storage topology
```

for either the primary filesystem block device or a possible external journal device.

## 12. Prior corrections preserved at brief level

The independent pass found no reason in these two new findings to reopen the previously corrected mechanisms for:

```text
initial user namespace value semantics
mount ID-mapping rejection
casefold / Linux inode semantic flags
Human-bound loose-object mtime
request-bound object staging namespace
nonfinal canonical fanout avoidance
post-fchmod/futimens file-fsync ordering
hardlink-free loose-object install
split-index/sharedindex rejection
raw extension-free index-v2 replacement
physical loose main ref topology
packed-main rejection
deterministic reflog projection
worktree/log alias-safe projection
replacement refs / commit encoding
hook closure
lazy-fetch/promisor/alternates
Human currentness/conflict/replay binding
```

This is not a blanket PASS for every historical line. The review verdict remains NOT PASS because either new blocker is independently sufficient.

## 13. Mandatory regressions implied by this review

A successor review must attack at least the following additional cases.

### 13.1 Backing storage persistence/topology

```text
primary ext4 on reviewed persistent device profile -> expected supported case
primary ext4 on /dev/zram* -> BLOCK
primary ext4 on /dev/ram* -> BLOCK
primary ext4 on loop device -> BLOCK unless complete backing persistence proof is frozen
primary ext4 on device-mapper/MD/network block topology -> BLOCK unless explicitly reviewed and bound
block-device class/topology source unavailable -> BLOCK
block-device identity/backing topology drift -> durability uncertainty / BLOCK
path /dev/<name> shape alone -> never sufficient persistence proof
```

The exact successor may choose a narrower positive-control device class rather than supporting every Linux block stack.

### 13.2 External journal topology

```text
internal ext4 journal proven exact -> expected supported case
external journal detected -> BLOCK unless separately supported
s_journal_inum = 0 with external journal device -> BLOCK under internal-only profile
journal device identity differs from filesystem device -> BLOCK under internal-only profile
journal location cannot be proven -> BLOCK
external journal on volatile/RAM-backed device -> BLOCK
external journal device identity/backing drift -> durability uncertainty / BLOCK
journal_task present but journal device unknown -> BLOCK
```

If a successor supports external journals, all journal-device persistence and durability fields must be Human-bound rather than inferred from the primary filesystem mount.

### 13.3 Preserve PR #137 attack regressions

Also rerun:

```text
/proc not procfs
/proc numeric current-PID directory overmounted
ns/user bind-mounted namespace file
uid_map/gid_map bind-mounted substitute
proc authority mount crossing
thread-self mismatch to direct PID/TID
statmount option field unavailable
nobarrier
barrier=0 representation
writeback data mode
journal_async_commit
noload
ext4 emergency/shutdown
ext4 error state
option-state drift
```

## 14. Review observation — option classification must remain closed

R4R12 requires every ext4 runtime token to pass a “reviewed V12 option table” and says unknown durability-affecting tokens block.

The exact table is not enumerated in this brief.

This review does not need to promote that omission to a third independent blocker because F001 and F002 already require a successor. A successor should nevertheless avoid leaving the positive-control allowlist and durability relevance classification to implementation discretion; any such table should be frozen as explicit reviewable authority rather than inferred ad hoc from code.

## 15. Required review verdict matrix

```text
PR #137 F001 procfs authority provenance           = ADDRESSED AT BRIEF LEVEL
PR #137 F002 ext4 durability mount options         = ADDRESSED AT BRIEF LEVEL

R4R12 IBR F001 backing block persistence topology  = BLOCKER
R4R12 IBR F002 external journal write domain       = BLOCKER

AK-CANON X1B R4R12 IMPLEMENTATION-BRIEF REVIEW    = NOT PASS
IMPLEMENTATION AUTHORITY                            = NOT ESTABLISHED
X1B                                                 = OPEN
V1 AUTHORITY                                        = NOT ESTABLISHED
```

## 16. STOP boundary

This artifact is review evidence only.

It does not authorize:

```text
R4R13 or other successor correction
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
   X1B-R4R12-IBR-F001
   X1B-R4R12-IBR-F002
```

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
NOT PASS != AUTHORITY TO FIX
AI PROPOSES != HUMAN DECIDES
```
