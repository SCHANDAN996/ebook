# Chapter 6: Report Card Comments

Report comments should describe learning evidence and a useful next step. This chapter's 30
prompts cover comment banks, balanced comments, subject-specific language, fictional bulk
demonstrations and tone repair. AI can improve consistency, but it must not invent progress,
effort, behaviour or family support to make a comment sound complete.

## How to use this chapter

Give the model verified evidence: objectives assessed, strengths demonstrated, recurring
errors, supports used and the next learning priority. Keep student identity outside the tool
where possible and insert names only in an approved system. Ask for a fact trace when the
comment is high stakes so each sentence can be tied to a supplied input.

## Final review

Check that comments are individualized by evidence rather than adjectives. Avoid fixed-
ability labels and predictions. Make sure the next step is achievable and understandable
to families. Bulk drafting saves time only if every individual comment is still reviewed
against the correct learner record before publication.


---


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

**Illustrative comment — entirely fictional, non-identifying evidence**

Fictional Learner A accurately solves one- and two-step equations and demonstrated this
on 8 of 10 invented practice items. The fictional work is clearest when each inverse
operation is shown on a separate line. The next practice priority is distributing negative
signs consistently across parentheses. Annotating the sign before simplifying is the
suggested next strategy in this invented example.

**Fact trace:** “8 of 10” comes from the supplied assessment record; “negative signs”
comes from the supplied error pattern; the suggested annotation is the teacher-provided
strategy. No claim is made about effort, personality, support at home or future results.

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
  "id": "RC-002",
  "slug": "turn-evidence-into-a-balanced-report-comment",
  "chapter": "report-card-comments",
  "subtopic": "strengths-and-next-steps",
  "title": "Turn evidence into a balanced report comment",
  "grade_bands": ["K-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
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

**Illustrative comment — entirely fictional, non-identifying evidence**

Fictional Learner A accurately solves one- and two-step equations and demonstrated this
on 8 of 10 invented practice items. The fictional work is clearest when each inverse
operation is shown on a separate line. The next practice priority is distributing negative
signs consistently across parentheses. Annotating the sign before simplifying is the
suggested next strategy in this invented example.

**Fact trace:** “8 of 10” comes from the supplied assessment record; “negative signs”
comes from the supplied error pattern; the suggested annotation is the teacher-provided
strategy. No claim is made about effort, personality, support at home or future results.

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
  "id": "RC-003",
  "slug": "rewrite-a-comment-for-clarity-and-fairness",
  "chapter": "report-card-comments",
  "subtopic": "tone-and-rewriting",
  "title": "Rewrite a comment for clarity and fairness",
  "grade_bands": ["K-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
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

Entirely fictional case: 'Learner A is lazy and never finishes anything.' Invented evidence: 2 of 4 practice tasks submitted over two weeks after reminders; Grade 7 science; calm and direct; 60 words.

## Sample output

**Illustrative comment — entirely fictional, non-identifying evidence**

Fictional Learner A accurately solves one- and two-step equations and demonstrated this
on 8 of 10 invented practice items. The fictional work is clearest when each inverse
operation is shown on a separate line. The next practice priority is distributing negative
signs consistently across parentheses. Annotating the sign before simplifying is the
suggested next strategy in this invented example.

**Fact trace:** “8 of 10” comes from the supplied assessment record; “negative signs”
comes from the supplied error pattern; the suggested annotation is the teacher-provided
strategy. No claim is made about effort, personality, support at home or future results.

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
  "id": "RC-004",
  "slug": "create-comment-starters-for-four-levels-of-demonstrated-mastery",
  "chapter": "report-card-comments",
  "subtopic": "comment-banks",
  "title": "Create comment starters for four levels of demonstrated mastery",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Create comment starters for four levels of demonstrated mastery

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on comment banks.

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
Complete this teacher task: Create comment starters for four levels of demonstrated mastery. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], comment banks; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

**Illustrative comment — entirely fictional, non-identifying evidence**

Fictional Learner A accurately solves one- and two-step equations and demonstrated this
on 8 of 10 invented practice items. The fictional work is clearest when each inverse
operation is shown on a separate line. The next practice priority is distributing negative
signs consistently across parentheses. Annotating the sign before simplifying is the
suggested next strategy in this invented example.

**Fact trace:** “8 of 10” comes from the supplied assessment record; “negative signs”
comes from the supplied error pattern; the suggested annotation is the teacher-provided
strategy. No claim is made about effort, personality, support at home or future results.

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
  "id": "RC-005",
  "slug": "build-modular-strength-evidence-and-next-step-sentence-parts",
  "chapter": "report-card-comments",
  "subtopic": "comment-banks",
  "title": "Build modular strength, evidence and next-step sentence parts",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Build modular strength, evidence and next-step sentence parts

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on comment banks.

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
Complete this teacher task: Build modular strength, evidence and next-step sentence parts. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], comment banks; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

**Illustrative comment — entirely fictional, non-identifying evidence**

Fictional Learner A accurately solves one- and two-step equations and demonstrated this
on 8 of 10 invented practice items. The fictional work is clearest when each inverse
operation is shown on a separate line. The next practice priority is distributing negative
signs consistently across parentheses. Annotating the sign before simplifying is the
suggested next strategy in this invented example.

**Fact trace:** “8 of 10” comes from the supplied assessment record; “negative signs”
comes from the supplied error pattern; the suggested annotation is the teacher-provided
strategy. No claim is made about effort, personality, support at home or future results.

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
  "id": "RC-006",
  "slug": "create-a-comment-bank-that-avoids-fixed-ability-labels",
  "chapter": "report-card-comments",
  "subtopic": "comment-banks",
  "title": "Create a comment bank that avoids fixed-ability labels",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": true,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a comment bank that avoids fixed-ability labels

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on comment banks.

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
Complete this teacher task: Create a comment bank that avoids fixed-ability labels. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], comment banks; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

## Sample output

**Illustrative comment — entirely fictional, non-identifying evidence**

Fictional Learner A accurately solves one- and two-step equations and demonstrated this
on 8 of 10 invented practice items. The fictional work is clearest when each inverse
operation is shown on a separate line. The next practice priority is distributing negative
signs consistently across parentheses. Annotating the sign before simplifying is the
suggested next strategy in this invented example.

**Fact trace:** “8 of 10” comes from the supplied assessment record; “negative signs”
comes from the supplied error pattern; the suggested annotation is the teacher-provided
strategy. No claim is made about effort, personality, support at home or future results.

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
  "id": "RC-007",
  "slug": "write-concise-comments-within-a-strict-character-limit",
  "chapter": "report-card-comments",
  "subtopic": "comment-banks",
  "title": "Write concise comments within a strict character limit",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Write concise comments within a strict character limit

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on comment banks.

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
Complete this teacher task: Write concise comments within a strict character limit. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], comment banks; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-008",
  "slug": "create-neutral-pronoun-variants-without-changing-the-evidence",
  "chapter": "report-card-comments",
  "subtopic": "comment-banks",
  "title": "Create neutral pronoun variants without changing the evidence",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create neutral pronoun variants without changing the evidence

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on comment banks.

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
Complete this teacher task: Create neutral pronoun variants without changing the evidence. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], comment banks; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-009",
  "slug": "build-a-comment-bank-with-visible-placeholders-for-supporting-evidence",
  "chapter": "report-card-comments",
  "subtopic": "comment-banks",
  "title": "Build a comment bank with visible placeholders for supporting evidence",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Build a comment bank with visible placeholders for supporting evidence

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on comment banks.

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
Complete this teacher task: Build a comment bank with visible placeholders for supporting evidence. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], comment banks; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-010",
  "slug": "audit-a-comment-bank-for-repetition-vagueness-and-invented-claims",
  "chapter": "report-card-comments",
  "subtopic": "comment-banks",
  "title": "Audit a comment bank for repetition, vagueness and invented claims",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Audit a comment bank for repetition, vagueness and invented claims

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on comment banks.

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
Complete this teacher task: Audit a comment bank for repetition, vagueness and invented claims. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], comment banks; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-011",
  "slug": "write-a-strength-statement-tied-to-a-specific-learning-objective",
  "chapter": "report-card-comments",
  "subtopic": "strengths-and-next-steps",
  "title": "Write a strength statement tied to a specific learning objective",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Write a strength statement tied to a specific learning objective

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on strengths & next steps.

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
Complete this teacher task: Write a strength statement tied to a specific learning objective. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], strengths & next steps; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-012",
  "slug": "convert-an-error-pattern-into-one-achievable-next-step",
  "chapter": "report-card-comments",
  "subtopic": "strengths-and-next-steps",
  "title": "Convert an error pattern into one achievable next step",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Convert an error pattern into one achievable next step

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on strengths & next steps.

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
Complete this teacher task: Convert an error pattern into one achievable next step. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], strengths & next steps; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-013",
  "slug": "build-a-balanced-comment-from-assessment-and-classroom-evidence",
  "chapter": "report-card-comments",
  "subtopic": "strengths-and-next-steps",
  "title": "Build a balanced comment from assessment and classroom evidence",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Build a balanced comment from assessment and classroom evidence

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on strengths & next steps.

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
Complete this teacher task: Build a balanced comment from assessment and classroom evidence. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], strengths & next steps; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-014",
  "slug": "write-a-comment-when-evidence-is-limited-or-inconsistent",
  "chapter": "report-card-comments",
  "subtopic": "strengths-and-next-steps",
  "title": "Write a comment when evidence is limited or inconsistent",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Write a comment when evidence is limited or inconsistent

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on strengths & next steps.

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
Complete this teacher task: Write a comment when evidence is limited or inconsistent. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], strengths & next steps; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-015",
  "slug": "create-a-learner-friendly-next-step-that-families-can-understand",
  "chapter": "report-card-comments",
  "subtopic": "strengths-and-next-steps",
  "title": "Create a learner-friendly next step that families can understand",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create a learner-friendly next step that families can understand

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on strengths & next steps.

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
Complete this teacher task: Create a learner-friendly next step that families can understand. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], strengths & next steps; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-016",
  "slug": "add-an-instructional-strategy-without-promising-a-future-result",
  "chapter": "report-card-comments",
  "subtopic": "strengths-and-next-steps",
  "title": "Add an instructional strategy without promising a future result",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Add an instructional strategy without promising a future result

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on strengths & next steps.

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
Complete this teacher task: Add an instructional strategy without promising a future result. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], strengths & next steps; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-017",
  "slug": "audit-a-report-comment-using-a-sentence-by-sentence-fact-trace",
  "chapter": "report-card-comments",
  "subtopic": "strengths-and-next-steps",
  "title": "Audit a report comment using a sentence-by-sentence fact trace",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Audit a report comment using a sentence-by-sentence fact trace

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on strengths & next steps.

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
Complete this teacher task: Audit a report comment using a sentence-by-sentence fact trace. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], strengths & next steps; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-018",
  "slug": "write-a-mathematics-comment-about-concepts-procedures-and-reasoning",
  "chapter": "report-card-comments",
  "subtopic": "subject-specific-comments",
  "title": "Write a mathematics comment about concepts, procedures and reasoning",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Write a mathematics comment about concepts, procedures and reasoning

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on subject specific comments.

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
Complete this teacher task: Write a mathematics comment about concepts, procedures and reasoning. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], subject specific comments; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-019",
  "slug": "write-a-science-comment-about-investigation-evidence-and-explanation",
  "chapter": "report-card-comments",
  "subtopic": "subject-specific-comments",
  "title": "Write a science comment about investigation, evidence and explanation",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Write a science comment about investigation, evidence and explanation

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on subject specific comments.

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
Complete this teacher task: Write a science comment about investigation, evidence and explanation. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], subject specific comments; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-020",
  "slug": "write-an-english-language-arts-comment-about-reading-and-writing-evidence",
  "chapter": "report-card-comments",
  "subtopic": "subject-specific-comments",
  "title": "Write an English language arts comment about reading and writing evidence",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Write an English language arts comment about reading and writing evidence

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on subject specific comments.

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
Complete this teacher task: Write an English language arts comment about reading and writing evidence. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], subject specific comments; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-021",
  "slug": "write-a-social-studies-comment-about-sources-claims-and-perspective",
  "chapter": "report-card-comments",
  "subtopic": "subject-specific-comments",
  "title": "Write a social studies comment about sources, claims and perspective",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Write a social studies comment about sources, claims and perspective

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on subject specific comments.

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
Complete this teacher task: Write a social studies comment about sources, claims and perspective. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], subject specific comments; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-022",
  "slug": "write-an-arts-comment-about-process-technique-and-reflection",
  "chapter": "report-card-comments",
  "subtopic": "subject-specific-comments",
  "title": "Write an arts comment about process, technique and reflection",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Write an arts comment about process, technique and reflection

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on subject specific comments.

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
Complete this teacher task: Write an arts comment about process, technique and reflection. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], subject specific comments; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-023",
  "slug": "write-a-physical-education-comment-using-observable-skill-evidence",
  "chapter": "report-card-comments",
  "subtopic": "subject-specific-comments",
  "title": "Write a physical education comment using observable skill evidence",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Write a physical education comment using observable skill evidence

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on subject specific comments.

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
Complete this teacher task: Write a physical education comment using observable skill evidence. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], subject specific comments; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-024",
  "slug": "audit-subject-specific-terminology-for-accuracy-and-family-clarity",
  "chapter": "report-card-comments",
  "subtopic": "subject-specific-comments",
  "title": "Audit subject-specific terminology for accuracy and family clarity",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Audit subject-specific terminology for accuracy and family clarity

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on subject specific comments.

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
Complete this teacher task: Audit subject-specific terminology for accuracy and family clarity. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], subject specific comments; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-025",
  "slug": "create-distinct-comment-drafts-from-a-fictional-evidence-table",
  "chapter": "report-card-comments",
  "subtopic": "bulk-drafts-from-fictional-evidence",
  "title": "Create distinct comment drafts from a fictional evidence table",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Create distinct comment drafts from a fictional evidence table

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on bulk drafts from fictional evidence.

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
Complete this teacher task: Create distinct comment drafts from a fictional evidence table. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], bulk drafts from fictional evidence; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-026",
  "slug": "generate-bulk-comments-without-mixing-one-learner-s-evidence-with-another",
  "chapter": "report-card-comments",
  "subtopic": "bulk-drafts-from-fictional-evidence",
  "title": "Generate bulk comments without mixing one learner's evidence with another",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Generate bulk comments without mixing one learner's evidence with another

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on bulk drafts from fictional evidence.

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
Complete this teacher task: Generate bulk comments without mixing one learner's evidence with another. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], bulk drafts from fictional evidence; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-027",
  "slug": "vary-sentence-structure-while-preserving-every-supplied-fact",
  "chapter": "report-card-comments",
  "subtopic": "bulk-drafts-from-fictional-evidence",
  "title": "Vary sentence structure while preserving every supplied fact",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Vary sentence structure while preserving every supplied fact

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on bulk drafts from fictional evidence.

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
Complete this teacher task: Vary sentence structure while preserving every supplied fact. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], bulk drafts from fictional evidence; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-028",
  "slug": "audit-a-bulk-comment-set-for-duplicates-contradictions-and-evidence-leakage",
  "chapter": "report-card-comments",
  "subtopic": "bulk-drafts-from-fictional-evidence",
  "title": "Audit a bulk comment set for duplicates, contradictions and evidence leakage",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Audit a bulk comment set for duplicates, contradictions and evidence leakage

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on bulk drafts from fictional evidence.

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
Complete this teacher task: Audit a bulk comment set for duplicates, contradictions and evidence leakage. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], bulk drafts from fictional evidence; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-029",
  "slug": "replace-harsh-or-vague-judgments-with-verified-learning-evidence",
  "chapter": "report-card-comments",
  "subtopic": "tone-and-rewriting",
  "title": "Replace harsh or vague judgments with verified learning evidence",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Replace harsh or vague judgments with verified learning evidence

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on tone & rewriting.

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
Complete this teacher task: Replace harsh or vague judgments with verified learning evidence. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], tone & rewriting; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
  "id": "RC-030",
  "slug": "shorten-a-report-comment-without-removing-the-material-concern",
  "chapter": "report-card-comments",
  "subtopic": "tone-and-rewriting",
  "title": "Shorten a report comment without removing the material concern",
  "grade_bands": ["3-12"],
  "subjects": ["Any"],
  "sensitivity": "standard",
  "sample_output": false,
  "review_status": "draft",
  "content_version": 1
}
---

# Shorten a report comment without removing the material concern

## Use this when

You need a concise report-card resource grounded only in verified evidence focused on tone & rewriting.

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
Complete this teacher task: Shorten a report comment without removing the material concern. Create a concise report-card resource grounded only in verified evidence using only the supplied inputs.

Required output:
Return: final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit.

Rules:
- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].
- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.
- Keep the named grade, time, materials, objective, and policy constraints unchanged.
- Make student-facing language clear and age-appropriate.
- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.
- End with a short TEACHER VERIFICATION checklist.
```

## Fictional test case

Fictional case: [GRADE], [SUBJECT], tone & rewriting; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.

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
