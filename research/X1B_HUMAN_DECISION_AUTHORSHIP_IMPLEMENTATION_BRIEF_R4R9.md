# X1B HUMAN DECISION AUTHORSHIP — CLEAN IMPLEMENTATION BRIEF R4R9

Status: `CLEAN R4R9 CORRECTIVE BRIEF / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-02`

## 1. Authority, purpose, and STOP boundary

This document is the self-contained successor to R4R8 after independent AK-CANON review PR #131 returned `NOT PASS`.

It preserves the accepted X1B corrective design and every R4R8 property not rejected by PR #131, while correcting exactly the two blockers frozen by that review:

1. R4R8 selected exact final filesystem modes but ordered its durability barriers incorrectly: object temp files, `main.lock` and reflog temp files were fsynced before final `fchmod`, so the final `0444` / `0644` mode changes were visible but not included in the completed file-fsync barrier; the loose-object path also changed link-count metadata through `linkat + unlink` after the file fsync;
2. R4R8 still delegated real `.git/index` projection to Git and did not close split-index state, allowing `.git/sharedindex.<SHA-1>` creation/deletion/mtime mutation outside the Human-bound effect.

R4R9 therefore changes both durability ordering and real-index projection.

New exact profiles:

```text
FSYNC_AFTER_FINAL_METADATA_V1
ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V2
FULL_SINGLE_FILE_INDEX_V1
CLOSED_FULL_INDEX_V2_REWRITE_V1
ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1
ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V3
DETERMINISTIC_MAIN_REFLOG_PROJECTION_V2
ALIAS_SAFE_WORKTREE_PROJECTION_V2
CRASH_DURABLE_OBJECT_REF_INDEX_V4
ALIAS_SAFE_MAIN_REF_COMMITMENT_V5
REF_CAS_FIRST_ALIAS_SAFE_RAW_GIT_METADATA_V7
```

The material effect changes again. All authority-critical schemas, request/review markers, admission identities, final-gate identities and records are therefore V9.

This document is an implementation brief only. It authorizes no ScriptOps source mutation, no Human decision PR/review, no live positive control, no canonical screenplay effect, no recovery, no merge, no X1B closure, no Agency Kernel v1, no release, deployment, or tag.

```text
R4R9 BRIEF != IMPLEMENTATION AUTHORITY
R4R9 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R9 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

After durable freeze of this brief, STOP. The next stage is a separately Human-authorized independent AK-CANON R4R9 implementation-brief review.

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

### 2.3 R4R8 predecessor

```text
FJ899/8 PR #130
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 6427f07347fedfcf8c2b719e16b67c37b2a7e296
TREE = ac93196b3d04e2b607c6aeeadd3485dc6c32dd6f
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R8.md
BLOB = 87c9bb4f57a33ea0d7c3b41c8305b04e8f9283f2
```

### 2.4 Binding R4R8 NOT-PASS review

```text
FJ899/8 PR #131
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = c3952084f45892d744668db339abd424b45d4971
TREE = fe0b3acd86ddb2ffb089bef6493a3c3031f88d91
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R8_AK_CANON_REVIEW.md
BLOB = 1d45b32c1286733892c450371465690153959251
VERDICT = AK-CANON X1B R4R8 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #131 froze:

```text
X1B-R4R8-IBR-F001 — final mode metadata is changed after the file fsync
X1B-R4R8-IBR-F002 — split-index / sharedindex durable effect is unbound
```

PR #131 also recorded that R4R8 addressed at brief level:

```text
X1B-R4R7-IBR-F001 primary object database physical topology
X1B-R4R7-IBR-F002 implicit ref/reflog replacement metadata selection
```

and preserved prior physical-ref, update-ref reflog, hook, fsync, lazy-fetch, replacement-ref, commit-encoding, hardlink/write-target-alias and freshness/supersession corrections.

`REVIEW FINDING != REPAIR AUTHORITY`; R4R9 exists only under fresh Human authorization for successor brief preparation.

## 3. Exact evidence-repository base

```text
FJ899/8 main
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

No history rewrite is part of R4R9.

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

## 5. Normative precedence and V9 migration

```text
R4R9 TEXT = CURRENT IMPLEMENTATION-BRIEF AUTHORITY
R4R8 / R4R7 / R4R6 / R4R5 / R4R4 / R4R3 / R4R2 / R4R1 / R4 / R3 / R2 / R1 = HISTORICAL INPUT ONLY
CORRECTIVE DESIGN PR #34 = HIGHER-LEVEL PROPERTY CONTRACT
```

R4R9 materially changes local metadata preparation and index projection:

```text
all final security metadata is applied before the file fsync that establishes the claimed durability barrier
loose-object install no longer uses linkat + unlink as the production no-replace primitive
Linux renameat2(RENAME_NOREPLACE) is the exact new-object install primitive
real .git/index is no longer written by Git
split-index and sharedindex state are unsupported and fail closed
final index bytes are derived in-process from a constrained full index-v2 prestate and the exact derived new tree
canonical index replacement is descriptor-relative and fsync-after-final-metadata
```

Therefore:

```text
V8 REQUEST/REVIEW/ADMISSION/GATE != R4R9 AUTHORITY
V8 HUMAN REVIEW MARKER != V9 HUMAN DECISION
V9 EFFECT PROFILE REQUIRES FRESH V9 HUMAN-BOUND REQUEST
```

No V8 or earlier Human evidence may authorize a V9 effect.

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

## 7. Core Human-decision rule

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

After implementation, the only current effect-capable Human-decision acceptance interface is:

```text
python phase6/scriptops-v2-hardening.py approve --decision-pr <positive-integer>
```

PR number is a locator only, never authority.

No caller-controlled field may supply Human actor/result/rationale, request path/digest, task/scene/candidate/impact identities, canonical target/ref, physical Git-dir/ref/object/index topology, metadata policy, reflog semantics, effect type, material effect, raw-object profile, hook profile, durability profile, commitment profile, or effect commit metadata.

Defect-era Phase-6 `approve --scene ... --why ...`, direct legacy `approve --scene ...`, and direct legacy `scene-promote --to accepted` remain disabled and non-effect-capable.

## 9. Git/runtime/OS profile V9

Git semantic compatibility remains bounded to:

```text
2.55.0 <= parsed Git version < 2.56.0
object format = sha1
ref storage format = files
```

R4R9 retains the Linux/POSIX mode-only profile and adds one exact Linux primitive:

```text
renameat2(..., RENAME_NOREPLACE)
```

Required runtime primitives are therefore:

```text
dir_fd relative open/mkdir/unlink/rename
renameat2(RENAME_NOREPLACE)
O_NOFOLLOW
O_DIRECTORY
O_EXCL
O_CLOEXEC
fstat/lstat
fchmod
fsync regular file
fsync directory
atomic same-directory rename
listxattr
POSIX ACL inspection capability
/proc/self/ns/mnt
/proc/self/mountinfo
```

A platform lacking `renameat2(RENAME_NOREPLACE)` or any other required proof primitive is `BLOCKED`.

Successful `fsync` is trusted only within the bounded OS/filesystem contract already used by R4R8: hardware/firmware/filesystems that falsely report durable completion are outside the claim.

Mount-namespace identity and reviewed mount containment remain stable through object preparation, ref commitment and post-effect verification.

## 10. POSIX_MODE_ONLY_SECURITY_METADATA_V1 preserved

The exact R4R8 metadata values remain:

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
logs/refs/heads/main if present or newly created   = 0644
.git/index                                         = 0644
canonical scene filesystem target                  = 0644
.scriptops/decision-log.ndjson                     = 0644
new loose-object fanout directory                  = 0755
new loose-object final file                        = 0444
ref/reflog/worktree/object/index temporary files   = 0600 before explicit final chmod
```

Required authority-critical metadata remain:

```text
uid = exact request-bound effective uid
gid = exact request-bound effective gid
no setuid/setgid/sticky bits
listxattr empty
POSIX access ACL equivalent to mode bits only
POSIX default ACL absent on writable authority-critical directories
no security capabilities / labels / arbitrary xattrs
```

Kernel inode number and ctime remain explicitly excluded operational metadata.

The effect process sets exactly:

```text
umask = 0077
```

in its dedicated effect process before any authority-critical temporary file is created.

## 11. FSYNC_AFTER_FINAL_METADATA_V1

This is the binding correction for PR #131 F001.

For every file inode newly created or replaced by the V9 effect, the durability barrier is ordered as follows:

```text
1. create private temporary inode
2. write exact complete final bytes
3. apply every authority-relevant final inode metadata value
4. verify exact bytes + mode + uid + gid + xattr/ACL profile
5. fsync(file_fd) AFTER the last authority-relevant inode metadata mutation
6. perform only a namespace operation that does not change any Human-bound inode field
7. fsync(containing_directory_fd)
8. reopen final path no-follow and verify exact poststate
```

Authority-relevant inode metadata include at least:

```text
content / size
mode
uid
gid
link-count requirement where the chosen installation primitive can change it
xattr/ACL absence
```

R4R9 therefore forbids a sequence of the form:

```text
fsync(file)
fchmod(file, final_mode)
install
```

and also forbids a sequence where the final security-relevant link-count is changed after the last file fsync.

After the final pre-install file fsync, only excluded operational metadata such as ctime may change as a consequence of the namespace operation.

If any authority-relevant inode metadata is modified again after installation, another file fsync is mandatory before any complete durable-success claim.

Directory fsync is always additional to, never a replacement for, the final file fsync.

## 12. Why loose-object linkat + unlink is removed

R4R8 used:

```text
linkat(temp, final)
unlink(temp)
```

as a no-replace install primitive.

That sequence temporarily changes `st_nlink` to 2 and then back to 1 after the earlier file fsync. Because `st_nlink = 1` is itself an authority/security predicate in the object profile, this violates `FSYNC_AFTER_FINAL_METADATA_V1` unless another file-fsync barrier is added after the final unlink.

R4R9 chooses a simpler closed primitive:

```text
renameat2(held_fanout_fd, temp_name,
          held_fanout_fd, final_oid_leaf,
          RENAME_NOREPLACE)
```

The production V9 loose-object installer MUST NOT use hard-link installation.

The final object inode has link count 1 before and after the rename; only its directory name changes.

If `RENAME_NOREPLACE` is unsupported or returns an unsupported semantic result, V9 is `BLOCKED`.

## 13. SINGLE_WORKTREE_REAL_GITDIR_V1 preserved

The R4R8 single-worktree physical Git-dir profile remains mandatory:

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

Retained descriptors for repository root and `.git` remain open through the final effect interval.

Root and `.git` satisfy the V9 metadata profile and reviewed mount identity.

## 14. PHYSICAL_PRIMARY_OBJECT_DB_NO_ALIAS_V1 preserved

The R4R8 object-database physical profile remains mandatory:

```text
.git/objects = real direct directory
held objects descriptor
same reviewed mount as .git
no nested/bind mount under objects
no symlink/reparse redirect
GIT_OBJECT_DIRECTORY absent
GIT_ALTERNATE_OBJECT_DIRECTORIES absent
objects/info/alternates absent
no partial/promisor/lazy-fetch escape
real no-follow authority-relevant fanout directories
real no-follow regular single-link authority-relevant loose leaves
real no-follow pack/info directories if present
```

Every authority-relevant object read/write remains physically contained under the held `.git/objects` descriptor chain.

## 15. COMPLETE_LOCAL_OBJECT_STORE_V2 preserved

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
unsupported pack metadata topology
```

No fetch, deepen, repair, repack, prune or normalization is authorized.

## 16. NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2 preserved

All object authority reads retain:

```text
GIT_NO_REPLACE_OBJECTS=1
GIT_NO_LAZY_FETCH=1
--no-replace-objects
--no-lazy-fetch
```

Missing local objects fail closed.

## 17. CLOSED_RAW_TREE_REWRITE_V1 preserved

The exact V9 tree is derived in memory from raw parent-tree bytes.

The helper:

```text
parses canonical raw tree entries
rejects malformed / duplicate / noncanonical / unsorted entries
uses Git 2.55 tree-name ordering
rewrites only the exact two target paths
uses tracked mode 100644 for both effect leaves
preserves every unrelated semantic tree entry
recursively reconstructs affected ancestor trees only
computes every tree SHA-1 from exact canonical object bytes
```

The only changed tracked paths remain:

```text
scenes/<scene_id>.fountain
.scriptops/decision-log.ndjson
```

## 18. CLOSED_RAW_COMMIT_OBJECT_V1 preserved

The effect commit remains exact raw bytes with only:

```text
tree
parent
author
committer
```

and exact message:

```text
scriptops x1b: accept <scene_id>\n
```

Identity/time remain deterministic from the Human-bound request.

No Git commit writer is permitted.

## 19. Canonical object bytes preserved

For each object type `T` and payload `P`:

```text
canonical_object_bytes = ASCII(T) + SP + ASCII(decimal(len(P))) + NUL + P
object_oid = lowercase_hex(SHA1(canonical_object_bytes))
```

Supported new object types remain exactly:

```text
blob
tree
commit
```

Loose zlib representation equivalence remains storage-only and non-authority-semantic; a fixed production compressor/runtime identity is still recorded as execution evidence.

## 20. ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V2 — fanout directory

For every required OID, derive exact lowercase two-hex fanout prefix.

Using held `.git/objects` fd:

```text
if fanout exists:
    open O_DIRECTORY | O_NOFOLLOW | O_CLOEXEC relative to objects fd
    require real 0755 dir
    exact uid/gid
    no xattrs/default ACL
    same mount identity
else:
    mkdir relative to held objects fd initial 0700
    open no-follow directory fd
    fchmod 0755
    verify metadata
    fsync(new_fanout_fd) AFTER fchmod
    fsync(held_objects_fd)
```

Retain fanout fd until all object installs assigned to it are complete.

Reopen from held objects fd and compare identity before and after each install.

## 21. ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V2 — existing leaf

If exact final OID leaf already exists:

```text
open relative to held fanout fd O_NOFOLLOW
require regular file
require st_nlink = 1
require mode 0444
require exact uid/gid
require no xattrs/ACL beyond profile
require same reviewed mount
inflate one complete stream with no trailing garbage
require exact canonical type/length/payload
require SHA1 = path OID
```

No overwrite or metadata normalization of an existing object is authorized.

Any malformed, aliased or unsupported object is `BLOCKED`.

## 22. ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V2 — new leaf

If final OID leaf is absent:

```text
A. create unpredictable temp leaf in held fanout dir
   O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC
   initial mode 0600 under umask 0077

B. write one complete zlib stream inflating to exact canonical object bytes

C. reread/verify exact canonical object bytes and OID

D. fchmod(temp_fd, 0444)

E. verify final pre-install metadata:
   regular file
   st_nlink = 1
   mode = 0444
   exact uid/gid
   xattrs empty
   ACL mode-only

F. fsync(temp_fd) AFTER fchmod and metadata verification

G. renameat2 held-fanout temp -> exact final OID leaf with RENAME_NOREPLACE

H. if RENAME_NOREPLACE reports EEXIST:
   do not alter winner
   unlink private temp
   fsync held fanout dir for temp removal
   verify winner through the existing-leaf rule

I. on successful rename:
   fsync(held_fanout_fd)

J. reopen final leaf O_NOFOLLOW and verify:
   regular
   st_nlink = 1
   mode 0444
   exact uid/gid/xattr/ACL
   exact canonical object content/OID
   exact canonical fanout hierarchy identity
```

No authority-relevant inode metadata is changed after step F on the successful rename path.

A crash after successful rename but before fanout-directory fsync yields an object-preparation durability uncertainty outcome, not complete preparation success.

## 23. New-object closure V9

After admission and deterministic decision-record construction, derive exact:

```text
new_object_closure = every blob/tree/commit reachable from effect commit
                     that is not reachable from raw request-base parent
```

Each member is represented by exact tuple:

```text
(type, payload_length, payload_sha256, oid)
```

Every member must have an exact physically contained loose representation before ref commitment, even if the same object also exists in a pack.

The contained loose copy remains an explicit Human-bound V9 preparation effect.

## 24. Object-preparation side-effect truth preserved

Pre-ref object installation may leave durable unreferenced objects/fanout dirs.

R4R9 never misreports that as “no filesystem effect”.

Normal pre-ref outcome classes continue to distinguish no preparation from prepared objects.

No cleanup routine may delete a pre-existing object or guess ownership of a concurrently installed object.

## 25. PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1 preserved

Required:

```text
HEAD = regular 0644 non-symlink exact bytes "ref: refs/heads/main\n"
refs = real 0755 directory
refs/heads = real 0755 directory
refs/heads/main = direct regular single-link 0644 loose ref
packed-refs contains no refs/heads/main
main.lock absent before acquisition
core.preferSymlinkRefs absent/false
exact uid/gid and mode-only metadata
same reviewed mount as .git
```

Held refs/heads descriptor and canonical identity revalidation remain mandatory.

## 26. ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V3

The physical ref commitment remains a non-Git descriptor-relative operation.

Acquire `main.lock` under held refs/heads fd with:

```text
O_WRONLY | O_CREAT | O_EXCL | O_NOFOLLOW | O_CLOEXEC
initial mode 0600
```

Then:

```text
1. repeat physical old-main / packed-main / hierarchy proof
2. write exact effect SHA + LF
3. reread exact bytes
4. fchmod(main.lock fd, 0644)
5. verify regular single-link 0644 exact uid/gid/xattr/ACL
6. fsync(main.lock fd) AFTER final fchmod
7. reread old main exact request base + LF
8. revalidate packed-main absence and hierarchy/mount identities
9. descriptor-relative same-directory atomic rename main.lock -> main
10. fsync held refs/heads directory
11. reopen main O_NOFOLLOW and verify exact final ref + metadata + hierarchy
```

There is no file metadata mutation between step 6 and step 9 other than excluded operational ctime caused by namespace replacement.

No Git ref-mutating command is permitted.

### 26.1 Crash residue truth

A crash after creation of `main.lock` but before ref rename may leave `refs/heads/main.lock`.

That residue is not a successful Human-attributed ref effect, but it is persistent Git metadata and must be reported truthfully.

A restart/recovery classifier MUST distinguish:

```text
main old + main.lock absent
main old + V9-shaped main.lock present
main new
ambiguous/unreadable
```

No automatic deletion of an ambiguous lockfile is authorized.

## 27. Main reflog prestate V9

The V8 deterministic Human-bound branch reflog semantics remain, with the durability implementation bumped to V2.

Required parent dirs remain real 0755 same-mount mode-only paths.

`logs/refs/heads/main` may be absent or an exact regular single-link 0644 prestate file.

The request binds exact:

```text
exists
file_sha256
byte_length
filesystem_mode
uid
gid
xattrs=[]
acl=MODE_BITS_ONLY
```

## 28. DETERMINISTIC_MAIN_REFLOG_PROJECTION_V2

Only after normal durable physical main-ref commitment:

```text
1. revalidate exact Human-bound reflog prestate
2. construct exact prior-bytes + exact V9 reflog line
3. create private temp 0600 in held logs/refs/heads directory
4. write exact complete after-bytes
5. reread exact content
6. fchmod temp to 0644
7. verify uid/gid/mode/xattr/ACL
8. fsync(temp_fd) AFTER final metadata
9. atomic descriptor-relative rename temp -> main
10. fsync held reflog parent directory
11. reopen final main reflog O_NOFOLLOW and verify exact bytes/hash/metadata
```

If reflog prestate drifted after ref commitment, do not overwrite; return committed recovery-required.

Exact reflog line remains:

```text
<request_base_sha> <effect_commit_sha> ScriptOps X1B <scriptops-x1b@local.invalid> <request_epoch> +0000\tscriptops x1b: accept <scene_id>\n
```

No execution wall clock, ambient Git identity, locale, timezone or `GIT_REFLOG_ACTION` contributes.

## 29. PR #131 F002 correction — FULL_SINGLE_FILE_INDEX_V1

R4R9 no longer accepts arbitrary Git index formats.

Before request creation, admission, FinalEffectGateV9, immediately pre-ref, immediately post-ref before index projection, and final verification, the canonical real index prestate must satisfy a closed profile.

### 29.1 Physical index file

Require:

```text
.git/index exists
regular non-symlink file
st_nlink = 1
mode = 0644
exact request-bound uid/gid
xattrs empty
ACL mode-only
same reviewed mount as .git
index.lock absent before post-ref index projection
```

### 29.2 Raw index format

The V9 in-process parser reads `.git/index` directly with no Git command and requires:

```text
signature = DIRC
version = exactly 2
entry count well-formed
trailing SHA-1 checksum valid
all entries parse canonically
all entries stage = 0
extended flag = 0
pathnames canonical and unique
entries sorted in Git index pathname order
no malformed padding
NO EXTENSIONS AT ALL
```

Because no extensions are permitted, the split-index `link` extension cannot exist.

No untracked-cache, fsmonitor, cache-tree, resolve-undo, sparse-index or unknown optional extension is preserved in the supported V9 index profile.

This is intentionally restrictive and fail-closed.

### 29.3 Semantic equality to raw parent tree

The exact stage-0 tuple set from the full index:

```text
(path, Git mode, object OID)
```

must equal the recursively flattened raw request-base tree exactly.

No unmerged stages, intent-to-add, sparse directory entries or index-only staged deltas are supported.

If index semantic content differs from parent tree before effect, V9 is `BLOCKED`.

## 30. Shared-index closure

R4R9 requires an exact negative namespace proof under held `.git` directory:

```text
no file whose basename matches sharedindex.<40-lowercase-hex>
no other sharedindex.* entry
```

at every authority checkpoint.

Also require effective config:

```text
core.splitIndex absent or false
all splitIndex.* config absent
```

and strip caller `GIT_INDEX_FILE` injection.

All authority-critical Git subprocesses receive:

```text
-c core.splitIndex=false
```

as defense in depth.

However, the core V9 property does not depend on Git obeying this flag because no authority-critical Git command is permitted to read or write the real index.

## 31. No pre-ref Git index read

This closes the PR #131 observation that merely reading a split index can freshen a shared-index mtime.

Before ref commitment:

```text
NO Git command may read canonical .git/index
```

All pre-ref index authority checks are performed by the in-process raw `FULL_SINGLE_FILE_INDEX_V1` parser.

Allowed Git cross-checks are object/tree-only commands that do not consult the index.

If a proposed command cannot be proven index-independent, it is forbidden from the V9 effect path.

## 32. CLOSED_FULL_INDEX_V2_REWRITE_V1

The final canonical index is derived entirely in memory.

Inputs:

```text
exact Human-bound raw prestate index bytes
parsed FULL_SINGLE_FILE_INDEX_V1 entries
exact derived V9 new_tree
exact two changed tracked paths
```

Output:

```text
one complete extension-free Git index version 2 byte string
```

### 32.1 Rewrite rule

For every path present in the derived `new_tree`:

```text
if the path existed in the prestate index:
    preserve its exact stat-cache fields
    preserve assume-valid bit
    preserve path bytes
    replace Git mode and object OID with exact new_tree values
    force stage = 0
    extended flag = 0
else:
    create a version-2 stage-0 entry
    all stat-cache numeric fields = 0
    Git mode = exact new_tree mode
    object OID = exact new_tree OID
    assume-valid = 0
    pathname = exact raw repo-relative path bytes
```

R4R9 effect does not delete an unrelated indexed path because `new_tree` differs from the parent at exactly the two bounded target paths.

### 32.2 Encoding rule

Construct exactly:

```text
DIRC header
version = 2
exact entry count
entries in canonical pathname order
version-2 entry fields in network byte order
NUL termination and 8-byte entry padding per Git index-v2 format
NO EXTENSIONS
trailing SHA-1 checksum over all preceding index bytes
```

The helper independently recomputes and verifies the checksum before any write.

### 32.3 Why stat fields may remain stale on changed paths

For an existing changed path, preserving prior stat-cache fields may cause a later ordinary Git command to refresh or re-check that entry.

That is deliberate and safe: index authority in X1B is the exact `(path,mode,OID)` stage-0 mapping, not a promise that cached worktree stat data is fresh.

R4R9 does not invent ambient wall-clock/stat data merely to make the index look freshly refreshed.

The Human-bound effect explicitly selects this deterministic preservation rule.

## 33. Canonical index effect binding

PresentedMaterialEffectV9 binds:

```text
index_prestate_sha256 = exact SHA-256 of raw .git/index bytes
index_profile = FULL_SINGLE_FILE_INDEX_V1
index_projection_profile = CLOSED_FULL_INDEX_V2_REWRITE_V1
index_install_profile = ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1
index_after_source = DETERMINISTIC_FROM_EXACT_PRESTATE_INDEX_PLUS_DERIVED_NEW_TREE
index_filesystem_mode_after = 0644
sharedindex_effect = NONE
```

The future final index digest is not copied into the request as an independently chosen value because its changed OIDs include the derived decision-log object.

The formula is closed and uniquely determines the bytes once admitted review metadata determines the decision record and therefore the exact derived new tree.

This is the same noncircular binding pattern used for the derived effect commit SHA.

## 34. ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1

No Git command writes the real index in V9.

Only after durable physical main-ref commitment and after confirming the raw canonical index is still byte-for-byte equal to the Human-bound prestate:

```text
1. require index.lock absent
2. require no sharedindex.* entries
3. acquire .git/index.lock via held .git fd:
   O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC
   initial mode 0600
4. reread .git/index exact prestate and revalidate physical identity/profile
5. if drifted: do not overwrite; return committed recovery-required
6. write exact CLOSED_FULL_INDEX_V2_REWRITE_V1 bytes to index.lock
7. reread and validate exact index-v2 structure/checksum/semantic new_tree equality
8. fchmod(index.lock fd, 0644)
9. verify exact uid/gid/mode/xattr/ACL
10. fsync(index.lock fd) AFTER final fchmod
11. descriptor-relative atomic rename index.lock -> index
12. fsync held .git directory
13. reopen .git/index O_NOFOLLOW and verify exact final bytes/profile
14. require no sharedindex.* entries
```

The production V9 effect path contains:

```text
GIT_REAL_INDEX_MUTATING_COMMAND = NONE
```

`post-index-change` hooks therefore cannot be generated by the index projection because Git is not performing the projection.

## 35. Index concurrency and recovery truth

Before ref commitment, concurrent canonical-index mutation is detected by repeated raw prestate digest checks.

If the index changes after the final pre-ref check but before ref commitment, ref commitment may still occur; post-ref index projection then detects the drift before overwrite and returns:

```text
DURABLY_REF_COMMITTED_RECOVERY_REQUIRED
```

It never silently overwrites a post-request index change.

If a crash after ref commitment leaves `.git/index.lock`, recovery must classify it explicitly.

No ambiguous `index.lock` is automatically deleted.

Because real index projection is post-ref, index-lock residue can never be misreported as pre-ref acceptance success.

## 36. ALIAS_SAFE_WORKTREE_PROJECTION_V2

Canonical scene and decision-log filesystem projection use the same ordered durability rule.

For each target:

```text
1. prove parent descriptor topology and exact Human-bound prestate
2. create private temp 0600 in target parent
3. write exact complete after-bytes
4. reread exact content
5. fchmod temp 0644
6. verify uid/gid/mode/xattr/ACL
7. fsync(temp_fd) AFTER final fchmod
8. atomic descriptor-relative rename temp -> final target
9. fsync held parent directory
10. reopen final target O_NOFOLLOW
11. verify exact content/hash/mode/metadata/topology
```

No in-place append is used for the decision log.

No post-fsync security metadata mutation is permitted.

If projection fails after durable ref commitment, return recovery-required and do not roll back the ref.

## 37. Hook closure preserved and simplified

`NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1` remains mandatory for all remaining Git subprocesses.

V9 removes two hook-relevant writers entirely:

```text
Git ref mutation = NONE
Git real-index mutation = NONE
```

Git primary-object mutation also remains:

```text
NONE
```

Remaining Git subprocesses are read-only cross-checks under the verified empty hookdir and sanitized profile.

## 38. Sanitized Git subprocess profile V9

Every authority-critical Git subprocess remains:

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

Strip caller Git config, loader, executable, object-directory, alternates, askpass, SSH and replacement variables.

Global/command-scope controls retain:

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

No V9 durability claim relies on Git `core.fsync` for object/ref/reflog/index/worktree writes because those writes are performed by explicit OS-level helpers.

## 39. PresentedMaterialEffectV9

Closed schema:

```text
PresentedMaterialEffectV9 = {
  "schema_version": "scriptops-x1b-presented-material-effect/v9",
  "repository": "FJ899/scriptops",
  "scene_id": <exact scene ID>,
  "candidate_path": <exact repo-relative candidate path>,
  "candidate_file_sha256": <64 lowercase hex>,
  "execution_identity": {
    "uid": <exact nonnegative integer>,
    "gid": <exact nonnegative integer>,
    "umask": "0077",
    "metadata_profile": "POSIX_MODE_ONLY_SECURITY_METADATA_V1"
  },
  "canonical_scene_effect": {
    "target_path": "scenes/<scene_id>.fountain",
    "before": <CanonicalPreStateV1>,
    "after_file_sha256": <accepted canonical SHA256>,
    "source_status": "candidate",
    "canonical_status_after": "accepted",
    "candidate_source_preserved": true,
    "git_mode_after": "100644",
    "filesystem_mode_after": "0644",
    "projection_profile": "ALIAS_SAFE_WORKTREE_PROJECTION_V2"
  },
  "decision_log_effect": {
    "target_path": ".scriptops/decision-log.ndjson",
    "append_count": 1,
    "record_schema_version": "scriptops-x1b-decision-record/v9",
    "record_result": "REF_COMMITTED",
    "append_semantics": "EXACT_PRIOR_BYTES_PLUS_ONE_CANONICAL_RECORD_PLUS_LF",
    "git_mode_after": "100644",
    "filesystem_mode_after": "0644",
    "projection_profile": "ALIAS_SAFE_WORKTREE_PROJECTION_V2"
  },
  "local_git_effect": {
    "target_ref": "refs/heads/main",
    "ref_before": <repository_head_at_request>,
    "commit_count": 1,
    "commit_message": "scriptops x1b: accept <exact scene_id>",
    "commit_author_name": "ScriptOps X1B",
    "commit_author_email": "scriptops-x1b@local.invalid",
    "commit_committer_name": "ScriptOps X1B",
    "commit_committer_email": "scriptops-x1b@local.invalid",
    "commit_time_source": "request_created_at",
    "git_semantics_profile": "GIT_2_55_X1B_V1",
    "ref_storage_format": "files",
    "gitdir_profile": "SINGLE_WORKTREE_REAL_GITDIR_V1",
    "physical_main_ref_profile": "PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1",
    "physical_object_db_profile": "PHYSICAL_PRIMARY_OBJECT_DB_NO_ALIAS_V1",
    "object_store_profile": "COMPLETE_LOCAL_OBJECT_STORE_V2",
    "tree_construction_profile": "CLOSED_RAW_TREE_REWRITE_V1",
    "object_install_profile": "ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V2",
    "metadata_profile": "POSIX_MODE_ONLY_SECURITY_METADATA_V1",
    "durability_order_profile": "FSYNC_AFTER_FINAL_METADATA_V1",
    "raw_object_profile": "NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2",
    "hook_profile": "NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1",
    "commit_object_profile": "CLOSED_RAW_COMMIT_OBJECT_V1",
    "ref_cas_profile": "ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V3",
    "durability_profile": "CRASH_DURABLE_OBJECT_REF_INDEX_V4",
    "success_commitment_profile": "ALIAS_SAFE_MAIN_REF_COMMITMENT_V5",
    "effect_transport_profile": "REF_CAS_FIRST_ALIAS_SAFE_RAW_GIT_METADATA_V7",
    "git_ref_mutating_command": "NONE",
    "git_primary_object_mutating_command": "NONE",
    "git_real_index_mutating_command": "NONE",
    "pre_ref_object_preparation": "EXACT_CONTAINED_LOOSE_OBJECTS_MAY_BE_DURABLY_INSTALLED_BEFORE_REF_CAS",
    "reflog_effect": {
      "target_git_metadata_path": "logs/refs/heads/main",
      "before": <MainReflogPreStateV2>,
      "projection_profile": "DETERMINISTIC_MAIN_REFLOG_PROJECTION_V2",
      "filesystem_mode_after": "0644",
      "entry_old_oid_source": "REQUEST_BASE_SHA",
      "entry_new_oid_source": "EXACT_DERIVED_EFFECT_COMMIT_SHA",
      "entry_committer": "ScriptOps X1B <scriptops-x1b@local.invalid>",
      "entry_time_source": "request_created_at",
      "entry_timezone": "+0000",
      "entry_message": "scriptops x1b: accept <exact scene_id>",
      "append_count": 1
    },
    "index_effect": {
      "target_git_metadata_path": "index",
      "before_file_sha256": <exact raw index prestate sha256>,
      "prestate_profile": "FULL_SINGLE_FILE_INDEX_V1",
      "projection_profile": "CLOSED_FULL_INDEX_V2_REWRITE_V1",
      "install_profile": "ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1",
      "after_source": "DETERMINISTIC_FROM_EXACT_PRESTATE_INDEX_PLUS_DERIVED_NEW_TREE",
      "filesystem_mode_after": "0644",
      "sharedindex_effect": "NONE"
    },
    "exact_changed_paths": [
      "scenes/<scene_id>.fountain",
      ".scriptops/decision-log.ndjson"
    ]
  },
  "file_identity_profile": "SINGLE_LINK_ALIAS_SAFE_REPOSITORY_TARGETS_V1"
}
```

## 40. Canonical prestates V9

`CanonicalPreStateV1` remains:

```text
{
  "exists": <true|false>,
  "file_sha256": <64 lowercase hex or null>
}
```

`MainReflogPreStateV2` remains exact from R4R8.

R4R9 adds an exact raw index prestate record:

```text
FullIndexPreStateV1 = {
  "file_sha256": <64 lowercase hex>,
  "byte_length": <nonnegative integer>,
  "version": 2,
  "entry_count": <nonnegative integer>,
  "extension_count": 0,
  "stage0_tree_digest": <sha256 canonical digest of ordered path/mode/oid tuples>,
  "filesystem_mode": "0644",
  "uid": <exact uid>,
  "gid": <exact gid>,
  "nlink": 1,
  "xattrs": [],
  "acl": "MODE_BITS_ONLY",
  "sharedindex_entries": []
}
```

The request also binds the exact physical-prestate digest for root, `.git`, objects/ref/log hierarchy, `main`, reflog, index and worktree targets.

## 41. HumanDecisionRequestBindingV9

```text
HumanDecisionRequestBindingV9 = {
  "schema_version": "scriptops-x1b-human-decision-request/v9",
  "repository": "FJ899/scriptops",
  "repository_head_at_request": <40 lowercase hex>,
  "repository_ref_at_request": "refs/heads/main",
  "request_created_at": <exact timestamp>,
  "execution_uid": <exact uid>,
  "execution_gid": <exact gid>,
  "task_id": <exact task ID>,
  "scene_id": <exact scene ID>,
  "candidate_path": <exact path>,
  "candidate_file_sha256": <exact digest>,
  "impact_report_path": <exact path>,
  "impact_report_sha256": <exact digest>,
  "canonical_target": "scenes/<scene_id>.fountain",
  "canonical_ref": "refs/heads/main",
  "main_reflog_prestate": <MainReflogPreStateV2>,
  "full_index_prestate": <FullIndexPreStateV1>,
  "physical_git_metadata_prestate_digest": <sha256 of closed V9 physical-prestate record>,
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect": <PresentedMaterialEffectV9>
}
```

```text
request_digest = sha256_canonical(binding)
decision_request_id = "x1b:" + request_digest
```

## 42. Proposal PR and V9 Human review marker

Proposal construction remains one-file and acyclic:

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

Exact manual GitHub UI APPROVE body is four LF-separated lines with no trailing LF:

```text
X1B-HUMAN-DECISION-V9
decision_request_id=<exact x1b:<request_digest>>
decision_request_sha256=<exact request_digest>
why=<Human rationale>
```

V8 or earlier review markers are invalid for V9.

## 43. Trusted GitHub evidence and freshness preserved

Public exact-origin GitHub evidence transport, no proxy/redirect/auth fallback, complete review pagination, current-head binding, duplicate ambiguity, active CHANGES_REQUESTED handling, no-latest-wins semantics, exact proposal envelope, replay lock and freshness/supersession rules remain as R4R8 with V9 schema names.

A selected decision is active only while every exact PR/request/review/local-ref/raw-object/object-store/physical-path/metadata/reflog/index/applicability predicate remains true.

```text
NO WALL-CLOCK TTL
AGE ALONE != STALE
```

## 44. X1BDecisionRecordV9

```text
X1BDecisionRecordV9 = {
  "schema_version": "scriptops-x1b-decision-record/v9",
  "result": "REF_COMMITTED",
  "result_scope": "PHYSICAL_LOOSE_REFS_HEADS_MAIN_POINTS_TO_EXACT_EFFECT_COMMIT",
  "decision_type": "scene_acceptance_ref_committed",
  "decision_request_id": <exact ID>,
  "request_digest": <exact digest>,
  "decision_pr_number": <positive integer>,
  "decision_pr_head": <exact head>,
  "human_review_numeric_id": <canonical decimal string>,
  "human_review_node_id": <exact node ID>,
  "human_actor": "litrgratis-pixel",
  "human_review_commit": <exact PR head>,
  "human_review_body_sha256": <exact digest>,
  "human_review_submitted_at": <exact timestamp>,
  "human_rationale": <exact rationale>,
  "admission_id": <exact admission ID>,
  "final_effect_gate_digest": <exact digest>,
  "complete_review_set_digest": <exact digest>,
  "task_id": <exact task>,
  "scene_id": <exact scene>,
  "candidate_path": <exact path>,
  "candidate_file_sha256": <exact digest>,
  "impact_report_path": <exact path>,
  "impact_report_sha256": <exact digest>,
  "canonical_target": "scenes/<scene_id>.fountain",
  "canonical_ref": "refs/heads/main",
  "ref_before": <exact request base>,
  "execution_uid": <exact uid>,
  "execution_gid": <exact gid>,
  "main_reflog_prestate": <MainReflogPreStateV2>,
  "full_index_prestate": <FullIndexPreStateV1>,
  "canonical_before": <CanonicalPreStateV1>,
  "canonical_after_file_sha256": <exact digest>,
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect_digest": <exact digest>,
  "gitdir_profile": "SINGLE_WORKTREE_REAL_GITDIR_V1",
  "physical_main_ref_profile": "PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1",
  "physical_object_db_profile": "PHYSICAL_PRIMARY_OBJECT_DB_NO_ALIAS_V1",
  "object_store_profile": "COMPLETE_LOCAL_OBJECT_STORE_V2",
  "tree_construction_profile": "CLOSED_RAW_TREE_REWRITE_V1",
  "object_install_profile": "ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V2",
  "metadata_profile": "POSIX_MODE_ONLY_SECURITY_METADATA_V1",
  "durability_order_profile": "FSYNC_AFTER_FINAL_METADATA_V1",
  "index_prestate_profile": "FULL_SINGLE_FILE_INDEX_V1",
  "index_projection_profile": "CLOSED_FULL_INDEX_V2_REWRITE_V1",
  "index_install_profile": "ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1",
  "raw_object_profile": "NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2",
  "hook_profile": "NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1",
  "commit_object_profile": "CLOSED_RAW_COMMIT_OBJECT_V1",
  "ref_cas_profile": "ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V3",
  "reflog_projection_profile": "DETERMINISTIC_MAIN_REFLOG_PROJECTION_V2",
  "durability_profile": "CRASH_DURABLE_OBJECT_REF_INDEX_V4",
  "success_commitment_profile": "ALIAS_SAFE_MAIN_REF_COMMITMENT_V5",
  "canonical_instance_scope": "LOCAL_PHYSICAL_MAIN_REF_OBJECT_DB_FULL_INDEX_WORKTREE_DECISION_LOG_REFLOG_V9"
}
```

The record continues to say `REF_COMMITTED`, not generic success.

## 45. FinalEffectGateV9

Immediately before deterministic record/object derivation, while the same-worktree exclusive X1B lock is held, freshly validate:

```text
exact V9 PR/request/review envelope
Human currentness/conflicts
CompleteReviewSetV9 digest
raw logical main SHA = request base
SINGLE_WORKTREE_REAL_GITDIR_V1
PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1
PHYSICAL_PRIMARY_OBJECT_DB_NO_ALIAS_V1
COMPLETE_LOCAL_OBJECT_STORE_V2
POSIX_MODE_ONLY_SECURITY_METADATA_V1
FSYNC_AFTER_FINAL_METADATA_V1 capability
FULL_SINGLE_FILE_INDEX_V1 exact
no sharedindex.*
core.splitIndex absent/false
MainReflogPreStateV2 exact
mount namespace and mountinfo containment exact
Git 2.55.x
files ref format
NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2
NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1
zero refs/replace
raw parent commit/tree
candidate/impact/canonical prestate
accepted preview
PresentedMaterialEffectV9
replay state
raw full-index semantic tree = raw parent tree
alias-safe worktree target preconditions
verified empty hook directory
system Git/OS proof primitives including renameat2(RENAME_NOREPLACE)
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

## 46. Exact local effect sequence V9

With X1B lock held after FinalEffectGateV9:

```text
A. re-prove raw-object, complete-local-store, physical Git-dir/ref/object-store,
   metadata, reflog and FULL_SINGLE_FILE_INDEX_V1 profiles

B. construct X1BDecisionRecordV9 bytes in memory

C. construct exact accepted-scene and decision-log payloads in memory
   compute exact blob canonical bytes/OIDs

D. execute CLOSED_RAW_TREE_REWRITE_V1
   derive exact affected tree payloads/OIDs
   prove exact two-path semantic delta

E. construct exact CLOSED_RAW_COMMIT_OBJECT_V1 in memory
   compute exact effect commit SHA

F. derive exact new_object_closure tuples

G. install every closure member through ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V2
   renameat2(RENAME_NOREPLACE)
   final metadata before file fsync
   directory fsync after final-name install

H. cross-check installed commit/tree/object closure using object-only read-only Git plumbing
   no index access

I. derive exact CLOSED_FULL_INDEX_V2_REWRITE_V1 final index bytes in memory
   do not write real index yet

J. final pre-ref checks:
   physical main exact old SHA
   packed main absent
   ref hierarchy exact
   object-store hierarchy exact
   every closure object exact/contained/durable
   reflog prestate exact
   FULL_SINGLE_FILE_INDEX_V1 exact raw prestate unchanged
   no sharedindex.*
   security metadata exact
   mount namespace/mount IDs exact
   hook census empty

K. acquire main.lock descriptor-relative O_EXCL/O_NOFOLLOW
   repeat old-value/topology/metadata proof

L. write exact effect SHA + LF
   fchmod 0644
   verify metadata
   fsync main.lock AFTER final metadata
   final old-main proof

M. descriptor-relative atomic rename main.lock -> main
   fsync held refs/heads directory
   classify physical ref result

N. after normal durable ref commitment:
   execute DETERMINISTIC_MAIN_REFLOG_PROJECTION_V2

O. execute ALIAS_SAFE_WORKTREE_PROJECTION_V2 for canonical scene

P. execute ALIAS_SAFE_WORKTREE_PROJECTION_V2 for decision log

Q. execute ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1
   only if canonical raw index still equals exact Human-bound prestate
   no Git index writer
   no sharedindex footprint

R. verify physical ref, logical ref, raw commit/tree/object closure,
   physical object-store containment, reflog, worktree, FULL_SINGLE_FILE_INDEX_V1
   final index semantic new_tree equality, zero sharedindex entries,
   mount identity and all security metadata

S. release X1B lock only after final outcome class is determined
```

No canonical worktree, decision-log, reflog or real-index mutation occurs before physical main-ref commitment.

Exact unreferenced loose object preparation may occur before ref commitment and is reported as such.

## 47. CRASH_DURABLE_OBJECT_REF_INDEX_V4

Normal durable new-object preparation requires:

```text
complete temp write
exact content reread
final fchmod 0444
exact metadata verification
file fsync AFTER final metadata
RENAME_NOREPLACE final-name install
fanout directory fsync
final no-follow exact reread
```

Normal durable ref commitment requires:

```text
main.lock complete write
final fchmod 0644
exact metadata verification
main.lock file fsync AFTER final metadata
atomic same-dir rename over main
refs/heads directory fsync
exact physical main reread
stable canonical hierarchy proof
```

Normal reflog/worktree/index projections each require:

```text
complete temp write
final fchmod 0644
exact metadata verification
file fsync AFTER final metadata
atomic descriptor-relative rename
parent directory fsync
exact final reread
```

A file-fsync barrier performed before the final authority-relevant metadata mutation never counts toward this profile.

## 48. ALIAS_SAFE_MAIN_REF_COMMITMENT_V5

Successful `REF_COMMITTED` truth requires:

```text
exact effect commit object closure physically contained
all new closure objects normal-durable under V4
main physical loose ref = exact effect SHA
main mode/uid/gid/xattr/ACL exact
main ref file and refs/heads directory durability barriers completed
canonical ref hierarchy still resolves to held identities
```

Reflog/worktree/index are post-ref projections and are prerequisites for complete zero exit, not prerequisites for truthful `REF_COMMITTED` record scope.

## 49. Outcome classes V9

Implementation must distinguish at least:

```text
DENIED
BLOCKED_PRE_COMMIT_NO_OBJECT_PREP
BLOCKED_PRE_COMMIT_OBJECT_PREPARED
BLOCKED_PRE_COMMIT_REF_LOCK_RESIDUE
OBJECT_STORE_TOPOLOGY_UNCERTAIN
REF_COMMITTED_DURABILITY_UNCERTAIN
REF_COMMITTED_TOPOLOGY_UNCERTAIN
COMMITMENT_STATE_UNKNOWN
DURABLY_REF_COMMITTED_RECOVERY_REQUIRED
DURABLY_REF_COMMITTED_COMPLETE
```

Semantics:

```text
DENIED:
  admission/final gate denies before preparation
  main remains old SHA

BLOCKED_PRE_COMMIT_NO_OBJECT_PREP:
  main old
  no new closure object durably installed
  no canonical worktree/index/reflog effect

BLOCKED_PRE_COMMIT_OBJECT_PREPARED:
  main old
  exact unreferenced contained objects/fanout dirs may remain
  no canonical worktree/index/reflog effect

BLOCKED_PRE_COMMIT_REF_LOCK_RESIDUE:
  main old
  refs/heads/main.lock may remain after crash/interruption
  no acceptance-success claim
  preserve evidence / require explicit recovery handling

OBJECT_STORE_TOPOLOGY_UNCERTAIN:
  object preparation target relationship uncertain
  no success claim

REF_COMMITTED_DURABILITY_UNCERTAIN:
  physical main visibly equals effect SHA
  required ref durability barrier not proven
  no complete-success claim
  no rollback

REF_COMMITTED_TOPOLOGY_UNCERTAIN:
  descriptor-relative ref commit may have occurred in held hierarchy
  canonical hierarchy relation unproven
  no complete-success claim

COMMITMENT_STATE_UNKNOWN:
  ref state cannot be classified exactly
  preserve evidence
  no rollback

DURABLY_REF_COMMITTED_RECOVERY_REQUIRED:
  main durably exact effect SHA
  one or more reflog/worktree/index post-ref projections incomplete,
  drifted, failed, ambiguous or left lock/temp residue
  no rollback

DURABLY_REF_COMMITTED_COMPLETE:
  durable ref exact
  deterministic reflog exact
  canonical scene exact
  decision log exact
  full single-file extension-free index v2 exact new_tree
  no sharedindex.*
  all metadata/durability profiles exact
```

## 50. No rollback rule preserved

After visible or possible ref commitment:

```text
NO AUTOMATIC HISTORY ROLLBACK
```

Post-ref failures use explicit recovery-required / uncertainty states.

Recovery authority remains separate and is not granted by this brief.

## 51. Mandatory negative regressions — PR #131 F001

A future independent review must require fault injection for at least:

```text
loose object crash after write before fchmod
loose object crash after fchmod before file fsync
loose object crash after file fsync before RENAME_NOREPLACE
loose object crash after rename before fanout-dir fsync
loose object successful final nlink = 1
prove production path never uses linkat hard-link install

main.lock crash after write before fchmod
main.lock crash after fchmod before file fsync
main.lock crash after file fsync before rename
main crash after rename before refs/heads dir fsync

reflog temp crash after fchmod before file fsync
reflog crash after file fsync before rename
reflog crash after rename before parent-dir fsync

scene temp crash after fchmod before file fsync
log temp crash after fchmod before file fsync
index.lock crash after fchmod before file fsync
index crash after file fsync before rename
index crash after rename before .git dir fsync
```

Expected: no `DURABLY_*_COMPLETE` classification unless the final metadata mutation is included in a completed file fsync and the final namespace mutation in a completed parent-dir fsync.

## 52. Mandatory negative regressions — split index / shared index

Must test at minimum:

```text
core.splitIndex=true
core.splitIndex=1
included splitIndex config
splitIndex.maxPercentChange present
splitIndex.sharedIndexExpire present
raw .git/index containing lowercase link extension
valid split index referencing sharedindex.<SHA1>
zero-hash link extension
pre-existing .git/sharedindex.<40hex>
multiple sharedindex.* files
sharedindex symlink
sharedindex hardlink
sharedindex unexpected basename
concurrent sharedindex appearance before ref
concurrent canonical index drift after ref before projection
index.lock preexists at post-ref projection
```

Expected:

```text
all split-index/sharedindex prestates BLOCK before ref
no Git command reads canonical index pre-ref
no Git command writes canonical index post-ref
no sharedindex file is created, touched, freshened or deleted by a successful V9 effect
post-ref index drift -> recovery-required, never overwrite
```

## 53. Mandatory raw-index regressions

Must test:

```text
index signature not DIRC
version 3
version 4
bad trailing checksum
truncated entry
bad padding
duplicate path
out-of-order path
stage 1/2/3 entry
extended flag set
optional uppercase extension
cache-tree extension
REUC extension
UNTR extension
FSMN extension
IEOT extension
sdir extension
link extension
unknown extension
index semantic tuple set differs from raw parent tree
new scene path absent in prestate -> deterministic zero-stat new v2 entry
existing scene path -> stat-cache preservation + new OID
existing decision-log path -> stat-cache preservation + new OID
final v2 checksum exact
final stage-0 tuple set exactly equals derived new_tree
```

Every unsupported case must fail closed before ref commitment.

## 54. Mandatory preserved regressions

Future review must also rerun earlier attack classes:

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
loose fanout symlink
loose object hardlink
alternate/promisor/lazy-fetch escape
replacement refs
commit encoding
configured hooks
ambient identity/time/reflog variables
reflog symlink/hardlink/parent redirect
reflog prestate drift
worktree target hardlink/symlink
freshness/supersession/conflict/replay
Human review author/currentness/body binding
```

R4R9 does not reopen any earlier closed property.

## 55. Required implementation helpers

Expected bounded implementation helpers include conceptually:

```text
canonical JSON/hash/time helpers
trusted GitHub evidence pagination/currentness
admission/replay lock
Linux mount namespace/mountinfo verifier
held descriptor identity helpers
POSIX mode/uid/gid/xattr/ACL verifier
FSYNC_AFTER_FINAL_METADATA helper
single-worktree real-gitdir verifier
physical loose-main-ref verifier
physical primary-object-DB verifier
raw object parser/hasher
closed raw tree rewrite
closed raw commit writer/verifier
ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V2
raw Git index-v2 parser
FULL_SINGLE_FILE_INDEX_V1 verifier
CLOSED_FULL_INDEX_V2_REWRITE_V1 builder
ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1
main reflog prestate binder
DETERMINISTIC_MAIN_REFLOG_PROJECTION_V2
ALIAS_SAFE_WORKTREE_PROJECTION_V2
alias-safe ref CAS V3
outcome classifier
post-effect verifier
```

No helper may silently broaden a profile or normalize an unsupported prestate.

## 56. Documentation obligations

Authority documentation must state at minimum:

```text
current Human route = approve --decision-pr <N> only
direct legacy approve/promotion disabled
canonical effect ref = refs/heads/main
Git ref mutation = NONE
Git primary object mutation = NONE
Git real-index mutation = NONE
primary object store physically contained
new objects installed with renameat2(RENAME_NOREPLACE)
final security metadata precedes the file fsync barrier
index prestate = extension-free full index v2 only
split index unsupported
sharedindex.* forbidden
final index = deterministic raw v2 rewrite + alias-safe replacement
main reflog = deterministic Human-bound projection
V9 Human marker required
```

## 57. No new implementation authority

This brief is intentionally not an implementation approval.

```text
CLEAN BRIEF != IMPLEMENTATION AUTHORITY
REVIEW PASS != IMPLEMENTATION AUTHORITY
REVIEW PASS != HUMAN DECISION
IMPLEMENTATION GREEN != X1B CLOSED
X1B OPEN != V1 AUTHORITY
```

## 58. Next legal step

After this R4R9 brief is durably frozen as exactly one evidence artifact, STOP.

Next legal step:

```text
fresh Human authorization
-> one independent AK-CANON R4R9 implementation-brief review
```

That review must attack this document independently and may return PASS or NOT PASS.

It must not implement ScriptOps, create Human decision evidence, run a positive control, perform the canonical effect, recover state, merge, close X1B, authorize V1, release, deploy or tag.

## 59. R4R9 acceptance checklist for the future independent review

A PASS review must establish all of the following without inference from intent:

```text
PR #131 F001 metadata-durability blocker addressed
PR #131 F002 split-index/sharedindex blocker addressed
all prior blockers remain closed
FSYNC_AFTER_FINAL_METADATA ordering is exact for every created/replaced file
no authority-relevant link-count mutation after final object file fsync
RENAME_NOREPLACE behavior is exact/fail-closed
FULL_SINGLE_FILE_INDEX_V1 parser is complete and canonical
no Git canonical-index read pre-ref
no Git canonical-index writer at all
no sharedindex effect under success
final raw index bytes uniquely determined
index drift is detected before overwrite
post-ref failures never roll back main
all uncertainty states truthful
all Human evidence remains separate, current and exact
```

Any ambiguity is NOT PASS.

## 60. Final R4R9 invariant summary

```text
AI PROPOSES != HUMAN DECIDES

V9 HUMAN DECISION EVIDENCE
= separate trusted current GitHub Human review
  bound to exact V9 request + exact Human-presented material effect

V9 LOCAL EFFECT PREPARATION
= contained raw loose objects only
  installed by RENAME_NOREPLACE
  final metadata -> file fsync -> namespace -> dir fsync

V9 COMMITMENT
= exact descriptor-relative physical loose main-ref replacement
  final metadata -> file fsync -> rename -> refs/heads dir fsync

V9 POST-REF PROJECTIONS
= deterministic reflog
+ alias-safe scene/log materialization
+ deterministic full extension-free index-v2 replacement

SPLIT INDEX
= unsupported

sharedindex.*
= forbidden / no effect

GIT REF WRITER
= NONE

GIT PRIMARY OBJECT WRITER
= NONE

GIT REAL INDEX WRITER
= NONE

R4R9 BRIEF
= REVIEW TARGET ONLY
```
