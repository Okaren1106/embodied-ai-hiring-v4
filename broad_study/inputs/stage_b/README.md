# B轮验收后公司证据补充包

**原修复及16卡入表包已通过独立验收；本版按用户追加授权补查并直接入表，补充后验证通过。** 原件独立验收与本轮自行补充验证分别记录。阶段B的有限业务组尚未固定，不声明整个B阶段完成。

- [公司资料总览](index.html)：24家公司，逐字段事实、证据原文、保存方式、缺口与资格。
- [验收及本轮新增说明](REPAIR_REPORT.md)；[原送审包独立验收](../../stage_b_evidence_integrated_acceptance/run_20260915T064258Z/REPORT.md)。
- [9条新增证据对照](SUPPLEMENT_INGESTION.md)；[原16卡对照](EVIDENCE_INGESTION.md)。
- [公司主表](company_profile.csv)、[事实](company_facts.csv)、[证据](company_evidence.csv)、[关系](evidence_links.csv)、[资本事件](capital_events.csv)、[缺口](company_gaps.csv)、[分组映射](company_group_mapping.csv)。

680条事实、111条证据记录、96个不同URL、457条关系、24条资本事件、307项原缺口、320条分组映射。证据记录数不是独立来源数；事实含未知和背景，不能当作全量外部确认。

产品/交付/场景时点资格覆盖23/23/22家公司，三项都有22家。FAR三项均不并入当前商业比较；星海图场景只作无日期背景。资格包含自述、媒体、提供形态及实际应用，不等于已售商品或付费证据齐全。业务组定义和Q2职能选择仍应在比较前固定。

## 复算

复制本目录至新的空目录，在副本执行：

```text
python -B -X utf8 scripts/s14_reproduce.py
```

入口先核验已封定输入锁，再重建并复跑故障与发布门禁。阶段A r3等既有只读底稿须保留脚本声明的本机原路径。`s01_lock_inputs.py`默认只核验；`--rebuild`仅供编制新版本，不用于掩盖审计时的输入漂移。

本轮9份新来源中7份保存HTTP原始字节、2份保存实际web工具返回，均有正文、记录与哈希。继承9张卡仅有工具正文的限制继续保留。旧包、研究库、measurement规则和1654条广告未修改。
