"""17-function query page and workbook."""
from common import *
import json as JSON
disp=read(ROOT/'tables/Q4_display_items.csv')
cov=read(ROOT/'tables/Q4_L0_coverage.csv')
roles=read(ROOT/'tables/Q1_role_coverage.csv')
html='''<!doctype html><meta charset="utf-8"><title>Q2 十七职能查询</title>
<style>body{font:14px/1.45 sans-serif;margin:24px;max-width:1100px}table{border-collapse:collapse;width:100%}td,th{border:1px solid #ccc;padding:4px 6px;font-size:12px}select,input{margin:4px}</style>
<h1>Q2 v2.1 十七职能查询</h1>
<p>整公司一般要求·无条件主图项。探索性汇总，非总体推断。数据：Q4_display_items.csv 与 Q4_L0_coverage.csv。</p>
<p>职能 <select id="role"><option value="">全部</option></select> 测量类型 <select id="mt"><option value="">全部</option></select></p>
<table id="t"><thead></thead><tbody></tbody></table>
<script>
const DISP='''+JSON.dumps(disp,ensure_ascii=False)+''';
const ROLES='''+JSON.dumps(roles,ensure_ascii=False)+''';
const roleSel=document.getElementById('role');
const mtSel=document.getElementById('mt');
[...new Set(ROLES.map(r=>r.role))].sort().forEach(v=>{const o=document.createElement('option');o.value=v;o.textContent=v;roleSel.appendChild(o)});
[...new Set(DISP.map(r=>r.measurement_type))].sort().forEach(v=>{const o=document.createElement('option');o.value=v;o.textContent=v;mtSel.appendChild(o)});
function pct(x){if(x===""||x==null)return "";const n=Number(x);return isNaN(n)?x:(100*n).toFixed(1)+"%"}
function draw(){
 const rr=roleSel.value, mt=mtSel.value;
 const rows=DISP.filter(r=>(!rr||r.role===rr)&&(!mt||r.measurement_type===mt));
 const cols=["role","label_name","measurement_type","P","N","U","share_ad_weighted","share_company_equal","dominance_warning"];
 document.querySelector("#t thead").innerHTML="<tr>"+cols.map(c=>"<th>"+c+"</th>").join("")+"</tr>";
 document.querySelector("#t tbody").innerHTML=rows.map(r=>"<tr>"+cols.map(c=>"<td>"+(c.includes("share")?pct(r[c]):(r[c]??""))+"</td>").join("")+"</tr>").join("");
}
roleSel.onchange=mtSel.onchange=draw;draw();
</script>'''
p=ROOT/'index.html'; p.write_text(html,encoding='utf-8')
# workbook: try openpyxl else csv bundle note
try:
    from openpyxl import Workbook
    wb=Workbook(); 
    def put(name,rows):
        ws=wb.create_sheet(name[:31])
        if not rows: return
        keys=list(rows[0]); ws.append(keys)
        for r in rows: ws.append([r.get(k,'') for k in keys])
    put('L0',cov); put('L3_status',roles); put('display',disp)
    if 'Sheet' in wb.sheetnames: del wb['Sheet']
    out=ROOT/'outputs'; out.mkdir(exist_ok=True)
    wb.save(out/'Q2_v2_17_functions.xlsx')
    print('xlsx', out/'Q2_v2_17_functions.xlsx')
except Exception as e:
    print('xlsx_skipped', e)
print('html', p)
