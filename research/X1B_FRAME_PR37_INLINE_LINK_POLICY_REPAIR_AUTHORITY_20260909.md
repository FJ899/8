# X1B-FRAME PR37 bounded inline-link policy repair authority

Human authorization recorded in-session on 2026-09-09.

Frozen ScriptOps predecessor:
- HEAD `a415c874038dbba8fa93cfead0b673e691d02971`
- TREE `ee118750a1ee753a26ecdb10bcc97de00ad86f1c`
- verifier blob `71404ab4921e2abc4887487636f83717bec7ffce`

Finding evidence: `FJ899/8 PR #548`, closed without merge.

Authorized pipeline only:

`RAW MARKDOWN -> existing block/ownership parsing -> extracted authority unit -> bounded inline-Markdown inline-link visible-text canonicalization -> existing inline-HTML canonicalization -> existing character-reference decoding -> existing self-promotion matcher`

Authorized scope:
- ordinary inline Markdown link syntax only;
- preserve visible link label as policy semantic text;
- omit invisible link destination/title from policy representation;
- canonicalization only after authority-unit extraction;
- exact failing reproduction plus a small bounded structural alternate set proving mechanism rather than one-URL patching;
- preserve prior inline-HTML and character-reference canonicalization;
- structural invariance;
- inherited corpus, Verify/Smoke, full known-regression replay;
- then STOP.

Not authorized:
- generic Markdown rendering-engine rewrite;
- image semantics;
- reference-link overhaul;
- autolink overhaul;
- raw-Markdown preprocessing;
- block/ownership/lifecycle changes;
- interaction matrix;
- P0-P9;
- merge/main/deploy/release/tag/canonical/status promotion.

Implementation constraint: do not implement this as a regex that merely removes `(url)`. The bounded parser must respect inline-link structure sufficiently to avoid silently misreading nested brackets, escapes, optional titles, or malformed input. Any need to broaden beyond this class is a STOP condition.