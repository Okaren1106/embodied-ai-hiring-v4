# 完整扩展增量源文核验与纳入规则诊断

日期：2026-09-26。当前版本使用七项 `data/v4_source_corrections.json` 与刷新后的 scope，包含 N0508 及 N0798/N1044。来源和旧版本保持只读；本审计没有修改生产分类。核验者为研究代理，事先知道主结果和选入理由，**不是独立人工、不是盲评、不是 gold standard**。

## 当前范围与版本

完整覆盖 ROBOT_MODEL 当前 Q 非 P、Q+E 为 P 的 **44 个目标对、43 个广告、13 家公司**：Python 1，PyTorch 43。转换为 **42 个 Z→P，2 个 U→P**。后两条 N0798/N1044 不是 known EXAMPLE：关系集合为 UNCONDITIONAL_OR_EXAMPLE；窄 Q 在两读法下取值不同而保留 U，扩展在两读法下均纳入而成为 P。这是构念上的不确定性传播，不是任意填补 U。

来源为38条历史 EXAMPLE、3条v3澄清（E0057/A032、N0158/A065、N0486/A099）、3条v4一致性澄清（N0508、N0798、N1044）。账本保留 origin、audit_id、旧分支和原v3 Q。N0508与N0486捕获全文相同，经协调者v4账本成为当前Q=Z，再进入扩展。N0798原Q=P、N1044原Q=Z，现均为U，扩展均P。

最初42版保留为 `*_pre_overlay.csv`，其后43版保留在 `analysis/example_increments/stage4_before_bare_parenthesis_consistency/`，不能替代当前44版。

逐条读取保存的完整 full_description、父句及前后资格范围。44个证据出现的目标跨度、字段SHA256、父句跨度、父句包含目标、标题至证据上下文共 **220个标准检查全部通过**。另核对v4引用跨度/哈希及N0508/N0486全文相等。通过表示冻结输入与账本一致，不是原网页完整性或语义准确率证书。

## 字面证据的区别

| 支配目标的线索 | 目标对 | Python | PyTorch | 限制 |
|---|---:|---:|---:|---|
| such as | 7 | 0 | 7 | 明确英文例示 |
| e.g. | 5 | 0 | 5 | 明确英文例示 |
| 如 | 5 | 0 | 5 | 明确中文例示 |
| 等-only开放列举 | 25 | 1 | 24 | 与明确cue分开；实际替代性未经验证 |
| 无提示括号列表 | 2 | 0 | 2 | N0798/N1044；含无限定与例示两读法 |
| 合计 | 44 | 1 | 43 | 不称全部为明确例示 |

没有目标受 for example、例如或 including 支配的新增记录；全文别处出现相同词不计入目标cue。全部目标可定位于候选资格条目，未发现能确定为纯DUTY/PREFERRED却误入GENERAL/REQUIRED的新增条目；这不是accuracy估计。

关键个案：

- **N0798**：`Familiarity with machine learning frameworks (PyTorch, JAX, TensorFlow)`。两个框架共享谓词和裸括号关系。同类扩展发现旧PyTorch P与新TensorFlow U不一致，协调者统一主层后两者Q=U、扩展=P；据实保留发现过程，不称盲验证。
- **N1044**：`Experience with modern ML frameworks (PyTorch, JAX) and large-scale training workflows.` 位于We’re Looking For与Nice to Have之间，没有明确例示词。按同一关系集合处理，不再把旧EXAMPLE当已知真值。
- **E0057**：工程栈子句有“优先”，分号后为PyTorch/TensorFlow等框架子句。当前GENERAL解释依赖子句范围，仍是外部语义复核点。
- **N0158**：框架及模拟器共同受“等工具”支配；外部开放列举与slash内部关系分别记录。
- **N0199**：唯一Python新增和一个PyTorch新增在同一父句，不能当成两个独立广告。
- **N0984**：nearest_heading_text留下前段What You’ll Do，全文另有We’re Looking For；标题提取器不是金标准。
- **N0490**：捕获末尾停在“等技”，可能截尾。目标父句完整，但不能保证原网页后面无另一表达。
- **N0508/N0486**：全文相同而旧分类不同，促成可追溯一致性修正；源核验仍不同于独立人审。

“等”可命名重要的具体技能，既不自动表示“任一个均可”，也不自动表示“每个都必须”。将其排除于窄Q是本研究构念定义，不是普遍语言真理。本审计不推测实际筛选权重或可接受的替代集合。

## 固定当前Q的纳入规则替代

比较Q、全部当前扩展scope、排除两个裸括号增量、只接纳清晰such as/e.g./如增量。排除增量是恢复为**当前Q**，不重新编码Q；两裸括号均恢复为U。原Q的P保留；两个较窄的替代规则也保留原Q的U。宽扩展独有的U→P来自已声明关系集合。

差值为Python−PyTorch；范围为recorded-unknown assignment outer bounds，不是置信区间。机器字段 `Q_plus_admitted_example_scope` 对应生产 `Q_plus_example`，包括关系集合传播，不能只理解为known EXAMPLE。

| 样本 | 规则 | Python P/U | PyTorch P/U | 确认差pp | 外界限pp |
|---|---|---:|---:|---:|---:|
| 全体105 | Q | 42/17 | 22/6 | +19.05 | +13.33至+35.24 |
| 全体105 | 全部当前扩展scope | 43/17 | 65/4 | −20.95 | −24.76至−4.76 |
| 全体105 | 排除两裸括号增量 | 43/17 | 63/6 | −19.05 | −24.76至−2.86 |
| 全体105 | 仅清晰非穷尽cue | 42/17 | 39/6 | +2.86 | −2.86至+19.05 |
| 共同提及66 | Q | 37/15 | 18/5 | +28.79 | +21.21至+51.52 |
| 共同提及66 | 全部当前扩展scope | 38/15 | 51/3 | −19.70 | −24.24至+3.03 |
| 共同提及66 | 排除两裸括号增量 | 38/15 | 49/5 | −16.67 | −24.24至+6.06 |
| 共同提及66 | 仅清晰非穷尽cue | 37/15 | 30/5 | +10.61 | +3.03至+33.33 |

全样本清晰cue给PyTorch增17、Python增0，使确认差从+19.05降至+2.86pp；等-only再给PyTorch增24、Python增1，净移−23/105即−21.90pp；两个裸括号再移−2/105即−1.90pp。**支持全样本负方向需要等类纳入，清晰cue单独不能推出该负方向；去除两裸括号后负方向仍受界限支持。**共同提及66在清晰cue下保留正的外界限，扩大至等类后不能排序。

这是admission rule alternatives，不是竞争真值或按观察方向进行的纠错。它支持明确构念和纳入规则的必要性，不能写成与语言惯例无关的真实用工排序。

## 局部句式与剩余威胁

NFKC、大小写、空白标准化后，有8组公司内相同目标父句且每组至少2个不同广告：XSquare三组（E0139/E0251；E0169/E0217/E0284；E0208/E0209），Apptronik E0414/E0415，Figure E0487/E0489/E0491/E0492/E0495，Galbot N0001/N0102，Fourier N0460/N0469，Deep Robotics N0486/N0508。它们是选入增量的描述，不是总体模板比例，未改样本权重。全文不同不妨碍共用决定技术关系的同一句。

最大剩余经验威胁是技术类别、语言惯例和公司局部模板共同产生关系分布，而缺少独立语义或行为效度证据。新增同类对照见 `extensions/framework_control/audit/framework_control_review.md`：26条共同提及广告内两框架的共享算子给出相同状态，限定了跨类别发现的范围；这仍不是语言规则的外部验证。

## 文件与复现

- `work/literature_validation/review_example_increments.py`：44条来源链、完整packet/ledger及220项标准检查。
- `work/literature_validation/review_annotations.json`：逐条模型阅读解释，不是accuracy gold labels。
- `work/literature_validation/admission_rule_diagnostics.py`：2样本×4规则；Q与完整扩展计数/界限逐项对比生产scope。
- `analysis/example_increments/`：当前ledger、summary、完整源文包、来源检查、纳入规则状态/比较、重复父句。
- `stage4_before_bare_parenthesis_consistency/`：已替代的43版；`*_pre_overlay.csv`：更早42版。

所有材料只保存在本地研究包，没有外传私有正文。
