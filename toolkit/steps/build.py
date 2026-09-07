"""Step 3 — catalog + asli outputs se book banao (HTML, phir PDF), aur QC chalao."""

from __future__ import annotations

import html
import json
import re
from typing import Dict, List

import config
from steps.keys import prompt_key, workflow_key
from steps.contracts import quality_issues, digest
from steps.storage import load_json, save_json

# ------------------------------------------------------------------ markdown
_BOLD = re.compile(r"\*\*(.+?)\*\*")
_ITAL = re.compile(r"(?<!\*)\*([^*\n]+?)\*(?!\*)")
_CODE = re.compile(r"`([^`\n]+?)`")


def _inline(text: str) -> str:
    out = html.escape(text)
    out = _BOLD.sub(r"<strong>\1</strong>", out)
    out = _ITAL.sub(r"<em>\1</em>", out)
    out = _CODE.sub(r"<code>\1</code>", out)
    return out


def _md(text: str) -> str:
    """Escaped Markdown subset: headings, lists, paragraphs and pipe tables."""
    source_lines = text.splitlines()
    for idx in range(len(source_lines) - 1):
        header, separator = source_lines[idx], source_lines[idx + 1]
        cells = separator.strip().strip("|").split("|")
        if "|" not in header or not cells or not all(re.fullmatch(r"\s*:?-{3,}:?\s*", cell) for cell in cells):
            continue
        end = idx + 2
        while end < len(source_lines) and "|" in source_lines[end] and source_lines[end].strip():
            end += 1
        rows = [header] + source_lines[idx + 2:end]
        table = ["<table>"]
        for row_index, row in enumerate(rows):
            tag = "th" if row_index == 0 else "td"
            table.append("<tr>" + "".join(f"<{tag}>{_inline(cell.strip())}</{tag}>"
                         for cell in row.strip().strip("|").split("|")) + "</tr>")
        table.append("</table>")
        return (_md("\n".join(source_lines[:idx])) + "\n" + "\n".join(table)
                + "\n" + _md("\n".join(source_lines[end:])))
    lines, parts, buf, list_tag = text.split("\n"), [], [], None

    def flush_para():
        if buf:
            parts.append(f"<p>{_inline(' '.join(buf))}</p>")
            buf.clear()

    def close_list():
        nonlocal list_tag
        if list_tag:
            parts.append(f"</{list_tag}>")
            list_tag = None

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()

        if not stripped:
            flush_para()
            close_list()
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            flush_para()
            close_list()
            level = min(len(m.group(1)) + 2, 6)
            parts.append(f"<h{level}>{_inline(m.group(2))}</h{level}>")
            continue

        m = re.match(r"^[-*+]\s+(.*)$", stripped)
        if m:
            flush_para()
            if list_tag != "ul":
                close_list()
                parts.append("<ul>")
                list_tag = "ul"
            parts.append(f"<li>{_inline(m.group(1))}</li>")
            continue

        m = re.match(r"^(\d+)[.)]\s+(.*)$", stripped)
        if m:
            flush_para()
            if list_tag != "ol":
                close_list()
                parts.append("<ol>")
                list_tag = "ol"
            parts.append(f"<li>{_inline(m.group(2))}</li>")
            continue

        if stripped.startswith("|") or set(stripped) <= set("-|: "):
            flush_para()
            close_list()
            parts.append(f'<div class="raw">{html.escape(line)}</div>')
            continue

        close_list()
        buf.append(stripped)

    flush_para()
    close_list()
    return "\n".join(parts)


def _trim(text: str) -> tuple[str, bool]:
    limit = config.MAX_OUTPUT_CHARS
    if not limit or len(text) <= limit:
        return text, False
    cut = text[:limit]
    nl = cut.rfind("\n")
    return (cut[:nl] if nl > limit * 0.6 else cut), True


# ------------------------------------------------------------------ css
CSS = """
@page { size: A4; margin: 18mm 19mm 22mm; }
* { box-sizing: border-box; }
body { font: 16px/1.65 system-ui, sans-serif; color:#21363d; margin:0 auto;
       max-width:850px; padding:28px; }
h1,h2,h3 { color:#123c45; line-height:1.3; break-after:avoid; }
h1 {font-size:32px;} h2 {font-size:25px; margin-top:32px;} h3 {font-size:19px;}
a {color:#176878;} .cover {border-bottom:3px solid #176878; padding:12px 0 24px;}
.sub,.meta,.label,.sectionnote {color:#53636a;}
.label {font-size:13px;font-weight:700;margin-bottom:5px;}
.prompt {background:#f0f4f7;border:1px solid #d9e3e8;border-radius:8px;padding:16px;
         white-space:pre-wrap;overflow-wrap:anywhere;font-size:15px;}
.card,.wf {border-bottom:1px solid #dae4e8;padding:0 0 20px;margin:24px 0;}
.output {border-left:3px solid #6e9eaa;padding-left:16px;margin-top:18px;}
.note {background:#fff4d8;padding:16px;border-radius:8px;margin:18px 0;}
.step {margin-top:20px;} .missing {color:#9c342e;}
.raw {white-space:pre-wrap;overflow-wrap:anywhere;}
table {border-collapse:collapse;width:100%;margin:15px 0;}
th,td {border:1px solid #cad7dd;padding:8px;text-align:left;vertical-align:top;}
footer {margin-top:24px;border-top:1px solid #dae4e8;padding-top:14px;}
@media(max-width:600px) {body {padding:16px;} h1 {font-size:27px;} .prompt {font-size:15px;}}
@media print {body {padding:0;font-size:10.5pt;} .prompt {font-size:9.5pt;}
 h1 {font-size:26pt;} h2 {font-size:18pt;} h3 {font-size:12pt;} }
"""


# ------------------------------------------------------------------ render
def _card(p: dict, record) -> str:
    output = record.get("output") if isinstance(record, dict) else None
    bits = [f'<div class="card">',
            f'<h3>{html.escape(p["title"])}</h3>',
            f'<p class="meta"><span>{html.escape(p.get("grade_band", "All"))}</span>'
            f'<span>{html.escape(p.get("subject", "Any"))}</span></p>',
            f'<p class="use">{html.escape(p.get("use_case", ""))}</p>',
            '<p class="label">The prompt</p>',
            f'<div class="prompt">{html.escape(p["prompt"])}</div>']

    if output:
        bits += ['<p class="label">Exact example input (fictional data)</p>',
                 f'<div class="prompt">{html.escape(record["input"])}</div>',
                 f'<p class="meta">Model: {html.escape(record.get("model", "unknown"))}; '
                 f'date: {html.escape(record.get("generated_at", "unknown"))}</p>']
        text, trimmed = _trim(output)
        bits.append('<div class="output"><p class="label">Recorded AI draft - teacher review required</p>')
        bits.append(_md(text))
        if trimmed:
            bits.append('<p class="trimmed">Output continues — trimmed here for length.</p>')
        bits.append("</div>")
    else:
        bits.append('<p class="missing">Sample output not generated yet.</p>')

    bits.append("</div>")
    return "\n".join(bits)


def _workflow(wf: dict, outputs: Dict[str, str]) -> str:
    bits = [f'<div class="wf"><h3>{html.escape(wf["title"])}</h3>',
            f'<p class="use">{html.escape(wf.get("goal", ""))}</p>',
            f'<p class="meta">Planning aid; no measured time-saving claim.</p>']
    for step in wf.get("steps", []):
        key = workflow_key(wf["slug"], step["step"])
        bits.append(f'<div class="step"><p class="label">Step {step["step"]} — '
                    f'{html.escape(step["title"])}</p>')
        bits.append(f'<div class="prompt">{html.escape(step["prompt"])}</div>')
        record = outputs.get(key)
        out = record.get("output") if isinstance(record, dict) else None
        if out:
            bits.append('<p class="label">Exact chained example input</p>')
            bits.append(f'<div class="prompt">{html.escape(record["input"])}</div>')
            text, trimmed = _trim(out)
            bits.append(f'<p class="meta">Model: {html.escape(record.get("model", "unknown"))}; '
                        f'date: {html.escape(record.get("generated_at", "unknown"))}</p>')
            bits.append('<div class="output"><p class="label">Recorded AI draft - teacher review required</p>')
            bits.append(_md(text))
            if trimmed:
                bits.append('<p class="trimmed">Output continues — trimmed for length.</p>')
            bits.append("</div>")
        bits.append("</div>")
    bits.append("</div>")
    return "\n".join(bits)


def render_html(catalog: dict, outputs: dict, release=False) -> str:
    p = config.PRODUCT
    parts = [
        "<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'>",
        f"<title>{html.escape(p['title'])}</title>",
        f"<style>{CSS}</style></head><body>",
        f"<div class='cover'><h1>{html.escape(p['title'])}</h1>",
        ("<p class='note'>Recorded human-review edition. Review for your own classroom.</p>" if release else
         "<p class='note'>DEVELOPMENT DRAFT - not for sale; classroom quality is not certified.</p>"),
        f"<p class='sub'>{html.escape(p['subtitle'])}</p>",
        f"<p class='promise'>{html.escape(p['promise'])}</p></div>",
        "<div class='toc'><h2 style='page-break-before:auto'>Contents</h2><ol>",
    ]
    for s in config.SECTIONS:
        n = len(catalog["sections"].get(s["id"], []))
        parts.append(f"<li><a href='#{s['id']}'>{html.escape(s['title'])}</a> - {n} prompts</li>")
    parts.append(f"<li><a href='#workflows'>Workflows</a> - {len(catalog.get('workflows', []))}</li></ol>")
    parts.append(f"<div class='note'><strong>Before you start.</strong> "
                 f"{html.escape(config.DISCLAIMER)}</div></div>")

    for s in config.SECTIONS:
        prompts = catalog["sections"].get(s["id"], [])
        parts.append(f"<h2 class='section' id='{s['id']}'>{html.escape(s['title'])}</h2>")
        parts.append(f"<p class='sectionnote'>{len(prompts)} prompts</p>")
        if s.get("sensitive"):
            parts.append(f"<div class='note'>{html.escape(config.DISCLAIMER)}</div>")
        for pr in prompts:
            parts.append(_card(pr, outputs.get(prompt_key(s["id"], pr["slug"]))))

    parts.append("<h2 class='section' id='workflows'>Workflows</h2>")
    if catalog.get("workflows"):
        parts.append("<p class='sectionnote'>Multi-step chains — each step feeds the next.</p>")
        for wf in catalog["workflows"]:
            parts.append(_workflow(wf, outputs))

    contact = (f'<a href="mailto:{html.escape(p["support_email"])}">Contact support</a>'
               if p["support_email"] else
               f'<a href="{html.escape(p["support_url"])}">Project feedback (no student data)</a>')
    parts.append(f"<footer><p>{contact}</p></footer></body></html>")
    return "\n".join(parts)


# ------------------------------------------------------------------ QC / build
def qc(catalog, outputs, release=False):
    issues = quality_issues(catalog, outputs, load_json(config.REVIEW_JSON, {}), release)
    save_json(config.QC_JSON, {"profile": config.PROFILE, "release": release,
                               "passed": not issues, "issues": issues})
    return issues


def run(draft=False, release=False, html_only=False):
    if release and (draft or html_only):
        raise ValueError("Release requires strict QC and PDF")
    catalog = load_json(config.CATALOG_JSON)
    outputs = load_json(config.OUTPUTS_JSON, {})
    issues = qc(catalog, outputs, release)
    if issues and not draft:
        raise ValueError("QC failed; no book built: " + "; ".join(issues[:12]))
    config.BUILD.mkdir(parents=True, exist_ok=True)
    source = render_html(catalog, outputs, release)
    config.BOOK_HTML.write_text(source, encoding="utf-8")
    if not html_only:
        from steps.pdf_export import export_pdf
        export_pdf(source, config.BOOK_PDF, config.PRODUCT["title"],
                   "Human review recorded - check before use" if release else "DEVELOPMENT DRAFT - not for sale")
    save_json(config.MANIFEST_JSON, {
        "profile": config.PROFILE, "release": release, "automated_qc_passed": not issues,
        "catalog_sha256": digest(catalog), "outputs_sha256": digest(outputs),
        "html_sha256": digest(source), "pdf_created": not html_only,
        "compatibility": "No cross-tool claim: check reviewer test records"})
    print(f"HTML: {config.BOOK_HTML}")
    if not html_only:
        print(f"PDF: {config.BOOK_PDF}")
    if issues:
        print(f"Draft only: {len(issues)} QC issues; see qc.json")
