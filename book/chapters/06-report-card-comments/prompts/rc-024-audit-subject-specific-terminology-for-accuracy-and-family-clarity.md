---
{
  "id": "RC-024",
  "slug": "audit-subject-specific-terminology-for-accuracy-and-family-clarity",
  "chapter": "report-card-comments",
  "subtopic": "subject-specific-comments",
  "title": "Audit subject-specific terminology for accuracy and family clarity",
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

# RC-024 | Audit subject-specific terminology for accuracy and family clarity

## Use this when

Choose this focused tool when your immediate task is to audit subject-specific terminology for accuracy and family clarity. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [SUBJECT_COMMENT: supply verified information; do not leave blank]
- [APPROVED_TERMS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Audit subject-specific terminology for accuracy and family clarity.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [SUBJECT_COMMENT: supply verified information; do not leave blank]
- [APPROVED_TERMS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Check technical correctness and family readability. Define essential terminology instead of substituting misleading simplifications.

Output:
Return an issue table with location, evidence, severity and smallest correction; then the corrected artifact and unresolved decisions.

```

## Fictional test case

Grade 6 mathematics; fictional record: three of four equivalent-fraction items correct; one explanation missing; 70-word limit; no identity supplied. This is an intentionally incomplete input-check exercise for RC-024, not a complete example run. Identify which of SUBJECT_COMMENT, APPROVED_TERMS are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Check technical correctness and family readability. Define essential terminology instead of substituting misleading simplifications.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

