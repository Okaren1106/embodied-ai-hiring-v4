from astra_review_tools import *
JUD={
'N0254':'完整OEM质量流程已读。按质量体系开展工作是明确上位类别使用；具体标准/检验规范子型斜线不使同一类别未知。主导/参与事故处置不强行定本人独立责任。',
'E0059':'工厂运营责任明确，库存/安全/精益分开；SOP等列举属于同一操作规范族，应无条件。生产停线和设备故障是实际运行异常，补运行排障，未将研发调试混入。',
'E0030':'本人测试规划、执行、专项统筹与EE协作分开；制定板级测试方案不直接证明开发评测工具，改为应用。优先BMS经验不硬化一般资格。',
'E0273':'焊接装机与物料管理明确，测试仅辅助；模数电理论未自动补成嵌入式固件或CAD工具。全部可读来源已核。',
'E0260':'系统性设计测试阈值、覆盖与完整工艺流程，符合测试方法开发，与E0259仅工站导入不同。可制造量产设计本人明确。',
'E0227':'本人算法效果评价，数采标注管线以协助为主；数据敏感性特质不等于工程开发。本人标准化评测记录与数据质量流程补SOP使用。',
'E0199':'APP与云端测试本人执行，编写测试用例未明确自动化工具开发；Python资格优先、Appium/Playwright斜线未知保持。',
'E0165':'自动化验收工具链本人开发，鲁棒性是被评估的目标，不足以证明本人开发可靠性机制。保留可靠性应用，并保持ROS2或ROS任选；AI coding不补品牌。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('N0254','N0254:1:0','质量体系这个上位类别直接指导本人工作；示例仅限具体标准。',branch='UNCONDITIONAL')
ov('E0059','E0059:4:0','所列SOP/指导书/工艺卡/检验标准都是操作规范族，编制该族本人责任明确。',branch='UNCONDITIONAL')
ov('E0030','E0030:O2','制定板级部件测试方案不足以证明开发可复用评测工具方法；本人测试应用明确。',metric='DUTY_OWN_USE')
ov('E0199','E0199:O2','编写并执行测试用例不自动等于开发测试系统或工具，未明示自动化。',metric='DUTY_OWN_USE')
ov('E0165','E0165:O5','开发的是验收工具链，鲁棒性/完整性是评估对象；未写研发可靠性机制。',metric='DUTY_OWN_USE')
add('E0059','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','EXAMPLE','统筹生产异常处理（停线、返工、物料缺料、设备故障等），快速闭环。','实际工厂运行中的停线/设备故障处理，故障项在所举异常之中；与研发调试分开。')
add('E0227','V2_SOP_OPERATION','DUTY_OWN_USE','UNCONDITIONAL','规范记录评测过程、算法对比结果及数采数据适配情况，输出标准化评测报告','明确执行评测数据记录和质量操作规范。')
register(list(R.values()),'Astra_v3_mfg_d')
