# X1B Human Decision Authorship — Independent AK-CANON Review of FINAL BOUNDED REOPEN F001-F004

Status: `INDEPENDENT AK-CANON REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: `2026-09-03`

## 1. Verdict

```text
AK-CANON X1B FINAL BOUNDED REOPEN F001-F004 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

The bounded successor in `FJ899/8 PR #155` materially closes the four blockers accepted from PR #153 at specification level:

```text
F001 mutable GitHub login -> durable numeric GitHub user ID
F002 mutable multi-endpoint PR snapshot -> single current review response + immutable reviewed commit H
F003 post-hoc stale-base detection -> prospective commit + pre-canonical update-ref CAS
F004 inherited Git repository-selection environment -> AnchoredGitV2 scrub + explicit git-dir/work-tree
```

No TPM, PMEM, NFIT, EK/CRL, BMC, bare-metal, hostile-hypervisor or power-loss requirement is reintroduced.

However, the review found one first credible counterexample inside the already-frozen X1B threat model and STOPped further blocker discovery:

```text
X1B-FINAL2-IBR-F005 — CALLER-CONTROLLED TLS CA ENVIRONMENT CAN REPLACE THE DECLARED OS TRUST STORE = BLOCKER
```

The V2 threat model explicitly permits arbitrary normal process environment variables. `GitHubDecisionReaderV2` rejects GitHub credential and proxy environment variables, but it does not reject or otherwise neutralize OpenSSL/Python default-CA environment overrides. Python's standard TLS stack documents that its default verify paths expose OpenSSL environment keys for the CA file and CA directory, and PEP 476 explicitly records that `SSL_CERT_FILE` and `SSL_CERT_DIR` can point Python at a different certificate database.

Therefore the frozen statement that the reader uses the default verified **OS** CA/TLS trust boundary is not established under the stated caller-environment model. The caller can replace the CA trust input without compromising the OS CA store itself.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
NOT PASS != SCOPE FAILURE
NOT PASS != R4R17 REOPEN
FIRST CREDIBLE COUNTEREXAMPLE = STOP FURTHER BLOCKER SEARCH IN THIS RUN
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#155`

```text
TITLE = X1B: bounded final brief reopen for F001-F004
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 3509c6e0922b28eb2d141fb3599ee21a1c7ee102
TREE = a499cbadbf85314e9e7ab473c97cd18d9afa8dd5
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_FINAL_BOUNDED_IMPLEMENTATION_BRIEF_REOPEN_F001_F004.md
BLOB = e796e00c778c4b149dbc79abf05795a61450360d
STATE = OPEN / DRAFT / UNMERGED
COMMITS = 1
CHANGED FILES = 1
```

The exact PR patch was reread during this independent review.

Current evidence/governance baseline remained:

```text
FJ899/8 main
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

Current ScriptOps baseline remained:

```text
FJ899/scriptops main
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

No reviewed-baseline drift was observed.

## 3. Governing authority and scope

This review is authorized by the Human `accept` following freeze of PR #155.

It remains bound by:

```text
FJ899/8 PR #150 = Human-accepted convergence/scope review
FJ899/8 PR #151 = Human acceptance of convergence disposition
FJ899/8 PR #153 = independent NOT PASS review of prior final bounded brief
FJ899/8 PR #154 = Human acceptance of exactly F001-F004 and one bounded reopen
```

The scope firewall remains:

```text
BLOCK if a defect can create false Human origin,
stale/incorrect Human currentness,
admission bypass,
logical-effect substitution,
legacy accepted-state bypass,
or false post-effect Human attribution
under the stated V2 threat model.
```

Do not block merely for attacks on unclaimed:

```text
TPM/EK/AK
vendor CRLs
PMEM/NFIT
bare-metal locality
BMC console process origin
universal power-loss durability
hostile kernel/filesystem/Git binary
compromised Human account
```

The blocker in this review is not a C-class platform claim. It concerns the selected GitHub HTTPS Human-authority reader itself.

## 4. Review method

The review checked:

```text
exact PR #155 identity and single-file freeze
F001 durable Human account identity
F002 Human-currentness and immutable content binding
F003 prospective effect + CAS semantics
F004 anchored Git repository environment
GitHub public review response structure
current real Human review identity evidence
GitHub review-list ordering semantics
Git update-ref compare-and-swap semantics
Python standard TLS default trust behavior
caller-controlled environment interaction with TLS CA selection
```

The review used the first-credible-counterexample STOP discipline. After F005 was established as blocking, no claim is made that an unlimited search for additional blocker classes was completed.

## 5. F001 disposition — materially closed at brief level

PR #155 replaces mutable login authority with:

```text
TRUSTED_HUMAN_GITHUB_USER_ID = 226907434
```

A fresh raw review read from previously used real Human evidence in `FJ899/scriptops PR #33` still reports:

```text
user.login = litrgratis-pixel
user.id = 226907434
user.node_id = U_kgDODYZVKg
state = APPROVED
```

GitHub's current user API documentation describes numeric user `ID` as durable and explicitly contrasts it with `login`, which can change over time.

The successor propagates the numeric ID through:

```text
request Human-authority validation
review qualification
admission
V2 decision record
positive/negative tests
```

A different account that later acquires login `litrgratis-pixel` cannot satisfy `user.id == 226907434`.

Disposition:

```text
X1B-FINAL-IBR-F001 = MATERIALLY CLOSED AT BRIEF LEVEL
```

## 6. F002 disposition — materially closed at brief level

The prior defect was the false claim of a current snapshot assembled from multiple mutable REST resources.

V2 removes that claim.

It freezes:

```text
one complete current review-list response = Human-currentness linearization
review.commit_id H = immutable Human-reviewed content generation
request digest D = exact Human marker/content binding
immutable H file reads = exact request/effect reconstruction
```

The current GitHub REST documentation states that the list-reviews endpoint returns the review list in chronological order. The successor conservatively caps the accepted response to fewer than 100 reviews and denies pagination ambiguity.

Mutable PR-head movement is no longer imported as Human authority. H2 cannot inherit H1 approval. A later Human authority-relevant review can supersede/revoke under the V2 rule.

The immutable file reads after review selection do not need to be in the same transaction as the mutable review-list response because their generation is the exact immutable `review.commit_id H` returned by the trusted GitHub review object.

Disposition:

```text
X1B-FINAL-IBR-F002 = MATERIALLY CLOSED AT BRIEF LEVEL
```

This disposition is limited to the current frozen V2 semantics; it is not a statement that GitHub REST generally provides transactional snapshots.

## 7. F003 disposition — materially closed at brief level

The successor no longer lets ordinary `git commit` advance main before stale-base detection.

It freezes:

```text
common-dir X1B lock
prospective blobs/private index/tree T
prospective commit C with parent B0
full pre-CAS verification
canonical linearization only through:
  git update-ref refs/heads/main C B0
```

Current Git documentation states that three-argument `git update-ref <ref> <new-oid> <old-oid>` stores the new object only after verifying that the current ref value matches the expected old object ID.

Therefore an external/concurrent B0->X change before the CAS prevents this run's stale C from becoming canonical.

Disposition:

```text
X1B-FINAL-IBR-F003 = MATERIALLY CLOSED AT BRIEF LEVEL
```

## 8. F004 disposition — materially closed for Git repository-selection environment

`AnchoredGitV2` requires:

```text
SOURCE_ROOT from resolved module source location
remove all inherited environment names beginning GIT_
clean discovery from SOURCE_ROOT
freeze git_dir/common_dir
explicit --git-dir and --work-tree on authority-critical Git commands
internal-only private GIT_INDEX_FILE
GIT_NO_REPLACE_OBJECTS=1
system/global Git config suppression
```

This directly closes the PR #153 counterexample based on inherited:

```text
GIT_DIR
GIT_WORK_TREE
GIT_COMMON_DIR
GIT_INDEX_FILE
GIT_OBJECT_DIRECTORY
GIT_ALTERNATE_OBJECT_DIRECTORIES
GIT_NAMESPACE
GIT_CONFIG_*
```

Disposition:

```text
X1B-FINAL-IBR-F004 = MATERIALLY CLOSED AT BRIEF LEVEL
```

This does not expand X1B into a malicious-Git-binary or hostile-filesystem theorem.

# FIRST CREDIBLE BLOCKER

## 9. X1B-FINAL2-IBR-F005 — caller-controlled TLS CA environment can replace the declared OS trust store

Severity: `BLOCKER`.

Classification:

```text
CORE X1B / TRUSTED HUMAN ORIGIN / SELECTED GITHUB HTTPS MECHANISM
```

### 9.1 Frozen threat model

PR #155 explicitly permits the evaluated AI/process to:

```text
set arbitrary normal process environment variables
```

The same brief says trusted infrastructure includes:

```text
operating-system CA/TLS implementation
GitHub HTTPS service
```

and `GitHubDecisionReaderV2` declares:

```text
https://api.github.com:443
with default verified OS TLS/hostname verification
```

Thus the selected Human-origin mechanism depends on the reader authenticating GitHub using the declared OS trust roots rather than caller-chosen trust roots.

### 9.2 Frozen environment checks are incomplete for that claim

The reader rejects non-empty:

```text
GITHUB_TOKEN
GH_TOKEN
GITHUB_ENTERPRISE_TOKEN
GH_ENTERPRISE_TOKEN
HTTP_PROXY
HTTPS_PROXY
ALL_PROXY
http_proxy
https_proxy
all_proxy
```

It does not freeze/reject or otherwise neutralize:

```text
SSL_CERT_FILE
SSL_CERT_DIR
```

### 9.3 Python/OpenSSL default CA lookup is environment-sensitive

Python's standard `ssl.get_default_verify_paths()` documents both:

```text
openssl_cafile_env
openssl_capath_env
```

as environment keys used by OpenSSL default certificate lookup.

On the ordinary Linux/Python environment used for this review, those keys resolve to:

```text
openssl_cafile_env = SSL_CERT_FILE
openssl_capath_env = SSL_CERT_DIR
```

Python PEP 476 explicitly records:

```text
OpenSSL has environment variables SSL_CERT_DIR and SSL_CERT_FILE
which can point Python at a different certificate database.
```

`ssl.create_default_context()` / default-certificate loading therefore does not by itself prove that the CA database is the immutable OS trust database when these caller variables are permitted.

### 9.4 Why this falsifies a claim actually made by V2

This is not an attack requiring modification of the OS CA store.

The V2 mechanism states both:

```text
caller may set arbitrary normal process environment
```

and:

```text
Human authority is reconstructed over HTTPS authenticated by OS CA/TLS trust
```

but leaves a documented caller-controlled input capable of selecting a different CA database.

That changes an authority input at exactly the layer that authenticates:

```text
review.user.id
review state/body/commit_id
immutable H content responses
```

If the TLS peer is accepted under a caller-selected CA rather than the declared OS trust boundary, forged GitHub API responses can satisfy all later JSON-level Human predicates without the trusted GitHub service or Human account having produced them.

The selected HTTPS mechanism therefore has not yet established trusted Human origin under its own environment model.

### 9.5 Scope test

F005 attacks:

```text
trusted GitHub origin
trusted Human review origin
fail-closed authority admission
separation of caller-controlled process state from Human evidence
```

These are explicitly blocking properties under the PR #150/#151 convergence firewall and PR #155 section-37 scope firewall.

It does not assert:

```text
compromised OS CA store
malicious kernel
malicious Python/OpenSSL implementation
TPM/PMEM/bare-metal properties
```

The issue is that the frozen reader allows the caller to replace which CA database the otherwise-trusted TLS implementation uses.

### 9.6 Required disposition

```text
X1B-FINAL2-IBR-F005 = BLOCKER
```

A successor may close this narrowly by freezing a caller-independent CA/trust configuration for `GitHubDecisionReader`, or by deterministically rejecting/neutralizing the documented CA-selection environment inputs while preserving the Human-accepted OS-CA/TLS scope.

This review does not select or authorize the repair mechanism.

## 10. Positive-path and non-blocking observations

### 10.1 Durable Human account ID remains evidenced

The selected account ID `226907434` is present in existing real Human review evidence and GitHub documents numeric user IDs as durable. No F001 regression was found before STOP.

### 10.2 Review endpoint semantics remain usable

GitHub currently documents public pull-request review listing and chronological review-list return order. No F002 positive-path blocker was found before STOP.

### 10.3 Git CAS primitive is realizable

Git currently documents the exact three-argument `update-ref` old-value verification required by V2. No F003 positive-path blocker was found before STOP.

### 10.4 Current ScriptOps baseline note

The exact current ScriptOps Git tree was inspected as part of positive-path checking. Any implementation must still prove its runtime handling of a first/absent decision-log prestate in the later implementation review and corrective-verification packet. This review does not promote that implementation detail to an additional blocker after the first-credible-counterexample STOP.

## 11. Scope/convergence assessment

The correct interpretation is:

```text
CONVERGENCE STRATEGY = STILL VALID
F001-F004 REPAIR DIRECTION = MATERIALLY VALID
PR #155 = NOT PASS DUE ONE NEW CORE READER-TRUST BLOCKER
R4R17 PHYSICAL-PLATFORM LINEAGE = STILL NOT REOPENED
```

F005 is narrow. It does not require a new security domain. It is a caller-environment closure at the existing GitHub/TLS boundary already selected by the final bounded mechanism.

## 12. PASS-criteria disposition

Against PR #155 section-39 criteria:

```text
1 stable numeric Human account identity
  = PASS at brief level

2 realizable V2 review currentness
  = PASS at brief level on reviewed evidence

3 immutable H prevents PR-head substitution
  = PASS at brief level

4 deterministic activity/supersession/replay
  = PASS at brief level on reviewed evidence

5 AnchoredGitV2 prevents caller Git repository-env substitution
  = PASS for the specified Git-environment class

6 lock + prospective commit + update-ref CAS prevents stale-base canonical effect
  = PASS at brief level

7 no successful HumanDecision before canonical/post-effect proof
  = NO REGRESSION FOUND BEFORE STOP

8 current/legacy bypass closure remains required
  = NO REGRESSION FOUND BEFORE STOP

9 negative/positive tests executable
  = NOT PASS because the Human-origin network reader still accepts caller-controlled CA trust selection

10 no C-class platform/hardware requirement reintroduced
  = PASS
```

Overall:

```text
AK-CANON X1B FINAL BOUNDED REOPEN F001-F004 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

## 13. Explicit non-authority / STOP

This review authorizes no:

```text
successor brief
F005 repair design
ScriptOps source mutation
phase6/x1b_human_decision.py creation
CODEOWNERS/ruleset mutation
live decision-evidence PR
Human live V2 approval
positive control
canonical screenplay effect
merge
X1B closure
Agency Kernel V1
release
deployment
tag
```

After durable freeze of this exact review:

```text
STOP
NEXT LEGAL STAGE = HUMAN DISPOSITION ON X1B-FINAL2-IBR-F005
```

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
ONE CORE BLOCKER != SCOPE EXPANSION
FIRST CREDIBLE COUNTEREXAMPLE = STOP
NOT PASS != R4R17 REOPEN
AI PROPOSES != HUMAN DECIDES
```
