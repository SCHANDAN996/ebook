---
{
  "id": "DF-001",
  "slug": "add-temporary-scaffolds-without-lowering-the-goal",
  "chapter": "differentiation-mixed-ability",
  "subtopic": "scaffolds",
  "title": "Add temporary scaffolds without lowering the goal",
  "grade_bands": ["K-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Add temporary scaffolds without lowering the goal

## Use this when

Some learners need access support while keeping the same objective.

## Teacher inputs

- `[GRADE_BAND]`
- `[SUBJECT_AND_TASK]`
- `[UNCHANGED_OBJECTIVE]`
- `[OBSERVED_BARRIERS: evidence only]`
- `[AVAILABLE_SUPPORTS]`
- `[TIME]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND]`
- `[SUBJECT_AND_TASK]`
- `[UNCHANGED_OBJECTIVE]`
- `[OBSERVED_BARRIERS: evidence only]`
- `[AVAILABLE_SUPPORTS]`
- `[TIME]`

Task:
Create fading scaffolds that preserve cognitive demand.

Required output:
Return: barrier-to-support map; before/during/after scaffolds; teacher language; visual or sentence supports; checks for independence; fade plan; same-goal success criteria; warning if evidence is insufficient.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 7 science; explain photosynthesis model; language load and diagram organization barriers; word bank and graphic organizer available.

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
