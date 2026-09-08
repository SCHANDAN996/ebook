---
{
  "id": "AS-036",
  "slug": "create-learner-friendly-solution-explanations-without-hiding-reasoning",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "answer-keys-and-feedback",
  "title": "Create learner-friendly solution explanations without hiding reasoning",
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

# AS-036 | Create learner-friendly solution explanations without hiding reasoning

## Use this when

Choose this focused tool when your immediate task is to create learner-friendly solution explanations without hiding reasoning. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [VERIFIED_SOLUTIONS: supply verified information; do not leave blank]
- [LEARNER_AGE: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Create learner-friendly solution explanations without hiding reasoning.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [VERIFIED_SOLUTIONS: supply verified information; do not leave blank]
- [LEARNER_AGE: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Explain why each step is valid and include a self-check. Preserve reasoning while simplifying vocabulary.

Output:
Return the named artifact with all questions, directions, examples or text needed for the task; put teacher keys and notes separately from student/family-facing text.

```

## Fictional test case

Grade 8 mathematics; solve and justify 2x+3=11; correct answer x=4; paper responses; ten minutes. This is an intentionally incomplete input-check exercise for AS-036, not a complete example run. Identify which of VERIFIED_SOLUTIONS, LEARNER_AGE are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Explain why each step is valid and include a self-check. Preserve reasoning while simplifying vocabulary.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

