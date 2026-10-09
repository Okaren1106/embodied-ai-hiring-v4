# Complete current-U modifier-scope consistency review

All 46 v3-current Q=U pairs from 44 advertisements were reviewed using the complete captured descriptions. Every target-bearing line in every other captured field was checked against the reviewed description after normalization. This is a post hoc model review, not independent human validation. This module preserves the frozen review frame and does not edit accepted states. All five proposals below were subsequently adopted in `data/v4_source_corrections.json`; their exact propagation is checked separately by `verify_v4_overlay_independent.py`.

The review proposes five U→Z corrections: N0508/PyTorch and E0071/C++ under the existing EXAMPLE rule; N0634/C++, E0549/C++ and E0560/C++ under explicit CHOICE scope. The remaining 41 original pairs retain U. Adopting these five yielded the phase-four total of 170 P, 285 Z and 41 U in the fixed 496-pair frame. A subsequent bounded parenthetical review moved two formerly resolved pairs to U, producing the current seven-correction total of 169 P, 284 Z and 43 U. All mention states, tasks and advertisements remain fixed. This review ledger deliberately retains each original U and the proposal that motivated its correction; the later review is documented separately in `bare_parenthetical_source_review.md`.

The decisive duplicate is N0508 against N0486/A099: every captured body field is byte-for-byte identical, while titles differ. Their shared text says ‘熟练掌握Python/C++中的至少一种编程语言，熟悉PyTorch/TensorFlow等深度学习框架’. N0486 received the v3 explicit-example clarification, but N0508 retained U. No additional unconditional PyTorch statement appears in either source. Applying the same modifier rule requires propagation in the new analysis layer, with the original v3 archive preserved.

Explicit outer choices or examples govern nested unresolved slash expressions. For N0634, Python can satisfy the ‘C/C++或Python’ alternative. For E0071, the entire ‘C/C++、MATLAB、Python等编程语言’ expression is an illustrative language list under the current rule. The two Figure advertisements use an identical list ending ‘Python or similar’; the alternative governs the list, not merely the spelling of the C/C++ item. These proposals do not infer employer behavior; they apply the existing narrow-Q construct consistently.

Scope is local. The review deliberately does not move an example marker from a neighboring PyTorch clause onto an earlier Python/C++ predicate. Nor does it turn C into C++, infer a mandatory framework from a qualification heading alone, or expand bare slash constructions using technical knowledge. Bare Python/PyTorch and Qt/C++ stacks remain unresolved under the primary rule and may enter separately identified readings.

The prior resolved analogues are preserved with exact parent spans in `current_u_rule_analogues.csv`: N0489 treats a language slash inside an explicit at-least-one operator as CHOICE/Z; N0473 treats C++ 或 Python as CHOICE/Z; N0199 treats a language list ending C/C++等 as EXAMPLE/Z for its Python target; E0599 and N0927 treat comma-separated language lists with final or as CHOICE/Z; N0876 treats PyTorch (or similar frameworks) as CHOICE/Z. N0011 is a counterexample: C/C++ appears together with a separate ‘了解现代C++常用特性’ qualification, so Q=P is supported despite the slash. These analogues establish scope priority under existing practice, not a universal rule that every slash is negative. N0486's old evidence branch is still UNRESOLVED; its current Z comes from the explicit v3 A099 adjudication.

The five proposed changes should be propagated into any Q thresholds, company eligibility, paired bounds, expanded-example/choice measures and semantic scenarios. The three choice cases enter the choice-inclusive construct; the two example cases enter the example-inclusive construct. H remains one for all five. Do not selectively implement only the duplicate or only changes that leave a preferred result intact.

## UREV_001 — N0431 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_AGIBOT|feishu|7571379728977840425|48a3fa66237ff87580ad23f1011767df4017b49e5d0b00f090f4e13239c17e7d`

Title: 系统架构师-软件算法. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [317, 370), recorded GENERAL/UNRESOLVED:

> 3. 了解SoC架构，了解Linux内核及驱动，精通C/C++，精通操作系统框架、中间件、底层HAL开发；

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 499 characters; SHA-256 `b93ca0d4b29ddb48c0397673389df75164abdac4b1ab3b3cf39e72053823d423`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_002 — N0508 — SK_PYTORCH

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_DEEPROBOTICS|moka|3e4c2387-4458-4b6f-a19c-f30efc7dcd8d|fa3ae951c64a2eccb531674abf23a7d1ec24f9fd7c47fad6d2d76691a90a633e`

Title: 运动控制算法工程师. Existing G/R/Q: U/Z/U. Action: **PROPOSE_U_TO_Z**.

`full_description` [211, 266), recorded GENERAL/UNRESOLVED:

> 3.熟练掌握Python/C++中的至少一种编程语言，熟悉PyTorch/TensorFlow等深度学习框架；

Review: The complete captured body is identical to N0486/A099, including the same qualification clause. The already-adjudicated 等 framework example must govern the unresolved slash inside that example. No other unconditional PyTorch qualification occurs.

Full captured body: 427 characters; SHA-256 `8a926195f9532332d64bf2460b6fd9040476295d97eeb5fd6d62b8940e7e3189`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_003 — N0509 — SK_PYTHON

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_DEEPROBOTICS|moka|53e81110-ad1d-48b2-936c-862bfee55b9a|6e66a39c6b4ecb8eb2b2baa30d1c0e1e12a54d8f23f4df13c32c1f8ba65e73d6`

Title: 算法工程师（具身操作）. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [188, 251), recorded GENERAL/UNRESOLVED:

> 2、熟练掌握编程语言（Python / C++），并有丰富的深度学习框架使用经验（如Pytorch, TensorFlow）；

Review: The target appears in an unexpanded programming-language slash. Example or choice markers in a neighboring framework clause or later proficiency phrase have their own predicate/scope and must not be transferred onto this target. No separate unconditional target qualification was found. Retain U.

Full captured body: 301 characters; SHA-256 `93475b5af45fed14f0db2def06ebb747461c26caf0ad803333e20dffc6e56ba2`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_004 — N0634 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_GALAXEA|zhiye|01de9cb5-764a-46b7-a7da-d9dba47e4a89|4d4579d3f706d58875bab80cc3a4b914cf4750c610db5bd790b977f5f19cd834`

Title: 人机交互系统资深工程师. Existing G/R/Q: U/Z/U. Action: **PROPOSE_U_TO_Z**.

`full_description` [413, 469), recorded GENERAL/UNRESOLVED:

> 3、具备Linux环境下的C/C++或Python开发能力，能独立完成SDK的接口封装、业务逻辑联调及性能优化。

Review: The full local requirement is C/C++或Python. The explicit outer 或 admits Python instead of the C/C++ expression, so uncertainty within the slash cannot establish an unconditional C++ item. No separate unconditional C++ occurrence appears.

Full captured body: 749 characters; SHA-256 `74ab251a1b900dc940f12b10559b1985b942c158409eeefa9c5e0461d64bfa9a`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_005 — N0633 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_GALAXEA|zhiye|33b17fb8-abcc-407b-89ec-7849ab1985a5|e5b13ab45af44c04c898a457ddf25798a75f1e89fa88abb47a44f6b36f3d870d`

Title: 高级工程师（qt方向）. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [437, 476), recorded GENERAL/UNRESOLVED:

> 2. 经验背景：3年以上Qt/C++开发经验，有完整的上位机软件项目交付经历。

Review: Qt/C++ can denote a technical stack, but the slash is unexpanded and no explicit inclusive operator or separate C++ qualification resolves it. Retain the existing primary U and its recorded alternative reading.

Full captured body: 729 characters; SHA-256 `e2c4d5bb6970c62692198fb051a67a5ee77dad13edcd14fa25e504e1e4e39094`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_006 — N0621 — SK_PYTHON

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_GALAXEA|zhiye|75a7b690-7523-4544-8006-ce045bea94f7|ceba718b75f34cc99ccf3e8234b18b73d24934e1dcbdfc5c293e93433b12c296`

Title: 基础模型算法实习生（27届实习）. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [1013, 1049), recorded GENERAL/UNRESOLVED:

> 2、具备扎实的Python/C++编程能力，良好的代码规范和工程实现能力

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 1296 characters; SHA-256 `eefd72fe496ecb2f892956615b1e62eaa8064cbf0a6f84b36401d9c5731b3162`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_007 — N0619 — SK_PYTHON

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_GALAXEA|zhiye|cbd1e6d0-f11f-46b6-97c3-02cacaad6d2a|99d576257a7c887ce24fe0c2e0d2007a0d68f6171172d0751ec9d4dcfb6925ce`

Title: 具身智能算法工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [1027, 1072), recorded GENERAL/UNRESOLVED:

> 扎实的 Python/C++ 功底，熟悉 CUDA 编程、模型量化/蒸馏/推理加速者优先；

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 1125 characters; SHA-256 `676fbe2ecb9f73bb74e590e000c38b965379b134e15772c36cf777aeba831276`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_008 — N0654 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_GALAXEA|zhiye|ea6d3ee6-62ad-4232-bb5b-328dec599e63|cf5b29e367b8bcee7d964d1b4f13b5e556502fd067eb41d46d434b1b599083c3`

Title: 应用开发工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [455, 515), recorded GENERAL/UNRESOLVED:

> 3. 熟练使用 C++/Python 进行开发，熟悉 Linux 开发环境，掌握 ROS/ROS2 或 Qt 开发优先。

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 838 characters; SHA-256 `f0b33d7bc9d2d6bb78aabbd404fad3f88a4b67a5415f93367af81ef480c9e7c4`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_009 — N0628 — SK_PYTHON

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_GALAXEA|zhiye|ef9981de-d0b1-449c-be9e-5819b585de4a|c7f641f0f7182ea714d59359a0b57774ab69c5df562a5ff96a7eb691ec6a05c8`

Title: RL运控算法工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [335, 397), recorded GENERAL/UNRESOLVED:

> - 技能工具：熟练使用Python/C++、PyTorch，掌握MuJoCo、Isaac Gym仿真平台及ROS机器人框架。

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 444 characters; SHA-256 `f02597fff1ddc42f58af85c671a5ab0e1d78869555477a7385e7a9834f6a334e`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_010 — N0095 — SK_LINUX

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_GALBOT|moka|106afaad-a17d-47cb-9a8b-f764d3746190|02d7e2451c608f2533377005f36cd64f3c99a67764730f914b6022280c249317`

Title: 人形机器人系统开发工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [296, 324), recorded GENERAL/UNRESOLVED:

> - 熟悉Linux/Unix系统，了解系统调用和内核机制

Review: Linux/Unix is an unexpanded slash expression. The separate unconditional C++ and C clause does not resolve the operating-system relation. Retain U.

Full captured body: 445 characters; SHA-256 `908d6ab9127a2b49c92d1d7bdc37f6a4cc95bc057dfe4fdf947272015a43b163`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_011 — N0173 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_GALBOT|moka|10eacc31-a1bb-4779-8c3f-fcda27db3688|30a2ec19bb7092c1174951e8f06b0751ad7c924bccb409d354bf8f71c44499fb`

Title: 中间件软件高级工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [75, 109), recorded SEPARATE/COLLABORATION_OBJECT:

> 2.支持C++/python语言下系统/控制等模块工具链相关搭建 ；

`full_description` [220, 255), recorded GENERAL/UNRESOLVED:

> 2.熟练掌握 C/C++编程，有5年以上的面向对象软件设计和开发经验；

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 437 characters; SHA-256 `c2e5c8f26387ff28cb5a47f2200c402811273f1fbcc1b1c8cf3036e1200e40f1`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_012 — N0009 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_GALBOT|moka|2bbec48f-96e7-4999-8126-d3b3c371d689|9d2fe425758bec387ca4b90f61fe0c1048e40cfa8345b5ee172681017e716ccc`

Title: 机器人系统软件开发工程师-27届校招. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [193, 227), recorded GENERAL/UNRESOLVED:

> 2、熟练掌握Linux环境下C/C++编程，熟悉常用数据结构和算法；

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 330 characters; SHA-256 `9cc5be8f86af9efeef58088b913eccad7dbe279b89f195a439ef8ce0163be6a6`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_013 — N0158 — SK_PYTHON

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_GALBOT|moka|6d7045d4-9874-4963-8793-35595f868889|d49bf2201e8038d060165342e4f65612726f34ede16d3f11676d329ddcb092e4`

Title: 强化学习算法工程师-苏州. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [659, 722), recorded GENERAL/UNRESOLVED:

> 扎实的工程能力： 优秀的Python/C++编程能力，熟悉Linux开发环境，具备良好的代码风格和工程化习惯。        

Review: The target appears in an unexpanded programming-language slash. Example or choice markers in a neighboring framework clause or later proficiency phrase have their own predicate/scope and must not be transferred onto this target. No separate unconditional target qualification was found. Retain U.

Full captured body: 876 characters; SHA-256 `0f29fa17e3c73bee7939ac57d4cd26bc3b2849adfef2d44eddacac95335f63b9`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_014 — N0149 — SK_PYTORCH

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_GALBOT|moka|9a4ce845-16a9-4033-93d7-b216ce7e0122|af9ef603462dc1272c2366d25655615c2be9423ed4dae753478bab7c88e20f76`

Title: 具身大模型算法专家（VLA/VLM）-苏州. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [243, 297), recorded GENERAL/UNRESOLVED:

> 熟练使用PyTorch/TensorFlow，大规模分布式训练及模型部署（TensorRT，ONNX）。  

Review: The framework slash has no explicit governing example or alternative operator in its own clause. Retain U; an optional alternative interpretation is not a compelled correction.

Full captured body: 346 characters; SHA-256 `b19581339ae50a462a3d7c81f072ae47f2c7809572eca5d806e1b9c6362824ca`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_015 — N0035 — SK_PYTHON

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_GALBOT|moka|a8c37b66-5356-45d9-9b85-8d7b40c45586|8f76406f6e97bd7e04a07b99184bc6adf9b156affdedcfbbb95af47a034c62bb`

Title: 强化学习算法工程师-工业方向. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [393, 448), recorded GENERAL/UNRESOLVED:

> 扎实的工程能力： 优秀的Python/C++编程能力，熟悉Linux开发环境，具备良好的代码风格和工程化习惯。

Review: The target appears in an unexpanded programming-language slash. Example or choice markers in a neighboring framework clause or later proficiency phrase have their own predicate/scope and must not be transferred onto this target. No separate unconditional target qualification was found. Retain U.

Full captured body: 599 characters; SHA-256 `b72cec83a674ed8d4478cba832588d4415eed4989f5051c49fb438f515fed91f`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_016 — N0175 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_GALBOT|moka|b6936723-356c-4729-8349-3481dc52364c|d7c10b7faa57a014f4a849261454c7046832974abda6c7f575e7fc3b16e8a2e7`

Title: 机器人系统软件开发工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [170, 204), recorded GENERAL/UNRESOLVED:

> 2、熟练掌握Linux环境下C/C++编程，熟悉常用数据结构和算法；

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 355 characters; SHA-256 `02e752bb6d635539140df94244564fc8201d29cd758d964d680d275513e72eab`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_017 — N0029 — SK_PYTORCH

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_GALBOT|moka|bde310a9-790b-4a24-aa6e-735dbb28d9a7|d3f573e821816d122a3657d936e43f102119d1722e0209664e2eaa85792323e1`

Title: 具身大模型后训练算法工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [437, 512), recorded GENERAL/UNRESOLVED:

> 2、熟练使用Python，熟悉PyTorch/Jax深度学习框架，有完整的VLA/WAM/VLM训练、部署、微调经验，有模型加速、推理优化经验者优先。

Review: The framework slash has no explicit governing example or alternative operator in its own clause. Retain U; an optional alternative interpretation is not a compelled correction.

Full captured body: 797 characters; SHA-256 `ff422ba2fc273a2c57d4c7d7e9dc585003ffa7e54540e052041cd46e11094e69`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_018 — N0010 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_GALBOT|moka|cb550f85-d1d7-4189-be4f-2dbf046541e6|4d4396d45bf74e2f4a104a6bf5175a1f19c4a7d44d9bbc42552a3065c2f91bf6`

Title: 机器人基础软件开发工程-27届校招. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [161, 190), recorded GENERAL/UNRESOLVED:

> 6.熟悉 C/C++，具备良好的数据结构、算法及编程基础；

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 337 characters; SHA-256 `e9a90ba2c7a22a6450fc240600a9154f347e2f046a220109505a34eaf235f822`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_019 — N0024 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_GALBOT|moka|f7d9d2ed-2106-4618-a98f-b2084fbcfc37|da920e0eb817cd77808f39f66bbf2a75902c7cba8978b76940268a4668348c94`

Title: 应用开发工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [330, 398), recorded GENERAL/UNRESOLVED:

> 3、精通 C++/Python 编程语言，具备 Linux 环境下的开发经验，编码规范良好；熟悉 ROS1/ROS2 框架及相关工具链。

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 505 characters; SHA-256 `a645508343f4208de4a70567c7e988ba59f2f851eeb99e5567bce244c1252209`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_020 — N0573 — SK_PYTHON

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_LIMX|feishu|7654151446108571958|fb3e31879317c49e25f72410c6f9874266b6e1e46f30b9b4a64c941007ebc246`

Title: 具身智能算法工程师（VLA 模型训练与部署）. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [340, 395), recorded GENERAL/UNRESOLVED:

> - 具备扎实的工程能力，熟悉 Python / PyTorch，能够独立完成模型训练、推理、调试与工程化开发。

Review: Bare Python / PyTorch wording can denote a joint implementation stack or an alternative/list relation. It contains no explicit governing example/choice operator. Retain U rather than resolve it from general technical knowledge; both target states should be considered jointly in any later reading scenario.

Full captured body: 1134 characters; SHA-256 `adcf45628ec021b81c6eb00f196f96c2461aae271c71454562be006f6a9921c5`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_021 — N0573 — SK_PYTORCH

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_LIMX|feishu|7654151446108571958|fb3e31879317c49e25f72410c6f9874266b6e1e46f30b9b4a64c941007ebc246`

Title: 具身智能算法工程师（VLA 模型训练与部署）. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [340, 395), recorded GENERAL/UNRESOLVED:

> - 具备扎实的工程能力，熟悉 Python / PyTorch，能够独立完成模型训练、推理、调试与工程化开发。

Review: Bare Python / PyTorch wording can denote a joint implementation stack or an alternative/list relation. It contains no explicit governing example/choice operator. Retain U rather than resolve it from general technical knowledge; both target states should be considered jointly in any later reading scenario.

Full captured body: 1134 characters; SHA-256 `adcf45628ec021b81c6eb00f196f96c2461aae271c71454562be006f6a9921c5`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_022 — E0008 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_NOETIX|noetix|4|bf9b354d9e7f73d64df21e6385492e71f7120ff2274622d5e08b6abc2f997266`

Title: 嵌入式linux软件工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`requirements` [38, 72), recorded GENERAL/UNRESOLVED:

> 2、熟练掌握C/C++编程,具有独立设计开发能力,善于解决疑难问题;

Review: The target C++ remains inside C/C++; the additional requirement explicitly names C语言, not C++. Do not substitute the distinct C language for the selected C++ target. Retain U.

Full captured body: 436 characters; SHA-256 `fc63de15a1f751837baf493d7d8285bd782a7effde13e9044809951c403e22d6`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_023 — N0315 — SK_PYTHON

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_PAXINI|zhiye|43a8a952-de51-4dc0-a845-5738bb08d3f7|61d4bab25f091e0ce9362c4eee767e89852a3e97f4dc7473d4fd0df836bdbc10`

Title: 具身智能算法工程师（预训练方向）. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [297, 355), recorded GENERAL/UNRESOLVED:

> 2.技术栈： 精通Python/C++，Pytorch；有大模型（LLM/VLM）全参数微调或预训练实战经验者优先。

Review: The target appears in an unexpanded programming-language slash. Example or choice markers in a neighboring framework clause or later proficiency phrase have their own predicate/scope and must not be transferred onto this target. No separate unconditional target qualification was found. Retain U.

Full captured body: 457 characters; SHA-256 `0e3f2d7f78dd97642a7d8c7ff6c865cb9be5851131af4eb44ef34e5aed57e99a`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_024 — N0320 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_PAXINI|zhiye|64d86c36-5cf2-44a7-a09d-06136ad43951|739cb1af58e77969bc3a00c811425e6a5605b9b3fc1e63000d922cd5a056d512`

Title: linux 嵌入式开发. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [369, 425), recorded GENERAL/UNRESOLVED:

> 2. 熟悉C/C++程序设计和常用的开发工具（GCC/GDB/Makefile/Git等），具备良好的编程习惯。

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 633 characters; SHA-256 `ef775cc67414162382a440257a4c7dcde9f9f91f1edfc31413d5f62612961792`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_025 — N0289 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_PAXINI|zhiye|e35c0894-1802-48e8-bec4-458d2355b934|d0fc1751baac0c6d9ab6614a5f28a64816dbf8cf90d72d540591ed9dfb78f121`

Title: linux 系统嵌入式工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [369, 425), recorded GENERAL/UNRESOLVED:

> 2. 熟悉C/C++程序设计和常用的开发工具（GCC/GDB/Makefile/Git等），具备良好的编程习惯。

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 859 characters; SHA-256 `21339888d9bdf464158f59194103c7e106c1d6cdc3eaa19c9040efd51cf5b793`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_026 — N0314 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_PAXINI|zhiye|ecb8f73a-891c-424d-811e-128731fda5a3|59fcca8b555ddfe4629601878a576a69166015547224b7fae051d3df855610af`

Title: 运控助理算法工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [181, 220), recorded GENERAL/UNRESOLVED:

> 2. 熟练掌握 C++/Python，熟悉 ROS/ROS2 框架及常用组件；

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 286 characters; SHA-256 `8ad3e7efa09c473a46e2fc96a0759e538b7b25a7f1e6c932cf8370a949891f52`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_027 — N0337 — SK_PYTHON

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_PAXINI|zhiye|ed1ede63-7812-4095-8341-233b04422ddc|b3513cba80bacf3c9aacf91b1a51cd2e014bb2994e6e8c8441bdf739e710dcbb`

Title: 具身智能算法工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`full_description` [348, 406), recorded GENERAL/UNRESOLVED:

> 2.精通Python/C++及Linux开发,熟练掌握Pytorch或TensorFlow,具备扎实的工程实现能力。

Review: The target appears in an unexpanded programming-language slash. Example or choice markers in a neighboring framework clause or later proficiency phrase have their own predicate/scope and must not be transferred onto this target. No separate unconditional target qualification was found. Retain U.

Full captured body: 560 characters; SHA-256 `7017fd39aa987682b2a2538e54a74fea29c1b3b22549212f673b19b4d6c47209`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_028 — E0071 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_SPIRITAI|feishu|7582838800151316772|745eddbd9aba24741841cbd043c3b25acbc613697c77022e39f377612e4d5c75`

Title: 机器人远程遥操系统开发. Existing G/R/Q: U/Z/U. Action: **PROPOSE_U_TO_Z**.

`requirements` [165, 211), recorded GENERAL/UNRESOLVED:

> 5、熟练掌握C/C++、MATLAB、Python等编程语言,熟练使用ROS/ROS2系统。

Review: The qualification clause is C/C++、MATLAB、Python等编程语言. Under the frozen 等-as-example rule, the outer language-example list governs C++ regardless of the inner C/C++ slash. No separate unconditional C++ qualification appears.

Full captured body: 509 characters; SHA-256 `da9dcb33dad010804b1ceb803ea57b44646b1a53cd406d07b69b827966eb6e0d`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_029 — E0043 — SK_PYTHON

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_SPIRITAI|feishu|7649642803568445742|badc2632c8a1f9c8626518c39b42c803899b45de10543bf21f49f26340b69993`

Title: 多模态世界模型算法工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`requirements` [44, 106), recorded GENERAL/UNRESOLVED:

> 2、具备扎实的深度学习和大模型基础,熟练掌握 Python / PyTorch,具备较强的论文复现、模型训练和工程实现能力。

Review: Bare Python / PyTorch wording can denote a joint implementation stack or an alternative/list relation. It contains no explicit governing example/choice operator. Retain U rather than resolve it from general technical knowledge; both target states should be considered jointly in any later reading scenario.

Full captured body: 1004 characters; SHA-256 `fc72145fed9eccefb34ca375e6237a80d8f1a3ba10780a0d4925f4df639227e1`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_030 — E0043 — SK_PYTORCH

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_SPIRITAI|feishu|7649642803568445742|badc2632c8a1f9c8626518c39b42c803899b45de10543bf21f49f26340b69993`

Title: 多模态世界模型算法工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`requirements` [44, 106), recorded GENERAL/UNRESOLVED:

> 2、具备扎实的深度学习和大模型基础,熟练掌握 Python / PyTorch,具备较强的论文复现、模型训练和工程实现能力。

Review: Bare Python / PyTorch wording can denote a joint implementation stack or an alternative/list relation. It contains no explicit governing example/choice operator. Retain U rather than resolve it from general technical knowledge; both target states should be considered jointly in any later reading scenario.

Full captured body: 1004 characters; SHA-256 `fc72145fed9eccefb34ca375e6237a80d8f1a3ba10780a0d4925f4df639227e1`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_031 — E0017 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_SPIRITAI|feishu|7677495021566265638|09f1c113ff59711d9bf4a6a2c5624836f06ca9a7209c572ff1c481dcb45f4268`

Title: 端侧计算性能优化专家. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`duties` [127, 233), recorded DUTY_OWN_USE/UNRESOLVED:

> 深入核心代码和计算链路,开展 C/C++、SIMD、Cache、Memory、多线程等底层优化;针对计算密集度高的模块能使用Cadence DSP、Mali GPU 等异构计算IP进行优化,充分发挥芯片计算能力。

`full_description` [614, 655), recorded GENERAL/UNRESOLVED:

> 3.精通C/C++，具备较强的并发、Memory、Cache、SIMD等底层能力。

Review: Several C/C++ occurrences exist in duties and qualifications, including C/C++/系统软件/高性能计算 and 精通C/C++. None resolves the internal language slash; duty scope does not supply an unconditional qualification. Retain U.

Full captured body: 1159 characters; SHA-256 `c1ace50fcc518359114a66e3ba1b6c88044fbb66a3614bc43ac54602c4df9874`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_032 — E0284 — SK_PYTHON

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_XSQUARE|feishu|7524261545276590363|538b789c5a2b27562e6ea288b09569343e2be1e90506b43c5ad4a6dfbc138cb3`

Title: 具身基础模型应用工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`requirements` [43, 91), recorded GENERAL/UNRESOLVED:

> 2.熟练使用Python/C++,精通PyTorch等主流深度学习框架,具备扎实的工程实现能力;

Review: The target appears in an unexpanded programming-language slash. Example or choice markers in a neighboring framework clause or later proficiency phrase have their own predicate/scope and must not be transferred onto this target. No separate unconditional target qualification was found. Retain U.

Full captured body: 1227 characters; SHA-256 `7355834a7cdf0acd40cbf051cf20438d792a49bcaddf6dc22c2ea4523251ef4f`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_033 — E0275 — SK_PYTHON

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_XSQUARE|feishu|7533570320353233190|ae8f0c0a7789bed4a90b5fec1c2f67669da40dd087787e742ce09bf052d983f5`

Title: 导航模型算法工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`requirements` [50, 115), recorded GENERAL/UNRESOLVED:

> 2. 熟练掌握 Python/C++,精通 PyTorch、JAX 等至少一种主流深度学习框架,具备良好的工程实践能力与调试习惯;

Review: The target appears in an unexpanded programming-language slash. Example or choice markers in a neighboring framework clause or later proficiency phrase have their own predicate/scope and must not be transferred onto this target. No separate unconditional target qualification was found. Retain U.

Full captured body: 930 characters; SHA-256 `c37acf4aee8a60466cdbf40e9082814aea5c0018a4c44734c617c1f53b96d851`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_034 — E0238 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_XSQUARE|feishu|7595550199419668787|42b5370d04bce60b0e52f2a0885f58334a2eceda10ecb612b3f93a138688cf70`

Title: 嵌入式软件工程师（Linux）. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`requirements` [82, 118), recorded GENERAL/UNRESOLVED:

> 2、精通 C/C++ 编程语言,熟悉 ROS 2 的基本架构与常用功能;

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 525 characters; SHA-256 `f056037ff6102ce6c7bacc6912cca81db7067a01ef555ca276d63f0911541b33`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_035 — E0235 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_XSQUARE|feishu|7597270667700832522|52173741079c17d278ec49bb57081c21f1481684320ee718c14f2cf2cc81e7de`

Title: 系统集成工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`requirements` [51, 100), recorded GENERAL/UNRESOLVED:

> - 熟悉C++/Python,熟悉实时内核配置与进程调度优化,具备扎实的多线程编程与性能调优能力。

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 545 characters; SHA-256 `4a572dabe91dcd2b0a91bbbc4f4b7021d24fe74aec7e3cacc7a71efa8bd0dc2c`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_036 — E0217 — SK_PYTHON

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_XSQUARE|feishu|7620028379181746495|253735b3b1a2cc1747aa3ec5c5297514291718a8be85c014a865d4f638ea37ef`

Title: 具身大模型后训练工程师（场景应用）. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`requirements` [43, 91), recorded GENERAL/UNRESOLVED:

> 2.熟练使用Python/C++,精通PyTorch等主流深度学习框架,具备扎实的工程实现能力;

Review: The target appears in an unexpanded programming-language slash. Example or choice markers in a neighboring framework clause or later proficiency phrase have their own predicate/scope and must not be transferred onto this target. No separate unconditional target qualification was found. Retain U.

Full captured body: 998 characters; SHA-256 `b6be2604afc2dd665f9c949465a06e57ad095f69e26b560d19ebd16bf67ddf87`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_037 — E0191 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_XSQUARE|feishu|7637527030159067433|95e9557ef07586a4f998f0a7ccf91619ac25a90658ff9203e3845b593e73d56a`

Title: 边缘容器工程师（机器人方向）. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`requirements` [193, 230), recorded GENERAL/UNRESOLVED:

> 4.  熟练掌握 Go、C/C++ 开发,具备良好的代码设计和编写习惯; 

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 669 characters; SHA-256 `b393ec8500e45c6212e2eb1ce9936eff40ca45aa29b663aeb4d023df5c80a51c`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_038 — E0190 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_XSQUARE|feishu|7637529176862279972|f8f3d4e6a20f0d108ec8f8a32091d29e8b1f41926db5807d1e8692e3b3aa0505`

Title: 机器人基础软件开发工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`requirements` [35, 96), recorded GENERAL/UNRESOLVED:

> 2、熟练使用 C/C++、Rust 开发,具备 3 年以上机器人基础软件、机器人平台或嵌入式 Linux 系统开发经验。 

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 967 characters; SHA-256 `1075581c8bf4d16985598b2764978bcb725484f8ec943f47200a0d871ca99ca7`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_039 — E0175 — SK_PYTHON

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_XSQUARE|feishu|7646374217139423534|a1465ace03a26992864d6974a1f081ca738ab28f65913490276ec7b56a82b3c2`

Title: 具身基础模型研究员/工程师（移动操作方向）. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`requirements` [41, 101), recorded GENERAL/UNRESOLVED:

> 2.熟练掌握Python/C++编程,精通PyTorch、JAX等至少一种主流深度学习框架,具备扎实的算法工程实现能力;

Review: The target appears in an unexpanded programming-language slash. Example or choice markers in a neighboring framework clause or later proficiency phrase have their own predicate/scope and must not be transferred onto this target. No separate unconditional target qualification was found. Retain U.

Full captured body: 1304 characters; SHA-256 `98ab78ee123ec02ae0b3cd23d37f27bcef10aecd387f07885002395caf9556a0`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_040 — E0174 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_XSQUARE|feishu|7646618698996779310|7b9b900be00778ea9e5fd9adc383cdcd1f3ce865dd4deab2f506d8220f095463`

Title: 机器人音视频工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`requirements` [62, 123), recorded GENERAL/UNRESOLVED:

> 2. 精通C/C++,具备扎实的Linux系统编程能力,熟悉多线程、进科程间通信、内存管理、网络编程、线程调度和性能优化;

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 836 characters; SHA-256 `4d6a06b8af13a628799690cac9f68e0765a733705ca0753cbb243bacaedb2408`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_041 — E0169 — SK_PYTHON

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_XSQUARE|feishu|7649332135966738698|538b789c5a2b27562e6ea288b09569343e2be1e90506b43c5ad4a6dfbc138cb3`

Title: VLA算法工程师-产品落地方向. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`requirements` [43, 91), recorded GENERAL/UNRESOLVED:

> 2.熟练使用Python/C++,精通PyTorch等主流深度学习框架,具备扎实的工程实现能力;

Review: The target appears in an unexpanded programming-language slash. Example or choice markers in a neighboring framework clause or later proficiency phrase have their own predicate/scope and must not be transferred onto this target. No separate unconditional target qualification was found. Retain U.

Full captured body: 1227 characters; SHA-256 `7355834a7cdf0acd40cbf051cf20438d792a49bcaddf6dc22c2ea4523251ef4f`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_042 — E0168 — SK_PYTHON

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_XSQUARE|feishu|7649410444289132843|50b3d927910d4662402073457a105c36a973e0429f868f82f88a52865b82719f`

Title: 具身智能触觉算法工程师（强化微调与力控方向）. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`requirements` [130, 169), recorded GENERAL/UNRESOLVED:

> 4. 熟悉 Python/C++,具备良好的算法实现、实验调试和工程落地能力。

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 847 characters; SHA-256 `35b76822914fc58d1195555699c6a80a2c8c02f1c4d101b5547e719dbe0e7a9a`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_043 — E0157 — SK_PYTHON

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_XSQUARE|feishu|7659688826927761705|e47a644cdcb622e5fa7c55a7a2a315ef3c5bd6b0c197b618ad87159c9b7606a8`

Title: 具身大模型后训练工程师. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`requirements` [39, 78), recorded GENERAL/UNRESOLVED:

> 熟练使用Python/C++,精通PyTorch等深度学习框架,工程能力扎实;

Review: The target appears in an unexpanded programming-language slash. Example or choice markers in a neighboring framework clause or later proficiency phrase have their own predicate/scope and must not be transferred onto this target. No separate unconditional target qualification was found. Retain U.

Full captured body: 652 characters; SHA-256 `6ce4f327f16d840ec5aa12838acfe3e92fa76de870510aabdb8b864f98d1f218`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_044 — E0115 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_XSQUARE|feishu|7673810736703965503|3c4f441704aefd9711ca4ba2783525238a844691e3d046832a1aa3e0815f8462`

Title: 语音工程化工程师（机器人端侧）. Existing G/R/Q: U/Z/U. Action: **RETAIN_U**.

`requirements` [46, 100), recorded GENERAL/UNRESOLVED:

> 2. 精通C++/Python,具备扎实的面向对象编程思想,拥有复杂工程代码的维护、重构及疑难问题定位能力;

Review: The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.

Full captured body: 774 characters; SHA-256 `47402b99ce00cda0189d90017e737fee8a186b23b95b58d7c27c87302820f8d7`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_045 — E0549 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|US_FIGURE|greenhouse|4620050006|8f4ebdb40f6cf944322d788835146a1dbc0a7606c5e6da734fcf02d49c66f680`

Title: Security Engineer, Application Security. Existing G/R/Q: U/Z/U. Action: **PROPOSE_U_TO_Z**.

`requirements` [210, 316), recorded GENERAL/UNRESOLVED:

> Strong software engineering (not scripting or automation) skills in C/C++, Rust, Golang, Python or similar

Review: The complete language list ends C/C++, Rust, Golang, Python or similar. The explicit list-level alternative permits another language; treating the embedded C/C++ slash as unresolved does not erase the governing alternative. No other C++ qualification appears.

Full captured body: 2509 characters; SHA-256 `df2a12f93fc61e95060205ad0ce8674faae78f2911cb5e79b11f440bb772438d`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.

## UREV_046 — E0560 — SK_CPP

Identity: `REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|US_FIGURE|greenhouse|4690871006|6a364b0a2e375248bc101f6b0bf93eee236a50e41b294d03cea0a174c5f8da37`

Title: Software Engineer, Privacy & Data Governance. Existing G/R/Q: U/Z/U. Action: **PROPOSE_U_TO_Z**.

`requirements` [258, 364), recorded GENERAL/UNRESOLVED:

> Strong software engineering (not scripting or automation) skills in C/C++, Rust, Golang, Python or similar

Review: The complete language list ends C/C++, Rust, Golang, Python or similar, identically to E0549. The outer alternative governs the embedded slash. No other C++ qualification appears.

Full captured body: 2910 characters; SHA-256 `6ad8f450f41acda024be60aaea624fbd38827f9ab69625882fd2dcd89119bf81`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.
