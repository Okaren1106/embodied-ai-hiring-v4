# 阶段D 公司解释与结论检查接续包 v1

**本包为 dsv4.1flash 完成的阶段D研究交付。** 先读 [REPORT.md](REPORT.md)，再看 [三张主图](charts/D1_cross_function_activity.png) 与 [T5 长表](tables/T5_company_hiring_correspondence.csv)、[T6 台账](tables/T6_conclusion_ledger.csv)。全部表格与分母见 [DATA_DICTIONARY.md](DATA_DICTIONARY.md) 与 [METHODS.md](METHODS.md)。

## 输入

阶段C正式包为唯一统计来源：`stage_c/run_20260915T105656Z`（T1—T4正式表、固定规则v1副本、184文件input_lock）。公司事实层继承 `stage_b_supplemented/run_20260915T073556Z`（680事实、111证据）。分组、场景与Q2规则来自 `analysis_rules_v1/run_20260915T085828Z`。广告正文补充读取冻结合并基线 `outputs/reference-expansion-2026-09-11/merged-baseline-2026-09-11/records.jsonl`。

输入路径、大小与SHA-256登记在 `input_lock.json`。阶段C原封存包、B包、研究库与规则包在本轮全部保持只读，未回写。

## 分析复算

Python 3.12、Matplotlib 3.11.2、NumPy 2.5.3；图中文字使用Windows微软雅黑msyh.ttc。数据派生只使用Python标准库。

```powershell
python scripts/reproduce.py --output 'D:\reproduction\stage_d_new'
```

复算入口先核验本包 `release_checksums.json` 的全部文件哈希与 `input_lock.json` 的输入哈希，随后在隔离目录重跑 step1 至 step7，逐字节比较派生表与三张图；全部一致才发布新目录。已有输出目录拒绝覆盖，输入漂移拒绝发布。

单模块入口依次为 `scripts/step1_coverage_cross_cooccurrence.py`、`step2_responsibility_and_cases.py`、`step3_company_and_K_comparison.py`、`step4_sensitivity_ledger.py`、`step5_deliverables.py`、`step6_charts.py`、`step7_package.py`，可单独检查。绘图依赖如装在隔离目录，传 `--plot-deps '绘图库目录'`。

## 范围

本包交付阶段D的覆盖与集中度、职能—活动双向交叉、三组活动共现与关系判定、业务责任长表与缺口、案例候选与选择、同职能统一权重比较、敏感性与未知情景，以及T5、T6与三张主图。样本仍为24个主体1,654条认可广告，未扩样、未重分类、未恢复周采。

案例组一（Galbot、AgiBot）具备共同职能比较资格；案例组二（Boston Dynamics、Pickle Robot）共同职能不足2个，统一权重比较记录为不适用，只保留逐职能点值与有限描述。
