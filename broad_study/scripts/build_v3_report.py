from common import *
import sys
from decimal import Decimal,ROUND_HALF_UP
sys.path.insert(0,str(ROOT/'runtime'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font=FontProperties(fname='C:/Windows/Fonts/msyh.ttc');plt.rcParams['font.family']=font.get_name();plt.rcParams['axes.unicode_minus']=False
def stream(p):
 with p.open(encoding='utf-8-sig',newline='') as f:yield from csv.DictReader(f)
def pct(v):return '不汇总' if v in [None,''] else str((Decimal(str(v))*100).quantize(Decimal('.1'),rounding=ROUND_HALF_UP))+'%'
def pn(a):return a['P']+'/'+a['N']
def tab(h,rows):return '\n'.join(['|'+'|'.join(h)+'|','|'+'|'.join(['---']*len(h))+'|']+['|'+'|'.join(str(v).replace('|','／') for v in r)+'|' for r in rows])
def cite(*names):return '数据与证据：'+'；'.join(f'[{n}](<{(ROOT/n).as_posix()}>)' for n in names)+'。'
qc=json.loads((ROOT/'verification/astra_materialization.json').read_text(encoding='utf-8'))
impact=json.loads((ROOT/'verification/V3_revision_impact_final.json').read_text(encoding='utf-8'))
coverage=read(ROOT/'tables/Q4_role_coverage_final.csv');review=read(ROOT/'tables/V3_review_coverage_final.csv')
chain=read(ROOT/'tables/V3_key_results_version_chain.csv');layers=read(ROOT/'tables/V3_two_layer_aggregates.csv');points=read(ROOT/'tables/V3_two_layer_company_points.csv')
L={(x['scenario'],x['task'],x['label_code']):x for x in layers}
P={(x['scenario'],x['task'],x['label_code'],x['company_id']):x for x in points}
main={};sens=[]
keyset={(x['role'],x['label_code'],x['metric'],x['branch']) for x in chain}
for x in stream(ROOT/'tables/Q4_aggregates_final.csv'):
 key=(x['role'],x['label_code'],x['metric'],x['branch'])
 if x['scope']=='WHOLE23':main[key]=x
 if key in keyset and x['scope'] in ['WHOLE23','DEDUPE_EXACT_DUTIES','EXCLUDE_EXPLICIT_CAMPUS_INTERN','S1_ACTIVITY_COMPLETE','S2_SOURCE_QUALITY','S3_SOURCE_QUALITY_LENGTH200']:sens.append(x)
tp={}
for x in stream(ROOT/'tables/Q4_task_company_points_final.csv'):
 if x['metric']=='GENERAL' and x['branch']=='UNCONDITIONAL' and x['label_code'] in ['SK_PYTHON','SK_CPP','SK_LINUX','SK_ALTIUM','V2_EMC_SIPI']:
  tp[x['task'],x['label_code'],x['company_id']]=x
loo=read(ROOT/'tables/V3_two_layer_leave_one_company_out.csv')
cross=[a for a in read(ROOT/'tables/R_cross_function.csv') if a['scope']=='WHOLE23' and a['activity']!='ACT_DEPLOYMENT']
dec=[a for a in read(ROOT/'tables/D2_decomposition_summary.csv') if a['case_id']=='D_MAIN' and a['mode']=='FIXED_K' and a['activity']=='ACT_ENGINEERING']
decm=next(a for a in dec if a['scenario']=='MAIN')
objects=read(ROOT/'tables/O4_company_role_object.csv');att=read(ROOT/'tables/O4_attribution_seniority_unknown.csv')
task_names={'ROBOT_MODEL':'机器人模型','ROBOT_RUNTIME':'机器人运行软件','BOARD_CIRCUIT':'板级电路'}
metnames={'GENERAL':'一般要求','REQUIRED':'明确必备','PREFERRED':'优先条件','DUTY_OWN_USE':'职责使用','DUTY_OWN_DEVELOP':'职责开发'}
out=[];p=out.append
p('# 具身智能公开招聘研究最终综合报告')
p('Astra　2026年9月18日　核心研究修订与 Q2 全职能拓展 V3')
p('本报告研究已冻结的24个招聘主体、1,654条公开广告中，公司如何组织职能、描述活动，以及表达同类工作的技术和工具要求。主要认识是：公司整体的活动比例会受到职能构成影响；同一职能内仍有不同工作对象；具体工具的提及、明确必备和一般要求也不能相互替代。')
p('**本轮六步工作已完成。** 三稿合并后的核心结果、84条工作对象研究、公司差异算术分解，与本版Q2内容复核和同任务深化分析在此合并。预设340条抽样已全文复核，1,208条强制队列已按规定范围复核。累计全文复核469条、仅边界语境复核760条；另347条不在本轮必做队列中，保留首轮编码。Q2成果按这个明确的复核范围收口，研究性质仍是固定样本的探索性描述。')
p('本版撤回依赖“部署与维护”历史标签口径一致性的实质结论。它保留原始编码和可追溯数字，但不再把这些数字用于证明客户现场部署或交付责任的差异。旧报告保留为历史版本，以本版结论台账为准。')
p('## 一 主要研究判断')
p('研究探索与宽口径质量活动经常出现在同名主职能之外。因此，招聘多少某类岗位，与多少岗位承担某项活动，是两个问题。研究活动不只发生在研究科学岗位，质量活动也不限于制造质量部门。这里观察的是广告里的职责，不是企业的组织架构。')
p('84条对象研究中，81条不能归属明确命名的产品或业务线。公司代表产品有助于理解背景，却不足以解释每条岗位。将模型、训练系统、机器人运行软件、业务后台等对象分开后，比较才更接近实际工作的差别。')
p('银河通用与Figure在四个共同职能内，工程活动率总差为+11.10个百分点。其中职能构成分量为+19.45，职能内活动率分量为−8.35；两个方向相反。总比例较高不能单独证明同类岗位更偏工程，也不能改写成业务模式的因果贡献率。')
p('Q2深化得到两种不同情形：机器人模型岗位里，银河通用与自变量的Python提及差异在放宽要求方式后仍存在；机器人运行软件里，两家C++提及率则接近。前者是当前文本中的差异线索，后者提示部分单格差异来自招聘写法和未解关系。两者都不直接测量实际工具使用量或工程能力。')
p('本轮不必补齐20家中国加20家美国。当前问题已能用冻结资料回答到有限范围。未来若研究供给类型，优先增加缺少独立公司的类型；若研究具身岗位的特殊性，需要相近的非具身工作作为对照。单纯凑齐国家数量不能解决这两类识别问题。')
p('## 二 样本和测量范围')
p(tab(['分析范围','广告数','解释单位'],[['冻结研究总体','1,654','24个招聘主体'],['整公司主范围','1,630','23家公司'],['Amazon FAR','24','团队单列'],['Q2具体职能全范围','1,576','17个具体职能'],['Q2整公司主范围','1,552','本版技术比较的总体'],['工作对象案例框','84','4家公司和2个职能']]))
p('广告数不是人数、招录量或员工存量。资料来自冻结包中各次真实观察，不能当作同一时刻的行业普查。公司归属、广告地点、文本语言、供给方式分别记录。缺采或文本未写出的内容保留为未知或未记正例，不反推企业没有相应业务。')
p('Q2使用冻结Q2-v2.1目录354项，各职能采用自己的适用清单。技术概念、具名工具与协议、工程方法和操作资格分开表达。原14个语境格保留，另有8个职责分支格，共22格；示例、任选、兼有二者及条件执行不会被强制归成无条件。目录之外的工具名称不临时扩入正式比例。')
p('其余78条广告没有被硬放入单一具体职能：包括复合与任选结构、主职能歧义、未映射和来源不足。因此，这套Q2子集不能估计全部1,654条广告的复合技能比例。原冻结主分类、A/B/C和研究数据库均保持原版本。')
p('### 正例 未知和复核状态')
p('原语境表中，P是该指标的明确正例，Z是当前判读中未记正例，U是已发现但未解的对象、责任或分支关系；不适用NA与来源排除单独保留。可判断分母N=P+Z，含未知分母B=P+Z+U，主比例P/N。将未知分别全部当作非正例和正例，得到P/B至(P+U)/B的界限。它不是置信区间，也不覆盖尚未发现的漏判。')
p('每个格至少需要3家公司、合计N≥20才显示探索性组比例；公司点值0<N<10标注小样本。公司等权先算各公司的比例再平均，广告加权则合并广告计数。门槛只限定展示，不能带来总体代表性或统计显著性。主图条目筛选另需覆盖5家公司、10条明确正例广告；因此，没有主图不等于任何指标都不能汇总。')
p('测量状态与复核状态分开。Z或U=0不表示已经二次全文复核；本版469条全文、760条边界复核和347条继承首轮的状态逐广告可查。Astra回读自己的旧编码不构成独立双编码；对grok编码的复核也没有建立独立人工金标准。')
p(cite('tables/Q4_scope_definitions.csv','tables/Q3_review_receipts.csv','configs/Q_catalog_v2_frozen.json'))
p('## 三 职能与活动分布')
p('制造质量供应链、软件与平台、ML、公司支持和硬件在所见招聘中占较大的广告量。完整17职能规模和复核范围列于附录一；这些广告规模描述招聘表达的构成，不能用来估计公司实际部门人数或研发预算。')
p(tab(['活动','同名职能外正例','比例','口径'],[[{'ACT_RESEARCH':'研究探索','ACT_QUALITY':'质量验证'}[a['activity']],pn(a),pct(a['ad_weighted']),'分母是该活动全部正例'] for a in cross]))
p('研究探索48/66、宽质量300/459出现在同名主职能之外。宽质量依据原规则包括验证执行、质量放行、合规和缺陷闭环，不能缩写为制造质量。全公司活动可判断广告中，研究与工程共同承担65/1,599，工程与质量共同承担301/1,599。活动可以并存，但共同写在一条广告里不证明实际流程的先后或部门协作结构。')
p('### 部署活动旧结论的处理')
p('原规则写的是“实际现场部署、验收、维修或运行维护”。八条定向全文回读显示，历史正例涉及模型集成、训练环境和物理样机，相关数字对象又存在未被同样纳入的记录。例如N0312的训练环境维护曾计入，N0401明确的模型维护却没有同类活动标签。旧报告把零值解释为“规则只测客户现场”，依据不足。')
p('因此，本版撤回“部署活动标签已经一致测量了客户现场或广义运维”的保证，也撤回依赖它的公司比较主结论。264/343及−0.81=+4.39−5.21个百分点只保留在历史测量附录，不参与本版实质推论。这是对结论的收口，没有暗中修改冻结数据，也没有把八条回查包装成全体部署编码验收。')
p(cite('tables/R_cross_function.csv','tables/R_joint_summary.csv','tables/V3_activity_rule_record_claim.csv','tables/V3_claim_disposition.csv'))
p('## 四 同职能的工作对象差异')
p('方向一固定四家公司、ML与软件两个职能，完整阅读84条广告。对象按原文多值记录，允许同一广告同时涉及模型、数据和训练系统；表内“涉及”包含明确承担与参与，不能与Q2较严格的本人职责格直接互换。')
orows=[]
for co in ['CN_AGIBOT','CN_GALBOT','US_DEXTERITY','US_NIMBLE']:
 def oval(role,obj):
  xs=[x for x in objects if x['company_id']==co and x['role']==role and x['object']==obj and x['responsibility']=='ANY_RESPONSIBILITY']
  return pn(xs[0]) if xs else '见底表'
 orows.append([CO[co]['company_name'],oval('RF_ML_AI_ENGINEERING','MODEL'),oval('RF_ML_AI_ENGINEERING','DATA'),oval('RF_ROBOTICS_SOFTWARE','ROBOT_RUNTIME'),oval('RF_ROBOTICS_SOFTWARE','FULFILMENT_IT')])
p(tab(['公司','ML模型','ML数据','软件机器人运行','软件履单业务'],orows))
p('智元与银河通用的ML广告中，模型、数据和训练工程经常共同出现；软件则有机器人运行时、内部基础设施与应用系统等不同对象。Nimble的软件出现履单业务对象；Dexterity的软件案例只有两条，不适合估计稳定的公司软件人才结构。机器人真机或物理现场对象还包括样机和实验室，不能全部解释为客户生产部署。')
p(f'产品归属方面，{sum(int(x["product_explicit"])+int(x["product_direct_link"]) for x in att)}条达到明确命名或直接连接标准，{sum(int(x["product_unknown"]) for x in att)}条未知。经验年限明确写出{sum(int(x["years_stated"]) for x in att)}条，未明示{sum(int(x["frame_N"])-int(x["years_stated"]) for x in att)}条。未知不表示没有产品归属，也不表示岗位是初级或资深。现有公司产品资料不能自动补上这条广告到产品的连接。')
p('我的判断是，工作对象比公司代表产品更接近这批资料的解释能力。它能说明同一主职能为何使用不同方法或工具；要解释具体客户、收入或交付模式对岗位的作用，仍需岗位与项目之间的直接证据。')
p(cite('tables/O4_company_role_object.csv','tables/O4_attribution_seniority_unknown.csv','tables/O2_evidence_long.csv'))
p('## 五 公司差异的算术分解')
p('比较固定为银河通用减Figure，在公司支持、制造质量供应链、ML、软件四个共同职能内计算工程活动率。先按各公司在共同范围内的职能份额加权，再把总差拆成“职能份额不同”与“同职能活动率不同”两部分；采用两家公司相应权重或活动率的平均值，两个分量与总差精确相加。')
p(tab(['情景','总差百分点','构成分量','职能内分量'],[[{'MAIN':'主范围','NO_EXPLICIT_CAMPUS_OR_INTERN':'去明确实习校招','EXACT_DUTY_DEDUP':'职责模板去重'}[a['scenario']],f'{float(a["delta_pp"]):+.2f}',f'{float(a["composition_pp"]):+.2f}',f'{float(a["within_role_pp"]):+.2f}'] for a in dec if a['qualification']=='ELIGIBLE']))
p('主范围中，银河通用工程活动率56.10%，Figure为45.00%。+19.45的构成分量表示，银河通用在这四类广告中给予工程活动率较高职能更大的权重；−8.35的职能内分量则指向相反方向。两部分互相抵消，不能说“构成解释了差异的百分之多少”而忽略另一部分。')
p('若四个职能直接等权，银河通用47.58%、Figure56.74%，排序改变。等权差−9.16与上述−8.35并不冲突：前者每类权重相同，后者使用两家公司平均职能份额。它们回答的是不同的标准化问题。')
p('这四类只覆盖银河通用活动可判断广告82/181、Figure 60/126，分别45.30%和47.62%。不能推广成全公司差异。去实习校招与职责模板去重后，两分量的相反方向保留；但固定来源质量方案排除了银河通用，比较记为NA，不能宣称通过这些来源敏感性检验。该分解没有控制资历、模板、地点或公司背景，更不是国家或业务模式的因果效应。')
p(f'![工程活动差异分解](<{(ROOT/"figures/V3_decomposition.png").as_posix()}>)')
p('图1　银河通用减Figure的工程活动差异。共同职能固定，单位为百分点；分量是算术组成。')
p(cite('tables/D2_decomposition_summary.csv','tables/D2_decomposition_role_parts.csv'))
p('## 六 Q2的内容复核与测量修订')
p(f'本版在上一版基础上新增{impact["v3_incremental_operations"]:,}条修订事务，涉及{impact["v3_incremental_ads"]}条不同广告。事务包含定位补全、分支和要求语境调整、遗漏补入、任务修订，以及对前次修订的恢复；不能把事务数当成错误广告数。比较最终证据版本后，{impact["effective_evidence_changed"]:,}条证据有实质字段变化或新增，涉及{impact["effective_evidence_ads"]}条广告。')
p('主要问题是一般与优先要求混淆、资格证据错锚到职责、工具使用被记成开发工具本体、示例或任选被记成无条件，以及局部来源不足未影响相应分母。修订保留每个旧值、原文位置、理由和署名。两条E0107虽然阅读编号和正文相同，仍按不同岗位ID保存，未以阅读编号覆盖其中一条。')
p(tab(['同口径指标','阶段C','grok首轮','Astra上一版','Astra本版'],[[('ML ' if a['role']=='RF_ML_AI_ENGINEERING' else '软件 ' if a['role']=='RF_ROBOTICS_SOFTWARE' else '控制 ' if a['role']=='RF_CONTROL_PLANNING' else '部署现场 ')+a['label_name']+' '+metnames[a['metric']],*[f'{a[v+"_P"]}/{a[v+"_N"]} U{a[v+"_U"]}' if a[v+'_P'] else '未纳入' for v in ['C','grok','Astra_v2','Astra_v3']]] for a in chain]))
p('表中均为无条件格。ML基础模型/VLA开发的18条正例退出原格，主要转为参与协作、示例、责任或对象未解，以及训练基础设施所支持的模型对象；这不表示18条广告完全没有模型工作。当前49/154、U=2只回答严格本人开发且无条件的文本格，不能作为“全部模型研发需求”的比例。训练推理系统、Python和Linux等也有变化，幅度并不一致。')
p('控制闭环一般要求在上一版为51/75，本版为52/75；数值回到grok并不意味着未经复核地恢复整份旧报告。应以最终逐条证据为准。相反，ML Python一般无条件从60/135、U=21回到60/133、U=23，说明“未知更少”本身不构成质量改进。')
p(f'相同22语境口径下，本版{impact["same_scope_cells"]:,}个整公司汇总格中，{impact["changed_cells"]:,}格的计数、分母或门槛改变，其中{impact["gate_changes"]}格门槛改变。修订影响集中在测量解释，不能当作企业需求的时间变化。C与Q2-v2.1目录不完全相同，只有可对齐条目才能比较。')
p(cite('tables/V3_key_results_version_chain.csv','tables/V3_incremental_change_axes.csv','tables/V3_revision_impact_v2_to_v3.csv','tables/Q3_astra_changes.csv'))
p('## 七 同任务中的技术提及与要求方式')
p('### 任务划分与两层指标')
p('任务按职责的主要交付和工作对象划分，不因为出现Python、C++或某工具就纳入。机器人模型要求本人训练或优化机器人策略/具身模型；训练基础设施另列。机器人运行软件交付运行时、中间件或机器人应用，普通业务后台和云界面另列。板级电路交付板卡、PCB、电源驱动等电路，单纯固件或线束另列。')
p('主分析一条广告只有一个主任务。最终三个层分别105、87、56条整公司广告；166条广告另有次任务。N0353的主体是业务场景模型，机器人仅在优先背景中出现，因此从机器人模型主层移出。主次任务同时纳入只用于另列敏感性，按广告去重。任务层提高可比性，但没有消除具体对象、资历和模板的差异。')
p('第一层统计技术是否可辨识地出现在本人职责或资格要求中，并按广告去重。明确任选、示例和C/C++等分支未解的写法仍表示术语出现；对象本身未解的UNKNOWN不计明确提及，纯背景或协作联系另列。第二层在这些提及广告中拆看职责、明确必备、一般和优先。各方式可能重叠，不能加成100%；无条件要求仍单独查原22格。')
focus=[('ROBOT_MODEL','SK_PYTHON'),('ROBOT_MODEL','SK_PYTORCH'),('ROBOT_RUNTIME','SK_CPP'),('ROBOT_RUNTIME','SK_LINUX'),('BOARD_CIRCUIT','SK_ALTIUM'),('BOARD_CIRCUIT','V2_EMC_SIPI')]
p(tab(['任务与条目','第一层提及','职责','明确必备','一般','优先'],[[task_names[t]+' '+L['PRIMARY',t,c]['label_name'],pn(L['PRIMARY',t,c]),*[L['PRIMARY',t,c][m] for m in ['DUTY_ANY','REQUIRED','GENERAL','PREFERRED']]] for t,c in focus]))
p('第二层各列是提及广告数，分母为该行第一层的正例数。例如机器人模型Python有73条相关提及，其中65条出现一般要求、6条出现优先、2条出现明确必备、3条出现职责，类别有重叠。运行软件C++有80条相关提及，其中25条含某处未解分支；不能由80/87推出80条都无条件要求C++。')
p('### 机器人模型中的Python差异仍可见')
comparisons=[('ROBOT_MODEL','SK_PYTHON','CN_GALBOT'),('ROBOT_MODEL','SK_PYTHON','CN_XSQUARE'),('ROBOT_RUNTIME','SK_CPP','CN_GALBOT'),('ROBOT_RUNTIME','SK_CPP','CN_XSQUARE'),('ROBOT_RUNTIME','SK_CPP','US_FIELD_AI')]
comp=[]
for t,c,co in comparisons:
 a=P['PRIMARY',t,c,co];b=tp[t,c,co]
 comp.append([task_names[t]+' '+a['label_name'],CO[co]['company_name'],pn(a)+' '+pct(a['share']),pn(b)+' U'+b['U'],pct(b['unknown_low'])+'—'+pct(b['unknown_high'])])
p(tab(['任务与条目','公司','技术提及','一般无条件','该格未知界限'],comp))
p('银河通用机器人模型Python提及14/18，自变量10/21，分别77.8%与47.6%。一般无条件格为12/16、U=2与3/14、U=7。在只改变已识别未知的前提下，该格界限66.7%—77.8%与14.3%—47.6%不重叠。改成不限要求方式的术语提及后，差距仍约30.2个百分点，但小于只看一般无条件时的53.6个百分点。')
p('这组比较不能全部归结为一般与优先段落偏好：两家这部分Python提及都写在一般要求中，差别主要还涉及是否提及，以及并列或斜线关系能否确认为无条件。N0098明确“精通Python”，而自变量一些广告使用多语言斜线。未知界限不重叠仅说明既有U赋值不能抹去方向；未发现的漏判、任务细分和模板差异仍可能影响解释。')
p('### 运行软件中共同表达的语言能力')
p('银河通用与自变量C++提及分别14/16和9/10，即87.5%与90.0%；一般无条件格为9/11、U=5与3/4、U=6。其未知界限56.3%—87.5%和30.0%—90.0%大幅重叠。对这两家公司，现有证据更支持“C++在相近运行软件任务中都经常被提到”，不足以排列谁更需要C++。')
p('Field AI点值6/8含一般要求，样本小于10条；它只能作为公司点值，不宜与大公司样本构成稳定排名。职责提及、一般资格和优先条件的交叠还说明，技术出现并非一种单一要求强度。')
p('### 板级电路中的工具与工程方法')
p('板级电路任务里，Altium提及24/56，电磁兼容与信号/电源完整性36/56。前者主要出现在资格要求，后者在职责中27条、一般要求20条、优先条件11条，方式可重叠。非算法工作不能只用编程语言衡量；设计工具与验证方法提供了不同的能力线索。')
bp=[]
for co in ['US_APPTRONIK','CN_XSQUARE','CN_GALAXEA']:
 a=P['PRIMARY','BOARD_CIRCUIT','SK_ALTIUM',co];b=P['PRIMARY','BOARD_CIRCUIT','V2_EMC_SIPI',co]
 bp.append([CO[co]['company_name'],a['total_ads'],pn(a),pn(b),'小样本' if int(a['total_ads'])<10 else '样本点值'])
p(tab(['公司','任务广告数','Altium提及','电磁及完整性提及','解释级别'],bp))
p('这些公司沿用此前按广告覆盖选出的观察对象。Apptronik的Altium一般提及7条，但无条件只有1条，其余主要是工具示例或可替代选项；不能把7条都写成必须掌握Altium。自变量在该任务层未记Altium正例，也不表示不用EDA工具。星海图仅3条，应阅读具体职责，不能据比例推公司技术路线。')
p(cite('tables/V3_two_layer_aggregates.csv','tables/V3_two_layer_company_points.csv','tables/V3_two_layer_evidence.csv','tables/Q4_task_company_points_final.csv'))
p('## 八 哪些结论对分析选择敏感')
p(tab(['任务与条目','主任务','加次任务','职责模板去重','去实习校招'],[[task_names[t]+' '+L['PRIMARY',t,c]['label_name'],*[pn(L[s,t,c])+' '+pct(L[s,t,c]['share_ad_weighted']) for s in ['PRIMARY','PLUS_SECONDARY','DEDUP_PRIMARY','NO_CAMPUS_PRIMARY']]] for t,c in [('ROBOT_MODEL','SK_PYTHON'),('ROBOT_RUNTIME','SK_CPP'),('BOARD_CIRCUIT','SK_ALTIUM'),('BOARD_CIRCUIT','V2_EMC_SIPI')]]))
p('在这些预定情景下，运行软件C++的高提及保持；板级电路Altium比例有所变化，不能将一个点值视为固定总体参数。职责模板去重仅在同公司同职能、职责文本归一空白后完全相同时保留一条；不同资格和不同岗位ID仍可能真实存在，因此它是敏感性方案，不替代主样本。去校招实习只排除明示受众，不把没写年限当成应届或有经验岗位。')
lr=[]
for t,c in [('ROBOT_MODEL','SK_PYTHON'),('ROBOT_RUNTIME','SK_CPP'),('BOARD_CIRCUIT','SK_ALTIUM'),('BOARD_CIRCUIT','V2_EMC_SIPI')]:
 xs=[x for x in loo if x['task']==t and x['label_code']==c];valid=[float(x['share_ad_weighted']) for x in xs if x['share_ad_weighted']]
 lr.append([task_names[t]+' '+L['PRIMARY',t,c]['label_name'],pct(min(valid))+'—'+pct(max(valid)),str(sum(x['gate']=='POINTS_ONLY' for x in xs)),pct(L['PRIMARY',t,c]['max_positive_contribution'])])
p(tab(['第一层提及指标','去一家公司的比例范围','失去门槛次数','最大公司正例贡献'],lr))
p('门槛与稳定性不同。例如部署与现场服务职能的Python一般无条件为11/78、U=6；去掉Field AI后为4/65，仍有17家有效公司，继续达到组门槛。广告加权由14.1%降至6.2%，公司等权由15.0%降至12.8%。应说它对单家公司广告贡献敏感，不能继续沿用“去掉Field后不能比较”的旧说法。这个职能不是前述已撤回的部署活动标签。')
p('### 责任边界的敏感性')
p('“参与、协助、共同开发”与独立承担在本版保留不同关系，但语言习惯不等于真实工作量。机器人模型层的基础模型/VLA本人职责提及54条；若把被编码为参与、协作或支持的联系也纳入，达到66条，多出12条。这个宽情景是联系上界，可能包括协作对象，不能直接解释为本人能力。报告同时保留两种数值，避免把严格责任规则造成的下降误读为研发消失。')
p('不同层次的界限不能互相替代：文本未知界限处理已识别U；来源方案处理文本可用性；去模板与去公司处理观察权重；责任宽情景处理关系定义。它们都不能证明没有未发现的语义错误，更不能替代外部独立验证。')
p(cite('tables/V3_two_layer_leave_one_company_out.csv','tables/V3_two_layer_membership.csv','tables/Q4_leave_one_company_out_final.csv','tables/Q4_dedup_membership.csv'))
p('## 九 对审核意见的采纳与最终验收')
p('本版采纳了审核中最影响研究成立的意见：把活动规则、具体记录与旧结论连起来；展示修订如何改变研究结论；说明任务分组独立于比较工具；完成原先未完成的复核队列；再把技术提及与要求方式分层比较。对“先缩小Q2发布范围”的建议，本轮依用户授权保留全17职能并完成预设工作，没有以缩小范围替代队列执行。')
p('原样本与主分类保持完成；合并裁决、84条对象研究、工程活动分解可进入综合主结果。部署活动相关实质结论已经撤回。Q2按340条全文抽样、1,208条强制边界队列和已知规则回查的范围完成内容收尾；全部17职能仍以探索性结果发表，不声称全部逐项双重验证。')
p('程序验收覆盖了4,402,134个状态格的独立重建、汇总与公司点值的独立矩阵复算，以及两层提及统计的独立SQL去重核验。SOURCE_EXCLUDED已在真实数据上物化，并检查特定条目、全适用条目、受影响语境和正例优先等路径。数值正确只保证当前编码被正确计算。')
p('局部来源限制涉及3条广告，证据冲突还可能影响单项判断。例如N1031的企业应用广告夹有制造和工装验证职责，受影响条目保留未知，未把它解释为已确认的跨职能能力。冻结输入909文件、原grok提交和旧Astra封存交付另有哈希保护检查；新稿与旧稿分别存放。')
p(cite('verification/V3_independent_state_resolution.json','verification/astra_independent_numeric.json','verification/V3_two_layer_independent_sql.json','verification/astra_isolated_reproduction.json','verification/V3_protected_inputs.json'))
p('## 十 当前进度与后续研究选择')
p('本轮授权的六步研究、M5规定复核与M6计算及报告交付均已完成。项目已具备一份可阅读、可追溯、可复算的综合研究稿。旧347条Astra首轮署名和grok4.6接续署名保留；本版复核、分析和报告署名Astra。')
p('仍未建立的是行业总体推断、真实招聘需求或人数测量、国家效应、业务模式因果效应和独立人工双编码。这些不是本报告已经做到的能力，也不应在下一轮简单通过增加图表补成。新增研究应由新问题决定。')
p('若继续使用现有数据，优先方向是把部署与维护重新定义为数字系统、物理样机、客户生产现场及持续运维责任，另立版本，系统回查正例和潜在漏例。这会修复一个明确的测量缺口；目前无需为此重开主职能分类。第二个可选方向是固定任务层后考察资历、模板和要求方式，但只在来源和样本允许时比较，不强行加入复杂回归。')
p('若扩公司，应先明确比较对象。当前整公司供给分组是整机产品18家、跨本体模型3家、运营服务1家和组件系统组合1家；后两类无法形成独立公司间的组内分布。要研究供给类型差异，应优先补这些稀缺类型，并统一公司或团队切分规则。要研究具身特色，则先设计相近非具身岗位对照。20加20可作为招募目标，但不是证明研究有效的条件。')
p('我最终保留的研究判断是：先识别岗位实际面对的工作，再比较它如何表达技术责任与资格。公司整体比例有描述价值，只有连同职能权重、任务对象、要求方式和未知边界一起看，才能得到有分寸的公司差异判断。')
p('## 附录一 全17职能覆盖与复核范围')
p('表内全文、边界、未选复核三列互斥，合计为全24主体该职能数量；整公司广告数另列。边界复核读取全部已编码或候选证据的相关段落、邻接语境和标题，未显示的正文不冒称已读。没有被本轮选中二次复核的347条仍保留首轮全文编码。')
rv={x['role']:x for x in review}
p(tab(['具体职能','全体广告','整公司广告','全文复核','边界复核','未选二次'],[[x['role_name'],x['all24_ads'],x['whole23_ads'],rv[x['role']]['full'],rv[x['role']]['boundary_only'],rv[x['role']]['not_selected']] for x in sorted(coverage,key=lambda x:-int(x['whole23_ads']))]))
p('总计：全体1,576，整公司1,552；全文469，边界760，未选二次347。全文样本含此前181条和本版新增288条；预设抽样与强制队列重叠，不能相加为1,548条独立复核。全文阅读还包含无常见关键词、非英语和局部来源问题的定向记录，不是随机准确率样本。')
p(cite('tables/V3_review_coverage_final.csv','verification/V3_review_progress.json'))
p('## 附录二 各职能的探索性指标入口')
p('下表每职能从具名工具、工程方法和操作资格中，按一般无条件正例数列最多两项，避免用职能定义本身制造高比例发现。它只是浏览入口；不同职能的清单不同，不能跨行排列技能含量。全部条目、语境、公司点值和证据见离线查询页。组比例门槛与公司小样本标记仍逐格适用。')
examples=[]
for cv in sorted(coverage,key=lambda x:-int(x['whole23_ads'])):
 cand=[x for key,x in main.items() if x['role']==cv['role'] and x['metric']=='GENERAL' and x['branch']=='UNCONDITIONAL' and x['measurement_type']!='TECHNICAL_CONCEPT' and not x['label_code'].startswith('SK_GENERIC') and x['label_code']!='SK_CAD' and int(x['P'])>0]
 picks=sorted(cand,key=lambda x:(-int(x['P']),x['label_code']))[:2]
 for x in picks:examples.append([cv['role_name'],x['label_name'],pn(x),x['U'],x['n_companies'],'组描述' if x['gate']=='EXPLORATORY_SUMMARY' else '仅公司点值'])
p(tab(['具体职能','一般无条件条目','P/N','U','有效公司','用途'],examples))
p('机器人操作与研究科学虽没有通过当前条目覆盖筛选的主图，也不应笼统称为完全不能做组比较。应查具体语境的N与有效公司数。机器人操作的作业安全应用属于另一职责语境；两种层次的相关安全标签不能相加成独立需求。')
p(cite('index.html','tables/Q4_aggregates_final.csv','tables/Q4_company_points_final.csv','tables/Q4_display_selection.csv'))
p('## 附录三 复算入口和结论追溯')
p('复算顺序和环境记录见README_REPRODUCE.md。它从冻结输入与已登记研究判断重新生成状态、17职能统计和三任务深化结果；不应重复执行register判读登记脚本。阅读ID用于查找，唯一身份始终包含数据集、公司、来源、岗位ID及正文版本。')
p('结论与有限公司解释分别由下列T6、T5表连接到原始证据和适用边界。主报告、Word和index.html为本版入口，旧稿保持封存；publication_manifest.json记录交付指纹。')
p(cite('README_REPRODUCE.md','tables/V3_T6_claims.csv','tables/V3_T5_company_interpretation.csv','publication_manifest.json'))
text='\n\n'.join(out)+'\n'
(ROOT/'REPORT_Astra_final.md').write_text(text,encoding='utf-8')
(ROOT/'REPORT.md').write_text(text,encoding='utf-8')
# Figure deliberately excludes the withdrawn deployment measure.
figdir=ROOT/'figures';figdir.mkdir(exist_ok=True)
fig,ax=plt.subplots(figsize=(8.2,3.7))
vals=[float(decm[k]) for k in ['delta_pp','composition_pp','within_role_pp']]
ax.barh(['总差','职能构成分量','职能内分量'],vals,color=['#203D57','#5C8898','#A86142']);ax.axvline(0,color='#aaa',lw=.7)
for i,v in enumerate(vals):ax.text(v+(.5 if v>0 else -.5),i,f'{v:+.2f}',va='center',ha='left' if v>0 else 'right',fontsize=11)
ax.set_xlim(-13,25);ax.set_xlabel('百分点　银河通用减Figure');ax.spines[['top','right']].set_visible(False);fig.tight_layout();fig.savefig(figdir/'V3_decomposition.png',dpi=180);plt.close(fig)
dump('tables/V3_T6_claims.csv',[
 dict(id='C1',status='RETAIN',claim='研究48/66与宽质量300/459在同名主职能外',source='R_cross_function.csv',limit='活动正例内部，非部门人数'),
 dict(id='C2',status='WITHDRAW',claim='264/343部署比例及部署分解不进入实质主结论',source='V3_activity_rule_record_claim.csv',limit='未重做全体部署测量'),
 dict(id='C3',status='RETAIN',claim='84条对象研究81条无明确产品归属',source='O4_attribution_seniority_unknown.csv',limit='四家公司有限案例'),
 dict(id='C4',status='RETAIN',claim='工程总差11.10=构成19.45+职能内负8.35百分点',source='D2_decomposition_summary.csv',limit='四共同职能；非因果；来源筛选NA'),
 dict(id='C5',status='EXPLORATORY',claim='机器人模型Python提及银河14/18与自变量10/21',source='V3_two_layer_company_points.csv',limit='当前样本与编码；不是实际需求规模'),
 dict(id='C6',status='EXPLORATORY',claim='运行软件C++两家公司提及14/16和9/10，严格格未知区间重叠',source='V3_two_layer_company_points.csv;Q4_task_company_points_final.csv',limit='不做公司技术需求排名'),
 dict(id='C7',status='EXPLORATORY',claim='板级Altium24/56、电磁及完整性36/56，表达方式不同',source='V3_two_layer_aggregates.csv',limit='示例任选不等于必备，部分公司小样本'),
 dict(id='C8',status='PASS_SPECIFIED_SCOPE',claim='预设340全文、1208强制复核完成，累计469全文760边界',source='Q3_review_receipts.csv',limit='非全样本二次全文、非独立双编码'),
 dict(id='C9',status='CORRECTED',claim='去Field后部署职能Python4/65，仍17家公司',source='Q4_leave_one_company_out_final.csv',limit='对公司贡献敏感但门槛仍通过')])
t5=read(ROOT/'tables/T5_Astra_final.csv')
t5.extend([dict(company_id='CN_XSQUARE',company='自变量',scope='机器人模型21；运行软件10；板级8',evidence='V3_two_layer_company_points.csv',judgment='Python模型提及10/21；运行软件C++9/10，不能从严格一般格排列需求高低。',product_boundary='未由公司代表产品补岗位归属',delivery_boundary='广告写法和任务范围有限'),dict(company_id='US_APPTRONIK',company='Apptronik',scope='板级12',evidence='V3_two_layer_company_points.csv',judgment='Altium7/12多为示例任选；电磁及完整性9/12，职责提及明显。',product_boundary='未给岗位补命名产品',delivery_boundary='不推出公司设计流程已经实施')])
dump('tables/V3_T5_company_interpretation.csv',t5)
save_json('reports/V3_report_data.json',dict(qc=qc,impact=impact,selected_two_layers=[L['PRIMARY',t,c] for t,c in focus],company_examples=comp,board_examples=bp,loo_examples=lr,role_examples=examples))
print('Report written',len(text),'characters')
