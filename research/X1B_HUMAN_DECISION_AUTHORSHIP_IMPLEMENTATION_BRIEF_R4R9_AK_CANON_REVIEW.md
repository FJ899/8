# X1B Human Decision Authorship — Independent AK-CANON R4R9 Implementation-Brief Review

Status: `INDEPENDENT REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: `2026-09-02`

## 1. Verdict

`AK-CANON X1B R4R9 IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

R4R9 materially improves R4R8 and addresses both findings frozen in PR #131 at brief level:

1. final security-relevant file metadata is now applied before the file `fsync()` that establishes the normal-success durability barrier, and the loose-object install no longer changes link-count after that barrier;
2. split-index/shared-index state is removed from the supported profile, the canonical index is constrained to an extension-free full v2 file, no Git command may read the canonical index pre-ref, no Git command may write it, and the post-ref index is rebuilt and replaced by a bounded raw writer.

The V9 schema migration correctly prevents V8 or earlier Human evidence from authorizing the changed V9 effect.

However, independent adversarial review found two new blockers:

1. R4R9 calls its filesystem profile `POSIX_MODE_ONLY_SECURITY_METADATA_V1`, but it does not inspect or bind Linux inode semantic flags. Linux filesystems expose flags outside mode bits, ACLs and xattrs that change file/directory semantics. Most importantly for V9, per-directory casefold can make a directory case-insensitive while its mode/uid/gid/xattr/ACL checks all pass. That defeats byte-exact namespace/no-alias claims including the negative `sharedindex.*` proof and exact object/ref/index path identity;
2. R4R9 normal-success object installation is correctly ordered, but its pre-ref crash/failure residue is not closed. A missing canonical fanout is created directly as `.git/objects/<xx>` with mode `0700` and only afterwards changed to `0755`; a crash between those operations may leave a persistent canonical fanout with non-profile metadata. Likewise a private object temp leaf may remain before `RENAME_NOREPLACE`. The V9 outcome model only describes exact prepared objects/fanout directories and does not classify or bind malformed/nonfinal object-store residue.

Either finding independently prevents implementation authority.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R9 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R9 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#132`

```text
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
BASE TREE = df807db7003dfd201e9be4d5927472e515a2e737
HEAD = 5a05f995b296cd550e853211739be926626ee607
TREE = 68888b64ca9fa122d133279b92aa8779f4c31e67
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R9.md
BLOB = ee61ca5d540120861f4cc9f5731242cb86554c01
```

Immediately before review write, PR #132 remained:

```text
state = OPEN
merged = false
draft = true
mergeable = true
commits = 1
changed_files = 1
additions = 1996
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

### 3.3 R4R8 predecessor and binding review

```text
FJ899/8 PR #130
HEAD = 6427f07347fedfcf8c2b719e16b67c37b2a7e296
TREE = ac93196b3d04e2b607c6aeeadd3485dc6c32dd6f
BLOB = 87c9bb4f57a33ea0d7c3b41c8305b04e8f9283f2
```

```text
FJ899/8 PR #131
HEAD = c3952084f45892d744668db339abd424b45d4971
TREE = fe0b3acd86ddb2ffb089bef6493a3c3031f88d91
BLOB = 1d45b32c1286733892c450371465690153959251
VERDICT = AK-CANON X1B R4R8 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #131 froze:

```text
X1B-R4R8-IBR-F001 final mode metadata is changed after the file fsync
X1B-R4R8-IBR-F002 split-index / sharedindex durable effect is unbound
```

## 4. Review method and current external semantics checked

The review attacked the exact R4R9 successor rather than inferring PASS from the stronger V9 profiles.

The review inspected at least:

```text
FSYNC_AFTER_FINAL_METADATA_V1 ordering
RENAME_NOREPLACE loose-object installation
fanout creation before object installation
object temp-file crash windows
Linux inode semantic attributes outside mode/xattr/ACL
case-sensitive vs casefolded directory lookup semantics
negative sharedindex namespace proof
FULL_SINGLE_FILE_INDEX_V1 format restrictions
CLOSED_FULL_INDEX_V2_REWRITE_V1 deterministic encoding
canonical index no-Git-reader/no-Git-writer rule
raw index replacement ordering
outcome/recovery coverage for pre-ref residue
```

Current external semantics checked included:

### 4.1 Linux rename semantics

Current Linux `renameat2(2)` documentation states that:

```text
RENAME_NOREPLACE = do not overwrite newpath; error if newpath exists
relative oldpath/newpath are resolved against the supplied directory fds
support for RENAME_NOREPLACE is filesystem-dependent
```

Source checked:

```text
https://man7.org/linux/man-pages/man2/rename.2.html
```

R4R9 correctly fail-closes when this primitive is unsupported.

### 4.2 Linux inode flags

Current Linux man-pages document `FS_IOC_GETFLAGS` / `FS_IOC_SETFLAGS` as an interface to inode flags that modify file and directory semantics independently of ordinary POSIX mode bits.

Examples include:

```text
FS_APPEND_FL
FS_IMMUTABLE_FL
FS_DIRSYNC_FL
FS_SYNC_FL
FS_NOCOW_FL
FS_PROJINHERIT_FL
```

Source checked:

```text
https://man7.org/linux/man-pages/man2/fs_ioc_getflags.2const.html
```

Current Linux UAPI also defines:

```text
FS_CASEFOLD_FL = 0x40000000
FS_XFLAG_CASEFOLD = case-insensitive lookups
```

and describes the default with no case-handling flag as POSIX case-sensitive lookup semantics.

Source checked:

```text
https://github.com/torvalds/linux/blob/master/include/uapi/linux/fs.h
```

### 4.3 ext4 casefold semantics

Current kernel ext4 documentation states that case-insensitive lookup is supported on a per-directory basis and can be enabled with the casefold inode attribute. The on-disk filename remains name-preserving, while lookup comparisons use normalization/casefolding.

Source checked:

```text
https://www.kernel.org/doc/html/latest/admin-guide/ext4.html
```

This is a direct counterexample to assuming that mode/uid/gid/xattr/ACL equivalence proves byte-exact directory-name lookup semantics.

### 4.4 Git index v2 semantics

Current Git index-format documentation was checked for:

```text
DIRC header
version 2 layout
network-byte-order numeric fields
32-bit stat fields
32-bit mode
16-bit flags
assume-valid / extended / stage / pathname-length fields
raw unsigned-byte pathname sort
NUL pathname termination
8-byte v2 entry padding
trailing object-format checksum
```

Source checked:

```text
https://git-scm.com/docs/index-format
```

No new blocker is frozen against R4R9's decision to support only extension-free full index v2. The profile is deliberately narrow and can be implemented against this format.

## 5. PR #131 finding F001 — post-fchmod durability

Disposition: `ADDRESSED AT BRIEF LEVEL` for the normal-success path.

R4R9 now freezes:

```text
write final bytes
apply final security metadata
verify metadata
fsync(file) AFTER the final metadata mutation
perform only the reviewed namespace operation
fsync(parent directory)
reopen and verify
```

The new loose-object installer also replaces R4R8's `linkat + unlink` production path with:

```text
renameat2(..., RENAME_NOREPLACE)
```

so successful final object `st_nlink = 1` is no longer changed after the file-fsync barrier.

The main ref, reflog, worktree and raw-index replacement paths also place final `fchmod(0644)` before their normal-success file fsync.

The blocker below is different: V9 still does not fully model nonfinal canonical object-store state left by a crash before the normal-success barrier completes.

## 6. PR #131 finding F002 — split index / sharedindex

Disposition: `ADDRESSED AT BRIEF LEVEL` under byte-exact POSIX namespace semantics.

R4R9 now requires:

```text
.git/index = full extension-free v2
all stages = 0
no extended flags
no index extensions
raw semantic tuple set = raw parent tree
no sharedindex.* namespace entries
core.splitIndex absent/false
splitIndex.* config absent
no Git command reads canonical index pre-ref
no Git command writes canonical index
post-ref final index built in-process
post-ref final index written through bounded index.lock replacement
```

This closes the exact PR #131 split-index/shared-index creation/deletion/mtime mechanism for an ordinary case-sensitive namespace.

The new inode-flag blocker below shows that V9 has not yet established that the namespace actually has those byte-exact semantics.

## 7. Finding X1B-R4R9-IBR-F001 — Linux inode semantic flags / casefold namespace are not bound

Severity: `BLOCKER`.

### 7.1 R4R9's current metadata proof

R4R9 `POSIX_MODE_ONLY_SECURITY_METADATA_V1` verifies authority-critical paths with fields such as:

```text
mode
uid
gid
setuid/setgid/sticky absence
listxattr empty
ACL mode-only
no security labels/capabilities/xattrs
```

Its required Linux primitives include `fstat/lstat`, `listxattr` and ACL inspection.

It does not require:

```text
FS_IOC_GETFLAGS
FS_IOC_FSGETXATTR
statx attribute-mask checks
casefold flag checks
immutable/append/sync/nocow/dax/verity/project-inherit checks
```

No R4R9 section establishes that authority-critical directories have byte-exact case-sensitive lookup semantics.

### 7.2 Concrete casefold counterexample

A Linux ext4 directory may satisfy:

```text
mode = 0755
uid/gid exact
listxattr = empty
ACL = mode bits only
no symlink
same mount ID
```

while also having per-directory casefold enabled.

In that state, the directory preserves the spelling of stored names but lookup is case-insensitive / normalization-aware.

Therefore an entry such as:

```text
SHAREDINDEX.<40-hex>
```

or another casefold-equivalent spelling can be a lookup alias for the lowercase pathname Git constructs:

```text
sharedindex.<40-hex>
```

while a byte-sensitive directory enumeration/pattern check can report that no literal lowercase `sharedindex.*` entry exists.

The same issue applies more generally to exact authority pathnames under:

```text
.git
.git/objects
.git/refs
.git/logs
worktree target parent directories
```

including lowercase object fanout/OID names and exact metadata leaf names.

### 7.3 Why `core.ignoreCase` is not the fix

Git's `core.ignoreCase` is an application workaround for case-insensitive filesystems. It does not change the kernel namespace semantics and cannot turn a casefolded directory back into a byte-exact POSIX lookup domain.

R4R9's security proof is below Git: it relies on exact directory entries, `openat`-style lookup and negative namespace proofs.

Therefore application config cannot substitute for a filesystem lookup-semantics gate.

### 7.4 Other inode semantic flags

The same missing proof class includes Linux inode flags that can change behavior without appearing in mode/xattrs/ACLs.

Examples include:

```text
append-only
immutable
sync / dirsync
nocow
dax
project inheritance
verity where supported
```

Some would simply force an operation to fail, but others change inheritance, I/O or lookup semantics while the R4R9 mode-only checks still pass.

A profile named `POSIX_MODE_ONLY_SECURITY_METADATA_V1` cannot assume these semantics away; it must prove the repository is in the intended subset.

### 7.5 Violated properties

The gap violates:

```text
physical namespace no-alias proof
sharedindex_effect = NONE proof
exact path identity
executor no-substitution
no hidden filesystem policy input
no core authority/security choice left implicit
```

### 7.6 Required successor correction class

A successor must add a closed Linux filesystem/inode-semantics profile.

At minimum it must:

```text
inspect supported inode/file-system flags through authoritative Linux interfaces
require case-sensitive, case-preserving lookup on every authority-critical directory
reject FS_CASEFOLD_FL / FS_XFLAG_CASEFOLD or equivalent lookup aliases
reject immutable/append/verity/encryption or other flags incompatible with the profile
freeze an explicit whitelist for benign storage-internal flags that may legitimately exist
reject unknown semantic flags
bind the result at request, admission, final gate and post-effect checkpoints
```

The exact allowed flag set may vary by supported filesystem, but it cannot remain implicit.

Mandatory regression classes must include at least:

```text
casefolded .git directory
casefolded .git/objects
casefolded .git/refs/heads
casefolded .git/logs/refs/heads
casefolded worktree target parent
casefold-equivalent sharedindex alias
casefold-equivalent loose-object leaf alias
append-only authority directory
immutable authority file
unknown semantic inode flag
```

## 8. Finding X1B-R4R9-IBR-F002 — pre-ref object-store crash residue is not closed

Severity: `BLOCKER`.

### 8.1 Missing-fanout creation sequence

R4R9 section 20 allows a missing canonical object fanout to be created directly as:

```text
mkdir .git/objects/<xx> with initial mode 0700
open directory fd
fchmod 0755
verify metadata
fsync(new fanout dir) AFTER fchmod
fsync(.git/objects)
```

Normal success is well ordered.

But the canonical pathname exists before its final metadata and durability barriers are complete.

### 8.2 Crash window

A crash can occur after:

```text
mkdir canonical fanout
```

and before:

```text
fchmod 0755
```

or before the directory and parent-directory fsyncs.

The absence of a parent-directory fsync does not prove that the new directory entry will be absent after reboot. Filesystem journaling may persist it anyway; without a completed barrier the correct statement is uncertainty, not nonexistence.

A surviving fanout can therefore be:

```text
canonical pathname = .git/objects/<xx>
mode = 0700
profile-required mode = 0755
```

This is not an exact prepared fanout under V9. It is malformed authority-critical object-store state created by the failed attempt.

### 8.3 Private object-temp residue

The new-object path also creates an unpredictable private temp leaf in the canonical fanout before `RENAME_NOREPLACE`.

Crash points include:

```text
after temp creation
while writing
post-write pre-fchmod
post-fchmod pre-file-fsync
post-file-fsync pre-RENAME_NOREPLACE
```

A temp directory entry may survive a crash in any of these windows depending on filesystem persistence.

It is not the exact final OID leaf and therefore is not one of the exact closure objects described by `BLOCKED_PRE_COMMIT_OBJECT_PREPARED`.

### 8.4 Outcome-model mismatch

R4R9 defines:

```text
BLOCKED_PRE_COMMIT_NO_OBJECT_PREP
BLOCKED_PRE_COMMIT_OBJECT_PREPARED
BLOCKED_PRE_COMMIT_REF_LOCK_RESIDUE
```

and explicitly gives main-lock crash residue its own classifier.

But its object-preparation outcomes say, in substance:

```text
NO_OBJECT_PREP -> no new closure object durably installed
OBJECT_PREPARED -> exact unreferenced contained objects/fanout dirs may remain
```

They do not bind or classify:

```text
canonical 0700 fanout residue
partially initialized canonical fanout
private non-OID temp object leaf
uncertain temp-name persistence
```

`OBJECT_STORE_TOPOLOGY_UNCERTAIN` is defined for uncertainty in the target relationship, not for known canonical residue with nonfinal metadata/content.

### 8.5 Why fail-closed on the next run is insufficient

A subsequent V9 run will observe a `0700` canonical fanout and block because the profile requires `0755`.

That is safe against falsely continuing, but it does not make the original failure truthfully modeled.

The failed attempt itself created durable or possibly durable Git object-store state that:

```text
was not part of the successful Human-bound effect
is not an exact prepared-object state
cannot be silently normalized
may require separate recovery authority
```

The higher-level design requires failed operations not to be durably misreported and forbids implicit recovery/security choices.

### 8.6 Required successor correction class

A successor must close canonical ODB creation/residue behavior.

Acceptable design classes include, for example:

```text
A. require every needed two-hex fanout directory to pre-exist in exact final profile before any effect preparation
```

or:

```text
B. create a private noncanonical fanout staging directory,
   apply final metadata,
   fsync it,
   atomically RENAME_NOREPLACE it into the canonical two-hex name,
   fsync .git/objects,
   and explicitly classify any private staging residue
```

In either design, object temp files also need a closed naming/residue classifier.

The outcome model must distinguish at least:

```text
exact final unreferenced closure objects
exact final fanout dirs
nonfinal private temp residue
malformed canonical fanout residue
object-store durability uncertainty
```

No cleanup or normalization of ambiguous residue may be performed without separately authorized recovery semantics.

Mandatory fault regressions must include crashes:

```text
after fanout mkdir before fchmod
after fanout fchmod before fanout fsync
after fanout fsync before objects-dir fsync
after object temp create before write
after object write before fchmod
after object fchmod before file fsync
after object file fsync before RENAME_NOREPLACE
on EEXIST cleanup before/after temp unlink and fanout-dir fsync
```

and must verify restart classification from the actual persisted namespace.

## 9. Review of FULL_SINGLE_FILE_INDEX_V1 / raw v2 writer

No additional blocker is frozen in this review against the deliberate V9 raw-index design.

The review confirms the brief makes the following choices explicit enough for a bounded implementation review:

```text
version exactly 2
no extensions
stage exactly 0
extended flag zero
raw unsigned-byte path ordering
network-byte-order fields
exact object-format checksum
prestate raw-byte digest
semantic path/mode/OID equality to raw parent tree
preserve existing stat cache and assume-valid policy
zero stat fields for newly added paths
post-ref index.lock replacement
no sharedindex effect
```

A future implementation review must still test the exact 16-bit v2 flags/name-length encoding, including the `0xFFF` long-name rule, padding and checksum against Git 2.55, but that is an implementation conformance obligation rather than a new brief-level ambiguity here because R4R9 explicitly binds the standard Git index-v2 format.

## 10. Review of RENAME_NOREPLACE choice

No new blocker is frozen against the switch from hard-link installation to `renameat2(RENAME_NOREPLACE)`.

For a supported filesystem, the primitive gives the intended no-overwrite namespace operation and avoids the R4R8 successful-path link-count mutation.

R4R9 also correctly requires unsupported `RENAME_NOREPLACE` semantics to block.

A future implementation review must still exercise:

```text
successful absent-destination rename
EEXIST winner path
unsupported-filesystem error
source/final same held fanout fd
post-rename fanout directory fsync
final nlink = 1
```

## 11. Prior findings disposition

```text
R4R7 IBR F001 PRIMARY OBJECT-STORE PHYSICAL ALIAS = ADDRESSED IN R4R8/R4R9
R4R7 IBR F002 REF/REFLOG METADATA VALUE SELECTION = ADDRESSED IN R4R8/R4R9

R4R8 IBR F001 POST-FCHMOD FILE-FSYNC ORDERING = ADDRESSED IN R4R9 NORMAL-SUCCESS PATH
R4R8 IBR F002 SPLIT-INDEX / SHAREDINDEX WRITER FOOTPRINT = ADDRESSED IN R4R9 UNDER BYTE-EXACT NAMESPACE SEMANTICS

R4R9 IBR F001 LINUX INODE SEMANTIC FLAGS / CASEFOLD = BLOCKER
R4R9 IBR F002 PRE-REF OBJECT-STORE CRASH RESIDUE = BLOCKER
```

## 12. Final AK-CANON disposition

The independent review therefore freezes:

```text
X1B-R4R9-IBR-F001 — LINUX INODE SEMANTIC FLAGS / CASEFOLD NAMESPACE = BLOCKER
X1B-R4R9-IBR-F002 — PRE-REF OBJECT-STORE CRASH RESIDUE = BLOCKER
```

Final verdict:

```text
AK-CANON X1B R4R9 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
IMPLEMENTATION AUTHORITY = NOT ESTABLISHED
X1B = OPEN
V1 AUTHORITY = NOT ESTABLISHED
```

## 13. Required successor scope

A successor corrective implementation brief, if separately Human-authorized, must close exactly the new blockers while preserving all prior corrections.

At minimum it must add:

```text
closed Linux inode/filesystem semantic-flag profile
case-sensitive byte-exact lookup proof for every authority directory
explicit allowed/rejected inode flag policy
casefold regression coverage
pre-ref object-store residue model
safe fanout creation or preexisting-fanout requirement
private object-temp residue classification
restart/recovery truth for malformed/nonfinal ODB residue
```

Any material change to the Human-presented effect/profile requires a schema version bump and fresh Human-bound evidence.

This review grants no repair authority.

## 14. STOP boundary

This review authorizes none of the following:

```text
successor repair
ScriptOps implementation
Human decision proposal/review
positive Human control
canonical screenplay effect
recovery
merge
X1B closure
Agency Kernel v1
release
deployment
tag
```

```text
REVIEW FINDING != REPAIR AUTHORITY
NOT PASS != AUTHORITY TO PATCH
AI PROPOSES != HUMAN DECIDES
```

After durable freeze of this independent review, STOP.

The next legal stage is a separately Human-authorized successor corrective implementation brief addressing the two frozen R4R9 blockers.