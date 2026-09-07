---
{
  "id": "LP-004",
  "slug": "create-a-matched-warm-up-and-exit-ticket",
  "chapter": "lesson-planning",
  "subtopic": "warm-ups-and-exit-tickets",
  "title": "Create a matched warm-up and exit ticket",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a matched warm-up and exit ticket

## Use this when

You want to expose prior knowledge and measure growth in one lesson.

## Teacher inputs

- `[GRADE_BAND]`
- `[SUBJECT_AND_TOPIC]`
- `[OBJECTIVE]`
- `[WARM_UP_MINUTES]`
- `[EXIT_TICKET_MINUTES]`
- `[KNOWN_MISCONCEPTION]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND]`
- `[SUBJECT_AND_TOPIC]`
- `[OBJECTIVE]`
- `[WARM_UP_MINUTES]`
- `[EXIT_TICKET_MINUTES]`
- `[KNOWN_MISCONCEPTION]`

Task:
Create two brief tasks aligned to the same learning target.

Required output:
Return: warm-up instructions and answer guide; what each response reveals; bridge into instruction; exit-ticket question and answer guide; 3 response categories (secure/developing/not yet); next-day action for each category.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 7 science; food webs; explain indirect ecosystem effects; 5 minutes each; students think only directly connected organisms are affected.

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
