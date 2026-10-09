from common import *
import sys
sys.path.insert(0,str(ROOT/'runtime'))
from datetime import datetime,timezone
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font=FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.rcParams['font.family']=font.get_name()
plt.rcParams['axes.unicode_minus']=False
data=json.loads((ROOT/'reports/final_report_data.json').read_text(encoding='utf-8'))
qc=data['qc'];cv=data['coverage']
M={'DUTY_OWN_USE':'本人职责 使用','DUTY_OWN_DEVELOP':'本人职责 开发','GENERAL':'一般要求','REQUIRED':'明确必备','PREFERRED':'优先条件'}
def pct(v):return '不汇总' if v in ['',None] else f'{float(v)*100:.2f}%'
def tab(head,rows):
 return '\n'.join(['|'+'|'.join(head)+'|','|'+'|'.join(['---']*len(head))+'|']+['|'+'|'.join(str(x).replace('|','／') for x in row)+'|' for row in rows])
def src(names):return '数据表：'+'；'.join('['+n+'](tables/'+n+')' for n in names)+'。'
out=[]
def p(s):out.append(s)
figdir=ROOT/'figures';figdir.mkdir(exist_ok=True)
# Four research figures, with units and scope stated in text.
sortedcv=sorted(cv,key=lambda a:int(a['whole23_ads']))
dump('figures/01_role_coverage.csv',sortedcv)
fig,ax=plt.subplots(figsize=(9,7.8))
ax.barh([a['role_name'] for a in sortedcv],[int(a['whole23_ads']) for a in sortedcv],color='#234E70')
for i,a in enumerate(sortedcv):ax.text(int(a['whole23_ads'])+2,i,a['whole23_ads'],va='center',fontsize=9)
ax.set_xlabel('公开广告条数');ax.set_title('17 个具体职能的整公司样本覆盖');ax.set_xlim(0,240);ax.spines[['top','right']].set_visible(False);fig.tight_layout()
fig.savefig(figdir/'01_role_coverage.png',dpi=180);plt.close(fig)
cross=[a for a in read(ROOT/'tables/R_cross_function.csv') if a['scope']=='WHOLE23']
dump('figures/02_activity_across_roles.csv',cross)
fig,ax=plt.subplots(figsize=(8,3.3))
an={'ACT_DEPLOYMENT':'部署与维护','ACT_QUALITY':'质量验证','ACT_RESEARCH':'研究探索'}
for i,a in enumerate(cross):
 ax.barh(i,100*float(a['P'])/float(a['N']),color='#234E70')
 ax.text(100*float(a['P'])/float(a['N'])+1,i,a['P']+'/'+a['N'],va='center')
ax.set_yticks(range(3),[an[a['activity']] for a in cross]);ax.set_xlim(0,100);ax.set_xlabel('该活动正例中位于同名主职能之外的比例 %');ax.spines[['top','right']].set_visible(False);fig.tight_layout();fig.savefig(figdir/'02_activity_across_roles.png',dpi=180);plt.close(fig)
dec=[a for a in read(ROOT/'tables/D2_decomposition_summary.csv') if a['case_id']=='D_MAIN' and a['scenario']=='MAIN' and a['mode']=='FIXED_K' and a['activity'] in ['ACT_ENGINEERING','ACT_DEPLOYMENT','ACT_QUALITY','ACT_RESEARCH']]
dump('figures/03_decomposition.csv',dec)
fig,ax=plt.subplots(figsize=(8,4.2))
for i,a in enumerate(dec):
 for j,(k,c,lab) in enumerate([('delta_pp','#1B365D','总差'),('composition_pp','#5599AA','构成分量'),('within_role_pp','#B76E47','职能内分量')]):
  v=float(a[k]);ax.barh(i+(j-1)*.23,v,height=.2,color=c,label=lab if i==0 else None)
  ax.text(v+(.4 if v>=0 else -.4),i+(j-1)*.23,f'{v:+.2f}',ha='left' if v>=0 else 'right',va='center',fontsize=8)
ax.axvline(0,color='#888',lw=.6);ax.set_yticks(range(len(dec)),[{'ACT_ENGINEERING':'工程实现',**an}[a['activity']] for a in dec]);ax.set_xlim(-19,25);ax.set_xlabel('银河通用减 Figure 百分点');ax.legend(loc='lower right',frameon=False);ax.spines[['top','right']].set_visible(False);fig.tight_layout();fig.savefig(figdir/'03_decomposition.png',dpi=180);plt.close(fig)
keys=[a for a in data['sensitivity'] if a['scope']=='WHOLE23' and a['label_code'] in ['SK_CPP','SK_PYTHON','SK_LINUX']]
dump('figures/04_unknown_bounds.csv',keys)
fig,ax=plt.subplots(figsize=(8,4))
for i,a in enumerate(keys):
 lo=100*float(a['unknown_low_ad']);hi=100*float(a['unknown_high_ad']);v=100*float(a['share_ad_weighted'])
 ax.plot([lo,hi],[i,i],lw=5,color='#85AFC1',solid_capstyle='round');ax.scatter([v],[i],color='#1B365D',s=30,zorder=3)
 ax.text(hi+1,i,f"P/N={a['P']}/{a['N']}  U={a['U']}",va='center',fontsize=8)
ax.set_yticks(range(len(keys)),[RN[a['role']]+' '+a['label_name'] for a in keys]);ax.set_xlim(0,90);ax.set_xlabel('一般要求 无条件 广告加权比例 %');ax.spines[['top','right']].set_visible(False);fig.tight_layout();fig.savefig(figdir/'04_unknown_bounds.png',dpi=180);plt.close(fig)

p('# 具身智能公开招聘研究最终综合报告')
p('作者 Astra　｜　2026年9月17日　｜　冻结样本研究与Q2全职能拓展')
p('本报告汇总三份阶段D研究的合并裁决、工作对象分析、公司差异算术分解，以及Q2拓展到17个具体职能后的研究结果。核心结论是：招聘文本中的工作差异同时存在于职能构成、同职能内部的任务对象，以及技术和工具的要求语境。公司产品与业务资料能限定解释，但当前证据不足以把这些差异归因于国家或业务模式。')
p('**交付状态：综合研究报告和全范围统计已经形成；Q2内容验收仍未完成。** 1,576条首轮编码由前序Astra与grok4.6共同形成。本轮Astra实际完成162条全文复核、725项修订记录；预设340条抽样中完成93条，1,208条强制复核队列中完成142条。下文Q2全样本比例应理解为当前修订编码的探索性描述，不能标成“全部内容已经复核通过”。这项限制不同于已经通过的数值复算。')
p('## 一 主要研究判断')
p('第一，职能名称不能替代活动分析。研究探索、部署与维护、质量验证的大多数正例位于同名主职能之外。同一广告可以承担多个活动；按主职能计数会漏掉其他岗位中的相关工作。')
p('第二，同一主职能内部存在实质不同的工作对象。84条对象研究中，81条无法归属明确命名产品或项目。ML岗位可能开发模型、建设训练系统或组织数据；软件岗位可能交付机器人运行软件、开发工具或履单业务后台。无法将公司所有广告统一归到其代表产品。')
p('第三，公司总体比例差异必须同时考虑招聘职能的权重。在银河通用与Figure的四个共同职能内，工程活动差为+11.10个百分点，构成分量+19.45、职能内分量−8.35。两部分方向相反；因此，不能说“差异几乎全部由构成解释”，更不能改写为业务模式贡献率。')
p('第四，Q2扩展有价值，尤其补入硬件、制造质量供应链、机械、数据、商业和支持岗位的方法与工具。但“扩展至17类”不等于“17类都能做相同深度的组比较”。5个预设任务层在当前样本下不满足20条可判断广告的最低门槛；不少公司点值也小于10条。')
p('第五，当前最优先的下一步是完成现有编码的针对性复核和规则一致性回查。立即补齐20家加20家不会修复已有语义误判。若未来问题明确转向企业总体或某类供给方式，应另建分层样本框；新增公司不是本轮报告成立的必要条件。')
p('## 二 研究范围与计量方法')
p(tab(['范围','广告数','用途'],[['冻结认可研究总体','1,654','24个招聘主体；公开广告，不是人数'],['整公司主范围','1,630','23家公司；Amazon FAR团队24条单列'],['Q2全体具体职能','1,576','17类；其余78条不强制归入单职能'],['Q2整公司主范围','1,552','本报告各职能主表分母起点'],['方向一固定框','84','4家公司；ML 44条，软件40条']]))
p('原始观察来自不同采集日期，主要包括2026年8月31日及9月11日。公司归属、招聘地点、发布语言和供给类型分别记录；它们不能相互替代。固定样本的覆盖也不等于公司全部在招职位。FAR只有团队范围，不能与整公司招聘结构直接等量比较。')
p('Q2沿用冻结Q2-v2.1目录，共354项；每个职能有自己的适用清单。原14个语境格继续保留，另补8个职责分支格，避免把“使用例如某工具”硬写成无条件使用。技术概念、具名工具协议、专业方法、资格与操作方法分别统计；目录外词保留记录，不临时扩项。')
p('P为明确正例；Z为当前判读中来源可读而该格未记正例；U为影响该项和语境的未解关系；NA为不适用；SOURCE_EXCLUDED为来源不足以评估该格。Z继承首轮全文判读，不能理解为所有广告都已由本轮Astra重读。N=P+Z，B=P+Z+U。主比例P/N排除U；未知赋值界限为P/B至(P+U)/B。来源排除与NA不进入B。')
p('公司等权比例先求各公司的P/N，再对N>0的公司求平均；广告加权比例是合计P除以合计N。前者回答所见公司的平均写法，后者更受广告多的公司影响。每个组格须有至少3家公司且合计N≥20才报告组比例；公司0<N<10标为小样本，N=0保留缺失。')
p('主图筛选要求某标签在任一本人职责或要求语境中覆盖至少5家公司、10条广告，每种测量类型最多8项；该筛选只控制展示数量，与3家公司加20条的组比较门槛分开。不同语境和标签可在同一广告中并存，比例不得相加成100%。未知赋值区间是文本歧义的敏感性范围，不是置信区间，也不包括潜在编码错误。')
p(src(['Q4_scope_definitions.csv','Q4_role_coverage_final.csv','Q3_review_receipts.csv']))
p('## 三 职能构成与跨职能活动')
p('制造质量供应链、软件与平台、ML、公司支持和硬件占据较大的广告量；这种构成描述的是所见岗位文本。广告数不提供员工存量、实际招录人数或研发预算，不能直接判断公司技术投入规模。')
p('![图1 整公司主范围17职能广告覆盖](figures/01_role_coverage.png)')
p('图1　主范围共1,552条具体职能广告。公司数和FAR增量见第六节完整覆盖表；主职能已经冻结，本轮没有重做分类。')
p('![图2 活动跨职能分布](figures/02_activity_across_roles.png)')
p(tab(['活动','同名职能之外 P/N','比例','明确的解释边界'],[[an[a['activity']],a['P']+'/'+a['N'],pct(a['ad_weighted']),'活动正例内部的分布，不是全体广告的活动发生率'] for a in cross]))
p('图2和表中，部署与维护包含模型部署、平台维护及机器人现场工作；质量验证也包含安全合规等任务。原阶段D部分文本将它们缩写为客户现场部署或制造质量，现予更正。对主职能不清楚的少量广告采用保守归属时，部署之外比例为76.09%，质量之外为64.49%，两项仍超过一半。')
p('同一广告中明确共同承担的活动也支持“工作组合”的观察：研究与工程65/1,599，工程与质量301/1,599，工程与部署维护235/1,599。三个分母均为整公司活动可判断广告，不能把这些共同承担率解释为部门协作率。')
p(src(['R_cross_function.csv','R_joint_summary.csv','R_role_activity_bidirectional.csv']))
p('## 四 工作对象深化分析')
p('方向一完整阅读固定四公司两职能的84条广告，保留对象多值及本人承担和参与的差别。AgiBot 19条、Galbot 49条、Dexterity 7条、Nimble 9条。它提供的是有限公司案例，而非四个独立的行业样本。')
p(tab(['公司','ML 模型或策略','ML 数据资产','软件 机器人运行','软件 履单业务'],[['智元','12/12','4/12','4/7','0/7'],['银河通用','22/24','12/24','19/25','0/25'],['Dexterity','5/5','3/5','0/2','0/2'],['Nimble','3/3','3/3','4/6','2/6']]))
p('模型岗位不能统一称为纯研究。银河通用的模型、数据、真机相关对象常同时出现；智元还涉及多模态交互、推理延迟和端侧资源。Nimble三条ML均涉及数据，但三条不足以支持公司层面稳定比例。机器人或物理现场对象包含样机与实验室，不能全部解释为客户生产部署。')
p('软件职能的任务异质性更明显。Nimble存在履单业务软件和WMS接口；其中Cloud Logistics广告明示无需机器人或物流经验。Dexterity两条软件主类分别涉及基础设施以及PLM/BOM/ECO文控。这些广告不能被放进同一“机器人算法软件”篮子比较工具优劣。')
p('仅3/84条直接指向记录中的命名产品、平台或业务线，其余81条维持未知。前序留存的使用方或共同开发方材料可支持部分产品场景与交付状态，但不能据此将G2、S1或Mech归给所有相关公司岗位，也不证明付款、持续维护或完整责任链。')
p('经验年限明示39条、未明示45条。学位、同等经历、不同年限路径及优先条件按原文保存，没有将未写年限的广告统一当作初级或资深。对象表的敏感性覆盖明确校招实习、完全一致职责文本、明示产品与明示年限；仅明示产品时多数公司职能格无法计算，这本身就是归属证据不足的结果。')
p(src(['O4_company_role_object.csv','O4_sensitivity.csv','O4_attribution_seniority_unknown.csv','O3_skill_task_links.csv']))
p('## 五 公司差异的算术分解')
p('主比较固定为银河通用减Figure，共同职能为公司支持、制造质量供应链、ML、软件。双方各共同职能的活动可读广告不少于10条；共同范围覆盖银河通用82/181=45.30%，Figure 60/126=47.62%。K以外广告仍保留，但不能把K内结论推广到全公司。')
p('分解把总体差分成两项：一项让两公司采用相同的平均职能内活动率，只改变招聘职能份额；另一项让两公司采用相同的平均职能份额，只改变职能内活动率。两项相加严格等于总体差。它是描述性算术，未控制公司年龄、招聘渠道、广告模板或岗位资历。')
p('![图3 固定共同职能范围的公司差异分解](figures/03_decomposition.png)')
p(tab(['活动','总差 百分点','构成分量','职能内分量'],[[{'ACT_ENGINEERING':'工程实现',**an}[a['activity']]]+[f'{float(a[k]):+.2f}' for k in ['delta_pp','composition_pp','within_role_pp']] for a in dec]))
p('银河通用K内的ML与软件份额较高，而这两个职能的工程活动率较高，形成正向构成分量；但Figure在这四个职能内的工程活动率都更高，形成反向的职能内分量。换成四职能等权，工程率成为47.58%与56.74%。这说明权重会影响总体比较方向，不能据原总率给公司能力排名。')
p('工程总差在剔除明确校招实习或应届受众后为+10.56个百分点，在职责文本完全一致去重后为+12.89，构成正、职能内负的方向保留。三个来源筛选都会排除银河通用，固定K出现零分母，故结果为NA；不能把缺少一方的结果写成稳健性通过。智元与银河通用仅两个共同职能，且只有ML是技术职能，应保留为有限补充。')
p(src(['D2_decomposition_summary.csv','D2_decomposition_role_parts.csv','D3_standardization_sensitivity.csv','D1_all_pair_qualification.csv']))
p('## 六 Q2拓展研究覆盖与结果')
p('### 6 1 全部17职能的覆盖')
p('表中“本轮复核”指实际有全文复读和判读记录的广告数，包含FAR；其他列另有注明。首轮编码覆盖全部1,576条；本轮162条复核不是一个可用于估计准确率的随机样本，包含种子抽样、无关键词广告及问题定向回查。')
p(tab(['具体职能','全24主体广告','整公司广告','整公司数','本轮复核'],[[a['role_name'],a['all24_ads'],a['whole23_ads'],a['whole23_companies'],a['full_review_ads']] for a in sorted(cv,key=lambda a:-int(a['whole23_ads']))]))
p('完整覆盖使研究不再局限于学习模型与运行软件。下列各职能首先列当前编码中覆盖较多的两个不同标签及其无条件语境，再解释应如何比较。条目选择按展示规则后的正例数排序，不能当作预先指定的差异检验；原始全项、全语境和零值在查询页及CSV中保留。')
comments={
'RF_COMMERCIAL_CUSTOMER':'销售、营销、客户成功是不同任务。销售任务层中客户经营一般要求26/58，而整个职能是27/117；差别首先反映子任务构成，不能据总职能工具出现率评价销售专业程度。',
'RF_CONTROL_PLANNING':'经典控制、强化学习控制、移动导航与车队规划并存。一般控制闭环51/75来自当前修订编码；预设足式与全身控制任务仅19条，不作组比例。控制岗位中的仿真器示例不应被写成全部必备。',
'RF_CORPORATE_SUPPORT':'招聘、人力、财税、法务、内部IT具有不同方法。进入HR任务层后，招聘与人力一般要求为27/34；总职能27/132的低值主要不能解释为缺少HR能力。西语和葡语广告也需要全文判读，英文关键词未命中不等于无方法。',
'RF_DATA_INFRA_OPERATIONS':'数据管线开发与机器人操作员采集分开；同一岗位可以涉及评测或质量管理。数据管线任务层Python一般要求15/27、另有3条未知，说明缩窄任务后工具分布和分母都会改变。',
'RF_DEPLOYMENT_FIELD_SERVICE':'安装调试、在役排障、培训与物流备件不能互相替代。Python一般要求11/78中Field AI贡献7条；该工具不是所有现场服务工作的共同核心。事故支持标签也应限定到真正运行期语境。',
'RF_HARDWARE_ELECTRICAL':'板级电路、嵌入式、传感器、电源和验证工作并不相同。评测是重要的职责对象，但执行仪表测试不同于开发仪表或测试方法。板级电路预设任务51条，适合继续比较EDA、PCB和测量语境；本轮内容复核覆盖不足限制了正式结论。',
'RF_INDUSTRIAL_EXPERIENCE_DESIGN':'23条已全文复核，工业外观与CMF、体验研究和视觉内容应分开。预设工业CMF任务11条，仅保留点值。工具熟悉、可提交作品集和本人设计交付具有不同证据意义，不能把展示平台名称当成开发工具。',
'RF_MANUFACTURING_QUALITY_SUPPLY':'这是样本最多也最异质的职能。装配与工艺、硬件测试质量、软件数据测试、采购供应分别比较；职能总量不能代表制造部门规模。技术评审供应商或处理8D不自动成为采购商务流程，测试执行也不等于测试工具研发。',
'RF_MECHANICAL_MECHATRONICS':'机械结构是多数所见广告的交付对象，同时涉及测试、可靠性与设计工具。机构、执行器与热设计工作仍有区别。机器人结构预设任务54条可做局部探索；制造性、材料工艺和CAD选择应保持专业方法与具名工具的层次。',
'RF_ML_AI_ENGINEERING':'模型本体、训练推理系统、数据闭环是并存对象，不能合成为一种“算法岗位”。机器人模型预设任务Python一般要求40/90、U=16；C/C++等关系未解会改变分母与上下界。对具体软件栈强弱的公司排名缺少足够依据。',
'RF_PERCEPTION':'感知融合、定位建图、目标视觉和空间重建需要按任务比较。预设目标视觉16条未达组门槛。SLAM工具、Ceres/g2o等裸括号或斜线列举若关系不明，应保留未知；不能把三维资产建模全部解释为算法式场景重建。',
'RF_PRODUCT_PROGRAM':'产品需求、项目管理和交付协调并不等于本人开发协调对象中的技术。技术名词少可能只是职责写法不同，不能推为技术能力低。预设机器人产品任务29条可作点值与探索性汇总，但现有方法标签边界仍需复核。',
'RF_RESEARCH_SCIENCE':'整公司23条，加入FAR后32条，范围变化对小职能尤其明显。研究科学已有可通过组门槛的具体语境，不能笼统说只有点值。研究问题、申请研究方向和协作领域不自动等于每个岗位亲自开发全部技术。',
'RF_ROBOTICS_SOFTWARE':'机器人运行软件、内部工具、基础设施与业务系统应拆开。运行软件任务Linux一般要求48/86，C++为36/63且U=24。同一工具在一般条件、明确必备和优先项中的不同写法，需要与任务及招聘模板一起解释。',
'RF_ROBOT_OPERATIONS':'22条已全文复核，作业安全应用21/22；操作交付可体现为演示采集、运行监视或具体流程，而不一定列编程语言。数据演示任务仅8条，不能发布组均值；处理已有动捕数据的算法研发也不是操作员采集。',
'RF_SIMULATION_EVALUATION':'仿真平台、评测体系、测量工具与实际测试执行并不相同。仿真平台预设任务24条具有有限探索空间；Python、仿真器、计量方法须分别辨认。不能把所有标为评测的职责都算成工具链研发。',
'RF_SYSTEMS_ENGINEERING_INTEGRATION':'系统集成主要连接需求、接口、验收和运行问题。整机任务13条仅保留点值。Jama配置属于使用，平台健康维护和开发期调试也应分开；同一团队出现机械、电气、软件字样不能推为个人开发全部模块。'}
for i,a in enumerate(sorted(cv,key=lambda a:-int(a['whole23_ads']))):
 r=a['role'];p('### 6 '+str(i+2)+' '+a['role_name'])
 seen=set();rows=[]
 for x in data['tops'][r]:
  if x['label_code'] in seen:continue
  seen.add(x['label_code']);rows.append([x['label_name'],M[x['metric']],x['P']+'/'+x['N'],x['U'],pct(x['share_company_equal'])])
  if len(rows)==2:break
 p(tab(['当前编码条目','语境','P/N','U','公司等权'],rows))
 p(comments[r])
p('### 6 19 同任务中的公司点值')
p('以下公司来自事前覆盖排序的指定名单，没有按差异最大者选例。展示一般要求且无条件的语境。表中所有公司都是当前编码的描述；N<10的点不得当作稳定公司估计。')
points=read(ROOT/'tables/Q5_prefixed_company_examples.csv')
points=[a for a in points if a['role'] in ['RF_ML_AI_ENGINEERING','RF_ROBOTICS_SOFTWARE']]
p(tab(['任务与工具','公司','P/N','U','小样本'],[[('机器人模型 ' if a['role']=='RF_ML_AI_ENGINEERING' else '运行软件 ')+a['label_name'],a['company_name'],a['P']+'/'+a['N'],a['U'],'是' if a['small_n']=='YES' else '否'] for a in points]))
p('银河通用和自变量在机器人模型Python一般要求中分别为12/16与3/14，同时未知为2与7。运行软件C++中自变量3/4看似很高，但其基础范围10条中有6条未知；按基础范围赋值的上下界为30%至90%。只看75%的可判断点值会掩盖信息不足。')
p('即使公司点值达到10条，同任务也只是提高了可比性，并未控制资历、地点、工具替代关系或广告重复。不同广告模板的必备/一般/优先写法也会影响某一个语境的比例，不能用单格给公司技术能力排序。')
p(src(['Q4_aggregates_final.csv','Q4_company_points_final.csv','Q4_task_strata_final.csv','Q4_task_company_points_final.csv','Q5_prefixed_company_examples.csv']))
p('## 七 敏感性分析与结论边界')
p('### 7 1 来源 范围与招聘受众')
p(tab(['方案','Q2广告数','公司数','解释'],[[a['scope'],a['ads'],a['companies'],a['note']] for a in data['scopes'] if a['scope'] in ['WHOLE23','ALL24','FAR','S1_ACTIVITY_COMPLETE','S2_SOURCE_QUALITY','S3_SOURCE_QUALITY_LENGTH200','EXCLUDE_EXPLICIT_CAMPUS_INTERN','DEDUPE_EXACT_DUTIES']]))
p('剔除明确校招实习或接受应届者后剩1,430条；同公司同职能职责文本归一空白后完全一致的模板敏感性剩1,501条。后者有些要求段不同，故只作为模板权重检查，不宣称删除了错误重复职位。S1—S3同时改变公司组成、来源质量和可读范围，不能把结果变化仅归因于文本长短。')
senskeys=[('RF_ML_AI_ENGINEERING','SK_PYTHON'),('RF_ROBOTICS_SOFTWARE','SK_LINUX'),('RF_HARDWARE_ELECTRICAL','TC_EMBEDDED')]
lookup={(a['scope'],a['role'],a['label_code']):a for a in data['sensitivity']}
srows=[]
for rr,cc in senskeys:
 a=lookup['WHOLE23',rr,cc];row=[RN[rr]+' '+a['label_name']]
 for sc in ['WHOLE23','EXCLUDE_EXPLICIT_CAMPUS_INTERN','DEDUPE_EXACT_DUTIES','S2_SOURCE_QUALITY']:
  b=lookup[sc,rr,cc];row.append(b['P']+'/'+b['N']+' '+pct(b['share_ad_weighted']))
 srows.append(row)
p(tab(['一般要求 无条件','主范围','剔除明确受众','模板去重','来源S2'],srows))
p('ML的Python和软件Linux在两项局部剔除中数值接近主范围，但来源S2的软件Linux降至12/61。这限制了“跨采集来源稳定”的措辞。不同筛选方案不是独立重复样本，也不能把相近数值当成语义编码已经正确的证明。')
p('供给类型亦按冻结分层重算：跨本体模型组3家公司、194条Q2广告；机器人运营服务组只有1家、33条；组件系统组合组只有1家、122条。后两组无法支持公司层面的组比较。整机产品组18家、1,203条与小组极不均衡，不能从组间均值推出业务模式效应。')
p('7类公司场景分别计算“当前联系”与有观察使用的子集；公司可属于多个场景。研究教育的使用子集包含研究使用，其他场景也可能包含捐赠，不能统一叫商业销售。家庭场景的观察使用子集在该冻结矩阵中为零，只表示本矩阵没有对应状态，并不证明不存在家庭使用。')
p('### 7 2 未知关系与单家公司贡献')
p('![图4 一般要求的文本未知赋值界限](figures/04_unknown_bounds.png)')
p('图4　横线为U全部不成立至全部成立的界限，圆点为可判断广告P/N。区间不是抽样置信区间，也不包含尚未发现的误判或漏判。C++的区间明显宽于Linux，主要提示斜线或关系未解对解释的限制。')
p(tab(['整公司一般要求','P/N','U','未知赋值界限'],[[RN[a['role']]+' '+a['label_name'],a['P']+'/'+a['N'],a['U'],pct(a['unknown_low_ad'])+'—'+pct(a['unknown_high_ad'])] for a in keys]))
p('部署现场Python的11条正例有7条来自Field AI。移除该公司后，P/N由11/78变为4/65，广告加权比例14.10%降至6.15%，公司等权15.03%降至12.75%；仍有17家有效公司，仍通过3家加20条门槛。原grok“去掉后组门槛不成立”的结论撤回。正确判断是正例集中且广告加权值敏感，不能混同为失去比较资格。')
p('本轮对展示标签的22种语境逐家公司剔除，输出100,166行。正例最大贡献与分母最大贡献分别记录，所有并列保留。研究科学和机器人操作的主图筛选与组许可也已重新分开；小样本职能可以有部分合格格，不能对整个职能一概批准或禁止。')
p(src(['Q4_leave_one_company_out_final.csv','Q4_scope_definitions.csv','Q4_dedup_membership.csv','Q4_display_selection.csv']))
p('## 八 对grok接续成果的验收判断')
p('grok接续工作完成了全范围首轮编码和大量可定位引文，具有可继续利用的研究价值；原“M0—M6均COMPLETE”不能作为独立验收结论。引文位置匹配只证明文字存在，不能证明要求强度、分支关系和本人责任判读正确。')
p(tab(['发现的问题','本轮处理','当前结论'],[
 ['同任务分母未扣未知','从逐格P Z U状态重算任务和公司表','计算修复'],
 ['小样本标记误用基础B','统一按实际可判断N判断','计算修复'],
 ['主图筛选与组比较门槛混同','分开5家10正例展示与3家20可判断广告许可','解释修复'],
 ['Field AI剔除后资格表述错误','重算4/65及17有效公司','原结论撤回'],
 ['SOURCE_EXCLUDED未物化','对N0528加分段截尾按语境排除，保留可见正例','路径实现；未做全库截尾普查'],
 ['优先 一般 必备及职责对象误判','实际162条全文复核并保留725项修订','已有修复；全队列未完成'],
 ['抽样与强制复核用队列成员代替证据','仅实际阅读记录记为本轮已复核','93/340及142/1208'],
 ['敏感性只列名称未全计算','来源 受众 模板 供给 场景 直接覆盖 未知及剔除重算','统计交付；编码仍有质量限制'],
 ['隔离复算不充分','采用物理复制与完整结果哈希比较','见本轮verification记录']]))
p('本轮重点纠正的实例包括：N0988的Jama配置属于使用，Desired项目归优先；N0983轨迹优化属于Nice to Have；E0583控制岗位属于PI，原注释中的Apptronik为误名；N0528的加分段截尾使未出现项不能一概归零。机器人操作、工业与体验设计两个小职能全部复核，其余职能覆盖不均。')
p('原347条Astra首轮署名与grok首轮署名保持不变。本轮Astra复读自身首轮是同模型再读，复读grok判读是跨模型复核；二者均不等于人工独立双编码或盲审。没有发布准确率、Cohen kappa或“零错误”内容质量声明。')
p('数值层面，独立NumPy矩阵实现未调用主统计函数，对4,402,134状态格及六类汇总表进行了52,921,096次数值核对，未发现差异。此结果只验证计算与当前状态表一致。完整输入锁909份保持通过；原grok送审包保持原样。')
p('## 九 最终研究结论与后续方向')
p('可以保留的研究结论是：公开招聘中的组织分工需要用职能、活动、工作对象和要求语境共同描述；总比例与职能内比例回答不同问题；部分公司案例具有相反方向的构成与职能内分量；产品归属和交付责任的证据缺口明显。以上判断比单纯罗列软件工具更接近项目的原始问题。')
p('Q2拓展已经展示了新增职能的分析价值，并提供完整比较数据，但当前尚不足以发布全17职能的正式公司排行榜、国家差异解释或业务模式贡献率。尤其是语义复核覆盖较少的硬件、制造、软件、ML等大职能，现有数字应作为待复核的探索结果。不能利用数百万状态格的规模掩盖内容验证不足。')
p('接下来的第一优先级仍在现有数据内：完成剩余247条预设抽样和1,066条强制复核队列的实际核对，两个队列互相重叠，不能相加当成新的广告数；将本轮发现的标题强度、裸列表关系、协作对象、运行排障和供应商流程边界回查到所有受影响记录。随后重算，不更改冻结主分类。')
p('第二优先级是在质量收口后，继续分析“要求方式本身”的差异：同一技术写在必备、一般、优先或职责中的比例，及这种差异对公司点值的影响。可在已冻结任务层里研究工具与任务的共同出现，但应事先固定比较项，控制重复模板和少数公司贡献，避免从海量格中挑最大差异。')
p('新增公司应服务明确的新研究问题。如果研究目标仍是解释这24个主体的现有广告，暂不补到20加20；如果转向供给类型比较，优先增加目前只有一家公司的运营服务、组件系统等层，而不是只凑国家数量。届时需统一观察窗口、可采范围、公司定义与职能覆盖，作为新样本版本，不回填进本轮冻结结果。')
p('## 十 当前项目进度与交付')
p(tab(['工作','状态','剩余工作'],[['冻结数据 分类 阶段C','保留完成','本轮不重做'],['三稿合并裁决 R','完成','保留16项裁决及边界'],['方向一 工作对象 O','完成','产品归属缺口是研究限制'],['方向二 算术分解 D','完成','不能升级为因果解释'],['Q2全17职能首轮与统计','已完成全范围计算','结果以当前判读为条件'],['Q2内容质量验收 M5','尚未完成','抽样与强制语义复核未达到研究书要求'],['综合报告及复算交付 M6','本轮报告已形成','正式最终验收仍依赖M5内容收口']]))
p('因此，本报告是本轮工作的最终综合研究交付，项目总体不能登记为“全部验收完成”。研究输出已经可读、可追溯、可复算；正式验收的主要剩余工作集中在Q2内容质量，而非扩公司、恢复采集或重新分类。')
p('### 10 1 阅读与追溯入口')
p('主文从REPORT_Astra_final.md阅读；index.html提供17职能逐项查询。tables目录包含全部公司点值、任务层、敏感性、复核收据和变更台账。review/astra_reviews.jsonl保存每次实际判读理由及原始字段哈希，configs保持冻结目录，scripts保留复算入口。')
p('主要来源索引：')
p(tab(['研究部分','证据或结果表'],[['冻结公司与广告','inputs/stage_c/tables/T1_company_sample.csv；inputs/accepted_jobs.jsonl'],['合并裁决','R1_discrepancy_ledger.csv；R2_adjudication.csv；R_T6_claim_mapping.csv'],['活动与共同承担','R_cross_function.csv；R_joint_summary.csv'],['对象及归属','O2_evidence_long.csv；O2_object_states.csv；O4_company_role_object.csv'],['分解及敏感性','D2_decomposition_summary.csv；D3_standardization_sensitivity.csv'],['Q2证据与质量','Q3_evidence_final.csv；Q3_review_receipts.csv；Q3_astra_changes.csv'],['Q2完整统计','Q4_aggregates_final.csv；Q4_company_points_final.csv；Q4_task_strata_final.csv'],['核验','verification/astra_independent_numeric.json；verification/astra_isolated_reproduction.json']]))
p('署名说明：综合判断、返修统计和本轮报告为Astra；前序grok4.6与Astra首轮编码身份在数据中分别保留。报告中的公司业务背景继承冻结证据，不宣称已重新核验至本报告日期。')
content='\n\n'.join(out)+'\n'
num=json.loads((ROOT/'verification/astra_independent_numeric.json').read_text(encoding='utf-8'))
calc=json.loads((ROOT/'verification/astra_comparison.json').read_text(encoding='utf-8'))
replacements={
 '162条':str(qc['reviewed_full'])+'条',
 '725项':str(qc['changes'])+'项',
 '93条':str(qc['seeded_full_reviewed'])+'条',
 '142条':str(qc['mandatory_reviewed'])+'条',
 '93/340':str(qc['seeded_full_reviewed'])+'/340',
 '142/1208':str(qc['mandatory_reviewed'])+'/1208',
 '247条':str(340-qc['seeded_full_reviewed'])+'条',
 '1,066条':format(1208-qc['mandatory_reviewed'],',')+'条',
 '52,921,096':format(num['scalar_checks'],','),
 '100,166':format(calc['loo'],',')}
for a,b in replacements.items():content=content.replace(a,b)
(ROOT/'REPORT_Astra_final.md').write_text(content,encoding='utf-8')
save_json('verification/report_build.json',dict(author='Astra',created_utc=datetime.now(timezone.utc).isoformat(),characters=sum(map(len,out)),sections=len(out),qc_complete=False,inputs_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'reports/final_report_data.json',ROOT/'tables/Q3_review_receipts.csv',ROOT/'tables/Q4_aggregates_final.csv',ROOT/'tables/Q4_task_strata_final.csv']}))
print('Report built',sum(map(len,out)),'characters')
