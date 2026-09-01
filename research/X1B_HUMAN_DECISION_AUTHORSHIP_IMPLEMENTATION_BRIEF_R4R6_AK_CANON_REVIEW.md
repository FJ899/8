# X1B Human Decision Authorship — Independent AK-CANON R4R6 Implementation-Brief Review

Status: `INDEPENDENT REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: `2026-09-01`

## 1. Verdict

`AK-CANON X1B R4R6 IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

R4R6 materially improves R4R5 and directly addresses both findings frozen in PR #125 at brief level:

1. configured Git hooks are no longer treated as equivalent to traditional hookdir hooks: R4R6 rejects ambient effective `hook.*` configuration, redirects the traditional hook path to a verified private empty directory, and hard-disables the two hook events reachable by the bounded Git 2.55.x plumbing sequence;
2. Git object/reference writes no longer inherit ambient durability defaults: R4R6 requires command-scope `core.fsync=all` plus `core.fsyncMethod=fsync`, rejects ambient durability overrides, verifies the new object closure before CAS, and distinguishes visible ref commitment from durability-proven completion.

The V6 migration correctly prevents V5 Human evidence from silently authorizing the changed V6 material effect.

However, independent adversarial review found two new material blockers in the exact `files` reference-store boundary:

1. R4R6 binds the logical ref name and value but does not bind the physical topology through which the `files` backend resolves and updates that ref. Git 2.55 continues to support real symlink refs whose link text begins with `refs/`; a logical `refs/heads/main` can therefore be a symlink to another ref. Directory symlinks or equivalent filesystem aliasing in the common Git directory can similarly redirect the physical ref write outside the intended path while logical Git reads still return the expected SHA;
2. `git update-ref` may durably append a reflog for `refs/heads/main`. In a worktree repository `core.logAllRefUpdates` is normally enabled, and an existing reflog also causes logging. The resulting record contains old/new object IDs plus committer identity and wall-clock date/time. R4R6 neither binds nor disables that durable side effect, so the exact Human-presented effect remains incomplete and ambient-dependent.

Either finding independently prevents implementation authority.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R6 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R6 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#126`

```text
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
BASE TREE = df807db7003dfd201e9be4d5927472e515a2e737
HEAD = 8cbe07b7e48379a49fdb6d154ffa56d489a45b5e
TREE = af54604cb1deb19e016a44e96efc5ee290be6d8e
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R6.md
BLOB = 8d9be9d8d2e481f990c90e63ed7de85320317cbb
```

Immediately before this review write, PR #126 remained:

```text
state = OPEN
merged = false
draft = true
commits = 1
changed_files = 1
```

The exact candidate commit, parent, tree, blob and one-file changed set were freshly reread before the review branch was created.

## 3. Normative lineage

### 3.1 Accepted corrective design

```text
FJ899/scriptops PR #34
HEAD = d7a5065c87e9a4b49fb608235c908bceac42b4b1
TREE = 3140d0ac95c120a7b1532942bae2e0dad38b4839
PATH = governance/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_CANDIDATE.md
BLOB = dac16f109d1414a2208c2ed9a166ae9e9a329216
```

Higher-level properties include:

```text
separate trusted Human decision evidence
exact content/scope/candidate/effect binding
executor no-substitution
fail closed on ambiguity
no core authority/security choice left implicit
current activity/conflict/replay semantics
real-boundary negative controls
post-effect truth matching the Human-bound effect
no failed operation durably misreported as successful Human-attributed effect
```

### 3.2 Independent corrective-design review

```text
FJ899/8 PR #109
HEAD = 132d65be48331a822039262b707c47a81d02a64d
TREE = a8bdc363d293beb7b15ae8b787cc3ebdd694fd99
BLOB = 439109e104244552a5ac1f3f08988dba283733d0
VERDICT = AK-CANON X1B CORRECTIVE DESIGN REVIEW R2 = PASS
```

### 3.3 R4R5 predecessor and binding review

```text
FJ899/8 PR #124
HEAD = 306bd9061a002f3615456dcb87c4cb9c7cd0d5b0
TREE = 42409e267506d97194abf0a9569d463285655e26
BLOB = ef67f2060cfe2593ef59a97ecab26aafcd46d4f8
```

```text
FJ899/8 PR #125
HEAD = 4a39aa7bc02d53928bb0f2a7c69a107d3623a953
TREE = 67e2e048d00a8bec02aa31bdb3e45e95733e108f
BLOB = d6e30fc22c204a1b7c18fb747878df265b501660
VERDICT = AK-CANON X1B R4R5 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #125 froze:

```text
X1B-R4R5-IBR-F001 configuration-defined Git hooks bypass core.hooksPath=/dev/null
X1B-R4R5-IBR-F002 unfrozen Git fsync / crash durability
```

## 4. Review method

The review attacked the exact R4R6 successor checklist rather than inferring PASS from stronger hook/fsync language.

The review checked current Git 2.55 documentation and upstream implementation behavior material to the frozen profile, including:

```text
hook.<name>.command / hook.<name>.event configuration
hook.<event>.enabled=false semantics
core.fsync=all component coverage
core.fsyncMethod=fsync
files backend ref resolution
real symbolic-link ref handling
git update-ref reflog creation/update rules
core.logAllRefUpdates worktree default
reflog record identity/time fields
```

Supporting disposable local reproductions were used only where the same behavior is explicitly retained/documented by the bounded Git 2.55 semantics. The local installed Git version was not used to infer absence of newer behavior.

No ScriptOps implementation, Human evidence, canonical screenplay content, local ScriptOps ref, or recovery state was mutated by this review.

## 5. PR #125 finding F001 — configured hooks

Disposition: `ADDRESSED AT BRIEF LEVEL`.

R4R6 now freezes three independent controls:

```text
ambient configured-hook census with includes/origin/scope
private verified empty traditional hook directory
command-scope event disables:
  hook.reference-transaction.enabled=false
  hook.post-index-change.enabled=false
```

The Git semantics profile is bounded to 2.55.x and the exact command set is bounded. Any additional command capable of firing another hook event is outside authority.

Current Git 2.55 documentation defines event-level `hook.<event>.enabled=false` to suppress hooks for that event regardless of per-hook enabled settings. The ambient census covers local/worktree/include configuration. The private hook directory separately closes the traditional hook path.

The exact configured-hook bypass frozen by PR #125 is therefore addressed at brief level.

## 6. PR #125 finding F002 — fsync / crash durability

Disposition: `ADDRESSED AT BRIEF LEVEL` within R4R6's explicit platform contract.

R4R6 requires every Git write that can introduce object/index/ref state to use:

```text
core.fsync=all
core.fsyncMethod=fsync
```

and rejects effective ambient values for:

```text
core.fsync
core.fsyncMethod
core.fsyncObjectFiles
```

It verifies the exact new object closure before CAS and bounds the reference backend to `files`.

Current Git documentation includes loose objects and references within the `all` durability component set. R4R6 also correctly treats an interrupted/nonzero `update-ref` that nevertheless leaves the new SHA visible as an uncertainty/recovery state rather than as no effect or complete durable success.

The exact unfrozen-fsync counterexample frozen by PR #125 is therefore addressed at brief level.

## 7. Finding X1B-R4R6-IBR-F001 — physical files-ref topology is not bound

Severity: `BLOCKER`.

### 7.1 Frozen R4R6 claim

R4R6 declares the only operative ref to be:

```text
refs/heads/main
```

and repeatedly validates:

```text
HEAD symbolic ref = refs/heads/main
raw HEAD SHA = raw refs/heads/main SHA = exact request base
ref storage format = files
```

The final update is an old-value CAS of that logical name.

The material effect binds:

```text
target_ref = refs/heads/main
ref_before = exact request base
ref storage format = files
```

but it does not bind the physical path/topology implementing that logical ref.

### 7.2 Git 2.55 real ref symlinks remain supported

Current Git `update-ref` documentation explicitly retains the historical behavior that, when a ref path is a real symbolic link and its link text begins with `refs/`, Git follows that symlink as a ref alias.

This is distinct from the ordinary `ref: refs/...` symbolic-ref file format.

The `files` backend source likewise contains real-symlink resolution logic for normalized `refs/...` symlink targets.

Therefore this state is valid within the exact R4R6 `files` backend unless R4R6 independently rejects it.

### 7.3 Direct ref alias counterexample

A repository can contain:

```text
.git/refs/heads/main -> refs/heads/other
```

with both logical names initially resolving to the exact request-base SHA.

Then all of these R4R6 facts can be true before CAS:

```text
HEAD symbolic name = refs/heads/main
rev-parse/read of refs/heads/main = request base
raw logical main value = request base
ref storage format = files
prepared commit parent = request base
```

Yet:

```text
git update-ref refs/heads/main <new> <old>
```

follows the real symlink and physically updates `refs/heads/other`.

A post-CAS logical reread of `refs/heads/main` again follows the same alias and returns `<new>`.

Thus the R4R6 pre-CAS and post-CAS logical checks can all pass while the physical ref actually mutated is not the Human-bound ref path.

A disposable supporting reproduction confirmed exactly this pattern: the real symlink remained, `update-ref` returned success, and the target ref moved to the new SHA.

### 7.4 Parent-directory redirection is worse

R4R6 also does not bind the physical directory chain in the common Git directory used for refs.

A filesystem alias such as a symbolic-link `refs/heads` directory can redirect the physical loose-ref write outside the intended Git metadata path while Git still resolves the logical `refs/heads/main` name.

A disposable supporting reproduction replaced the heads directory with an outside-directory symlink; logical ref read returned the expected old SHA, and `update-ref` wrote the new loose ref into the outside target directory.

The exact portability details vary by platform/filesystem, but the security issue is invariant: `ref format = files` plus logical ref-name/value equality does not prove physical target containment or no-alias topology.

### 7.5 Why worktree target alias protections do not close this

R4R6 has strong inode/symlink/hardlink protections for:

```text
scenes/<scene_id>.fountain
.scriptops/decision-log.ndjson
```

Those protections do not apply to the Git common directory reference store.

The same rigor is not frozen for:

```text
.git or common Git directory identity
refs/
refs/heads/
refs/heads/main
packed-refs when consulted
logs/refs/heads/main when consulted/created
```

The ref update is delegated to Git after only logical checks.

### 7.6 Security consequence

The Human-presented effect says:

```text
mutate refs/heads/main from P to C
```

but the actual bounded implementation could perform:

```text
logical refs/heads/main -> physical refs/heads/other
```

or a path outside the intended repository metadata location, while logical post-verification still succeeds.

This violates:

```text
exact target-ref binding
exact material-effect binding
executor no-substitution
no hidden additional/ref-substitution effect
post-effect truth matching the Human-bound effect
no core security choice left implicit
```

### 7.7 Required successor correction class

A successor brief must freeze physical files-ref-store topology rather than only logical ref semantics.

At minimum it must establish a reviewed fail-closed policy covering the effective common Git directory and every physical path relevant to the main ref transaction, including alias/symlink/reparse/mount-style substitution where applicable.

It must explicitly define treatment of:

```text
loose refs/heads/main
parent refs directories
packed-refs when authority-relevant
common-dir/worktree indirection
physical path containment
real symbolic-link refs
filesystem aliases capable of redirecting the ref write
```

Mandatory regressions must include at least:

```text
refs/heads/main real symlink -> another refs/... name
refs/heads parent-directory symlink/redirect
outside-repository ref-store redirect
post-check logical ref still expected while physical target differs
packed-vs-loose ambiguity if packed refs are supported
```

All such cases must fail closed before Human-attributed commitment unless their exact physical effect is explicitly Human-bound and independently reviewed.

This review does not authorize the correction mechanism.

## 8. Finding X1B-R4R6-IBR-F002 — update-ref reflog is an unbound durable effect

Severity: `BLOCKER`.

### 8.1 R4R6's declared effect set

R4R6 presents the Human with a material effect containing:

```text
one exact two-path Git tree delta
one exact local ref update
one decision-log record
post-CAS filesystem/index materialization
```

The exact ref commitment is delegated to `git update-ref` under the hardened profile.

No V6 schema field describes a Git reflog effect.

### 8.2 `update-ref` can write a reflog

Current Git `update-ref` documentation states that an update to a branch ref is logged when the applicable reflog policy requires it, including when `core.logAllRefUpdates` is enabled or a reflog for the ref already exists.

For a worktree/non-bare repository, `core.logAllRefUpdates` normally defaults to enabling logs for branch refs.

The reflog line records at least:

```text
old object ID
new object ID
committer name
committer email
committer date/time
```

plus optional log message metadata where supplied.

Appending the reflog is part of the ref update operation and can itself affect whether the operation succeeds.

### 8.3 The reflog bytes are not Human-bound

R4R6 carefully freezes the raw commit object's author/committer identity and timestamp:

```text
ScriptOps X1B <scriptops-x1b@local.invalid>
request_created_at-derived epoch
+0000
```

But those exact values apply to the raw commit content constructed in memory.

R4R6 does not correspondingly freeze for the `update-ref` reflog:

```text
GIT_COMMITTER_NAME
GIT_COMMITTER_EMAIL
GIT_COMMITTER_DATE
core.logAllRefUpdates
existing reflog presence/absence
reflog prior bytes/hash
reflog target physical identity/path
a deterministic update-ref log message
exact resulting reflog bytes/hash
```

Therefore two repositories with identical Human-bound request content/ref/object state can produce different durable metadata bytes during the same supposed exact effect.

### 8.4 This is not merely diagnostic output

The reflog is repository state under the Git common directory. It is semantically observable and participates in ordinary Git reference-history/reachability behavior.

Under R4R6's own `core.fsync=all` policy, ref-related metadata may also be explicitly hardened rather than left as an ephemeral cache.

So the effect is not safely characterized as an irrelevant transient side effect.

### 8.5 Failure behavior is also ambient-dependent

Because reflog append is part of the ref update path, an unbound reflog topology/permission/identity problem can change the command outcome.

For example, identical Human-bound content can behave differently depending on:

```text
whether logs/refs/heads/main already exists
whether ref logging is enabled
whether committer identity can be resolved
whether the reflog path can be created/appended
filesystem alias/permission state on the logs path
```

Those are not frozen V6 authority inputs.

### 8.6 Exact material-effect violation

R4R6 claims a bounded Human effect but leaves a durable Git-generated mutation outside the presented effect schema.

The problem is not only that the bytes are unpredicted. The ref transaction can be expanded from:

```text
P -> C on refs/heads/main
```

into:

```text
P -> C on refs/heads/main
+
append ambient-dependent reflog record
```

without the Human request binding that second mutation.

This violates:

```text
exact material-effect binding
executor no-substitution/no-expansion
same content + scope + candidate + effect identity
post-effect truth matching Human-presented effect
no core security choice left implicit
```

### 8.7 Required successor correction class

A successor brief must explicitly resolve reflog semantics for the exact ref transaction.

It must choose and freeze a reviewed policy that either:

```text
Human-binds the complete deterministic reflog effect
```

or:

```text
proves no reflog can be created or modified by the bounded commitment operation
```

The mechanism itself is not authorized by this review.

If reflog mutation is permitted, the bound effect must cover at minimum:

```text
reflog existence/pre-state
exact physical target topology
old/new SHA
identity
exact timestamp source/offset
message semantics
exact append bytes
post-state hash/bytes
crash-durability relationship to the ref transaction
```

If reflog mutation is forbidden, the successor must prove the exact bounded Git 2.55.x path cannot create/update one even when:

```text
core.logAllRefUpdates would otherwise enable it
an existing reflog is present
repository/worktree/include config attempts to enable logging
```

Mandatory regressions must include both existing-reflog and auto-create-policy cases and must prove there is no hidden extra durable mutation.

This review does not authorize the correction mechanism.

## 9. Preserved pass-level dispositions

The following R4R6 properties are not rejected by this review and remain acceptable at brief level subject to the two blockers above:

```text
V6 schema migration and no V5 evidence reuse
one current approve --decision-pr interface
direct legacy acceptance disabled
exact Human actor/review-body binding
credential-free exact-origin public GitHub evidence transport
complete review pagination/currentness/conflict semantics
NO WALL-CLOCK TTL / age-alone-not-stale policy
exact refs/heads/main logical ref requirement
side/detached ref denial
no-replace raw-object authority
no-lazy-fetch / complete-local-store policy
partial/promisor/alternate-store denial
closed raw commit object with independent SHA-1
no commit-tree / no ambient encoding header
private temporary index / exact two-path tree
configured-hook census and Git 2.55 event disables
private traditional hook directory
core.fsync=all + core.fsyncMethod=fsync hardening
ambient fsync override rejection
new object closure verification
no canonical worktree/index mutation before CAS
REF_COMMITTED result narrower than generic SUCCESS
durability-uncertain / commitment-unknown outcome classes
no silent ref rollback after visible commitment
alias-safe post-CAS scene/log materialization
hardlink/symlink protections on worktree targets
bounded replay and same-worktree lock
Human attribution only from validated Human review
```

These dispositions do not offset either new blocker.

## 10. Why implementation authority is not established

An implementation brief must be specific enough that the implementer does not invent a security-critical policy at the authority boundary.

R4R6 still leaves two such policies unresolved:

```text
what physical files-ref topology is trusted/allowed
what exact reflog effect is allowed or forbidden
```

Both directly determine what persistent repository state `update-ref` may mutate.

Therefore an implementation that merely follows the current R4R6 text could be internally test-green while violating the Human-presented material effect.

`TESTS GREEN != BINDING CLOSURE`.

## 11. Frozen successor obligations

Any later successor brief must preserve every accepted R4R6 property and explicitly resolve both blockers.

### Obligation A — physical files-ref topology

It must make it impossible for a logically correct `refs/heads/main` read/CAS/post-read sequence to silently mutate another physical ref/path.

The proof must cover all physical ref-store inputs actually used by the bounded Git 2.55.x files backend.

### Obligation B — reflog exact-effect semantics

It must make reflog behavior part of the closed authority model rather than ambient Git behavior.

A failed or successful ref transaction must have no hidden Human-unpresented durable log mutation.

### Regression minimum

At least:

```text
real symlink main ref -> other ref
ref parent directory redirection
outside common-dir ref target
logical ref post-check passes while physical target differs
pre-existing main reflog
auto-created main reflog
ambient core.logAllRefUpdates variations
ambient committer identity/date variations
reflog path alias/permission failure
ref CAS success/failure with exact reflog policy proved
```

No successor mechanism is authorized by this review artifact.

## 12. Review disposition

```text
R4R5 IBR F001 CONFIGURED-HOOK EXECUTION = ADDRESSED IN R4R6
R4R5 IBR F002 UNFROZEN GIT FSYNC / CRASH DURABILITY = ADDRESSED IN R4R6

R4R6 IBR F001 PHYSICAL FILES-REF TOPOLOGY / SYMLINK ALIAS = BLOCKER
R4R6 IBR F002 UNBOUND UPDATE-REF REFLOG EFFECT = BLOCKER

AK-CANON X1B R4R6 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
IMPLEMENTATION AUTHORITY = NOT ESTABLISHED
X1B = OPEN
V1 AUTHORITY = NOT ESTABLISHED
```

## 13. Explicit non-authority

This review does not authorize:

```text
successor brief preparation
physical ref-store repair
reflog-policy repair
ScriptOps source mutation
Human decision PR creation
Human review creation
positive control
canonical screenplay mutation
decision-log mutation
refs/heads/main effect
recovery
merge
X1B closure
V1 entry
release
deployment
tag
```

`REVIEW FINDING != REPAIR AUTHORITY`.

## 14. STOP

The only next governance stage that may be considered is a successor corrective implementation brief that addresses both frozen R4R6 findings while preserving prior accepted properties.

That successor brief requires fresh separate Human authorization.

```text
R4R6 REVIEW NOT PASS != SUCCESSOR REPAIR AUTHORITY
R4R6 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R6 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
STOP
```
