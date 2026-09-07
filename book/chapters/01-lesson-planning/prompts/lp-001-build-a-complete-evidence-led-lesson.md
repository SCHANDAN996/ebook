---
{
  "id": "LP-001",
  "slug": "build-a-complete-evidence-led-lesson",
  "chapter": "lesson-planning",
  "subtopic": "complete-lessons",
  "title": "Build a complete evidence-led lesson",
  "grade_bands": ["3-8"],
  "subjects": ["Science"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Build a complete evidence-led lesson

## Use this when

You need a teachable lesson, not a loose list of activities.

## Teacher inputs

- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_TOPIC: exact content]`
- `[DURATION_MINUTES: total time]`
- `[LEARNING_STANDARD_OR_OBJECTIVE: paste verbatim]`
- `[AVAILABLE_MATERIALS: include constraints]`
- `[LEARNER_CONTEXT: relevant strengths and needs; no names]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_TOPIC: exact content]`
- `[DURATION_MINUTES: total time]`
- `[LEARNING_STANDARD_OR_OBJECTIVE: paste verbatim]`
- `[AVAILABLE_MATERIALS: include constraints]`
- `[LEARNER_CONTEXT: relevant strengths and needs; no names]`

Task:
Create a classroom-ready lesson whose assessment directly measures the supplied objective.

Required output:
Return: objective in student-friendly language; timed agenda; teacher moves; student actions; checks for understanding; independent evidence; exit ticket with answer guide; likely misconception and response; materials and preparation.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 6 science; photosynthesis; 50 minutes; students model matter and energy; board, paper, colored pencils; mixed reading levels.

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
