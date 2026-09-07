"""Step 1 — prompt catalog banao.

Har section ke liye ek alag request jaati hai (chhoti request = reliable schema),
aur har section disk par cache hota hai. Beech mein ruk gaya to dobara chalane par
sirf bacha hua kaam hoga.
"""

from __future__ import annotations

import json
from typing import List, Literal

import anthropic
from pydantic import BaseModel, Field

import config
from steps.storage import load_json, save_json
from steps.contracts import catalog_issues, digest


# ------------------------------------------------------------------ schema
class Prompt(BaseModel):
    slug: str = Field(description="kebab-case id, unique within the section")
    title: str = Field(description="What this prompt does, 3-8 words")
    use_case: str = Field(description="One sentence: when a teacher reaches for this")
    grade_band: Literal["K-2", "3-5", "6-8", "9-12", "All"]
    subject: str = Field(description='Subject, or "Any"')
    prompt: str = Field(
        description="The copy-paste prompt. Use [SQUARE BRACKETS] for anything the "
                    "teacher must fill in. Long enough to give the model real context "
                    "(role, constraints, output format) — not a one-liner."
    )
    variables: List[str] = Field(description="The [PLACEHOLDERS] used, without brackets")
    example_filled_prompt: str = Field(
        description="The same prompt with every placeholder replaced by a realistic "
                    "example value. This exact text gets run to produce the sample "
                    "output printed in the book, so it must stand alone."
    )


class PromptSet(BaseModel):
    prompts: List[Prompt]


class WorkflowStep(BaseModel):
    step: int
    title: str
    prompt: str
    example_filled_prompt: str


class Workflow(BaseModel):
    slug: str
    title: str
    goal: str = Field(description="The finished thing the teacher walks away with")
    replaces: str = Field(description='Task it helps with; never claim measured time savings')
    steps: List[WorkflowStep]


class WorkflowSet(BaseModel):
    workflows: List[Workflow]


# ------------------------------------------------------------------ prompts
SYSTEM = f"""You write prompt libraries for {config.PRODUCT['audience']}.

The buyer is a working teacher, not a technologist. Everything you write is judged
on one question: does this save a real teacher real time on Sunday night?

Rules:
- Every prompt must be genuinely useful on its own. No filler, no near-duplicates.
- Write prompts that give the model real context: role, grade band, constraints,
  and the exact output format wanted. A bare one-line instruction is a bad prompt.
- Use [SQUARE BRACKETS] for what the teacher fills in. Keep placeholders few and obvious.
- Use fictional demonstration data only, never real student records or initials.
- Do not invent student facts, pronouns, curriculum codes or achievements.
- Require the teacher to supply standard TEXT; a code alone is not verified alignment.
- Avoid tool-specific features. Compatibility is untested until recorded by reviewers.
- Vary grade bands and subjects across the set. Do not cluster everything on one band.
- example_filled_prompt must read like a real teacher's real request, with specific
  values (fictional class size, concrete topic and supplied standard text).
- Do not promise hours saved. Outputs must be reviewed by a qualified teacher.
- Workflow steps 2 onward MUST use {{{{PREVIOUS_OUTPUT}}}} in both prompt and
  example_filled_prompt; step 1 must be self-contained without this marker."""


def _client() -> anthropic.Anthropic:
    return anthropic.Anthropic(max_retries=0)


def _load() -> dict:
    if config.CATALOG_JSON.exists():
        return load_json(config.CATALOG_JSON)
    return {"sections": {}, "workflows": []}


def _save(catalog: dict) -> None:
    save_json(config.CATALOG_JSON, catalog)


def _parsed(resp, field, want):
    usage = resp.usage.model_dump()
    log = load_json(config.USAGE_JSON, {})
    log[resp.id] = {"stage": "catalog", "batch": False, "model": resp.model,
                    "usage": usage, "stop_reason": resp.stop_reason,
                    "estimated_usd": (usage.get("input_tokens", 0) * config.PRICE_IN_PER_MTOK
                                      + usage.get("output_tokens", 0) * config.PRICE_OUT_PER_MTOK) / 1e6}
    save_json(config.USAGE_JSON, log)
    if resp.stop_reason != "end_turn" or resp.parsed_output is None:
        raise ValueError("Catalog response incomplete/refused; saved chunks preserved. No auto-retry.")
    batch = [p.model_dump() for p in getattr(resp.parsed_output, field)]
    if len(batch) != want:
        raise ValueError(f"Expected exactly {want} {field}; received {len(batch)}. No auto-retry.")
    slugs = [p["slug"] for p in batch]
    import re
    if len(set(slugs)) != len(slugs) or any(not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", s) for s in slugs):
        raise ValueError("Invalid or duplicate generated slug")
    return batch


def _extra(effort):
    return {"output_config": {"effort": effort}} if effort else {}


def _gen_section(client: anthropic.Anthropic, section: dict,
                 existing: List[dict]) -> List[dict]:
    """Chunk-by-chunk generate karo. Ek hi request mein 60 prompts maangne par
    output max_tokens se bahar nikal kar kat jaata hai — isliye chunking."""
    prompts = list(existing)

    while len(prompts) < section["count"]:
        want = min(config.CATALOG_CHUNK, section["count"] - len(prompts))
        covered = "\n".join(f"- {p['title']}" for p in prompts)
        avoid = (f"\n\nThese are already written for this section. Do not repeat "
                 f"them or write near-duplicates:\n{covered}" if prompts else "")

        user = f"""Write exactly {want} prompts for the section "{section['title']}".

What this section covers:
{section['brief']}

Spread them across these grade bands: {', '.join(config.GRADE_BANDS)}.
Every prompt must be distinct from the others in kind, not just in wording.{avoid}"""

        resp = client.messages.parse(
            model=config.MODEL,
            max_tokens=config.CATALOG_MAX_TOKENS,
            system=SYSTEM,
            messages=[{"role": "user", "content": user}],
            output_format=PromptSet,
            **_extra(config.CATALOG_EFFORT),
        )
        batch = _parsed(resp, "prompts", want)
        if set(p["slug"] for p in prompts) & set(p["slug"] for p in batch):
            raise ValueError("Duplicate slug across catalog chunks; existing chunks preserved")

        prompts.extend(batch)
        _checkpoint(section["id"], prompts)
        print(f"    {len(prompts)}/{section['count']}", flush=True)

    return prompts[: section["count"]]


def _gen_workflows(client: anthropic.Anthropic, existing: List[dict]) -> List[dict]:
    workflows = list(existing)

    while len(workflows) < config.WORKFLOW_COUNT:
        want = min(config.WORKFLOW_CHUNK, config.WORKFLOW_COUNT - len(workflows))
        covered = "\n".join(f"- {w['title']}" for w in workflows)
        avoid = (f"\n\nAlready written — do not repeat:\n{covered}" if workflows else "")

        user = f"""Write exactly {want} multi-step workflows.

{config.WORKFLOW_BRIEF}

Each step's prompt should be written so it can consume the previous step's output
(say so explicitly in the prompt text, e.g. "Using the unit plan below: ...").{avoid}"""

        resp = client.messages.parse(
            model=config.MODEL,
            max_tokens=config.CATALOG_MAX_TOKENS,
            system=SYSTEM,
            messages=[{"role": "user", "content": user}],
            output_format=WorkflowSet,
            **_extra(config.CATALOG_EFFORT),
        )
        batch = _parsed(resp, "workflows", want)
        if set(w["slug"] for w in workflows) & set(w["slug"] for w in batch):
            raise ValueError("Duplicate workflow across chunks")

        workflows.extend(batch)
        _checkpoint("__workflows__", workflows)
        print(f"    {len(workflows)}/{config.WORKFLOW_COUNT}", flush=True)

    return workflows[: config.WORKFLOW_COUNT]


# Har chunk ke baad disk par likho — kaam kabhi khota nahi.
_STATE: dict = {"sections": {}, "workflows": []}


def _checkpoint(key: str, items: List[dict]) -> None:
    if key == "__workflows__":
        _STATE["workflows"] = items
    else:
        _STATE["sections"][key] = items
    _save(_STATE)


def run(force: bool = False) -> dict:
    global _STATE
    if force:
        raise ValueError("Destructive --force regeneration disabled. Preserve existing runs separately.")
    generation_hash = digest({"system": SYSTEM, "sections": config.SECTIONS,
                               "workflows": config.WORKFLOW_COUNT, "brief": config.WORKFLOW_BRIEF,
                               "model": config.MODEL, "max_tokens": config.CATALOG_MAX_TOKENS,
                               "effort": config.CATALOG_EFFORT, "schema": config.SCHEMA_VERSION})
    existing = _load()
    if config.CATALOG_JSON.exists() and existing.get("generation_hash") != generation_hash:
        raise ValueError("Catalog generation settings changed or legacy cache found. Preserve it separately first.")
    if load_json(config.BATCH_STATE, {}):
        raise ValueError("A batch is pending; do not change catalog until it is recovered")
    client = _client()
    _STATE = existing
    _STATE["generation_hash"] = generation_hash
    _STATE.setdefault("sections", {})
    _STATE.setdefault("workflows", [])

    for section in config.SECTIONS:
        sid = section["id"]
        have = _STATE["sections"].get(sid, [])
        if len(have) >= section["count"]:
            print(f"  \u2713 {section['title']:<30} {len(have)} prompts (cached)")
            continue

        print(f"  \u2026 {section['title']:<30} {len(have)} -> {section['count']}", flush=True)
        _STATE["sections"][sid] = _gen_section(client, section, have)
        _save(_STATE)
        print(f"  \u2713 {section['title']:<30} {len(_STATE['sections'][sid])} prompts")

    have_wf = _STATE.get("workflows", [])
    if len(have_wf) >= config.WORKFLOW_COUNT:
        print(f"  \u2713 {'Workflows':<30} {len(have_wf)} (cached)")
    else:
        print(f"  \u2026 {'Workflows':<30} {len(have_wf)} -> {config.WORKFLOW_COUNT}", flush=True)
        _STATE["workflows"] = _gen_workflows(client, have_wf)
        _save(_STATE)
        print(f"  \u2713 {'Workflows':<30} {len(_STATE['workflows'])} workflows")

    issues = catalog_issues(_STATE)
    if issues:
        raise ValueError("Catalog QC failed: " + "; ".join(issues[:10]))
    return _STATE
