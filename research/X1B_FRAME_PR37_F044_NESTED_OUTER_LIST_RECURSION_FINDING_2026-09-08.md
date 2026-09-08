# X1B-FRAME — PR #37 F044 nested outer-list recursion finding — 2026-09-08

## Review authority and exact target

Human authorization in chat granted exactly one read-only F044 nested-outer-list-recursion probe on the frozen implementation candidate, with a depth=1 control and an otherwise identical depth=2 probe, no repair, and STOP on first FAIL or PASS.

Exact implementation target:

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `f286a6351a20037de7d9948f4f021dac7ed22547`
- TREE: `2ab1f67e42c0b995fc52c64c06536dd933eb42f5`
- verifier entrypoint blob: `6e7981d64f06fa3638844e4e2f423afabab77faa`

The previously validated position axis remains frozen as:

- `POSITION-DEPENDENCE AXIS = CLOSED`
- `F044 FAMILY = NOT CLOSED BY THIS RESULT`

No implementation mutation was performed during this probe.

## Frozen semantic variables

The probe changes only outer-list container depth.

Frozen across control and probe:

- sibling position: constant
- sibling cardinality: constant
- continuation run length: exactly 1
- quoted-parent cardinality: exactly 1
- no block transition
- no blank/fence/HTML transition
- same self-reference placement
- same promotion placement

Therefore:

`ONLY DELTA = +1 OUTER-LIST CONTAINER DEPTH`

## Control — depth = 1

```markdown
- neutral outer parent
  > - neutral quoted parent
  >   - This file
  >     ordinary continuation
  >   - grants release authority.
```

This is the existing F044-D17 list-owned outer-quote sibling shape. The frozen final verification run `34273100958` explicitly reports:

`[PASS] F044-D17 list-owned outer-quote sibling regression`

The intended classification is therefore GREEN/inert: the self-reference in one quoted child must not leak into its same-level sibling's promotion text.

## Probe — depth = 2

```markdown
- neutral outer parent
  - neutral nested outer
    > - neutral quoted parent
    >   - This file
    >     ordinary continuation
    >   - grants release authority.
```

This preserves the same inner semantic shape and adds exactly one outer list container.

## Reproduction and root mechanism

The current position-generic entrypoint is intentionally limited to the existing source-column-zero outer-list-owned quote family and states that `nested outer lists` and further recursion remain outside its repair boundary.

The inherited list-owned chain also leaves this dimension open. F044-D18 explicitly leaves `deeper nesting`, `nested outer lists`, and other list-owned quote recursion outside; F044-D29 repeats that `deeper nesting`, `nested outer lists`, and further list-owned quote recursion remain outside.

For the depth=2 source:

1. the source-column-zero F044 list-owned splitters do not match the nested outer list shape;
2. the core list parser opens one list frame for `- neutral outer parent`;
3. it opens a nested list frame for `  - neutral nested outer`;
4. the quote lines at the nested outer content indentation are owned by that deepest surviving list frame;
5. at EOF, `emit_active_list_path()` emits all parts of all active list frames as one authority unit;
6. `layer_b_self_promotion_claim()` then sees both the self-reference term `THIS FILE` and promotion term `GRANTS` inside that fused unit and rejects it as forbidden self-promotion.

The resulting semantic fusion is equivalent to one security unit containing both:

- child A: `This file` + ordinary continuation
- child B: `grants release authority.`

although those are distinct same-level quoted child list items under CommonMark list ownership.

This is the same false-positive class that D17 prevents at depth=1, but it reappears when the identical shape is moved one level deeper in the outer-list container stack.

## Disposition

`F044-NESTED-OUTER-LIST-RECURSION = FAIL / REPRODUCIBLE`

Classification:

- independent F044 dimension
- container-stack-depth / recursive ownership-propagation defect
- not a reopening of the closed sibling-position axis
- not a D41-style positional finding

The evidence strongly supports:

`DEPTH=1 = GREEN`

`DEPTH=2 = FALSE-POSITIVE REJECTION`

with all other semantic variables frozen.

## STOP

No repair is authorized by this probe.

No merge, movement of `main`, deploy, release, tag, canonical effect, status promotion, X1B reopen, or V1 action is authorized or performed.

Next action requires a separate scope decision / Human authorization for any repair or broader recursion-depth validation.
