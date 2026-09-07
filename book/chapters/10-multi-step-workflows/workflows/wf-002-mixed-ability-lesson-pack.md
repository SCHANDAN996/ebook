---
{
  "id": "WF-002",
  "slug": "mixed-ability-lesson-pack",
  "chapter": "multi-step-workflows",
  "subtopic": "mixed-ability-lesson",
  "title": "Mixed-ability lesson pack",
  "sensitivity": "standard",
  "review_status": "draft",
  "content_version": 1
}
---

# Mixed-ability lesson pack

## Outcome

Create one common-goal lesson with evidence-based access routes.

## Teacher inputs

- `[VERBATIM_SOURCE_MATERIAL]`
- `[GRADE_SUBJECT_AND_CONTEXT]`
- `[TIME_MATERIALS_AND_POLICY_CONSTRAINTS]`
- `[NON_IDENTIFYING_EVIDENCE]`

## Workflow

1. Define the unchanged objective and mastery evidence.
2. Describe observed barriers without names or labels.
3. Create core lesson and formative checks.
4. Create scaffolded, on-level and extension routes; teacher reviews parity.
5. Add grouping, fade plan and next-day decision rules.

At every step, paste the previous **reviewed** output into the next prompt. Correct errors
before continuing; never allow the model to silently replace supplied facts.

## Copy-paste controller prompt

```text
Guide me through this workflow one step at a time. At each step: state the required
inputs, produce only the requested artifact, list uncertainties, and stop for teacher
review. Do not continue until I reply APPROVED or provide corrections. Preserve source
wording where requested, never invent school policy or student facts, and finish with
an alignment, privacy, accuracy and feasibility audit.
```

## Fictional end-to-end example

Context: Grade 7 science, a fictional ecosystem unit, 45-minute lessons, paper-based
materials, and anonymous evidence only. The teacher supplies the objective and constraints,
reviews each intermediate artifact, corrects any science or timing issue, and approves the
final pack only after checking alignment, accessibility, privacy and school policy.

## Review checklist

- [ ] Every stage uses the previous reviewed output.
- [ ] Unknown facts remain visible placeholders.
- [ ] No identifiable student information is present.
- [ ] Final artifacts align to one another and to the supplied goal.
- [ ] A qualified teacher has approved the current content fingerprint.
