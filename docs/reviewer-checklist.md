# Human review checklist

Automated checks do not establish teaching quality or certify privacy compliance.
Do not upload real student data. Store reviewer IDs and anonymous aggregate feedback,
not teacher/customer contact lists, in this public repository.

## Before approval

For every prompt and every workflow step:

- Check the exact fictional input and the full, untrimmed output.
- Verify answers independently; check questions, solutions, units and difficulty.
- Check age appropriateness, accessibility and classroom practicality.
- Require supplied standard text; verify alignment rather than trusting a code.
- Reject invented student observations, pronouns, diagnoses, citations or achievements.
- Check privacy language: initials do not guarantee anonymity.
- Check material reuse rights and school-approved-tool requirements.
- Verify that each workflow output actually feeds its successor.
- Try the task without founder help and record needed corrections.
- Record the model/tool, plan tier and date actually tested.
- Do not claim compatibility with tools that were not tested.
- Record editing time as well as generation time before making any savings claim.

## Approval record

Use the keys from the current outputs.json. Each review entry must include:
`approved`, `reviewer`, `reviewed_at`, `notes`, `fingerprint`, `output_sha256`.

Copy both hashes from the exact record reviewed; do not recompute them to bypass
a changed-output warning. Example structure: [reviews.example.json](../toolkit/reviews.example.json).
The example deliberately has approved=false. A passing release gate only confirms
that records exist and match; it cannot verify a reviewer is genuine.

Keep a separate private interview sheet with consent, anonymized participant ID,
task, tool/date, corrections, repeat-use signal and stated-price purchase decision.
Do not put identities or student records into public GitHub issues.

## Release acceptance

- All automated checks and output-specific human reviews pass.
- PDF and HTML inspected; links, bookmarks, printing and copy/paste checked.
- No misleading time-saving, teacher-authorship or endorsement claims.
- Real support contact and honest refund/delivery policy established.
- Checkout/delivery tested separately before any sales launch.
