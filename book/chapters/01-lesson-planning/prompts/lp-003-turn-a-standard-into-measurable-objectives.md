---
{
  "id": "LP-003",
  "slug": "turn-a-standard-into-measurable-objectives",
  "chapter": "lesson-planning",
  "subtopic": "standards-and-objectives",
  "title": "Turn a standard into measurable objectives",
  "grade_bands": ["K-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Turn a standard into measurable objectives

## Use this when

A standard is too broad to teach or assess in one lesson.

## Teacher inputs

- `[GRADE_BAND]`
- `[SUBJECT]`
- `[STANDARD_TEXT: paste exactly]`
- `[LESSON_COUNT]`
- `[CONTEXT_OR_UNIT]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND]`
- `[SUBJECT]`
- `[STANDARD_TEXT: paste exactly]`
- `[LESSON_COUNT]`
- `[CONTEXT_OR_UNIT]`

Task:
Unpack the supplied standard without changing its meaning.

Required output:
Return: key nouns and verbs; prerequisite skills; 3-6 measurable objectives; student-friendly 'I can' statements; success criteria; one aligned evidence task per objective; ambiguity questions. Quote the supplied standard exactly before analysis.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 5 ELA; standard supplied by teacher; 4 lessons; informational text unit.

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
