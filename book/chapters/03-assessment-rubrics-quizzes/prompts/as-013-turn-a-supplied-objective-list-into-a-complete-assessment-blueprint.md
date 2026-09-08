---
{
  "id": "AS-013",
  "slug": "turn-a-supplied-objective-list-into-a-complete-assessment-blueprint",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "quizzes-and-tests",
  "title": "Turn a supplied objective list into a complete assessment blueprint",
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

# AS-013 | Turn a supplied objective list into a complete assessment blueprint

## Use this when

Choose this focused tool when your immediate task is to turn a supplied objective list into a complete assessment blueprint. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [OBJECTIVE_LIST: supply verified information; do not leave blank]
- [WEIGHTS: supply verified information; do not leave blank]
- [ITEM_COUNT: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Turn a supplied objective list into a complete assessment blueprint.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [OBJECTIVE_LIST: supply verified information; do not leave blank]
- [WEIGHTS: supply verified information; do not leave blank]
- [ITEM_COUNT: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Return a blueprint mapping every item slot to objective, demand, format and points. Flag objectives with no evidence.

Output:
Return the named artifact with all questions, directions, examples or text needed for the task; put teacher keys and notes separately from student/family-facing text.

```

## Fictional test case

Grade 8 mathematics; solve and justify 2x+3=11; correct answer x=4; paper responses; ten minutes. This is an intentionally incomplete input-check exercise for AS-013, not a complete example run. Identify which of OBJECTIVE_LIST, WEIGHTS, ITEM_COUNT are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Return a blueprint mapping every item slot to objective, demand, format and points. Flag objectives with no evidence.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

