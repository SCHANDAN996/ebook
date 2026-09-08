---
{
  "id": "AD-022",
  "slug": "audit-a-club-or-duty-plan-for-gaps-overload-and-unclear-responsibility",
  "chapter": "teacher-admin-paperwork",
  "subtopic": "clubs-and-duty-plans",
  "title": "Audit a club or duty plan for gaps, overload and unclear responsibility",
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

# AD-022 | Audit a club or duty plan for gaps, overload and unclear responsibility

## Use this when

Choose this focused tool when your immediate task is to audit a club or duty plan for gaps, overload and unclear responsibility. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [DUTY_OR_CLUB_PLAN: supply verified information; do not leave blank]
- [ROLE_REQUIREMENTS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Audit a club or duty plan for gaps, overload and unclear responsibility.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [DUTY_OR_CLUB_PLAN: supply verified information; do not leave blank]
- [ROLE_REQUIREMENTS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Check coverage, overload, breaks and unclear ownership. Preserve contractual or local requirements supplied by the teacher.

Output:
Return an issue table with location, evidence, severity and smallest correction; then the corrected artifact and unresolved decisions.

```

## Fictional test case

Fictional staff planning; two proposed actions: check answer keys and confirm room layout; neither owner nor deadline agreed. This is an intentionally incomplete input-check exercise for AD-022, not a complete example run. Identify which of DUTY_OR_CLUB_PLAN, ROLE_REQUIREMENTS are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Check coverage, overload, breaks and unclear ownership. Preserve contractual or local requirements supplied by the teacher.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

