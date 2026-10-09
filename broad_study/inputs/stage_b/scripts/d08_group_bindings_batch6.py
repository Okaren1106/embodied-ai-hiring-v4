"""Stage B repair / extension step: group bindings for the sixth research batch."""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import WORK  # noqa: E402

RULE_FILE = os.path.join(WORK, "grouping_rules_source.json")

BATCH6 = {
    "delivery_form": {
        "CN_GALAXEA": {
            "具身基础模型、数据体系、机器人本体与开发平台并行的业务形态（公司口径）":
                ["FOUNDATION_MODEL_AND_TOOLING", "HARDWARE_SALES"],
        },
        "CN_LIMX": {
            "人形机器人整机销售与交付；资金用于完善全球制造与交付能力并推进规模化部署":
                ["HARDWARE_SALES", "FLEET_PLATFORM_INTEGRATION"],
        },
    },
    "target_markets": {
        "CN_GALAXEA": {"": ["NO_MARKET_VALUE_ESTABLISHED"]},
        "CN_LIMX": {
            "科研教育、商业服务、全地形巡检、工业应用、建筑等场景；重点市场布局含中东、欧洲与亚洲其他国家":
                ["RESEARCH_EDUCATION", "COMMERCIAL_SERVICE", "ALL_TERRAIN_INSPECTION", "INDUSTRIAL", "CONSTRUCTION"],
        },
    },
    "product_lines": {
        "CN_GALAXEA": {
            "具身基础模型族：G0 VLA（2025-08 开源）、G0 Plus（2026-01 开源）、面向衣物折叠的垂类模型与轻量化小模型 G0 Tiny（2026-02）；机器人本体与开发平台业务；后续拟推出 G0.5 与世界模型 Fast-WAM":
                ["ROBOT_FOUNDATION_MODELS", "HUMANOID_ROBOTICS"],
        },
        "CN_LIMX": {
            "通用人形机器人整机产品线；AI 基础设施与具身智能体 OS（System 1）；FluxVLA Engine 企业级开源平台（覆盖数据处理、仿真训练、真机迭代到硬件部署）":
                ["HUMANOID_ROBOTICS", "ROBOT_FOUNDATION_MODELS", "ROBOT_OS"],
        },
    },
    "deployment_status_actual": {
        "CN_GALAXEA": {"": ["NO_DEPLOYMENT_VALUE_ESTABLISHED"]},
        "CN_LIMX": {
            "各款机器人产品上线以来共获数千台订单，其中过半来自海外（公司口径）；本轮未取得实际部署现场记录":
                ["ORDER_BOOK_REPORTED_NO_SITE_RECORD"],
        },
    },
    "evidence_customer_delivery": {
        "CN_GALAXEA": {"": ["NO_CUSTOMER_DELIVERY_RETRIEVED"]},
        "CN_LIMX": {"": ["NO_COMPLETED_HANDOVER_RETRIEVED"]},
    },
    "evidence_paid": {
        "CN_GALAXEA": {"": ["NO_PAYMENT_EVIDENCE_RETRIEVED"]},
        "CN_LIMX": {"": ["NO_PAYMENT_EVIDENCE_RETRIEVED"]},
    },
    "own_listing_status": {
        "CN_GALAXEA": {"": ["NOT_LISTED_NO_FILING_RETRIEVED"]},
        "CN_LIMX": {
            "未上市；已完成股改（2026-03）并据媒体报道于 2026 年初稍早开启 IPO 进程，Pre-IPO 轮融资近 2 亿美元已完成":
                ["NOT_LISTED_IPO_PROCESS_STARTED"],
        },
    },
    "parent_relationship": {
        "CN_GALAXEA": {"": ["NO_PARENT_DISCLOSED_UNKNOWN"]},
        "CN_LIMX": {"": ["NO_PARENT_DISCLOSED_UNKNOWN"]},
    },
}


def main() -> int:
    rules = json.load(open(RULE_FILE, encoding="utf-8"))
    added: dict[str, int] = {}
    for dim in rules["dimensions"]:
        bindings = dim.setdefault("group_bindings", {})
        for cid, mapping in BATCH6.get(dim["dimension"], {}).items():
            bindings.setdefault(cid, {}).update(mapping)
            added[cid] = added.get(cid, 0) + 1
    with open(RULE_FILE, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(rules, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(json.dumps({"bindings_added_per_company": added}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
