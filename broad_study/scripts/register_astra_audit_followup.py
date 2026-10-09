from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='FOLLOWUP',judgment='',evidence_overrides=[],additions=[]) for r in ['N0528','N0619']}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
R['N0528']['judgment']='完成初审留下的3个跨语境去重漏项：Blender一般使用能力、Codex一般示例与Agent应用。源末尾截断仅限制优先未观察格；可见职责及一般要求保留。三维重建与流程规范有原文，工具与上位方法分别补全。'
R['N0528']['candidate_reconsiderations_resolved']=['N0528:14','N0528:16','N0528:17']
q='能结合 GPT-6 等模型与 Codex 等 AI 编程 Agent 编写、调试 Blender 脚本，并验证和复现结果'
add('N0528','V2_BLENDER','GENERAL','UNCONDITIONAL',q,'一般要求独立明确Blender脚本，不能用职责出现去重掉要求。')
add('N0528','V2_CODEX','GENERAL','EXAMPLE',q,'一般要求中的Codex等为示例，与本人职责语境分别计。')
add('N0528','V2_AGENT_WORKFLOW','GENERAL','UNCONDITIONAL',q,'明确结合AI编程Agent进行工作的一般能力要求，命名Codex为子例。')
add('N0528','V2_AGENT_WORKFLOW','DUTY_OWN_USE','UNCONDITIONAL','结合 AI 编程 Agent 与三维生成工具','本人使用AI编程Agent处理仿真资产。')
add('N0528','V2_3D_RECONSTRUCTION','DUTY_OWN_USE','UNCONDITIONAL','真实场景重建：基于实拍图片与尺寸信息，还原场景布局和可操作物体','本人真实场景三维重建应用，而非发明重建算法。')
add('N0528','V2_3D_RECONSTRUCTION','GENERAL','CHOICE','具备真实场景或物体重建能力','要求对场景或物体重建的路径任选。')
add('N0528','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','资产管线标准化：制定交付规范，开发批量转换与自动质检工具','明确制定资产交付及自动质量规范。')
for eid in ['N0528:O12','N0528:O17']:ov('N0528',eid,'GPT-6等模型为具体模型示例，不记成无条件基础模型条款。',branch='EXAMPLE')
ov('N0528','N0528:9:3','Isaac Sim / USD关系未知。',branch='UNRESOLVED')
ov('N0528','N0528:18:0','3D GS或NeRF明确重建方法任选。',branch='CHOICE')
ov('N0528','N0528:27:0','可见文本Omniverse Kit、Isaac Sim扩展或...明确工具路径任选；未知尾部影响未观察格。',branch='CHOICE')
ov('N0528','N0528:O14','真实场景或物体重建能力有明确对象任选。',branch='CHOICE')
R['N0619']['judgment']='补齐Isaac及仿真上位标签斜线一致处理。首条主导或参与的未知仍保留，但第二条独立探索VLA联合预训练明确支持本人基础模型开发；正例优先不能因首条不明而抹去另条证据。'
for eid in ['N0619:O5','N0619:O29','N0619:O30','N0619:O31']:ov('N0619',eid,'Isaac Gym / MuJoCo / PyBullet斜线关系未知，与同句其它命名平台统一。',branch='UNRESOLVED')
for eid in ['N0619:O17','N0619:O18']:ov('N0619',eid,'人形/双臂机器人控制对象分支未明确，保留此条要求关系未知。',branch='UNRESOLVED')
add('N0619','TC_FOUNDATION_MODEL','DUTY_OWN_DEVELOP','UNCONDITIONAL','探索视觉-语言-动作联合预训练的新范式','独立第二条明示本人研究VLA预训练，足以支持该格正例；不改首条责任未知记录。')
register(list(R.values()),'Astra_audit_open_items_closed')
