Fresh independent final review harness for ScriptOps PR #37 exact frozen candidate.

Target:
- HEAD 2fe2867eec5a5e8e0efb71d9b41f729cd1170fa8
- TREE a1bdf5fe152f5a62151364a5d57d335b8b84a05c
- verifier 60d050b76673e2aa27bd778a8765fcd65b8b9c02

Mode: read-only, final-state first, not replay-first. Stop at first credible new counterexample or PASS.

First independent risk inspected: policy-semantic visibility across inline HTML markup inside an ordinary Markdown paragraph. Control uses literal visible text; test wraps only `file` in a valid inline `<span>` while preserving the same visible text.
