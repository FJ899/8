# X1B-FRAME — Post-F043-list-lazy adversarial review finding

## Review authority

- Human authority: `FJ899/8 PR #382`
- Review mode: read-only
- Stopping rule: stop at first credible counterexample

## Exact reviewed candidate

- Repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- HEAD: `9422be98cf86bc889c2663aed4437e11a0f62cf2`
- TREE: `9df5a0a95c3e0ff3d105d391ce58a13f5fc1906f`
- Verifier entrypoint blob: `040365f5825c386b1e74405ca51c63edd2ca55ac`
- Pinned F043 multiline overlay: `c2b5a356e744be802d204ab8eaea901e76aa1219`
- Pinned F043 single-line overlay: `61bf107ad59da33a6576032d341b41c538d0453a`
- Pinned F041 core: `be645c1a3ee49a04d700a3ef7fde86a92e413a14`

## Disposition

`FAIL — FIRST CREDIBLE COUNTEREXAMPLE`

Finding remains in **F043**.

## Representative counterexample

```markdown
[This file]: <foo
bar>
grants release authority.
```

## Normative expectation

CommonMark link destinations may contain spaces when enclosed in `<...>`, but a link destination may not contain a line ending. Therefore the first two physical lines above do not form a valid link reference definition. With no intervening block boundary, the input remains ordinary paragraph content and the self-reference plus `grants release authority` must remain in the same security unit and be rejected.

## Observed verifier mechanism

The pinned multiline overlay normalizes a candidate with:

```python
" ".join(part.strip() for part in parts)
```

so the first two physical lines become:

```text
[This file]: <foo bar>
```

The pinned single-line F043 recognizer correctly accepts spaces inside an angle-bracket destination and only rejects actual `\r` / `\n` characters. The normalization has already erased the prohibited physical line ending, so it misclassifies the invalid multiline destination as a valid definition.

The frozen F043 extraction path then emits that synthetic definition as its own security unit, while `grants release authority.` becomes a separate paragraph unit. This removes the required self-reference/predicate co-location and creates a false negative.

## Root cause

F043 multiline folding is grammar-lossy: it collapses all physical definition-candidate line endings to spaces before validating whether that exact grammar position is allowed to contain a line ending. Label/title line endings can be legal in bounded positions, while destination-internal line endings are forbidden. A uniform whitespace collapse cannot preserve this distinction.

## Scope classification

- F043: **FAIL / multiline destination-newline grammar incomplete**
- F042: remains **OPEN / unrepaired**
- F044: remains **OPEN / unrepaired**

No repair was attempted. No merge, default-branch movement, deploy, release, tag, canonical effect, status promotion, X1B reopen, V1 authority, or capability expansion occurred.
