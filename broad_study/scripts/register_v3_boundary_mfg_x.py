from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0575':'仓内接收、检验、库存、人员与安全明确；退货路由给维修方不是本人修理，SOP创建是Help。',
'E0526':'本人维护过渡数据不等同当前使用ERP；具体ERP品牌仍受上层ERP/MRP关系未知影响。',
'N0910':'仓库主管本人安全运营、人员管理和记录维护问题成立；参与恢复按参与和条件保留，PPE工作要求不是专业证书。',
'N0912':'逐条核对Haslet广告与Burlington模板差异，地点和原文版本保留；未凭模板身份虚记全文复核。',
'N0911':'独立核对Cypress原文语境，仓库机械设备斜线未知，WMS和OSHA要求清楚。',
'N0928':'本人供应商检验与首件批准、RCA明确；ISO14001目录外，质量体系上位主题独立成立。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
ov('E0526','O2','维护数据供未来transition into ERP使用，未明当前本人实际使用ERP。',metric='SEPARATE',branch='FUTURE_SYSTEM_TARGET')
for e in ['3:2','3:3','3:4']:ov('E0526',e,'同一GENERAL层ERP/MRP关系未解，具体品牌继承未知祖先；无示例词也不能另推示例。',branch='UNRESOLVED')
ov('N0928','5:0','international quality standards上位职责明确，括号无示例词；ISO9001证据足以支持类别，ISO14001仍目录外。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_mfg_x')
