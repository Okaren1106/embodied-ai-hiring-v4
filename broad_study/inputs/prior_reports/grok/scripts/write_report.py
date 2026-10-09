"""Stage D report, methods, dictionary and HTML. Marked grok4.6 research."""
from analyze import ROOT,T,IN,read,js,dump
from html import escape
from pathlib import Path
S=js(ROOT/'summary.json');F=js(ROOT/'figure_manifest.json')
t1=read(IN/'stage_c'/'tables'/'T1_company_sample.csv');cb={r['company_id']:r for r in t1}
head=read(T/'D2_headline_cross_split.csv')
co=read(T/'D4_activity_cooccurrence_summary.csv')
ml=read(T/'D4_ml_technical_cooccurrence.csv')
uw=read(T/'D3_unified_weight_cases.csv')
dep=read(T/'D3_deployment_composition.csv')
t6=read(T/'T6_conclusions.csv')
reg=read(T/'D5_case_register.csv')
ctrl=read(T/'D9_q2_unknown_bound_control.csv')
q1=read(T/'D1_q1_coverage.csv')
source=js(IN/'decisions'/'source_complete_subset.json')
researcher=js(IN/'decisions'/'researcher.json')
g1=S['g1'];g2=S['g2']
def pct(x):
 if x in ('',None):return 'NA'
 return f'{float(x)*100:.1f}%'
def md(headers,rows):
 return '| '+' | '.join(headers)+' |\n|'+'|'.join(['---']*len(headers))+'|\n'+'\n'.join('| '+' | '.join(str(c).replace('|','／').replace('\n',' ')[:180] for c in row)+' |' for row in rows)
def q1row(scope,code):
 return next(r for r in q1 if r['scope']==scope and r['class_code']==code)
def deprow(c):
 return next(r for r in dep if r['company_id']==c)
hres=next(r for r in head if r['activity_code']=='ACT_RESEARCH')
hdep=next(r for r in head if r['activity_code']=='ACT_DEPLOYMENT')
hqual=next(r for r in head if r['activity_code']=='ACT_QUALITY')
co24=[r for r in co if r['scope']=='ALL24']
sel=[r for r in reg if r['status']=='SELECTED']
# compact T5 case profile: prefer customer-confirmed deployment, not retail/self-arrival
t5long=read(T/'T5_delivery_responsibility.csv')
d9=read(T/'D9_sensitivity.csv')
def d9v(cid,scope):
 return next(r for r in d9 if r['check_id']==cid and r['scope']==scope)
eq_fn=float(d9v('DEPLOYMENT_FUNCTION_SHARE_EQUAL','WHOLE23')['share_outside'])
eq_act=float(d9v('DEPLOYMENT_ACTIVITY_OVERALL_EQUAL','WHOLE23')['share_outside'])
eq_out=float(d9v('DEPLOYMENT_ACTIVITY_OUTSIDE_FUNCTION_EQUAL','WHOLE23')['share_outside'])
def pick_fact(c,group):
 rows=[x for x in t5long if x['company_id']==c and x['main_comparison']=='YES']
 def score(x):
  s=0;kind=x.get('assertion_kind') or '';stg=x.get('business_stage') or '';val=x.get('fact_value') or '';sub=x.get('responsibility_subject') or ''
  if kind in ['CUSTOMER_CONFIRMED_USE','COUNTERPARTY_CONFIRMATION']:s+=100
  if stg=='CUSTOMER_SITE_DEPLOYMENT':s+=50
  elif stg=='ONGOING_OPERATIONS':s+=40
  if any(k in val for k in ['宁德','BMW','GXO','SPANX','履单','3PL']):s+=30
  if group=='CASE_G2_LOGISTICS_DELIVERY' and sub=='COMPANY' and any(k in val for k in ['履单','3PL']):s+=25
  if kind=='ARRIVAL_SELF_REPORT':s-=80
  if group=='CASE_G1_MANUFACTURING_OBSERVED' and '香港' in val:s-=40
  return -s
 rows=sorted(rows,key=score)
 return rows[0] if rows else {}
prof=[]
for r in sel:
 c=r['company_id'];d=deprow(c);t=cb[c];fact=pick_fact(c,r['selected_group'])
 prof.append(dict(company_id=c,company_name=t['company_name'],case_id=r['selected_group'],stratum=t['stratum_name'],n_ads=t['n_ads'],observation_date=t['observation_dates'],scene=t['current_scenes_json'],deployment_function_share=d['share_deployment_function'],deployment_activity_share=d['share_deployment_activity'],activity_outside_function=d['share_deployment_activity_outside_deployment_function'],key_fact=fact.get('fact_value',''),key_stage=fact.get('business_stage',''),key_subject=fact.get('responsibility_subject',''),time_applicability=fact.get('time_applicability',''),evidence_ids=fact.get('evidence_ids',''),assertion_kind=fact.get('assertion_kind',''),eligibility=r['exclusion_or_inclusion']))
from analyze import table as wtable
wtable('T5_case_profile.csv',prof)

uwg1=[r for r in uw if r['group_id']=='CASE_G1_MANUFACTURING_OBSERVED' and r['activity_code'] in ['ACT_ENGINEERING','ACT_QUALITY','ACT_DEPLOYMENT','ACT_RESEARCH']]
q2case=read(T/'D7_case_q2_points.csv')
def q2p(c,role,label,metric='DUTY_OWN_DEVELOP'):
 rows=[r for r in q2case if r['company_id']==c and r['role_code']==role and r['label_name']==label and r['metric_bucket']==metric and r['branch_bucket']=='UNCONDITIONAL']
 return rows[0] if rows else {}
q2_g_fm=q2p('CN_GALBOT','RF_ML_AI_ENGINEERING','基础模型/VLA')
q2_g_sys=q2p('CN_GALBOT','RF_ML_AI_ENGINEERING','训练推理系统')
q2_f_fm=q2p('US_FIGURE','RF_ML_AI_ENGINEERING','基础模型/VLA')
q2_f_sys=q2p('US_FIGURE','RF_ML_AI_ENGINEERING','训练推理系统')
q2_g_rel=q2p('CN_GALBOT','RF_ROBOTICS_SOFTWARE','可靠性')
q2_f_rel=q2p('US_FIGURE','RF_ROBOTICS_SOFTWARE','可靠性')
def q2frac(r):
 return f"{r.get('n_positive','?')}/{r.get('n_interpretable') or r.get('n_base','?')}"

report=f'''# 具身智能公开招聘研究阶段D结果报告

**研究标记：grok4.6研究**  
研究者 / 模型：{researcher['model']}  
日期：2026-09-16  
执行依据：[阶段D研究执行书 v1](inputs/protocol/研究执行书.md)  
本方案形成于阶段C描述结果之后，不称为事前预注册。

入口：[图表页](index.html) · [计数与分母](METHODS.md) · [表格目录](DATA_DICTIONARY.md) · [复算说明](README.md)

## 1. 研究问题与完成情况

核心问题：公司间的工作组合差异，有多少表现为招聘的职能构成不同，又有多少表现为同类职能承担的任务不同？

| 问题 | 本阶段做了什么 |
|---|---|
| Q1 业务边界与职能组合 | 补公司覆盖与集中度；把部署活动拆成职能构成与非部署职能内的任务安排；按产品场景与证据选两组四家公司 |
| Q2 同类职能的技术任务 | 维持 ML/AI 工程与软件与平台两个代表；报告整公司点值、ML三项共现、案例公司语境点值 |
| Q3 活动跨职能与共同承担 | 双向交叉并拆出结构/未明确；三组活动共现做关系判定；参与协作另表不并入本人承担 |

没有扩样、没有重分类、没有把融资当主解释。无稳定差异或门槛失败已写入 T6，不凑样本。

## 2. 样本与已锁定输入

- 认可集合 REFERENCE1654：24主体 1,654条。整公司23家 1,630条；Amazon FAR 24条单列。
- 两批观察：2026-08-31 的610条，2026-09-11 的1,044条，不是同日普查。
- 活动可判读 1,623条。Q2整公司 ML 156、软件 180。
- 来源较完整子集在读取阶段D派生结果前锁定，11家：{', '.join(source['included_company_ids'])}。纳入只看整公司、官方渠道、T1质量 EXCELLENT/GOOD、主职能与活动来源不足为0。不用活动率或正文长度。
- 原封存 A/B/C 与研究库未改。REPRO-01 另版修复见 `stage_c_repro_complete/`。

## 3. Q3：活动跨职能分布

三项对照与阶段C一致，并补结构类、未明确状态：

| 本人承担活动 | 正向广告 | 同名主职能 | 其他具体职能 | 结构类 | 未明确 | 同名之外 |
|---|---:|---:|---:|---:|---:|---:|
| 研究探索 | {hres['n_owned']} | {hres['n_namesake']} | {hres['n_other_concrete']} | {hres['n_structure']} | {hres['n_unspecified']} | {pct(hres['share_outside_namesake'])} |
| 部署与维护 | {hdep['n_owned']} | {hdep['n_namesake']} | {hdep['n_other_concrete']} | {hdep['n_structure']} | {hdep['n_unspecified']} | {pct(hdep['share_outside_namesake'])} |
| 质量验证 | {hqual['n_owned']} | {hqual['n_namesake']} | {hqual['n_other_concrete']} | {hqual['n_structure']} | {hqual['n_unspecified']} | {pct(hqual['share_outside_namesake'])} |

部署271条“非同名”现拆为其他具体255 + 结构13 + 未明确3；质量306条拆为293 + 9 + 4。不能把结构广告或歧义全部称为已确定的其他具体职能。

![跨职能活动分布]({F[0]['png']})

整公司与来源较完整子集、逐一剔除公司后，三项“同名之外”比例方向一致，见 T6_Q3_CROSS_FUNCTION。这不是原分类错误，也不等于实际跨部门协同。

## 4. 活动共现

主指标只计明确无条件共同承担。三组双正向广告均无任选根结构；复合树按同时承担处理。未解决为0。

| 配对 | 可判读 | 原始双正向 | 无条件共同承担 | 条件性 | 任选 | 未解决 | 主率 |
|---|---:|---:|---:|---:|---:|---:|---:|
'''
for r in co24:
 report+=f"| {r['name_a']} × {r['name_b']} | {r['n_assessable']} | {r['n_raw_dual']} | {r['n_unconditional']} | {r['n_conditional']} | {r['n_alternative']} | {r['n_unresolved']} | {pct(r['share_unconditional'])} |\n"
report+=f'''
研究×工程 71/1,623（4.4%），自变量占无条件共同承担的 {pct(next(r['max_positive_contribution'] for r in co24 if r['pair_id']=='RESEARCH_ENGINEERING'))}，未过50%集中线。工程×质量、工程×部署更常见，但仍是同广告职责组合，不是复合职能人数。

ML 三项本人开发独立条目两两共现（整公司156条，未知0）：训练系统×基础模型 34/156，训练系统×数据管线 45/156，基础模型×数据管线 34/156。共现不写成生产率互补，也不写成该技能用于该任务。

## 5. Q1：构成差异与同职能任务差异

整公司23家，制造/质量/供应链公司等权 {pct(q1row('WHOLE23','RF_MANUFACTURING_QUALITY_SUPPLY')['share_company_equal'])}、广告加权 {pct(q1row('WHOLE23','RF_MANUFACTURING_QUALITY_SUPPLY')['share_ad_weighted'])}，中位数 {pct(q1row('WHOLE23','RF_MANUFACTURING_QUALITY_SUPPLY')['median_company_share'])}，四分位 {pct(q1row('WHOLE23','RF_MANUFACTURING_QUALITY_SUPPLY')['p25_company_share'])}–{pct(q1row('WHOLE23','RF_MANUFACTURING_QUALITY_SUPPLY')['p75_company_share'])}。部署与现场服务等权 {pct(q1row('WHOLE23','RF_DEPLOYMENT_FIELD_SERVICE')['share_company_equal'])}、中位数 {pct(q1row('WHOLE23','RF_DEPLOYMENT_FIELD_SERVICE')['median_company_share'])}；最大一家 Boston Dynamics 占该类正向广告 {pct(q1row('WHOLE23','RF_DEPLOYMENT_FIELD_SERVICE')['max_positive_contribution'])}。Q1 观测零进入公司分布，零不是“公司不需要该工作”。

部署活动不能还原成部署职能招聘。整公司等权：部署职能占比 {eq_fn*100:.1f}%，本人承担部署活动 {eq_act*100:.1f}%，**非部署主职能内部**仍有 {eq_out*100:.1f}%。点落在“活动率 = 职能占比”线上方，构成解释不够。

![部署职能与部署活动]({F[2]['png']})

## 6. 案例（至多两组四家）

入选规则在比较前锁定：制造组要求整公司、整机系统、制造产线 OBSERVED_USE，优先客户确认，并在 |K|≥2 的共同职能对中取最大 K。物流组取自营履单服务与客户侧证据最强的系统产品公司对照；统一权重不是入选前置。

{md(['公司','组别','供给形态','广告数','入选/退出'], [[r['company_name'], r['selected_group'] or '—', r['stratum'], r['n_ads'], r['exclusion_or_inclusion'][:120]] for r in reg if r['status']!='NOT_CANDIDATE' or r['company_id'] in ['US_AMAZON_FTR']])}

### 组1 制造产线实际使用：银河通用 × Figure

- 银河通用：观察日 2026-09-11，宁德时代客户确认 S1 入线；另有香港自营零售，不与产线混成一种模式。
- Figure：观察日 2026-08-31，BMW 确认 Figure 02 在车身车间运行。Figure 03 到厂自述不升为已运行。
- 两国差异只作背景，不写成国家效应。批次不同已记录。
- 共同职能 K：公司支持、制造质量供应、ML/AI工程、软件与平台（各 ≥10 条活动可判读）。K 内覆盖约 48% / 48%。

{md(['活动','银河通用自身权重','Figure自身权重','银河通用职能等权','Figure职能等权'], [[r['activity_name'], pct(r['own_weight_a']), pct(r['own_weight_b']), pct(r['equal_weight_a']), pct(r['equal_weight_b'])] for r in uwg1])}

K 内工程实现银河通用仍高于 Figure（自身权重 56.1% / 45.0%；等权 47.6% / 56.7% 方向会随权重改变）。质量验证 Figure 更高。部署活动在共同职能内接近（15.9% / 16.7%），但**全公司**部署活动 Figure 29.4%、银河通用 13.8%，因为 Figure 部署职能本身更高（11.1% / 1.1%），且非部署职能内部署活动也更高（20.5% / 13.4%）。构成与岗内任务同时存在；权重变化足以改变工程实现的高低方向，故工程实现不写成稳定的公司排序。

![共同职能内活动率]({F[1]['png']})

Q2 同职能任务（本人开发、独立条目）：银河通用 ML {q2_g_fm.get('n_base')}条中基础模型/VLA {q2frac(q2_g_fm)}，训练推理系统 {q2frac(q2_g_sys)}；Figure ML {q2_f_sys.get('n_base')}条中训练系统 {q2frac(q2_f_sys)}，基础模型 {q2frac(q2_f_fm)}（Figure ML 分母={q2_f_sys.get('n_base')}，小样本）。软件可靠性开发银河通用 {q2frac(q2_g_rel)}，Figure {q2frac(q2_f_rel)}。没有原文用途连接时，这些是共现与职责语境，不是“该技能用于产线交付”。可靠性开发尤其不能写成客户现场交付责任。

### 组2 物流交付责任：Agility × Nimble

- Agility：整机/RaaS，GXO SPANX 客户确认商业部署；部署职能 3.0%，部署活动 24.2%，非部署职能内 23.4%。
- Nimble：自营机器人履单 3PL；部署职能 14.7%，部署活动 38.2%，非部署职能内 27.6%。
- 共同职能 |K|=0，统一权重 **不适用**，只保留点值。不补零、不合并类别。
- 二者都有物流实际使用证据，但责任主体不同：Agility 是客户现场供应，现场谁运营仍标未知；Nimble 是公司自营履单。招聘上 Nimble 部署职能更高，但两家的部署活动都远高于部署职能占比。

未入选但检索过的同条件对象：智元（制造为供应方自述）、千寻（媒体且 media_only）、Boston Dynamics（多产品，Stretch 与 Atlas 不能共用招聘板）、Pickle（13条）、Dexterity（来源不足1条）。没有为了预期叙事挑选最大差距。

## 7. 公司证据与 T5

交付责任长表继承 B 包 680条事实中可映射到产品开发、集成、现场部署、持续运行、维护、演示/试点/付款等环节的记录。时间主比较只用招聘观察时点及此前已公开、`USABLE_AT_OBSERVATION` 的条目。无日期页与观察后变化不进入时点匹配。系统远程管理不等于供应方负责运行；缺某职能招聘不证明外包。

{md(['公司','案例组','供给','关键环节','责任主体','事实摘要','证据'], [[p['company_name'], p['case_id'], p['stratum'], p['key_stage'], p['key_subject'], p['key_fact'], p['evidence_ids']] for p in prof])}

Figure 的付费/交付字段在 B 包仍为未查，保持未知，不把 BMW 运行写成付款合同。银河通用产线是客户确认使用，不是已核收入。Agility 收入自述留在客户页上的供应方引语，不升为独立核账。

## 8. 敏感性与 T6

Q2 未知赋值对照与研究书算术检查一致：ML Python 一般要求独立 60正向 / 23未知 / 基础156，范围 {pct(ctrl[0]['bound_low'])}–{pct(ctrl[0]['bound_high'])}；软件 Linux 70/3/180 为 {pct(ctrl[1]['bound_low'])}–{pct(ctrl[1]['bound_high'])}。这不是置信区间。

{md(['结论ID','问题','状态','最终措辞'], [[r['conclusion_id'], r['q'], r['status'], r['final_wording']] for r in t6])}

未声称：人才短缺、行业独有、国家因果、员工人数、技能互补带来生产率。

## 9. 限制

- 公开招聘广告样本，非概率，两批次。
- 广告≠在职结构；缺采是未知。
- 共同职能统一权重只覆盖 K 内广告。
- 活动共现判定对无结构广告按同一岗位正文的本人承担处理；30棵树中无本组双正向落在任选根上，故条件性/任选计数为0，不是“不存在任选岗位”。
- 资历与工作对象只对案例广告从标题和活动引语做标记，未说明≠初级。
- 阶段E研究初稿尚未开始。

本报告由 Cursor Grok 4.6 按阶段D研究执行书 v1 计算并撰写。
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')

methods='''# 阶段D计数、分母与案例规则

阶段C的Q1–Q3分母继续有效。本页只记录D新增规则。

## 覆盖

Q1：各主职能的公司分布包含观测零。中位数与四分位按公司 share_all。最大贡献是该公司该类正向广告 / 该类总正向广告。零分母公司不存在于Q1（每家都有全部广告分母）。

Q2/Q3：分别报告基础公司数、可解释公司数、正向公司数。分母贡献与正向贡献分开。没有该职能或分母为0的公司不按零参加Q2中位数。分母贡献>50%标集中。

## 双向交叉

P(活动|主职能) 使用该主职能活动可判读广告。P(主职能|活动) 使用该活动本人承担正向广告。结构类、未明确状态单列。

## 共同职能 K

两家公司统一权重时，只纳入双方均有至少10条活动可判读广告的具体主职能，且至少2个共同职能。K 外、结构与未知主类退出该受限比较。三种权重：自身职能比重、K内职能等权、双方合并职能比重。不满足则 INAPPLICABLE，不补零。

## 共现

三组限定本人承担。无条件共同承担为主率分子；条件性与任选为已知非无条件；未解决退出该配对分母。无职责结构的双正向记无条件共同承担（同一广告、同一招聘对象）。根 ALL 记无条件。根 OR 按引语与分支跨度绑定；无法绑定则未解决。不覆盖原 OWNED 标签。

## 来源较完整子集

锁定文件 `inputs/decisions/source_complete_subset.json`。在计算D派生率之前写入。

## 案例

锁定文件 `inputs/decisions/case_selection_rules.json`。制造组取最大 |K| 且优先客户确认。物流组为自营履单对客户确认系统产品。统计差距不作为优先级。
'''
(ROOT/'METHODS.md').write_text(methods,encoding='utf-8')

rows=[]
for p in sorted((T).glob('*.csv')):
 n=sum(1 for _ in open(p,encoding='utf-8-sig'))-1
 rows.append(f'| [{p.name}](tables/{p.name}) | {n} | |')
dd='# 阶段D数据表目录\n\nUTF-8 BOM。比例为0–1，空值为NA。\n\n| 文件 | 行数 | 说明 |\n|---|---:|---|\n'+'\n'.join(rows)+'\n\nidentity_key 为完整主键。T5 为长表，一格不压平不同产品或时期。T6 每条结论可回溯到数字、敏感性、反例和限制。\n'
(ROOT/'DATA_DICTIONARY.md').write_text(dd,encoding='utf-8')

# HTML
cards=[]
for fig in F:
 cards.append(f'<figure><img src="{escape(fig["png"])}" alt="{escape(fig["title"])}"><figcaption><strong>{escape(fig["title"])}</strong> {escape(fig["caption"])}</figcaption></figure>')
sel_html=''.join(f'<tr><td>{escape(r["company_name"])}</td><td>{escape(r["selected_group"])}</td><td>{escape(r["stratum"])}</td><td>{escape(str(r["n_ads"]))}</td></tr>' for r in sel)
html=f'''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>阶段D · grok4.6研究</title>
<style>
body{{font-family:"Microsoft YaHei",sans-serif;margin:0;background:#f4f6f8;color:#213247}}
main{{max-width:1100px;margin:0 auto;padding:28px 20px 80px}}
h1{{font-size:26px;margin:0 0 8px}}
.mark{{display:inline-block;background:#213247;color:#fff;padding:4px 10px;font-size:13px;margin-bottom:16px}}
.sub{{color:#5b6a78;margin-bottom:24px}}
figure{{margin:24px 0;background:#fff;padding:12px;border:1px solid #e3e8ee}}
img{{max-width:100%;height:auto}}
table{{border-collapse:collapse;width:100%;background:#fff;margin:16px 0}}
th,td{{border:1px solid #e3e8ee;padding:8px 10px;text-align:left;font-size:14px}}
a{{color:#286793}}
</style></head><body><main>
<div class="mark">grok4.6研究 · Cursor Grok 4.6</div>
<h1>具身智能公开招聘研究 · 阶段D</h1>
<p class="sub">职能构成与同职能任务分开测量。完整正文见 <a href="REPORT.md">REPORT.md</a>。</p>
{''.join(cards)}
<h2>入选案例</h2>
<table><thead><tr><th>公司</th><th>组别</th><th>供给</th><th>广告</th></tr></thead><tbody>{sel_html}</tbody></table>
<p>T6 结论状态均为已检查口径下方向一致，但范围限于本样本。物流组统一权重不适用。</p>
</main></body></html>
'''
# pretty print / avoid mega lines: already multiline
(ROOT/'index.html').write_text(html,encoding='utf-8')
S=js(ROOT/'summary.json')
S['table_rows']={p.name:sum(1 for _ in open(p,encoding='utf-8-sig'))-1 for p in sorted(T.glob('*.csv'))}
dump(ROOT/'summary.json',S)
print('wrote REPORT METHODS DATA_DICTIONARY index')
