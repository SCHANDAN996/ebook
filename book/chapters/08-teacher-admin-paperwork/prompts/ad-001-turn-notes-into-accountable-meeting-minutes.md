---
{
  "id": "AD-001",
  "slug": "turn-notes-into-accountable-meeting-minutes",
  "chapter": "teacher-admin-paperwork",
  "subtopic": "agendas-and-minutes",
  "title": "Turn notes into accountable meeting minutes",
  "grade_bands": [
    "All"
  ],
  "subjects": [
    "Any"
  ],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 2
}
---

# AD-001 | Turn notes into accountable meeting minutes

## Use this when

A team needs concise decisions and next actions from rough notes. Use the task-specific check below to distinguish it from related tools.

## Teacher inputs

- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [AUTHORIZED_NOTES: supply verified information; do not leave blank]
- [CONFIRMED_DECISIONS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

## Copy-paste prompt

```text
Turn notes into accountable meeting minutes.

Required inputs:
- [GRADE_SUBJECT: exact age/grade and subject]
- [GOAL: the learning or communication purpose]
- [AUTHORIZED_NOTES: supply verified information; do not leave blank]
- [CONFIRMED_DECISIONS: supply verified information; do not leave blank]
- [CONSTRAINTS: duration, format, resources and approved access requirements; write none only if confirmed]

Specific requirements:
Separate decisions, proposed actions and open questions. Never invent attendees, consensus, owners or deadlines.

Output:
Return the named artifact with all questions, directions, examples or text needed for the task; put teacher keys and notes separately from student/family-facing text.

```

## Fictional test case

Fictional notes: team agreed common exit item next week; teacher-role A volunteered to draft; exact date not agreed.

## Sample output

**Editorial illustration - selected excerpt, not a logged AI run or classroom result.**

Decision: use one common exit item next week. Action: draft the item. Owner: teacher-role A. Due: [NEEDS TEACHER INPUT]. Open question: when will the team review the draft? Do not convert next week into an invented calendar date. Record only the agreement actually present in these notes.

## Teacher verification checklist

- [ ] Task-specific acceptance: Separate decisions, proposed actions and open questions. Never invent attendees, consensus, owners or deadlines.
- [ ] Factual claims trace to supplied evidence; proposals and unknowns are labelled.
- [ ] Answers and subject content checked independently; access and local policy preserved.
- [ ] No identifying or sensitive records were shared; final recipient/content checked locally.

