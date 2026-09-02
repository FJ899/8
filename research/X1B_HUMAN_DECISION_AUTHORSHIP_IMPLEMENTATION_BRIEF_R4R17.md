# X1B HUMAN DECISION AUTHORSHIP — CLEAN IMPLEMENTATION BRIEF R4R17

Status: `CLEAN R4R17 CORRECTIVE BRIEF / IMPLEMENTATION NOT AUTHORIZED`

Date: `2026-09-02`

## 1. Authority, purpose, and STOP boundary

This is the self-contained successor implementation brief after independent AK-CANON review PR #147 returned `NOT PASS` on R4R16.

R4R17 preserves the accepted X1B corrective-design contract and every predecessor correction not rejected by PR #147. It corrects exactly:

```text
X1B-R4R16-IBR-F001 — OFFLINE CRL ROLLBACK / LATEST-ISSUER-STATE IS NOT BOUND
X1B-R4R16-IBR-F002 — PHYSICAL TPM QUOTE DOES NOT BIND THE EXECUTING CPU / TPM TRANSPORT LOCALITY
```

R4R17 freezes two new authority profiles:

```text
INFINEON_LIVE_CRL_CURRENTNESS_V1
LIVE_HUMAN_EXECUTOR_LOCALITY_ATTESTATION_V1
```

The CRL correction changes revocation from stapled-only evidence to an explicit live publication-state rule. Human V4 evidence contains the exact CRL bytes the Human reviewed. The executor independently reads the exact issuer-designated Infineon HTTPS publication points and, at the final pre-ref gate, requires the live bytes to equal the Human-bound bytes. `CRLNumber`, AKI, signature, validity, scope and revocation are all mandatory. The final live read is a defined linearization point immediately before main-ref rename.

The locality correction deliberately removes the false claim that a TPM quote proves CPU/TPM transport locality:

```text
TPM EVIDENCE AUTHENTICATES THE TPM AND ITS SIGNED STATE.
TPM EVIDENCE DOES NOT BY ITSELF PROVE THAT THE EFFECT-CAPABLE CPU CONTEXT IS BARE METAL.
THE BARE-METAL / NO-PROXY EXECUTION-LOCALITY PREMISE IS A FRESH TRUSTED-HUMAN AUTHORITY ACT.
```

That act is a new V4 Human review bound to a fresh unpredictable executor nonce generated only after the exact physical main-ref CAS lock is held. The Human observes the exact nonce-bearing executor challenge through an independently authenticated physical-host console or BMC host-console channel and explicitly judges that the effect-capable context is the physical host and is not a guest, TPM-passthrough guest, or TPM-proxy client.

This is an explicit governance trust decision, not a software inference. A deliberately false statement by the trusted Human is outside executor detection. The correction is that the environmental premise is fresh, authenticated, request/process/effect bound, and explicitly Human-authoritative rather than mislabeled as TPM cryptographic proof.

This brief authorizes no ScriptOps source mutation, no independent R4R17 review, no certifi vendoring, no TPM provisioning, no Human V4 review creation, no Human final V17 decision, no positive control, no canonical effect, no recovery, no merge, no X1B closure, no V1 authority, no release, deployment, or tag.

```text
R4R17 BRIEF != IMPLEMENTATION AUTHORITY
R4R17 REVIEW PASS != IMPLEMENTATION AUTHORITY
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
TPM POSSESSION != CPU LOCALITY
SIGNED CRL != CURRENT PUBLICATION STATE
```

After exact durable freeze of this brief, STOP. The next legal stage is one separately Human-authorized independent AK-CANON review of this exact artifact.

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

R4R16 predecessor:

```text
FJ899/8 PR #146
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = d390390f9523c10dd7741a8c4aa7ae3c4895128b
TREE = 396327e9cb70ed5941bfeeb87cc22b2e80547e31
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R16.md
BLOB = 86ca7ad54e04c8e52749453ffe1a8fdda8a9c369
```

Binding R4R16 review:

```text
FJ899/8 PR #147
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 96e9eebd12a290ff324f892998238421797b4933
TREE = 41607b983169d3678a6f7b795327737b9e42a5fb
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R16_AK_CANON_REVIEW.md
BLOB = dd25369e8d6949861b9ef2d85446afbc2bb5fc95
VERDICT = NOT PASS
```

PR #147 freezes the two R4R16 blockers above and records these earlier corrections as addressed at brief level:

```text
R4R15 F001 Name / Qualified-Name signer mismatch
R4R15 F002 missing EK trust path / trust anchor for the exact pinned Infineon profile
```

R4R17 MUST NOT weaken them.

Preserved higher-level properties:

```text
separate trusted Human decision act
exact content/scope/candidate/effect binding
freshness/activity/supersession/conflict/replay semantics
executor no-substitution
fail closed on ambiguity
real-boundary negatives
separately authorized positive Human control
post-effect truth matching Human-bound effect
no durable successful Human attribution for a failed/uncertain operation
no core security/authority choice left implicit
```

## 3. Exact repository state before R4R17 preparation

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

## 4. Normative precedence / migration

```text
R4R17 TEXT = CURRENT IMPLEMENTATION-BRIEF AUTHORITY
R4R16 AND EARLIER IMPLEMENTATION BRIEFS = HISTORICAL INPUT ONLY
CORRECTIVE DESIGN PR #34 = HIGHER-LEVEL PROPERTY CONTRACT
```

V17 authority-critical changes:

```text
stapled-only CRL currentness removed
CRLNumber + AKI mandatory
exact Infineon HTTPS publication response becomes explicit current-publication authority
Human-bound V4 CRL bytes must equal final live publication bytes
final CRL observation has a named pre-rename linearization point
no blocking/external authority read may occur after CRL linearization and before ref rename
maximum monotonic linearization-to-rename interval = 2 seconds
frozen certifi wheel supplies the only TLS CA bundle
ambient/system/proxy TLS authority forbidden
TPM quote no longer described as CPU-locality proof
fresh locality nonce generated only after physical ref lock
Human V4 live locality/platform act mandatory
V4 binds exact effect-capable executor identity + nonce + effect + CRLs + TPM/platform
final Human V17 review separately references exact V4
V4/final age at commit <= 120 seconds
```

No V16-or-earlier request/platform/final evidence authorizes V17.

# PART I — CORE HUMAN DECISION RULE

## 5. HumanDecision V17

```text
HumanDecision = TRUE
ONLY IF
separate trusted Human final V17 decision evidence
for exact content + scope + candidate + material effect
AND exact current trusted Human PlatformAttestationV4
AND all machine-verifiable TPM/PKI/storage/ref predicates are independently satisfied.
```

Never sufficient alone:

```text
approval-command possession
non-empty rationale
caller identity
silence/continuation
AI-created record
CI success
mergeability
successful fsync
guest ACPI/NFIT appearance
TPM quote alone
TPM EK/AK possession alone
PCR/IMA continuity alone
signed but possibly superseded CRL
HTTP response outside the frozen TLS/currentness profile
stale Human platform review
V4 not bound to fresh live locality nonce
```

Normative distinctions:

```text
AI PROPOSED != HUMAN DECIDED
HUMAN DECISION EVIDENCE != EXECUTION CREDENTIAL
TPM IDENTITY != CPU LOCALITY
TPM IDENTITY != BACKEND PERSISTENCE DECISION
HUMAN LOCALITY JUDGMENT != TPM QUOTE
SIGNED CRL != CURRENT PUBLICATION STATE
```

## 6. Future bounded implementation surface

Expected future ScriptOps changed surface exactly:

```text
phase6/scriptops-v2-hardening.py
legacy/scriptops-v2-single.py
phase6/x1b_human_decision.py
phase6/x1b_tpm_attestation.py
phase6/x1b_ek_pki.py
phase6/x1b_crl_currentness.py
phase6/x1b_live_locality.py
third_party/certifi/certifi-2026.7.22-py3-none-any.whl
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
tests/test_x1b_crl_currentness.py
tests/test_x1b_live_locality.py
.github/workflows/x1b-human-decision.yml
```

Expected unchanged:

```text
phase6/bounded-proposal-view.py
.github/workflows/phase6-scriptops-smoke.yml
.github/workflows/verify-repository.yml
sources/prototype/scriptops-v2-single.py.part01..part07
```

No TPM private material, hierarchy secret, Human credential, proxy credential, BMC credential, or provisioning secret may be committed. The future implementation vendors the exact certifi wheel; runtime download/update is forbidden.

# PART II — PRESERVED STORAGE / PLATFORM AUTHORITY

## 7. Supported storage profile

Preserve exactly:

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
identity uid/gid maps
non-ID-mapped mount
authenticated procfs/sysfs
internal ext4 journal only
barrier enabled
data=ordered or data=journal
journal_async_commit absent
DAX disabled
ext4 errors_count = 0
```

Unavailable, ambiguous, unreadable, substituted, or drifting authority primitive means `BLOCKED`.

## 8. Procfs / user namespace / idmap authority

Preserve exact predecessor profiles:

```text
AUTHENTIC_CURRENT_TASK_PROCFS_V1
LINUX_INITIAL_USER_NAMESPACE_V2
LINUX_EXECUTION_CREDENTIAL_STATE_V2
LINUX_NON_IDMAPPED_EXT4_MOUNT_V2
AUTHENTIC_EXT4_RUNTIME_STATE_V1
LINUX_EXT4_BYTE_EXACT_NAMESPACE_V1
LINUX_INODE_SEMANTIC_FLAGS_V1
```

Require genuine procfs/sysfs, initial user namespace inode `4026531837`, identity uid/gid maps, stable credentials/capabilities, non-ID-mapped ext4 mount, no lazytime, no casefold and no unsupported authority-changing inode flags.

## 9. ACPI NFIT persistence profile

Positive kernel-visible state remains exactly:

```text
whole /dev/pmem<N>
physical /sys/dev/block topology
provider=ACPI.NFIT
ACPI0012 ancestry
positive range_index
positive exact mappings
all mapped nmem identities
all nfit/flags empty
all nfit/format raw = "0x0101\n"
persistence_domain raw = "cpu_cache\n"
deep_flush raw = "0\n"
```

Preserve all prior negatives for zram, ramdisk, loop, DM, md, network, virtio, NVMe, SCSI, CXL, E820/manual/test PMEM, partitions, BTT, PFN, DAX-char and unknown stacks/topology/health drift.

## 10. Published PlatformSnapshotV17

Complete canonical `PlatformSnapshotV17` bytes are published verbatim inside immutable `DecisionRequestV17`.

Every Human-review-required raw authority value uses:

```text
<field>.raw_len=<canonical unsigned decimal>
<field>.raw_hex=<lowercase even-length complete raw bytes>
<field>.semantic=<canonical parsed value>
```

No Human-required authority value may exist only behind a digest.

Bounds:

```text
mappings <= 16
mapped nmem <= 16
one raw snapshot value <= 4096 bytes
PlatformSnapshotV17 <= 32768 bytes
DecisionRequestV17 body <= 60000 bytes
```

Truncation or hidden-preimage fallback blocks.

# PART III — PRESERVED TPM / EK PKI AUTHORITY

## 11. AK Name / Qualified Name separation

Required persistent AK handle:

```text
AK_HANDLE = 0x8101F515
```

Required AK public profile:

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

Typed identities:

```text
AK_NAME := UINT16_BE(TPM_ALG_SHA256) || SHA256(canonical TPMT_PUBLIC wire bytes)
AK_QUALIFIED_NAME := exact TPM2_ReadPublic qualifiedName bytes
```

Require:

```text
ak_name_returned == AK_NAME
TPMS_ATTEST.qualifiedSigner == AK_QUALIFIED_NAME
MakeCredential.objectName == AK_NAME
```

No helper/schema/comment may use `name` ambiguously for both types.

## 12. Exact pinned Infineon EK profile

Only:

```text
INFINEON_SLB9670_FW7_87_ECC_EK_PKI_V1
```

Require:

```text
TPM_PT_MANUFACTURER = 0x49465800
TPM2 low-range ECC NIST P-256 EK
NV EK certificate index = 0x01C0000A
TCG low-range ECC P-256 EK template
nameAlg=SHA256
current EK public point == authenticated leaf SPKI point
leaf SAN manufacturer = id:49465800
leaf SAN model = SLB 9670 TPM2.0
leaf SAN version = id:0757
leaf EKU includes exactly required EK OID 2.23.133.8.1
leaf KeyUsage critical keyAgreement
leaf BasicConstraints critical CA=FALSE
```

Pinned root:

```text
INFINEON_OPTIGA_ECC_ROOT_CA_V1
DER length = 607
DER SHA-256 = cfeb02fecd55ad7a73c6e1d11985d4c47dee248ab63dcb66091a2489660443c3
SPKI SHA-256 = ce5183a19d6fe79a6c1b058cfa700379f67d587a8afd0f51621e82d9f00c5a28
SKI = b41885c84a4ac5127af24039dec4f58b1e7e4ad1
```

Accepted path only:

```text
EK leaf
-> Infineon OPTIGA(TM) TPM 2.0 ECC CA 085
-> pinned Infineon OPTIGA(TM) ECC Root CA
```

No system EK trust store, caller root, alternate intermediate, cross-cert, AIA path search, runtime network path building or implementation-selected CA.

## 13. TPM liveness, with narrowed meaning

Preserve predecessor request/reference/gate nonces, ECDSA quote verification, exact SHA-256 PCR selection `0,2,4,7,10`, independent PCR digest verification, authenticated IMA/PCR10 replay, reset/restart/safe/clock/firmware continuity and fresh MakeCredential/ActivateCredential co-residency checks.

Normative meaning:

```text
TPM quote + ActivateCredential = evidence of current access to exact authenticated TPM/EK/AK
PCR/IMA/clock = TPM/measured-state continuity signals
NOT = proof that executor CPU context is bare metal
NOT = proof that TPM transport is not proxied/passed through
```

Any implementation/success evidence claiming TPM-to-CPU locality is nonconforming.

# PART IV — PR #147 F001: LIVE CRL CURRENTNESS

## 14. Current-publication authority model

R4R17 explicitly defines the trust boundary:

```text
CURRENT CRL PUBLICATION STATE
=
exact bytes returned at the live gate by the issuer-designated HTTPS publication URL
under DIRECT_NO_PROXY_HTTPS_CURRENTNESS_V1 and CERTIFI_WEBPKI_2026_07_22_V1.
```

The executor does not claim visibility into an unpublished CA database entry or a CRL not yet served by the issuer-designated publication endpoint. Compromise of the CA/publication infrastructure or a valid public-WebPKI key is outside this executor's detection boundary. That boundary is explicit, not implicit.

Within this boundary, a caller/Human cannot select a cached/superseded CRL: the executor independently obtains the publication bytes.

## 15. Exact CRL publication URLs

Only:

```text
LEAF_STATUS_URL = https://pki.infineon.com/OptigaEccMfrCA085/OptigaEccMfrCA085.crl
INTERMEDIATE_STATUS_URL = https://pki.infineon.com/OptigaEccRootCA/OptigaEccRootCA.crl
```

No caller-derived URI is authority. Certificate CDP/AIA values are consistency data only.

Forbidden:

```text
HTTP
FTP
file/data URI
mirror
alternate hostname
caller URL
local cached file
redirect target
```

Any 3xx response blocks.

## 16. Frozen WebPKI authority

Profile:

```text
CERTIFI_WEBPKI_2026_07_22_V1
```

Future implementation vendors exactly:

```text
certifi-2026.7.22-py3-none-any.whl
size = 136983 bytes
SHA-256 = 62f22742b58a1a33014a2b6b706588a8d7e2a88ae7bd1a6ebe8c992928483775
PyPI upload_time = 2026-07-22T03:35:11.276376Z
PyPI source provenance commit = certifi/python-certifi@f4bc676bc101fe2235846e37044e8c693d6cbaf4
```

Runtime TLS trust store is built only from `certifi/cacert.pem` extracted from that exact vendored wheel after verifying wheel SHA-256.

Forbidden TLS CA authority:

```text
/etc/ssl
SSL_CERT_FILE
SSL_CERT_DIR
REQUESTS_CA_BUNDLE
CURL_CA_BUNDLE
NSS/browser store
caller CA
enterprise-injected CA
ambient installed certifi
runtime-downloaded CA
```

No automatic certifi/root rotation. Any bundle change requires new governance.

## 17. Direct HTTPS currentness transport

Profile:

```text
DIRECT_NO_PROXY_HTTPS_CURRENTNESS_V1
```

Future code uses a closed direct socket/TLS/HTTP client and MUST:

```text
fresh TCP connection per fetch
hostname exactly pki.infineon.com
port exactly 443
TLS hostname validation for pki.infineon.com
TLS trust only CERTIFI_WEBPKI_2026_07_22_V1
TLS >= 1.2
no anonymous/null/insecure cipher mode
no proxy CONNECT
ignore proxy environment variables
no redirect
no cookie/auth/client certificate
no local HTTP cache
no conditional request reuse
status exactly 200
body length 1..16384 bytes
no Content-Encoding transform
read exact response body bytes once
Connection: close
```

Each request carries an independent `getrandom(32)` cache-busting token:

```text
?x1b_currentness=<64 lowercase hex>
```

and request headers:

```text
Cache-Control: no-cache, no-store, max-age=0
Pragma: no-cache
Accept: application/pkix-crl, application/octet-stream, */*
Connection: close
```

Response admission requires:

```text
Date header present and valid HTTP-date
Age absent or exactly 0
Via absent
Warning absent
Date within +/- 120 seconds of the trusted current GitHub HTTPS Date sample for the same gate
```

If the exact Infineon endpoints do not support this frozen request/response profile, the positive V17 path is `BLOCKED`; implementation may not weaken it. Independent R4R17 review MUST test positive-path implementability.

## 18. CRL semantic profile

For both CRLs require:

```text
complete DER
issuer exact
signature validates under expected issuer certificate
signature hash SHA-256 or SHA-384 family only
AuthorityKeyIdentifier present
AKI keyIdentifier exactly equals expected issuer SKI/key identifier
CRLNumber present
CRLNumber non-negative canonical INTEGER
thisUpdate present
nextUpdate present
thisUpdate <= PKI_VALIDATION_TIME < nextUpdate
issuer certificate KeyUsage includes cRLSign
indirect CRL unsupported
delta CRL unsupported
issuingDistributionPoint absent unless exact full-scope semantics are separately frozen and matched
unknown critical CRL extension -> BLOCK
```

Target certificate serial must be absent from `revokedCertificates`.

`PKI_VALIDATION_TIME` for the Human V4 evidence remains exact immutable GitHub V4 review `submitted_at`; live-gate CRL validity additionally uses the trusted current GitHub HTTPS Date sample for that live gate.

## 19. Typed live CRL observation

For each fetch:

```text
CurrentCRLObservationV17 {
  url,
  fetch_nonce,
  response_date,
  trusted_github_date,
  tls_peer_leaf_der_sha256,
  tls_peer_chain_digest,
  body_len,
  body_sha256,
  issuer,
  authority_key_identifier,
  crl_number,
  this_update,
  next_update,
  revoked_serial_set_digest
}
```

TLS peer hashes are evidence only, not trust anchors.

## 20. V4 CRL acquisition

After the physical main-ref CAS lock is held and `ExecutorIdentityV17` is frozen, but before the Human V4 review, the exact executor fetches both publication URLs through separate fresh connections.

Call exact admitted bytes:

```text
V4_LEAF_CRL
V4_ROOT_CRL
```

Require all section-18 semantics. V4 binds full raw CRL preimages plus:

```text
leaf_crl_sha256
leaf_crl_number
leaf_crl_this_update
leaf_crl_next_update
root_crl_sha256
root_crl_number
root_crl_this_update
root_crl_next_update
```

The Human reviews those exact bytes/parsed semantics; a digest-only CRL target is insufficient.

## 21. Final CRL currentness gate and linearization

Before this gate, while the physical main-ref CAS lock remains held, executor MUST finish every other authority read/revalidation that could block or wait, including:

```text
request/candidate/scope
ref lock identity + CAS old OID
ExecutorIdentityV17
PlatformSnapshotV17
proc/userns/credentials
ext4 runtime/error state
EK path
AK Name/Qualified Name
fresh TPM quote/activation
PCR/IMA/lifecycle
V4 review currentness/freshness
final V17 review currentness/freshness
prepared canonical object/ref/reflog/index/worktree bytes
```

Only then does executor perform two new live direct HTTPS CRL fetches, one for each exact URL.

Require:

```text
PRE_RENAME_LEAF_CRL bytes == V4_LEAF_CRL bytes
PRE_RENAME_ROOT_CRL bytes == V4_ROOT_CRL bytes
```

and independently reparse/reverify section-18 semantics.

Explicit outcomes:

```text
live CRLNumber > V4 CRLNumber -> BLOCK; new V4 + final V17 required
live CRLNumber < V4 CRLNumber -> BLOCK as rollback
same CRLNumber but different DER -> BLOCK
same bytes but now time-invalid -> BLOCK
newly listed target serial -> BLOCK
network/TLS/currentness ambiguity -> BLOCK
same exact valid bytes -> eligible to linearize
```

Define:

```text
PRE_REF_RENAME_CRL_LINEARIZATION_POINT
=
local monotonic timestamp captured immediately after the second of the two final CRL responses
has been completely read, TLS-admitted, DER-parsed, signature/AKI/CRLNumber/time/revocation-validated,
and byte-equality checked against the V4 CRL pair.
```

This is the normative current-publication-state sample for the main-ref commitment.

After the linearization point and before durable physical main-ref rename:

```text
NO network read
NO GitHub read
NO Human wait
NO TPM command
NO filesystem scan
NO config read
NO sleep/retry
NO other blocking/external authority operation
```

Only already-prepared local lock/ref checks and the bounded durable ref-commit syscalls may execute.

Maximum monotonic interval:

```text
main_ref_rename_monotonic - PRE_REF_RENAME_CRL_LINEARIZATION_POINT <= 2.000 seconds
```

If the interval would exceed 2 seconds, do not rename. Repeat both final CRL fetches and create a new linearization point after rechecking equality/validity.

A CRL first published **after** the successful linearization point is a later external revocation-publication event. It does not retroactively mean an authentic older CRL was rolled back at the already-defined gate. This exact temporal trust boundary is deliberate and reviewable.

No silent authority update to a newer CRL is permitted: any different current bytes require new V4 and new final V17 Human decision.

## 22. CRL failure semantics

Before main-ref commitment:

```text
any CRL/TLS/currentness failure = BLOCKED
```

After durable main-ref commitment has begun:

```text
new ambiguity = UNCERTAIN / RECOVERY REQUIRED
```

No recovery mutation is authorized here.

# PART V — PR #147 F002: LIVE HUMAN EXECUTOR LOCALITY

## 23. Explicit authority model

Positive premise:

```text
A trusted Human, using an independently authenticated out-of-band physical-host observation channel,
attests that the exact nonce-bearing effect-capable executor currently shown on that host console
is running on the reviewed physical bare-metal host,
not in a VM/guest and not through a TPM proxy or TPM passthrough transport.
```

This Human judgment is the locality authority. TPM evidence is independent machine evidence for TPM identity/state but is not the locality authority.

A deliberately false trusted-Human locality assertion is outside executor detection, exactly as a deliberately false final Human decision is outside executor semantic truth detection. An accidental/mistaken assertion is mitigated by exact live challenge/process/platform binding and mandatory observation-channel rules, not by pretending the TPM proves the claim.

## 24. ExecutorIdentityV17

Construct from authenticated current-task sources:

```text
request_digest
pid
/proc/self/stat starttime
/proc/self/exe st_dev
/proc/self/exe st_ino
/proc/self/exe size
/proc/self/exe mode
SHA256(exact /proc/self/exe bytes)
/proc/self/ns/pid inode
/proc/self/ns/mnt inode
/proc/self/ns/user inode
/proc/self/ns/net inode
SHA256(exact /proc/self/cgroup bytes)
exact /proc/sys/kernel/random/boot_id bytes
uid/gid/euid/egid/fsuid/fsgid
capability sets
platform_snapshot_sha256
AK_NAME
AK_QUALIFIED_NAME
EK leaf DER SHA256
```

Canonical bytes:

```text
executor_identity_sha256 = SHA256(canonical ExecutorIdentityV17 bytes)
```

PID alone is never identity. Every field is revalidated before the final CRL linearization gate; any drift aborts and requires new V4/final evidence.

## 25. Ref-lock-first locality challenge

Before challenge generation:

```text
all read-only authority gates pass
all candidate/raw object/index/ref/reflog/worktree bytes are computed
bounded non-canonical staging is sealed
NO canonical loose-object installation
NO main-ref rename
NO raw index/worktree projection
```

Acquire exact physical main-ref CAS lock under the preserved alias-safe profile and re-read old OID/CAS expectation.

Only while that exact lock is held generate:

```text
executor_locality_nonce = getrandom(32)
```

Caller cannot provide or reuse it.

Challenge domain:

```text
X1B-LIVE-EXECUTOR-LOCALITY-V17\x00
```

Challenge digest:

```text
locality_challenge_sha256 = SHA256(
 domain
 || request_digest
 || executor_identity_sha256
 || platform_snapshot_sha256
 || main_ref_old_oid
 || main_ref_new_oid
 || executor_locality_nonce
 || SHA256(V4_LEAF_CRL)
 || SHA256(V4_ROOT_CRL)
 || AK_NAME
 || AK_QUALIFIED_NAME
)
```

## 26. Accepted Human observation channels

Only:

```text
physical-local-console
bmc-kvm-host-console
bmc-serial-over-lan-host-console
```

Forbidden as sole authority:

```text
SSH shell
executor-served web terminal
VNC/RDP to OS
container exec
CI/GitHub Actions log
VM console
QEMU monitor
unproven serial stream
screenshot supplied by executor
AI summary
```

For a BMC channel, Human authenticates BMC/chassis identity independently of executor. ScriptOps never receives BMC credentials.

## 27. Exact live challenge display

While the physical main-ref lock is held and before any canonical mutation, executor displays exactly:

```text
X1B-V17-LOCALITY request=<request_digest> executor=<executor_identity_sha256> nonce=<64hex> challenge=<locality_challenge_sha256>
```

The Human must see the exact line through one accepted out-of-band host-console channel and independently verify at least:

```text
intended physical chassis / host console
host OS rather than guest console
no hypervisor/VM layer mediates this effect-capable executor
no QEMU hardware-TPM passthrough serves this execution
no custom TPM command proxy/relay serves this execution
exact request/executor/nonce/challenge match V4 body
physical ACPI-NFIT PMEM/backend premise remains true
```

Human supporting observations may include BMC inventory, physical labels, firmware inventory and host process/service inspection. They are recorded in `why=`; executor does not silently infer them.

## 28. PlatformAttestationV4 origin and sequencing

Exactly one unique trusted Human APPROVED GitHub PR review on the exact decision PR, distinct from the final Human V17 review, not dismissed, non-bot/app/AI, exact body bytes fetched directly from GitHub.

Sequence:

```text
request published
read-only validation + noncanonical staging
physical main-ref CAS lock acquired
ExecutorIdentityV17 frozen
V4 CRL pair live-fetched
fresh executor_locality_nonce generated
challenge displayed on accepted host-console channel
Human performs live locality/backend observation
Human submits V4 APPROVED review containing exact nonce/challenge
executor fetches V4 + immutable submitted_at
executor validates V4/PKI/CRLs/TPM/snapshot/executor identity
Human submits final V17 decision referencing exact V4
executor fetches/revalidates both Human acts
canonical object installation begins only after both Human acts are admitted
all non-CRL final authority revalidation completes
final CRL linearization fetch pair executes last
bounded main-ref rename follows
post-effect truth verification
```

There is deliberately no attempt to compare a local nonce-generation wall-clock timestamp to GitHub `submitted_at`. Sequencing is established structurally: the 256-bit nonce is generated from `getrandom()` only after the exact lock is held, is not caller-supplied or published beforehand, and the independently fetched immutable V4 review body must contain that exact nonce/challenge. A pre-existing review cannot predict/satisfy the fresh nonce except with negligible cryptographic probability.

Executor cannot create/edit/submit/approve/dismiss/refresh/supersede either Human authority act.

## 29. Exact V4 marker

Exact ordered LF-only body:

```text
X1B-PLATFORM-PERSISTENCE-ATTESTATION-V4
decision_request_id=<x1b:request_digest>
decision_request_sha256=<request_digest>
platform_snapshot_sha256=<digest>
executor_identity_sha256=<64 hex>
executor_locality_nonce=<64 hex>
locality_challenge_sha256=<64 hex>
main_ref_old_oid=<40 hex>
main_ref_new_oid=<40 hex>
environment_class=bare-metal
virtualization_layer=none
execution_locality=physical-host
trusted_locality_authority=human-live-out-of-band
tpm_cpu_locality_claim=not-claimed-by-tpm
observation_channel=<physical-local-console|bmc-kvm-host-console|bmc-serial-over-lan-host-console>
tpm_proxy=absent
tpm_passthrough=absent
backend_class=physical-acpi-nfit-nvdimm
power_loss_persistence=affirmed
persistence_domain=cpu_cache
deep_flush=0
nfit_format=0x0101
tpm_profile=PHYSICAL_TPM2_ECC_EK_AK_V2
ek_pki_profile=INFINEON_SLB9670_FW7_87_ECC_EK_PKI_V1
tpm_ak_name=<68 lowercase hex>
tpm_ak_qualified_name=<68 lowercase hex>
ek_leaf_der_sha256=<64 hex>
leaf_crl_sha256=<64 hex>
leaf_crl_number=<canonical unsigned decimal>
leaf_crl_this_update=<canonical UTC>
leaf_crl_next_update=<canonical UTC>
root_crl_sha256=<64 hex>
root_crl_number=<canonical unsigned decimal>
root_crl_this_update=<canonical UTC>
root_crl_next_update=<canonical UTC>
why=<Human one-line live observation basis>
-----BEGIN X1B-V17-LIVE-EVIDENCE-----
<canonical bounded evidence>
-----END X1B-V17-LIVE-EVIDENCE-----
```

No Human-authored `submitted_at` or locality-time field exists.

## 30. V4 bounded evidence

Complete evidence includes:

```text
ExecutorIdentityV17 canonical bytes
PlatformSnapshotV17 canonical bytes or exact immutable request block reference + digest
EK leaf DER
CA085 DER
AK TPMT_PUBLIC bytes
AK_NAME
AK_QUALIFIED_NAME
reference TPM2B_ATTEST + signature
PCR values and IMA digest/record metadata
V4_LEAF_CRL complete DER
V4_ROOT_CRL complete DER
CurrentCRLObservationV17 for each URL
host-console challenge line exact bytes
```

Bounds:

```text
V4 body <= 60000 UTF-8 bytes
one CRL <= 16384 DER bytes
one certificate <= 8192 DER bytes
ExecutorIdentityV17 <= 8192 bytes
```

No truncation or hidden attachment fallback.

## 31. V4 / final freshness

Trusted time for GitHub evidence freshness is current GitHub HTTPS response `Date`.

Require:

```text
V4 submitted_at >= request published_at
final V17 submitted_at > V4 submitted_at
V4 APPROVED/current/not dismissed/no conflict
final V17 APPROVED/current/not dismissed/no conflict
```

Fresh nonce-in-body establishes that V4 is causally after nonce generation; local wall clock does not.

At final main-ref rename:

```text
V4 age <= 120 seconds
final V17 age <= 120 seconds
```

If either expires, abort before rename, release transient ref lock, and obtain a new nonce + V4 + final decision. Old nonce reuse is forbidden.

## 32. Final Human V17 marker

Only:

```text
X1B-HUMAN-DECISION-V17
decision_request_id=<x1b:request_digest>
decision_request_sha256=<request_digest>
platform_attestation_review_id=<exact V4 review id>
platform_attestation_sha256=<SHA256 exact V4 body bytes>
platform_snapshot_sha256=<digest>
executor_identity_sha256=<exact V4 value>
executor_locality_nonce=<exact V4 nonce>
locality_challenge_sha256=<exact V4 challenge>
leaf_crl_sha256=<exact V4 digest>
root_crl_sha256=<exact V4 digest>
tpm_ak_name=<AK_NAME>
tpm_ak_qualified_name=<AK_QUALIFIED_NAME>
why=<Human one-line final decision rationale>
```

New V4 requires new final V17 decision. V16 or earlier markers do not satisfy V17.

The same trusted Human natural person MAY perform V4 and final V17 acts only if the current accepted X1B Human trust policy permits that principal for both roles; review objects, marker semantics and timestamps remain distinct.

# PART VI — PRESERVED EXT4 / OBJECT / REF DURABILITY

## 33. Internal ext4 journal

Preserve raw primary-superblock predicate:

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

Preserve complete closed predecessor option table and authenticated `statmount`/proc/ext4-sysfs authority.

Required includes:

```text
rw
barrier
data=ordered OR data=journal
errors=remount-ro
auto_da_alloc
```

Forbidden includes at least:

```text
nobarrier
data=writeback
journal_async_commit
noload
DAX
external journal
alternate superblock
debug/test-encryption
emergency/shutdown/error state
unknown durability-affecting option
```

## 35. Human-bound loose-object mtime

Preserve exact sentinel:

```text
2038-01-18T00:00:00.000000000Z
tv_sec=2147385600
tv_nsec=0
```

Final metadata is set before file fsync, exact readback follows, then directory fsync.

## 36. Closed Git/filesystem profiles

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

No alternates, promisor/lazy fetch, replacement refs, split/shared index, Git authority writer, hooks, filters, smudge/clean, textconv, signing or ambient config authority.

Canonical commitment remains durable physical main-ref CAS. Post-ref projections must be durably verified before success. Uncertain post-commit truth is never reported as clean success.

# PART VII — REQUEST / EFFECT SEQUENCE

## 37. DecisionRequestV17

Immutable request binds at least:

```text
schema X1B-DECISION-REQUEST-V17
request id/digest
repository identity
baseline HEAD/TREE/security BLOBs
candidate content/scope/object/tree/commit closure
old/new main OIDs
index/ref/reflog/worktree projection digests
material-effect digest
full PlatformSnapshotV17 bytes + length/digest
nfit_format=0x0101
persistence_domain=cpu_cache
deep_flush=0
TPM profile V2
EK PKI profile INFINEON_SLB9670_FW7_87_ECC_EK_PKI_V1
pinned EK root DER/SPKI hashes
AK handle 0x8101F515
CRL currentness profile INFINEON_LIVE_CRL_CURRENTNESS_V1
TLS profile CERTIFI_WEBPKI_2026_07_22_V1
certifi wheel SHA-256
exact two CRL publication URLs
CRL linearization max gap = 2 seconds
Human locality profile LIVE_HUMAN_EXECUTOR_LOCALITY_ATTESTATION_V1
V4 marker version
V4/final max age = 120 seconds
final Human marker V17
```

Caller cannot override authority values after publication.

## 38. Pre-V4 gates

Before physical ref lock/locality challenge:

```text
request/candidate/scope exact
proc/userns/credentials exact
mount/storage/PlatformSnapshot exact
EK path exact
AK Name/QName exact
reference TPM quote exact
PCR/IMA exact
bounded staging namespace exact
all future object/index/ref/reflog/worktree bytes computed
old main ref exact
no conflicting effect
```

No canonical loose object, raw index, worktree, reflog or main-ref mutation occurs yet.

## 39. Exact material sequence

```text
1 validate request + complete PlatformSnapshot
2 validate proc/userns/credentials/mount/ext4/NFIT/Git topology
3 validate pinned EK path + current EK/AK + Name/QName + reference TPM state
4 compute all candidate/raw future bytes
5 seal bounded noncanonical staging
6 acquire alias-safe physical main-ref CAS lock
7 re-read old main OID and verify CAS expectation
8 freeze ExecutorIdentityV17
9 fetch/validate V4 leaf/root CRLs
10 generate fresh executor_locality_nonce
11 compute/display exact live locality challenge
12 Human submits V4 live platform/locality review
13 executor fetches/validates V4 + submitted_at
14 Human submits final V17 decision referencing exact V4
15 executor fetches/validates final V17
16 FinalEffectGateV17
17 install/fsync canonical loose objects and verify object closure under preserved rules
18 prepare/validate already-computed raw ref/reflog/index/worktree projections while lock remains held
19 complete every non-CRL final authority revalidation, including fresh TPM quote/activation, process identity, snapshot, Human freshness and ref-lock/CAS state
20 perform final live leaf CRL fetch and validation
21 perform final live root CRL fetch and validation
22 require exact V4 byte equality and capture PRE_REF_RENAME_CRL_LINEARIZATION_POINT
23 with no external/blocking authority operation, perform bounded physical main-ref/reflog durable commitment within 2 monotonic seconds
24 durably apply raw index/worktree projections
25 POST_EFFECT TPM quote + full post-effect truth verification
26 SUCCESS only after exact Human-bound truth
```

If a final pre-ref gate fails after canonical loose-object installation but before main-ref rename, preserve the predecessor's bounded loose-object residue classification/mtime rules; do not misreport the requested Human-attributed effect as committed. No cleanup mutation beyond already-authorized pre-commit transient lock/staging cleanup may invent a recovery authority.

## 40. FinalEffectGateV17

Requires every prior predicate current:

```text
request/candidate/scope
proc/userns/credentials
mount/storage/PlatformSnapshot
EK path/current EK/AK
correct Name/QName
fresh TPM quote/activation
PCR/IMA/lifecycle
exact ExecutorIdentityV17
current locality nonce/challenge
V4 Human live locality/platform review
final Human V17 review
ext4 journal/options/errors
mtime horizon
object/ref/index/reflog/worktree topology
physical ref lock + old-OID CAS
no conflicting effect
```

CRL currentness is then sampled last at section-21 linearization immediately before ref commitment.

## 41. Success / uncertainty

Before durable main-ref commitment:

```text
failed gate = BLOCKED
```

After durable main-ref commitment begins:

```text
new ambiguity = UNCERTAIN / RECOVERY REQUIRED
```

Never convert uncertainty to success because later projections appear plausible. No recovery mutation is authorized by this brief.

# PART VIII — MANDATORY REGRESSIONS

## 42. PR #147 F001 regressions

Real-boundary tests must include:

```text
signed old CRL N still before nextUpdate, live endpoint returns N+1 -> BLOCK
live CRLNumber > V4 -> BLOCK/new V4+final
live CRLNumber < V4 -> rollback BLOCK
same CRLNumber different DER -> BLOCK
missing/noncanonical CRLNumber -> BLOCK
AKI missing/mismatch -> BLOCK
wrong issuer -> BLOCK
invalid signature -> BLOCK
issuer certificate lacks cRLSign -> BLOCK
leaf serial revoked -> BLOCK
CA085 serial revoked -> BLOCK
expired/not-yet-valid CRL -> BLOCK
missing nextUpdate -> BLOCK
delta CRL -> BLOCK
indirect CRL -> BLOCK
unsupported issuingDistributionPoint scope -> BLOCK
redirect -> BLOCK
HTTP/non-authority URL -> BLOCK
proxy environment cannot alter direct client
custom/system CA injection -> BLOCK
wrong vendored certifi wheel hash -> BLOCK
TLS hostname/path validation failure -> BLOCK
response status != 200 -> BLOCK
Age > 0 -> BLOCK
Via or Warning present -> BLOCK
Date outside +/-120s gate window -> BLOCK
oversized/transformed response -> BLOCK
network unavailable/ambiguous -> BLOCK
query-token endpoint incompatibility -> positive path BLOCK, no weakening
V4 CRL bytes differ at final live gate -> BLOCK/new V4+final
blocking/network/Human/TPM operation after linearization -> BLOCK/relinearize
linearization-to-rename > 2.000s -> BLOCK/relinearize
CRL published after successful linearization -> later external event; does not retroactively fail that linearized gate
```

Independent review MUST test whether the exact Infineon endpoints support the frozen query/header/response profile; a nonimplementable positive path is a blocker.

## 43. PR #147 F002 regressions

Must include:

```text
valid TPM quote but no V4 Human locality act -> BLOCK
TPM passthrough guest with same physical EK/AK but no Human bare-metal assertion -> BLOCK
TPM command proxy with valid quotes but no accepted host-console observation -> BLOCK
V4 created before physical ref lock -> BLOCK
nonce generated before ref lock -> BLOCK
caller-supplied/replayed nonce -> BLOCK
V4 executor identity mismatch -> BLOCK
process restart/PID reuse/starttime drift -> BLOCK
exe dev/inode/digest drift -> BLOCK
namespace/cgroup/boot_id/credential drift -> BLOCK
observation_channel=ssh -> BLOCK
observation_channel=vm-console -> BLOCK
observation_channel=ci-log -> BLOCK
tpm_proxy != absent -> BLOCK
tpm_passthrough != absent -> BLOCK
execution_locality != physical-host -> BLOCK
code/evidence claims TPM cryptographically proves CPU locality -> nonconforming
V4 >120s at rename -> BLOCK
final V17 >120s -> BLOCK
new V4 with old final decision -> BLOCK
ref lock lost/replaced -> BLOCK/new challenge
```

Positive Human control must show the exact fresh challenge was observed through an accepted out-of-band host channel by a separately authorized Human. AI-created V4 evidence cannot satisfy that control.

## 44. Preserve TPM / PKI regressions

```text
self-issued leaf matching EK -> BLOCK
untrusted/alternate CA -> BLOCK
wrong root/intermediate -> BLOCK
wrong SAN manufacturer/model/version -> BLOCK
wrong EKU/KeyUsage/BasicConstraints -> BLOCK
current EK point != authenticated leaf SPKI -> BLOCK
wrong AK -> BLOCK
Name/QName substitution -> BLOCK
old quote/new request or gate -> BLOCK
copied EK cert without EK private capability -> ActivateCredential BLOCK
same snapshot/different TPM -> BLOCK
clear/EPS/reset/restart/PCR/IMA/firmware drift -> BLOCK
safe=0 -> BLOCK
non-increasing TPM clock -> BLOCK
invalid quote signature -> BLOCK
```

## 45. Preserve storage/Git regressions

Preserve all predecessor NFIT/storage, ext4, proc/userns/idmap, casefold/inode flags, staging/mtime/object closure, alternates/promisor/lazy fetch, replacement refs, split/shared index, main-ref alias, hook/filter/config, lost CAS, reflog/worktree and post-effect uncertainty negatives.

# PART IX — CURRENT EXTERNAL SEMANTICS

## 46. RFC CRL semantics checked

Current public semantics checked on 2026-09-02:

```text
RFC 5280
RFC 10007 (June 2026; updates RFC 5280 CRL validation keyUsage processing)
```

R4R17 relies on:

```text
CRLNumber is monotonically increasing for a given issuer/scope
CRLNumber enables supersession determination
a suitably recent CRL normally means the most recently issued applicable CRL
CRL-signing certificate must be authorized by keyUsage cRLSign
```

## 47. Infineon publication semantics checked

Current Infineon public material identifies:

```text
CA085 = SLB 9670 FW7.87
CA085 ECC CRL publication point
OPTIGA ECC Root CRL publication point
```

The section-15 URLs are frozen V17 current-publication authority.

## 48. certifi provenance checked

Current PyPI metadata on 2026-09-02 identifies release `2026.7.22` and wheel:

```text
certifi-2026.7.22-py3-none-any.whl
size = 136983 bytes
SHA-256 = 62f22742b58a1a33014a2b6b706588a8d7e2a88ae7bd1a6ebe8c992928483775
Trusted Publishing = yes
source tag = refs/tags/2026.07.22
source commit = f4bc676bc101fe2235846e37044e8c693d6cbaf4
```

Certifi supplies Mozilla's curated CA bundle for TLS server identity verification. Runtime cannot choose another bundle.

## 49. QEMU passthrough semantic retained

Current QEMU documentation explicitly supports exposing host `/dev/tpm0` to a guest through the TPM passthrough backend and forwarding guest TPM commands to the host hardware TPM.

Therefore R4R17 deliberately treats:

```text
valid physical TPM quote
```

as insufficient CPU-locality proof.

# PART X — INDEPENDENT REVIEW CHECKLIST

## 50. Independent R4R17 review must answer at least

```text
Does live publication equality reject an authentic superseded Human-stapled CRL?
Are CRLNumber/AKI/scope/cRLSign rules semantically correct?
Is pki.infineon.com response explicitly the intended current-publication trust boundary?
Can cache/CDN/proxy behavior make a stale response pass the frozen transport predicate?
Is the certifi wheel provenance exact and runtime substitution excluded?
Do the exact Infineon URLs accept the query token and frozen headers?
Do real responses satisfy status/body/Date/Age/Via/Warning requirements?
Is a positive currentness path demonstrably implementable rather than only fail-closed?
Is PRE_REF_RENAME_CRL_LINEARIZATION_POINT defined after all other blocking authority reads?
Can any hidden operation after linearization delay or invalidate the 2s bound?
Is a CRL published after the linearization point correctly classified as a later external event rather than pre-gate rollback?
Does main-ref commitment really occur without network/Human/TPM reads after linearization?
Does R4R17 correctly stop claiming TPM->CPU cryptographic locality?
Is Human V4 explicitly the authority for physical-host/no-proxy locality?
Does V4 bind exact effect-capable process identity, ref lock, effect, TPM, platform and CRL state?
Can a VM/TPM proxy display a matching challenge while causing an honest Human using an allowed channel to believe it is host execution?
Is residual risk explicitly trusted-Human environmental judgment rather than hidden machine inference?
Does fresh nonce-in-V4 body correctly establish post-lock causal sequencing without local wall-clock authority?
Are V4/final 120s windows compatible with a real separately authorized Human positive control?
Does ref-lock-first waiting preserve CAS and avoid unauthorized canonical effect before Human authority?
Are all earlier Name/QName, EK path, PlatformSnapshot, NFIT, ext4 and Git durability corrections preserved?
```

## 51. Intended predecessor-finding disposition target

If independent review finds no new blocker:

```text
R4R16 F001 offline CRL rollback = ADDRESSED AT BRIEF LEVEL BY LIVE ISSUER-PUBLICATION EQUALITY + LINEARIZATION
R4R16 F002 false TPM->CPU locality inference = ADDRESSED AT BRIEF LEVEL BY EXPLICIT FRESH HUMAN EXECUTOR-LOCALITY AUTHORITY
```

This is a review target, not a predeclared PASS.

# PART XI — STOP

## 52. Explicit non-authority

This brief does not authorize:

```text
independent R4R17 review under this accept
ScriptOps implementation
certifi vendoring in ScriptOps
TPM provisioning/persistence
TPM clear/NV/hierarchy mutation
Human V4 platform/locality review
Human final V17 decision
positive control
canonical effect
recovery
merge
X1B closure
V1 authority
release/deployment/tag
```

## 53. Next legal step

After exact R4R17 brief is frozen in one draft PR, STOP.

```text
fresh Human authorization
-> exactly one independent AK-CANON adversarial review
   of exact frozen R4R17 implementation brief
```

Preserve:

```text
AI PROPOSES != HUMAN DECIDES
REVIEW FINDING != REPAIR AUTHORITY
R4R17 BRIEF != IMPLEMENTATION AUTHORITY
R4R17 REVIEW PASS != IMPLEMENTATION AUTHORITY
X1B OPEN != V1 AUTHORITY
```
