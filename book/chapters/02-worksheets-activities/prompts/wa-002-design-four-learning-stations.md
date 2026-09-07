---
{
  "id": "WA-002",
  "slug": "design-four-learning-stations",
  "chapter": "worksheets-activities",
  "subtopic": "learning-stations",
  "title": "Design four learning stations",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Design four learning stations

## Use this when

You need varied practice modes with manageable rotations.

## Teacher inputs

- `[GRADE_BAND]`
- `[SUBJECT_AND_TOPIC]`
- `[OBJECTIVE]`
- `[CLASS_SIZE]`
- `[TOTAL_TIME]`
- `[MATERIALS]`
- `[ROOM_OR_NOISE_CONSTRAINTS]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND]`
- `[SUBJECT_AND_TOPIC]`
- `[OBJECTIVE]`
- `[CLASS_SIZE]`
- `[TOTAL_TIME]`
- `[MATERIALS]`
- `[ROOM_OR_NOISE_CONSTRAINTS]`

Task:
Design four distinct stations that can run simultaneously.

Required output:
Return for each station: mode; materials per group; student-facing instruction card; expected product; teacher look-fors; misconception; brief answer guide. Also return groups, rotation timing, transition signal and setup checklist.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 7 science; ripple effects in ecosystems; 32 students; 48 minutes; paper, dominoes, whiteboards; one quiet station.

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
