---
{
  "id": "AD-009",
  "slug": "convert-discussion-notes-into-decisions-actions-and-a-parking-lot",
  "chapter": "teacher-admin-paperwork",
  "subtopic": "agendas-and-minutes",
  "title": "Convert discussion notes into decisions, actions and a parking lot",
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

# AD-009 | Convert discussion notes into decisions, actions and a parking lot

## Use this when

Choose this focused tool when your immediate task is to convert discussion notes into decisions, actions and a parking lot. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [DISCUSSION_NOTES: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Convert discussion notes into decisions, actions and a parking lot.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [DISCUSSION_NOTES: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Return decision, action, owner, due date and parking-lot fields. Use unknown markers where the notes do not establish agreement.

Output:
Return the named artifact with all questions, directions, examples or text needed for the task; put teacher keys and notes separately from student/family-facing text.

```

## Fictional test case

Fictional staff planning; two proposed actions: check answer keys and confirm room layout; neither owner nor deadline agreed. This is an intentionally incomplete input-check exercise for AD-009, not a complete example run. Identify which of DISCUSSION_NOTES are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Return decision, action, owner, due date and parking-lot fields. Use unknown markers where the notes do not establish agreement.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

