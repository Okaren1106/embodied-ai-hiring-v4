from astra_review_tools import *
JUD={
'N0980':'执行器现场与产线故障本人调查、ECO实际设计改善明确，RCA与运行排障均成立；CI是持续改善而非持续集成。设计改变同时明确可制造性，补DFM职责。',
'N0886':'已部署车队故障在实验室复现仍属于运行故障研究；不因bench/lab关键词排除。根因上位方法明确，括号FTA/FMEA/8D为具体子例；校准/测试和仪器斜线U保持。',
'N0784':'组装传感计算载荷与测试/现场支持分别读；协议and other为开放列举，应职责例示。Linux/ROS2协助与优先任选分开；IPC-certified个人持证不清仍U。',
'E0514':'生产线工艺与夹具开发、设备采购本人责任明确，MES是经验要求。设置末端测试和过程检查不足以直接推评测工具开发，保留测试应用。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
R['N0980']['additions']=[dict(code='V2_DFM',metric='DUTY_OWN_USE',branch='UNCONDITIONAL',quote='Propose, develop, and execute design changes through Engineering Change Orders (ECOs) to resolve defects and enhance future reliability and manufacturability.',reason='本人执行设计改变以改善可制造性，符合制造约束驱动设计；非只向其他工程师提供建议。')]
for eid in ['N0886:O1','N0886:O2','N0886:O3']:
 R['N0886']['evidence_overrides'].append(dict(evidence_id=eid,branch='EXAMPLE',reason='具体方法在standard methodologies后的括号列举；上位RCA与每种具体方法的关系分开。'))
for eid in ['N0784:2:0','N0784:2:1','N0784:2:2','N0784:2:3']:
 R['N0784']['evidence_overrides'].append(dict(evidence_id=eid,branch='EXAMPLE',reason='and other interfaces构成开放式例示，不能把每种具体接口记为无条件。'))
R['E0514']['evidence_overrides']=[dict(evidence_id='E0514:O3',metric='DUTY_OWN_USE',reason='设置产线末端测试和过程质量检查，没有明确开发可复用测试工具方法。')]
register(list(R.values()),'Astra_v3_mfg_h')
