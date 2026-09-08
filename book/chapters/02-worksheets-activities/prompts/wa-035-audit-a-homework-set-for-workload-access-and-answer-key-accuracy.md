---
{
  "id": "WA-035",
  "slug": "audit-a-homework-set-for-workload-access-and-answer-key-accuracy",
  "chapter": "worksheets-activities",
  "subtopic": "homework-sets",
  "title": "Audit a homework set for workload, access and answer-key accuracy",
  "grade_bands": [
    "3-5",
    "6-8",
    "9-12"
  ],
  "subjects": [
    "Any"
  ],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 2
}
---

# WA-035 | Audit a homework set for workload, access and answer-key accuracy

## Use this when

Choose this focused tool when your immediate task is to audit a homework set for workload, access and answer-key accuracy. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [HOMEWORK_DRAFT: supply verified information; do not leave blank]
- [TIME_LIMIT: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Audit a homework set for workload, access and answer-key accuracy.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [HOMEWORK_DRAFT: supply verified information; do not leave blank]
- [TIME_LIMIT: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Check access assumptions, length and every answer. Offer a shorter essential set without hiding which learning evidence is reduced.

Output:
Return an issue table with location, evidence, severity and smallest correction; then the corrected artifact and unresolved decisions.

```

## Fictional test case

Grade 5 mathematics; equal-whole fractions; 25 minutes; paper and pencils; goal: justify 1/2=2/4. This is an intentionally incomplete input-check exercise for WA-035, not a complete example run. Identify which of HOMEWORK_DRAFT, TIME_LIMIT are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Check access assumptions, length and every answer. Offer a shorter essential set without hiding which learning evidence is reduced.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

