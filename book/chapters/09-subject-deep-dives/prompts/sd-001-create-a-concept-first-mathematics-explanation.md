---
{
  "id": "SD-001",
  "slug": "create-a-concept-first-mathematics-explanation",
  "chapter": "subject-deep-dives",
  "subtopic": "mathematics",
  "title": "Create a concept-first mathematics explanation",
  "grade_bands": ["3-12"],
  "subjects": ["Mathematics"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a concept-first mathematics explanation

## Use this when

Students can follow a procedure but need the underlying idea.

## Teacher inputs

- `[GRADE_BAND]`
- `[CONCEPT]`
- `[PRIOR_KNOWLEDGE]`
- `[KNOWN_MISCONCEPTION]`
- `[REPRESENTATIONS_AVAILABLE]`
- `[EXAMPLE_AND_NON_EXAMPLE]`
- `[TIME]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND]`
- `[CONCEPT]`
- `[PRIOR_KNOWLEDGE]`
- `[KNOWN_MISCONCEPTION]`
- `[REPRESENTATIONS_AVAILABLE]`
- `[EXAMPLE_AND_NON_EXAMPLE]`
- `[TIME]`

Task:
Create a mathematically accurate explanation connecting concrete, visual and symbolic representations.

Required output:
Return: concept statement; prerequisite check; representation sequence; teacher think-aloud; worked example; non-example; hinge question with distractors; guided task; independent transfer; answer guide.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 5; compare fractions near one; unit fractions understood; misconception that larger denominator means larger value; fraction strips and number lines.

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
