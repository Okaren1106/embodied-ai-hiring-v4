# 第二轮返修对照（B2-01～B2-06）

对应独立验收报告与 `REPAIR_INSTRUCTIONS.md`。前轮已确认的 FAR 摘录绑定、母公司 `CONTEXT_ONLY`、未知不转否定、307 原缺口、六表离线重建一致予以保留，不推倒重做。

## B2-01 / P1 公司主体错配（CN_NOETIX）

| 项 | 内容 |
|---|---|
| 问题 | `CN_NOETIX` 应为松延动力 / Noetix Robotics（r3：13 条广告，官网 `noetixrobotics.com`），送审包写入非夕 Flexiv，至少污染 8 条事实、7 条严格分组、6 项缺口映射 |
| 返修 | 撤回 Flexiv 绑定；用松延官网 Organization 重查；样本 ID 与 13 条广告不改。新增 `work/identity_map.json` 与自检 `I1`：必须含 Noetix/松延，禁止 flexiv/非夕 |
| 替代 | 法定主体「北京松延动力科技集团股份有限公司」；产品 N2/E1/Bumi/Hobbs；无依据的交付/部署/客户保持查后未找到或未查 |
| 检查 | `I1`；故障实验「修改当前副本的研究源文件」把官网改成错误域后被拒 |
| 状态 | 已修。追溯见 `WITHDRAWN_FACTS.md` |

## B2-02 / P1 假 SEARCH 轨迹

| 项 | 内容 |
|---|---|
| 问题 | `s11b_search_log_ext.py` 按最终 `SEARCHED_NOT_FOUND` 自动补写 192 条 SEARCH，不能证明实际检索 |
| 返修 | 停用补写；历史行标 `DERIVED_STATUS_SUMMARY`。无真实逐问题轨迹的扩展结论降为 `NOT_YET_SEARCHED`。验收区分真实 SEARCH / FETCH / PAGE_REVIEW / 派生总结 |
| 实测 | 真实 SEARCH 27；派生 192；FETCH 114；PAGE_REVIEW 22；缺逐问题真实轨迹 0 |
| 检查 | 自检 `G6`；`s09` / `s11b`；门禁拒绝不完整检索轨迹 |
| 状态 | 已修。说明见 `SEARCH_TRAIL.md` |

## B2-03 / P1 门禁可绕过

| 项 | 内容 |
|---|---|
| 问题 | 核锁读回送审包绝对路径；改页面/广告数/Node 脚本或留失败负例仍可发布；checksum 早于门禁状态；完整复跑 13/14 |
| 返修 | `resolve_locked_path()`：r3 走密封根，本包走当前 RUN 身份；锁定 `work/companies.json`。正对照必须能发布。新增 6 类受控实验。checksum 在门禁通过后再生成 |
| 实测 | 20/20 通过。正对照 PUBLISHED。负例拒绝原因见 `work/fault_probes.json` |
| 检查 | `s06` + `s11`：改研究源、换 `index.html`、`n_ads`→999、负例 FAIL 但计数全绿、换 Node 留旧报告、分别篡改 sha256 / `code_digest` |
| 状态 | 已修 |

## B2-04 / P1 时点规则与千寻智能日期

| 项 | 内容 |
|---|---|
| 问题 | 事件日/发布日分别取 min 再拼；无发布日仍标观察日可用；`B_CN_LIMX_002` 正文 7 月 14 日却写 4 月 |
| 返修 | `qualify_pairs` 成对日期；事件 BEFORE 但发布日 UNKNOWN → `DATE_UNKNOWN`。`B_CN_LIMX_002` 发布日 2026-07-14；资本行事件 2026-07-14 / 发布 2026-07-18 来自同一条 21 世纪经济报道 |
| 检查 | 自检 `T*`、`K7`；故障实验改发布日到 2027、改日后强行保留观察日可用 |
| 状态 | 已修 |

## B2-05 / P2 资本口径（Figure、Diligent）

| 项 | 内容 |
|---|---|
| 问题 | Figure C 轮缺官方日期与「承诺资本」定义；Diligent 把 2900 万与 530 万或有相加 |
| 返修 | Figure：官方 https://www.figure.ai/news/series-c ，2025-09-16，承诺资本 >$1B、投后 $39B；B 轮无发布日退出观察日比较。Diligent：SEC 8-K 交割 2026-01-27，2900 万**包括**最高 530 万或有；媒体「另加」降为背景 |
| 检查 | 资本行声明日期必须对应某一条证据的成对日期 |
| 状态 | 已修 |

## B2-06 / P2 范围文案与清单时序

| 项 | 内容 |
|---|---|
| 问题 | README/页面/scope 仍写三家试点或「其余 21 家未查」；checksum 早于门禁 |
| 返修 | 统一为 24 家修订范围；逐字段未查仍展示。标记 `REPAIR_R2_PENDING_ACCEPTANCE`。`s11` 先写状态再跑 `s10` |
| 状态 | 已修 |

## 仍未关闭（如实保留，不是本轮失败条件）

1. 傅利叶人形在新加坡临床部署证据不足，冲突未关闭。
2. 自变量上市状态为查后未找到，保持未知并退出该比较维度。
3. FAR 团队成立日未找到；FAR/FTR 边界仅有一次访问受阻记录。
4. Boston Dynamics 计划交付组保持 `DELIVERY_PLAN_NAMED_RECIPIENTS`，不改成已实现；Stretch 本轮未核验，保持未知。
5. 融资金额未披露的轮次保留未知。
6. 分组表仍有 2 行 `NOT_RESEARCHED`（傅利叶 `product_lines` / `target_markets` 维度未给分组取值）及 1 行 Agility `delivery_form`=`UNCLASSIFIED_VALUE`（规则文件未声明该取值，退出比较）。不据此宣称全部字段已分组完毕。
7. 24 家均有公司记录 ≠ 每字段已检索完毕。
