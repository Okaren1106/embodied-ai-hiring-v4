from astra_review_tools import *
ids=['N0962','E0516','N0902']
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for r in ids}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def add(r,c,m,b,q,why,**v):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why,**v))
R['N0962']['judgment']='FAR合成数据工具链是本人交付，基础模型是下游训练对象。USD职责e.g为例示；优先工具e.g不能改成任选。明确仿真到真实数据需求但本人是否执行迁移方法仍不明。'
ov('N0962','N0962:1:0','e.g明确例示。',branch='EXAMPLE')
ov('N0962','N0962:4:0','与研究者确定数据质量用于迁移，不充分确认本人执行迁移方法。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
ov('N0962','N0962:7:0','Preferred下裸括号USD/OpenVDB无关系词。',metric='PREFERRED',branch='UNRESOLVED')
for e in ['N0962:10:0','N0962:10:1','N0962:10:2','N0962:10:3']:ov('N0962',e,'e.g工具例示，没有or。',branch='EXAMPLE')
R['E0516']['judgment']='量产EOL软件与自动测试本人研发，产线失败处理有运行语境。嵌入式栈冒号并列没有例示词；补明确校准软件方法开发，不把普通校准执行强加给研发岗位。'
ov('E0516','E0516:O3','冒号直接列举embedded stacks，和其余协议保持相同无条件关系。',branch='UNCONDITIONAL')
add('E0516','V2_CALIBRATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','our end of line software for programming, calibrating, and verifying subassemblies','本人编写维护执行编程校准验证的EOL软件。')
R['N0902']['judgment']='HIL框架研发、实物pick/pack测试和DAQ使用清楚。HIL经验明确strongly preferred；Jenkins e.g为例示。协议裸括号关系保持未知，CI运行维护另补职责。'
ov('N0902','N0902:9:0','HIL experience strongly preferred。',metric='PREFERRED')
ov('N0902','N0902:10:0','e.g Jenkins是示例。',branch='EXAMPLE')
for e in ['N0902:4:0','N0902:4:1','N0902:4:2','N0902:13:0','N0902:13:1','N0902:13:2']:ov('N0902',e,'协议裸括号未明确全部/例示/任选，保留关系未知。',branch='UNRESOLVED')
add('N0902','V2_CI_CD','DUTY_OWN_USE','UNCONDITIONAL','keep CI jobs on the HILs green','本人维护实际CI作业运行。')
register(list(R.values()),'Astra_sim_fullread_c')
