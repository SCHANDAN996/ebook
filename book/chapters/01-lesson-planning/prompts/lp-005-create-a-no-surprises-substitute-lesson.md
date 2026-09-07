---
{
  "id": "LP-005",
  "slug": "create-a-no-surprises-substitute-lesson",
  "chapter": "lesson-planning",
  "subtopic": "substitute-and-emergency-plans",
  "title": "Create a no-surprises substitute lesson",
  "grade_bands": ["K-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a no-surprises substitute lesson

## Use this when

A substitute teacher needs a safe, self-contained plan with minimal preparation.

## Teacher inputs

- `[GRADE_BAND]`
- `[SUBJECT_AND_TOPIC]`
- `[DURATION_MINUTES]`
- `[MATERIALS_ALREADY_IN_ROOM]`
- `[STUDENT_ROUTINES]`
- `[ACCESSIBILITY_NEEDS: non-identifying]`
- `[PROHIBITED_ACTIVITIES_OR_RESOURCES]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND]`
- `[SUBJECT_AND_TOPIC]`
- `[DURATION_MINUTES]`
- `[MATERIALS_ALREADY_IN_ROOM]`
- `[STUDENT_ROUTINES]`
- `[ACCESSIBILITY_NEEDS: non-identifying]`
- `[PROHIBITED_ACTIVITIES_OR_RESOURCES]`

Task:
Write a substitute plan that another adult can run without guessing.

Required output:
Return: one-page overview; minute-by-minute plan; exact directions to read aloud; attendance and safety notes as placeholders; independent task; early-finisher option; answer key; collection procedure; contingency if technology fails. Never invent school procedures.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 4 social studies; map skills; 55 minutes; atlases and paper; no devices; established pair-share routine.

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
