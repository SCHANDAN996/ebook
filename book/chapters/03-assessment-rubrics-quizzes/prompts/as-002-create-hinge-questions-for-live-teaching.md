---
{
  "id": "AS-002",
  "slug": "create-hinge-questions-for-live-teaching",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "formative-checks-and-exit-tickets",
  "title": "Create hinge questions for live teaching",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create hinge questions for live teaching

## Use this when

You need quick questions that determine what to do next.

## Teacher inputs

- `[GRADE_BAND]`
- `[SUBJECT_AND_CONCEPT]`
- `[OBJECTIVE]`
- `[KNOWN_MISCONCEPTIONS]`
- `[NUMBER_OF_QUESTIONS]`
- `[RESPONSE_METHOD]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND]`
- `[SUBJECT_AND_CONCEPT]`
- `[OBJECTIVE]`
- `[KNOWN_MISCONCEPTIONS]`
- `[NUMBER_OF_QUESTIONS]`
- `[RESPONSE_METHOD]`

Task:
Write diagnostic hinge questions with unambiguous instructional decisions.

Required output:
Return each question with answer/options; correct answer; misconception mapped to each distractor; acceptable response threshold; immediate teacher action for each response pattern. End with a 3-minute exit ticket.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 5 science; matter conservation; 4 hinge questions; fingers 1-4; students think matter disappears when dissolved.

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
