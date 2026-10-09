"""Stage B repair / extension step: group bindings for the fourth research batch.

Appends value-to-group declarations for CN_UNITREE, US_DILIGENT and US_PICKLE to the
locked rule document. Values that are not declared leave the comparison instead of
being silently labelled.
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import WORK  # noqa: E402

RULE_FILE = os.path.join(WORK, "grouping_rules_source.json")

BATCH4 = {
    "delivery_form": {
        "CN_UNITREE": {
            "机器人整机销售；上市募资投向含智能机器人大模型、机器人本体性能升级、新型智能机器人产品开发与制造基地建设":
                ["HARDWARE_SALES", "FOUNDATION_MODEL_AND_TOOLING"],
        },
        "US_DILIGENT": {
            "医院场景服务机器人交付与部署；被收购后 Moxi 成为收购方新医疗业务线的首批部署机器人":
                ["HARDWARE_SALES", "HEALTHCARE_DEPLOYMENT"],
        },
        "US_PICKLE": {
            "面向仓库与分拨中心的卸货机器人系统交付与部署；B 轮资金用于扩大部署与产品化":
                ["HARDWARE_SALES", "WAREHOUSE_DEPLOYMENT"],
        },
    },
    "target_markets": {
        "CN_UNITREE": {"": ["NO_MARKET_VALUE_ESTABLISHED"]},
        "US_DILIGENT": {
            "医院与医疗场景（护士站、药房等院内物流与物资运送）":
                ["HEALTHCARE_HOSPITAL_LOGISTICS"],
        },
        "US_PICKLE": {
            "物流与供应链场景的卡车／集装箱卸货（分拨中心、仓库月台）":
                ["LOGISTICS_TRUCK_UNLOADING"],
        },
    },
    "product_lines": {
        "CN_UNITREE": {
            "四足机器人与人形机器人（招股与上市报道语境为通用机器人整机）；继承资料另有 G1 人形机器人等型号记录":
                ["QUADRUPED_ROBOTICS", "HUMANOID_ROBOTICS"],
        },
        "US_DILIGENT": {
            "Moxi 医院服务机器人（由 Nvidia AI 芯片驱动，协助护士与药房人员运送实验室样本等物资）；收购前数月另发布新机器人设计（Nvidia GTC 大会）":
                ["SERVICE_ROBOTICS_HEALTHCARE"],
        },
        "US_PICKLE": {
            "Pickle Unload System（配备吸盘式抓取的机械臂＋移动底盘机器人，可驶入集装箱抓取重达 50 磅的箱体并放上传送带；单个机器人约两小时可卸完一辆典型卡车）":
                ["MOBILE_MANIPULATION_UNLOADING"],
        },
    },
    "deployment_status_actual": {
        "CN_UNITREE": {"": ["NO_DEPLOYMENT_VALUE_ESTABLISHED"]},
        "US_DILIGENT": {
            "Moxi 已在美国 30 家以上医院部署运行":
                ["DEPLOYED_IN_NAMED_SECTOR_COUNT_REPORTED"],
        },
        "US_PICKLE": {
            "Pickle Unload Systems 自 2023 年夏季起已在多个客户的分拨中心以量产状态运行；累计卸货超过 1000 万磅（公司口径）":
                ["PRODUCTION_RUNNING_AT_CUSTOMER_SITES", "CUMULATIVE_THROUGHPUT_REPORTED"],
        },
    },
    "evidence_customer_delivery": {
        "CN_UNITREE": {"": ["NO_CUSTOMER_DELIVERY_RETRIEVED"]},
        "US_DILIGENT": {
            "已在 30 家以上医院部署（报道口径，未列具名医院）":
                ["DEPLOYMENT_COUNT_REPORTED_NO_NAMED_SITE"],
        },
        "US_PICKLE": {"": ["NO_COMPLETED_HANDOVER_RETRIEVED"]},
    },
    "evidence_paid": {
        "CN_UNITREE": {"": ["NO_PAYMENT_EVIDENCE_RETRIEVED"]},
        "US_DILIGENT": {"": ["NO_PAYMENT_EVIDENCE_RETRIEVED"]},
        "US_PICKLE": {"": ["NO_PAYMENT_EVIDENCE_RETRIEVED"]},
    },
    "own_listing_status": {
        "CN_UNITREE": {
            "已于 2026-08-19 正式登陆科创板（688836.SH），发行价 150.80 元/股，为 A 股「人形机器人第一股」":
                ["LISTED"],
        },
        "US_DILIGENT": {
            "不适用（非独立上市主体；被 Serve Robotics 收购后为其子公司）":
                ["NOT_APPLICABLE_SUBSIDIARY"],
        },
        "US_PICKLE": {
            "未上市；截至观察日未取得公开上市或申报上市的直接披露":
                ["NOT_LISTED_NO_FILING_RETRIEVED"],
        },
    },
    "parent_relationship": {
        "CN_UNITREE": {"": ["NO_PARENT_DISCLOSED_UNKNOWN"]},
        "US_DILIGENT": {
            "2026-01-20 宣布被 Serve Robotics 收购（对价 2900 万美元普通股＋530 万美元业绩里程碑），交易预计 2026 年一季度完成；Diligent 由联合创始人兼 CEO Andrea Thomaz 继续领导":
                ["ACQUIRED_BY_SERVE_ROBOTICS"],
        },
        "US_PICKLE": {"": ["NO_PARENT_DISCLOSED_UNKNOWN"]},
    },
}


def main() -> int:
    rules = json.load(open(RULE_FILE, encoding="utf-8"))
    added: dict[str, int] = {}
    for dim in rules["dimensions"]:
        name = dim["dimension"]
        bindings = dim.setdefault("group_bindings", {})
        for cid, mapping in BATCH4.get(name, {}).items():
            bindings.setdefault(cid, {}).update(mapping)
            added[cid] = added.get(cid, 0) + 1
    with open(RULE_FILE, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(rules, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(json.dumps({"bindings_added_per_company": added}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
