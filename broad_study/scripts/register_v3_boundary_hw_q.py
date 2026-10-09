from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0736':'人形电气：明确板卡、电源、现场支持三类本人动作；EMI/EMC同上位，保留一般要求中的including示例。',
'N0735':'联邦电气：不由团队名推资格细节；独立电气设计及服务明确，EMC要求跨语境一致修正。',
'N0737':'机器人电气：此版本优先标题后无技术条款，未借用其他广告；硬件组介绍不当本人技术要求。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
for r,pcb,d,g,p in [('N0736','O3','14:0','26:0','29:0'),('N0735','O1','13:0','25:0','28:0'),('N0737','O3','13:0','25:0',None)]:
 ov(r,pcb,'设计板卡使用PCB方法。',metric='DUTY_OWN_USE')
 ov(r,d,'EMI与EMC均属同一兼容方法族。',branch='UNCONDITIONAL')
 ov(r,g,'EMI/EMC同族，上层including保留示例。',branch='EXAMPLE')
 if p:ov(r,p,'EMI和EMC同族，优先要求上位确定。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_hw_q')
