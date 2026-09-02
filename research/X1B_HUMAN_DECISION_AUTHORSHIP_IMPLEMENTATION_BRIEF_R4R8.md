# X1B HUMAN DECISION AUTHORSHIP — CLEAN IMPLEMENTATION BRIEF R4R8

Status: `CLEAN R4R8 CORRECTIVE BRIEF / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-02`

## 1. Authority, purpose, and STOP boundary

This document is the self-contained successor to R4R7 after independent AK-CANON review PR #129 returned `NOT PASS`.

It preserves the accepted X1B corrective design and every R4R7 property not rejected by PR #129, while correcting exactly the two blockers frozen by that review:

1. R4R7 physically closed the reference store but did not bind the physical topology of the primary Git object database; a symlinked or redirected `.git/objects` could receive new blob/tree/commit writes outside the intended repository metadata boundary while logical object checks still passed;
2. R4R7 replaced `refs/heads/main` and the main reflog through temporary files but left the resulting security-relevant filesystem metadata under an unspecified “frozen supported mode”, allowing final permissions and related metadata to depend on implementation, umask, repository-sharing policy, or filesystem inheritance.

R4R8 therefore changes object preparation and metadata authority again.

New exact profiles:

```text
PHYSICAL_PRIMARY_OBJECT_DB_NO_ALIAS_V1
CLOSED_RAW_TREE_REWRITE_V1
ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V1
POSIX_MODE_ONLY_SECURITY_METADATA_V1
COMPLETE_LOCAL_OBJECT_STORE_V2
CRASH_DURABLE_OBJECT_AND_ALIAS_SAFE_REF_V3
ALIAS_SAFE_MAIN_REF_COMMITMENT_V4
REF_CAS_FIRST_ALIAS_SAFE_GIT_PLUMBING_V6
```

The material effect changes. All authority-critical schemas, request/review markers, admission identities, final-gate identities and records are therefore V8.

This document is an implementation brief only. It authorizes no ScriptOps source mutation, no Human decision PR/review, no live positive control, no canonical screenplay effect, no recovery, no merge, no X1B closure, no Agency Kernel v1, no release, deployment, or tag.

```text
R4R8 BRIEF != IMPLEMENTATION AUTHORITY
R4R8 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R8 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

After durable freeze of this brief, STOP. The next stage is a separately Human-authorized independent AK-CANON R4R8 implementation-brief review.

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

### 2.3 R4R7 predecessor

```text
FJ899/8 PR #128
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 6879b3f551a0eff674002509b3c31925ce639ac7
TREE = 0e515d1d121869e3ec2d437e630d67b24b5dc63f
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R7.md
BLOB = 01dbb04f7f238bebc3565f779d074ca3824e74ad
```

### 2.4 Binding R4R7 NOT-PASS review

```text
FJ899/8 PR #129
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 7ac626a9ab0b01eb07cf5ece1f444f3b0e23cb14
TREE = 714f48826e36634190fd275506ee5d29e6176dfd
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R7_AK_CANON_REVIEW.md
BLOB = 5af7e4cb6310666f544f8556c5242d4e0f8ec9d4
VERDICT = AK-CANON X1B R4R7 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #129 froze:

```text
X1B-R4R7-IBR-F001 — primary object database physical topology is not bound
X1B-R4R7-IBR-F002 — ref/reflog replacement metadata remains implicit
```

PR #129 also recorded that R4R7 addressed at brief level:

```text
X1B-R4R6-IBR-F001 physical files-ref topology
X1B-R4R6-IBR-F002 unbound update-ref reflog
```

and preserved prior configured-hook, fsync, lazy-fetch, replacement-ref, commit-encoding, hardlink/write-target-alias and freshness/supersession corrections.

`REVIEW FINDING != REPAIR AUTHORITY`; R4R8 exists only under fresh Human authorization for successor brief preparation.

## 3. Exact evidence-repository base

```text
FJ899/8 main
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

No history rewrite is part of R4R8.

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

## 5. Normative precedence and V8 migration

```text
R4R8 TEXT = CURRENT IMPLEMENTATION-BRIEF AUTHORITY
R4R7 / R4R6 / R4R5 / R4R4 / R4R3 / R4R2 / R4R1 / R4 / R3 / R2 / R1 = HISTORICAL INPUT ONLY
CORRECTIVE DESIGN PR #34 = HIGHER-LEVEL PROPERTY CONTRACT
```

R4R8 materially changes the local effect again:

```text
Git is no longer permitted to write new primary object-database objects
new blob/tree/commit objects are derived in memory and installed by fd-relative no-alias loose-object helpers
primary object database topology becomes authority-critical
security-relevant filesystem metadata becomes exact and non-ambient
core.sharedRepository and process umask can no longer select final effect permissions
```

Therefore:

```text
V7 REQUEST/REVIEW/ADMISSION/GATE != R4R8 AUTHORITY
V7 HUMAN REVIEW MARKER != V8 HUMAN DECISION
V8 EFFECT PROFILE REQUIRES FRESH V8 HUMAN-BOUND REQUEST
```

No V7 or earlier Human evidence may authorize a V8 effect.

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

No caller-controlled field may supply Human actor/result/rationale, request path/digest, task/scene/candidate/impact identities, canonical target/ref, physical Git-dir/ref/object topology, metadata policy, reflog semantics, effect type, material effect, raw-object profile, hook profile, durability profile, commitment profile, or effect commit metadata.

Defect-era Phase-6 `approve --scene ... --why ...`, direct legacy `approve --scene ...`, and direct legacy `scene-promote --to accepted` remain disabled and non-effect-capable.

## 9. Git/runtime/OS profile V8

Git semantic compatibility remains bounded to:

```text
2.55.0 <= parsed Git version < 2.56.0
object format = sha1
ref storage format = files
```

R4R8 narrows filesystem authority to a Linux/POSIX mode-only profile because the correction requires complete proof of path identity and security-relevant metadata.

Required runtime primitives:

```text
dir_fd relative open/mkdir/link/unlink/rename
O_NOFOLLOW
O_DIRECTORY
O_EXCL
O_CLOEXEC
fstat/lstat
fsync regular file
fsync directory
atomic same-directory rename
linkat-equivalent no-replace hard-link creation
listxattr
POSIX ACL inspection capability
/proc/self/ns/mnt
/proc/self/mountinfo
```

A platform lacking any required proof primitive is `BLOCKED`.

Successful `fsync` is trusted only within the same bounded OS/filesystem contract used by R4R7: hardware/firmware/filesystems that falsely report durable completion are outside the claim.

The mount namespace identity must remain stable through object preparation, ref commitment and post-effect verification.

## 10. POSIX_MODE_ONLY_SECURITY_METADATA_V1

R4R8 makes security-relevant filesystem metadata explicit.

This profile intentionally supports only repositories where authority-critical targets use POSIX mode/owner/group semantics with no additional inherited or attached security metadata.

Required for every authority-critical file or directory named below:

```text
owner uid = exact execution effective uid bound at request creation
group gid = exact execution effective gid bound at request creation
no setuid bit
no setgid bit except where a directory is explicitly declared unsupported and therefore BLOCKED
no sticky bit
listxattr = empty
POSIX access ACL = equivalent to ordinary mode bits only
POSIX default ACL on writable authority-critical directories = absent
security labels / capabilities / arbitrary extended attributes = absent
```

If extended-attribute or ACL inspection is unsupported, ambiguous or reports any non-mode metadata, R4R8 is `BLOCKED`.

R4R8 explicitly does not claim to preserve arbitrary ACL/xattr/MAC-label semantics. Those environments require a separately reviewed profile.

Kernel-assigned inode numbers and ctime are operational metadata, not Human authority fields. They may change when an inode is replaced. Their exclusion is explicit, not implicit.

The following exact numeric final modes are frozen:

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
ref/reflog/worktree/object temporary files         = 0600 before explicit final chmod
```

Existing authority-critical paths whose required mode is not exact are `BLOCKED`; R4R8 does not normalize an unapproved prestate merely to make it eligible.

The effect process sets exactly:

```text
umask = 0077
```

before any authority-critical temporary file is created. It must execute in a dedicated process and no effect-path code may change the umask afterward.

Every final target mode is set explicitly with `fchmod` before installation or, for the real index, verified and restored to exact `0644` before complete success. Final permission truth never depends on umask.

## 11. Repository-sharing configuration closure

At request creation, admission, FinalEffectGateV8, pre-object-install, pre-ref-CAS and post-effect, reject any effective repository/worktree value for:

```text
core.sharedRepository
core.sharedrepository
```

Config key matching follows Git's case-insensitive key rules rather than literal-case assumptions.

Every authority-critical Git subprocess receives command-scope:

```text
-c core.sharedRepository=false
```

This is defense in depth. Ambient shared-repository policy cannot widen modes for index or other Git-created temporary files.

## 12. SINGLE_WORKTREE_REAL_GITDIR_V1 preserved

The R4R7 single-worktree profile remains mandatory:

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

R4R8 additionally requires root and `.git` to satisfy `POSIX_MODE_ONLY_SECURITY_METADATA_V1`.

## 13. PHYSICAL_PRIMARY_OBJECT_DB_NO_ALIAS_V1

The primary object store is authority-critical physical state.

Under the held `.git` descriptor, require:

```text
objects = real directory
objects not symlink/reparse redirect
objects st_dev/st_ino stable
objects owner/group/mode exact under POSIX_MODE_ONLY_SECURITY_METADATA_V1
GIT_OBJECT_DIRECTORY absent from caller environment
GIT_ALTERNATE_OBJECT_DIRECTORIES absent from caller environment
objects/info/alternates absent
GIT_COMMON_DIR not redirecting object storage
```

The process opens and retains `.git/objects` with descriptor-relative no-follow directory semantics.

If `objects/info` exists it must be a real no-symlink directory satisfying exact metadata.

If `objects/pack` exists it must be a real no-symlink directory satisfying exact metadata.

Every authority-relevant pack/index/bitmap/midx file read from `objects/pack` must be a regular non-symlink single-link file with owner/group under the V8 metadata profile. `.promisor` sidecars remain forbidden.

No path under `.git/objects` that is read or written for authority may traverse a symlink, hardlink alias, reparse redirect or unreviewed mount boundary.

## 14. Mount containment profile

R4R8 parses `/proc/self/mountinfo` and binds the exact mount-namespace identity from `/proc/self/ns/mnt`.

Required:

```text
repository root and .git are in the same mount namespace throughout effect
.git/objects is on the same mount ID as .git
.git/refs is on the same mount ID as .git
.git/logs is on the same mount ID as .git
no separate mountpoint exists at or below .git/objects
no separate mountpoint exists at or below .git/refs
no separate mountpoint exists at or below .git/logs
```

A bind mount, nested mount or mount-namespace change affecting any authority-critical Git metadata path is `BLOCKED` before ref commitment or an explicit uncertainty state if discovered after a possible commitment.

`same st_dev` alone is not accepted as proof of same mount.

## 15. COMPLETE_LOCAL_OBJECT_STORE_V2

V2 includes every R4R7 V1 rule and the new physical rules.

Reject:

```text
shallow repository
grafts
replacement refs
partial clone
promisor config
promisor sidecars
lazy fetch requirement
objects/info/alternates
caller alternate/object-directory injection
external common object directory
symlinked primary objects directory
nested/bind-mounted primary object store
symlinked authority-relevant loose fanout
symlinked or hardlinked authority-relevant loose object file
symlinked pack/info directories
unsupported pack metadata topology
```

No fetch, deepen, object repair or normalization is authorized.

## 16. Raw SHA-1 object identity preserved

`NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2` remains mandatory.

The request base, parent tree and all prestate Git object authority are read with:

```text
GIT_NO_REPLACE_OBJECTS=1
GIT_NO_LAZY_FETCH=1
--no-replace-objects
--no-lazy-fetch
```

Missing local objects fail closed.

## 17. Why Git is no longer the primary object writer

Current Git stores loose objects beneath `$GIT_DIR/objects/<two-hex>/<remaining-hex>` and ordinary object-writing code resolves those pathnames through the primary object-directory path.

R4R8 does not attempt to make pathname-based Git object writes alias-safe by repeated pre/post checks.

Instead, during the V8 effect path the following Git writes are forbidden:

```text
git hash-object -w
git write-tree
git mktree when it writes an object
git commit-tree
any Git command that creates a new blob/tree/commit in the primary ODB
any Git command that repacks, prunes, migrates or rewrites the ODB
```

Read-only object inspection remains permitted under the sanitized Git profile.

## 18. CLOSED_RAW_TREE_REWRITE_V1

The exact V8 tree is derived in memory from raw parent-tree bytes.

The helper:

```text
reads exact raw parent tree objects locally with no replacement/lazy fetch
parses each raw tree entry as mode SP raw-name NUL raw-20-byte-SHA1
rejects malformed, duplicate, noncanonical or unsorted tree entries
uses Git 2.55 tree-name ordering semantics including directory slash ordering
rewrites only the two exact target paths
uses mode 100644 for both tracked leaves
preserves every unrelated raw tree entry byte-for-byte at the semantic entry level
recursively reconstructs only affected ancestor tree objects
computes each tree OID as SHA1("tree " + decimal_length + NUL + exact_tree_payload)
```

The only changed tracked paths are:

```text
scenes/<scene_id>.fountain
.scriptops/decision-log.ndjson
```

No filter, checkout conversion, working-tree normalization, pathspec expansion or index-driven tree construction is allowed to select tree content.

After installation, read-only Git plumbing independently verifies the exact resulting tree and two-path delta.

## 19. CLOSED_RAW_COMMIT_OBJECT_V1 preserved without Git write

The effect commit remains exact raw bytes with only:

```text
tree
parent
author
committer
```

headers and exact message:

```text
scriptops x1b: accept <scene_id>\n
```

No encoding header, gpgsig, mergetag, extra parent or unknown header is permitted.

R4R8 computes the commit SHA-1 in process and may cross-check it with read-only/non-writing `git hash-object -t commit --stdin`, but no `-w` or equivalent object write is permitted.

## 20. Canonical raw object bytes

For each new object type `T` and exact payload bytes `P`:

```text
canonical_object_bytes = ASCII(T) + SP + ASCII(decimal(len(P))) + NUL + P
object_oid = lowercase_hex(SHA1(canonical_object_bytes))
```

Supported new object types in the effect are exactly:

```text
blob
tree
commit
```

The object type, payload length, payload bytes and OID are authority-critical.

Loose-object zlib compression is storage representation, not Git object identity. R4R8 explicitly treats different valid zlib encodings as equivalent only if they inflate to the exact canonical object bytes and no trailing garbage remains. This representation equivalence is deliberate and non-authority-semantic, not an implicit security choice.

The implementation must nevertheless use one fixed production compression helper and record its runtime/library identity in execution evidence for reproducibility.

## 21. ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V1 — fanout directory

For every required OID, derive exact lowercase two-hex fanout prefix.

Using the held `.git/objects` descriptor:

```text
if fanout directory exists:
    open with O_DIRECTORY | O_NOFOLLOW | O_CLOEXEC relative to objects fd
    require real directory
    require exact uid/gid/mode 0755
    require no xattrs/default ACL
    require same mount ID as objects
else:
    mkdir relative to held objects fd with initial mode 0700
    open no-follow directory fd
    fchmod to exact 0755
    verify uid/gid/xattr/ACL/mount identity
    fsync new fanout directory
    fsync held objects directory
```

Retain the fanout descriptor until installation and post-write verification for every object assigned to it are complete.

Reopening `<objects>/<prefix>` from the retained objects fd must resolve to the same `st_dev/st_ino` and mount identity immediately before and after each object installation.

## 22. ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V1 — existing final leaf

The final object leaf is the remaining 38 lowercase hex characters.

If the final leaf already exists:

```text
open relative to held fanout fd with O_NOFOLLOW
require regular file
require st_nlink = 1
require same mount ID
require no xattrs/ACL beyond mode-only profile
inflate exact bytes with no trailing garbage
require exact canonical type/length/payload
require SHA1 = path OID
```

An existing symlink, hardlink (`st_nlink > 1`), device, FIFO, socket, unsupported metadata or malformed object is `BLOCKED`.

R4R8 never overwrites an existing object pathname.

## 23. ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V1 — new final leaf

If the final leaf is absent:

1. Create a fresh unpredictable temp leaf inside the held fanout directory with descriptor-relative `O_CREAT | O_EXCL | O_NOFOLLOW | O_CLOEXEC`, mode `0600` under process umask `0077`.
2. Write one complete valid zlib stream inflating exactly to the canonical object bytes.
3. `fsync(temp_fd)`.
4. Re-read/inflate from the temp fd and verify exact type/length/payload/OID.
5. `fchmod(temp_fd, 0444)` and verify uid/gid/mode/xattr/ACL exact.
6. Install without replacement by descriptor-relative same-directory `linkat`/equivalent from temp leaf to exact final OID leaf.
7. If final creation reports `EEXIST`, do not replace it; open and verify the concurrently created final object under the existing-leaf rule.
8. `fsync(fanout_fd)` after final-name creation.
9. Unlink the temp leaf.
10. `fsync(fanout_fd)` after temp removal.
11. Reopen final leaf no-follow and require regular single-link mode `0444`, exact canonical object content and exact OID.

The temporary hard-link count of two between link creation and temp unlink is internal to the atomic install sequence. Complete success requires final `st_nlink = 1`.

## 24. New-object closure V8

After Human review admission and deterministic decision-record creation, R4R8 derives the exact effect commit and exact set:

```text
new_object_closure = every blob/tree/commit reachable from effect commit that is not reachable from raw request-base parent
```

Every member is represented by an exact canonical object tuple:

```text
(type, payload_length, payload_sha256, oid)
```

Every member must have an exact physically contained loose-object representation under `ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V1` before ref commitment, even if an equivalent object also exists in a pack.

This deliberately creates a contained loose copy when an effect-critical object existed only in packed form.

The loose copy is part of the V8 preparation profile and is Human-bound by rule.

## 25. Object preparation side-effect truth

Object installation occurs before ref commitment.

Therefore V8 does not say that every pre-commit failure has “no filesystem effect”. A denied/blocked execution may have already installed exact unreferenced loose objects or newly required empty fanout directories.

These preparations are not a Human-attributed scene acceptance because canonical `refs/heads/main` remains unchanged, but their existence must be reported truthfully.

Outcome reporting distinguishes:

```text
BLOCKED_PRE_COMMIT_NO_OBJECT_PREP
BLOCKED_PRE_COMMIT_OBJECT_PREPARED
OBJECT_STORE_TOPOLOGY_UNCERTAIN
```

No cleanup routine may delete a pre-existing object or guess which concurrently created object is safe to remove.

## 26. PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1 preserved

The R4R7 physical main-ref profile remains mandatory:

```text
HEAD = regular non-symlink file with exact bytes "ref: refs/heads/main\n"
refs = real directory
refs/heads = real directory
refs/heads/main = direct regular non-symlink single-link loose ref
packed-refs contains no refs/heads/main entry
main.lock absent before acquisition
core.preferSymlinkRefs absent/false
```

R4R8 adds exact V8 metadata requirements:

```text
refs = 0755
refs/heads = 0755
HEAD = 0644
refs/heads/main = 0644
uid/gid exact execution uid/gid
no xattrs/ACL beyond mode bits
same mount ID as .git
```

A main-ref prestate that does not already satisfy this profile is `BLOCKED`.

## 27. ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V2

The R4R7 descriptor-relative ref CAS is preserved and metadata is now exact.

Acquire `main.lock` under held `refs/heads` fd with:

```text
O_WRONLY | O_CREAT | O_EXCL | O_NOFOLLOW | O_CLOEXEC
initial mode 0600
```

After lock acquisition and old-value/topology reproof:

```text
write exact effect SHA + LF
fsync lock fd
re-read exact bytes
fchmod lock fd to 0644
verify uid/gid = request-bound execution uid/gid
verify xattrs empty / mode-only ACL
re-read old main = exact request base + LF
revalidate packed-main absence
revalidate canonical hierarchy/mount identities
```

Only then perform same-directory descriptor-relative atomic rename:

```text
main.lock -> main
```

Then:

```text
fsync held refs/heads directory
reopen main O_NOFOLLOW
verify regular single-link 0644 exact effect SHA + LF
verify uid/gid/xattr/ACL exact
verify canonical root -> .git -> refs -> heads hierarchy still resolves to held identities
```

No final ref permissions depend on umask or `core.sharedRepository`.

## 28. Main reflog metadata closure

`DETERMINISTIC_MAIN_REFLOG_PROJECTION_V1` is preserved with V8 metadata.

Required parent directories:

```text
.git/logs = real 0755 directory
.git/logs/refs = real 0755 directory
.git/logs/refs/heads = real 0755 directory
same uid/gid as execution profile
no xattrs/default ACL
same mount ID as .git
```

`logs/refs/heads/main` may be absent or an existing regular non-symlink single-link `0644` file with empty xattrs/mode-only ACL.

Any other metadata or topology is `BLOCKED` before ref commitment.

Projection temp file is created `0600`, fully written and fsynced, then explicitly `fchmod(0644)` and metadata-verified before atomic descriptor-relative rename and parent-directory fsync.

## 29. Exact V8 reflog line

After exact effect commit SHA `C` is known and only after durable physical main-ref commitment, construct exactly:

```text
<request_base_sha> SP <C> SP ScriptOps X1B <scriptops-x1b@local.invalid> SP <request_epoch> SP +0000 TAB scriptops x1b: accept <scene_id> LF
```

No execution wall clock, ambient identity, locale, timezone or `GIT_REFLOG_ACTION` contributes.

New reflog bytes are exactly:

```text
existing exact Human-bound bytes + exact V8 line
```

or, when absent:

```text
exact V8 line
```

If the prestate changes after ref commitment, do not overwrite it; return committed recovery state.

## 30. Worktree and real-index metadata closure

R4R8 applies the same mode-only security profile to the post-ref projections to avoid moving the metadata ambiguity to the next write.

Canonical scene and decision-log filesystem materialization:

```text
final mode = 0644
uid/gid = request-bound execution uid/gid
xattrs = empty
ACL = mode-only
parent directories real/no-symlink/no unexpected mount
```

The real `.git/index` prestate must already be regular, single-link, mode `0644`, exact uid/gid, empty xattrs/mode-only ACL.

Git may update the real index after ref commitment using bounded hook-disabled plumbing, but complete success requires the resulting `.git/index` metadata to be explicitly restored/verified as the exact V8 profile before zero exit.

If restoring/verifying index metadata fails after ref commitment, return `DURABLY_REF_COMMITTED_RECOVERY_REQUIRED` rather than complete success.

## 31. PresentedMaterialEffectV8

Closed schema:

```text
PresentedMaterialEffectV8 = {
  "schema_version": "scriptops-x1b-presented-material-effect/v8",
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
    "filesystem_mode_after": "0644"
  },
  "decision_log_effect": {
    "target_path": ".scriptops/decision-log.ndjson",
    "append_count": 1,
    "record_schema_version": "scriptops-x1b-decision-record/v8",
    "record_result": "REF_COMMITTED",
    "append_semantics": "EXACT_PRIOR_BYTES_PLUS_ONE_CANONICAL_RECORD_PLUS_LF",
    "git_mode_after": "100644",
    "filesystem_mode_after": "0644"
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
    "object_install_profile": "ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V1",
    "metadata_profile": "POSIX_MODE_ONLY_SECURITY_METADATA_V1",
    "raw_object_profile": "NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2",
    "hook_profile": "NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1",
    "commit_object_profile": "CLOSED_RAW_COMMIT_OBJECT_V1",
    "ref_cas_profile": "ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V2",
    "durability_profile": "CRASH_DURABLE_OBJECT_AND_ALIAS_SAFE_REF_V3",
    "success_commitment_profile": "ALIAS_SAFE_MAIN_REF_COMMITMENT_V4",
    "effect_transport_profile": "REF_CAS_FIRST_ALIAS_SAFE_GIT_PLUMBING_V6",
    "git_ref_mutating_command": "NONE",
    "git_primary_object_mutating_command": "NONE",
    "pre_ref_object_preparation": "EXACT_CONTAINED_LOOSE_OBJECTS_MAY_BE_DURABLY_INSTALLED_BEFORE_REF_CAS",
    "reflog_effect": {
      "target_git_metadata_path": "logs/refs/heads/main",
      "before": <MainReflogPreStateV2>,
      "projection_profile": "DETERMINISTIC_MAIN_REFLOG_PROJECTION_V1",
      "filesystem_mode_after": "0644",
      "entry_old_oid_source": "REQUEST_BASE_SHA",
      "entry_new_oid_source": "EXACT_DERIVED_EFFECT_COMMIT_SHA",
      "entry_committer": "ScriptOps X1B <scriptops-x1b@local.invalid>",
      "entry_time_source": "request_created_at",
      "entry_timezone": "+0000",
      "entry_message": "scriptops x1b: accept <exact scene_id>",
      "append_count": 1
    },
    "exact_changed_paths": [
      "scenes/<scene_id>.fountain",
      ".scriptops/decision-log.ndjson"
    ]
  },
  "file_identity_profile": "SINGLE_LINK_ALIAS_SAFE_REPOSITORY_TARGETS_V1"
}
```

## 32. Canonical and metadata prestates

Existing canonical scene prestate remains:

```text
CanonicalPreStateV1 = {
  "exists": <true|false>,
  "file_sha256": <64 lowercase hex or null>
}
```

R4R8 extends reflog prestate:

```text
MainReflogPreStateV2 = {
  "exists": <true|false>,
  "file_sha256": <64 lowercase hex or null>,
  "byte_length": <nonnegative integer>,
  "filesystem_mode": <"0644" or null>,
  "uid": <exact uid or null>,
  "gid": <exact gid or null>,
  "xattrs": <[] or null>,
  "acl": <"MODE_BITS_ONLY" or null>
}
```

The request also binds exact physical identities for:

```text
repository root
.git
.git/objects
.git/refs
.git/refs/heads
.git/logs
.git/logs/refs
.git/logs/refs/heads
.git/index
refs/heads/main
```

using closed records containing path role, `st_dev`, `st_ino`, mount ID, file type, mode, uid, gid, nlink where meaningful and metadata-profile result.

Directory identity is revalidated rather than embedded as a promise that inode numbers never change for unrelated reasons.

## 33. HumanDecisionRequestBindingV8

```text
HumanDecisionRequestBindingV8 = {
  "schema_version": "scriptops-x1b-human-decision-request/v8",
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
  "physical_git_metadata_prestate_digest": <sha256 of closed V8 physical-prestate record>,
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect": <PresentedMaterialEffectV8>
}
```

`request_digest = sha256_canonical(binding)` and `decision_request_id = "x1b:" + request_digest`.

## 34. Decision proposal PR and V8 Human review

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
X1B-HUMAN-DECISION-V8
decision_request_id=<exact x1b:<request_digest>>
decision_request_sha256=<exact request_digest>
why=<Human rationale>
```

V7 or earlier review markers are invalid for V8.

## 35. Trusted GitHub evidence and freshness preserved

Public exact-origin GitHub evidence transport, no proxy/redirect/auth fallback, complete review pagination, current-head binding, duplicate ambiguity, active CHANGES_REQUESTED handling, no-latest-wins semantics, exact proposal envelope, replay lock and freshness/supersession rules remain as R4R7 with V8 schema names.

A selected decision remains active only while every exact PR/request/review/local-ref/raw-object/object-store/physical-path/metadata/reflog/applicability predicate remains true.

```text
NO WALL-CLOCK TTL
AGE ALONE != STALE
```

## 36. Hook closure preserved

`NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1` remains mandatory.

Every authority-critical Git command retains:

```text
verified private empty core.hooksPath
hook.reference-transaction.enabled=false
hook.post-index-change.enabled=false
ambient hook.* census with includes/origin/scope
```

No Git ref-mutating command exists in the V8 effect path.

No Git primary-object-writing command exists in the V8 effect path.

Git index writing remains post-ref and `post-index-change` remains disabled.

## 37. Sanitized Git subprocess profile V8

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

Caller Git config injection, object-directory injection, alternates, executable-path, SSH, askpass, loader and replacement variables remain stripped.

Global options:

```text
--no-replace-objects
--no-lazy-fetch
```

Command-scope controls include:

```text
-c core.hooksPath=<verified empty private hook dir>
-c hook.reference-transaction.enabled=false
-c hook.post-index-change.enabled=false
-c core.fsmonitor=false
-c commit.gpgSign=false
-c credential.helper=
-c core.sharedRepository=false
-c core.fsync=all
-c core.fsyncMethod=fsync
```

`core.fsync` remains relevant to the post-ref real-index Git write. New primary object installation uses explicit OS-level file and directory fsyncs instead of Git object fsync policy.

## 38. X1BDecisionRecordV8

```text
X1BDecisionRecordV8 = {
  "schema_version": "scriptops-x1b-decision-record/v8",
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
  "canonical_before": <CanonicalPreStateV1>,
  "canonical_after_file_sha256": <exact digest>,
  "effect_type": "ACCEPT_SCENE_CANDIDATE",
  "presented_material_effect_digest": <exact digest>,
  "gitdir_profile": "SINGLE_WORKTREE_REAL_GITDIR_V1",
  "physical_main_ref_profile": "PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1",
  "physical_object_db_profile": "PHYSICAL_PRIMARY_OBJECT_DB_NO_ALIAS_V1",
  "object_store_profile": "COMPLETE_LOCAL_OBJECT_STORE_V2",
  "tree_construction_profile": "CLOSED_RAW_TREE_REWRITE_V1",
  "object_install_profile": "ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V1",
  "metadata_profile": "POSIX_MODE_ONLY_SECURITY_METADATA_V1",
  "raw_object_profile": "NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2",
  "hook_profile": "NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1",
  "commit_object_profile": "CLOSED_RAW_COMMIT_OBJECT_V1",
  "ref_cas_profile": "ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V2",
  "reflog_projection_profile": "DETERMINISTIC_MAIN_REFLOG_PROJECTION_V1",
  "durability_profile": "CRASH_DURABLE_OBJECT_AND_ALIAS_SAFE_REF_V3",
  "success_commitment_profile": "ALIAS_SAFE_MAIN_REF_COMMITMENT_V4",
  "canonical_instance_scope": "LOCAL_PHYSICAL_MAIN_REF_OBJECT_DB_WORKTREE_DECISION_LOG_REFLOG_V8"
}
```

The record says `REF_COMMITTED`, not generic success. Object preparation occurs before the record becomes reachable from main; reflog/worktree/index completion remains post-ref truth.

## 39. FinalEffectGateV8

Immediately before decision-record/object derivation, while the same-worktree exclusive X1B lock is held, freshly validate:

```text
exact V8 PR/request/review envelope
Human currentness/conflicts
CompleteReviewSetV8 digest
raw logical main SHA = request base
SINGLE_WORKTREE_REAL_GITDIR_V1
PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1
PHYSICAL_PRIMARY_OBJECT_DB_NO_ALIAS_V1
COMPLETE_LOCAL_OBJECT_STORE_V2
POSIX_MODE_ONLY_SECURITY_METADATA_V1
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
PresentedMaterialEffectV8
replay state
real index tree = raw parent tree
real index metadata = exact V8 profile
alias-safe worktree target preconditions
verified empty hook directory
system Git/OS proof primitives
```

FinalEffectGateV8 remains in-memory one-shot state.

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
```

## 40. Exact local effect sequence V8

With the X1B lock held after FinalEffectGateV8:

```text
A. re-prove raw-object, complete-local-store, physical Git-dir/ref/object-store, metadata and reflog-prestate profiles

B. construct X1BDecisionRecordV8 bytes in memory

C. construct exact accepted-scene blob payload and exact decision-log blob payload in memory
   compute canonical blob object bytes and OIDs

D. parse raw parent tree(s) and execute CLOSED_RAW_TREE_REWRITE_V1
   derive exact affected subtree/root tree payloads and OIDs
   prove exact two-path semantic delta

E. construct exact CLOSED_RAW_COMMIT_OBJECT_V1 in memory
   compute exact effect commit SHA

F. derive exact new_object_closure tuples

G. install every closure member as physically contained loose object through ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V1
   no Git object-writing command
   verify each final no-follow object leaf and canonical hierarchy

H. cross-check all installed objects with read-only no-replace/no-lazy Git plumbing
   verify raw commit/tree and exact two-path diff

I. final pre-ref checks:
   physical main exact old SHA
   packed main absent
   ref descriptor hierarchy exact
   physical object-store hierarchy exact
   every closure object physically contained/exact
   reflog prestate exact
   security metadata exact
   mount namespace/mount IDs exact
   hook census empty
   real index still parent tree and metadata exact

J. acquire main.lock descriptor-relative O_EXCL/O_NOFOLLOW
   repeat old-value/topology/metadata proof

K. write exact effect SHA + LF
   fsync lock
   fchmod exact 0644
   verify metadata
   final old-main proof

L. descriptor-relative atomic rename main.lock -> main
   fsync held refs/heads directory
   classify physical ref result

M. only after normal durable ref commitment, construct/materialize exact deterministic main reflog bytes with final metadata 0644

N. materialize canonical scene bytes with final metadata 0644

O. materialize canonical decision-log bytes with final metadata 0644

P. update real index to exact committed new_tree under bounded hook-disabled Git plumbing
   restore/verify exact index security metadata 0644

Q. verify physical ref, logical ref, raw commit/tree/object closure, physical object-store containment, reflog, worktree, real index, mount identity and all security metadata

R. release X1B lock only after final outcome class is determined
```

No canonical worktree, decision-log, reflog or real-index mutation occurs before physical main-ref commitment.

Exact unreferenced loose object preparation may occur before ref commitment and is reported as such.

## 41. CRASH_DURABLE_OBJECT_AND_ALIAS_SAFE_REF_V3

Normal durable object preparation requires for every newly installed loose object:

```text
temp file full write
file fsync
exact content reread
explicit final mode 0444
no-replace final-name link creation or exact existing-object verification
fanout directory fsync
final no-follow single-link reread
canonical objects/fanout path identity revalidation
```

New fanout creation additionally requires:

```text
fanout directory fsync
objects directory fsync
```

Normal durable ref commitment then requires:

```text
main.lock file fsync
exact mode/uid/gid/xattr/ACL proof
atomic same-directory rename
refs/heads directory fsync
exact physical main reread
stable canonical hierarchy proof
```

Post-ref reflog/worktree/index projections remain prerequisites for complete zero exit, not prerequisites for truthful `REF_COMMITTED` record scope.

## 42. Outcome classes V8

Implementation must distinguish at least:

```text
DENIED
BLOCKED_PRE_COMMIT_NO_OBJECT_PREP
BLOCKED_PRE_COMMIT_OBJECT_PREPARED
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
  admission/final gate denies before effect preparation
  main remains old SHA

BLOCKED_PRE_COMMIT_NO_OBJECT_PREP:
  main remains old SHA
  no new V8 closure object was durably installed
  no canonical worktree/index/reflog effect

BLOCKED_PRE_COMMIT_OBJECT_PREPARED:
  main remains old SHA
  one or more exact contained unreferenced loose closure objects or fanout directories may remain
  no canonical worktree/index/reflog effect
  no V8 record reachable from canonical main

OBJECT_STORE_TOPOLOGY_UNCERTAIN:
  object preparation may have written through a retained directory identity whose canonical-path relationship became uncertain
  main remains old SHA unless separately proven otherwise
  no acceptance-success claim
  preserve evidence

REF_COMMITTED_DURABILITY_UNCERTAIN:
  physical main visibly equals effect SHA
  ref-file/directory durability completion not proven
  no complete-success claim
  no rollback

REF_COMMITTED_TOPOLOGY_UNCERTAIN:
  a descriptor-relative ref write may have committed in held ref directory but canonical hierarchy identity is not proven
  no success/no-effect claim
  preserve evidence

COMMITMENT_STATE_UNKNOWN:
  ref outcome cannot be proven
  preserve evidence
  no rollback

DURABLY_REF_COMMITTED_RECOVERY_REQUIRED:
  physical canonical main durably equals exact effect SHA
  exact contained object truth is proven
  one or more reflog/worktree/index/metadata projections are incomplete or unproven
  no history rewrite

DURABLY_REF_COMMITTED_COMPLETE:
  durable physically contained object closure
  durable physical main commitment
  exact deterministic reflog
  exact worktree scene and decision log
  exact real index
  exact V8 security metadata and mount/path truth
```

User-visible wording must not collapse any uncertainty/preparation/recovery state into either “no effect” or “complete success”.

## 43. Zero-exit post-effect truth

Zero exit requires all:

```text
repository root/.git/objects/refs/logs physical hierarchies exact
mount namespace identity exact
no nested critical Git-metadata mount
HEAD exact ref: refs/heads/main LF
physical loose main regular single-link 0644 no-symlink
physical main bytes = expected effect SHA + LF
packed-refs has no main entry
logical no-replace/no-lazy HEAD/main = expected effect SHA
Git version/ref format exact
zero refs/replace
COMPLETE_LOCAL_OBJECT_STORE_V2
all new_object_closure members physically contained as exact loose regular single-link objects
new loose object modes = 0444
object/fanout metadata exact
raw effect commit exact
one parent = request base
raw tree exact new_tree
raw changed set exactly two tracked paths
tracked modes 100644
main reflog bytes = exact Human-bound prestate + exact deterministic V8 line
main reflog mode/security metadata exact 0644
canonical filesystem bytes exact 0644 metadata
candidate source unchanged
exactly one V8 decision record line in committed tree/filesystem
record result = REF_COMMITTED
real index tree = raw HEAD tree
real index metadata exact 0644
worktree clean relative to raw HEAD
hook census empty/private hook dir exact
core.sharedRepository ambient absent/false
X1B lock held until verification complete
```

`GREEN COMMAND EXIT != POST-EFFECT TRUTH`.

## 44. Object-store physical regression suite

Mandatory tests include:

```text
.git/objects symlink -> outside directory
.git/objects bind mount -> outside directory
objects/info symlink
objects/pack symlink
loose two-hex fanout symlink -> outside directory
loose fanout replaced after gate before object install
loose fanout replaced during multi-object install
existing effect-critical loose object symlink
existing effect-critical loose object hardlink nlink > 1
existing effect-critical loose object malformed zlib
existing effect-critical loose object correct path but wrong canonical content
object only in pack, requiring contained loose copy
packed parent-object read from regular contained pack
pack file symlink/hardlink alias
mount namespace changes after object install before ref CAS
caller GIT_OBJECT_DIRECTORY
caller GIT_ALTERNATE_OBJECT_DIRECTORIES
objects/info/alternates
```

The exact PR #129 `.git/objects -> outside` counterexample must be reproduced and rejected before any Human-attributed ref commitment.

No Git object-writing command may be reachable in the V8 effect path.

## 45. Metadata regression suite

Mandatory tests include:

```text
main ref mode 0600 instead of 0644
main ref mode 0664/0666 instead of 0644
reflog mode mismatch
index mode mismatch
critical directory group/other writable mode
uid mismatch
gid mismatch
setgid/sticky critical directory
ref/reflog/object/worktree xattr present
POSIX ACL broader than mode bits
default ACL on writable critical parent
SELinux/security label or file capability xattr present
process caller umask 0000
process caller umask 0077
local core.sharedRepository=group
local core.sharedRepository=0660
included/worktree sharedRepository setting
main.lock initial 0600 then exact fchmod 0644
reflog temp initial 0600 then exact fchmod 0644
object temp initial 0600 then exact fchmod 0444
post-ref real-index metadata restoration failure
```

Expected behavior:

```text
unsupported/mismatched prestate => DENIED/BLOCKED before Human-attributed commitment
caller umask cannot change final modes
core.sharedRepository cannot change final modes
post-ref metadata failure => recovery-required, never complete success
```

## 46. Tree/object construction regression suite

Mandatory tests include:

```text
parent raw tree malformed
noncanonical tree ordering
duplicate raw tree entry
target path absent/present variants
nested target ancestor replacement
file-vs-directory collision
non-100644 target mode attempt
extra changed path
filter configuration present
attributes that would alter working-tree conversion
hash-object without -w cross-check mismatch
attempted hash-object -w
attempted write-tree
attempted commit-tree
raw commit unknown header
raw commit encoding/gpgsig/mergetag/extra parent
```

The production derivation must not rely on index filters or working-tree conversion to define accepted Git object bytes.

## 47. Ref/reflog regression suites preserved

All R4R7 physical-ref and reflog tests remain mandatory, including:

```text
real main symlink to another ref
main symlink outside
refs parent symlink
packed main
main hardlink
main.lock preexists
parent substitution before/after lock
post-rename topology uncertainty
reflog symlink/hardlink/parent symlink
reflog prestate drift before ref
reflog drift after ref before projection
ambient user.name/user.email
ambient GIT_COMMITTER_*
ambient GIT_REFLOG_ACTION
core.logAllRefUpdates true/false/always
```

No Git ref-mutating command may run.

The only permitted reflog change is the exact V8 deterministic projection with exact V8 metadata.

## 48. Durability/fault suite V8

Mandatory fault points include:

```text
fanout mkdir failure
fanout fsync failure
object temp create/write/fsync failure
object content verification failure
object final link failure
concurrent EEXIST final-object collision
object fanout directory fsync failure
object topology changes after one or more objects installed
mount namespace change during object preparation
main.lock acquisition/write/fsync failure
main metadata fchmod/verification failure
old main changes while lock held
ref rename failure before replacement
ambiguous rename result
refs/heads directory fsync failure
kill immediately before/after ref rename
reflog temp write/fsync/chmod/rename/dir-fsync failure
canonical scene projection failure
canonical decision-log projection failure
real-index write failure
real-index metadata restoration failure
post-effect object/ref topology verification failure
```

No visible/possible main-ref commitment may be silently rewritten.

## 49. Prior security regression suites remain mandatory

Preserve all earlier mandatory suites for:

```text
configured and traditional hooks
filters/helpers/config injection
lazy fetch/partial/promisor state
replacement refs/grafts/shallow state
candidate/impact substitution
hardlink/symlink worktree targets
freshness/supersession/replay
Human-authorship attacks
legacy/defect acceptance routes
```

## 50. Trusted-origin claim

For this exact bounded V8 profile only:

```text
manual Human APPROVE by litrgratis-pixel
+
exact public GitHub evidence
+
exact V8 request/PR/review/effect binding
+
independent admission
+
fresh FinalEffectGateV8
+
NO_REPLACE + NO_LAZY_FETCH raw SHA-1 semantics
+
COMPLETE_LOCAL_OBJECT_STORE_V2
+
PHYSICAL_PRIMARY_OBJECT_DB_NO_ALIAS_V1
+
CLOSED_RAW_TREE_REWRITE_V1
+
ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V1
+
POSIX_MODE_ONLY_SECURITY_METADATA_V1
+
NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1
+
SINGLE_WORKTREE_REAL_GITDIR_V1
+
PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1
+
CLOSED_RAW_COMMIT_OBJECT_V1
+
ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V2
+
DETERMINISTIC_MAIN_REFLOG_PROJECTION_V1
+
CRASH_DURABLE_OBJECT_AND_ALIAS_SAFE_REF_V3
+
post-ref alias-safe reflog/worktree/index projection
=
bounded trusted Human decision effect
```

No claim is made that GitHub metadata proves private Human mental state.

## 51. Implementation responsibility split

`phase6/scriptops-v2-hardening.py`:

```text
expose only approve --decision-pr
reject defect-era acceptance forms
obtain V8 admission
execute only final-gated V8 effect
never invent Human attribution
never invoke Git ref mutation
never invoke Git primary object mutation
surface preparation/uncertainty/recovery outcomes distinctly
```

`legacy/scriptops-v2-single.py`:

```text
disable direct approve
disable direct accepted promotion
```

`phase6/x1b_human_decision.py`:

```text
V8 schemas/canonical JSON
pure accepted preview
trusted GitHub evidence transport
review pagination/currentness
admission/replay/lock
raw object/ref checks
FinalEffectGateV8
Git 2.55 profile
Linux mount-namespace/mountinfo verifier
single-worktree real-gitdir verifier
physical loose-main-ref verifier
physical primary-object-DB verifier
held descriptor identity helpers
POSIX mode/uid/gid/xattr/ACL verifier
fixed umask process guard
sharedRepository census
raw tree parser/rewrite/serializer
raw object canonicalizer/SHA1 verifier
alias-safe fanout creator
alias-safe loose-object installer
object topology outcome classifier
packed-main absence parser
alias-safe main.lock CAS
ref CAS outcome classifier
reflog prestate binder
exact deterministic reflog-line constructor
alias-safe reflog projection
complete-local-object-store V2 detector
no-replace/no-lazy helpers
closed raw commit constructor/verifier
alias-safe canonical worktree materialization
real-index metadata verifier/restorer
post-effect verifier
```

## 52. Independent implementation-review obligations

Later implementation review must prove, not infer:

```text
changed surface authorized
no third acceptance route
legacy/defect paths deny
V8 request identity acyclic
one-file decision PR exact
trusted transport exact
review currentness complete
single-worktree real .git enforced
physical primary .git/objects contained and no-alias
mount-ID containment enforced
no object-directory/alternate escape
no Git primary object-writing command reachable
raw tree construction exact and only two paths changed
all new closure objects physically contained as exact loose objects
fanout and object leaf operations descriptor-relative/no-follow/no-replace
object file final nlink = 1 and mode 0444
physical main ref profile preserved
ref CAS descriptor-relative and exact
no Git ref-mutating command reachable
reflog prestate and deterministic projection exact
final ref/reflog modes 0644 exact
uid/gid exact
xattrs empty and ACL mode-only
caller umask cannot select final permissions
core.sharedRepository cannot select final permissions
real index final mode/security metadata exact
replacement/lazy/partial/promisor closure preserved
configured/traditional hook closure preserved
no canonical worktree/index/reflog mutation before ref commitment
pre-ref object preparation reported truthfully
post-ref failures never silently rewrite history
Human attribution only from validated review
no circular evidence
```

## 53. Separately authorized positive controls

A later live positive control requires fresh Human authorization and a disposable ScriptOps execution instance with inert/synthetic content.

Human must see exact V8 material effect including:

```text
canonical before/after hash
physical/logical refs/heads/main effect
single-worktree real-gitdir restriction
physical primary object-store restriction
no Git primary-object writer
exact loose-object installation profile
exact mode-only security metadata profile
main reflog prestate and deterministic projection
exact two-path one-parent commit
Git 2.55 semantics profile
no-replace/no-lazy profile
complete-local-object-store V2 profile
hook profile
combined durability profile
post-ref alias-safe worktree/index projection
```

A separately authorized fault-injection control must exercise at least:

```text
.git/objects symlink counterexample
fanout substitution during object preparation
object install failure after one object is durable
post-ref pre-fsync interruption
post-ref reflog projection failure
post-ref index metadata failure
```

and prove truthful classifications.

## 54. Corrective closure composition

X1B cannot be closed by brief review, implementation, green CI or positive control alone.

Minimum later closure remains accepted design + independent design review + implementation authority + exact implementation + independent implementation review + fresh corrective verification + required negatives + separately authorized real Human positive control + exact post-effect truth + independent closure review + final Human closure acceptance + durable evidence freeze.

Preserve:

```text
GREEN TESTS != CORRECTIVE CLOSURE
IMPLEMENTATION REVIEW PASS != CORRECTIVE CLOSURE
LIVE POSITIVE CONTROL PASS != CORRECTIVE CLOSURE
TECHNICAL VERIFICATION PASS != HUMAN CLOSURE ACCEPTANCE
X1B CLOSED != V1 AUTHORITY
```

## 55. Successor-review adversarial checklist

Independent R4R8 brief review must explicitly attack at least:

```text
Can .git/objects be symlinked while checks pass?
Can .git/objects be a bind mount with same st_dev while checks pass?
Can a two-hex fanout be symlinked or swapped during install?
Can an existing loose object hardlink escape physical containment?
Can a pack/index used for parent authority be symlinked or externally mounted?
Can any Git command still write a blob/tree/commit to the primary ODB?
Is raw tree ordering and serialization fully determined?
Can object zlib representation change authority semantics?
Can a concurrent final-object creation be overwritten?
Can object preparation be falsely reported as “no effect” after a pre-CAS failure?
Can main/ref/reflog final mode still depend on caller umask?
Can core.sharedRepository or include/worktree config widen permissions?
Can xattr/ACL/security-label inheritance survive undetected?
Can missing ACL/xattr inspection be treated as success?
Can ref/reflog/index metadata differ after successful replacement?
Can a mount-namespace change redirect physical storage while post-checks report complete?
Can V7 evidence authorize V8 semantics?
Can configured hooks, replacement refs, lazy fetch or alternates reappear?
Is any core authority/security choice still left to implementer?
```

Any credible counterexample freezes a finding and returns `NOT PASS`.

## 56. Explicit non-authority

This brief does not authorize:

```text
ScriptOps source mutation
Human decision PR creation
Human review creation
live positive control
canonical screenplay mutation
decision-log mutation
refs/heads/main effect
main reflog effect
primary object-store effect in a live ScriptOps instance
recovery operation
merge
X1B closure
V1 entry
release
deployment
tag
```

R4R8 review PASS, if later obtained, establishes only that this brief is acceptable for a separately Human-authorized implementation stage.

## 57. STOP

Required next stage after durable R4R8 freeze:

```text
INDEPENDENT AK-CANON X1B R4R8 IMPLEMENTATION-BRIEF REVIEW
```

Only fresh separate Human authorization may create that review artifact.

```text
R4R8 BRIEF != IMPLEMENTATION AUTHORITY
R4R8 REVIEW PASS != IMPLEMENTATION AUTHORITY
R4R8 REVIEW PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
STOP
```
