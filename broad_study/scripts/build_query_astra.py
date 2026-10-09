from common import *
import html
def stream(n):
 with (ROOT/'tables'/n).open(encoding='utf-8-sig',newline='') as f:yield from csv.DictReader(f)
cat=json.loads((ROOT/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'))['labels']
roles={a['role']:a for a in stream('Q1_prefixed_comparison_plan.csv')}
names={c:a['company_name'] for c,a in CO.items()}
qs=ROOT/'query';qs.mkdir(exist_ok=True)
points=defaultdict(list);aggs=defaultdict(list);evs=defaultdict(list)
for fname,task in [('Q4_company_points_final.csv',False),('Q4_task_company_points_final.csv',True)]:
 for a in stream(fname):
  if task and a['prefixed_focus']!='YES':continue
  points[a['role']].append([a.get('task','ALL'),a['label_code'],a['metric'],a['branch'],a['company_id']]+[int(a[k]) for k in ['P','U','Z','NA','SOURCE_EXCLUDED','N']])
for fname,task in [('Q4_aggregates_final.csv',False),('Q4_task_strata_final.csv',True)]:
 for a in stream(fname):
  if a['scope']!='WHOLE23' or (task and a['prefixed_focus']!='YES'):continue
  aggs[a['role']].append([a.get('task','ALL'),a['label_code'],a['metric'],a['branch'],a['P'],a['U'],a['N'],a['gate'],a['share_ad_weighted'],a['share_company_equal'],a['unknown_low_ad'],a['unknown_high_ad']])
ad={a['identity_key']:a for a in stream('Q3_ads_final.csv')}
for a in stream('Q3_evidence_final.csv'):
 if a.get('excluded_from_catalog')=='True':continue
 if ad[a['identity_key']]['company_id'] not in WHOLE:continue
 evs[a['role']].append([a['code'],a['metric'],a['branch'],a['reading_id'],a['quote'],a['field'],a['start'],a['reviewer'],ad[a['identity_key']]['qc_status'],ad[a['identity_key']]['task']])
css='body{font:16px/1.65 system-ui,Microsoft YaHei;margin:30px auto;max-width:1150px;padding:0 22px;color:#172c3d}h1{font-size:28px}select,input{font-size:15px;padding:8px;margin:5px;max-width:95%}table{width:100%;border-collapse:collapse;margin:18px 0}td,th{padding:8px;border:1px solid #ccd4db;text-align:left}th{background:#eef3f6}p.note{color:#6b4b1f}blockquote{border-left:3px solid #aac0cf;margin:12px 0;padding:6px 12px}small{color:#52616a}a{color:#165983}'
page='''<!doctype html><html lang="zh"><meta charset="utf-8"><title>__TITLE__</title><style>__CSS__</style>
<a href="../index.html">返回17职能目录</a><h1>__TITLE__</h1>
<p class="note">主范围为23家整公司。V3固定样本探索结果；规定的340条全文抽样与1208条强制队列已完成，累计469全文、760边界，347条继承首轮。不是全体二次全文或独立双编码。P为正例，U为未知，N=P+Z；NA和来源排除不计入分母。职责、必备、一般和优先不得合并解释。</p>
<label>任务 <select id="task"><option value="ALL">整个职能</option><option value="__TASK__">预设任务 __TASK__</option></select></label>
<label>条目 <select id="label"></select></label><label>语境 <select id="ctx"></select></label>
<div id="summary"></div><table><thead><tr><th>公司</th><th>P</th><th>U</th><th>Z</th><th>NA</th><th>来源排除</th><th>N</th><th>P/N</th><th>标记</th></tr></thead><tbody id="points"></tbody></table>
<h2>可定位证据</h2><p>下列证据按所选条目和语境展示。只有明确P参与该格正例；UNKNOWN和SEPARATE记录可从完整证据CSV检查。最多展开100条，完整结果见CSV。</p><div id="evidence"></div>
<p><a href="../tables/Q3_evidence_final.csv">完整证据CSV</a> · <a href="../tables/Q4_aggregates_final.csv">30范围全部汇总</a> · <a href="../tables/Q4_task_strata_final.csv">全部任务层</a> · <a href="../tables/Q3_review_receipts.csv">实际复核收据</a></p>
<script>const data=__DATA__;
const names=__NAMES__;
const esc=x=>String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const fmt=x=>x===''||x==null?'不汇总':(100*Number(x)).toFixed(2)+'%';
const lab=document.getElementById('label'),ctx=document.getElementById('ctx'),task=document.getElementById('task');
const m={GENERAL:'一般要求',REQUIRED:'明确必备',PREFERRED:'优先条件',DUTY_OWN_USE:'本人职责 使用',DUTY_OWN_DEVELOP:'本人职责 开发'};
const b={UNCONDITIONAL:'无条件',CHOICE:'任选',EXAMPLE:'示例',CHOICE_AND_EXAMPLE:'任选且示例',CONDITIONAL:'条件执行'};
lab.innerHTML=data.labels.map(a=>'<option value="'+esc(a[0])+'">'+esc(a[1])+' · '+esc(a[0])+'</option>').join('');
const contexts=[...new Set(data.aggregates.map(a=>a[2]+'|'+a[3]))];ctx.innerHTML=contexts.map(c=>{const [x,y]=c.split('|');return '<option value="'+c+'">'+m[x]+' / '+b[y]+'</option>'}).join('');ctx.value='GENERAL|UNCONDITIONAL';
function update(){const [metric,branch]=ctx.value.split('|'),code=lab.value,t=task.value;
 const a=data.aggregates.find(a=>a[0]===t&&a[1]===code&&a[2]===metric&&a[3]===branch);
 document.getElementById('summary').textContent=a?'当前组 P='+a[4]+' U='+a[5]+' N='+a[6]+'；'+(a[7]==='POINTS_ONLY'?'未通过组门槛，仅点值':'达到探索性组门槛')+'；广告加权 '+fmt(a[8])+'；公司等权 '+fmt(a[9])+'；未知赋值界限 '+fmt(a[10])+' 至 '+fmt(a[11]):'无此范围';
 const rows=data.points.filter(a=>a[0]===t&&a[1]===code&&a[2]===metric&&a[3]===branch);
 document.getElementById('points').innerHTML=rows.map(a=>'<tr><td>'+esc(names[a[4]]||a[4])+'</td>'+a.slice(5,11).map(v=>'<td>'+v+'</td>').join('')+'<td>'+fmt(a[10]?a[5]/a[10]:null)+'</td><td>'+(a[10]===0?'无可判断分母':a[10]<10?'小样本':'')+'</td></tr>').join('');
 const ee=data.evidence.filter(a=>a[0]===code&&a[1]===metric&&a[2]===branch&&(t==='ALL'||a[9]===t));
 document.getElementById('evidence').innerHTML=ee.slice(0,100).map(a=>'<blockquote>'+esc(a[4])+'<br><small>'+esc(a[3]+' · '+a[5]+' @'+a[6]+' · '+a[7]+' · '+a[8])+'</small></blockquote>').join('')||'<p>该格没有明确正例引文。请结合未知状态和其他语境解释。</p>';}
lab.onchange=ctx.onchange=task.onchange=update;update();</script></html>'''
index=['<!doctype html><html lang="zh"><meta charset="utf-8"><title>Astra 具身智能招聘研究</title><style>'+css+'</style><h1>Astra 具身智能公开招聘研究</h1><p>冻结24主体1,654条广告；Q2为17具体职能1,576条，整公司主范围1,552条。</p><p class="note">Astra V3研究和规定复核范围已完成：469条全文、760条边界，347条继承首轮；抽样340/340，强制1208/1208。统计保持探索性质。</p><p><a href="REPORT_Astra_final.md">最终综合报告Markdown</a> · <a href="document/具身智能公开招聘研究_最终综合报告_Astra.docx">Word报告</a></p><p><a href="two_layers.html">三任务技术提及与要求方式</a></p><h2>17职能全项查询</h2><ul>']
for r,plan in roles.items():
 d=dict(labels=[[a['code'],a['name']] for a in cat if r in a['applicable_roles']],points=points[r],aggregates=aggs[r],evidence=evs[r])
 h=page.replace('__TITLE__',html.escape(plan['role_name'])).replace('__CSS__',css).replace('__TASK__',html.escape(plan['focus_task'])).replace('__DATA__',json.dumps(d,ensure_ascii=False,separators=(',',':')).replace('</','<\/')).replace('__NAMES__',json.dumps(names,ensure_ascii=False))
 (qs/(r+'.html')).write_text(h,encoding='utf-8')
 index.append('<li><a href="query/'+r+'.html">'+html.escape(plan['role_name'])+'</a></li>')
index.append('</ul><h2>复算与质量</h2><p><a href="verification/astra_independent_numeric.json">独立数值核验</a> · <a href="verification/astra_isolated_reproduction.json">隔离复算</a> · <a href="tables/Q3_astra_changes.csv">725项修订记录</a> · <a href="tables/Q3_review_receipts.csv">实际复核覆盖</a></p></html>')
qc=json.loads((ROOT/'verification/astra_materialization.json').read_text(encoding='utf-8'))
idx='\n'.join(index).replace('162条',str(qc['reviewed_full'])+'条').replace('93/340',str(qc['seeded_full_reviewed'])+'/340').replace('142/1208',str(qc['mandatory_reviewed'])+'/1208').replace('725项',str(qc['changes'])+'项')
(ROOT/'index.html').write_text(idx,encoding='utf-8')
print('Query pages',len(roles),'main points',sum(len(v) for v in points.values()),'evidence',sum(len(v) for v in evs.values()))
