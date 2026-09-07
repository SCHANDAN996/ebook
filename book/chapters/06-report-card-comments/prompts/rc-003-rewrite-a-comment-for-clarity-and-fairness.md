---
{
  "id": "RC-003",
  "slug": "rewrite-a-comment-for-clarity-and-fairness",
  "chapter": "report-card-comments",
  "subtopic": "tone-and-rewriting",
  "title": "Rewrite a comment for clarity and fairness",
  "grade_bands": ["K-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Rewrite a comment for clarity and fairness

## Use this when

A draft comment may be vague, harsh or unsupported.

## Teacher inputs

- `[ORIGINAL_COMMENT]`
- `[VERIFIED_EVIDENCE]`
- `[GRADE_AND_SUBJECT]`
- `[DESIRED_TONE]`
- `[WORD_LIMIT]`
- `[SCHOOL_POLICY_NOTES]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[ORIGINAL_COMMENT]`
- `[VERIFIED_EVIDENCE]`
- `[GRADE_AND_SUBJECT]`
- `[DESIRED_TONE]`
- `[WORD_LIMIT]`
- `[SCHOOL_POLICY_NOTES]`

Task:
Rewrite the comment while preserving verified facts and removing unsupported judgments.

Required output:
Return: revised comment; change log categorized as clarity/tone/evidence/actionability; any claim that cannot be retained; one next-step sentence. Do not soften away a material concern.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Original: 'Jordan is lazy and never finishes anything.' Evidence: 2 of 4 tasks submitted in two weeks after reminders; Grade 7 science; calm and direct; 60 words.

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
