---
{
  "id": "WA-001",
  "slug": "build-a-focused-practice-worksheet",
  "chapter": "worksheets-activities",
  "subtopic": "practice-worksheets",
  "title": "Build a focused practice worksheet",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Build a focused practice worksheet

## Use this when

Students need purposeful practice rather than repetitive filler.

## Teacher inputs

- `[GRADE_BAND]`
- `[SUBJECT_AND_SKILL]`
- `[LEARNING_OBJECTIVE]`
- `[NUMBER_OF_ITEMS]`
- `[DIFFICULTY_RANGE]`
- `[ALLOWED_FORMATS]`
- `[ACCOMMODATIONS]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND]`
- `[SUBJECT_AND_SKILL]`
- `[LEARNING_OBJECTIVE]`
- `[NUMBER_OF_ITEMS]`
- `[DIFFICULTY_RANGE]`
- `[ALLOWED_FORMATS]`
- `[ACCOMMODATIONS]`

Task:
Create a printable worksheet with a deliberate progression and usable answer key.

Required output:
Return: title and directions; brief model; items grouped as foundation/application/reasoning; workspace cues; one misconception diagnostic; optional challenge; complete answer key with short explanations; alignment check.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 6 mathematics; ratio tables; 12 items; easy to moderate; black-and-white printing; larger spacing.

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
