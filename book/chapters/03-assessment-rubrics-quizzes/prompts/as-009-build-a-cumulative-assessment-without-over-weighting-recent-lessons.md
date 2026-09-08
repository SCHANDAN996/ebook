---
{
  "id": "AS-009",
  "slug": "build-a-cumulative-assessment-without-over-weighting-recent-lessons",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "quizzes-and-tests",
  "title": "Build a cumulative assessment without over-weighting recent lessons",
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

# AS-009 | Build a cumulative assessment without over-weighting recent lessons

## Use this when

Choose this focused tool when your immediate task is to build a cumulative assessment without over-weighting recent lessons. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [TAUGHT_UNITS: supply verified information; do not leave blank]
- [COVERAGE_WEIGHTS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Build a cumulative assessment without over-weighting recent lessons.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [TAUGHT_UNITS: supply verified information; do not leave blank]
- [COVERAGE_WEIGHTS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Sample across the taught period according to explicit weights. Flag missing coverage rather than overusing recently taught material.

Output:
Return the named artifact with all questions, directions, examples or text needed for the task; put teacher keys and notes separately from student/family-facing text.

```

## Fictional test case

Grade 8 mathematics; solve and justify 2x+3=11; correct answer x=4; paper responses; ten minutes. This is an intentionally incomplete input-check exercise for AS-009, not a complete example run. Identify which of TAUGHT_UNITS, COVERAGE_WEIGHTS are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Sample across the taught period according to explicit weights. Flag missing coverage rather than overusing recently taught material.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

