"""Stage B repair / extension step: group bindings for the fifth research batch.

Appends value-to-group declarations for US_BOSTON_DYNAMICS, CN_AGIBOT and CN_ASTRIBOT to
the locked rule document.
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import WORK  # noqa: E402

RULE_FILE = os.path.join(WORK, "grouping_rules_source.json")

BATCH5 = {
    "delivery_form": {
        "US_BOSTON_DYNAMICS": {
            "工业机器人整机交付与部署，配 Orbit 平台做机队管理与系统集成；Atlas 由公司波士顿总部生产":
                ["HARDWARE_SALES", "FLEET_PLATFORM_INTEGRATION"],
        },
        "CN_AGIBOT": {
            "人形机器人整机对外交付（报道口径为向客户交付台数）":
                ["HARDWARE_SALES"],
        },
        "CN_ASTRIBOT": {
            "机器人本体销售（T 系列起售价 8.99 万元）＋模型与 OS 一体化；2025 年底开启千台级交付，2026 年推进 T1 量产与万台级产能建设":
                ["HARDWARE_SALES", "MODEL_INTEGRATED_SYSTEM"],
        },
    },
    "target_markets": {
        "US_BOSTON_DYNAMICS": {
            "工业与仓储制造场景（物料搬运、企业级应用）":
                ["INDUSTRIAL_MATERIAL_HANDLING", "MANUFACTURING_AUTOMATION"],
        },
        "CN_AGIBOT": {
            "国内大型汽车制造厂与 3C 电子装配线（报道口径的主力部署场景）":
                ["AUTOMOTIVE_MANUFACTURING", "ELECTRONICS_ASSEMBLY"],
        },
        "CN_ASTRIBOT": {
            "商业场景（报道提及机器人 MART 等零售标杆产品）与通用智能应用；投资方提及灵巧拟人操作、交互安全等场景优势":
                ["RETAIL_SERVICE", "GENERAL_PURPOSE_MANIPULATION"],
        },
    },
    "product_lines": {
        "US_BOSTON_DYNAMICS": {
            "全电 Atlas 人形机器人（工业物料搬运，支持条码扫描与工作流集成、自主换电）；Spot 四足机器人；Orbit 机队与工作流管理平台（可接入 MES、WMS）":
                ["HUMANOID_ROBOTICS", "QUADRUPED_ROBOTICS", "ROBOT_FLEET_SOFTWARE"],
        },
        "CN_AGIBOT": {
            "人形机器人整机（报道统称「类人形机器人」；具体型号本轮证据未逐一列明）":
                ["HUMANOID_ROBOTICS"],
        },
        "CN_ASTRIBOT": {
            "本体：绳驱 AI 机器人（旗舰 S 系列；2026-05-27 发布 T 系列，起售价 8.99 万元）；模型侧：基座模型 Lumo 与快慢系统模型框架 DuoCore；另有面向 AI 设计的具身 OS 层":
                ["HUMANOID_ROBOTICS", "ROBOT_FOUNDATION_MODELS", "ROBOT_OS"],
        },
    },
    "deployment_status_actual": {
        "US_BOSTON_DYNAMICS": {
            "Atlas 已在公司波士顿总部开始生产，2026 年部署额度已全部被预订，机队将交付现代 RMAC 与 Google":
                ["PRODUCTION_STARTED_DEPLOYMENTS_COMMITTED"],
        },
        "CN_AGIBOT": {
            "上半年向客户交付 8400 台（第三方统计算口径）；6 月累计出货突破 1.5 万台；主力产品部署于国内汽车制造厂与 3C 电子装配线":
                ["MASS_DELIVERY_REPORTED", "DEPLOYED_IN_MANUFACTURING_SCENES"],
        },
        "CN_ASTRIBOT": {
            "2025 年底开启千台级交付；报道提及机器人 MART 等零售标杆产品的商业落地表现":
                ["VOLUME_DELIVERY_STARTED", "RETAIL_PILOT_REPORTED"],
        },
    },
    "evidence_customer_delivery": {
        "US_BOSTON_DYNAMICS": {
            "机队计划交付至现代 RMAC 与 Google":
                ["DELIVERY_PLAN_NAMED_RECIPIENTS"],
        },
        "CN_AGIBOT": {
            "上半年向客户交付 8400 台人形机器人（第三方统计口径）":
                ["DELIVERY_COUNT_THIRD_PARTY_STAT"],
        },
        "CN_ASTRIBOT": {
            "2025 年底开启千台级交付（报道口径，未列具名客户）":
                ["DELIVERY_COUNT_REPORTED_NO_NAMED_SITE"],
        },
    },
    "evidence_paid": {
        "US_BOSTON_DYNAMICS": {"": ["NO_PAYMENT_EVIDENCE_RETRIEVED"]},
        "CN_AGIBOT": {
            "2026 年第一季度营业收入 10 亿元人民币（报道转述公司业绩，追平 2025 年全年）":
                ["REVENUE_REPORTED_VIA_MEDIA"],
        },
        "CN_ASTRIBOT": {"": ["NO_PAYMENT_EVIDENCE_RETRIEVED"]},
    },
    "own_listing_status": {
        "US_BOSTON_DYNAMICS": {"": ["NOT_LISTED_NO_FILING_RETRIEVED"]},
        "CN_AGIBOT": {
            "未上市；已于 2026-07-24 启动香港 IPO 程序，目标估值 400 亿至 500 亿港元（约 51 亿至 64 亿美元），联席保荐人为中信证券、中金公司、摩根士丹利":
                ["NOT_LISTED_IPO_PROCESS_STARTED"],
        },
        "CN_ASTRIBOT": {"": ["NOT_LISTED_NO_FILING_RETRIEVED"]},
    },
    "parent_relationship": {
        "US_BOSTON_DYNAMICS": {
            "现代汽车集团（Hyundai Motor Group）为控股方；Atlas 首批机队交付至现代 Robotics Metaplant Application Centre（RMAC）":
                ["PARENT_HYUNDAI_MOTOR_GROUP"],
        },
        "CN_AGIBOT": {"": ["NO_PARENT_DISCLOSED_UNKNOWN"]},
        "CN_ASTRIBOT": {"": ["NO_PARENT_DISCLOSED_UNKNOWN"]},
    },
}


def main() -> int:
    rules = json.load(open(RULE_FILE, encoding="utf-8"))
    added: dict[str, int] = {}
    for dim in rules["dimensions"]:
        bindings = dim.setdefault("group_bindings", {})
        for cid, mapping in BATCH5.get(dim["dimension"], {}).items():
            bindings.setdefault(cid, {}).update(mapping)
            added[cid] = added.get(cid, 0) + 1
    with open(RULE_FILE, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(rules, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(json.dumps({"bindings_added_per_company": added}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
