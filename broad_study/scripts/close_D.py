from common import *
from fractions import Fraction as F
import sqlite3
results=read(ROOT/'tables/D2_decomposition_summary.csv');parts=read(ROOT/'tables/D2_decomposition_role_parts.csv');qual=read(ROOT/'tables/D1_all_pair_qualification.csv')
db=sqlite3.connect(':memory:');db.execute('create table j(k text,c text,f text,valid int)');db.executemany('insert into j values(?,?,?,?)',[(k,r['company_id'],role(r),int(k in admitted)) for k,r in J.items()]);db.execute('create table act(k text,a text,rel text)');db.executemany('insert into act values(?,?,?)',[(r['identity_key'],r['label_code'],r['relation']) for r in activities]);checks=[]
source=read(ROOT/'tables/R_source_membership.csv');aud={r['identity_key'] for r in read(ROOT/'tables/D_explicit_audience_exclusions.csv')};dups=read(ROOT/'tables/D_exact_duplicate_groups.csv');drop=set()
for r in dups:drop.update(set(json.loads(r['all_ids_json']))-{r['retained_id']})
for r in results:
    if r['qualification'].startswith('NA'):continue
    if r['scenario']=='MAIN':allowed=set(J)
    elif r['scenario']=='NO_EXPLICIT_CAMPUS_OR_INTERN':allowed=set(J)-aud
    elif r['scenario']=='EXACT_DUTY_DEDUP':allowed=set(J)-drop
    else:allowed={x['identity_key'] for x in source if x['scope']==r['scenario']}
    db.execute('drop table if exists scope');db.execute('create table scope(k text primary key)');db.executemany('insert into scope values(?)',[(k,) for k in allowed]);K=json.loads(r['K_json']);count={}
    for c in [r['company_a'],r['company_b']]:
        for f in K:
            n,p=db.execute("select count(distinct j.k),count(distinct a.k) from j join scope s on j.k=s.k left join act a on a.k=j.k and a.a=? and a.rel='OWNED' where j.c=? and j.f=? and j.valid=1",(r['activity'],c,f)).fetchone();count[c,f]=(p,n)
    a,b=r['company_a'],r['company_b'];na=sum(count[a,f][1] for f in K);nb=sum(count[b,f][1] for f in K);ra=sum(F(count[a,f][0],na) for f in K);rb=sum(F(count[b,f][0],nb) for f in K)
    # Cross-standardized rates form a second, algebraically different computation.
    ab=sum(F(count[a,f][1],na)*F(*count[b,f]) for f in K);ba=sum(F(count[b,f][1],nb)*F(*count[a,f]) for f in K)
    C=(ab-rb+ra-ba)/2;W=(ba-rb+ra-ab)/2
    checks.append(dict(case_id=r['case_id'],scenario=r['scenario'],mode=r['mode'],activity=r['activity'],delta=float(ra-rb)*100,composition=float(C)*100,within=float(W)*100,pass_value=abs(float(C)*100-float(r['composition_pp']))<1e-10 and abs(float(W)*100-float(r['within_role_pp']))<1e-10 and ra-rb==C+W))
assert all(r['pass_value'] for r in checks);save_json('verification/D_SQL_fraction_checks.json',{'method':'Same researcher independent SQLite counts and exact rational cross-standardized calculation','n_checks':len(checks),'checks':checks})
main=[r for r in results if r['case_id']=='D_MAIN' and r['scenario']=='MAIN' and r['mode']=='FIXED_K'];core=['ACT_ENGINEERING','ACT_DEPLOYMENT','ACT_QUALITY','ACT_RESEARCH']
out=['# 方向二：职能构成与职能内活动差异｜Astra','## 1. 研究结果','在银河通用与Figure四个共同职能内，工程活动的总体差异由方向相反的两部分组成：职能构成对应+19.45个百分点，职能内活动率对应−8.35个百分点，合计银河通用高11.10个百分点。部署与维护的总差只有−0.81个百分点，但两部分为+4.39与−5.21个百分点。这说明总率相近也可能掩盖两种相反差异。','这些是固定广告范围的算术分量，不是公司业务模式或国家的因果贡献率。','## 2. 固定范围与覆盖','主比较A=银河通用、B=Figure；K为公司支持、制造质量供应链、ML、软件。双方每类活动可读广告均至少10条。K分别覆盖82/181=45.30%和60/126=47.62%。旧Grok正文及研究书约48%/48%的近似表述已更正为R16；四职能及旧对应活动率未改变。','银河通用观察于9月11日，Figure为8月31日，且国家、招聘渠道和公司背景不同。K之外分别99和66条广告另表保存，不能把K内结果推广为全公司。','补充比较A=智元、B=银河通用，仅公司支持与ML两类，覆盖23/82=28.05%和37/181=20.44%，只有一个技术职能。Nimble×Dexterity与Agility×Nimble的K均为空，明确不适用。全部253个公司对只做资格检查，17对满足形式门槛，没有按差异大小再挑样本。','## 3. 算术定义','对固定K，s为该职能在公司K内的可读广告份额，q为职能内本人承担某活动的比例。R=Σsq；Δ=R_A−R_B。','构成分量 C=Σ(s_A−s_B)(q_A+q_B)/2；职能内分量 W=Σ(q_A−q_B)(s_A+s_B)/2。恒有Δ=C+W。下表单位为百分点，不发布C/Δ之类贡献百分比。','|活动|A率|B率|总差Δ|构成C|职能内W|','|---|---:|---:|---:|---:|---:|']
for a in core:
    r=next(r for r in main if r['activity']==a);out.append(f"|{AN[a]}|{float(r['R_A'])*100:.2f}%|{float(r['R_B'])*100:.2f}%|{float(r['delta_pp']):+.2f}|{float(r['composition_pp']):+.2f}|{float(r['within_role_pp']):+.2f}|")
out+=['','工程的正向构成分量主要来自银河通用K内较高的ML与软件份额；这两类在双方的工程活动率均较高。与此同时，Figure这四类职能的工程活动率都高于银河通用，故职能内分量为负。等权后工程率47.58%/56.74%反向；这不是公司能力排名，而是权重变化的具体后果。','部署与维护需依R的A01理解：它包含不同对象，不能写成全为客户现场部署。O已显示同职能中模型运行、机器人实机、业务后台并不一致。质量也不限定制造质量。','## 4. 智元与银河通用有限补充','在两类K内，智元减银河通用的部署与维护差−21.62个百分点，其中构成−2.12、职能内−19.51。工程差−1.88，构成−11.63、职能内+9.75，仍有抵消。低覆盖与公司支持的零技术活动使其主要是ML的局部对照，不能称两个技术职能的重复验证。','## 5. 敏感性与NA规则','三个来源筛选均排除银河通用，固定K中出现零分母，结果均为NA；不把Figure保留而Galbot退出的结果当成稳健性验证。剔除明确校招、实习及接受应届者后、以及同公司同职能完全一致职责文本去重后，固定K重算，并另列重建K结果；后者是改变研究范围。','受众检测候选经过语境复核：5条人力资源广告中的校招/应届是工作服务对象，未作为候选人资格剔除。最终全样本137条进入该明确受众敏感性；没有把未写受众视为资深。','|主比较情景|资格|总差：工程|构成|职能内|','|---|---|---:|---:|---:|']
for sn in ['MAIN','NO_EXPLICIT_CAMPUS_OR_INTERN','EXACT_DUTY_DEDUP']:
    r=next(x for x in results if x['case_id']=='D_MAIN' and x['scenario']==sn and x['mode']=='FIXED_K' and x['activity']=='ACT_ENGINEERING');out.append(f"|{sn}|{r['qualification']}|{float(r['delta_pp']):+.2f}|{float(r['composition_pp']):+.2f}|{float(r['within_role_pp']):+.2f}|")
out+=['','固定K某格0<N<10时仅为不达原门槛的诊断结果；N=0退出。当前固定K内无来源未知，因此未知赋值界限退化为点值；主职能本身不明的来源不足广告不能无依据分配到K。通用敏感性算法按B重算权重，并按系数符号求Δ/C/W的盒状极值，未把全0与全1同时赋值冒充通用上下界。','## 6. 验证与结论强度',f'{len(checks)}个可计算情景通过Δ=C+W、交换A/B变号、相同权重C=0和相同比例W=0检查。第二套SQLite原始计数加有理数交叉标准化实现检查全部{len(checks)}个结果。这是同一研究者独立计算实现，非外部评审。','逐职能P/N、s/q、C/W、K内外范围和未知、固定及重建K敏感性均交付。这里新增的是严格算术分解。公开产品使用及交付责任与这些分量之间的机制联系仍缺少足够广告归属证据，保留为待检验解释。']
(ROOT/'reports/D_构成与职能内分解报告_Astra.md').write_text('\n\n'.join(out),encoding='utf-8')
print('D SQL rational checks',len(checks))
