---
{
  "id": "AS-012",
  "slug": "audit-a-test-for-alignment-ambiguity-and-answer-key-errors",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "quizzes-and-tests",
  "title": "Audit a test for alignment, ambiguity and answer-key errors",
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

# AS-012 | Audit a test for alignment, ambiguity and answer-key errors

## Use this when

Choose this focused tool when your immediate task is to audit a test for alignment, ambiguity and answer-key errors. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [TEST: supply verified information; do not leave blank]
- [KEY: supply verified information; do not leave blank]
- [OBJECTIVES: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Audit a test for alignment, ambiguity and answer-key errors.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [TEST: supply verified information; do not leave blank]
- [KEY: supply verified information; do not leave blank]
- [OBJECTIVES: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Independently solve each item, identify ambiguous keys and check point totals. Keep the original numbering in the correction log.

Output:
Return an issue table with location, evidence, severity and smallest correction; then the corrected artifact and unresolved decisions.

```

## Fictional test case

Grade 8 mathematics; solve and justify 2x+3=11; correct answer x=4; paper responses; ten minutes. This is an intentionally incomplete input-check exercise for AS-012, not a complete example run. Identify which of TEST, KEY, OBJECTIVES are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Independently solve each item, identify ambiguous keys and check point totals. Keep the original numbering in the correction log.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

