from astra_review_tools import *
R=[]
for r in ['N0323','N0335']:
 ovs=[]
 for eid in ['O1','O2','1:0','4:0','4:1','4:2','4:3']:
  e=next(e for e in EB[RID[r]] if e['evidence_id']==r+':'+eid)
  ovs.append(dict(evidence_id=e['evidence_id'],metric='DUTY_OWN_USE',branch='UNRESOLVED' if eid in ['O1','O2'] else e['branch'],reason='本人中间件通信性能及接口功能测试是该软件/协议的技术使用；与仅列被测SDK实现语言不同。恢复执行口径，ROS/ROS2裸斜线仍未知。'))
 R.append(dict(reading_id=r,review_mode='FOLLOWUP',judgment='复核使用口径：直接测试中间件和通信接口支持使用，不能解释为开发；仅语言实现说明不据此推编程。',evidence_overrides=ovs))
R.append(dict(reading_id='E0182',review_mode='FOLLOWUP',judgment='协议测试执行支持职责使用，但跨协议斜线不明，不能无条件示例。',evidence_overrides=[dict(evidence_id='E0182:'+e,metric='DUTY_OWN_USE',branch='UNRESOLVED',reason='信号完整性测试是实际协议接口技术测试；IIC/SPI/MIPI/DDR/CAN跨类裸斜线，未知关系优先。') for e in ['1:0','1:1','1:2']]))
register(R,'Astra_v3_protocol_test_followup')
