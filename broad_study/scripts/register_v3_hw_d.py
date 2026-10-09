from astra_review_tools import *
JUD={
'E0358':'主导架构、原理图和测试工装/软件开发明确，验证开发非只检查表。Bonus祖先任选与Jira局部esp示例共同保留；DFM/DFT协作独立。根因原文存在但硬件角色目录不覆盖，记缺口。',
'N0960':'固件FOC、实时保护和HIL环境本人开发明确；prototype bring-up仪器条款属于support，不提升独立本人使用。职责接口标准是需求工程应用。协议列表or similar同时任选和示例。',
'N0952':'整机电气与板卡设计兼有，以主任务电气架构保留；OrCAD/Allegro内部U而Cadence可替代明确。DFM/DFA同一方法类别可判；差分信号经验不等于信号完整性分析，另有EMI缓解知识证据保留。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[]) for r,j in JUD.items()}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
ov('E0358','E0358:6:0','Jira由esp.局部示例且承接one or more祖先任选，与相近E0329一致。',branch='CHOICE_AND_EXAMPLE')
for eid in ['N0960:O1','N0960:O2']:
 ov('N0960',eid,'Support rapid bring-up控制整个仪器使用句，未给本人独立仪器责任，保留协作。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for eid in ['N0960:14:0','N0960:14:1','N0960:14:2','N0960:14:3','N0960:14:4']:
 ov('N0960',eid,'协议为上位protocols后的括号例示且or similar明示替代，两个关系共同保留。',branch='CHOICE_AND_EXAMPLE')
ov('N0960','N0960:ADD4','本人定义接口标准、维护规范是需求工程方法应用，未证开发需求工程工具方法。',metric='DUTY_OWN_USE')
ov('N0952','N0952:21:0','DFM/DFA均属于冻结可制造可装配同一类别，类别存在可判，未强推分别全掌握。',branch='UNCONDITIONAL')
ov('N0952','N0952:ADD1','为传感器计算模块定义实现电气接口是需求工程应用，不是研发需求工程方法。',metric='DUTY_OWN_USE')
ov('N0952','N0952:ADD3','high-speed differential signaling经验未明示EMC/抗扰或完整性分析，不以相近对象补方法。',metric='SEPARATE',branch='SIGNALING_NOT_INTEGRITY')
R['E0358']['catalog_gap_notes']=[dict(code='V2_RCA',quote='Leading debugging efforts and root cause analysis for hardware and software defects',reason='硬件职能适用目录未收RCA，保留可见内容覆盖缺口。')]
register(list(R.values()),'Astra_v3_hw_d')
