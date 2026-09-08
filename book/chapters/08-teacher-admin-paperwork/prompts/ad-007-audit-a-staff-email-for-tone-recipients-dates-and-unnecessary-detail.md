---
{
  "id": "AD-007",
  "slug": "audit-a-staff-email-for-tone-recipients-dates-and-unnecessary-detail",
  "chapter": "teacher-admin-paperwork",
  "subtopic": "staff-emails",
  "title": "Audit a staff email for tone, recipients, dates and unnecessary detail",
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

# AD-007 | Audit a staff email for tone, recipients, dates and unnecessary detail

## Use this when

Choose this focused tool when your immediate task is to audit a staff email for tone, recipients, dates and unnecessary detail. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [EMAIL: supply verified information; do not leave blank]
- [VERIFIED_CALENDAR: supply verified information; do not leave blank]
- [RECIPIENT_ROLES: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Audit a staff email for tone, recipients, dates and unnecessary detail.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [EMAIL: supply verified information; do not leave blank]
- [VERIFIED_CALENDAR: supply verified information; do not leave blank]
- [RECIPIENT_ROLES: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Check recipient scope, tone, dates and attachments. Keep private addresses out of shared prompts and verify them locally before sending.

Output:
Return an issue table with location, evidence, severity and smallest correction; then the corrected artifact and unresolved decisions.

```

## Fictional test case

Fictional staff planning; two proposed actions: check answer keys and confirm room layout; neither owner nor deadline agreed. This is an intentionally incomplete input-check exercise for AD-007, not a complete example run. Identify which of EMAIL, VERIFIED_CALENDAR, RECIPIENT_ROLES are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Check recipient scope, tone, dates and attachments. Keep private addresses out of shared prompts and verify them locally before sending.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

