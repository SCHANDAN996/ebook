---
{
  "id": "WA-030",
  "slug": "audit-a-review-game-for-fairness-accuracy-and-useful-teacher-data",
  "chapter": "worksheets-activities",
  "subtopic": "review-games",
  "title": "Audit a review game for fairness, accuracy and useful teacher data",
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

# WA-030 | Audit a review game for fairness, accuracy and useful teacher data

## Use this when

Choose this focused tool when your immediate task is to audit a review game for fairness, accuracy and useful teacher data. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [GAME_RULES: supply verified information; do not leave blank]
- [ITEMS: supply verified information; do not leave blank]
- [SCORING: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Audit a review game for fairness, accuracy and useful teacher data.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [GAME_RULES: supply verified information; do not leave blank]
- [ITEMS: supply verified information; do not leave blank]
- [SCORING: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Check ambiguity, luck, speed advantage and access. Revise scoring so the resulting teacher data has instructional meaning.

Output:
Return an issue table with location, evidence, severity and smallest correction; then the corrected artifact and unresolved decisions.

```

## Fictional test case

Grade 5 mathematics; equal-whole fractions; 25 minutes; paper and pencils; goal: justify 1/2=2/4. This is an intentionally incomplete input-check exercise for WA-030, not a complete example run. Identify which of GAME_RULES, ITEMS, SCORING are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Check ambiguity, luck, speed advantage and access. Revise scoring so the resulting teacher data has instructional meaning.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

