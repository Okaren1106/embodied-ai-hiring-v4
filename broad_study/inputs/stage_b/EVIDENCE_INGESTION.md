# 16张审阅卡的证据入表对照

证据记录不是独立来源数量。同一网址可按不同说话者、产品或事件拆成多条证据断言。

| 审阅卡 | 公司 | 入表证据ID | 操作 | 保存方式 | 原文来源 |
|---|---|---|---|---|---|
| IR_NOETIX_01 | CN_NOETIX | IR_NOETIX_01 | NEW_EVIDENCE | ORIGINAL_HTTP_BYTES | [首程控股：北京机器人基金投资松延动力](https://www.hkexnews.hk/listedco/listconews/sehk/2025/0902/2025090201606.pdf) |
| IR_NOETIX_02 | CN_NOETIX | IR_NOETIX_02 | NEW_EVIDENCE | WEB_TOOL_EXTRACT | [松延动力智能机器人公益赋能怀柔山区教育](https://www.bjhr.gov.cn/zjhr/tzhr/gyxxh/202607/t20260703_4745938.html) |
| IR_NOETIX_03 | CN_NOETIX | IR_NOETIX_03 | NEW_EVIDENCE | WEB_TOOL_EXTRACT | [AI时代的清华电子力量：松延动力姜哲源](https://www.ee.tsinghua.edu.cn/info/1076/4958.htm) |
| IR_SPIRITAI_01 | CN_SPIRITAI | IR_SPIRITAI_01 | NEW_EVIDENCE | ORIGINAL_PDF_WITH_VISUAL_TRANSCRIPTION | [千寻智能三折页](https://www.worldrobotconference.com/profile/robot/download/2025/07/19/20250719155138000853_20250719155138A100.pdf) |
| IR_SPIRITAI_02 | CN_SPIRITAI | IR_SPIRITAI_02 | NEW_EVIDENCE | WEB_TOOL_EXTRACT | [遇见独角兽：千寻智能的北京故事](https://kw.beijing.gov.cn/ztzl/rdzt/kjrmt/202608/t20260812_4819478.html) |
| IR_SPIRITAI_03 | CN_SPIRITAI | IR_SPIRITAI_03 | NEW_EVIDENCE | WEB_TOOL_EXTRACT | [千寻智能推动具身智能从产线到家庭全场景延伸](https://www.ncsti.gov.cn/kjdt/scyq/zgckxc/zgcdt/202606/t20260623_250127.html) |
| IR_FAR_01 | US_AMAZON_FTR | IR_FAR_01 | NEW_EVIDENCE | ORIGINAL_HTTP_BYTES | [Amazon Fulfillment Technologies and Robotics teams](https://amazon.jobs/content/en/teams/ftr) |
| IR_FAR_02 | US_AMAZON_FTR | IR_FAR_02 | NEW_EVIDENCE | WEB_TOOL_EXTRACT | [TWIST2 固定 v1 论文](https://arxiv.org/html/2511.02832v1) |
| IR_FAR_03 | US_AMAZON_FTR | IR_FAR_03 | NEW_EVIDENCE | ORIGINAL_HTTP_BYTES | [Amazon FAR 官方组织 TWIST2 仓库](https://github.com/amazon-far/TWIST2) |
| IR_FIGURE_01 | US_FIGURE | B_US_FIGURE_004 | REVIEW_EXISTING_AND_REBIND | ORIGINAL_HTTP_BYTES | [Figure C轮承诺资本公告](https://www.figure.ai/news/series-c) |
| IR_FIGURE_02 | US_FIGURE | IR_FIGURE_02、IR_FIGURE_02_F02 | NEW_EVIDENCE | WEB_TOOL_EXTRACT | [BMW Figure 03 project in Spartanburg](https://www.press.bmwgroup.com/canada/article/detail/T0458794EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg) |
| IR_FOURIER_01 | CN_FOURIER | IR_FOURIER_01 | NEW_EVIDENCE | WEB_TOOL_EXTRACT | [Fourier Makes CES Debut With GR-3](https://tools.prnewswire.com/en-us/live/20823/release/20260106EN55830) |
| IR_FOURIER_02 | CN_FOURIER | IR_FOURIER_02 | NEW_EVIDENCE | WEB_TOOL_EXTRACT | [傅利叶携多款康养陪伴新品方案亮相WAIC 2026](https://news.pedaily.cn/202607/566499.shtml) |
| IR_ASTRIBOT_01 | CN_ASTRIBOT | B_CN_ASTRIBOT_001 | REVIEW_EXISTING_AND_REBIND | WEB_TOOL_EXTRACT | [星尘智能完成B轮超10亿元融资](https://stcn.com/article/detail/3941094.html) |
| IR_AGILITY_01 | US_AGILITY | IR_AGILITY_01 | NEW_EVIDENCE | ORIGINAL_HTTP_BYTES | [GXO与Agility多年RaaS协议](https://gxo.com/news_article/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics/) |
| IR_BD_01 | US_BOSTON_DYNAMICS | B_US_BOSTON_DYNAMICS_003 | REVIEW_EXISTING_AND_REBIND | ORIGINAL_HTTP_BYTES | [DHL与Boston Dynamics的Stretch合作与MOU](https://group.dhl.com/en/media-relations/press-releases/2025/dhl-group-signs-mou-with-boston-dynamics-and-accelerates-cross-business-automation-strategy.html) |

Figure03产品证据006属于修复旧编号冲突，另计新增记录。详见`work/supplement_ingestion.json`和`repair_records/fact_delta.json`；后者列出重建后的最终变更。

9条web读取记录以`.web.json`保存，JSON内`not_original_http_bytes=true`；其哈希不是网站原件哈希。论文PDF宣传册保留原件，图像PDF说明采用人工视觉转录。
