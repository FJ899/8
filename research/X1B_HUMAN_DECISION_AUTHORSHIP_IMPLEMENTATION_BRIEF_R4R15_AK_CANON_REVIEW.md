# X1B Human Decision Authorship — Independent AK-CANON R4R15 Implementation-Brief Review

Status: `INDEPENDENT REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: `2026-09-02`

## 1. Verdict

`AK-CANON X1B R4R15 IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

R4R15 materially improves the R4R14 platform-attestation design.

The independent review records the two exact PR #143 findings as addressed at brief level for their original mechanisms:

```text
R4R14 F001 OPAQUE PLATFORM-SNAPSHOT ATTESTATION TARGET = ADDRESSED AT BRIEF LEVEL
R4R14 F002 TRANSFERABLE DIGEST-ONLY ENVIRONMENT ATTESTATION = ADDRESSED AT BRIEF LEVEL FOR WRONG-HOST / DIFFERENT-vTPM REPLAY
```

R4R15 now publishes the exact bounded canonical platform-snapshot preimage in the immutable request and introduces request-specific TPM evidence, a pre-existing AK, fresh MakeCredential/ActivateCredential challenges, fresh quote nonces, PCR/clock lifecycle continuity and a distinct Human V2 platform review.

However, two independent TPM-profile defects prevent implementation authority:

```text
X1B-R4R15-IBR-F001 — TPMS_ATTEST qualifiedSigner IS BOUND TO AK Name INSTEAD OF AK Qualified Name = BLOCKER
X1B-R4R15-IBR-F002 — EK CERTIFICATE TRUST PATH / TRUST ANCHOR IS NOT FROZEN OR VALIDATED = BLOCKER
```

Either blocker independently prevents PASS.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R15 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R15 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#144`

```text
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
BASE TREE = df807db7003dfd201e9be4d5927472e515a2e737
HEAD = 5cb4c0e650e648efab844f08ddd4be7cc9b2d0c3
TREE = ade1f1db4b52ea0e75cedea17af29f92fcfc0d4b
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R15.md
BLOB = 341eb23b5d185eeb2f91f7035fc12280753ca301
```

Immediately before review preparation PR #144 remained:

```text
state = OPEN
merged = false
draft = true
mergeable = true
commits = 1
changed_files = 1
additions = 1277
deletions = 0
```

`FJ899/8 main` remained exactly:

```text
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

The exact R4R15 file was freshly reread from the reviewed HEAD before this review artifact was written.

## 3. Binding governance lineage

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
separate trusted Human decision act
exact content/scope/candidate/effect binding
explicit freshness/activity/supersession/conflict/replay semantics
executor no-substitution
fail closed on ambiguity
real-boundary negative regressions
real separately authorized positive Human control
post-effect truth matching Human-bound effect
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
VERDICT = PASS
```

### 3.3 R4R14 predecessor

```text
FJ899/8 PR #142
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 1e5b39b04a61f4b2d487ee086ae1b99ea0f33a53
TREE = d8b1e130576d1ee8e5337e5b78b6ec0ade412222
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R14.md
BLOB = f857390bf30dc4357e3b91db194096e962878c66
```

### 3.4 Binding R4R14 NOT-PASS review

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

## 4. Review method

The independent pass attacked the exact frozen R4R15 artifact rather than assuming that adding a TPM makes the environmental premise non-transferable.

The review inspected at least:

```text
exact PR/base/head/blob freeze
published PlatformSnapshotV15 byte-preimage rules
request/snapshot length and digest binding
request-attestation nonce binding
TPM character-device/sysfs provenance
ECC EK construction and certificate source
persistent AK public attributes
AK Name versus Qualified Name semantics
TPM2_Quote TPMS_ATTEST fields
quote extraData request/stage binding
PCR selection and PCR-digest verification
TPM clock/reset/restart/safe continuity
IMA/PCR10 replay rule
MakeCredential/ActivateCredential semantics
EK/AK co-residency claim
V2 Human platform review enrollment
final Human V15 review binding
same-host physical TPM passthrough/proxy threat
prior NFIT/ext4/object/ref/index controls
```

The review distinguishes four questions:

```text
A. can the Human inspect the exact snapshot preimage?
B. does current quote evidence identify the intended TPM/AK?
C. is the TPM identity itself authenticated as the intended physical TPM root?
D. does the quote parser compare each signed field to the correct TPM semantic identity?
```

R4R15 materially improves A and request-specific liveness.

The frozen blockers are C and D.

## 5. Current external semantics checked

The review independently checked current public TPM/QEMU material on 2026-09-02.

Current TCG TPM Library landing page identifies TPM 2.0 Library Version 185 as the current base library and current TCG material defines `TPMS_ATTEST.qualifiedSigner` as the **Qualified Name of the signing key**.

Relevant TCG resources:

```text
https://trustedcomputinggroup.org/resource/tpm-library-specification/
https://trustedcomputinggroup.org/resource/http-trustedcomputinggroup-org-wp-content-uploads-tcg-ek-credential-profile/
```

Current TCG EK Credential Profile landing page identifies Version 2.7 dated 2026-03-19 as current. Current profile material defines the low-range ECC NIST P-256 EK certificate index as:

```text
0x01c0000a = ECC NIST P256 EK Certificate
```

and treats the value as an X.509 DER EK certificate. Current profile material also provides optional EK certificate-chain indices and specifies that the Root CA certificate is not stored in TPM NV.

Current QEMU source/docs at commit:

```text
a925240509d1b4b656cc480f1cc79ba4d7c8bc08
```

explicitly implement a TPM passthrough backend in which a Linux host hardware TPM can be made available to a QEMU guest. QEMU documents:

```text
-tpmdev passthrough,id=tpm0,path=/dev/tpm0
-device tpm-tis,tpmdev=tpm0
```

and describes the backend as sending commands to and receiving responses from the host TPM device.

Relevant QEMU paths:

```text
docs/specs/tpm.rst
backends/tpm/tpm_passthrough.c
```

This QEMU fact is retained as an adversarial observation in section 11 below.

## 6. PR #143 F001 disposition — opaque snapshot target

Disposition:

```text
ADDRESSED AT BRIEF LEVEL FOR THE EXACT PRIOR MECHANISM
```

R4R15 no longer asks a Human to approve only:

```text
platform_snapshot_sha256=<opaque digest>
```

It defines an exact bounded canonical block:

```text
-----BEGIN X1B-PLATFORM-SNAPSHOT-V15-----
...
-----END X1B-PLATFORM-SNAPSHOT-V15-----
```

and requires Human-review-required raw values to be published as full preimages with exact length, raw hex and semantic value.

The immutable DecisionRequestV15 contains the exact snapshot block and request digest covers the exact bytes.

The request and snapshot are size bounded; truncation is not an authorized fallback.

The V2 platform review binds the exact request and snapshot digest, while the executor reconstructs and compares the current snapshot byte-for-byte.

No new blocker was found against the narrow property that the snapshot target is now Human-reviewable rather than digest-only.

## 7. PR #143 F002 disposition — wrong-host/different-vTPM replay

Disposition:

```text
MATERIALLY ADDRESSED FOR THE EXACT SIMPLE WRONG-HOST / DIFFERENT-vTPM MECHANISM
```

R4R15 introduces all of:

```text
per-request getrandom nonce
exact enrolled EK certificate/public key
exact pre-existing fixedTPM/fixedParent AK
reference quote bound to request/snapshot/nonce
fresh MakeCredential/ActivateCredential
fresh live gate quote nonce
PCR0/2/4/7/10 continuity
TPM reset/restart/safe/clock/firmware continuity
V2 Human enrollment of the exact EK/AK/reference quote
```

A different TPM or a copied old quote does not satisfy those rules.

The independent review therefore does not simply repeat PR #143 F002 as though R4R15 had made no correction.

The new blockers are defects in the TPM identity/quote profile itself.

# FINDING 1

## 8. X1B-R4R15-IBR-F001 — TPMS_ATTEST qualifiedSigner is compared to AK Name instead of AK Qualified Name

Severity: `BLOCKER`.

### 8.1 R4R15 binds both Name and Qualified Name but requires the wrong signed identity

R4R15 section 24 requires `TPM2_ReadPublic` to bind:

```text
AK Name
AK Qualified Name (when available)
```

However section 28 requires:

```text
qualifiedSigner = exact AK Name
```

and section 35 repeats the same gate-quote requirement:

```text
qualifiedSigner = exact AK Name
```

The V2 marker also enrolls only:

```text
tpm_ak_name=<...>
```

as the quote signer identity carried into the Human authority record.

### 8.2 TPM semantics are explicit: qualifiedSigner is a Qualified Name

`TPMS_ATTEST.qualifiedSigner` is not defined as the object's ordinary Name.

The TPM Library defines it as:

```text
TPM2B_NAME qualifiedSigner = Qualified Name of the signing key
```

Name and Qualified Name are distinct TPM concepts.

The Qualified Name cryptographically incorporates the object's hierarchy/ancestry relationship; the ordinary Name identifies the public area.

R4R15 already acknowledges the distinction by saying that both Name and Qualified Name are bound, but then compares the signed `qualifiedSigner` field to the wrong one.

### 8.3 Consequence

A conforming TPM quote signed by the exact intended AK can have:

```text
TPMS_ATTEST.qualifiedSigner = exact AK Qualified Name
```

while R4R15 demands:

```text
TPMS_ATTEST.qualifiedSigner = exact AK Name
```

Those are not semantically interchangeable.

Therefore the brief has no frozen correct parser/acceptance rule for the quote signer identity.

An implementer must either:

```text
reject a conforming intended quote
OR
silently reinterpret "AK Name" as Qualified Name
OR
change the brief's identity semantics during implementation
```

All three outcomes violate the requirement that authority-critical choices be frozen before implementation.

### 8.4 This is not repaired by signature verification

ECDSA verification with the AK public key proves that the signature matches the public key.

It does not make an incorrect signed-field predicate correct.

The design explicitly uses `qualifiedSigner` as a bound TPM-generated identity field. That field must be compared to the semantic identity defined by the TPM specification.

### 8.5 This finding is independent of EK certificate trust

Even if a successor perfectly authenticates the EK certificate chain and manufacturer trust root, the quote parser still has the wrong `qualifiedSigner` equality predicate.

Therefore F001 survives an F002-only repair.

### 8.6 Required successor correction

A successor must freeze at least:

```text
exact AK Name bytes
exact AK Qualified Name bytes
exact rule for deriving/reading/verifying both
TPMS_ATTEST.qualifiedSigner == exact AK Qualified Name
MakeCredential credentialed-name input == exact AK Name where TPM semantics require Name
V2 Human marker/reference evidence binds the exact Qualified Name used for quote signer checks
all reference/gate regressions distinguish Name from Qualified Name
```

No implementation alias such as:

```text
"name" means either Name or Qualified Name
```

is acceptable.

Until corrected:

```text
X1B-R4R15-IBR-F001 = BLOCKER
```

# FINDING 2

## 9. X1B-R4R15-IBR-F002 — EK certificate trust path / trust anchor is not frozen or validated

Severity: `BLOCKER`.

### 9.1 What R4R15 actually validates

R4R15 section 23 requires:

```text
TPM 2.0 ECC NIST P-256 EK
EK cert read from NV index 0x01C0000A
nameAlg SHA256
TCG default ECC P-256 EK template
```

and binds:

```text
DER certificate bytes/digest
SPKI digest/public point
issuer
subject
serial
validity interval
current EK TPM public area
```

It then requires:

```text
current EK public point == certificate SPKI public key
```

This proves only that the TPM-presented leaf certificate and the current EK public point agree.

### 9.2 Missing authority: who issued and authenticated that certificate?

The brief contains no normative requirement to validate the leaf EK certificate signature through a certificate chain to a pinned trusted manufacturer/OEM/TCG-approved trust anchor.

It freezes no exact:

```text
trusted root CA certificate bytes or digest
trusted root SPKI digest
allowed issuing/intermediate certificate chain
certificate path-building rule
signature-policy rule
revocation rule
revocation evidence snapshot
trusted time source for validity evaluation
```

No system trust store is named, but no replacement trust root is frozen either.

### 9.3 The current EK profile makes the omission material

Current TCG EK credential material explicitly treats the EK value as an X.509 certificate and provides for EK certificate chains.

The Root CA certificate is not expected to come from the TPM NV chain storage.

Therefore:

```text
leaf certificate present in NV
+
leaf SPKI == current EK public point
```

is not by itself an authenticated manufacturer-issued EK credential.

The missing trust anchor must come from somewhere outside the leaf bytes.

R4R15 does not say where.

### 9.4 Concrete untrusted-certificate class

A software/vTPM implementation can in principle present:

```text
its own ECC P-256 EK
an X.509 certificate blob at the expected NV index
that certificate's SPKI matching its own EK
issuer/subject/serial/validity fields that parse successfully
```

Without chain/trust-anchor validation, the executor has no cryptographic rule that distinguishes:

```text
manufacturer-authenticated physical EK credential
```

from:

```text
certificate-shaped bytes controlled by the TPM implementation itself
```

The guest sysfs anti-vTPM checks do not repair this because the threat model already recognizes that guest-visible hardware shape can be synthesized.

### 9.5 Human V2 review does not freeze the missing PKI policy

The V2 Human review binds the exact EK certificate digest and asserts that the EK/AK belongs to the intended physical machine.

That is useful external evidence, but it does not define the cryptographic trust policy by which the executor calls the profile:

```text
PHYSICAL_TPM2_ECC_EK_AK_V1
```

The higher-level contract forbids leaving a core authority/security choice implicit.

Whether a particular X.509 issuer is trusted to authenticate the hardware root is exactly such a choice.

The Human cannot be presumed to silently supply an unspecified CA-validation policy merely by approving a digest.

### 9.6 This finding is independent of qualifiedSigner

Suppose a successor fixes F001 and correctly compares the quote's `qualifiedSigner` to the AK Qualified Name.

A self-issued or otherwise untrusted EK certificate whose SPKI matches the current EK would still pass the frozen section-23 checks because no chain/trust anchor is verified.

Therefore F002 survives an F001-only repair.

### 9.7 Required successor correction

A successor must choose and freeze one bounded trust model.

A narrow reviewable direction is:

```text
one explicitly supported TPM manufacturer/model profile
exact accepted root CA certificate DER SHA-256 and/or SPKI SHA-256 frozen in the brief
exact allowed intermediate/issuing chain rules
exact X.509 signature/path validation algorithm
exact EK leaf/profile constraints needed by the supported platform
exact trusted time authority for certificate validity
explicit revocation policy and fail-closed behavior
all chain certificates/evidence included in the bounded Human-reviewable V2 evidence
current EK public point must still equal authenticated leaf SPKI
```

Alternative trust systems are possible, but implementation may not choose one implicitly.

A generic OS/system trust store, opportunistic network lookup or caller-supplied root is not frozen authority.

Until corrected:

```text
X1B-R4R15-IBR-F002 = BLOCKER
```

## 10. Snapshot publication remains addressed

The two new TPM findings do not reopen the snapshot-preimage correction.

R4R15 requires:

```text
full canonical snapshot block in request
full Human-required raw preimages
exact len/digest
request digest covering exact block
bounded maximum sizes
no truncation
byte-for-byte current reconstruction
```

Disposition remains:

```text
R4R14 F001 OPAQUE PLATFORM SNAPSHOT = ADDRESSED AT BRIEF LEVEL
```

## 11. Same-host physical TPM passthrough/proxy — review observation, not third frozen blocker

R4R15 correctly required this independent review to attack same-host physical TPM passthrough/proxy.

Current QEMU documents a concrete passthrough mode in which the host's hardware TPM `/dev/tpm0` is made available to a guest and TPM commands are sent to the host hardware device.

This matters because it demonstrates the general proposition:

```text
fresh valid quote from exact physical EK/AK
!= by itself
proof that the Linux CPU context consuming the quote is bare-metal rather than a VM using that TPM
```

QEMU also warns that host/guest sharing of the physical TPM is not a recommended scenario because both operating systems would share one set of PCR resources and subsystems such as IMA do not expect that sharing.

R4R15's exact PCR10/IMA replay and lifecycle rules may block a straightforward stock-QEMU passthrough sequence, so this review does **not** freeze passthrough as a third blocker without a complete passing counterexample under the brief's trusted-kernel assumptions.

However, fixing F001/F002 must not erase this attack surface.

The next independent review must again test at least:

```text
same-host hardware TPM passthrough
TPM command proxy to a guest
host and guest sharing the physical PCR set
reference IMA/PCR10 continuity under passthrough
whether any allowed transport decouples TPM possession from executor CPU/platform identity
whether an out-of-band Human no-proxy statement is the only remaining barrier
```

If, after the two deterministic blockers are repaired, the exact accepted V15 successor still permits physical TPM proxy while preserving all frozen continuity predicates, that must become a blocker then.

## 12. PCR10/IMA disposition

No blocker is frozen against the mere use of PCR10 as a continuity-only signal.

R4R15 explicitly says PCR10 is not a semantic bare-metal proof and requires replay of authenticated IMA measurements to current PCR10.

The review therefore does not mischaracterize PCR10 as proving hardware provenance.

Successor work must preserve that limitation.

## 13. MakeCredential/ActivateCredential disposition

The review accepts the narrow intended semantic role:

```text
fresh challenge
+
MakeCredential against enrolled EK public and AK Name
+
ActivateCredential using current AK/EK
+
exact recovered secret
```

as evidence that the current credentialed AK is available on the TPM possessing the corresponding EK private capability.

This does not authenticate the EK certificate issuer; that is F002.

It also does not correct the `TPMS_ATTEST.qualifiedSigner` Name/Qualified-Name bug; that is F001.

## 14. Prior NFIT/ext4 corrections remain preserved

The review found no R4R15 change that reopens the previously addressed storage findings.

Preserved:

```text
nfit/format = 0x0101 only
persistence_domain = cpu_cache only
deep_flush = 0 only
internal ext4 journal raw predicate
closed ext4 runtime option table
barrier/data-mode restrictions
no active DAX
ext4 errors_count = 0
```

No new blocker is raised against those preserved brief-level mechanisms in this review.

## 15. Earlier procfs/filesystem/Git controls remain preserved

The two TPM findings do not reopen:

```text
current-task procfs provenance
initial user namespace and uid/gid maps
credential stability
non-ID-mapped mount
casefold/inode semantic flags
Human-bound loose-object mtime
bounded object staging
hardlink/alias-safe loose objects
closed local object store
single-file raw index / no split-index
physical loose main ref
reflog projection
worktree projection
replacement-ref closure
hook/filter/config closure
lazy-fetch/promisor closure
ref CAS and post-effect truth rules
```

## 16. Mandatory successor regressions implied by F001

A successor review must test at least:

```text
AK Name != AK Qualified Name -> expected and explicitly handled
TPMS_ATTEST.qualifiedSigner == exact AK Qualified Name -> prerequisite
TPMS_ATTEST.qualifiedSigner == only AK Name -> BLOCK
wrong Qualified Name with valid AK signature -> BLOCK
right Qualified Name with wrong AK signature -> BLOCK
reference quote and every gate quote use identical Qualified-Name semantics
V2 evidence binds both exact Name and Qualified Name
MakeCredential uses the TPM-defined credentialed Name input and does not substitute Qualified Name
implementation cannot alias Name/Qualified Name strings
```

## 17. Mandatory successor regressions implied by F002

At minimum:

```text
leaf EK cert SPKI matches EK but chain untrusted -> BLOCK
self-signed EK cert matching current EK -> BLOCK
leaf chain ends at unknown root -> BLOCK
wrong manufacturer root -> BLOCK
intermediate signature/path failure -> BLOCK
certificate expired/not-yet-valid under frozen trusted time -> BLOCK
revoked credential under frozen revocation policy -> BLOCK
caller-supplied root -> BLOCK
ambient OS trust-store-only acceptance -> BLOCK
network-fetched opportunistic root -> BLOCK
exact pinned supported root/path + matching EK SPKI -> positive prerequisite
V2 Human evidence binds exact authenticated certificate-chain evidence
```

## 18. Preserve PR #143 snapshot regressions

```text
request publishes digest only -> BLOCK
snapshot block absent/truncated -> BLOCK
snapshot len/digest mismatch -> BLOCK
Human-required raw value hidden behind digest -> BLOCK
current snapshot byte mismatch -> BLOCK
V2 snapshot mismatch -> BLOCK
```

## 19. Preserve TPM liveness regressions

```text
old quote/new request -> extraData mismatch BLOCK
old quote/new gate -> fresh nonce mismatch BLOCK
wrong AK -> BLOCK
same snapshot/different TPM -> BLOCK
TPM clear/EPS/AK change -> BLOCK
reset/restart drift -> BLOCK
PCR0/2/4/7/10 drift -> BLOCK
IMA/PCR10 replay inconsistency -> BLOCK
firmware drift -> BLOCK
safe=0 -> BLOCK
non-increasing clock -> BLOCK
invalid quote signature/PCR digest -> BLOCK
```

These are preserved as intended requirements; F001 changes only the signer-identity comparison to the correct Qualified Name semantic.

## 20. Verdict matrix

```text
PR #143 F001 opaque platform-snapshot target              = ADDRESSED AT BRIEF LEVEL
PR #143 F002 digest-only transferable environment binding = MATERIALLY ADDRESSED FOR WRONG-HOST / DIFFERENT-vTPM REPLAY
R4R14 NFIT persistence-domain/deep-flush                  = PRESERVED
R4R13 internal ext4 journal                               = PRESERVED
R4R13 closed ext4 runtime option table                    = PRESERVED

X1B-R4R15-IBR-F001 qualifiedSigner Name/QName semantics   = BLOCKER
X1B-R4R15-IBR-F002 EK certificate trust path/root         = BLOCKER

AK-CANON X1B R4R15 IMPLEMENTATION-BRIEF REVIEW            = NOT PASS
IMPLEMENTATION AUTHORITY                                   = NOT ESTABLISHED
X1B                                                        = OPEN
V1 AUTHORITY                                               = NOT ESTABLISHED
```

## 21. Required successor direction

A successor corrective implementation brief must correct both blockers without weakening the successful R4R15 snapshot/liveness work.

At minimum it must freeze:

```text
A. AK Name versus Qualified Name as distinct exact TPM identities, with TPMS_ATTEST.qualifiedSigner bound to exact Qualified Name
B. one explicit authenticated EK credential trust path, with pinned root/trust anchor, deterministic chain validation, time and revocation semantics
```

It must preserve:

```text
published exact snapshot preimage
per-request nonce
fresh activation
fresh gate quote nonces
PCR/clock lifecycle continuity
V2/final-Human separation
NFIT/ext4/object/ref/index controls
```

and the next independent review must continue attacking same-host physical TPM passthrough/proxy after these two deterministic TPM-profile defects are removed.

## 22. No implementation authority

This artifact is review evidence only.

It does not authorize:

```text
R4R16 or another successor correction
ScriptOps implementation
TPM provisioning/persistence mutation
Human V2 platform-attestation creation
Human final-decision creation
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

## 23. Exact STOP boundary

After this review artifact is durably frozen in one draft PR, STOP.

Required next legal step:

```text
fresh Human authorization
-> one successor corrective implementation brief addressing
   X1B-R4R15-IBR-F001
   X1B-R4R15-IBR-F002
```

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R15 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```
