
## N0353 CN_PAXINI RF_ML_AI_ENGINEERING 强化学习研究员
TASK ROBOT_MODEL RL_RESEARCH_GENERAL_APPLICATION
REVIEW ["CATALOG_BOUNDARY"]
F1 工作职责
F2 ① 算法研发：设计、实现和优化基于强化学习的算法，解决实际业务中的复杂问题。 
F3 ② 实验与评估：进行实验设计、模型训练和调优，评估算法在各种环境中的性能，并改进模型表现。 
F4 ③ 跨团队协作：与数据科学家、工程师、产品经理等核心研发团队合作，确保算法能够在实际产品中稳定运行。
F5 ④ 技术前沿探索：关注强化学习领域的最新研究进展，持续探索创新方法，并将其应用于实际项目中。 
F6 ⑤ 代码质量与可维护性：编写高质量、易维护的代码，保证算法的可复现性和扩展性。
F8 任职资格
F9 ① 教育背景：计算机科学、人工智能、数学或相关领域的硕士及以上学历，具有扎实的理论基础和数学功底。
F10 ② 强化学习经验：至少2年以上强化学习算法相关的研究或工程实践经验，熟悉强化学习的经典算法（如Q-learning、DQN、PPO、A3C等）。
F11 ③ 编程能力：精通至少一种编程语言（如Python、C++等），熟悉TensorFlow、PyTorch等深度学习框架，具备较强的代码实现能力。
F12 ④ 数学和统计学能力：对机器学习、优化理论、统计学等有深刻理解，具备良好的数学建模和算法分析能力。
F13 ⑤ 解决问题能力：能够独立分析问题、设计实验并提出有效解决方案，具有较强的动手能力和创新能力。
F14 ⑥ 良好的团队合作精神：具备良好的沟通能力，能够与跨学科团队成员协作，推动项目进展。 
F16  优先考虑：具有强化学习在实际应用中的经验（如自动驾驶、机器人控制、金融交易等）。  有学术论文发表或技术专利。 熟悉分布式计算和云平台（如AWS、Google Cloud等）。
EV N0353:O1 SK_GENERIC_LANGUAGE GENERAL/UNCONDITIONAL @F11
EV N0353:O2 SK_PYTHON GENERAL/EXAMPLE @F11
EV N0353:O3 SK_CPP GENERAL/EXAMPLE @F11
EV N0353:O4 SK_GENERIC_ML_FRAMEWORK GENERAL/UNCONDITIONAL @F11
EV N0353:O5 SK_TENSORFLOW GENERAL/EXAMPLE @F11
EV N0353:O6 SK_PYTORCH GENERAL/EXAMPLE @F11
EV N0353:O7 TC_RL DUTY_OWN_DEVELOP/UNCONDITIONAL @F2
EV N0353:O8 TC_EVALUATION DUTY_OWN_USE/UNCONDITIONAL @F3
EV N0353:O9 TC_RL GENERAL/UNCONDITIONAL @F10
EV N0353:O10 TC_ML_MODELS GENERAL/UNCONDITIONAL @F12
EV N0353:O11 TC_RL PREFERRED/UNCONDITIONAL @F16
EV N0353:O12 TC_CONTROL PREFERRED/EXAMPLE @F16
EV N0353:6:0 V2_AWS PREFERRED/EXAMPLE @F16
EV N0353:6:1 V2_GCP PREFERRED/EXAMPLE @F16
CAND N0353:1 OUTSIDE:Q-learning为RL算法示例。 @F10
CAND N0353:2 OUTSIDE:DQN。 @F10
CAND N0353:3 OUTSIDE:PPO。 @F10
CAND N0353:4 OUTSIDE:A3C。 @F10
CAND N0353:5 REJECT:Python、C++等不是C语言；语言示例保持示例分支。 @F11
NOTES RL研究岗，优先经验含机器人控制但正文未限定只做机器人策略。云平台为优先示例。