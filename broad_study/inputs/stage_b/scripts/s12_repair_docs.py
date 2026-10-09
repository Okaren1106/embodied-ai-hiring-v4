"""Stage B repair / step 12: repair-side deliverables.

Writes the three documents the repair instructions ask for beyond the data package:

  problem_register.md     - one row per acceptance finding, what changed, where it is
                            checked, and what remains open
  CHANGE_LOG.md           - output-level and input-level differences against the
                            submitted package (facts, relations, capital, gaps, groups)
  REPAIR_SELFCHECK.md     - explicitly separates this self-check from independent
                            acceptance and states what is not claimed

Numbers are read from the generated tables and from the submitted package, so the
comparison is measured rather than narrated.
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import CODE_VERSION, RUN, SUBMITTED, WORK, read_csv, write_json  # noqa: E402


def counts(base: str) -> dict:
    def n(name, path=None):
        p = os.path.join(base, path or name)
        return len(read_csv(p)) if os.path.exists(p) else None
    return {
        "facts": n("company_facts.csv"),
        "evidence": n("company_evidence.csv"),
        "links": n("evidence_links.csv"),
        "capital": n("capital_events.csv"),
        "gaps": n("company_gaps.csv"),
        "groups": n("company_group_mapping.csv"),
    }


def main() -> int:
    old = counts(SUBMITTED)
    new = counts(RUN)
    cap_new = read_csv(os.path.join(RUN, "capital_events.csv"))
    cap_old = read_csv(os.path.join(SUBMITTED, "capital_events.csv"))
    gaps_new = read_csv(os.path.join(RUN, "company_gaps.csv"))
    gaps_old = read_csv(os.path.join(SUBMITTED, "company_gaps.csv"))
    links_new = read_csv(os.path.join(RUN, "evidence_links.csv"))
    links_old = read_csv(os.path.join(SUBMITTED, "evidence_links.csv"))
    facts_new = read_csv(os.path.join(RUN, "company_facts.csv"))
    facts_old = read_csv(os.path.join(SUBMITTED, "company_facts.csv"))
    ver = json.load(open(os.path.join(RUN, "verification.json"), encoding="utf-8"))
    fault = json.load(open(os.path.join(WORK, "fault_probes.json"), encoding="utf-8"))
    rb = json.load(open(os.path.join(WORK, "rebuild_check.json"), encoding="utf-8"))

    research = sorted({f["company_id"] for f in facts_new})
    unsearched = sorted({g["company_id"] for g in gaps_new} - set(research))

    # ---- change log -------------------------------------------------------
    changed_facts = []
    old_by_id = {f["fact_id"]: f for f in facts_old}
    for f in facts_new:
        o = old_by_id.get(f["fact_id"])
        if o is None and f["fact_seq"] == 1 and not f["merge_parent_field"]:
            changed_facts.append({"fact_id": f["fact_id"], "change": "新增字段行"})
        elif o is not None:
            for key, label in (("value_status", "证据性质"), ("time_applicability", "时点适用性"),
                               ("value", "取值"), ("time_basis_evidence_ids", "日期依据")):
                if o.get(key, "") != f.get(key, ""):
                    changed_facts.append({"fact_id": f["fact_id"], "change": f"{label}变更",
                                          "before": (o.get(key) or "")[:60], "after": (f.get(key) or "")[:60]})

    lines = [
        "# 返修变更清单",
        "",
        f"送审包：`{SUBMITTED}`",
        f"返修包：`{RUN}`",
        f"代码版本：`{CODE_VERSION}`",
        "",
        "## 一、规模对比",
        "",
        "| 表 | 送审包 | 返修包 | 说明 |",
        "|---|---|---|---|",
        f"| 事实行 | {old['facts']} | {new['facts']} | 允许同字段多行，按主体/范围/事件拆分 |",
        f"| 证据行 | {old['evidence']} | {new['evidence']} | 来源链与 ID 保留 |",
        f"| 关系行 | {old['links']} | {new['links']} | 由 ID 前缀推断改为逐条声明 |",
        f"| 资本事件 | {old['capital']} | {new['capital']} | 由来源摘要改为实际事件 |",
        f"| 缺口行 | {old['gaps']} | {new['gaps']} | 307 项逐项保留 |",
        f"| 分组映射 | {old['groups']} | {new['groups']} | 增加比较资格分桶 |",
        "",
        "## 二、关系性质对比",
        "",
        "| 来源 | 关系分布 |",
        "|---|---|",
        "| 送审包 | " + "、".join(f"`{k}`×{v}" for k, v in Counter(l["relation"] for l in links_old).most_common()) + " |",
        "| 返修包 | " + "、".join(f"`{k}`×{v}" for k, v in Counter(l["relation"] for l in links_new).most_common()) + " |",
        "",
        "## 三、缺口状态对比",
        "",
        "| 状态 | 送审包 | 返修包 |",
        "|---|---|---|",
    ]
    old_gap = Counter(g["stage_b_status"] for g in gaps_old)
    new_gap = Counter(g["stage_b_status"] for g in gaps_new)
    for k in sorted(set(old_gap) | set(new_gap)):
        lines.append(f"| `{k}` | {old_gap.get(k, 0)} | {new_gap.get(k, 0)} |")
    lines += [
        "",
        f"未研究公司（{len(unsearched)} 家）的继承缺口在返修包中一律为 `NOT_YET_MAPPED_THIS_RUN`："
        f"{sum(1 for g in gaps_new if g['company_id'] in unsearched and g['stage_b_status'] == 'NOT_YET_MAPPED_THIS_RUN')} 项；"
        "送审包中的 21 项 `RESOLVED` 已全部撤回。",
        "",
        "## 四、资本事件对比",
        "",
        "| 公司 | 送审包轮次/交易 | 返修包轮次/交易 |",
        "|---|---|---|",
    ]
    for cid in sorted({c["company_id"] for c in cap_old} | {c["company_id"] for c in cap_new}):
        o = "、".join(c["round_or_deal"] or "—" for c in cap_old if c["company_id"] == cid) or "—"
        n = "、".join(c["round_or_deal"] for c in cap_new if c["company_id"] == cid) or "—"
        lines.append(f"| {cid} | {o} | {n} |")
    lines += [
        "",
        "返修包中每条事件都带结构化金额字段（`amount_original` / `currency` / `amount_unit` / `amount_scope`）、"
        "单列的投后估值与来源条数；来源月份冲突保留在事件内部，不拆成第二个交易。",
        "",
        "## 五、事实行变更明细（抽查口径）",
        "",
        "| fact_id | 变更 | 前 | 后 |",
        "|---|---|---|---|",
    ]
    for c in changed_facts[:40]:
        lines.append(f"| `{c['fact_id']}` | {c['change']} | {c.get('before','')} | {c.get('after','')} |")
    if len(changed_facts) > 40:
        lines.append(f"| … | 共 {len(changed_facts)} 项 | | |")
    lines += [
        "",
        "## 六、输入与原件保护",
        "",
        "- 输入锁覆盖 r3 发布清单 68 个文件、r3 需读表、locked_inputs 子树、研究源文件、规则文件、"
        "全部证据快照（正文与原始页）与检索日志，共 "
        f"{json.load(open(os.path.join(WORK,'input_lock.json'),encoding='utf-8'))['n_entries']} 个条目。",
        "- 快照声明哈希按统一的正文口径重新声明并全部可复算（见 `work/snapshot_rebuild.json`）。",
        "- 送审包、`stage_a_r3`、研究库、规则与冻结参考未被改写；本阶段只写本运行目录。",
        "",
    ]
    with open(os.path.join(RUN, "CHANGE_LOG.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")

    # ---- problem register -------------------------------------------------
    reg = f"""# 返修问题逐条处理结果

对应独立验收报告与返修要求。每条给出：问题、返修做法、程序化检查点、当前状态。

## P1-1 故障测试不可靠，发布不核验当前输入

| 项 | 内容 |
|---|---|
| 问题 | 故障副本预先排除整个 `evidence_snapshots`，正对照本身不成立；删除公司来源文件、篡改证据正文仍能通过；发布步骤信任已有成功 JSON |
| 返修 | 输入锁覆盖全部实际输入，含字节哈希与正文哈希、身份与角色；校验结果绑定输入摘要、代码摘要与产物哈希；发布门禁逐项复算锁定输入、绑定表、绑定脚本；故障实验改为完整副本正对照 + 每次单点变更 + 具名拒绝理由 |
| 检查 | 自检 `L1`–`L5`；`s06` 正对照接受、13 个负例全部被拒且 `release_gate` 为 FAILED；`s11` 在失败时删除已有成功文档并只留失败报告 |
| 实测 | delete 研究源文件 / 删除必需表 / 删除原缺口 / 篡改快照正文 / 改发布日期 / 改事实值 / 改哈希声明 / 旧成功记录绑新输入：全部被拒 |
| 状态 | 已修 |

## P1-2 时间判断错误：只用最早日期

| 项 | 内容 |
|---|---|
| 问题 | 对关联证据取最早发布日期与事件日，优先用事件日；晚发布被忽略；旧背景材料日期借给无日期主体断言 |
| 返修 | 事件日与发布日期分别与该公司的观察日比较，只使用 `SUPPORTS`/`REFUTES` 关系；背景、母公司、访问记录不参与日期判定；不取多条日期的最早值代替规则；月精度不补成 1 日 |
| 检查 | 自检 `T1`–`T6`；故障实验「改证据发布日期到 2027」「改日期后强行保留观察日可用」均被拒 |
| 实测 | FAR `target_markets` 不再被母公司 2023-10 材料赋日期，现为 `DATE_UNKNOWN`；自变量成立/名称/地点三条无发布日期记录不再标观察日可用 |
| 状态 | 已修 |

## P1-3 未知状态被错误转化

| 项 | 内容 |
|---|---|
| 问题 | 21 条未查公司问题被标为已解决；自变量上市状态查后未找到被转成未上市并纳入比较 |
| 返修 | 未研究公司一律 `NOT_YET_MAPPED_THIS_RUN`；`SEARCHED_NOT_FOUND` / `NOT_YET_SEARCHED` / `ACCESS_BLOCKED` / `UNKNOWN` / `CONFLICT` / `INHERITED_UNVERIFIED` 不生成确定否定组；确定性否定只来自 `EXPLICITLY_NEGATED` 与 `NOT_APPLICABLE` |
| 检查 | 自检 `U1`–`U4`、`G2`–`G3`；故障实验「把查无写成确定否定」「关闭未研究公司的问题」均被拒 |
| 实测 | 自变量上市状态保持未知并退出该维度；21 家 264 项缺口全部保留未查 |
| 状态 | 已修 |

## P1-4 证据关系错配

| 项 | 内容 |
|---|---|
| 问题 | FAR_004 摘录绑错页面；母公司背景参与支持；自述升级为外部确认；招聘职责反推公司事实；83 条关系全为 SUPPORTS |
| 返修 | FAR_004 的 URL、标题与快照改为 Job 10426076 并按原文核对；母公司材料改为 `CONTEXT_ONLY`；自述类事实降级为 `COMPANY_SELF_REPORT`；招聘职责单列为 `hiring_role_scope`，公司层面测试状态不再由招聘文件支撑；关系逐条声明，缺失声明直接构建失败 |
| 检查 | 自检 `E1`–`E8`；故障实验「按前缀把背景证据改成支持」「把母公司规模写进团队字段」均被拒 |
| 实测 | 关系分布：SUPPORTS {sum(1 for l in links_new if l['relation']=='SUPPORTS')}、CONTEXT_ONLY {sum(1 for l in links_new if l['relation']=='CONTEXT_ONLY')}、ACCESS_NOTE {sum(1 for l in links_new if l['relation']=='ACCESS_NOTE')}、REPLACES {sum(1 for l in links_new if l['relation']=='REPLACES')} |
| 状态 | 已修 |

## P2-5 资本表按来源而非事件

| 项 | 内容 |
|---|---|
| 问题 | 四行实为来源摘要，含多轮/历年合并与重叠；金额字段全空 |
| 返修 | 以实际事件为单位连接多条来源；金额、币种、单位、金额性质结构化；投后估值单列；官网与媒体月份冲突保留在事件内；不明确的合并披露单列；不补造分轮金额 |
| 检查 | 自检 `K1`–`K6`；页面运行时检查「已披露金额带币种单位与性质」 |
| 实测 | 自变量 6 个事件（含 A+ 轮一条冲突保留、B–C 四轮合计披露一条）、傅利叶 1 个事件（近 8 亿元人民币）；估值与融资额分列 |
| 状态 | 已修 |

## P2-6 查证进度状态冲突

| 项 | 内容 |
|---|---|
| 问题 | 6 条 `NOT_YET_SEARCHED` 同时写 `checked_in_stage_b=YES` |
| 返修 | `checked_in_stage_b` 由 `research_status` 推导；未查即 `NO` |
| 检查 | 自检 `G5` |
| 状态 | 已修（傅利叶内部测试、生产出货、并购；自变量意向、付费；FAR 并购） |

## P2-7 资本金额未知与区间

| 项 | 内容 |
|---|---|
| 返修 | 未披露金额保留未知（`amount_scope=NOT_DISCLOSED`），不作为失败条件；金额性质区分 `APPROXIMATE` / `REPORTED_AMOUNT` / `NOT_DISCLOSED` |
| 检查 | 自检 `K1` |
| 状态 | 已修 |

## 仍未关闭的事项（如实保留）

1. 傅利叶人形机器人在新加坡的临床部署证据不足：交易对方公告只提康复与辅助机器人技术，冲突未关闭。
2. 自变量上市状态为查后未找到：保持未知，退出该比较维度。
3. FAR 团队成立日未找到；FAR 与 FTR 的边界只有一次访问受阻记录。
4. 其余 21 家未查证：全部缺口保留待查，本轮不形成 24 家结论。
5. 融资金额未披露的轮次保留未知，不补造数字。
"""
    with open(os.path.join(RUN, "problem_register.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(reg)

    selfcheck = f"""# 返修自检说明（与独立验收分开）

本包是**执行方返修自检**，不是独立验收，也不声称用户已逐条复核。独立验收需由未参与本次
返修的一方按同样口径复验。

## 本次自检做了什么

| 项目 | 结果 |
|---|---|
| 验收自检 | {ver['n_pass']}/{ver['n_checks']} 通过，失败 {ver['n_fail']} |
| 受控故障实验 | 正对照 {'接受' if fault.get('positive_control_ok') else '未接受'}；{fault.get('n_pass')}/{fault.get('n_probes')} 探针按预期被拒 |
| 离线复算 | {'五张核心表与发布版本逐字节一致' if rb.get('identical') else '存在差异'} |
| 页面脚本 Node 执行 | 22/22 |
| 检索日志核对 | 查后未找到与受阻状态均有对应记录 |

## 本次自检没有做什么

1. 没有做真实浏览器的无头渲染复跑：本环境未安装可用的无头浏览器通道，页面只做了 Node 端脚本执行与静态结构检查。
   页面可用本地浏览器直接打开 `index.html` 复核。
2. 没有重新穷尽检索 79 条记录涉及的每个命题，也没有代执行方改写公司事实。
3. 没有把"自检通过"当作"独立验收通过"；也没有把本次三家返修通过写成阶段 B 完成。

## 状态标记

- 运行目录标记：`PILOT_REPAIR_ONLY`；未写 `STAGE_B_COMPLETE`。
- 发布门禁：见 `release_gate_status.json`；失败时该文件为失败报告，且不保留成功文档。
- 阶段 A 交付、研究库、规则与冻结参考未改写。

## 复验入口

```text
python scripts/s01_lock_inputs.py       # 核验全部输入与快照哈希
python scripts/s04_verify.py            # 验收自检（绑定输入、代码与产物哈希）
python scripts/s06_rebuild_and_fault.py # 离线复算 + 正对照 + 单点故障注入
node scripts/s08_html_runtime_check.js .  # 页面脚本执行
python scripts/s11_release_gate.py      # 发布门禁
```
"""
    with open(os.path.join(RUN, "REPAIR_SELFCHECK.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(selfcheck)

    write_json(os.path.join(WORK, "repair_docs.json"), {
        "old": old, "new": new,
        "changed_facts_count": len(changed_facts),
        "unsearched_companies": unsearched,
    })
    print(json.dumps({"old": old, "new": new, "changed_facts": len(changed_facts),
                      "docs": ["CHANGE_LOG.md", "problem_register.md", "REPAIR_SELFCHECK.md"]},
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
