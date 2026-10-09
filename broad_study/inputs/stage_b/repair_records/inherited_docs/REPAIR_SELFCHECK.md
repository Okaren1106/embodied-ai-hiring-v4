# 第二轮返修自检说明（与独立验收分开）

本包是**执行方返修自检**，不是独立验收，也不声称用户已逐条复核。独立验收需由未参与本次返修的一方按同样口径复验。状态只写「返修完成，待独立验收」。

## 本次自检做了什么

| 项目 | 结果 |
|---|---|
| 验收自检 | 45/45 通过，失败 0（`verification.json`） |
| 受控故障实验 | 正对照接受并可发布；20/20 探针按预期（`work/fault_probes.json`） |
| 离线复算 | 五张核心表与发布版本逐字节一致（`work/rebuild_check.json`） |
| 页面脚本 Node 执行 | 23/23（`work/html_runtime_checks.json`） |
| 检索日志 | 真实 SEARCH 27、派生 192、FETCH 114、PAGE_REVIEW 22；缺逐问题轨迹 0 |
| 身份映射 | `I1`：CN_NOETIX 为松延/Noetix，authored 正文不含 Flexiv/非夕 |

## 本次自检没有做什么

1. Node 脚本检查覆盖：页面可解析、24 家齐全、缺口 307 在页内、未查字段可见、详情含快照路径与来源链接。**不覆盖**真实点击、搜索框输入、切公司后的人工阅读。
2. 本轮已用 Cursor 内置浏览器打开 `http://127.0.0.1:8765/index.html`（本地静态服务，因 `file://` 被工具禁止）。实测：首屏渲染 24 家与 45/45 标记；搜索 `CN_NOETIX` 后侧栏只剩一家；切换后主体为松延动力、广告数 13、页面无 Flexiv/非夕；搜索 `B_CN_NOETIX_001` 可见证据卡（官网 Organization 摘录与快照哈希）及 15 项继承缺口。事实表中的证据 ID 为同页展示，不是可点击跳转链接。未做全页面交互审计。
3. 没有把自检通过写成独立验收通过，也没有写 `STAGE_B_COMPLETE` 或进入阶段 C。
4. 没有重分类招聘广告、没有改 1654 分母、没有改写送审包 / r3 / 研究库 / 规则 / 冻结参考。

## 状态标记

- 范围：`REPAIR_R2_PENDING_ACCEPTANCE`（24 家修订完成，待独立验收）。
- 发布门禁：见 `release_gate_status.json`；失败时该文件为失败报告，且不保留成功文档。
- 阶段 A 交付、研究库、规则与冻结参考未改写。

## 复验入口

```text
python scripts/s01_lock_inputs.py       # 核验全部输入与快照哈希（不要默认 --rebuild）
python scripts/s04_verify.py            # 验收自检
python scripts/s06_rebuild_and_fault.py # 离线复算 + 正对照 + 单点故障注入
node scripts/s08_html_runtime_check.js .  # 页面脚本执行
python scripts/s11_release_gate.py      # 发布门禁（通过后再写清单）
```

解释器：`C:/Users/bestl/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`
