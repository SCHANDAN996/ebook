---
{
  "id": "PC-012",
  "slug": "request-a-brief-family-check-in-with-two-exact-scheduling-options",
  "chapter": "parent-communication",
  "subtopic": "concern-emails",
  "title": "Request a brief family check-in with two exact scheduling options",
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

# PC-012 | Request a brief family check-in with two exact scheduling options

## Use this when

Choose this focused tool when your immediate task is to request a brief family check-in with two exact scheduling options. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [TWO_CONFIRMED_SLOTS: supply verified information; do not leave blank]
- [TIMEZONE: supply verified information; do not leave blank]
- [CHANNEL: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Request a brief family check-in with two exact scheduling options.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [TWO_CONFIRMED_SLOTS: supply verified information; do not leave blank]
- [TIMEZONE: supply verified information; do not leave blank]
- [CHANNEL: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Offer exactly the supplied slots with timezone and response route. Leave dates unfilled when availability is not confirmed.

Output:
Return the named artifact with all questions, directions, examples or text needed for the task; put teacher keys and notes separately from student/family-facing text.

```

## Fictional test case

Grade 6 class communication; fictional fact: the class completed a paper-based map activity; 80-word limit; no learner identities or school dates supplied. This is an intentionally incomplete input-check exercise for PC-012, not a complete example run. Identify which of TWO_CONFIRMED_SLOTS, TIMEZONE, CHANNEL are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Offer exactly the supplied slots with timezone and response route. Leave dates unfilled when availability is not confirmed.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

