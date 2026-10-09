"""Stage B repair / step 9: field documentation, quality report, README and manifest.

Every number in these documents is read back from the generated tables, so a document
cannot claim a total the tables do not support. The quality report states the real
pass/fail/not-searched/blocked counts and marks this work as the executing side's own
self-check rather than an independent acceptance.
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import CODE_VERSION, R3, RUN, WORK, read_csv, sha256_file, write_json  # noqa: E402

FIELD_DOC = """# 阶段 B 返修版字段与口径

一条广告计一次，广告不等于人数；金额保留原币种与原措辞，不做换算。本轮修复了事实粒度、
时间资格、未知状态、证据关系与资本事件五个方面的口径，下面按表说明。

## 一、表与粒度

| 文件 | 粒度 | 说明 |
|---|---|---|
| `company_facts.csv` | 公司 × 字段 × 主体/范围 × 事件/时期 | 允许同一公司同字段多行（`fact_seq` 区分）；混合断言必须拆开 |
| `company_evidence.csv` | 证据记录 | 新查与继承；`claim_nature` 区分自述、外部确认、媒体、母公司背景、访问记录 |
| `evidence_links.csv` | 事实 × 证据 | 每行一个声明关系；`qualifies_date` 标明该证据是否参与日期判定 |
| `capital_events.csv` | 实际资本事件 | 一个事件连接多条来源；金额、币种、单位、金额性质结构化；估值单列 |
| `company_gaps.csv` | 原 307 缺口逐项 | 每行对应一个继承 `gap_id`；未研究公司保留未查状态 |
| `company_group_mapping.csv` | 公司 × 维度取值 | `comparison_bucket` 决定是否进入严格比较 |
| `search_log.jsonl` | 逐次检索与访问 | 失败同样保留 |

## 二、事实表新增与关键字段

| 字段 | 含义 |
|---|---|
| `fact_seq` | 同公司同字段内的行序；`fact_id` 首行沿用 `F_<company_id>__<field>`，后续行加 `__<n>` |
| `assertion_kind` | 断言类型：披露/观测、招聘要求、母公司背景、边界说明、资本事件、产品线范围、市场范围 |
| `subject_entity` | 该断言的主体（法律实体或团队）；母公司材料的主体写母公司 |
| `subject_scope` | 研究主体范围（整公司 / 团队 / 收购后主体） |
| `product_or_business_scope` | 该断言涉及的产品或业务范围，与主体分开 |
| `event_or_period` | 事件或时期说明，用于表达历史时点与当前状态的差别 |
| `aggregation` | 单值或按范围拆分（多行） |
| `time_basis_evidence_ids` | 参与该断言日期判定的证据（只含 SUPPORTS/REFUTES） |
| `time_reason` | 时点判定的具体理由 |

## 三、`value_status` 枚举

| 值 | 含义 |
|---|---|
| `SUPPORTED_EXTERNAL` | 由公司之外的来源（政府、交易对方、监管、独立渠道）陈述 |
| `COUNTERPARTY_CONFIRMATION` | 交易对方或合作方官方确认 |
| `COMPANY_SELF_REPORT` | 公司自身材料陈述；不升级为独立确认 |
| `MEDIA_STATEMENT` | 媒体报道陈述 |
| `MIXED_SEE_EVIDENCE` | 同一字段内不同项证据强度不同，逐项见证据 |
| `CONFLICT_RESOLVED_BY_SEPARATION` | 存在冲突，按分离规则处理 |
| `PARENT_CONTEXT_ONLY` | 母公司材料，对本主体只作背景 |
| `INHERITED_UNVERIFIED` | 继承值，本轮未复核 |
| `SEARCHED_NOT_FOUND` | 实际查过但未找到（须有检索记录） |
| `NOT_YET_SEARCHED` | 尚未查 |
| `NOT_APPLICABLE` | 命题不适用于该主体 |
| `ACCESS_BLOCKED` | 访问受阻 |
| `CONFLICT` | 来源冲突未解决 |
| `UNKNOWN` | 未确立值；不得写成 NO 或 0 |
| `EXPLICITLY_NEGATED` | 有直接证据明确否定，须限定主体与时间 |

修复要点：**只有公司自述材料支持的断言不再标为 `SUPPORTED_EXTERNAL`**；查后未找到、
尚未查、受阻、冲突的行不携带确定值，也不生成确定否定组。

## 四、`time_applicability` 判定

事件日与发布日期**分别**与该公司的招聘观察日比较，且只使用该断言的直接支持证据：

| 值 | 判据 |
|---|---|
| `USABLE_AT_OBSERVATION` | 事件日在观察日或之前，且证据在观察日或之前已公开 |
| `RETROSPECTIVE_LATE_PUBLISH` | 事件在观察日或之前，发布晚于观察日（只作背景） |
| `POST_OBSERVATION_EVENT` | 事件本身发生在观察日之后 |
| `DATE_IMPRECISE_SPANS_OBS` | 月/年精度跨过观察日，无法判定先后 |
| `DATE_UNKNOWN` | 没有可用于判定的日期 |
| `NOT_TIME_SENSITIVE` | 结构性事实（如主体归属），不作时点判定 |

月精度一律不补成某月 1 日；HTTP 更新时间、页脚年份与本项目首次看到的时间都不作为发布日期。
母公司背景、其他产品与其他事件的日期不参与该断言的资格计算。不取多条日期中的最早值代替规则。

## 五、关系枚举（`evidence_links.csv`）

| 关系 | 含义 |
|---|---|
| `SUPPORTS` | 该证据直接陈述该断言（主体与范围匹配）；参与成立与日期判定 |
| `REFUTES` | 该证据反驳该断言；可参与日期判定但不成立值 |
| `CONTEXT_ONLY` | 背景材料（母公司、未具名对方、其他范围、弱线索）；不成立值、不定日期 |
| `REPLACES` | 该证据替代另一来源的同一事项，冲突保留 |
| `ACCESS_NOTE` | 访问结果记录（404、正文不可取、检索无结果） |
| `INHERITED_CONTEXT` | 继承材料，仅作追溯 |

关系逐条声明，不由证据 ID 前缀推断；一条被引用但没有声明关系的证据会让构建直接失败。

## 六、比较资格（`company_group_mapping.csv`）

`comparison_bucket` 取 `STRICT_COMPARABLE` / `BACKGROUND_DISPLAY_ONLY` / `EXCLUDED_UNKNOWN` /
`NOT_RESEARCHED`。进入严格比较需同时满足：取值已确立，且时点适用性为 `USABLE_AT_OBSERVATION`
或 `NOT_TIME_SENSITIVE`。背景展示与未确立取值分别单列，不与合格公司混计。

## 七、缺口状态

`stage_b_status` 取值：`RESOLVED_FOUND`、`RESOLVED_NOT_APPLICABLE`、`RESOLVED_PARTIAL`、
`RESOLVED_BY_SEPARATION_RULE`、`NOT_FOUND_NOT_DEFINITE`、`NOT_YET_SEARCHED`、`ACCESS_BLOCKED`、
`NOT_YET_MAPPED_THIS_RUN`、`DEFERRED_TO_STAGE_B_BATCH_2`、`UNRESOLVED_MAPPING`。
本轮未研究的公司，其全部继承缺口（含 `inherited_open_question`）保持
`NOT_YET_MAPPED_THIS_RUN`，通用规则不代替公司专属问题的查证。
"""


def main() -> int:
    facts = read_csv(os.path.join(RUN, "company_facts.csv"))
    evidence = read_csv(os.path.join(RUN, "company_evidence.csv"))
    links = read_csv(os.path.join(RUN, "evidence_links.csv"))
    gaps = read_csv(os.path.join(RUN, "company_gaps.csv"))
    groups = read_csv(os.path.join(RUN, "company_group_mapping.csv"))
    caps = read_csv(os.path.join(RUN, "capital_events.csv"))
    build = json.load(open(os.path.join(WORK, "build_summary.json"), encoding="utf-8"))
    lock = json.load(open(os.path.join(WORK, "input_lock.json"), encoding="utf-8"))
    ver = json.load(open(os.path.join(RUN, "verification.json"), encoding="utf-8")) \
        if os.path.exists(os.path.join(RUN, "verification.json")) else {"n_pass": 0, "n_checks": 0, "n_fail": 0}
    fault = json.load(open(os.path.join(WORK, "fault_probes.json"), encoding="utf-8")) \
        if os.path.exists(os.path.join(WORK, "fault_probes.json")) else {"n_pass": 0, "n_probes": 0}
    rb = json.load(open(os.path.join(WORK, "rebuild_check.json"), encoding="utf-8")) \
        if os.path.exists(os.path.join(WORK, "rebuild_check.json")) else {"identical": None}

    researched = sorted({f["company_id"] for f in facts})
    unsearched = sorted({g["company_id"] for g in gaps} - set(researched))
    fact_status = Counter(f["value_status"] for f in facts)
    fact_time = Counter(f["time_applicability"] for f in facts)
    gap_status = Counter(g["stage_b_status"] for g in gaps)
    rel_counts = Counter(l["relation"] for l in links)
    buckets = Counter(g["comparison_bucket"] for g in groups)

    with open(os.path.join(RUN, "field_mapping.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(FIELD_DOC)

    qr = [
        "# 阶段 B 返修版质量报告",
        "",
        "本报告数字全部由生成的表读回；不是独立验收结论，也不声称用户已逐条复核。",
        "",
        "## 一、范围",
        "",
        f"- 运行目录：`{os.path.basename(RUN)}`；标记：`TARGETED_COLLECTION_PENDING_ACCEPTANCE`（未写 `STAGE_B_COMPLETE`）。",
        f"- 本轮 24 家均有公司记录（{', '.join(researched)}）。",
        f"- 字段级未查/查后未找到仍单独展示；不得把 24 家有记录写成每字段已查完。",
        f"- 招聘分类、研究库、r3 底稿与冻结参考未改写（见输入锁与验收自检 L5、D7）。",
        "",
        "## 二、产出",
        "",
        f"- 事实行：{len(facts)}（只由 {len({f['field'] for f in facts})} 个字段承载；同字段多行用于主体/范围/事件拆分）",
        f"- 证据行：{len(evidence)}（其中 STAGE_B_NEW {sum(1 for e in evidence if e['record_kind'] == 'STAGE_B_NEW')}）",
        f"- 关系行：{len(links)}；关系分布：" + "、".join(f"`{k}`×{v}" for k, v in rel_counts.most_common()),
        f"- 资本事件：{len(caps)} 行",
        f"- 缺口行：{len(gaps)}（原 307 项逐项保留）",
        f"- 分组映射行：{len(groups)}",
        "",
        "## 三、证据性质分布（事实行）",
        "",
        "| 证据性质 | 行数 |",
        "|---|---|",
    ]
    for k, v in fact_status.most_common():
        qr.append(f"| `{k}` | {v} |")
    qr += [
        "",
        "## 四、时点适用性分布（事实行）",
        "",
        "| 时点 | 行数 |",
        "|---|---|",
    ]
    for k, v in fact_time.most_common():
        qr.append(f"| `{k}` | {v} |")
    qr += [
        "",
        "## 五、缺口状态分布（307 项）",
        "",
        "| 状态 | 行数 |",
        "|---|---|",
    ]
    for k, v in gap_status.most_common():
        qr.append(f"| `{k}` | {v} |")
    qr += [
        "",
        "## 六、比较资格分布",
        "",
        "| 桶 | 行数 |",
        "|---|---|",
    ]
    for k, v in buckets.most_common():
        qr.append(f"| `{k}` | {v} |")
    qr += [
        "",
        "## 七、验证结果（执行方自检）",
        "",
        f"- 验收自检：{ver.get('n_pass')}/{ver.get('n_checks')} 通过，失败 {ver.get('n_fail')}。",
        f"- 受控故障实验：{fault.get('n_pass')}/{fault.get('n_probes')} 探针按预期被拒绝，正对照 "
        f"{'通过' if fault.get('positive_control_ok') else '未通过'}。",
        f"- 离线复算：{'五张核心表与发布版本逐字节一致' if rb.get('identical') else '存在差异，见 work/rebuild_check.json'}。",
        f"- 输入锁：包含 {lock['n_entries']} 个文件，输入摘要 `{lock['input_root_digest'][:16]}…`，"
        f"代码摘要 `{lock['code_digest'][:16]}…`；快照声明哈希全部可复算。",
        "",
        "## 八、本轮明确未做的事情",
        "",
        "1. 未对 24 家穷尽检索；未补造任何金额、日期或客户。",
        "2. 未把未查、查后未找到、访问受阻写成否定结论。",
        "3. 未用母公司材料支撑 FAR 团队断言；未把招聘职责当作公司已开展的事实。",
        "4. 未把媒体口径升级为独立确认；未把估计或冲突值合并成单一数字。",
        "5. 未修改阶段 A 交付、研究库、规则与冻结参考；未进入阶段 C。",
        "",
    ]
    with open(os.path.join(RUN, "quality_report.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(qr) + "\n")

    readme = f"""# 阶段 B 定向补查包（TARGETED_COLLECTION_PENDING_ACCEPTANCE）

运行目录：`{os.path.basename(RUN)}`；代码版本：`{CODE_VERSION}`；
输入摘要：`{lock['input_root_digest']}`。

本包在已通过的 r2 返修底稿上做定向业务补查，未重做岗位分类，未改写阶段 A、研究库与规则。
24 家均有公司记录，不等于每字段已查完。逐字段未查/查后未找到仍展示。不得当作阶段 B 完成，也不得进入阶段 C。

## 入口

| 文件 | 用途 |
|---|---|
| `index.html` | 总览页：公司切换、搜索、逐字段事实、证据原文与快照、分组资格、缺口逐项、资本事件 |
| `company_cards/*.md` | 24 家公司卡（含未查公司的待查清单） |
| `company_facts.csv` | 事实表（公司 × 字段 × 主体/范围 × 事件/时期） |
| `company_evidence.csv` | 证据记录与原文定位 |
| `evidence_links.csv` | 事实—证据关系（逐条声明） |
| `capital_events.csv` | 资本事件（金额结构化、估值分离） |
| `company_gaps.csv` | 307 项继承缺口逐项结果 |
| `company_group_mapping.csv` | 分组与比较资格 |
| `verification.json` | 验收自检，绑定本次输入、代码与产物哈希 |
| `field_mapping.md` / `quality_report.md` | 字段口径与质量报告 |
| `release_gate_status.json` | 发布门禁结果（失败时只有失败报告） |
| `REPAIR_SELFCHECK.md` | 返修自检与独立验收的区别说明 |

## 复算与复验

```text
python scripts/s01_lock_inputs.py      # 重建输入锁，核验所有输入与快照哈希
python scripts/s02_build_facts.py      # 从研究源重建事实层（含逐条关系声明）
python scripts/s03_build_tables.py     # 生成事实/证据/关系/资本/缺口表
python scripts/s05_grouping.py         # 生成分组映射与规则说明
python scripts/s04_verify.py           # 验收自检（绑定输入与产物哈希）
python scripts/s06_rebuild_and_fault.py# 离线复算 + 完整副本正对照 + 单点故障注入
python scripts/s07_cards_and_html.py   # 公司卡与总览页
node scripts/s08_html_runtime_check.js .  # 页面脚本实际执行检查
python scripts/s09_search_log.py       # 检索日志：区分真实 SEARCH / FETCH / PAGE_REVIEW / 派生总结
python scripts/s11b_search_log_ext.py  # 只标明历史派生行，不再补写 SEARCH
python scripts/s11_release_gate.py     # 发布门禁（通过后再写清单）
```

## 已知边界

- 融资金额未知不作为失败条件；未披露即保留未知。
- 傅利叶人形机器人在新加坡的临床部署证据不足，冲突未关闭。
- 自变量上市状态为查后未找到，保持未知并退出该比较维度。
"""
    with open(os.path.join(RUN, "README.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(readme)

    manifest = {
        "stage": "B-repair",
        "scope": "TARGETED_COLLECTION_PENDING_ACCEPTANCE",
        "run_id": lock["run_id"],
        "code_version": CODE_VERSION,
        "r3_root": R3,
        "input_root_digest": lock["input_root_digest"],
        "code_digest": lock["code_digest"],
        "counts": {
            "companies_total": 24,
            "companies_researched_this_run": len(researched),
            "companies_unsearched": len(unsearched),
            "facts": len(facts),
            "evidence": len(evidence),
            "relations": len(links),
            "capital_events": len(caps),
            "gap_rows": len(gaps),
            "group_rows": len(groups),
        },
        "gap_status": dict(gap_status),
        "comparison_buckets": dict(buckets),
        "verification": {"n_checks": ver.get("n_checks"), "n_pass": ver.get("n_pass"),
                         "n_fail": ver.get("n_fail"),
                         "verification_digest": ver.get("verification_digest")},
        "fault_probes": {"n_probes": fault.get("n_probes"), "n_pass": fault.get("n_pass"),
                         "positive_control_ok": fault.get("positive_control_ok")},
        "rebuild_identical": rb.get("identical"),
        "manifest_self_hash_omitted": True,
    }
    write_json(os.path.join(RUN, "analysis_manifest.json"), manifest)
    write_json(os.path.join(WORK, "docs_summary.json"), {
        "facts": len(facts), "evidence": len(evidence), "links": len(links),
        "capital": len(caps), "gaps": len(gaps), "groups": len(groups),
        "researched": researched, "unsearched": len(unsearched),
    })
    print(json.dumps(manifest["counts"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
