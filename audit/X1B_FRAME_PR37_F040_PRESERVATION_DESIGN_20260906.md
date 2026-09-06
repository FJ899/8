# F040 preservation audit and bounded repair design

Binding: ScriptOps PR #37; BASE `2f22843ac570498b506101addeba5453ab777f08`; OLD HEAD `e8e745b5787f7f98c5e2df3fd03934acee332413`; OLD TREE `6363566d5b36f4669e234f31cd4660a1687c0597`; OLD verifier `73504fe6897a5b6a038da39b14478a37aa36bbc7`; finding PR #355; Human repair authority PR #356.

The repair preserves F039-F029 and all earlier frozen regressions. It builds on F027, which already records that post-marker whitespace greater than four columns can start indented code inside a list item while item ownership uses marker width plus one.

Bounded design:
- add explicit indented-code leaf state only in `scripts/verify_repository.py`;
- top-level code starts at four-plus leading columns only when no ordinary paragraph is open; it cannot interrupt a paragraph;
- active code is literal, survives blank lines, ends on the first nonblank dedent, reprocesses that line, and closes at EOF;
- top-level code is a separate authority unit, while list-owned code retains its list-item context;
- list markers that begin with post-marker whitespace greater than four columns activate code state for the new item;
- after a list leaf is already closed, a line at least four columns beyond an owning item content indent may start list-owned code, with deeper descendants closed as needed;
- dedent from list-owned code ends code state and forces ownership re-resolution instead of paragraph lazy continuation;
- explicit block-quote content that begins with four-plus indentation is not a paragraph and cannot enable lazy unmarked quote continuation;
- preserve controls: three columns are not code, code does not interrupt open paragraphs, and deep indentation inside an already-open list paragraph without a leaf boundary remains existing paragraph continuation;
- add F040 regressions for representative top-level separation, literal payload, EOF/blank handling, paragraph non-interruption, quote behavior, initial/later list-owned code, same-item continuation, and dedent-outside separation.

Excluded: link-reference-definition work, generic Markdown parser expansion, runtime/status changes, or files other than the verifier.

Completion still requires verifier-only OLD->NEW, one replacement commit over frozen BASE, same 12 BASE-relative paths, full local verifier including F040 and prior regressions, both workflows on exact repaired HEAD, durable completion evidence, then STOP before independent review.
