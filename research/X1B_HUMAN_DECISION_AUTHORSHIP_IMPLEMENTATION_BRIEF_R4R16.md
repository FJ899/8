# X1B HUMAN DECISION AUTHORSHIP — CLEAN IMPLEMENTATION BRIEF R4R16

Status: `CLEAN R4R16 CORRECTIVE BRIEF / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-02`

## 1. Authority, purpose, and STOP boundary

This is the self-contained successor implementation brief after independent AK-CANON review PR #145 returned `NOT PASS` on R4R15.

R4R16 preserves the accepted X1B corrective-design contract and every earlier brief-level correction not rejected by PR #145. It corrects exactly:

```text
X1B-R4R15-IBR-F001 — TPMS_ATTEST qualifiedSigner bound to AK Name instead of AK Qualified Name
X1B-R4R15-IBR-F002 — EK certificate trust path / trust anchor not frozen or validated
```

New authority-critical profiles:

```text
AK_NAME_QUALIFIED_NAME_SEPARATION_V1
INFINEON_SLB9670_FW7_87_ECC_EK_PKI_V1
PLATFORM_ATTESTATION_V3
```

Positive V16 requires all of:

```text
published complete Human-reviewable PlatformSnapshotV16
exact current physical TPM/EK/AK identity
correct ordinary AK Name semantics
correct AK Qualified Name semantics
TPMS_ATTEST.qualifiedSigner == AK Qualified Name
MakeCredential objectName == ordinary AK Name
pinned exact Infineon OPTIGA ECC Root CA
single CA085 intermediate path
exact SLB 9670 / FW7.87 EK leaf profile
stapled offline leaf/intermediate revocation evidence
X.509/CRL validation at GitHub V3 review submitted_at
fresh request/gate quotes and fresh AK/EK credential activation
separate trusted Human V3 platform act
separate trusted Human final V16 decision act
```

No system trust store, runtime AIA/OCSP/CRL lookup, caller-supplied CA, or implementation-selected trust root is authority.

Same-host physical-TPM passthrough/proxy remains an explicit independent-review attack surface. R4R16 does not predeclare that surface closed.

This brief authorizes no ScriptOps mutation, independent R4R16 review, TPM provisioning, Human platform review, Human final decision, positive control, canonical effect, recovery, merge, X1B closure, V1 authority, release, deployment, or tag.

```text
R4R16 BRIEF != IMPLEMENTATION AUTHORITY
R4R16 REVIEW PASS != IMPLEMENTATION AUTHORITY
AI PROPOSES != HUMAN DECIDES
AK Name != AK Qualified Name
EK LEAF SPKI MATCH != AUTHENTICATED EK CREDENTIAL
```

After exact durable freeze of this brief, STOP. Next legal stage: one separately Human-authorized independent AK-CANON review of this exact artifact.

## 2. Exact governance lineage

Accepted corrective design:

```text
FJ899/scriptops PR #34
HEAD = d7a5065c87e9a4b49fb608235c908bceac42b4b1
TREE = 3140d0ac95c120a7b1532942bae2e0dad38b4839
PATH = governance/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_CANDIDATE.md
BLOB = dac16f109d1414a2208c2ed9a166ae9e9a329216
```

Independent corrective-design review:

```text
FJ899/8 PR #109
HEAD = 132d65be48331a822039262b707c47a81d02a64d
TREE = a8bdc363d293beb7b15ae8b787cc3ebdd694fd99
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_DESIGN_AK_CANON_REVIEW_R2.md
BLOB = 439109e104244552a5ac1f3f08988dba283733d0
VERDICT = PASS
```

R4R15 predecessor:

```text
FJ899/8 PR #144
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 5cb4c0e650e648efab844f08ddd4be7cc9b2d0c3
TREE = ade1f1db4b52ea0e75cedea17af29f92fcfc0d4b
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R15.md
BLOB = 341eb23b5d185eeb2f91f7035fc12280753ca301
```

Binding R4R15 review:

```text
FJ899/8 PR #145
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 84b91d2f53a520be16eb62ec805e6c5e89c48ab9
TREE = d422bc3100432fc1b23f3fc5b2598a5919bb9a48
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R15_AK_CANON_REVIEW.md
BLOB = 17facc8abbdb5ce7c5977f3d069c1230e1aac5aa
VERDICT = NOT PASS
```

PR #145 also records:

```text
R4R14 opaque snapshot finding = addressed at brief level
simple wrong-host / different-vTPM replay = materially addressed
same-host physical TPM passthrough/proxy = continuing mandatory attack surface
```

Preserved higher-level contract:

```text
separate trusted Human decision act
exact content/scope/candidate/effect binding
freshness/activity/supersession/conflict/replay semantics
executor no-substitution
fail closed on ambiguity
real-boundary negatives
separately authorized positive Human control
post-effect truth matching Human-bound effect
no durable successful Human attribution for failed/uncertain operation
no core security/authority choice implicit
```

## 3. Exact repository state before preparation

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

Historical prototype reconstruction SHA-256 remains `881dade6c6c506b9a9d41ebfbf68afb18b66db7583d35f746fb29ed7b36ac596`, size `51980`.

## 4. Normative precedence / V16 migration

```text
R4R16 TEXT = CURRENT IMPLEMENTATION-BRIEF AUTHORITY
R4R15 AND EARLIER BRIEFS = HISTORICAL INPUT ONLY
CORRECTIVE DESIGN PR #34 = HIGHER-LEVEL PROPERTY CONTRACT
```

V16 changes:

```text
Name and Qualified Name are different schema types
ordinary AK Name is independently derived from exact TPMT_PUBLIC
AK Qualified Name is separately returned/bound
quote qualifiedSigner compares only to AK Qualified Name
MakeCredential objectName remains ordinary AK Name
reference/gate extraData bind both identities
V3 Human marker binds both identities
root CA bytes are frozen constants
only exact Infineon SLB9670 FW7.87 / CA085 path is supported
path and CRLs are complete bounded Human-reviewable V3 evidence
certificate/CRL time source is GitHub V3 review metadata submitted_at
no runtime PKI discovery/network/store authority
```

V15 and earlier request/review/decision evidence is invalid for V16.

# PART I — CORE HUMAN RULE

## 5. HumanDecision

```text
HumanDecision = TRUE
ONLY IF
separate trusted Human final V16 decision
for exact content + scope + candidate + material effect
AND exact current independently validated PlatformAttestationV3.
```

Never sufficient alone:

```text
approve command possession
non-empty rationale
caller identity
silence/continuation
AI record
CI success
mergeability
successful fsync
guest ACPI/NFIT appearance
snapshot digest without preimage
Human platform marker without live TPM proof
TPM quote without authenticated EK credential path
leaf cert matching EK without trusted path
AK Name where Qualified Name is required
```

## 6. Future bounded implementation surface

Expected future changed surface exactly:

```text
phase6/scriptops-v2-hardening.py
legacy/scriptops-v2-single.py
phase6/x1b_human_decision.py
phase6/x1b_tpm_attestation.py
phase6/x1b_ek_pki.py
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
tests/test_x1b_ek_pki.py
.github/workflows/x1b-human-decision.yml
```

No TPM private material, hierarchy secret, Human credential, or persistent provisioning secret may be committed.

No TPM clear, hierarchy-auth change, persistent-key creation/eviction, NV mutation, or intentional PCR mutation is authorized. Required pre-existing AK absence/incompatibility means `BLOCKED`.

# PART II — PRESERVED STORAGE / SNAPSHOT AUTHORITY

## 7. Supported storage profile

Preserve exact predecessor constraints for:

```text
Git 2.55.0 <= version < 2.56.0
SHA-1 object format
files ref backend
Linux/ext4
whole direct /dev/pmem<N>
ACPI.NFIT PMEM
nfit/format = 0x0101
persistence_domain = cpu_cache
deep_flush = 0
initial user namespace
identity uid/gid maps
non-ID-mapped ext4
AUTHENTIC_CURRENT_TASK_PROCFS_V1
authenticated sysfs
internal ext4 journal
barrier enabled
data=ordered or data=journal
journal_async_commit absent
DAX disabled
ext4 errors_count=0
```

Preserve the complete earlier rejection set for volatile/software/network/virtual/test/unknown block stacks, partitions, BTT/PFN/DAX chars, NFIT health/topology drift, proc/sysfs overmounts, noninitial userns, ID maps, casefold and unsupported inode flags.

## 8. Published PlatformSnapshotV16

Preserve the R4R15 correction: complete canonical snapshot bytes are published inside immutable `DecisionRequestV16`; no Human-required raw authority value may exist only behind a digest.

Each raw Human-review-required field uses:

```text
<field>.raw_len=<decimal>
<field>.raw_hex=<full lowercase even-length bytes>
<field>.semantic=<canonical semantic>
```

Bounds:

```text
mappings <= 16
mapped nmem <= 16
one raw snapshot value <= 4096 bytes
PlatformSnapshotV16 <= 32768 bytes
DecisionRequestV16 <= 60000 bytes
```

No truncation/external hidden preimage fallback.

# PART III — PR #145 F001: NAME / QUALIFIED NAME

## 9. Required AK

Persistent handle:

```text
AK_HANDLE = 0x8101F515
```

Exact public profile:

```text
ECC NIST P-256
nameAlg=SHA256
scheme=ECDSA/SHA256
fixedTPM=1
fixedParent=1
sensitiveDataOrigin=1
restricted=1
sign/encrypt=1
decrypt=0
```

`TPM2_ReadPublic(AK_HANDLE)` must return exact:

```text
TPMT_PUBLIC ak_public
TPM2B_NAME ak_name_returned
TPM2B_NAME ak_qualified_name_returned
```

## 10. Ordinary AK Name

Define typed value `AK_NAME` only as ordinary TPM Name.

Require `nameAlg = TPM_ALG_SHA256 (0x000B)` and independently compute:

```text
AK_NAME = UINT16_BE(0x000B) || SHA256(canonical TPMT_PUBLIC wire bytes)
```

Hash input is `TPMT_PUBLIC`, excluding the outer `TPM2B_PUBLIC.size` field.

Require:

```text
len(AK_NAME)=34
ak_name_returned == AK_NAME
```

Mismatch blocks.

## 11. AK Qualified Name

Define separate typed value:

```text
AK_QUALIFIED_NAME = exact ak_qualified_name_returned
```

Require:

```text
len(AK_QUALIFIED_NAME)=34
first two bytes = UINT16_BE(0x000B)
```

The exact value is bound in request/reference/V3/final evidence and re-read before material commitment.

No implementation may reinterpret `name` as either Name or Qualified Name based on context.

## 12. Correct quote signer predicate

Every reference and live quote must satisfy:

```text
TPMS_ATTEST.magic = TPM_GENERATED_VALUE
TPMS_ATTEST.type = TPM_ST_ATTEST_QUOTE
TPMS_ATTEST.qualifiedSigner == AK_QUALIFIED_NAME
```

Explicit negative:

```text
qualifiedSigner == AK_NAME while AK_NAME != AK_QUALIFIED_NAME -> BLOCK
```

ECDSA/SHA256 verification under `ak_public` is separately mandatory.

## 13. Correct MakeCredential predicate

The fresh co-residency challenge uses ordinary Name:

```text
MakeCredential(authenticated_EK_public, AK_NAME, activation_secret)
ActivateCredential(current_AK,current_EK,...)
```

It is forbidden to substitute `AK_QUALIFIED_NAME` into the credentialed object Name.

Normative split:

```text
Quote.qualifiedSigner -> AK_QUALIFIED_NAME
MakeCredential.objectName -> AK_NAME
```

# PART IV — PR #145 F002: PINNED EK PKI

## 14. Exact supported profile

Only:

```text
INFINEON_SLB9670_FW7_87_ECC_EK_PKI_V1
```

Required TPM manufacturer:

```text
TPM_PT_MANUFACTURER = 0x49465800  # IFX\0
```

Required EK:

```text
TPM2 low-range ECC NIST P-256 EK
NV EK certificate index = 0x01C0000A
TCG default low-range ECC P-256 EK template
nameAlg=SHA256
current EK public point == authenticated leaf SPKI public point
```

Other manufacturer/model/FW/root/index profiles block.

## 15. Frozen root trust anchor

Profile id:

```text
INFINEON_OPTIGA_ECC_ROOT_CA_V1
```

Exact root properties:

```text
subject = C=DE,O=Infineon Technologies AG,OU=OPTIGA(TM) Devices,CN=Infineon OPTIGA(TM) ECC Root CA
issuer = same
serial = 4
notBefore = 2013-07-26T00:00:00Z
notAfter = 2043-07-25T23:59:59Z
public key = EC secp384r1
self signature = ECDSA/SHA384
DER length = 607
DER SHA-256 = cfeb02fecd55ad7a73c6e1d11985d4c47dee248ab63dcb66091a2489660443c3
SPKI SHA-256 = ce5183a19d6fe79a6c1b058cfa700379f67d587a8afd0f51621e82d9f00c5a28
SKI = b41885c84a4ac5127af24039dec4f58b1e7e4ad1
BasicConstraints critical CA=TRUE
KeyUsage critical keyCertSign,cRLSign
```

Exact DER base64 (no PEM armor):

```text
MIICWzCCAeKgAwIBAgIBBDAKBggqhkjOPQQDAzB3MQswCQYDVQQGEwJERTEh
MB8GA1UECgwYSW5maW5lb24gVGVjaG5vbG9naWVzIEFHMRswGQYDVQQLDBJP
UFRJR0EoVE0pIERldmljZXMxKDAmBgNVBAMMH0luZmluZW9uIE9QVElHQShU
TSkgRUNDIFJvb3QgQ0EwHhcNMTMwNzI2MDAwMDAwWhcNNDMwNzI1MjM1OTU5
WjB3MQswCQYDVQQGEwJERTEhMB8GA1UECgwYSW5maW5lb24gVGVjaG5vbG9n
aWVzIEFHMRswGQYDVQQLDBJPUFRJR0EoVE0pIERldmljZXMxKDAmBgNVBAMM
H0luZmluZW9uIE9QVElHQShUTSkgRUNDIFJvb3QgQ0EwdjAQBgcqhkjOPQIB
BgUrgQQAIgNiAAQm1HxLVgvAu1q2GM+ymTz12zdTEu0JBVG9CdsVEJv/pE7p
SWOlsG3YwU792YAvjSy7zL+WtDK40KGeOm8bSWt46QJ00MQUkYxz6YqXbb14
BBr06hWD6u6IMBupNkPd9pKjQjBAMB0GA1UdDgQWBBS0GIXISkrFEnryQDne
xPWLHn5K0TAOBgNVHQ8BAf8EBAMCAAYwDwYDVR0TAQH/BAUwAwEB/zAKBggq
hkjOPQQDAwNnADBkAjA6QZcV8DjjbPuKjKDZQmTRywZkMAn8wE6kuW3EouVv
Bt+/2O+szxMe4vxj8R6TDCYCMG7c9ov86ll/jDlJb/q0L4G++O3Bdel9P5+c
OgzIGANkOPEzBQM3VfJegfnriT/kaA==
```

Future implementation embeds these exact bytes and self-checks DER/SPKI hashes before admitting any request.

No automatic root rotation. Any root change requires new Human-authorized governance.

## 16. Exact CA085 path

Accepted path length is exactly 3:

```text
EK leaf
-> Infineon OPTIGA(TM) TPM 2.0 ECC CA 085
-> pinned INFINEON_OPTIGA_ECC_ROOT_CA_V1
```

The complete intermediate DER is included in the Human-reviewable V3 reference evidence.

Intermediate rules:

```text
subject CN = Infineon OPTIGA(TM) TPM 2.0 ECC CA 085
subject O = Infineon Technologies AG
subject OU = OPTIGA(TM)
subject C = DE
issuer == pinned root subject
BasicConstraints CA=TRUE
KeyUsage includes keyCertSign,cRLSign
pathLen absent or 0
signature verifies under pinned root
signature hash SHA-256 or SHA-384 only
unknown critical extension -> BLOCK
```

No cross cert, extra intermediate, alternate path, system root, AIA-fetched cert, or caller-selected issuer.

## 17. Exact EK leaf profile

Read complete DER leaf from current TPM NV `0x01C0000A`.

Require:

```text
X.509 v3
positive serial
issuer == exact CA085 subject
signature verifies under exact supplied CA085 certificate
signature hash SHA-256 or SHA-384 only
BasicConstraints critical CA=FALSE
KeyUsage critical and keyAgreement=TRUE
EKU present and exactly contains 2.23.133.8.1 (tcg-kp-EKCertificate)
TCG SubjectAlternativeName directoryName present
unknown critical extension -> BLOCK
SPKI = ECC P-256
current EK public point == leaf SPKI point
```

Required TCG SAN semantic values:

```text
2.23.133.2.1 TPMManufacturer = id:49465800
2.23.133.2.2 TPMModel = SLB 9670 TPM2.0
2.23.133.2.3 TPMVersion = id:0757
```

If present, AIA/CDP must be consistent with CA085:

```text
/OptigaEccMfrCA085/OptigaEccMfrCA085.crt
/OptigaEccMfrCA085/OptigaEccMfrCA085.crl
```

Those URIs are consistency data only; executor never follows them.

## 18. Trusted PKI validation time — no circular marker field

After fetching the accepted GitHub V3 review, define internally:

```text
PKI_VALIDATION_TIME := exact immutable GitHub review metadata submitted_at
```

`PKI_VALIDATION_TIME` is NOT a Human-authored body field and MUST NOT appear as a value the Human has to predict before submission.

Use that exact UTC instant for root/intermediate/leaf certificate validity and stapled CRL validity.

Require:

```text
certificate.notBefore <= PKI_VALIDATION_TIME <= certificate.notAfter
```

Forbidden time authority:

```text
caller input
local wall clock alone
file mtime
certificate-derived guessed time
ad-hoc network time
```

V3 review freshness remains separately evaluated against current GitHub server time with max age 900 seconds.

## 19. Offline revocation profile

No runtime OCSP/AIA/CRL network lookup.

V3 evidence staples exactly:

```text
LEAF_STATUS_CRL = CA085-issued CRL for EK leaf serial
INTERMEDIATE_STATUS_CRL = pinned-root-issued CRL for CA085 serial
```

Each CRL:

```text
complete DER evidence
DER <= 16384 bytes
SHA-256 bound in V3 marker
issuer exact
signature verifies under expected issuer certificate
signature hash SHA-256 or SHA-384 only
thisUpdate <= PKI_VALIDATION_TIME < nextUpdate
nextUpdate required
indirect CRL unsupported
delta CRL unsupported
unknown critical CRL extension -> BLOCK
```

Require:

```text
leaf serial absent from LEAF_STATUS_CRL revokedCertificates
CA085 serial absent from INTERMEDIATE_STATUS_CRL revokedCertificates
```

Pinned root is a governance trust anchor and is not dynamically replaced/revoked by an OS store. Root removal/rotation is a new governance act.

Missing/stale/invalid/oversized CRL or listed serial => `BLOCKED`.

## 20. Closed path algorithm

Executor does exactly:

```text
1 parse embedded pinned root and self-check exact DER/SPKI hashes
2 parse exactly one V3 CA085 intermediate
3 parse exact current EK leaf from TPM NV
4 require leaf issuer == intermediate subject
5 require intermediate issuer == pinned root subject
6 verify leaf signature under intermediate
7 verify intermediate signature under pinned root
8 enforce all certificate constraints/SAN/critical extensions
9 set PKI_VALIDATION_TIME from GitHub review submitted_at metadata
10 validate all certificate validity intervals at that instant
11 parse/verify two stapled CRLs at that instant
12 require leaf and CA085 serials unrevoked
13 require current EK P-256 point == authenticated leaf SPKI point
```

No generic PKIX path search.

No `/etc/ssl`, NSS/browser store, environment variable, AIA, DNS, HTTP, caller root or unreviewed CA may enter the algorithm.

## 21. PKI evidence bounds

```text
leaf DER <= 8192 bytes
CA085 DER <= 8192 bytes
leaf CRL DER <= 16384 bytes
intermediate CRL DER <= 16384 bytes
pinned root DER = 607 bytes
complete V3 review body <= 60000 UTF-8 bytes
```

Evidence too large => unsupported/BLOCK; no truncation or hidden attachment fallback.

# PART V — TPM LIVE CONTINUITY

## 22. Physical TPM gate

Preserve authenticated `/dev/tpm0`, `/dev/tpmrm0`, `/sys/class/tpm/tpm0`, char-device rdev/sysfs topology, manufacturer/firmware/revision binding and rejection of exposed `tpm_vtpm_proxy`, `/dev/vtpmx`, Xen/software/known virtual TPM or unknown topology.

Absence of virtualization markers is never positive authority by itself.

## 23. Request nonce / reference quote

Request construction generates exactly 32 bytes using Linux `getrandom()`; caller cannot supply it.

Reference domain:

```text
X1B-TPM2-REFERENCE-QUOTE-V16\x00
```

Reference extraData:

```text
SHA256(
 domain
 || request_digest
 || platform_snapshot_sha256
 || request_attestation_nonce
 || AK_NAME
 || AK_QUALIFIED_NAME
 || ek_leaf_der_sha256
 || pinned_root_der_sha256
)
```

Quote qualifyingData must equal exact 32-byte result.

## 24. PCR / IMA continuity

Exact SHA-256 PCR selection remains:

```text
0,2,4,7,10
```

PCR10 is continuity-only, never a semantic bare-metal proof.

Require authenticated securityfs IMA log and replayed SHA-256 PCR10 exactly equal current TPM PCR10; bind IMA log SHA-256 and record count. Failure/drift blocks pre-commit.

## 25. Reference quote validation

Require:

```text
magic = TPM_GENERATED_VALUE
type = TPM_ST_ATTEST_QUOTE
qualifiedSigner = AK_QUALIFIED_NAME
extraData = exact reference extraData
PCR selection = exact SHA256 0,2,4,7,10
PCR digest independently recomputed
safe=YES
firmwareVersion exact
ECDSA/SHA256 signature valid under exact AK public
```

Bind PCR values, clock, resetCount, restartCount, safe, firmwareVersion, AK_NAME and AK_QUALIFIED_NAME.

## 26. Fresh AK/EK co-residency

At V3 admission and immediately before main-ref lock:

```text
activation_secret = getrandom(32)
MakeCredential(authenticated current EK public, AK_NAME, activation_secret)
ActivateCredential(current AK,current EK,...)
recovered == activation_secret
```

Fresh secret every time. Caller cannot supply it. Never store secret in success evidence.

## 27. Live gate quotes

Fresh 32-byte `gate_nonce=getrandom()` at each closed stage:

```text
FINAL_EFFECT_GATE
PRE_OBJECT
PRE_REF_LOCK
PRE_REF_RENAME
POST_EFFECT
```

Gate extraData binds:

```text
stage label
request digest
snapshot digest
V3 body digest
gate nonce
AK_NAME
AK_QUALIFIED_NAME
EK leaf digest
```

Every gate quote requires:

```text
valid exact AK signature
qualifiedSigner == AK_QUALIFIED_NAME
fresh exact extraData
PCR 0,2,4,7,10 == reference
PCR digest exact
firmware == reference
safe=YES
resetCount/restartCount == reference
clock strictly increasing
```

Reboot/reset/clear/EPS/AK/EK/path/profile/PCR/IMA/firmware/safe/clock drift blocks pre-commit; any reboot requires new request + V3 + final V16 decision.

# PART VI — HUMAN PLATFORM V3

## 28. V3 origin / sequencing

Exactly one unique trusted Human APPROVED GitHub PR review on the exact decision PR, distinct from final Human review, not dismissed, non-bot/app/AI, exact body bytes fetched from GitHub.

Sequence:

```text
request published
Human inspects exact request + out-of-band machine/backend + complete bounded TPM/PKI evidence
Human submits V3
executor gets immutable V3 metadata submitted_at
executor validates PKI at that submitted_at and validates live TPM
Human submits final V16 decision referencing exact V3
executor revalidates both before effect
```

Executor cannot create/edit/approve/dismiss either Human authority act.

## 29. Exact V3 marker

Exact ordered LF-only body:

```text
X1B-PLATFORM-PERSISTENCE-ATTESTATION-V3
decision_request_id=<x1b:request_digest>
decision_request_sha256=<request_digest>
platform_snapshot_len=<decimal>
platform_snapshot_sha256=<digest>
request_attestation_nonce=<64 hex>
environment_class=bare-metal
virtualization_layer=none
backend_class=physical-acpi-nfit-nvdimm
power_loss_persistence=affirmed
persistence_domain=cpu_cache
deep_flush=0
nfit_format=0x0101
tpm_profile=PHYSICAL_TPM2_ECC_EK_AK_V2
ek_pki_profile=INFINEON_SLB9670_FW7_87_ECC_EK_PKI_V1
ek_root_profile=INFINEON_OPTIGA_ECC_ROOT_CA_V1
ek_root_der_sha256=cfeb02fecd55ad7a73c6e1d11985d4c47dee248ab63dcb66091a2489660443c3
ek_root_spki_sha256=ce5183a19d6fe79a6c1b058cfa700379f67d587a8afd0f51621e82d9f00c5a28
ek_intermediate_der_sha256=<64 hex>
ek_leaf_der_sha256=<64 hex>
ek_leaf_status_crl_sha256=<64 hex>
ek_intermediate_status_crl_sha256=<64 hex>
tpm_ek_nv_index=0x01c0000a
tpm_ek_spki_sha256=<64 hex>
tpm_ak_handle=0x8101f515
tpm_ak_public_sha256=<64 hex>
tpm_ak_name=<68 lowercase hex>
tpm_ak_qualified_name=<68 lowercase hex>
tpm_reference_quote_sha256=<64 hex>
tpm_quote_pcr0=<64 hex>
tpm_quote_pcr2=<64 hex>
tpm_quote_pcr4=<64 hex>
tpm_quote_pcr7=<64 hex>
tpm_quote_pcr10=<64 hex>
tpm_ima_log_sha256=<64 hex>
tpm_ima_record_count=<positive decimal>
tpm_quote_clock=<unsigned decimal>
tpm_quote_reset_count=<unsigned decimal>
tpm_quote_restart_count=<unsigned decimal>
tpm_quote_safe=1
tpm_quote_firmware_version=<16 lowercase hex>
observation_channel=out-of-band-non-guest
why=<Human one-line rationale>
-----BEGIN X1B-TPM-PKI-REFERENCE-EVIDENCE-V16-----
<canonical bounded evidence>
-----END X1B-TPM-PKI-REFERENCE-EVIDENCE-V16-----
```

There is deliberately NO Human-authored `pki_validation_time=` field. The only validation time is immutable GitHub `submitted_at` metadata obtained after submission.

## 30. V3 evidence preimages

Complete bounded evidence contains:

```text
EK leaf DER base64url-no-padding
CA085 DER base64url-no-padding
leaf-status CRL DER base64url-no-padding
intermediate-status CRL DER base64url-no-padding
AK TPMT_PUBLIC bytes
AK_NAME bytes
AK_QUALIFIED_NAME bytes
TPM2B_ATTEST bytes
TPMT_SIGNATURE bytes
PCR values
parsed attestation semantics
parsed X.509 semantics
parsed CRL semantics
```

Pinned root is already exact normative bytes; V3 binds root DER/SPKI hashes.

No hidden external file or network-only evidence.

## 31. V3 validation order

```text
1 request/snapshot/nonce exact
2 V3 unique/trusted/APPROVED/current
3 PKI_VALIDATION_TIME := V3 GitHub submitted_at metadata
4 pinned root self-check
5 exact path + X.509 constraints + validity at submitted_at
6 exact two CRLs + revocation at submitted_at
7 current EK point == authenticated leaf SPKI
8 current AK public exact; recompute AK_NAME
9 read/bind AK_QUALIFIED_NAME
10 reference quote qualifiedSigner == AK_QUALIFIED_NAME
11 PCR/IMA/lifecycle exact
12 fresh ActivateCredential using AK_NAME
13 current snapshot byte-for-byte exact
```

V3 max age remains 900 seconds by current GitHub server time. Freshness never replaces PKI or TPM verification.

# PART VII — FINAL HUMAN V16

## 32. Final marker

Only:

```text
X1B-HUMAN-DECISION-V16
decision_request_id=<x1b:request_digest>
decision_request_sha256=<request_digest>
platform_attestation_review_id=<exact V3 review id>
platform_attestation_sha256=<sha256 exact V3 body>
platform_snapshot_sha256=<digest>
ek_leaf_der_sha256=<exact V3 leaf digest>
tpm_ak_name=<AK_NAME>
tpm_ak_qualified_name=<AK_QUALIFIED_NAME>
why=<Human one-line rationale>
```

Final review must be later than V3 and independently fetched/validated. New V3 requires new final Human decision.

# PART VIII — PRESERVED EXT4 / OBJECT / REF DURABILITY

## 33. Internal ext4 journal

Preserve exact raw primary-superblock predicate:

```text
magic=0xEF53
HAS_JOURNAL set
s_journal_inum>0
s_journal_uuid=zero
s_journal_dev=0
INCOMPAT_JOURNAL_DEV absent
```

External journal unsupported.

## 34. Runtime ext4 state

Preserve complete closed R4R13 option table and authenticated statmount/proc/ext4-sysfs sources.

Required includes:

```text
rw
barrier
data=ordered OR data=journal
errors=remount-ro
auto_da_alloc
```

Preserve prior forbidden nobarrier/writeback/async-commit/noload/recovery-abort/emergency/shutdown/DAX/external-journal/alternate-sb/debug/test-encryption/unknown states.

## 35. Human-bound loose-object mtime

Preserve exact sentinel:

```text
2038-01-18T00:00:00.000000000Z
tv_sec=2147385600
tv_nsec=0
```

Final metadata before fsync, exact readback, directory fsync ordering unchanged.

## 36. Git/filesystem profiles

Preserve exactly:

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

No alternates/promisor/lazy fetch/replacement refs/split/shared index/Git authority writer.

Canonical commitment remains durable main-ref CAS. Post-ref projections must be durably verified before complete success. Uncertain post-commit truth is never reported as clean success.

# PART IX — REQUEST / EFFECT

## 37. DecisionRequestV16

Immutable request binds at least:

```text
schema X1B-DECISION-REQUEST-V16
request id/digest
repository identity
baseline HEAD/TREE/security BLOBs
candidate content/scope/object/tree/commit closure
old/new main OIDs
index/ref/reflog/worktree projection digests
material-effect digest
full PlatformSnapshotV16 bytes + len/digest
nfit_format=0x0101
persistence_domain=cpu_cache
deep_flush=0
TPM profile V2
EK PKI profile INFINEON_SLB9670_FW7_87_ECC_EK_PKI_V1
pinned root DER/SPKI hashes
AK handle 0x8101F515
request attestation nonce
V3 platform marker version
V3 max age 900s
final Human marker V16
```

Caller cannot override authority values after publication.

## 38. FinalEffectGateV16

Requires every prior predicate current: request/candidate/scope, proc/userns/credentials, mount/storage/snapshot, pinned root/path/CRLs, current EK/AK, correct Name/QName, fresh quote/activation, PCR/IMA/lifecycle, V3/final Human evidence, ext4 journal/options/errors, mtime horizon, object/ref/index/reflog/worktree topology and no conflicting effect.

## 39. Material sequence

```text
1 validate request + full snapshot
2 select V3; derive PKI_VALIDATION_TIME from GitHub submitted_at
3 validate pinned root/path/cert validity/CRLs/revocation
4 read EK/AK; authenticate EK leaf; recompute AK_NAME; bind AK_QUALIFIED_NAME
5 verify reference quote signer == AK_QUALIFIED_NAME
6 fresh ActivateCredential using AK_NAME
7 validate final Human decision
8 fresh FINAL_EFFECT_GATE quote
9 prepare/seal/fsync objects
10 install canonical objects + fsync dirs
11 exact closure / zero staging residue
12 prepare raw projections
13 full authority revalidation
14 fresh PRE_REF_LOCK quote
15 fresh ActivateCredential using AK_NAME
16 acquire main-ref CAS lock
17 fresh PRE_REF_RENAME quote
18 refetch V3/final Human evidence
19 durable main-ref/reflog commitment
20 durable raw index/worktree projections
21 fresh POST_EFFECT quote
22 full post-effect truth verification
23 SUCCESS only after exact Human-bound truth
```

Before main-ref commitment, PKI/TPM/snapshot/review failure blocks with no Human-attributed success. After material commitment begins, new ambiguity is `UNCERTAIN / RECOVERY REQUIRED`; no recovery mutation is authorized here.

# PART X — MANDATORY REGRESSIONS

## 40. F001 Name/QName regressions

```text
AK Name recomputation mismatch -> BLOCK
AK Qualified Name absent/malformed -> BLOCK
quote qualifiedSigner == AK_NAME but not AK_QUALIFIED_NAME -> BLOCK
quote qualifiedSigner != AK_QUALIFIED_NAME -> BLOCK
correct Qualified Name signer -> prerequisite only
MakeCredential given Qualified Name instead of Name -> BLOCK
V3/final Name/QName substitution -> BLOCK
```

## 41. F002 PKI regressions

```text
self-issued leaf matching EK -> BLOCK
leaf signed by untrusted CA -> BLOCK
system trust store path -> BLOCK
caller root -> BLOCK
wrong pinned root DER/SPKI -> BLOCK
wrong Infineon intermediate / CA number -> BLOCK
extra intermediate/cross cert/alternate path -> BLOCK
AIA-fetched path -> BLOCK
SAN manufacturer != id:49465800 -> BLOCK
SAN model != SLB 9670 TPM2.0 -> BLOCK
SAN version != id:0757 -> BLOCK
EKU missing/wrong -> BLOCK
CA=TRUE leaf -> BLOCK
keyAgreement missing -> BLOCK
certificate invalid at V3 submitted_at -> BLOCK
missing/stale/invalid CRL -> BLOCK
CRL nextUpdate absent -> BLOCK
indirect/delta CRL -> BLOCK
leaf revoked -> BLOCK
CA085 revoked -> BLOCK
current EK point != authenticated leaf SPKI -> BLOCK
```

## 42. Preserve TPM liveness negatives

```text
V3 replay other host -> EK/AK mismatch
V3 in VM + different vTPM -> BLOCK
copied EK cert without EK private key -> ActivateCredential BLOCK
old quote/new request -> extraData BLOCK
old quote/new gate -> nonce BLOCK
wrong AK -> BLOCK
same snapshot/different TPM -> BLOCK
clear/EPS/AK/EK change -> BLOCK
reset/restart/PCR/IMA/firmware drift -> BLOCK
safe=0 -> BLOCK
non-increasing clock -> BLOCK
invalid signature -> BLOCK
```

## 43. Mandatory same-host passthrough/proxy attack

Independent review MUST test current hardware-TPM passthrough/proxy, including QEMU host `/dev/tpm0` passthrough, host/guest shared PCRs, IMA/PCR10 behavior, genuine EK/AK quote consumption from VM, and whether Human no-proxy attestation is the only remaining CPU/locality barrier.

A complete passing proxy counterexample under the frozen threat model is a blocker.

## 44. Preserve all prior negatives

Preserve NFIT/storage, ext4, proc/userns/idmap, inode/casefold, staging/mtime/object closure, split/shared index, alternates/promisor/lazy fetch, main-ref aliases, replacement refs, hooks/filters, lost CAS, reflog/worktree and post-effect-uncertainty regressions.

# PART XI — EXTERNAL SEMANTICS CHECKED

## 45. Current sources checked on 2026-09-02

```text
TCG TPM 2.0 Library Specification Version 185
https://trustedcomputinggroup.org/resource/tpm-library-specification/

TCG EK Credential Profile TPM 2.0 Version 2.7
https://trustedcomputinggroup.org/resource/http-trustedcomputinggroup-org-wp-content-uploads-tcg-ek-credential-profile/

Infineon OPTIGA TPM certificate publication page
https://www.infineon.com/design-resources/platforms/optiga-software-tools/optiga-tpm-and-trust-certificates

CA085 publication identifiers
https://pki.infineon.com/OptigaEccMfrCA085/OptigaEccMfrCA085.crt
https://pki.infineon.com/OptigaEccMfrCA085/OptigaEccMfrCA085.crl

OPTIGA ECC Root CA publication identifier
https://pki.infineon.com/OptigaEccRootCA/OptigaEccRootCA.crt
```

Research semantics used:

```text
TPMS_ATTEST.qualifiedSigner = Qualified Name of signing key
MakeCredential credentialed object uses ordinary object Name
TPM vendor ID Infineon = 0x49465800
low-range ECC EK cert index = 0x01C0000A
TCG EK certificate SAN binds manufacturer/model/version
ECC decrypt EK certificate KeyUsage requires keyAgreement
EK EKU = 2.23.133.8.1
Infineon official page maps CA085 to SLB 9670 FW7.87
```

The embedded trust-anchor bytes are normative; URLs are research provenance only. Runtime network content is never authority.

CLI textual stdout is never authority. Future code parses TPM wire structures, DER certificates and DER CRLs under this exact schema.

# PART XII — INDEPENDENT REVIEW CHECKLIST

## 46. Independent R4R16 review must answer at least

```text
Is ordinary Name correctly recomputed from TPMT_PUBLIC?
Is Qualified Name separately typed and bound?
Does every quote compare qualifiedSigner to Qualified Name, not Name?
Does MakeCredential still use ordinary Name only?
Are embedded root DER/SPKI hashes correct for the bytes?
Is the selected root the intended Infineon OPTIGA TPM root?
Is CA085 path closed enough to exclude alternate authorities?
Are CA085 subject/profile assumptions exact?
Is FW7.87 SAN value id:0757 correct and implementable?
Are leaf KeyUsage/EKU/BasicConstraints rules compatible with current TCG/Infineon leafs?
Is GitHub submitted_at a non-circular trusted validation-time rule?
Can required root/intermediate CRLs be supplied and fit the bounded V3 evidence?
Do CRL semantics fully fail closed for leaf/intermediate revocation?
Can self-issued/vTPM leaf ever reach pinned root without Infineon signing authority?
Does current EK point equal authenticated leaf SPKI?
Can simple wrong-host/different-vTPM replay pass?
Can same-host physical TPM passthrough/proxy still pass every predicate?
Are earlier snapshot/NFIT/ext4/Git durability corrections preserved?
```

## 47. Intended predecessor-finding disposition target

If independent review finds no new blocker:

```text
R4R15 F001 Name/QName signer mismatch = ADDRESSED AT BRIEF LEVEL
R4R15 F002 EK path/trust anchor = ADDRESSED AT BRIEF LEVEL FOR EXACT PINNED INFINEON PROFILE
```

This is not a predeclared PASS.

# PART XIII — STOP

## 48. Explicit non-authority

This brief does not authorize:

```text
independent R4R16 review under same accept
ScriptOps implementation
TPM provisioning/persistence
TPM clear/NV/hierarchy mutation
Human V3 platform review
Human final V16 decision
positive control
canonical effect
recovery
merge
X1B closure
V1 authority
release/deployment/tag
```

## 49. Next legal step

After exact R4R16 brief is frozen in one draft PR, STOP.

```text
fresh Human authorization
-> exactly one independent AK-CANON adversarial review
   of exact frozen R4R16 implementation brief
```

Preserve:

```text
AI PROPOSES != HUMAN DECIDES
REVIEW FINDING != REPAIR AUTHORITY
R4R16 BRIEF != IMPLEMENTATION AUTHORITY
R4R16 REVIEW PASS != IMPLEMENTATION AUTHORITY
X1B OPEN != V1 AUTHORITY
```
