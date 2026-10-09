from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'runtime'))
import fitz
p=ROOT/'document_qa';doc=fitz.open(p/'Astra_final_report.pdf')
pages=[]
for i,page in enumerate(doc):
 page.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(p/f'page-{i+1}.png')
 pages.append(dict(page=i+1,characters=len(page.get_text()),width=page.rect.width,height=page.rect.height))
(p/'page_text.txt').write_text('\n'.join('PAGE '+str(i+1)+'\n'+d.get_text() for i,d in enumerate(doc)),encoding='utf-8')
(ROOT/'verification/document_render.json').write_text(json.dumps(dict(renderer='Microsoft Word native COM PDF export; PyMuPDF rasterization',packaged_renderer_error='Missing soffice.exe; Windows runtime did not bundle LibreOffice. No system LibreOffice used.',pages=pages,visual_review='PENDING'),ensure_ascii=False,indent=2),encoding='utf-8')
print(len(pages),'pages',pages)
