"""Markdown -> HTML (dark, with a working Copy button) -> PDF (light, for print).

Content lives in book/. This file only renders it.

    python3 toolkit/build_book.py

Each PDF is a full-bleed cover merged in front of body pages that carry a
running header and a page number. After the merge the prompt IDs are read back
out of the finished file and written into the PDF outline, so a 61-page chapter
opens with a clickable list of all 60 prompts.
"""
import glob
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

TITLE = "The Teacher AI Toolkit"
SUBTITLE = "300 copy-paste prompts and 12 multi-step workflows"
AUDIENCE = "for K-12 classroom teachers"
AUDIENCE_LINE = "For K-12 classroom teachers"
EDITION = "First edition"
YEAR = "2026"
TOOLS = "Works in ChatGPT, Claude and Gemini"


def contact():
    """Real support details only. A placeholder is left out, never printed."""
    out = {}
    try:
        import config as cfg
        for k in ("support_email", "support_url"):
            v = str(cfg.PRODUCT.get(k, ""))
            if v and "REPLACE_BEFORE_SELLING" not in v and "CHANGE_ME" not in v:
                out[k] = v
    except Exception:
        pass
    return out


# ------------------------------------------------------------------- the pages
FRONT = {
    "00-index": dict(kicker="Reference", num="", title="Index",
                     count="300 prompts · 12 workflows", blurb=(
        "Every prompt and workflow in the toolkit, listed by ID and by name. "
        "Find the ID here, then open that one chapter file.")),
    "00-how-to-use": dict(kicker="Start here", num="", title="How to use this book",
                          count="Read this first", blurb=(
        "How the prompts are built, which file to open, and the five steps that "
        "turn any prompt in this book into something you can use in class.")),
    "00-safety": dict(kicker="Read once", num="", title="Before you start",
                      count="Applies to every prompt", blurb=(
        "The rules that apply to every prompt in every chapter: student privacy, "
        "what to check before you send, and what never goes into a chat window.")),
}


# --------------------------------------------------------------- shared design
CSS = """
:root{
  --bg:#0d1117; --panel:#161b22; --panel-2:#1b222b; --line:#262d36;
  --ink:#e3e9ef; --dim:#8d97a3; --faint:#5f6a76;
  --accent:#4dd6c1; --accent-dim:#2a6f66; --warn:#e0b04a;
  --pad:26px; --radius:10px;
  --serif:'Bitstream Charter','Charter',Georgia,'Times New Roman',serif;
  --sans:-apple-system,BlinkMacSystemFont,'Segoe UI','Liberation Sans',Roboto,Helvetica,Arial,sans-serif;
  --mono:ui-monospace,SFMono-Regular,Menlo,'DejaVu Sans Mono',Consolas,monospace;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  margin:0; background:var(--bg); color:var(--ink);
  font:16px/1.7 var(--sans);
  font-feature-settings:"kern","liga";
}
.wrap{max-width:760px; margin:0 auto; padding:56px 24px 120px}

/* ---- headings ---------------------------------------------------------- */
h1{font-size:2.15rem; line-height:1.2; letter-spacing:-.022em; margin:0 0 .5rem;
   font-weight:650}
.lede{color:var(--dim); font-size:1.02rem; margin:0 0 2.6rem; max-width:60ch}
h2{font-size:.82rem; font-weight:650; letter-spacing:.14em; text-transform:uppercase;
   color:var(--accent); margin:4rem 0 1.4rem; padding-bottom:.7rem;
   border-bottom:1px solid var(--line)}
h3{font-size:1.06rem; font-weight:620; letter-spacing:-.008em; margin:0; color:var(--ink)}
p{margin:0 0 1.1rem; text-align:justify; text-justify:inter-word;
  hyphens:auto; -webkit-hyphens:auto}
ul{margin:0 0 1.1rem; padding-left:1.15rem}
li{margin:.3rem 0; text-align:justify; hyphens:auto; -webkit-hyphens:auto}
.lede,.meta,.lbl,th,td{text-align:left; hyphens:manual}
strong{font-weight:640; color:#f2f6fa}
code{background:var(--panel-2); border:1px solid var(--line); color:var(--accent);
     padding:1px 6px; border-radius:5px; font-size:.85em}
a{color:var(--accent)}
hr{display:none}

/* ---- tables ------------------------------------------------------------ */
table{border-collapse:collapse; width:100%; margin:0 0 1.8rem; font-size:.91rem}
th,td{text-align:left; padding:11px 14px; border-bottom:1px solid var(--line);
      vertical-align:top}
th{color:var(--dim); font-weight:600; font-size:.76rem; letter-spacing:.08em;
   text-transform:uppercase; border-bottom:1px solid var(--line)}
tbody tr:last-child td{border-bottom:none}
td:first-child{white-space:nowrap; color:var(--accent); font-variant-numeric:tabular-nums}
td:first-child a{text-decoration:none}

/* ---- prompt card ------------------------------------------------------- */
.card{background:var(--panel); border:1px solid var(--line); border-radius:var(--radius);
      padding:var(--pad); margin:0 0 20px}
.card > *:last-child{margin-bottom:0}
.head{display:flex; align-items:baseline; gap:.7rem; margin-bottom:.35rem;
      flex-wrap:wrap}
.pid{font:600 .78rem/1 var(--mono); letter-spacing:.06em;
     color:#0d1117; background:var(--accent); padding:5px 8px; border-radius:5px;
     flex:none}
.meta{color:var(--faint); font-size:.83rem; margin:0 0 1.5rem}
.lbl{font-size:.72rem; font-weight:650; letter-spacing:.13em; text-transform:uppercase;
     color:var(--dim); margin:1.6rem 0 .5rem}
.card .lbl:first-of-type{margin-top:1.2rem}

/* ---- the prompt box ---------------------------------------------------- */
.box{border:1px solid var(--accent-dim); border-radius:var(--radius);
     overflow:hidden; margin:0 0 .4rem; background:#0b0f14}
.bar{display:flex; align-items:center; justify-content:space-between; gap:1rem;
     background:rgba(77,214,193,.09); border-bottom:1px solid var(--accent-dim);
     padding:9px 14px}
.bar span{font-size:.7rem; font-weight:650; letter-spacing:.13em;
          text-transform:uppercase; color:var(--accent)}
.copy{font:600 .78rem/1 inherit; color:#0d1117; background:var(--accent);
      border:0; border-radius:6px; padding:7px 15px; cursor:pointer;
      transition:background .12s, transform .06s}
.copy:hover{background:#66e6d2}
.copy:active{transform:translateY(1px)}
.copy.ok{background:var(--warn)}
/* Prompts are hard-wrapped at ~78 characters. The type is sized so that
   measure reaches the right edge of the box instead of stopping short. */
.box pre{margin:0; padding:18px 20px; overflow-x:auto; white-space:pre-wrap;
         word-break:break-word; color:#d5dfe9;
         font:14.6px/1.6 var(--mono)}

blockquote{margin:0 0 1.4rem; padding:.85rem 1.1rem; border-radius:8px;
  background:rgba(224,176,74,.09); border-left:3px solid var(--warn);
  color:#f0e2c4; font-size:.92rem; max-width:66ch}
blockquote p{margin:0}
blockquote strong{color:var(--warn)}

@media(max-width:640px){
  .wrap{padding:34px 16px 80px} :root{--pad:18px}
  h1{font-size:1.7rem} .box pre{padding:14px; font-size:12.5px}
}

/* ---- print: flip to light, drop the buttons ---------------------------- */
@media print{
  :root{--bg:#fff; --panel:#fff; --panel-2:#f4f6f8; --line:#d7dee8;
        --ink:#172033; --dim:#5b6775; --faint:#6d7883;
        --accent:#0f6e68; --accent-dim:#a8ccc6; --warn:#8a6510}
  @page{size:A4; margin:20mm 17mm 18mm}
  body{font-size:10.6pt; line-height:1.58; color:var(--ink); background:#fff;
       font-family:var(--serif)}
  .wrap{max-width:100%; padding:0}
  .copy{display:none}
  p,li{orphans:3; widows:3}

  /* The chapter opener sits on the first body page, under the cover. */
  h1{font-family:var(--serif); font-size:19pt; font-weight:700; letter-spacing:-.01em;
     color:var(--navy,#183153); margin:0 0 3pt}
  .lede{font-family:var(--sans); font-size:8.5pt; letter-spacing:.13em; max-width:none;
        text-transform:uppercase; color:var(--accent); margin:0 0 16pt;
        padding-bottom:10pt; border-bottom:2px solid var(--accent)}
  h2{font-family:var(--sans); font-size:8pt; letter-spacing:.15em; margin:22pt 0 9pt;
     break-after:avoid; padding-bottom:5pt; border-bottom:1px solid var(--line)}
  h3{font-family:var(--serif); font-size:12.5pt; font-weight:700; break-after:avoid;
     color:#101a26}

  /* One prompt per page: you look a prompt up, you get a clean page.
     The section heading shares its page with the first prompt under it. */
  .card{break-before:page; page-break-before:always; break-inside:auto;
        padding:0; border:0; border-radius:0; margin:0}
  /* A group heading starts a fresh page and keeps its first prompt with it.
     :has() limits this to headings that actually introduce a prompt, so the
     chapter opener's own headings stay where they are. */
  h2:has(+ .card){break-before:page; page-break-before:always; margin-top:0}
  h2 + .card{break-before:auto; page-break-before:auto}
  .head{break-inside:avoid; break-after:avoid; display:block; margin-bottom:2pt}
  .pid{display:block; background:none; color:var(--accent); padding:0;
       font:700 8.4pt/1 var(--sans); letter-spacing:.16em; margin-bottom:3pt}
  .meta{font-family:var(--sans); font-size:8pt; color:var(--faint); margin:0 0 12pt;
        padding-bottom:9pt; border-bottom:1px solid var(--line)}
  .lbl{font-family:var(--sans); font-size:7pt; letter-spacing:.15em;
       margin:13pt 0 5pt; color:var(--dim)}
  /* The screen theme lifts bold text to near-white. On paper that is invisible. */
  strong{color:#101a26; font-weight:700}

  /* The prompt itself stays whole. */
  .box{break-inside:avoid; page-break-inside:avoid; background:#f5f8f8;
       border:1px solid #cfe0dd; border-left:3pt solid var(--accent);
       border-radius:3pt; margin-bottom:10pt}
  .bar{background:#e6f0ee; padding:5pt 10pt; border-bottom:1px solid #cfe0dd}
  .bar span{font-family:var(--sans); font-size:6.8pt; color:var(--accent)}
  /* 78-character measure sized to reach the right margin */
  .box pre{color:#131c26; font-size:10pt; line-height:1.52; padding:11pt 12pt;
           white-space:pre-wrap; overflow:visible; font-family:var(--mono)}

  blockquote{background:#fdf8ec; border-left:2.5pt solid var(--warn);
             border-radius:3pt; break-inside:avoid; color:#4a3a12;
             font-family:var(--sans); font-size:9pt}
  table{font-size:8.8pt; break-inside:avoid; font-family:var(--sans)}
  th,td{padding:5pt 8pt}
  th{font-size:6.8pt}
  code{background:#eef2f5; border:1px solid var(--line); font-family:var(--mono)}
  a{color:var(--accent); text-decoration:none}
}
"""

COMPLETE_CSS = """
.cover{min-height:88vh; display:flex; flex-direction:column; justify-content:center;
  border-bottom:1px solid var(--line); margin-bottom:3rem; padding-bottom:3rem}
.covertitle{font-size:3rem; line-height:1.08; letter-spacing:-.03em; margin:0 0 1.2rem}
.coversub{font-size:1.15rem; color:var(--accent); margin:0 0 2.4rem; text-align:left}
.coverline{color:var(--dim); font-size:.95rem; text-align:left; margin:0}
h1.chap{font-size:2rem; margin:0 0 .4rem}
@media print{
  .cover{display:none}
  h1.chap{break-before:page; page-break-before:always}
}
"""

# ------------------------------------------------------------------ the cover
# A separate one-page document rendered at zero margin, then merged in front of
# the body. Doing it this way is what allows full-bleed colour on the cover and
# a page number on every other page.
COVER_CSS = """
*{box-sizing:border-box; margin:0; padding:0}
@page{size:A4; margin:0}
html,body{width:210mm; height:297mm}
body{font-family:%(sans)s; color:#172033; background:#fff;
     -webkit-print-color-adjust:exact; print-color-adjust:exact}
.top{background:#183153; color:#fff; height:186mm; padding:26mm 22mm 30mm;
     position:relative; overflow:hidden;
     display:flex; flex-direction:column; justify-content:flex-end}
.top:after{content:""; position:absolute; left:0; right:0; bottom:0; height:3mm;
           background:#0f9e91}
.rule{width:26mm; height:1.4mm; background:#0f9e91; margin-bottom:9mm}
.kicker{font-size:9.5pt; letter-spacing:.30em; text-transform:uppercase;
        color:#8fd6cd; font-weight:700}
.num{position:absolute; right:18mm; top:30mm; font-family:%(serif)s;
     font-size:170pt; line-height:1; font-weight:700; color:rgba(143,214,205,.11)}
.title{font-family:%(serif)s; font-size:38pt; line-height:1.1; font-weight:700;
       letter-spacing:-.015em; margin:6mm 0 0; max-width:150mm}
.count{margin-top:9mm; font-size:11pt; letter-spacing:.16em; text-transform:uppercase;
       color:#8fd6cd; font-weight:700}
.bottom{height:111mm; padding:16mm 22mm 14mm; display:flex; flex-direction:column;
        justify-content:space-between}
.blurb{font-family:%(serif)s; font-size:13pt; line-height:1.55; color:#3a4756;
       max-width:150mm}
.foot{border-top:1px solid #d7dee8; padding-top:6mm; font-size:8.5pt;
      line-height:1.7; color:#5b6775}
.foot .brand{font-family:%(serif)s; font-size:12pt; font-weight:700; color:#183153;
             display:block; margin-bottom:2mm}
.foot .tools{color:#0f6e68; font-weight:600}
""" % dict(sans=("-apple-system,BlinkMacSystemFont,'Segoe UI','Liberation Sans',"
                 "Roboto,Helvetica,Arial,sans-serif"),
           serif="'Bitstream Charter','Charter',Georgia,'Times New Roman',serif")


def cover_html(kicker, num, title, count, blurb):
    c = contact()
    tail = []
    if c.get("support_url"):
        tail.append(html.escape(c["support_url"]))
    if c.get("support_email"):
        tail.append(html.escape(c["support_email"]))
    tail = " &nbsp;·&nbsp; ".join(tail)
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        f'<title>{html.escape(title)}</title><style>{COVER_CSS}</style></head><body>'
        '<div class="top">'
        + (f'<div class="num">{html.escape(num)}</div>' if num else "")
        + '<div class="rule"></div>'
        f'<div class="kicker">{html.escape(kicker)}</div>'
        f'<h1 class="title">{html.escape(title)}</h1>'
        + (f'<div class="count">{html.escape(count)}</div>' if count else "")
        + '</div><div class="bottom">'
        f'<p class="blurb">{html.escape(blurb)}</p>'
        '<div class="foot">'
        # On the master cover the title is already the headline; name the
        # audience there instead of repeating it.
        f'<span class="brand">{html.escape(AUDIENCE_LINE if title == TITLE else TITLE)}</span>'
        f'<span class="tools">{html.escape(TOOLS)}</span><br>'
        f'{html.escape(EDITION)} &nbsp;·&nbsp; &copy; {YEAR}. '
        'Licensed to one teacher for classroom use. Do not redistribute.'
        + (f'<br>{tail}' if tail else "")
        + '</div></div></body></html>')


# ------------------------------------------------------------ running furniture
def header_template(chapter):
    return (
        '<div style="width:100%;font-size:7pt;font-family:Helvetica,Arial,sans-serif;'
        'color:#8b96a3;padding:0 17mm;margin-top:8mm;">'
        '<div style="border-bottom:.5pt solid #dde3ea;padding-bottom:2mm;'
        'display:flex;justify-content:space-between;">'
        f'<span>{html.escape(TITLE)}</span>'
        f'<span>{html.escape(chapter)}</span></div></div>')


FOOTER_TEMPLATE = (
    '<div style="width:100%;font-size:7.5pt;font-family:Helvetica,Arial,sans-serif;'
    'color:#8b96a3;padding:0 17mm;margin-bottom:7mm;text-align:right;">'
    '<span class="pageNumber"></span></div>')


# Clipboard API only works over https/localhost. Opened from disk (file://) it
# fails silently, so fall back to execCommand, which does work there.
JS = """
function copyText(t){
  if(navigator.clipboard && window.isSecureContext){
    return navigator.clipboard.writeText(t);
  }
  return new Promise(function(res,rej){
    var a=document.createElement('textarea');
    a.value=t; a.setAttribute('readonly','');
    a.style.cssText='position:fixed;top:0;left:0;opacity:0';
    document.body.appendChild(a);
    a.select(); a.setSelectionRange(0,a.value.length);
    var ok=false;
    try{ ok=document.execCommand('copy'); }catch(e){ ok=false; }
    document.body.removeChild(a);
    ok?res():rej();
  });
}
document.querySelectorAll('.copy').forEach(function(b){
  b.addEventListener('click',function(){
    var t=b.closest('.box').querySelector('pre').innerText;
    copyText(t).then(function(){
      b.textContent='Copied'; b.classList.add('ok');
      setTimeout(function(){b.textContent='Copy'; b.classList.remove('ok')},1600);
    }).catch(function(){
      b.textContent='Select it'; b.classList.add('ok');
      var r=document.createRange(); r.selectNodeContents(b.closest('.box').querySelector('pre'));
      var s=window.getSelection(); s.removeAllRanges(); s.addRange(r);
      setTimeout(function(){b.textContent='Copy'; b.classList.remove('ok')},2600);
    });
  });
});
"""

LABELS = ("When you need this", "Before you send it", "Before you use it",
          "Then, one at a time", "Fill in", "Example")


def inline(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\w)`([^`]+)`", r"<code>\1</code>", s)
    return s


def render_body(text):
    """Markdown block -> HTML. Consecutive lines join into one paragraph."""
    blocks = []

    def stash(m):
        blocks.append(m.group(1))
        return f"\x00B{len(blocks) - 1}\x00"

    text = re.sub(r"```text\n(.*?)\n```", stash, text, flags=re.S)

    out, para, table, items = [], [], [], []

    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    def flush_items():
        if items:
            out.append("<ul>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>")
            items.clear()

    def flush_table():
        if table:
            # keep every row except the |---|---| separator
            rows = [r for r in table if not set("".join(r)) <= set("-: ")]
            if not rows:
                table.clear()
                return
            out.append("<table><thead><tr>"
                       + "".join(f"<th>{inline(c)}</th>" for c in rows[0])
                       + "</tr></thead><tbody>")
            for r in rows[1:]:
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            out.append("</tbody></table>")
            table.clear()

    for line in text.split("\n"):
        s = line.strip()
        if s.startswith("|"):
            flush_para(); flush_items()
            table.append([c.strip() for c in s.strip("|").split("|")])
            continue
        flush_table()

        if not s:
            flush_para(); flush_items()
            continue
        if s.startswith("\x00B"):
            flush_para(); flush_items(); out.append(s); continue
        if s == "---" or s == "**TO HERE**":
            flush_para(); flush_items(); continue

        m = re.match(r"(#{2,4}) (.+)", s)
        if m:
            flush_para(); flush_items()
            n = min(len(m.group(1)), 4)
            out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
            continue
        if s.startswith("> "):
            flush_para(); flush_items()
            out.append("<blockquote><p>" + inline(s[2:]) + "</p></blockquote>")
            continue
        if s.startswith("- "):
            flush_para()
            items.append(s[2:])
            continue
        if s.startswith("*") and s.endswith("*") and not s.startswith("**"):
            flush_para(); flush_items()
            out.append(f'<p class="meta">{inline(s[1:-1])}</p>')
            continue
        stripped = s.strip("*")
        if s.startswith("**") and s.endswith("**") and stripped in LABELS:
            flush_para(); flush_items()
            out.append(f'<p class="lbl">{stripped}</p>')
            continue
        if s == "**COPY FROM HERE**":
            flush_para(); flush_items(); continue

        para.append(s)

    flush_para(); flush_items(); flush_table()
    h = "\n".join(out)
    for i, b in enumerate(blocks):
        h = h.replace(
            f"\x00B{i}\x00",
            '<div class="box"><div class="bar"><span>Copy this prompt</span>'
            '<button class="copy">Copy</button></div><pre>'
            + html.escape(b) + "</pre></div>")
    return h


def render_page(text):
    """Split on prompt headings so each prompt becomes its own card."""
    parts = re.split(r"\n(?=### )", text)
    out = [render_body(parts[0])]
    for part in parts[1:]:
        m = re.match(r"### (\S+) · (.+)", part)
        if not m:
            out.append(render_body(part))
            continue
        rest = part.split("\n", 1)[1] if "\n" in part else ""
        pid = m.group(1)
        out.append(
            f'<article class="card" id="{html.escape(pid)}"><div class="head">'
            f'<span class="pid">{html.escape(pid)}</span>'
            f"<h3>{html.escape(m.group(2))}</h3></div>"
            + render_body(rest) + "</article>")
    return "\n".join(out)


def prompt_ids(text):
    """The prompts in a chapter, in the order they appear. Used for bookmarks."""
    return [(m.group(1), m.group(2).strip())
            for m in re.finditer(r"^### (\S+) · (.+)$", text, flags=re.M)]


def sources():
    fm = ROOT / "book/front-matter"
    pages = [("00-index", fm / "index.md"),
             ("00-how-to-use", fm / "how-to-use.md"),
             ("00-safety", fm / "safety-rules.md")]
    pages += [(f.stem, f) for f in
              sorted((ROOT / "book/manuscript/chapters").glob("*.md"))]
    return pages


def preflight():
    """Refuse to build a sellable edition with placeholders still in it."""
    import config as cfg
    bad = []
    for k, v in cfg.PRODUCT.items():
        if isinstance(v, str) and ("REPLACE_BEFORE_SELLING" in v or "CHANGE_ME" in v):
            bad.append("config.PRODUCT[%r] = %r" % (k, v))
    for f in sorted((ROOT / "book/manuscript/chapters").glob("*.md")):
        t = f.read_text()
        for marker in ("REPLACE_BEFORE_SELLING", "CHANGE_ME", "TODO", "FIXME"):
            if marker in t:
                bad.append("%s contains %s" % (f.name, marker))
    return bad


def split_head(text):
    """-> (title, lede, body)."""
    title = re.search(r"^# (.+)", text).group(1)
    body = text.split("\n", 1)[1]
    lede = ""
    m = re.match(r"\s*\*\*(.+?)\*\*\s*\n", body)
    if m:
        lede = m.group(1)
        body = body[m.end():]
    return title, lede, body


def first_sentence(body, limit=260):
    """The chapter's opening paragraph, for the cover blurb."""
    for para in body.split("\n\n"):
        p = " ".join(l.strip() for l in para.strip().split("\n"))
        if p and not p.startswith(("#", "|", "-", ">", "*", "`")):
            p = re.sub(r"\*\*(.+?)\*\*", r"\1", p)
            if len(p) <= limit:
                return p
            cut = p[:limit].rsplit(". ", 1)[0]
            return cut + "." if cut else p[:limit].rsplit(" ", 1)[0] + "…"
    return ""


def cover_meta(name, title, lede, body):
    """Cover fields for one output file."""
    if name in FRONT:
        return dict(FRONT[name])
    m = re.match(r"Chapter (\d+) — (.+)", title)
    num, short = (m.group(1), m.group(2)) if m else ("", title)
    return dict(kicker=f"Chapter {num}" if num else "Chapter", num=num,
                title=short, count=lede, blurb=first_sentence(body))


def link_index(page_html):
    """In the complete edition the index IDs jump to the prompt itself."""
    return re.sub(r"<td>([A-Z]{2}-\d{3})</td>",
                  r'<td><a href="#\1">\1</a></td>', page_html)


def build_complete(pages):
    """One file with everything, for buyers who want a single download."""
    parts = []
    for name, src in pages:
        title, lede, body = split_head(src.read_text())
        block = (f'<h1 class="chap" id="{html.escape(name)}">{html.escape(title)}</h1>'
                 + (f'<p class="lede">{html.escape(lede)}</p>' if lede else "")
                 + render_page(body))
        parts.append(link_index(block) if name == "00-index" else block)
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{html.escape(TITLE)}</title><style>{CSS}{COMPLETE_CSS}</style>'
            '</head><body><div class="wrap">'
            '<section class="cover">'
            f'<h1 class="covertitle">{html.escape(TITLE)}</h1>'
            f'<p class="coversub">{html.escape(SUBTITLE)}<br>{html.escape(AUDIENCE)}</p>'
            f'<p class="coverline">{html.escape(TOOLS)}.<br>'
            'Ten chapters. Open only the one you need.</p></section>'
            + "\n".join(parts) + f"</div><script>{JS}</script></body></html>")


# ------------------------------------------------------------------ PDF output
def chromium():
    """The first Chromium that actually launches, or None."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return None
    found = [p for p in
             sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))
             + ["/usr/bin/chromium", "/usr/bin/google-chrome"]
             if pathlib.Path(p).exists()]
    pw = sync_playwright().start()
    for exe in found + [None]:
        try:
            return pw, pw.chromium.launch(
                args=["--no-sandbox"],
                **({"executable_path": exe} if exe else {}))
        except Exception as e:
            last = e
    pw.stop()
    print("  no Chromium could be launched: %s" % last)
    return None


def render_pdf(page, url, out, header=None):
    page.goto(url, wait_until="load")
    page.emulate_media(media="print")
    if header is None:
        page.pdf(path=str(out), format="A4", print_background=True,
                 prefer_css_page_size=True,
                 margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
    else:
        page.pdf(path=str(out), format="A4", print_background=True,
                 prefer_css_page_size=False,
                 display_header_footer=True,
                 header_template=header_template(header),
                 footer_template=FOOTER_TEMPLATE,
                 margin={"top": "20mm", "bottom": "18mm",
                         "left": "17mm", "right": "17mm"})


def page_text(reader):
    """Each page's text, plus a whitespace-free copy of it.

    The prompt ID is set with wide letter-spacing, so Chromium writes it into
    the PDF as "L P - 0 0 6". Searching the flattened copy finds it anyway.
    """
    out = []
    for p in reader.pages:
        try:
            raw = p.extract_text() or ""
        except Exception:
            raw = ""
        out.append((raw, re.sub(r"\s+", "", raw)))
    return out


def find_pages(text, ids, start=0):
    """Which page each prompt ID lands on, searching forward only.

    Forward-only matters: the index lists every ID in the book, so a plain
    search would find them all on the index pages. `start` keeps each chapter's
    search inside that chapter.
    """
    where, at = {}, start
    for pid, _ in ids:
        # A prompt opens its own page, so the page whose text starts with the ID
        # is the right one. Chapter openers list every ID in a table, so plain
        # containment is only a fallback.
        hit = next((i for i in range(at, len(text))
                    if text[i][1].startswith(pid)), None)
        if hit is None:
            hit = next((i for i in range(at, len(text))
                        if pid in text[i][1]), None)
        if hit is not None:
            where[pid] = hit
            at = hit
    return where


def finish(cover_pdf, body_pdf, out, title, tree):
    """Cover + body -> one file with an outline and real metadata.

    `tree` is [(label, body_page, [(label, body_page), ...]), ...]; body pages
    are shifted by one to make room for the cover.
    """
    from pypdf import PdfReader, PdfWriter
    w = PdfWriter()
    w.append(PdfReader(str(cover_pdf)))
    w.append(PdfReader(str(body_pdf)))
    offset = 1  # the cover

    w.add_outline_item("Cover", 0)
    for label, page, children in tree:
        parent = w.add_outline_item(label, page + offset)
        for child_label, child_page in children:
            w.add_outline_item(child_label, child_page + offset, parent=parent)

    w.add_metadata({
        "/Title": title if title == TITLE else f"{title} — {TITLE}",
        "/Author": TITLE,
        "/Subject": f"{SUBTITLE} {AUDIENCE}",
        "/Keywords": ("teaching, lesson planning, AI prompts, ChatGPT, Claude, "
                      "Gemini, K-12, classroom"),
        "/Creator": TITLE,
    })
    w.page_layout = "/SinglePage"
    w.page_mode = "/UseOutlines"   # open with the bookmark panel showing
    with open(out, "wb") as fh:
        w.write(fh)


def build_pdfs(pages):
    got = chromium()
    if not got:
        print("  PDF skipped - pip install playwright")
        return
    pw, browser = got
    try:
        from pypdf import PdfReader
    except ImportError:
        print("  PDF outline skipped - pip install pypdf")
        PdfReader = None

    tmp = ROOT / "output/.tmp"
    tmp.mkdir(parents=True, exist_ok=True)
    page = browser.new_page()

    for name, src, meta, ids, title in pages:
        (tmp / f"{name}-cover.html").write_text(cover_html(**meta), encoding="utf-8")
        render_pdf(page, (tmp / f"{name}-cover.html").resolve().as_uri(),
                   tmp / f"{name}-cover.pdf")
        render_pdf(page, (ROOT / f"output/html/{name}.html").resolve().as_uri(),
                   tmp / f"{name}-body.pdf", header=meta["title"])
        out = ROOT / f"output/pdf/{name}.pdf"
        if PdfReader is None:
            (tmp / f"{name}-body.pdf").replace(out)
            continue
        text = page_text(PdfReader(str(tmp / f"{name}-body.pdf")))
        where = find_pages(text, ids)
        tree = [(title, 0, [(f"{pid} — {name_}", where[pid])
                            for pid, name_ in ids if pid in where])]
        finish(tmp / f"{name}-cover.pdf", tmp / f"{name}-body.pdf", out, title,
               tree)

    # the complete edition
    cm = dict(kicker="Complete edition", num="", title=TITLE,
              count=f"300 prompts · 12 workflows", blurb=(
                  "Every chapter of the toolkit in one file, for reading offline "
                  "or printing. The single chapter files are quicker to work from."))
    (tmp / "all-cover.html").write_text(cover_html(**cm), encoding="utf-8")
    render_pdf(page, (tmp / "all-cover.html").resolve().as_uri(), tmp / "all-cover.pdf")
    render_pdf(page,
               (ROOT / "output/html/teacher-ai-toolkit-complete.html").resolve().as_uri(),
               tmp / "all-body.pdf", header="Complete edition")
    out = ROOT / "output/pdf/teacher-ai-toolkit-complete.pdf"
    if PdfReader is not None:
        text = page_text(PdfReader(str(tmp / "all-body.pdf")))
        tree, at = [], 0
        for chapter_title, ids in COMPLETE_CHAPTERS:
            for i in range(at, len(text)):
                if text[i][0].lstrip().startswith(chapter_title):
                    at = i
                    break
            where = find_pages(text, ids, at)
            tree.append((chapter_title, at,
                         [(f"{pid} — {name_}", where[pid])
                          for pid, name_ in ids if pid in where]))
        finish(tmp / "all-cover.pdf", tmp / "all-body.pdf", out, TITLE, tree)
    else:
        (tmp / "all-body.pdf").replace(out)

    browser.close()
    pw.stop()
    for f in tmp.glob("*"):
        f.unlink()
    tmp.rmdir()
    print("  PDFs built - covers, page numbers, bookmarks")


COMPLETE_CHAPTERS = []


def main():
    problems = preflight()
    for problem in problems:
        print("  ! %s" % problem)
    if problems:
        print("  ! the PDFs will build, but do not sell them until these are set")
    (ROOT / "output/html").mkdir(parents=True, exist_ok=True)
    (ROOT / "output/pdf").mkdir(parents=True, exist_ok=True)

    srcs = sources()
    jobs = []
    for name, src in srcs:
        text = src.read_text()
        title, lede, body = split_head(text)
        page_html = render_page(body)
        if name == "00-index":
            page_html = link_index(page_html)
        (ROOT / f"output/html/{name}.html").write_text(
            '<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f"<title>{html.escape(title)}</title><style>{CSS}</style></head><body>"
            f'<div class="wrap"><h1>{html.escape(title)}</h1>'
            + (f'<p class="lede">{html.escape(lede)}</p>' if lede else "")
            + page_html
            + f"</div><script>{JS}</script></body></html>", encoding="utf-8")
        ids = prompt_ids(text)
        jobs.append((name, src, cover_meta(name, title, lede, body), ids, title))
        COMPLETE_CHAPTERS.append((title, ids))

    (ROOT / "output/html/teacher-ai-toolkit-complete.html").write_text(
        build_complete(srcs), encoding="utf-8")
    print(f"  {len(srcs)} HTML pages + 1 complete edition")

    build_pdfs(jobs)


if __name__ == "__main__":
    main()
