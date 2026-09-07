"""Offline checks for the human-editable master-book blueprint."""

from __future__ import annotations

import json
import re
from pathlib import Path


BOOK_ROOT = Path(__file__).resolve().parents[2] / "book"
HEX = re.compile(r"^#[0-9A-Fa-f]{6}$")
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_PROMPT_SECTIONS = (
    "## Use this when", "## Teacher inputs", "## Copy-paste prompt",
    "## Fictional test case", "## Sample output",
    "## Teacher verification checklist", "## Editorial notes",
)


def load_blueprint(root: Path = BOOK_ROOT) -> dict:
    try:
        return json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Invalid book manifest: {exc}") from exc


def blueprint_issues(root: Path = BOOK_ROOT) -> list[str]:
    issues: list[str] = []
    manifest = load_blueprint(root)
    chapters = manifest.get("chapters")
    if not isinstance(chapters, list) or not chapters:
        return ["manifest chapters must be a non-empty list"]

    orders = [c.get("order") for c in chapters]
    ids = [c.get("id") for c in chapters]
    if orders != list(range(1, len(chapters) + 1)):
        issues.append("chapter order must be consecutive and match manifest order")
    if len(ids) != len(set(ids)) or any(not isinstance(i, str) or not SLUG.fullmatch(i) for i in ids):
        issues.append("chapter IDs must be unique kebab-case values")

    prompt_total = 0
    workflow_total = 0
    for chapter in chapters:
        count = chapter.get("item_count")
        subtopics = chapter.get("subtopics")
        if not isinstance(count, int) or count < 1:
            issues.append(f"{chapter.get('id')}: item_count must be a positive integer")
            continue
        if not isinstance(subtopics, dict) or any(
                not SLUG.fullmatch(str(k)) or not isinstance(v, int) or v < 1
                for k, v in subtopics.items()):
            issues.append(f"{chapter.get('id')}: invalid subtopic allocation")
        elif sum(subtopics.values()) != count:
            issues.append(f"{chapter.get('id')}: subtopic counts do not equal item_count")
        kind = chapter.get("kind")
        if kind == "prompt":
            prompt_total += count
        elif kind == "workflow":
            workflow_total += count
        else:
            issues.append(f"{chapter.get('id')}: kind must be prompt or workflow")
        intro = root / str(chapter.get("intro", ""))
        if not intro.is_file():
            issues.append(f"{chapter.get('id')}: missing chapter intro {intro.relative_to(root)}")

    expected_prompts = manifest.get("standalone_prompt_total")
    expected_workflows = manifest.get("workflow_total")
    if prompt_total != expected_prompts or prompt_total != 300:
        issues.append(f"standalone prompt allocation is {prompt_total}, expected 300")
    if workflow_total != expected_workflows or workflow_total != 12:
        issues.append(f"workflow allocation is {workflow_total}, expected 12")
    sample_target = manifest.get("full_sample_output_target")
    if not isinstance(sample_target, int) or not 0 <= sample_target <= prompt_total:
        issues.append("full_sample_output_target must fit within standalone prompts")

    for required in [
        "templates/prompt.md", "templates/workflow.md", "schema/prompt.schema.json",
        "design/tokens.json", "front-matter/title-page.md", "front-matter/introduction.md",
        "front-matter/how-to-use.md", "front-matter/privacy-and-safety.md",
        "front-matter/table-of-contents.md"
    ]:
        if not (root / required).is_file():
            issues.append(f"missing required source: {required}")

    try:
        design = json.loads((root / "design/tokens.json").read_text(encoding="utf-8"))
        for name, value in design.get("colors", {}).items():
            if not isinstance(value, str) or not HEX.fullmatch(value):
                issues.append(f"invalid design colour {name}")
        if design.get("copy_policy", {}).get("pdf_javascript") is not False:
            issues.append("portable PDF policy must keep PDF JavaScript disabled")
    except (OSError, json.JSONDecodeError) as exc:
        issues.append(f"invalid design tokens: {exc}")

    return issues


def check(root: Path = BOOK_ROOT) -> dict:
    manifest = load_blueprint(root)
    issues = blueprint_issues(root)
    if issues:
        raise ValueError("Book blueprint failed: " + "; ".join(issues))
    return {
        "chapters": len(manifest["chapters"]),
        "prompts": manifest["standalone_prompt_total"],
        "workflows": manifest["workflow_total"],
        "sample_outputs": manifest["full_sample_output_target"],
    }


def beta_content_issues(root: Path = BOOK_ROOT) -> list[str]:
    """Validate the editorial shape of the Phase 3 beta corpus offline."""
    issues: list[str] = []
    prompts = sorted((root / "chapters").glob("0[1-9]-*/prompts/*.md"))
    workflows = sorted((root / "chapters" / "10-multi-step-workflows" / "workflows").glob("*.md"))
    if len(prompts) != 30:
        issues.append(f"beta must contain 30 prompts, found {len(prompts)}")
    if len(workflows) != 3:
        issues.append(f"beta must contain 3 workflows, found {len(workflows)}")

    ids: list[str] = []
    for path in prompts:
        text = path.read_text(encoding="utf-8")
        match = re.search(r'"id":\s*"([A-Z]{2}-\d{3})"', text)
        if not match:
            issues.append(f"{path.relative_to(root)}: missing valid prompt ID")
        else:
            ids.append(match.group(1))
        for section in REQUIRED_PROMPT_SECTIONS:
            if section not in text:
                issues.append(f"{path.relative_to(root)}: missing {section}")
        if "[NEEDS TEACHER INPUT]" not in text:
            issues.append(f"{path.relative_to(root)}: missing unknown-facts safeguard")
        if "```text" not in text:
            issues.append(f"{path.relative_to(root)}: copy-paste prompt is not fenced")
    if len(ids) != len(set(ids)):
        issues.append("beta prompt IDs must be unique")

    for path in workflows:
        text = path.read_text(encoding="utf-8")
        if "## Workflow" not in text or "## Fictional end-to-end example" not in text:
            issues.append(f"{path.relative_to(root)}: incomplete workflow structure")
        if "previous **reviewed** output" not in text:
            issues.append(f"{path.relative_to(root)}: missing human review gate")
    return issues


def check_beta(root: Path = BOOK_ROOT) -> dict:
    issues = beta_content_issues(root)
    if issues:
        raise ValueError("Beta content failed: " + "; ".join(issues))
    prompts = list((root / "chapters").glob("0[1-9]-*/prompts/*.md"))
    samples = sum('"sample_output": true' in p.read_text(encoding="utf-8") for p in prompts)
    return {"prompts": len(prompts), "workflows": 3, "sample_outputs": samples}
