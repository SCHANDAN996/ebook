---
{
  "id": "RC-026",
  "slug": "generate-bulk-comments-without-mixing-one-learner-s-evidence-with-another",
  "chapter": "report-card-comments",
  "subtopic": "bulk-drafts-from-fictional-evidence",
  "title": "Generate bulk comments without mixing one learner's evidence with another",
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

# RC-026 | Generate bulk comments without mixing one learner's evidence with another

## Use this when

Choose this focused tool when your immediate task is to generate bulk comments without mixing one learner's evidence with another. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [ONE_DEIDENTIFIED_RECORD_AT_A_TIME: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Generate bulk comments without mixing one learner's evidence with another.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [ONE_DEIDENTIFIED_RECORD_AT_A_TIME: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Reset context between records and export drafts with local placeholders. Reconcile row IDs and prevent merging evidence across learners.

Output:
Return the named artifact with all questions, directions, examples or text needed for the task; put teacher keys and notes separately from student/family-facing text.

```

## Fictional test case

Grade 6 mathematics; fictional record: three of four equivalent-fraction items correct; one explanation missing; 70-word limit; no identity supplied. This is an intentionally incomplete input-check exercise for RC-026, not a complete example run. Identify which of ONE_DEIDENTIFIED_RECORD_AT_A_TIME are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Reset context between records and export drafts with local placeholders. Reconcile row IDs and prevent merging evidence across learners.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

