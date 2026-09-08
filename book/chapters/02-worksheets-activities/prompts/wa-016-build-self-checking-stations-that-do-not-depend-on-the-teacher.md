---
{
  "id": "WA-016",
  "slug": "build-self-checking-stations-that-do-not-depend-on-the-teacher",
  "chapter": "worksheets-activities",
  "subtopic": "learning-stations",
  "title": "Build self-checking stations that do not depend on the teacher",
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

# WA-016 | Build self-checking stations that do not depend on the teacher

## Use this when

Choose this focused tool when your immediate task is to build self-checking stations that do not depend on the teacher. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [STATION_TASKS: supply verified information; do not leave blank]
- [VERIFIED_KEYS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Build self-checking stations that do not depend on the teacher.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [STATION_TASKS: supply verified information; do not leave blank]
- [VERIFIED_KEYS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Separate task cards from self-check cards. Add a retry step and an escalation signal when the key does not resolve confusion.

Output:
Return the named artifact with all questions, directions, examples or text needed for the task; put teacher keys and notes separately from student/family-facing text.

```

## Fictional test case

Grade 5 mathematics; equal-whole fractions; 25 minutes; paper and pencils; goal: justify 1/2=2/4. This is an intentionally incomplete input-check exercise for WA-016, not a complete example run. Identify which of STATION_TASKS, VERIFIED_KEYS are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Separate task cards from self-check cards. Add a retry step and an escalation signal when the key does not resolve confusion.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

