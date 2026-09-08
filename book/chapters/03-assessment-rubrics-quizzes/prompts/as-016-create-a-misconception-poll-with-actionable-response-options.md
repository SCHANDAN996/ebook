---
{
  "id": "AS-016",
  "slug": "create-a-misconception-poll-with-actionable-response-options",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "formative-checks-and-exit-tickets",
  "title": "Create a misconception poll with actionable response options",
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

# AS-016 | Create a misconception poll with actionable response options

## Use this when

Choose this focused tool when your immediate task is to create a misconception poll with actionable response options. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [MISCONCEPTION_OPTIONS: supply verified information; do not leave blank]
- [RESPONSE_CHANNEL: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Create a misconception poll with actionable response options.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [MISCONCEPTION_OPTIONS: supply verified information; do not leave blank]
- [RESPONSE_CHANNEL: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Create a poll with one conceptual distinction per option. Follow uncertain patterns with an explanation request, not a learner diagnosis.

Output:
Return the named artifact with all questions, directions, examples or text needed for the task; put teacher keys and notes separately from student/family-facing text.

```

## Fictional test case

Grade 8 mathematics; solve and justify 2x+3=11; correct answer x=4; paper responses; ten minutes. This is an intentionally incomplete input-check exercise for AS-016, not a complete example run. Identify which of MISCONCEPTION_OPTIONS, RESPONSE_CHANNEL are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Create a poll with one conceptual distinction per option. Follow uncertain patterns with an explanation request, not a learner diagnosis.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

