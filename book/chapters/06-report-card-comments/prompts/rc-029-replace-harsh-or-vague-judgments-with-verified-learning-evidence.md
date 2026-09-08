---
{
  "id": "RC-029",
  "slug": "replace-harsh-or-vague-judgments-with-verified-learning-evidence",
  "chapter": "report-card-comments",
  "subtopic": "tone-and-rewriting",
  "title": "Replace harsh or vague judgments with verified learning evidence",
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

# RC-029 | Replace harsh or vague judgments with verified learning evidence

## Use this when

Choose this focused tool when your immediate task is to replace harsh or vague judgments with verified learning evidence. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [HARSH_COMMENT: supply verified information; do not leave blank]
- [OBSERVATIONS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Replace harsh or vague judgments with verified learning evidence.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [HARSH_COMMENT: supply verified information; do not leave blank]
- [OBSERVATIONS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Remove judgments about character or intent. Preserve the concern using supported observations and flag gaps instead of guessing.

Output:
Return the named artifact with all questions, directions, examples or text needed for the task; put teacher keys and notes separately from student/family-facing text.

```

## Fictional test case

Grade 6 mathematics; fictional record: three of four equivalent-fraction items correct; one explanation missing; 70-word limit; no identity supplied. This is an intentionally incomplete input-check exercise for RC-029, not a complete example run. Identify which of HARSH_COMMENT, OBSERVATIONS are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Remove judgments about character or intent. Preserve the concern using supported observations and flag gaps instead of guessing.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

