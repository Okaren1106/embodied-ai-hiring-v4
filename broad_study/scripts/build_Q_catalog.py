"""Build the candidate catalog and lexical review queue. Never assigns semantic positives."""
from common import *
import datetime
baseline=json.loads((ROOT/'configs/Q_baseline_catalog_reference.json').read_text(encoding='utf-8'))
pilot=json.loads((ROOT/'configs/Q_calibration_notes.json').read_text(encoding='utf-8'))
pool=read(ROOT/'tables/Q_candidate_mention_pool.csv')
catalog={}
professional_old={'SK_CPA','SK_CURRICULUM','SK_COST_ANALYSIS','SK_FINANCIAL_MODELING','SK_INVENTORY','SK_SUPPLIER_NEGOTIATION','SK_VOC_ANALYSIS'}
for dim,labels in baseline['labels'].items():
 for code,d in labels.items():
  catalog[code]=dict(code=code,name=d['name'],measurement_type='TECHNICAL_CONCEPT' if dim=='technical_concepts' else ('PROFESSIONAL_CAPABILITY' if code in professional_old else d.get('type','TOOL_METHOD')),legacy_dimension=dim,definition=d['definition'],include=d['include'],exclude=d['exclude'],aliases=d.get('aliases',[d['name']]),change='RETAIN_DEFINITION',baseline_reference_version=baseline['source_version'])
# These are bounded named-tool entries, not a claim that every named technology in the corpus is covered.
tool_text="""
C|C语言|C语言
GIT|Git|git;GitHub;GitLab
SHELL|Shell脚本|Shell;Bash;BASH;bash shell
JAVASCRIPT|JavaScript|JavaScript;Javascript;JS
TYPESCRIPT|TypeScript|TypeScript;Typescript;Typscript
REACT|React|React;React.js;React Native
VUE|Vue|Vue;Vue3
NODEJS|Node.js|Node.js;NodeJS
SQL_MYSQL|MySQL|MySQL
POSTGRESQL|PostgreSQL|PostgreSQL;Postgres
REDIS|Redis|Redis
MONGODB|MongoDB|MongoDB
PANDAS|Pandas|Pandas
SCIPY|SciPy|SciPy
SPARK|Apache Spark|Apache Spark;Spark;pyspark
FLINK|Flink|Flink
KAFKA|Kafka|Kafka
AIRFLOW|Apache Airflow|Airflow;Apache Airflow
DBT|dbt|dbt
SNOWFLAKE|Snowflake|Snowflake
CLICKHOUSE|ClickHouse|ClickHouse
DATABRICKS|Databricks|Databricks
PARQUET|Parquet|Parquet
MCAP|MCAP|MCAP;mcap
ROSBAG|ROS bag|ROS bag;rosbag;rosbags
AWS|Amazon Web Services|AWS;Amazon Web Services
GCP|Google Cloud|GCP;Google Cloud;Google Cloud Platform
AZURE|Azure|Azure
TERRAFORM|Terraform|Terraform
ANSIBLE|Ansible|Ansible
SLURM|Slurm|Slurm;SLURM
JENKINS|Jenkins|Jenkins;jenkins
GITHUB_ACTIONS|GitHub Actions|GitHub Actions
GITLAB_CI|GitLab CI|GitLab CI;Gitlab CI;gitlab cicd
BAZEL|Bazel|Bazel
CMAKE|CMake|CMake;cmake
PYTEST|pytest|pytest;Pytest
GTEST|Google Test|Google Test;GTest
POSTMAN|Postman|Postman;PostMan
PLAYWRIGHT|Playwright|Playwright
JIRA|Jira|Jira;JIRA;jira
CONFLUENCE|Confluence|Confluence;confluence
GRAFANA|Grafana|Grafana
PROMETHEUS|Prometheus|Prometheus
FOXGLOVE|Foxglove|Foxglove
KIBANA|Kibana|Kibana
GDB|GDB|GDB
WIRESHARK|Wireshark|Wireshark
PERF|Linux perf|perf
FTRACE|ftrace|ftrace
TENSORRT|TensorRT|TensorRT;NVIDIA TensorRT;TensorRT-LLM
ONNX|ONNX|ONNX
ONNX_RUNTIME|ONNX Runtime|ONNX Runtime
VLLM|vLLM|vLLM;vllm
SGLANG|SGLang|SGLang;sglang
TRITON_COMPILER|Triton GPU编程语言|Triton
TRITON_SERVER|Triton Inference Server|Triton Inference Server;Tensorflow Serving
NCCL|NCCL|NCCL
DEEPSPEED|DeepSpeed|DeepSpeed
FSDP|FSDP|FSDP
DDP|DistributedDataParallel|DDP;PyTorch DDP
HUGGINGFACE|Hugging Face工具库|Hugging Face;HuggingFace;Hugging Face Transformers
NSIGHT|Nsight|Nsight;Nsight Systems
EIGEN|Eigen|Eigen
CERES|Ceres Solver|Ceres;Ceres Solver
G2O|g2o|g2o;G2O
GTSAM|GTSAM|GTSAM
PCL|Point Cloud Library|PCL
OPEN3D|Open3D|Open3D
MOVEIT|MoveIt|MoveIt
NAV2|Nav2|Nav2
OMPL|OMPL|OMPL
OCS2|OCS2|OCS2;ocs2
OSQP|OSQP|OSQP
IPOPT|Ipopt|Ipopt;IPOPT
QPOASES|qpOASES|qpOASES
RVIZ|RViz|RViz;rviz
BLENDER|Blender|Blender;blender;BLENDER
HOUDINI|Houdini|Houdini
UNITY|Unity|Unity
UNREAL|Unreal Engine|Unreal;Unreal Engine;unreal
OMNIVERSE|Omniverse|Omniverse;Omniverse Kit
HABITAT|Habitat|Habitat;AI Habitat
SAPIEN|SAPIEN|SAPIEN;Sapien
MANISKILL|ManiSkill|ManiSkill
GENESIS|Genesis|Genesis;Genesis World;genesis world
PHYSX|PhysX|PhysX;NVIDIA PhysX
BULLET|Bullet|Bullet
USD|Universal Scene Description|USD
URDF|URDF|URDF
MJCF|MJCF|MJCF
SDF|Simulation Description Format|SDF
FREE_RTOS|FreeRTOS|FreeRTOS;freertos
RT_THREAD|RT-Thread|RT-Thread;rt-thread
QNX|QNX|QNX
YOCTO|Yocto|Yocto
BUILDROOT|Buildroot|Buildroot
DDS|DDS|DDS
ZENOH|Zenoh|Zenoh
AIMRT|AimRT|AimRT
ZEROMQ_EXTRA|ZeroMQ补充别名|ZeroMQ
CAN|CAN协议族|CAN;CAN FD;CAN-FD;CANFD;CANOpen;CANopen;CAN bus;CANBUS
ETHERCAT|EtherCAT|EtherCAT;Ethercat;EtherCat;ethercat
ETHERNET|Ethernet|Ethernet;ethernet;以太网
TCPIP|TCP/IP|TCP/IP;TCP;UDP
RS485|RS-485串口|RS-485;RS485;RS232;串口
I2C|I2C|I2C;IIC;I²C
SPI|SPI|SPI
UART|UART|UART
USB|USB|USB;usb;USB 3.0
GMSL|GMSL|GMSL
PTP|PTP时间同步|PTP
NTP|NTP时间同步|NTP
PROFINET|PROFINET|PROFINET;Profinet
MODBUS|Modbus|MODBUS;Modbus
PLC|PLC|PLC;PLCs;Safety PLCs
STRUCTURED_TEXT|Structured Text|Structured Text
LADDER|Ladder Logic|Ladder Logic
FBD|Function Block Diagrams|Function Block Diagrams
ANSYS|ANSYS|ANSYS;Ansys;ansys;Anasys;ansoft
ABAQUS|Abaqus|ABAQUS;Abaqus
COMSOL|COMSOL|COMSOL
HYPERMESH|HyperMesh|Hypermesh;HyperMesh
ADAMS|Adams|Adams
KISSSOFT|KISSsoft|KISSsoft;Kisssoft
LTSPICE|LTspice|LTspice;LTSpice
HFSS|HFSS|HFSS
ADS|Advanced Design System|ADS
KICAD|KiCad|KiCad;KiCAD
PADS|PADS|PADS;Pads;Mentor PADS
ORCAD|OrCAD|OrCAD;ORCAD
ALLEGRO|Cadence Allegro|Allegro
EPLAN|EPLAN|EPLAN;EPLAN Electric
AUTOCAD|AutoCAD|AutoCAD
ONSHAPE|Onshape|Onshape;OnShape
FUSION360|Fusion 360|Fusion 360
MASTERCAM|Mastercam|Mastercam;Master Cam
LABVIEW|LabVIEW|LabVIEW;LabView;labview
TESTSTAND|TestStand|TestStand;NI/TestStand
AUDIO_PRECISION|Audio Precision|Audio Precision
SOUNDCHECK|SoundCheck|SoundCheck
DAQ|数据采集仪系统|DAQ;DAQs;DAQ systems;数据采集仪;数据采集卡
SPECTRUM_ANALYZER|频谱分析仪|spectrum analyzers;频谱仪;频谱分析仪
NETWORK_ANALYZER|网络分析仪|network analyzers;矢网;VNA
THERMAL_CAMERA|热像仪|thermal cameras
CMM|三坐标测量|CMM;CMMs;三坐标
HAND_METROLOGY|手持尺寸量具|calipers;micrometers;卡尺;高度规
POWER_SUPPLY|测试电源与负载|power supplies;electronic loads;可编程电源;程控电源;电子负载
FIGMA|Figma|Figma
PHOTOSHOP|Adobe Photoshop|Photoshop;PS
ILLUSTRATOR|Adobe Illustrator|Illustrator
RHINO|Rhino|Rhino;Rhino(SUBD)
KEYSHOT|KeyShot|KeyShot;Keyshot;keyshot
ADOBE_CREATIVE|Adobe Creative Suite|Adobe Creative Suite
AXURE|Axure|Axure
NOTION|Notion|Notion
LINEAR|Linear|Linear
MS_PROJECT|Microsoft Project|MS Project;Microsoft Project;Project;project
SMARTSHEET|Smartsheet|Smartsheet;Smartsheets
ASANA|Asana|Asana
VISIO|Visio|Visio
MIRO|Miro|Miro
JAMA|Jama|Jama;JAMA
TESTRAIL|TestRail|TestRail;Testrails
PROCORE|Procore|Procore
BLUEBEAM|Bluebeam|Bluebeam
FEISHU|飞书|飞书;飞书多维表格;飞书项目
OFFICE|Microsoft Office|Office;Microsoft Office;Microsoft Office Suite
GOOGLE_WORKSPACE|Google Workspace|Google Workspace;Google Suite;google suite;G-Suite
CRM|CRM系统|CRM;CRM platform
SALESFORCE|Salesforce|Salesforce
HUBSPOT|HubSpot|HubSpot
ZENDESK|Zendesk|Zendesk
SAP|SAP|SAP
ORACLE|Oracle业务系统|Oracle
NETSUITE|NetSuite|NetSuite;Netsuite
QUICKBOOKS|QuickBooks|QuickBooks
KINGDEE|金蝶|金蝶;金蝶云星空;金蝶 BOS
YONYOU|用友|用友
MES|MES系统|MES;mes
MRP|MRP系统|MRP
SRM|SRM系统|SRM;SRM系统
PLM|PLM系统|PLM
ASHBY|Ashby|Ashby
LEVER|Lever|Lever
RIPPLING|Rippling|Rippling
ADP|ADP|ADP;ADP Workforce Now
WORKDAY|Workday|Workday
POWERBI|Power BI|Power BI;PowerBI
TABLEAU|Tableau|Tableau
LOOKER|Looker|Looker
CURSOR|Cursor|Cursor
CODEX|Codex|Codex;codex
CLAUDE_CODE|Claude Code|Claude Code;ClaudeCode;Claude code
"""
for line in tool_text.strip().splitlines():
 c,n,a=line.split('|');code='V2_'+c
 catalog[code]=dict(code=code,name=n,measurement_type='NAMED_TOOL_OR_PROTOCOL',legacy_dimension='',definition=f'广告明确提及{n}作为工具、系统、格式、协议或相关能力。',include='对应名称或已列别名，且原文可辨识对象；逐提及另判职责/要求/背景与分支。',exclude='公司宣传、招聘对象、产品采购对象不能成为本人使用正例；不由相邻工具、泛称或上位概念补值。',aliases=a.split(';'),change='ADD',baseline_reference_version='')
# Fix intentionally sensitive families: definitions do not silently equate related products.
del catalog['V2_ZEROMQ_EXTRA']
del catalog['V2_WORKDAY']
catalog['V2_TRITON_SERVER']['aliases']=['Triton Inference Server']
special={
'V2_GIT':'Git版本控制及明确GitHub/GitLab代码协作使用；仅品牌传播、开源发表渠道、一般网站链接排除。',
'V2_C':'独立C语言或C/C++中的C；不匹配C++单独出现、C级资历、字母编号。',
'V2_TRITON_COMPILER':'Triton GPU kernel/编译器/语言；推理服务Triton Inference Server另列，无法分辨记U。',
'V2_TRITON_SERVER':'NVIDIA Triton Inference Server；不是TensorFlow Serving，也不是Triton GPU编程语言。',
'V2_HUGGINGFACE':'作为模型训练、数据或软件库使用/开发/技能；社区宣传和发布渠道另列非本人使用。',
'V2_PTP':'时间同步Precision Time Protocol；一般项目缩写不能归入。',
'V2_SDF':'仿真描述文件Simulation Description Format；signed distance field几何概念不能归入。',
'V2_PHOTOSHOP':'PS仅在设计工具列表或图像编辑语境中作Photoshop；其他缩写记U。',
'V2_MS_PROJECT':'Project仅在软件列表或明确项目管理工具语境中；一般project名词排除。',
'V2_ANSYS':'ANSYS产品族；具体Mechanical/Fluent等仍保留原词，不声称型号相同。Anasys仅有明确工程仿真语境时归一。',
'V2_PLC':'PLC平台/编程/使用方法；仅采购PLC或被修设备含PLC不自动为编程能力。',
'V2_ILLUSTRATOR':'明确Illustrator；AI只有明确Adobe软件列表才可候选，不将人工智能或2D/AI效果图归入。',
'V2_ORACLE':'Oracle业务系统/ERP；数据库Oracle保留候选并按具体对象另判，泛称品牌不自动合并。',
'V2_NETWORK_ANALYZER':'网络/矢量网络分析仪器；软件抓包分析不是该仪器。',
'V2_HAND_METROLOGY':'明确手持尺寸测量量具；按产品保留原词，此为仪器类别而非单一品牌。',
'V2_POWER_SUPPLY':'测试台可编程电源/电子负载等仪器；被设计的供电电路不是工具。',
}
for c,s in special.items():catalog[c]['include']=s;catalog[c]['exclude']+=' '+s
# Domain methods/professional measures, each with a substantive inclusion/exclusion boundary.
method_text="""
DFM|可制造与可装配设计|ENGINEERING_METHOD|DFM;DFA;DFMA;DfX;DFX|明确制造/装配约束驱动设计与优化|仅经历制造公司或泛称设计不足
LEAN|精益与六西格玛方法|ENGINEERING_METHOD|Lean;Lean Manufacturing;Six Sigma;六西格玛;DMAIC;5S;6S|精益生产、六西格玛或明确方法实施/知识|一般持续改进修辞不足；证书单列
APQP_PPAP|生产质量先期策划与批准|ENGINEERING_METHOD|APQP;PPAP;FAI;FAIs;PPAPs|明确质量策划、生产件批准或首件检验流程|供应商管理泛称不足；保留具体方法
RCA|根因分析方法|ENGINEERING_METHOD|RCA;RCCA;FACA;5-Whys;5WHY;5Why;5-why;鱼骨图;fishbone|明确根因分析、5Why或鱼骨分析|一般解决问题能力不足
DOE_MSA|试验设计与测量系统分析|ENGINEERING_METHOD|DOE;MSA;GRR;GR&R;Gauge R&R|明确统计试验设计或测量重复性再现性分析|一般测试或统计分析不足
HALT_HASS|加速寿命与应力筛选|ENGINEERING_METHOD|HALT;HASS|明确加速寿命/应力试验或筛选|一般可靠性测试不足
DFT|可测试性与电路产测|ENGINEERING_METHOD|DFT;ICT;FCT;bed-of-nails|可测试性设计、在线或功能电路测试方法|仅泛称软件测试不足
HIL|硬件在环|ENGINEERING_METHOD|HIL;hardware-in-the-loop|硬件在环测试、环境或验证|普通实机测试不自动纳入
CALIBRATION|传感器与系统标定|ENGINEERING_METHOD|calibration;calibrate;标定;校准|传感器、关节、运动学、测试仪器的明确标定/校准|人员绩效校准或仅读传感器不足
SYSID|系统辨识|ENGINEERING_METHOD|system identification;SysID;系统辨识|估计动力学/执行器模型参数的系统辨识|一般故障诊断不等于辨识
CLASSICAL_CONTROL|经典与最优控制方法|ENGINEERING_METHOD|PID;LQR;MPC;FOC;WBC;QP;optimal control|明确控制算法/优化方法；记录具体子型|仅泛称控制理论不足，不把各种算法视为互换
PATH_SEARCH|路径搜索与轨迹优化|ENGINEERING_METHOD|A*;RRT;RRT*;PRM;trajectory optimization|明确路径搜索、轨迹优化算法|项目计划与泛称导航不足
KALMAN_FACTOR|状态估计与因子图方法|ENGINEERING_METHOD|Kalman Filter;卡尔曼滤波;EKF;UKF;ESKF;Factor Graph;因子图|明确状态估计滤波或图优化方法|普通传感器融合不自动指定方法
FE_TOPOLOGY|结构拓扑优化与数值方法|ENGINEERING_METHOD|SIMP;Level Set;ESO;BESO;拓扑优化;PDE;偏微分方程;变分法|明确结构拓扑优化或数值求解研究|一般机械结构设计不足
CNC_PROCESS|加工与成型工艺|ENGINEERING_METHOD|CNC;injection molding;casting;die casting;stamping;3D printing;3D打印;注塑;压铸;冲压|明确加工、成型、增材制造方法的实践或设计约束|公司生产背景不足；保留工艺子型
EMC_SIPI|电磁兼容与信号电源完整性|ENGINEERING_METHOD|EMC;EMI;SI/PI;signal integrity;power integrity|明确电磁兼容、抗扰、信号或电源完整性分析/设计|采购符合标准器件不等于本人设计能力
SAFETY_ANALYSIS|功能安全分析与验证|ENGINEERING_METHOD|SIL;PL;HARA;FMEDA;SISTEMA|明确安全完整性/性能等级、危害分析或安全验证|通用行政合规或保密要求不足
REQUIREMENTS_ENGINEERING|系统需求与验证追溯|ENGINEERING_METHOD|requirements traceability;MBSE;V-model;DVP&R;需求分解;接口定义|系统指标分解、接口约束、验证追溯等明确工程方法|仅一般产品需求收集/项目日程不同
CI_CD|持续集成与交付|ENGINEERING_METHOD|CI/CD;CICD;continuous integration;持续集成|明确自动构建测试发布流程|一般协作软件或Git不自动推出CI
SIM2REAL|仿真与现实迁移|TECHNICAL_CONCEPT|Sim2Real;sim-to-real;Real2Sim;虚实迁移|明确虚实迁移、模型/数据/参数对齐|拥有仿真与真机两种经验不足以推断迁移
DOMAIN_RANDOMIZATION|域随机化|TECHNICAL_CONCEPT|Domain Randomization;domain randomization;域随机化|明确随机化参数/场景以支持训练或泛化|一般随机采样不足
WORLD_MODEL|世界模型|TECHNICAL_CONCEPT|world model;World Model;world models;世界模型|明确环境动态/世界预测生成模型|WAM须看展开；whole-body action model不是世界模型
POSTTRAINING|模型后训练与对齐|TECHNICAL_CONCEPT|post-training;后训练;RLHF;DPO;GRPO;SFT|明确后训练、对齐、偏好优化/监督微调|一般模型训练不足
MODEL_COMPRESSION|模型压缩与推理优化方法|TECHNICAL_CONCEPT|quantization;量化;知识蒸馏;pruning;LoRA;QLoRA|明确量化、蒸馏、裁剪或低秩适配；保留子型|仅追求速度或小模型不足
3D_RECONSTRUCTION|三维重建表示|TECHNICAL_CONCEPT|3DGS;3D GS;Gaussian Splatting;NeRF;高斯Splatting|明确三维高斯/辐射场等场景重建方法|一般3D建模不足；不自动等于机器人感知本人任务
AGENT_WORKFLOW|AI Agent应用与工作流|TECHNICAL_CONCEPT|AI Agent;agentic;RAG;LangChain;LangGraph;Function Calling|明确智能体应用、检索增强或工具调用工作流|招聘代理、服务代理或仅使用聊天工具不足
QUALITY_STANDARDS|质量体系标准|ENGINEERING_STANDARD|ISO 9001;ISO9001;IATF16949;IATF 16949;AS9100;ISO17025;CNAS|明确质量管理/实验室体系标准|普通quality一词不足；保留标准编号不认为等同
SAFETY_STANDARDS|机器人与电气安全标准|ENGINEERING_STANDARD|ISO 10218;ISO 13849;ISO 12100;ISO 13482;IEC 61508;IEC 62061;IEC 60204;IEC 62368;NFPA79;NFPA 79;ANSI/RIA;UL 1740;UL3100|明确标准适用/设计/测试知识；原编号保留|提及认证不证明公司或个人已获认证
IPC_STANDARDS|电子装联IPC标准|ENGINEERING_STANDARD|IPC-A-610;IPC-2221;IPC-7351;IPC certification|明确电子装联IPC标准或证书|进程间通信IPC、仿真IPC coupler排除；裸IPC须审读
GD_STANDARD|尺寸公差标准|ENGINEERING_STANDARD|ASME Y14.5|明确ASME Y14.5标准|一般GD&T另有旧标签；不自动推断标准版本
ENV_COMPLIANCE|产品法规与环境认证知识|ENGINEERING_STANDARD|CE;FCC;RoHS;ATEX;IECEx;EMC Directive|明确产品合规、认证、测试知识|公司有认证/广告产品宣传不是岗位知识；不验证现行法律要求
ACCOUNTING|会计财税与核算|PROFESSIONAL_CAPABILITY|GAAP;IFRS;US GAAP;ASC 606;SOX 404;会计;税务|明确核算、财务报告、税务或审计专业知识/职责|一般预算或报销动作不足
LEGAL|法律与合同专业|PROFESSIONAL_CAPABILITY|contract negotiation;securities law;法律;合同审查;知识产权|明确法律分析、合同、公司治理、专利职责或专业要求|行政签收合同或普通遵守法律不足
HR|招聘与人力流程|PROFESSIONAL_CAPABILITY|recruiting;talent acquisition;payroll;薪酬;招聘;人力资源|明确人才获取、雇佣流程、薪酬或劳动关系专业职责|所有招聘广告的投递说明排除；招聘工程师不成为工程技能
PROCUREMENT|采购与供应商流程|PROFESSIONAL_CAPABILITY|sourcing;procurement;RFQ;供应商;采购|明确询报价、寻源、商务谈判、供货管理|仅协作供应商或购买办公物品按具体责任另判
SALES_CRM|销售与客户经营|PROFESSIONAL_CAPABILITY|sales pipeline;account management;销售;客户成功;customer success|明确销售、客户关系、客户成功与服务经营方法|面向客户的一般沟通不自动为销售能力
MARKETING|营销内容与传播|PROFESSIONAL_CAPABILITY|SEO;SEM;marketing;市场营销;品牌;传播|明确营销内容、渠道、活动、增长或技术传播工作|公司口号与一般产品展示排除
PROJECT_METHOD|项目计划与风险管理|PROFESSIONAL_CAPABILITY|Agile;Scrum;Waterfall;WBS;Kanban;关键路径;甘特图;风险矩阵|明确计划、依赖、风险、范围或敏捷方法|仅参与项目不足；PMP方法论不是已持证
UX_RESEARCH|用户研究与体验设计方法|PROFESSIONAL_CAPABILITY|journey mapping;user research;human factors;用户研究;用户旅程;人因|明确用户研究、体验路径、可用性与人因方法|客户满意度运营与机械尺寸设计不同
CMF_DESIGN|工业外观与CMF|PROFESSIONAL_CAPABILITY|CMF;industrial design;工业设计;色彩;材质|明确工业外观、材料色彩与表面体验设计|机械强度材料选型不自动是CMF
TELEOP|遥操作与示教|OPERATING_METHOD|teleoperation;teleoperate;遥操作;示教|本人操作/示教机器人或相关经验；开发遥操系统另判开发关系|模型训练愿景或遥操数据研究背景不自动为本人操作
MOCAP|动作捕捉与演示数据采集|OPERATING_METHOD|motion capture;mocap;motion capture suits;动作捕捉;动捕|明确身体动作捕捉、传感服/控制器示范数据采集|一般数据工程与电影动画经验需按语境记录
SOP_OPERATION|SOP操作与数据质量|OPERATING_METHOD|SOP;standard operating procedures;操作规程;标准作业|明确执行/编制操作规程、采集规范与质量流程|普通守时负责等性格要求排除
INCIDENT_SUPPORT|运行排障与事件升级|OPERATING_METHOD|triage;troubleshooting;incident;故障排查;问题升级|本人运行中的排障、恢复、工单记录与升级|开发调试须按对象区分，不能当客户现场维护
CUSTOMER_SERVICE|客户与医院服务流程|PROFESSIONAL_CAPABILITY|customer service;de-escalation;hospital workflow;客户服务|明确用户协助、服务沟通、医院流程或去激化技能|一般跨团队沟通不足
SAFETY_OPERATION|作业安全知识与操作|OPERATING_METHOD|OSHA;HIPAA;LOTO;安全操作;作业安全|明确作业安全、医院操作培训与流程要求|不据要求推断已经获证；公司一般平等雇佣声明排除
ACCOUNTING_CREDENTIAL|财会资格|PROFESSIONAL_QUALIFICATION|ACCA;CFA;CMA;中级会计;初级会计;税务师;registro CRC|明确财会金融资格或考试要求；保持已持证/部分通过/优先|不等于财会学位；CPA沿用旧单项
LEGAL_CREDENTIAL|法律执业与资格|PROFESSIONAL_QUALIFICATION|California Bar;licensed to practice law;法律职业资格;司法考试;专利代理人资格|明确执业资格/考试/代理资格|JD法律学位或法律专业背景不是执照
HR_CREDENTIAL|人力专业资格|PROFESSIONAL_QUALIFICATION|SHRM;PHR;SPHR;SHRM-SCP|明确人力专业认证|HRIS软件经验不是认证
PM_CREDENTIAL|项目管理资格|PROFESSIONAL_QUALIFICATION|PMP;PgMP;PRINCE2;CAPM;Certified Scrum Master;项目管理师|明确资格/认证要求或优先|仅PMP方法论、项目实践经验不等于资格
QUALITY_CREDENTIAL|质量与供应链资格|PROFESSIONAL_QUALIFICATION|CQE;CMQ;ASQ;APICS;CPIM;CSCP;CPSM;SCMP;Six Sigma Black Belt;六西格玛绿带;黑带|明确资格认证或等级；原证书保留|仅使用六西格玛工具不是持证
SECURITY_CREDENTIAL|信息安全资格|PROFESSIONAL_QUALIFICATION|CISSP;CISA;CISM;Security+|明确信息安全专业资格|ISO27001公司体系不是个人资格
"""
for line in method_text.strip().splitlines():
 c,n,t,a,inc,exc=line.split('|');code='V2_'+c
 catalog[code]=dict(code=code,name=n,measurement_type=t,legacy_dimension='',definition=inc,include=inc,exclude=exc,aliases=a.split(';'),change='ADD',baseline_reference_version='')
# Typographical aliases are explicit, do not edit raw sources.
catalog['SK_CREO']['aliases']+=['CERO','Pro/E','Proe']
catalog['SK_SOLIDWORKS']['aliases']+=['Soildworks']
catalog['SK_NX']['aliases']+=['UG']
catalog['V2_C']['aliases'].append('C')
# Family membership allows future no-hit ads to remain in the denominator of the role catalog.
# Active role lists are inventory-based, never based on positivity, company gaps or outcomes.
def hits(text,alias):
 if not alias:return False
 pat=re.escape(alias)
 if re.match(r'^[A-Za-z0-9]',alias):pat=r'(?<![A-Za-z0-9_])'+pat
 if re.search(r'[A-Za-z0-9]$',alias):pat+=r'(?![A-Za-z0-9_])'
 return bool(re.search(pat,text,re.I))
compiled={}
for c,d in catalog.items():
 pats=[]
 for a in d['aliases']:
  if not a:continue
  p=re.escape(a)
  if re.match(r'^[A-Za-z0-9]',a):p=r'(?<![A-Za-z0-9_])'+p
  if re.search(r'[A-Za-z0-9]$',a):p+=r'(?![A-Za-z0-9_])'
  pats.append(p)
 compiled[c]=re.compile('|'.join('(?:'+p+')' for p in pats),re.I)
surface_cache={}
role_scopes=defaultdict(set);lexical=[];candidate_by_label=defaultdict(list)
for r in pool:
 if r['origin']=='ACCEPTED_TAG':
  matches=[r['label_code']]
 else:
  surface=r['surface'] or json.loads(r['raw_json']).get('quote','')
  if surface not in surface_cache:surface_cache[surface]=[c for c,p in compiled.items() if p.search(surface)]
  matches=surface_cache[surface]
 for c in matches:
  role_scopes[c].add(r['role']);candidate_by_label[c].append(r)
 lexical.append(dict(candidate_id=r['candidate_id'],identity_key=r['identity_key'],role=r['role'],surface=r['surface'],origin=r['origin'],candidate_codes=js(matches),status='INHERITED_LABEL_REVIEW_REQUIRED' if r['origin']=='ACCEPTED_TAG' else ('LEXICAL_CANDIDATES_ONLY' if matches else 'OUTSIDE_INITIAL_CATALOG_REQUIRES_CONTEXT_REVIEW')))
# Some legacy mentions have blank surface fields; raw text is an independent
# coverage inventory, never a semantic-positive classifier.
raw_scope_inventory=[]
for k,j in J.items():
 f=role(j)
 if f not in CONCRETE:continue
 txt='\n'.join(RAW[k].get(field,'') or '' for field in ['full_description','duties','requirements'])
 for c,pat in compiled.items():
  if pat.search(txt):
   role_scopes[c].add(f)
   raw_scope_inventory.append(dict(identity_key=k,reading_id=j['reading_id'],role=f,code=c,status='LEXICAL_SCOPE_ONLY'))
dump('tables/Q_raw_text_scope_inventory.csv',raw_scope_inventory)
# All task/competence lists are tailored by role, and may be revised only through versioned whole-role review.
manual_scope={
'RF_MANUFACTURING_QUALITY_SUPPLY':['DFM','LEAN','APQP_PPAP','RCA','DOE_MSA','HALT_HASS','DFT','CNC_PROCESS','QUALITY_STANDARDS','IPC_STANDARDS','PROCUREMENT','QUALITY_CREDENTIAL','SOP_OPERATION','CI_CD'],
'RF_HARDWARE_ELECTRICAL':['DFM','EMC_SIPI','DFT','HIL','CALIBRATION','SAFETY_STANDARDS','IPC_STANDARDS','ENV_COMPLIANCE'],
'RF_ML_AI_ENGINEERING':['SIM2REAL','DOMAIN_RANDOMIZATION','WORLD_MODEL','POSTTRAINING','MODEL_COMPRESSION','3D_RECONSTRUCTION','AGENT_WORKFLOW'],
'RF_ROBOTICS_SOFTWARE':['CI_CD','AGENT_WORKFLOW','INCIDENT_SUPPORT','MODEL_COMPRESSION'],
'RF_COMMERCIAL_CUSTOMER':['SALES_CRM','MARKETING','CUSTOMER_SERVICE','PROJECT_METHOD'],
'RF_CONTROL_PLANNING':['CLASSICAL_CONTROL','PATH_SEARCH','SYSID','CALIBRATION','SIM2REAL','DOMAIN_RANDOMIZATION'],
'RF_CORPORATE_SUPPORT':['ACCOUNTING','LEGAL','HR','ACCOUNTING_CREDENTIAL','LEGAL_CREDENTIAL','HR_CREDENTIAL','SECURITY_CREDENTIAL','PROJECT_METHOD'],
'RF_DATA_INFRA_OPERATIONS':['SOP_OPERATION','TELEOP','MOCAP','PROJECT_METHOD','CI_CD'],
'RF_DEPLOYMENT_FIELD_SERVICE':['INCIDENT_SUPPORT','RCA','CALIBRATION','SAFETY_OPERATION','CUSTOMER_SERVICE','SOP_OPERATION'],
'RF_INDUSTRIAL_EXPERIENCE_DESIGN':['UX_RESEARCH','CMF_DESIGN','DFM','CNC_PROCESS','3D_RECONSTRUCTION'],
'RF_MECHANICAL_MECHATRONICS':['DFM','CNC_PROCESS','FE_TOPOLOGY','GD_STANDARD','HALT_HASS','RCA'],
'RF_PERCEPTION':['KALMAN_FACTOR','CALIBRATION','3D_RECONSTRUCTION','SIM2REAL','WORLD_MODEL'],
'RF_PRODUCT_PROGRAM':['PROJECT_METHOD','PM_CREDENTIAL','SALES_CRM','REQUIREMENTS_ENGINEERING','PROCUREMENT'],
'RF_RESEARCH_SCIENCE':['WORLD_MODEL','POSTTRAINING','SIM2REAL','FE_TOPOLOGY','DOMAIN_RANDOMIZATION','CLASSICAL_CONTROL'],
'RF_ROBOT_OPERATIONS':['TELEOP','MOCAP','SOP_OPERATION','INCIDENT_SUPPORT','CUSTOMER_SERVICE','SAFETY_OPERATION'],
'RF_SIMULATION_EVALUATION':['HIL','CALIBRATION','SYSID','DFT','SIM2REAL','DOMAIN_RANDOMIZATION','CI_CD','RCA'],
'RF_SYSTEMS_ENGINEERING_INTEGRATION':['REQUIREMENTS_ENGINEERING','SAFETY_ANALYSIS','SAFETY_STANDARDS','CALIBRATION','SYSID','RCA','DFM','EMC_SIPI']}
for f,cc in manual_scope.items():
 for c in cc:role_scopes['V2_'+c].add(f)
for c,d in catalog.items():
 original_type=d['measurement_type']
 d['source_measurement_type']=original_type
 if original_type in ['NAMED_TOOL_OR_PROTOCOL','SOFTWARE_TOOL','INSTRUMENT']:d['measurement_type']='TOOL_INSTRUMENT_PROTOCOL'
 if original_type in ['METHOD','WORK_SKILL']:d['measurement_type']='ENGINEERING_METHOD'
 if c=='SK_CPA':d['measurement_type']='PROFESSIONAL_QUALIFICATION'
 d.update(catalog_version='Q2-v2.1-candidate',applicable_roles=sorted(role_scopes[c]),applicable_tasks='原文任务或要求与该条目可相联系；同职能目录格先保留全广告，确证不适用才NA，缺少提及本身不是NA。',contexts='EXACT_14_SLICES_PLUS_SEPARATE_CONTEXTS',unknown_reasons=['SOURCE_INCOMPLETE_AFFECTING_ITEM','AMBIGUOUS_ALIAS_OR_OBJECT','UNRESOLVED_USE_OR_RELATION','UNRESOLVED_REQUIREMENT_BRANCH','UNRESOLVED_APPLICABILITY'],example_policy='候选原文用于目录示例；正式P须全文判断及证据定位，不能把候选当正例。')
 candidates=candidate_by_label[c]
 d['candidate_examples']=[dict(candidate_id=r['candidate_id'],reading_id=J[r['identity_key']]['reading_id'],surface=r['surface']) for r in candidates[:3]]
 d['example']=('示例（合成，非观察正例）：熟悉'+d['name']+'并用于上述定义中的任务。') if not candidates else '见candidate_examples；保留原语境，不预定正例。'
rules=json.loads((C/'inputs/rules_v1/decisions/q2_rules.json').read_text(encoding='utf-8'))
slices=[(m,'UNCONDITIONAL') for m in ['DUTY_OWN_USE','DUTY_OWN_DEVELOP']]+[(m,b) for m in ['REQUIRED','GENERAL','PREFERRED'] for b in ['UNCONDITIONAL','CHOICE','EXAMPLE','CHOICE_AND_EXAMPLE']]
assert len(slices)==14
save_json('configs/Q_catalog_v2_candidate.json',dict(version='Q2-v2.1-candidate',researcher='Astra',status='DRAFT_PENDING_BRIDGE_AND_SCHEMA_REVIEW',pilot_read_ads=340,labels=list(catalog.values())))
save_json('configs/Q_coding_rules_v2.json',dict(version='Q2-v2.1',legacy_14_slices=[dict(metric=m,branch=b) for m,b in slices],inherited_branch_logic=rules['branch_logic'],inherited_positive_buckets=rules['positive_buckets'],states={'P':'至少一个全文支持的该格明确正例','Z':'来源可判、适用、全文已读，未记录该格正例','U':'影响该项/语境的未知','NA':'有记录的不适用理由','SOURCE_EXCLUDED':'来源不足以评估该维度或该项','PENDING':'尚未执行，不得计入Z或U'},duty_branch='本人职责中的示例、任选、条件执行保留DUTY_CHOICE/DUTY_EXAMPLE/DUTY_CONDITIONAL，不强推无条件；旧v1另版精确复算。',positivity='关键词仅候选；全篇语义裁定。现有编码可继承，但新增目录映射必须全文核对。',read_rule='每广告先完整阅读三个原文字段，再作新标签或Z/NA判断；重复内容可引用已读原文但须审读不同段落。',requirement_strength='明确required/必须/必备为REQUIRED；一般熟悉/经验要求为GENERAL；preferred/加分项为PREFERRED；ideal/desirable按明确局部语境，不自动硬化。',branch_rule='所有祖先关系；缺节点的新项须研究者给出原文依据的派生分支，不凭邻近命中猜测。',professional_type_rule='专业能力、资格、操作方法单列，不充当技术概念；证书要求不证明已持证。',scope_main='WHOLE23; FAR单列，24主体敏感性',display={'min_positive_companies':5,'min_positive_ads':10,'max_per_type':8,'sort':['positive_companies_desc','positive_ads_desc','code_asc']},group_gate={'min_valid_companies':3,'min_interpretable_ads':20,'small_company_n':10},qc={'seed':20260916,'minimum_per_role':'max(10,ceil(0.2*n))','all_cases':['unknown','NA','new-label-boundary','dispute','main-text-evidence'],'reviewer':'Astra second pass, not independent external review'}))
dump('tables/Q_lexical_catalog_candidates.csv',lexical)
dump('tables/Q2_role_catalog.csv',[dict(role=f,role_name=RN[f],code=c,name=d['name'],measurement_type=d['measurement_type'],definition=d['definition']) for c,d in catalog.items() for f in d['applicable_roles']])
dump('tables/Q2_catalog_bridge.csv',[dict(old_code=c if c.startswith(('SK_','TC_')) else '',new_code=c,change=d['change'],old_definition=d['definition'] if d['change'].startswith('RETAIN') else '',new_definition=d['definition'],reason='旧定义独立保留；新目录扩展覆盖，不是改写认可标签' if d['change']=='RETAIN_DEFINITION' else '340条校准及全目录外原词普查后新增有限测量项',potentially_affected_ads=js(sorted({r['identity_key'] for r in candidate_by_label[c]})),affected_status='LEXICAL_POTENTIAL_NOT_SEMANTIC_CHANGE',baseline_version=d['baseline_reference_version']) for c,d in catalog.items()])
print('catalog labels',len(catalog),'role-label pairs',sum(len(d['applicable_roles']) for d in catalog.values()))
print('unmapped review queue',Counter(r['status'] for r in lexical))
