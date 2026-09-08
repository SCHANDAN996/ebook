---
{
  "id": "RC-028",
  "slug": "audit-a-bulk-comment-set-for-duplicates-contradictions-and-evidence-leakage",
  "chapter": "report-card-comments",
  "subtopic": "bulk-drafts-from-fictional-evidence",
  "title": "Audit a bulk comment set for duplicates, contradictions and evidence leakage",
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

# RC-028 | Audit a bulk comment set for duplicates, contradictions and evidence leakage

## Use this when

Choose this focused tool when your immediate task is to audit a bulk comment set for duplicates, contradictions and evidence leakage. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [COMMENT_SET: supply verified information; do not leave blank]
- [MATCHED_RECORDS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Audit a bulk comment set for duplicates, contradictions and evidence leakage.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [COMMENT_SET: supply verified information; do not leave blank]
- [MATCHED_RECORDS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Check duplicate text, contradictions and cross-record leakage. Hold any draft whose evidence cannot be matched to exactly one record.

Output:
Return an issue table with location, evidence, severity and smallest correction; then the corrected artifact and unresolved decisions.

```

## Fictional test case

Grade 6 mathematics; fictional record: three of four equivalent-fraction items correct; one explanation missing; 70-word limit; no identity supplied. This is an intentionally incomplete input-check exercise for RC-028, not a complete example run. Identify which of COMMENT_SET, MATCHED_RECORDS are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Check duplicate text, contradictions and cross-record leakage. Hold any draft whose evidence cannot be matched to exactly one record.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

