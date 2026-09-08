---
{
  "id": "PC-025",
  "slug": "audit-a-logistics-message-for-missing-consent-safety-and-contact-details",
  "chapter": "parent-communication",
  "subtopic": "permissions-and-logistics",
  "title": "Audit a logistics message for missing consent, safety and contact details",
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

# PC-025 | Audit a logistics message for missing consent, safety and contact details

## Use this when

Choose this focused tool when your immediate task is to audit a logistics message for missing consent, safety and contact details. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [LOGISTICS_DRAFT: supply verified information; do not leave blank]
- [OFFICIAL_REQUIREMENTS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Audit a logistics message for missing consent, safety and contact details.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [LOGISTICS_DRAFT: supply verified information; do not leave blank]
- [OFFICIAL_REQUIREMENTS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Check consent references, safety contacts, cost and dates. Hold the message if essential authorization is missing.

Output:
Return an issue table with location, evidence, severity and smallest correction; then the corrected artifact and unresolved decisions.

```

## Fictional test case

Grade 6 class communication; fictional fact: the class completed a paper-based map activity; 80-word limit; no learner identities or school dates supplied. This is an intentionally incomplete input-check exercise for PC-025, not a complete example run. Identify which of LOGISTICS_DRAFT, OFFICIAL_REQUIREMENTS are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Check consent references, safety contacts, cost and dates. Hold the message if essential authorization is missing.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

