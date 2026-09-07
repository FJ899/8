# P9-R4 Stage 1 — Check/Use Target-Instance Race Finding

Status: **OPEN / BLOCKING / REPAIR NOT YET APPLIED**

## Frozen review input

- repository: `FJ899/8`
- P9-R3 green HEAD: `673461f6aaadf1ff2ada5c3cb1902c151f8433bf`
- P9-R3 green TREE: `2d2d38bb6c5c10ca359977ee852d28da4e725b43`
- P9-R3 green workflow run: `34153650811`
- finding: `P9-R3-RV-F003`
- origin: **NEWLY REVEALED DURING BLIND POST-REPAIR CONTINUATION**

## Finding

P9-R3 revalidates the durable historical target binding immediately before delegating to each domain kernel. That closes substitution that is already present when `EffectAdapter.execute()` begins, but the checked target and the target actually used by the effect primitive are still separate resolutions.

For G3 the sequence is:

`load historical T1 binding -> stat current kernel.target_db as T1 -> compare -> kernel.execute_put_if_version_admission() -> consume admission -> _target_connect() using current kernel.target_db -> mutate`.

For G4 the sequence is analogous: the adapter stats `kernel.git_repo.repo`, then `Kernel.execute_git_admission()` later performs multiple Git commands through the current `git_repo` path.

For HTTP CAS the adapter performs an authenticated provider `/identity` read, then the kernel separately issues the effecting `/cas` request to its configured endpoint.

Therefore a target-route change after the successful instance check but before the domain effect boundary can still separate the checked target from the used target:

`historical T1 -> execution check observes T1 -> route switches to T2 -> domain primitive uses T2`.

This is deeper than `P9-R2-RV-F002`, which covered a target already changed before execution-time validation. `P9-R3-RV-F003` asks whether the validated target and effect target are the same bound object/route, rather than two time-separated resolutions.

As with the preceding target-provenance findings, this is not classified here as an untrusted-Executor CAI-001 bypass: direct mutation of trusted adapter/kernel target composition is inside the frozen TCB. It blocks the stronger reference-runtime claim that historical target binding is enforced through, rather than merely before, the protected effect boundary.

## Required counterexample

At minimum on G3:

1. admit through the trusted adapter on T1 so a durable historical T1 binding exists;
2. begin adapter execution while T1 is still current;
3. after the adapter derives a matching T1 execution binding but before the domain kernel opens its target connection, switch the kernel target route to distinct T2 with compatible state;
4. execute the exact historical admission;
5. the frozen P9-R3 candidate is vulnerable if T2 receives the mutation.

Expected secure behavior:

`validated T1 MUST be the same target instance used by the effect primitive`.

The Stage-1 workflow is intentionally expected-red. No repair is included in this stage.

## Subsequent repair boundary

Any repair must remain in the dependency closure of `P9-R3-RV-F003`:

- this durable finding and exact reproducer;
- a target/route binding that remains stable from validation through the effect primitive;
- domain-correct G3/G4/HTTP implementations;
- minimum common seam only if justified by all domains;
- tests and evidence directly required for the repair;
- broad regressions as verification only.

No speculative architecture cleanup, generic Broker work, unrelated evidence redesign, merge/main movement, deploy/release/tag, canonical/status promotion, product/API freeze, or Human acceptance inference is authorized.
