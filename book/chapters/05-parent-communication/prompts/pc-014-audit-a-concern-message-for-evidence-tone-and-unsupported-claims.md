---
{
  "id": "PC-014",
  "slug": "audit-a-concern-message-for-evidence-tone-and-unsupported-claims",
  "chapter": "parent-communication",
  "subtopic": "concern-emails",
  "title": "Audit a concern message for evidence, tone and unsupported claims",
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

# PC-014 | Audit a concern message for evidence, tone and unsupported claims

## Use this when

Choose this focused tool when your immediate task is to audit a concern message for evidence, tone and unsupported claims. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [MESSAGE: supply verified information; do not leave blank]
- [EVIDENCE_RECORD: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Audit a concern message for evidence, tone and unsupported claims.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [MESSAGE: supply verified information; do not leave blank]
- [EVIDENCE_RECORD: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Trace factual sentences to evidence and flag assumptions. Return send/hold recommendation with specific unresolved details.

Output:
Return an issue table with location, evidence, severity and smallest correction; then the corrected artifact and unresolved decisions.

```

## Fictional test case

Grade 6 class communication; fictional fact: the class completed a paper-based map activity; 80-word limit; no learner identities or school dates supplied. This is an intentionally incomplete input-check exercise for PC-014, not a complete example run. Identify which of MESSAGE, EVIDENCE_RECORD are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Trace factual sentences to evidence and flag assumptions. Return send/hold recommendation with specific unresolved details.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

