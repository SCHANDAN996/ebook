# Phase 2 design prototype

Status: prototype v1, not approved for the final edition.

## Direction

The book should feel like a calm, capable teacher's desk: editorial rather than
childish, warm rather than corporate, and easy to scan while planning. Navy carries
authority, teal marks action, coral highlights cautions and gold is reserved for
progress and chapter identity. Warm paper replaces a harsh white background.

## Prototype pages

1. Cover with a restrained abstract planning-card illustration.
2. Chapter opener with scope, chapter promise and subtopic map.
3. Prompt page with metadata, teacher inputs, copy-ready text and verification rail.
4. Sample-output page visibly marked as an illustrative draft.
5. Workflow page showing verified output hand-offs and a human review gate.

## Typography

The intended release families remain Source Serif 4, Source Sans 3 and JetBrains Mono.
The prototype uses bundled DejaVu equivalents so it builds offline. Release fonts will
be downloaded only with their licence files and embedded in the final PDF.

## Copy interaction

Prompt text in the PDF is selectable. `COPY ONLINE` is a normal PDF link to the
companion page, never embedded clipboard JavaScript. The companion HTML provides the
clipboard action with keyboard focus, visible success feedback and a manual-selection
fallback when browser permission is unavailable.

## Approval questions

- Is the editorial style premium enough without looking like a children's workbook?
- Is the prompt text large enough for laptop and tablet reading?
- Should chapter colours vary, or should every chapter remain teal?
- Is the sample-output warning prominent without distracting from the example?

