from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0073':'硬件测试代表：控制、机械和关节作为被测对象分离，安全安规与耐久测试保留实际方法。',
'N0612':'装配工：明确机器人机械组装是本人机械技术使用，设备日常维护另补，控制单元安装不等同控制算法。',
'N0610':'SQE：来料检验与可靠性标准自主开发；研发器件验证为配合，供应商质量不扩大成采购。',
'N0589':'DQE：明确新产品标准开发及样品测试；风险和制造性评审已有直接依据。',
'N0555':'制造经理：DFM/DFA/DFT跨类别未知保留，同一DFM/DFA一般示例明确；质量机制建设补录。',
'N0266':'塑胶采购：本人订单、库存、成本分析成立，价格谈判职责协助与一般谈判能力分开。',
'N0265':'电气采购：电机及传动件仅采购对象，不作本人技术开发；ERP等为工具示例。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason=why))
for e in ['O3','O4','O6']:ov('N0073',e,'控制、机械及关节作为明确被测对象，与实际测试方法使用分离。',metric='SEPARATE',branch='TEST_OBJECT')
ov('N0612','O2','明确本人完成机械部件组装，而非仅机械产品背景。',metric='DUTY_OWN_USE')
add('N0612','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL',4,'明确对在用装配工具设备日常维护。')
add('N0610','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','EXAMPLE',4,'制定来料检验及测试质量标准。')
add('N0589','TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',4,'明确制定覆盖多维测试的全测标准。')
add('N0589','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',4,'明确标准制定及质量流程宣导。')
add('N0555','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',5,'本人建立生产质量管理及反馈改进机制，不仅协作文件转化。')
register(list(R.values()),'Astra_v3_boundary_mfg_g')
