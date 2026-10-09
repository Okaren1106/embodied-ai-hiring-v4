from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0527':'NPI试制协调与排期方法明确，PLM/ERP/MRP关系未知；专业项目管理经历与软件产品名称区分。',
'E0481':'采购机械零件不推机械设计；独立Required工艺知识和谈判要求成立。',
'E0480':'采购技术品类的Required限定采购经验，功率芯片和接口名保持采购对象；合同谈判实际本人承担。',
'E0463':'库存物流职能建设与软件系统实施要求分开；无人形机器人算法推断。',
'E0460':'现场客户验证广告，Linux与语言串列的并列/任选边界未明，不把语言上位类别直接判无条件。',
'E0461':'不同地点广告单独核对，Linux/语言语境与E0460同裁决，客户现场测试不自动当维护。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
R['E0527']['additions'].append(dict(code='V2_PROJECT_METHOD',metric='GENERAL',branch='CHOICE',quote=RAW[RID['E0527']]['full_description'].splitlines()[19],reason='NPI/manufacturing/project management经历明确任选；不是MS Project工具，但专业项目管理类别可纳入。'))
for r in ['E0460','E0461']:
 for e in ['O1','O2']:ov(r,e,'Linux, Python or other coding languages存在Linux与语言组如何组合的歧义；Linux并非编程语言，上位语言不能稳定判无条件。',branch='UNRESOLVED')
register(list(R.values()),'Astra_v3_boundary_mfg_v')
