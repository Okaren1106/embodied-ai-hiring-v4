# 真实检索轨迹说明（B2-02）

本文件说明检索日志里哪些行能证明「实际查过」，哪些只是状态派生。验收应按问题审查，不能只看公司有没有任意 SEARCH。

## 分类

| 种类 | 条数 | 可否当作查证证据 |
|---|---|---|
| 真实 SEARCH（`ORIGINAL_QUERY` 或试点原始查询，非派生） | 27 | 可以 |
| FETCH | 114 | 证明打开过页面，不能单独把该公司全部字段记成查后未找到 |
| PAGE_REVIEW | 22 | 可以挂到对应字段的查后未找到 |
| ACCESS_FAILURE | 9 | 访问失败记录 |
| 派生 SEARCH（`DERIVED_STATUS_SUMMARY`） | 192 | **不可以**；由上一轮程序按最终状态补写 |

`s11b_search_log_ext.py` 本轮不再补写 SEARCH，只给历史派生行打标。`n_searches_added=0`。

## 本轮新增的真实查询

| 时间 (UTC) | 公司 | 查询词 | 结果要点 |
|---|---|---|---|
| 2026-09-15T02:30:00Z | CN_NOETIX | `Noetix Robotics 松延动力 noetixrobotics.com 北京 昌平` | 官网 Organization：北京松延动力科技集团股份有限公司，foundingDate 2023 |
| 2026-09-15T02:30:00Z | US_FIGURE | `Figure AI Series C $1 billion 39 billion site:figure.ai` | 官方 2025-09-16：承诺资本 >$1B，投后 $39B |
| 2026-09-15T02:30:00Z | US_DILIGENT | `Serve Robotics Form 8-K Diligent January 27 2026 29 million includes 5.3 million` | 交割 2026-01-27；2900 万包括最高 530 万或有 |

## 扩展包降级

没有对应真实 SEARCH / PAGE_REVIEW 的扩展「查后未找到」已降为 `NOT_YET_SEARCHED`，`checked_in_stage_b=NO`。这不是把未知写成错误，也不是把资料不存在写成事实否定。

逐问题缺口见 `work/search_log_summary.json`：`missing_per_question_trail` 为空，`blocked_without_fetch_failure` 为空。
