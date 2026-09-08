"""Build the editorial-review PDF and offline copy companion from current source.

Does not grant human approval or run paid model requests.
"""
from pathlib import Path
import re, json, html, hashlib
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak, NextPageTemplate, Flowable
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
try:
    from .editorial_engine import EXAMPLES
except ImportError:
    from editorial_engine import EXAMPLES

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pdf'
NAVY=HexColor('#092137'); TEAL=HexColor('#167D8D'); GOLD=HexColor('#DDAE58'); INK=HexColor('#203346')
FONTDIR=Path('/usr/share/fonts/truetype/dejavu')
for name,file in [('Body','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf'),('Serif','DejaVuSerif.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(FONTDIR/file)))

STYLES={
 'body':ParagraphStyle('body',fontName='Body',fontSize=9.3,leading=12.3,textColor=INK,spaceAfter=6),
 'small':ParagraphStyle('small',fontName='Body',fontSize=8.4,leading=11,textColor=INK,spaceAfter=4),
 'h1':ParagraphStyle('h1',fontName='Bold',fontSize=22,leading=27,textColor=NAVY,spaceAfter=18,keepWithNext=True),
 'h2':ParagraphStyle('h2',fontName='Bold',fontSize=10.4,leading=13,textColor=TEAL,spaceBefore=8,spaceAfter=5,keepWithNext=True),
 'title':ParagraphStyle('title',fontName='Bold',fontSize=16,leading=20,textColor=NAVY,spaceAfter=10,keepWithNext=True),
 'code':ParagraphStyle('code',fontName='Body',fontSize=8.8,leading=11.5,textColor=INK,spaceAfter=4),
}

def plain(s):
    return s.replace('—',' - ').replace('–','-').replace('‑','-').replace('→',' -> ').replace('−','-').replace('↑','increase').replace('↓','decrease')

def markup(s):
    s=escape(plain(s))
    s=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'`(.*?)`',r'\1',s)
    return s

def P(s,style='body'):
    return Paragraph(markup(s),STYLES[style])

def page(c,d):
    c.saveState(); c.setFillColor(TEAL);c.rect(0,775,612,17,fill=1,stroke=0)
    c.setFont('Body',7.5);c.setFillColor(NAVY)
    c.drawString(42,759,'TEACHER AI TOOLKIT  /  CHANDAN SINGH')
    c.setStrokeColor(HexColor('#CCDADC'));c.line(42,38,570,38)
    c.drawString(42,24,'Editorial review edition  |  Verify before classroom use')
    c.drawRightString(570,24,str(d.page));c.restoreState()

def cover(c,d):
    c.drawImage(str(ROOT/'book/assets/generated/cover-art.png'),0,0,width=612,height=792,mask='auto')
    c.setFillColor(GOLD);c.setFont('Bold',11);c.drawString(49,723,'THE PRACTICAL REFERENCE EDITION')
    c.setFillColor(white);c.setFont('Bold',47)
    c.drawString(45,658,'TEACHER')
    c.drawString(45,601,'AI TOOLKIT')
    c.setFont('Body',14);c.drawString(49,566,'300 focused prompts. 12 guided workflows.')
    c.setFont('Body',11);c.drawString(49,541,'Plan lessons. Create materials. Communicate clearly.')
    c.setFont('Bold',12);c.drawString(49,67,'CHANDAN SINGH')
    c.setFont('Body',9);c.drawString(49,48,'AI-assisted editorial development  |  Review edition')

class BookDoc(BaseDocTemplate):
    def afterFlowable(self,f):
        if hasattr(f,'bookmark'):
            self.canv.bookmarkPage(f.bookmark)
            self.canv.addOutlineEntry(f.getPlainText(),f.bookmark,f.level,False)
            if f.level==0:
                self.notify('TOCEntry',(0,f.getPlainText(),self.page,f.bookmark))

class ChapterPanel(Flowable):
    def __init__(self,number):
        Flowable.__init__(self);self.number=number;self.width=528;self.height=180
    def draw(self):
        c=self.canv;c.setFillColor(NAVY);c.roundRect(0,0,528,170,14,fill=1,stroke=0)
        c.setFillColor(GOLD);c.setFont('Bold',48);c.drawString(25,97,f'{self.number:02}')
        c.setFillColor(white);c.setFont('Bold',17);c.drawString(115,119,'Plan with purpose.')
        c.drawString(115,91,'Draft with context.')
        c.drawString(115,63,'Verify with judgment.')
        c.setFillColor(TEAL);c.rect(25,28,476,4,fill=1,stroke=0)

def markdown_blocks(text,skip=()):
    text=re.sub(r'^---\n\{.*?\}\n---\n','',text,flags=re.S)
    if skip:
        for section in skip:
            text=re.sub(r'\n## '+re.escape(section)+r'\n.*?(?=\n## |\Z)','',text,flags=re.S)
    blocks=[]; code=False
    for chunk in re.split(r'\n\s*\n',text.strip()):
        if chunk.startswith('# '): continue
        if chunk.startswith('## '): blocks.append(P(chunk[3:],'h2'));continue
        chunk=chunk.replace('```text\n','').replace('```','').strip()
        if not chunk:continue
        if chunk.startswith('- ') or '\n- ' in chunk:
            for line in chunk.splitlines():
                if line.strip():blocks.append(P(line.replace('- [ ]','Check:').lstrip('- '),'small'))
        else:
            blocks.append(P(chunk.replace('\n',' '),'body'))
    return blocks

def build():
    OUT.mkdir(parents=True,exist_ok=True)
    target=OUT/'teacher-ai-toolkit-review.pdf'
    doc=BookDoc(str(target),pagesize=(612,792),leftMargin=42,rightMargin=42,topMargin=50,bottomMargin=49,title='Teacher AI Toolkit - Editorial Review Edition',author='Chandan Singh',pageCompression=1)
    frame=Frame(42,49,528,692,id='normal',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
    doc.addPageTemplates([PageTemplate('cover',[frame],onPage=cover),PageTemplate('body',[frame],onPage=page)])
    story=[Spacer(1,10),NextPageTemplate('body'),PageBreak()]
    toc=TableOfContents();toc.levelStyles=[ParagraphStyle('toc',fontName='Body',fontSize=10,leading=15,leftIndent=0,spaceBefore=9,textColor=INK)]
    story += [P('Contents','h1'),P('Use the PDF bookmarks to jump to any prompt or workflow. The offline HTML companion provides title search and one-click prompt copying.'),toc,PageBreak()]
    for name in ['editorial-guide','privacy-and-safety','extension-guide']:
        txt=(ROOT/f'book/front-matter/{name}.md').read_text()
        heading=P(txt.splitlines()[0][2:],'h1');heading.bookmark=name;heading.level=0
        story.append(heading);story+=markdown_blocks(txt);story.append(PageBreak())
    manifest=json.loads((ROOT/'book/manifest.json').read_text())
    articles=[]; fingerprint=hashlib.sha256()
    for ch in manifest['chapters']:
        folder=ROOT/'book/chapters'/f"{ch['order']:02d}-{ch['id']}"
        intro=(folder/'chapter.md').read_text();heading=P(intro.splitlines()[0][2:],'h1');heading.bookmark=ch['id'];heading.level=0
        story.append(heading);story+=markdown_blocks(intro)
        story.append(P('Choose a tool by its task, not its position. Related tools cover different stages; use the smallest one that solves your immediate need.','body'))
        story.append(Spacer(1,22));story.append(ChapterPanel(ch['order']))
        story.append(PageBreak())
        sources=sorted((folder/('prompts' if ch['kind']=='prompt' else 'workflows')).glob('*.md'))
        for src in sources:
            txt=src.read_text();fingerprint.update(txt.encode());meta=json.loads(txt.split('---',2)[1]);pid=meta['id']
            heading=P(f"{pid}  /  {meta['title']}",'title');heading.bookmark=pid;heading.level=1
            story.append(heading)
            # Inputs already appear inside the copyable block. Development notes stay in source.
            story += markdown_blocks(txt,('Teacher inputs','Editorial notes','Fictional test case','Sample output','Teacher verification checklist','Workflow','Review checklist'))
            story.append(P('CHECK BEFORE USE: Verify the task-specific requirements, factual provenance, answers, access and local authorization.','small'))
            if pid in EXAMPLES:
                story.append(P('Worked illustration: see the example gallery entry '+pid+'.','small'))
            story.append(PageBreak())
            prompt=re.search(r'```text\n(.*?)```',txt,re.S).group(1).strip()
            articles.append(dict(id=pid,title=meta['title'],chapter=ch['id'],prompt=prompt,source=txt))
    gallery=P('Example gallery / 60 selected excerpts','h1');gallery.bookmark='example-gallery';gallery.level=0
    story.append(gallery)
    story.append(P('All cases are fictional editorial illustrations. These excerpts show the key reasoning or artifact; they are not complete logged outputs or classroom results. Other source prompts include missing-input exercises.'))
    for a in articles:
        if a['id'] not in EXAMPLES:continue
        ex=EXAMPLES[a['id']]
        story.append(P(a['id']+' / '+a['title'],'h2'))
        story.append(P('Fictional inputs: '+ex['Fictional inputs for the illustrated excerpt']))
        story.append(P(ex['Illustrative output excerpt']))
        story.append(Spacer(1,12))
    if isinstance(story[-1],PageBreak):story.pop()
    doc.multiBuild(story)
    build_html(articles)
    (OUT/'edition-manifest.json').write_text(json.dumps({'edition':'editorial-review-v2','prompts':300,'workflows':12,'distinct_example_excerpts':60,'human_approval':False,'model_execution_testing':False,'source_sha256':fingerprint.hexdigest(),'pdf':target.name},indent=2)+'\n')
    print(target)

def build_html(articles):
    cards=[]
    for a in articles:
        escaped=html.escape(a['prompt'])
        cards.append(f'<article id="{a["id"]}" data-search="{html.escape((a["id"]+" "+a["title"]+" "+a["chapter"]).lower())}"><h2>{a["id"]} · {html.escape(a["title"])}</h2><button type="button">Copy prompt</button><span role="status" aria-live="polite"></span><details><summary>Show prompt</summary><pre>{escaped}</pre></details></article>')
    text='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Teacher AI Toolkit - Copy Companion</title><style>body{font:17px/1.6 system-ui;margin:0;background:#f3f6f6;color:#203346}header,main{max-width:920px;margin:auto;padding:28px}header{background:#092137;color:white}h1{line-height:1.15}input{padding:14px;width:90%;font:inherit}article{background:white;padding:22px;margin:18px 0;border-left:5px solid #167d8d;border-radius:8px}h2{font-size:20px}button{background:#167d8d;color:white;border:0;padding:12px 18px;border-radius:6px;font:inherit;cursor:pointer}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:15px/1.6 system-ui}summary{cursor:pointer;padding:12px 0}span{margin-left:12px}a{color:inherit}</style><header><p>CHANDAN SINGH / PRACTICAL REFERENCE</p><h1>Teacher AI Toolkit</h1><p>300 prompts + 12 workflows. Offline, searchable and copyable.</p><p>Editorial review edition. No classroom-testing or human-approval claim. Do not enter student records here; this page sends nothing to a server.</p><label for="q">Find a task or ID</label><br><input id="q" type="search" placeholder="Try fractions, report, WF-004..."></header><main>'''+''.join(cards)+'''</main><script>document.querySelector('#q').addEventListener('input',e=>{let q=e.target.value.toLowerCase();document.querySelectorAll('article').forEach(a=>a.hidden=!a.dataset.search.includes(q))});document.querySelectorAll('button').forEach(b=>b.addEventListener('click',async()=>{let a=b.closest('article'),t=a.querySelector('pre').textContent,s=a.querySelector('[role=status]');try{await navigator.clipboard.writeText(t);s.textContent='Copied';}catch(e){a.querySelector('details').open=true;let r=document.createRange();r.selectNodeContents(a.querySelector('pre'));let selection=window.getSelection();selection.removeAllRanges();selection.addRange(r);s.textContent='Text selected. Use Copy from your device menu.';}}));</script></html>'''
    (OUT/'teacher-ai-toolkit-companion.html').write_text(text,encoding='utf-8')

if __name__=='__main__': build()
