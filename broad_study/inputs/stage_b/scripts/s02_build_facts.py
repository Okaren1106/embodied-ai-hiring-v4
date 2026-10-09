"""Stage B repair / step 2: rebuild the authored fact layer from the corrected research.

This step applies every content fix the independent acceptance found, and it is the
only writer of work/pilot_facts_v2_*.json. It never edits the submitted package.

Fixes applied per company, keyed to the acceptance report:

  P1-2 time      : every fact declares subject / scope / event-or-period and which
                   evidence directly qualifies its date. Parent-company and other
                   background material is marked CONTEXT_ONLY and can never supply
                   the date of a fact it does not support.
  P1-3 unknown   : SEARCHED_NOT_FOUND / NOT_YET_SEARCHED / ACCESS_BLOCKED /
                   INHERITED_UNVERIFIED stay unknown; no definite negative value.
  P1-5 evidence  : FAR 004 moves to job 10426076 (the page its text is actually on);
                   FAR 007 becomes parent context with no support relation;
                   self-report-only claims drop out of SUPPORTED_EXTERNAL;
                   hiring duties are recorded as hiring scope, not as proof that the
                   company already performs internal testing.
  P2-6 capital   : capital semantics are declared per event with structured amount,
                   currency, unit and amount scope; valuation kept apart from amount.
  P2-7 progress  : NOT_YET_SEARCHED facts carry checked_in_stage_b=NO.
"""
from __future__ import annotations

import glob
import json
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import RUN, WORK, write_json  # noqa: E402

OLD = {
    "CN_XSQUARE": os.path.join(WORK, "pilot_facts_CN_XSQUARE.json"),
    "US_AMAZON_FTR": os.path.join(WORK, "pilot_facts_US_AMAZON_FTR.json"),
    "CN_FOURIER": os.path.join(WORK, "pilot_facts_CN_FOURIER.json"),
}

EVIDENCE_FIX = {
    "B_US_AMAZON_FTR_004": {
        "url": "https://www.amazon.jobs/en/jobs/10426076/technical-lab-manager-robotics-r-d-frontier-ai-robotics",
        "source_title": "Technical Lab Manager - Robotics R&D, Frontier AI & Robotics (Job ID 10426076)",
        "snapshot_id": "job_detail_10426076",
        "note": ("本行摘录经逐字复核位于 Job 10426076 页面（Key job responsibilities 与 A day in the life 两段）；"
                 "原送审版本把本行绑到 10424277，属页面错绑，已按原文更正。原 10424277 页面快照仍保留在 "
                 "evidence_snapshots 内，该页只用于确认同一 FAR 团队第二个岗位的存在。"),
        "relation_to_inherited": "CONFIRMS_AND_EXTENDS",
    },
    "B_US_AMAZON_FTR_007": {
        "claim_nature": "PARENT_CONTEXT",
        "note": ("母公司机器人与履约业务背景，仅作背景展示；不参与 FAR 任何断言的日期判定，也不支持 FAR 的目标市场、"
                 "部署或时间结论。750,000 台为母公司口径，未写入 FAR 部署值。"),
    },
    "B_CN_XSQUARE_009": {
        "note": ("四轮融资并全部交割、投后估值突破 200 亿元人民币；轮次金额未单独披露，故金额保留未知而不是补造分轮数字。"
                 "同一事件在公司官网时间线另有自述，两条来源连接到一个资本事件，不重复计为两个交易。"),
    },
    "B_CN_XSQUARE_006": {
        "url": "https://fgw.sz.gov.cn/ztzl/qtztzl/szscjmyjjfzzhfwpt/mqfc/myqyfzdt/content/post_12909775.html",
        "note": ("深圳市发展和改革委员会网站转载的报社稿件（请求路径 /ztztl/ 会 301 到 /ztzl/，此处记录落地 URL）；"
                 "非政府采购或验收文件；正文称「近日」上岗、正推进场景适配，因此记录为已上岗部署而非规模化运营。"),
    },
}


def r(fact, evidence, role, why):
    return {"fact": fact, "evidence": evidence, "role": role, "review_note": why}


_CUR = {"cid": None}
_REL_OUT: list[dict] = []


def rr(fact, evidence, role, why):
    """Declare a relation for the company currently being built."""
    _REL_OUT.append({"cid": _CUR["cid"], "fact": fact, "evidence": evidence,
                     "role": role, "review_note": why})
    return None


def initialize_relations() -> list[dict]:
    for cid, block in RELATION_BLOCKS:
        _CUR["cid"] = cid
        block()
    return list(_REL_OUT)


_INLINE_RELATIONS: dict[str, list[dict]] = {}


def rels_for(cid: str) -> list[dict]:
    """Relations for one company: an extension source declares them inline, the pilot
    envelope declares them in the table above."""
    if cid in _INLINE_RELATIONS:
        return _INLINE_RELATIONS[cid]
    return [x for x in _REL_OUT if x["cid"] == cid]


RELATION_BLOCKS: list[tuple] = [

    ("CN_XSQUARE", lambda: [
    rr("legal_entity_name", "B_CN_XSQUARE_001", "SUPPORTS", "官网自述主体名称与注册地；自述不升级为独立确认"),
    rr("research_subject", "B_CN_XSQUARE_001", "SUPPORTS", "官方站点自述研究主体"),
    rr("research_subject", "B_CN_XSQUARE_003", "SUPPORTS", "官网产品页确定研究对象业务范围"),
    rr("research_subject", "B_CN_XSQUARE_004", "SUPPORTS", "官网招聘入口确定招聘主体"),
    rr("hq_or_team_location", "B_CN_XSQUARE_001", "SUPPORTS", "官网主体自述含深圳注册主体"),
    rr("hiring_board_channel", "B_CN_XSQUARE_004", "SUPPORTS", "官网加入我们页声明社招与校招两个入口"),
    rr("hiring_board_channel", "B_CN_XSQUARE_005", "SUPPORTS", "飞书板可达性确认渠道归属"),
    rr("founded_or_team_start_date", "B_CN_XSQUARE_002", "SUPPORTS", "官网时间线自述 2023 年 12 月在深圳启动运营"),
    rr("product_lines", "B_CN_XSQUARE_006", "SUPPORTS", "政府网站渠道：养老护理机器人 0755 上岗"),
    rr("product_lines", "B_CN_XSQUARE_003", "CONTEXT_ONLY", "无日期官网产品目录，仅作背景"),
    rr("product_lines", "B_CN_XSQUARE_001", "CONTEXT_ONLY", "无日期官网时间线模型，仅作背景"),
    rr("delivery_form", "B_CN_XSQUARE_003", "SUPPORTS", "官网产品清单确定硬件与部件交付形态"),
    rr("delivery_form", "B_CN_XSQUARE_007", "SUPPORTS", "真实场景运行的公司口径"),
    rr("target_markets", "B_CN_XSQUARE_010", "SUPPORTS", "官网时间线自述场景与业务方向"),
    rr("target_markets", "B_CN_XSQUARE_007", "SUPPORTS", "物流场景合作的公司口径"),
    rr("target_markets", "B_CN_XSQUARE_006", "SUPPORTS", "养老机构场景的政府网站渠道记录"),
    rr("named_customers_or_partners", "B_CN_XSQUARE_006", "SUPPORTS", "具名机构：深圳市福利服务指导中心"),
    rr("named_customers_or_partners", "B_CN_XSQUARE_008", "SUPPORTS", "具名合作方：58 到家（未获该方确认）"),
    rr("named_customers_or_partners", "B_CN_XSQUARE_007", "CONTEXT_ONLY",
      "原文明确客户未具名（仅称头部物流企业），不构成具名客户证据，仅作背景"),
    rr("named_customers_or_partners", "B_CN_XSQUARE_009", "CONTEXT_ONLY",
      "投资方与产业股东名单不是客户或业务伙伴命题，仅作背景"),
    rr("deployment_status_actual", "B_CN_XSQUARE_006", "SUPPORTS", "具名机构实地上岗"),
    rr("deployment_status_actual", "B_CN_XSQUARE_007", "SUPPORTS", "真实场景运行数月的公司口径"),
    rr("evidence_demo", "B_CN_XSQUARE_007", "SUPPORTS", "全自主分拣直播与物流场景演示"),
    rr("evidence_demo", "B_CN_XSQUARE_010", "CONTEXT_ONLY",
      "官网时间线记录历史展出节点；无发布日期，不参与本次演示断言的时间判定，仅作背景"),
    rr("evidence_internal_test", "B_CN_XSQUARE_007", "SUPPORTS", "同次报道记述的自主分拣测试"),
    rr("evidence_internal_test", "B_CN_XSQUARE_003", "CONTEXT_ONLY",
      "官网产品与数采工厂自述，不是测试活动记录；仅作背景，不参与本断言的成立与时间判定"),
    rr("evidence_external_pilot", "B_CN_XSQUARE_007", "SUPPORTS", "与头部物流企业合作的场景试点（公司口径）"),
    rr("evidence_external_pilot", "B_CN_XSQUARE_006", "SUPPORTS", "机构内场景协作项目"),
    rr("evidence_customer_delivery", "B_CN_XSQUARE_006", "SUPPORTS", "具名机构上岗使用"),
    rr("evidence_customer_delivery", "B_CN_XSQUARE_012", "SUPPORTS", "独立渠道对同一上岗事件的重述，交叉印证"),
    rr("evidence_customer_delivery", "B_CN_XSQUARE_008", "SUPPORTS", "58 到家联合服务走进近千户（公司口径）"),
    rr("evidence_paid", "B_CN_XSQUARE_008", "CONTEXT_ONLY",
      "原文只述服务户数与联合推出，未说明付费关系，故不参与付费证据的成立与时间判定"),
    rr("evidence_repeat_order", "B_CN_XSQUARE_008", "CONTEXT_ONLY",
      "近千户为服务覆盖面，不能等同于重复订单；仅作背景"),
    rr("evidence_sustained_use", "B_CN_XSQUARE_008", "CONTEXT_ONLY",
      "服务覆盖面不是持续使用的直接证据；仅作背景"),
    rr("latest_financing_disclosed", "B_CN_XSQUARE_009", "SUPPORTS", "媒体披露四轮交割与投后估值"),
    rr("latest_financing_disclosed", "B_CN_XSQUARE_010", "SUPPORTS", "官网时间线自述历年融资"),
    rr("latest_financing_disclosed", "B_CN_XSQUARE_011", "REPLACES", "A+ 轮第三方报道，替代官网节点月份口径并保存冲突"),
    rr("latest_financing_at_observation", "B_CN_XSQUARE_009", "SUPPORTS", "观察日前披露的最近融资事件"),
    rr("latest_financing_at_observation", "B_CN_XSQUARE_010", "SUPPORTS", "官网时间线观察日前节点"),
    rr("own_listing_status", "B_CN_XSQUARE_009", "CONTEXT_ONLY",
      "股东与融资披露不回答上市状态命题；本轮未取得监管或交易所披露，故不参与成立判定"),
    rr("capital_event_x2_angel", "B_CN_XSQUARE_010", "SUPPORTS", "官网时间线天使轮节点"),
    rr("capital_event_x2_pre_a", "B_CN_XSQUARE_010", "SUPPORTS", "官网时间线 Pre-A 系列节点"),
    rr("capital_event_x2_a_round", "B_CN_XSQUARE_010", "SUPPORTS", "官网时间线 A 轮节点"),
    rr("capital_event_x2_a_plus", "B_CN_XSQUARE_011", "SUPPORTS", "A+ 轮第三方报道（2025-09）"),
    rr("capital_event_x2_a_plus", "B_CN_XSQUARE_010", "SUPPORTS", "官网时间线 A+ 轮节点（标注 2025-08，与报道月份冲突）"),
    rr("capital_event_x2_a_plus_plus", "B_CN_XSQUARE_010", "SUPPORTS", "官网时间线 A++ 轮节点"),
    rr("capital_event_x2_b_to_c", "B_CN_XSQUARE_009", "SUPPORTS", "媒体披露 B 至 C 四轮交割与估值"),
    rr("capital_event_x2_b_to_c", "B_CN_XSQUARE_010", "SUPPORTS", "官网时间线同一四轮的合计披露"),
    ]),
    ("US_AMAZON_FTR", lambda: [
    rr("legal_entity_name", "B_US_AMAZON_FTR_002", "SUPPORTS", "官方职位署名雇主为 Amazon.com Services LLC"),
    rr("legal_entity_name", "B_US_AMAZON_FTR_005", "SUPPORTS", "官方代码组织名称"),
    rr("research_subject", "B_US_AMAZON_FTR_002", "SUPPORTS", "官方职位的团队主体"),
    rr("research_subject", "B_US_AMAZON_FTR_003", "SUPPORTS", "官方职位团队段自述"),
    rr("parent_relationship", "B_US_AMAZON_FTR_002", "SUPPORTS", "官方把该岗位挂在 Amazon Robotics 组织标签下"),
    rr("hq_or_team_location", "B_US_AMAZON_FTR_001", "SUPPORTS", "官方职位 Job details 地点字段"),
    rr("founded_or_team_start_date", "B_US_AMAZON_FTR_008", "ACCESS_NOTE", "官方站点检索记录，仅说明未找到，不提供日期"),
    rr("hiring_board_channel", "B_US_AMAZON_FTR_001", "SUPPORTS", "官方职位页可达"),
    rr("hiring_board_channel", "B_US_AMAZON_FTR_004", "SUPPORTS", "官方职位页可达"),
    rr("product_lines", "B_US_AMAZON_FTR_003", "SUPPORTS", "官方职位团队段自述的技术范围"),
    rr("product_lines", "B_US_AMAZON_FTR_005", "SUPPORTS", "官方代码组织公开仓库方向"),
    rr("product_lines", "B_US_AMAZON_FTR_004", "CONTEXT_ONLY",
      "该页快照实为 10426076 页面，其摘录主体为岗位职责与原型硬件要求；仅作背景，不参与产品线断言的日期判定"),
    rr("hiring_role_scope", "B_US_AMAZON_FTR_004", "SUPPORTS",
      "招聘职责确证的岗位要求；不用于断言公司已完成的测试或生产状态"),
    rr("delivery_form", "B_US_AMAZON_FTR_003", "SUPPORTS", "官方自述研究与原型形态"),
    rr("delivery_form", "B_US_AMAZON_FTR_004", "CONTEXT_ONLY",
       "该页快照实为 10426076 页面，其正文为岗位职责；不参与交付形态断言的成立与时间判定"),
    rr("target_markets", "B_US_AMAZON_FTR_003", "SUPPORTS", "官方自述的目标方向"),
    rr("target_markets", "B_US_AMAZON_FTR_007", "CONTEXT_ONLY",
      "母公司履约规模与 Sequoia 属母公司业务，不参与 FAR 目标市场的成立与日期判定"),
    rr("deployment_status_actual", "B_US_AMAZON_FTR_003", "CONTEXT_ONLY",
      "原文为方向性表述（将要扩展至全球运营），未提供 FAR 已部署记录；仅作背景"),
    rr("evidence_internal_test", "B_US_AMAZON_FTR_004", "CONTEXT_ONLY",
      "招聘职责说明岗位要求，不能证明公司已开展内部测试；仅作岗位范围背景"),
    rr("own_listing_status", "B_US_AMAZON_FTR_002", "SUPPORTS", "官方职位署名主体，团队无独立上市状态"),
    rr("parent_listing_status", "B_US_AMAZON_FTR_006", "ACCESS_NOTE", "访问受阻记录，不构成母公司上市状态证据"),
    rr("boundary_far_vs_ftr", "B_US_AMAZON_FTR_006", "ACCESS_NOTE", "团队页 404 的访问记录"),
    rr("parent_robotics_scale_context", "B_US_AMAZON_FTR_007", "CONTEXT_ONLY", "母公司规模背景，永不计入 FAR"),
    ]),
    ("CN_FOURIER", lambda: [
    rr("legal_entity_name", "B_CN_FOURIER_001", "SUPPORTS", "官方招聘板署名主体"),
    rr("legal_entity_name", "B_CN_FOURIER_003", "SUPPORTS", "报道指认主体为上海傅利叶智能科技股份有限公司"),
    rr("research_subject", "B_CN_FOURIER_001", "SUPPORTS", "官方招聘入口确定研究主体"),
    rr("research_subject", "B_CN_FOURIER_003", "SUPPORTS", "报道确认主体范围"),
    rr("research_subject", "B_CN_FOURIER_005", "SUPPORTS", "交易对方公告使用的对方名称 Fourier Rehab"),
    rr("research_subject", "B_CN_FOURIER_006", "SUPPORTS", "成果记录署名主体与产品线"),
    rr("hq_or_team_location", "B_CN_FOURIER_005", "CONTEXT_ONLY", "公告涉及新加坡合作方，非本公司注册地；仅作背景"),
    rr("hiring_board_channel", "B_CN_FOURIER_001", "SUPPORTS", "社招频道可达"),
    rr("hiring_board_channel", "B_CN_FOURIER_002", "SUPPORTS", "校招频道可达，与社招分开"),
    rr("hiring_board_channel", "B_CN_FOURIER_010", "ACCESS_NOTE",
       "官网正文静态不可取的访问记录；不参与渠道断言的成立与时间判定"),
    rr("hiring_source_history", "B_CN_FOURIER_001", "SUPPORTS", "当前 Moka 社招渠道"),
    rr("hiring_source_history", "B_CN_FOURIER_002", "SUPPORTS", "当前 Moka 校招渠道"),
    rr("product_lines_rehab", "B_CN_FOURIER_006", "SUPPORTS", "型号与模块清单（第三方平台发布、申报方提供）"),
    rr("product_lines_rehab", "B_CN_FOURIER_007", "SUPPORTS", "受访者口径的康复产品广度"),
    rr("product_lines_rehab", "B_CN_FOURIER_003", "SUPPORTS", "交付报道中的康复产品组合"),
    rr("product_lines_humanoid", "B_CN_FOURIER_006", "SUPPORTS", "GRx 系列人形机器人型号"),
    rr("product_lines_humanoid", "B_CN_FOURIER_004", "SUPPORTS", "现场人形机器人属傅利叶产品（未指明型号）"),
    rr("product_lines_companion", "B_CN_FOURIER_006", "CONTEXT_ONLY",
      "仅有媒体标题级线索，未取得官方产品页；不参与陪伴方向断言的成立与时间判定"),
    rr("delivery_form", "B_CN_FOURIER_003", "SUPPORTS", "整院设备交付形态"),
    rr("delivery_form", "B_CN_FOURIER_005", "SUPPORTS", "交易对方确认的合作与研究形态"),
    rr("delivery_form", "B_CN_FOURIER_006", "SUPPORTS", "康复港解决方案形态"),
    rr("target_markets_malaysia", "B_CN_FOURIER_003", "SUPPORTS", "马来西亚国家级康复中心交付"),
    rr("target_markets_singapore", "B_CN_FOURIER_005", "SUPPORTS", "新加坡陈笃生医院部署与评估"),
    rr("target_markets_domestic_rehab", "B_CN_FOURIER_006", "SUPPORTS", "全国康复科室落地（申报方口径）"),
    rr("target_markets_domestic_rehab", "B_CN_FOURIER_007", "SUPPORTS", "受访者口径的国内与海外康复场景"),
    rr("named_customers_or_partners", "B_CN_FOURIER_003", "SUPPORTS", "具名机构：马来西亚 PERKESO 汝来康复中心"),
    rr("named_customers_or_partners", "B_CN_FOURIER_005", "SUPPORTS", "具名交易对方：新加坡国立医疗集团 NHG Health"),
    rr("deployment_status_actual", "B_CN_FOURIER_003", "SUPPORTS", "整院设备交付并自 2025-10 起试运营 8 个月"),
    rr("deployment_status_actual", "B_CN_FOURIER_005", "SUPPORTS", "陈笃生医院已部署并评估（交易对方公告）"),
    rr("deployment_status_actual", "B_CN_FOURIER_006", "CONTEXT_ONLY",
       "康复港落地家数为申报方口径的既往累计，不是具体部署事件；仅作背景，不参与部署断言的时间判定"),
    rr("evidence_customer_delivery", "B_CN_FOURIER_003", "SUPPORTS", "具名机构整院交付"),
    rr("evidence_customer_delivery", "B_CN_FOURIER_005", "SUPPORTS", "交易对方确认的部署关系"),
    rr("evidence_external_pilot", "B_CN_FOURIER_003", "SUPPORTS", "自 2025-10 起为期 8 个月的试运营"),
    rr("evidence_external_pilot", "B_CN_FOURIER_005", "SUPPORTS", "陈笃生医院的评估阶段记录"),
    rr("evidence_paid", "B_CN_FOURIER_003", "SUPPORTS", "总价上千万元的媒体口径"),
    rr("evidence_sustained_use", "B_CN_FOURIER_005", "SUPPORTS", "2021 年起持续合作与既有部署"),
    rr("evidence_sustained_use", "B_CN_FOURIER_003", "CONTEXT_ONLY",
       "单次交付与 8 个月试运营是部署与试点证据，不单独构成持续使用；仅作背景"),
    rr("evidence_demo", "B_CN_FOURIER_006", "SUPPORTS", "WRC 2025 展出记录"),
    rr("evidence_loi_intent", "B_CN_FOURIER_005", "SUPPORTS", "五年谅解备忘录（交易对方公告）"),
    rr("own_listing_status", "B_CN_FOURIER_009", "SUPPORTS", "媒体陈述的股份制改造与上市进程名单"),
    rr("latest_financing_disclosed", "B_CN_FOURIER_008", "SUPPORTS", "E 轮融资报道"),
    rr("latest_financing_at_observation", "B_CN_FOURIER_008", "SUPPORTS", "观察日前最近披露融资"),
    rr("capital_event_fourier_e", "B_CN_FOURIER_008", "SUPPORTS", "E 轮事件来源"),
    ]),
]

FACT_META: dict[tuple[str, str], dict] = {
    ("CN_XSQUARE", "legal_entity_name"): dict(subject="自变量机器人科技（深圳）有限公司", aggregation="single"),
    ("CN_XSQUARE", "hq_or_team_location"): dict(
        subject="自变量机器人科技（深圳）有限公司", aggregation="single",
        period_note="官网主体自述落址深圳；本轮未取得登记文件"),
    ("CN_XSQUARE", "founded_or_team_start_date"): dict(
        subject="自变量机器人科技（深圳）有限公司", aggregation="single"),
    ("CN_XSQUARE", "evidence_paid"): dict(
        subject="自变量机器人科技（深圳）有限公司", aggregation="single",
        note="本轮未取得付费关系的直接证据；不写成 0，也不写成未付费"),
    ("CN_XSQUARE", "evidence_repeat_order"): dict(
        subject="自变量机器人科技（深圳）有限公司", aggregation="single"),
    ("CN_XSQUARE", "evidence_sustained_use"): dict(
        subject="自变量机器人科技（深圳）有限公司", aggregation="single"),
    ("CN_XSQUARE", "own_listing_status"): dict(
        subject="自变量机器人科技（深圳）有限公司", aggregation="single",
        note="未取得监管或交易所披露；保持未知并退出上市状态比较维度"),
    ("CN_XSQUARE", "parent_relationship"): dict(
        subject="自变量机器人科技（深圳）有限公司", aggregation="single"),
    ("CN_XSQUARE", "ma_events"): dict(
        subject="自变量机器人科技（深圳）有限公司", aggregation="single"),
    ("CN_XSQUARE", "evidence_production_shipment"): dict(
        subject="自变量机器人科技（深圳）有限公司", aggregation="single"),
    ("US_AMAZON_FTR", "target_markets"): dict(
        subject="Amazon Frontier AI & Robotics（FAR）团队", aggregation="single",
        note="直接支持证据为职位页的团队段；母公司材料只作背景，不参与本行日期判定"),
    ("US_AMAZON_FTR", "deployment_status_actual"): dict(
        subject="Amazon Frontier AI & Robotics（FAR）团队", aggregation="single",
        note="官方表述为方向（将要扩展至全球运营）；未找到 FAR 已部署记录，母公司规模不计入"),
    ("US_AMAZON_FTR", "evidence_internal_test"): dict(
        subject="Amazon Frontier AI & Robotics（FAR）团队", aggregation="single",
        note="仅记录招聘职责要求；不足以作为公司已开展内部测试的证据，故按背景处理"),
    ("US_AMAZON_FTR", "product_lines"): dict(
        subject="Amazon Frontier AI & Robotics（FAR）团队", aggregation="single"),
    ("US_AMAZON_FTR", "parent_listing_status"): dict(
        subject="Amazon.com, Inc.（母公司）", aggregation="single",
        note="本轮未打开 SEC 或交易所页面，故保持未找到"),
    ("US_AMAZON_FTR", "ma_events"): dict(
        subject="Amazon Frontier AI & Robotics（FAR）团队", aggregation="single"),
    ("US_AMAZON_FTR", "founded_or_team_start_date"): dict(
        subject="Amazon Frontier AI & Robotics（FAR）团队", aggregation="single"),
    ("US_AMAZON_FTR", "research_subject"): dict(
        subject="Amazon Frontier AI & Robotics（FAR）团队", aggregation="single"),
    ("US_AMAZON_FTR", "hiring_role_scope"): dict(
        subject="Amazon Frontier AI & Robotics（FAR）团队", aggregation="single",
        assertion_kind="HIRING_REQUIREMENT",
        note="招聘文件所示的岗位职责范围；不代表公司层面已开展状态"),
    ("US_AMAZON_FTR", "parent_robotics_scale_context"): dict(
        subject="Amazon.com, Inc.（母公司）", aggregation="single",
        assertion_kind="PARENT_BACKGROUND",
        note="仅背景展示；不进入 FAR 任何比较维度"),
    ("US_AMAZON_FTR", "boundary_far_vs_ftr"): dict(
        subject="Amazon Frontier AI & Robotics（FAR）团队", aggregation="single",
        assertion_kind="BOUNDARY_NOTE",
        note="记录一次访问受阻；不作为团队存在与否的结论"),
    ("CN_FOURIER", "evidence_sustained_use"): dict(
        subject="上海傅利叶智能科技股份有限公司", aggregation="single",
        note="以交易对方公告的多年合作与既有部署为限，不外推到全部产品持续使用"),
    ("CN_FOURIER", "evidence_paid"): dict(
        subject="上海傅利叶智能科技股份有限公司", aggregation="single",
        note="总价上千万元为媒体口径，未见合同或付款凭据"),
    ("CN_FOURIER", "evidence_demo"): dict(
        subject="上海傅利叶智能科技股份有限公司", aggregation="single"),
    ("CN_FOURIER", "own_listing_status"): dict(
        subject="上海傅利叶智能科技股份有限公司", aggregation="single",
        note="股份制改造与上市进程为媒体陈述；未取得监管披露，不写成已申报或已上市"),
    ("CN_FOURIER", "hq_or_team_location"): dict(
        subject="上海傅利叶智能科技股份有限公司", aggregation="single",
        note="公告涉及新加坡合作方，非本公司注册地；本轮未取得登记文件，故保持未找到"),
    ("CN_FOURIER", "parent_relationship"): dict(
        subject="上海傅利叶智能科技股份有限公司", aggregation="single"),
    ("CN_FOURIER", "evidence_internal_test"): dict(
        subject="上海傅利叶智能科技股份有限公司", aggregation="single"),
    ("CN_FOURIER", "evidence_production_shipment"): dict(
        subject="上海傅利叶智能科技股份有限公司", aggregation="single"),
    ("CN_FOURIER", "ma_events"): dict(
        subject="上海傅利叶智能科技股份有限公司", aggregation="single"),
    ("CN_FOURIER", "latest_financing_disclosed"): dict(
        subject="上海傅利叶智能科技股份有限公司", aggregation="single"),
    ("CN_FOURIER", "latest_financing_at_observation"): dict(
        subject="上海傅利叶智能科技股份有限公司", aggregation="single"),
    ("CN_FOURIER", "product_lines_rehab"): dict(
        subject="上海傅利叶智能科技股份有限公司", aggregation="multi",
        assertion_kind="PRODUCT_LINE_SCOPE"),
    ("CN_FOURIER", "product_lines_humanoid"): dict(
        subject="上海傅利叶智能科技股份有限公司", aggregation="multi",
        assertion_kind="PRODUCT_LINE_SCOPE"),
    ("CN_FOURIER", "product_lines_companion"): dict(
        subject="上海傅利叶智能科技股份有限公司", aggregation="multi",
        assertion_kind="PRODUCT_LINE_SCOPE"),
    ("CN_FOURIER", "target_markets_malaysia"): dict(
        subject="上海傅利叶智能科技股份有限公司", aggregation="multi",
        assertion_kind="MARKET_SCOPE"),
    ("CN_FOURIER", "target_markets_singapore"): dict(
        subject="上海傅利叶智能科技股份有限公司", aggregation="multi",
        assertion_kind="MARKET_SCOPE"),
    ("CN_FOURIER", "target_markets_domestic_rehab"): dict(
        subject="上海傅利叶智能科技股份有限公司", aggregation="multi",
        assertion_kind="MARKET_SCOPE"),
}

DEGRADE_TO_SELF_REPORT = {"F_US_AMAZON_FTR__product_lines"}

UNKNOWN_STATUS_KEEP_EMPTY = {"SEARCHED_NOT_FOUND", "NOT_YET_SEARCHED", "ACCESS_BLOCKED", "UNKNOWN"}

FIELD_SPLIT = {
    ("CN_FOURIER", "product_lines"): [
        {"field": "product_lines_rehab",
         "value": "康复机器人产品线：ExoMotus M4 下肢外骨骼、ArmMotus EMU 三维上肢康复机器人、下肢康复机器人、伽利略生物力学分析与训练系统（约 40 余款康复产品为受访者口径）",
         "evidence_ids": ["B_CN_FOURIER_006", "B_CN_FOURIER_007", "B_CN_FOURIER_003"],
         "label": "康复产品线"},
        {"field": "product_lines_humanoid",
         "value": "人形机器人产品线：GRx 系列（GR-2、GR-3）；2026-06 报道中在 PERKESO 康复中心引导认知训练的一台人形机器人亦属傅利叶产品（未指明型号）",
         "evidence_ids": ["B_CN_FOURIER_006", "B_CN_FOURIER_004"],
         "label": "人形机器人产品线"},
        {"field": "product_lines_companion",
         "value": "陪伴与管家方向：媒体标题级线索提及 2026 年发布的管家系统与陪伴新品，本轮未逐项核实到产品页",
         "value_status": "MEDIA_STATEMENT",
         "evidence_ids": ["B_CN_FOURIER_006"],
         "decision_reason": "仅取得媒体层面的方向线索，未取得官方产品页；按媒体陈述记录，不并入康复或人形产品线",
         "label": "陪伴与管家方向"},
    ],
    ("CN_FOURIER", "target_markets"): [
        {"field": "target_markets_malaysia",
         "value": "马来西亚：国家级康复中心（PERKESO 汝来康复医院）整院康复设备交付",
         "evidence_ids": ["B_CN_FOURIER_003"],
         "label": "马来西亚交付场景"},
        {"field": "target_markets_singapore",
         "value": "新加坡：与国立医疗集团 NHG Health 的康复与机器人技术合作，涉及陈笃生医院部署与评估",
         "evidence_ids": ["B_CN_FOURIER_005"],
         "label": "新加坡临床合作场景"},
        {"field": "target_markets_domestic_rehab",
         "value": "中国国内：康复科室与康养、居家场景（落地家数为申报方与受访者口径）",
         "evidence_ids": ["B_CN_FOURIER_006", "B_CN_FOURIER_007"],
         "label": "国内康复场景"},
    ],
    ("US_AMAZON_FTR", "evidence_internal_test"): [
        {"field": "evidence_internal_test", "value_from": 0, "label": "内部测试证据"},
        {"field": "hiring_role_scope",
         "value": "岗位职责要求高自由度机器人硬件原型装配、集成、bring-up 验证、HIL 测试与失效分析（招聘文件所示职责，不代表公司当前已开展状态）",
         "value_status": "COMPANY_SELF_REPORT", "research_status": "SEARCHED_FOUND",
         "evidence_ids": ["B_US_AMAZON_FTR_004"],
         "decision_reason": "招聘页面确证的岗位职责范围；与公司层面实际测试状态分开记录",
         "label": "招聘职责范围"},
        {"field": "parent_robotics_scale_context",
         "value": "亚马逊母公司披露在运营中部署超过 75 万台机器人并介绍 Sequoia 系统（母公司口径，仅作背景）",
         "value_status": "PARENT_CONTEXT_ONLY", "research_status": "SEARCHED_FOUND",
         "evidence_ids": ["B_US_AMAZON_FTR_007"],
         "decision_reason": "母公司材料，只作背景展示，不计入 FAR 任何字段",
         "label": "母公司规模背景"},
        {"field": "boundary_far_vs_ftr",
         "value": "边界记录：amazon.jobs 团队页 /en/teams/ftr 返回 404，未取得 FTR 团队页内容，无法用该页比较 FAR 与 Fulfillment Technologies and Robotics",
         "value_status": "ACCESS_BLOCKED", "research_status": "ACCESS_BLOCKED",
         "evidence_ids": ["B_US_AMAZON_FTR_006"],
         "decision_reason": "记录一次访问受阻；该路径不存在不等于 FTR 团队不存在，不作团队存在性结论",
         "label": "FAR 与 FTR 边界访问记录"},
    ],
}

DROP_EVIDENCE_REFS = {
    ("CN_FOURIER", "target_markets", "B_CN_FOURIER_008"),
    ("CN_FOURIER", "target_markets", "B_CN_FOURIER_009"),
    ("CN_FOURIER", "target_markets", "B_CN_FOURIER_010"),
    ("US_AMAZON_FTR", "evidence_internal_test", "B_US_AMAZON_FTR_007"),
}

CAPITAL_EVENTS = {
    "CN_XSQUARE": [
        {"event_key": "capital_event_x2_angel", "event_type": "EQUITY_FINANCING", "round_or_deal": "天使轮",
         "event_date": "", "publication_date": "", "evidence_ids": ["B_CN_XSQUARE_010"],
         "amount_original": "", "currency": "", "amount_unit": "", "amount_scope": "NOT_DISCLOSED",
         "declared_event_or_period": "官网时间线节点写 2023 年 12 月；页面未给发布日期",
         "wording_original": "2023年12月 完成天使轮融资",
         "note": "官网时间线自述；金额未披露，保留未知不补造"},
        {"event_key": "capital_event_x2_pre_a", "event_type": "EQUITY_FINANCING",
         "round_or_deal": "Pre-A / Pre-A+ / Pre-A++（合并披露）",
         "event_date": "", "publication_date": "", "evidence_ids": ["B_CN_XSQUARE_010"],
         "amount_original": "数亿元", "currency": "CNY", "amount_unit": "亿元", "amount_scope": "APPROXIMATE",
         "declared_event_or_period": "官网时间线节点写 2024 年 11 月；页面未给发布日期",
         "wording_original": "2024年11月 获数亿元Pre-A++轮融资",
         "note": "官网时间线对 Pre-A 系列为合并式披露，未给出各轮金额与日期，故记一条合并披露行"},
        {"event_key": "capital_event_x2_a_round", "event_type": "EQUITY_FINANCING", "round_or_deal": "A 轮",
         "event_date": "", "publication_date": "", "evidence_ids": ["B_CN_XSQUARE_010"],
         "amount_original": "数亿元", "currency": "CNY", "amount_unit": "亿元", "amount_scope": "APPROXIMATE",
         "declared_event_or_period": "官网时间线节点写 2025 年 04 月；页面未给发布日期",
         "wording_original": "2025年04月 A轮融资数亿元", "note": "官网时间线自述"},
        {"event_key": "capital_event_x2_a_plus", "event_type": "EQUITY_FINANCING", "round_or_deal": "A+ 轮",
         "event_date": "", "publication_date": "", "evidence_ids": ["B_CN_XSQUARE_011", "B_CN_XSQUARE_010"],
         "amount_original": "近10亿元", "currency": "CNY", "amount_unit": "亿元", "amount_scope": "APPROXIMATE",
         "declared_event_or_period": "官网节点写 2025-08，媒体口径 2025-09；两条来源月份不一致",
         "wording_original": "阿里云首度落子具身智能 领投自变量机器人10亿规模融资",
         "note": "同一事件两条来源：官网节点写 2025-08，第三方报道为 2025-09；月份冲突保留在事件证据里，不拆成两个交易",
         "conflict_note": "官网时间线月份写 2025-08，媒体口径为 2025-09，按原措辞分别保存，不合并成单一日期的确定值"},
        {"event_key": "capital_event_x2_a_plus_plus", "event_type": "EQUITY_FINANCING", "round_or_deal": "A++ 轮",
         "event_date": "", "publication_date": "", "evidence_ids": ["B_CN_XSQUARE_010"],
         "amount_original": "10亿元", "currency": "CNY", "amount_unit": "亿元", "amount_scope": "REPORTED_AMOUNT",
         "declared_event_or_period": "官网时间线列出 A++ 轮但未给节点月份；页面未给发布日期",
         "wording_original": "10 亿元 A++ 轮", "note": "官网时间线自述；日期精度不足，保持未知"},
        {"event_key": "capital_event_x2_b_to_c", "event_type": "EQUITY_FINANCING",
         "round_or_deal": "B / B+ / B++ / C（四轮合计披露）",
         "event_date": "", "publication_date": "", "evidence_ids": ["B_CN_XSQUARE_009", "B_CN_XSQUARE_010"],
         "amount_original": "", "currency": "", "amount_unit": "", "amount_scope": "NOT_DISCLOSED",
         "post_money_valuation_original": "突破200亿元", "post_money_valuation_currency": "CNY",
         "declared_event_or_period": "官网时间线写 2026 年 05 月节点、媒体 2026-06-29 披露两个月内完成",
         "wording_original": "两个多月内连续完成B轮、B+轮、B++轮及C轮四轮融资并全部交割，投后估值突破200亿元",
         "note": "四轮为合计披露且两个月内连续完成，按一条事件记录并连接官网与媒体两条来源；估值与融资金额分开保存"},
    ],
    "CN_FOURIER": [
        {"event_key": "capital_event_fourier_e", "event_type": "EQUITY_FINANCING", "round_or_deal": "E 轮",
         "event_date": "", "publication_date": "", "evidence_ids": ["B_CN_FOURIER_008"],
         "amount_original": "近8亿元人民币", "currency": "CNY", "amount_unit": "亿元", "amount_scope": "APPROXIMATE",
         "declared_event_or_period": "媒体口径事件月份 2025-01，发布日 2025-01-07",
         "wording_original": "傅利叶宣布完成E轮融资 融资总额近8亿元",
         "note": "金额按原文措辞原单位保留（近 8 亿元人民币）；参与方为浦东创投、张江科投"},
    ],
    "US_AMAZON_FTR": [],
}


PILOT_IDS = ("CN_XSQUARE", "US_AMAZON_FTR", "CN_FOURIER")
AUTHORED_DIR = os.path.join(WORK, "research")


def all_company_ids() -> list[str]:
    """Every company that has an authored source: pilots first, then extensions."""
    ids = list(PILOT_IDS)
    for path in sorted(glob.glob(os.path.join(AUTHORED_DIR, "authored_*.json"))):
        cid = os.path.basename(path)[len("authored_"):-len(".json")]
        if cid not in ids:
            ids.append(cid)
    return ids


def load_old(cid: str) -> dict:
    path = OLD.get(cid)
    if path is None:
        path = os.path.join(AUTHORED_DIR, f"authored_{cid}.json")
    if not os.path.exists(path):
        raise SystemExit(
            f"research source is missing: {os.path.basename(path)} — the fact layer cannot be "
            "rebuilt from an incomplete source set")
    with open(path, "r", encoding="utf-8") as fh:
        doc = json.load(fh)
    return doc["companies"][0] if "companies" in doc else doc


def company_blocks(cid: str) -> dict:
    """The per-company block of an authored source, including the pilot envelope form."""
    doc = load_old(cid)
    return doc


def main() -> int:
    initialize_relations()
    summary = {}
    for cid in all_company_ids():
        comp = load_old(cid)
        obs = comp["observation_date"]
        _CUR["cid"] = cid
        # an extension source declares its own relations inline; the pilot envelope keeps
        # using the relation table above
        # capital events come from the source when it declares them, otherwise from the
        # pilot table above
        capital_list = comp.get("capital_events") or CAPITAL_EVENTS.get(cid, []) or []
        raw_relations = comp.get("relations") or []
        if raw_relations:
            _INLINE_RELATIONS[cid] = [
                {"cid": cid, "fact": r["fact"], "evidence": r["evidence"],
                 "role": r["role"], "review_note": r.get("review_note", ""), "fact_seq": r.get("fact_seq", 1)}
                for r in raw_relations]
        else:
            _INLINE_RELATIONS.pop(cid, None)

        evidence = []
        for ev in comp.get("evidence", []) or []:
            row = dict(ev)
            row.update(EVIDENCE_FIX.get(row["evidence_id"], {}))
            row.setdefault("claim_nature", "COMPANY_SELF_REPORT")
            evidence.append(row)
        ev_ids = {e["evidence_id"] for e in evidence}

        fact_specs: list[dict] = []
        for f in comp.get("facts", []) or []:
            field = f["field"]
            split = None if comp.get("scope_rows_materialized") else FIELD_SPLIT.get((cid, field))
            if not split:
                fact_specs.append(dict(f))
                continue
            for item in split:
                new = dict(f)
                new["field"] = item["field"]
                new["_label"] = item["label"]
                new["_parent_field"] = field
                new["value"] = item.get("value", "")
                if item.get("value_status"):
                    new["value_status"] = item["value_status"]
                if item.get("research_status"):
                    new["research_status"] = item["research_status"]
                if item.get("evidence_ids"):
                    new["evidence_ids"] = item["evidence_ids"]
                if item.get("decision_reason"):
                    new["decision_reason"] = item["decision_reason"]
                fact_specs.append(new)

        fact_label: dict[str, str] = {}
        facts = []
        seq_by_field: dict[str, int] = defaultdict(int)
        for f in fact_specs:
            field = f["field"]
            parent_field = f.get("_parent_field", field)
            meta = FACT_META.get((cid, field), {})
            seq_by_field[field] += 1
            seq = seq_by_field[field]
            fact_id = f"F_{cid}__{field}" if seq == 1 else f"F_{cid}__{field}__{seq}"
            evs = [e for e in (f.get("evidence_ids") or []) if e in ev_ids]
            evs = [e for e in evs if (cid, parent_field, e) not in DROP_EVIDENCE_REFS
                   and (cid, field, e) not in DROP_EVIDENCE_REFS]
            fact_label[fact_id] = f.get("_label", "")
            declared_ev = {x["evidence"] for x in rels_for(cid) if x["fact"] == field and x.get("fact_seq", 1) == seq}
            undeclared = [e for e in evs if e not in declared_ev]
            if undeclared:
                raise SystemExit(
                    f"relation declaration missing for {cid}:{field} -> {undeclared}; "
                    "every referenced evidence row must have an explicit relation")
            value_status = f.get("value_status", "")
            if fact_id in DEGRADE_TO_SELF_REPORT and value_status == "SUPPORTED_EXTERNAL":
                value_status = "COMPANY_SELF_REPORT"
            research_status = f.get("research_status", "") or (
                "SEARCHED_FOUND" if value_status not in UNKNOWN_STATUS_KEEP_EMPTY else value_status)
            value = f.get("value", "")
            if value_status in UNKNOWN_STATUS_KEEP_EMPTY:
                value = ""
            facts.append({
                "company_id": cid,
                "fact_id": fact_id,
                "field": field,
                "merge_parent_field": f.get("merge_parent_field", parent_field if parent_field != field else ""),
                "fact_seq": seq,
                "assertion_kind": f.get("assertion_kind", meta.get("assertion_kind", "OBSERVATION_OR_DISCLOSURE")),
                "subject_entity": f.get("subject_entity", meta.get("subject", comp.get("research_subject", ""))),
                "subject_scope": comp.get("research_subject", ""),
                "product_or_business_scope": f.get("product_or_business_scope", meta.get("product_scope", f.get("_label", ""))),
                "event_or_period": f.get("event_or_period", meta.get("period_note", "")),
                "aggregation": f.get("aggregation", meta.get("aggregation", "single")),
                "value": value,
                "unit": f.get("unit", ""),
                "value_status": value_status,
                "research_status": research_status,
                "checked_in_stage_b": "NO" if research_status == "NOT_YET_SEARCHED" else "YES",
                "decision_reason": f.get("decision_reason", ""),
                "note": f.get("note", meta.get("note", "")),
                "evidence_ids": evs,
                "inherited_gap_ids": f.get("inherited_gap_ids", []) or [],
            })

        # --- capital events exist as facts too, so every relation resolves to a fact row
        for cap in capital_list:
            parts = [p for p in (cap.get("amount_original"), cap.get("post_money_valuation_original")) if p]
            value = f"{cap['round_or_deal']}：{'；'.join(parts)}" if parts else cap["round_or_deal"]
            facts.append({
                "company_id": cid,
                "fact_id": f"F_{cid}__{cap['event_key']}",
                "field": cap["event_key"],
                "merge_parent_field": "",
                "fact_seq": 1,
                "assertion_kind": "CAPITAL_EVENT",
                "subject_entity": FACT_META.get((cid, "latest_financing_disclosed"), {}).get(
                    "subject", comp.get("research_subject", "")),
                "subject_scope": comp.get("research_subject", ""),
                "product_or_business_scope": "资本事件",
                "event_or_period": cap.get("event_date", "") or "日期未知",
                "aggregation": "single",
                "value": value,
                "unit": cap.get("amount_unit", ""),
                "value_status": "SUPPORTED_EXTERNAL" if cap.get("claim_nature") != "COMPANY_SELF_REPORT"
                                else "COMPANY_SELF_REPORT",
                "research_status": "SEARCHED_FOUND",
                "checked_in_stage_b": "YES",
                "decision_reason": cap.get("note", ""),
                "note": cap.get("conflict_note", ""),
                "evidence_ids": list(cap["evidence_ids"]),
                "inherited_gap_ids": [],
            })

        rels = []
        for rf in rels_for(cid):
            field = rf["fact"]
            rows = [x for x in facts if x["field"] == field and x["fact_seq"] == rf.get("fact_seq", 1)]
            if not rows:
                raise SystemExit(f"relation points at a fact that does not exist: {cid}:{field}")
            if rf["evidence"] not in ev_ids:
                raise SystemExit(f"relation points at unknown evidence: {cid}:{field}:{rf['evidence']}")
            frow = rows[0]
            rels.append({
                "company_id": cid,
                "fact_id": frow["fact_id"],
                "field": field,
                "fact_label": fact_label.get(frow["fact_id"], ""),
                "evidence_id": rf["evidence"],
                "relation": rf["role"],
                "review_note": rf.get("review_note", ""),
            })
        for rw in rels:
            frow = next(x for x in facts if x["fact_id"] == rw["fact_id"])
            if rw["relation"] == "SUPPORTS" and rw["evidence_id"] not in frow["evidence_ids"]:
                frow["evidence_ids"].append(rw["evidence_id"])

        caps = []
        for ev in capital_list:
            item = dict(ev)
            item["company_id"] = cid
            for e in item["evidence_ids"]:
                if e not in ev_ids:
                    raise SystemExit(f"capital event references unknown evidence: {cid}:{e}")
            caps.append(item)

        write_json(os.path.join(WORK, f"pilot_facts_v2_{cid}.json"), {
            "company_id": cid,
            "observation_date": obs,
            "research_subject": comp.get("research_subject", ""),
            "entity_note": comp.get("entity_note", ""),
            "evidence": evidence,
            "facts": facts,
            "relations": rels,
            "capital_events": caps,
            "extra_notes": comp.get("extra_notes", []),
        })
        summary[cid] = {
            "n_facts": len(facts), "n_evidence": len(evidence), "n_relations": len(rels),
            "n_capital_events": len(caps),
            "relation_roles": {k: sum(1 for x in rels if x["relation"] == k)
                               for k in sorted({x["relation"] for x in rels})},
            "value_status": {k: sum(1 for x in facts if x["value_status"] == k)
                             for k in sorted({x["value_status"] for x in facts})},
            "not_yet_searched": [x["fact_id"] for x in facts if x["research_status"] == "NOT_YET_SEARCHED"],
        }

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
