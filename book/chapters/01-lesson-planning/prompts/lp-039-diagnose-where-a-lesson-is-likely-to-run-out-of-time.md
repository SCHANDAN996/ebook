---
{
  "id": "LP-039",
  "slug": "diagnose-where-a-lesson-is-likely-to-run-out-of-time",
  "chapter": "lesson-planning",
  "subtopic": "pacing-and-transitions",
  "title": "Diagnose where a lesson is likely to run out of time",
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

# LP-039 | Diagnose where a lesson is likely to run out of time

## Use this when

Choose this focused tool when your immediate task is to diagnose where a lesson is likely to run out of time. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [DRAFT_TIMELINE: supply verified information; do not leave blank]
- [CLASSROOM_CONSTRAINTS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Diagnose where a lesson is likely to run out of time.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [DRAFT_TIMELINE: supply verified information; do not leave blank]
- [CLASSROOM_CONSTRAINTS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Identify the three most likely bottlenecks with observable warning signs. Estimate ranges, not falsely precise guaranteed durations.

Output:
Return an issue table with location, evidence, severity and smallest correction; then the corrected artifact and unresolved decisions.

```

## Fictional test case

Grade 6 mathematics; equivalent ratios; 40 minutes; board and paper; goal: explain why 2:3 and 4:6 are equivalent. This is an intentionally incomplete input-check exercise for LP-039, not a complete example run. Identify which of DRAFT_TIMELINE, CLASSROOM_CONSTRAINTS are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Identify the three most likely bottlenecks with observable warning signs. Estimate ranges, not falsely precise guaranteed durations.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

