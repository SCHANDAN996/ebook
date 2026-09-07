# Teacher AI Toolkit - development project

A pipeline for building and checking teacher-facing prompt/workflow resources.
**Not a launch-ready paid product.** Demand, teaching quality, time savings and
cross-tool compatibility have not yet been validated.

## Current state

- Free preview: **25 prompts + 3 clearly labelled editorial examples**, all fictional.
- Default technical pilot: **5 prompts + 1 workflow**, isolated from beta/full caches.
- Beta profile: **30 prompts + 3 workflows**; full profile: **300 + 12**.
- Workflow steps consume the previous step's **actual successful output**.
- Strict automated QC, content/model-aware cache, execution provenance and offline tests.
- Paid generation, teacher review, checkout, ads and email collection are **not activated**.

## Start here - no API spending

```bash
python -m unittest discover -s tests -v
python toolkit/run.py book-check
python toolkit/run.py design-preview
python toolkit/run.py estimate
python toolkit/run.py status
```

The tests use an in-memory fake provider, not an API key. PDF-specific tests require
the optional PDF dependencies.

### Rebuild the free preview locally

```bash
python -m pip install -r toolkit/requirements-pdf.txt
python toolkit/lead_magnet.py --output-dir deliverables
```

Outputs: [PDF](deliverables/lead-magnet.pdf) and [mobile-readable HTML](deliverables/lead-magnet.html).
No API or browser download is required. A PDF-generation error fails the command.
The examples are **not** represented as logged AI executions or teacher-tested results.

### Full-book source

The structured source for the planned 300-prompt, 12-workflow master edition lives in
[`book/`](book/). Its manifest fixes chapter allocations, prompt/workflow templates,
review boundaries and provisional design tokens before bulk writing begins. No final
master PDF is generated until the content and design gates pass.

## Paid generation - only after explicit budget approval

Read [pipeline instructions](toolkit/README.md), then configure provider spending limits.
Keep API keys in your local environment, never in GitHub or a prompt.

```bash
python -m pip install -r toolkit/requirements.txt
python toolkit/run.py estimate --profile pilot
# Only after reviewing the estimate and setting the provider limit:
python toolkit/run.py all --profile pilot --yes --budget-usd 4
```

The last command **spends money**. The $4 argument acknowledges a planning allowance;
it is **not a provider-enforced billing cap**. The current pilot planning allowance
is about $3.35, subject to settings and pricing. Do not edit a single section count
to simulate a pilot: select the profile instead.

The default build is visibly marked as a development edition. A sellable release
requires recorded human approvals for every current output and a real support email:

```bash
python toolkit/run.py qc --profile beta --release
python toolkit/run.py build --profile beta --release
```

Do not upload a paid edition or sensitive customer data into a public repository.
This repository is currently public; the free preview is intentionally visible.

## Working documents

| Document | Purpose |
|---|---|
| [Current strategy](docs/strategy.md) | Evidence, uncertainties, costs and decision gates |
| [Channel analysis](docs/channels-cold-email.md) | Why cold email is not the initial channel, and the school B2B alternative |
| [30-day roadmap](docs/roadmap.md) | Prioritized next steps; no automatic ad launch |
| [Reviewer checklist](docs/reviewer-checklist.md) | Classroom, accuracy, privacy and usability review |
| [Decision log](docs/decision-log.md) | Corrections followed by historical decisions |
| [Parked Plan B](docs/plan-b-thekedar-kit.md) | Historical alternative, not approved launch instructions |
| [Free preview PDF](deliverables/lead-magnet.pdf) | 25 prompts and three clearly labelled fictional examples |
| [Toolkit instructions](toolkit/README.md) | Build, validate and release workflow |

The first goal is a useful product people choose to pay for, not the largest prompt count.
