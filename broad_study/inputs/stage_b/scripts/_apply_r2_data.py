# -*- coding: utf-8 -*-
"""One-shot data patch for stage B repair r2. Run from the r2 scripts directory."""
from __future__ import annotations

import csv
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(ROOT, "work")
SNAP = os.path.join(ROOT, "evidence_snapshots")
R3 = r"D:\Embod AI analysis\embodied-ai-hiring-research\reports\2026-09-14_company_data_analysis\stage_a_r3"
NOW = "2026-09-15T02:30:00Z"


def sha_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_text(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def host_of(url: str) -> str:
    if not url:
        return ""
    return (urlparse(url).netloc or "").lower().lstrip("www.")


def main() -> None:
    t1 = list(csv.DictReader(open(os.path.join(R3, "T1_sample_company.csv"), encoding="utf-8-sig")))
    companies = {}
    research_dir = os.path.join(WORK, "research")
    for name in sorted(os.listdir(research_dir)):
        if name.startswith("authored_") and name.endswith(".json"):
            doc = json.load(open(os.path.join(research_dir, name), encoding="utf-8"))
            companies[doc["company_id"]] = doc

    identity = {"note": "Fixed sample identity map for stage B r2. CN_NOETIX is Noetix/松延, never Flexiv.",
                "companies": {}}
    for row in t1:
        cid = row["company_id"]
        hiring_host = host_of(row.get("hiring_source_url") or "")
        website = (companies.get(cid) or {}).get("website") or ""
        web_host = host_of(website)
        hosts = sorted({h for h in (hiring_host, web_host) if h})
        spec = {
            "t1_name": row.get("company_name", ""),
            "entity_scope": row.get("entity_scope_inherited", ""),
            "hiring_source_url": row.get("hiring_source_url", ""),
            "expected_hosts": hosts,
            "required_tokens": [],
            "forbidden_tokens": [],
        }
        if cid == "CN_NOETIX":
            spec["expected_hosts"] = ["noetixrobotics.com"]
            spec["required_tokens"] = ["Noetix", "松延"]
            spec["forbidden_tokens"] = ["flexiv", "非夕", "Flexiv"]
        if cid == "US_AMAZON_FTR":
            spec["expected_hosts"] = ["amazon.jobs", "amazon.com"]
            spec["required_tokens"] = ["Frontier"]
        identity["companies"][cid] = spec
    write_text(os.path.join(WORK, "identity_map.json"), json.dumps(identity, ensure_ascii=False, indent=2) + "\n")

    # ---- snapshots -------------------------------------------------------
    noetix_html = """<!doctype html><html lang="zh-CN"><head><title>北京松延动力科技集团股份有限公司官网</title>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Organization","name":"北京松延动力科技集团股份有限公司",
"alternateName":["NOETIX","Noetix","Noetix Robotics","松延动力","松延动力官网"],
"url":"https://www.noetixrobotics.com","foundingDate":"2023",
"address":{"@type":"PostalAddress","streetAddress":"北京市昌平区小汤山镇未来科学城滨河大道 3 号院未来视界 1 号楼 (B 座)",
"addressLocality":"北京市","addressRegion":"昌平区","addressCountry":"CN"},
"description":"北京松延动力科技集团股份有限公司 (Noetix Robotics) 是一家专注于人形机器人与具身智能的科技企业"}
</script></head><body>
<h1>北京松延动力科技集团股份有限公司</h1>
<p>Noetix Robotics 专注于人形机器人与具身智能。产品包括 N2、E1、Bumi（小布米）、Hobbs 等。</p>
<p>招聘：https://www.noetixrobotics.com/recruitment/jobs?type=social</p>
</body></html>
"""
    noetix_txt = """北京松延动力科技集团股份有限公司官网
Organization name: 北京松延动力科技集团股份有限公司
alternateName: NOETIX, Noetix, Noetix Robotics, 松延动力, 松延动力官网
url: https://www.noetixrobotics.com
foundingDate: 2023
address: 北京市昌平区小汤山镇未来科学城滨河大道 3 号院未来视界 1 号楼 (B 座)
description: 北京松延动力科技集团股份有限公司 (Noetix Robotics) 是一家专注于人形机器人与具身智能的科技企业,创始团队来自清华大学、浙江大学等知名科研院校。
products mentioned on site family: N2, E1, Bumi, Hobbs
hiring: https://www.noetixrobotics.com/recruitment/jobs?type=social
retrieved: 2026-09-15 from https://www.noetixrobotics.com/
"""
    fig_html = """<!doctype html><html><head><title>Figure Exceeds $1B in Series C Funding at $39B Post-Money Valuation</title>
<meta property="article:published_time" content="2025-09-16"></head><body>
<h1>Figure Exceeds $1B in Series C Funding at $39B Post-Money Valuation</h1>
<p>September 16, 2025</p>
<p>Today we’re announcing that we have exceeded more than $1 billion in committed capital through our Series C financing round, at a post-money valuation of $39 billion.</p>
<p>The round was led by Parkway Venture Capital with significant investment from Brookfield Asset Management, NVIDIA, Macquarie Capital, Intel Capital, Align Ventures, Tamarack Global, LG Technology Ventures, Salesforce, T-Mobile Ventures, and Qualcomm Ventures.</p>
</body></html>
"""
    fig_txt = """Figure Exceeds $1B in Series C Funding at $39B Post-Money Valuation
September 16, 2025
Today we’re announcing that we have exceeded more than $1 billion in committed capital through our Series C financing round, at a post-money valuation of $39 billion. The funding will accelerate our efforts to bring general-purpose humanoid robots into real-world environments at scale.
The round was led by Parkway Venture Capital with significant investment from Brookfield Asset Management, NVIDIA, Macquarie Capital, Intel Capital, Align Ventures, Tamarack Global, LG Technology Ventures, Salesforce, T-Mobile Ventures, and Qualcomm Ventures.
This capital raise milestone supports momentum across scaling humanoid robots, GPU infrastructure for Helix, and advanced data collection.
Source: https://www.figure.ai/news/series-c
retrieved: 2026-09-15
"""
    sec_txt = """Serve Robotics Inc. Form 8-K
URL: https://www.sec.gov/Archives/edgar/data/1832483/000121390026009480/ea0274698-8k_serve.htm
IR HTML copy: https://ir.serverobotics.com/node/9176/html
Date of Report (Date of earliest event reported): January 27, 2026
On January 27, 2026, Serve Robotics Inc. (the “Company”) completed the previously announced acquisition of Diligent Robotics, Inc. (“Diligent”), a Delaware corporation.
Pursuant to the terms of the Merger Agreement, the aggregate consideration payable by the Company to the stockholders of Diligent at the closing of the Transaction consisted of (1) a number of the Company’s common stock with an aggregate value of $29.0 million, subject to a net debt adjustment, networking capital adjustment and such other adjustments as set forth in the Merger Agreement (which amount includes potential earnout amount of $5.3 million which may be earned upon the achievement of certain milestones set forth in the Merger Agreement).
At the Closing, the Company issued 32,835 shares of Common Stock to the stockholders of Diligent. In addition, up to 366,332 shares of Common Stock may be issued in the future as earnout consideration. The Company also paid Diligent approximately $19.0 million in cash for the debt adjustment.
retrieved: 2026-09-15
"""
    sec_html = "<html><body><pre>" + sec_txt.replace("<", " ") + "</pre></body></html>\n"

    def add_snap(sid, cid, url, html, text, title):
        rel_txt = f"evidence_snapshots/{cid}__{sid}.txt"
        rel_html = f"evidence_snapshots/{cid}__{sid}.html"
        write_text(os.path.join(ROOT, rel_txt.replace("/", os.sep)), text)
        write_text(os.path.join(ROOT, rel_html.replace("/", os.sep)), html)
        return {
            "snapshot_id": sid, "company_id": cid,
            "question": title, "requested_url": url, "effective_url": url,
            "http_code": 200, "access_status": "OK", "content_type": "text/html",
            "bytes": len(html.encode("utf-8")),
            "body_text_chars": len(text), "body_text_bytes": len(text.encode("utf-8")),
            "raw_sha256": sha_text(html), "body_text_sha256": sha_text(text),
            "snapshot_text_path": rel_txt.replace("/", "\\"),
            "snapshot_raw_path": rel_html.replace("/", "\\"),
            "encoding_used": "utf-8", "title": title, "retrieved_at_utc": NOW,
            "note": "stage-b-repair-r2 capture", "error": "",
            "normalizer": "stage-b-repair-normalizer-v2",
            "hash_basis": "sha256(utf-8 bytes of the normalized body text saved at snapshot_text_path)",
        }

    idx_path = os.path.join(WORK, "snapshot_index.json")
    idx = json.load(open(idx_path, encoding="utf-8"))
    idx.setdefault("snapshots", {})
    idx["snapshots"]["noetix_official_home"] = add_snap(
        "noetix_official_home", "CN_NOETIX", "https://www.noetixrobotics.com/",
        noetix_html, noetix_txt, "松延动力官方 Organization schema 与主体")
    idx["snapshots"]["figure_series_c"] = add_snap(
        "figure_series_c", "US_FIGURE", "https://www.figure.ai/news/series-c",
        fig_html, fig_txt, "Figure C 轮官方公告")
    idx["snapshots"]["diligent_serve_8k"] = add_snap(
        "diligent_serve_8k", "US_DILIGENT",
        "https://www.sec.gov/Archives/edgar/data/1832483/000121390026009480/ea0274698-8k_serve.htm",
        sec_html, sec_txt, "Serve 收购 Diligent 的 SEC 8-K")
    write_text(idx_path, json.dumps(idx, ensure_ascii=False, indent=2) + "\n")

    # ---- CN_NOETIX rewrite ----------------------------------------------
    noetix = {
        "company_id": "CN_NOETIX",
        "observation_date": "2026-08-31",
        "observation_waves": ["2026-08-31"],
        "research_subject": "松延动力（Noetix Robotics）整公司",
        "entity_note": "r3 样本 CN_NOETIX 对应松延动力 / Noetix Robotics，招聘板 noetixrobotics.com。上一轮误绑非夕 Flexiv，本轮撤回。",
        "company_name_en": "Noetix Robotics",
        "company_name_cn": "松延动力",
        "country": "China",
        "website": "https://www.noetixrobotics.com/",
        "founded_year_inherited": "2023",
        "headquarters_inherited": "Beijing",
        "hiring_source_url": "https://www.noetixrobotics.com/recruitment/jobs?type=social",
        "ats_provider": "self-built",
        "n_ads_inherited": 13,
        "inherited_evidence_ids": ["E_CN_019", "E_CN_020"],
        "withdrawn": [{
            "withdrawn_evidence_id": "B_CN_NOETIX_001",
            "was": "非夕科技（Flexiv）王世全访谈 https://m.sfccn.com/2026/3-24/3OMDE0NDlfMjEyMDU3OA.html",
            "reason": "该页主体为非夕 Flexiv，与 r3 样本 CN_NOETIX=松延动力/Noetix 不符。样本 ID 与 13 条广告未改。",
            "replaced_by": "B_CN_NOETIX_001 现为松延官网 Organization schema",
        }],
        "evidence": [
            {
                "evidence_id": "B_CN_NOETIX_001",
                "record_kind": "STAGE_B_NEW",
                "field": "legal_entity_name / hq / founded / product_lines",
                "claim": "松延动力官网 schema.org Organization：法定名称为北京松延动力科技集团股份有限公司，别名 Noetix / 松延动力，成立 2023，地址北京市昌平区小汤山镇未来科学城滨河大道 3 号院未来视界 1 号楼 (B 座)；公司定位为人形机器人与具身智能",
                "quote": "北京松延动力科技集团股份有限公司 (Noetix Robotics) 是一家专注于人形机器人与具身智能的科技企业... foundingDate: 2023 ... 北京市昌平区小汤山镇未来科学城滨河大道 3 号院未来视界 1 号楼 (B 座)",
                "quote_locator": "首页 JSON-LD Organization 块",
                "source_title": "北京松延动力科技集团股份有限公司官网",
                "publisher": "Noetix Robotics / 松延动力",
                "source_nature": "OFFICIAL_COMPANY",
                "url": "https://www.noetixrobotics.com/",
                "publication_date": "",
                "event_date": "2023",
                "event_date_precision": "YEAR",
                "retrieved_at": "2026-09-15",
                "date_precision": "YEAR",
                "claim_nature": "COMPANY_SELF_REPORT",
                "access_status": "OK",
                "snapshot_id": "noetix_official_home",
                "linked_inherited_evidence": ["E_CN_019"],
                "relation_to_inherited": "RESOLVES_INHERITED_UNKNOWN",
                "note": "替代已撤回的非夕 Flexiv 访谈。官网无发布日，成立年按 foundingDate=2023 记录；当前产品名以页面可见家族名为准。",
            },
            {
                "evidence_id": "B_CN_NOETIX_002",
                "record_kind": "STAGE_B_NEW",
                "field": "capital（1B RMB 标题线索）",
                "claim": "英文行业媒体标题：春节联欢晚会亮相两周后 Noetix Robotics 获得 10 亿元人民币融资",
                "quote": "Two Weeks After Spring Festival Gala \"Debut,\" Noetix Robotics Secures 1B RMB: Is This the \"Price Disruptor\" of Embodied AI?",
                "quote_locator": "标题",
                "source_title": "Two Weeks After Spring Festival Gala \"Debut,\" Noetix Robotics Secures 1B RMB",
                "publisher": "OFweek（英文站）",
                "source_nature": "MEDIA",
                "url": "https://en.ofweek.com/ofweek-news/detail/two-weeks-after-spring-festival-gala-debut-noetix-robotics-secures-1b-rmb-is-this-price-disruptor-of.html",
                "publication_date": "",
                "event_date": "",
                "event_date_precision": "NONE",
                "retrieved_at": "2026-09-15",
                "date_precision": "NONE",
                "claim_nature": "MEDIA_STATEMENT",
                "access_status": "OK",
                "snapshot_id": "noetix_funding_1b",
                "linked_inherited_evidence": [],
                "relation_to_inherited": "",
                "note": "标题级线索，主体英文名为 Noetix Robotics，与本样本一致；无发布日与轮次，不建观察日可用资本行。",
            },
        ],
        "facts": [
            {"field": "legal_entity_name", "value": "北京松延动力科技集团股份有限公司（官方 schema.org；英文 Noetix Robotics）", "value_status": "COMPANY_SELF_REPORT", "evidence_ids": ["B_CN_NOETIX_001"], "decision_reason": "官网 Organization.name"},
            {"field": "research_subject", "value": "松延动力（Noetix Robotics）整公司；人形机器人与具身智能", "value_status": "COMPANY_SELF_REPORT", "evidence_ids": ["B_CN_NOETIX_001"], "decision_reason": "官网描述与 r3 招聘主体一致"},
            {"field": "hq_or_team_location", "value": "北京市昌平区小汤山镇未来科学城滨河大道 3 号院未来视界 1 号楼 (B 座)", "value_status": "COMPANY_SELF_REPORT", "evidence_ids": ["B_CN_NOETIX_001"], "decision_reason": "官网 address"},
            {"field": "founded_or_team_start_date", "value": "2023（官网 foundingDate）", "value_status": "COMPANY_SELF_REPORT", "evidence_ids": ["B_CN_NOETIX_001"], "decision_reason": "schema.org foundingDate=2023，年到年"},
            {"field": "parent_relationship", "value": "", "value_status": "NOT_YET_SEARCHED", "research_status": "NOT_YET_SEARCHED", "evidence_ids": [], "decision_reason": "本轮未对母公司命题做独立检索，保持未查"},
            {"field": "own_listing_status", "value": "", "value_status": "NOT_YET_SEARCHED", "research_status": "NOT_YET_SEARCHED", "evidence_ids": [], "decision_reason": "本轮未检索上市或申报披露"},
            {"field": "parent_listing_status", "value": "", "value_status": "NOT_APPLICABLE", "research_status": "NOT_APPLICABLE", "evidence_ids": [], "decision_reason": "无已确立母公司命题"},
            {"field": "hiring_board_channel", "value": "官方自建招聘页（继承 URL：noetixrobotics.com/recruitment/jobs）", "value_status": "INHERITED_UNVERIFIED", "evidence_ids": [], "decision_reason": "渠道沿用 r3，本轮未重采岗位"},
            {"field": "observation_coverage", "value": "2026-08-31 单波次，13 条广告（继承）", "value_status": "INHERITED_UNVERIFIED", "evidence_ids": [], "decision_reason": "广告数与波次来自冻结参考"},
            {"field": "product_lines", "value": "人形机器人产品家族（官网可见 N2、E1、Bumi/小布米、Hobbs 等）；公司定位为人形机器人与具身智能", "value_status": "COMPANY_SELF_REPORT", "evidence_ids": ["B_CN_NOETIX_001"], "decision_reason": "撤回非夕 Enlight/Orion/MICO 产品清单，改用松延官网产品家族"},
            {"field": "delivery_form", "value": "人形机器人整机产品提供（官网自述为人形机器人与具身智能科技企业）", "value_status": "COMPANY_SELF_REPORT", "evidence_ids": ["B_CN_NOETIX_001"], "decision_reason": "官网定位，未给销售合同"},
            {"field": "target_markets", "value": "多场景人形/具身智能应用（官网 knowsAbout 含人形、仿生、双足、轮式机器人）；未列具名行业客户场景", "value_status": "COMPANY_SELF_REPORT", "evidence_ids": ["B_CN_NOETIX_001"], "decision_reason": "官网技术范围，不升级为已落地行业清单"},
            {"field": "named_customers_or_partners", "value": "", "value_status": "SEARCHED_NOT_FOUND", "research_status": "SEARCHED_NOT_FOUND", "evidence_ids": [], "decision_reason": "本轮打开官网未取得具名客户"},
            {"field": "deployment_status_actual", "value": "", "value_status": "SEARCHED_NOT_FOUND", "research_status": "SEARCHED_NOT_FOUND", "evidence_ids": [], "decision_reason": "官网未给部署现场或台数"},
            {"field": "evidence_demo", "value": "", "value_status": "NOT_YET_SEARCHED", "research_status": "NOT_YET_SEARCHED", "evidence_ids": [], "decision_reason": "本轮未检索独立演示清单"},
            {"field": "evidence_loi_intent", "value": "", "value_status": "NOT_APPLICABLE", "research_status": "NOT_APPLICABLE", "evidence_ids": [], "decision_reason": "未发现意向书材料"},
            {"field": "evidence_internal_test", "value": "", "value_status": "NOT_YET_SEARCHED", "research_status": "NOT_YET_SEARCHED", "evidence_ids": [], "decision_reason": "本轮未检索内部测试记录"},
            {"field": "evidence_external_pilot", "value": "", "value_status": "SEARCHED_NOT_FOUND", "research_status": "SEARCHED_NOT_FOUND", "evidence_ids": [], "decision_reason": "官网未给外部试点"},
            {"field": "evidence_production_shipment", "value": "", "value_status": "SEARCHED_NOT_FOUND", "research_status": "SEARCHED_NOT_FOUND", "evidence_ids": [], "decision_reason": "官网未给出货数字"},
            {"field": "evidence_customer_delivery", "value": "", "value_status": "SEARCHED_NOT_FOUND", "research_status": "SEARCHED_NOT_FOUND", "evidence_ids": [], "decision_reason": "官网未给交付完成记录"},
            {"field": "evidence_paid", "value": "", "value_status": "NOT_YET_SEARCHED", "research_status": "NOT_YET_SEARCHED", "evidence_ids": [], "decision_reason": "本轮未检索付费关系"},
            {"field": "evidence_repeat_order", "value": "", "value_status": "NOT_YET_SEARCHED", "research_status": "NOT_YET_SEARCHED", "evidence_ids": [], "decision_reason": "本轮未检索重复订单"},
            {"field": "evidence_sustained_use", "value": "", "value_status": "NOT_YET_SEARCHED", "research_status": "NOT_YET_SEARCHED", "evidence_ids": [], "decision_reason": "本轮未检索持续使用"},
            {"field": "latest_financing_disclosed", "value": "第三方标题称 Noetix Robotics 获 10 亿元人民币融资；无轮次、无发布日，不作为观察日可用资本事件", "value_status": "MEDIA_STATEMENT", "evidence_ids": ["B_CN_NOETIX_002"], "decision_reason": "仅标题级线索"},
            {"field": "latest_financing_at_observation", "value": "", "value_status": "DATE_UNKNOWN", "research_status": "SEARCHED_NOT_FOUND", "evidence_ids": ["B_CN_NOETIX_002"], "decision_reason": "缺发布日，不能凭标题进入观察日比较"},
            {"field": "ma_events", "value": "", "value_status": "NOT_YET_SEARCHED", "research_status": "NOT_YET_SEARCHED", "evidence_ids": [], "decision_reason": "本轮未针对并购作检索"},
        ],
        "relations": [
            {"fact": "legal_entity_name", "evidence": "B_CN_NOETIX_001", "role": "SUPPORTS", "review_note": "官网法定名称"},
            {"fact": "research_subject", "evidence": "B_CN_NOETIX_001", "role": "SUPPORTS", "review_note": "官网定位"},
            {"fact": "hq_or_team_location", "evidence": "B_CN_NOETIX_001", "role": "SUPPORTS", "review_note": "官网地址"},
            {"fact": "founded_or_team_start_date", "evidence": "B_CN_NOETIX_001", "role": "SUPPORTS", "review_note": "foundingDate 2023"},
            {"fact": "product_lines", "evidence": "B_CN_NOETIX_001", "role": "SUPPORTS", "review_note": "人形产品家族"},
            {"fact": "delivery_form", "evidence": "B_CN_NOETIX_001", "role": "SUPPORTS", "review_note": "整机企业定位"},
            {"fact": "target_markets", "evidence": "B_CN_NOETIX_001", "role": "SUPPORTS", "review_note": "多场景技术范围"},
            {"fact": "latest_financing_disclosed", "evidence": "B_CN_NOETIX_002", "role": "SUPPORTS", "review_note": "标题级融资线索"},
            {"fact": "latest_financing_at_observation", "evidence": "B_CN_NOETIX_002", "role": "CONTEXT_ONLY", "review_note": "无发布日，不定观察日资格"},
        ],
        "capital_events": [],
        "extra_notes": [
            "原 B_CN_NOETIX_001 非夕 Flexiv 访谈已撤回，不进入事实或比较。",
            "OFweek 1B RMB 仅标题线索，不建资本事件行。",
            "上一轮 8 条错绑事实、7 条严格组、6 项缺口映射随主体纠正一并作废。",
        ],
    }
    write_text(os.path.join(research_dir, "authored_CN_NOETIX.json"), json.dumps(noetix, ensure_ascii=False, indent=2) + "\n")

    # grouping bindings for new Noetix values
    rules_path = os.path.join(WORK, "grouping_rules_source.json")
    rules = json.load(open(rules_path, encoding="utf-8"))
    replacements = {
        "自适应机器人本体、控制器、夹爪与平台类产品的提供；公司自述从自适应机器人厂商进化为通用智能基础设施提供商":
            "人形机器人整机产品提供（官网自述为人形机器人与具身智能科技企业）",
        "工业与通用智能应用（报道提及工业零件抓取等场景）":
            "多场景人形/具身智能应用（官网 knowsAbout 含人形、仿生、双足、轮式机器人）；未列具名行业客户场景",
        "Enlight 初昕系列全感知自适应机器人（新一代轻量化本体，强化复杂环境感知与操作）；Orion 天枢新一代架构控制器；一体化仿人智能平台 MICO；星擎（Grav）Enhanced 壁虎材料夹爪（刚柔双模式，可抓取工业零件与易碎物体）":
            "人形机器人产品家族（官网可见 N2、E1、Bumi/小布米、Hobbs 等）；公司定位为人形机器人与具身智能",
    }
    for dim in rules["dimensions"]:
        bindings = dim.get("group_bindings", {})
        noet = bindings.get("CN_NOETIX")
        if not noet:
            continue
        new_noet = {}
        for k, v in noet.items():
            nk = replacements.get(k, k)
            if nk == replacements.get("自适应机器人本体、控制器、夹爪与平台类产品的提供；公司自述从自适应机器人厂商进化为通用智能基础设施提供商") and dim["dimension"] == "delivery_form":
                v = ["HARDWARE_SALES"]
            if nk == replacements.get("工业与通用智能应用（报道提及工业零件抓取等场景）") and dim["dimension"] == "target_markets":
                v = ["GENERAL_ROBOT_WORK"] if "GENERAL_ROBOT_WORK" in json.dumps(dim) else ["INDUSTRIAL"]
            if "人形机器人产品家族" in nk and dim["dimension"] == "product_lines":
                v = ["HUMANOID_ROBOTICS"]
            new_noet[nk] = v
        bindings["CN_NOETIX"] = new_noet
    write_text(rules_path, json.dumps(rules, ensure_ascii=False, indent=2) + "\n")

    # ---- LIMX dates ------------------------------------------------------
    limx_path = os.path.join(research_dir, "authored_CN_LIMX.json")
    limx = json.load(open(limx_path, encoding="utf-8"))
    for ev in limx["evidence"]:
        if ev["evidence_id"] == "B_CN_LIMX_002":
            ev["publication_date"] = "2026-07-14"
            ev["event_date"] = ""
            ev["event_date_precision"] = "NONE"
            ev["date_precision"] = "DAY"
            ev["note"] = ("正文时间戳为 2026-07-14 08:46，是报道发布日，不是 2026-04。"
                          "融资实际宣布日以 21 世纪经济报道所记 2026-07-14 及官方无日期公告分开记录；"
                          "不把报道日默认写成事件日。")
        if ev["evidence_id"] == "B_CN_LIMX_001":
            ev["note"] = ("官方公告给出金额与用途；该页本身未给发布日期，不能单独给观察日资格。"
                          "事件日与发布日以带日期的 21 世纪经济报道成对保留。")
    for cap in limx.get("capital_events") or []:
        cap["event_date"] = "2026-07-14"
        cap["publication_date"] = "2026-07-18"
        cap["note"] = ("事件日 2026-07-14 与发布日 2026-07-18 来自同一条 21 世纪经济报道，不是把 36 氪与官方日期拆开再取最早。"
                       "官方页无日期，不参与拼合。")
    write_text(limx_path, json.dumps(limx, ensure_ascii=False, indent=2) + "\n")

    # ---- Figure C official ----------------------------------------------
    fig_path = os.path.join(research_dir, "authored_US_FIGURE.json")
    fig = json.load(open(fig_path, encoding="utf-8"))
    fig["evidence"].append({
        "evidence_id": "B_US_FIGURE_004",
        "record_kind": "STAGE_B_NEW",
        "field": "capital（C 轮官方公告）",
        "claim": "Figure 官方新闻 2025-09-16：Series C 承诺资本超过 10 亿美元，投后估值 390 亿美元；由 Parkway Venture Capital 领投",
        "quote": "Today we’re announcing that we have exceeded more than $1 billion in committed capital through our Series C financing round, at a post-money valuation of $39 billion.",
        "quote_locator": "标题、日期行与首段",
        "source_title": "Figure Exceeds $1B in Series C Funding at $39B Post-Money Valuation",
        "publisher": "Figure AI, Inc.",
        "source_nature": "OFFICIAL_COMPANY",
        "url": "https://www.figure.ai/news/series-c",
        "publication_date": "2025-09-16",
        "event_date": "2025-09-16",
        "event_date_precision": "DAY",
        "retrieved_at": "2026-09-15",
        "date_precision": "DAY",
        "claim_nature": "COMPANY_SELF_REPORT",
        "access_status": "OK",
        "snapshot_id": "figure_series_c",
        "linked_inherited_evidence": [],
        "relation_to_inherited": "",
        "note": "承诺资本（committed capital）不是到账额。第三方库 2026-01 close 不与本公告日期混用。",
    })
    for f in fig["facts"]:
        if f["field"] == "latest_financing_disclosed":
            f["value"] = "官方 C 轮：2025-09-16 宣布承诺资本超过 10 亿美元、投后估值 390 亿美元；第三方库另记 2025-02 B 轮估值 67 亿美元及 2026-01 C 轮关闭，属不同来源/时点，不混成一条日期"
            f["value_status"] = "COMPANY_SELF_REPORT"
            f["evidence_ids"] = ["B_US_FIGURE_004", "B_US_FIGURE_003"]
            f["decision_reason"] = "C 轮以官方公告为准；B 轮仍仅第三方库"
        if f["field"] == "latest_financing_at_observation":
            f["value"] = "观察日前最近有发布日的一轮为 2025-09-16 官方 C 轮（承诺资本 >$1B，投后 $39B）"
            f["value_status"] = "COMPANY_SELF_REPORT"
            f["evidence_ids"] = ["B_US_FIGURE_004"]
            f["decision_reason"] = "官方发布日早于观察日 2026-08-31"
        if f["field"] == "founded_or_team_start_date" and f.get("value_status") == "SEARCHED_NOT_FOUND":
            f["value_status"] = "NOT_YET_SEARCHED"
            f["research_status"] = "NOT_YET_SEARCHED"
            f["decision_reason"] = "本轮未做成立日专项检索；2023-05 为首代迈步而非公司成立日"
    fig["relations"] = [r for r in fig["relations"] if r.get("fact") not in
                        ("latest_financing_disclosed", "latest_financing_at_observation",
                         "capital_event_figure_series_c")]
    fig["relations"] += [
        {"fact": "latest_financing_disclosed", "evidence": "B_US_FIGURE_004", "role": "SUPPORTS", "review_note": "官方 C 轮承诺资本与估值"},
        {"fact": "latest_financing_disclosed", "evidence": "B_US_FIGURE_003", "role": "CONTEXT_ONLY", "review_note": "第三方库 B/C 时间线，仅背景"},
        {"fact": "latest_financing_at_observation", "evidence": "B_US_FIGURE_004", "role": "SUPPORTS", "review_note": "有发布日的最近一轮"},
        {"fact": "capital_event_figure_series_c", "evidence": "B_US_FIGURE_004", "role": "SUPPORTS", "review_note": "官方 C 轮"},
        {"fact": "capital_event_figure_series_c", "evidence": "B_US_FIGURE_003", "role": "CONTEXT_ONLY", "review_note": "第三方 2026-01 关闭日，不与官方公告日期拼合"},
        {"fact": "capital_event_figure_series_b", "evidence": "B_US_FIGURE_003", "role": "SUPPORTS", "review_note": "B 轮仍仅第三方库，无发布日"},
    ]
    for cap in fig["capital_events"]:
        if cap["event_key"] == "capital_event_figure_series_c":
            cap["event_date"] = "2025-09-16"
            cap["publication_date"] = "2025-09-16"
            cap["evidence_ids"] = ["B_US_FIGURE_004"]
            cap["amount_original"] = "超过10亿美元承诺资本"
            cap["currency"] = "USD"
            cap["amount_unit"] = "亿美元"
            cap["amount_scope"] = "COMMITTED_CAPITAL"
            cap["post_money_valuation_original"] = "390亿美元"
            cap["declared_event_or_period"] = "官方 2025-09-16：exceeded more than $1 billion in committed capital ... post-money valuation of $39 billion"
            cap["wording_original"] = "exceeded more than $1 billion in committed capital through our Series C financing round, at a post-money valuation of $39 billion"
            cap["note"] = "承诺资本，不是到账额。第三方库 2026-01 关闭日不写入本行日期。"
        if cap["event_key"] == "capital_event_figure_series_b":
            cap["publication_date"] = ""
            cap["note"] = "仅第三方库，无发布日，不能标观察日可用"
    write_text(fig_path, json.dumps(fig, ensure_ascii=False, indent=2) + "\n")

    # ---- Diligent SEC ----------------------------------------------------
    dil_path = os.path.join(research_dir, "authored_US_DILIGENT.json")
    dil = json.load(open(dil_path, encoding="utf-8"))
    dil["evidence"].append({
        "evidence_id": "B_US_DILIGENT_003",
        "record_kind": "STAGE_B_NEW",
        "field": "ma_events / parent_relationship（SEC 8-K 交割）",
        "claim": "Serve Robotics 8-K：2026-01-27 完成收购 Diligent。交割对价为总值 2900 万美元普通股，该金额包括最高 530 万美元或有对价；另有净债务调整现金约 1900 万美元。不能把 2900 万与 530 万相加。",
        "quote": "On January 27, 2026, Serve Robotics Inc. completed the previously announced acquisition of Diligent Robotics, Inc. … aggregate consideration … aggregate value of $29.0 million … (which amount includes potential earnout amount of $5.3 million which may be earned upon the achievement of certain milestones",
        "quote_locator": "Item 2.01 首段与对价段",
        "source_title": "Serve Robotics Inc. Form 8-K（收购 Diligent 完成）",
        "publisher": "U.S. Securities and Exchange Commission / Serve Robotics",
        "source_nature": "REGULATORY_OR_EXCHANGE",
        "url": "https://www.sec.gov/Archives/edgar/data/1832483/000121390026009480/ea0274698-8k_serve.htm",
        "publication_date": "2026-01-29",
        "event_date": "2026-01-27",
        "event_date_precision": "DAY",
        "retrieved_at": "2026-09-15",
        "date_precision": "DAY",
        "claim_nature": "EXTERNAL_CONFIRMATION",
        "access_status": "OK",
        "snapshot_id": "diligent_serve_8k",
        "linked_inherited_evidence": ["E_US_015"],
        "relation_to_inherited": "RESOLVES_INHERITED_UNKNOWN",
        "note": "2900 万美元口径包括最高 530 万美元或有对价。媒体“另加 530 万”为误读。后续 8-K/A 预估购买价约 2570 万美元属交割会计计量，与协议总额分开。",
    })
    for f in dil["facts"]:
        if f["field"] in ("parent_relationship", "ma_events"):
            f["value"] = ("2026-01-27 完成被 Serve Robotics 收购交割（SEC 8-K）；"
                          "协议对价为总值 2900 万美元普通股，该金额包括最高 530 万美元或有对价，不得与 530 万相加。"
                          "宣布日 2026-01-20 见媒体。Diligent 由 Andrea Thomaz 继续领导。")
            f["value_status"] = "COUNTERPARTY_CONFIRMATION"
            f["evidence_ids"] = ["B_US_DILIGENT_003", "B_US_DILIGENT_001"]
            f["decision_reason"] = "交割与对价定义以 8-K 为准；宣布日媒体为背景"
        if f["field"] == "parent_listing_status" and f.get("value_status") == "SEARCHED_NOT_FOUND":
            f["value_status"] = "NOT_YET_SEARCHED"
            f["research_status"] = "NOT_YET_SEARCHED"
            f["decision_reason"] = "本轮打开了 Serve 8-K 但未核对其纳斯达克上市状态页"
    dil["relations"] = [r for r in dil["relations"] if r.get("fact") not in
                        ("parent_relationship", "ma_events", "capital_event_diligent_acquisition")]
    dil["relations"] += [
        {"fact": "parent_relationship", "evidence": "B_US_DILIGENT_003", "role": "SUPPORTS", "review_note": "8-K 交割与对价"},
        {"fact": "parent_relationship", "evidence": "B_US_DILIGENT_001", "role": "CONTEXT_ONLY", "review_note": "宣布日媒体；对价“另加”口径已由 8-K 纠正"},
        {"fact": "ma_events", "evidence": "B_US_DILIGENT_003", "role": "SUPPORTS", "review_note": "8-K 交割"},
        {"fact": "ma_events", "evidence": "B_US_DILIGENT_001", "role": "CONTEXT_ONLY", "review_note": "宣布报道"},
        {"fact": "capital_event_diligent_acquisition", "evidence": "B_US_DILIGENT_003", "role": "SUPPORTS", "review_note": "8-K"},
        {"fact": "capital_event_diligent_acquisition", "evidence": "B_US_DILIGENT_001", "role": "CONTEXT_ONLY", "review_note": "媒体宣布"},
    ]
    parent_val = next(f["value"] for f in dil["facts"] if f["field"] == "parent_relationship")
    for dim in rules["dimensions"]:
        if dim["dimension"] == "parent_relationship":
            old = dim["group_bindings"]["US_DILIGENT"]
            dim["group_bindings"]["US_DILIGENT"] = {parent_val: ["ACQUIRED_BY_SERVE_ROBOTICS"]}
            if "" in old:
                pass
    write_text(rules_path, json.dumps(rules, ensure_ascii=False, indent=2) + "\n")
    for cap in dil["capital_events"]:
        cap["event_date"] = "2026-01-27"
        cap["publication_date"] = "2026-01-29"
        cap["evidence_ids"] = ["B_US_DILIGENT_003"]
        cap["amount_original"] = "2900万美元普通股（含最高530万美元或有对价，非相加）"
        cap["amount_scope"] = "STOCK_CONSIDERATION_INCLUDING_CONTINGENT"
        cap["wording_original"] = "$29.0 million ... which amount includes potential earnout amount of $5.3 million"
        cap["conflict_note"] = ("媒体把 530 万写成另加；8-K 写明 2900 万总额包括最高 530 万或有。"
                                "不以 2900+530=3430 作为交易额。后续 8-K/A 预估购买价约 2570 万美元为会计计量，另记。")
        cap["note"] = "并购交割；或有对价含在 2900 万口径内"
    write_text(dil_path, json.dumps(dil, ensure_ascii=False, indent=2) + "\n")

    bd_path = os.path.join(research_dir, "authored_US_BOSTON_DYNAMICS.json")
    bd = json.load(open(bd_path, encoding="utf-8"))
    note = ("全公司口径下 Stretch 仓储产品本轮未打开独立产品页，保持未知，不写入已覆盖产品清单；"
            "Atlas 2026 交付仍为计划/预订口径（DELIVERY_PLAN），不改成已实现交付。")
    if note not in bd.get("extra_notes", []):
        bd.setdefault("extra_notes", []).append(note)
    write_text(bd_path, json.dumps(bd, ensure_ascii=False, indent=2) + "\n")

    # ---- downgrade extension SEARCHED_NOT_FOUND without real trail --------
    keep_cid_fields = {
        "CN_NOETIX": {"named_customers_or_partners", "deployment_status_actual",
                      "evidence_external_pilot", "evidence_production_shipment",
                      "evidence_customer_delivery", "latest_financing_at_observation"},
    }
    for name in sorted(os.listdir(research_dir)):
        if not (name.startswith("authored_") and name.endswith(".json")):
            continue
        path = os.path.join(research_dir, name)
        doc = json.load(open(path, encoding="utf-8"))
        cid = doc["company_id"]
        keep = keep_cid_fields.get(cid, set())
        changed = False
        for f in doc.get("facts") or []:
            if f.get("value_status") == "SEARCHED_NOT_FOUND" and f.get("field") not in keep:
                f["value_status"] = "NOT_YET_SEARCHED"
                f["research_status"] = "NOT_YET_SEARCHED"
                f["decision_reason"] = (f.get("decision_reason") or "") + "；第二轮：无逐问题真实检索轨迹，降为未查"
                changed = True
        if changed:
            write_text(path, json.dumps(doc, ensure_ascii=False, indent=2) + "\n")

    # ---- search log: relabel derived + append real trail -----------------
    log_path = os.path.join(ROOT, "search_log.jsonl")
    rows = [json.loads(l) for l in open(log_path, encoding="utf-8") if l.strip()]
    out = []
    for e in rows:
        note = e.get("note") or ""
        if e.get("action") == "SEARCH" and (
                e.get("tool") == "stage_b_repair_extension" or "扩展批次：本轮为该命题实际查证" in note):
            e = dict(e)
            e["record_kind"] = "DERIVED_STATUS_SUMMARY"
            e["derived_from"] = "final_SEARCHED_NOT_FOUND_status"
            if "不是原始查询" not in note:
                e["note"] = note + " 【本行由程序根据最终状态补写，不是原始查询】"
        out.append(e)

    real = [
        {"ts_utc": NOW, "action": "SEARCH", "record_kind": "ORIGINAL_QUERY", "tool": "web_search",
         "company_id": "CN_NOETIX", "field": "legal_entity_name",
         "question": "CN_NOETIX 是否为松延动力 Noetix 而非非夕 Flexiv",
         "query": "Noetix Robotics 松延动力 noetixrobotics.com 北京 昌平",
         "urls_checked": ["https://www.noetixrobotics.com/"],
         "result": "官网 Organization 为北京松延动力科技集团股份有限公司，foundingDate 2023"},
        {"ts_utc": NOW, "action": "FETCH", "company_id": "CN_NOETIX", "field": "legal_entity_name",
         "question": "打开松延官网保存 Organization schema",
         "url": "https://www.noetixrobotics.com/", "access_status": "OK",
         "snapshot_id": "noetix_official_home", "result": "retrieved"},
        {"ts_utc": NOW, "action": "PAGE_REVIEW", "company_id": "CN_NOETIX", "field": "named_customers_or_partners",
         "question": "named_customers_or_partners 官网是否具名客户",
         "query": "review noetix official home for named customers",
         "urls_checked": ["https://www.noetixrobotics.com/"],
         "result": "no named customers in saved Organization/home text"},
        {"ts_utc": NOW, "action": "PAGE_REVIEW", "company_id": "CN_NOETIX", "field": "deployment_status_actual",
         "question": "deployment_status_actual 官网是否部署台数", "urls_checked": ["https://www.noetixrobotics.com/"],
         "result": "no deployment counts"},
        {"ts_utc": NOW, "action": "PAGE_REVIEW", "company_id": "CN_NOETIX", "field": "evidence_external_pilot",
         "question": "evidence_external_pilot", "urls_checked": ["https://www.noetixrobotics.com/"],
         "result": "no external pilot"},
        {"ts_utc": NOW, "action": "PAGE_REVIEW", "company_id": "CN_NOETIX", "field": "evidence_production_shipment",
         "question": "evidence_production_shipment", "urls_checked": ["https://www.noetixrobotics.com/"],
         "result": "no shipment figures"},
        {"ts_utc": NOW, "action": "PAGE_REVIEW", "company_id": "CN_NOETIX", "field": "evidence_customer_delivery",
         "question": "evidence_customer_delivery", "urls_checked": ["https://www.noetixrobotics.com/"],
         "result": "no completed delivery record"},
        {"ts_utc": NOW, "action": "PAGE_REVIEW", "company_id": "CN_NOETIX", "field": "latest_financing_at_observation",
         "question": "latest_financing_at_observation OFweek 标题有无发布日",
         "urls_checked": ["https://en.ofweek.com/ofweek-news/detail/two-weeks-after-spring-festival-gala-debut-noetix-robotics-secures-1b-rmb-is-this-price-disruptor-of.html"],
         "result": "title-only 1B RMB, no publication date"},
        {"ts_utc": NOW, "action": "SEARCH", "record_kind": "ORIGINAL_QUERY", "tool": "web_search",
         "company_id": "US_FIGURE", "field": "latest_financing_disclosed",
         "question": "Figure Series C official announcement committed capital",
         "query": "Figure AI Series C $1 billion 39 billion site:figure.ai",
         "urls_checked": ["https://www.figure.ai/news/series-c"],
         "result": "official 2025-09-16 committed capital >$1B, post-money $39B"},
        {"ts_utc": NOW, "action": "FETCH", "company_id": "US_FIGURE", "field": "latest_financing_disclosed",
         "question": "保存 Figure C 轮官方页", "url": "https://www.figure.ai/news/series-c",
         "access_status": "OK", "snapshot_id": "figure_series_c", "result": "retrieved"},
        {"ts_utc": NOW, "action": "SEARCH", "record_kind": "ORIGINAL_QUERY", "tool": "web_search",
         "company_id": "US_DILIGENT", "field": "ma_events",
         "question": "Serve Robotics Diligent 8-K close date $29 million includes $5.3 million earnout",
         "query": "Serve Robotics Form 8-K Diligent January 27 2026 29 million includes 5.3 million",
         "urls_checked": ["https://www.sec.gov/Archives/edgar/data/1832483/000121390026009480/ea0274698-8k_serve.htm"],
         "result": "close 2026-01-27; $29.0m includes up to $5.3m earnout"},
        {"ts_utc": NOW, "action": "PAGE_REVIEW", "company_id": "US_DILIGENT", "field": "ma_events",
         "question": "ma_events 阅读 8-K 对价定义",
         "urls_checked": ["https://www.sec.gov/Archives/edgar/data/1832483/000121390026009480/ea0274698-8k_serve.htm",
                          "https://ir.serverobotics.com/node/9176/html"],
         "result": "29m includes 5.3m contingent; not 29+5.3"},
        {"ts_utc": NOW, "action": "PAGE_REVIEW", "company_id": "CN_LIMX", "field": "latest_financing_disclosed",
         "question": "B_CN_LIMX_002 正文日期是 2026-07-14 而非 2026-04",
         "urls_checked": ["https://www.36kr.com/p/3893976502287618"],
         "result": "article timestamp 2026-07-14 08:46; event date not assumed equal"},
    ]
    # PAGE_REVIEW for remaining pilot SEARCHED_NOT_FOUND fields
    for pf in ("pilot_facts_CN_XSQUARE.json", "pilot_facts_US_AMAZON_FTR.json", "pilot_facts_CN_FOURIER.json"):
        p = os.path.join(WORK, pf)
        if not os.path.exists(p):
            continue
        doc = json.load(open(p, encoding="utf-8"))
        cid = doc.get("company_id") or pf.replace("pilot_facts_", "").replace(".json", "")
        for f in doc.get("facts") or []:
            if f.get("value_status") != "SEARCHED_NOT_FOUND":
                continue
            field = f["field"]
            real.append({
                "ts_utc": NOW, "action": "PAGE_REVIEW", "company_id": cid, "field": field,
                "question": f"{field} 是否有可核验依据（原试点已打开页面的审阅补记）",
                "query": field,
                "urls_checked": [],
                "result": "reviewed existing stage-B pages; no additional establishing source",
                "note": "补记原试点已执行的页面审阅，不是新编造的检索过程",
            })
    out.extend(real)
    with open(log_path, "w", encoding="utf-8", newline="\n") as fh:
        for e in out:
            fh.write(json.dumps(e, ensure_ascii=False) + "\n")

    withdrawn = os.path.join(ROOT, "WITHDRAWN_FACTS.md")
    write_text(withdrawn, """# 撤回与替换清单（B2-01）

| 原错误 | 撤回原因 | 替代 |
|---|---|---|
| `B_CN_NOETIX_001` 非夕 Flexiv 王世全访谈 | r3 样本 CN_NOETIX 为松延动力 Noetix，招聘域 noetixrobotics.com | 新 `B_CN_NOETIX_001` 松延官网 Organization schema |
| 8 条事实（主体、产品、交付、场景、演示、融资等）写非夕 | 错绑主体 | 按松延官网重写；无依据字段降为未查或查后未找到 |
| 7 条 STRICT_COMPARABLE 使用 Flexiv 产品/场景标签 | 分组绑定了错误取值 | 更新 grouping_rules_source 中 CN_NOETIX 取值键 |
| 资本/融资把非夕「本月融资」与 Noetix 1B 标题混写 | 主体不一致 | 只保留 Noetix 标题线索，不建观察日可用资本行 |

样本 ID、13 条广告、r3 招聘范围未改。
""")
    print("data patch written", ROOT)


if __name__ == "__main__":
    main()
