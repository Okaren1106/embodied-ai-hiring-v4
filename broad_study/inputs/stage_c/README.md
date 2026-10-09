# Q1—Q3 正式分析接续包

先读 [REPORT.md](REPORT.md)，再用 [index.html](index.html) 看图和查询公司语境点值。Excel查看文件在outputs/01a0a3f0/Q1-Q3_results.xlsx。完整表格与分母、原文追溯见DATA_DICTIONARY.md和METHODS.md。

## 输入

inputs/rules_v1为已固定v1完整副本，原封存179个文件及其清单保留。inputs/stage_a_extra补入A包活动、次职能和原说明。input_lock.json封存184个文件。外部业务分类按既定v1使用，未重查、重分类或扩展Q2。

## 分析复算

Python 3.12、Matplotlib 3.11.2、NumPy 2.5.3；图中文字使用Windows微软雅黑msyh.ttc，其哈希见verification/plot_environment.json。纯数据分析仅用Python标准库。发布复算入口先核验全包文件清单及SHA-256，再复制输入/脚本到隔离临时目录，重算数据、图表和报告，逐字节比较，全部通过后才发布新目录；拒绝覆盖已有目录。

```powershell
python scripts/reproduce.py --output 'D:\reproduction\stage_c_new'
```

如绘图库在隔离目录，传`--plot-deps '绘图库目录'`。本次环境的绘图库只安装在项目临时分析目录，未修改正式研究依赖。

可单独检查已封存结果：`python scripts/verify.py`。已有包原则上只读；若需更改分析规则，应开新版本并说明理由，不重锁旧输入来掩盖变化。

工作簿是已验证的查看导出，发布复算复制其已封存字节，**不把工作簿复制称为重新计算**。需要重新导出时，scripts/workbook.mjs读取workbook_data.json；使用Codex bundled Node和@oai/artifact-tool，先按Spreadsheets技能标记创建操作，在临时执行目录连接bundled node_modules后复制该脚本运行，参数为本包根目录。作者验证保留计算、错误扫描和七页渲染；不承诺不同Excel引擎或不同字体环境输出完全相同字节。

## 范围

阶段C交付T1整合、T2—T4正式结果、6主图/4附图和基础敏感性。T5/T6、公司事实解释与研究初稿属于后续D/E阶段。Q2维持两个代表职能。
