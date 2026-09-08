---
{
  "id": "AS-033",
  "slug": "create-a-complete-worked-answer-key-from-verified-questions",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "answer-keys-and-feedback",
  "title": "Create a complete worked answer key from verified questions",
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

# AS-033 | Create a complete worked answer key from verified questions

## Use this when

Choose this focused tool when your immediate task is to create a complete worked answer key from verified questions. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [VERIFIED_QUESTIONS: supply verified information; do not leave blank]
- [SCORING_RULES: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Create a complete worked answer key from verified questions.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [VERIFIED_QUESTIONS: supply verified information; do not leave blank]
- [SCORING_RULES: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Solve every question fully and include alternative valid methods. Flag underspecified questions rather than inventing missing conditions.

Output:
Return the named artifact with all questions, directions, examples or text needed for the task; put teacher keys and notes separately from student/family-facing text.

```

## Fictional test case

Grade 8 mathematics; solve and justify 2x+3=11; correct answer x=4; paper responses; ten minutes. This is an intentionally incomplete input-check exercise for AS-033, not a complete example run. Identify which of VERIFIED_QUESTIONS, SCORING_RULES are still needed. Expected behavior: request missing essentials, not invent the finished artifact.

## Teacher verification checklist

- [ ] Task-specific acceptance: Solve every question fully and include alternative valid methods. Flag underspecified questions rather than inventing missing conditions.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

