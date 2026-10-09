"""Repair pass / diagnostic 3: attach per-value group bindings to the locked rule
document.

The submitted package turned free-text fact values into group labels through a
per-company table living in code. Here every group label is declared beside the
exact fact value it belongs to, inside the locked rule document, so the mapping is
reviewable and any change to it changes the locked input digest.

A value that is not declared is reported as UNCLASSIFIED_VALUE and leaves the
comparison rather than being silently labelled.

Run once; the result is a locked input for every later step.
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import RUN, WORK  # noqa: E402

RULE_FILE = os.path.join(WORK, "grouping_rules_source.json")

BINDINGS: dict[str, dict[str, dict[str, list[str]]]] = {
    "delivery_form": {
        "CN_XSQUARE": {
            "硬件本体、核心零部件与数采设备全栈自研；具身基础模型与开源训练代码；开发者平台；系统集成与服务未见公司外证据":
                ["HARDWARE_SALES", "FOUNDATION_MODEL_AND_TOOLING"],
        },
        "US_AMAZON_FTR": {
            "研究与原型硬件开发为主；无对外销售产品的官方证据": ["RESEARCH_AND_PROTOTYPE_ONLY"],
        },
        "CN_FOURIER": {
            "硬件设备销售与交付（含整院康复设备包）、临床部署与培训、远程康复系统、研究与共建合作":
                ["HARDWARE_SALES", "CLINICAL_DEPLOYMENT", "SYSTEM_INTEGRATION", "RESEARCH_COLLABORATION"],
        },
    },
    "target_markets": {
        "CN_XSQUARE": {
            "工业制造、物流、养老、家居（公司自述「已逐步进入」）":
                ["INDUSTRIAL_MANUFACTURING", "LOGISTICS", "ELDERCARE", "HOUSEHOLD_SERVICE"],
        },
        "US_AMAZON_FTR": {
            "亚马逊自有全球运营（仓储／履约）为目标方向（官方自述方向性表述）":
                ["INTERNAL_OPERATIONS_TARGET"],
        },
        "CN_FOURIER": {
            "马来西亚：国家级康复中心（PERKESO 汝来康复医院）整院康复设备交付":
                ["HEALTHCARE_REHABILITATION"],
            "新加坡：与国立医疗集团 NHG Health 的康复与机器人技术合作，涉及陈笃生医院部署与评估":
                ["HEALTHCARE_REHABILITATION"],
            "中国国内：康复科室与康养、居家场景（落地家数为申报方与受访者口径）":
                ["HEALTHCARE_REHABILITATION", "ELDERCARE"],
        },
    },
    "product_lines": {
        "CN_XSQUARE": {
            "量子1号 / 量子1号 Pro、量子2号（具身轮式仿人形）、五指灵巧手（单手20自由度）、无本体数采系统 XR Zero-G0、桌面主从套装、高性能六轴机械臂；模型侧 WALL-A、WALL-OSS(0.5)、WALL-B、WALL-WM、X-Tokenizer":
                ["HUMANOID_ROBOTICS", "DEXTEROUS_HANDS", "DATA_COLLECTION_SYSTEMS",
                 "FOUNDATION_MODEL_AND_TOOLING", "MANIPULATOR_ARMS"],
        },
        "US_AMAZON_FTR": {
            "前沿机器人基础模型与端到端学习系统、多模态感知与自适应操作；高自由度机器人原型硬件（执行器、传感器、机电集成）；公开代码侧含仿真、人形数据采集、行为克隆、机器人控制策略与世界模型方向":
                ["ROBOT_FOUNDATION_MODELS", "PROTOTYPE_ROBOT_HARDWARE", "OPEN_SOURCE_ROBOTICS_CODE"],
        },
        "CN_FOURIER": {
            "康复机器人产品线：ExoMotus M4 下肢外骨骼、ArmMotus EMU 三维上肢康复机器人、下肢康复机器人、伽利略生物力学分析与训练系统（约 40 余款康复产品为受访者口径）":
                ["REHAB_ROBOTICS", "EXOSKELETON", "BIOMECHANICS_SYSTEMS"],
            "人形机器人产品线：GRx 系列（GR-2、GR-3）；2026-06 报道中在 PERKESO 康复中心引导认知训练的一台人形机器人亦属傅利叶产品（未指明型号）":
                ["HUMANOID_ROBOTICS"],
            "陪伴与管家方向：媒体标题级线索提及 2026 年发布的管家系统与陪伴新品，本轮未逐项核实到产品页":
                ["COMPANION_SYSTEMS_MEDIA_LEAD_ONLY"],
        },
    },
    "deployment_status_actual": {
        "CN_XSQUARE": {
            "已取得位于具名机构（深圳市福利服务指导中心老人颐养院）的实地上岗部署证据；物流为真实场景运行数月（客户未具名）；两条均不足以支持大规模运营":
                ["DEPLOYED_AT_NAMED_INSTITUTION", "RUNNING_IN_REAL_SCENARIO_CUSTOMER_UNDISCLOSED"],
        },
        "US_AMAZON_FTR": {"": ["NO_DEPLOYMENT_VALUE_ESTABLISHED"]},
        "CN_FOURIER": {
            "马来西亚 PERKESO 康复中心：整套康复设备自 2025-10 起试运营并于 2026-06-16 随中心开业正式投用；新加坡：陈笃生医院康复技术部署与评估（对方公告）；全国康复港落地家数与服务人次仅为成果发布页文字口径":
                ["DEPLOYED_AT_NAMED_INSTITUTION", "DEPLOYED_UNDER_COUNTERPARTY_AGREEMENT"],
        },
    },
    "evidence_customer_delivery": {
        "CN_XSQUARE": {
            "有：深圳市福利服务指导中心以养老护理员岗位实际使用（政府网站渠道）；58 到家联合家政服务口径近千户（公司口径）":
                ["DELIVERY_TO_NAMED_INSTITUTION", "DELIVERY_REPORTED_COMPANY_CLAIM"],
        },
        "US_AMAZON_FTR": {"": ["NO_CUSTOMER_DELIVERY_VALUE_ESTABLISHED"]},
        "CN_FOURIER": {
            "有：PERKESO 康复中心整院康复设备交付（总价上千万元，媒体口径）；陈笃生医院康复技术部署（对方公告）":
                ["DELIVERY_TO_NAMED_INSTITUTION", "COUNTERPARTY_CONFIRMED_DEPLOYMENT"],
        },
    },
    "evidence_paid": {
        "CN_XSQUARE": {"": ["NOT_YET_SEARCHED"]},
        "US_AMAZON_FTR": {"": ["NOT_APPLICABLE_INTERNAL_TEAM"]},
        "CN_FOURIER": {
            "PERKESO 项目总价上千万元（媒体口径，未取得合同或付款凭证）；NHG 合作未披露交易金额":
                ["ORDER_AMOUNT_MEDIA_ONLY"],
        },
    },
    "own_listing_status": {
        "CN_XSQUARE": {"": ["UNKNOWN_NOT_COMPARABLE:SEARCHED_NOT_FOUND"]},
        "US_AMAZON_FTR": {"不适用（非独立法人；研究主体为母公司内团队）": ["NOT_APPLICABLE_TEAM"]},
        "CN_FOURIER": {
            "未上市；有记录称已完成股份制改造并列入已启动上市进程名单，尚未递表":
                ["NOT_LISTED_LISTING_PROCESS_REPORTED"],
        },
    },
    "parent_relationship": {
        "CN_XSQUARE": {"": ["NO_PARENT_DISCLOSED_UNKNOWN"]},
        "US_AMAZON_FTR": {
            "母公司 Amazon；FAR 岗位在官方职位详情中挂在 Amazon Robotics 组织标签下，行政归属与团队边界并存":
                ["PARENT_COMPANY_AMAZON"],
        },
        "CN_FOURIER": {"": ["NO_PARENT_DISCLOSED_UNKNOWN"]},
    },
}

PILOT_IDS = ("CN_XSQUARE", "US_AMAZON_FTR", "CN_FOURIER")


def main() -> int:
    rules = json.load(open(RULE_FILE, encoding="utf-8"))
    declared_values = {
        dim: {cid: sorted(v for v in BINDINGS.get(dim, {}).get(cid, {}))
              for cid in PILOT_IDS}
        for dim in BINDINGS
    }
    for dim in rules["dimensions"]:
        name = dim["dimension"]
        dim["group_bindings"] = {cid: BINDINGS.get(name, {}).get(cid, {}) for cid in PILOT_IDS}
        dim["group_labels"] = {}
    rules["binding_note"] = (
        "每个取值到组标签的对应关系在此逐条声明；程序不做关键词归类。"
        "未声明的取值标为 UNCLASSIFIED_VALUE 并退出比较。"
        "空字符串键表示该事实没有确立值（例如查后未找到）；此时只会生成 UNKNOWN_NOT_COMPARABLE 行，"
        "不会生成确定否定组。")
    with open(RULE_FILE, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(rules, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(json.dumps({d: sum(len(v) for v in declared_values[d].values()) for d in declared_values},
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
