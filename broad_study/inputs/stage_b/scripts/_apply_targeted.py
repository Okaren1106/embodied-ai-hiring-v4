"""Write dated business evidence into this targeted-collection pack only."""
from __future__ import annotations

import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import RUN, WORK  # noqa: E402
from s03_fetch import SEARCH_LOG, append_jsonl  # noqa: E402

RES = os.path.join(WORK, "research")
NOW = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
RETRIEVED = "2026-09-15"


def load(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save(path: str, doc) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def authored(cid: str) -> str:
    return os.path.join(RES, f"authored_{cid}.json")


def ev(**kwargs) -> dict:
    row = {
        "record_kind": "STAGE_B_NEW",
        "linked_inherited_evidence": [],
        "relation_to_inherited": "",
        "retrieved_at": RETRIEVED,
        "access_status": "OK",
    }
    row.update(kwargs)
    return row


def upsert_ev(doc: dict, row: dict) -> None:
    eid = row["evidence_id"]
    for i, old in enumerate(doc["evidence"]):
        if old["evidence_id"] == eid:
            if old.get("url") != row.get("url"):
                raise ValueError(f"Evidence identity collision: {eid}; assign a new ID")
            doc["evidence"][i] = row
            return
    doc["evidence"].append(row)


def set_fact(doc: dict, field: str, **kwargs) -> None:
    for f in doc["facts"]:
        if f["field"] == field:
            f.update(kwargs)
            f.pop("research_status", None)
            if kwargs.get("value_status") in ("NOT_YET_SEARCHED", "SEARCHED_NOT_FOUND", "ACCESS_BLOCKED"):
                f["research_status"] = kwargs["value_status"]
            return
    raise SystemExit(f"missing fact {doc.get('company_id')}:{field}")


def set_rel(doc: dict, field: str, evidence: str, role: str, note: str) -> None:
    for r in doc["relations"]:
        if r["fact"] == field and r["evidence"] == evidence:
            r["role"] = role
            r["review_note"] = note
            return
    doc["relations"].append({"fact": field, "evidence": evidence, "role": role, "review_note": note})


def bind(rules: dict, dimension: str, cid: str, value: str, labels: list[str]) -> None:
    for dim in rules["dimensions"]:
        if dim["dimension"] == dimension:
            dim["group_bindings"].setdefault(cid, {})[value] = labels
            return
    raise SystemExit(dimension)


def log(action: str, **kwargs) -> None:
    rec = {"ts_utc": NOW, "action": action}
    rec.update(kwargs)
    append_jsonl(SEARCH_LOG, rec)


def main() -> int:
    # --- Agility -----------------------------------------------------------
    a = load(authored("US_AGILITY"))
    upsert_ev(a, ev(
        evidence_id="B_US_AGILITY_005",
        field="product_lines / delivery_form / target_markets / deployment_status_actual",
        claim="GXO 于 2024-06-27 宣布与 Agility 签署多年 RaaS 协议，在 SPANX 设施部署 Digit 人形机器人与 Agility Arc 云平台，此前 2023 年底完成概念验证；该页称这是人形机器人首次正式商业部署与首次人形 RaaS 部署。扩张规模为协议下继续探索，不记为已部署台数。",
        quote="Greenwich, USA | June 27, 2024 … Robots-as-a-Service (RaaS) agreement integrates Agility’s Humanoid robots with other cobots at SPANX facility … This agreement, which follows a proof-of-concept pilot in late 2023, is both the industry’s first formal commercial deployment of humanoid robots and first Robots-as-a-Service (RaaS) deployment of humanoid robots. … As part of the RaaS agreement, GXO is deploying Digit robots and Agility Arc ™, Agility’s cloud automation platform for deploying and managing Digit fleets.",
        quote_locator="标题区日期行、副题与正文第 1—4 段",
        source_title="GXO signs industry-first multi-year agreement with Agility Robotics",
        publisher="GXO Logistics, Inc.",
        source_nature="COUNTERPARTY_CONFIRMATION",
        url="https://gxo.com/news_article/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics/",
        publication_date="2024-06-27",
        event_date="2024-06-27",
        event_date_precision="DAY",
        date_precision="DAY",
        claim_nature="COUNTERPARTY_CONFIRMATION",
        snapshot_id="gxo_digit_raas_html",
        note="客户一侧官方新闻稿。1000 台 Digit v5 秋季交付不在本页，仍留在媒体计划口径，不并入本条。",
    ))
    set_fact(a, "product_lines",
             value="Digit 双足移动操作人形机器人（MMR）；Agility Arc 云端机队部署与管理平台",
             value_status="COUNTERPARTY_CONFIRMATION",
             evidence_ids=["B_US_AGILITY_005"],
             decision_reason="GXO 客户公告同时写明 Digit 与 Arc；官网无日期产品页改为背景")
    set_fact(a, "delivery_form",
             value="Robots-as-a-Service（RaaS）：GXO 多年协议在 SPANX 设施部署 Digit 人形机器人与 Agility Arc 云平台",
             value_status="COUNTERPARTY_CONFIRMATION",
             evidence_ids=["B_US_AGILITY_005"],
             decision_reason="交付形态以客户公告的 RaaS 为准；媒体所报 1000 台秋季交付为计划，不写入本条")
    set_fact(a, "target_markets",
             value="合同物流仓库现场（GXO SPANX 设施；从协作机器人取料箱放到传送带等重复作业）",
             value_status="COUNTERPARTY_CONFIRMATION",
             evidence_ids=["B_US_AGILITY_005"],
             decision_reason="场景以 GXO 现场描述为准，不把媒体列举的其他行业并入本条")
    set_fact(a, "named_customers_or_partners",
             value="GXO Logistics（多年 RaaS，SPANX 设施）",
             value_status="COUNTERPARTY_CONFIRMATION",
             evidence_ids=["B_US_AGILITY_005"],
             decision_reason="具名客户来自对方公告；Toyota 等媒体名单改为背景")
    set_fact(a, "deployment_status_actual",
             value="GXO SPANX 设施已部署 Digit 与 Arc，协助从协作机器人取料箱放到传送带（客户所称商业部署；协议下继续探索更多用例，不记已部署台数）",
             value_status="COUNTERPARTY_CONFIRMATION",
             evidence_ids=["B_US_AGILITY_005"],
             decision_reason="已发生的是 SPANX 现场部署；扩展规模不是本条取值")
    set_fact(a, "evidence_external_pilot",
             value="2023 年底 GXO 概念验证之后进入 SPANX 商业部署（客户公告）",
             value_status="COUNTERPARTY_CONFIRMATION",
             evidence_ids=["B_US_AGILITY_005"],
             decision_reason="试点与随后商业部署均由客户公告陈述")
    set_rel(a, "product_lines", "B_US_AGILITY_004", "CONTEXT_ONLY", "无日期官网，仅作背景")
    set_rel(a, "product_lines", "B_US_AGILITY_003", "CONTEXT_ONLY", "媒体 Digit v5 计划，仅作背景")
    set_rel(a, "product_lines", "B_US_AGILITY_005", "SUPPORTS", "GXO 公告的 Digit 与 Arc")
    set_rel(a, "delivery_form", "B_US_AGILITY_003", "CONTEXT_ONLY", "媒体 RaaS 金额与秋季计划，仅作背景")
    set_rel(a, "delivery_form", "B_US_AGILITY_001", "CONTEXT_ONLY", "媒体月份精度跨越观察日，仅作背景")
    set_rel(a, "delivery_form", "B_US_AGILITY_005", "SUPPORTS", "GXO 多年 RaaS")
    set_rel(a, "target_markets", "B_US_AGILITY_004", "CONTEXT_ONLY", "无日期官网行业，仅作背景")
    set_rel(a, "target_markets", "B_US_AGILITY_003", "CONTEXT_ONLY", "媒体客户行业，仅作背景")
    set_rel(a, "target_markets", "B_US_AGILITY_005", "SUPPORTS", "GXO SPANX 仓库现场")
    set_rel(a, "named_customers_or_partners", "B_US_AGILITY_003", "CONTEXT_ONLY", "媒体客户名单未获对方确认")
    set_rel(a, "named_customers_or_partners", "B_US_AGILITY_001", "CONTEXT_ONLY", "媒体补充名单")
    set_rel(a, "named_customers_or_partners", "B_US_AGILITY_005", "SUPPORTS", "GXO 自身公告")
    set_rel(a, "deployment_status_actual", "B_US_AGILITY_003", "CONTEXT_ONLY", "媒体运行时长，仅作背景")
    set_rel(a, "deployment_status_actual", "B_US_AGILITY_001", "CONTEXT_ONLY", "媒体月份精度跨越观察日")
    set_rel(a, "deployment_status_actual", "B_US_AGILITY_005", "SUPPORTS", "GXO SPANX 商业部署")
    set_rel(a, "evidence_external_pilot", "B_US_AGILITY_003", "CONTEXT_ONLY", "媒体客户现场，仅作背景")
    set_rel(a, "evidence_external_pilot", "B_US_AGILITY_005", "SUPPORTS", "GXO 所述 2023 试点与随后部署")
    save(authored("US_AGILITY"), a)

    # --- Physical Intelligence --------------------------------------------
    p = load(authored("US_PHYSICAL_INTELLIGENCE"))
    upsert_ev(p, ev(
        evidence_id="B_US_PI_002",
        field="product_lines / delivery_form / target_markets / evidence_demo",
        claim="Physical Intelligence 于 2024-10-31 发布 π0（pi-zero）通用机器人基础模型，可控制多种机器人，经文本提示或微调执行任务；页面展示洗衣、叠衣、做咖啡、装袋等研究演示。该页不是付费客户或商业部署记录。",
        quote="Published October 31, 2024 … we’ve developed a general-purpose robot foundation model that we call π 0 (pi-zero). … It can control a variety of different robots, and can either be prompted to carry out the desired task, or fine-tuned to specialize it to challenging application scenarios. … Laundry Folding clothes Make coffee Bag groceries",
        quote_locator="发布日期行、导语段与任务示意",
        source_title="π0: Our First Generalist Policy",
        publisher="Physical Intelligence",
        source_nature="OFFICIAL_COMPANY",
        url="https://www.pi.website/blog/pi0",
        publication_date="2024-10-31",
        event_date="2024-10-31",
        event_date_precision="DAY",
        date_precision="DAY",
        claim_nature="COMPANY_SELF_REPORT",
        snapshot_id="pi0_official",
        note="研究演示不等于付费客户；不能用 π0 日期证明后来的 π0.7。",
    ))
    set_fact(p, "product_lines",
             value="π0（pi-zero）跨本体通用机器人基础模型（官方 2024-10-31 发布；可控制多种机器人，经文本提示或微调执行任务）",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_PI_002"],
             decision_reason="以带日期的 π0 发布页为准；无日期官网 π0.7 改为背景")
    set_fact(p, "delivery_form",
             value="研究型基础模型发布；页面展示跨本体策略与任务演示，未陈述对外销售、许可合同或付费客户",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_PI_002"],
             decision_reason="该页证明模型存在，不证明商业交付形态")
    set_fact(p, "target_markets",
             value="研究演示任务含洗衣、叠衣、做咖啡、装袋等操作；未给出商业行业清单",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_PI_002"],
             decision_reason="任务清单来自研究发布页，不升级为已签约行业")
    set_fact(p, "deployment_status_actual",
             value="",
             value_status="SEARCHED_NOT_FOUND",
             research_status="SEARCHED_NOT_FOUND",
             evidence_ids=["B_US_PI_002"],
             decision_reason="打开 π0 发布页未见付费客户或商业部署；研究演示不记为部署")
    set_fact(p, "evidence_demo",
             value="π0 发布页展示跨本体策略与洗衣、叠衣、做咖啡、装袋等研究演示",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_PI_002"],
             decision_reason="演示来自官方研究发布")
    set_rel(p, "product_lines", "B_US_PI_001", "CONTEXT_ONLY", "无日期官网 π0.7，仅作背景")
    set_rel(p, "product_lines", "B_US_PI_002", "SUPPORTS", "π0 带日期发布")
    set_rel(p, "delivery_form", "B_US_PI_001", "CONTEXT_ONLY", "无日期官网伙伴自述")
    set_rel(p, "delivery_form", "B_US_PI_002", "SUPPORTS", "研究模型发布，非许可合同")
    set_rel(p, "target_markets", "B_US_PI_001", "CONTEXT_ONLY", "无日期方向性自述")
    set_rel(p, "target_markets", "B_US_PI_002", "SUPPORTS", "发布页任务演示")
    set_rel(p, "deployment_status_actual", "B_US_PI_002", "CONTEXT_ONLY", "该页无部署陈述，作查后未找到依据")
    set_rel(p, "evidence_demo", "B_US_PI_002", "SUPPORTS", "研究演示")
    save(authored("US_PHYSICAL_INTELLIGENCE"), p)

    # --- Field AI ----------------------------------------------------------
    f = load(authored("US_FIELD_AI"))
    upsert_ev(f, ev(
        evidence_id="B_US_FIELD_AI_002",
        field="product_lines / delivery_form / target_markets / deployment_status_actual",
        claim="Field AI 于 2025-08-20 官方宣布 FFM／单一软件大脑可驱动多种机器人，并列出建筑、能源、制造、城市配送与巡检等范围；同时自述已在全球众多客户现场日常运行、并在数百个复杂工业环境测试与部署。部署量为公司自述。",
        quote="Press Release August 20, 2025 … FieldAI is at the forefront of the general-purpose robotics revolution, developing a single software brain that is powering a variety of robots in many diverse environments. FieldAI robots are deployed in daily operations at numerous customer sites worldwide. Deployments span a variety of robot types in high-complexity environments from Japan, to Europe, to the U.S., with some of the world’s largest companies in industries including construction, energy, manufacturing, urban delivery and inspection. … successful testing and deployments across hundreds of complex real-world industrial environments.",
        quote_locator="日期行与正文部署／行业段",
        source_title="FieldAI Announces Over $400M in Funds Raised to Advance Embodied AI at Scale",
        publisher="Field AI",
        source_nature="OFFICIAL_COMPANY",
        url="https://www.fieldai.com/news/fieldai-announces-over-400m-in-funds-raised-to-advance-embodied-ai-at-scale",
        publication_date="2025-08-20",
        event_date="2025-08-20",
        event_date_precision="DAY",
        date_precision="DAY",
        claim_nature="COMPANY_SELF_REPORT",
        snapshot_id="fieldai_20250820",
        note="本条用于业务范围与自述部署，不把融资金额写入比较变量。",
    ))
    set_fact(f, "product_lines",
             value="Field Foundation Models（FFMs）单一软件大脑／风险感知机器人基础模型；可驱动多种机器人形态",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_FIELD_AI_002"],
             decision_reason="以 2025-08-20 官方公告为准；无日期首页改为背景")
    set_fact(f, "delivery_form",
             value="软件大脑在客户工作流中边缘实时部署（公司自述）；未陈述独立确认的许可或销售合同形态",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_FIELD_AI_002"],
             decision_reason="交付为公司自述的现场部署，不升级为已核验许可合同")
    set_fact(f, "target_markets",
             value="建筑、能源、制造、城市配送与巡检（官方 2025-08-20 公告）",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_FIELD_AI_002"],
             decision_reason="行业清单来自带日期公告")
    set_fact(f, "deployment_status_actual",
             value="公司自述已在全球众多客户现场日常运行，并在数百个复杂工业环境测试与部署；部署量为自述，未取得客户确认",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_FIELD_AI_002"],
             decision_reason="部署量保持自述，不升级为客户确认")
    set_rel(f, "product_lines", "B_US_FIELD_AI_001", "CONTEXT_ONLY", "无日期首页")
    set_rel(f, "product_lines", "B_US_FIELD_AI_002", "SUPPORTS", "2025-08-20 公告")
    set_rel(f, "delivery_form", "B_US_FIELD_AI_001", "CONTEXT_ONLY", "无日期首页")
    set_rel(f, "delivery_form", "B_US_FIELD_AI_002", "SUPPORTS", "公告中的现场部署自述")
    set_rel(f, "target_markets", "B_US_FIELD_AI_001", "CONTEXT_ONLY", "无日期首页分类")
    set_rel(f, "target_markets", "B_US_FIELD_AI_002", "SUPPORTS", "公告行业清单")
    set_rel(f, "deployment_status_actual", "B_US_FIELD_AI_001", "CONTEXT_ONLY", "无日期三大洲自述")
    set_rel(f, "deployment_status_actual", "B_US_FIELD_AI_002", "SUPPORTS", "公告自述部署")
    save(authored("US_FIELD_AI"), f)

    # --- Skild -------------------------------------------------------------
    s = load(authored("US_SKILD"))
    upsert_ev(s, ev(
        evidence_id="B_US_SKILD_003",
        field="product_lines / delivery_form / target_markets",
        claim="Skild 于 2025-07-29 发布 Skild Brain：跨四足、人形、桌面臂、移动操作等形态的机器人基础模型。",
        quote="By Skild AI Team · 29 July, 2025 … Our foundation model, the Skild Brain , which works on various quadrupeds, humanoids, table-top arms, mobile manipulators and more",
        quote_locator="署名日期行与模型段",
        source_title="Building the general-purpose robotic brain",
        publisher="Skild AI",
        source_nature="OFFICIAL_COMPANY",
        url="https://www.skild.ai/blogs/building-the-general-purpose-robotic-brain",
        publication_date="2025-07-29",
        event_date="2025-07-29",
        event_date_precision="DAY",
        date_precision="DAY",
        claim_nature="COMPANY_SELF_REPORT",
        snapshot_id="skild_brain_20250729",
        note="研究／产品发布，不是付费客户确认。",
    ))
    upsert_ev(s, ev(
        evidence_id="B_US_SKILD_004",
        field="product_lines / delivery_form",
        claim="Skild 于 2026-08-18 发布旗舰基础模型 S1，定位为上下文学习／视频提示的机器人基础模型。",
        quote="Introducing S1: In-Context Learning for Robotics … Skild AI. Introducing S1: In-Context Learning for Robotics. August 2026. https://skild.ai/blogs/s1",
        quote_locator="标题与文末引用块",
        source_title="Introducing S1: In-Context Learning for Robotics",
        publisher="Skild AI",
        source_nature="OFFICIAL_COMPANY",
        url="https://skild.ai/blogs/s1",
        publication_date="2026-08-18",
        event_date="2026-08-18",
        event_date_precision="DAY",
        date_precision="DAY",
        claim_nature="COMPANY_SELF_REPORT",
        snapshot_id="skild_s1_20260818",
        note="页内引用写 August 2026，meta 为 Aug 18, 2026；早于观察日 2026-09-11。",
    ))
    set_fact(s, "product_lines",
             value="Skild Brain 跨形态机器人基础模型（四足、人形、桌面臂、移动操作等，2025-07-29）；S1 旗舰基础模型（官方 2026-08-18 发布，上下文学习）",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_SKILD_003", "B_US_SKILD_004"],
             decision_reason="两条带日期官方发布；无日期首页与 ARR 博客改为背景")
    set_fact(s, "delivery_form",
             value="研究型基础模型发布（Skild Brain / S1）；商业许可与付费交付仅见无日期博客自述，不纳入本条",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_SKILD_003", "B_US_SKILD_004"],
             decision_reason="有日期页只证明模型发布，不证明许可合同")
    set_fact(s, "target_markets",
             value="跨形态机器人控制（四足、人形、桌面臂、移动操作）；未给出已签约商业行业清单",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_SKILD_003"],
             decision_reason="形态范围来自 Brain 发布页")
    set_rel(s, "product_lines", "B_US_SKILD_001", "CONTEXT_ONLY", "无日期 ARR 博客")
    set_rel(s, "product_lines", "B_US_SKILD_002", "CONTEXT_ONLY", "无日期首页")
    set_rel(s, "product_lines", "B_US_SKILD_003", "SUPPORTS", "Brain 发布")
    set_rel(s, "product_lines", "B_US_SKILD_004", "SUPPORTS", "S1 发布")
    set_rel(s, "delivery_form", "B_US_SKILD_001", "CONTEXT_ONLY", "无日期商业自述")
    set_rel(s, "delivery_form", "B_US_SKILD_003", "SUPPORTS", "模型发布")
    set_rel(s, "delivery_form", "B_US_SKILD_004", "SUPPORTS", "S1 发布")
    set_rel(s, "target_markets", "B_US_SKILD_001", "CONTEXT_ONLY", "无日期场景清单")
    set_rel(s, "target_markets", "B_US_SKILD_002", "CONTEXT_ONLY", "无日期首页")
    set_rel(s, "target_markets", "B_US_SKILD_003", "SUPPORTS", "跨形态范围")
    save(authored("US_SKILD"), s)

    # --- Dexterity ---------------------------------------------------------
    d = load(authored("US_DEXTERITY"))
    upsert_ev(d, ev(
        evidence_id="B_US_DEXTERITY_002",
        field="product_lines / delivery_form / target_markets",
        claim="Dexterity 于 2025-03-17 发布 Mech：工业双臂移动操作机器人，首发应用为卡车装载，并称向工业与企业客户提供。",
        quote="← Back to Blog March 17, 2025 Meet the Mech … Mech, the first industrial superhumanoid robot designed specifically to transform enterprises. … The initial application available at launch is a specialized truck-loading app … Mech is available to Dexterity's industrial and enterprise customers for truck loading",
        quote_locator="日期行、导语与供应段",
        source_title="Meet the Mech",
        publisher="Dexterity, Inc.",
        source_nature="OFFICIAL_COMPANY",
        url="https://dexterity.ai/blog/meet-the-mech",
        publication_date="2025-03-17",
        event_date="2025-03-17",
        event_date_precision="DAY",
        date_precision="DAY",
        claim_nature="COMPANY_SELF_REPORT",
        snapshot_id="dexterity_mech_20250317",
        note="产品发布与供应对象为公司自述。",
    ))
    upsert_ev(d, ev(
        evidence_id="B_US_DEXTERITY_003",
        field="named_customers_or_partners / evidence_external_pilot / deployment_status_actual",
        claim="Dexterity 于 2025-10-22 称 Sagawa Express 批准在东京 X Frontier 中继中心对 Mech 进行现场操作验证，现场使用自 2025-05 开始；1000 台为随后几年计划，不是已交付。",
        quote="October 22, 2025 Mech Begins Truck Loading Operational Validation with Sagawa Express … marks the beginning of Mech’s onsite use at Sagawa starting May 2025. … they plan to deliver over 1,000 Mech robots to Japanese customers within the next few years",
        quote_locator="日期行、导语与计划段",
        source_title="Mech Begins Truck Loading Operational Validation with Sagawa Express",
        publisher="Dexterity, Inc.",
        source_nature="OFFICIAL_COMPANY",
        url="https://dexterity.ai/blog/mech-sagawa-express-x-relay",
        publication_date="2025-10-22",
        event_date="2025-05",
        event_date_precision="MONTH",
        date_precision="DAY",
        claim_nature="COMPANY_SELF_REPORT",
        snapshot_id="dexterity_sagawa",
        note="Sagawa 总经理引语刊于 Dexterity 博客，仍属公司渠道；1000 台为计划。",
    ))
    set_fact(d, "product_lines",
             value="Mech 工业双臂移动操作机器人（首发应用为卡车装载；物理 AI 在机载计算运行）",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_DEXTERITY_002"],
             decision_reason="以 2025-03-17 产品发布为准")
    set_fact(d, "delivery_form",
             value="向工业与企业客户提供 Mech 及任务软件应用（官方 2025-03-17；首发卡车装载应用）",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_DEXTERITY_002"],
             decision_reason="供应对象来自产品发布页")
    set_fact(d, "target_markets",
             value="仓储与工业现场的卡车装载、码垛与拣选",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_DEXTERITY_002"],
             decision_reason="任务范围来自 Mech 发布页")
    set_fact(d, "named_customers_or_partners",
             value="Sagawa Express、住友商事（Dexterity 博客刊载对方表述；操作为验证／试点）",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_DEXTERITY_003"],
             decision_reason="具名来自公司博客，未打开 Sagawa 本站")
    set_fact(d, "evidence_external_pilot",
             value="Sagawa X Frontier 中继中心对 Mech 卡车装载进行现场操作验证（公司博客 2025-10-22；现场使用自 2025-05 开始）",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_DEXTERITY_003"],
             decision_reason="操作验证／试点，不是规模交付")
    set_rel(d, "product_lines", "B_US_DEXTERITY_001", "CONTEXT_ONLY", "无日期首页")
    set_rel(d, "product_lines", "B_US_DEXTERITY_002", "SUPPORTS", "Mech 发布")
    set_rel(d, "delivery_form", "B_US_DEXTERITY_001", "CONTEXT_ONLY", "无日期首页")
    set_rel(d, "delivery_form", "B_US_DEXTERITY_002", "SUPPORTS", "向企业客户提供")
    set_rel(d, "target_markets", "B_US_DEXTERITY_001", "CONTEXT_ONLY", "无日期首页")
    set_rel(d, "target_markets", "B_US_DEXTERITY_002", "SUPPORTS", "卡车装载等任务")
    set_rel(d, "named_customers_or_partners", "B_US_DEXTERITY_003", "SUPPORTS", "Sagawa / 住友")
    set_rel(d, "evidence_external_pilot", "B_US_DEXTERITY_003", "SUPPORTS", "Sagawa 操作验证")
    save(authored("US_DEXTERITY"), d)

    # --- Nimble ------------------------------------------------------------
    n = load(authored("US_NIMBLE"))
    upsert_ev(n, ev(
        evidence_id="B_US_NIMBLE_002",
        field="product_lines / delivery_form / target_markets / deployment_status_actual",
        claim="Nimble 于 2024-09-26 宣布启用新泽西机器人履单中心，作为全国 3PL 网络节点，服务服装、鞋类、健康美容、消费电子等。",
        quote="Nimble Launches Robotic Fulfillment Center in New Jersey Date: Sep 26, 2024 … Nimble recently launched its new state-of-the-art warehouse in New Jersey to scale autonomous fulfillment operations. … This East Coast facility is servicing brands across apparel, footwear, health & beauty, consumer electronics, and more through robotic fulfillment",
        quote_locator="标题、日期行与正文",
        source_title="Nimble Launches Robotic Fulfillment Center in New Jersey",
        publisher="Nimble Robotics, Inc.",
        source_nature="OFFICIAL_COMPANY",
        url="https://nimble.ai/news/nimble-launches-robotic-fulfillment-center-in-new-jersey",
        publication_date="2024-09-26",
        event_date="2024-09-26",
        event_date_precision="DAY",
        date_precision="DAY",
        claim_nature="COMPANY_SELF_REPORT",
        snapshot_id="nimble_nj_20240926",
        note="节点启用为公司自述；FedEx 融资横幅不写入本条。",
    ))
    set_fact(n, "product_lines",
             value="AI 拣选包装机器人系统与机器人履单中心（2024-09-26 启用新泽西节点）",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_NIMBLE_002"],
             decision_reason="以带日期的节点启用公告为准")
    set_fact(n, "delivery_form",
             value="机器人第三方物流（robotic 3PL）：自有履单中心网络，2024-09-26 启用新泽西节点",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_NIMBLE_002"],
             decision_reason="3PL／履单中心来自节点公告")
    set_fact(n, "target_markets",
             value="电商履单与第三方物流（服装、鞋类、健康美容、消费电子等；新泽西节点）",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_NIMBLE_002"],
             decision_reason="品类来自节点公告")
    set_fact(n, "deployment_status_actual",
             value="新泽西机器人履单中心已启用，服务服装、鞋类、健康美容、消费电子等（公司 2024-09-26 公告）",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_NIMBLE_002"],
             decision_reason="设施启用为公司自述")
    set_rel(n, "product_lines", "B_US_NIMBLE_001", "CONTEXT_ONLY", "无日期首页")
    set_rel(n, "product_lines", "B_US_NIMBLE_002", "SUPPORTS", "新泽西节点公告")
    set_rel(n, "delivery_form", "B_US_NIMBLE_001", "CONTEXT_ONLY", "无日期首页")
    set_rel(n, "delivery_form", "B_US_NIMBLE_002", "SUPPORTS", "3PL 节点")
    set_rel(n, "target_markets", "B_US_NIMBLE_001", "CONTEXT_ONLY", "无日期首页")
    set_rel(n, "target_markets", "B_US_NIMBLE_002", "SUPPORTS", "品类清单")
    set_rel(n, "deployment_status_actual", "B_US_NIMBLE_001", "CONTEXT_ONLY", "无日期处理量自述")
    set_rel(n, "deployment_status_actual", "B_US_NIMBLE_002", "SUPPORTS", "节点启用")
    save(authored("US_NIMBLE"), n)

    # --- Spirit: official Moz1 text, still no publication date -------------
    sp = load(authored("CN_SPIRITAI"))
    upsert_ev(sp, ev(
        evidence_id="B_CN_SPIRITAI_002",
        field="product_lines",
        claim="千寻智能官方新闻称 2025 年 6 月发布全力控人形机器人 Moz1，并提及自研 VLA 模型 Spirit v1。该页未给出自身发布日期；新闻列表同样无日期。",
        quote="2025 年 6 月，千寻智能正式发布搭载自研 VLA 模型的全力控人形机器人 Moz1。 … 在具身模型层面，千寻智能自研的 VLA 模型 Spirit v1 持续迭代升级",
        quote_locator="「首次发布搭载具身大脑的全力控人形机器人」节",
        source_title="京东领投！千寻智能完成近6亿元PreA+轮融资，众多老股东超额加码",
        publisher="千寻智能（Spirit AI）",
        source_nature="OFFICIAL_COMPANY",
        url="https://www.spirit-ai.com/news/11",
        publication_date="",
        event_date="2025-06",
        event_date_precision="MONTH",
        date_precision="MONTH",
        claim_nature="COMPANY_SELF_REPORT",
        snapshot_id="spirit_news11_moz1",
        note="有事件月份、无发布日，不能进入观察日严格比较。news/10 为壳页。",
    ))
    set_fact(sp, "product_lines",
             value="全力控人形机器人 Moz1；自研 VLA 模型 Spirit v1（官方新闻述 2025 年 6 月发布；页面无发布日期）",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_CN_SPIRITAI_002"],
             decision_reason="改用官方 Moz1／Spirit v1 原文；因无发布日，时点仍不能进入严格比较")
    set_rel(sp, "product_lines", "B_CN_SPIRITAI_001", "CONTEXT_ONLY", "日文媒体无发布日")
    set_rel(sp, "product_lines", "B_CN_SPIRITAI_002", "SUPPORTS", "官方 Moz1 正文")
    save(authored("CN_SPIRITAI"), sp)

    # --- Boston Dynamics Stretch ------------------------------------------
    bd = load(authored("US_BOSTON_DYNAMICS"))
    upsert_ev(bd, ev(
        evidence_id="B_US_BOSTON_DYNAMICS_003",
        field="product_lines / target_markets / named_customers_or_partners / evidence_customer_delivery",
        claim="DHL Group 于 2025-05-13 宣布：Stretch 已用于集装箱卸货，DHL Supply Chain 2023 年在北美商业引入并扩展至英国与欧洲；同时签署再部署超过 1000 台的谅解备忘录，后者为计划／意向，不是已交付。",
        quote="05/13/2025, 10:00 AM CEST … Building on the proven success of Boston Dynamics' Stretch robot - designed for case handling and initially deployed by DHL to automate container unloading - the agreement paves the way for the global deployment of more than 1,000 additional units. … DHL Supply Chain, the Group's contract logistics division, has led the way, introducing Stretch commercially in North America in 2023 and more recently expanding deployments to the United Kingdom and across Europe.",
        quote_locator="日期行与正文第 1、3 段",
        source_title="DHL Group signs MOU with Boston Dynamics for additional 1,000-robot deployment",
        publisher="DHL Group（Internet Archive 保存的官方新闻稿）",
        source_nature="COUNTERPARTY_CONFIRMATION",
        url="https://group.dhl.com/en/media-relations/press-releases/2025/dhl-group-signs-mou-with-boston-dynamics-and-accelerates-cross-business-automation-strategy.html",
        publication_date="2025-05-13",
        event_date="2025-05-13",
        event_date_precision="DAY",
        date_precision="DAY",
        claim_nature="COUNTERPARTY_CONFIRMATION",
        snapshot_id="dhl_stretch_ia_20250513",
        note="直连 PDF/HTML 超时后改用 Internet Archive 2025-05-15 快照；1000 台为 MOU。",
    ))
    set_fact(bd, "product_lines",
             value="全电 Atlas 人形机器人（工业物料搬运，支持条码扫描与工作流集成、自主换电）；Spot 四足机器人；Orbit 机队与工作流管理平台；Stretch 箱体处理／集装箱卸货机器人（与 Atlas、Spot 分开）",
             value_status="SUPPORTED_EXTERNAL",
             evidence_ids=["B_US_BOSTON_DYNAMICS_001", "B_US_BOSTON_DYNAMICS_003"],
             decision_reason="Atlas/Spot 沿用已有有日期报道；Stretch 由 DHL 客户公告补入并分开记录")
    set_fact(bd, "target_markets",
             value="工业与仓储制造场景（物料搬运、企业级应用）；合同物流集装箱卸货与箱体处理（DHL Stretch）",
             value_status="SUPPORTED_EXTERNAL",
             evidence_ids=["B_US_BOSTON_DYNAMICS_001", "B_US_BOSTON_DYNAMICS_003"],
             decision_reason="卸货场景来自 DHL 公告")
    set_fact(bd, "named_customers_or_partners",
             value="现代汽车（Robotics Metaplant Application Centre）；Google；DHL Group／DHL Supply Chain（Stretch 卸货，客户公告）",
             value_status="MIXED_SEE_EVIDENCE",
             evidence_ids=["B_US_BOSTON_DYNAMICS_001", "B_US_BOSTON_DYNAMICS_003"],
             decision_reason="DHL 为客户确认；现代与 Google 仍为媒体口径")
    set_fact(bd, "evidence_loi_intent",
             value="DHL 与 Boston Dynamics 签署再部署超过 1000 台机器人的谅解备忘录（2025-05-13）",
             value_status="COUNTERPARTY_CONFIRMATION",
             evidence_ids=["B_US_BOSTON_DYNAMICS_003"],
             decision_reason="MOU 记为意向，不记已交付")
    set_rel(bd, "product_lines", "B_US_BOSTON_DYNAMICS_003", "SUPPORTS", "DHL Stretch 产品与既有部署")
    set_rel(bd, "target_markets", "B_US_BOSTON_DYNAMICS_003", "SUPPORTS", "卸货与合同物流")
    set_rel(bd, "named_customers_or_partners", "B_US_BOSTON_DYNAMICS_003", "SUPPORTS", "DHL 客户公告")
    set_rel(bd, "evidence_loi_intent", "B_US_BOSTON_DYNAMICS_003", "SUPPORTS", "1000 台 MOU")
    save(authored("US_BOSTON_DYNAMICS"), bd)

    # --- Figure ------------------------------------------------------------
    fig = load(authored("US_FIGURE"))
    upsert_ev(fig, ev(
        evidence_id="B_US_FIGURE_006",
        field="product_lines / delivery_form / target_markets",
        claim="Figure 于 2025-10-09 发布第三代人形机器人 Figure 03，为 Helix、家庭使用与规模制造设计。",
        quote="Introducing Figure 03 October 09, 2025 Today we’re introducing Figure 03, our 3rd generation humanoid robot. Figure 03 is designed for Helix, the home, and the world at scale.",
        quote_locator="标题、日期行与导语",
        source_title="Introducing Figure 03",
        publisher="Figure AI, Inc.",
        source_nature="OFFICIAL_COMPANY",
        url="https://www.figure.ai/news/introducing-figure-03",
        publication_date="2025-10-09",
        event_date="2025-10-09",
        event_date_precision="DAY",
        date_precision="DAY",
        claim_nature="COMPANY_SELF_REPORT",
        snapshot_id="figure_03_20251009",
        note="产品发布；产能目标（BotQ 年产 12000 台）为计划，不写入部署。",
    ))
    upsert_ev(fig, ev(
        evidence_id="B_US_FIGURE_005",
        field="named_customers_or_partners / deployment_status_actual / target_markets",
        claim="Figure 于 2026-06-30 称 Figure 03 已到达 BMW Group Plant Spartanburg Hall 52，从事物流排序；此前 Figure 02 于 2025 年在装配线部署。该页为公司公告，不是 BMW 本站。",
        quote="F.03 Arrives at BMW June 30, 2026 … Following the successful deployment of Figure 02 on the assembly line in 2025, our latest generation robot - Figure 03 - arrived in Hall 52, one of the assembly and logistics halls at BMW Group Plant Spartanburg.",
        quote_locator="标题、日期行与导语",
        source_title="F.03 Arrives at BMW",
        publisher="Figure AI, Inc.",
        source_nature="OFFICIAL_COMPANY",
        url="https://www.figure.ai/news/f-03-at-bmw",
        publication_date="2026-06-30",
        event_date="2026-06-30",
        event_date_precision="DAY",
        date_precision="DAY",
        claim_nature="COMPANY_SELF_REPORT",
        snapshot_id="figure_f03_bmw_20260630",
        note="客户现场为公司自述，未取得 BMW 一侧页面。",
    ))
    set_fact(fig, "product_lines",
             value="Figure 03 第三代人形机器人（官方 2025-10-09 发布；为 Helix VLA、家庭使用与规模制造设计）；Helix 自研视觉-语言-动作模型",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_FIGURE_006"],
             decision_reason="以带日期产品发布为准；无日期首页改为背景")
    set_fact(fig, "delivery_form",
             value="人形机器人整机与自研 Helix 模型一体提供（官方 2025-10-09 产品发布）",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_FIGURE_006"],
             decision_reason="一体提供来自产品发布页")
    set_fact(fig, "target_markets",
             value="家庭环境（官方 2025-10-09）；汽车制造物流现场（公司称 Figure 03 已到达 BMW Spartanburg）",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_FIGURE_006", "B_US_FIGURE_005"],
             decision_reason="家庭来自产品发布；工厂来自公司后续公告")
    set_fact(fig, "named_customers_or_partners",
             value="BMW Group（Plant Spartanburg Hall 52；公司 2026-06-30 公告，未取得 BMW 本站）",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_FIGURE_005"],
             decision_reason="具名客户为公司自述")
    set_fact(fig, "deployment_status_actual",
             value="公司称 Figure 03 已到达 BMW Spartanburg Hall 52 从事物流排序；Figure 02 此前在装配线部署",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_US_FIGURE_005"],
             decision_reason="现场到达为公司公告，不升级为客户确认")
    set_rel(fig, "product_lines", "B_US_FIGURE_001", "CONTEXT_ONLY", "无日期首页")
    set_rel(fig, "product_lines", "B_US_FIGURE_002", "CONTEXT_ONLY", "无发布日沿革页")
    set_rel(fig, "product_lines", "B_US_FIGURE_003", "CONTEXT_ONLY", "第三方库无发布日")
    set_rel(fig, "product_lines", "B_US_FIGURE_006", "SUPPORTS", "Figure 03 发布")
    set_rel(fig, "delivery_form", "B_US_FIGURE_001", "CONTEXT_ONLY", "无日期首页")
    set_rel(fig, "delivery_form", "B_US_FIGURE_006", "SUPPORTS", "整机与 Helix")
    set_rel(fig, "target_markets", "B_US_FIGURE_001", "CONTEXT_ONLY", "无日期首页")
    set_rel(fig, "target_markets", "B_US_FIGURE_002", "CONTEXT_ONLY", "无发布日沿革")
    set_rel(fig, "target_markets", "B_US_FIGURE_006", "SUPPORTS", "家庭用途")
    set_rel(fig, "target_markets", "B_US_FIGURE_005", "SUPPORTS", "BMW 工厂物流")
    set_rel(fig, "named_customers_or_partners", "B_US_FIGURE_003", "CONTEXT_ONLY", "第三方库")
    set_rel(fig, "named_customers_or_partners", "B_US_FIGURE_005", "SUPPORTS", "公司公告中的 BMW")
    set_rel(fig, "deployment_status_actual", "B_US_FIGURE_003", "CONTEXT_ONLY", "第三方库台数")
    set_rel(fig, "deployment_status_actual", "B_US_FIGURE_005", "SUPPORTS", "Spartanburg 到达")
    save(authored("US_FIGURE"), fig)

    # --- Agibot ------------------------------------------------------------
    ag = load(authored("CN_AGIBOT"))
    upsert_ev(ag, ev(
        evidence_id="B_CN_AGIBOT_003",
        field="product_lines",
        claim="智元官方新闻室 2026-09-08：人形机器人 AGIBOT A3、AGIBOT X2 在 IFA 2026 获奖；同篇称产品组合含人形、四足、灵巧手与商用清洁，并称 2026 年 6 月第 15000 台下线（公司自述）。",
        quote="发布时间：2026-09-08 18:46:21 … AGIBOT, a pioneer in the global general-purpose AI robotics industry, earned broad recognition at IFA 2026, with its humanoid robots AGIBOT A3 and AGIBOT X2 honored by the IFA Innovation Awards … Its portfolio spans humanoid robots, quadrupeds, dexterous systems, and commercial cleaning solutions. In June 2026, AGIBOT announced that its 15,000th robot had rolled off the production line.",
        quote_locator="发布时间行、导语与公司简介段",
        source_title="AGIBOT Humanoid Robots Recognized by IFA Innovation Awards and Global Tech Media at IFA 2026",
        publisher="AGIBOT Innovation (Shanghai) Technology Co., Ltd.",
        source_nature="OFFICIAL_COMPANY",
        url="https://www.agibot.com/article/231/detail/98.html",
        publication_date="2026-09-08",
        event_date="2026-09-08",
        event_date_precision="DAY",
        date_precision="DAY",
        claim_nature="COMPANY_SELF_REPORT",
        snapshot_id="agibot_news_20260908",
        note="展会奖项与下线台数为公司自述；下线不等于客户交付。",
    ))
    set_fact(ag, "product_lines",
             value="人形机器人 AGIBOT A3、AGIBOT X2（官方 2026-09-08）；产品组合另含四足、灵巧手与商用清洁方案（同篇）",
             value_status="COMPANY_SELF_REPORT",
             evidence_ids=["B_CN_AGIBOT_003"],
             decision_reason="以观察日前官方新闻室带日期条目为准")
    set_rel(ag, "product_lines", "B_CN_AGIBOT_001", "CONTEXT_ONLY", "无发布日媒体")
    set_rel(ag, "product_lines", "B_CN_AGIBOT_003", "SUPPORTS", "IFA 新闻室")
    save(authored("CN_AGIBOT"), ag)

    # --- Galbot product date from existing retail article ------------------
    gb = load(authored("CN_GALBOT"))
    set_fact(gb, "product_lines",
             value="人形机器人（香港自营零售店服务本体；2026-09-07 报道未列 ET1/G1/S1 型号）",
             value_status="MEDIA_STATEMENT",
             evidence_ids=["B_CN_GALBOT_001"],
             decision_reason="复用已有带日期零售报道；无日期官网型号改为背景")
    set_rel(gb, "product_lines", "B_CN_GALBOT_003", "CONTEXT_ONLY", "无日期官网型号")
    set_rel(gb, "product_lines", "B_CN_GALBOT_001", "SUPPORTS", "带日期零售店报道")
    save(authored("CN_GALBOT"), gb)

    # --- Deeprobotics product date from existing IPO article ---------------
    dr = load(authored("CN_DEEPROBOTICS"))
    set_fact(dr, "product_lines",
             value="四足机器人（证券时报 2026-05-19 转述招股／沙利文：2025 年四足行业应用收入全球第一）",
             value_status="MEDIA_STATEMENT",
             evidence_ids=["B_CN_DEEPROBOTICS_001"],
             decision_reason="复用已有带日期 IPO 报道中的四足产品类别；无日期官网型号清单改为背景")
    set_rel(dr, "product_lines", "B_CN_DEEPROBOTICS_003", "CONTEXT_ONLY", "无日期官网型号")
    set_rel(dr, "product_lines", "B_CN_DEEPROBOTICS_001", "SUPPORTS", "带日期四足类别")
    save(authored("CN_DEEPROBOTICS"), dr)

    # --- XSquare: reuse dated 0755 article for product_lines ---------------
    xs_path = os.path.join(WORK, "pilot_facts_CN_XSQUARE.json")
    xs = load(xs_path)
    block = xs["companies"][0] if "companies" in xs else xs
    for fact in block["facts"]:
        if fact["field"] == "product_lines":
            fact["value"] = "养老护理机器人「0755」（深圳市福利中心上岗，市政府网站 2026-07-16）"
            fact["value_status"] = "SUPPORTED_EXTERNAL"
            fact["evidence_ids"] = ["B_CN_XSQUARE_006"]
            fact["decision_reason"] = "复用已有带日期政府渠道报道；无日期官网产品目录改为背景"
    save(xs_path, xs)

    # --- grouping ----------------------------------------------------------
    rules_path = os.path.join(WORK, "grouping_rules_source.json")
    rules = load(rules_path)
    rules["rule_version"] = "stage-b-targeted-grouping-v1-2026-09-15"
    bind(rules, "delivery_form", "US_AGILITY",
         "Robots-as-a-Service（RaaS）：GXO 多年协议在 SPANX 设施部署 Digit 人形机器人与 Agility Arc 云平台",
         ["RAAS"])
    bind(rules, "product_lines", "US_AGILITY",
         "Digit 双足移动操作人形机器人（MMR）；Agility Arc 云端机队部署与管理平台",
         ["HUMANOID_ROBOTICS", "ROBOT_FLEET_SOFTWARE"])
    bind(rules, "target_markets", "US_AGILITY",
         "合同物流仓库现场（GXO SPANX 设施；从协作机器人取料箱放到传送带等重复作业）",
         ["WAREHOUSE_LOGISTICS", "CONTRACT_LOGISTICS"])
    bind(rules, "deployment_status_actual", "US_AGILITY",
         "GXO SPANX 设施已部署 Digit 与 Arc，协助从协作机器人取料箱放到传送带（客户所称商业部署；协议下继续探索更多用例，不记已部署台数）",
         ["DEPLOYED_AT_NAMED_CUSTOMER_SITE"])
    bind(rules, "product_lines", "US_PHYSICAL_INTELLIGENCE",
         "π0（pi-zero）跨本体通用机器人基础模型（官方 2024-10-31 发布；可控制多种机器人，经文本提示或微调执行任务）",
         ["ROBOT_FOUNDATION_MODELS", "VLA_ROBOT_POLICY"])
    bind(rules, "delivery_form", "US_PHYSICAL_INTELLIGENCE",
         "研究型基础模型发布；页面展示跨本体策略与任务演示，未陈述对外销售、许可合同或付费客户",
         ["RESEARCH_MODEL_RELEASE"])
    bind(rules, "target_markets", "US_PHYSICAL_INTELLIGENCE",
         "研究演示任务含洗衣、叠衣、做咖啡、装袋等操作；未给出商业行业清单",
         ["HOUSEHOLD_MANIPULATION_RESEARCH"])
    bind(rules, "product_lines", "US_FIELD_AI",
         "Field Foundation Models（FFMs）单一软件大脑／风险感知机器人基础模型；可驱动多种机器人形态",
         ["ROBOT_FOUNDATION_MODELS", "RISK_AWARE_AUTONOMY"])
    bind(rules, "delivery_form", "US_FIELD_AI",
         "软件大脑在客户工作流中边缘实时部署（公司自述）；未陈述独立确认的许可或销售合同形态",
         ["MODEL_DEPLOYMENT_SELF_REPORT"])
    bind(rules, "target_markets", "US_FIELD_AI",
         "建筑、能源、制造、城市配送与巡检（官方 2025-08-20 公告）",
         ["CONSTRUCTION", "INDUSTRIAL_ENERGY", "MANUFACTURING", "URBAN_DELIVERY_INSPECTION"])
    bind(rules, "deployment_status_actual", "US_FIELD_AI",
         "公司自述已在全球众多客户现场日常运行，并在数百个复杂工业环境测试与部署；部署量为自述，未取得客户确认",
         ["DEPLOYMENT_SELF_REPORTED"])
    bind(rules, "product_lines", "US_SKILD",
         "Skild Brain 跨形态机器人基础模型（四足、人形、桌面臂、移动操作等，2025-07-29）；S1 旗舰基础模型（官方 2026-08-18 发布，上下文学习）",
         ["ROBOT_FOUNDATION_MODELS"])
    bind(rules, "delivery_form", "US_SKILD",
         "研究型基础模型发布（Skild Brain / S1）；商业许可与付费交付仅见无日期博客自述，不纳入本条",
         ["RESEARCH_MODEL_RELEASE"])
    bind(rules, "target_markets", "US_SKILD",
         "跨形态机器人控制（四足、人形、桌面臂、移动操作）；未给出已签约商业行业清单",
         ["CROSS_EMBODIMENT_CONTROL"])
    bind(rules, "product_lines", "US_DEXTERITY",
         "Mech 工业双臂移动操作机器人（首发应用为卡车装载；物理 AI 在机载计算运行）",
         ["MOBILE_MANIPULATION_UNLOADING"])
    bind(rules, "delivery_form", "US_DEXTERITY",
         "向工业与企业客户提供 Mech 及任务软件应用（官方 2025-03-17；首发卡车装载应用）",
         ["HARDWARE_SALES", "TASK_SOFTWARE_APPS"])
    bind(rules, "target_markets", "US_DEXTERITY",
         "仓储与工业现场的卡车装载、码垛与拣选",
         ["LOGISTICS_TRUCK_LOADING"])
    bind(rules, "product_lines", "US_NIMBLE",
         "AI 拣选包装机器人系统与机器人履单中心（2024-09-26 启用新泽西节点）",
         ["PICK_AND_PACK_ROBOTICS", "FULFILLMENT_NETWORK"])
    bind(rules, "delivery_form", "US_NIMBLE",
         "机器人第三方物流（robotic 3PL）：自有履单中心网络，2024-09-26 启用新泽西节点",
         ["ROBOTIC_3PL_SERVICE"])
    bind(rules, "target_markets", "US_NIMBLE",
         "电商履单与第三方物流（服装、鞋类、健康美容、消费电子等；新泽西节点）",
         ["ECOMMERCE_FULFILLMENT", "THIRD_PARTY_LOGISTICS"])
    bind(rules, "deployment_status_actual", "US_NIMBLE",
         "新泽西机器人履单中心已启用，服务服装、鞋类、健康美容、消费电子等（公司 2024-09-26 公告）",
         ["FULFILLMENT_NODE_IN_SERVICE"])
    bind(rules, "product_lines", "CN_SPIRITAI",
         "全力控人形机器人 Moz1；自研 VLA 模型 Spirit v1（官方新闻述 2025 年 6 月发布；页面无发布日期）",
         ["HUMANOID_ROBOTICS", "ROBOT_FOUNDATION_MODELS"])
    bind(rules, "product_lines", "US_BOSTON_DYNAMICS",
         "全电 Atlas 人形机器人（工业物料搬运，支持条码扫描与工作流集成、自主换电）；Spot 四足机器人；Orbit 机队与工作流管理平台；Stretch 箱体处理／集装箱卸货机器人（与 Atlas、Spot 分开）",
         ["HUMANOID_ROBOTICS", "QUADRUPED_ROBOTICS", "ROBOT_FLEET_SOFTWARE", "WAREHOUSE_UNLOADING_ROBOT"])
    bind(rules, "target_markets", "US_BOSTON_DYNAMICS",
         "工业与仓储制造场景（物料搬运、企业级应用）；合同物流集装箱卸货与箱体处理（DHL Stretch）",
         ["INDUSTRIAL_WAREHOUSE", "LOGISTICS_TRUCK_UNLOADING"])
    bind(rules, "product_lines", "US_FIGURE",
         "Figure 03 第三代人形机器人（官方 2025-10-09 发布；为 Helix VLA、家庭使用与规模制造设计）；Helix 自研视觉-语言-动作模型",
         ["HUMANOID_ROBOTICS", "ROBOT_FOUNDATION_MODELS"])
    bind(rules, "delivery_form", "US_FIGURE",
         "人形机器人整机与自研 Helix 模型一体提供（官方 2025-10-09 产品发布）",
         ["HARDWARE_SALES", "MODEL_INTEGRATED_SYSTEM"])
    bind(rules, "target_markets", "US_FIGURE",
         "家庭环境（官方 2025-10-09）；汽车制造物流现场（公司称 Figure 03 已到达 BMW Spartanburg）",
         ["HOME_ENVIRONMENT", "MANUFACTURING_AUTOMATION"])
    bind(rules, "deployment_status_actual", "US_FIGURE",
         "公司称 Figure 03 已到达 BMW Spartanburg Hall 52 从事物流排序；Figure 02 此前在装配线部署",
         ["DEPLOYED_AT_NAMED_FACTORY_SELF_REPORT"])
    bind(rules, "product_lines", "CN_AGIBOT",
         "人形机器人 AGIBOT A3、AGIBOT X2（官方 2026-09-08）；产品组合另含四足、灵巧手与商用清洁方案（同篇）",
         ["HUMANOID_ROBOTICS", "QUADRUPED_ROBOTICS", "DEXTEROUS_HANDS"])
    bind(rules, "product_lines", "CN_GALBOT",
         "人形机器人（香港自营零售店服务本体；2026-09-07 报道未列 ET1/G1/S1 型号）",
         ["HUMANOID_ROBOTICS"])
    bind(rules, "product_lines", "CN_DEEPROBOTICS",
         "四足机器人（证券时报 2026-05-19 转述招股／沙利文：2025 年四足行业应用收入全球第一）",
         ["QUADRUPED_ROBOTICS"])
    bind(rules, "product_lines", "CN_XSQUARE",
         "养老护理机器人「0755」（深圳市福利中心上岗，市政府网站 2026-07-16）",
         ["ELDERCARE_SERVICE_ROBOT"])
    save(rules_path, rules)

    # search / page-review trail
    searches = [
        ("US_AGILITY", "delivery_form product_lines target_markets deployment_status_actual",
         "GXO Agility Robotics RaaS Digit SPANX 2024", "cursor-web-search+official-fetch",
         "GXO HTML 2024-06-27；PDF 超时后改网页"),
        ("US_PHYSICAL_INTELLIGENCE", "product_lines delivery_form target_markets deployment_status_actual evidence_demo",
         "Physical Intelligence pi0 official blog 2024-10-31", "cursor-web-search+official-fetch",
         "π0 发布页；未见付费部署"),
        ("US_FIELD_AI", "product_lines delivery_form target_markets deployment_status_actual",
         "FieldAI FFMs construction energy manufacturing 2025-08-20", "cursor-web-search+official-fetch",
         "官方融资／业务公告；部署量为自述"),
        ("US_SKILD", "product_lines delivery_form target_markets",
         "Skild Brain S1 foundation model blog 2025 2026", "cursor-web-search+official-fetch",
         "Brain 2025-07-29；S1 2026-08-18"),
        ("CN_SPIRITAI", "product_lines",
         "千寻智能 Moz1 Spirit v1 官方新闻", "cursor-web-search+official-fetch",
         "news/11 有正文无发布日；news/10 壳页；新闻列表无日期"),
        ("US_DEXTERITY", "product_lines delivery_form target_markets named_customers_or_partners evidence_external_pilot",
         "Dexterity Mech Sagawa truck loading 2025", "cursor-web-search+official-fetch",
         "Mech 发布与 Sagawa 验证"),
        ("US_NIMBLE", "product_lines delivery_form target_markets deployment_status_actual",
         "Nimble robotic fulfillment center New Jersey 2024-09-26", "cursor-web-search+official-fetch",
         "新泽西节点公告"),
        ("US_BOSTON_DYNAMICS", "product_lines target_markets Stretch DHL",
         "DHL Boston Dynamics Stretch MOU 2025-05-13", "cursor-web-search+archive-fetch",
         "直连超时；Internet Archive 保存官方稿"),
        ("US_AMAZON_FTR", "research_subject hiring_board_channel delivery_form",
         "Amazon FAR vs FTR team boundary amazon.jobs", "page-review-existing-snapshots",
         "FTR 团队页仍 404；业务组保持退出严格比较"),
        ("US_FIGURE", "product_lines delivery_form target_markets deployment_status_actual",
         "Figure 03 introducing October 2025 BMW Spartanburg", "cursor-web-search+official-fetch",
         "产品发布与 BMW 到达均为公司页"),
        ("CN_AGIBOT", "product_lines",
         "AGIBOT A3 X2 IFA 2026-09-08 newsroom", "cursor-web-search+official-fetch",
         "观察日前官方新闻室"),
        ("CN_NOETIX", "product_lines",
         "松延动力 新闻中心 产品发布日期", "official-fetch",
         "news 页正文为空，产品日期仍不足"),
        ("CN_XSQUARE", "product_lines",
         "review existing dated 0755 government article for product claim", "page-review",
         "复用 B_CN_XSQUARE_006"),
        ("CN_GALBOT", "product_lines",
         "review existing dated Hong Kong retail article for product claim", "page-review",
         "复用 B_CN_GALBOT_001"),
        ("CN_DEEPROBOTICS", "product_lines",
         "review existing dated IPO article for quadruped product claim", "page-review",
         "复用 B_CN_DEEPROBOTICS_001"),
        ("CN_FOURIER", "product_lines target_markets",
         "map split child facts onto parent grouping dimensions", "code-fix-review",
         "s05 并入子事实，无需新证据"),
    ]
    for cid, question, query, tool, outcome in searches:
        log("SEARCH", company_id=cid, question=question, query=query, tool=tool,
            result=outcome, urls_checked=[])
    for cid, field, result in [
        ("US_PHYSICAL_INTELLIGENCE", "deployment_status_actual", "π0 page is research demo, no paying customer"),
        ("US_AMAZON_FTR", "delivery_form", "still undated research/prototype; FTR 404 unresolved"),
        ("US_AMAZON_FTR", "research_subject", "FAR job pages remain the team boundary"),
        ("US_AMAZON_FTR", "hiring_board_channel", "amazon.jobs still the hiring channel"),
        ("CN_SPIRITAI", "product_lines", "official Moz1 text has event month, no publication date"),
        ("CN_NOETIX", "product_lines", "news page empty; home still undated"),
        ("US_BOSTON_DYNAMICS", "product_lines", "Stretch separated via DHL archive page"),
        ("CN_FOURIER", "product_lines", "child facts mapped in s05"),
    ]:
        log("PAGE_REVIEW", company_id=cid, field=field, question=field,
            result=result, urls_checked=[])
    print(json.dumps({"ok": True, "search_log": SEARCH_LOG}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit("Historical targeted importer disabled in integrated package; rebuild with s02/s03 from sealed authored inputs.")
    raise SystemExit(main())
