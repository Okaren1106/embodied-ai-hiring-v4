"""Replace both workspace entry briefs after final package acceptance."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
def main():
    acceptance=json.loads((ROOT/'verification/final_package_verification.json').read_text(encoding='utf-8'))
    assert acceptance['pass'] and acceptance['numeric_outputs_compared']==89
    repo=ROOT.parent;workspace=repo.parent
    paths=[workspace/'必读.md',repo/'必读.md']
    history=repo/'reports/2026-09-26_workspace_progress_before_v4_close.md'
    if not history.exists():history.write_bytes(paths[0].read_bytes())
    base=ROOT.as_posix()
    content=f'''# 当前进度：IJM方向研究升级v4已交付

更新：2026-09-26。本轮持续研究升级及论文重写已完成：五个实质研究阶段加最终综合验收。协调代理负责研究与验证，论文按用户要求由GPT-5.6 Sol重写。当前可用证据内未发现值得继续堆叠的高价值分析；下一次跃迁需要独立人工或招聘行为证据，因此按用户的停止条件结束本轮。没有实际投稿。

## 当前阅读与交付入口

- [英文完整阅读版Word，14页](<{base}/release/IJM_Research_Reading_Copy.docx>)。
- [主文Word，13页](<{base}/release/IJM_Main_Working_Text.docx>)；[主表，3页](<{base}/release/IJM_Research_Tables.docx>)；[补充材料，7页](<{base}/release/IJM_Research_Supplement.docx>)。
- [研究升级与投稿准备说明](<{base}/release/研究升级与投稿准备说明.md>)；[完整私有研究包ZIP](<{base}/Embodied_AI_IJM_Research_v4.0.zip>)；[复算说明](<{base}/README.md>)。
- 阶段记录：`analysis_E_english_v4_0/stages/00`至`06`；最终整体回顾：`audit/final_whole_paper_review.md`；验收：`verification/final_package_verification.json`。

## 当前研究结论

研究主线已从少数公司排名转为：同一广告中，技术排序如何依赖资格关系的定义。M为提及，H为GENERAL/REQUIRED资格语境，Q为无限定技术特指。H不含独立PREFERRED指标；Q不等于真实需求或全部候选资格。

原主样本仍为248广告、496广告—技术对。七项有来源的派生层修正后，Q为169 P、284 Z、43 U。原v3的170/280/46与五修正阶段170/285/41仅作历史，不可当作当前值。原始记录、冻结参考和正式研究库没有回写。

105条机器人模型广告中，Python减PyTorch的窄Q确认差为+19.0pp，未知赋值范围+13.3至+35.2；计入例示可纳入关系后确认差为−21.0pp，范围−24.8至−4.8。明确例示提示单独纳入时范围跨零，开放“等”列表有实质作用；66条共同提及的完整扩展也跨零。新增PyTorch—TensorFlow对照的26条共同提及均为同谓词、同记录状态，未复现主案例差异。严格零差须另加共享读法假设。

模型辅助源文解释、确定性计算和独立算术核验分别记账，没有虚构独立人工双编码、样本外验证或招聘行为。公司排序已降为次要脆弱度诊断。结论限于目的性捕获语料，不是行业总体、因果效应或真实筛选要求。

## 完成验收

20步离线复算通过；89份CSV/JSON隔离复算与ZIP解压复算均逐字节一致。10张表的374个正文单元格、70个表头及366个数字分量核对通过；141项Word内容检查通过；四文件37页全部看图验收。主文加5个图表各280词约6,926词，摘要含关键词与分类215词。767个旧v3文件保护哈希不变。

用户明确后续AI投稿政策由其自行处理。本轮不再以此停工或重复询问；工作稿据实保留模型使用来源，未伪造人工作者、编辑许可或完成投稿。下一步作者事项和真实外部验证不冒充已完成。

## 原项目其他有效状态

- 原研究语料为24主体1,654条版本化广告。认可参考归档：`outputs/reference-expansion-2026-09-11/accepted-reference1654-v1-2026-09-14/`；当前可编辑研究库：`data/research/research.sqlite3`。
- 规则为measurement-v0.7.5（17具体职能、2结构类）。原工作台v0.7.10分类器未完成质量验收、仍绑定旧规则，不能因本次论文验收通过而宣布分类器通过。
- 周采仍按用户要求关闭，没有恢复后台任务或自动采集。
- 2026-09-25公开的独立代码仓库为[embodied-ai-hiring-pipeline](https://github.com/Okaren1106/embodied-ai-hiring-pipeline)，本地副本`public/embodied-ai-hiring-pipeline`，既有提交`3a60240771b37f2ec803434409dd1b925144d0bf`。本轮未改动或推送该公开副本。真实语料、论文及研究原仓库保持私有。
- v3历史论文仍完整保存于`analysis_E_english_v3_0/`；本轮当前入口为v4。旧轮“不可扩公司/不可重开主分类”等只描述当时授权，已被本次可突破原规模的新授权取代。

此前完整项目过程与历史验证记录已保存至[交付前进度归档](<{history.as_posix()}>). 本正文只反映当前状态；后续更改时请同步改写工作区与仓库两份`必读.md`。
'''
    for p in paths:p.write_text(content,encoding='utf-8',newline='\n')
    assert paths[0].read_bytes()==paths[1].read_bytes()
    print('Final v4 status synchronized in both entry briefs; earlier progress archived.')
if __name__=='__main__':main()
