from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'runtime'))
import fitz
from PIL import Image,ImageDraw
pdf=fitz.open(ROOT/'document_qa/Astra_final_report.pdf')
rows=[]
for i,page in enumerate(pdf):
 pix=page.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False);pix.save(ROOT/f'document_qa/page-{i+1}.png')
 blocks=page.get_text('blocks');rows.append(dict(page=i+1,words=len(page.get_text().split()),text_chars=len(page.get_text()),bbox=[min((b[0] for b in blocks),default=0),min((b[1] for b in blocks),default=0),max((b[2] for b in blocks),default=0),max((b[3] for b in blocks),default=0)],start=page.get_text()[:130],end=page.get_text()[-150:]))
for start in range(0,len(pdf),6):
 sheet=Image.new('RGB',(918,1188),'#d9d9d9')
 for j,i in enumerate(range(start,min(start+6,len(pdf)))):
  im=Image.open(ROOT/f'document_qa/page-{i+1}.png');im.thumbnail((450,365))
  x=(j%2)*459+(459-im.width)//2;y=(j//2)*396
  sheet.paste(im,(x,y+24));ImageDraw.Draw(sheet).text((j%2*459+8,y+5),f'Page {i+1}',fill='black')
 sheet.save(ROOT/f'document_qa/contact-{start+1}.png')
(ROOT/'document_qa/page_text.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print('Rendered',len(pdf),'pages');print(json.dumps(rows,ensure_ascii=False))
