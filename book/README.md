# Master book source

This directory is the source of truth for the full Teacher AI Toolkit. The final
PDF and companion HTML will be generated from these files only after the content,
design and review gates pass.

## Fixed Phase 1 decisions

- Audience: working K-12 teachers.
- Language: clear international English; avoid unexplained regional jargon.
- Master edition: 300 standalone prompts plus 12 multi-step workflows.
- Page target: US Letter, with an A4 export supported by the same source.
- One prompt per Markdown file, grouped by chapter.
- Missing facts remain visible placeholders; models must not invent people, dates,
  standards, evidence or availability.
- Full sample outputs are limited to 60 selected prompts to keep the book usable.
- Every workflow receives a reviewed end-to-end example.
- The PDF contains selectable text and links. Reliable clipboard buttons live in
  the companion HTML because PDF JavaScript is not portable across viewers.
- `approved` means a qualified human reviewed the current content fingerprint.

## Production gates

1. Blueprint passes `python toolkit/run.py book-check`.
2. The complete 300-prompt source passes structural checks and editorial review.
3. Design prototypes for cover, chapter opener, prompt, example and workflow pages
   are approved before bulk layout work.
4. Remaining content is written chapter by chapter and frozen after review.
5. Chapter illustrations and licensed fonts are added with provenance records.
6. Companion HTML is built with a real Copy Prompt button.
7. The master PDF is generated once content is complete, then rendered page by page
   for visual QA before release.

## Phase 2 prototype

Run `python toolkit/run.py design-preview` to build the five-page layout prototype and
its copy-enabled companion HTML. This is a design approval artifact, not the master
book. See [`design/design-spec.md`](design/design-spec.md) for the decisions to review.

Generated files never replace the Markdown sources. Do not put API keys, student
records or unlicensed source material anywhere in this public repository.

## Full content draft

Run `python toolkit/build_full_content.py` to deterministically rebuild the complete
300-prompt, 12-workflow source, then `python toolkit/run.py content-check`. There is no
separate 30-prompt beta gate. Every item remains `draft` until final editorial review.
The same command also writes ten review-friendly compiled chapter files under
`book/manuscript/chapters/`; these mirror the individual source files and are convenient
for GitHub review, export and final layout.
