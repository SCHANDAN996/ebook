---
{
  "id": "AD-025",
  "slug": "audit-a-proposal-for-unsupported-claims-missing-evidence-and-compliance",
  "chapter": "teacher-admin-paperwork",
  "subtopic": "grants-and-proposals",
  "title": "Audit a proposal for unsupported claims, missing evidence and compliance",
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

# AD-025 | Audit a proposal for unsupported claims, missing evidence and compliance

## Use this when

Choose this focused tool when your immediate task is to audit a proposal for unsupported claims, missing evidence and compliance. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [PROPOSAL: supply verified information; do not leave blank]
- [FUNDER_RULES: supply verified information; do not leave blank]
- [SOURCES: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Audit a proposal for unsupported claims, missing evidence and compliance.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [PROPOSAL: supply verified information; do not leave blank]
- [FUNDER_RULES: supply verified information; do not leave blank]
- [SOURCES: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Trace claims to evidence and check eligibility, budget and missing documents. Do not fabricate citations or approval likelihood.

Output:
Return an issue table with location, evidence, severity and smallest correction; then the corrected artifact and unresolved decisions.

```

## Fictional test case

Fictional staff planning; two proposed actions: check answer keys and confirm room layout; neither owner nor deadline agreed. This is an intentionally incomplete input-check exercise for AD-025, not a complete example run. Identify which of PROPOSAL, FUNDER_RULES, SOURCES are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Trace claims to evidence and check eligibility, budget and missing documents. Do not fabricate citations or approval likelihood.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

