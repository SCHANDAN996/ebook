---
{
  "id": "RC-027",
  "slug": "vary-sentence-structure-while-preserving-every-supplied-fact",
  "chapter": "report-card-comments",
  "subtopic": "bulk-drafts-from-fictional-evidence",
  "title": "Vary sentence structure while preserving every supplied fact",
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

# RC-027 | Vary sentence structure while preserving every supplied fact

## Use this when

Choose this focused tool when your immediate task is to vary sentence structure while preserving every supplied fact. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [VERIFIED_COMMENT: supply verified information; do not leave blank]
- [VARIANT_COUNT: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Vary sentence structure while preserving every supplied fact.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [VERIFIED_COMMENT: supply verified information; do not leave blank]
- [VARIANT_COUNT: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Vary syntax only; preserve every factual claim and uncertainty. Compare variants against the original evidence clause by clause.

Output:
Return the named artifact with all questions, directions, examples or text needed for the task; put teacher keys and notes separately from student/family-facing text.

```

## Fictional test case

Grade 6 mathematics; fictional record: three of four equivalent-fraction items correct; one explanation missing; 70-word limit; no identity supplied. This is an intentionally incomplete input-check exercise for RC-027, not a complete example run. Identify which of VERIFIED_COMMENT, VARIANT_COUNT are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Vary syntax only; preserve every factual claim and uncertainty. Compare variants against the original evidence clause by clause.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

