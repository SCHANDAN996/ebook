"""Render every PDF page and check content completeness and text bounds."""
from pathlib import Path
import json, re
import fitz
from PIL import Image, ImageOps, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'output/pdf/teacher-ai-toolkit-review.pdf'
QA=ROOT/'tmp/pdfs/review-qa'
QA.mkdir(parents=True,exist_ok=True)
doc=fitz.open(PDF)
alltext='\n'.join(p.get_text() for p in doc)
issues=[]
for prefix,n in [('LP',60),('WA',40),('AS',40),('DF',35),('PC',30),('RC',30),('CM',25),('AD',25),('SD',15),('WF',12)]:
    for i in range(1,n+1):
        if f'{prefix}-{i:03}' not in alltext:issues.append(f'Missing {prefix}-{i:03}')
for forbidden in ['Not included in this edition.','"review_status"','Full-book content draft.']:
    if forbidden in alltext:issues.append('Leaked production text: '+forbidden)
thumbs=[]
for i,p in enumerate(doc):
    pix=p.get_pixmap(matrix=fitz.Matrix(.45,.45),alpha=False)
    pix.save(QA/f'page-{i+1:03}.png')
    im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
    im=ImageOps.expand(im,border=(4,20,4,4),fill='white')
    ImageDraw.Draw(im).text((5,3),str(i+1),fill='black');thumbs.append(im)
    for block in p.get_text('dict')['blocks']:
        for line in block.get('lines',[]):
            for span in line['spans']:
                x0,y0,x1,y1=span['bbox']
                if x0<0 or y0<0 or x1>613 or y1>793:issues.append(f'Text outside page {i+1}')
for offset in range(0,len(thumbs),48):
    group=thumbs[offset:offset+48];w=max(x.width for x in group);h=max(x.height for x in group)
    sheet=Image.new('RGB',(w*8,h*6),'#cbd5db')
    for j,im in enumerate(group):sheet.paste(im,((j%8)*w,(j//8)*h))
    sheet.save(QA/f'contact-{offset//48+1:02}.jpg')
report={'pages':len(doc),'bookmarks':len(doc.get_toc()),'rendered_pages':len(thumbs),'issues':sorted(set(issues)),'human_review_complete':False,'note':'Automated checks do not establish educational correctness or classroom performance.'}
(ROOT/'output/pdf/qa-report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
