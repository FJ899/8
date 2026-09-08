# F044 nested outer-list recursion depth=3 finding

## Authority and exact target

Human-authorized exactly one read-only adjacent probe comparing repaired depth=2 against otherwise identical depth=3 on frozen `FJ899/scriptops PR #37`.

- HEAD: `8589fdbf49ecc62e9df8097fedb06b6bb0b7c222`
- TREE: `e3c94616e3971dbdf6aea9c68f5b971e420d4caf`
- verifier entrypoint blob: `98ef815bd246d600a64de3f379ebd0d7483aa21d`
- control: repaired depth=2 shape from the current verifier
- probe: identical semantic shape with exactly one additional outer-list container
- no repair and no ScriptOps implementation mutation were authorized

## Control

Depth=2 is the current repaired GREEN control and is explicitly validated by final Verify run `34274551978` as:

`[PASS] F044 nested outer-list depth=2 finding repaired structurally`

## Probe

The depth=3 probe uses the same structural oracle and the same child/sibling semantics as depth=2. The only delta is one additional outer-list container:

```markdown
- neutral outer parent
  - neutral nested outer
    - further nested outer
      > - neutral quoted parent
      >   - This file
      >     ordinary continuation
      >   - grants release authority.
```

## Reproduction on the frozen verifier path

The current depth=2 overlay explicitly requires this `further_nested` source to remain unchanged, proving the bounded repair does not normalize depth=3. Its predecessor position-generic overlay also explicitly leaves nested outer lists and further recursion outside scope.

The unchanged source therefore reaches the frozen core list-frame parser. The three outer list items establish three active list frames. The quote at the innermost content indentation is owned by the deepest frame, and all quoted lines are appended to that deepest frame. At end of input, `emit_active_list_path()` flattens the parts of every active frame into one authority unit.

That resulting unit contains both the self-reference `This file` and the promotion predicate `grants release authority.`. `layer_b_self_promotion_claim()` therefore classifies the fused unit as forbidden self-promotion even though the two quoted sibling items are semantically separate.

This is the same recursive container-boundary collapse mechanism seen at the prior depth transition; sibling position/cardinality, continuation run length, quoted-parent cardinality, block-transition state, and promotion placement are unchanged.

## Disposition

`F044 NESTED OUTER-LIST depth=2 -> depth=3 = FAIL / REPRODUCIBLE`

`ONLY DELTA = +1 OUTER-LIST CONTAINER DEPTH`

`RECURSION-DEPTH DEPENDENCE = NOW SUPPORTED BY TWO SUCCESSIVE TRANSITIONS, BUT NOT YET PROVEN CLOSED`

`POSITION-DEPENDENCE AXIS = CLOSED`

`F044 FAMILY = NOT CLOSED`

No repair, merge, ScriptOps main movement, deploy, release, tag, canonical effect, status promotion, X1B reopen, or V1 action was performed. STOP before any depth-generic repair or broader recursion sweep.
