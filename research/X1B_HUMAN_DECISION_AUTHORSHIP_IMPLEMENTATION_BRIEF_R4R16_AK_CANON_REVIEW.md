# X1B Human Decision Authorship — Independent AK-CANON R4R16 Implementation-Brief Review

Status: `INDEPENDENT REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: `2026-09-02`

## 1. Verdict

`AK-CANON X1B R4R16 IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

R4R16 materially corrects both deterministic defects frozen by PR #145:

```text
R4R15 F001 Name / Qualified-Name signer mismatch = ADDRESSED AT BRIEF LEVEL
R4R15 F002 missing EK trust path / trust anchor = ADDRESSED AT BRIEF LEVEL FOR THE EXACT PINNED INFINEON PROFILE
```

The ordinary AK Name and AK Qualified Name are now distinct typed values. Quote `qualifiedSigner` is compared to the Qualified Name, while MakeCredential continues to use the ordinary Name.

The EK leaf is no longer self-authenticating. R4R16 pins an exact Infineon OPTIGA ECC Root CA, closes the positive profile to CA085 / SLB 9670 FW7.87, requires a complete intermediate, verifies leaf and intermediate signatures, and requires two signed offline CRLs.

However, independent review found two new authority blockers:

```text
X1B-R4R16-IBR-F001 — OFFLINE CRL ROLLBACK / LATEST-ISSUER-STATE IS NOT BOUND = BLOCKER
X1B-R4R16-IBR-F002 — PHYSICAL TPM QUOTE DOES NOT BIND THE EXECUTING CPU / TPM TRANSPORT LOCALITY = BLOCKER
```

Either blocker independently prevents PASS.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R16 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R16 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#146`

```text
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
BASE TREE = df807db7003dfd201e9be4d5927472e515a2e737
HEAD = d390390f9523c10dd7741a8c4aa7ae3c4895128b
TREE = 396327e9cb70ed5941bfeeb87cc22b2e80547e31
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R16.md
BLOB = 86ca7ad54e04c8e52749453ffe1a8fdda8a9c369
```

Immediately before review preparation PR #146 remained:

```text
state = OPEN
merged = false
draft = true
mergeable = true
commits = 1
changed_files = 1
additions = 1239
deletions = 0
```

`FJ899/8 main` remained exactly:

```text
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

`FJ899/scriptops main` remained exactly:

```text
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

The exact R4R16 file was freshly reread from reviewed HEAD before this review artifact was written.

## 3. Binding governance lineage

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

PR #145 froze:

```text
X1B-R4R15-IBR-F001 — TPMS_ATTEST qualifiedSigner bound to AK Name instead of AK Qualified Name
X1B-R4R15-IBR-F002 — EK certificate trust path / trust anchor not frozen or validated
```

PR #145 separately required same-host hardware-TPM passthrough/proxy to remain an explicit adversarial target.

## 4. Review method

The review attacked the exact frozen R4R16 brief rather than treating “pinned root + fresh quote” as sufficient proof of a current bare-metal execution environment.

The pass inspected at least:

```text
exact PR/base/head/blob freeze
AK ordinary Name derivation
AK Qualified Name typing
TPMS_ATTEST qualifiedSigner predicate
MakeCredential objectName predicate
embedded root DER and hashes
CA085 closed path
leaf SAN / EKU / KeyUsage profile
certificate validation time
CRL issuer/signature/time rules
CRL rollback / supersession semantics
V3 Human evidence binding
request / gate quote liveness
PCR0/2/4/7/10 continuity
IMA replay rule
same-host TPM passthrough
TPM command proxy to a VM
guest-visible platform snapshot substitution
prior NFIT/ext4/object/ref/index controls
```

## 5. Current external semantics checked

Current public material checked on 2026-09-02 includes:

```text
RFC 5280 — Internet X.509 PKI Certificate and CRL Profile
https://www.rfc-editor.org/rfc/rfc5280

Infineon OPTIGA TPM & Trust certificates
https://www.infineon.com/design-resources/platforms/optiga-software-tools/optiga-tpm-and-trust-certificates

Infineon CA085 publication identifiers
https://pki.infineon.com/OptigaEccMfrCA085/OptigaEccMfrCA085.crt
https://pki.infineon.com/OptigaEccMfrCA085/OptigaEccMfrCA085.crl

Infineon OPTIGA ECC Root publication identifiers
https://pki.infineon.com/OptigaEccRootCA/OptigaEccRootCA.crt
https://pki.infineon.com/OptigaEccRootCA/OptigaEccRootCA.crl

QEMU TPM documentation
https://www.qemu.org/docs/master/specs/tpm
```

Infineon currently publishes CA085 specifically for SLB 9670 FW7.87 and publishes separate ECC CRLs for CA085 and for the OPTIGA TPM root.

The embedded R4R16 root DER was independently decoded. Its byte length is 607 and its SHA-256 is:

```text
cfeb02fecd55ad7a73c6e1d11985d4c47dee248ab63dcb66091a2489660443c3
```

Its SPKI SHA-256 is:

```text
ce5183a19d6fe79a6c1b058cfa700379f67d587a8afd0f51621e82d9f00c5a28
```

Those values match the R4R16 pinned constants.

RFC 5280 states that a suitably recent CRL usually means the most recently issued CRL. It also defines `CRLNumber` as a monotonically increasing issuer/scope sequence that allows a verifier to determine when one CRL supersedes another.

Current QEMU documentation states that on a Linux host the host hardware TPM can be exposed to a QEMU guest through the passthrough backend, with commands sent to and responses received from the host TPM. QEMU also warns that host and guest then share one PCR set and that IMA does not expect such sharing.

# PREDECESSOR FINDING DISPOSITIONS

## 6. R4R15 F001 — Name / Qualified Name

Disposition:

```text
ADDRESSED AT BRIEF LEVEL
```

R4R16 now defines distinct typed values:

```text
AK_NAME
AK_QUALIFIED_NAME
```

It independently recomputes ordinary Name from exact `TPMT_PUBLIC` bytes and requires:

```text
ak_name_returned == AK_NAME
```

It separately binds the returned Qualified Name and requires every reference/live quote:

```text
TPMS_ATTEST.qualifiedSigner == AK_QUALIFIED_NAME
```

while MakeCredential continues to use:

```text
objectName == AK_NAME
```

The exact PR #145 semantic mismatch is therefore corrected.

## 7. R4R15 F002 — EK trust path

Disposition:

```text
ADDRESSED AT BRIEF LEVEL FOR THE EXACT PINNED ROOT / CA085 PATH MECHANISM
```

R4R16 no longer trusts a leaf merely because its SPKI matches the current EK.

It pins exact root DER/SPKI hashes, requires one CA085 intermediate, validates leaf/intermediate signatures, enforces Infineon / SLB 9670 FW7.87 SAN semantics, and requires current EK public point equality with the authenticated leaf SPKI.

The new CRL finding below does not mean the root/path correction failed. It is a distinct current-revocation-state defect after the path itself became authenticated.

# FINDING 1

## 8. X1B-R4R16-IBR-F001 — offline CRL rollback / latest issuer state is not bound

Severity: `BLOCKER`.

### 8.1 Frozen R4R16 CRL predicate

For both the CA085 leaf-status CRL and root-issued intermediate-status CRL, R4R16 requires:

```text
complete DER
digest bound in V3
issuer exact
signature valid under expected issuer
thisUpdate <= PKI_VALIDATION_TIME < nextUpdate
nextUpdate present
no indirect CRL
no delta CRL
no unknown critical CRL extension
certificate serial absent from revokedCertificates
```

Those checks establish that the stapled CRL is authentic and temporally usable.

They do **not** establish that it is the issuer's latest applicable complete CRL as of `PKI_VALIDATION_TIME`.

### 8.2 R4R16 does not bind CRLNumber or supersession

The brief contains no normative requirement to parse or bind:

```text
CRLNumber
AuthorityKeyIdentifier
most-recent CRLNumber for this issuer/scope
most-recent thisUpdate for this issuer/scope
issuer-signed publication sequence / manifest
anti-rollback state from a previous accepted request
```

Nor does it define an authenticated current publication source that the executor must compare against.

A signed CRL is therefore accepted solely because its validity window covers `submitted_at` and the target serial is absent.

### 8.3 Why `nextUpdate` does not solve rollback

RFC 5280 explicitly says the next CRL may be issued **before** the prior CRL's `nextUpdate` time.

Therefore two complete CRLs for the same issuer/scope can overlap in time:

```text
CRL N
  thisUpdate = T0
  nextUpdate = T2

CRL N+1
  thisUpdate = T1
  nextUpdate = T3

with T0 < T1 < submitted_at < T2
```

At `submitted_at`, both are temporally valid under the R4R16 rule.

RFC 5280 uses monotonically increasing `CRLNumber` precisely to identify supersession.

R4R16 does not use that field.

### 8.4 Concrete rollback class

Suppose CA085 issues:

```text
CRL N   -> target EK serial absent
CRL N+1 -> target EK serial revoked
```

and `submitted_at` occurs after CRL N+1 was issued but before CRL N's `nextUpdate`.

A V3 body stapling the older correctly signed CRL N still satisfies every frozen R4R16 CRL rule:

```text
issuer exact = yes
signature valid = yes
thisUpdate <= submitted_at < nextUpdate = yes
serial absent = yes
```

The executor accepts the revoked EK because it has no rule establishing that N+1 superseded N.

The same rollback class applies to the root-issued CRL that governs CA085 itself.

### 8.5 Trusted Human does not repair machine-state ambiguity

The trusted Human V3 act binds exact CRL bytes and digests, but the brief's machine-verifiable security claim is that the EK/CA is not revoked at the trusted validation time.

A Human can innocently use a cached but still temporally valid CRL.

No compromised Human is required for the counterexample.

Whether the accepted CRL is current is a core revocation-authority choice and cannot be inferred merely from approval of its digest.

### 8.6 `CRLNumber` is materially relevant current semantics

RFC 5280 defines the CRL Number extension as a monotonically increasing sequence for a CRL scope/issuer and says it allows users to determine when one CRL supersedes another.

A successor may choose a different anti-rollback mechanism, but the current brief must not leave the question implicit.

### 8.7 Required successor correction

A successor must freeze a fail-closed current-revocation-state mechanism for both CRLs.

At minimum it must distinguish:

```text
authentic but superseded CRL
from
current applicable CRL
```

A bounded correction needs explicit rules for at least:

```text
CRLNumber presence/type/scope
issuer AKI binding where applicable
supersession / monotonicity
how the executor learns the current issuer publication state
how stale-but-not-yet-nextUpdate CRLs are rejected
how rollback is detected without caller discretion
what happens if current-state evidence cannot be obtained
```

A system trust store, caller assertion, or “Human probably fetched the newest file” is not sufficient frozen authority.

Until corrected:

```text
X1B-R4R16-IBR-F001 = BLOCKER
```

# FINDING 2

## 9. X1B-R4R16-IBR-F002 — physical TPM quote does not bind executing CPU / TPM transport locality

Severity: `BLOCKER`.

### 9.1 R4R16 correctly proves access to the exact TPM

The following R4R16 mechanisms are meaningful and preserved:

```text
pinned authenticated EK credential
exact AK public / Name / Qualified Name
fresh MakeCredential / ActivateCredential
fresh reference and gate nonces
valid quote signature under exact AK
PCR0/2/4/7/10 equality
reset/restart/safe/clock continuity
IMA replay to PCR10
```

They prove current access to the intended physical TPM and its signed state.

They do **not** prove that the CPU/kernel execution context consuming the quote is the same bare-metal execution environment that the Human inspected.

### 9.2 Current QEMU establishes the missing transport property

Current QEMU documentation explicitly supports:

```text
-tpmdev passthrough,id=tpm0,path=/dev/tpm0
-device tpm-tis,tpmdev=tpm0
```

The backend sends TPM commands to and receives responses from the host hardware TPM while exposing a TPM frontend to the guest.

Therefore this proposition is false:

```text
fresh valid quote from exact physical TPM
=>
caller is bare-metal host CPU context
```

The quote authenticates the TPM, not the command transport endpoint.

### 9.3 V16 has no cryptographic transport/locality binding

The brief authenticates guest-visible TPM device/sysfs topology and rejects known virtual markers, but it explicitly says absence of a marker is not positive authority.

No signed TPM evidence in V16 contains an independently authenticated statement of:

```text
which CPU executed the verifier
which kernel instance submitted the TPM command
whether a hypervisor/proxy relayed that command
whether the TPM frontend was physical MMIO from this CPU or a mediated device
whether the bare-metal/no-proxy Human observation remains true at the effect gate
```

Fresh `extraData` only proves freshness and request/stage binding of the TPM signature. It does not authenticate the path over which the nonce reached the TPM.

### 9.4 Why PCR/IMA continuity is not a general transport proof

R4R16 explicitly treats PCR10 as a continuity signal, not semantic bare-metal proof.

That limitation is correct.

But the frozen predicate also does not bind an exact IMA policy that guarantees measurement of VM/hypervisor/proxy introduction.

The only IMA rule is essentially:

```text
authenticated guest securityfs log
replay(log) == quoted PCR10
```

This proves consistency between an accepted log and the accepted PCR value.

It does not prove that every virtualization/proxy transition capable of mediating TPM commands must change that PCR.

### 9.5 Complete proxy counterexample class

The bounded attack class does not require a forged EK certificate, stolen AK private key, replayed quote, compromised TPM hardware, or compromised trusted Human.

Start from a valid bare-metal request/V3 state on physical host `H`:

```text
H has exact supported Infineon TPM
H has valid EK/AK/PKI state
Human V3 truthfully observes bare-metal/no-proxy at submitted_at
reference PCRs and IMA log L are accepted
```

After V3 but before material commitment, introduce a VM execution environment `G` on the same host and a TPM command mediator.

The mediator can expose an ordinary TPM frontend to `G` while forwarding authority-bearing operations to the real host TPM:

```text
ReadPublic        -> real TPM
Quote             -> real TPM
ActivateCredential -> real TPM
GetCapability     -> real TPM
```

Fresh V16 request/gate nonces therefore receive genuinely fresh signatures from the exact enrolled physical AK. `ActivateCredential` also succeeds on the exact physical EK/AK.

For guest measurement commands, a mediator can avoid using guest extends as evidence of CPU locality. In the simplest attack class it can return successful virtualized measurement behavior while preserving the host physical PCR set used by the genuine quote.

R4R16 has no end-to-end authenticated TPM transport primitive that distinguishes that mediator from direct physical access.

### 9.6 PCR10 / IMA does not close the class

Because V16 does not freeze an IMA policy that uniquely binds the bare-metal execution instance, a supported state can have a deterministic non-empty IMA log `L` whose replay value is the accepted PCR10.

A guest constructed from the same measured software/policy can expose the same valid log semantics while the mediator keeps authority-bearing quotes on the host physical TPM state.

PCR0/2/4/7 do not have a separately replay-verified guest event log in V16; the quote merely requires equality with the reference values.

Thus fresh quote nonces, exact PCR values, exact reset/restart counts and increasing TPM clock can all remain properties of the physical host TPM while the effect-capable executor has moved behind a virtualization/proxy boundary.

### 9.7 Guest-visible platform snapshot does not restore CPU locality

Earlier review already established that guest ACPI/NFIT/sysfs state can be synthesized by a hypervisor and is not host provenance by itself.

R4R16 intentionally relies on TPM continuity to close that transferability gap.

Once the same physical TPM can be mediated into another execution context, the guest-visible snapshot is again only a consistency predicate, not a non-transferable execution-environment identity.

### 9.8 Human no-proxy statement is point-in-time, not live cryptographic continuity

The V3 Human marker says:

```text
environment_class=bare-metal
virtualization_layer=none
observation_channel=out-of-band-non-guest
```

and the Human premise includes no intentional TPM proxy/passthrough.

That premise can be true at `submitted_at` and false later within the 900-second window.

At later gates R4R16 refetches the same V3 body and obtains fresh TPM quotes, but no fresh Human observation or independent CPU-rooted proof establishes that the no-proxy environmental fact remains true.

Therefore the executor can satisfy a current physical-TPM proof while consuming an environmental statement that became stale for the exact property it is supposed to bind.

### 9.9 Threat-model fit

This is not excluded as malicious TPM hardware.

The TPM itself can remain honest and uncompromised throughout.

The attack is an execution-environment / command-transport substitution, exactly the surface that R4R16 section 43 requires the independent review to attack:

```text
same-host hardware TPM passthrough/proxy
TPM command proxy to a guest
host/guest shared PCRs
whether Human no-proxy attestation is the only remaining CPU/locality barrier
```

The review therefore freezes this surface as a blocker rather than leaving it as another observation.

### 9.10 Required successor correction

A successor must either remove the claim that the current executor is cryptographically continuous with the Human-reviewed bare-metal environment, or introduce an independently authenticated non-transferable execution-environment/locality mechanism.

The correction must bind the effect-capable execution context, not merely the TPM identity.

Possible categories require separate governance/review and are not pre-authorized here, for example:

```text
hardware-rooted confidential-computing / CPU attestation with request nonce and host policy
reviewed DRTM/locality profile whose semantics actually bind the execution environment
an out-of-band online gate that freshly observes environment immediately at commitment
another explicit mechanism proving that the exact TPM cannot be mediated to another accepted executor context
```

DMI strings, CPUID hypervisor-bit absence, ACPI shape, sysfs topology, TPM EK/AK identity, PCR equality, or Human V3 freshness alone are not sufficient substitutes.

Until corrected:

```text
X1B-R4R16-IBR-F002 = BLOCKER
```

# OTHER REVIEW DISPOSITIONS

## 10. Embedded root constants

No blocker was found against the frozen root byte constants themselves.

Independent decoding confirmed:

```text
DER length = 607
DER SHA-256 = cfeb02fecd55ad7a73c6e1d11985d4c47dee248ab63dcb66091a2489660443c3
SPKI SHA-256 = ce5183a19d6fe79a6c1b058cfa700379f67d587a8afd0f51621e82d9f00c5a28
serial = 4
subject == issuer = Infineon OPTIGA(TM) ECC Root CA
```

The review does not reopen PR #145 merely by asking for a different trust anchor.

## 11. CA085 / FW7.87 selection

Infineon's current certificate publication page maps:

```text
Infineon Intermediate CA 085
-> SLB 9670 FW7.87
```

and publishes ECC certificate/CRL material plus the corresponding OPTIGA TPM root certificate/CRL.

No blocker is frozen against the mere decision to support only that narrow profile.

## 12. GitHub submitted_at validation time

No circularity blocker remains from the discarded pre-freeze working draft.

Final R4R16 correctly defines:

```text
PKI_VALIDATION_TIME := immutable GitHub V3 review metadata submitted_at
```

only after the review exists.

That rule is non-circular.

The new CRL blocker concerns supersession/currentness, not the source of the validation instant.

## 13. Snapshot / NFIT / ext4 / Git durability

This review found no reason to reopen the previously corrected mechanisms merely because the TPM/PKI layer remains blocked.

Preserve as historical accepted brief-level corrections:

```text
published exact platform snapshot preimage
NFIT format 0x0101
persistence_domain = cpu_cache
deep_flush = 0
internal ext4 journal raw predicate
closed ext4 option table
authenticated procfs/sysfs
initial user namespace / identity maps
non-ID-mapped mount
Human-bound loose-object mtime
bounded object staging
closed object/index/ref/reflog/worktree projections
raw main-ref CAS first durability sequence
post-commit uncertainty classification
```

No PASS for those historical mechanisms implies implementation authority while the current R4R16 blockers remain.

# REQUIRED SUCCESSOR REGRESSIONS

## 14. CRL anti-rollback regressions

A successor must include at least:

```text
older still-nextUpdate-valid CRL after newer CRL exists -> BLOCK
lower CRLNumber than current issuer state -> BLOCK
same issuer/scope with superseded CRL -> BLOCK
missing/invalid CRLNumber when profile requires it -> BLOCK
current revocation entry absent only because older CRL was stapled -> BLOCK
rollback of CA085-status root CRL -> BLOCK
rollback of EK-leaf-status CA085 CRL -> BLOCK
ambiguous issuer/scope/AKI -> BLOCK
current-state evidence unavailable -> BLOCK
```

## 15. TPM transport/locality regressions

A successor must include at least:

```text
same physical EK/AK exposed to VM -> BLOCK unless execution locality independently proven
fresh physical quote relayed through TPM proxy -> BLOCK unless executor locality independently proven
fresh ActivateCredential through proxy -> BLOCK unless executor locality independently proven
same-host QEMU /dev/tpm0 passthrough -> BLOCK unless exact successor locality predicate proves intended environment
proxy that preserves physical PCRs while mediating guest measurement traffic -> BLOCK
V3 bare-metal truth at submitted_at followed by VM/proxy introduction before commitment -> BLOCK
fresh quote + stale no-proxy environmental premise -> BLOCK
DMI/CPUID/ACPI/sysfs-only anti-VM heuristic -> insufficient
```

# IMPLEMENTATION-AUTHORITY DISPOSITION

## 16. Authority result

Because F001 and F002 are independent blockers:

```text
AK-CANON X1B R4R16 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
IMPLEMENTATION AUTHORITY = NOT ESTABLISHED
X1B = OPEN
AGENCY KERNEL V1 AUTHORITY = NOT ESTABLISHED
```

This review does not authorize repair.

It does not authorize implementation.

It does not authorize TPM provisioning, Human V3 evidence, final Human V16 evidence, positive control, canonical effect, recovery or merge.

## 17. Next legal step

The next legal stage, if separately authorized by a fresh Human act, is exactly one successor corrective implementation brief addressing the two frozen R4R16 findings.

A successor must not modify PR #146 or this review in place as a substitute for a fresh frozen artifact.

Preserve:

```text
AI PROPOSES != HUMAN DECIDES
REVIEW FINDING != REPAIR AUTHORITY
R4R16 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R16 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
```
