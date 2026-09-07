# Chapter 1: Lesson Planning

Good lesson planning begins with evidence, not activities. Before asking AI for a lesson,
decide what learners should understand or do and what would count as convincing proof.
The 60 prompts in this chapter cover complete lessons, backward unit planning, standards,
objectives, openings, exit tickets, pacing, substitute plans, projects and reflection.

## How to use this chapter

Start with the smallest prompt that matches the job. Supply the grade, exact objective,
time, available materials and relevant learner context. If a standard must be followed,
paste its exact wording rather than asking the model to recall it. Treat suggested timings
as a draft: walking across a room, distributing materials and answering questions all take
real time.

## Before teaching

Confirm that every activity produces evidence connected to the objective. Check subject
accuracy, reading demand, safety, accessibility and material availability. Replace generic
teacher language with words that sound natural in your classroom. A polished plan is not
proof that the lesson will work; your knowledge of the learners remains the final filter.


---


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

**Illustrative excerpt — Grade 6 science, 50 minutes**

**Objective:** I can draw and label a model showing how a plant uses sunlight, water and
carbon dioxide to make sugar and release oxygen.

**Sequence:** 0-5 min: students answer, “Where does a plant's food come from?” 5-15 min:
teacher models a plant as a solar-powered food factory and labels three inputs and two
outputs. 15-30 min: pairs sort input/output cards and justify each placement. 30-43 min:
students independently draw an arrow model and add a one-sentence explanation. 43-50 min:
exit ticket—“Can a watered plant make sugar without carbon dioxide? Explain using *input*.”

**Evidence:** A secure response shows all five substances in the correct direction and
explains that sugar is made rather than absorbed from soil. **Reteach trigger:** If more
than 25% label sugar as an input, begin the next lesson with a carbon-source model.

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
  "id": "LP-002",
  "slug": "plan-a-unit-backward-from-mastery",
  "chapter": "lesson-planning",
  "subtopic": "backward-unit-planning",
  "title": "Plan a unit backward from mastery",
  "grade_bands": ["6-12"],
  "subjects": ["Mathematics"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Plan a unit backward from mastery

## Use this when

You have an end goal and need a coherent learning sequence.

## Teacher inputs

- `[GRADE_BAND]`
- `[SUBJECT_AND_UNIT]`
- `[NUMBER_AND_LENGTH_OF_LESSONS]`
- `[FINAL_MASTERY_EXPECTATION]`
- `[REQUIRED_STANDARDS]`
- `[KNOWN_PRIOR_KNOWLEDGE]`
- `[AVAILABLE_RESOURCES]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND]`
- `[SUBJECT_AND_UNIT]`
- `[NUMBER_AND_LENGTH_OF_LESSONS]`
- `[FINAL_MASTERY_EXPECTATION]`
- `[REQUIRED_STANDARDS]`
- `[KNOWN_PRIOR_KNOWLEDGE]`
- `[AVAILABLE_RESOURCES]`

Task:
Design a backward-planned unit in which every lesson builds toward final mastery.

Required output:
Return: unpacked mastery criteria; final assessment; prerequisite map; lesson sequence table; formative checkpoints; reteaching triggers; extension path; resource list; alignment self-check.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 8 mathematics; linear equations; 8 lessons of 45 minutes; solve and justify one-variable equations; students know integer operations.

## Sample output

**Illustrative excerpt — Grade 6 science, 50 minutes**

**Objective:** I can draw and label a model showing how a plant uses sunlight, water and
carbon dioxide to make sugar and release oxygen.

**Sequence:** 0-5 min: students answer, “Where does a plant's food come from?” 5-15 min:
teacher models a plant as a solar-powered food factory and labels three inputs and two
outputs. 15-30 min: pairs sort input/output cards and justify each placement. 30-43 min:
students independently draw an arrow model and add a one-sentence explanation. 43-50 min:
exit ticket—“Can a watered plant make sugar without carbon dioxide? Explain using *input*.”

**Evidence:** A secure response shows all five substances in the correct direction and
explains that sugar is made rather than absorbed from soil. **Reteach trigger:** If more
than 25% label sugar as an input, begin the next lesson with a carbon-source model.

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
  "id": "LP-003",
  "slug": "turn-a-standard-into-measurable-objectives",
  "chapter": "lesson-planning",
  "subtopic": "standards-and-objectives",
  "title": "Turn a standard into measurable objectives",
  "grade_bands": ["K-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
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

**Illustrative excerpt — Grade 6 science, 50 minutes**

**Objective:** I can draw and label a model showing how a plant uses sunlight, water and
carbon dioxide to make sugar and release oxygen.

**Sequence:** 0-5 min: students answer, “Where does a plant's food come from?” 5-15 min:
teacher models a plant as a solar-powered food factory and labels three inputs and two
outputs. 15-30 min: pairs sort input/output cards and justify each placement. 30-43 min:
students independently draw an arrow model and add a one-sentence explanation. 43-50 min:
exit ticket—“Can a watered plant make sugar without carbon dioxide? Explain using *input*.”

**Evidence:** A secure response shows all five substances in the correct direction and
explains that sugar is made rather than absorbed from soil. **Reteach trigger:** If more
than 25% label sugar as an input, begin the next lesson with a carbon-source model.

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
  "id": "LP-004",
  "slug": "create-a-matched-warm-up-and-exit-ticket",
  "chapter": "lesson-planning",
  "subtopic": "warm-ups-and-exit-tickets",
  "title": "Create a matched warm-up and exit ticket",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a matched warm-up and exit ticket

## Use this when

You want to expose prior knowledge and measure growth in one lesson.

## Teacher inputs

- `[GRADE_BAND]`
- `[SUBJECT_AND_TOPIC]`
- `[OBJECTIVE]`
- `[WARM_UP_MINUTES]`
- `[EXIT_TICKET_MINUTES]`
- `[KNOWN_MISCONCEPTION]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND]`
- `[SUBJECT_AND_TOPIC]`
- `[OBJECTIVE]`
- `[WARM_UP_MINUTES]`
- `[EXIT_TICKET_MINUTES]`
- `[KNOWN_MISCONCEPTION]`

Task:
Create two brief tasks aligned to the same learning target.

Required output:
Return: warm-up instructions and answer guide; what each response reveals; bridge into instruction; exit-ticket question and answer guide; 3 response categories (secure/developing/not yet); next-day action for each category.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 7 science; food webs; explain indirect ecosystem effects; 5 minutes each; students think only directly connected organisms are affected.

## Sample output

**Illustrative excerpt — Grade 6 science, 50 minutes**

**Objective:** I can draw and label a model showing how a plant uses sunlight, water and
carbon dioxide to make sugar and release oxygen.

**Sequence:** 0-5 min: students answer, “Where does a plant's food come from?” 5-15 min:
teacher models a plant as a solar-powered food factory and labels three inputs and two
outputs. 15-30 min: pairs sort input/output cards and justify each placement. 30-43 min:
students independently draw an arrow model and add a one-sentence explanation. 43-50 min:
exit ticket—“Can a watered plant make sugar without carbon dioxide? Explain using *input*.”

**Evidence:** A secure response shows all five substances in the correct direction and
explains that sugar is made rather than absorbed from soil. **Reteach trigger:** If more
than 25% label sugar as an input, begin the next lesson with a carbon-source model.

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
  "id": "LP-005",
  "slug": "create-a-no-surprises-substitute-lesson",
  "chapter": "lesson-planning",
  "subtopic": "substitute-and-emergency-plans",
  "title": "Create a no-surprises substitute lesson",
  "grade_bands": ["K-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a no-surprises substitute lesson

## Use this when

A substitute teacher needs a safe, self-contained plan with minimal preparation.

## Teacher inputs

- `[GRADE_BAND]`
- `[SUBJECT_AND_TOPIC]`
- `[DURATION_MINUTES]`
- `[MATERIALS_ALREADY_IN_ROOM]`
- `[STUDENT_ROUTINES]`
- `[ACCESSIBILITY_NEEDS: non-identifying]`
- `[PROHIBITED_ACTIVITIES_OR_RESOURCES]`

## Copy-paste prompt

```text
You are an experienced K-12 instructional planning assistant.

Teacher inputs:
- `[GRADE_BAND]`
- `[SUBJECT_AND_TOPIC]`
- `[DURATION_MINUTES]`
- `[MATERIALS_ALREADY_IN_ROOM]`
- `[STUDENT_ROUTINES]`
- `[ACCESSIBILITY_NEEDS: non-identifying]`
- `[PROHIBITED_ACTIVITIES_OR_RESOURCES]`

Task:
Write a substitute plan that another adult can run without guessing.

Required output:
Return: one-page overview; minute-by-minute plan; exact directions to read aloud; attendance and safety notes as placeholders; independent task; early-finisher option; answer key; collection procedure; contingency if technology fails. Never invent school procedures.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Grade 4 social studies; map skills; 55 minutes; atlases and paper; no devices; established pair-share routine.

## Sample output

**Illustrative excerpt — Grade 6 science, 50 minutes**

**Objective:** I can draw and label a model showing how a plant uses sunlight, water and
carbon dioxide to make sugar and release oxygen.

**Sequence:** 0-5 min: students answer, “Where does a plant's food come from?” 5-15 min:
teacher models a plant as a solar-powered food factory and labels three inputs and two
outputs. 15-30 min: pairs sort input/output cards and justify each placement. 30-43 min:
students independently draw an arrow model and add a one-sentence explanation. 43-50 min:
exit ticket—“Can a watered plant make sugar without carbon dioxide? Explain using *input*.”

**Evidence:** A secure response shows all five substances in the correct direction and
explains that sugar is made rather than absorbed from soil. **Reteach trigger:** If more
than 25% label sugar as an input, begin the next lesson with a carbon-source model.

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
  "id": "LP-006",
  "slug": "plan-a-concept-development-lesson-from-prior-knowledge",
  "chapter": "lesson-planning",
  "subtopic": "complete-lessons",
  "title": "Plan a concept-development lesson from prior knowledge",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Plan a concept-development lesson from prior knowledge

## Use this when

You need a classroom-ready instructional plan focused on complete lessons.

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
Complete this teacher task: Plan a concept-development lesson from prior knowledge. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], complete lessons; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

**Illustrative excerpt — Grade 6 science, 50 minutes**

**Objective:** I can draw and label a model showing how a plant uses sunlight, water and
carbon dioxide to make sugar and release oxygen.

**Sequence:** 0-5 min: students answer, “Where does a plant's food come from?” 5-15 min:
teacher models a plant as a solar-powered food factory and labels three inputs and two
outputs. 15-30 min: pairs sort input/output cards and justify each placement. 30-43 min:
students independently draw an arrow model and add a one-sentence explanation. 43-50 min:
exit ticket—“Can a watered plant make sugar without carbon dioxide? Explain using *input*.”

**Evidence:** A secure response shows all five substances in the correct direction and
explains that sugar is made rather than absorbed from soil. **Reteach trigger:** If more
than 25% label sugar as an input, begin the next lesson with a carbon-source model.

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
  "id": "LP-007",
  "slug": "plan-an-inquiry-lesson-around-a-puzzling-phenomenon",
  "chapter": "lesson-planning",
  "subtopic": "complete-lessons",
  "title": "Plan an inquiry lesson around a puzzling phenomenon",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Plan an inquiry lesson around a puzzling phenomenon

## Use this when

You need a classroom-ready instructional plan focused on complete lessons.

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
Complete this teacher task: Plan an inquiry lesson around a puzzling phenomenon. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], complete lessons; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

**Illustrative excerpt — Grade 6 science, 50 minutes**

**Objective:** I can draw and label a model showing how a plant uses sunlight, water and
carbon dioxide to make sugar and release oxygen.

**Sequence:** 0-5 min: students answer, “Where does a plant's food come from?” 5-15 min:
teacher models a plant as a solar-powered food factory and labels three inputs and two
outputs. 15-30 min: pairs sort input/output cards and justify each placement. 30-43 min:
students independently draw an arrow model and add a one-sentence explanation. 43-50 min:
exit ticket—“Can a watered plant make sugar without carbon dioxide? Explain using *input*.”

**Evidence:** A secure response shows all five substances in the correct direction and
explains that sugar is made rather than absorbed from soil. **Reteach trigger:** If more
than 25% label sugar as an input, begin the next lesson with a carbon-source model.

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
  "id": "LP-008",
  "slug": "create-an-explicit-instruction-lesson-with-guided-release",
  "chapter": "lesson-planning",
  "subtopic": "complete-lessons",
  "title": "Create an explicit-instruction lesson with guided release",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Create an explicit-instruction lesson with guided release

## Use this when

You need a classroom-ready instructional plan focused on complete lessons.

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
Complete this teacher task: Create an explicit-instruction lesson with guided release. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], complete lessons; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

**Illustrative excerpt — Grade 6 science, 50 minutes**

**Objective:** I can draw and label a model showing how a plant uses sunlight, water and
carbon dioxide to make sugar and release oxygen.

**Sequence:** 0-5 min: students answer, “Where does a plant's food come from?” 5-15 min:
teacher models a plant as a solar-powered food factory and labels three inputs and two
outputs. 15-30 min: pairs sort input/output cards and justify each placement. 30-43 min:
students independently draw an arrow model and add a one-sentence explanation. 43-50 min:
exit ticket—“Can a watered plant make sugar without carbon dioxide? Explain using *input*.”

**Evidence:** A secure response shows all five substances in the correct direction and
explains that sugar is made rather than absorbed from soil. **Reteach trigger:** If more
than 25% label sugar as an input, begin the next lesson with a carbon-source model.

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
  "id": "LP-009",
  "slug": "design-a-discussion-centered-lesson-with-equitable-participation",
  "chapter": "lesson-planning",
  "subtopic": "complete-lessons",
  "title": "Design a discussion-centered lesson with equitable participation",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Design a discussion-centered lesson with equitable participation

## Use this when

You need a classroom-ready instructional plan focused on complete lessons.

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
Complete this teacher task: Design a discussion-centered lesson with equitable participation. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], complete lessons; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

**Illustrative excerpt — Grade 6 science, 50 minutes**

**Objective:** I can draw and label a model showing how a plant uses sunlight, water and
carbon dioxide to make sugar and release oxygen.

**Sequence:** 0-5 min: students answer, “Where does a plant's food come from?” 5-15 min:
teacher models a plant as a solar-powered food factory and labels three inputs and two
outputs. 15-30 min: pairs sort input/output cards and justify each placement. 30-43 min:
students independently draw an arrow model and add a one-sentence explanation. 43-50 min:
exit ticket—“Can a watered plant make sugar without carbon dioxide? Explain using *input*.”

**Evidence:** A secure response shows all five substances in the correct direction and
explains that sugar is made rather than absorbed from soil. **Reteach trigger:** If more
than 25% label sugar as an input, begin the next lesson with a carbon-source model.

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
  "id": "LP-010",
  "slug": "build-a-no-technology-lesson-using-basic-classroom-materials",
  "chapter": "lesson-planning",
  "subtopic": "complete-lessons",
  "title": "Build a no-technology lesson using basic classroom materials",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Build a no-technology lesson using basic classroom materials

## Use this when

You need a classroom-ready instructional plan focused on complete lessons.

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
Complete this teacher task: Build a no-technology lesson using basic classroom materials. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], complete lessons; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

**Illustrative excerpt — Grade 6 science, 50 minutes**

**Objective:** I can draw and label a model showing how a plant uses sunlight, water and
carbon dioxide to make sugar and release oxygen.

**Sequence:** 0-5 min: students answer, “Where does a plant's food come from?” 5-15 min:
teacher models a plant as a solar-powered food factory and labels three inputs and two
outputs. 15-30 min: pairs sort input/output cards and justify each placement. 30-43 min:
students independently draw an arrow model and add a one-sentence explanation. 43-50 min:
exit ticket—“Can a watered plant make sugar without carbon dioxide? Explain using *input*.”

**Evidence:** A secure response shows all five substances in the correct direction and
explains that sugar is made rather than absorbed from soil. **Reteach trigger:** If more
than 25% label sugar as an input, begin the next lesson with a carbon-source model.

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
  "id": "LP-011",
  "slug": "create-a-lesson-around-one-complex-text-or-source",
  "chapter": "lesson-planning",
  "subtopic": "complete-lessons",
  "title": "Create a lesson around one complex text or source",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a lesson around one complex text or source

## Use this when

You need a classroom-ready instructional plan focused on complete lessons.

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
Complete this teacher task: Create a lesson around one complex text or source. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], complete lessons; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

**Illustrative excerpt — Grade 6 science, 50 minutes**

**Objective:** I can draw and label a model showing how a plant uses sunlight, water and
carbon dioxide to make sugar and release oxygen.

**Sequence:** 0-5 min: students answer, “Where does a plant's food come from?” 5-15 min:
teacher models a plant as a solar-powered food factory and labels three inputs and two
outputs. 15-30 min: pairs sort input/output cards and justify each placement. 30-43 min:
students independently draw an arrow model and add a one-sentence explanation. 43-50 min:
exit ticket—“Can a watered plant make sugar without carbon dioxide? Explain using *input*.”

**Evidence:** A secure response shows all five substances in the correct direction and
explains that sugar is made rather than absorbed from soil. **Reteach trigger:** If more
than 25% label sugar as an input, begin the next lesson with a carbon-source model.

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
  "id": "LP-012",
  "slug": "plan-a-safe-hands-on-investigation-lesson",
  "chapter": "lesson-planning",
  "subtopic": "complete-lessons",
  "title": "Plan a safe hands-on investigation lesson",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Plan a safe hands-on investigation lesson

## Use this when

You need a classroom-ready instructional plan focused on complete lessons.

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
Complete this teacher task: Plan a safe hands-on investigation lesson. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], complete lessons; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

**Illustrative excerpt — Grade 6 science, 50 minutes**

**Objective:** I can draw and label a model showing how a plant uses sunlight, water and
carbon dioxide to make sugar and release oxygen.

**Sequence:** 0-5 min: students answer, “Where does a plant's food come from?” 5-15 min:
teacher models a plant as a solar-powered food factory and labels three inputs and two
outputs. 15-30 min: pairs sort input/output cards and justify each placement. 30-43 min:
students independently draw an arrow model and add a one-sentence explanation. 43-50 min:
exit ticket—“Can a watered plant make sugar without carbon dioxide? Explain using *input*.”

**Evidence:** A secure response shows all five substances in the correct direction and
explains that sugar is made rather than absorbed from soil. **Reteach trigger:** If more
than 25% label sugar as an input, begin the next lesson with a carbon-source model.

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
  "id": "LP-013",
  "slug": "design-a-problem-based-mathematics-lesson",
  "chapter": "lesson-planning",
  "subtopic": "complete-lessons",
  "title": "Design a problem-based mathematics lesson",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Design a problem-based mathematics lesson

## Use this when

You need a classroom-ready instructional plan focused on complete lessons.

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
Complete this teacher task: Design a problem-based mathematics lesson. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], complete lessons; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-014",
  "slug": "compress-a-full-lesson-into-a-purposeful-30-minute-period",
  "chapter": "lesson-planning",
  "subtopic": "complete-lessons",
  "title": "Compress a full lesson into a purposeful 30-minute period",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Compress a full lesson into a purposeful 30-minute period

## Use this when

You need a classroom-ready instructional plan focused on complete lessons.

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
Complete this teacher task: Compress a full lesson into a purposeful 30-minute period. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], complete lessons; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-015",
  "slug": "expand-a-lesson-for-a-90-minute-block-without-filler",
  "chapter": "lesson-planning",
  "subtopic": "complete-lessons",
  "title": "Expand a lesson for a 90-minute block without filler",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Expand a lesson for a 90-minute block without filler

## Use this when

You need a classroom-ready instructional plan focused on complete lessons.

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
Complete this teacher task: Expand a lesson for a 90-minute block without filler. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], complete lessons; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-016",
  "slug": "repair-a-draft-lesson-whose-activities-do-not-match-its-objective",
  "chapter": "lesson-planning",
  "subtopic": "complete-lessons",
  "title": "Repair a draft lesson whose activities do not match its objective",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Repair a draft lesson whose activities do not match its objective

## Use this when

You need a classroom-ready instructional plan focused on complete lessons.

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
Complete this teacher task: Repair a draft lesson whose activities do not match its objective. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], complete lessons; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-017",
  "slug": "unpack-final-mastery-into-a-prerequisite-learning-map",
  "chapter": "lesson-planning",
  "subtopic": "backward-unit-planning",
  "title": "Unpack final mastery into a prerequisite learning map",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Unpack final mastery into a prerequisite learning map

## Use this when

You need a classroom-ready instructional plan focused on backward unit planning.

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
Complete this teacher task: Unpack final mastery into a prerequisite learning map. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], backward unit planning; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-018",
  "slug": "design-a-final-performance-task-before-planning-daily-lessons",
  "chapter": "lesson-planning",
  "subtopic": "backward-unit-planning",
  "title": "Design a final performance task before planning daily lessons",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Design a final performance task before planning daily lessons

## Use this when

You need a classroom-ready instructional plan focused on backward unit planning.

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
Complete this teacher task: Design a final performance task before planning daily lessons. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], backward unit planning; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-019",
  "slug": "create-a-coherent-lesson-sequence-from-an-approved-assessment",
  "chapter": "lesson-planning",
  "subtopic": "backward-unit-planning",
  "title": "Create a coherent lesson sequence from an approved assessment",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a coherent lesson sequence from an approved assessment

## Use this when

You need a classroom-ready instructional plan focused on backward unit planning.

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
Complete this teacher task: Create a coherent lesson sequence from an approved assessment. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], backward unit planning; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-020",
  "slug": "place-formative-checkpoints-and-reteaching-decisions-across-a-unit",
  "chapter": "lesson-planning",
  "subtopic": "backward-unit-planning",
  "title": "Place formative checkpoints and reteaching decisions across a unit",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Place formative checkpoints and reteaching decisions across a unit

## Use this when

You need a classroom-ready instructional plan focused on backward unit planning.

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
Complete this teacher task: Place formative checkpoints and reteaching decisions across a unit. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], backward unit planning; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-021",
  "slug": "audit-a-unit-for-gaps-repetition-and-cognitive-progression",
  "chapter": "lesson-planning",
  "subtopic": "backward-unit-planning",
  "title": "Audit a unit for gaps, repetition and cognitive progression",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Audit a unit for gaps, repetition and cognitive progression

## Use this when

You need a classroom-ready instructional plan focused on backward unit planning.

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
Complete this teacher task: Audit a unit for gaps, repetition and cognitive progression. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], backward unit planning; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-022",
  "slug": "shorten-a-unit-while-protecting-its-essential-learning",
  "chapter": "lesson-planning",
  "subtopic": "backward-unit-planning",
  "title": "Shorten a unit while protecting its essential learning",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Shorten a unit while protecting its essential learning

## Use this when

You need a classroom-ready instructional plan focused on backward unit planning.

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
Complete this teacher task: Shorten a unit while protecting its essential learning. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], backward unit planning; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-023",
  "slug": "add-transfer-and-reflection-to-the-end-of-a-unit",
  "chapter": "lesson-planning",
  "subtopic": "backward-unit-planning",
  "title": "Add transfer and reflection to the end of a unit",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Add transfer and reflection to the end of a unit

## Use this when

You need a classroom-ready instructional plan focused on backward unit planning.

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
Complete this teacher task: Add transfer and reflection to the end of a unit. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], backward unit planning; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-024",
  "slug": "separate-knowledge-skill-and-reasoning-within-a-standard",
  "chapter": "lesson-planning",
  "subtopic": "standards-and-objectives",
  "title": "Separate knowledge, skill and reasoning within a standard",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Separate knowledge, skill and reasoning within a standard

## Use this when

You need a classroom-ready instructional plan focused on standards & objectives.

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
Complete this teacher task: Separate knowledge, skill and reasoning within a standard. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], standards & objectives; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-025",
  "slug": "rewrite-a-technical-objective-as-a-student-friendly-i-can-statement",
  "chapter": "lesson-planning",
  "subtopic": "standards-and-objectives",
  "title": "Rewrite a technical objective as a student-friendly I-can statement",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Rewrite a technical objective as a student-friendly I-can statement

## Use this when

You need a classroom-ready instructional plan focused on standards & objectives.

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
Complete this teacher task: Rewrite a technical objective as a student-friendly I-can statement. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], standards & objectives; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-026",
  "slug": "create-observable-success-criteria-for-an-existing-objective",
  "chapter": "lesson-planning",
  "subtopic": "standards-and-objectives",
  "title": "Create observable success criteria for an existing objective",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create observable success criteria for an existing objective

## Use this when

You need a classroom-ready instructional plan focused on standards & objectives.

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
Complete this teacher task: Create observable success criteria for an existing objective. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], standards & objectives; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-027",
  "slug": "check-whether-an-activity-truly-aligns-to-a-supplied-standard",
  "chapter": "lesson-planning",
  "subtopic": "standards-and-objectives",
  "title": "Check whether an activity truly aligns to a supplied standard",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Check whether an activity truly aligns to a supplied standard

## Use this when

You need a classroom-ready instructional plan focused on standards & objectives.

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
Complete this teacher task: Check whether an activity truly aligns to a supplied standard. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], standards & objectives; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-028",
  "slug": "map-several-objectives-into-a-logical-teaching-order",
  "chapter": "lesson-planning",
  "subtopic": "standards-and-objectives",
  "title": "Map several objectives into a logical teaching order",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Map several objectives into a logical teaching order

## Use this when

You need a classroom-ready instructional plan focused on standards & objectives.

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
Complete this teacher task: Map several objectives into a logical teaching order. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], standards & objectives; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-029",
  "slug": "identify-prerequisite-skills-without-lowering-the-grade-level-target",
  "chapter": "lesson-planning",
  "subtopic": "standards-and-objectives",
  "title": "Identify prerequisite skills without lowering the grade-level target",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Identify prerequisite skills without lowering the grade-level target

## Use this when

You need a classroom-ready instructional plan focused on standards & objectives.

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
Complete this teacher task: Identify prerequisite skills without lowering the grade-level target. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], standards & objectives; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-030",
  "slug": "write-evidence-statements-showing-what-mastery-would-look-like",
  "chapter": "lesson-planning",
  "subtopic": "standards-and-objectives",
  "title": "Write evidence statements showing what mastery would look like",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Write evidence statements showing what mastery would look like

## Use this when

You need a classroom-ready instructional plan focused on standards & objectives.

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
Complete this teacher task: Write evidence statements showing what mastery would look like. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], standards & objectives; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-031",
  "slug": "design-a-warm-up-that-exposes-prior-knowledge-in-five-minutes",
  "chapter": "lesson-planning",
  "subtopic": "warm-ups-and-exit-tickets",
  "title": "Design a warm-up that exposes prior knowledge in five minutes",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Design a warm-up that exposes prior knowledge in five minutes

## Use this when

You need a classroom-ready instructional plan focused on warm ups & exit tickets.

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
Complete this teacher task: Design a warm-up that exposes prior knowledge in five minutes. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], warm ups & exit tickets; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-032",
  "slug": "write-a-misconception-revealing-hinge-question",
  "chapter": "lesson-planning",
  "subtopic": "warm-ups-and-exit-tickets",
  "title": "Write a misconception-revealing hinge question",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Write a misconception-revealing hinge question

## Use this when

You need a classroom-ready instructional plan focused on warm ups & exit tickets.

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
Complete this teacher task: Write a misconception-revealing hinge question. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], warm ups & exit tickets; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-033",
  "slug": "create-an-exit-ticket-with-secure-developing-and-not-yet-response-bands",
  "chapter": "lesson-planning",
  "subtopic": "warm-ups-and-exit-tickets",
  "title": "Create an exit ticket with secure, developing and not-yet response bands",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create an exit ticket with secure, developing and not-yet response bands

## Use this when

You need a classroom-ready instructional plan focused on warm ups & exit tickets.

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
Complete this teacher task: Create an exit ticket with secure, developing and not-yet response bands. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], warm ups & exit tickets; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-034",
  "slug": "turn-yesterday-s-exit-ticket-patterns-into-today-s-opening-task",
  "chapter": "lesson-planning",
  "subtopic": "warm-ups-and-exit-tickets",
  "title": "Turn yesterday's exit-ticket patterns into today's opening task",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Turn yesterday's exit-ticket patterns into today's opening task

## Use this when

You need a classroom-ready instructional plan focused on warm ups & exit tickets.

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
Complete this teacher task: Turn yesterday's exit-ticket patterns into today's opening task. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], warm ups & exit tickets; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-035",
  "slug": "build-a-retrieval-practice-warm-up-without-introducing-new-content",
  "chapter": "lesson-planning",
  "subtopic": "warm-ups-and-exit-tickets",
  "title": "Build a retrieval-practice warm-up without introducing new content",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Build a retrieval-practice warm-up without introducing new content

## Use this when

You need a classroom-ready instructional plan focused on warm ups & exit tickets.

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
Complete this teacher task: Build a retrieval-practice warm-up without introducing new content. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], warm ups & exit tickets; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-036",
  "slug": "create-a-transfer-exit-ticket-that-cannot-be-answered-by-copying",
  "chapter": "lesson-planning",
  "subtopic": "warm-ups-and-exit-tickets",
  "title": "Create a transfer exit ticket that cannot be answered by copying",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a transfer exit ticket that cannot be answered by copying

## Use this when

You need a classroom-ready instructional plan focused on warm ups & exit tickets.

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
Complete this teacher task: Create a transfer exit ticket that cannot be answered by copying. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], warm ups & exit tickets; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-037",
  "slug": "audit-an-exit-ticket-for-alignment-ambiguity-and-reading-load",
  "chapter": "lesson-planning",
  "subtopic": "warm-ups-and-exit-tickets",
  "title": "Audit an exit ticket for alignment, ambiguity and reading load",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Audit an exit ticket for alignment, ambiguity and reading load

## Use this when

You need a classroom-ready instructional plan focused on warm ups & exit tickets.

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
Complete this teacher task: Audit an exit ticket for alignment, ambiguity and reading load. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], warm ups & exit tickets; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-038",
  "slug": "build-a-realistic-minute-by-minute-lesson-timeline",
  "chapter": "lesson-planning",
  "subtopic": "pacing-and-transitions",
  "title": "Build a realistic minute-by-minute lesson timeline",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Build a realistic minute-by-minute lesson timeline

## Use this when

You need a classroom-ready instructional plan focused on pacing & transitions.

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
Complete this teacher task: Build a realistic minute-by-minute lesson timeline. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], pacing & transitions; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-039",
  "slug": "diagnose-where-a-lesson-is-likely-to-run-out-of-time",
  "chapter": "lesson-planning",
  "subtopic": "pacing-and-transitions",
  "title": "Diagnose where a lesson is likely to run out of time",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Diagnose where a lesson is likely to run out of time

## Use this when

You need a classroom-ready instructional plan focused on pacing & transitions.

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
Complete this teacher task: Diagnose where a lesson is likely to run out of time. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], pacing & transitions; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-040",
  "slug": "write-concise-transitions-between-lesson-segments",
  "chapter": "lesson-planning",
  "subtopic": "pacing-and-transitions",
  "title": "Write concise transitions between lesson segments",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Write concise transitions between lesson segments

## Use this when

You need a classroom-ready instructional plan focused on pacing & transitions.

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
Complete this teacher task: Write concise transitions between lesson segments. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], pacing & transitions; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-041",
  "slug": "create-a-pacing-contingency-when-discussion-runs-long",
  "chapter": "lesson-planning",
  "subtopic": "pacing-and-transitions",
  "title": "Create a pacing contingency when discussion runs long",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a pacing contingency when discussion runs long

## Use this when

You need a classroom-ready instructional plan focused on pacing & transitions.

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
Complete this teacher task: Create a pacing contingency when discussion runs long. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], pacing & transitions; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-042",
  "slug": "plan-meaningful-early-finisher-work-connected-to-the-objective",
  "chapter": "lesson-planning",
  "subtopic": "pacing-and-transitions",
  "title": "Plan meaningful early-finisher work connected to the objective",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Plan meaningful early-finisher work connected to the objective

## Use this when

You need a classroom-ready instructional plan focused on pacing & transitions.

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
Complete this teacher task: Plan meaningful early-finisher work connected to the objective. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], pacing & transitions; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-043",
  "slug": "adapt-one-lesson-for-both-a-regular-period-and-a-shortened-schedule",
  "chapter": "lesson-planning",
  "subtopic": "pacing-and-transitions",
  "title": "Adapt one lesson for both a regular period and a shortened schedule",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Adapt one lesson for both a regular period and a shortened schedule

## Use this when

You need a classroom-ready instructional plan focused on pacing & transitions.

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
Complete this teacher task: Adapt one lesson for both a regular period and a shortened schedule. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], pacing & transitions; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-044",
  "slug": "build-an-emergency-no-print-lesson-from-materials-already-in-the-room",
  "chapter": "lesson-planning",
  "subtopic": "substitute-and-emergency-plans",
  "title": "Build an emergency no-print lesson from materials already in the room",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Build an emergency no-print lesson from materials already in the room

## Use this when

You need a classroom-ready instructional plan focused on substitute & emergency plans.

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
Complete this teacher task: Build an emergency no-print lesson from materials already in the room. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], substitute & emergency plans; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-045",
  "slug": "write-exact-substitute-directions-that-require-no-subject-guessing",
  "chapter": "lesson-planning",
  "subtopic": "substitute-and-emergency-plans",
  "title": "Write exact substitute directions that require no subject guessing",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Write exact substitute directions that require no subject guessing

## Use this when

You need a classroom-ready instructional plan focused on substitute & emergency plans.

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
Complete this teacher task: Write exact substitute directions that require no subject guessing. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], substitute & emergency plans; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-046",
  "slug": "create-a-technology-failure-backup-for-a-digital-lesson",
  "chapter": "lesson-planning",
  "subtopic": "substitute-and-emergency-plans",
  "title": "Create a technology-failure backup for a digital lesson",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a technology-failure backup for a digital lesson

## Use this when

You need a classroom-ready instructional plan focused on substitute & emergency plans.

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
Complete this teacher task: Create a technology-failure backup for a digital lesson. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], substitute & emergency plans; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-047",
  "slug": "prepare-an-independent-catch-up-lesson-for-an-unexpected-absence",
  "chapter": "lesson-planning",
  "subtopic": "substitute-and-emergency-plans",
  "title": "Prepare an independent catch-up lesson for an unexpected absence",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Prepare an independent catch-up lesson for an unexpected absence

## Use this when

You need a classroom-ready instructional plan focused on substitute & emergency plans.

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
Complete this teacher task: Prepare an independent catch-up lesson for an unexpected absence. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], substitute & emergency plans; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-048",
  "slug": "audit-a-substitute-plan-for-safety-clarity-and-collection-procedures",
  "chapter": "lesson-planning",
  "subtopic": "substitute-and-emergency-plans",
  "title": "Audit a substitute plan for safety, clarity and collection procedures",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Audit a substitute plan for safety, clarity and collection procedures

## Use this when

You need a classroom-ready instructional plan focused on substitute & emergency plans.

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
Complete this teacher task: Audit a substitute plan for safety, clarity and collection procedures. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], substitute & emergency plans; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-049",
  "slug": "launch-a-project-with-a-clear-driving-question-and-final-product",
  "chapter": "lesson-planning",
  "subtopic": "projects-and-interdisciplinary-lessons",
  "title": "Launch a project with a clear driving question and final product",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Launch a project with a clear driving question and final product

## Use this when

You need a classroom-ready instructional plan focused on projects & interdisciplinary lessons.

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
Complete this teacher task: Launch a project with a clear driving question and final product. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], projects & interdisciplinary lessons; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-050",
  "slug": "connect-two-subjects-around-one-authentic-problem",
  "chapter": "lesson-planning",
  "subtopic": "projects-and-interdisciplinary-lessons",
  "title": "Connect two subjects around one authentic problem",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Connect two subjects around one authentic problem

## Use this when

You need a classroom-ready instructional plan focused on projects & interdisciplinary lessons.

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
Complete this teacher task: Connect two subjects around one authentic problem. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], projects & interdisciplinary lessons; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-051",
  "slug": "break-a-multiweek-project-into-milestones-and-checkpoints",
  "chapter": "lesson-planning",
  "subtopic": "projects-and-interdisciplinary-lessons",
  "title": "Break a multiweek project into milestones and checkpoints",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Break a multiweek project into milestones and checkpoints

## Use this when

You need a classroom-ready instructional plan focused on projects & interdisciplinary lessons.

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
Complete this teacher task: Break a multiweek project into milestones and checkpoints. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], projects & interdisciplinary lessons; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-052",
  "slug": "create-individual-accountability-inside-a-group-project",
  "chapter": "lesson-planning",
  "subtopic": "projects-and-interdisciplinary-lessons",
  "title": "Create individual accountability inside a group project",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create individual accountability inside a group project

## Use this when

You need a classroom-ready instructional plan focused on projects & interdisciplinary lessons.

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
Complete this teacher task: Create individual accountability inside a group project. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], projects & interdisciplinary lessons; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-053",
  "slug": "design-a-project-rubric-that-measures-learning-rather-than-decoration",
  "chapter": "lesson-planning",
  "subtopic": "projects-and-interdisciplinary-lessons",
  "title": "Design a project rubric that measures learning rather than decoration",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Design a project rubric that measures learning rather than decoration

## Use this when

You need a classroom-ready instructional plan focused on projects & interdisciplinary lessons.

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
Complete this teacher task: Design a project rubric that measures learning rather than decoration. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], projects & interdisciplinary lessons; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-054",
  "slug": "plan-a-public-product-option-that-protects-student-privacy",
  "chapter": "lesson-planning",
  "subtopic": "projects-and-interdisciplinary-lessons",
  "title": "Plan a public-product option that protects student privacy",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Plan a public-product option that protects student privacy

## Use this when

You need a classroom-ready instructional plan focused on projects & interdisciplinary lessons.

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
Complete this teacher task: Plan a public-product option that protects student privacy. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], projects & interdisciplinary lessons; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-055",
  "slug": "turn-lesson-evidence-into-a-next-day-adjustment",
  "chapter": "lesson-planning",
  "subtopic": "reflection-and-adaptation",
  "title": "Turn lesson evidence into a next-day adjustment",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Turn lesson evidence into a next-day adjustment

## Use this when

You need a classroom-ready instructional plan focused on reflection & adaptation.

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
Complete this teacher task: Turn lesson evidence into a next-day adjustment. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], reflection & adaptation; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-056",
  "slug": "write-a-post-lesson-reflection-based-on-observations-rather-than-feelings-alone",
  "chapter": "lesson-planning",
  "subtopic": "reflection-and-adaptation",
  "title": "Write a post-lesson reflection based on observations rather than feelings alone",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Write a post-lesson reflection based on observations rather than feelings alone

## Use this when

You need a classroom-ready instructional plan focused on reflection & adaptation.

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
Complete this teacher task: Write a post-lesson reflection based on observations rather than feelings alone. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], reflection & adaptation; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-057",
  "slug": "identify-what-to-keep-change-and-investigate-after-a-lesson",
  "chapter": "lesson-planning",
  "subtopic": "reflection-and-adaptation",
  "title": "Identify what to keep, change and investigate after a lesson",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Identify what to keep, change and investigate after a lesson

## Use this when

You need a classroom-ready instructional plan focused on reflection & adaptation.

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
Complete this teacher task: Identify what to keep, change and investigate after a lesson. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], reflection & adaptation; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-058",
  "slug": "adapt-a-lesson-after-most-learners-miss-the-same-misconception",
  "chapter": "lesson-planning",
  "subtopic": "reflection-and-adaptation",
  "title": "Adapt a lesson after most learners miss the same misconception",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Adapt a lesson after most learners miss the same misconception

## Use this when

You need a classroom-ready instructional plan focused on reflection & adaptation.

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
Complete this teacher task: Adapt a lesson after most learners miss the same misconception. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], reflection & adaptation; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-059",
  "slug": "plan-targeted-follow-up-for-three-anonymous-response-patterns",
  "chapter": "lesson-planning",
  "subtopic": "reflection-and-adaptation",
  "title": "Plan targeted follow-up for three anonymous response patterns",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Plan targeted follow-up for three anonymous response patterns

## Use this when

You need a classroom-ready instructional plan focused on reflection & adaptation.

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
Complete this teacher task: Plan targeted follow-up for three anonymous response patterns. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], reflection & adaptation; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "LP-060",
  "slug": "compare-the-intended-lesson-with-what-learners-actually-demonstrated",
  "chapter": "lesson-planning",
  "subtopic": "reflection-and-adaptation",
  "title": "Compare the intended lesson with what learners actually demonstrated",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Compare the intended lesson with what learners actually demonstrated

## Use this when

You need a classroom-ready instructional plan focused on reflection & adaptation.

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
Complete this teacher task: Compare the intended lesson with what learners actually demonstrated. Create a classroom-ready instructional plan using only the supplied inputs.

Required output:
Return: objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], reflection & adaptation; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
