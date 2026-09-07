---
{
  "id": "WF-003",
  "slug": "incident-to-parent-conversation",
  "chapter": "multi-step-workflows",
  "subtopic": "incident-to-parent-conversation",
  "title": "Incident to parent conversation",
  "sensitivity": "standard",
  "review_status": "draft",
  "content_version": 1
}
---

# Incident to parent conversation

## Outcome

Move from verified classroom facts to a calm, policy-aligned family conversation.

## Teacher inputs

- `[VERBATIM_SOURCE_MATERIAL]`
- `[GRADE_SUBJECT_AND_CONTEXT]`
- `[TIME_MATERIALS_AND_POLICY_CONSTRAINTS]`
- `[NON_IDENTIFYING_EVIDENCE]`

## Workflow

1. Record observable facts, immediate actions and applicable policy.
2. Separate facts, unknowns and interpretations; teacher verifies.
3. Draft neutral contact message with placeholders.
4. Prepare questions, support options and an action-plan table.
5. Document agreed actions and schedule follow-up without adding new claims.

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
