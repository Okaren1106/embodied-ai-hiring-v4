# 本轮9条新增证据入表

逐条来源均已打开正文；同一TWIST2论文同时解释FAR研究产物和宇树G1实际使用，只增加证据记录，不增加独立来源数量。

| 证据ID | 公司 | 发布日 | 保存方式 | 原文 |
|---|---|---|---|---|
| NEW_AGIBOT_01 | CN_AGIBOT | 2026-03-31 | ORIGINAL_HTTP_BYTES | [智元第10000台通用具身机器人正式下线](https://www.agibot.com.cn/article/315/detail/147.html) |
| NEW_DEEP_01 | CN_DEEPROBOTICS | 2025-03-04 | ORIGINAL_HTTP_BYTES | [X30 robot dog pioneers smart inspection in Singapore power cable tunnel](https://www.deeprobotics.cn/en/wap/article/id/241.html) |
| NEW_DEEP_02 | CN_DEEPROBOTICS | 2024-11-27 | ORIGINAL_HTTP_BYTES | [How this technical officer and robot SPock hunt hazards to protect Singapore power tunnels](https://www.spgroup.com.sg/about-us/media-resources/energy-hub/reliability/How-this-technical-officer-and-robot-SPock-hunt-hazards-to-protect-Singapore-power-tunnels) |
| NEW_LIMX_01 | CN_LIMX | 2024-10-16 | ORIGINAL_HTTP_BYTES | [新品上市：逐际动力发售多形态双足机器人TRON 1](https://www.limxdynamics.com/zh/news/BK000014) |
| NEW_SPIRIT_01 | CN_SPIRITAI | 2025-12-17 | WEB_TOOL_EXTRACT | [宁德时代落地人形机器人动力电池PACK生产线](https://www.cls.cn/detail/2232711) |
| NEW_GALAXEA_01 | CN_GALAXEA | 未知 | ORIGINAL_HTTP_BYTES | [星海图R1产品页](https://www.galaxea-ai.com/cn/products/R1) |
| NEW_UNITREE_01 | CN_UNITREE | 2025-11 | ORIGINAL_HTTP_BYTES | [TWIST2固定v1论文：实验本体为Unitree G1](https://arxiv.org/html/2511.02832v1) |
| NEW_UNITREE_02 | CN_UNITREE | 未知 | ORIGINAL_HTTP_BYTES | [Advanced Quadruped Inspection Solutions](https://www.unitree.com/industry/electricity/) |
| NEW_GALBOT_01 | CN_GALBOT | 2026-06-24 | WEB_TOOL_EXTRACT | [首款搭载宁德时代电池的重载人形机器人上岗](https://www.catl.com/news/10053.html) |

- 全量变更：`supplement_records/ingestion.json`（研究源变更）及`fact_delta.json`（最终表变更）。
- 原始字节、正文、读取记录：`evidence_snapshots/NEW_*`。
- 首次受限环境直连失败，随后经网络权限审核执行公开来源下载；7成功、2 TLS失败，后者使用已实际读取的web工具正文。没有自动审批拒绝导致的未完成事项。
- 搜索结果与失败导航保留在原验收目录`web_records/`，新增HTTP请求结果保存于`supplement_records/NEW_*.fetch.json`。
