# F038 preservation audit and bounded repair design

## Exact input binding

- repository: `FJ899/scriptops`
- PR: `#37`
- BASE: `2f22843ac570498b506101addeba5453ab777f08`
- OLD HEAD: `5d07e181c1a9d43f4bfca000962790b087b6fe15`
- OLD TREE: `bdbc73b06bb29c5b334cb2cd4bca0d49b68df63b`
- OLD verifier blob: `b29df53ab96596ac075118943b364d9b47eda6cd`
- finding: `FJ899/8 PR #343`
- Human repair authority: `FJ899/8 PR #344`

## Preservation result

F037 through F029 and all earlier frozen regressions must remain unchanged in meaning. The repair remains verifier-only relative to OLD HEAD and must preserve the frozen 12-path BASE-relative surface and one-commit replacement topology.

## CommonMark boundary being repaired

CommonMark 0.31.2 section 4.6 defines seven HTML-block kinds. Types 1 through 6 may interrupt a paragraph. Type 7 may not interrupt a paragraph.

The F038 failure mechanism is therefore bounded to the paragraph-interrupting HTML-block families 1 through 6. A valid 0-3-column type-1..6 opener must terminate the preceding ordinary paragraph before raw HTML block content is accumulated. Raw HTML block content remains security-relevant as one literal block unit rather than being reparsed as Markdown.

The bounded recognizer covers:

1. `<pre`, `<script`, `<style`, `<textarea` blocks, ending on the first line containing any corresponding type-1 end tag;
2. `<!--` comments, ending on a line containing `-->`;
3. `<?` processing instructions, ending on a line containing `?>`;
4. `<!` followed by an ASCII letter, ending on a line containing `>`;
5. `<![CDATA[`, ending on a line containing `]]>`;
6. CommonMark's fixed block-tag-name family, ending before the next blank line or at the containing block/document end.

Type 7 is deliberately not promoted into a paragraph-interrupting boundary because CommonMark explicitly forbids that interruption. This repair is not a generic HTML parser.

## Container and literal-state design

- Active HTML-block state runs before generic Markdown marker parsing so fenced-code/list/heading-looking text inside raw HTML stays literal.
- Top-level type-1..6 HTML blocks flush any open ordinary paragraph and emit their raw nonblank lines as one separate authority unit.
- Type 1 through 5 use their normative terminator and may end on the opening line; everything on that ending line remains inside the HTML block.
- Type 6 ends at the next blank line or EOF.
- A top-level HTML block reached at EOF is emitted.
- A paragraph-interrupting HTML opener at top level closes an active list path before starting the HTML block.
- A list-owned HTML block keeps the owning list-item security context; deeper descendants are closed before ownership is inherited by the nearest valid owner.
- An unclosed list-owned HTML block ends at the end of its containing item. Dedented nonblank text is reprocessed under the surviving outer structure.
- After a list-owned HTML block ends, paragraph-only lazy continuation is disabled until ownership is re-resolved.
- Explicit quoted type-1..6 HTML openers disable block-quote paragraph laziness so following unquoted text cannot be borrowed into the quote. Type 7 remains non-interrupting.

## Invalid/non-boundary controls

The repair must not manufacture boundaries from:

- four-column top-level HTML-looking text;
- escaped `\\<div>` text;
- unknown inline/custom tags such as `<x-widget>` when they are not type 1..6 starts;
- type-7 complete tags occurring inside an already-open paragraph.

These forms remain ordinary/lazy text under the existing conservative authority folding.

## Required regression coverage

Add F038 controls for the representative type-6 boundary, type-1 same-line close, comment/processing-instruction/declaration/CDATA families, type-6 EOF and blank termination, top-level HTML closing an active list, quoted HTML preventing lazy outside donation, list-owned HTML preserving self-reference, HTML payload self-promotion remaining rejected, type-6 literal suppression of Markdown-looking content, and invalid/four-column/type-7 non-boundaries.

No HTML link-reference, inline-HTML, indented-code, or parser-wide expansion is authorized by this design.
