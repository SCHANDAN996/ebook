---
{
  "id": "RC-017",
  "slug": "audit-a-report-comment-using-a-sentence-by-sentence-fact-trace",
  "chapter": "report-card-comments",
  "subtopic": "strengths-and-next-steps",
  "title": "Audit a report comment using a sentence-by-sentence fact trace",
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

# RC-017 | Audit a report comment using a sentence-by-sentence fact trace

## Use this when

Choose this focused tool when your immediate task is to audit a report comment using a sentence-by-sentence fact trace. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [COMMENT: supply verified information; do not leave blank]
- [SOURCE_RECORD: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Audit a report comment using a sentence-by-sentence fact trace.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [COMMENT: supply verified information; do not leave blank]
- [SOURCE_RECORD: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Return a sentence-by-sentence fact trace, unsupported claims and corrected draft. Verify that no evidence from another learner appears.

Output:
Return an issue table with location, evidence, severity and smallest correction; then the corrected artifact and unresolved decisions.

```

## Fictional test case

Grade 6 mathematics; fictional record: three of four equivalent-fraction items correct; one explanation missing; 70-word limit; no identity supplied. This is an intentionally incomplete input-check exercise for RC-017, not a complete example run. Identify which of COMMENT, SOURCE_RECORD are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Return a sentence-by-sentence fact trace, unsupported claims and corrected draft. Verify that no evidence from another learner appears.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

