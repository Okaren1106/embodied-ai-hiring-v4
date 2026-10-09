"""Q2 figures without third-party plotting libraries. Writes SVG and 24-bit BMP."""
from common import *
from pathlib import Path
figdir=ROOT/'figures'; figdir.mkdir(exist_ok=True)

def svg_escape(s):
    return (s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;'))

def write_bmp(path, w, h, pixels):
    # pixels: list of (r,g,b) row-major, top-left first. BMP stores bottom-up BGR, pad to 4.
    rowb=((w*3+3)//4)*4
    img=rowb*h; off=54
    def u32(n): return n.to_bytes(4,'little')
    def u16(n): return n.to_bytes(2,'little')
    hdr=b'BM'+u32(off+img)+u32(0)+u32(off)+u32(40)+u32(w)+u32(h)+u16(1)+u16(24)+u32(0)+u32(img)+u32(0)*4
    buf=bytearray(hdr)
    for y in range(h-1,-1,-1):
        row=bytearray()
        for x in range(w):
            r,g,b=pixels[y*w+x]
            row += bytes((b,g,r))
        row += b'\x00'*(rowb-w*3)
        buf += row
    path.write_bytes(buf)

def lerp(a,b,t):
    return tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))

cov=sorted(read(ROOT/'tables/Q4_L0_coverage.csv'), key=lambda r: -int(r['whole23_ads']))
# SVG coverage
W,H=900,620; left=260; top=40; bh=28; gap=6
maxv=max(int(r['whole23_ads']) for r in cov) or 1
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" font-family="Microsoft YaHei, SimHei, sans-serif">'%(W,H)]
parts.append('<text x="20" y="24" font-size="16">Q2 v2.1 L0 覆盖：整公司广告数（非比较资格）</text>')
for i,r in enumerate(cov):
    y=top+i*(bh+gap); w=int((W-left-40)*int(r['whole23_ads'])/maxv)
    parts.append('<rect x="%d" y="%d" width="%d" height="%d" fill="#2F5D8A"/>'%(left,y,w,bh))
    parts.append('<text x="%d" y="%d" font-size="12" text-anchor="end">%s</text>'%(left-8,y+19,svg_escape(r['role_name'])))
    parts.append('<text x="%d" y="%d" font-size="11" fill="#333">%s</text>'%(left+w+6,y+19,r['whole23_ads']))
parts.append('</svg>')
(figdir/'Q2_L0_coverage.svg').write_text('\n'.join(parts),encoding='utf-8')
# BMP coverage
pw,ph=1100,760
pix=[(255,255,255)]*(pw*ph)
def rect(x,y,w,h,c):
    for yy in range(max(0,y),min(ph,y+h)):
        for xx in range(max(0,x),min(pw,x+w)):
            pix[yy*pw+xx]=c
def blit_text_skip():
    pass
# bars only; labels live in SVG/caption
leftb=40; topb=40
for i,r in enumerate(cov):
    y=topb+i*40; w=int((pw-leftb-80)*int(r['whole23_ads'])/maxv)
    rect(leftb,y,w,24,(47,93,138))
write_bmp(figdir/'Q2_L0_coverage.bmp', pw, ph, pix)

disp=read(ROOT/'tables/Q4_display_items.csv')
keys=[('RF_ML_AI_ENGINEERING','SK_PYTHON'),('RF_ROBOTICS_SOFTWARE','SK_LINUX'),('RF_CONTROL_PLANNING','TC_CONTROL'),('RF_HARDWARE_ELECTRICAL','SK_PCB'),('RF_MECHANICAL_MECHATRONICS','TC_MECHANICAL'),('RF_COMMERCIAL_CUSTOMER','V2_SALES_CRM')]
rows=[]
for role,code in keys:
    hit=[r for r in disp if r['role']==role and r['label_code']==code]
    if hit: rows.append(hit[0])
W,H=860,420
s=['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" font-family="Microsoft YaHei, SimHei, sans-serif">'%(W,H)]
s.append('<text x="20" y="24" font-size="16">主图项公司等权与广告加权（门槛内，非总体推断）</text>')
s.append('<text x="520" y="24" font-size="12">圆=公司等权  方=广告加权</text>')
for i,r in enumerate(rows):
    y=60+i*55
    eq=float(r['share_company_equal'])*100; aw=float(r['share_ad_weighted'])*100
    x0=280
    def xof(p): return x0+int(p*5.2)
    xa,xb=xof(min(eq,aw)),xof(max(eq,aw))
    s.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#B8C5CF" stroke-width="3"/>'%(xa,y,xb,y))
    s.append('<circle cx="%d" cy="%d" r="6" fill="#1d4f7a"/>'%(xof(eq),y))
    s.append('<rect x="%d" y="%d" width="10" height="10" fill="#c45c26"/>'%(xof(aw)-5,y-5))
    lab=r['role'].replace('RF_','')+' / '+r['label_name']
    s.append('<text x="20" y="%d" font-size="11">%s</text>'%(y+4,svg_escape(lab)))
    s.append('<text x="%d" y="%d" font-size="11">%.1f / %.1f</text>'%(xof(max(eq,aw))+12,y+4,eq,aw))
s.append('</svg>')
(figdir/'Q2_display_equal_vs_weighted.svg').write_text('\n'.join(s),encoding='utf-8')
pw,ph=1000,480
pix=[(255,255,255)]*(pw*ph)
for i,r in enumerate(rows):
    y=40+i*70
    eq=float(r['share_company_equal'])*100; aw=float(r['share_ad_weighted'])*100
    def xof(p): return 80+int(p*8)
    xa,xb=xof(min(eq,aw)),xof(max(eq,aw))
    rect(xa,y+10,max(1,xb-xa),4,(184,197,207))
    rect(xof(eq)-5,y+4,10,16,(29,79,122))
    rect(xof(aw)-5,y+8,10,10,(196,92,38))
write_bmp(figdir/'Q2_display_equal_vs_weighted.bmp', pw, ph, pix)
print('figures svg+bmp', 4)
