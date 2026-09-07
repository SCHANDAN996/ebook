---
{
  "id": "AS-003",
  "slug": "build-a-student-readable-analytic-rubric",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "rubrics",
  "title": "Build a student-readable analytic rubric",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Build a student-readable analytic rubric

## Use this when

A complex product needs transparent, observable criteria.

## Teacher inputs

- `[GRADE_BAND]`
- `[TASK_DESCRIPTION]`
- `[LEARNING_OBJECTIVES]`
- `[CRITERIA_COUNT]`
- `[PERFORMANCE_LEVELS]`
- `[TOTAL_POINTS]`
- `[NON_NEGOTIABLES]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND]`
- `[TASK_DESCRIPTION]`
- `[LEARNING_OBJECTIVES]`
- `[CRITERIA_COUNT]`
- `[PERFORMANCE_LEVELS]`
- `[TOTAL_POINTS]`
- `[NON_NEGOTIABLES]`

Task:
Create a rubric that scores evidence of learning rather than compliance or personality.

Required output:
Return: rubric table; observable descriptors for every cell; point calculation; student checklist; calibration examples using fictional work; teacher note on avoiding double-penalties; accessibility review.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 7 science ecosystem model; 4 criteria; four levels; 16 points; causal arrows and evidence explanation required.

## Sample output

A strong response should preserve every supplied fact, follow the requested sections, include usable teacher-facing details, and flag any missing information instead of inventing it.

## Teacher verification checklist

- [ ] Every fact can be traced to the teacher inputs.
- [ ] Content, answers and examples are accurate.
- [ ] Timing, materials and difficulty are feasible.
- [ ] Accessibility supports preserve the learning goal.
- [ ] A teacher reviews the result before classroom or family use.

## Editorial notes

Phase 3 beta draft. Cross-tool model testing and qualified human review are pending.
