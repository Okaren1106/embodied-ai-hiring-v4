# 复算指南 / Reproduction guide

## 获取完整发布包

```bash
git clone https://github.com/Okaren1106/embodied-ai-hiring-v4.git
cd embodied-ai-hiring-v4
```

建议使用 Python 3.12+。源码包含已完成的判读结果，数值流程从这些结果重新计算；无需重新联网采集，也无需调用模型。公开包保留原文、编码关系与修订记录。

## V4：技术资格配对研究

```bash
python tools/reproduce.py v4
```

该命令在 `_reproduction/` 创建新的物理目录，从公开输入运行 20 个数值步骤，重新生成配对表、资格关系分析、公司比较、模板敏感性与 PyTorch—TensorFlow 扩展，并将 **89 份 CSV/JSON 输出**逐字节与发布版本比较。返回 `PASS` 后，可在新目录的 `REPRODUCTION_RECEIPT.json` 查看逐文件哈希。

此流程只需要 Python 标准库。原始入口 `paper_v4/REPRODUCE.py` 也可使用，会在 `paper_v4` 内重建输出；新的工具入口使用独立目录，便于对照。

## 全样本：职能、活动、工作对象与资格目录

大表和广告全文的七个文件采用 gzip 压缩，每个文件的原始大小与 SHA-256 记录在 `COMPRESSION_MANIFEST.json`。恢复命令是：

```bash
python tools/restore_large_files.py
```

这会恢复原文件字节，并检查大小和哈希。已存在且匹配的文件会跳过；不同内容会报错，避免覆盖。最大的状态表恢复后约 1.49 GB。恢复文件和完整独立复算建议预留 **至少 8 GB** 可用磁盘空间；具体时间取决于磁盘与处理器。

```bash
python tools/reproduce.py broad
```

该命令先恢复压缩文件，再复制输入、规则、证据与研究事务到新的目录，依次运行：

1. `materialize_astra_final.py`：重新构造广告、证据、修订事务和 4,402,134 个语境状态格。
2. `compute_astra_final.py`：重新计算 17 职能目录、公司点值、各范围和敏感性结果。
3. `compute_v3_two_layers.py`：重新计算三个任务层的技术提及与表达方式。

最后比较 **21 份输出**的 SHA-256。原研究 `scripts/reproduce_astra_isolated.py` 还核对相邻历史工作目录，公开包使用新的便携入口完成相同核心数值重建，省去对原计算机目录的依赖。

## 可选的独立核验与文档构建

核心复算不需要第三方库。全样本独立矩阵核验使用 NumPy；图与 Word 重建分别使用 Matplotlib 和 python-docx。原交付环境使用 NumPy 2.3.5、Matplotlib 3.11.2、python-docx 1.2.0，详细环境记录见 `broad_study/verification/environment_v3.json`。

```bash
python -m pip install numpy matplotlib python-docx
```

在完整恢复数据后，下列脚本提供不同实现的核验：

```bash
python broad_study/scripts/verify_v3_states.py
python broad_study/scripts/verify_astra_numeric.py
python broad_study/scripts/verify_v3_two_layers.py
```

V4 的独立核验已包含在 20 步入口中。图片与 Word 生成是可选工作流，公开的 PDF、Word 和图表可直接阅读。历史脚本包含原机器路径、文档导出环境以及研究修订登记逻辑；**register 开头的脚本用于保留历史判读事务，复算时不要重复登记**。便携入口只执行数值重建。

## 校验公开文件

```bash
python tools/verify_publication.py
```

`PUBLICATION_MANIFEST.json`记录发布文件的大小与哈希；`SOURCE_PROVENANCE.json`记录来源版本和原文件哈希；`COMPRESSION_MANIFEST.json`用于校验恢复后的七个文件。根清单不包含自身和 Git 元数据。旧版本内的清单记录的是各自原始交付状态，保留用于历史追溯。

English: run `python tools/reproduce.py v4` for the standard-library V4 workflow, or `python tools/reproduce.py broad` for the complete broad study. Both create fresh directories, reconstruct the numerical outputs from the published evidence, and compare their SHA-256 hashes with the release. Large broad-study files are restored losslessly before use. Optional numerical, figure and Word rebuilds use the libraries listed above.
