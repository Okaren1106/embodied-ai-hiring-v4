from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0220':'研发质量：问题关闭规则本人建立执行；8D/5Why/FMEA/APQP为跨方法斜线，等不能解除各项之间关系未知。',
'N0223':'关节工艺：职责段精通工艺是能力陈述；测试体系搭建另为评测开发，DFMEA/PFMEA/SOP跨类未知保留。',
'N0191':'实操支持：本人焊接加工明确；仅整理归档SOP不是执行或编制规程，配合输出仍是协作。',
'N0195':'软件质量：ROS与ROS2分别建类，裸斜线不当两项确定优先示例；CICD接入与优先经验分列。',
'N0225':'电气工艺：工艺方法使用与工艺流程开发有区别，必须具备处保留硬性；质量流程一般知识补录。',
'N0196':'软件产测：产测异常定位是测试调试，未明确运行事故恢复，不直接算运行支持；ROS和脚本斜线未知保留。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason=why))
for e in ['O1','O2','1:0','1:1']:ov('N0220',e,'跨方法斜线未说明全部、任选或仅部分举例；等不解除关系不清。',branch='UNRESOLVED')
for m in ['DUTY_OWN_DEVELOP','DUTY_OWN_USE']:add('N0220','V2_SOP_OPERATION',m,'UNCONDITIONAL',5,'明确建立与执行质量问题关闭规则。')
ov('N0223','2:0','精通全工序工艺为能力陈述，不由岗位职责标题变成本人实施。',metric='GENERAL')
add('N0223','TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',8,'明确本人搭建测试体系。')
ov('N0191','3:0','整理归档已有SOP资料，不证明执行或编制规程。',metric='SEPARATE',branch='DOCUMENTATION_OBJECT')
add('N0191','V2_CNC_PROCESS','DUTY_OWN_USE','UNCONDITIONAL',3,'明确本人焊接和组装方法实践。')
add('N0191','V2_CNC_PROCESS','GENERAL','UNCONDITIONAL',13,'明确焊接与组装实践能力。')
for e in ['O3','O4']:ov('N0195',e,'ROS/ROS2为两个冻结条目，裸斜线关系不清。',branch='UNRESOLVED')
add('N0225','V2_CNC_PROCESS','DUTY_OWN_USE','EXAMPLE',3,'对焊接等方法制定工艺流程，属于应用具体制造方法。')
add('N0225','V2_CNC_PROCESS','REQUIRED','EXAMPLE',23,'必须具备焊接加工等工艺实践。')
add('N0225','V2_CNC_PROCESS','GENERAL','EXAMPLE',27,'精通焊接加工等制造工艺。')
add('N0225','V2_SOP_OPERATION','GENERAL','UNCONDITIONAL',25,'明确工艺文件编制与质量控制流程知识。')
ov('N0196','ADD1','仅产测异常和试验工装需求联调，未明示运行中的事故工单或服务恢复。',metric='SEPARATE',branch='TEST_DEBUGGING')
register(list(R.values()),'Astra_v3_boundary_mfg_c')
