"""Stage B repair / extension step: group bindings for the seventh research batch."""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import WORK  # noqa: E402

RULE_FILE = os.path.join(WORK, "grouping_rules_source.json")

B7 = {
    "delivery_form": {
        "CN_NOETIX": {
            "自适应机器人本体、控制器、夹爪与平台类产品的提供；公司自述从自适应机器人厂商进化为通用智能基础设施提供商":
                ["HARDWARE_SALES", "MODEL_INTEGRATED_SYSTEM"],
        },
        "CN_PAXINI": {
            "触觉感知芯片与传感器的量产供应＋灵巧手与人形机器人；公司称把半导体晶圆工艺引入触觉芯片生产以实现芯片级规模生产":
                ["COMPONENT_SUPPLY", "HARDWARE_SALES"],
        },
        "CN_SPIRITAI": {
            "基座模型开源＋人形机器人整机在客户产线投入实际作业":
                ["FOUNDATION_MODEL_AND_TOOLING", "HARDWARE_SALES"],
        },
        "US_SKILD": {
            "基础模型与机器人平台交付；与硬件及制造伙伴联合部署（NVIDIA、富士康）":
                ["MODEL_LICENSING", "FLEET_PLATFORM_INTEGRATION"],
        },
    },
    "target_markets": {
        "CN_NOETIX": {"工业与通用智能应用（报道提及工业零件抓取等场景）": ["INDUSTRIAL"]},
        "CN_PAXINI": {
            "具身智能产业的基础配置（触觉感知）与人形机器人整机应用；报道提及与比亚迪相关语境（标题），但正文未给出具体场景":
                ["COMPONENT_FOR_EMBODIED_AI", "HUMANOID_APPLICATIONS"],
        },
        "CN_SPIRITAI": {
            "动力电池制造产线（宁德时代中州基地电池 Pack 生产线）；通用机器人作业场景":
                ["BATTERY_MANUFACTURING", "GENERAL_ROBOT_WORK"],
        },
        "US_SKILD": {
            "搬运与配送、场地巡检、安保、食品制备、商用厨房、精密装配等（公司口径的场景清单）":
                ["LOGISTICS_MOVING", "SITE_INSPECTION", "SECURITY", "FOOD_PREPARATION", "PRECISION_ASSEMBLY"],
        },
    },
    "product_lines": {
        "CN_NOETIX": {
            "Enlight 初昕系列全感知自适应机器人（新一代轻量化本体，强化复杂环境感知与操作）；Orion 天枢新一代架构控制器；一体化仿人智能平台 MICO；星擎（Grav）Enhanced 壁虎材料夹爪（刚柔双模式，可抓取工业零件与易碎物体）":
                ["ADAPTIVE_ROBOTICS", "ROBOT_CONTROLLERS", "ROBOT_GRIPPERS", "ROBOT_PLATFORM_SOFTWARE"],
        },
        "CN_PAXINI": {
            "GEN4 FUSE 真 6D 触觉感知芯片（公司称全球首款实现量产的原生真 6D 触觉感知阵列芯片）；PX6AX GEN4 产品矩阵；灵巧手与人形机器人（全栈布局的一部分）；具身数据生态（采集设备、数据工厂集群与跨平台复现系统）":
                ["TACTILE_SENSING_CHIPS", "DEXTEROUS_HANDS", "HUMANOID_ROBOTICS", "EMBODIED_DATA_SYSTEMS"],
        },
        "CN_SPIRITAI": {
            "开源基座模型 Spirit v1.5（报道称在中国首次于性能上超过 Physical Intelligence 的 Pi0.5，具零样本泛化能力）；人形机器人 Moz Robot":
                ["ROBOT_FOUNDATION_MODELS", "HUMANOID_ROBOTICS"],
        },
        "US_SKILD": {
            "Skild Brain 机器人基础模型（可通过观看人类视频学习）；安全／巡检机器人平台；双臂机械手上的装配应用（Skild Brain 部署于 NVIDIA Blackwell 系统高精度装配）":
                ["ROBOT_FOUNDATION_MODELS", "SECURITY_INSPECTION_PLATFORM", "MANIPULATION_ASSEMBLY"],
        },
    },
    "deployment_status_actual": {
        "CN_NOETIX": {"": ["NO_DEPLOYMENT_VALUE_ESTABLISHED"]},
        "CN_PAXINI": {"": ["NO_DEPLOYMENT_VALUE_ESTABLISHED"]},
        "CN_SPIRITAI": {
            "2025 年末宁德时代中州基地启动人形机器人规模化导入的电池 Pack 产线，Moz Robot 在该产线实际作业（报道口径）":
                ["DEPLOYED_AT_NAMED_CUSTOMER_PRODUCTION_LINE"],
        },
        "US_SKILD": {
            "首次商业部署后十个月突破 1 亿美元 ARR，扩展至 60 家以上付费客户（公司口径）":
                ["PAYING_CUSTOMERS_REPORTED", "ARR_REPORTED_COMPANY_CLAIM"],
        },
    },
    "evidence_customer_delivery": {
        "CN_NOETIX": {"": ["NO_CUSTOMER_DELIVERY_RETRIEVED"]},
        "CN_PAXINI": {"": ["NO_CUSTOMER_DELIVERY_RETRIEVED"]},
        "CN_SPIRITAI": {
            "人形机器人已导入宁德时代产线从事实际作业（报道口径，未给交付台数）":
                ["DEPLOYED_INTO_CUSTOMER_LINE_NO_UNIT_COUNT"],
        },
        "US_SKILD": {
            "已向 60 家以上付费客户交付（场景含搬运、配送、巡检、安保、食品制备等，公司口径）":
                ["PAYING_CUSTOMER_COUNT_REPORTED"],
        },
    },
    "evidence_paid": {
        "CN_NOETIX": {"": ["NO_PAYMENT_EVIDENCE_RETRIEVED"]},
        "CN_PAXINI": {"": ["NO_PAYMENT_EVIDENCE_RETRIEVED"]},
        "CN_SPIRITAI": {"": ["NO_PAYMENT_EVIDENCE_RETRIEVED"]},
        "US_SKILD": {
            "首次商业部署后十个月达 1 亿美元 ARR，60 家以上为付费客户（公司口径）":
                ["ARR_REPORTED_COMPANY_CLAIM"],
        },
    },
    "own_listing_status": {
        "CN_NOETIX": {"": ["NOT_LISTED_NO_FILING_RETRIEVED"]},
        "CN_PAXINI": {
            "未上市；已完成股份制改革（报道口径，时间在报道前一个月内）":
                ["NOT_LISTED_SHARE_REFORM_COMPLETED"],
        },
        "CN_SPIRITAI": {"": ["NOT_LISTED_NO_FILING_RETRIEVED"]},
        "US_SKILD": {"": ["NOT_LISTED_NO_FILING_RETRIEVED"]},
    },
    "parent_relationship": {
        "CN_NOETIX": {"": ["NO_PARENT_DISCLOSED_UNKNOWN"]},
        "CN_PAXINI": {"": ["NO_PARENT_DISCLOSED_UNKNOWN"]},
        "CN_SPIRITAI": {"": ["NO_PARENT_DISCLOSED_UNKNOWN"]},
        "US_SKILD": {"": ["NO_PARENT_DISCLOSED_UNKNOWN"]},
    },
}


def main() -> int:
    rules = json.load(open(RULE_FILE, encoding="utf-8"))
    added: dict[str, int] = {}
    for dim in rules["dimensions"]:
        bindings = dim.setdefault("group_bindings", {})
        for cid, mapping in B7.get(dim["dimension"], {}).items():
            bindings.setdefault(cid, {}).update(mapping)
            added[cid] = added.get(cid, 0) + 1
    with open(RULE_FILE, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(rules, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(json.dumps({"bindings_added_per_company": added}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
