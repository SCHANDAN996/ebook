"""Markdown -> HTML (dark, with a working Copy button) -> PDF (light, for print).

Content lives in book/. This file only renders it.

    python3 toolkit/build_book.py
"""
import glob
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]

CSS = """
:root{
  --bg:#0d1117; --panel:#161b22; --panel-2:#1b222b; --line:#262d36;
  --ink:#e3e9ef; --dim:#8d97a3; --faint:#5f6a76;
  --accent:#4dd6c1; --accent-dim:#2a6f66; --warn:#e0b04a;
  --pad:26px; --radius:10px;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  margin:0; background:var(--bg); color:var(--ink);
  font:16px/1.7 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,sans-serif;
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

/* ---- prompt card ------------------------------------------------------- */
.card{background:var(--panel); border:1px solid var(--line); border-radius:var(--radius);
      padding:var(--pad); margin:0 0 20px}
.card > *:last-child{margin-bottom:0}
.head{display:flex; align-items:baseline; gap:.7rem; margin-bottom:.35rem;
      flex-wrap:wrap}
.pid{font:600 .78rem/1 ui-monospace,Menlo,Consolas,monospace; letter-spacing:.06em;
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
         font:14.6px/1.6 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}

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
  :root{--bg:#fff; --panel:#fff; --panel-2:#f4f6f8; --line:#d7dee5;
        --ink:#16202b; --dim:#4e5a67; --faint:#6d7883;
        --accent:#0b6f63; --accent-dim:#a8ccc6; --warn:#8a6510}
  body{font-size:10.4pt; line-height:1.55; color:var(--ink); background:#fff}
  .wrap{max-width:100%; padding:0}
  .copy{display:none}
  h1{font-size:20pt} h2{font-size:8.5pt; margin:22pt 0 9pt; break-after:avoid}
  h3{font-size:11.2pt; break-after:avoid}
  p,li{orphans:3; widows:3}

  /* One prompt per page: you look a prompt up, you get a clean page.
     The section heading shares its page with the first prompt under it. */
  .card{break-before:page; page-break-before:always; break-inside:auto;
        padding:0; border:0; border-radius:0; margin:0}
  h2 + .card, .wrap > .card:first-of-type{break-before:auto;
        page-break-before:auto}
  .head{break-after:avoid}

  /* The prompt itself stays whole. */
  .box{break-inside:avoid; page-break-inside:avoid; background:#f6f8fa;
       border:1px solid #c9d6d3; margin-bottom:10pt}
  .bar{background:#e8f1ef; padding:6pt 10pt; border-bottom:1px solid #c9d6d3}
  .bar span{font-size:7pt; color:var(--accent)}
  /* 78-character measure sized to reach the right margin */
  .box pre{color:#131c26; font-size:10pt; line-height:1.52; padding:11pt 12pt;
           white-space:pre-wrap; overflow:visible}
  .pid{background:none; color:var(--accent); padding:0; font-size:.92em;
       letter-spacing:.05em}
  .meta{font-size:8pt; margin-bottom:9pt}
  .lbl{font-size:6.8pt; margin:11pt 0 4pt}
  blockquote{background:#fdf8ec; border-left:2.5pt solid var(--warn);
             break-inside:avoid; color:#4a3a12}
  table{font-size:8.8pt; break-inside:avoid}
  th,td{padding:5pt 8pt}
}
"""

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

LABELS = ("When you need this", "Before you send it", "Fill in", "Example")


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
        out.append(
            '<article class="card"><div class="head">'
            f'<span class="pid">{html.escape(m.group(1))}</span>'
            f"<h3>{html.escape(m.group(2))}</h3></div>" + render_body(rest) + "</article>")
    return "\n".join(out)


def sources():
    fm = ROOT / "book/front-matter"
    pages = [("00-index", fm / "index.md"),
             ("00-how-to-use", fm / "how-to-use.md"),
             ("00-safety", fm / "safety-rules.md")]
    pages += [(f.stem, f) for f in
              sorted((ROOT / "book/manuscript/chapters").glob("*.md"))]
    return pages


def main():
    (ROOT / "output/html").mkdir(parents=True, exist_ok=True)
    (ROOT / "output/pdf").mkdir(parents=True, exist_ok=True)

    pages = sources()
    for name, src in pages:
        text = src.read_text()
        title = re.search(r"^# (.+)", text).group(1)
        body = text.split("\n", 1)[1]
        lede = ""
        m = re.match(r"\s*\*\*(.+?)\*\*\s*\n", body)
        if m:
            lede = m.group(1)
            body = body[m.end():]
        (ROOT / f"output/html/{name}.html").write_text(
            '<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f"<title>{html.escape(title)}</title><style>{CSS}</style></head><body>"
            f'<div class="wrap"><h1>{html.escape(title)}</h1>'
            + (f'<p class="lede">{html.escape(lede)}</p>' if lede else "")
            + render_page(body)
            + f"</div><script>{JS}</script></body></html>", encoding="utf-8")
    print(f"  {len(pages)} HTML pages (dark)")

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("  PDF skipped - pip install playwright && playwright install chromium")
        return

    found = [p for p in sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))
             + ["/usr/bin/chromium", "/usr/bin/google-chrome"] if pathlib.Path(p).exists()]
    for exe in [None] + found:
        try:
            with sync_playwright() as pw:
                b = pw.chromium.launch(**({"executable_path": exe} if exe else {}))
                pg = b.new_page()
                for h in sorted((ROOT / "output/html").glob("*.html")):
                    pg.goto(h.resolve().as_uri(), wait_until="load")
                    pg.emulate_media(media="print")
                    pg.pdf(path=str(ROOT / f"output/pdf/{h.stem}.pdf"), format="A4",
                           print_background=True, prefer_css_page_size=False,
                           margin={"top": "17mm", "bottom": "18mm",
                                   "left": "17mm", "right": "17mm"})
                b.close()
            print("  PDFs built (light, for print)")
            return
        except Exception:
            continue
    print("  PDF failed - open the HTML and print to PDF instead")


if __name__ == "__main__":
    main()
