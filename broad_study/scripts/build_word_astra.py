from pathlib import Path
import re
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
ROOT=Path(__file__).resolve().parents[1]
doc=Document();sec=doc.sections[0]
sec.page_width=Inches(8.5);sec.page_height=Inches(11)
sec.top_margin=sec.bottom_margin=Inches(.75);sec.left_margin=sec.right_margin=Inches(.75)
for name in ['Normal','Title','Heading 1','Heading 2','Heading 3','Caption']:
 st=doc.styles[name];st.font.name='Microsoft YaHei';st._element.rPr.rFonts.set(qn('w:eastAsia'),'微软雅黑');st.font.color.rgb=RGBColor.from_string('000000')
st=doc.styles['Normal'];st.font.size=Pt(11);st.paragraph_format.line_spacing=1.2;st.paragraph_format.space_after=Pt(7)
doc.styles['Title'].font.size=Pt(24);doc.styles['Title'].font.bold=True
for style in doc.styles:
 for border in style._element.xpath('.//w:pBdr'):
  border.getparent().remove(border)
for name,size in [('Heading 1',16),('Heading 2',12.5),('Heading 3',11.5)]:
 st=doc.styles[name];st.font.size=Pt(size);st.font.bold=True;st.paragraph_format.space_before=Pt(15);st.paragraph_format.space_after=Pt(8)
doc.styles['Caption'].font.size=Pt(9.5)
doc.styles['Caption'].font.bold=False
doc.styles['Caption'].font.italic=False
def plain(s):
 s=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',s);return s.replace('**','').replace('`','')
def paragraph(s,style=None):
 p=doc.add_paragraph(style=style)
 for i,t in enumerate(re.split(r'(\*\*.*?\*\*)',s)):
  run=p.add_run(plain(t));run.bold=True if t.startswith('**') else None
 return p
def table(lines):
 rows=[[plain(x.strip()) for x in line.strip().strip('|').split('|')] for line in lines]
 rows=[r for r in rows if not all(re.fullmatch(r'[: -]+',c) for c in r)]
 n=len(rows[0]);t=doc.add_table(rows=0,cols=n);t.autofit=False
 widths={2:[1.65,5.35],3:[2.2,1.25,3.55],4:[2.3,1.5,1.5,1.7],5:[2.0,1.25,1.25,1.25,1.25],6:[2.15,1.25,.9,.9,.9,.9]}.get(n,[7/n]*n)
 if rows[0][0]=='公司':widths=[1.15,1.5,1.35,1.5,1.5]
 if rows[0][0]=='具体职能':widths=[2.1,1.45,1.0,.65,.8,1.0] if '一般无条件条目' in rows[0] else [2.45,.91,.91,.91,.91,.91]
 if rows[0][0]=='同口径指标':widths=[2.4,1.15,1.15,1.15,1.15]
 if rows[0][0]=='任务与条目' and n==5:widths=[2.05,1.35,1.25,1.1,1.25] if rows[0][1]=='公司' else [2.0,1.25,1.25,1.25,1.25]
 if rows[0][0]=='一般要求 无条件':widths=[2.0,1.25,1.25,1.25,1.25]
 if rows[0][0] in ['发现的问题','工作']:widths=[2.2,1.9,2.9]
 for c,w in zip(t.columns,widths):c.width=Inches(w)
 for ri,row in enumerate(rows):
  cells=t.add_row().cells
  for ci,(c,text) in enumerate(zip(cells,row)):
   c.width=Inches(widths[ci]);c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
   p=c.paragraphs[0];p.paragraph_format.space_before=Pt(4);p.paragraph_format.space_after=Pt(4);p.paragraph_format.line_spacing=1.1
   p.paragraph_format.keep_with_next=(ri==0)
   p.alignment=WD_ALIGN_PARAGRAPH.CENTER if len(text)<12 and ci>0 else WD_ALIGN_PARAGRAPH.LEFT
   # Break long filenames at underscores for an uninterrupted source identifier in plain text.
   run=p.add_run(text);run.font.size=Pt(10)
   if ri==0:run.bold=True;run.font.color.rgb=RGBColor(255,255,255)
   pr=c._tc.get_or_add_tcPr();sh=OxmlElement('w:shd');sh.set(qn('w:fill'),'234E70' if ri==0 else ('F2F5F7' if ri%2==0 else 'FFFFFF'));pr.append(sh)
   bord=OxmlElement('w:tcBorders')
   for side in ['top','left','bottom','right']:
    x=OxmlElement('w:'+side);x.set(qn('w:val'),'single');x.set(qn('w:sz'),'4');x.set(qn('w:color'),'D9D9D9');bord.append(x)
   pr.append(bord);m=OxmlElement('w:tcMar')
   for side in ['top','bottom','left','right']:
    x=OxmlElement('w:'+side);x.set(qn('w:w'),'90');x.set(qn('w:type'),'dxa');m.append(x)
   pr.append(m)
  rp=t.rows[-1]._tr.get_or_add_trPr();x=OxmlElement('w:cantSplit');rp.append(x)
  if ri==0:x=OxmlElement('w:tblHeader');rp.append(x)
 doc.add_paragraph().paragraph_format.space_after=Pt(2)
lines=(ROOT/'REPORT_Astra_final.md').read_text(encoding='utf-8').splitlines()
i=0
while i<len(lines):
 s=lines[i].strip()
 if not s:i+=1;continue
 if s.startswith('|'):
  block=[]
  while i<len(lines) and lines[i].strip().startswith('|'):block.append(lines[i]);i+=1
  table(block);continue
 if s.startswith('!['):
  m=re.match(r'!\[(.*?)\]\((.*?)\)',s);p=doc.add_paragraph();p.paragraph_format.keep_with_next=True
  run=p.add_run();run.add_picture(str(ROOT/m[2].strip('<>')),width=Inches(6.65))
  inline=run._r.xpath('.//wp:docPr')[0];inline.set('descr',m[1]);inline.set('title',m[1])
 elif s.startswith('# '):paragraph(s[2:],'Title')
 elif s.startswith('## '):paragraph(s[3:],'Heading 1')
 elif s.startswith('### '):paragraph(s[4:],'Heading 2')
 else:paragraph(s,'Caption' if s.startswith(('图1　','图2　','图3　','图4　','数据表：','数据与证据：')) else None)
 i+=1
footer=sec.footer.paragraphs[0];footer.alignment=WD_ALIGN_PARAGRAPH.RIGHT
footer.add_run('Astra  |  ').font.size=Pt(9)
fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');footer._p.append(fld)
doc.core_properties.author='Astra';doc.core_properties.title='具身智能公开招聘研究最终综合报告';doc.core_properties.subject='冻结24主体公开招聘分析及17职能Q2拓展';doc.core_properties.comments='本轮研究交付，内容验收状态以正文和复核收据为准。'
dest=ROOT/'document';dest.mkdir(exist_ok=True)
path=dest/'具身智能公开招聘研究_最终综合报告_Astra.docx';doc.save(path)
print(path)
