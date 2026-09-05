# X1B HUMAN DECISION AUTHORSHIP — CLEAN IMPLEMENTATION BRIEF R4R15

Status: `CLEAN R4R15 CORRECTIVE BRIEF / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-02`

## 1. Authority, purpose, and STOP boundary

This document is the self-contained successor implementation brief after independent AK-CANON review PR #143 returned `NOT PASS` on R4R14.

R4R15 preserves the accepted X1B corrective-design properties and every R4R14 mechanism not rejected by PR #143, while correcting the two exact blockers frozen by that review:

1. `X1B-R4R14-IBR-F001`: R4R14 defined a rich platform snapshot but Human authority bound only its digest, without requiring publication of the exact canonical preimage;
2. `X1B-R4R14-IBR-F002`: R4R14's Human platform review was fresh and request-bound but transferable because the current executor proved guest-clonable snapshot equality, not possession of a non-migratable hardware root bound to the reviewed environment.

R4R15 chooses a narrow successor profile:

```text
PUBLISHED_PLATFORM_SNAPSHOT_EVIDENCE_V1
PHYSICAL_TPM2_ECC_EK_AK_V1
TPM2_REQUEST_CHALLENGE_QUOTE_V1
TPM2_MEASURED_BOOT_CONTINUITY_V1
TPM2_LIVE_GATE_CONTINUITY_V1
OUT_OF_BAND_PLATFORM_PERSISTENCE_ATTESTATION_V2
PLATFORM_ATTESTATION_CURRENTNESS_V2
```

The positive V15 path requires both:

```text
Human-reviewable exact PlatformSnapshotV15 bytes
AND
live request-specific cryptographic continuity to the exact Human-reviewed physical TPM EK/AK identity
```

A digest without its required reviewable preimage is never platform authority.

A Human machine statement without current cryptographic possession proof is never platform continuity authority.

R4R15 is an implementation brief only. It authorizes no ScriptOps source mutation, no independent R4R15 review, no TPM provisioning or persistence mutation, no Human platform-attestation creation, no Human final-decision creation, no positive control, no canonical screenplay effect, no recovery mutation, no merge, no X1B closure, no V1 authority, no release/deployment/tag.

```text
R4R15 BRIEF != IMPLEMENTATION AUTHORITY
R4R15 REVIEW PASS != IMPLEMENTATION AUTHORITY
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
DIGEST WITHOUT REVIEWABLE PREIMAGE != REVIEWABLE AUTHORITY
HUMAN MACHINE STATEMENT != LIVE HARDWARE POSSESSION PROOF
```

After durable freeze of this brief, STOP. The next legal stage is one separately Human-authorized independent AK-CANON R4R15 implementation-brief review.

## 2. Exact governance lineage

### 2.1 Accepted corrective design

```text
FJ899/scriptops PR #34
HEAD = d7a5065c87e9a4b49fb608235c908bceac42b4b1
TREE = 3140d0ac95c120a7b1532942bae2e0dad38b4839
PATH = governance/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_CANDIDATE.md
BLOB = dac16f109d1414a2208c2ed9a166ae9e9a329216
```

Preserved higher-level properties:

```text
separate trusted Human decision act
exact content/scope/candidate/effect binding
freshness/activity/supersession/conflict/replay semantics
executor no-substitution
fail closed on ambiguity
real-boundary negative regressions
real separately authorized positive Human control
post-effect truth matching Human-bound effect
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
VERDICT = PASS
```

### 2.3 R4R14 predecessor

```text
FJ899/8 PR #142
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 1e5b39b04a61f4b2d487ee086ae1b99ea0f33a53
TREE = d8b1e130576d1ee8e5337e5b78b6ec0ade412222
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R14.md
BLOB = f857390bf30dc4357e3b91db194096e962878c66
```

### 2.4 Binding R4R14 NOT-PASS review

```text
FJ899/8 PR #143
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 8b97e469e553b5655d0b7f64c1f972fbad886c5f
TREE = 0b0accfee46cf91500fa599ee3547222e1c70bc6
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R14_AK_CANON_REVIEW.md
BLOB = f5575229a994c70a0dc18650bd5b07d2bf7748ba
VERDICT = NOT PASS
```

PR #143 froze:

```text
X1B-R4R14-IBR-F001 — OPAQUE PLATFORM-SNAPSHOT ATTESTATION TARGET
X1B-R4R14-IBR-F002 — EXECUTION-ENVIRONMENT SUBSTITUTION / TRANSFERABLE ATTESTATION
```

PR #143 also recorded the prior R4R13/R4R14 kernel persistence, internal-journal, and ext4-option corrections as addressed/preserved. V15 may not weaken them.

## 3. Exact repository state before R4R15 preparation

```text
FJ899/8 main
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

```text
FJ899/scriptops main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Security baseline BLOBs remain:

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

## 4. Normative precedence and V15 migration

```text
R4R15 TEXT = CURRENT IMPLEMENTATION-BRIEF AUTHORITY
R4R14 AND EARLIER IMPLEMENTATION BRIEFS = HISTORICAL INPUT ONLY
CORRECTIVE DESIGN PR #34 = HIGHER-LEVEL PROPERTY CONTRACT
```

V15 authority-critical changes:

```text
full PlatformSnapshotV15 canonical bytes are published inside immutable DecisionRequestV15
all Human-review-required raw snapshot values have full byte preimages in that block
snapshot and request are strictly size-bounded to fit trusted GitHub evidence surfaces
request contains a CSPRNG-generated 32-byte attestation nonce
platform Human review V2 binds exact request/snapshot/nonce plus full reference TPM evidence
V2 review enrolls one exact current ECC EK certificate and one exact fixedTPM/fixedParent AK per request
current executor proves AK/EK co-residency with fresh MakeCredential/ActivateCredential challenge
current executor proves live possession of exact AK with TPM2_Quote
reference/gate quote extraData bind request + snapshot + fresh nonce
PCR selection is exact SHA-256 0,2,4,7,10
PCR10 is continuity-only, not a semantic bare-metal proof
TPM clock/reset/restart/safe/firmware/PCR continuity is bound through commitment
```

No V14 or earlier request/review/decision evidence may authorize V15.

## 5. Future bounded implementation surface

Expected future ScriptOps surface exactly:

```text
phase6/scriptops-v2-hardening.py
legacy/scriptops-v2-single.py
phase6/x1b_human_decision.py
phase6/x1b_tpm_attestation.py
scripts/restore_v2.py
scripts/verify_repository.py
sources/prototype/RESTORE.md
SOURCE_MANIFEST.md
README.md
PROJECT_STATE.md
HANDOFF.md
tests/test_phase6_scriptops_smoke.py
tests/test_x1b_human_decision.py
tests/test_x1b_tpm_attestation.py
.github/workflows/x1b-human-decision.yml
```

Expected unchanged:

```text
phase6/bounded-proposal-view.py
.github/workflows/phase6-scriptops-smoke.yml
.github/workflows/verify-repository.yml
sources/prototype/scriptops-v2-single.py.part01..part07
```

No TPM private key, EK private material, AK private material, hierarchy auth secret, Human credential, or persistent provisioning secret may be committed.

Future V15 may create transient TPM objects/sessions needed for verification. It MUST NOT clear the TPM, change hierarchy authorization, persist/evict a key, define/undefine NV state, intentionally extend/reset PCRs, or provision a new AK.

A required pre-existing AK absence/incompatibility means `BLOCKED`; provisioning requires separate Human authority.

# PART I — CORE HUMAN DECISION RULE

## 6. HumanDecision rule

```text
HumanDecision = TRUE
ONLY IF
separate trusted Human final-decision evidence
for exact content + scope + candidate + material effect
AND exact current PlatformAttestationV2
is independently validated and admitted.
```

Never sufficient alone:

```text
approval-command possession
non-empty rationale
caller identity/rationale
continuation/silence
AI-created record
CI success
mergeability
effect credential
successful fsync
guest ACPI/NFIT shape
platform snapshot digest without exact published snapshot bytes
Human platform marker without live TPM proof
TPM quote without Human physical-backend attestation
```

Preserve:

```text
AI PROPOSED != HUMAN DECIDED
HUMAN DECISION EVIDENCE != EXECUTION CREDENTIAL
PLATFORM SNAPSHOT DIGEST != PLATFORM SNAPSHOT PREIMAGE
TPM IDENTITY != BACKEND PERSISTENCE DECISION
HUMAN BACKEND STATEMENT != LIVE TPM CONTINUITY
```

## 7. Interfaces

Only effect-capable interface remains:

```text
python phase6/scriptops-v2-hardening.py approve --decision-pr <positive-integer>
```

PR number is locator only.

A future read-only preparation interface may exist:

```text
python phase6/x1b_human_decision.py platform-evidence --decision-pr <positive-integer>
```

It may print evidence only; it may not create/edit/submit/approve/dismiss GitHub authority or mutate repository/TPM persistent state.

# PART II — PRESERVED LINUX / STORAGE AUTHORITY

## 8. Supported platform

```text
Git 2.55.0 <= version < 2.56.0
object format = sha1
ref storage = files
OS = Linux
filesystem = ext4
source = direct whole /dev/pmem<N>
ACPI_NFIT_PMEM_PERSISTENT_BLOCK_V2
nfit/format = 0x0101 only
persistence_domain = cpu_cache only
deep_flush = 0 only
initial user namespace
non-ID-mapped mount
authenticated procfs/sysfs
internal ext4 journal only
barrier enabled
data=ordered or data=journal
journal_async_commit absent
DAX disabled
ext4 errors_count = 0
```

Unavailable/ambiguous/unreadable authority primitive means `BLOCKED`.

## 9. AUTHENTIC_CURRENT_TASK_PROCFS_V1 preserved

Hold genuine `/proc`, require `PROC_SUPER_MAGIC`, exact proc mount ID/statmount fs_type, bind `getpid/gettid` to genuine `thread-self`, and use descriptor-relative numeric authority paths with:

```text
RESOLVE_BENEATH
RESOLVE_NO_XDEV
RESOLVE_NO_SYMLINKS
```

Any overmount/cross-mount/source drift blocks.

## 10. User namespace / credentials preserved

Require:

```text
USER_NS_INIT_INO = 4026531837
uid_map = 0 0 4294967295
gid_map = 0 0 4294967295
```

Bind/revalidate r/e/s/fs uid/gid, supplementary groups, all capability sets and NoNewPrivs. Direct syscall/proc views must agree.

## 11. Non-ID-mapped ext4 mount preserved

Use exact mount ID/statx/statmount. Require ext4, writable, `MOUNT_ATTR_IDMAP=0`, `SB_LAZYTIME=0`, zero uid/gid maps and required `MNT_OPTS`, `OPT_ARRAY`, `SB_SOURCE`, `MNT_ROOT` availability.

## 12. Authenticated block/sysfs profile preserved

Hold genuine `/sys`, require `SYSFS_MAGIC`, exact sysfs mount ID, exact block-special `/dev/pmem<N>` rdev matching ext4 `sb_dev`, exact `/sys/dev/block/M:m` physical target.

Reject partitions, aliases, loop, DM/LVM/crypt, md, network, virtio/xen, zram/ramdisk, NVMe/SCSI/SATA, CXL, E820/manual/test PMEM, DAX chars, BTT/PFN and unknown stacks.

## 13. ACPI NFIT PMEM profile preserved

Require:

```text
whole pmem<N>
region devtype=nd_pmem
provider=ACPI.NFIT
ACPI0012 ancestry
positive nfit/range_index
positive exact mappings
all mapped nmem identities
all nfit/flags empty
all nfit/format raw bytes = 0x0101
```

## 14. Persistence-domain profile preserved

Require exact raw:

```text
persistence_domain = "cpu_cache\n"
deep_flush = "0\n"
```

Reject memory_controller, missing/unknown values, deep_flush=1/absent/indeterminate.

# PART III — PR #143 F001: EXACT PUBLISHED SNAPSHOT PREIMAGE

## 15. Correction rule

Positive path:

```text
construct bounded canonical PlatformSnapshotV15
-> publish exact bytes verbatim inside immutable request
-> request digest covers exact bytes
-> Human can inspect exact values before V2 platform approval
-> V2 review binds request digest + snapshot digest
-> executor reconstructs current bytes
-> byte-for-byte equality required
```

No `Human sees hash only` path exists.

## 16. Canonical PlatformSnapshotV15 block

Exact UTF-8/LF block:

```text
-----BEGIN X1B-PLATFORM-SNAPSHOT-V15-----
...
-----END X1B-PLATFORM-SNAPSHOT-V15-----
```

No BOM/CR/tabs/trailing spaces/Unicode normalization/Markdown normalization/reordering/duplicate/omitted authority field.

For every Human-review-required raw source:

```text
<field>.raw_len=<canonical unsigned decimal>
<field>.raw_hex=<lowercase even-length full raw bytes>
<field>.semantic=<canonical parsed value>
```

No authority raw value may appear only as a digest.

## 17. Required snapshot preimages

Include at least full raw+semantic preimages for:

```text
repository sb_source
sb_dev major/minor
/dev source mode/rdev
/sys/dev/block raw link target
canonical physical target
sysfs mount ID
block basename,size,ro,required queue values
ndbus identity/provider/nfit revision
ACPI ancestry
region identity/devtype/range_index/mappings
mapping0..mapping(K-1)
namespace identity/personality
all mapped nmem identities
required NFIT identity fields
nfit/format
nfit/flags
persistence_domain
deep_flush
TPM char-device and physical sysfs identity
TPM driver
TPM manufacturer/firmware/revision properties
required AK persistent handle
```

## 18. Snapshot/request bounds

To fit trusted GitHub evidence without truncation:

```text
maximum mappings = 16
maximum mapped nmem = 16
maximum one raw value = 4096 bytes
maximum PlatformSnapshotV15 block = 32768 bytes
maximum complete DecisionRequestV15 body = 60000 bytes
```

Any larger evidence is unsupported and blocks. No truncation is authorized.

Define:

```text
platform_snapshot_len = exact byte length including delimiters
platform_snapshot_sha256 = SHA256(exact block bytes)
```

DecisionRequestV15 contains exact `len`, digest, then exact block. Request digest covers it.

## 19. Reviewability validation

Block if snapshot block absent/truncated, len/digest mismatch, request drift, incomplete GitHub response, hidden executor-only raw authority value, or current reconstruction differs byte-for-byte.

# PART IV — PR #143 F002: PHYSICAL TPM ROOT AND LIVE CONTINUITY

## 20. Correction strategy

Human V2 platform review remains authority for the external environmental facts. Executor separately proves live access to the same Human-reviewed TPM identity.

The Human attests:

```text
this EK/AK identity belongs to the intended physical machine
this is the machine inspected out of band
repository PMEM backing is the reviewed physical ACPI NFIT NVDIMM
power-loss persistence is affirmed
no VM/hypervisor layer mediates this backend for this request
physical TPM is not intentionally proxied/passed through to another execution environment for this request
```

The executor proves:

```text
current TPM presents exact enrolled EK certificate/public key
current AK is exact enrolled fixedTPM/fixedParent key
current AK and EK are co-resident via fresh credential activation
fresh request/gate quotes verify under that exact AK
reference boot/PCR/clock continuity remains exact
```

Neither layer substitutes for the other.

## 21. Standards basis

Current semantics used:

```text
TCG TPM 2.0 Library Specification Version 185 (2026-03-12)
TCG EK Credential Profile TPM 2.0 Version 2.7 (2026-03-19)
TPM2_Quote / TPMS_ATTEST / TPMS_CLOCK_INFO
TPM2_MakeCredential / TPM2_ActivateCredential
```

V15 relies on:

```text
qualifyingData echoed as TPMS_ATTEST.extraData
quote signs qualifiedSigner + extraData + clockInfo + firmwareVersion + PCR digest
clockInfo includes clock/resetCount/restartCount/safe
fixedTPM = non-duplicable key property
fixedParent = parent migration restriction
ActivateCredential proves credentialed AK is on TPM possessing corresponding EK
standard low-range ECC P-256 EK certificate index = 0x01C0000A
```

## 22. Physical TPM device gate

Require exactly one TPM 2.0 exposure:

```text
/dev/tpm0
/dev/tpmrm0
/sys/class/tpm/tpm0
```

Authenticate sysfs origin and bind char-device rdevs, canonical physical target, driver, TPM version, `TPM_PT_MANUFACTURER`, firmware versions and revision.

Explicitly reject when exposed:

```text
tpm_vtpm_proxy
/dev/vtpmx
Xen vTPM
software TPM identity
known virtual TPM ancestry
unknown TPM topology
```

Absence of such marker is not positive authority; EK/AK live proof remains mandatory.

## 23. Exact ECC EK profile

V15 supports only:

```text
TPM 2.0 ECC NIST P-256 EK
EK cert read from TPM NV index 0x01C0000A
nameAlg SHA256
TCG default ECC P-256 EK template unless a manufacturer-populated template/nonce is actually present; such non-default material is unsupported in V15
```

Therefore if 0x01C0000B or 0x01C0000C is populated and affects EK construction, V15 blocks rather than improvises.

Bind exact DER certificate bytes/digest, SPKI digest/public point, issuer/subject/serial, validity interval and current EK TPM public area.

Current EK public point must equal certificate SPKI public key.

No manufacturer web retrieval is runtime authority.

## 24. Exact persistent AK profile

Required pre-existing handle:

```text
0x8101F515
```

`TPM2_ReadPublic` must yield exact ECC P-256 restricted attestation signing key:

```text
type=ECC
curve=NIST P-256
nameAlg=SHA256
scheme=ECDSA/SHA256
fixedTPM=1
fixedParent=1
sensitiveDataOrigin=1
restricted=1
sign/encrypt=1
decrypt=0
```

Exact TPMT_PUBLIC bytes, public digest, Name, Qualified Name (when available) and ECC point are bound.

Any semantic attribute mismatch blocks. There is no review-time equivalence override and no implementation discretion.

## 25. Request attestation nonce

At request construction obtain exactly 32 bytes from Linux `getrandom()` with no caller input.

Publish as 64 lowercase hex:

```text
request_attestation_nonce=<64 hex>
```

Nonce is part of request digest. Collision with any known consumed V15 request nonce blocks.

## 26. Reference quote extraData

Define exact domain bytes:

```text
X1B-TPM2-REFERENCE-QUOTE-V15\x00
```

Define 32-byte:

```text
reference_extra_data = SHA256(
  domain
  || request_digest_bytes
  || platform_snapshot_sha256_bytes
  || request_attestation_nonce_bytes
  || ak_name_bytes
)
```

TPM2_Quote qualifyingData MUST equal those exact 32 bytes.

## 27. TPM2_MEASURED_BOOT_CONTINUITY_V1 PCR selection

Exact quoted bank/selection:

```text
SHA256 PCR 0
SHA256 PCR 2
SHA256 PCR 4
SHA256 PCR 7
SHA256 PCR 10
```

No SHA-1 fallback and no omitted PCR.

PCR 0/2/4/7 are frozen boot-chain continuity inputs.

PCR10 is used only as a continuity/tamper signal. V15 does **not** infer `bare metal` or backend persistence from an opaque PCR10 value.

V15 requires Linux IMA to be active such that `/sys/kernel/security/ima/ascii_runtime_measurements` is available from authenticated securityfs and its replayed aggregate for SHA-256 PCR10 equals the current TPM PCR10 at reference admission.

The full IMA log is not Human platform authority and is not hidden evidence for a semantic Human decision. It is machine-verification input only. Its SHA-256 and record count are bound in reference evidence to detect log substitution.

If IMA is unavailable, cannot be replay-verified, or PCR10 changes before ref commitment, V15 blocks. This deliberately sacrifices availability for continuity.

## 28. Reference quote requirements

Parse binary TPM2B_ATTEST/TPMS_ATTEST and require:

```text
magic = TPM_GENERATED_VALUE
type = TPM_ST_ATTEST_QUOTE
qualifiedSigner = exact AK Name
extraData = exact reference_extra_data
PCR selection = exact V15 selection
PCR digest = independently recomputed exact digest
clockInfo.safe = YES
firmwareVersion exact
```

Bind exact PCR values, clock, resetCount, restartCount, safe, firmwareVersion.

Signature must verify with exact AK public key under ECDSA/SHA256.

## 29. Fresh AK/EK co-residency proof

At platform-attestation admission and again immediately before main-ref lock:

```text
activation_secret = getrandom(32)
MakeCredential(EK public, AK Name, activation_secret)
ActivateCredential(current AK, current EK, generated credential)
require recovered secret == activation_secret byte-for-byte
```

Fresh secret each time; never caller supplied; never stored in success record except optional transcript digest.

Failure/ambiguity blocks.

## 30. V2 Human review as per-request hardware enrollment

No hidden long-lived config selects arbitrary TPM identity.

The exact V2 review enrolls, for this request only:

```text
request/snapshot/nonce
EK certificate digest + EK SPKI digest
AK public digest + AK Name + fixed handle
reference quote digest/full evidence
exact PCR0/2/4/7/10
reference TPM clock/reset/restart/safe/firmware
IMA log digest/record count
out-of-band physical machine/backend facts
```

A different TPM/AK is not auto-enrolled.

## 31. V2 review origin

One distinct GitHub PR review on exact decision PR. Require trusted Human author, non-bot/app/AI, APPROVED, not dismissed, positive review ID, submitted_at, exact body bytes from GitHub.

It must differ from final Human decision review.

Executor cannot create/edit/submit/approve/dismiss it.

## 32. Exact V2 marker

Exact ordered LF-only body:

```text
X1B-PLATFORM-PERSISTENCE-ATTESTATION-V2
decision_request_id=<exact x1b:<request_digest>>
decision_request_sha256=<exact request_digest>
platform_snapshot_len=<exact decimal>
platform_snapshot_sha256=<exact published snapshot digest>
request_attestation_nonce=<64 lowercase hex>
environment_class=bare-metal
virtualization_layer=none
backend_class=physical-acpi-nfit-nvdimm
power_loss_persistence=affirmed
persistence_domain=cpu_cache
deep_flush=0
nfit_format=0x0101
tpm_profile=PHYSICAL_TPM2_ECC_EK_AK_V1
tpm_ek_nv_index=0x01c0000a
tpm_ek_cert_sha256=<64 hex>
tpm_ek_spki_sha256=<64 hex>
tpm_ak_handle=0x8101f515
tpm_ak_public_sha256=<64 hex>
tpm_ak_name=<lowercase hex exact TPM Name>
tpm_reference_quote_sha256=<64 hex>
tpm_quote_pcr0=<64 hex>
tpm_quote_pcr2=<64 hex>
tpm_quote_pcr4=<64 hex>
tpm_quote_pcr7=<64 hex>
tpm_quote_pcr10=<64 hex>
tpm_ima_log_sha256=<64 hex>
tpm_ima_record_count=<canonical positive decimal>
tpm_quote_clock=<canonical unsigned decimal>
tpm_quote_reset_count=<canonical unsigned decimal>
tpm_quote_restart_count=<canonical unsigned decimal>
tpm_quote_safe=1
tpm_quote_firmware_version=<16 lowercase hex>
observation_channel=out-of-band-non-guest
why=<Human one-line rationale>
-----BEGIN X1B-TPM-REFERENCE-EVIDENCE-V15-----
<canonical reference evidence>
-----END X1B-TPM-REFERENCE-EVIDENCE-V15-----
```

Canonical reference evidence contains full preimages of:

```text
EK certificate DER as base64url-no-padding
AK TPMT_PUBLIC bytes as base64url-no-padding
AK Name bytes
TPM2B_ATTEST quote bytes as base64url-no-padding
TPMT_SIGNATURE bytes as base64url-no-padding
normalized PCR values
parsed attestation semantic values
```

Maximum complete V2 review body = 60000 bytes. Larger evidence is unsupported and blocks. No external hidden quote file or truncation.

## 33. V2 validation

Executor must:

```text
refetch request and exact published snapshot
verify request/snapshot len/digests/nonce
refetch/select unique trusted V2 review
parse exact body
re-read current TPM identity/EK cert/AK public+Name
require exact enrolled EK/AK
verify reference quote raw signature/fields/extraData/PCR digest
verify IMA log replay -> PCR10 and bind log digest/count
perform fresh ActivateCredential challenge
reconstruct current PlatformSnapshotV15 byte-for-byte
```

Only then may final Human decision be admitted.

## 34. Live gate nonce / extraData

At each gate generate fresh `gate_nonce=getrandom(32)`.

Closed stage labels:

```text
FINAL_EFFECT_GATE
PRE_OBJECT
PRE_REF_LOCK
PRE_REF_RENAME
POST_EFFECT
```

Define:

```text
gate_extra_data = SHA256(
  "X1B-TPM2-GATE-QUOTE-V15\x00"
  || stage_label
  || request_digest_bytes
  || platform_snapshot_sha256_bytes
  || platform_review_body_sha256_bytes
  || gate_nonce
  || ak_name_bytes
)
```

Gate qualifyingData must equal exact result.

## 35. TPM2_LIVE_GATE_CONTINUITY_V1

Every accepted gate quote must:

```text
verify under exact enrolled AK
qualifiedSigner = exact AK Name
extraData = exact fresh gate_extra_data
PCR selection = SHA256 0,2,4,7,10
PCR values = exact reference values
PCR digest = exact recomputation
firmwareVersion = reference exact
safe = YES
resetCount = reference exact
restartCount = reference exact
clock > previous accepted quote clock
```

Any lifecycle/PCR/clock drift blocks pre-commit and becomes UNCERTAIN if first discovered after material commitment begins.

Replayed quote cannot satisfy fresh gate nonce.

## 36. Reboot/reset/clear semantics

Block on EK/AK replacement, TPM clear/EPS change, reset/restart count drift, firmware drift, PCR drift, safe=0, non-increasing clock, IMA/PCR10 inconsistency.

Any reboot requires a completely new V15 request + snapshot + V2 platform review + final decision.

## 37. Wrong-host / cloned-vTPM rule

Required negatives:

```text
same snapshot on other host -> EK/AK mismatch
same EK cert bytes without EK private key -> ActivateCredential failure
cloned VM + different vTPM -> AK mismatch
old quote copied into VM -> fresh nonce failure
fresh vTPM quote with cloned PCRs -> AK mismatch
wrong request/stage nonce -> extraData mismatch
same host after reboot -> reset/restart/PCR continuity failure
```

Independent review MUST separately attack same-host physical TPM passthrough/proxy. V15 does not claim sysfs or PCR10 alone proves absence of passthrough; the review must determine whether Human no-proxy attestation + non-migratable EK/AK + measured-boot/live continuity closes the bounded claim or creates a new blocker.

# PART V — CURRENTNESS AND FINAL HUMAN DECISION

## 38. V2 currentness

Sequence:

```text
1 request publishes full snapshot + nonce
2 Human inspects exact request + out-of-band host/backend
3 Human submits exact V2 review with reference TPM evidence
4 executor validates V2/current TPM/fresh activation
5 Human submits exact final V15 decision referencing V2 review
6 executor revalidates both + live TPM before effect
```

Require V2 `submitted_at >= request published_at`, V2 before final decision, APPROVED/not dismissed, exact body digest, active request, exact snapshot/nonce, no conflict/supersession.

Freshness remains:

```text
GitHub-server-time - V2.submitted_at <= 900 seconds
```

Freshness is necessary but never replaces live TPM proof.

## 39. V2 uniqueness/conflict

Block on zero/multiple conflicting V2, request/snapshot/nonce mismatch, actor/state/dismissal/staleness failure, EK/AK/reference quote mismatch.

## 40. Final Human marker V15

Only:

```text
X1B-HUMAN-DECISION-V15
decision_request_id=<exact x1b:<request_digest>>
decision_request_sha256=<exact request_digest>
platform_attestation_review_id=<exact GitHub review id>
platform_attestation_sha256=<sha256 exact V2 body>
platform_snapshot_sha256=<exact snapshot digest>
tpm_ak_name=<exact V2 AK Name>
why=<Human one-line rationale>
```

Final decision later than V2 and independently fetched/validated. Neither V2 nor final decision implies the other.

# PART VI — PRESERVED EXT4 DURABILITY

## 41. Internal journal raw predicate preserved

Read exact primary ext4 superblock at offset 1024 from authenticated primary block fd. Require:

```text
magic 0xEF53
HAS_JOURNAL set
s_journal_inum > 0
s_journal_uuid = zero
s_journal_dev = 0
INCOMPAT_JOURNAL_DEV absent
```

External journal unsupported.

## 42. Runtime ext4 state/table preserved

Require statmount `MNT_OPTS`/`OPT_ARRAY`, authenticated `/proc/fs/ext4/<pmemN>/options` full nodefs view and ext4 sysfs journal/error state.

Required durability states include:

```text
rw
barrier
data=ordered OR data=journal
errors=remount-ro
auto_da_alloc
```

Reject prior forbidden tokens including nobarrier/barrier=0, data=writeback, journal_async_commit, noload/norecovery, abort/emergency_ro/shutdown, DAX active, external journal options, alternate superblock, unknown token.

Preserve the complete closed R4R13 option table without implementation discretion.

## 43. EXT4_BARRIERED_FSYNC_DURABILITY_V4

Success requires conjunction of all preserved Linux/ext4 profiles plus:

```text
PUBLISHED_PLATFORM_SNAPSHOT_EVIDENCE_V1
PHYSICAL_TPM2_ECC_EK_AK_V1
TPM2_REQUEST_CHALLENGE_QUOTE_V1
TPM2_MEASURED_BOOT_CONTINUITY_V1
TPM2_LIVE_GATE_CONTINUITY_V1
OUT_OF_BAND_PLATFORM_PERSISTENCE_ATTESTATION_V2
PLATFORM_ATTESTATION_CURRENTNESS_V2
```

All required file/directory fsync calls must succeed.

Claim boundary excludes compromised trusted Human, malicious/failing TPM hardware, kernel compromise, deliberate cryptographic hardware deception, and media failure after acknowledged durability. Ordinary wrong-host/cloned-VM replay is explicitly inside V15 regressions.

# PART VII — PRESERVED GIT/FILESYSTEM CONTROLS

## 44. Namespace/inode profile preserved

Preserve `LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1`, `LINUX_INODE_SEMANTIC_FLAGS_V1`, no casefold, and narrow reviewed inode semantic flags.

## 45. Human-bound loose object mtime preserved

Exact sentinel:

```text
2038-01-18T00:00:00.000000000Z
tv_sec=2147385600
tv_nsec=0
```

Applies to new, pre-existing exact and concurrent winner closure leaves. Require futimens/readback/fsync. Runtime horizon `< 2147385600`.

## 46. Staging/object/index/ref profiles preserved

Preserve:

```text
BOUND_OBJECT_STAGING_NAMESPACE_V2
ALIAS_SAFE_LOOSE_OBJECT_INSTALL_V4
COMPLETE_LOCAL_OBJECT_STORE_V4
FULL_SINGLE_FILE_INDEX_V1
CLOSED_FULL_INDEX_V2_REWRITE_V1
ALIAS_SAFE_RAW_INDEX_REPLACEMENT_V1
PHYSICAL_LOOSE_MAIN_REF_NO_ALIAS_V1
ALIAS_SAFE_FSYNC_LOOSE_REF_CAS_V3
DETERMINISTIC_MAIN_REFLOG_PROJECTION_V2
ALIAS_SAFE_WORKTREE_PROJECTION_V2
CLOSED_RAW_TREE_REWRITE_V1
CLOSED_RAW_COMMIT_OBJECT_V1
NO_REPLACE_NO_LAZY_FETCH_RAW_SHA1_OBJECTS_V2
NO_TRADITIONAL_OR_CONFIGURED_HOOK_EXECUTION_V1
```

No alternates/promisor/lazy fetch/replacement refs/split index/sharedindex/Git authority writer.

# PART VIII — REQUEST / ADMISSION / EFFECT

## 47. DecisionRequestV15

Immutable request binds at least:

```text
schema X1B-DECISION-REQUEST-V15
request id/digest
repository identity
exact ScriptOps baseline HEAD/TREE/security BLOBs
candidate content/scope/old OID/new commit-tree-object closure
index/ref/reflog/worktree projection digests
material-effect digest
primary storage profile
platform_snapshot_len/digest/full exact block
required nfit_format=0x0101
required persistence_domain=cpu_cache
required deep_flush=0
required TPM profile
AK handle=0x8101F515
request_attestation_nonce
V2 platform marker version
platform freshness max=900s
final Human marker V15
```

Request digest covers full snapshot block and nonce. Caller cannot override authority values after publication.

## 48. Platform admission exact order

```text
validate request/currentness
extract/verify published snapshot preimage
reconstruct current snapshot byte-for-byte
refetch/select unique V2 review
validate request/snapshot/nonce/freshness
read current TPM/EK/AK
verify exact enrolled identity
verify reference quote + PCRs + IMA/PCR10
fresh ActivateCredential
fresh live TPM quote
reconstruct snapshot again
```

Only then final Human decision can be considered.

## 49. FinalEffectGateV15

Require all previous predicates plus current request/candidate/scope, proc/userns/credentials, mount, full snapshot, EK/AK identity, fresh activation where specified, fresh TPM quote, exact boot/PCR/clock continuity, V2/final reviews, ext4 internal journal/options/errors, mtime horizon, object/ref/index/reflog/worktree topology, no stale staging, no conflicting committed effect.

## 50. Material sequence

```text
1 validate request + full snapshot
2 validate V2/reference quote
3 fresh AK/EK activation
4 validate final Human decision
5 fresh FINAL_EFFECT_GATE TPM quote
6 prepare/seal/fsync staged loose objects
7 install canonical objects + fsync dirs
8 require zero staging residue/exact closure
9 prepare exact raw index/ref/reflog/worktree projections
10 revalidate full authority
11 fresh PRE_REF_LOCK TPM quote
12 fresh AK/EK activation
13 acquire main-ref CAS lock
14 fresh PRE_REF_RENAME TPM quote
15 refetch V2/final reviews
16 commit main ref + reflog
17 fsync ref/reflog parents
18 install raw index + fsync
19 install worktree + fsync
20 fresh POST_EFFECT TPM quote
21 full post-effect verification
22 SUCCESS only after exact Human-bound truth
```

# PART IX — FAILURE / SUCCESS RECORD

## 51. Failure classification

Before main-ref commitment: no Human-attributed success; snapshot/TPM/review failure blocks.

After material commitment begins: ambiguity or newly discovered continuity failure is `UNCERTAIN / RECOVERY REQUIRED`, never a clean success/failure fiction.

No recovery mutation is authorized.

## 52. Aggregate durability names

```text
CRASH_DURABLE_OBJECT_REF_INDEX_V10
ALIAS_SAFE_MAIN_REF_COMMITMENT_V11
REF_CAS_FIRST_ALIAS_SAFE_RAW_GIT_METADATA_V13
```

V15 additions: published snapshot preimage, random request nonce, Human-reviewed EK/AK/reference quote, fresh activation, fresh gate quotes, PCR/boot/TPM lifecycle continuity.

## 53. Success record V15

Record at least:

```text
request id/digest
snapshot len/digest
V2 review id/body digest/author
final review id/body digest/author
EK cert digest
AK public digest/Name
reference quote digest/PCR0,2,4,7,10/reset/restart
accepted gate quote digests and gate-nonce digests
old/new main OIDs
candidate/effect/object/index/ref/reflog/worktree digests
post-effect result
```

Never store activation secret or TPM private material.

# PART X — MANDATORY REGRESSIONS

## 54. PR #143 F001 regressions

```text
full canonical snapshot published -> prerequisite
request digest-only snapshot -> BLOCK
snapshot absent/truncated/len mismatch/digest mismatch -> BLOCK
field ordering/encoding mismatch -> BLOCK
Human-required raw source hidden behind digest -> BLOCK
current snapshot bytes differ -> BLOCK
V2 review snapshot mismatch -> BLOCK
```

## 55. PR #143 F002 regressions

```text
valid V2 replayed on another host -> EK/AK mismatch BLOCK
V2 copied into VM + different vTPM -> BLOCK
same EK cert bytes without EK private key -> ActivateCredential BLOCK
old quote/new request -> extraData BLOCK
old quote/new gate -> nonce BLOCK
wrong AK -> BLOCK
same snapshot/different TPM -> BLOCK
TPM clear/EPS/AK change -> BLOCK
reset/restart drift -> BLOCK
PCR0/2/4/7/10 drift -> BLOCK
IMA/PCR10 replay inconsistency -> BLOCK
firmware drift -> BLOCK
safe=0 -> BLOCK
non-increasing clock -> BLOCK
invalid signature/qualifiedSigner -> BLOCK
```

Independent review MUST attack physical TPM passthrough/proxy on same host, pre-existing hypervisor, backend swap with preserved guest state, and whether the exact V15 measured-boot/TPM/Human conjunction is sufficient.

## 56. Preserve kernel/ext4 negatives

Preserve all prior negatives for NFIT 0x0201/0x0301, non-cpu_cache, deep_flush=1/missing, external journal, barrier/data mode, DAX, ext4 error, proc overmount, noninitial userns, ID-map, casefold/inode flags.

## 57. Preserve platform sequencing

```text
V2 before request -> BLOCK
V2 after final decision -> BLOCK
stale/dismissed/conflicting V2 -> BLOCK
new V2 without new final decision -> BLOCK
final decision not binding exact V2 id/body -> BLOCK
snapshot/AK enrollment drift -> BLOCK
```

## 58. Preserve object/ref/index negatives

Preserve stale staging, split/shared index, alternates/promisor/lazy fetch, wrong object mtime/bytes, main-ref alias, replacement refs, hooks/filters, lost CAS, and post-ref uncertain projection rules.

# PART XI — EXTERNAL SEMANTICS CHECKED

## 59. TPM sources checked on 2026-09-02

```text
TCG TPM 2.0 Library Version 185
https://trustedcomputinggroup.org/resource/tpm-library-specification/

TCG EK Credential Profile TPM 2.0 Version 2.7
https://trustedcomputinggroup.org/resource/http-trustedcomputinggroup-org-wp-content-uploads-tcg-ek-credential-profile/

TPM2 quote/checkquote
https://tpm2-tools.readthedocs.io/en/latest/man/tpm2_quote.1/
https://tpm2-tools.readthedocs.io/en/latest/man/tpm2_checkquote.1/

TPM2 makecredential/activatecredential
https://tpm2-tools.readthedocs.io/en/latest/man/tpm2_makecredential.1/
https://tpm2-tools.readthedocs.io/en/stable/man/tpm2_activatecredential.1/
```

`tpm2-tools` textual stdout is never authority. Future implementation must parse/verify binary TPM/X.509 evidence under exact V15 schema; a tool may be command transport only.

## 60. Linux/NFIT semantics preserved

Continue current reviewed semantics for `persistence_domain`, `deep_flush`, and NFIT FIC 0x0101/0x0201/0x0301. R4R15 does not reopen them.

# PART XII — INDEPENDENT REVIEW CHECKLIST

## 61. Independent R4R15 review must answer at least

```text
Is complete PlatformSnapshotV15 preimage really in immutable request?
Can any Human-required raw value remain hidden behind a digest?
Can GitHub/Markdown normalization change canonical bytes?
Do size bounds prevent truncation?
Does V2 bind exact request/snapshot/random nonce?
Is EK certificate read from exact current TPM and matched to EK public?
Is AK exact fixedTPM/fixedParent restricted P-256 signing key?
Does quote qualifiedSigner equal AK Name?
Does extraData bind exact request/snapshot/nonce?
Are signature/PCR digest independently verified?
Is PCR10 continuity machine-only rather than an opaque Human semantic premise?
Does ActivateCredential prove current AK/EK co-residency?
Can another host reproduce AK private identity?
Can cloned vTPM satisfy live gate?
Can old quote satisfy fresh nonce?
Do reboot/reset/clear invalidate continuity?
Can same-host physical TPM passthrough/proxy still satisfy every predicate after VM substitution?
Can backend swap occur without snapshot/TPM continuity drift?
Are R4R14 NFIT persistence corrections preserved?
Are R4R13 internal-journal/option corrections preserved?
Are all prior object/ref/index/reflog/worktree controls preserved?
```

## 62. Intended predecessor-finding disposition target

If no new blocker is found, R4R15 intends to support:

```text
R4R14 F001 OPAQUE PLATFORM SNAPSHOT = ADDRESSED AT BRIEF LEVEL
R4R14 F002 TRANSFERABLE ATTESTATION = ADDRESSED AT BRIEF LEVEL FOR WRONG-HOST / CLONED-vTPM REPLAY
```

This is not a predeclared PASS. Same-host physical TPM proxy/passthrough is explicitly review-required.

# PART XIII — STOP

## 63. Explicit non-authority

This brief does not authorize:

```text
independent R4R15 review under same accept
ScriptOps implementation
TPM AK provisioning/persistence
TPM clear/NV/hierarchy mutation
platform V2 Human review creation
final Human V15 review creation
positive control
canonical effect
recovery
merge
X1B closure
V1 authority
release/deployment/tag
```

## 64. Next legal step

After exact R4R15 brief is frozen in one draft PR, STOP.

```text
fresh Human authorization
-> exactly one independent AK-CANON adversarial review
   of exact frozen R4R15 implementation brief
```

Preserve:

```text
AI PROPOSES != HUMAN DECIDES
REVIEW FINDING != REPAIR AUTHORITY
R4R15 BRIEF != IMPLEMENTATION AUTHORITY
R4R15 REVIEW PASS != IMPLEMENTATION AUTHORITY
X1B OPEN != V1 AUTHORITY
```
