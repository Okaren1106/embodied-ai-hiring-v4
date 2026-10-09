from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0792':'模块装配、通电校验和接口验证明确本人执行，Linux/ROS2启动仅协助；空的优先标题不补造要求。',
'N0852':'测试建设、运行车队健康与协助维护分开；括号协议/工具清单没有示例词，标定状态追踪不等于执行标定。',
'N0777':'制造流程与验收方法开发明确，SOP与夹治具设计独立；自动测试协作与本人流程责任分开。',
'N0776':'额外复核现场运营管理广告：职责流程建设、升级问题入口与优先技术能力语境清楚。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason=why))
for e in ['O1','26:0','26:1','26:2','26:3','26:4']:ov('N0852',e,'括号中列举明确条目，无如/等/例如或任选，不自动作示例。',branch='UNCONDITIONAL')
for e in ['17:0','18:0']:ov('N0852',e,'维护标定追溯记录、跟踪标定状态不是本人实际标定。',metric='SEPARATE',branch='CALIBRATION_RECORD_OBJECT')
ov('N0852','36:0','明确功能安全合规上位主题，括号编号只是类别内具体标准。',branch='UNCONDITIONAL')
add('N0852','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',17,'本人构建测试流程、标准与最佳实践。')
register(list(R.values()),'Astra_v3_boundary_mfg_s')
