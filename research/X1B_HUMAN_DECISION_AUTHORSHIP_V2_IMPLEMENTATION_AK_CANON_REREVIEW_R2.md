# X1B Human Decision Authorship V2 — Independent AK-CANON Implementation Re-review R2

Status: `INDEPENDENT IMPLEMENTATION RE-REVIEW / NOT REPAIR OR EXECUTION AUTHORITY`

Date: `2026-09-03`

## 1. Verdict

```text
AK-CANON X1B HUMAN DECISION AUTHORSHIP V2 IMPLEMENTATION RE-REVIEW R2 = NOT PASS
```

First credible blocker in this R2 review:

```text
X1B-V2-IMPL-R2-F001 — F005 SUPPORTED-HOST LIVE GITHUB AUTHORITY POSITIVE-PATH EVIDENCE IS ABSENT = BLOCKER
```

The prior implementation blocker `X1B-V2-IMPL-F001` concerning symbolic `refs/heads/main` dereference is materially closed by the bounded repair on the reviewed candidate. The overall candidate still cannot receive implementation-review PASS because the separately frozen F005 brief makes a real supported-host public-GitHub positive path a mandatory precondition to implementation-review PASS, and that evidence is not present on this exact candidate.

Per the review rule:

```text
FIRST CREDIBLE COUNTEREXAMPLE / MANDATORY-PROOF FAILURE = STOP
```

No further blocker discovery is claimed after R2-F001.

## 2. Exact review target

Repository:

```text
FJ899/scriptops
```

Pull request:

```text
PR #35
```

Exact implementation baseline:

```text
BASE = 2f22843ac570498b506101addeba5453ab777f08
BASE TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

Exact repaired implementation candidate:

```text
HEAD = b281383be083be24d7e4b9f6c9411d3cc1c317f2
TREE = aa2b974efa01f55e0f909a0de60fcbde2b7e6a3f
COMMITS AHEAD = 1
COMMITS BEHIND = 0
CHANGED FILES = 13
```

The changed-file set remains exactly within the frozen implementation surface:

```text
.github/workflows/x1b-human-decision.yml
HANDOFF.md
PROJECT_STATE.md
README.md
SOURCE_MANIFEST.md
legacy/scriptops-v2-single.py
phase6/scriptops-v2-hardening.py
phase6/x1b_human_decision.py
scripts/restore_v2.py
scripts/verify_repository.py
sources/prototype/RESTORE.md
tests/test_phase6_scriptops_smoke.py
tests/test_x1b_human_decision.py
```

Relevant exact repaired blobs observed on the candidate include:

```text
phase6/x1b_human_decision.py       87f91babb6199d323b57f26c75d87495347c3647
tests/test_x1b_human_decision.py   d710f4ebfa5d21fd03d7e39c3784196d5a8842fd
scripts/verify_repository.py        4f0b58721a89dbfe7dc6cfac75ac23f051323afe
.github/workflows/x1b-human-decision.yml a39321840f1c94a90776a9f149bcaddf44ac11f8
```

PR #35 remains draft/open/unmerged.

## 3. Governing specification composite

Non-network V2 semantics remain governed by:

```text
FJ899/8 PR #155
HEAD = 3509c6e0922b28eb2d141fb3599ee21a1c7ee102
TREE = a499cbadbf85314e9e7ab473c97cd18d9afa8dd5
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_FINAL_BOUNDED_IMPLEMENTATION_BRIEF_REOPEN_F001_F004.md
BLOB = e796e00c778c4b149dbc79abf05795a61450360d
```

F005 network/TLS semantics are superseded only by:

```text
FJ899/8 PR #158
HEAD = e188a452b0960d846479a975fc2d9f2c76aac50d
TREE = 83263b8c297eca72cca8bb35fe6c3c9338dc700b
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_FINAL2_F005_TLS_TRUST_REPAIR_BRIEF.md
BLOB = ff06a772275bc861de9211375e8bda08d67ead3e
```

Independent specification review:

```text
FJ899/8 PR #159
HEAD = 99101fe17925b8155bfe46c0b7d47a07aab5635b
TREE = 108c8ffee6590d495bf69addd80a239e17a8e14a
BLOB = d06afae000adb91673fda29b2aae12aee8363007
VERDICT = PASS
```

PR #159 explicitly preserved one implementation-review requirement because its own review host could not perform outbound DNS:

```text
the exact future supported-host live GitHub GET remains mandatory implementation-review evidence
```

The composite brief therefore cannot be treated as permitting a deterministic-test-only implementation PASS.

## 4. Prior implementation review and bounded repair authority

Initial implementation review:

```text
FJ899/8 PR #160
HEAD = 0e57cc2aeb35f561bdf83094bfd88a0eb1b7625a
TREE = 6b3b8871527ed03dc9dfa572ce50d37b67ad9990
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_V2_IMPLEMENTATION_AK_CANON_REVIEW.md
BLOB = 590f1be0c83c3044114fc857fb81227297a048d0
VERDICT = NOT PASS
```

Its first credible blocker was:

```text
X1B-V2-IMPL-F001 — MAIN-REF CAS DEREFERENCES A CONCURRENT SYMBOLIC refs/heads/main AND CAN MUTATE AN UNBOUND TARGET REF
```

Human bounded repair authority:

```text
FJ899/8 PR #161
HEAD = df0a985e1129a3d638e1ee2cf69846ac43c2eefc
HUMAN RESPONSE = accept
AUTHORIZED REPAIR = X1B-V2-IMPL-F001 ONLY
```

That authority did not authorize a live decision-evidence PR, Human V2 approval, positive control, canonical screenplay effect, merge, X1B closure, or repair/proof work outside F001.

## 5. Final CI on the exact repaired HEAD

The exact repaired HEAD `b281383be083be24d7e4b9f6c9411d3cc1c317f2` has green repository CI:

```text
x1b-human-decision       run 33796528671 = SUCCESS
Phase 6 ScriptOps smoke run 33796528663 = SUCCESS
Verify repository state run 33796528470 = SUCCESS
```

These results establish that the deterministic regression suites and repository verifier pass on the exact review target.

They do not, by themselves, establish the mandatory live F005 positive path described below.

```text
GREEN CI != REQUIRED LIVE AUTHORITY POSITIVE-PATH EVIDENCE
```

## 6. Disposition of prior F001

### 6.1 Reviewed repair

The repaired `AnchoredGitV2` now distinguishes resolved ref truth from direct named-ref truth.

The candidate:

- rejects `refs/heads/main` when it is itself a symbolic ref;
- verifies direct `refs/heads/main` through a dedicated direct-ref check;
- requires direct main at local preflight;
- rechecks direct main after Human authority read and before effect;
- performs canonicalization using:

```text
git update-ref --no-deref refs/heads/main NEW OLD
```

- requires direct main again during post-effect verification.

### 6.2 Exact regression coverage

The candidate includes deterministic regressions that:

1. reproduce `main -> shadow`, with `shadow = B0`, while ordinary resolved `main` still appears to be `B0`, and require rejection before effect;
2. model the narrow race in which symbolic substitution occurs after the direct-ref check and verify that `--no-deref` leaves `shadow` at `B0` rather than mutating the unbound target.

Both pass in the exact final X1B CI.

### 6.3 R2 disposition

```text
X1B-V2-IMPL-F001 = MATERIALLY CLOSED ON THIS CANDIDATE
```

This R2 review does not reopen F001.

## 7. F005 normative implementation-PASS requirement

The F005 brief does not merely require code that appears capable of a verified TLS read. Section 18 freezes a positive-path proof prerequisite:

Before any implementation candidate can PASS independent implementation review, evidence must demonstrate on the exact supported execution host/runtime:

```text
fresh child spawned with exact isolated environment
SSL_CERT_FILE absent in child
SSL_CERT_DIR absent in child
OPENSSL_CONF absent in child
isolated child default CA store x509_ca > 0
check_hostname = true
verify_mode = CERT_REQUIRED
TLS minimum >= TLSv1_2
successful direct HTTPS GET to api.github.com public pull-request-review endpoint
no Authorization header
same real trusted Human account user.id = 226907434 visible in a qualifying positive-control review response
```

The brief explicitly classifies this as implementation-review evidence rather than a screenplay canonical effect.

PR #159 did not discharge this requirement. It reported that outbound DNS was unavailable on its review host and carried the supported-host live GET forward as mandatory implementation-review evidence.

## 8. What the exact implementation proves statically/deterministically

The code contains the intended isolated-reader construction:

```text
subprocess child with -I
fresh environment = {X1B_NETWORK_CHILD: 1}
stdlib ssl + http.client
fixed api.github.com:443
create_default_context(SERVER_AUTH)
check_hostname true
CERT_REQUIRED
TLS minimum >= 1.2
nonempty CA-store check
no Authorization header
```

The deterministic unit suite also confirms that an attacker-populated parent environment does not get copied into `network_child_env()`.

This is useful and consistent with the F005 design.

It is not the same fact as successful supported-host execution of the actual public GitHub authority read.

## 9. Missing evidence on the exact candidate

The exact `.github/workflows/x1b-human-decision.yml` runs only:

```text
python unittest deterministic X1B + Phase6 tests
python scripts/verify_repository.py
python scripts/restore_v2.py --check-only
```

It contains no supported-host live GitHub authority-reader invocation and no assertion over a real public review response from the trusted Human account.

The exact `tests/test_x1b_human_decision.py` contains a deterministic `test_network_child_env_is_fresh`, but no live equivalent of the frozen F005 `X1B-TLS11` requirement and no evidence that the same real `user.id = 226907434` was obtained through the implemented child on the supported host/runtime.

No separate implementation-evidence artifact bound to `b281383...` was found that supplies the omitted live proof.

Therefore the following mandatory chain remains unproven:

```text
exact implemented isolated child
+
exact supported runtime/OS CA store
+
real DNS/TCP/TLS to api.github.com
+
real public reviews endpoint
+
real trusted Human numeric user ID observation
->
realizable positive Human-authority read through the exact implementation
```

## 10. Finding R2-F001

```text
X1B-V2-IMPL-R2-F001 — F005 SUPPORTED-HOST LIVE GITHUB AUTHORITY POSITIVE-PATH EVIDENCE IS ABSENT = BLOCKER
```

### 10.1 Why this blocks PASS

This is not optional hardening and is not a C-class physical-platform expansion.

It is an explicit implementation-review PASS prerequisite in the Human-authorized F005 brief and was explicitly carried forward by the independent specification PASS review.

An implementation review cannot convert:

```text
code looks implementable
```

into:

```text
required supported-host positive path has been evidenced
```

when the frozen brief distinguishes those facts.

### 10.2 What is not claimed

This review does not establish that the TLS/HTTP implementation is broken.

It establishes only the narrower and sufficient blocker:

```text
MANDATORY IMPLEMENTATION POSITIVE-PATH EVIDENCE = NOT YET PRESENT
```

### 10.3 Minimum evidence capable of closing the finding

A later separately Human-authorized bounded proof could, without invoking ScriptOps canonical approval/effect, establish exactly the missing F005 facts by using the exact candidate implementation on a supported host/runtime and a real public V2 review response from trusted numeric user ID `226907434`.

Such a proof would need to freeze at least:

```text
exact candidate HEAD/TREE
exact Python/OpenSSL/support-host observation
fresh child environment keys
CA-store stats
TLS verify_mode/check_hostname/minimum
actual successful public reviews GET through the exact child
absence of Authorization
raw/normalized qualifying review evidence showing user.id = 226907434
no ScriptOps CAS/worktree/canonical effect
```

Whether to create the inert evidence PR/review needed for that proof is a Human authority question, not something this review authorizes.

## 11. STOP / non-authority

Because R2-F001 is the first credible mandatory-proof failure in this R2 review:

```text
STOP FURTHER BLOCKER DISCOVERY
```

This review authorizes no:

- source repair or workflow mutation;
- live X1B decision-evidence PR;
- Human V2 approval review;
- positive control execution;
- ScriptOps `approve` invocation;
- canonical screenplay effect;
- merge of ScriptOps PR #35;
- merge of evidence/review PRs;
- X1B closure;
- V1 authority;
- release, deployment, or tag.

Preserve:

```text
REVIEW FINDING != REPAIR OR PROOF AUTHORITY
GREEN CI != REQUIRED LIVE POSITIVE-PATH PROOF
FIRST CREDIBLE COUNTEREXAMPLE / MANDATORY-PROOF FAILURE = STOP
AI PROPOSES != HUMAN DECIDES
```

## 12. Next legal gate

The next legal stage is not the preregistered corrective-verification packet because implementation-review PASS has not yet been earned.

A Human may separately authorize exactly one bounded F005 implementation-positive-path proof that:

- uses the exact repaired candidate;
- proves only the missing supported-host read path;
- creates no ScriptOps canonical effect;
- does not merge PR #35;
- does not claim X1B closure.

Only after that evidence is frozen may the exact implementation candidate be independently re-reviewed again.
