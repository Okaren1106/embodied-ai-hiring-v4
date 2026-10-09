from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0808':'机器人人工测试和流程优化明确；脚本括号列举没有示例词，应记录独立优先要求。',
'N0850':'采购成本和资产追溯明确，辅助质量与FAI保留协作；MRP/ERP和robotics/actuation未知不强猜。',
'N0844':'系统V&V与仿真HIL测试开发明确；状态估计不自动扩成SLAM，测评上位类别的测试备选合并为无条件出现。',
'N0727':'BIM模型非机器学习模型；验证对象与建筑工具的大量目录缺口已披露，不替换目录。',
'E0535':'安全认证、危害分析与需求制定本人承担；与测试机构对接不等于本人执行技术测试。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
for e in ['O1','4:0']:ov('N0808',e,'Python、Bash括号没有示例词或任选，优先项明确列出。',branch='UNCONDITIONAL')
for e in ['O22','O23','O24']:ov('N0844',e,'仿真、HIL、故障注入或场景测试均属于测评上位概念。',branch='UNCONDITIONAL')
ov('E0535','O4','原文为推动认证测试并作为测试机构主要接口，未明确本人执行测试。',metric='SEPARATE',branch='COORDINATION_OBJECT')
register(list(R.values()),'Astra_v3_boundary_mfg_t')
