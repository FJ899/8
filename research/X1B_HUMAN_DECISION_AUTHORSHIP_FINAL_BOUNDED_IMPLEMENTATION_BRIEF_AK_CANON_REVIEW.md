# X1B Human Decision Authorship — Independent AK-CANON Review of FINAL BOUNDED IMPLEMENTATION BRIEF

Status: `INDEPENDENT AK-CANON REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: `2026-09-03`

## 1. Verdict

```text
AK-CANON X1B FINAL BOUNDED IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

The final bounded brief successfully removes the R4R13-R4R17 physical-platform scope expansion and returns X1B to the Human-decision-authorship property accepted by the original preregistration, real-boundary finding, corrective design and Human-accepted convergence firewall.

The selected GitHub-review mechanism is materially narrower than R4R17. Its public credential-free read dependency is realizable at specification level: `FJ899/8` is public, GitHub documents public pull-request review reads as usable without authentication, REST API version `2026-03-10` is currently supported, and the trusted Human account currently has repository read access sufficient to submit a review.

However, adversarial review found four blockers that remain inside the accepted X1B scope. They concern trusted Human origin, current evidence, exact local logical-effect binding and executor no-substitution. None depends on TPM, PMEM, NFIT, EK/CRL, bare-metal locality, BMC provenance or power-loss durability.

```text
X1B-FINAL-IBR-F001 — MUTABLE GITHUB LOGIN IS THE SOLE HUMAN AUTHORITY IDENTITY = BLOCKER
X1B-FINAL-IBR-F002 — MULTI-REQUEST GITHUB AUTHORITY READ HAS NO CONSISTENT CURRENT-STATE LINEARIZATION = BLOCKER
X1B-FINAL-IBR-F003 — LOCAL EFFECT LACKS MUTUAL EXCLUSION / PRE-COMMIT BASE CAS = BLOCKER
X1B-FINAL-IBR-F004 — CALLER-CONTROLLED GIT REPOSITORY ENVIRONMENT CAN REDIRECT AUTHORITY-CRITICAL GIT OPERATIONS = BLOCKER
```

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
FINAL BRIEF REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
FINAL BRIEF REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
FINDING VALIDITY != SCOPE EXPANSION
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#152`

```text
TITLE = X1B: freeze final bounded implementation brief
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
HEAD = 3e5cfd88340387a3fe893a2ada114709dc43bc81
TREE = ec6db48f44c67b8a4bfe373758464bc5cbdc7860
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_FINAL_BOUNDED_IMPLEMENTATION_BRIEF.md
BLOB = 17c71355902472155710a063f1661018dcfd5a57
STATE = OPEN / DRAFT / UNMERGED
COMMITS = 1
CHANGED FILES = 1
```

The exact file was reread from reviewed HEAD during this review.

Current `FJ899/8 main` remained:

```text
HEAD = 1e4114e3f7ab6383af2549383b25329bed21eef9
TREE = df807db7003dfd201e9be4d5927472e515a2e737
```

Current `FJ899/scriptops main` remained:

```text
HEAD = 2f22843ac570498b506101addeba5453ab777f08
TREE = 4215d9306392070e64c6fd74a6cfb813ca9d0601
```

No reviewed baseline drift was observed.

## 3. Governing scope

This review is bound by the Human-accepted convergence disposition:

```text
FJ899/8 PR #150
HEAD = b452d08120263956b66b792d3add11ae7d6a1931
TREE = 08c8fc7eb7f67345833f103de5928597d5b89197
PATH = research/X1B_CONVERGENCE_SCOPE_REVIEW_2026-09-03.md
BLOB = 75998cff59fa7ca86c3977ac7222853e6446884d
```

Human acceptance:

```text
FJ899/8 PR #151
HEAD = 42c74a3e12cb5ba3557e5f1b17101a84adafa65d
TREE = 27a4991a8605ba332cb915d8585130bd34d31211
PATH = acceptance/X1B_CONVERGENCE_SCOPE_HUMAN_ACCEPT_2026-09-03.md
BLOB = 70f3d644e89fffba15cabeac287b2dfb37fc089b
HUMAN DECISION = accept
```

Therefore this review does not treat the following as X1B blockers by themselves:

```text
TPM/EK/AK
vendor CRLs
PMEM/NFIT
physical bare-metal locality
BMC console origin
ext4-only crash durability
universal power-loss persistence
hostile hypervisor/kernel/filesystem/Git binary
```

A finding is blocking here only when it attacks a property still required by the final brief, including trusted Human origin, currentness/supersession, fail-closed admission, exact logical effect, bypass closure, no-substitution, positive-path implementability or post-effect truth.

All four findings below satisfy that test.

## 4. Review method

The review checked the exact final brief against:

```text
original X1B false-attribution question
accepted corrective-design property set
Human-accepted convergence scope firewall
current FJ899/8 repository visibility
current trusted-Human repository permission
current GitHub REST review response structure
current GitHub REST version/public-read documentation
GitHub username-change identity semantics
Git repository-selection environment semantics
concurrent local approval/effect interleavings
current ScriptOps approve and legacy accepted-state surfaces
```

The review distinguished:

```text
availability/DoS
from
false Human authority / stale authority / logical-effect substitution
```

A pure availability weakness was not promoted to a blocker unless it invalidated the brief's required positive path. The findings below are stronger than DoS.

## 5. Positive-path dependency checks that passed

### 5.1 Evidence repository is public

Current repository metadata reports:

```text
FJ899/8 visibility = public
```

This supports the brief's choice of a credential-free public REST reader.

### 5.2 Public pull-request review list supports unauthenticated reads

GitHub's current REST documentation for:

```text
GET /repos/{owner}/{repo}/pulls/{pull_number}/reviews
```

states that the endpoint can be used without authentication when only public resources are requested.

Reference:

`https://docs.github.com/en/rest/pulls/reviews?apiVersion=2026-03-10`

### 5.3 API version is current

GitHub's API-version documentation currently lists:

```text
2026-03-10 = supported
```

Reference:

`https://docs.github.com/en/rest/about-the-rest-api/api-versions`

The final brief's `X-GitHub-Api-Version: 2026-03-10` is therefore not a blocker.

### 5.4 Trusted Human can submit a review

Current repository permission lookup reports:

```text
FJ899/8
litrgratis-pixel permission = read
```

GitHub documents that users with read access can review pull requests; in public repositories approving/request-changes reviews are available subject to repository review-limit settings.

References:

`https://docs.github.com/en/pull-requests/reference/pull-request-reviews`

`https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-pull-request-reviews-in-your-repository`

Thus the Human-positive-review mechanism is plausible on current repository permissions.

# FINDING 1

## 6. X1B-FINAL-IBR-F001 — mutable GitHub login is the sole Human authority identity

Severity: `BLOCKER`.

### 6.1 Frozen mechanism

The final brief freezes:

```text
TRUSTED HUMAN ACTOR = litrgratis-pixel
```

and accepts a Human review when, among other predicates:

```text
author.login = litrgratis-pixel
state = APPROVED
```

The Human authority object carries `human_login`, and the admission/decision record carries `human_actor = litrgratis-pixel`.

The brief does not freeze or validate the GitHub account's durable numeric user ID or user node ID.

### 6.2 GitHub login is not a durable account identity

GitHub's current username-change documentation states that a personal-account username can be changed and that, after the change, the old username becomes available for another person to claim.

Reference:

`https://docs.github.com/en/account-and-profile/concepts/username-changes`

GitHub's REST user documentation explicitly distinguishes login from durable identity and provides an endpoint described as using the durable user `ID` instead of a `login`, which can change over time.

Reference:

`https://docs.github.com/en/rest/users/users?apiVersion=2026-03-10`

### 6.3 Current evidence demonstrates a durable ID is available

A raw current review object from the already-used Human account in `FJ899/scriptops PR #33` contains:

```text
user.login = litrgratis-pixel
user.id = 226907434
user.node_id = U_kgDODYZVKg
```

Therefore the API already provides an account identity stronger than the mutable login string.

### 6.4 False-Human-origin counterexample

The following path uses normal GitHub semantics rather than account compromise:

```text
1. trusted Human account currently named litrgratis-pixel exists;
2. that account changes its GitHub username to another available login;
3. GitHub releases the old login litrgratis-pixel for reuse;
4. another account claims the old login;
5. that different account submits the exact required APPROVED review body;
6. review.user.login == "litrgratis-pixel";
7. verifier accepts the review because no durable user ID/node ID is bound;
8. ScriptOps can reach HumanDecision = TRUE although the trusted Human account did not perform this decision act.
```

This is not a compromised-Human-account attack. The trusted original account may remain fully secure; the problem is that the authority identity is a reassignable label.

### 6.5 Scope disposition

This directly attacks:

```text
trusted Human decision origin
Human authority identity
false Human attribution
```

It is therefore Classification-A/core X1B, not separate platform hardening.

### 6.6 Required disposition

```text
X1B-FINAL-IBR-F001 = BLOCKER
```

Any successor brief must freeze an authority identity that remains bound to the same GitHub account across login changes and must propagate that identity through review validation, admission and durable attribution. This review does not select the repair mechanism.

# FINDING 2

## 7. X1B-FINAL-IBR-F002 — multi-request GitHub authority read has no consistent current-state linearization

Severity: `BLOCKER`.

### 7.1 Frozen mechanism

The final reader builds what the brief calls one fresh current authority snapshot from multiple independent REST operations:

```text
PR metadata
changed-file pages
review pages
request.json at fetched head SHA
accepted-scene.fountain at fetched head SHA
```

The brief then treats successful completion as the final authority linearization point.

No final re-read or generation token is frozen that proves the PR head/current-review state remained unchanged across those calls.

### 7.2 Evaluated adversary is allowed to update the evidence PR

The final threat model explicitly allows the evaluated AI/process to:

```text
create/update GitHub decision-evidence PRs using a non-Human account or external orchestration
```

Therefore PR-head mutation during the reader sequence is in scope.

### 7.3 Head-drift counterexample

Let the evidence PR initially be at Human-approved head `H1`.

Interleaving:

```text
T1 reader GETs PR metadata and records head = H1
T2 AI/process updates the evidence PR to H2
T3 reader obtains a changed-path collection whose path set remains the same two paths
T4 reader fetches request.json and accepted-scene.fountain explicitly by old H1
T5 reader obtains the review collection containing the exact Human APPROVED review on H1
T6 all frozen comparisons against the locally retained H1 tuple pass
T7 admission is produced even though current evidence-PR head is H2
```

The two files on H2 may contain different decision material while retaining the same two paths. The changed-file collection alone does not prove its contents equal H1.

The brief itself states:

```text
An older APPROVED review on an old PR head never authorizes the changed head.
```

The sequence above violates that property because `current PR head` was observed only before the mutation.

### 7.4 Review-state mutation has the same structural problem

The review list can also change while multi-page or multi-endpoint collection is in progress. GitHub review dismissal changes a submitted review's state to `DISMISSED`, while the returned object retains the review's original `submitted_at` field. GitHub also exposes a separate `review_dismissed` timeline event with its own event time.

References:

`https://docs.github.com/en/rest/pulls/reviews?apiVersion=2026-03-10`

`https://docs.github.com/en/rest/using-the-rest-api/issue-event-types?apiVersion=2026-03-10`

The brief does not bind a transaction/generation across PR metadata, review state and file reads. Therefore the term `snapshot` presently overstates what the REST sequence establishes.

### 7.5 Why this is not an impossible instantaneous-currentness demand

No system can prevent an external event from occurring after a defined linearization point.

The blocker is narrower:

```text
there is presently no single defined observation in the frozen algorithm
at which the complete admitted tuple is proven to have coexisted.
```

A later event after a correctly defined final check may be treated as later. A mutation between unbound reads cannot simply be labeled later than the whole snapshot when part of the snapshot was read before it.

### 7.6 Scope disposition

This directly attacks:

```text
current Human review/head semantics
freshness / supersession
old-head denial
exact current evidence binding
```

It is core X1B currentness, not hardware/platform hardening.

### 7.7 Required disposition

```text
X1B-FINAL-IBR-F002 = BLOCKER
```

Any successor must freeze a realizable consistency/linearization rule for the multi-resource GitHub read. This review does not prescribe the mechanism.

# FINDING 3

## 8. X1B-FINAL-IBR-F003 — local effect lacks mutual exclusion / pre-commit base CAS

Severity: `BLOCKER`.

### 8.1 Frozen local effect

After admission the brief requires:

```text
1. re-check exact main/base and clean tree/index;
2. capture pre-effect scene/log;
3. write scene;
4. append record;
5. stage;
6. verify two staged paths;
7. verify staged bytes;
8. set executor identity;
9. git commit;
10. post-effect verify parent == request.scriptops_base_head.
```

There is no frozen process-wide mutual exclusion covering this sequence and no compare-and-swap on `refs/heads/main` immediately before the effect becomes canonical.

### 8.2 Evaluated adversary can invoke approval repeatedly

The final threat model explicitly permits repeated invocation of the local approval path.

Nothing freezes a single-executor assumption or forbids concurrent invocations.

### 8.3 Deterministic two-invocation interleaving

Consider two independently Human-approved requests `A` and `B`, both generated from the same ScriptOps base `B0`, for different scenes.

Both processes can complete pre-admission and final Human-evidence validation while main is `B0`.

Then:

```text
A: effect step 1 sees main = B0, clean
B: effect step 1 sees main = B0, clean
A: writes/stages/verifies its exact two-path effect
A: commits C1 with parent B0
B: continues after its already-completed step-1 check
B: captures the now-current log prestate containing A's record
B: writes/stages/verifies its own scene + one append relative to that newer prestate
B: git commit creates C2 with parent C1
```

At that point `B` has created a canonical commit although its admission and request were bound to base `B0`.

The later post-effect test correctly notices:

```text
parent(C2) != B0
```

and returns `RECOVERY_REQUIRED`, but detection occurs **after the unauthorized/substituted logical effect has already been committed to main**.

### 8.4 Post-effect detection does not satisfy executor no-substitution

The accepted corrective design and convergence firewall preserve:

```text
executor no-substitution at the selected logical canonical-effect boundary
```

A mechanism that can commit an effect after its bound base has changed and only discover the mismatch afterward does not prevent substitution.

This is not a power-loss durability theorem. It is an ordinary concurrent-process correctness problem inside the selected logical Git effect.

### 8.5 Git provides compare-and-swap semantics, demonstrating realizability

Git documents that:

```text
git update-ref <ref> <new-oid> <old-oid>
```

updates a ref only after verifying that its current value matches the expected old object ID.

Reference:

`https://git-scm.com/docs/git-update-ref`

This review does not require that exact implementation. It establishes only that the brief currently lacks any frozen equivalent mutual-exclusion/CAS property.

### 8.6 Scope disposition

This attacks:

```text
exact base binding
logical canonical-effect identity
executor no-substitution
ordinary process failure/concurrency semantics
```

All are explicitly inside the final scope firewall.

### 8.7 Required disposition

```text
X1B-FINAL-IBR-F003 = BLOCKER
```

# FINDING 4

## 9. X1B-FINAL-IBR-F004 — caller-controlled Git repository environment can redirect authority-critical Git operations

Severity: `BLOCKER`.

### 9.1 Caller environment is already treated as authority-relevant input

The final brief explicitly rejects caller environment values for GitHub credentials and proxy variables. Therefore the invocation environment is not implicitly trusted as fixed.

However, authority-critical Git operations do not have an equivalent repository-identity environment contract.

### 9.2 Git repository identity is environment-overridable

Git's current documentation states:

```text
GIT_DIR sets the repository directory instead of the default .git
GIT_WORK_TREE sets the working-tree root
GIT_COMMON_DIR redirects normally shared repository files
GIT_INDEX_FILE selects an alternate index
GIT_OBJECT_DIRECTORY / GIT_ALTERNATE_OBJECT_DIRECTORIES alter object lookup
GIT_NAMESPACE changes ref namespace
```

References:

`https://git-scm.com/docs/git`

`https://git-scm.com/book/en/v2/Git-Internals-Environment-Variables`

The final brief only freezes `GIT_NO_REPLACE_OBJECTS=1` for some readback commands. It does not require authority-critical Git commands to reject/scrub repository-redirection variables or independently prove that the Git directory/ref namespace being read and committed is the intended ScriptOps repository.

### 9.3 Repository-redirection counterexample

Under ordinary trusted Git semantics, the evaluated caller can prepare an alternate Git directory whose main ref/index/object view is consistent with the expected ScriptOps base, then invoke the approval process with repository-location environment variables pointing Git at that alternate repository while the Python runtime still uses the real ScriptOps working-tree paths.

A representative shape is:

```text
GIT_DIR=<attacker-prepared alternate gitdir>
GIT_WORK_TREE=<real ScriptOps working tree>
```

The exact environment can be made to expose the expected base objects/index to Git.

Then authority-critical commands that rely on inherited Git environment can:

```text
read symbolic HEAD/main from the alternate gitdir
stage real ScriptOps path bytes into the alternate index
commit and advance alternate refs/heads/main
post-verify the alternate commit/ref
report HumanDecision = TRUE
```

while the intended ScriptOps repository's actual `.git` `refs/heads/main` did not receive the proven canonical effect.

That is a direct failure of:

```text
scriptops_repository = FJ899/scriptops
canonical ref = intended local refs/heads/main
post-effect logical truth
```

It does not require a malicious Git binary, kernel or filesystem.

### 9.4 Why this is within the Human-accepted convergence scope

The convergence review explicitly preserved mechanism-specific Git closure when a final implementation chooses local Git as the canonical effect and the mechanism can otherwise substitute the logical effect.

The final brief selected local Git main as its logical canonical target, so repository/ref identity is a Classification-B requirement that became active again by mechanism choice.

This is not a return to raw-object crash durability or physical storage proofs.

### 9.5 Required disposition

```text
X1B-FINAL-IBR-F004 = BLOCKER
```

Any successor must freeze how authority-critical Git commands are anchored to the intended ScriptOps repository/ref/worktree independently of caller-controlled repository-redirection environment. This review does not select the repair mechanism.

## 10. Non-blocking observations

### 10.1 Public API rate limits are availability, not false Human authority

Credential-free public API access is subject to GitHub's unauthenticated rate limits and network availability. The final brief correctly fails closed on API/rate-limit failure.

This may reduce availability but does not create a false Human decision and is not promoted here to a blocker.

### 10.2 Public third-party reviews can cause deliberate denial

Because the evidence repository is public, other users may be able to submit reviews depending on moderation settings. The final brief's reserved-marker ambiguity rule can therefore be used to deny a particular evidence PR.

That is a DoS/liveness concern. It does not let a non-Human account satisfy the exact trusted-Human review predicate, so it is not promoted to a false-authorship blocker in this review.

### 10.3 Hardware findings remain out of scope

Nothing in this review reopens:

```text
R4R17 BMC/console locality
Infineon CRL positive-path profile
TPM transport locality
PMEM/NFIT
ext4 crash durability
```

Those remain preserved historical/separate-hardening findings under PR #150/#151.

## 11. Finding-to-scope matrix

| Finding | Property falsified | X1B scope |
|---|---|---|
| F001 mutable login | trusted Human origin / authority identity | `CORE / BLOCKING` |
| F002 non-atomic REST snapshot | currentness / supersession / exact current head | `CORE / BLOCKING` |
| F003 no CAS/mutual exclusion | base binding / executor no-substitution | `CORE / BLOCKING` |
| F004 Git environment redirect | selected logical canonical target / post-effect truth | `MECHANISM-ACTIVE B-CLASS / BLOCKING` |

No finding above relies on a C-class physical-platform claim.

## 12. PASS-criteria disposition

Against the final brief's own section-35 criteria:

```text
1 self-contained implementability
  = NOT PASS because authority and local-effect security choices remain unfrozen

2 Human authority separate from effect capability
  = NOT PASS because login label is reassignable independently of the trusted account

3 non-circular identities
  = PASS on current evidence

4 Human-readable exact presentation
  = PASS on current evidence

5 complete/deterministic current Human review semantics
  = NOT PASS because multi-call state has no consistent current-state linearization

6 changed head/old review must deny
  = NOT PASS because head can change between metadata read and admission

7 current/legacy accepted-state bypass coverage
  = PASS at brief level on current evidence

8 public credential-free GitHub positive path
  = PASS at dependency/specification level on current evidence

9 local two-path effect sufficiently specified
  = NOT PASS because concurrent base drift and repository redirection are not prevented

10 machine metadata not Human authorship
  = PASS on current evidence

11 failure/replay cannot yield unauthorized success/effect
  = NOT PASS because concurrent invocation can commit before base mismatch is detected

12 mandatory controls executable
  = NOT PASS until the blocking mechanisms above are frozen/testable

13 no C-class hardware reintroduced
  = PASS
```

Overall:

```text
AK-CANON X1B FINAL BOUNDED IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

## 13. Convergence assessment

This NOT PASS does **not** reverse the Human-accepted convergence decision.

The final brief is materially closer to the original X1B problem than R4R17. All four blockers are finite and directly tied to the selected mechanism:

```text
immutable Human account identity
consistent current GitHub evidence
single/CAS local canonical-effect execution
fixed local Git repository identity
```

No new hardware/security domain is required to address them.

Therefore the correct project interpretation is:

```text
CONVERGENCE STRATEGY = STILL VALID
FINAL BOUNDED BRIEF = NEEDS ONE BOUNDED REOPEN
R4R18 PHYSICAL-PLATFORM LINEAGE = STILL NOT REOPENED
```

This review does not authorize that reopen.

## 14. Explicit non-authority / STOP

This review authorizes no:

```text
successor final brief
repair design
ScriptOps source mutation
phase6/x1b_human_decision.py creation
CODEOWNERS/ruleset mutation
GitHub decision-evidence PR for a live effect
Human live APPROVED decision
positive-control execution
canonical screenplay effect
merge
X1B corrective closure
Agency Kernel V1
release
deployment
tag
```

After durable freeze of this exact review:

```text
STOP
NEXT LEGAL STAGE = HUMAN DISPOSITION ON THESE FOUR IN-SCOPE BLOCKERS
```

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
NOT PASS != SCOPE FAILURE
NOT PASS != R4R17 REOPEN
AI PROPOSES != HUMAN DECIDES
```
