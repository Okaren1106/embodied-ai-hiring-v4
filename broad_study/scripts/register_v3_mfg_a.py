from astra_review_tools import *
judgments={
'E0259':'完整职责与要求已读。测试工站导入不等于本人开发可复用测试系统；有独立制造流程知识，不能因无新增工具命中漏掉工艺方法。',
'E0002':'量产结构转化任务成立。DFM/DFA本人采用明确；加工成型这个上位方法族本身被直接要求，不能因子工艺以等列举而把整个方法族降为例示。',
'N0517':'寻源、询比价、供应商引入本人责任明确；参与体系搭建与协同执行另列。采购流程要求及谈判证据足够，没有新增命名工具。',
'E0088':'完整冻结来源仅职责，无资格段但无截尾证据，不凭缺要求段判来源排除。自动化脚本编写支持本人开发评测工具，不能只记测试执行。',
'N0429':'根因分析本人责任、ISO9001一般要求和质量工具示例有据。DFX对象X未知仍保留；市场售后合作不替代本人客户服务。',
'N0382':'必备和加分段清晰，继承强度基本成立。Triton名称在推理框架中不足以确认GPU语言；保留U，不用工具子串解除。Shell与Python明确并列。',
'N0221':'完整回读整机测试、自动化框架、要求与加分。Python/LabVIEW斜线仍U；仪器一般要求与职责示例分开。经典控制与通信协议在上位概念后的括号是子例，不能统一当无条件；本人DFx评审输入不等于独立设计。',
'N0193':'完整回读NPI试产、工装协同、工艺输出与知识。操作规程的上位方法经验明确，括号里的工艺路线/指导书为其组成，不能把整个SOP经验降为示例。职责段熟悉板子加工与走线不是新的命名软件。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in judgments.items()}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('E0259','E0259:O1','测试工站导入与成熟度收敛说明本人应用测试，不证明本人开发测试工具。',metric='DUTY_OWN_USE')
add('E0088','TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','包括自动化测试脚本的编写和执行','本人编写测试脚本提供评测工具开发的明确证据。')
for eid in ['E0002:3:0','E0002:4:0']:
 ov('E0002',eid,'被列举的是加工成型方法族内部工艺，标签表示上位方法族，本身明确，不外推示例关系。',branch='UNCONDITIONAL')
ov('N0193','N0193:ADD3','工艺输出经验本身明确；括号给出同一上位SOP方法的组成，不使上位经验变成例示。',branch='UNCONDITIONAL')
for eid in ['N0221:5:0','N0221:5:1','N0221:5:2','N0221:5:3','N0221:5:4']:
 ov('N0221',eid,'通信协议和电机控制上位概念后括号列举具体方法/协议；无明确全部或任选，应保存例示。',branch='EXAMPLE')
register(list(R.values()),'Astra_v3_mfg_a')
