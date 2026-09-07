---
{
  "id": "AD-001",
  "slug": "turn-notes-into-accountable-meeting-minutes",
  "chapter": "teacher-admin-paperwork",
  "subtopic": "agendas-and-minutes",
  "title": "Turn notes into accountable meeting minutes",
  "grade_bands": ["K-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Turn notes into accountable meeting minutes

## Use this when

A team needs concise decisions and next actions from rough notes.

## Teacher inputs

- `[MEETING_NAME_AND_DATE]`
- `[ATTENDEE_ROLES]`
- `[AGENDA]`
- `[ROUGH_NOTES]`
- `[CONFIRMED_DECISIONS]`
- `[ACTION_OWNERS_AND_DATES]`
- `[CONFIDENTIALITY_RULES]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[MEETING_NAME_AND_DATE]`
- `[ATTENDEE_ROLES]`
- `[AGENDA]`
- `[ROUGH_NOTES]`
- `[CONFIRMED_DECISIONS]`
- `[ACTION_OWNERS_AND_DATES]`
- `[CONFIDENTIALITY_RULES]`

Task:
Produce factual minutes without inventing consensus, owners or deadlines.

Required output:
Return: attendees; agenda summary; decisions; action table; parking lot; unresolved questions; next meeting placeholder; verification flags. Mark unclear statements as [CONFIRM].

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade-level planning meeting; anonymized notes; three confirmed decisions; two tentative actions missing owners.

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
