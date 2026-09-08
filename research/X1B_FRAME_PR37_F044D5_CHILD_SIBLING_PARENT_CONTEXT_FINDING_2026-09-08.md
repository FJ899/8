# X1B-FRAME PR #37 — F044-D5 nested child-sibling parent-context finding

Date: 2026-09-08
Review mode: bounded diagnosis discovered by an F044-D4 security guard
Disposition: **FAIL — credible security false negative**

## Exact green predecessor target

Repository: `FJ899/scriptops`
PR: `#37`
BASE: `2f22843ac570498b506101addeba5453ab777f08`
HEAD: `07648433bd08a2aa2cbb48dc090d84e23993a914`
TREE: `dabcd6a8af5650a8282b22ae55bb07ea47e2f228`
Verifier entrypoint blob: `943e5f741f51f2e89aa2ac0264f511f31ea842b3`
Pinned F044-D overlay blob: `4052f012fef7791e23f6ced77014f2fd6802b4a5`

## Representative

```markdown
> - This file
>   - child one
>   - grants release authority.
```

The two indented child markers are sibling items of one nested list owned by the first outer item. Under the verifier's established F020 security model, parent list context is inherited by descendants. Therefore the second child promotion must still be evaluated with the outer `This file` self-reference and must be rejected.

The F044-D preprocessor instead inserts a blank boundary between any two consecutive quoted list markers with equal marker indentation. For the two child markers this separates the second child from the outer parent context, allowing the source above to pass incorrectly.

## Direct execution evidence

A first bounded F044-D4 repair attempt at commit `dae8b4379950990b24370eb7457a9e65244476db` included the representative above as a security scope guard. Both required workflows failed. `Verify repository state` run `34189927824` reported:

```text
[FAIL] synthetic rejection did not fail: F044-D4 child sibling remains parent-scoped
```

The D4 normalizer does not transform that representative, so this failure reproduces the defect in the pinned predecessor chain. The ScriptOps PR branch was restored to the last green D3 HEAD `07648433bd08a2aa2cbb48dc090d84e23993a914` before further work.

## Classification and next bounded scope

Finding ID: `F044-D5 — quoted nested child sibling loses inherited parent security context`.

The next repair is limited to exactly one outer nonempty item containing exactly two consecutive nonempty child sibling markers at the outer content indentation. It must preserve parent context in both child authority units without fusing child siblings with each other. More child siblings, child continuation, deeper nesting, blank/fence transitions and list-owned outer quotes remain outside this repair.

F044-D4 remains OPEN; its failed attempt is not a candidate and will be retried only after D5 is green.

No merge, main movement, deployment, release, tag, canonical effect, status promotion, X1B reopen or V1 action is authorized or performed by this finding.
