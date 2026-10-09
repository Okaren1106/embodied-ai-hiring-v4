"""Render hidden-Word PDF exports to page PNGs with bundled PDFium."""
from pathlib import Path
import json,hashlib
import pypdfium2 as pdfium
ROOT=Path(__file__).resolve().parents[1]
stats=json.loads((ROOT/'verification/word_statistics.json').read_text(encoding='utf-8-sig'))
allpages=[]
for name,metadata in stats.items():
    source=Path(metadata['pdf']);pdf=pdfium.PdfDocument(str(source))
    output=ROOT/'verification/rendered'/name;output.mkdir(parents=True,exist_ok=True)
    assert len(pdf)==metadata['pages']
    for i in range(len(pdf)):
        page=pdf[i];png=output/f'page-{i+1:02}.png'
        page.render(scale=1.7).to_pil().save(png)
        textpage=page.get_textpage();text=textpage.get_text_range()
        (output/f'page-{i+1:02}.txt').write_text(text,encoding='utf-8')
        allpages.append({'document':name,'page':i+1,'image':str(png.relative_to(ROOT)),
                         'text_characters':len(text),'pdf_sha256':hashlib.sha256(source.read_bytes()).hexdigest()})
        textpage.close();page.close()
    pdf.close()
(ROOT/'verification/rendered_pages.json').write_text(json.dumps(allpages,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'pages_rendered':len(allpages),'documents':len(stats)}))
