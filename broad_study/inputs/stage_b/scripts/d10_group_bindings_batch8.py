"""Stage B repair / extension step: group bindings for the eighth (final) research batch."""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import WORK  # noqa: E402

RULE_FILE = os.path.join(WORK, "grouping_rules_source.json")

B8 = {
    "delivery_form": {
        "US_FIELD_AI": {
            "基础模型与解决方案提供，配合产业伙伴在客户场景部署（与 Caterpillar、NVIDIA 系列合作条目）":
                ["MODEL_LICENSING", "SOLUTION_INTEGRATION"],
        },
        "US_PHYSICAL_INTELLIGENCE": {
            "基础模型与算法能力输出；官网称合作伙伴已在真实场景应用（未列具名合作方与交付形式）":
                ["MODEL_LICENSING"],
        },
        "US_DEXTERITY": {
            "机器人系统与平台部署（官网提供「开始部署」入口，并称只与准备好部署的公司合作）":
                ["HARDWARE_SALES", "FLEET_PLATFORM_INTEGRATION"],
        },
        "US_NIMBLE": {
            "机器人第三方物流服务（3PL）：以自有履单中心网络向 DTC 品牌提供履单与配送服务":
                ["ROBOTIC_3PL_SERVICE"],
        },
    },
    "target_markets": {
        "US_FIELD_AI": {
            "建筑、城市运营、工业与能源、联邦（政府）等（官网解决方案分类）":
                ["CONSTRUCTION", "URBAN_OPERATIONS", "INDUSTRIAL_ENERGY", "FEDERAL_GOVERNMENT"],
        },
        "US_PHYSICAL_INTELLIGENCE": {
            "通用机器人应用（官网称通用物理智能模型将带来机器人应用的爆发；未给具体行业清单）":
                ["GENERAL_PURPOSE_ROBOTICS"],
        },
        "US_DEXTERITY": {
            "物流与供应链（官网称客户为全球最大物流公司；未列具名客户）":
                ["LOGISTICS_SUPPLY_CHAIN"],
        },
        "US_NIMBLE": {
            "电商履单与第三方物流（服装、健康与美容、鞋类、电子、快消品等品类；服务对象含财富 500 强企业与此类高成长品牌）":
                ["ECOMMERCE_FULFILLMENT", "THIRD_PARTY_LOGISTICS"],
        },
    },
    "product_lines": {
        "US_FIELD_AI": {
            "Field Foundation Models（FFMs）机器人基础模型族，围绕 Belief World Model（BWM）构建，定位为风险感知的机器人 AI；解决方案按建筑、城市运营、工业与能源、联邦（政府）分类":
                ["ROBOT_FOUNDATION_MODELS", "RISK_AWARE_AUTONOMY"],
        },
        "US_PHYSICAL_INTELLIGENCE": {
            "π0.7 可引导机器人基础模型（官网称泛化能力阶跃式提升）；RL Token 机制（从 VLA 模型提取，支持快速在线强化学习）；多尺度具身记忆（MEM，支持超过十分钟的复杂任务）":
                ["ROBOT_FOUNDATION_MODELS", "VLA_ROBOT_POLICY"],
        },
        "US_DEXTERITY": {
            "面向物流的机械臂机器人（官网称机器人全轮班运行）；物理 AI 世界模型（以超过 1 亿次生产自主行动经验训练）；Dexterity 平台（AI 智能体团队为机器人提供类人灵巧性）":
                ["LOGISTICS_MANIPULATION_ROBOTS", "WORLD_MODEL", "ROBOT_FLEET_SOFTWARE"],
        },
        "US_NIMBLE": {
            "AI 驱动的拣选与包装机器人系统；机器人履单中心网络（robotic fulfillment centers）；自主履单服务（fully autonomous fulfillment，与 FedEx 一起扩展）":
                ["PICK_AND_PACK_ROBOTICS", "FULFILLMENT_NETWORK", "AUTONOMOUS_FULFILLMENT_SERVICE"],
        },
    },
    "deployment_status_actual": {
        "US_FIELD_AI": {
            "官网自述在三大洲有部署；具体客户现场的部署规模与运行数据本轮未取得":
                ["DEPLOYMENT_ACROSS_THREE_CONTINENTS_CLAIMED"],
        },
        "US_PHYSICAL_INTELLIGENCE": {"": ["NO_DEPLOYMENT_VALUE_ESTABLISHED"]},
        "US_DEXTERITY": {
            "公司自述机器人在全球最大物流公司全轮班运行、做出数百万次自主决策且零安全事故；世界模型以超过 1 亿次生产自主行动经验训练":
                ["FULL_SHIFT_OPERATION_CLAIMED", "AUTONOMOUS_ACTIONS_VOLUME_REPORTED"],
        },
        "US_NIMBLE": {
            "公司自述 AI 机器人已拣选、包装并处理数百万件商品，覆盖多个品类；通过全国机器人履单中心网络提供服务（未给站点数与产能）":
                ["ITEMS_HANDLED_VOLUME_REPORTED", "FULFILLMENT_NETWORK_IN_SERVICE"],
        },
    },
    "evidence_customer_delivery": {
        "US_FIELD_AI": {
            "官网列有 Caterpillar、Big-D Construction 等客户案例条目（公司自述，未给交付数量）":
                ["CUSTOMER_CASES_ON_OWN_SITE"],
        },
        "US_PHYSICAL_INTELLIGENCE": {"": ["NO_CUSTOMER_DELIVERY_RETRIEVED"]},
        "US_DEXTERITY": {
            "已在物流客户现场部署并全轮班运行（公司口径，未具名、未给交付数量）":
                ["DEPLOYED_AT_UNNAMED_LARGE_LOGISTICS_COMPANY"],
        },
        "US_NIMBLE": {
            "已为财富 500 强企业与高成长品牌处理数百万件商品（公司口径，未具名除 FedEx 外的客户）":
                ["CUSTOMER_TYPES_REPORTED_NO_NAMES"],
        },
    },
    "evidence_paid": {
        "US_FIELD_AI": {"": ["NO_PAYMENT_EVIDENCE_RETRIEVED"]},
        "US_PHYSICAL_INTELLIGENCE": {"": ["NO_PAYMENT_EVIDENCE_RETRIEVED"]},
        "US_DEXTERITY": {"": ["NO_PAYMENT_EVIDENCE_RETRIEVED"]},
        "US_NIMBLE": {
            "以机器人 3PL 服务收费（官网称「行业低单位成本」；未给收入或定价结构）":
                ["SERVICE_FEE_MODEL_NO_AMOUNT"],
        },
    },
    "own_listing_status": {
        "US_FIELD_AI": {"": ["NOT_LISTED_NO_FILING_RETRIEVED"]},
        "US_PHYSICAL_INTELLIGENCE": {"": ["NOT_LISTED_NO_FILING_RETRIEVED"]},
        "US_DEXTERITY": {"": ["NOT_LISTED_NO_FILING_RETRIEVED"]},
        "US_NIMBLE": {"": ["NOT_LISTED_NO_FILING_RETRIEVED"]},
    },
    "parent_relationship": {
        "US_FIELD_AI": {"": ["NO_PARENT_DISCLOSED_UNKNOWN"]},
        "US_PHYSICAL_INTELLIGENCE": {"": ["NO_PARENT_DISCLOSED_UNKNOWN"]},
        "US_DEXTERITY": {"": ["NO_PARENT_DISCLOSED_UNKNOWN"]},
        "US_NIMBLE": {"": ["NO_PARENT_DISCLOSED_UNKNOWN"]},
    },
}


def main() -> int:
    rules = json.load(open(RULE_FILE, encoding="utf-8"))
    added: dict[str, int] = {}
    for dim in rules["dimensions"]:
        bindings = dim.setdefault("group_bindings", {})
        for cid, mapping in B8.get(dim["dimension"], {}).items():
            bindings.setdefault(cid, {}).update(mapping)
            added[cid] = added.get(cid, 0) + 1
    with open(RULE_FILE, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(rules, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(json.dumps({"bindings_added_per_company": added}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
