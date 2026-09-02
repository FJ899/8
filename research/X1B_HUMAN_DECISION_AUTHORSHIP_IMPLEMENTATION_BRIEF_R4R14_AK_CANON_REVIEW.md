# X1B Human Decision Authorship — Independent AK-CANON R4R14 Implementation-Brief Review

Status: `INDEPENDENT REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: `2026-09-02`

## 1. Verdict

`AK-CANON X1B R4R14 IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

R4R14 materially improves the persistence-authority model and addresses the exact prior PR #141 defects at brief level in two important respects:

1. the kernel-visible NVDIMM persistence premise is no longer implicit. V14 binds exact `nfit/format=0x0101`, exact `persistence_domain=cpu_cache`, and exact visible `deep_flush=0`, and repeatedly revalidates those values;
2. guest ACPI/NFIT state is no longer treated as bare-metal proof. V14 explicitly requires a distinct trusted-Human platform-persistence review before any positive effect.

The independent review therefore records the exact PR #141 findings as addressed at brief level for their original mechanisms.

However, the new out-of-band platform-attestation mechanism still does not produce a non-transferable, reviewable binding between the Human-observed physical environment and the executor instance that later commits the effect.

Two independent blockers remain:

```text
X1B-R4R14-IBR-F001 — OPAQUE PLATFORM-SNAPSHOT ATTESTATION TARGET = BLOCKER
X1B-R4R14-IBR-F002 — EXECUTION-ENVIRONMENT SUBSTITUTION / TRANSFERABLE ATTESTATION = BLOCKER
```

Either blocker independently prevents implementation authority.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R14 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R14 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#142`

```text
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
BASE TREE = df807db7003dfd201e9be4d5927472e515a2e737
HEAD = 1e5b39b04a61f4b2d487ee086ae1b99ea0f33a53
TREE = d8b1e130576d1ee8e5337e5b78b6ec0ade412222
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R14.md
BLOB = f857390bf30dc4357e3b91db194096e962878c66
```

Immediately before review write, PR #142 remained:

```text
state = OPEN
merged = false
draft = true
mergeable = true
commits = 1
changed_files = 1
additions = 2133
deletions = 0
```

`FJ899/8 main` remained exactly:

```text
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

The exact R4R14 file was freshly reread from the reviewed HEAD before this artifact was written.

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

### 3.3 R4R13 predecessor

```text
FJ899/8 PR #140
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = d0e420ffa08384f4f11efc6edcd042ebb21b4280
TREE = 66fb4a95313287a5715143b64cfa47e0025e6e6e
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R13.md
BLOB = 6da06d21b05c8acbe6a6a39793ec0b1e54396204
```

### 3.4 Binding R4R13 NOT-PASS review

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

## 4. Review method

This review attacks the exact R4R14 artifact rather than treating the introduction of a Human platform-attestation marker as self-proving.

The adversarial pass inspected at least:

```text
exact PR/base/head/blob freeze
current Linux persistence_domain semantics
current Linux deep_flush / nvdimm_has_flush semantics
current NFIT format-interface definitions
R4R14 authenticated sysfs provenance
R4R14 PMEM/NFIT topology
R4R14 PlatformSnapshotV14 contents
DecisionRequestV14 snapshot binding
platform-attestation review origin
platform-attestation marker fields
platform-attestation freshness/currentness
final Human decision -> attestation binding
QEMU / hypervisor guest-state synthesis threat
execution-environment substitution after attestation
snapshot preimage reviewability
request replay / environment replay
prior procfs/userns/idmap corrections
prior ext4 internal-journal and option-state corrections
prior object/index/ref/reflog/worktree durability controls
```

The review distinguishes:

```text
A. is the kernel-visible persistence state explicitly bound?
B. is guest-only state sufficient? (V14 says no)
C. is the Human attestation reviewable against an immutable snapshot preimage?
D. is the attestation non-transferably bound to the actual execution environment?
```

R4R14 substantially improves A and B.

The blockers are C and D.

## 5. Current external semantics checked

The independent pass checked current public source rather than relying only on predecessor review prose.

Linux source state used for semantic inspection:

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
```

Current Linux `region_devs.c` exposes `persistence_domain` from region persistence flags:

```text
ND_REGION_PERSIST_CACHE   -> cpu_cache
ND_REGION_PERSIST_MEMCTRL -> memory_controller
```

and current `deep_flush` renders `nvdimm_has_flush()`.

Current `nvdimm_has_flush()` documents:

```text
1      writes require flushing
0      writes do not require flushing
-ENXIO flushing capability cannot be determined
```

and contains the compatibility fallback that when DIMMs have neither flush hints nor an explicit flush callback, Linux assumes a platform persistence mechanism such as ADR and returns `0`.

Current NFIT definitions include:

```text
NFIT_FIC_BYTE  = 0x0101  byte-addressable energy backed
NFIT_FIC_BLK   = 0x0201  block-addressable non-energy backed
NFIT_FIC_BYTEN = 0x0301  byte-addressable non-energy backed
```

Sources checked:

```text
https://github.com/torvalds/linux/blob/89a312991dc6e638a36adc43ccb91dbc25504c04/drivers/nvdimm/region_devs.c
https://github.com/torvalds/linux/blob/89a312991dc6e638a36adc43ccb91dbc25504c04/drivers/acpi/nfit/nfit.h
```

QEMU source/docs state used for the virtualization threat model:

```text
a925240509d1b4b656cc480f1cc79ba4d7c8bc08
```

The reviewed QEMU material continues to expose standard ACPI/NFIT virtual NVDIMM behavior and host backend choices such as `memory-backend-file` / `memory-backend-ram`, with persistence depending on host-side conditions that are not established merely by guest ACPI/NFIT state.

Source checked:

```text
https://github.com/qemu/qemu/blob/a925240509d1b4b656cc480f1cc79ba4d7c8bc08/docs/nvdimm.txt
```

## 6. PR #141 F001 disposition — persistence-domain / deep-flush authority

Disposition: `ADDRESSED AT BRIEF LEVEL FOR THE EXACT PRIOR MECHANISM`.

R4R13 omitted the current region authority:

```text
persistence_domain
deep_flush
```

R4R14 now requires both attributes to exist on the authenticated sysfs mount and supports exactly:

```text
persistence_domain raw bytes = "cpu_cache\n"
deep_flush raw bytes = "0\n"
```

It explicitly rejects:

```text
memory_controller
missing/empty/unknown persistence_domain
deep_flush=1
missing/indeterminate deep_flush
parse ambiguity
```

The values are included in `PlatformSnapshotV14` and revalidated at multiple gates through post-effect verification.

This directly closes the prior hidden reliance on libnvdimm's fallback assumption as an unbound implementation premise.

R4R14 also adds exact `nfit/format=0x0101` and rejects the known `0x0201` / `0x0301` non-energy-backed FICs.

No new blocker is raised against the fact that V14 deliberately supports only the narrower `cpu_cache + deep_flush=0 + FIC 0x0101` kernel-visible profile.

## 7. PR #141 F002 disposition — guest ACPI NFIT alone as backend proof

Disposition: `ADDRESSED AT BRIEF LEVEL FOR THE EXACT PRIOR COUNTEREXAMPLE`.

R4R14 states explicitly:

```text
NO PURE GUEST SOFTWARE TEST CAN ESTABLISH BARE-METAL BACKING AGAINST A HYPERVISOR THAT CONTROLS GUEST ACPI/NFIT STATE.
```

and creates no guest-only positive path.

A positive V14 effect requires a distinct trusted-Human GitHub review with exact marker:

```text
X1B-PLATFORM-PERSISTENCE-ATTESTATION-V1
```

The review must assert an out-of-band non-guest observation and bare-metal physical ACPI NFIT NVDIMM backing.

Standard QEMU vNVDIMM with its reviewed `0x0301` FIC is also rejected earlier by the kernel-state profile.

Even synthetically guest-spoofed:

```text
0x0101
cpu_cache
deep_flush=0
empty nfit/flags
ACPI0012
ACPI.NFIT
/dev/pmem0
```

is not sufficient without the Human platform review.

Thus the exact prior defect — treating guest ACPI/NFIT as host/backend attestation — is not preserved in R4R14.

The new blockers concern whether the replacement attestation is itself reviewable and non-transferably bound to the committing environment.

# FINDING 1

## 8. X1B-R4R14-IBR-F001 — opaque platform-snapshot attestation target

Severity: `BLOCKER`.

### 8.1 V14 defines a rich snapshot but publishes only its digest as request authority

Section 22 defines `PrimaryStoragePreStateV2` / `PlatformSnapshotV14` as a rich canonical record containing, among other things:

```text
repository sb_source
repository sb_dev major/minor
/dev source identity
raw /sys/dev/block link target
canonical sysfs physical path
block queue fields
ndbus identity
provider
ACPI ancestry
region identity
range index
mappings
namespace identity/personality
mapped nmem identities
NFIT identity fields
nfit/format bytes
nfit/flags bytes
persistence_domain bytes
deep_flush bytes
```

It then defines:

```text
platform_snapshot_sha256 = SHA256(canonical PlatformSnapshotV14 bytes)
```

However, `DecisionRequestV14` binds only:

```text
exact platform_snapshot_sha256
required nfit_format = 0x0101
required persistence_domain = cpu_cache
required deep_flush = 0
```

The request schema does not normatively require publication of the exact canonical `PlatformSnapshotV14` bytes, nor an immutable content-addressed snapshot artifact whose bytes are available to the Human attestor.

The platform-attestation marker likewise binds only:

```text
platform_snapshot_sha256=<digest>
```

not a snapshot artifact id/blob/URL plus digest.

### 8.2 The Human is asked to attest an opaque commitment

V14's sequence says:

```text
1. immutable V14 decision request is published
2. trusted Human independently inspects the exact request and out-of-band platform/backend state
3. trusted Human submits the platform attestation
```

But the exact request, as normatively specified, exposes only the snapshot digest for the rich guest-state record.

The Human can read:

```text
platform_snapshot_sha256 = <64 hex>
```

without having a normative trusted artifact containing the canonical preimage that produced it.

A SHA-256 digest provides integrity for known bytes; it does not make unknown bytes reviewable.

Therefore the Human cannot, from the immutable request evidence alone, verify such questions as:

```text
which exact /sys/dev/block target was hashed?
which exact region/mapping identities were hashed?
which exact NVDIMM serial/phys_id/vendor/device values were hashed?
which exact raw nfit/format bytes were hashed?
which exact raw persistence_domain/deep_flush bytes were hashed?
which exact queue/source/topology values were hashed?
```

The marker's `why=` field does not close this; it is an unconstrained one-line rationale, not the canonical snapshot evidence.

### 8.3 Internal executor consistency is not Human reviewability

The executor later recomputes `PlatformSnapshotV14` and requires the digest to match.

That proves consistency between the executor's later observation and the executor-generated request commitment.

It does not prove that the Human who supplied the out-of-band environmental premise reviewed the same complete canonical snapshot values.

A buggy or incorrectly specified implementation can commit to the wrong canonical field set and remain self-consistent at all later executor gates.

The higher-level contract requires no core authority/security choice to remain implicit and requires exact binding of the Human act to the material effect.

For an external environmental attestation, an opaque digest without reviewable preimage is insufficiently reviewable to establish that exact binding.

### 8.4 This blocker is independent of environment substitution

Suppose a successor fixes F002 below by adding a perfect hardware-rooted machine identity.

If the Human still signs only an opaque `platform_snapshot_sha256` without a published immutable preimage, the Human cannot audit the complete snapshot fields to which the attestation is said to apply.

Therefore F001 survives an F002-only fix.

### 8.5 Required successor correction

A successor must publish the exact canonical snapshot evidence that the Human is asked to attest.

A reviewable direction is:

```text
immutable request
-> exact canonical PlatformSnapshot bytes or immutable content-addressed snapshot artifact
-> artifact blob/content digest
-> request binds exact artifact identity + digest
-> platform-attestation review binds exact artifact identity + digest
-> Human can inspect the exact canonical values before approval
-> executor later reconstructs and compares byte-for-byte / digest-for-digest
```

If variable-length raw values remain represented only by sub-digests inside the canonical snapshot, the exact raw preimages needed for Human review must themselves be available through an immutable content-addressed evidence artifact, or the review must explicitly define why those values need not be Human-reviewable.

Until then:

```text
X1B-R4R14-IBR-F001 = BLOCKER
```

# FINDING 2

## 9. X1B-R4R14-IBR-F002 — execution-environment substitution / transferable attestation

Severity: `BLOCKER`.

### 9.1 V14 correctly says guest state is cloneable

R4R14 explicitly recognizes that a hypervisor can synthesize guest-visible fields.

The positive guest snapshot nevertheless consists entirely of state observed from within the executing Linux environment, including:

```text
/proc-derived execution state
statmount/ext4 state
/dev identity
/sys/dev/block topology
ACPI ancestry
ACPI.NFIT provider
region mappings
NVDIMM identity fields
nfit/format
nfit/flags
persistence_domain
deep_flush
```

Those checks are useful consistency constraints.

They are not a non-clonable machine identity against the threat model that motivated PR #141 F002.

### 9.2 The Human review contains assertions but no non-transferable environment binding

The exact platform marker contains:

```text
decision_request_id
decision_request_sha256
platform_snapshot_sha256
environment_class=bare-metal
virtualization_layer=none
backend_class=physical-acpi-nfit-nvdimm
power_loss_persistence=affirmed
persistence_domain=cpu_cache
deep_flush=0
nfit_format=0x0101
observation_channel=out-of-band-non-guest
why=...
```

It contains no normative field such as:

```text
hardware-rooted platform identity
TPM/TEE/device attestation key identity
host-generated request nonce response
platform quote digest
host/backend signed evidence id
out-of-band observer evidence artifact digest
physical machine identity that the executor can independently verify
```

The exact R4R14 brief contains no TPM quote, challenge nonce or equivalent cryptographic environment binding.

`environment_class=bare-metal` and `observation_channel=out-of-band-non-guest` are authenticated Human statements.

They are not themselves non-transferable evidence that the executor instance currently about to rename `main` is still the same environment that the Human inspected.

### 9.3 Concrete substitution sequence

Consider this sequence within the permitted 900-second attestation window.

1. The request is created on the intended physical machine.
2. `PlatformSnapshotV14` has digest `S`.
3. A trusted Human inspects the physical machine out of band and submits a valid platform review for request `R`, snapshot `S`.
4. The final Human decision references that review.
5. Before material commitment, execution is moved/restarted on a different environment controlled by a hypervisor.
6. The replacement environment presents the same guest-visible values used to calculate snapshot `S`.
7. GitHub request/review state is unchanged and still fresh.
8. The executor recomputes the guest snapshot and again obtains `S`.
9. No negative-only virtualization hint is exposed by the replacement environment.

Under the V14 predicates, the executor can still observe:

```text
request R exact
platform snapshot S exact
platform review exact/APPROVED/fresh
Human decision exact
nfit/format 0x0101
persistence_domain cpu_cache
deep_flush 0
all other guest topology exact
```

The platform review is now being used on a different execution environment than the Human inspected.

The review object itself was not forged.

The request was not modified.

The snapshot digest did not drift.

The attack exploits transferability of the attestation binding target.

### 9.4 Why the 900-second window does not close substitution

Freshness constrains time:

```text
GitHub-server-time - submitted_at <= 900 seconds
```

It does not establish location or platform continuity.

An attestation can be both:

```text
fresh
and
bound to the wrong current execution environment
```

The same is true of repeated pre-lock / pre-rename refetches: they prove the GitHub review remains current, not that the executing machine remains the attested machine.

### 9.5 Why publishing the full snapshot would not close substitution

Suppose F001 is fixed and the full canonical snapshot is published and reviewed.

A hypervisor capable of reproducing the same guest-visible snapshot can still present the same reviewed bytes.

Thus full snapshot reviewability alone does not make the attestation non-transferable.

F002 therefore survives an F001-only fix.

### 9.6 R4R14's own threat statement makes this binding necessary

R4R14 states:

```text
NO PURE GUEST SOFTWARE TEST CAN ESTABLISH BARE-METAL BACKING AGAINST A HYPERVISOR THAT CONTROLS GUEST ACPI/NFIT STATE.
```

The same principle applies to continuity after the Human observation.

If the only executor-verifiable link from the Human review to the current machine is a digest of guest-observed state, a hypervisor that controls that state can satisfy the link after substitution.

The out-of-band origin of the Human observation is valuable, but it must be bound to a current environment identity that cannot be reproduced merely by synthesizing guest state.

### 9.7 Required successor correction

A successor must define a non-transferable current-environment binding for the platform attestation.

A reviewable narrow direction is one of:

```text
request-bound hardware-rooted quote with fresh challenge nonce
host/hypervisor/backend attestation signed by a separately trusted key and bound to the exact request digest + nonce + machine/backend identity
out-of-band platform evidence whose identity is independently verifiable by the executor and cannot be synthesized solely through guest ACPI/NFIT/sysfs
```

The exact trust root, key enrollment, nonce/challenge freshness, replay behavior, revocation and executor verification semantics must be frozen rather than delegated to implementation discretion.

A mere additional Human marker field such as:

```text
machine_id=<free text>
```

would not be sufficient unless the executor has an independent authenticated source for the same identity.

Until then:

```text
X1B-R4R14-IBR-F002 = BLOCKER
```

## 10. Human-attestation origin itself is not rejected

This review does not claim that a trusted Human can never be an authority source for an external environmental premise.

R4R14 makes that premise explicit and separates it from the final Human effect decision, which is an improvement.

The blocker is narrower:

```text
Human review authenticity != reviewable snapshot preimage
Human review freshness != current machine continuity
Human statement about bare metal != executor-verifiable binding to this current execution environment
```

A successor may retain a Human attestation layer if it supplies the missing evidence publication and non-transferable environment binding.

## 11. Negative-only virtualization diagnostics disposition

R4R14 correctly treats guest virtualization hints only as negative diagnostics.

A positive hypervisor-present signal must block.

Absence of:

```text
CPUID hypervisor bit
/sys/hypervisor
known DMI virtualization marker
```

is not treated as positive bare-metal proof.

No blocker is raised against that rule.

## 12. Internal ext4 journal preservation

The independent review found no R4R14 change that reopens the R4R13 internal-journal correction.

V14 preserves:

```text
HAS_JOURNAL set
s_journal_inum > 0
s_journal_uuid = zero
s_journal_dev = 0
INCOMPAT_JOURNAL_DEV absent
```

and retains the current ext4 rule that a nonzero external journal override cannot coexist with a nonzero internal journal inode in the reviewed mounted state.

Disposition:

```text
R4R12 F002 EXTERNAL EXT4 JOURNAL WRITE DOMAIN = ADDRESSED AT BRIEF LEVEL
```

## 13. Preservation of earlier corrections

The two new findings do not reopen the established brief-level corrections for:

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

This is not a blanket implementation proof.

## 14. Mandatory successor regressions implied by this review

### 14.1 Snapshot publication / reviewability

A successor review must test at least:

```text
request publishes exact canonical PlatformSnapshot evidence -> required
request publishes digest only -> BLOCK
platform review references digest but no immutable snapshot artifact -> BLOCK
snapshot artifact content digest mismatch -> BLOCK
snapshot artifact identity substituted -> BLOCK
canonical snapshot byte-order/field-order mismatch -> BLOCK
raw sub-evidence digest without available immutable preimage where Human review requires it -> BLOCK or explicitly justified unsupported review path
Human attestor can inspect exact values before approval -> positive prerequisite
executor recomputation differs from published artifact -> BLOCK
```

### 14.2 Environment continuity / anti-transferability

A successor review must attack at least:

```text
valid physical-host attestation replayed on another host -> BLOCK
valid attestation replayed inside VM with cloned guest snapshot -> BLOCK
valid attestation reused after host reboot if continuity evidence invalid -> BLOCK
valid attestation reused after backend swap with same guest-visible fields -> BLOCK
fresh GitHub review + wrong current machine -> BLOCK
snapshot digest identical + machine identity different -> BLOCK
absence of hypervisor hints + wrong machine -> BLOCK
host/machine quote for wrong request nonce -> BLOCK
old quote replayed for new request -> BLOCK
quote/signature valid but trust root unknown/revoked -> BLOCK
```

### 14.3 Preserve R4R14 kernel-state negatives

```text
nfit/format=0x0301 -> BLOCK
nfit/format=0x0201 -> BLOCK
nfit/format absent -> BLOCK
persistence_domain=memory_controller -> BLOCK
persistence_domain absent/unknown -> BLOCK
deep_flush=1 -> BLOCK
deep_flush absent/indeterminate -> BLOCK
kernel-state drift -> BLOCK/UNCERTAIN according to stage
```

### 14.4 Preserve platform-review sequencing

```text
platform review before request -> BLOCK
platform review after final decision -> BLOCK
stale/dismissed/conflicting review -> BLOCK
new platform review without new final Human decision -> BLOCK
final Human decision not binding exact platform review id/body digest -> BLOCK
```

## 15. Review verdict matrix

```text
PR #141 F001 NVDIMM persistence-domain/deep-flush      = ADDRESSED AT BRIEF LEVEL FOR EXACT PRIOR MECHANISM
PR #141 F002 guest ACPI/NFIT as backend proof          = ADDRESSED AT BRIEF LEVEL FOR EXACT PRIOR COUNTEREXAMPLE
R4R13 internal ext4 journal correction                 = PRESERVED
R4R13 closed ext4 runtime option table                 = PRESERVED

X1B-R4R14-IBR-F001 opaque platform snapshot target     = BLOCKER
X1B-R4R14-IBR-F002 transferable environment attestation= BLOCKER

AK-CANON X1B R4R14 IMPLEMENTATION-BRIEF REVIEW         = NOT PASS
IMPLEMENTATION AUTHORITY                                = NOT ESTABLISHED
X1B                                                     = OPEN
V1 AUTHORITY                                            = NOT ESTABLISHED
```

## 16. Required successor direction

A successor corrective brief must not merely add more guest fields or lengthen the 900-second window.

At minimum it must freeze both:

```text
A. exact immutable Human-reviewable PlatformSnapshot evidence publication
B. non-transferable current-environment attestation bound to request-specific freshness/challenge and a separately authenticated host/hardware/backend identity
```

The second requirement must be independently verifiable by the executor; otherwise the same substitution attack survives.

Potential technology choices are not pre-authorized by this review.

The successor must independently research and freeze one bounded supported profile before implementation authority can be considered.

## 17. No implementation authority

This artifact is review evidence only.

It does not authorize:

```text
R4R15 or another successor correction
ScriptOps source mutation
Human platform-attestation creation
Human decision evidence creation
positive control
canonical screenplay effect
recovery mutation
merge
X1B closure
Agency Kernel v1 authority
release
deployment
tag
```

## 18. Exact STOP boundary

After this review artifact is frozen in one draft PR, STOP.

Required next legal step:

```text
fresh Human authorization
-> successor corrective implementation brief addressing
   X1B-R4R14-IBR-F001
   X1B-R4R14-IBR-F002
```

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R14 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```
