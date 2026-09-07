# Chapter 9: Subject-Specific Deep Dives

General prompting rules are not enough when disciplinary accuracy matters. These 15 prompts
cover mathematics, English language arts, science, social studies and arts, physical
education or electives. Each asks the model to respect how knowledge and evidence work in
that subject.

## How to use this chapter

In mathematics, demand complete solutions and connected representations. In language arts,
provide the authorized text and distinguish evidence from interpretation. In science, state
variables, safety limits and uncertainty; expected patterns are not fabricated results. In
social studies, provide sources and request perspective and corroboration. In practical or
performance subjects, include space, equipment and physical-access constraints.

## Accuracy check

Verify every equation, quotation, date, scientific claim and source. Never accept a citation
merely because it looks plausible. Preserve copyright boundaries and local curriculum
requirements. If evidence supports only a possible outcome, the final language must not
present that outcome as certain.


---


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

**Illustrative concept explanation — fractions near one**

Both 3/4 and 5/6 are one unit fraction short of a whole, but the missing pieces are not
the same size. Fourths are larger pieces than sixths, so 1/4 > 1/6. Therefore subtracting
1/6 from one leaves more than subtracting 1/4: `5/6 > 3/4`.

**Representation:** Draw two equal number lines from 0 to 1 and mark the unfilled final
interval on each. **Hinge question:** “Two pizzas each have one slice missing. Must the
amount left be equal?” Correct response: no; the original partitions determine slice
size. **Transfer:** Order 2/3, 7/8 and 11/12 without common denominators. Answer:
`2/3 < 7/8 < 11/12`, because the missing unit fractions decrease.

## Teacher verification checklist

- [ ] Every fact can be traced to the teacher inputs.
- [ ] Content, answers and examples are accurate.
- [ ] Timing, materials and difficulty are feasible.
- [ ] Accessibility supports preserve the learning goal.
- [ ] A teacher reviews the result before classroom or family use.

## Editorial notes

Full-book content draft. Final editorial review is pending.


---


---
{
  "id": "SD-002",
  "slug": "design-an-evidence-based-science-investigation",
  "chapter": "subject-deep-dives",
  "subtopic": "science",
  "title": "Design an evidence-based science investigation",
  "grade_bands": ["3-12"],
  "subjects": ["Science"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Design an evidence-based science investigation

## Use this when

Students need to investigate a testable question safely.

## Teacher inputs

- `[GRADE_BAND]`
- `[SCIENCE_TOPIC]`
- `[LEARNING_OBJECTIVE]`
- `[AVAILABLE_MATERIALS]`
- `[TIME]`
- `[SAFETY_RULES]`
- `[VARIABLES_OR_PHENOMENON]`
- `[DATA_FORMAT]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND]`
- `[SCIENCE_TOPIC]`
- `[LEARNING_OBJECTIVE]`
- `[AVAILABLE_MATERIALS]`
- `[TIME]`
- `[SAFETY_RULES]`
- `[VARIABLES_OR_PHENOMENON]`
- `[DATA_FORMAT]`

Task:
Design a feasible investigation and distinguish observation from explanation.

Required output:
Return: question; prediction prompt; variables; controls; safety check; numbered procedure; data table; analysis questions; claim-evidence-reasoning task; expected pattern, not fabricated results; limitations; cleanup.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 6; factors affecting dissolving rate; water, cups, sugar, spoons, thermometers; 40 minutes; no tasting; temperature as variable.

## Sample output

**Illustrative concept explanation — fractions near one**

Both 3/4 and 5/6 are one unit fraction short of a whole, but the missing pieces are not
the same size. Fourths are larger pieces than sixths, so 1/4 > 1/6. Therefore subtracting
1/6 from one leaves more than subtracting 1/4: `5/6 > 3/4`.

**Representation:** Draw two equal number lines from 0 to 1 and mark the unfilled final
interval on each. **Hinge question:** “Two pizzas each have one slice missing. Must the
amount left be equal?” Correct response: no; the original partitions determine slice
size. **Transfer:** Order 2/3, 7/8 and 11/12 without common denominators. Answer:
`2/3 < 7/8 < 11/12`, because the missing unit fractions decrease.

## Teacher verification checklist

- [ ] Every fact can be traced to the teacher inputs.
- [ ] Content, answers and examples are accurate.
- [ ] Timing, materials and difficulty are feasible.
- [ ] Accessibility supports preserve the learning goal.
- [ ] A teacher reviews the result before classroom or family use.

## Editorial notes

Full-book content draft. Final editorial review is pending.


---


---
{
  "id": "SD-003",
  "slug": "connect-concrete-visual-and-symbolic-mathematics-representations",
  "chapter": "subject-deep-dives",
  "subtopic": "mathematics",
  "title": "Connect concrete, visual and symbolic mathematics representations",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Connect concrete, visual and symbolic mathematics representations

## Use this when

You need a subject-accurate teaching resource connecting concepts, evidence and transfer focused on mathematics.

## Teacher inputs

- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

Task:
Complete this teacher task: Connect concrete, visual and symbolic mathematics representations. Create a subject-accurate teaching resource connecting concepts, evidence and transfer using only the supplied inputs.

Required output:
Return: core concept; prerequisites; accurate model; worked example; misconception diagnostic; guided application; independent transfer; answer guide; subject-accuracy audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], mathematics; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

**Illustrative concept explanation — fractions near one**

Both 3/4 and 5/6 are one unit fraction short of a whole, but the missing pieces are not
the same size. Fourths are larger pieces than sixths, so 1/4 > 1/6. Therefore subtracting
1/6 from one leaves more than subtracting 1/4: `5/6 > 3/4`.

**Representation:** Draw two equal number lines from 0 to 1 and mark the unfilled final
interval on each. **Hinge question:** “Two pizzas each have one slice missing. Must the
amount left be equal?” Correct response: no; the original partitions determine slice
size. **Transfer:** Order 2/3, 7/8 and 11/12 without common denominators. Answer:
`2/3 < 7/8 < 11/12`, because the missing unit fractions decrease.

## Teacher verification checklist

- [ ] Every fact can be traced to the teacher inputs.
- [ ] Content, answers and examples are accurate.
- [ ] Timing, materials and difficulty are feasible.
- [ ] Accessibility supports preserve the learning goal.
- [ ] A teacher reviews the result before classroom or family use.

## Editorial notes

Full-book content draft. Final editorial review is pending.


---


---
{
  "id": "SD-004",
  "slug": "build-a-mathematics-error-analysis-lesson-with-verified-solutions",
  "chapter": "subject-deep-dives",
  "subtopic": "mathematics",
  "title": "Build a mathematics error-analysis lesson with verified solutions",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Build a mathematics error-analysis lesson with verified solutions

## Use this when

You need a subject-accurate teaching resource connecting concepts, evidence and transfer focused on mathematics.

## Teacher inputs

- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

Task:
Complete this teacher task: Build a mathematics error-analysis lesson with verified solutions. Create a subject-accurate teaching resource connecting concepts, evidence and transfer using only the supplied inputs.

Required output:
Return: core concept; prerequisites; accurate model; worked example; misconception diagnostic; guided application; independent transfer; answer guide; subject-accuracy audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], mathematics; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

**Illustrative concept explanation — fractions near one**

Both 3/4 and 5/6 are one unit fraction short of a whole, but the missing pieces are not
the same size. Fourths are larger pieces than sixths, so 1/4 > 1/6. Therefore subtracting
1/6 from one leaves more than subtracting 1/4: `5/6 > 3/4`.

**Representation:** Draw two equal number lines from 0 to 1 and mark the unfilled final
interval on each. **Hinge question:** “Two pizzas each have one slice missing. Must the
amount left be equal?” Correct response: no; the original partitions determine slice
size. **Transfer:** Order 2/3, 7/8 and 11/12 without common denominators. Answer:
`2/3 < 7/8 < 11/12`, because the missing unit fractions decrease.

## Teacher verification checklist

- [ ] Every fact can be traced to the teacher inputs.
- [ ] Content, answers and examples are accurate.
- [ ] Timing, materials and difficulty are feasible.
- [ ] Accessibility supports preserve the learning goal.
- [ ] A teacher reviews the result before classroom or family use.

## Editorial notes

Full-book content draft. Final editorial review is pending.


---


---
{
  "id": "SD-005",
  "slug": "build-a-close-reading-lesson-from-an-authorized-supplied-text",
  "chapter": "subject-deep-dives",
  "subtopic": "english-language-arts",
  "title": "Build a close-reading lesson from an authorized supplied text",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Build a close-reading lesson from an authorized supplied text

## Use this when

You need a subject-accurate teaching resource connecting concepts, evidence and transfer focused on english language arts.

## Teacher inputs

- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

Task:
Complete this teacher task: Build a close-reading lesson from an authorized supplied text. Create a subject-accurate teaching resource connecting concepts, evidence and transfer using only the supplied inputs.

Required output:
Return: core concept; prerequisites; accurate model; worked example; misconception diagnostic; guided application; independent transfer; answer guide; subject-accuracy audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], english language arts; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

Not included in this edition.

## Teacher verification checklist

- [ ] Every fact can be traced to the teacher inputs.
- [ ] Content, answers and examples are accurate.
- [ ] Timing, materials and difficulty are feasible.
- [ ] Accessibility supports preserve the learning goal.
- [ ] A teacher reviews the result before classroom or family use.

## Editorial notes

Full-book content draft. Final editorial review is pending.


---


---
{
  "id": "SD-006",
  "slug": "create-an-evidence-based-writing-task-with-a-clear-mentor-model",
  "chapter": "subject-deep-dives",
  "subtopic": "english-language-arts",
  "title": "Create an evidence-based writing task with a clear mentor model",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create an evidence-based writing task with a clear mentor model

## Use this when

You need a subject-accurate teaching resource connecting concepts, evidence and transfer focused on english language arts.

## Teacher inputs

- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

Task:
Complete this teacher task: Create an evidence-based writing task with a clear mentor model. Create a subject-accurate teaching resource connecting concepts, evidence and transfer using only the supplied inputs.

Required output:
Return: core concept; prerequisites; accurate model; worked example; misconception diagnostic; guided application; independent transfer; answer guide; subject-accuracy audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], english language arts; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

Not included in this edition.

## Teacher verification checklist

- [ ] Every fact can be traced to the teacher inputs.
- [ ] Content, answers and examples are accurate.
- [ ] Timing, materials and difficulty are feasible.
- [ ] Accessibility supports preserve the learning goal.
- [ ] A teacher reviews the result before classroom or family use.

## Editorial notes

Full-book content draft. Final editorial review is pending.


---


---
{
  "id": "SD-007",
  "slug": "design-a-revision-lesson-that-separates-ideas-organization-and-conventions",
  "chapter": "subject-deep-dives",
  "subtopic": "english-language-arts",
  "title": "Design a revision lesson that separates ideas, organization and conventions",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Design a revision lesson that separates ideas, organization and conventions

## Use this when

You need a subject-accurate teaching resource connecting concepts, evidence and transfer focused on english language arts.

## Teacher inputs

- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

Task:
Complete this teacher task: Design a revision lesson that separates ideas, organization and conventions. Create a subject-accurate teaching resource connecting concepts, evidence and transfer using only the supplied inputs.

Required output:
Return: core concept; prerequisites; accurate model; worked example; misconception diagnostic; guided application; independent transfer; answer guide; subject-accuracy audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], english language arts; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

Not included in this edition.

## Teacher verification checklist

- [ ] Every fact can be traced to the teacher inputs.
- [ ] Content, answers and examples are accurate.
- [ ] Timing, materials and difficulty are feasible.
- [ ] Accessibility supports preserve the learning goal.
- [ ] A teacher reviews the result before classroom or family use.

## Editorial notes

Full-book content draft. Final editorial review is pending.


---


---
{
  "id": "SD-008",
  "slug": "build-a-claim-evidence-reasoning-task-from-supplied-observations",
  "chapter": "subject-deep-dives",
  "subtopic": "science",
  "title": "Build a claim-evidence-reasoning task from supplied observations",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Build a claim-evidence-reasoning task from supplied observations

## Use this when

You need a subject-accurate teaching resource connecting concepts, evidence and transfer focused on science.

## Teacher inputs

- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

Task:
Complete this teacher task: Build a claim-evidence-reasoning task from supplied observations. Create a subject-accurate teaching resource connecting concepts, evidence and transfer using only the supplied inputs.

Required output:
Return: core concept; prerequisites; accurate model; worked example; misconception diagnostic; guided application; independent transfer; answer guide; subject-accuracy audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], science; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

Not included in this edition.

## Teacher verification checklist

- [ ] Every fact can be traced to the teacher inputs.
- [ ] Content, answers and examples are accurate.
- [ ] Timing, materials and difficulty are feasible.
- [ ] Accessibility supports preserve the learning goal.
- [ ] A teacher reviews the result before classroom or family use.

## Editorial notes

Full-book content draft. Final editorial review is pending.


---


---
{
  "id": "SD-009",
  "slug": "audit-a-science-explanation-for-causation-uncertainty-and-safety",
  "chapter": "subject-deep-dives",
  "subtopic": "science",
  "title": "Audit a science explanation for causation, uncertainty and safety",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Audit a science explanation for causation, uncertainty and safety

## Use this when

You need a subject-accurate teaching resource connecting concepts, evidence and transfer focused on science.

## Teacher inputs

- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

Task:
Complete this teacher task: Audit a science explanation for causation, uncertainty and safety. Create a subject-accurate teaching resource connecting concepts, evidence and transfer using only the supplied inputs.

Required output:
Return: core concept; prerequisites; accurate model; worked example; misconception diagnostic; guided application; independent transfer; answer guide; subject-accuracy audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], science; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

Not included in this edition.

## Teacher verification checklist

- [ ] Every fact can be traced to the teacher inputs.
- [ ] Content, answers and examples are accurate.
- [ ] Timing, materials and difficulty are feasible.
- [ ] Accessibility supports preserve the learning goal.
- [ ] A teacher reviews the result before classroom or family use.

## Editorial notes

Full-book content draft. Final editorial review is pending.


---


---
{
  "id": "SD-010",
  "slug": "create-a-source-analysis-lesson-using-origin-purpose-and-context",
  "chapter": "subject-deep-dives",
  "subtopic": "social-studies",
  "title": "Create a source-analysis lesson using origin, purpose and context",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a source-analysis lesson using origin, purpose and context

## Use this when

You need a subject-accurate teaching resource connecting concepts, evidence and transfer focused on social studies.

## Teacher inputs

- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

Task:
Complete this teacher task: Create a source-analysis lesson using origin, purpose and context. Create a subject-accurate teaching resource connecting concepts, evidence and transfer using only the supplied inputs.

Required output:
Return: core concept; prerequisites; accurate model; worked example; misconception diagnostic; guided application; independent transfer; answer guide; subject-accuracy audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], social studies; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

Not included in this edition.

## Teacher verification checklist

- [ ] Every fact can be traced to the teacher inputs.
- [ ] Content, answers and examples are accurate.
- [ ] Timing, materials and difficulty are feasible.
- [ ] Accessibility supports preserve the learning goal.
- [ ] A teacher reviews the result before classroom or family use.

## Editorial notes

Full-book content draft. Final editorial review is pending.


---


---
{
  "id": "SD-011",
  "slug": "build-a-corroboration-task-with-multiple-supplied-perspectives",
  "chapter": "subject-deep-dives",
  "subtopic": "social-studies",
  "title": "Build a corroboration task with multiple supplied perspectives",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Build a corroboration task with multiple supplied perspectives

## Use this when

You need a subject-accurate teaching resource connecting concepts, evidence and transfer focused on social studies.

## Teacher inputs

- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

Task:
Complete this teacher task: Build a corroboration task with multiple supplied perspectives. Create a subject-accurate teaching resource connecting concepts, evidence and transfer using only the supplied inputs.

Required output:
Return: core concept; prerequisites; accurate model; worked example; misconception diagnostic; guided application; independent transfer; answer guide; subject-accuracy audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], social studies; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

Not included in this edition.

## Teacher verification checklist

- [ ] Every fact can be traced to the teacher inputs.
- [ ] Content, answers and examples are accurate.
- [ ] Timing, materials and difficulty are feasible.
- [ ] Accessibility supports preserve the learning goal.
- [ ] A teacher reviews the result before classroom or family use.

## Editorial notes

Full-book content draft. Final editorial review is pending.


---


---
{
  "id": "SD-012",
  "slug": "design-a-historical-claim-task-that-distinguishes-evidence-from-interpretation",
  "chapter": "subject-deep-dives",
  "subtopic": "social-studies",
  "title": "Design a historical claim task that distinguishes evidence from interpretation",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Design a historical claim task that distinguishes evidence from interpretation

## Use this when

You need a subject-accurate teaching resource connecting concepts, evidence and transfer focused on social studies.

## Teacher inputs

- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

Task:
Complete this teacher task: Design a historical claim task that distinguishes evidence from interpretation. Create a subject-accurate teaching resource connecting concepts, evidence and transfer using only the supplied inputs.

Required output:
Return: core concept; prerequisites; accurate model; worked example; misconception diagnostic; guided application; independent transfer; answer guide; subject-accuracy audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], social studies; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

Not included in this edition.

## Teacher verification checklist

- [ ] Every fact can be traced to the teacher inputs.
- [ ] Content, answers and examples are accurate.
- [ ] Timing, materials and difficulty are feasible.
- [ ] Accessibility supports preserve the learning goal.
- [ ] A teacher reviews the result before classroom or family use.

## Editorial notes

Full-book content draft. Final editorial review is pending.


---


---
{
  "id": "SD-013",
  "slug": "create-a-skill-development-lesson-with-modelling-practice-and-reflection",
  "chapter": "subject-deep-dives",
  "subtopic": "arts-physical-education-and-electives",
  "title": "Create a skill-development lesson with modelling, practice and reflection",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a skill-development lesson with modelling, practice and reflection

## Use this when

You need a subject-accurate teaching resource connecting concepts, evidence and transfer focused on arts physical education & electives.

## Teacher inputs

- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

Task:
Complete this teacher task: Create a skill-development lesson with modelling, practice and reflection. Create a subject-accurate teaching resource connecting concepts, evidence and transfer using only the supplied inputs.

Required output:
Return: core concept; prerequisites; accurate model; worked example; misconception diagnostic; guided application; independent transfer; answer guide; subject-accuracy audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], arts physical education & electives; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

Not included in this edition.

## Teacher verification checklist

- [ ] Every fact can be traced to the teacher inputs.
- [ ] Content, answers and examples are accurate.
- [ ] Timing, materials and difficulty are feasible.
- [ ] Accessibility supports preserve the learning goal.
- [ ] A teacher reviews the result before classroom or family use.

## Editorial notes

Full-book content draft. Final editorial review is pending.


---


---
{
  "id": "SD-014",
  "slug": "adapt-a-performance-task-for-space-equipment-and-physical-access",
  "chapter": "subject-deep-dives",
  "subtopic": "arts-physical-education-and-electives",
  "title": "Adapt a performance task for space, equipment and physical access",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Adapt a performance task for space, equipment and physical access

## Use this when

You need a subject-accurate teaching resource connecting concepts, evidence and transfer focused on arts physical education & electives.

## Teacher inputs

- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

Task:
Complete this teacher task: Adapt a performance task for space, equipment and physical access. Create a subject-accurate teaching resource connecting concepts, evidence and transfer using only the supplied inputs.

Required output:
Return: core concept; prerequisites; accurate model; worked example; misconception diagnostic; guided application; independent transfer; answer guide; subject-accuracy audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], arts physical education & electives; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

Not included in this edition.

## Teacher verification checklist

- [ ] Every fact can be traced to the teacher inputs.
- [ ] Content, answers and examples are accurate.
- [ ] Timing, materials and difficulty are feasible.
- [ ] Accessibility supports preserve the learning goal.
- [ ] A teacher reviews the result before classroom or family use.

## Editorial notes

Full-book content draft. Final editorial review is pending.


---


---
{
  "id": "SD-015",
  "slug": "build-an-observable-process-rubric-for-an-arts-pe-or-elective-task",
  "chapter": "subject-deep-dives",
  "subtopic": "arts-physical-education-and-electives",
  "title": "Build an observable process rubric for an arts, PE or elective task",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Build an observable process rubric for an arts, PE or elective task

## Use this when

You need a subject-accurate teaching resource connecting concepts, evidence and transfer focused on arts physical education & electives.

## Teacher inputs

- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND: learner age or grade]`
- `[SUBJECT_AND_CONTEXT: exact course, unit or situation]`
- `[GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable]`
- `[VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information]`
- `[TIME_LENGTH_AND_FORMAT_CONSTRAINTS]`
- `[AVAILABLE_MATERIALS_OR_SUPPORTS]`
- `[SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS]`

Task:
Complete this teacher task: Build an observable process rubric for an arts, PE or elective task. Create a subject-accurate teaching resource connecting concepts, evidence and transfer using only the supplied inputs.

Required output:
Return: core concept; prerequisites; accurate model; worked example; misconception diagnostic; guided application; independent transfer; answer guide; subject-accuracy audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], arts physical education & electives; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

Not included in this edition.

## Teacher verification checklist

- [ ] Every fact can be traced to the teacher inputs.
- [ ] Content, answers and examples are accurate.
- [ ] Timing, materials and difficulty are feasible.
- [ ] Accessibility supports preserve the learning goal.
- [ ] A teacher reviews the result before classroom or family use.

## Editorial notes

Full-book content draft. Final editorial review is pending.


---
