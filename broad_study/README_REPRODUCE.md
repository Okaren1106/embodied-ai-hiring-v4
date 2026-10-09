# Astra V3 复算说明

本包在冻结24主体1,654条广告上，完成17具体职能1,576条的规定复核范围与三任务深化。当前阅读入口是 `REPORT_Astra_final.md`、`document/具身智能公开招聘研究_最终综合报告_Astra.docx` 与 `index.html`。

## 数据版本

- 主分类和A/B/C沿用冻结版本；Q2目录为 Q2-v2.1，判读版本为 Astra-Q2-v2.1-review3。
- 首轮证据保留原Astra或grok署名；`review/astra_reviews.jsonl` 为可追溯修订事务，按完整 `identity_key` 区分广告。E0107有两个不同岗位身份。
- 原14语境加8职责分支格；源文本、定位、未知适用语境、来源排除与复核状态分开。
- 全文469、仅边界760、未选二次347。完成预设340全文与1,208强制队列不等于全样本二次全文或独立双编码。

## 计算顺序

使用交付机器已配置的Python运行时（版本见 `verification/environment_v3.json`），从本包的scripts目录执行：

```text
materialize_astra_final.py
compute_astra_final.py
compute_v3_two_layers.py
verify_v3_states.py
verify_astra_numeric.py
verify_v3_two_layers.py
```

前三项只从保留的输入、规则和研究事务构造统计结果，不重新判读广告。后三项分别独立重建状态、使用NumPy重算汇总和公司点值、使用SQLite按广告去重核验两层结果。目录本身不包含可替代研究判断的自动语义分类器。

`reproduce_astra_isolated.py <新后缀>` 创建全新物理目录，复制输入、配置、判读及所需脚本，重新生成Q3、Q4与三任务两层统计，比较21份输出的字节哈希。存在目标目录时拒绝覆盖；本次完成目录和收据见 `verification/astra_isolated_reproduction.json`。

`compute_v3_revision_impact.py` 比较保留的上一版与本版。它需要同级旧Astra、grok目录；这与基础数值复算的自包含边界不同。报告的旧版本链与字段差异已经写入CSV。

## 禁止误用历史登记脚本

不要重新运行register开头的脚本，它们是已经提交的研究判读记录。新判读须以有原文、理由、署名的FOLLOWUP事务提交。不能把未选二次复核的记录批量改成未知，也不能将旧草稿登记回正式包。

## 文档和保护

`build_v3_report.py` 构建研究正文和图；`build_word_astra.py` 使用python-docx创建Word。图形依赖位于runtime，数值核验使用环境记录中的NumPy。Word通过隐藏的Microsoft Word只读导出PDF，并用PyMuPDF逐页生成PNG核查；默认LibreOffice渲染器在本机不可用，诊断和替代路径记录于文档验收收据。

`verification/V3_protected_inputs.json` 核验冻结输入909文件、grok提交1,742文件和上一版Astra封存1,835文件。publication_manifest不包含自身、运行时、字节码与校验图片；不以自引用哈希假装封存。

## 研究解释边界

部署活动旧标签不保证对象口径一致，相关比例与分解撤出实质主结论；历史数据保留。两层第一层包括明确术语提及但分支尚未解的文本，第二层按职责/必备/一般/优先分列，可重叠；它不是无条件技能要求合计。责任宽情景包括协作联系，只是上界，不能当作本人能力。数值验收不证明标注准确率。
