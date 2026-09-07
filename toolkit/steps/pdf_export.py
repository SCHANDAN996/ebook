"""Local HTML-subset to PDF export. No browser, network, or AI SDK required."""
import html
from html.parser import HTMLParser
from pathlib import Path
import re


def export_pdf(source, destination, title, footer="Development edition"):
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle

    font_dir = Path("/usr/share/fonts/truetype/dejavu")
    if (font_dir / "DejaVuSans.ttf").exists():
        for name, filename in [("Body", "DejaVuSans.ttf"), ("Body-Bold", "DejaVuSans-Bold.ttf"),
                               ("Body-Oblique", "DejaVuSans-Oblique.ttf"),
                               ("Body-BoldOblique", "DejaVuSans-BoldOblique.ttf")]:
            path = font_dir / filename
            if not path.exists():
                path = font_dir / "DejaVuSans.ttf"
            pdfmetrics.registerFont(TTFont(name, str(path)))
        pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold",
                                      italic="Body-Oblique", boldItalic="Body-BoldOblique")
        font = "Body"
    else:
        font = "Helvetica"
    styles = {
        "p": ParagraphStyle("body", fontName=font, fontSize=10, leading=15,
                            spaceAfter=7, alignment=TA_LEFT, splitLongWords=True),
        "prompt": ParagraphStyle("prompt", fontName=font, fontSize=9.5, leading=14,
                                 backColor=colors.HexColor("#f0f4f7"), borderPadding=8,
                                 spaceBefore=7, spaceAfter=14),
        "note": ParagraphStyle("note", fontName=font, fontSize=9, leading=14,
                               backColor=colors.HexColor("#fff4d8"), borderPadding=8,
                               spaceBefore=7, spaceAfter=14),
    }
    for level, size in [(1, 25), (2, 17), (3, 12), (4, 11), (5, 10), (6, 10)]:
        styles[f"h{level}"] = ParagraphStyle(f"h{level}", fontName=font,
            fontSize=size, leading=size * 1.35, spaceBefore=14 if level > 1 else 0,
            spaceAfter=9, keepWithNext=True, textColor=colors.HexColor("#123c45"))
    for name in ("meta", "use", "label", "sectionnote"):
        styles[name] = ParagraphStyle(name, parent=styles["p"], keepWithNext=True)

    story = []
    class Parser(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.frame = None
            self.depth = 0
            self.hidden = 0
            self.table = None
            self.row = None
            self.cell = None

        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            if tag in {"style", "script", "head"}:
                self.hidden += 1
                return
            if self.hidden:
                return
            if tag == "table":
                self.table = []
                return
            if self.table is not None:
                if tag == "tr":
                    self.row = []
                elif tag in {"td", "th"}:
                    self.cell = []
                return
            if self.frame:
                if tag == self.frame["tag"]:
                    self.depth += 1
                if tag in {"strong", "b", "em", "i"}:
                    self.frame["parts"].append(f"<{tag}>")
                elif tag == "br":
                    self.frame["parts"].append("<br/>")
                elif tag == "a":
                    href = attrs.get("href", "")
                    if href.startswith(("https://", "mailto:", "#")):
                        self.frame["parts"].append(f'<a href="{html.escape(href, quote=True)}" color="#176878">')
                        self.frame["link"] = True
                return
            kind = attrs.get("class", "") if tag == "div" else tag
            if tag == "p" and attrs.get("class") in styles:
                kind = attrs["class"]
            if kind in styles or tag == "li" or kind == "raw":
                self.frame = {"tag": tag, "kind": kind, "parts": [], "id": attrs.get("id")}
                self.depth = 1

        def handle_endtag(self, tag):
            if tag in {"style", "script", "head"}:
                self.hidden = max(0, self.hidden - 1)
                return
            if self.hidden:
                return
            if self.table is not None:
                if tag in {"td", "th"} and self.cell is not None:
                    self.row.append(Paragraph("".join(self.cell), styles["p"]))
                    self.cell = None
                elif tag == "tr" and self.row is not None:
                    self.table.append(self.row)
                    self.row = None
                elif tag == "table":
                    rows, self.table = self.table, None
                    if rows:
                        columns = max(len(row) for row in rows)
                        rows = [row + [""] * (columns - len(row)) for row in rows]
                        table = Table(rows, colWidths=[(A4[0] - 38 * mm) / columns] * columns,
                                      repeatRows=1, splitByRow=1, splitInRow=1, spaceAfter=12)
                        table.setStyle(TableStyle([
                            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e2edf0")),
                            ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#bdcfd6")),
                            ("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 6),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 6)]))
                        story.append(table)
                return
            if not self.frame:
                return
            if tag in {"strong", "b", "em", "i"}:
                self.frame["parts"].append(f"</{tag}>")
            elif tag == "a" and self.frame.pop("link", False):
                self.frame["parts"].append("</a>")
            if tag != self.frame["tag"]:
                return
            self.depth -= 1
            if self.depth:
                return
            frame, self.frame = self.frame, None
            text = "".join(frame["parts"]).strip()
            if not text:
                return
            kind = frame["kind"]
            if frame["tag"] == "li":
                text = "- " + text
            para = Paragraph(text, styles.get(kind, styles["p"]))
            if kind in {"h1", "h2"} and frame["id"]:
                para.bookmark = (frame["id"], re.sub("<[^>]+>", "", html.unescape(text)))
            story.append(para)

        def handle_data(self, data):
            if self.table is not None and self.cell is not None:
                self.cell.append(html.escape(data))
                return
            if self.frame and not self.hidden:
                text = html.escape(data)
                if self.frame["kind"] in {"prompt", "raw"}:
                    text = text.replace("\n", "<br/>")
                self.frame["parts"].append(text)

    parser = Parser()
    parser.feed(source)
    parser.close()
    if not story:
        raise ValueError("PDF source has no renderable content")

    class Document(SimpleDocTemplate):
        def afterFlowable(self, flowable):
            if hasattr(flowable, "bookmark"):
                name, text = flowable.bookmark
                self.canv.bookmarkPage(name)
                self.canv.addOutlineEntry(text, name, level=0, closed=False)

    def page_footer(canvas, doc):
        canvas.saveState()
        canvas.setFont(font, 8)
        canvas.setFillColor(colors.HexColor("#53636a"))
        canvas.drawString(17 * mm, 12 * mm, footer)
        canvas.drawRightString(A4[0] - 17 * mm, 12 * mm, f"Page {doc.page}")
        canvas.restoreState()

    destination.parent.mkdir(parents=True, exist_ok=True)
    doc = Document(str(destination), pagesize=A4, rightMargin=19 * mm, leftMargin=19 * mm,
                   topMargin=18 * mm, bottomMargin=22 * mm, title=title,
                   author="Teacher AI Toolkit project")
    doc.build(story, onFirstPage=page_footer, onLaterPages=page_footer)
    if destination.stat().st_size > 25 * 1024 * 1024:
        raise ValueError("PDF exceeds 25 MB; split the edition without discarding output text")
