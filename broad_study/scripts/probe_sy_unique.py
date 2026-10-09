"""Check uniqueness of planned systems quotes."""
from common import locate, J
tests = [
('N0595','负责机器人整机系统方案设计与技术架构规划'),
('E0125','负责关节模组在整机中的技术选型、性能匹配、集成应用和问题闭环'),
('E0125','对一体化关节模组具有系统级理解，熟悉电机、减速器、轴承、编码器、力矩传感器、制动器、驱动控制器和嵌入式软件的基本原理及相互影响'),
('E0125','机械、电机、电气、自动化、控制、机器人等相关专业'),
('N0871','Define functional safety requirements for robotic systems'),
('E0349','Architect the strategy for the bring-up and integration of full humanoid robotic systems'),
('E0101','负责宇树机器人产品的安全'),
('N0933','Lead the application of diffusion-based policy learning'),
('E0035','负责机器人整机系统架构规划与整体方案设计'),
('E0567','Collaborate on the system-level deployment of actuators within the humanoid robot'),
('E0567','capability to read C++'),
('E0567','Proficiency in C++'),
('E0567','with a focus on actuation, manipulation or integration'),
('N0236','主导公司新产品研发项目从立项到量产交付的全过程管理'),
('N0438','制定具身本体核心技术路径与关键技术方向'),
('E0592','Drive and execute fleet acceptance testing'),
('N0827','As a Sensor Systems Engineer on the Hardware Team, you will contribute to the design, integration, calibration'),
('N0924','Own and execute the robot picking'),
('N0988','The Systems Engineering, Integration, and Test (SEIT) Department of Boston Dynamics'),
('N0078','深入理解现有机器人系统架构'),
('E0156','定义整机自由度、关节配置、传感器架构'),
('E0317','Build, lead, and develop a high-performing diagnostics and analysis team'),
('E0041','负责人形机器人末端灵巧执行器'),
('E0534','Design and conduct measurements to characterize power bus performance'),
('N0367','负责机器人产品声学系统整体方案设计'),
('N0443','负责机器人产品相关研发类系统的方案架构设计'),
('E0350','Define and document system and subsystem architectures spanning mechanical'),
('E0366','Define system and subsystem architectures spanning all domains'),
('E0366','hazard analysis (HARA, HAZOP, FTA, FMEA)'),
('E0366','with embedded functional safety'),
('E0320','Lead functional safety efforts from concept through deployment'),
('E0320','including 7+ years focused on functional safety'),
('N0820','you will deliver the sensor modules that turn our robots into data-collection platforms'),
('N0774','you will serve as the team'),
('N0734','Field AI builds autonomous robotic systems designed to operate in complex'),
('N0806','Own robot bring-up, calibration, configuration, diagnostics, and validation workflows'),
('N0835','As a Perception Systems Engineer on the Federal Team'),
('N0810','As a Robotics Integration Engineer on the Hardware Team at Field AI'),
('E0568','Plan and execute behaviors to validate motion, sensing and control at the system level'),
]
rid_to_k = {}
for k,j in J.items():
    rid_to_k.setdefault(j['reading_id'], []).append(k)
lines=[]
for rid,q in tests:
    ks=rid_to_k[rid]
    k=ks[0]
    loc=locate(k, dict(quote=q))
    lines.append('%s %s | %s | %s' % (rid, loc['method'], loc.get('field'), q[:80]))
from pathlib import Path
Path(__file__).resolve().parents[1].joinpath('notes/sy_unique.txt').write_text('\n'.join(lines), encoding='utf-8')
print('n', len(lines))
