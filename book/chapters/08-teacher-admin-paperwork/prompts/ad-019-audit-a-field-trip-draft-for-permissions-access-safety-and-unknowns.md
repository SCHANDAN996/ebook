---
{
  "id": "AD-019",
  "slug": "audit-a-field-trip-draft-for-permissions-access-safety-and-unknowns",
  "chapter": "teacher-admin-paperwork",
  "subtopic": "field-trip-logistics",
  "title": "Audit a field-trip draft for permissions, access, safety and unknowns",
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

# AD-019 | Audit a field-trip draft for permissions, access, safety and unknowns

## Use this when

Choose this focused tool when your immediate task is to audit a field-trip draft for permissions, access, safety and unknowns. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [TRIP_DRAFT: supply verified information; do not leave blank]
- [APPROVED_REQUIREMENTS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Audit a field-trip draft for permissions, access, safety and unknowns.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [TRIP_DRAFT: supply verified information; do not leave blank]
- [APPROVED_REQUIREMENTS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Audit permissions, access, safety and unresolved facts. Block operational use while a critical approval is missing.

Output:
Return an issue table with location, evidence, severity and smallest correction; then the corrected artifact and unresolved decisions.

```

## Fictional test case

Fictional staff planning; two proposed actions: check answer keys and confirm room layout; neither owner nor deadline agreed. This is an intentionally incomplete input-check exercise for AD-019, not a complete example run. Identify which of TRIP_DRAFT, APPROVED_REQUIREMENTS are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Audit permissions, access, safety and unresolved facts. Block operational use while a critical approval is missing.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

