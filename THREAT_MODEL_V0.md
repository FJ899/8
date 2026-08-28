# Agency Kernel v0 — Threat Model

Status: **FROZEN**

## 1. Adversary controls

The v0 adversary may control:

- `ActionRequest` contents;
- Executor control flow;
- request timing;
- replay attempts;
- malformed inputs;
- Executor crashes;
- Executor-owned workspace;
- candidate changes proposed by the Executor;
- false claims made by the Executor.

The adversary is allowed to behave deliberately and deterministically against the system.

## 2. Adversary does not control

The v0 adversary does not control:

- trusted Kernel/Broker process;
- Broker OS identity;
- authority/control ledger implementation;
- supported effect-adapter implementation;
- observer implementation;
- host isolation mechanism;
- external runner infrastructure.

## 3. Adversary does not possess

The untrusted Executor must not possess:

- target write credentials;
- target write mount/path;
- ledger write access;
- Broker credentials;
- an alternate writable API/path to the modeled target.

## 4. Trusted Computing Base

The experimental TCB includes:

- Kernel/Broker implementation;
- authority/control ledger;
- supported effect adapter;
- OS/container capability-isolation mechanism;
- observer implementation;
- controlled workflow/container topology used for accepted evidence runs.

For GitHub Actions evidence runs, the GitHub-hosted VM, host kernel, container runtime, and GitHub infrastructure are trusted external substrate and are recorded as execution-instance properties rather than claimed as immutable candidate properties.

## 5. Out of scope v0

The following are outside the v0 adversary model:

- Broker compromise;
- host/OS compromise;
- credential theft from the Broker;
- malicious observer;
- malicious SQLite implementation;
- deliberately malicious trusted effect adapter;
- compromise of GitHub infrastructure or runner host.

These elements may still be tested for accidental unsoundness where useful, but v0 does not claim to defend against their deliberate compromise.

## 6. Capability-boundary invariant

There must exist no writable path:

`UNTRUSTED EXECUTOR → MODELED TARGET`

except through:

`authenticated IPC → trusted Kernel/Broker → valid OperationAdmission → effect-aware primitive → target`

Process separation alone is insufficient. The experiment must test actual capability separation.

## 7. Identity invariant

Declared principal identity is not authoritative.

`DECLARED PRINCIPAL ≠ AUTHENTICATED PRINCIPAL`

Principal identity used for authority evaluation must be derived from a trusted authenticated channel/session, not from request content.

## 8. Claim B scope

The v0 Claim B statement is deliberately limited:

> Under the preregistered capability topology, executed on the recorded external substrate instance, no tested hostile-executor trace obtained a writable path to the modeled target except through a valid Broker admission.

This does not claim that Docker, GitHub, the host OS, or all possible Executor escapes are proven secure.
