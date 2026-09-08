"""Markdown -> HTML (with a Copy button on every prompt) -> PDF.

Content lives in book/. This file only renders it. Run after editing any
markdown source:

    python3 toolkit/build_book.py
"""
import glob
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]

CSS = """
*{box-sizing:border-box}
body{font:16px/1.65 -apple-system,'Segoe UI',Roboto,sans-serif;color:#1b2733;
 max-width:820px;margin:0 auto;padding:32px 20px 80px;background:#fff}
h1{font-size:2em;letter-spacing:-.02em;margin:0 0 .3em}
h2{font-size:1.35em;margin:2.2em 0 .6em;padding-top:1em;border-top:1px solid #e4e9ee}
h3{font-size:1.12em;margin:1.6em 0 .2em;letter-spacing:-.01em}
table{border-collapse:collapse;width:100%;margin:1em 0;font-size:.93em}
th,td{border:1px solid #e4e9ee;padding:7px 10px;text-align:left}
th{background:#f6f8fa;font-weight:600}
blockquote{margin:1em 0;padding:.7em 1em;background:#fdf7e8;
 border-left:3px solid #ddae58;font-size:.94em}
.meta{font-size:.83em;color:#6b7885;margin:0 0 1em}
.lbl{font-size:.73em;letter-spacing:.09em;text-transform:uppercase;color:#6b7885;
 font-weight:600;margin:1.4em 0 .4em}
.box{position:relative;background:#f6f8fa;border:1px solid #dde3e9;border-radius:8px;
 padding:16px 18px;margin:.4em 0 1em}
.box pre{margin:0;white-space:pre-wrap;color:#243240;
 font:13.5px/1.55 ui-monospace,Menlo,Consolas,monospace}
.copy{position:absolute;top:10px;right:10px;border:1px solid #cdd5dd;background:#fff;
 border-radius:6px;padding:5px 12px;font-size:12.5px;cursor:pointer;color:#33414f}
.copy:hover{background:#eef2f6}
.copy.ok{background:#167d8d;border-color:#167d8d;color:#fff}
hr{border:0;border-top:1px solid #e4e9ee;margin:2.4em 0}
ul{padding-left:1.3em;margin:.4em 0}
code{background:#eef2f6;padding:1px 5px;border-radius:4px;font-size:.9em}
a{color:#167d8d}
@media(max-width:600px){body{padding:18px 14px 60px}}
"""

JS = """document.querySelectorAll(".copy").forEach(function(b){b.onclick=function(){
var t=b.parentNode.querySelector("pre").innerText;
navigator.clipboard.writeText(t).then(function(){b.textContent="Copied";
b.classList.add("ok");setTimeout(function(){b.textContent="Copy";
b.classList.remove("ok")},1600)})}})"""

LABELS = r"COPY FROM HERE|TO HERE|When you need this|Before you send it"


def to_html(text):
    blocks = []

    def stash(m):
        blocks.append(m.group(1))
        return f"\x00B{len(blocks) - 1}\x00"

    text = re.sub(r"```text\n(.*?)\n```", stash, text, flags=re.S)

    out, table = [], []
    for line in text.split("\n"):
        s = line.strip()
        if s.startswith("|"):
            table.append([c.strip() for c in s.strip("|").split("|")])
            continue
        if table:
            out.append("<table>")
            for i, row in enumerate(table):
                if set("".join(row)) <= set("-: "):
                    continue
                tag = "th" if i == 0 else "td"
                out.append("<tr>" + "".join(f"<{tag}>{c}</{tag}>" for c in row) + "</tr>")
            out.append("</table>")
            table = []
        if not s:
            continue
        if s.startswith("\x00B"):
            out.append(s)
            continue
        m = re.match(r"(#{1,4}) (.+)", s)
        if m:
            n = len(m.group(1))
            out.append(f"<h{n}>{m.group(2)}</h{n}>")
            continue
        if s.startswith("> "):
            out.append("<blockquote>" + s[2:] + "</blockquote>")
            continue
        if s.startswith("- "):
            out.append("<li>" + s[2:] + "</li>")
            continue
        if s == "---":
            out.append("<hr>")
            continue
        if s.startswith("*") and s.endswith("*") and not s.startswith("**"):
            out.append(f'<p class="meta">{s[1:-1]}</p>')
            continue
        if re.fullmatch(rf"\*\*({LABELS})\*\*", s):
            out.append(f'<p class="lbl">{s.strip("*")}</p>')
            continue
        out.append("<p>" + s + "</p>")

    h = "\n".join(out)
    h = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", h)
    h = re.sub(r"(?<!\w)`([^`]+)`", r"<code>\1</code>", h)
    h = re.sub(r"(<li>.*?</li>\n?)+",
               lambda m: "<ul>" + m.group(0).rstrip("\n") + "</ul>", h, flags=re.S)
    for i, b in enumerate(blocks):
        h = h.replace(
            f"\x00B{i}\x00",
            '<div class="box"><button class="copy">Copy</button><pre>'
            + html.escape(b) + "</pre></div>")
    return h


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

    for name, src in sources():
        text = src.read_text()
        title = re.search(r"^# (.+)", text).group(1)
        (ROOT / f"output/html/{name}.html").write_text(
            '<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f"<title>{html.escape(title)}</title><style>{CSS}</style></head><body>"
            + to_html(text) + f"<script>{JS}</script></body></html>",
            encoding="utf-8")
    print(f"  {len(sources())} HTML pages")

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
                    pg.add_style_tag(content=".copy{display:none}"
                                             "h3,blockquote{page-break-after:avoid}"
                                             ".box{page-break-inside:avoid}")
                    pg.pdf(path=str(ROOT / f"output/pdf/{h.stem}.pdf"), format="A4",
                           print_background=True,
                           margin={"top": "16mm", "bottom": "18mm",
                                   "left": "15mm", "right": "15mm"})
                b.close()
            print("  PDFs built")
            return
        except Exception:
            continue
    print("  PDF failed - open the HTML and print to PDF instead")


if __name__ == "__main__":
    main()
