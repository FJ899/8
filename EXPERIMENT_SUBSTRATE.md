# Agency Kernel v0 — Experiment Substrate

Status: **FROZEN**

## 1. Role of GitHub Actions

`GitHub Actions = EXECUTION + EVIDENCE SUBSTRATE`

`GitHub Actions ≠ VERIFIER`

A successful workflow means only that the workflow reached its configured successful completion condition.

`workflow green ≠ Gate PASS`

## 2. Experiment Candidate vs Execution Instance

`EXPERIMENT CANDIDATE ≠ EXECUTION INSTANCE`

### Experiment Candidate

The candidate is the controlled, preregistered material that exists before a run:

- repository HEAD/tree;
- workflow definitions;
- container definitions;
- dependency locks;
- external GitHub Actions pinned to immutable commit SHAs;
- container images used in accepted evidence runs pinned to immutable digests;
- Gate Contract;
- attack definitions;
- evidence-capture definition.

Controlled execution components used in an accepted evidence run **MUST be immutable/pinned**.

### Execution Instance

The execution instance records what actually executed:

- candidate identity;
- GitHub Actions run ID;
- observed runner image/OS information;
- host/kernel/runtime information available to the job;
- container runtime information;
- actual container image digests;
- UID/GID;
- relevant effective capabilities;
- mount topology;
- network topology;
- commands actually executed;
- attack traces;
- exit codes;
- stdout/stderr;
- raw observations;
- artifact hashes.

External substrate properties that cannot be immutably pinned must be observed and recorded, not assumed stable.

## 3. Controlled vs external substrate

### Controlled execution components

For accepted evidence runs, the following must be immutable/pinned:

- repository candidate;
- workflow definition;
- external actions;
- controlled container images;
- dependency lock inputs where the Gate depends on them.

### External substrate

Examples:

- GitHub-hosted VM;
- host kernel;
- host container runtime;
- GitHub runner infrastructure.

These are trusted external experimental substrate for v0. They are recorded per Execution Instance.

## 4. Claim B isolation

Copilot firewall is not Claim B enforcement.

Claim B isolation must come from the preregistered capability topology controlled by the experiment, e.g.:

- Executor has no target mount;
- Executor has no ledger mount;
- Executor has no target credentials;
- Executor has no Broker credentials;
- Executor has no alternative write API;
- Executor external network is denied by the experiment harness where required;
- Executor has only the intended authenticated Broker IPC path.

## 5. Candidate mutation rule

A change to any of the following after candidate freeze creates a new Experiment Candidate:

- workflow;
- topology;
- container definition;
- controlled image digest;
- attack definition;
- evidence-capture definition;
- Gate implementation code.

## 6. Evidence-run acceptance

An accepted evidence run must permit the auditor to reconstruct:

1. what was preregistered to happen;
2. what exact candidate was executed;
3. on what observed substrate instance;
4. what topology/capabilities were actually present;
5. what attack actually ran;
6. what the raw outcome was.

The execution substrate does not interpret the evidence on behalf of the Gate acceptance authority.
