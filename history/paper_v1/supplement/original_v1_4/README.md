# 具身智能公开招聘研究 论文v1.4

本版完成2026年9月21日建议中的定稿前编辑，作为本轮稳定中文工作稿。论文与一页摘要同时提供Word、PDF和Markdown。[编辑说明](本轮编辑说明_v1.4.md)列出本轮处理及展示比例。旧版保留在原目录。

[补充材料索引](appendix/补充材料索引.md)连接测量规则、编码来源与完整结果；[语境证据](evidence/index.html)包含248条广告、496个广告—技术项和456条证据，可在浏览器本地打开。

## 表格与编号

正文含13张表，附录含A1与A2，共15张可编辑表、3幅图。原表6的20行情景移为附表A2；表5c新增P/提及数，表5b分母不变。来源方案为R1、R2、R3，分别对应冻结底表代码S1、S2、S3；材料目录仍使用S1至S7。内部表资产键S3对应附表A1，T5对应附表A2。

## 复算与文档生成

使用Python 3.10或更新版本，在本目录执行：

```text
python reproduce/reproduce.py --output ../v14_recomputed
```

输出目录必须不存在。程序核对输入清单后重建基础汇总、派生分析、15张表及语境页面。基础计算只用标准库；`--figures`另需matplotlib、numpy及中文字体。固定状态输入不重新运行语义编码。证据页面返回补充材料的链接依赖完整交付包。

`authoring/build_documents.py`读取本包的表图和文字源生成Word与展开后的Markdown，需要python-docx。`authoring/export_pdf.ps1`使用Microsoft Word导出独立副本；`authoring/render_pages.py`以pypdfium2及Pillow渲染页面。

## 当前核对

统计输入、分析底表与语境证据沿用v1.3。新增比例直接来自既有联合表；49/82和21/60来自四职能基础计数。本轮验证仅针对改动后的含义、直接计算、材料连接和成稿版式，见verification。完整文件清单为publication_manifest.json；历史研究核查沿材料S2与历次回复追溯。
