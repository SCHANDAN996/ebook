---
{
  "id": "LP-027",
  "slug": "check-whether-an-activity-truly-aligns-to-a-supplied-standard",
  "chapter": "lesson-planning",
  "subtopic": "standards-and-objectives",
  "title": "Check whether an activity truly aligns to a supplied standard",
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

# LP-027 | Check whether an activity truly aligns to a supplied standard

## Use this when

Choose this focused tool when your immediate task is to check whether an activity truly aligns to a supplied standard. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [ACTIVITY: supply verified information; do not leave blank]
- [EXACT_STANDARD: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Check whether an activity truly aligns to a supplied standard.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [ACTIVITY: supply verified information; do not leave blank]
- [EXACT_STANDARD: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Return evidence-for/evidence-against alignment and a minimal repair. Do not declare alignment from shared vocabulary alone.

Output:
Return an issue table with location, evidence, severity and smallest correction; then the corrected artifact and unresolved decisions.

```

## Fictional test case

Grade 6 mathematics; equivalent ratios; 40 minutes; board and paper; goal: explain why 2:3 and 4:6 are equivalent. This is an intentionally incomplete input-check exercise for LP-027, not a complete example run. Identify which of ACTIVITY, EXACT_STANDARD are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Return evidence-for/evidence-against alignment and a minimal repair. Do not declare alignment from shared vocabulary alone.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

