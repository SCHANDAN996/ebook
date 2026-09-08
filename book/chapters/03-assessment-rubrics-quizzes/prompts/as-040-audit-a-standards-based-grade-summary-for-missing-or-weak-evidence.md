---
{
  "id": "AS-040",
  "slug": "audit-a-standards-based-grade-summary-for-missing-or-weak-evidence",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "standards-based-grading",
  "title": "Audit a standards-based grade summary for missing or weak evidence",
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

# AS-040 | Audit a standards-based grade summary for missing or weak evidence

## Use this when

Choose this focused tool when your immediate task is to audit a standards-based grade summary for missing or weak evidence. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [GRADE_SUMMARY: supply verified information; do not leave blank]
- [EVIDENCE_RULES: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Audit a standards-based grade summary for missing or weak evidence.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [GRADE_SUMMARY: supply verified information; do not leave blank]
- [EVIDENCE_RULES: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Trace every proficiency claim to evidence and flag sparse or contradictory records. Leave final grades to the authorized teacher.

Output:
Return an issue table with location, evidence, severity and smallest correction; then the corrected artifact and unresolved decisions.

```

## Fictional test case

Grade 8 mathematics; solve and justify 2x+3=11; correct answer x=4; paper responses; ten minutes. This is an intentionally incomplete input-check exercise for AS-040, not a complete example run. Identify which of GRADE_SUMMARY, EVIDENCE_RULES are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Trace every proficiency claim to evidence and flag sparse or contradictory records. Leave final grades to the authorized teacher.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

