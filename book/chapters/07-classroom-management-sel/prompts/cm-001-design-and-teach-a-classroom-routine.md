---
{
  "id": "CM-001",
  "slug": "design-and-teach-a-classroom-routine",
  "chapter": "classroom-management-sel",
  "subtopic": "routines-and-transitions",
  "title": "Design and teach a classroom routine",
  "grade_bands": ["K-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Design and teach a classroom routine

## Use this when

A recurring transition is costing time or creating confusion.

## Teacher inputs

- `[GRADE_BAND]`
- `[ROUTINE_OR_TRANSITION]`
- `[CURRENT_OBSERVATIONS]`
- `[DESIRED_BEHAVIOR]`
- `[TIME_TARGET]`
- `[ROOM_CONSTRAINTS]`
- `[SCHOOL_EXPECTATIONS]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND]`
- `[ROUTINE_OR_TRANSITION]`
- `[CURRENT_OBSERVATIONS]`
- `[DESIRED_BEHAVIOR]`
- `[TIME_TARGET]`
- `[ROOM_CONSTRAINTS]`
- `[SCHOOL_EXPECTATIONS]`

Task:
Create an explicitly taught routine, not a punishment system.

Required output:
Return: observable steps; teacher script; visual cue; model/non-model practice; feedback language; 5-day rehearsal plan; simple time/data tracker; reset procedure; accessibility considerations.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 4; move from carpet to tables; takes 4 minutes with materials forgotten; goal 90 seconds; narrow aisle.

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
