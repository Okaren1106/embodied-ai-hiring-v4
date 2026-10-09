"""Stage B repair / extension step: attach group bindings for a researched company.

Group labels are declared beside the exact fact value they belong to, inside the locked
rule document, so a company cannot enter a comparison group through a code default. This
script appends the declarations for one batch of newly researched companies; existing
declarations are left untouched.
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import WORK  # noqa: E402

RULE_FILE = os.path.join(WORK, "grouping_rules_source.json")

BATCH3 = {
    "delivery_form": {
        "US_APPTRONIK": {
            "人形机器人硬件与部署方案提供；投资方公告称新资金用于加速 Apollo 生产并扩大全球商业部署与试点网络":
                ["HARDWARE_SALES", "DEPLOYMENT_AND_INTEGRATION"],
        },
        "US_FIGURE": {
            "人形机器人整机与自研 AI 模型一体提供；第三方库记录称 Helix 为端到端 VLA 并在工厂场景运行":
                ["HARDWARE_SALES", "MODEL_INTEGRATED_SYSTEM"],
        },
        "CN_GALBOT": {
            "机器人本体与具身大模型一体提供；商用形态为自主运营的零售门店（机器人独立完成接单、取货与支付）":
                ["HARDWARE_SALES", "MODEL_INTEGRATED_SYSTEM", "SELF_OPERATED_RETAIL"],
        },
    },
    "target_markets": {
        "US_APPTRONIK": {
            "初始面向制造、仓储与物流等关键行业；公告称后续计划扩展至零售、医疗，最终进入家庭":
                ["MANUFACTURING_AUTOMATION", "WAREHOUSE_LOGISTICS", "RETAIL_PLANNED", "HEALTHCARE_PLANNED", "HOME_PLANNED"],
        },
        "US_FIGURE": {
            "家庭场景（官方当前主线）与制造业／工厂场景（官方沿革与第三方库记录）":
                ["HOME_ENVIRONMENT", "MANUFACTURING_AUTOMATION"],
        },
        "CN_GALBOT": {
            "零售（香港门店已营业，计划扩展至迪士尼乐园、海洋公园等人流密集与旅游区）；报道另称双足机器人未来拟拓展至招揽顾客、图书馆与博物馆讲解及工业应用":
                ["RETAIL_SELF_OPERATED", "TOURISM_LOCATIONS_PLANNED", "CULTURAL_VENUES_PLANNED", "INDUSTRIAL_PLANNED"],
        },
    },
    "product_lines": {
        "US_APPTRONIK": {
            "Apollo 通用人形机器人（模块化设计，提供双足与轮式两种移动选项，具备移动、灵巧操作与技能学习能力）；配套机队级部署与软件工具":
                ["HUMANOID_ROBOTICS", "ROBOT_FLEET_SOFTWARE"],
        },
        "US_FIGURE": {
            "Figure 03（面向日常的通用人形机器人，官方称已针对居住环境改进观感与触感）；Figure 02（上一代，官方沿革称曾在劳动力场景测试）；F.01（首代，2023-05 迈出第一步）；Helix 视觉-语言-动作模型（官方称用于应对不断变化的家庭环境）":
                ["HUMANOID_ROBOTICS", "ROBOT_FOUNDATION_MODELS"],
        },
        "CN_GALBOT": {
            "机器人本体型号 ET1、G1、S1；AstraBrain 具身大模型族（通用大脑 AstraBrain-WAM 世界动作模型、通用小脑 AstraBrain-WBC、面向灵巧手的世界模型 AstraBrain-Dex）；官方资讯另载原生智能体机器人「银河星仔」预订":
                ["HUMANOID_ROBOTICS", "ROBOT_FOUNDATION_MODELS", "DEXTEROUS_HANDS"],
        },
    },
    "deployment_status_actual": {
        "US_APPTRONIK": {
            "公告与官网均称存在商业部署与试点项目网络，但本轮未取得具名部署现场或运行数据":
                ["DEPLOYMENT_NETWORK_CLAIMED_NO_NAMED_SITE"],
        },
        "US_FIGURE": {
            "第三方库记录称 2026-01 已交付 350 台以上 Figure 03，且 BMW 侧部署在 2025-11 扩展至 100 台以上；公司官网未公布部署台数":
                ["DELIVERY_COUNT_THIRD_PARTY_ONLY"],
        },
        "CN_GALBOT": {
            "已在香港启德、红磡、湾仔开设自有品牌人形机器人零售店（报道称香港首家由机器人全自主服务），机器人自主完成接单、取货与支付":
                ["SELF_OPERATED_RETAIL_STORES_OPEN"],
        },
    },
    "evidence_customer_delivery": {
        "US_APPTRONIK": {"": ["NO_CUSTOMER_DELIVERY_RETRIEVED"]},
        "US_FIGURE": {"": ["NO_CUSTOMER_DELIVERY_RETRIEVED"]},
        "CN_GALBOT": {"": ["SELF_OPERATED_NOT_CUSTOMER_DELIVERY"]},
    },
    "evidence_paid": {
        "US_APPTRONIK": {"": ["NO_PAYMENT_EVIDENCE_RETRIEVED"]},
        "US_FIGURE": {"": ["NO_PAYMENT_EVIDENCE_RETRIEVED"]},
        "CN_GALBOT": {
            "门店机器人自主完成接单与支付全流程（媒体报道的运营方式）":
                ["TRANSACTION_FLOW_REPORTED_NO_REVENUE_DISCLOSED"],
        },
    },
    "own_listing_status": {
        "US_APPTRONIK": {
            "未上市；截至观察日未取得公开上市或申报上市的直接披露":
                ["NOT_LISTED_NO_FILING_RETRIEVED"],
        },
        "US_FIGURE": {
            "未上市；截至观察日未取得公开上市或申报上市的直接披露":
                ["NOT_LISTED_NO_FILING_RETRIEVED"],
        },
        "CN_GALBOT": {
            "未上市；报道中创始人称公司在具身智能行业持续融资，未披露上市安排":
                ["NOT_LISTED_FUNDING_ONGOING_REPORTED"],
        },
    },
    "parent_relationship": {
        "US_APPTRONIK": {"": ["NO_PARENT_DISCLOSED_UNKNOWN"]},
        "US_FIGURE": {"": ["NO_PARENT_DISCLOSED_UNKNOWN"]},
        "CN_GALBOT": {"": ["NO_PARENT_DISCLOSED_UNKNOWN"]},
    },
}


def main() -> int:
    rules = json.load(open(RULE_FILE, encoding="utf-8"))
    added = {}
    for dim in rules["dimensions"]:
        name = dim["dimension"]
        bindings = dim.setdefault("group_bindings", {})
        for cid, mapping in BATCH3.get(name, {}).items():
            bindings.setdefault(cid, {}).update(mapping)
            added.setdefault(cid, 0)
            added[cid] += 1
    with open(RULE_FILE, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(rules, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(json.dumps({"bindings_added_per_company": added,
                      "companies": sorted(added)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
