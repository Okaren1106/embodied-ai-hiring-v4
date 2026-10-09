# IJM / Emerald 官方要求核查

核查日期：2026-09-26（Asia/Shanghai）。本文件是内部研究与投稿可行性备忘录，不是投稿正文。网页要求可能变化，最终提交当天须复核。

## 先行结论：不能把辅助分析与生成数据混为一谈

官方来源：[Emerald Publishing — Publishing ethics](https://www.emeraldgrouppublishing.com/publish-with-us/ethics-integrity/research-publishing-ethics)；另核对新的官方入口 [Publication ethics](https://www.emerald.com/publish-with-us/pages/publication-ethics)。本轮 web 搜索实际返回了两个官方入口的 AI 条款正文；中途直接打开及额外检索发生 connection failed，后续搜索恢复。PowerShell 直连遇 TLS EOF，curl 遇吊销服务离线，浏览器直连 IJM 页连接关闭；不得将这些失败写成没有取得任何官方内容，也不得声称已保存官方完整 HTML。

在 **AI and content creation** 标题下，准确原句：

> Generating, manipulating, or reporting research data and results using a generative AI tool/LLM is not permitted.

同一标题的下一条分别处理两种用途：禁止用 LLM 在文内报告统计量，但明确容许在适当、透明披露下以该工具辅助工作分析。本页另外区分作者已存在原创材料的 copy-editing（可用）和生成新材料的 copywriting（不可用，特别点名摘要和文献综述）。因此，**不能把政策概括为“禁止所有 AI 辅助分析”**；也不能把“披露即可”当作生成稿件的豁免。

**Declaring AI Usage** 要求在 Methods 和 Acknowledgements 或其他合适部分透明说明 AI 使用、内容改动、工具名称和版本，并核验引用。**AI and content editing** 要求保留使用记录且作者负责。政策还保留出版社对具体用途是否获准的判断权。

以上是官方规则的摘要；以下是本研究的适用判断：既有模型语义分类、程序计算协助、作者原文润色、AI 初稿写作必须分别记账。程序从真实冻结数据进行确定性统计，不应被擅自等同于编造数据；但本项目以 LLM 从广告生成研究标签、并由 LLM 撰写统计结果叙述，如何落在该政策边界内，官方页没有给出与本案例完全对应的解释。应由真实作者核对原始材料、保留全过程，必要时向编辑提交不含私有原文的用途说明，请其明确认定。禁止虚构“编辑已同意”，不得把本备忘录的建议当作已获豁免。

本轮仍可完成文献核查、数据诊断、可复算程序、方法备忘录和供作者使用的证据包；这些交付不应被命名为已满足 IJM 政策的可直接投稿稿件。

### 官方表格的补充约束与不一致

新入口 `emerald.com/publish-with-us/pages/publication-ethics` 的搜索返回整张 AI usage table，关键标记如下（转述，非完整转载）：

| 用途 | 新入口表格标记 |
| --- | --- |
| 方法构思 | YES |
| 新写假设、引言、方法、结论 | NO |
| 文献综述/书目创建，包括评价和分析文献 | NO |
| 生成研究数据 | NO |
| 分析或描述数据/结果 | NO |
| 汇总作者已有数据/结果 | YES |
| 据作者已分析数据作图 | YES |
| AI单独生成研究代码、没有其他人参与 | NO |
| 作者既有材料copy-editing；翻译作者未发表原作 | YES |

父任务在旧入口检索到Data generation行显示YES，而本任务新入口明确显示NO；目前不能判定是站点版本不同还是表格抽取错位，未作视觉核验。另一方面，新入口的Results analysis=NO与上文允许辅助分析也存在适用口径张力。因此，**不宣布现有LLM语义编码必然获准或必然不获准**；具体生成标签、程序辅助和结果总结的分界须向编辑澄清。明晰的copywriting禁令不因这处差异而消失。

表格还限制文献评估/书目创建，故本轮资料只能作为检索线索与内部研究审计，作者应亲读、核查并形成自己的论证和引文选择。不能把AI产出的内部证据备忘录稍作改名后直接当作投稿文献综述，也不能声称真实作者亲读了本轮所有来源。

## IJM 覆盖范围与作者要求

官方入口：[International Journal of Manpower](https://www.emeraldgrouppublishing.com/journal/ijm)。搜索返回期刊页与作者指南，直接打开遭403。Scope偏重人力资源、管理和劳动经济学的强实证/分析定量研究，极高质量定性研究偶可考虑；明确不再接收fuzzy类型方法、文献计量、文献综述或纯概念稿。2026-04-22副编辑公告重申定量定位。当前题材相容，但语义分类需要明确的劳动市场问题；下述是研究判断，不代表编辑预审通过。

期刊页的 **Emerald’s Policy on AI Usage** 指向上述出版伦理规则，并没有返回本研究类别的例外。禁止新内容 copywriting、容许作者既有材料 copy-editing 的规定适用；不能以 GOJA 所在 ACL 的写作披露惯例推断 IJM 允许同样用途。

已从官方期刊页定向检索确认：

| 项目 | 当前要求 | 对本项目的含义 |
| --- | --- | --- |
| 总字数 | 6,000–8,000，含摘要、参考文献、表图文字和附录；每图表折280词 | 重新计入全文，不只计算主体段落 |
| 摘要 | 结构式；Purpose、Design/methodology/approach、Findings、Originality；总250词含关键词与分类 | 原稿字数核验可重用方法，须按最终版重算 |
| 关键词 | 最多12个短关键词 | 不是必须凑12个 |
| 文件 | Word；LaTeX需配PDF | 实际生成仍受写作政策约束 |
| 表格 | 与正文分别提交 | 不以同一整合阅读版代替投稿文件 |
| 引文 | Harvard；参考文献按字母序；有DOI应列 | 核实发表版/工作论文版，不混写年份 |
| 审稿 | 双匿名 | 准备匿名主文并检查文件元数据 |

补充材料托管、数据公开义务和匿名自引的详细条款未在本轮定向返回中充分取得，因此不宣称它们已逐项核实。该页通用文章类型列表虽仍列Literature review/Conceptual paper等定义，但更具体的scope排除应优先理解，不把表单模板当作适用许可。未核验当前APC金额或指标，也不以二手指南的接收率替代官方标准。

## 证据可追溯性

- 官方政策页：首次成功读取为 2026-09-26 的 web 搜索结果正文（本工具会话引用 `turn1search0`，只作内部溯源，不是对外引文）。返回范围含 Declaring AI Usage、AI and authorship、AI and content creation、AI and content editing、AI evaluation and peer review 及 AI usage table 引言。
- IJM：官方搜索返回作者指南、双匿名审稿说明、2026-04-22公告；后续定向搜索取得字数/摘要/关键词（内部 `turn12search0`）、表格/参考文献（`turn35search1`）、scope排除（`turn37search1`）。直接open HTTP403。完整HTML未落盘，不能提供其哈希。
- 新版政策入口：2026-09-26定向web搜索（内部 `turn12search1`）取得表格。上述链接是可复查官方来源；本文件保存已读证据摘要和适用边界，不伪造抓取快照。
- 旧新闻：[2024-05-02 Emerald statement](https://www.emeraldgrouppublishing.com/news-and-press-releases/emerald-publishings-stance-ai-tools-content-creation-and-peer-review) 已读取，但当前政策页更细且对图像用途已有区分，故不用旧新闻替代当前规则。

本记录不进行投稿、外发邮件或上传研究私稿。
