# Pipeline operation

Python 3.10+. All generation uses fictional demonstration data.
The API adapter still needs a real, owner-approved smoke test; offline tests do
not establish provider access or classroom quality.

## Dependency separation

- Status, estimate, QC, HTML builds and core tests: Python standard library.
- PDF: `python -m pip install -r toolkit/requirements-pdf.txt`
- Paid generation: `python -m pip install -r toolkit/requirements.txt`

No browser engine or Anthropic SDK is needed for offline builds.
Set `ANTHROPIC_API_KEY` through your shell or secret manager when you deliberately
choose paid generation. Never commit it.

## Profiles and cache locations

| Profile | Prompts | Workflows | Cache |
|---|---:|---:|---|
| pilot (default) | 5 | 1 | toolkit/build/pilot/ |
| beta | 30 | 3 | toolkit/build/beta/ |
| full | 300 | 12 | toolkit/build/full/ |

Each workflow has 3-6 sequential steps. The pilot has at most 11 output requests,
not 300. Requests across independent workflows can share a batch, but later
steps wait for actual predecessor results. Multiple rounds may take much longer
than a single batch. A one-hour local timeout preserves state; it does not cancel
the provider's batch or prevent billing.

Old files in `toolkit/build/` are untouched. They are not silently imported into
a new profile, and legacy plain-text outputs do not qualify as verified results.

## Commands

```bash
python toolkit/run.py estimate --profile pilot
python toolkit/run.py status --profile pilot
python toolkit/run.py qc --profile pilot
python toolkit/run.py build --profile pilot --html-only
python toolkit/run.py build --profile pilot --draft --html-only
```

Normal build fails on missing/stale/incomplete content. Only explicit `--draft`
allows a visibly marked preview despite QC failures.
No command produces an unmarked sales edition by default.

### Commands that spend money

```bash
python toolkit/run.py catalog --profile pilot --yes --budget-usd 4
python toolkit/run.py outputs --profile pilot --yes --budget-usd 4
# Or both stages plus build:
python toolkit/run.py all --profile pilot --yes --budget-usd 4
```

Run the estimate again before selecting beta/full. Both explicit approval and
a sufficient planning allowance are required. The allowance is deliberately
conservative but not a hard billing cap: it assumes at most 24K input tokens per
request and configured model prices; unusual/edited inputs can exceed that.
Each invocation acknowledges a fresh allowance. Configure provider-level spend
limits and reconcile usage with the provider invoice.

No automatic catalog retry, failed-item resubmission or SDK retry is enabled.
Rerunning failed work can cost money.

## Saved state

- `catalog.json`: generated catalog and generation-settings fingerprint.
- `outputs.json`: exact executed input, complete output, model, timestamp,
  prompt/settings fingerprint, output hash, batch ID and token usage.
- `batch_state.json`: submitted batch ID plus immutable request manifest.
- `failures.json`: per-item error/refusal/truncation reason.
- `usage.json`: deduplicated response usage and estimated charges, including
  nonempty truncated/refused messages. This is not a complete invoice.
- `reviews.json`: genuine human approvals, created by the reviewer workflow.
- `qc.json`: latest validation report.
- `manifest.json`: successful build profile, checksums and release status.

JSON writes are atomic. A corrupt cache raises an error rather than becoming an
empty cache. This is a **single-process pipeline**: never run two writers against
the same profile at once.

### Recovery rules

1. If a saved batch has an ID, rerun the same profile/settings to retrieve it.
2. If settings/catalog changed while a batch is pending, restore the original
   inputs before resuming. Do not combine old results with new inputs.
3. If state says `submitting` but has no ID, the request outcome is uncertain.
   Inspect your authorized provider batch list, identify the exact request batch,
   and restore its ID. Do not delete the state and blindly submit again.
4. Failed steps block descendants. Read `failures.json`, fix the cause, review
   the budget and then explicitly rerun.
5. Catalog-setting changes require preserving the previous run separately before
   regenerating. Destructive `--force` regeneration is intentionally disabled.

## Release gate

Configure a real `support_email` in `config.py`'s product definition.
Copy the structure in `reviews.example.json` and have the reviewer record
each **current** output's fingerprint and hash, reviewer ID, review date and notes.
Never mark a generated/test approval as a real teacher review.

```bash
python toolkit/run.py qc --profile beta --release
python toolkit/run.py build --profile beta --release
```

Release rejects missing approvals, placeholder contact, invalid counts, stale
outputs, missing dependencies and PDF failures. `--release` cannot be combined
with `--draft` or `--html-only`.

A passing machine check verifies records and structure, **not** reviewer identity,
factual correctness, legal compliance or usefulness. The human checklist remains
mandatory. No sales, delivery, marketing or classroom rollout is performed by
this pipeline.
