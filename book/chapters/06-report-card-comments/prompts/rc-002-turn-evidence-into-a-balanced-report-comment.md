---
{
  "id": "RC-002",
  "slug": "turn-evidence-into-a-balanced-report-comment",
  "chapter": "report-card-comments",
  "subtopic": "strengths-and-next-steps",
  "title": "Turn evidence into a balanced report comment",
  "grade_bands": ["K-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Turn evidence into a balanced report comment

## Use this when

You have assessment evidence and need a concise, defensible comment.

## Teacher inputs

- `[STUDENT_NAME_OR_PLACEHOLDER]`
- `[GRADE_AND_SUBJECT]`
- `[OBSERVED_STRENGTHS]`
- `[SPECIFIC_EVIDENCE]`
- `[NEXT_LEARNING_PRIORITY]`
- `[SUPPORT_OR_STRATEGY]`
- `[WORD_LIMIT]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[STUDENT_NAME_OR_PLACEHOLDER]`
- `[GRADE_AND_SUBJECT]`
- `[OBSERVED_STRENGTHS]`
- `[SPECIFIC_EVIDENCE]`
- `[NEXT_LEARNING_PRIORITY]`
- `[SUPPORT_OR_STRATEGY]`
- `[WORD_LIMIT]`

Task:
Write a report comment using only supplied evidence.

Required output:
Return one comment and a fact trace showing which input supports each sentence. Include one actionable next step; avoid personality, effort or home-support claims unless explicitly evidenced.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

[STUDENT]; Grade 8 mathematics; solves two-step equations accurately; 8/10 on quiz; sign errors with distribution; annotate negative signs; 70 words.

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
