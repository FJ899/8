# X1B Human Decision Authorship — Independent AK-CANON R4R17 Implementation-Brief Review

Status: `INDEPENDENT REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: `2026-09-03`

## 1. Verdict

`AK-CANON X1B R4R17 IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

R4R17 materially addresses the two exact blockers frozen by PR #147 at brief level:

```text
R4R16 F001 offline CRL rollback / latest issuer state not bound = MATERIALLY ADDRESSED IN DESIGN
R4R16 F002 false TPM->CPU locality inference = MATERIALLY REFRAMED TO EXPLICIT HUMAN AUTHORITY
```

However, independent adversarial review found a new blocker in the Human locality mechanism:

```text
X1B-R4R17-IBR-F001 — ACCEPTED HOST-CONSOLE CHANNEL DOES NOT AUTHENTICATE CHALLENGE ORIGIN TO THE BARE-METAL EXECUTOR = BLOCKER
```

The fresh post-lock nonce proves causal freshness of the reviewed challenge, but the frozen V17 mechanism does not independently authenticate that the exact challenge line visible through `physical-local-console`, `bmc-kvm-host-console`, or `bmc-serial-over-lan-host-console` was emitted by the bare-metal effect-capable process rather than relayed/injected by a guest or mediation layer on the same physical host.

Because the Human V4 locality assertion is the sole positive authority for `execution_locality=physical-host`, a same-host VM/relay can preserve valid physical TPM evidence and present the exact fresh nonce-bearing challenge through an accepted host-console path while the actual effect-capable executor remains a guest/proxied context. The Human can therefore honestly observe the intended chassis and exact challenge while still being shown guest-originated output. Freshness is established; origin is not.

This blocker is independent of the previously rejected claim that TPM proves CPU locality. R4R17 correctly removes that false machine-proof claim, but the replacement Human observation channel remains insufficiently authenticated to the exact executor origin.

A second review requirement also remains unresolved rather than passed: R4R17 itself requires independent proof that the exact Infineon CRL endpoints support its frozen query/header/response profile. The authoritative Infineon publication page identifies the CA085 and root CRL publication links, but the available review environment could not retrieve and inspect the binary CRL HTTP response headers under the exact positive profile. Therefore no PASS claim is made for positive-path implementability.

Either the locality blocker or a nonimplementable CRL positive path independently prevents PASS.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R17 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R17 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#148`

```text
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 44ff8a2c5a59a38e1e7d8cb834675f9f0ee3731d
TREE = a340982b0255494a2d7299169ae469b78b9eab58
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R17.md
BLOB = efa124b1f361788e5ce17faae0dd74f09f162dcc
STATE = OPEN / DRAFT / UNMERGED
```

The exact R4R17 file was freshly reread from reviewed HEAD before this review artifact was written.

## 3. Binding predecessor review

R4R16 independent review:

```text
FJ899/8 PR #147
HEAD = 96e9eebd12a290ff324f892998238421797b4933
TREE = 41607b983169d3678a6f7b795327737b9e42a5fb
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R16_AK_CANON_REVIEW.md
BLOB = dd25369e8d6949861b9ef2d85446afbc2bb5fc95
VERDICT = NOT PASS
```

PR #147 froze exactly:

```text
X1B-R4R16-IBR-F001 — OFFLINE CRL ROLLBACK / LATEST-ISSUER-STATE IS NOT BOUND
X1B-R4R16-IBR-F002 — PHYSICAL TPM QUOTE DOES NOT BIND THE EXECUTING CPU / TPM TRANSPORT LOCALITY
```

## 4. Review method

The review attacked the exact frozen R4R17 brief on its own claimed positive paths. It did not treat fail-closed behavior as sufficient when the brief itself required a realizable positive control.

The pass inspected at least:

```text
exact PR/base/head/tree/blob freeze
CRLNumber/AKI/cRLSign semantics
issuer-publication equality rule
frozen Infineon publication URLs
query-token and strict HTTP response requirements
linearization ordering and 2-second bound
fresh post-lock locality nonce
ExecutorIdentityV17 binding
accepted host-console channels
same-host TPM passthrough/proxy threat model
challenge-origin ambiguity
V4/final review sequencing/freshness
preservation of earlier Name/QName, EK path, PlatformSnapshot, NFIT, ext4 and Git durability properties
```

# PREDECESSOR FINDING DISPOSITIONS

## 5. R4R16 F001 — offline CRL rollback

Disposition:

```text
MATERIALLY ADDRESSED AT BRIEF LEVEL, SUBJECT TO POSITIVE-PATH IMPLEMENTABILITY
```

R4R17 no longer accepts a Human-stapled CRL merely because it is signed and still within `nextUpdate`.

It adds:

```text
CRLNumber
AuthorityKeyIdentifier
issuer-designated live publication URLs
exact live byte equality to Human-reviewed CRLs
rollback/newer-publication rejection
named PRE_REF_RENAME_CRL_LINEARIZATION_POINT
no external/blocking authority reads after linearization
2-second linearization-to-ref-rename bound
```

These rules directly address the PR #147 rollback class at the specification level.

However, R4R17 explicitly makes positive-path implementability review-gating: the exact Infineon endpoints must accept the frozen query/header profile and return responses satisfying its strict Date/Age/Via/Warning/body rules. The current review environment could confirm the authoritative publication identifiers but could not obtain inspectable live binary response headers under that exact profile. This is recorded as unresolved, not silently treated as PASS.

## 6. R4R16 F002 — false TPM->CPU locality inference

Disposition:

```text
FALSE TPM->CPU CRYPTOGRAPHIC CLAIM = REMOVED
REPLACEMENT HUMAN LOCALITY AUTHORITY = NOT SUFFICIENTLY ORIGIN-AUTHENTICATED
```

R4R17 correctly states:

```text
TPM EVIDENCE DOES NOT BY ITSELF PROVE THAT THE EFFECT-CAPABLE CPU CONTEXT IS BARE METAL.
```

It moves bare-metal/no-proxy locality to a fresh Human V4 authority act tied to a post-lock random nonce.

That is a material conceptual correction. The residual blocker is in the exact channel/authentication mechanics of that Human act.

# FINDING 1

## 7. X1B-R4R17-IBR-F001 — accepted host-console channel does not authenticate challenge origin

Severity: `BLOCKER`.

### 7.1 Frozen R4R17 mechanism

R4R17 requires the effect-capable executor to display:

```text
X1B-V17-LOCALITY request=<request_digest> executor=<executor_identity_sha256> nonce=<64hex> challenge=<locality_challenge_sha256>
```

through one of:

```text
physical-local-console
bmc-kvm-host-console
bmc-serial-over-lan-host-console
```

The Human then attests that the visible execution is on the physical host, with no VM mediation, TPM passthrough or proxy.

### 7.2 Fresh nonce proves sequencing, not origin

The fresh 256-bit nonce generated after the physical ref lock is strong evidence that a V4 body containing that exact nonce was created after challenge generation.

It does not establish which execution context emitted the visible line.

A same-host guest can receive or generate its own request-bound challenge state and route console output through a host-visible physical/BMC console path. The channel identifies the physical console destination, not necessarily the process/kernel execution origin of each displayed byte.

The exact distinction is:

```text
FRESH CHALLENGE OBSERVED ON HOST CONSOLE
!=
CHALLENGE ORIGIN AUTHENTICATED AS BARE-METAL EFFECT-CAPABLE EXECUTOR
```

### 7.3 Same-host relay / passthrough counterexample class

Consider a physical host H with the exact expected physical TPM and storage environment. A VM G runs the effect-capable ScriptOps executor. G can access the same physical TPM through passthrough/proxy, which is the threat class already frozen by predecessor reviews.

Now additionally arrange a console relay such that output produced by G appears on an accepted physical/BMC console of H. This can be done by ordinary host/guest console plumbing; the console channel itself is not an authenticated statement that the bytes were emitted by a host-native process.

Then:

```text
physical chassis observed = correct
BMC/host console authenticated = correct
fresh nonce/challenge visible = correct
physical TPM EK/AK quote/ActivateCredential = correct
challenge digest fields = internally consistent
actual effect-capable executor context = guest / mediated
```

An honest Human can therefore see the right chassis, the right fresh challenge and valid TPM/platform evidence while still being shown guest-originated output.

R4R17 asks the Human to independently determine `host OS rather than guest console` and `no hypervisor/VM layer mediates this effect-capable executor`, but it does not freeze a deterministic origin-authentication mechanism by which the Human distinguishes host-native challenge output from guest/relay output when both arrive through the accepted physical console.

### 7.4 ExecutorIdentityV17 does not close this gap

`ExecutorIdentityV17` binds rich current-task `/proc`, namespace, executable, cgroup, boot-id, credential, platform and TPM values.

Those values identify the process relative to the kernel view available to that process; they do not by themselves provide a hardware-rooted proof that the process is executing in the host kernel rather than a guest whose environment is arranged to satisfy or relay the observed evidence.

The Human sees only the digest of `ExecutorIdentityV17` in the challenge line. Without an independently authenticated mapping from that digest/process identity to the host-native execution context, the digest does not authenticate console-output origin.

### 7.5 Why the frozen Human-authority formulation is still insufficient

It is valid to make locality an explicit trusted-Human environmental authority act rather than a TPM theorem.

But for the Human act to close the predecessor threat class, the Human must be able to distinguish the exact effect-capable executor from a guest/proxy context using the frozen allowed evidence/channel contract.

R4R17 presently permits a channel where a guest can cause the exact challenge bytes to appear while relying on the Human to infer origin from environmental inspection that is described only as possible supporting observation (`may include BMC inventory, physical labels, firmware inventory and host process/service inspection`).

The authority-critical process-origin test is therefore not fully frozen; it can depend on runtime Human improvisation and environment-specific judgment.

That violates the brief's own higher-level requirement that no core security/authority choice be left implicit.

### 7.6 Required disposition

```text
X1B-R4R17-IBR-F001 = BLOCKER
R4R17 REVIEW = NOT PASS
```

No repair design is authorized by this review.

# ADDITIONAL REVIEW NOTE

## 8. CRL positive-path implementability remains unresolved

R4R17 explicitly states that if the exact Infineon endpoints do not support its frozen request/response profile, the positive V17 path is `BLOCKED`, and independent review must test positive-path implementability.

The public Infineon material identifies the exact CA085 and root CRL publication locations. The available review environment could not retrieve and inspect the binary CRL response headers using the exact frozen query-token/header profile. Therefore this review does not claim:

```text
INFINEON_LIVE_CRL_CURRENTNESS_V1 POSITIVE PATH = VERIFIED IMPLEMENTABLE
```

This is not promoted to a second deterministic blocker because endpoint incompatibility was not established; it remains unresolved evidence required before any future PASS.

# PRESERVED CORRECTIONS

## 9. Earlier corrections not reopened

Nothing in this review reopens, on current evidence:

```text
AK ordinary Name / Qualified Name separation
pinned Infineon root / CA085 path mechanism
published PlatformSnapshot preimage requirement
NFIT persistence-domain/deep-flush profile
procfs/userns/idmap authority profiles
internal ext4 journal / closed ext4 runtime profile
Human-bound loose-object mtime
closed object/index/ref/reflog/worktree durability sequence
fail-closed success/uncertainty distinction
```

# STOP

## 10. Explicit non-authority

This review does not authorize:

```text
R4R18 repair
ScriptOps implementation
certifi vendoring
TPM provisioning or mutation
Human V4 evidence creation
Human final decision creation
positive control
canonical effect
recovery
merge
X1B closure
V1
release
deployment
tag
```

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R17 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R17 REVIEW NOT PASS != X1B CLOSED
AI PROPOSES != HUMAN DECIDES
```
