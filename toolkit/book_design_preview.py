#!/usr/bin/env python3
"""Build the five-page Phase 2 PDF design prototype and copy-enabled HTML."""

from __future__ import annotations

from pathlib import Path
import html

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
PDF_DEFAULT = ROOT / "output" / "pdf" / "phase-2-design-prototype.pdf"
HTML_DEFAULT = ROOT / "output" / "html" / "phase-2-design-prototype.html"
W, H = letter

PAPER = HexColor("#FFFDF8")
INK = HexColor("#172033")
NAVY = HexColor("#183153")
TEAL = HexColor("#167D7F")
CORAL = HexColor("#E8664A")
GOLD = HexColor("#D59A2D")
MUTED = HexColor("#667085")
LINE = HexColor("#D7DEE8")
PROMPT_BG = HexColor("#F2F7F7")
WARNING_BG = HexColor("#FFF4E8")

PROMPT = """You are an experienced [GRADE] teacher planning a [MINUTES]-minute lesson on [TOPIC].

Use this supplied standard text exactly as written: [SUPPLIED STANDARD TEXT]

Create: (1) a student-facing objective, (2) a warm-up, (3) explicit teacher modelling, (4) guided practice with observable checks, (5) independent practice, (6) one diagnostic exit ticket, and (7) the most likely misconception with a question that exposes it.

Use only [AVAILABLE MATERIALS]. Keep the total timing within [MINUTES] minutes. Do not invent standards, student facts, materials, dates or evidence. For science, distinguish a possible effect from a certain effect. Finish with a constraint self-check."""


def _register_fonts() -> None:
    fonts = {
        "Display": "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
        "Display-Bold": "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
        "Body": "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "Body-Bold": "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "Mono": "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "Mono-Bold": "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
    }
    for name, path in fonts.items():
        if name not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(name, path))


def _wrap(text: str, font: str, size: float, width: float) -> list[str]:
    lines: list[str] = []
    for paragraph in text.splitlines() or [""]:
        if not paragraph:
            lines.append("")
            continue
        words = paragraph.split()
        current = words.pop(0)
        for word in words:
            trial = current + " " + word
            if pdfmetrics.stringWidth(trial, font, size) <= width:
                current = trial
            else:
                lines.append(current)
                current = word
        lines.append(current)
    return lines


def _text(c: canvas.Canvas, text: str, x: float, y: float, width: float,
          font: str = "Body", size: float = 10, leading: float | None = None,
          color=INK, max_lines: int | None = None) -> float:
    leading = leading or size * 1.42
    lines = _wrap(text, font, size, width)
    if max_lines is not None:
        lines = lines[:max_lines]
    c.setFillColor(color)
    c.setFont(font, size)
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


def _round_box(c: canvas.Canvas, x: float, y: float, w: float, h: float,
               fill, stroke=LINE, radius: float = 10) -> None:
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=1)


def _chip(c: canvas.Canvas, text: str, x: float, y: float, fill=TEAL,
          color=white, width: float | None = None) -> float:
    size = 7.2
    w = width or pdfmetrics.stringWidth(text, "Body-Bold", size) + 16
    c.setFillColor(fill)
    c.roundRect(x, y, w, 18, 9, fill=1, stroke=0)
    c.setFillColor(color)
    c.setFont("Body-Bold", size)
    c.drawCentredString(x + w / 2, y + 5.3, text)
    return w


def _page_base(c: canvas.Canvas, number: int, label: str, dark: bool = False) -> None:
    c.setFillColor(NAVY if dark else PAPER)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    if dark:
        return
    c.setStrokeColor(LINE)
    c.line(42, 31, W - 42, 31)
    c.setFont("Body", 7.5)
    c.setFillColor(MUTED)
    c.drawString(42, 18, "THE TEACHER AI TOOLKIT  /  DESIGN PROTOTYPE")
    c.drawRightString(W - 42, 18, f"{label.upper()}   {number:02d}")


def _bookmark(c: canvas.Canvas, key: str, title: str, level: int = 0) -> None:
    c.bookmarkPage(key)
    c.addOutlineEntry(title, key, level=level, closed=False)


def _cover(c: canvas.Canvas) -> None:
    _page_base(c, 1, "Cover", dark=True)
    _bookmark(c, "cover", "Cover")
    c.setFillColor(TEAL)
    c.circle(W - 72, H - 78, 105, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.circle(W - 38, H - 45, 28, fill=1, stroke=0)
    c.setStrokeColor(HexColor("#FFFFFF22"))
    for i in range(4):
        c.roundRect(345 + i * 18, 108 + i * 17, 170, 220, 14, fill=0, stroke=1)
    c.setFillColor(white)
    c.setFont("Body-Bold", 8)
    c.drawString(52, H - 58, "DEVELOPMENT EDITION  /  DESIGN PROTOTYPE")
    c.setFillColor(GOLD)
    c.rect(52, H - 83, 46, 4, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Display-Bold", 39)
    c.drawString(50, 520, "The Teacher")
    c.drawString(50, 474, "AI Toolkit")
    _text(c, "300 copy-ready prompts and 12 connected workflows for K-12 teachers",
          54, 426, 370, "Body", 13, 19, HexColor("#DCE7F3"))
    _round_box(c, 50, 116, 265, 178, HexColor("#203E62"), HexColor("#3F5D7D"), 16)
    c.setFillColor(GOLD)
    c.setFont("Body-Bold", 8)
    c.drawString(70, 264, "PLAN  /  ADAPT  /  VERIFY")
    _text(c, "A practical planning library built around visible inputs, precise outputs and teacher judgement.",
          70, 226, 220, "Display", 15, 22, white)
    c.setFillColor(HexColor("#B9C9DA"))
    c.setFont("Body", 8)
    c.drawString(52, 56, "Prototype v1  -  not a final product or teaching-quality certification")


def _chapter(c: canvas.Canvas) -> None:
    _page_base(c, 2, "Chapter opener")
    _bookmark(c, "chapter", "Chapter opener")
    c.setFillColor(TEAL)
    c.rect(0, 0, 18, H, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.circle(492, 628, 74, fill=1, stroke=0)
    c.setFillColor(PAPER)
    c.circle(492, 628, 51, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.setFont("Display-Bold", 44)
    c.drawCentredString(492, 612, "01")
    c.setFillColor(CORAL)
    c.setFont("Body-Bold", 8)
    c.drawString(52, 694, "CHAPTER 01  /  60 PROMPTS")
    c.setFillColor(NAVY)
    c.setFont("Display-Bold", 31)
    c.drawString(52, 636, "Lesson Planning")
    _text(c, "Move from a supplied standard and a real classroom constraint to a draft a teacher can inspect at a glance.",
          54, 590, 350, "Display", 14, 21, INK)
    topics = [
        ("12", "Complete lessons"), ("08", "Backward unit planning"),
        ("08", "Standards and objectives"), ("08", "Warm-ups and exit tickets"),
        ("06", "Pacing and transitions"), ("06", "Substitute plans"),
        ("06", "Projects"), ("06", "Reflection and adaptation")
    ]
    y = 442
    for index, (count, title) in enumerate(topics):
        col = index % 2
        row = index // 2
        x = 54 + col * 260
        yy = y - row * 70
        _round_box(c, x, yy, 236, 50, white)
        _chip(c, count, x + 12, yy + 16, NAVY, white, 34)
        c.setFillColor(INK)
        c.setFont("Body-Bold", 9.5)
        c.drawString(x + 58, yy + 20, title)
    _round_box(c, 54, 92, 496, 68, WARNING_BG, CORAL)
    c.setFillColor(CORAL)
    c.setFont("Body-Bold", 8)
    c.drawString(70, 135, "CHAPTER RULE")
    _text(c, "Every plan must reconcile total time, available materials, supplied standards and observable evidence of learning.",
          70, 116, 452, "Body", 9, 13, INK)


def _prompt_page(c: canvas.Canvas) -> None:
    _page_base(c, 3, "Prompt")
    _bookmark(c, "prompt", "Prompt page")
    c.setFillColor(CORAL)
    c.setFont("Body-Bold", 8)
    c.drawString(42, 742, "LP-001  /  COMPLETE LESSONS")
    c.setFillColor(NAVY)
    c.setFont("Display-Bold", 24)
    c.drawString(42, 704, "A full lesson from one standard")
    x = 42
    for label in ["GRADES 3-12", "ANY SUBJECT", "10-60 MIN"]:
        x += _chip(c, label, x, 668, TEAL) + 7
    _chip(c, "COPY ONLINE", 438, 668, CORAL, white, 108)
    c.linkURL("../html/phase-2-design-prototype.html#lp-001", (438, 668, 546, 686), relative=1)
    c.setFillColor(MUTED)
    c.setFont("Body-Bold", 7.5)
    c.drawString(42, 640, "USE THIS WHEN")
    _text(c, "You have the required standard text and need a complete, reviewable first draft.",
          42, 620, 355, "Body", 10.5, 15, INK)
    c.setFillColor(MUTED)
    c.setFont("Body-Bold", 7.5)
    c.drawString(418, 640, "TEACHER INPUTS")
    _text(c, "[GRADE]\n[MINUTES]\n[TOPIC]\n[STANDARD TEXT]\n[MATERIALS]",
          418, 620, 130, "Mono", 7.8, 13, INK)
    _round_box(c, 42, 162, 356, 420, PROMPT_BG, TEAL, 12)
    c.setFillColor(TEAL)
    c.setFont("Body-Bold", 8)
    c.drawString(58, 556, "COPY-PASTE PROMPT")
    _text(c, PROMPT, 58, 530, 324, "Mono", 9.5, 14, INK)
    _round_box(c, 416, 162, 138, 420, white, LINE, 12)
    c.setFillColor(NAVY)
    c.setFont("Body-Bold", 8)
    c.drawString(430, 554, "VERIFY BEFORE USE")
    checks = [
        "All facts were supplied",
        "Answer/content is correct",
        "Timing totals correctly",
        "Materials are available",
        "Difficulty fits the class",
        "No private student data",
        "School policy is followed"
    ]
    yy = 520
    for item in checks:
        c.setStrokeColor(TEAL)
        c.rect(430, yy - 2, 9, 9, fill=0, stroke=1)
        yy = _text(c, item, 446, yy, 92, "Body", 8.5, 11.5, INK) - 12
    _round_box(c, 428, 184, 114, 74, WARNING_BG, CORAL, 8)
    c.setFillColor(CORAL)
    c.setFont("Body-Bold", 7)
    c.drawString(439, 239, "PRIVACY")
    _text(c, "Use fictional tests. Initials are not anonymization.", 439, 223, 92,
          "Body", 8, 11, INK)


def _sample(c: canvas.Canvas) -> None:
    _page_base(c, 4, "Sample output")
    _bookmark(c, "sample", "Sample output")
    _round_box(c, 42, 704, 528, 45, WARNING_BG, CORAL, 10)
    c.setFillColor(CORAL)
    c.setFont("Body-Bold", 8)
    c.drawString(57, 730, "ILLUSTRATIVE DRAFT  /  NOT TEACHER-APPROVED")
    _text(c, "A sample demonstrates format, not classroom effectiveness or factual certification.",
          57, 715, 480, "Body", 7.5, 10, INK)
    c.setFillColor(NAVY)
    c.setFont("Display-Bold", 22)
    c.drawString(42, 664, "What a reviewed example should show")
    _round_box(c, 42, 150, 326, 480, white, LINE, 12)
    c.setFillColor(TEAL)
    c.setFont("Body-Bold", 8)
    c.drawString(58, 606, "GRADE 6 SCIENCE  /  PHOTOSYNTHESIS")
    sections = [
        ("OBJECTIVE", "I can model how light energy, water and carbon dioxide contribute to sugar production and oxygen release."),
        ("WARM-UP  /  5 MIN", "Students record what a plant takes in and releases. Preserve responses before correction."),
        ("GUIDED CHECK", "Ask students to distinguish sunlight as energy from matter entering the plant."),
        ("EXIT TICKET", "Can a watered plant make sugar without light? Explain which required input is missing."),
        ("MISCONCEPTION CHECK", "Most carbon in a plant's dry mass comes from carbon dioxide, not directly from soil.")
    ]
    yy = 574
    for heading, body in sections:
        c.setFillColor(NAVY)
        c.setFont("Body-Bold", 7.4)
        c.drawString(58, yy, heading)
        yy = _text(c, body, 58, yy - 16, 294, "Body", 10, 14, INK) - 15
    _round_box(c, 386, 150, 184, 480, PROMPT_BG, TEAL, 12)
    c.setFillColor(TEAL)
    c.setFont("Body-Bold", 8)
    c.drawString(402, 606, "EDITORIAL REVIEW")
    review = [
        ("PASS", "Objective matches the supplied standard."),
        ("PASS", "The lesson distinguishes energy and matter."),
        ("FIX", "Do not say total tree mass simply comes from air; specify dry-mass carbon."),
        ("CHECK", "Confirm all activity minutes plus transitions fit the period."),
        ("CHECK", "Replace unavailable materials or retain them as inputs.")
    ]
    yy = 568
    for status, body in review:
        fill = TEAL if status == "PASS" else (CORAL if status == "FIX" else GOLD)
        _chip(c, status, 402, yy - 2, fill, white, 42)
        yy = _text(c, body, 452, yy + 2, 99, "Body", 8.2, 11, INK) - 19
    c.setFillColor(MUTED)
    c.setFont("Body", 7.5)
    c.drawString(402, 176, "Review applies only to this content version.")


def _workflow(c: canvas.Canvas) -> None:
    _page_base(c, 5, "Workflow")
    _bookmark(c, "workflow", "Workflow page")
    c.setFillColor(CORAL)
    c.setFont("Body-Bold", 8)
    c.drawString(42, 742, "WF-001  /  CONNECTED WORKFLOW")
    c.setFillColor(NAVY)
    c.setFont("Display-Bold", 24)
    c.drawString(42, 704, "From supplied standard to lesson pack")
    _text(c, "Each stage consumes the actual verified output above it. A failed or incomplete stage stops the chain.",
          42, 674, 510, "Body", 9.2, 14, INK)
    steps = [
        ("01", "PLAN", "Create the lesson skeleton from the supplied standard and constraints."),
        ("02", "ADAPT", "Use the verified plan to create scaffolded, on-level and extension access."),
        ("03", "ASSESS", "Use the verified lesson to draft an aligned check and answer key."),
        ("04", "PACKAGE", "Assemble teacher notes, student pages and the final verification list.")
    ]
    y = 554
    for index, (num, title, body) in enumerate(steps):
        _round_box(c, 76, y, 456, 82, white, LINE, 12)
        c.setFillColor(TEAL if index < 3 else NAVY)
        c.circle(105, y + 41, 19, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Body-Bold", 8)
        c.drawCentredString(105, y + 38, num)
        c.setFillColor(NAVY)
        c.setFont("Body-Bold", 8)
        c.drawString(140, y + 54, title)
        _text(c, body, 140, y + 34, 370, "Body", 9.5, 13, INK)
        if index < len(steps) - 1:
            c.setStrokeColor(TEAL)
            c.setLineWidth(1.5)
            c.line(105, y, 105, y - 22)
            c.line(101, y - 17, 105, y - 22)
            c.line(109, y - 17, 105, y - 22)
        y -= 108
    _round_box(c, 76, 78, 456, 48, WARNING_BG, CORAL, 10)
    c.setFillColor(CORAL)
    c.setFont("Body-Bold", 8)
    c.drawString(92, 107, "HUMAN GATE")
    _text(c, "Verify facts, answer keys, privacy, accessibility and local policy before classroom use.",
          176, 108, 334, "Body", 7.6, 10, INK)


def build_pdf(path: Path = PDF_DEFAULT) -> Path:
    _register_fonts()
    path.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(path), pagesize=letter, pageCompression=1,
                      initialFontName="Body", initialFontSize=10)
    c.setTitle("Teacher AI Toolkit - Phase 2 Design Prototype")
    c.setAuthor("Chandan Singh")
    c.setSubject("Five-page layout prototype; not the final book")
    for draw in [_cover, _chapter, _prompt_page, _sample, _workflow]:
        draw(c)
        c.showPage()
    c.save()
    return path


def build_html(path: Path = HTML_DEFAULT) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    safe_prompt = html.escape(PROMPT)
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Teacher AI Toolkit - Copy Prototype</title>
<style>
:root{{--paper:#fffdf8;--ink:#172033;--navy:#183153;--teal:#167d7f;--coral:#e8664a;--line:#d7dee8;--soft:#f2f7f7}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--paper);color:var(--ink);font-family:system-ui,sans-serif}}
header{{background:var(--navy);color:white;padding:42px 20px}} header div,main{{max-width:860px;margin:auto}}
.eyebrow{{color:#f0bd58;font-size:12px;font-weight:800;letter-spacing:.14em}} h1{{font-family:Georgia,serif;font-size:clamp(32px,6vw,54px);margin:12px 0}}
main{{padding:32px 20px 80px}} .card{{border:1px solid var(--line);border-radius:18px;background:white;overflow:hidden;box-shadow:0 16px 45px #18315316}}
.meta{{padding:18px 22px;border-bottom:1px solid var(--line);display:flex;gap:8px;flex-wrap:wrap}} .tag{{background:var(--teal);color:white;border-radius:999px;padding:6px 10px;font-size:11px;font-weight:800}}
.body{{padding:24px}} pre{{white-space:pre-wrap;background:var(--soft);border-left:4px solid var(--teal);border-radius:10px;padding:20px;font:14px/1.65 ui-monospace,monospace}}
button{{background:var(--coral);color:white;border:0;border-radius:10px;padding:12px 18px;font-weight:800;cursor:pointer}} button:focus{{outline:3px solid #d59a2d;outline-offset:3px}}
#status{{margin-left:12px;font-weight:700;color:var(--teal)}} .note{{margin-top:22px;color:#667085;font-size:14px}}
</style></head><body><header><div><div class="eyebrow">COPY EXPERIENCE PROTOTYPE</div><h1>The Teacher AI Toolkit</h1><p>Use the real clipboard action here; the PDF stays portable and selectable.</p></div></header>
<main><article class="card" id="lp-001"><div class="meta"><span class="tag">LP-001</span><span class="tag">LESSON PLANNING</span><span class="tag">GRADES 3-12</span></div><div class="body"><h2>A full lesson from one standard</h2><pre id="prompt">{safe_prompt}</pre><button type="button" id="copy">Copy prompt</button><span id="status" role="status" aria-live="polite"></span><p class="note">If clipboard permission is blocked, select the prompt text manually. Never paste identifiable student records into an unapproved service.</p></div></article></main>
<script>
const button=document.getElementById('copy'),status=document.getElementById('status'),prompt=document.getElementById('prompt');
button.addEventListener('click',async()=>{{try{{await navigator.clipboard.writeText(prompt.innerText);status.textContent='Copied';button.textContent='Copied';}}catch(e){{const range=document.createRange();range.selectNodeContents(prompt);const selection=getSelection();selection.removeAllRanges();selection.addRange(range);status.textContent='Clipboard blocked - prompt selected for manual copy';}}}});
</script></body></html>"""
    path.write_text(page, encoding="utf-8")
    return path


def run(pdf: Path = PDF_DEFAULT, companion_html: Path = HTML_DEFAULT) -> tuple[Path, Path]:
    return build_pdf(pdf), build_html(companion_html)


if __name__ == "__main__":
    pdf, companion = run()
    print(f"PDF: {pdf}")
    print(f"HTML: {companion}")
