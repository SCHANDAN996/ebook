---
{
  "id": "AS-035",
  "slug": "audit-an-answer-key-for-mathematical-factual-and-scoring-errors",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "answer-keys-and-feedback",
  "title": "Audit an answer key for mathematical, factual and scoring errors",
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

# AS-035 | Audit an answer key for mathematical, factual and scoring errors

## Use this when

Choose this focused tool when your immediate task is to audit an answer key for mathematical, factual and scoring errors. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [QUESTIONS: supply verified information; do not leave blank]
- [ANSWER_KEY: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Audit an answer key for mathematical, factual and scoring errors.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [QUESTIONS: supply verified information; do not leave blank]
- [ANSWER_KEY: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Recompute solutions and totals independently, then list item-level discrepancies. Do not use the existing key as proof of correctness.

Output:
Return an issue table with location, evidence, severity and smallest correction; then the corrected artifact and unresolved decisions.

```

## Fictional test case

Grade 8 mathematics; solve and justify 2x+3=11; correct answer x=4; paper responses; ten minutes. This is an intentionally incomplete input-check exercise for AS-035, not a complete example run. Identify which of QUESTIONS, ANSWER_KEY are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Recompute solutions and totals independently, then list item-level discrepancies. Do not use the existing key as proof of correctness.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

