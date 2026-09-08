---
{
  "id": "AS-010",
  "slug": "adapt-an-assessment-for-a-shorter-testing-period",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "quizzes-and-tests",
  "title": "Adapt an assessment for a shorter testing period",
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

# AS-010 | Adapt an assessment for a shorter testing period

## Use this when

Choose this focused tool when your immediate task is to adapt an assessment for a shorter testing period. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [ORIGINAL_TEST: supply verified information; do not leave blank]
- [NEW_TIME_LIMIT: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Adapt an assessment for a shorter testing period.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [ORIGINAL_TEST: supply verified information; do not leave blank]
- [NEW_TIME_LIMIT: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Remove redundant items while preserving essential coverage. State the resulting loss of precision instead of claiming unchanged reliability.

Output:
Return the named artifact with all questions, directions, examples or text needed for the task; put teacher keys and notes separately from student/family-facing text.

```

## Fictional test case

Grade 8 mathematics; solve and justify 2x+3=11; correct answer x=4; paper responses; ten minutes. This is an intentionally incomplete input-check exercise for AS-010, not a complete example run. Identify which of ORIGINAL_TEST, NEW_TIME_LIMIT are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Remove redundant items while preserving essential coverage. State the resulting loss of precision instead of claiming unchanged reliability.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

