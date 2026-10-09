# 阶段D结果包 · grok4.6研究

先读 [REPORT.md](REPORT.md)。图表页 [index.html](index.html)。计数与分母 [METHODS.md](METHODS.md)。表格目录 [DATA_DICTIONARY.md](DATA_DICTIONARY.md)。独立核验 [verification/REPORT.md](verification/REPORT.md)。

研究标记：**grok4.6研究**。模型：Cursor Grok 4.6。执行依据为锁定副本 `inputs/protocol/研究执行书.md`（阶段D研究执行书 v1）。方案形成于阶段C描述结果之后，不称为事前预注册。

## 输入

`input_lock.json` 封存阶段C表与广告、B补充事实、规则v1、研究执行书及案例/来源决策。来源较完整子集在派生D结果之前按T1覆盖字段锁定，不使用活动率或正文长度。原封存A/B/C与研究库不在本包改写。

## 分析复算

Python 3.12、Matplotlib 3.11.2、NumPy 2.5.3；图中文字使用 Windows 微软雅黑。纯数据分析仅用标准库。

```powershell
python scripts/reproduce.py --output 'D:\reproduction\stage_d_new' --plot-deps '绘图库目录'
```

已完成包先核验全包 SHA-256，再在隔离目录重跑 `analyze.py`、`figures.py`、`write_report.py`、`verify.py`，表、图、报告与核验文件逐字节一致后才发布新目录。拒绝覆盖已有目录；输入或发布清单漂移会失败。仅封存当前已完成运行：

```powershell
python scripts/reproduce.py --seal-current
```

单独核验：`python scripts/verify.py`。生成程序自检不等于独立核验。

## 范围

本包交付覆盖与双向交叉、活动共现关系判定、部署构成与共同职能统一权重、两组四家案例、T5交付责任长表、T6结论台账及三张主图。Q2维持 ML/AI 工程与软件与平台两个代表。未扩样、未重分类。阶段E研究初稿不在本包。

## 完整接续包装

包装标识 `STAGE_D_COMPLETE_V1`。含 README、scripts、inputs、input_lock 及本目录自身的 release_checksums.json。新目录的清单不是来源包清单的复制。
