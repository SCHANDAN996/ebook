# Chapter 3: Assessment, Rubrics & Quizzes

Assessment quality depends on what an item reveals. This chapter contains 40 prompts for
quizzes, formative checks, exit tickets, rubrics, misconception diagnosis, answer keys and
standards-based grading support. The aim is not to generate more questions; it is to obtain
better evidence for the next instructional decision.

## How to use this chapter

Provide the objective, content boundaries, time limit, permitted formats and intended
cognitive balance. Tell the model which misconceptions you actually want distractors to
diagnose. When building a rubric, describe observable evidence and avoid scoring personality,
neatness or compliance unless those features are explicitly part of the task.

## Non-negotiable verification

Solve every question independently and confirm that one—and only one—multiple-choice answer
is correct. Check reading load, point totals and alignment. AI-generated answer keys can be
wrong even when their explanations sound confident. Do not publish an assessment until a
qualified teacher has reviewed every item, solution and scoring rule.


---


---
{
  "id": "AS-001",
  "slug": "create-a-balanced-classroom-assessment",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "quizzes-and-tests",
  "title": "Create a balanced classroom assessment",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a balanced classroom assessment

## Use this when

You need a valid assessment with diagnostic distractors.

## Teacher inputs

- `[GRADE_BAND]`
- `[SUBJECT_AND_SKILLS]`
- `[TIME_LIMIT]`
- `[ITEM_COUNT]`
- `[ITEM_FORMATS]`
- `[COGNITIVE_BALANCE]`
- `[ACCOMMODATIONS]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND]`
- `[SUBJECT_AND_SKILLS]`
- `[TIME_LIMIT]`
- `[ITEM_COUNT]`
- `[ITEM_FORMATS]`
- `[COGNITIVE_BALANCE]`
- `[ACCOMMODATIONS]`

Task:
Create an assessment that samples recall, application and reasoning.

Required output:
Return: student directions; numbered items; point values; complete answer key; worked solutions where needed; distractor rationale; scoring guide; standards/objective map; two priority items for reteaching analysis.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 8 mathematics; one-variable linear equations; 20 minutes; 8 items; 5 multiple choice and 3 constructed response.

## Sample output

**Illustrative excerpt — Grade 8 linear equations**

1. Solve `x - 9 = -4`. A −13, B 5, C 13, D −5. **Answer: B.** Choosing A suggests the
same operation was used instead of the inverse.
2. Solve `4(y - 3) = 20` and show each step. **Answer:** `y = 8`.
3. Explain why `6x + 4 = 2(3x + 5)` has no solution. **Answer:** expanding gives
`6x + 4 = 6x + 10`; subtracting `6x` leaves the false statement `4 = 10`.

**Decision rule:** 3/3 secure; 2/3 check the error code; 0-1/3 reteach inverse operations
with balance models. Inspect Question 3 first when deciding whether learners distinguish
no solution from infinitely many solutions.

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
  "id": "AS-002",
  "slug": "create-hinge-questions-for-live-teaching",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "formative-checks-and-exit-tickets",
  "title": "Create hinge questions for live teaching",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
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

**Illustrative excerpt — Grade 8 linear equations**

1. Solve `x - 9 = -4`. A −13, B 5, C 13, D −5. **Answer: B.** Choosing A suggests the
same operation was used instead of the inverse.
2. Solve `4(y - 3) = 20` and show each step. **Answer:** `y = 8`.
3. Explain why `6x + 4 = 2(3x + 5)` has no solution. **Answer:** expanding gives
`6x + 4 = 6x + 10`; subtracting `6x` leaves the false statement `4 = 10`.

**Decision rule:** 3/3 secure; 2/3 check the error code; 0-1/3 reteach inverse operations
with balance models. Inspect Question 3 first when deciding whether learners distinguish
no solution from infinitely many solutions.

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
  "id": "AS-003",
  "slug": "build-a-student-readable-analytic-rubric",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "rubrics",
  "title": "Build a student-readable analytic rubric",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Build a student-readable analytic rubric

## Use this when

A complex product needs transparent, observable criteria.

## Teacher inputs

- `[GRADE_BAND]`
- `[TASK_DESCRIPTION]`
- `[LEARNING_OBJECTIVES]`
- `[CRITERIA_COUNT]`
- `[PERFORMANCE_LEVELS]`
- `[TOTAL_POINTS]`
- `[NON_NEGOTIABLES]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND]`
- `[TASK_DESCRIPTION]`
- `[LEARNING_OBJECTIVES]`
- `[CRITERIA_COUNT]`
- `[PERFORMANCE_LEVELS]`
- `[TOTAL_POINTS]`
- `[NON_NEGOTIABLES]`

Task:
Create a rubric that scores evidence of learning rather than compliance or personality.

Required output:
Return: rubric table; observable descriptors for every cell; point calculation; student checklist; calibration examples using fictional work; teacher note on avoiding double-penalties; accessibility review.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 7 science ecosystem model; 4 criteria; four levels; 16 points; causal arrows and evidence explanation required.

## Sample output

**Illustrative excerpt — Grade 8 linear equations**

1. Solve `x - 9 = -4`. A −13, B 5, C 13, D −5. **Answer: B.** Choosing A suggests the
same operation was used instead of the inverse.
2. Solve `4(y - 3) = 20` and show each step. **Answer:** `y = 8`.
3. Explain why `6x + 4 = 2(3x + 5)` has no solution. **Answer:** expanding gives
`6x + 4 = 6x + 10`; subtracting `6x` leaves the false statement `4 = 10`.

**Decision rule:** 3/3 secure; 2/3 check the error code; 0-1/3 reteach inverse operations
with balance models. Inspect Question 3 first when deciding whether learners distinguish
no solution from infinitely many solutions.

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
  "id": "AS-004",
  "slug": "diagnose-errors-from-anonymous-work",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "diagnosis-and-misconceptions",
  "title": "Diagnose errors from anonymous work",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Diagnose errors from anonymous work

## Use this when

You have non-identifying student responses and need instructional patterns.

## Teacher inputs

- `[GRADE_BAND]`
- `[SUBJECT_AND_SKILL]`
- `[TASK_AND_CORRECT_ANSWER]`
- `[ANONYMOUS_RESPONSES]`
- `[SCORING_CRITERIA]`
- `[NUMBER_OF_GROUPS_FOR_RETEACHING]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND]`
- `[SUBJECT_AND_SKILL]`
- `[TASK_AND_CORRECT_ANSWER]`
- `[ANONYMOUS_RESPONSES]`
- `[SCORING_CRITERIA]`
- `[NUMBER_OF_GROUPS_FOR_RETEACHING]`

Task:
Analyze response patterns without inferring ability, motivation or personal traits.

Required output:
Return: response-by-response evidence; misconception codes; frequency table; confidence/uncertainty notes; flexible reteaching groups; one targeted mini-task per group; reassessment question. Preserve original responses exactly.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 6 fractions; compare unlike fractions; 12 responses labeled A-L; three reteaching groups.

## Sample output

**Illustrative excerpt — Grade 8 linear equations**

1. Solve `x - 9 = -4`. A −13, B 5, C 13, D −5. **Answer: B.** Choosing A suggests the
same operation was used instead of the inverse.
2. Solve `4(y - 3) = 20` and show each step. **Answer:** `y = 8`.
3. Explain why `6x + 4 = 2(3x + 5)` has no solution. **Answer:** expanding gives
`6x + 4 = 6x + 10`; subtracting `6x` leaves the false statement `4 = 10`.

**Decision rule:** 3/3 secure; 2/3 check the error code; 0-1/3 reteach inverse operations
with balance models. Inspect Question 3 first when deciding whether learners distinguish
no solution from infinitely many solutions.

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
  "id": "AS-005",
  "slug": "build-a-short-quiz-across-recall-application-and-reasoning",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "quizzes-and-tests",
  "title": "Build a short quiz across recall, application and reasoning",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Build a short quiz across recall, application and reasoning

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on quizzes & tests.

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
Complete this teacher task: Build a short quiz across recall, application and reasoning. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], quizzes & tests; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

**Illustrative excerpt — Grade 8 linear equations**

1. Solve `x - 9 = -4`. A −13, B 5, C 13, D −5. **Answer: B.** Choosing A suggests the
same operation was used instead of the inverse.
2. Solve `4(y - 3) = 20` and show each step. **Answer:** `y = 8`.
3. Explain why `6x + 4 = 2(3x + 5)` has no solution. **Answer:** expanding gives
`6x + 4 = 6x + 10`; subtracting `6x` leaves the false statement `4 = 10`.

**Decision rule:** 3/3 secure; 2/3 check the error code; 0-1/3 reteach inverse operations
with balance models. Inspect Question 3 first when deciding whether learners distinguish
no solution from infinitely many solutions.

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
  "id": "AS-006",
  "slug": "write-diagnostic-multiple-choice-questions-with-purposeful-distractors",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "quizzes-and-tests",
  "title": "Write diagnostic multiple-choice questions with purposeful distractors",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Write diagnostic multiple-choice questions with purposeful distractors

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on quizzes & tests.

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
Complete this teacher task: Write diagnostic multiple-choice questions with purposeful distractors. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], quizzes & tests; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

**Illustrative excerpt — Grade 8 linear equations**

1. Solve `x - 9 = -4`. A −13, B 5, C 13, D −5. **Answer: B.** Choosing A suggests the
same operation was used instead of the inverse.
2. Solve `4(y - 3) = 20` and show each step. **Answer:** `y = 8`.
3. Explain why `6x + 4 = 2(3x + 5)` has no solution. **Answer:** expanding gives
`6x + 4 = 6x + 10`; subtracting `6x` leaves the false statement `4 = 10`.

**Decision rule:** 3/3 secure; 2/3 check the error code; 0-1/3 reteach inverse operations
with balance models. Inspect Question 3 first when deciding whether learners distinguish
no solution from infinitely many solutions.

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
  "id": "AS-007",
  "slug": "create-a-constructed-response-assessment-with-a-scoring-guide",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "quizzes-and-tests",
  "title": "Create a constructed-response assessment with a scoring guide",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a constructed-response assessment with a scoring guide

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on quizzes & tests.

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
Complete this teacher task: Create a constructed-response assessment with a scoring guide. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], quizzes & tests; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

**Illustrative excerpt — Grade 8 linear equations**

1. Solve `x - 9 = -4`. A −13, B 5, C 13, D −5. **Answer: B.** Choosing A suggests the
same operation was used instead of the inverse.
2. Solve `4(y - 3) = 20` and show each step. **Answer:** `y = 8`.
3. Explain why `6x + 4 = 2(3x + 5)` has no solution. **Answer:** expanding gives
`6x + 4 = 6x + 10`; subtracting `6x` leaves the false statement `4 = 10`.

**Decision rule:** 3/3 secure; 2/3 check the error code; 0-1/3 reteach inverse operations
with balance models. Inspect Question 3 first when deciding whether learners distinguish
no solution from infinitely many solutions.

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
  "id": "AS-008",
  "slug": "design-a-pre-assessment-that-separates-prerequisite-and-grade-level-skills",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "quizzes-and-tests",
  "title": "Design a pre-assessment that separates prerequisite and grade-level skills",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Design a pre-assessment that separates prerequisite and grade-level skills

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on quizzes & tests.

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
Complete this teacher task: Design a pre-assessment that separates prerequisite and grade-level skills. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], quizzes & tests; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

**Illustrative excerpt — Grade 8 linear equations**

1. Solve `x - 9 = -4`. A −13, B 5, C 13, D −5. **Answer: B.** Choosing A suggests the
same operation was used instead of the inverse.
2. Solve `4(y - 3) = 20` and show each step. **Answer:** `y = 8`.
3. Explain why `6x + 4 = 2(3x + 5)` has no solution. **Answer:** expanding gives
`6x + 4 = 6x + 10`; subtracting `6x` leaves the false statement `4 = 10`.

**Decision rule:** 3/3 secure; 2/3 check the error code; 0-1/3 reteach inverse operations
with balance models. Inspect Question 3 first when deciding whether learners distinguish
no solution from infinitely many solutions.

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
  "id": "AS-009",
  "slug": "build-a-cumulative-assessment-without-over-weighting-recent-lessons",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "quizzes-and-tests",
  "title": "Build a cumulative assessment without over-weighting recent lessons",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Build a cumulative assessment without over-weighting recent lessons

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on quizzes & tests.

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
Complete this teacher task: Build a cumulative assessment without over-weighting recent lessons. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], quizzes & tests; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-010",
  "slug": "adapt-an-assessment-for-a-shorter-testing-period",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "quizzes-and-tests",
  "title": "Adapt an assessment for a shorter testing period",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Adapt an assessment for a shorter testing period

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on quizzes & tests.

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
Complete this teacher task: Adapt an assessment for a shorter testing period. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], quizzes & tests; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-011",
  "slug": "create-parallel-assessment-forms-with-equivalent-demand",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "quizzes-and-tests",
  "title": "Create parallel assessment forms with equivalent demand",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create parallel assessment forms with equivalent demand

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on quizzes & tests.

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
Complete this teacher task: Create parallel assessment forms with equivalent demand. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], quizzes & tests; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-012",
  "slug": "audit-a-test-for-alignment-ambiguity-and-answer-key-errors",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "quizzes-and-tests",
  "title": "Audit a test for alignment, ambiguity and answer-key errors",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Audit a test for alignment, ambiguity and answer-key errors

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on quizzes & tests.

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
Complete this teacher task: Audit a test for alignment, ambiguity and answer-key errors. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], quizzes & tests; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-013",
  "slug": "turn-a-supplied-objective-list-into-a-complete-assessment-blueprint",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "quizzes-and-tests",
  "title": "Turn a supplied objective list into a complete assessment blueprint",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Turn a supplied objective list into a complete assessment blueprint

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on quizzes & tests.

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
Complete this teacher task: Turn a supplied objective list into a complete assessment blueprint. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], quizzes & tests; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-014",
  "slug": "build-a-five-minute-check-for-understanding-during-instruction",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "formative-checks-and-exit-tickets",
  "title": "Build a five-minute check for understanding during instruction",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Build a five-minute check for understanding during instruction

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on formative checks & exit tickets.

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
Complete this teacher task: Build a five-minute check for understanding during instruction. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], formative checks & exit tickets; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-015",
  "slug": "write-an-exit-ticket-that-distinguishes-three-levels-of-understanding",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "formative-checks-and-exit-tickets",
  "title": "Write an exit ticket that distinguishes three levels of understanding",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Write an exit ticket that distinguishes three levels of understanding

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on formative checks & exit tickets.

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
Complete this teacher task: Write an exit ticket that distinguishes three levels of understanding. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], formative checks & exit tickets; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-016",
  "slug": "create-a-misconception-poll-with-actionable-response-options",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "formative-checks-and-exit-tickets",
  "title": "Create a misconception poll with actionable response options",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a misconception poll with actionable response options

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on formative checks & exit tickets.

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
Complete this teacher task: Create a misconception poll with actionable response options. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], formative checks & exit tickets; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-017",
  "slug": "design-a-show-me-task-using-mini-whiteboards-or-paper",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "formative-checks-and-exit-tickets",
  "title": "Design a show-me task using mini-whiteboards or paper",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Design a show-me task using mini-whiteboards or paper

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on formative checks & exit tickets.

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
Complete this teacher task: Design a show-me task using mini-whiteboards or paper. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], formative checks & exit tickets; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-018",
  "slug": "turn-anonymous-responses-into-a-next-day-formative-check",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "formative-checks-and-exit-tickets",
  "title": "Turn anonymous responses into a next-day formative check",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Turn anonymous responses into a next-day formative check

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on formative checks & exit tickets.

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
Complete this teacher task: Turn anonymous responses into a next-day formative check. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], formative checks & exit tickets; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-019",
  "slug": "create-a-transfer-question-that-reveals-reasoning-rather-than-recall",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "formative-checks-and-exit-tickets",
  "title": "Create a transfer question that reveals reasoning rather than recall",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a transfer question that reveals reasoning rather than recall

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on formative checks & exit tickets.

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
Complete this teacher task: Create a transfer question that reveals reasoning rather than recall. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], formative checks & exit tickets; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-020",
  "slug": "audit-a-formative-check-for-speed-reading-load-and-decision-usefulness",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "formative-checks-and-exit-tickets",
  "title": "Audit a formative check for speed, reading load and decision usefulness",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Audit a formative check for speed, reading load and decision usefulness

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on formative checks & exit tickets.

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
Complete this teacher task: Audit a formative check for speed, reading load and decision usefulness. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], formative checks & exit tickets; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-021",
  "slug": "create-observable-descriptors-for-four-performance-levels",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "rubrics",
  "title": "Create observable descriptors for four performance levels",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create observable descriptors for four performance levels

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on rubrics.

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
Complete this teacher task: Create observable descriptors for four performance levels. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], rubrics; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-022",
  "slug": "turn-an-objective-and-task-into-aligned-rubric-criteria",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "rubrics",
  "title": "Turn an objective and task into aligned rubric criteria",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Turn an objective and task into aligned rubric criteria

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on rubrics.

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
Complete this teacher task: Turn an objective and task into aligned rubric criteria. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], rubrics; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-023",
  "slug": "build-a-single-point-rubric-with-feedback-space",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "rubrics",
  "title": "Build a single-point rubric with feedback space",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Build a single-point rubric with feedback space

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on rubrics.

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
Complete this teacher task: Build a single-point rubric with feedback space. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], rubrics; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-024",
  "slug": "create-a-rubric-for-collaborative-work-with-individual-evidence",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "rubrics",
  "title": "Create a rubric for collaborative work with individual evidence",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a rubric for collaborative work with individual evidence

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on rubrics.

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
Complete this teacher task: Create a rubric for collaborative work with individual evidence. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], rubrics; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-025",
  "slug": "rewrite-vague-rubric-words-as-observable-evidence",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "rubrics",
  "title": "Rewrite vague rubric words as observable evidence",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Rewrite vague rubric words as observable evidence

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on rubrics.

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
Complete this teacher task: Rewrite vague rubric words as observable evidence. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], rubrics; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-026",
  "slug": "calibrate-a-rubric-using-fictional-work-samples",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "rubrics",
  "title": "Calibrate a rubric using fictional work samples",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Calibrate a rubric using fictional work samples

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on rubrics.

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
Complete this teacher task: Calibrate a rubric using fictional work samples. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], rubrics; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-027",
  "slug": "audit-a-rubric-for-double-penalties-bias-and-irrelevant-criteria",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "rubrics",
  "title": "Audit a rubric for double penalties, bias and irrelevant criteria",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Audit a rubric for double penalties, bias and irrelevant criteria

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on rubrics.

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
Complete this teacher task: Audit a rubric for double penalties, bias and irrelevant criteria. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], rubrics; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-028",
  "slug": "code-anonymous-responses-by-misconception-rather-than-score-alone",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "diagnosis-and-misconceptions",
  "title": "Code anonymous responses by misconception rather than score alone",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Code anonymous responses by misconception rather than score alone

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on diagnosis & misconceptions.

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
Complete this teacher task: Code anonymous responses by misconception rather than score alone. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], diagnosis & misconceptions; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-029",
  "slug": "build-flexible-reteaching-groups-from-response-patterns",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "diagnosis-and-misconceptions",
  "title": "Build flexible reteaching groups from response patterns",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Build flexible reteaching groups from response patterns

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on diagnosis & misconceptions.

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
Complete this teacher task: Build flexible reteaching groups from response patterns. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], diagnosis & misconceptions; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-030",
  "slug": "distinguish-a-careless-slip-from-a-conceptual-misunderstanding",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "diagnosis-and-misconceptions",
  "title": "Distinguish a careless slip from a conceptual misunderstanding",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Distinguish a careless slip from a conceptual misunderstanding

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on diagnosis & misconceptions.

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
Complete this teacher task: Distinguish a careless slip from a conceptual misunderstanding. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], diagnosis & misconceptions; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-031",
  "slug": "create-targeted-mini-tasks-for-three-misconception-groups",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "diagnosis-and-misconceptions",
  "title": "Create targeted mini-tasks for three misconception groups",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create targeted mini-tasks for three misconception groups

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on diagnosis & misconceptions.

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
Complete this teacher task: Create targeted mini-tasks for three misconception groups. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], diagnosis & misconceptions; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-032",
  "slug": "plan-a-reassessment-that-shows-whether-reteaching-worked",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "diagnosis-and-misconceptions",
  "title": "Plan a reassessment that shows whether reteaching worked",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Plan a reassessment that shows whether reteaching worked

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on diagnosis & misconceptions.

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
Complete this teacher task: Plan a reassessment that shows whether reteaching worked. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], diagnosis & misconceptions; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-033",
  "slug": "create-a-complete-worked-answer-key-from-verified-questions",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "answer-keys-and-feedback",
  "title": "Create a complete worked answer key from verified questions",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a complete worked answer key from verified questions

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on answer keys & feedback.

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
Complete this teacher task: Create a complete worked answer key from verified questions. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], answer keys & feedback; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-034",
  "slug": "write-actionable-feedback-matched-to-common-response-patterns",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "answer-keys-and-feedback",
  "title": "Write actionable feedback matched to common response patterns",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Write actionable feedback matched to common response patterns

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on answer keys & feedback.

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
Complete this teacher task: Write actionable feedback matched to common response patterns. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], answer keys & feedback; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-035",
  "slug": "audit-an-answer-key-for-mathematical-factual-and-scoring-errors",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "answer-keys-and-feedback",
  "title": "Audit an answer key for mathematical, factual and scoring errors",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Audit an answer key for mathematical, factual and scoring errors

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on answer keys & feedback.

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
Complete this teacher task: Audit an answer key for mathematical, factual and scoring errors. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], answer keys & feedback; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-036",
  "slug": "create-learner-friendly-solution-explanations-without-hiding-reasoning",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "answer-keys-and-feedback",
  "title": "Create learner-friendly solution explanations without hiding reasoning",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create learner-friendly solution explanations without hiding reasoning

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on answer keys & feedback.

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
Complete this teacher task: Create learner-friendly solution explanations without hiding reasoning. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], answer keys & feedback; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-037",
  "slug": "map-assessment-evidence-to-supplied-standards-and-objectives",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "standards-based-grading",
  "title": "Map assessment evidence to supplied standards and objectives",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Map assessment evidence to supplied standards and objectives

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on standards based grading.

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
Complete this teacher task: Map assessment evidence to supplied standards and objectives. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], standards based grading; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-038",
  "slug": "create-a-standards-based-proficiency-scale-with-observable-evidence",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "standards-based-grading",
  "title": "Create a standards-based proficiency scale with observable evidence",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a standards-based proficiency scale with observable evidence

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on standards based grading.

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
Complete this teacher task: Create a standards-based proficiency scale with observable evidence. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], standards based grading; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-039",
  "slug": "summarize-class-mastery-without-averaging-unrelated-skills",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "standards-based-grading",
  "title": "Summarize class mastery without averaging unrelated skills",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Summarize class mastery without averaging unrelated skills

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on standards based grading.

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
Complete this teacher task: Summarize class mastery without averaging unrelated skills. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], standards based grading; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "AS-040",
  "slug": "audit-a-standards-based-grade-summary-for-missing-or-weak-evidence",
  "chapter": "assessment-rubrics-quizzes",
  "subtopic": "standards-based-grading",
  "title": "Audit a standards-based grade summary for missing or weak evidence",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Audit a standards-based grade summary for missing or weak evidence

## Use this when

You need a valid classroom assessment resource aligned to the supplied objective focused on standards based grading.

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
Complete this teacher task: Audit a standards-based grade summary for missing or weak evidence. Create a valid classroom assessment resource aligned to the supplied objective using only the supplied inputs.

Required output:
Return: student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], standards based grading; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
