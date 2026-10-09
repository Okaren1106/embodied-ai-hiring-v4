
## N0401 CN_AGIBOT 多模态部署工程师
[duties]
岗位职责
1、部署并维护多模态感知算法/模型； 平台化推理与加速适配；
2、建立可生产使用的质量与稳定性机制；
3、对多模交互前端做系统级剖析与优化；
4、建立全链路可观测体系，保障可维护性。
任职要求
一、核心能力
1、熟悉多传感器输入的零拷贝链路设计与实现（共享内存/环形缓冲/DMABUF/DMA 等任一或多项），理解 buffer 生命周期与并发访问安全。
2、能独立交付端侧前端感知层：从采集同步、感知推理到输入解释与时序聚合，形成可稳定运行的工程模块。
3、具备扎实的端侧性能优化能力：能对 CPU/内存/延迟/吞吐做定量分析与系统性优化，并产出可复现的 benchmark 报告与改进闭环。
二、技术栈要求
1、精通 C/C++，熟悉多线程/锁优化/无锁队列、内存管理、编译与链接、跨平台构建（CMake 等）。
2、熟悉端侧系统：Linux/QNX 其一或两者；具备驱动/多媒体管线/NDK 或底层接口调试经验。
3、熟悉至少一套推理部署体系： Rockchip：RKNN 相关工具链与 Runtime 接入经验（模型转换、量化、精度对齐、性能评估） ； Jetson：TensorRT/CUDA 推理与多流并发优化经验（了解 Jetson AGX Orin 架构者优先）
4、具备基本 CV/语音/多模态工程常识：图像采集与格式（YUV/RGB/RAW）、预处理、后处理、置信度与时序滤波等。
5、具备工程化能力：模块化设计、接口定义、单测/集成测试、故障注入、日志与指标体系（latency breakdown、fps、drop rate、mem peak 等）。
三、加分项（Nice-to-have）
1、具备机器人/具身智能/AR/VR/智能硬件量产经验，对实时性与资源约束有实践。
2、有音视频同步、相机多路同步、麦克风阵列、SLAM/标定、坐标系统一与传感器融合相关经验。
3、熟悉 GStreamer/V4L2/MediaCodec/AAudio 等多媒体栈或类似框架；了解 GPU 图形/计算（OpenGL/Vulkan/OpenCL/CUDA）任一。
4、熟悉性能剖析工具链（perf/atrace/systrace/VTune/Nsight 等任一）并能输出可行动的优化建议。 有隐私与安全意识：端侧数据最小化、权限治理、敏感数据脱敏与合规处理经验。
ACT [{"label": "ACT_ENGINEERING", "quote": "1、部署并维护多模态感知算法/模型； 平台化推理与加速适配；", "relation": "OWNED"}]

## N0384 CN_AGIBOT 机器人端侧模型运行与性能工程师
[duties]
岗位职责
岗位介绍
-负责机器人端侧/边缘侧多模态模型运行系统的设计、开发与性能优化，将 LLM、VLM、Omni、ASR、TTS 等模型转化为可稳定运行、可双向流式调用、可低时延中断和可观测的系统级推理能力。
-你将重点参与原生多模态模型的组件拆分、轻量化适配、端云分层运行、双向流式 API 和运行时资源治理，为机器人实时交互系统建设低延迟、高可靠的模型运行底座。
-本岗位聚焦 Model Runtime、Inference Backend、Realtime Streaming 和 Performance Engineering，不同于常规模型转换或部署脚本开发，不负责上层 Agent 业务编排和机器人交互状态机。
1. 建设端侧多模态模型运行系统
负责 LLM、VLM、Omni、ASR、TTS 等模型的统一接入与稳定运行，完成模型拆分、轻量化适配、端云分层部署和推理引擎构建。
2.建设双向流式推理 API
基于 gRPC 双向流、WebSocket 等协议，支持音频、视频、文本流式输入和文本、语音增量输出，并管理 Session、Deadline、序列一致性和流量反压。
3. 建设模型流式中断能力
实现 Streaming Infer、Cancel、Abort 和 Timeout，支持用户插话时快速停止模型生成及音频输出，并保障 Buffer、队列和 KV Cache 等运行时资源状态一致。
4. 负责推理后端适配与性能优化
适配 TensorRT、TensorRT-LLM、vLLM、SGLang、ONNX Runtime 及厂商 NPU/DSP 工具链，开展模型导出、量化、精度对齐和性能优化。
5. 建设资源调度、性能与稳定性闭环
优化多模型资源分配和音视频数据通路，建立 TTFT、首音频输出延迟、Audio-to-Audio Latency、Cancel 响应时延及 P95/P99 等性能基线，完善 Trace、自动化回归和长稳测试，并支持真实机器人联调与 Demo 交付。
任职要求
1. 本科及以上学历，计算机、软件工程、人工智能、电子信息、自动化、高性能计算等相关专业优先。
2. 具备 3 年以上 AI 推理系统、端侧模型运行、高性能计算、异构计算、实时音视频、机器人软件、智能座舱或大模型基础设施相关经验。
3. 熟练掌握 C++，具备良好的 Python 和 Linux 开发、调试及性能分析能力。
4. 在以下两个方向中，至少一个方向具备深入项目经验，并对另一方向有完整理解：
* 模型推理 Runtime、推理后端、模型服务或端侧运行系统；
* 双向流式协议、实时音视频、异步网络或低延迟流式系统。
5. 熟悉 TensorRT / TensorRT-LLM、vLLM / SGLang、ONNX Runtime、Triton、CUDA 或厂商 NPU/DSP 工具链中的至少一种。
6. 理解 Transformer、LLM、VLM 或 Omni 模型的基本推理流程，熟悉 Prefill / Decode、KV Cache、Streaming Generation 和动态/静态 Shape 等概念；具备多线程、异步任务、内存管理和性能 Profiling 能力。
加分项
1. 有 Qwen-Omni 或类似原生多模态、Any-to-Any、端到端语音交互模型的拆分、流式推理或端云分层运行经验。
2. 有 gRPC 双向流、WebSocket、RTC、Realtime API 或流式 SDK 设计经验。
3. 有请求级 Cancel、原生流式中断、Session 资源隔离、KV Cache 回收或 Deadline 管理经验。
4. 有 Jetson Orin、Thor、高通 SoC、地平线、昇腾等边缘 AI 平台的模型运行和性能优化经验。
5. 熟悉 FP8 / INT8 / INT4 量化、CUDA Kernel、TensorRT Plugin、计算图优化，或有机器人、智能座舱、自动驾驶等真实端侧项目交付经验。
ACT [{"label": "ACT_ENGINEERING", "quote": "负责 LLM、VLM、Omni、ASR、TTS 等模型的统一接入与稳定运行，完成模型拆分、轻量化适配、端云分层部署和推理引擎构建。", "relation": "OWNED"}]

## E0248 CN_XSQUARE 机器人软件开发工程师
[duties]
- 负责 UI 采数与模型推理交互模块开发:基于 ROS2 实现数据获取、机器人控制、采集任务配置、实时可视化展示与模型交互。
- 负责校验数据采集系统:多传感器数据接入与时间同步、rosbag2 录包与回放、数据质量校验等。
- 负责模型推理工程化集成与部署:对接内部模型推理框架,实现批量实时推理、模型传输与模型版本更新。
- 根据强化学习(RL)训练/评测流程开发数据 Pipeline:trajectory/episode 构建(obs/action/reward)、数据集切分与版本化、离线评测指标统计与回归验证(仿真/实机)。
- 基于内部机器人 SDK 平台开发,抽象多机型统一接口与组件化能力,沉淀可复用模块、示例工程与二次开发文档。
[requirements]
- 本科及以上,计算机/自动化/机器人相关专业。
- 熟练 C++,掌握数据结构、计算机网络、操作系统等基础知识,具备良好工程化能力与代码质量意识。
- 熟悉 Linux 开发环境与常用命令,具备调试与性能分析能力。
- 熟悉 ROS2等生命周期管理,可独立完成模块化节点设计与系统集成。
- 具备 AI 推理落地能力:了解深度学习基础与端侧部署要点,能完成模型导出与推理集成。
- 理解 RL 基本流程与数据形态,能围绕训练/评测闭环构建数据采集、回放复现、数据集管理与指标体系。
- 理解设计模式与接口抽象,能够在复杂系统中进行模块解耦与可维护架构设计。
- 有RL经验/顶会论文/竞赛经历(Robomaster/Robocon)者优先。
[full_description]
岗位职责
- 负责 UI 采数与模型推理交互模块开发：基于 ROS2 实现数据获取、机器人控制、采集任务配置、实时可视化展示与模型交互。
- 负责校验数据采集系统：多传感器数据接入与时间同步、rosbag2 录包与回放、数据质量校验等。
- 负责模型推理工程化集成与部署：对接内部模型推理框架，实现批量实时推理、模型传输与模型版本更新。
- 根据强化学习（RL）训练/评测流程开发数据 Pipeline：trajectory/episode 构建（obs/action/reward）、数据集切分与版本化、离线评测指标统计与回归验证（仿真/实机）。
- 基于内部机器人 SDK 平台开发，抽象多机型统一接口与组件化能力，沉淀可复用模块、示例工程与二次开发文档。
任职要求
- 本科及以上，计算机/自动化/机器人相关专业。
- 熟练 C++，掌握数据结构、计算机网络、操作系统等基础知识，具备良好工程化能力与代码质量意识。
- 熟悉 Linux 开发环境与常用命令，具备调试与性能分析能力。
- 熟悉 ROS2等生命周期管理，可独立完成模块化节点设计与系统集成。
- 具备 AI 推理落地能力：了解深度学习基础与端侧部署要点，能完成模型导出与推理集成。
- 理解 RL 基本流程与数据形态，能围绕训练/评测闭环构建数据采集、回放复现、数据集管理与指标体系。
- 理解设计模式与接口抽象，能够在复杂系统中进行模块解耦与可维护架构设计。
- 有RL经验/顶会论文/竞赛经历（Robomaster/Robocon）者优先。
ACT [{"label": "ACT_DEPLOYMENT", "quote": "负责模型推理工程化集成与部署", "relation": "OWNED"}, {"label": "ACT_ENGINEERING", "quote": "负责 UI 采数与模型推理交互模块开发", "relation": "OWNED"}, {"label": "ACT_QUALITY", "quote": "负责校验数据采集系统", "relation": "OWNED"}]

## N0312 CN_PAXINI 初级具身智能算法工程师
[duties]
1.数据工程： 负责海量机器人遥操作数据的采集、清洗、标注及标准化处理，搭建高效的数据流水线。
2.训练与评测： 协助高级工程师进行模型训练，负责在多场景、多构型下进行模型性能的自动化评测与Benchmark构建。
3.环境运维： 负责训练环境的维护、Bug排查及日志分析，解决训练过程中的环境崩溃和显存溢出等周边问题。
4.实验跟踪： 详细记录实验过程与结果，协助进行模型推理加速和部署脚本的开发。
[requirements]
1.硬性背景： 本科及以上学历，计算机、电子信息、自动化等相关专业。
2.代码能力： 精通Python，熟悉Linux开发环境，代码规范，具备良好的Debug能力。
3.工具链： 熟悉PyTorch；了解Isaac Sim/Mujoco等物理仿真平台的基本使用。
4.软素质： 自驱力强，能吃苦（需配合真机实验进度），具备优秀的团队协作精神，愿意投身一线工程落地。
[full_description]
工作职责
任职资格
ACT [{"label": "ACT_DATA_OPERATIONS", "quote": "1.数据工程： 负责海量机器人遥操作数据的采集、清洗、标注及标准化处理，搭建高效的数据流水线。", "relation": "OWNED"}, {"label": "ACT_DEPLOYMENT", "quote": "3.环境运维： 负责训练环境的维护、Bug排查及日志分析，解决训练过程中的环境崩溃和显存溢出等周边问题。", "relation": "OWNED"}, {"label": "ACT_ENGINEERING", "quote": "负责在多场景、多构型下进行模型性能的自动化评测与Benchmark构建", "relation": "OWNED"}, {"label": "ACT_ENGINEERING", "quote": "2.训练与评测： 协助高级工程师进行模型训练，负责在多场景、多构型下进行模型性能的自动化评测与Benchmark构建。\n3.环境运维： 负责训练环境的维护、Bug排查及日志分析，解决训练过程中的环境崩溃和显存溢出等周边问题。\n4.实验跟踪： 详细记录实验过程与结果，协助进行模型推理加速和部署脚本的开发。", "relation": "PARTICIPATES"}]

## N0867 US_DEXTERITY Security Architect
[duties]
As the Security Architect, you will be leading all aspects of Software Security for Dexterity’s Robotics Product Lines. This is a very visible and “hands-on” role that requires you to write and review code, write and audit policies, and work with auditors, prospects and customers to demonstrate compliance with security policies. 
The role also requires keeping our Security Guidelines, Incident Plan and other policy documents updated with the latest industry best-practices. You will work with a team of very talented Software and DevOps Engineers, Operations and Customer Success Managers to ensure that we have the right policies and processes in place and are effectively communicating and enforcing them.
We are very interested in candidates that have previously led or played a significant role in achieving ISO27001 and SOC2 compliance at a software company. Multiple years of real-world production experience is required. Other duties involve analyzing requirements, mentoring software developers and communicating best practices via documents. 
 
In order to thrive in this role you will have strong knowledge of modern DevOps/SecOps tooling and industry trends. Strong communication and problem-solving skills are essential to the role. Solid experience in C++ and Python is required to ensure you are operating at all of the required levels to be successful. 
About Dexterity: 
At Dexterity, we believe robots can positively transform the world. Our breakthrough technology frees people to do the creative, inspiring, problem-solving jobs that humans do best by enabling robots to handle repetitive and physically difficult work.
We’re starting with warehouse automation, where the need for smarter, more resilient supply chains impacts millions of lives and businesses around the world. Dexterity's full-stack robotics systems pick, move, pack, and collaborate with human-like skill, awareness, and learning capabilities. Our systems are software-driven, hardware-agnostic, and have already picked over 15 million goods in production. And did we mention we’re customer-obsessed? Every decision, large and small, is driven by one question – how can we empower our customers with robots to do more than they thought was possible?
Dexterity is one of the fastest growing companies in robotics, backed by world-class investors such as Kleiner Perkins, Lightspeed Venture Partners, and Obvious Ventures. We’re a diverse and multidisciplinary team with a culture built on passion, trust, and dedication. Come join Dexterity and help make intelligent robots a reality!
Required Skills:
MS or PhD in Computer Science, or a related discipline, or equivalent experience.
Background in InfoSec, software supply chain security and secure coding practices
Previous experience leading or significant contribution to achieving ISO27001 and SOC2 Compliance
Experience working with auditors and customer InfoSec/IT teams. Strong internal and external communication skills, Attention to details
Strong knowledge of Modern C++ and Python
Experience with Git and modern CI pipelines
Nice to haves:
Knowledge of Network Security
Experience with Docker and Kubernetes
Experience with cloud infrastructure such as AWS, GCP, Azure etc. 
Previous startup experience
Equal Opportunity Employer
We are an equal opportunity employer and value diversity at our company. We do not discriminate on the basis of race, religion, color, national origin, gender, sexual orientation, age, marital status, veteran status, or disability status.
ACT [{"label": "ACT_BUSINESS", "quote": "write and audit policies", "relation": "OWNED"}, {"label": "ACT_ENGINEERING", "quote": "write and review code", "relation": "OWNED"}, {"label": "ACT_QUALITY", "quote": "work with auditors, prospects and customers to demonstrate compliance with security policies.", "relation": "OWNED"}]

## N0577 CN_LIMX 强化学习算法工程师
[duties]
岗位职责
1. 负责人形机器人强化学习与控制算法相关工作，支持公司新一代人形机器人硬件平台的算法预研、仿真训练、真机适配与工程化落地。
2. 负责机器人强化学习 sim2real 相关工作，包括但不限于电机 / 电推杆等执行器建模、系统辨识、通讯延时、感知延时、噪声、摩擦、结构柔性等真实物理因素的仿真建模与随机化。
3. 参与新型人形机器人硬件的 RL 控制算法预研，例如电推杆、准直驱 / 串弹执行器、灵巧关节等新执行机构上的控制策略训练、稳定性验证与真机部署。
4. 负责 locomotion、whole-body tracking controller、whole-body control 等控制算法在人形机器人硬件平台上的适配、调参、评测与性能优化。
5. 负责强化学习算法在机器人物理样机上的部署落地，包括模型导出、推理部署、控制频率适配、实时性优化、异常保护和安全机制建设。
6. 负责机器人自动化部署、实验管理、仿真评测、真机数据采集与回放等工具链开发，提升算法迭代效率和真机实验稳定性。
7. 跟进机器人强化学习、模仿学习、sim2real、humanoid locomotion、whole-body control 等方向前沿技术，完成算法复现、改进和工程化验证。
任职要求
1. 熟悉机器人系统，有人形机器人、四足机器人、双足机器人、机械臂、灵巧手等真实机器人项目经验者优先。
2. 掌握 C++ 和 Python，了解 ROS / ROS2 系统工作方式，具备良好的工程实现、调试和问题定位能力。
3. 熟悉 PyTorch、TensorFlow、JAX 等至少一种深度学习 / 强化学习框架，有 RL 算法训练、调参、评测和部署经验者优先。
4. 熟悉机器人仿真软件，如 MuJoCo、Gazebo、NVIDIA Isaac Gym / Isaac Sim、Genesis、RaiSim 等。
5. 了解机器人 sim2real 过程中的关键问题，包括执行器建模、系统辨识、通讯延时模拟、噪声建模、感知仿真、domain randomization、reality gap 分析等。
6. 了解机器人运动控制相关方法，如 PD 控制、MPC、QP、轨迹优化、whole-body control、whole-body tracking、状态估计等，有相关实践经验者优先。
7. 对机器人技术、强化学习、人形机器人硬件系统和真机调试有浓厚兴趣，能接受快速实验迭代和跨软硬件协作。
加分项
1. 有 humanoid locomotion、whole-body tracking、RL controller、sim2real 真机部署经验。
2. 有电推杆、串联弹性执行器、准直驱电机、液压 / 气动执行器等新型执行器建模和控制经验。
3. 熟悉机器人硬件系统，包括电机驱动、传感器、通讯总线、实时控制、安全保护等。
4. 参与过 RoboMaster、Robocon、智能车等机器人竞赛，或参与过机器人开源项目。
5. 在 ICRA、IROS、RSS、CoRL、NeurIPS、ICLR、ICML 等会议发表过机器人学习、强化学习、控制相关论文。
ACT [{"label": "ACT_DEPLOYMENT", "quote": "负责强化学习算法在机器人物理样机上的部署落地", "relation": "OWNED"}, {"label": "ACT_ENGINEERING", "quote": "负责 locomotion、whole-body tracking controller、whole-body control 等控制算法在人形机器人硬件平台上的适配、调参、评测与性能优化。", "relation": "OWNED"}, {"label": "ACT_ENGINEERING", "quote": "参与新型人形机器人硬件的 RL 控制算法预研", "relation": "PARTICIPATES"}]

## N0611 CN_LIMX 机器人强化学习实习生
[duties]
岗位职责
1、负责机器人强化学习sim2real部分工作，包括机器人硬件相关的电机建模、通讯及感知模块延时、噪声模拟等。
2、负责sim2real真机部署，以及相关自动化部署工具开发。
3、实现强化学习算法sim2real在机器人物理样机上的落地应用。
任职要求
1、实习时间至少3个月；
2、海内外研究生及以上学历在读生，机器人、自动化等相关专业优先，有机器人操作相关项目经验者优先；
3、掌握C++ 和 python 编程语言，了解ROS系统工作方式，了解PyTorch，TensorFlow等深度学习框架使用方式。
4、了解机器人仿真软件，如mojuco, gazebo, NVIDIA Isaac等.
5、了解机器sim2real 过程中的关键问题，如电机建模，通讯延时模拟，噪声，感知仿真等。
6、对机器人技术和AI强化学习有浓厚的兴趣和激情。
ACT [{"label": "ACT_DEPLOYMENT", "quote": "负责sim2real真机部署，以及相关自动化部署工具开发。", "relation": "OWNED"}, {"label": "ACT_ENGINEERING", "quote": "负责sim2real真机部署，以及相关自动化部署工具开发。", "relation": "OWNED"}]

## N0614 CN_LIMX 机器人强化学习工程师
[duties]
岗位职责
1、负责机器人强化学习sim2real部分工作，包括机器人硬件相关的电机建模、通讯及感知模块延时、噪声模拟等。
2、负责sim2real真机部署，以及相关自动化部署工具开发。
3、实现强化学习算法sim2real在机器人物理样机上的落地应用。
任职要求
1、熟悉机器人，有机器人工作背景优先
2、掌握C++ 和 python 编程语言，了解ROS系统工作方式，了解PyTorch，TensorFlow等深度学习框架使用方式。
3、了解机器人仿真软件，如mojuco, gazebo, NVIDIA Isaac等.
4、了解机器sim2real 过程中的关键问题，如电机建模，通讯延时模拟，噪声，感知仿真等。
5、对机器人技术和AI强化学习有浓厚的兴趣和激情。
ACT [{"label": "ACT_DEPLOYMENT", "quote": "负责sim2real真机部署，以及相关自动化部署工具开发。", "relation": "OWNED"}, {"label": "ACT_ENGINEERING", "quote": "负责sim2real真机部署，以及相关自动化部署工具开发。", "relation": "OWNED"}]