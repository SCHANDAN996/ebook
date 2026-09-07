---
{
  "id": "RC-001",
  "slug": "build-an-evidence-safe-comment-bank",
  "chapter": "report-card-comments",
  "subtopic": "comment-banks",
  "title": "Build an evidence-safe comment bank",
  "grade_bands": ["K-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Build an evidence-safe comment bank

## Use this when

You need reusable comments that still sound specific and humane.

## Teacher inputs

- `[GRADE_AND_SUBJECT]`
- `[LEARNING_OBJECTIVES]`
- `[PERFORMANCE_CATEGORIES]`
- `[TONE]`
- `[LENGTH_RANGE]`
- `[RESTRICTED_WORDS_OR_POLICIES]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_AND_SUBJECT]`
- `[LEARNING_OBJECTIVES]`
- `[PERFORMANCE_CATEGORIES]`
- `[TONE]`
- `[LENGTH_RANGE]`
- `[RESTRICTED_WORDS_OR_POLICIES]`

Task:
Create modular comments with visible evidence placeholders rather than invented claims.

Required output:
Return comments for exceeding/meeting/developing/beginning; each includes strength, evidence placeholder and next step; neutral pronoun variants; repetition audit; prohibited-inference checklist.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 6 science; model systems and explain evidence; four performance categories; 45-65 words; avoid fixed-ability labels.

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
