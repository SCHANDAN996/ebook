---
{
  "id": "AS-004",
  "slug": "diagnose-errors-from-anonymous-work",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "diagnosis-and-misconceptions",
  "title": "Diagnose errors from anonymous work",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Diagnose errors from anonymous work

## Use this when

You have non-identifying student responses and need instructional patterns.

## Teacher inputs

- `[GRADE_BAND]`
- `[SUBJECT_AND_SKILL]`
- `[TASK_AND_CORRECT_ANSWER]`
- `[ANONYMOUS_RESPONSES]`
- `[SCORING_CRITERIA]`
- `[NUMBER_OF_GROUPS_FOR_RETEACHING]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND]`
- `[SUBJECT_AND_SKILL]`
- `[TASK_AND_CORRECT_ANSWER]`
- `[ANONYMOUS_RESPONSES]`
- `[SCORING_CRITERIA]`
- `[NUMBER_OF_GROUPS_FOR_RETEACHING]`

Task:
Analyze response patterns without inferring ability, motivation or personal traits.

Required output:
Return: response-by-response evidence; misconception codes; frequency table; confidence/uncertainty notes; flexible reteaching groups; one targeted mini-task per group; reassessment question. Preserve original responses exactly.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 6 fractions; compare unlike fractions; 12 responses labeled A-L; three reteaching groups.

## Sample output

Not included in this edition.

## Teacher verification checklist

- [ ] Every fact can be traced to the teacher inputs.
- [ ] Content, answers and examples are accurate.
- [ ] Timing, materials and difficulty are feasible.
- [ ] Accessibility supports preserve the learning goal.
- [ ] A teacher reviews the result before classroom or family use.

## Editorial notes

Phase 3 beta draft. Cross-tool model testing and qualified human review are pending.
