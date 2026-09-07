---
{
  "id": "AS-001",
  "slug": "create-a-balanced-classroom-assessment",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "quizzes-and-tests",
  "title": "Create a balanced classroom assessment",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a balanced classroom assessment

## Use this when

You need a valid assessment with diagnostic distractors.

## Teacher inputs

- `[GRADE_BAND]`
- `[SUBJECT_AND_SKILLS]`
- `[TIME_LIMIT]`
- `[ITEM_COUNT]`
- `[ITEM_FORMATS]`
- `[COGNITIVE_BALANCE]`
- `[ACCOMMODATIONS]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND]`
- `[SUBJECT_AND_SKILLS]`
- `[TIME_LIMIT]`
- `[ITEM_COUNT]`
- `[ITEM_FORMATS]`
- `[COGNITIVE_BALANCE]`
- `[ACCOMMODATIONS]`

Task:
Create an assessment that samples recall, application and reasoning.

Required output:
Return: student directions; numbered items; point values; complete answer key; worked solutions where needed; distractor rationale; scoring guide; standards/objective map; two priority items for reteaching analysis.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 8 mathematics; one-variable linear equations; 20 minutes; 8 items; 5 multiple choice and 3 constructed response.

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
