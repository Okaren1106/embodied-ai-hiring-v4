# 阶段D独立研究接续包｜Astra v1

日期：2026-09-16。初步独立研究交付；另一位研究者验收与阶段E尚未进行。本包不覆盖其他研究者结果，也不改原认可分类、研究库及A/B/C。

## 阅读

- [独立研究报告](REPORT.md)：主结果、两组案例、反例、限制及8个来源链接。
- [Word阅读版](document/具身智能公开招聘研究_阶段D独立研究报告_Astra_v1.docx)。
- [T5交付责任](tables/T5_responsibility_long.csv)、[T5工作对象原文](tables/T5_case_work_object_evidence.csv)、[T6结论台账](tables/T6_conclusions_sensitivity.csv)。
- [方法](METHODS.md)、[全部数据表](DATA_DICTIONARY.md)、[验证记录](verification/REPORT.md)。

## 完整复算

Python 3.12，分析使用标准库；图形使用matplotlib、numpy与微软雅黑。作者使用Codex bundled Python和项目已有绘图库；不要求现场数据库、浏览器或网络。包内复制979个输入文件；外部证据返回及阅读判断另有evidence_lock.json。字体为Windows的C:\Windows\Fonts\msyh.ttc；其他平台需安装/显式配置同一字体才能要求图像字节一致。

在PowerShell设置运行路径后执行（输出必须是尚不存在的新目录）：

```powershell
$astraPython = 'C:\Users\bestl\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$astraPlots = 'D:\Embod AI analysis\embodied-ai-hiring-research\.b5accept\stage_c_plot_deps'
& $astraPython -X utf8 .\scripts\reproduce.py --output '..\astra_new_copy' --plot-deps $astraPlots
```

进入新目录后，可用同样入口再生成第三个目录。入口先校验自身发布清单、输入和证据锁，在临时目录重新计算所有派生表、图和Markdown，运行第二实现核对，逐字节比较后才发布。已存在目录、清单漂移、输入漂移、证据漂移或结果不一致都会拒绝；失败不留下目标目录。新包带自己的scripts、inputs、锁、README和release_checksums.json。

Word及其排版验收是封存阅读导出，复算时复制字节；不宣称重新排版DOCX。主数据、图及Markdown重新生成。verification中历史作者检查随包携带，新一轮复算另记reproduction.json，不冒充新一轮人工视觉审阅。

## 来源与研究独立性

输入C：stage_c/run_20260915T105656Z；B：stage_b_supplemented/run_20260915T073556Z；规则：analysis_rules_v1/run_20260915T085828Z；原始认可广告快照来自stage_a_r3，SHA以input_lock为准。ANALYSIS_DECISIONS.md保留预先选择及后续探索性调整。责任断言与案例选择保存在evidence，不在复算中重新调用模型判断。

C的REPRO-01包装修复另存于本包父目录的repro_c_second和repro_c_third；两轮各60个结果文件与封存C一致。工程代码来自项目已有修复，Astra修正README重复追加；研究内容未引用其他研究者阶段D结论。
