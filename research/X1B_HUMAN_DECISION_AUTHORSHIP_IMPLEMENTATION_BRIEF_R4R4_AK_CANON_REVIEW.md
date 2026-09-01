# X1B Human Decision Authorship — Independent AK-CANON R4R4 Implementation-Brief Review

Status: `INDEPENDENT REVIEW / NOT IMPLEMENTATION AUTHORITY`

Date: `2026-09-01`

## 1. Verdict

`AK-CANON X1B R4R4 IMPLEMENTATION-BRIEF REVIEW = NOT PASS`

R4R4 materially improves R4R3 and directly addresses both findings frozen in PR #121 at brief level:

1. replacement-object interpretation is explicitly denied and authority-critical commit/tree semantics are raw/no-replace;
2. operative `commit-tree` construction is removed and replaced with an independently constructed closed raw commit object whose SHA-1 and exact bytes are verified before ref mutation.

The V4 schema migration also correctly prevents hypothetical V3 Human evidence from authorizing the changed V4 material effect profile.

However, independent adversarial review found two new material blockers:

1. R4R4 does not disable Git partial-clone/promisor lazy fetching. An authority-critical plumbing command such as `read-tree` can automatically spawn `git fetch` for a missing promised tree, including after `FinalEffectGateV4`, despite the brief's explicit no-network rule. The exact subprocess profile omits `--no-lazy-fetch` / `GIT_NO_LAZY_FETCH=1` and does not reject partial/promisor repositories.
2. R4R4 writes a canonical `X1BDecisionRecordV4` with `"result":"SUCCESS"` and Human attribution before successful `refs/heads/main` compare-and-swap. The brief explicitly permits a later pre-CAS failure whose rollback cannot be proven, leaving a dirty/BLOCKED state. In that allowed state, the canonical decision log can retain a durable Human-attributed `SUCCESS` record even though the effect never reached the successful ref commitment point.

Either finding independently prevents implementation authority.

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R4 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R4 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 2. Exact reviewed candidate

Repository: `FJ899/8`

PR: `#122`

```text
BASE = 1e4114e3f7ab6383af2549383b25329bed21eef9
BASE TREE = df807db7003dfd201e9be4d5927472e515a2e737
HEAD = 7727407eef42447509eae2e60ef2d1e1892c0105
TREE = ce8c4e636ab036fedfca1a2a1bff88c7fdbd020a
PATH = research/X1B_HUMAN_DECISION_AUTHORSHIP_IMPLEMENTATION_BRIEF_R4R4.md
BLOB = 23817f0823898d0c857483c2fa5d64c2c261ba06
```

Immediately before review write, PR #122 remained:

```text
state = OPEN
merged = false
draft = true
commits = 1
changed_files = 1
```

The exact one-file candidate, commit, tree and BLOB were freshly re-read before this review branch was created.

## 3. Normative lineage

### 3.1 Accepted corrective design

```text
FJ899/scriptops PR #34
HEAD = d7a5065c87e9a4b49fb608235c908bceac42b4b1
TREE = 3140d0ac95c120a7b1532942bae2e0dad38b4839
PATH = governance/X1B_HUMAN_DECISION_AUTHORSHIP_CORRECTIVE_CANDIDATE.md
BLOB = dac16f109d1414a2208c2ed9a166ae9e9a329216
```

The accepted design requires, among other things:

```text
separate trusted Human decision evidence
exact content/scope/candidate/effect binding
executor no-substitution
fail closed on ambiguity
current activity/conflict/replay semantics
no unauthorized canonical effect in required negative controls
post-effect truth matching the Human-bound effect
durable Human attribution derived from exact trusted evidence
```

### 3.2 Independent corrective-design review

```text
FJ899/8 PR #109
HEAD = 132d65be48331a822039262b707c47a81d02a64d
TREE = a8bdc363d293beb7b15ae8b787cc3ebdd694fd99
BLOB = 439109e104244552a5ac1f3f08988dba283733d0
VERDICT = AK-CANON X1B CORRECTIVE DESIGN REVIEW R2 = PASS
```

### 3.3 R4R3 and its binding review

```text
FJ899/8 PR #120
HEAD = df095fc822f6b454bc69e24e727c9b9dcfe64844
TREE = ad625ba054ba0c38d3dfd1baf3b7980753c553a2
BLOB = 17521e2f3616bdc356c4dca4c13c96fcd5114117
```

```text
FJ899/8 PR #121
HEAD = 4c2f553b5caa82684ab01ad9ff4dc426c25f4821
TREE = 88724b607d497c72bfdf7b46a68ec0e10e09fabc
BLOB = 113cd77025d9f57261417300be01d98507f90a0a
VERDICT = AK-CANON X1B R4R3 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
```

PR #121 froze:

```text
X1B-R4R3-IBR-F001 replacement-ref / raw-object substitution
X1B-R4R3-IBR-F002 local commit-encoding config / extra commit header
```

and recorded that the earlier local-ref, write-target-hardlink and freshness/supersession findings were already addressed at brief level.

## 4. Review method

The review did not infer PASS from R4R4's explicit no-replace and raw-commit construction rules.

The successor checklist was attacked literally, together with adjacent local-Git and failure-boundary questions:

```text
Can replacement refs still reinterpret the Human-bound SHA/tree?
Can graft/shallow state defeat the raw-parent claim?
Can commit-local config add headers to the durable commit object?
Can any authority-critical Git command perform implicit network I/O?
Can a promisor remote cause a fetch after the Human-currentness commitment point?
Can a failure before successful ref CAS leave canonical accepted bytes?
Can a failure before successful ref CAS leave a durable record claiming SUCCESS?
Does the rollback contract prove absence of false Human-attributed success, or only attempt restoration?
Can V3 evidence authorize V4 effect semantics?
Can side/detached refs or known filesystem aliases become operative?
Is any core security choice still left to the implementer?
```

Two local disposable reproductions were used only to test Git semantics. No ScriptOps repository or canonical screenplay content was mutated.

## 5. PR #121 finding F001 — R4R4 disposition

`ADDRESSED AT BRIEF LEVEL`.

R4R4 now requires both:

```text
GIT_NO_REPLACE_OBJECTS=1
git --no-replace-objects <subcommand>
```

for every authority-critical Git command and separately requires zero `refs/replace/*` at repeated checkpoints.

Raw request-base authority is derived from exact no-replace `cat-file commit` bytes, with the tree header parsed from those raw bytes rather than trusted through replace-aware revision interpretation.

R4R4 also explicitly rejects shallow repositories and legacy graft sources and requires corresponding negative regressions.

This closes the exact replacement-ref counterexample frozen by PR #121 at brief level.

## 6. PR #121 finding F002 — R4R4 disposition

`ADDRESSED AT BRIEF LEVEL`.

R4R4 no longer permits `git commit-tree` to choose the operative effect commit representation.

It defines exact raw commit content with exactly four headers in exact order:

```text
tree
parent
author
committer
```

and forbids `encoding`, signature, `mergetag`, duplicate/unknown header and extra parent state.

The effect commit object ID is independently computed as raw SHA-1 over:

```text
"commit <len>\0" + exact raw commit content
```

before `hash-object -w -t commit --stdin`; Git's returned object ID must equal the independent digest and no-replace `cat-file` readback must be byte-identical.

Therefore repository-local `i18n.commitEncoding` cannot alter the operative commit object under the literal R4R4 construction.

The V4 migration correctly binds the changed raw-object/commit-object profile into fresh Human evidence rather than silently reusing V3 authority.

## 7. Finding X1B-R4R4-IBR-F001 — promisor lazy fetch can perform implicit network I/O after FinalEffectGateV4

Severity: `BLOCKER`.

R4R4 states:

```text
No acceptance Git subprocess may be a network operation.
```

It also freezes the Human-currentness commitment point at successful `FinalEffectGateV4` immediately before the first canonical filesystem mutation and states that between that point and first mutation there may be:

```text
no network
```

The exact Git subprocess profile contains:

```text
GIT_NO_REPLACE_OBJECTS=1
--no-replace-objects
GIT_CONFIG_NOSYSTEM=1
GIT_CONFIG_SYSTEM=/dev/null
GIT_CONFIG_GLOBAL=/dev/null
...
```

but does not contain:

```text
GIT_NO_LAZY_FETCH=1
--no-lazy-fetch
```

and R4R4 does not reject a partial-clone/promisor repository.

This matters because ordinary object-reading plumbing can automatically fetch a promised missing object. The invoking command need not literally be `git fetch`; Git can spawn fetch internally.

### 7.1 Concrete reproduction

A disposable local test repository was created with nested trees, then cloned using a partial-clone tree filter:

```text
server uploadpack.allowFilter = true
clone --no-checkout --filter=tree:0 file://<server> client
remote.origin.promisor = true
```

With a fresh temporary index, the authority-relevant command:

```text
GIT_INDEX_FILE=<tmp-index> GIT_TRACE=<trace> git -C client read-tree HEAD
```

returned success and the trace contained exactly one spawned `git fetch`.

In a fresh equivalent clone, the same operation with:

```text
GIT_NO_LAZY_FETCH=1
```

returned nonzero:

```text
128
fatal: failed to unpack tree object HEAD
```

The difference is exactly automatic promisor lazy fetching.

### 7.2 Why this reaches the R4R4 effect boundary

R4R4 step B initializes a temporary index from the exact raw parent tree with `read-tree <raw_parent_tree>` after `FinalEffectGateV4` success.

A non-shallow partial clone may have the commit object and top-level identity required to reach that stage while missing promised tree objects required to materialize the complete index. `read-tree` can then lazily fetch them.

Thus the literal R4R4 sequence permits:

```text
valid Human evidence
+
FinalEffectGateV4 success
+
partial/promisor local repository
+
missing promised tree object
->
post-gate implicit network fetch
```

This violates the frozen no-network commitment and can execute remote transport/helper behavior from repository-local promisor configuration after the Human-currentness commitment point.

The statement `no acceptance Git subprocess may be a network operation` is not sufficient by itself because the exact mechanism for ensuring that property is absent. The implementer must still choose whether to:

```text
set GIT_NO_LAZY_FETCH=1
use git --no-lazy-fetch
reject promisor/partial clones
prove every required object is local before the gate
or combine these controls
```

That is a security/effect-boundary choice, not a cosmetic implementation detail.

Disposition: `NOT PASS`.

## 8. Finding X1B-R4R4-IBR-F002 — pre-CAS canonical SUCCESS record can survive an explicitly permitted failed rollback

Severity: `BLOCKER`.

R4R4 constructs `X1BDecisionRecordV4` before the first filesystem mutation with:

```text
"result": "SUCCESS"
"human_actor": "litrgratis-pixel"
"human_rationale": <exact validated rationale>
```

and defines the decision-log effect as one canonical append.

The exact local effect sequence then performs, in order:

```text
E. materialize exact accepted scene bytes
F. materialize exact post-append decision-log bytes
G. verify both filesystem targets
H. update real index
I. prove real index tree
J. recheck ref/replacement state
K. only then CAS refs/heads/main to the prepared effect commit
```

Therefore the canonical decision-log file contains the Human-attributed `SUCCESS` record before the success-defining ref compare-and-swap.

R4R4 later states that if a failure occurs after filesystem/index mutation but before successful ref update it must:

```text
return nonzero
attempt deterministic restoration
...
never emit SUCCESS Human attribution
```

but it explicitly recognizes a failure mode where:

```text
exact restoration cannot be proven
```

and in that case requires a dirty/error `BLOCKED` state rather than claiming success.

### 8.1 Concrete counterexample class

The brief itself requires a negative regression for:

```text
main moved after FinalEffectGateV4 but before update-ref
```

Take that exact race after steps E/F have completed.

At step J or K the old-ref condition fails. The invocation is not successful. Now combine it with any condition under which exact restoration of `.scriptops/decision-log.ndjson` cannot be proven — a case R4R4 explicitly admits can occur.

The allowed terminal state is then:

```text
command result = BLOCKED/nonzero
refs/heads/main != prepared effect commit
successful ref effect = false
canonical decision-log may still contain X1BDecisionRecordV4
record.result = SUCCESS
record.human_actor = litrgratis-pixel
record.human_rationale = exact Human rationale
```

The same rollback failure may also leave the canonical scene filesystem bytes in their accepted form.

This is not merely an unreferenced Git object. `.scriptops/decision-log.ndjson` is itself an authority-relevant canonical target and the replay rule later treats any existing object carrying the same `decision_request_id` as prior consumption.

Thus a failed pre-CAS invocation can leave a durable artifact that both claims Human-attributed success and changes later replay behavior, while R4R4 simultaneously declares that the effect was not successful.

That contradicts the brief's own required properties:

```text
before successful refs/heads/main CAS, effect is not successful
never emit SUCCESS Human attribution on pre-CAS failure
failure/rollback never misreported as success
post-effect truth must match durable attribution
```

A best-effort rollback is not a proof that the false-success artifact cannot survive.

A successor brief must freeze a transaction/recovery representation in which a failed pre-success-commit path cannot leave an operative canonical record claiming `SUCCESS`, and must define the corresponding real failure-injection regressions. The exact repair mechanism is not authorized by this review.

Disposition: `NOT PASS`.

## 9. Mandatory adversarial question matrix

### Q1 — replacement ref reinterprets Human-bound SHA/tree

`PASS AT BRIEF LEVEL`.

Repeated zero-replace checks plus mandatory no-replace semantics and raw base parsing directly close the PR #121 counterexample.

### Q2 — graft/shallow ambiguity

`PASS AT BRIEF LEVEL`.

Both are explicitly rejected and tested.

### Q3 — local i18n.commitEncoding changes durable commit

`PASS AT BRIEF LEVEL`.

The closed raw commit bytes are constructed independently of `commit-tree` and verified byte-for-byte.

### Q4 — extra raw commit headers / second parent / altered message

`PASS AT BRIEF LEVEL`.

The closed four-header raw schema and independent digest/readback rule make these testable and fail-closed.

### Q5 — Git-returned object ID differs from independent SHA-1

`PASS AT BRIEF LEVEL`.

Exact equality is mandatory before canonical mutation.

### Q6 — V3 Human evidence reused for V4 effect

`PASS AT BRIEF LEVEL`.

The material effect profile and all authority-critical schemas/review marker are version-bumped and V3 is explicitly denied.

### Q7 — side/detached local ref

`PASS AT BRIEF LEVEL`.

`refs/heads/main` remains exact and CAS-bound.

### Q8 — known hardlink/symlink target substitution

`PASS AT BRIEF LEVEL` as to the predecessor attack class.

Single-link/no-follow/descriptor-relative target handling remains preserved.

### Q9 — post-gate local Git network effect

`FAIL` under X1B-R4R4-IBR-F001.

Promisor lazy fetch remains enabled by the frozen subprocess profile.

### Q10 — pre-CAS failure cannot leave SUCCESS attribution

`FAIL` under X1B-R4R4-IBR-F002.

The record is written as `SUCCESS` before CAS and rollback is explicitly allowed to be unprovable.

### Q11 — failure/rollback never misreported as success

`FAIL`.

The literal sequence permits a surviving canonical `SUCCESS` record in a BLOCKED/non-successful invocation.

### Q12 — core security/authority choice left to implementer

`FAIL`.

At minimum the implementer must still invent:

```text
promisor/partial-clone no-lazy-fetch policy
local-object-completeness proof before the commitment point
transaction/recovery semantics preventing surviving pre-CAS SUCCESS records
failure-injection semantics proving no false canonical success attribution
```

## 10. What R4R4 successfully preserves or improves

This NOT PASS does not erase the substantial corrections already frozen.

R4R4 preserves or improves at brief level:

```text
separate trusted Human decision event
exact V4 content/scope/candidate/effect binding
V3 -> V4 authority migration
acyclic request identity
one-file decision PR
exact Human actor + strict review body
credential-free public GitHub evidence
complete selected-PR review reconstruction
explicit no-TTL currentness policy
explicit conflict/deactivation/supersession policy
bounded replay claim
same-worktree invocation lock
exact refs/heads/main effect ref
old-SHA ref CAS
side/detached/ref-drift denial
raw no-replace base commit/tree authority
zero refs/replace requirements
shallow/graft denial
closed raw commit header/message/time schema
independent raw commit SHA-1
hash-object raw commit write + byte-identical readback
filter-safe exact output blobs
hook/signing/credential-helper controls
exact two-path temporary-index tree construction
single-link alias-safe target replacement
legacy approve denial
legacy scene-promote accepted denial
historical-vs-active runtime split
separate positive-control authority
closure/V1 separation
```

These properties are not reopened merely because new blockers were discovered.

## 11. Required successor-brief acceptance obligations

This review does not authorize repair.

A separately Human-authorized successor brief would need to preserve all accepted R4R4 properties and additionally freeze, at minimum:

```text
A. NO-LAZY-FETCH / LOCAL-OBJECT COMPLETENESS
   - authority-critical Git commands cannot perform promisor lazy fetch;
   - no network/helper invocation can occur through missing promised objects;
   - the effect process either rejects partial/promisor state or disables lazy
     fetch and proves all authority-required objects locally available;
   - negative regression uses a real partial clone with a missing promised
     tree/blob and proves fail-closed with zero fetch/helper execution;
   - post-FinalEffectGateV4 local Git remains network-inert by construction.

B. PRE-CAS SUCCESS-RECORD / RECOVERY TRUTH
   - no pre-success failure can leave an operative canonical record claiming
     result=SUCCESS for an effect whose successful commitment did not occur;
   - Human attribution and execution result remain semantically distinct and
     reconstructably true under failure;
   - rollback/recovery behavior is not merely best-effort where a false
     SUCCESS artifact could survive;
   - failure injection after scene/log materialization and before ref CAS
     proves no false durable SUCCESS attribution or replay-consumption state;
   - any dirty forensic state has an explicit non-success representation that
     cannot be mistaken for completed acceptance.
```

The mechanism is a future Human-authorized design decision, not authority granted by this review.

## 12. Final disposition

```text
R4R3 IBR F001 REPLACEMENT-REF / RAW-OBJECT SUBSTITUTION = ADDRESSED IN R4R4
R4R3 IBR F002 LOCAL COMMIT-ENCODING / EXTRA HEADER = ADDRESSED IN R4R4

R4R4 IBR F001 PROMISOR / LAZY-FETCH NETWORK EFFECT = BLOCKER
R4R4 IBR F002 PRE-CAS SUCCESS RECORD / UNPROVABLE ROLLBACK = BLOCKER

AK-CANON X1B R4R4 IMPLEMENTATION-BRIEF REVIEW = NOT PASS
IMPLEMENTATION AUTHORITY = NOT ESTABLISHED
X1B = OPEN
V1 AUTHORITY = NOT ESTABLISHED
```

Preserve:

```text
REVIEW FINDING != REPAIR AUTHORITY
R4R4 REVIEW NOT PASS != IMPLEMENTATION AUTHORITY
R4R4 REVIEW NOT PASS != X1B CLOSED
X1B OPEN != V1 AUTHORITY
AI PROPOSES != HUMAN DECIDES
```

## 13. STOP

No ScriptOps implementation, repair, Human decision PR/review, live positive control, canonical effect, merge, closure, V1, release, deployment or tag is authorized by this review artifact.

`STOP`
