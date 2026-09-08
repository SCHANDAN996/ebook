---
{
  "id": "AS-004",
  "slug": "diagnose-errors-from-anonymous-work",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "diagnosis-and-misconceptions",
  "title": "Diagnose errors from anonymous work",
  "grade_bands": [
    "3-5",
    "6-8",
    "9-12"
  ],
  "subjects": [
    "Any"
  ],
  "sensitivity": "sensitive",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 2
}
---

# AS-004 | Diagnose errors from anonymous work

## Use this when

You have non-identifying student responses and need instructional patterns. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [TASK: supply verified information; do not leave blank]
- [CORRECT_ANSWER: supply verified information; do not leave blank]
- [ANONYMOUS_RESPONSES: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Diagnose errors from anonymous work.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [TASK: supply verified information; do not leave blank]
- [CORRECT_ANSWER: supply verified information; do not leave blank]
- [ANONYMOUS_RESPONSES: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Preserve response text and code only visible errors. State alternative explanations and the follow-up question needed before grouping.

Output:
Return the named artifact with all questions, directions, examples or text needed for the task; put teacher keys and notes separately from student/family-facing text.

```

## Fictional test case

Grade 5 fraction comparison; compare 3/4 and 5/6; fictional responses A: 5/6 because twelfths are 10 and 9; B: 3/4 because fourths are larger; C: blank.

## Sample output

**Editorial illustration - selected excerpt, not a logged AI run or classroom result.**

A: correct comparison with common-whole evidence; verify that 3/4=9/12 and 5/6=10/12. B: possible confusion between unit-piece size and total fraction; ask for a diagram before assigning a stable misconception. C: insufficient evidence, not a misconception code. Follow-up task: compare 2/3 and 3/4 using equal strips. Key: 3/4 is larger because 9/12 exceeds 8/12.

## Teacher verification checklist

- [ ] Task-specific acceptance: Preserve response text and code only visible errors. State alternative explanations and the follow-up question needed before grouping.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

