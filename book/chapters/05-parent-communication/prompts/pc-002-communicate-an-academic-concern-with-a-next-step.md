---
{
  "id": "PC-002",
  "slug": "communicate-an-academic-concern-with-a-next-step",
  "chapter": "parent-communication",
  "subtopic": "concern-emails",
  "title": "Communicate an academic concern with a next step",
  "grade_bands": ["K-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Communicate an academic concern with a next step

## Use this when

A family needs clear facts and a manageable path forward.

## Teacher inputs

- `[STUDENT_FIRST_NAME_OR_PLACEHOLDER]`
- `[GRADE_AND_SUBJECT]`
- `[STRENGTH_EVIDENCE]`
- `[CONCERN_EVIDENCE_AND_DATES]`
- `[SUPPORT_ALREADY_OFFERED]`
- `[REQUESTED_NEXT_STEP]`
- `[AVAILABLE_CONTACT_OPTIONS]`
- `[TONE_AND_LENGTH]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[STUDENT_FIRST_NAME_OR_PLACEHOLDER]`
- `[GRADE_AND_SUBJECT]`
- `[STRENGTH_EVIDENCE]`
- `[CONCERN_EVIDENCE_AND_DATES]`
- `[SUPPORT_ALREADY_OFFERED]`
- `[REQUESTED_NEXT_STEP]`
- `[AVAILABLE_CONTACT_OPTIONS]`
- `[TONE_AND_LENGTH]`

Task:
Write a factual, collaborative message without blame, diagnosis or invented context.

Required output:
Return: neutral subject; full email; brief version; factual consistency check. Separate observation from interpretation and retain all scheduling details exactly.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Jordan; Grade 7 science; thoughtful discussion contributions; 2 of 4 tasks submitted over two weeks; written reminders and extra class time; 10-minute call; Thursday 3:30 PM or Friday 8:00 AM.

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
