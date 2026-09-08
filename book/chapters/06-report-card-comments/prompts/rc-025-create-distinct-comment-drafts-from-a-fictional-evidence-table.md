---
{
  "id": "RC-025",
  "slug": "create-distinct-comment-drafts-from-a-fictional-evidence-table",
  "chapter": "report-card-comments",
  "subtopic": "bulk-drafts-from-fictional-evidence",
  "title": "Create distinct comment drafts from a fictional evidence table",
  "grade_bands": [
    "3-5",
    "6-8",
    "9-12"
  ],
  "subjects": [
    "Any"
  ],
  "sensitivity": "sensitive",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 2
}
---

# RC-025 | Create distinct comment drafts from a fictional evidence table

## Use this when

Choose this focused tool when your immediate task is to create distinct comment drafts from a fictional evidence table. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [SYNTHETIC_EVIDENCE_TABLE: supply verified information; do not leave blank]
- [LENGTH_LIMIT: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Create distinct comment drafts from a fictional evidence table.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [SYNTHETIC_EVIDENCE_TABLE: supply verified information; do not leave blank]
- [LENGTH_LIMIT: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Process each fictional row independently and return row IDs with fact traces. Include a deliberately sparse row to test restraint.

Output:
Return the named artifact with all questions, directions, examples or text needed for the task; put teacher keys and notes separately from student/family-facing text.

```

## Fictional test case

Grade 6 mathematics; fictional record: three of four equivalent-fraction items correct; one explanation missing; 70-word limit; no identity supplied. This is an intentionally incomplete input-check exercise for RC-025, not a complete example run. Identify which of SYNTHETIC_EVIDENCE_TABLE, LENGTH_LIMIT are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Process each fictional row independently and return row IDs with fact traces. Include a deliberately sparse row to test restraint.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

